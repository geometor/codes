"""Typed registries, cross-system query helpers, and optional `_refs/` inspector.

Loads the five canonical comparative datasets from `resources/` (`systems.json`,
`syntax_lexicon.json`, `opus_matrix.json`, `rosetta_benchmarks.json`, and
`geometor_hierarchy.json`) into immutable Python 3.13 dataclasses. Gracefully
operates 100% standalone on CI when external `_refs/` clones are absent.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


def default_resources_dir() -> Path:
    """Return the canonical `resources/` directory of the `geometor-codes` repo.

    Returns:
        Absolute `Path` to `resources/`.
    """
    return Path(__file__).resolve().parents[3] / "resources"


def default_workspace_root() -> Path:
    """Return the parent GEOMETOR workspace root (`/home/phi/PROJECTS/geometor`).

    Returns:
        Absolute `Path` to workspace root.
    """
    return Path(__file__).resolve().parents[4]


@dataclass(frozen=True)
class SystemProfile:
    """Structured architectural profile of a formal or symbolic geometry system."""

    id: str
    name: str
    paradigm: str
    host_language: str
    license: str
    local_ref_relpath: str
    upstream_url: str
    primitives: tuple[str, ...]
    underlying_algebra_or_logic: str
    metric_treatment: str
    diorismos_and_degeneracy: str
    verification_engine: str
    signature_opus_scale: str
    strengths: tuple[str, ...]
    blind_spots: tuple[str, ...]
    geometor_takeaway: str

    def check_local_path(self, workspace_root: Path | None = None) -> Path | None:
        """Return resolved local reference path if present on disk, else ``None``.

        Args:
            workspace_root: Optional workspace directory override.

        Returns:
            Existing ``Path`` when ``_refs/`` is available locally, otherwise ``None``.
        """
        root = workspace_root if workspace_root is not None else default_workspace_root()
        candidate = root / self.local_ref_relpath
        return candidate if candidate.exists() else None


@dataclass(frozen=True)
class SyntaxEntry:
    """Cross-system symbol, operator, binder, predicate, or tactic decoder entry."""

    symbol: str
    aliases: tuple[str, ...]
    system_ids: tuple[str, ...]
    category: str
    pronunciation: str
    plain_meaning: str
    formal_semantics: str
    example_snippet: str
    geometor_equivalent: str


@dataclass(frozen=True)
class OpusDomain:
    """One of the 8 canonical domains of the geometric opus coverage matrix."""

    id: str
    number: int
    title: str
    summary: str


@dataclass(frozen=True)
class OpusCoverageCell:
    """Coverage status and canonical identifier of one topic in one system."""

    status: str
    ref: str


@dataclass(frozen=True)
class OpusTopic:
    """Single canonical geometric concept, construction, or theorem in the opus matrix."""

    id: str
    domain_id: str
    title: str
    role: str
    coverage: dict[str, OpusCoverageCell]
    notes: str


@dataclass(frozen=True)
class RosettaImplementation:
    """Encoding of a Rosetta Stone benchmark inside a single system."""

    language: str
    source_ref: str
    code: str
    reveals: str
    hides: str


@dataclass(frozen=True)
class RosettaBenchmark:
    """Side-by-side Rosetta Stone benchmark comparing a canonical figure across systems."""

    id: str
    number: int
    title: str
    geometor_signature: str
    euclid_ref: str
    geometric_essence: str
    figure_svg: str
    implementations: dict[str, RosettaImplementation]


@dataclass(frozen=True)
class HierarchyRepo:
    """Single repository entry in the 7-layer GEOMETOR ecosystem architecture."""

    name: str
    pillar: str
    status: str
    summary: str
    informed_by_codes: str


@dataclass(frozen=True)
class HierarchyLayer:
    """Architectural layer in the GEOMETOR ecosystem hierarchy."""

    layer_index: int
    id: str
    title: str
    epistemic_role: str
    repos: tuple[HierarchyRepo, ...]


@dataclass(frozen=True)
class ArchitecturalRecommendation:
    """Actionable design recommendation flowing from ``codes`` into GEOMETOR."""

    id: str
    priority: int
    target_repo: str
    title: str
    inspired_by: tuple[str, ...]
    summary: str
    api_sketch: str


class CodesRegistry:
    """Central query interface over all `geometor-codes` comparative datasets."""

    def __init__(self, resources_dir: Path | None = None) -> None:
        """Load and validate all JSON datasets from `resources_dir`.

        Args:
            resources_dir: Optional directory override; defaults to `resources/`.
        """
        self.resources_dir: Path = (
            resources_dir if resources_dir is not None else default_resources_dir()
        )
        self.systems: tuple[SystemProfile, ...] = self._load_systems()
        self.systems_by_id: dict[str, SystemProfile] = {s.id: s for s in self.systems}
        self.lexicon: tuple[SyntaxEntry, ...] = self._load_lexicon()
        self.domains, self.topics = self._load_opus()
        self.benchmarks: tuple[RosettaBenchmark, ...] = self._load_benchmarks()
        self.layers, self.recommendations = self._load_hierarchy()

    def _read_json(self, filename: str) -> Any:  # noqa: ANN401
        path = self.resources_dir / filename
        return json.loads(path.read_text(encoding="utf-8"))

    def _load_systems(self) -> tuple[SystemProfile, ...]:
        raw = self._read_json("systems.json")
        out: list[SystemProfile] = []
        for item in raw["systems"]:
            out.append(
                SystemProfile(
                    id=item["id"],
                    name=item["name"],
                    paradigm=item["paradigm"],
                    host_language=item["host_language"],
                    license=item["license"],
                    local_ref_relpath=item["local_ref_relpath"],
                    upstream_url=item["upstream_url"],
                    primitives=tuple(item["primitives"]),
                    underlying_algebra_or_logic=item["underlying_algebra_or_logic"],
                    metric_treatment=item["metric_treatment"],
                    diorismos_and_degeneracy=item["diorismos_and_degeneracy"],
                    verification_engine=item["verification_engine"],
                    signature_opus_scale=item["signature_opus_scale"],
                    strengths=tuple(item["strengths"]),
                    blind_spots=tuple(item["blind_spots"]),
                    geometor_takeaway=item["geometor_takeaway"],
                )
            )
        return tuple(out)

    def _load_lexicon(self) -> tuple[SyntaxEntry, ...]:
        raw = self._read_json("syntax_lexicon.json")
        out: list[SyntaxEntry] = []
        for item in raw["entries"]:
            out.append(
                SyntaxEntry(
                    symbol=item["symbol"],
                    aliases=tuple(item.get("aliases", [])),
                    system_ids=tuple(item["system_ids"]),
                    category=item["category"],
                    pronunciation=item["pronunciation"],
                    plain_meaning=item["plain_meaning"],
                    formal_semantics=item["formal_semantics"],
                    example_snippet=item["example_snippet"],
                    geometor_equivalent=item["geometor_equivalent"],
                )
            )
        return tuple(out)

    def _load_opus(self) -> tuple[tuple[OpusDomain, ...], tuple[OpusTopic, ...]]:
        raw = self._read_json("opus_matrix.json")
        domains = tuple(
            OpusDomain(
                id=d["id"],
                number=int(d["number"]),
                title=d["title"],
                summary=d["summary"],
            )
            for d in raw["domains"]
        )
        topics: list[OpusTopic] = []
        for t in raw["topics"]:
            cov = {
                sys_id: OpusCoverageCell(status=cell["status"], ref=cell["ref"])
                for sys_id, cell in t["coverage"].items()
            }
            topics.append(
                OpusTopic(
                    id=t["id"],
                    domain_id=t["domain_id"],
                    title=t["title"],
                    role=t["role"],
                    coverage=cov,
                    notes=t["notes"],
                )
            )
        return domains, tuple(topics)

    def _load_benchmarks(self) -> tuple[RosettaBenchmark, ...]:
        raw = self._read_json("rosetta_benchmarks.json")
        out: list[RosettaBenchmark] = []
        for b in raw["benchmarks"]:
            impls = {
                sys_id: RosettaImplementation(
                    language=imp["language"],
                    source_ref=imp["source_ref"],
                    code=imp["code"],
                    reveals=imp["reveals"],
                    hides=imp["hides"],
                )
                for sys_id, imp in b["implementations"].items()
            }
            out.append(
                RosettaBenchmark(
                    id=b["id"],
                    number=int(b["number"]),
                    title=b["title"],
                    geometor_signature=b["geometor_signature"],
                    euclid_ref=b["euclid_ref"],
                    geometric_essence=b["geometric_essence"],
                    figure_svg=b.get("figure_svg", ""),
                    implementations=impls,
                )
            )
        return tuple(out)

    def _load_hierarchy(
        self,
    ) -> tuple[tuple[HierarchyLayer, ...], tuple[ArchitecturalRecommendation, ...]]:
        raw = self._read_json("geometor_hierarchy.json")
        layers: list[HierarchyLayer] = []
        for lyr in raw["layers"]:
            repos = tuple(
                HierarchyRepo(
                    name=r["name"],
                    pillar=r["pillar"],
                    status=r["status"],
                    summary=r["summary"],
                    informed_by_codes=r["informed_by_codes"],
                )
                for r in lyr["repos"]
            )
            layers.append(
                HierarchyLayer(
                    layer_index=int(lyr["layer_index"]),
                    id=lyr["id"],
                    title=lyr["title"],
                    epistemic_role=lyr["epistemic_role"],
                    repos=repos,
                )
            )
        recs = tuple(
            ArchitecturalRecommendation(
                id=rec["id"],
                priority=int(rec["priority"]),
                target_repo=rec["target_repo"],
                title=rec["title"],
                inspired_by=tuple(rec["inspired_by"]),
                summary=rec["summary"],
                api_sketch=rec["api_sketch"],
            )
            for rec in raw["recommendations"]
        )
        return tuple(layers), recs

    def decode(self, query: str) -> list[SyntaxEntry]:
        """Search the strange-symbol lexicon by exact token, alias, or substring.

        Args:
            query: Symbol, operator, tactic, or keyword to look up.

        Returns:
            Matching `SyntaxEntry` items ranked with exact/alias matches first.
        """
        q = query.strip()
        if not q:
            return list(self.lexicon)
        q_low = q.lower()
        exact: list[SyntaxEntry] = []
        partial: list[SyntaxEntry] = []
        for entry in self.lexicon:
            if entry.symbol == q or entry.symbol.lower() == q_low or any(
                a.lower() == q_low for a in entry.aliases
            ):
                exact.append(entry)
            elif (
                q_low in entry.symbol.lower()
                or any(q_low in a.lower() for a in entry.aliases)
                or q_low in entry.pronunciation.lower()
                or q_low in entry.plain_meaning.lower()
                or q_low in entry.geometor_equivalent.lower()
            ):
                partial.append(entry)
        return exact + partial

    def opus_coverage_counts(self) -> dict[str, dict[str, int]]:
        """Compute per-system status tallies across all opus topics.

        Returns:
            Nested mapping from ``system_id`` to status counts.
        """
        counts: dict[str, dict[str, int]] = {
            s.id: {"native": 0, "derived": 0, "partial": 0, "broken": 0, "absent": 0}
            for s in self.systems
        }
        for topic in self.topics:
            for sys_id, cell in topic.coverage.items():
                if sys_id in counts:
                    counts[sys_id][cell.status] = counts[sys_id].get(cell.status, 0) + 1
        return counts
