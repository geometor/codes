"""Canonical lexicon: one name per geometric concept, aliased across systems.

The lexicon lives in ``resources/lexicon/lexicon.toml`` and is seeded from the
function vocabulary of ``geometor.etc`` (``ops.py``). See
``resources/lexicon/conventions.md`` for the naming rules.
"""

from __future__ import annotations

import ast
import re
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

from geometor.codes.registry import default_resources_dir, default_workspace_root

KINDS = (
    "object",
    "relation",
    "measure",
    "construction",
    "center",
    "triangle",
    "circle",
    "operator",
    "property",
)

# Repos whose public Python identifiers are audited against the lexicon.
AUDIT_REPOS = (
    "etc",
    "elements",
    "model",
    "explorer",
    "pappus",
    "wildberger",
    "fundamentals",
    "divine",
)

# Systems that GEOMETOR owns; divergence here is actionable (rename proposals).
OWNED_SYSTEMS = ("etc", "elements", "model")


@dataclass(frozen=True)
class LexiconEntry:
    """A canonical concept with its aliases in each system."""

    name: str
    kind: str
    family: str
    summary: str
    aliases: dict[str, tuple[str, ...]]
    etc_x: int | None = None

    def all_aliases(self) -> list[tuple[str, str]]:
        """Return ``(system, alias)`` pairs in deterministic order."""
        return [(s, a) for s in sorted(self.aliases) for a in self.aliases[s]]


@dataclass
class Lexicon:
    """The loaded canonical lexicon."""

    entries: dict[str, LexiconEntry]
    systems: tuple[str, ...]
    families: tuple[str, ...]
    etc_infrastructure: tuple[str, ...]
    _index: dict[tuple[str, str], str] = field(default_factory=dict, repr=False)

    @classmethod
    def load(cls, path: Path | None = None) -> Lexicon:
        """Load the lexicon TOML.

        Args:
            path: Optional path to ``lexicon.toml``; defaults to the packaged resource.

        Returns:
            A populated `Lexicon`.
        """
        path = path or default_resources_dir() / "lexicon" / "lexicon.toml"
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        meta = data.get("meta", {})
        systems = tuple(meta.get("systems", ()))
        entries: dict[str, LexiconEntry] = {}
        for name, raw in data.get("entry", {}).items():
            aliases = {s: tuple(raw[s]) for s in systems if s in raw}
            entries[name] = LexiconEntry(
                name=name,
                kind=raw.get("kind", ""),
                family=raw.get("family", ""),
                summary=raw.get("summary", ""),
                aliases=aliases,
                etc_x=raw.get("etc_x"),
            )
        lex = cls(
            entries=entries,
            systems=systems,
            families=tuple(meta.get("families", ())),
            etc_infrastructure=tuple(meta.get("etc_infrastructure", {}).get("names", ())),
        )
        for entry in entries.values():
            for system, alias in entry.all_aliases():
                lex._index.setdefault((system, alias), entry.name)
        return lex

    def resolve(self, system: str, name: str) -> LexiconEntry | None:
        """Return the canonical entry that ``name`` denotes in ``system``.

        Args:
            system: System key (e.g. ``"alphageometry"``).
            name: The system's own identifier.

        Returns:
            The matching `LexiconEntry`, or ``None``.
        """
        key = self._index.get((system, name))
        if key is None and name in self.entries:
            return self.entries[name]
        return self.entries.get(key) if key else None

    def search(self, query: str) -> list[LexiconEntry]:
        """Case-insensitive search over names, aliases and summaries.

        Args:
            query: Substring to look for.

        Returns:
            Matching entries sorted by name.
        """
        q = query.lower()
        hits = []
        for entry in self.entries.values():
            hay = [entry.name, entry.summary] + [a for _, a in entry.all_aliases()]
            if any(q in h.lower() for h in hay):
                hits.append(entry)
        return sorted(hits, key=lambda e: e.name)

    def validate(self) -> list[str]:
        """Check structural rules of the lexicon.

        Returns:
            A list of human-readable problems (empty when valid).
        """
        problems: list[str] = []
        seen: dict[tuple[str, str], str] = {}
        for entry in self.entries.values():
            if entry.kind not in KINDS:
                problems.append(f"{entry.name}: unknown kind {entry.kind!r}")
            if entry.family not in self.families:
                problems.append(f"{entry.name}: unknown family {entry.family!r}")
            if not re.fullmatch(r"[a-z][a-z0-9_]*", entry.name):
                problems.append(f"{entry.name}: canonical name is not snake_case")
            for system, alias in entry.all_aliases():
                other = seen.get((system, alias))
                if other and other != entry.name:
                    problems.append(
                        f"alias {system}:{alias} maps to both {other} and {entry.name}"
                    )
                seen[(system, alias)] = entry.name
        return problems


