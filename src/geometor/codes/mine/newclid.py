"""Newclid miner: AST extraction of ``all_rules.py`` without importing Newclid."""

from __future__ import annotations

import ast
from pathlib import Path

from geometor.codes.mine.schema import Decl, MinedSystem, git_head


def _str_tuple(node: ast.AST | None) -> list[str]:
    if node is None:
        return []
    if isinstance(node, (ast.Tuple, ast.List)):
        out: list[str] = []
        for elt in node.elts:
            if isinstance(elt, ast.Constant) and isinstance(elt.value, str):
                out.append(elt.value)
        return out
    return []


def _const_val(node: ast.AST | None) -> object:
    if isinstance(node, ast.Constant):
        return node.value
    return None


def _collect_set_names(node: ast.AST | None) -> set[str]:
    if isinstance(node, (ast.Set, ast.List, ast.Tuple)):
        return {elt.id for elt in node.elts if isinstance(elt, ast.Name)}
    return set()


def parse_newclid_rules(path: Path, workspace_root: Path) -> list[Decl]:
    """Parse ``all_rules.py`` via AST into rule declarations.

    Args:
        path: Path to ``all_rules.py``.
        workspace_root: Workspace root for relative source paths.

    Returns:
        List of `Decl` objects.
    """
    src = str(path.relative_to(workspace_root))
    tree = ast.parse(path.read_text(encoding="utf-8"))

    # First collect rule-list membership sets (e.g. DEACTIVATED_RULES).
    list_sets: dict[str, set[str]] = {}
    for stmt in tree.body:
        target_name = ""
        value: ast.AST | None = None
        if isinstance(stmt, ast.Assign) and len(stmt.targets) == 1 and isinstance(stmt.targets[0], ast.Name):
            target_name = stmt.targets[0].id
            value = stmt.value
        elif isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
            target_name = stmt.target.id
            value = stmt.value
        if target_name in (
            "DEACTIVATED_RULES",
            "TRIAGE_NO_RULE_NEEDED",
            "TRIAGE_LEAVE_RULE_OUT",
        ):
            list_sets[target_name] = _collect_set_names(value)

    decls: list[Decl] = []
    for stmt in tree.body:
        if not isinstance(stmt, ast.Assign) or len(stmt.targets) != 1:
            continue
        target = stmt.targets[0]
        if not isinstance(target, ast.Name) or not isinstance(stmt.value, ast.Call):
            continue
        call = stmt.value
        if not (isinstance(call.func, ast.Name) and call.func.id == "Rule"):
            continue

        kw = {k.arg: k.value for k in call.keywords if k.arg is not None}
        rule_id = str(_const_val(kw.get("id")) or target.id)
        desc = str(_const_val(kw.get("description")) or "")
        premises = _str_tuple(kw.get("premises_txt"))
        conclusions = _str_tuple(kw.get("conclusions_txt"))
        allow_rep = bool(_const_val(kw.get("allow_point_repetition")) or False)

        flags = [
            group
            for group, members in sorted(list_sets.items())
            if target.id in members
        ]
        is_default = not flags
        ag_origin = rule_id if (rule_id.startswith("r") and rule_id[1:].isdigit() and int(rule_id[1:]) <= 42) else ""

        statement = f"{', '.join(premises)} => {', '.join(conclusions)}"
        decls.append(
            Decl(
                system="newclid",
                id=target.id,
                name=rule_id,
                kind="rule",
                module="newclid.all_rules",
                family="AG Core (r00-r42)" if ag_origin else "Newclid Extensions",
                statement=statement,
                text=desc,
                premises=premises,
                conclusions=conclusions,
                source=src,
                line=stmt.lineno,
                extra={
                    "rule_id": rule_id,
                    "constant": target.id,
                    "allow_point_repetition": allow_rep,
                    "default": is_default,
                    "flags": flags,
                    "ag_rule": ag_origin,
                },
            )
        )
    return decls


def mine_newclid(root: Path, workspace_root: Path) -> MinedSystem:
    """Mine Newclid's ``all_rules.py``.

    Args:
        root: Newclid checkout root (``_refs/Newclid``).
        workspace_root: Workspace root.

    Returns:
        A `MinedSystem`.
    """
    rules_file = root / "newclid" / "src" / "newclid" / "all_rules.py"
    decls = parse_newclid_rules(rules_file, workspace_root) if rules_file.exists() else []
    return MinedSystem(
        system="newclid",
        decls=decls,
        source=str(root.relative_to(workspace_root)),
        commit=git_head(root),
    )
