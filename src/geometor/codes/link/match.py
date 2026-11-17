"""Match discovered principles against indexed linked libraries."""

from __future__ import annotations

import re
from pathlib import Path

from geometor.codes.discover.cluster import Catalog, Principle
from geometor.codes.lexicon import Lexicon
from geometor.codes.link.indexers import LinkedEntry, load_linked_snapshot
from geometor.codes.registry import default_resources_dir

_STOP_WORDS = frozenset({
    "and", "are", "the", "for", "from", "with", "that", "this", "into",
    "two", "three", "four", "one", "line", "lines", "point", "points",
    "theorem", "euclid", "book", "prop", "proposition", "rule",
})


def _tokens(text: str) -> set[str]:
    return {
        t
        for t in re.split(r"[^a-z0-9]+", text.lower())
        if len(t) >= 4 and t not in _STOP_WORDS
    }


def _euclid_ref_tokens(euclid_refs: list[str]) -> set[str]:
    """Turn ``I.5`` into GeoCoq-style tokens like ``proposition_5``, ``prop_i_5``."""
    out: set[str] = set()
    for ref in euclid_refs:
        m = re.fullmatch(r"([IVX]+)\.(\d+)", ref)
        if not m:
            continue
        book, num = m[1], m[2]
        if book == "I":
            out.add(f"proposition_{num}")
            out.add(f"proposition_{num}'")
        out.add(f"prop_{book.lower()}_{num}")
    return out


def match_linked_to_catalog(
    catalog: Catalog,
    linked_dir: Path | None = None,
    lexicon: Lexicon | None = None,
    top_k: int = 3,
) -> dict[str, int]:
    """Attach ranked linked-library matches to each principle in ``catalog``.

    Args:
        catalog: Discovered `Catalog` (updated in place).
        linked_dir: Directory containing ``<system>.jsonl`` snapshots.
        lexicon: Optional `Lexicon`.
        top_k: Maximum matches kept per linked system per principle.

    Returns:
        Count of linked matches attached per system.
    """
    ldir = linked_dir or default_resources_dir() / "linked"
    lex = lexicon or Lexicon.load()

    systems = ("geocoq", "mathlib4", "jgex", "kingdon", "galgebra", "cindyjs")
    entries_by_sys: dict[str, list[LinkedEntry]] = {
        s: load_linked_snapshot(s, ldir) for s in systems
    }

    # Pre-index GeoCoq OriginalProofs by proposition name for O(1) exact hits.
    geocoq_orig: dict[str, list[LinkedEntry]] = {}
    for e in entries_by_sys["geocoq"]:
        if "OriginalProofs" in e.id:
            geocoq_orig.setdefault(e.name.lower(), []).append(e)

    # Pre-index entries by lowercase name token for fast lookup.
    token_idx: dict[str, dict[str, list[LinkedEntry]]] = {}
    for s, items in entries_by_sys.items():
        idx: dict[str, list[LinkedEntry]] = {}
        for e in items:
            for tok in _tokens(e.name) | _tokens(e.doc):
                idx.setdefault(tok, []).append(e)
        token_idx[s] = idx

    totals: dict[str, int] = {s: 0 for s in systems}
    for p in catalog.principles:
        links: list[dict[str, object]] = []
        lex_entry = lex.entries.get(p.id)
        euclid_toks = _euclid_ref_tokens(p.euclid_refs)
        p_toks = _tokens(p.id) | _tokens(p.title)

        for sys_id in systems:
            scored: dict[str, tuple[float, str, LinkedEntry]] = {}

            # 1. Exact Euclid Book I match in GeoCoq OriginalProofs
            if sys_id == "geocoq":
                for etok in euclid_toks:
                    for e in geocoq_orig.get(etok, ()):
                        scored[e.id] = (1.0, f"euclid_ref:{etok}", e)

            # 2. Lexicon alias match
            if lex_entry is not None:
                for alias in lex_entry.aliases.get(sys_id, ()):
                    short = alias.rsplit(".", 1)[-1].lower()
                    for e in entries_by_sys[sys_id]:
                        if e.name.lower() == short or e.id.lower().endswith(alias.lower()):
                            scored[e.id] = (0.95, f"lexicon:{alias}", e)

            # 3. Token overlap (skip singleton Euclid items with no keywords to avoid noise)
            if p_toks and (len(p.members) > 1 or p.id in lex.entries or p.euclid_refs):
                cand_counts: dict[str, tuple[int, LinkedEntry]] = {}
                for tok in p_toks:
                    for e in token_idx[sys_id].get(tok, ()):
                        prev = cand_counts.get(e.id)
                        cand_counts[e.id] = ((prev[0] + 1) if prev else 1, e)
                for eid, (hits, e) in cand_counts.items():
                    if eid in scored:
                        continue
                    score = min(0.85, 0.35 * hits)
                    if score >= 0.35:
                        scored[eid] = (score, f"tokens:{hits}", e)

            top = sorted(scored.values(), key=lambda x: (-x[0], x[2].id))[:top_k]
            for conf, ev, e in top:
                totals[sys_id] += 1
                links.append({
                    "system": sys_id,
                    "id": e.id,
                    "name": e.name,
                    "statement": e.statement,
                    "url": e.url,
                    "relation": "equivalent" if conf >= 0.95 else "candidate",
                    "confidence": round(conf, 2),
                    "evidence": ev,
                })

        p.linked = links
    return totals
