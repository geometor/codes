"""Lightweight pure-Python indexers for the linked libraries."""

from __future__ import annotations

import ast
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

from geometor.codes.context import ContextManifest, ContextSystem
from geometor.codes.mine.schema import git_head
from geometor.codes.registry import default_resources_dir, default_workspace_root

_COQ_DECL = re.compile(
    r"^\s*(Lemma|Theorem|Definition|Axiom|Class|Corollary|Fact)\s+([A-Za-z_][\w']*)\s*([^\n.]*)"
)
_MATHLIB_DECL = re.compile(
    r"^(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*"
    r"(theorem|lemma|def|abbrev|structure|class)\s+([^\s:(\[{]+)\s*([^\n]*)"
)
_JAVA_CLASS = re.compile(
    r"^\s*(?:public|private|protected)?\s*(?:static\s+)?(?:abstract\s+)?"
    r"(class|interface|enum)\s+([A-Za-z_]\w*)"
)
_JAVA_METHOD = re.compile(
    r"^\s*(?:public|protected)\s+(?:static\s+)?[\w<>\[\]]+\s+([a-zA-Z_]\w*)\s*\(([^)]*)\)"
)
_JS_FN = re.compile(
    r"(?:^function\s+([A-Za-z_$][\w$]*)\s*\(|([A-Za-z_$][\w$]*)\s*=\s*function\s*\()"
)


@dataclass(frozen=True)
class LinkedEntry:
    """One indexed declaration from a linked library."""

    system: str
    id: str
    name: str
    kind: str
    statement: str = ""
    doc: str = ""
    source: str = ""
    line: int = 0
    url: str = ""

    def to_dict(self) -> dict[str, Any]:
        """Serialize to JSON-ready dict."""
        return {k: v for k, v in asdict(self).items() if v not in ("", 0)}


def _blob_url(upstream: str, commit: str, rel_in_repo: str, line: int) -> str:
    if not upstream or not commit:
        return ""
    base = upstream.rstrip("/")
    return f"{base}/blob/{commit}/{rel_in_repo}#L{line}"


def index_geocoq(spec: ContextSystem, ws: Path) -> tuple[list[LinkedEntry], str]:
    """Index GeoCoq Coq declarations."""
    root = ws / spec.source
    repo = ws / "_refs/GeoCoq"
    sha = git_head(repo)
    entries: list[LinkedEntry] = []
    seen: set[str] = set()
    for p in sorted(root.rglob("*.v")):
        rel_repo = str(p.relative_to(repo))
        rel_ws = str(p.relative_to(ws))
        mod = str(p.relative_to(root).with_suffix("")).replace("/", ".")
        for lineno, line in enumerate(p.read_text(errors="ignore").splitlines(), start=1):
            if m := _COQ_DECL.match(line):
                kind, name, tail = m[1].lower(), m[2], m[3].strip()
                eid = f"{mod}.{name}"
                if eid in seen:
                    continue
                seen.add(eid)
                entries.append(
                    LinkedEntry(
                        system="geocoq",
                        id=eid,
                        name=name,
                        kind=kind,
                        statement=f"{name} {tail}".strip()[:240],
                        source=rel_ws,
                        line=lineno,
                        url=_blob_url(spec.upstream, sha, rel_repo, lineno),
                    )
                )
    return entries, sha


def index_mathlib4(spec: ContextSystem, ws: Path) -> tuple[list[LinkedEntry], str]:
    """Index Mathlib4 Euclidean geometry declarations."""
    root = ws / spec.source
    repo = ws / "_refs/mathlib4"
    sha = git_head(repo)
    entries: list[LinkedEntry] = []
    seen: set[str] = set()
    for p in sorted(root.rglob("*.lean")):
        rel_repo = str(p.relative_to(repo))
        rel_ws = str(p.relative_to(ws))
        mod = str(p.relative_to(repo).with_suffix("")).replace("/", ".")
        lines = p.read_text(errors="ignore").splitlines()
        for lineno, line in enumerate(lines, start=1):
            if m := _MATHLIB_DECL.match(line):
                kind, name, tail = m[1], m[2], m[3].strip()
                eid = f"{mod}.{name}"
                if eid in seen:
                    continue
                seen.add(eid)
                doc = ""
                if lineno >= 2 and lines[lineno - 2].strip().endswith("-/"):
                    doc = lines[lineno - 2].strip().removesuffix("-/").strip()
                entries.append(
                    LinkedEntry(
                        system="mathlib4",
                        id=eid,
                        name=name,
                        kind=kind,
                        statement=f"{name} {tail}".strip()[:240],
                        doc=doc[:200],
                        source=rel_ws,
                        line=lineno,
                        url=_blob_url(spec.upstream, sha, rel_repo, lineno),
                    )
                )
    return entries, sha


