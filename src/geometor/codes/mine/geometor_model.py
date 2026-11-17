"""geometor.model miner: proof predicates, invariants, constructions, and spg foundation map."""

from __future__ import annotations

import ast
from collections import defaultdict
from pathlib import Path

from geometor.codes.mine.schema import Decl, MinedSystem, git_head

_TARGET_FILES = (
    "proof.py",
    "invariants.py",
    "intersections.py",
    "lines.py",
    "circles.py",
    "points.py",
    "segments.py",
    "polygons.py",
    "wedges.py",
    "sections.py",
)

_SKIP_FUNCTIONS = frozenset({
    "add_poly",
    "all_coeffs",
    "approx_coords",
    "clear_new_points",
    "degree",
    "delete_element",
    "eval",
    "extract_points",
    "extract_segments",
    "fibonacci_",
    "floats",
    "flow",
    "from_dict",
    "get_",
    "get_ancestors",
    "get_ancestors_",
    "get_dependents",
    "include",
    "is_logging_enabled",
    "keep",
    "limits",
    "log",
    "max_float",
    "max_length",
    "max_segment",
    "min_float",
    "min_length",
    "min_segment",
    "name",
    "new_points",
    "numerical_lengths",
    "parse_command",
    "point_",
    "poly",
    "promote_point_to_top",
    "real_roots",
    "remove_by_",
    "report_group_by_type",
    "report_sequence",
    "report_summary",
    "save",
    "scope_id",
    "set_analysis_hook",
    "set_angle_by_",
    "set_polygon_by_",
    "set_section_by_",
    "set_segment_by_",
    "set_simplifier",
    "set_wedge_by_",
    "to_dict",
})


def _first_doc_line(node: ast.FunctionDef | ast.AsyncFunctionDef | ast.ClassDef) -> str:
    doc = ast.get_docstring(node) or ""
    for ln in doc.splitlines():
        s = ln.strip()
        if s:
            return s
    return ""


def _classify_model_fn(module_stem: str, name: str) -> str:
    if module_stem == "proof" and (name.startswith("assert_") or name == "conclude"):
        return "predicate"
    if name in ("is_harmonic", "is_right", "is_golden"):
        return "predicate"
    if name in (
        "quadrance",
        "line_spread",
        "cross",
        "vertex_spread",
        "vertex_dot_sign",
        "signed_area2",
        "orientation",
        "polygon_area2",
        "cross_ratio",
        "spread",
        "area",
        "perimeter",
        "length",
        "ratio",
        "radians",
        "degrees",
        "arc_length",
    ):
        return "measure"
    if name in (
        "construct_line",
        "construct_circle",
        "given_point",
        "set_point",
        "set_segment",
        "set_polygon",
        "set_angle",
        "set_wedge",
        "set_section",
        "intersect",
        "intersect_all",
        "intersect_2d",
        "subconstruction",
        "proposition",
    ):
        return "construction"
    return "method"


def _collect_spg_usage(py_files: list[Path], workspace_root: Path) -> dict[str, list[str]]:
    """Map ``spg.<Name>`` references to ``file:line`` occurrences."""
    usage: dict[str, list[str]] = defaultdict(list)
    for path in py_files:
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except (SyntaxError, UnicodeDecodeError):
            continue
        rel = str(path.relative_to(workspace_root))
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Attribute)
                and isinstance(node.value, ast.Name)
                and node.value.id == "spg"
            ):
                usage[node.attr].append(f"{rel}:{node.lineno}")
    return dict(usage)


def mine_geometor_model(root: Path, workspace_root: Path) -> MinedSystem:
    """Mine ``geometor.model`` public geometric API and its ``spg`` foundation map.

    Args:
        root: Path to ``model/src/geometor/model``.
        workspace_root: Workspace root.

    Returns:
        A `MinedSystem`.
    """
    all_py = sorted(root.glob("*.py"))
    spg_usage = _collect_spg_usage(all_py, workspace_root)

    decls: list[Decl] = []
    seen_ids: set[str] = set()
    for fname in _TARGET_FILES:
        path = root / fname
        if not path.exists():
            continue
        stem = path.stem
        src = str(path.relative_to(workspace_root))
        tree = ast.parse(path.read_text(encoding="utf-8"))

        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if node.name.startswith("_") or node.name in _SKIP_FUNCTIONS:
                    continue
                decl_id = f"{stem}.{node.name}"
                if decl_id in seen_ids:
                    continue
                seen_ids.add(decl_id)
                args = [a.arg for a in node.args.args if a.arg != "self"]
                decls.append(
                    Decl(
                        system="geometor_model",
                        id=decl_id,
                        name=node.name,
                        kind=_classify_model_fn(stem, node.name),
                        module=f"geometor.model.{stem}",
                        family=stem,
                        statement=f"{node.name}({', '.join(args)})",
                        text=_first_doc_line(node),
                        source=src,
                        line=node.lineno,
                    )
                )
            elif isinstance(node, ast.ClassDef):
                for item in node.body:
                    if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        continue
                    if item.name.startswith("_") or item.name in _SKIP_FUNCTIONS:
                        continue
                    # Skip boilerplate construct_line_by_ / set_segment_by_ etc.
                    if item.name.endswith("_by_"):
                        continue
                    decl_id = f"{node.name}.{item.name}"
                    if decl_id in seen_ids:
                        continue
                    seen_ids.add(decl_id)
                    args = [a.arg for a in item.args.args if a.arg != "self"]
                    decls.append(
                        Decl(
                            system="geometor_model",
                            id=decl_id,
                            name=item.name,
                            kind=_classify_model_fn(stem, item.name),
                            module=f"geometor.model.{stem}.{node.name}",
                            family=stem,
                            statement=f"{node.name}.{item.name}({', '.join(args)})",
                            text=_first_doc_line(item),
                            source=src,
                            line=item.lineno,
                        )
                    )

    for spg_name, locs in sorted(spg_usage.items()):
        decls.append(
            Decl(
                system="geometor_model",
                id=f"foundation.spg.{spg_name}",
                name=f"spg.{spg_name}",
                kind="foundation",
                module="geometor.model.spg_foundation",
                family="SymPy Foundation",
                statement=f"sympy.geometry.{spg_name}",
                text=f"Used {len(locs)} time(s) in geometor.model",
                uses=[f"sympy:{spg_name}"],
                source=locs[0].rsplit(":", 1)[0],
                line=int(locs[0].rsplit(":", 1)[1]),
                extra={"occurrences": len(locs), "locations": locs[:10]},
            )
        )

    repo_root = root.parents[2]
    return MinedSystem(
        system="geometor_model",
        decls=decls,
        source=str(root.relative_to(workspace_root)),
        commit=git_head(repo_root),
    )
