"""Mining layer: extract declarations from the base-context systems.

Each miner turns one system into a list of `Decl` records. Snapshots are
written as deterministic JSONL under ``resources/mined/`` so that ``codes``
works without ``_refs/`` checkouts (for example on CI).
"""

from __future__ import annotations

from geometor.codes.mine.schema import Decl, MinedSystem, load_snapshot, write_snapshot

__all__ = ["Decl", "MinedSystem", "load_snapshot", "write_snapshot"]