def index_jgex(spec: ContextSystem, ws: Path) -> tuple[list[LinkedEntry], str]:
    """Index Java Geometry Expert classes and prover rules."""
    repo = ws / spec.source
    sha = git_head(repo)
    entries: list[LinkedEntry] = []
    seen: set[str] = set()
    src_root = repo / "src"
    if not src_root.exists():
        return entries, sha
    for p in sorted(src_root.rglob("*.java")):
        rel_repo = str(p.relative_to(repo))
        rel_ws = str(p.relative_to(ws))
        pkg = str(p.relative_to(src_root).with_suffix("")).replace("/", ".")
        for lineno, line in enumerate(p.read_text(errors="ignore").splitlines(), start=1):
            if m := _JAVA_CLASS.match(line):
                kind, name = m[1], m[2]
                eid = f"{pkg}" if name == p.stem else f"{pkg}.{name}"
                if eid not in seen:
                    seen.add(eid)
                    entries.append(
                        LinkedEntry(
                            system="jgex",
                            id=eid,
                            name=name,
                            kind=kind,
                            statement=line.strip()[:200],
                            source=rel_ws,
                            line=lineno,
                            url=_blob_url(spec.upstream, sha, rel_repo, lineno),
                        )
                    )
            elif "gprover" in rel_repo and (m := _JAVA_METHOD.match(line)):
                name = m[1]
                eid = f"{pkg}.{name}"
                if eid not in seen and len(name) > 2:
                    seen.add(eid)
                    entries.append(
                        LinkedEntry(
                            system="jgex",
                            id=eid,
                            name=name,
                            kind="method",
                            statement=line.strip()[:200],
                            source=rel_ws,
                            line=lineno,
                            url=_blob_url(spec.upstream, sha, rel_repo, lineno),
                        )
                    )
    return entries, sha


def _index_python_pkg(spec: ContextSystem, ws: Path, pkg_sub: str) -> tuple[list[LinkedEntry], str]:
    repo = ws / spec.source
    sha = git_head(repo)
    pkg_dir = repo / pkg_sub
    entries: list[LinkedEntry] = []
    if not pkg_dir.exists():
        return entries, sha
    for p in sorted(pkg_dir.rglob("*.py")):
        rel_repo = str(p.relative_to(repo))
        rel_ws = str(p.relative_to(ws))
        mod = str(p.relative_to(repo).with_suffix("")).replace("/", ".")
        try:
            tree = ast.parse(p.read_text(encoding="utf-8", errors="ignore"))
        except SyntaxError:
            continue
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                if node.name.startswith("_"):
                    continue
                kind = "class" if isinstance(node, ast.ClassDef) else "function"
                doc = (ast.get_docstring(node) or "").splitlines()[0].strip() if ast.get_docstring(node) else ""
                entries.append(
                    LinkedEntry(
                        system=spec.id,
                        id=f"{mod}.{node.name}",
                        name=node.name,
                        kind=kind,
                        statement=f"{kind} {node.name}",
                        doc=doc[:200],
                        source=rel_ws,
                        line=node.lineno,
                        url=_blob_url(spec.upstream, sha, rel_repo, node.lineno),
                    )
                )
    return entries, sha


def index_cindyjs(spec: ContextSystem, ws: Path) -> tuple[list[LinkedEntry], str]:
    """Index CindyJS functions and CindyScript operators."""
    repo = ws / spec.source
    sha = git_head(repo)
    src_root = repo / "src"
    entries: list[LinkedEntry] = []
    seen: set[str] = set()
    if not src_root.exists():
        return entries, sha
    for p in sorted(src_root.rglob("*.js")):
        rel_repo = str(p.relative_to(repo))
        rel_ws = str(p.relative_to(ws))
        mod = str(p.relative_to(src_root).with_suffix("")).replace("/", ".")
        for lineno, line in enumerate(p.read_text(errors="ignore").splitlines(), start=1):
            if m := _JS_FN.search(line):
                name = m[1] or m[2]
                if not name or name.startswith("_"):
                    continue
                eid = f"{mod}.{name}"
                if eid in seen:
                    continue
                seen.add(eid)
                entries.append(
                    LinkedEntry(
                        system="cindyjs",
                        id=eid,
                        name=name,
                        kind="function",
                        statement=line.strip()[:200],
                        source=rel_ws,
                        line=lineno,
                        url=_blob_url(spec.upstream, sha, rel_repo, lineno),
                    )
                )
    return entries, sha


def index_all_linked(
    workspace_root: Path | None = None,
    out_dir: Path | None = None,
    manifest: ContextManifest | None = None,
) -> dict[str, int]:
    """Index every ``role = "linked"`` system and write deterministic snapshots.

    Returns:
        Mapping ``system_id -> entry_count``.
    """
    ws = workspace_root or default_workspace_root()
    out = out_dir or default_resources_dir() / "linked"
    out.mkdir(parents=True, exist_ok=True)
    ctx = manifest or ContextManifest.load()

    dispatch = {
        "geocoq": index_geocoq,
        "mathlib4": index_mathlib4,
        "jgex": index_jgex,
        "kingdon": lambda s, w: _index_python_pkg(s, w, "kingdon"),
        "galgebra": lambda s, w: _index_python_pkg(s, w, "galgebra"),
        "cindyjs": index_cindyjs,
    }

    counts: dict[str, int] = {}
    snap_manifest: dict[str, Any] = {}
    for spec in ctx.by_role("linked"):
        fn = dispatch.get(spec.id)
        if fn is None:
            continue
        entries, sha = fn(spec, ws)
        entries.sort(key=lambda e: e.id)
        path = out / f"{spec.id}.jsonl"
        with path.open("w", encoding="utf-8") as fh:
            for e in entries:
                fh.write(json.dumps(e.to_dict(), ensure_ascii=False, sort_keys=True) + "\n")
        counts[spec.id] = len(entries)
        snap_manifest[spec.id] = {"commit": sha, "count": len(entries)}

    (out / "manifest.json").write_text(
        json.dumps(dict(sorted(snap_manifest.items())), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return counts


def load_linked_snapshot(system: str, snap_dir: Path | None = None) -> list[LinkedEntry]:
    """Load a linked library snapshot from ``resources/linked/<system>.jsonl``."""
    sdir = snap_dir or default_resources_dir() / "linked"
    path = sdir / f"{system}.jsonl"
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return [LinkedEntry(**json.loads(line)) for line in fh if line.strip()]
