"""Context manifest loader and base-context mining orchestrator."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass
from pathlib import Path

from geometor.codes.mine.ag import mine_alphageometry
from geometor.codes.mine.euclid import mine_euclid
from geometor.codes.mine.geometor_model import mine_geometor_model
from geometor.codes.mine.lean import mine_lean
from geometor.codes.mine.newclid import mine_newclid
from geometor.codes.mine.schema import MinedSystem, write_snapshot
from geometor.codes.mine.sympy_geo import mine_sympy
from geometor.codes.registry import default_resources_dir, default_workspace_root


@dataclass(frozen=True)
class ContextSystem:
    """One entry in ``resources/context.toml``."""

    id: str
    role: str
    name: str
    source: str
    miner: str = ""
    upstream: str = ""
    not_yet_in_canon: tuple[str, ...] = ()


@dataclass(frozen=True)
class ContextManifest:
    """Loaded ``context.toml`` manifest separating base and linked systems."""

    systems: dict[str, ContextSystem]

    @classmethod
    def load(cls, path: Path | None = None) -> ContextManifest:
        """Load the context manifest from TOML.

        Args:
            path: Optional path to ``context.toml``.

        Returns:
            A populated `ContextManifest`.
        """
        path = path or default_resources_dir() / "context.toml"
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        systems: dict[str, ContextSystem] = {}
        for sys_id, raw in data.get("systems", {}).items():
            systems[sys_id] = ContextSystem(
                id=sys_id,
                role=raw["role"],
                name=raw["name"],
                source=raw["source"],
                miner=raw.get("miner", ""),
                upstream=raw.get("upstream", ""),
                not_yet_in_canon=tuple(raw.get("not_yet_in_canon", ())),
            )
        return cls(systems=systems)

    def by_role(self, role: str) -> list[ContextSystem]:
        """Return systems matching ``role`` (``"base"`` or ``"linked"``)."""
        return [s for s in self.systems.values() if s.role == role]


def mine_system(
    spec: ContextSystem, workspace_root: Path
) -> MinedSystem:
    """Run the appropriate miner for one `ContextSystem`.

    Args:
        spec: System specification from `context.toml`.
        workspace_root: Workspace root.

    Returns:
        The `MinedSystem` result.
    """
    src_path = workspace_root / spec.source
    if spec.miner == "euclid":
        return mine_euclid(src_path, workspace_root, spec.not_yet_in_canon)
    if spec.miner == "lean":
        return mine_lean(src_path, workspace_root)
    if spec.miner == "alphageometry":
        return mine_alphageometry(src_path, workspace_root)
    if spec.miner == "newclid":
        return mine_newclid(src_path, workspace_root)
    if spec.miner == "sympy":
        return mine_sympy()
    if spec.miner == "model":
        return mine_geometor_model(src_path, workspace_root)
    raise ValueError(f"Unknown miner {spec.miner!r} for system {spec.id!r}")


def mine_all_base(
    workspace_root: Path | None = None,
    out_dir: Path | None = None,
    manifest: ContextManifest | None = None,
) -> list[MinedSystem]:
    """Mine every ``role = "base"`` system and write deterministic snapshots.

    Args:
        workspace_root: Workspace root (defaults to parent of ``codes``).
        out_dir: Output directory (defaults to ``resources/mined``).
        manifest: Optional preloaded `ContextManifest`.

    Returns:
        List of `MinedSystem` results in manifest order.
    """
    ws = workspace_root or default_workspace_root()
    out = out_dir or default_resources_dir() / "mined"
    ctx = manifest or ContextManifest.load()

    results: list[MinedSystem] = []
    for spec in ctx.by_role("base"):
        mined = mine_system(spec, ws)
        write_snapshot(mined, out)
        results.append(mined)
    return results
