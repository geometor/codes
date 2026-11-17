"""Shared record types and deterministic snapshot I/O for miners."""

from __future__ import annotations

import json
import subprocess
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Decl:
    """One declaration mined from a system.

    Attributes:
        system: System key from ``context.toml`` (e.g. ``"leaneuclid"``).
        id: Identifier unique within the system (e.g. ``"Elements.Book1.proposition_5"``).
        name: Short display name.
        kind: Declaration kind (``axiom``, ``theorem``, ``rule``, ``construction``,
            ``definition``, ``postulate``, ``common_notion``, ``relation``, ``sort``,
            ``predicate``, ``measure``, ``method``, ``foundation``).
        module: Hierarchical location inside the system (path-like).
        family: Grouping used by the system itself (file, book, category).
        statement: Formal statement as written in the system.
        text: Natural-language text (docstring, description, enunciation).
        premises: Premise atoms (rule-like systems), raw syntax.
        conclusions: Conclusion atoms, raw syntax.
        uses: Other declarations cited by this one (proof trace / dependencies).
        source: Source file relative to the workspace root.
        line: 1-based line number in ``source``.
        extra: System-specific fields.
    """

    system: str
    id: str
    name: str
    kind: str
    module: str = ""
    family: str = ""
    statement: str = ""
    text: str = ""
    premises: list[str] = field(default_factory=list)
    conclusions: list[str] = field(default_factory=list)
    uses: list[str] = field(default_factory=list)
    source: str = ""
    line: int = 0
    extra: dict[str, Any] = field(default_factory=dict)

    @property
    def key(self) -> str:
        """Return the globally unique key ``system:id``."""
        return f"{self.system}:{self.id}"

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable dict with empty fields dropped."""
        data = asdict(self)
        return {k: v for k, v in data.items() if v not in ("", [], {}, 0) or k in ("system", "id")}

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Decl:
        """Build a `Decl` from `to_dict` output.

        Args:
            data: Serialized declaration.

        Returns:
            The reconstructed `Decl`.
        """
        return cls(**data)


@dataclass
class MinedSystem:
    """A system's mined declarations plus provenance."""

    system: str
    decls: list[Decl]
    source: str = ""
    commit: str = ""
    version: str = ""

    def counts(self) -> dict[str, int]:
        """Return declaration counts by kind (sorted)."""
        return dict(sorted(Counter(d.kind for d in self.decls).items()))


def git_head(path: Path) -> str:
    """Return the git HEAD commit of ``path`` or ``""`` when unavailable.

    Args:
        path: A directory inside a git checkout.

    Returns:
        The full commit SHA, or an empty string.
    """
    try:
        out = subprocess.run(
            ["git", "-C", str(path), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return ""
    return out.stdout.strip()


def write_snapshot(mined: MinedSystem, out_dir: Path) -> Path:
    """Write ``<system>.jsonl`` and update ``manifest.json`` deterministically.

    Args:
        mined: The mined system.
        out_dir: Snapshot directory (``resources/mined``).

    Returns:
        Path of the written JSONL file.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    decls = sorted(mined.decls, key=lambda d: d.id)
    ids = [d.id for d in decls]
    if len(ids) != len(set(ids)):
        dup = sorted(k for k, v in Counter(ids).items() if v > 1)
        raise ValueError(f"duplicate ids in {mined.system}: {dup[:5]}")
    path = out_dir / f"{mined.system}.jsonl"
    with path.open("w", encoding="utf-8") as fh:
        for d in decls:
            fh.write(json.dumps(d.to_dict(), ensure_ascii=False, sort_keys=True) + "\n")

    manifest_path = out_dir / "manifest.json"
    manifest: dict[str, Any] = {}
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest[mined.system] = {
        "source": mined.source,
        "commit": mined.commit,
        "version": mined.version,
        "count": len(decls),
        "by_kind": mined.counts(),
    }
    manifest_path.write_text(
        json.dumps(dict(sorted(manifest.items())), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def load_snapshot(system: str, snap_dir: Path) -> list[Decl]:
    """Load a system's declarations from its JSONL snapshot.

    Args:
        system: System key.
        snap_dir: Snapshot directory.

    Returns:
        Declarations in snapshot order (empty if the snapshot is missing).
    """
    path = snap_dir / f"{system}.jsonl"
    if not path.exists():
        return []
    with path.open(encoding="utf-8") as fh:
        return [Decl.from_dict(json.loads(line)) for line in fh if line.strip()]


def load_manifest(snap_dir: Path) -> dict[str, Any]:
    """Load the snapshot manifest.

    Args:
        snap_dir: Snapshot directory.

    Returns:
        The manifest mapping (empty when missing).
    """
    path = snap_dir / "manifest.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
