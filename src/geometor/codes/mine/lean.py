"""LeanEuclid miner: System E sorts, relations and axioms; Book I; UniGeo.

Parsing is purely textual (no Lean toolchain). It recovers each top-level
declaration with its namespace-qualified name, signature, docstring or
preceding comment, and, for theorems, the ``euclid_apply`` proof trace.
"""

from __future__ import annotations

import re
from pathlib import Path

from geometor.codes.mine.schema import Decl, MinedSystem, git_head

_DECL = re.compile(
    r"^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*"
    r"(axiom|theorem|lemma|def|abbrev|opaque|inductive|structure)\s+([^\s:(\[{]+)"
)
_STOP = re.compile(
    r"^(namespace|end\b|section|open\b|notation|instance|macro|syntax|import|variable|"
    r"set_option|#|@\[|/-|noncomputable instance)"
)
_APPLY = re.compile(r"euclid_apply\s+\(?\s*([A-Za-z_][\w.']*)")
_ASSERT = re.compile(r"euclid_assert\s+(.+)")

# Directories (relative to the LeanEuclid root) that are mined.
SCOPES = ("SystemE/Theory", "Book", "UniGeo")


def _strip_block_comments(lines: list[str]) -> list[str]:
    """Blank out non-doc ``/- ... -/`` block comments, keeping line numbers."""
    out: list[str] = []
    depth = 0
    doc = False
    for line in lines:
        s = line.strip()
        if depth == 0 and s.startswith("/--"):
            doc = "-/" not in s[3:]
            out.append(line)
            continue
        if doc:
            out.append(line)
            if "-/" in s:
                doc = False
            continue
        if depth == 0 and s.startswith("/-"):
            depth = 0 if "-/" in s[2:] else 1
            out.append("")
            continue
        if depth:
            depth += s.count("/-") - s.count("-/")
            depth = max(depth, 0)
            out.append("")
            continue
        out.append(line)
    return out


def _doc_above(lines: list[str], start: int) -> str:
    """Return the docstring or ``--`` comment block directly above ``start``."""
    i = start - 1
    while i >= 0 and (not lines[i].strip() or lines[i].lstrip().startswith("@[")):
        i -= 1
    if i < 0:
        return ""
    if lines[i].strip().endswith("-/"):
        j = i
        while j >= 0 and not lines[j].lstrip().startswith("/--"):
            j -= 1
        if j < 0:
            return ""
        block = " ".join(ln.strip() for ln in lines[j : i + 1])
        return block.removeprefix("/--").removesuffix("-/").strip()
    comments: list[str] = []
    while i >= 0 and (lines[i].lstrip().startswith("--") or not lines[i].strip()):
        text = lines[i].strip().lstrip("-").strip().strip("*").strip()
        if text and not set(text) <= {"*", "-"}:
            comments.append(text)
        i -= 1
    comments.reverse()
    return " ".join(c for c in comments if not re.fullmatch(r"\d+\.?", c))


def _split_statement(body: str) -> tuple[str, str]:
    """Split a declaration body into ``(signature, proof_or_definition)``."""
    m = re.search(r":=|^\s*by\b", body, re.MULTILINE)
    if not m:
        return body, ""
    return body[: m.start()], body[m.start() :].removeprefix(":=").strip()