# ---------------------------------------------------------------- audit


@dataclass(frozen=True)
class RenameProposal:
    """A proposal to align a GEOMETOR identifier with the canonical name."""

    system: str
    current: str
    canonical: str
    where: str


@dataclass
class AuditReport:
    """Result of `audit_lexicon`."""

    problems: list[str]
    etc_missing: list[str]
    proposals: list[RenameProposal]
    unresolved_sympy: list[str]
    stats: dict[str, int]


def _public_functions(path: Path) -> list[tuple[str, int]]:
    """Return top-level public function names and line numbers in a module."""
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"))
    except (SyntaxError, UnicodeDecodeError):
        return []
    return [
        (node.name, node.lineno)
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and not node.name.startswith("_")
    ]


def _resolve_sympy(alias: str) -> bool:
    """Return whether a ``Class.member`` alias exists in ``sympy.geometry``."""
    import sympy.geometry as spg

    parts = alias.split(".")
    obj: object = spg
    for part in parts:
        if not hasattr(obj, part):
            return False
        obj = getattr(obj, part)
    return True


def audit_lexicon(
    lexicon: Lexicon | None = None, workspace_root: Path | None = None
) -> AuditReport:
    """Audit the lexicon and propose canonical renames across GEOMETOR repos.

    No files are modified. Proposals are informational: any adopted rename must
    keep the old name as an alias.

    Args:
        lexicon: Lexicon to audit (loaded from resources when omitted).
        workspace_root: GEOMETOR workspace root (``/home/phi/PROJECTS/geometor``).

    Returns:
        An `AuditReport`.
    """
    lex = lexicon or Lexicon.load()
    root = workspace_root or default_workspace_root()
    problems = lex.validate()

    # 1. Every etc ops function is a lexicon concept or declared infrastructure.
    etc_missing: list[str] = []
    ops = root / "etc" / "src" / "geometor" / "etc" / "ops.py"
    etc_names: list[tuple[str, int]] = _public_functions(ops) if ops.exists() else []
    infra = set(lex.etc_infrastructure)
    for name, _ in etc_names:
        if name not in infra and lex.resolve("etc", name) is None:
            etc_missing.append(name)

    # 2. Divergent aliases in owned systems (ETC is the seed and never diverges;
    # model method names are API verbs and are reported only via the scan).
    proposals: set[RenameProposal] = set()
    for entry in lex.entries.values():
        for alias in entry.aliases.get("elements", ()):
            if alias != entry.name:
                proposals.add(RenameProposal("elements", alias, entry.name, "lexicon"))

    # 3. Public functions in GEOMETOR repos that use another system's alias.
    alias_to_canon: dict[str, str] = {}
    for entry in lex.entries.values():
        for system, alias in entry.all_aliases():
            if system in ("model", "etc") or "." in alias or len(alias) <= 3:
                continue
            if alias != entry.name:
                alias_to_canon.setdefault(alias, entry.name)
    scanned = 0
    for repo in AUDIT_REPOS:
        src = root / repo / "src"
        if not src.exists():
            continue
        for py in sorted(src.rglob("*.py")):
            scanned += 1
            for name, line in _public_functions(py):
                canon = alias_to_canon.get(name)
                if canon and canon != name and name not in lex.entries:
                    rel = py.relative_to(root)
                    proposals.add(RenameProposal(repo, name, canon, f"{rel}:{line}"))

    # 4. SymPy aliases must exist in the installed SymPy.
    unresolved = sorted(
        alias
        for entry in lex.entries.values()
        for alias in entry.aliases.get("sympy", ())
        if not _resolve_sympy(alias)
    )

    stats = {
        "entries": len(lex.entries),
        "aliases": sum(len(e.all_aliases()) for e in lex.entries.values()),
        "etc_functions": len(etc_names),
        "etc_infrastructure": len(infra),
        "files_scanned": scanned,
    }
    return AuditReport(
        problems=problems,
        etc_missing=sorted(etc_missing),
        proposals=sorted(proposals, key=lambda p: (p.canonical, p.system, p.current, p.where)),
        unresolved_sympy=unresolved,
        stats=stats,
    )
