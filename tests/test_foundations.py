"""Tests for truth foundations data, graphs, generic witnesses, and site generation."""

from __future__ import annotations

from pathlib import Path

import pytest

from geometor.codes.foundations import LAYERS, audit_foundations, load_foundations, load_showcase
from geometor.codes.generic import GENERIC_BUILDERS, GENERIC_GAPS, generic_witness
from geometor.codes.graphs import (
    bridges_graph,
    chain_graph,
    ladder_graph,
    ontology_graph,
    overlap_graph,
    shared_principles,
    showcase_graph,
    trust_graph,
)


def test_foundations_load_and_audit() -> None:
    """Foundations and showcase data load and are referentially consistent."""
    fnd = load_foundations()
    showcase = load_showcase()
    assert len(fnd.systems) == 12
    assert {lv.id for lv in fnd.levels} >= {"L0", "L1", "L2", "L3", "L4", "L5", "H"}
    assert audit_foundations(fnd, showcase) == []
    for s in fnd.systems:
        assert set(s.stack) == {k for k, _, _ in LAYERS}, s.id
        assert s.summary, s.id


def test_truth_ladder_placements() -> None:
    """Key placements reflect the audited trust chains."""
    fnd = load_foundations()
    placed = {s.id: s.ladder for s in fnd.systems}
    assert placed["mathlib4"] == "L5"
    assert placed["geocoq"] == "L4"
    assert placed["leaneuclid"] == "L3"  # SMT_VERIF oracle axiom
    assert placed["geometor_model"] == "L1"
    assert placed["cindyjs"] == "L0"
    assert "smt_verif" in fnd.system("leaneuclid").trusts


def test_atlas_json_shape() -> None:
    """The Atlas payload carries layers, axes, levels, and every system."""
    data = load_foundations().to_json()
    assert len(data["layers"]) == 7
    assert len(data["systems"]) == 12
    assert all(s["card"].startswith("foundations/cards/") for s in data["systems"])


def test_graphs_are_dot() -> None:
    """Every graph builder emits balanced DOT source."""
    fnd = load_foundations()
    showcase = load_showcase()
    shared, totals = shared_principles({"p1": {"euclid", "leaneuclid"}, "p2": {"euclid"}})
    assert shared == {("euclid", "leaneuclid"): 1}
    assert totals == {"euclid": 2, "leaneuclid": 1}
    sources = [
        ladder_graph(fnd),
        chain_graph(fnd, fnd.systems[0]),
        trust_graph(fnd),
        bridges_graph(fnd),
        ontology_graph(fnd),
        overlap_graph(fnd, shared, totals),
        showcase_graph(fnd, showcase[0]),
    ]
    for dot in sources:
        assert dot.lstrip().startswith(("digraph", "graph"))
        assert dot.count("{") == dot.count("}")


@pytest.mark.parametrize("pid", sorted(GENERIC_BUILDERS))
def test_generic_witnesses_prove(pid: str) -> None:
    """Symbolic-parameter witnesses reduce exactly to zero."""
    w = generic_witness(pid)
    assert w is not None
    assert w.proved, w.residual
    assert w.ndg


def test_generic_gap_documented() -> None:
    """Pasch is documented as outside polynomial (L2) methods."""
    assert "pasch" in GENERIC_GAPS
    assert generic_witness("pasch") is None


def test_build_site_docs(tmp_path: Path) -> None:
    """Site generation writes foundations, showcase, and catalog trees."""
    from geometor.codes.present import build_site_docs

    counts = build_site_docs(docsrc_dir=tmp_path)
    assert counts["cards"] == 12
    assert counts["showcase"] == 5
    assert (tmp_path / "foundations" / "index.rst").exists()
    assert (tmp_path / "foundations" / "_atlas.inc").read_text(encoding="utf-8").count("codes-atlas-data") == 2
    assert (tmp_path / "foundations" / "cards" / "leaneuclid.rst").exists()
    assert (tmp_path / "showcase" / "pasch.rst").exists()
    catalog = (tmp_path / "catalog" / "index.rst").read_text(encoding="utf-8")
    assert "codes-catalog-data" in catalog
    assert not (tmp_path / "principles").exists()
