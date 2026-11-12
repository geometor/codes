"""Comprehensive test suite for `geometor.codes` registries, figures, and CLI."""

from __future__ import annotations

from pathlib import Path
import sympy as sp

from geometor.codes import FIGURE_SPECS, CodesRegistry, __version__, build_all_figures
from geometor.codes.__main__ import main as cli_main
from geometor.codes.cli import run_cli
from geometor.codes.render import render_svg

VALID_STATUSES: frozenset[str] = frozenset(
    {"native", "derived", "partial", "broken", "absent"}
)
EXPECTED_SYSTEM_IDS: tuple[str, ...] = (
    "leaneuclid",
    "geocoq",
    "mathlib4",
    "alphageometry",
    "newclid",
    "jgex",
    "pga_cga",
    "cindyjs",
    "sympy_geometry",
    "byrne_1847",
    "geometor_model",
)


def test_version_string() -> None:
    """Verify package exposes semantic version string."""
    assert __version__ == "0.1.0"


def test_registry_systems_and_offline_resilience(tmp_path: Path) -> None:
    """Verify all 11 system profiles load and gracefully handle missing `_refs/`."""
    reg = CodesRegistry()
    assert tuple(s.id for s in reg.systems) == EXPECTED_SYSTEM_IDS
    for sys_prof in reg.systems:
        assert sys_prof.name
        assert sys_prof.paradigm
        assert len(sys_prof.primitives) >= 1
        assert len(sys_prof.strengths) >= 2
        assert len(sys_prof.blind_spots) >= 2
        assert sys_prof.geometor_takeaway
        # Simulate CI environment without external _refs/ clones
        assert sys_prof.check_local_path(workspace_root=tmp_path) is None


def test_syntax_lexicon_and_decoder() -> None:
    """Verify strange-symbol lexicon completeness and query ranking."""
    reg = CodesRegistry()
    assert len(reg.lexicon) >= 58

    for query, expected_sys in (
        ("-ᵥ", "mathlib4"),
        ("eqangle", "alphageometry"),
        (">>", "pga_cga"),
        ("Bet", "geocoq"),
        ("side_of", "geometor_model"),
        ("::", "byrne_1847"),
        ("quadrance", "geometor_model"),
    ):
        matches = reg.decode(query)
        assert matches, f"Expected matches for {query!r}"
        assert expected_sys in matches[0].system_ids

    assert reg.decode("") == list(reg.lexicon)
    assert reg.decode("nonexistent_xyz_token_999") == []


def test_opus_matrix_completeness_and_counts() -> None:
    """Verify 8 domains x 69 canonical topics x 11 systems with valid statuses."""
    reg = CodesRegistry()
    assert len(reg.domains) == 8
    assert len(reg.topics) == 69

    for topic in reg.topics:
        assert "_" in topic.id or topic.id.islower()
        assert tuple(topic.coverage.keys()) == EXPECTED_SYSTEM_IDS
        for sys_id, cell in topic.coverage.items():
            assert cell.status in VALID_STATUSES, f"Invalid status on {topic.id}/{sys_id}"
            assert cell.ref

    counts = reg.opus_coverage_counts()
    for sys_id in EXPECTED_SYSTEM_IDS:
        assert sum(counts[sys_id].values()) == len(reg.topics)

    # Verify forensic bug flags are captured accurately
    by_id = {t.id: t for t in reg.topics}
    assert by_id["excenters_and_excircles"].coverage["sympy_geometry"].status == "broken"
    assert by_id["pappus_hexagon_theorem"].coverage["sympy_geometry"].status == "broken"
    assert by_id["golden_ratio_extreme_mean_cut"].coverage["byrne_1847"].status == "native"
    assert by_id["golden_ratio_extreme_mean_cut"].coverage["geometor_model"].status == "native"
    assert by_id["golden_ratio_extreme_mean_cut"].coverage["geocoq"].status == "absent"


def test_rosetta_benchmarks_schema() -> None:
    """Verify all 7 Rosetta Stone benchmarks cover all 11 surveyed systems."""
    reg = CodesRegistry()
    assert len(reg.benchmarks) == 7
    for idx, bench in enumerate(reg.benchmarks, start=1):
        assert bench.number == idx
        assert bench.figure_svg.endswith(".svg")
        assert tuple(bench.implementations.keys()) == EXPECTED_SYSTEM_IDS
        for imp in bench.implementations.values():
            assert imp.code
            assert imp.reveals
            assert imp.hides


def test_geometor_hierarchy_and_recommendations() -> None:
    """Verify 7-layer, 33-repository GEOMETOR ecosystem map and recommendations."""
    reg = CodesRegistry()
    assert len(reg.layers) == 7
    total_repos = sum(len(layer.repos) for layer in reg.layers)
    assert total_repos == 33
    repo_names = {r.name for layer in reg.layers for r in layer.repos}
    for expected_repo in ("codes", "byrne", "model", "elements", "wildberger", "pappus", "etc"):
        assert expected_repo in repo_names
    assert len(reg.recommendations) >= 11


def test_all_figures_exact_float_free_and_svg_export(tmp_path: Path) -> None:
    """Verify all 9 `geometor.model` figures contain ZERO `sp.Float` and render clean SVGs."""
    assert len(FIGURE_SPECS) == 9
    for spec in FIGURE_SPECS:
        model, annotations = spec.builder()
        assert len(model) > 0
        for elem in model:
            if hasattr(elem, "x") and hasattr(elem, "y"):
                assert not elem.x.atoms(sp.Float), f"Float found in {spec.slug} point {elem}"
                assert not elem.y.atoms(sp.Float), f"Float found in {spec.slug} point {elem}"
        out_svg = tmp_path / f"{spec.slug}.svg"
        render_svg(model, out_svg, annotations=annotations)
        raw = out_svg.read_text(encoding="utf-8")
        assert 'class="euclid-graphic codes-diagram"' in raw
        assert 'data-ref="A"' in raw or "data-ref=" in raw

    built = build_all_figures(output_dir=tmp_path / "batch")
    assert len(built) == 9


def test_cli_commands(tmp_path: Path, monkeypatch: object) -> None:
    """Verify all `codes` CLI subcommands execute cleanly."""
    import pytest
    import sys

    assert run_cli(["summary"]) == 0
    assert run_cli(["decode", "eqangle"]) == 0
    assert run_cli(["decode", "[━━] / [◣]"]) == 0
    assert run_cli(["decode", "missing_symbol_zzz"]) == 1
    assert run_cli(["opus", "--domain", "4"]) == 0
    assert run_cli(["rosetta", "06-circle-power-inversion-polar"]) == 0
    assert run_cli(["rosetta", "99-missing"]) == 1
    assert run_cli(["hierarchy"]) == 0
    assert run_cli(["build-figures", "--output-dir", str(tmp_path)]) == 0

    mp = pytest.MonkeyPatch()
    mp.setattr(sys, "argv", ["codes", "summary"])
    try:
        with pytest.raises(SystemExit) as exc_info:
            cli_main()
        assert exc_info.value.code == 0
    finally:
        mp.undo()
    del monkeypatch
