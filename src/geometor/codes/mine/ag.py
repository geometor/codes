"""AlphaGeometry miner: deduction rules (``rules.txt``) and constructions (``defs.txt``)."""

from __future__ import annotations

from pathlib import Path

from geometor.codes.mine.schema import Decl, MinedSystem, git_head


def _split_atoms(text: str) -> list[str]:
    """Split comma- or semicolon-separated predicate atoms."""
    atoms: list[str] = []
    for part in text.replace(";", ",").split(","):
        cleaned = " ".join(part.split())
        if cleaned:
            atoms.append(cleaned)
    return atoms


def parse_rules(path: Path, workspace_root: Path) -> list[Decl]:
    """Parse ``rules.txt`` into rule declarations.

    Args:
        path: Path to ``rules.txt``.
        workspace_root: Workspace root for relative source paths.

    Returns:
        List of rule `Decl` objects.
    """
    src = str(path.relative_to(workspace_root))
    decls: list[Decl] = []
    rule_idx = 0
    for lineno, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith("#") or "=>" not in line:
            continue
        lhs, rhs = line.split("=>", 1)
        premises = _split_atoms(lhs)
        conclusions = _split_atoms(rhs)
        decls.append(
            Decl(
                system="alphageometry",
                id=f"rule.r{rule_idx:02d}",
                name=f"r{rule_idx:02d}",
                kind="rule",
                module="rules.txt",
                family="Deduction Rules",
                statement=line,
                premises=premises,
                conclusions=conclusions,
                source=src,
                line=lineno,
            )
        )
        rule_idx += 1
    return decls


def parse_defs(path: Path, workspace_root: Path) -> list[Decl]:
    """Parse ``defs.txt`` into construction declarations.

    Args:
        path: Path to ``defs.txt``.
        workspace_root: Workspace root for relative source paths.

    Returns:
        List of construction `Decl` objects.
    """
    src = str(path.relative_to(workspace_root))
    lines = path.read_text(encoding="utf-8").splitlines()
    blocks: list[tuple[int, list[str]]] = []
    cur: list[str] = []
    cur_start = 1
    for lineno, raw in enumerate(lines, start=1):
        if raw.strip():
            if not cur:
                cur_start = lineno
            cur.append(raw.rstrip())
        elif cur:
            blocks.append((cur_start, cur))
            cur = []
    if cur:
        blocks.append((cur_start, cur))

    decls: list[Decl] = []
    seen_ids: dict[str, int] = {}
    for start_line, block in blocks:
        header = block[0].split()
        name = header[0]
        args = header[1:]
        count = seen_ids.get(name, 0) + 1
        seen_ids[name] = count
        decl_id = f"def.{name}" if count == 1 else f"def.{name}_{count}"

        preconditions: list[str] = []
        predicates: list[str] = []
        deps = ""
        sketch: list[str] = []
        for ln in block[1:]:
            stripped = ln.strip()
            if "=" in stripped and ":" not in stripped:
                _, rhs = stripped.split("=", 1)
                preconditions.extend(_split_atoms(rhs))
            elif ":" in stripped:
                lhs, rhs = stripped.split(":", 1)
                if not deps and rhs.strip() and all(
                    tok.isalpha() and len(tok) <= 2 for tok in rhs.split()
                ):
                    deps = f"{lhs.strip()} : {rhs.strip()}"
                else:
                    predicates.extend(_split_atoms(rhs))
            else:
                sketch.append(stripped)

        decls.append(
            Decl(
                system="alphageometry",
                id=decl_id,
                name=name,
                kind="construction",
                module="defs.txt",
                family="Constructions",
                statement=block[0],
                premises=preconditions,
                conclusions=predicates,
                source=src,
                line=start_line,
                extra={
                    "args": args,
                    "deps": deps,
                    "sketch": sketch,
                },
            )
        )
    return decls


def mine_alphageometry(root: Path, workspace_root: Path) -> MinedSystem:
    """Mine AlphaGeometry's ``rules.txt`` and ``defs.txt``.

    Args:
        root: AlphaGeometry checkout root (``_refs/alphageometry``).
        workspace_root: Workspace root.

    Returns:
        A `MinedSystem`.
    """
    decls: list[Decl] = []
    rules_path = root / "rules.txt"
    if rules_path.exists():
        decls.extend(parse_rules(rules_path, workspace_root))
    defs_path = root / "defs.txt"
    if defs_path.exists():
        decls.extend(parse_defs(defs_path, workspace_root))
    return MinedSystem(
        system="alphageometry",
        decls=decls,
        source=str(root.relative_to(workspace_root)),
        commit=git_head(root),
    )