def _collapse(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def _family(rel: Path) -> tuple[str, dict[str, object]]:
    parts = rel.with_suffix("").parts
    if parts[0] == "Book":
        num = int(re.sub(r"\D", "", parts[-1]) or 0)
        return "Book I", {"euclid": f"I.{num}"} if num else {}
    if parts[0] == "UniGeo":
        if len(parts) >= 3:
            num = int(re.sub(r"\D", "", parts[-1]) or 0)
            return f"UniGeo {parts[1]}", {"category": parts[1], "number": num}
        return f"UniGeo {parts[-1]}", {}
    return parts[-1], {}


def parse_lean_file(path: Path, root: Path, workspace_root: Path) -> list[Decl]:
    """Parse one Lean file into declarations.

    Args:
        path: The ``.lean`` file.
        root: LeanEuclid checkout root.
        workspace_root: Workspace root, for relative source paths.

    Returns:
        Declarations in file order.
    """
    raw = path.read_text(encoding="utf-8").splitlines()
    lines = _strip_block_comments(raw)
    rel = path.relative_to(root)
    family, fam_extra = _family(rel)
    src = str(path.relative_to(workspace_root))

    starts: list[tuple[int, str, str]] = []
    ns_at: list[list[str]] = []
    ns: list[str] = []
    for i, line in enumerate(lines):
        if m := re.match(r"^namespace\s+(\S+)", line):
            ns.extend(m[1].split("."))
        elif m := re.match(r"^end\s+(\S+)", line):
            for _ in m[1].split("."):
                if ns:
                    ns.pop()
        elif m := _DECL.match(line):
            starts.append((i, m[1], m[2]))
            ns_at.append(list(ns))

    decls: list[Decl] = []
    for (start, keyword, name), namespace in zip(starts, ns_at):
        body_lines = [lines[start]]
        for j in range(start + 1, len(lines)):
            ln = lines[j]
            if not ln.strip() or ln.lstrip().startswith("--"):
                body_lines.append("")
                continue
            if ln[0].isspace() or re.match(r"^(by\b|\||:=|\))", ln):
                body_lines.append(ln)
                continue
            if _DECL.match(ln) or _STOP.match(ln) or not ln[0].isspace():
                break
        body = "\n".join(body_lines).rstrip()
        header = _DECL.match(lines[start])
        after = body[header.end() :] if header else body
        sig, rest = _split_statement(after)
        sig = _collapse(sig).removeprefix(":").strip() if sig.strip().startswith(":") else _collapse(sig)
        full_id = ".".join([*namespace, name]) if namespace else name

        if keyword == "axiom":
            kind = "sort" if re.fullmatch(r":?\s*Type", sig.strip()) else "axiom"
        elif keyword in ("theorem", "lemma"):
            kind = "theorem"
        elif keyword in ("def", "abbrev"):
            kind = "definition"
        elif keyword == "opaque":
            kind = "relation" if "Prop" in sig else "measure"
        else:
            kind = "sort"

        extra: dict[str, object] = dict(fam_extra)
        uses: list[str] = []
        if kind == "theorem" and rest:
            trace = [ln.strip() for ln in rest.splitlines() if ln.strip() and ln.strip() != "by"]
            for t in trace:
                if m := _APPLY.search(t):
                    target = m[1]
                    if target not in uses:
                        uses.append(target)
            extra["trace"] = trace
            extra["proof_steps"] = len(trace)
            asserts = [m[1].strip() for t in trace if (m := _ASSERT.search(t))]
            if asserts:
                extra["asserts"] = asserts
        elif kind == "definition" and rest:
            extra["definition"] = _collapse(rest)
        if name.endswith("'"):
            extra["restriction_of"] = name.rstrip("'")
        if "euclid" in extra and not re.fullmatch(r"proposition_\d+'*", name):
            extra.pop("euclid")

        decls.append(
            Decl(
                system="leaneuclid",
                id=full_id,
                name=name,
                kind=kind,
                module=str(rel.with_suffix("")),
                family=family,
                statement=sig,
                text=_doc_above(lines, start),
                uses=uses,
                source=src,
                line=start + 1,
                extra=extra,
            )
        )
    return decls


def mine_lean(root: Path, workspace_root: Path) -> MinedSystem:
    """Mine LeanEuclid's System E theory, Book I and UniGeo.

    Args:
        root: LeanEuclid checkout root (``_refs/LeanEuclid``).
        workspace_root: Workspace root.

    Returns:
        A `MinedSystem`. UniGeo theorems carry their natural-language
        statement (``texts/N.txt``) and proof (``proofs/N.txt``) in ``extra``.
    """
    files: list[Path] = []
    for scope in SCOPES:
        base = root / scope
        if base.is_file() or base.with_suffix(".lean").is_file():
            pass
        files.extend(sorted(p for p in base.rglob("*.lean") if ".lake" not in p.parts))
    decls: list[Decl] = []
    for path in files:
        decls.extend(parse_lean_file(path, root, workspace_root))

    for d in decls:
        cat, num = d.extra.get("category"), d.extra.get("number")
        if d.kind == "theorem" and cat and num:
            for key, sub in (("nl_statement", "texts"), ("nl_proof", "proofs")):
                p = root / "UniGeo" / str(cat) / sub / f"{num}.txt"
                if p.exists():
                    d.extra[key] = p.read_text(encoding="utf-8").strip()
            if "nl_statement" in d.extra:
                d.text = str(d.extra.pop("nl_statement"))

    return MinedSystem(
        system="leaneuclid",
        decls=decls,
        source=str(root.relative_to(workspace_root)),
        commit=git_head(root),
    )
