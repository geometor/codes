"""Tests for lexicon, miners, discovery fingerprinting, exact verification, and CLI."""

from __future__ import annotations

import json
from pathlib import Path

from geometor.codes.cli import run_cli
from geometor.codes.context import ContextManifest
from geometor.codes.discover import (
    Atom,
    fingerprint_form,
    load_catalog,
)
from geometor.codes.lexicon import Lexicon, audit_lexicon
from geometor.codes.mine.ag import parse_defs, parse_rules
from geometor.codes.mine.euclid import mine_euclid
from geometor.codes.mine.lean import parse_lean_file
from geometor.codes.mine.newclid import parse_newclid_rules
from geometor.codes.mine.schema import Decl, MinedSystem, load_snapshot, write_snapshot
from geometor.codes.mine.sympy_geo import mine_sympy
from geometor.codes.verify import verify_pilot


def test_lexicon_valid_and_unique() -> None:
    """Lexicon validates and resolves cross-system aliases."""
    lex = Lexicon.load()
    assert lex.validate() == []
    assert lex.resolve("alphageometry", "foot").name == "perpendicular_foot"
    assert lex.resolve("elements", "bisect_segment").name == "midpoint"
    assert lex.resolve("gibert", "g").name == "isogonal_conjugate"


def test_lexicon_audit_clean_and_covers_etc() -> None:
    """Audit covers all etc ops functions and resolves SymPy aliases."""
    rep = audit_lexicon()
    assert rep.problems == []
    assert rep.etc_missing == []
    assert rep.unresolved_sympy == []


def test_ag_miner_fixtures(tmp_path: Path) -> None:
    """AlphaGeometry rules and defs parsers handle fixture files."""
    rules = tmp_path / "rules.txt"
    rules.write_text("cong O A O B, ncoll O A B => eqangle O A A B A B O B\n", encoding="utf-8")
    r_decls = parse_rules(rules, tmp_path)
    assert len(r_decls) == 1
    assert r_decls[0].premises == ["cong O A O B", "ncoll O A B"]
    assert r_decls[0].conclusions == ["eqangle O A A B A B O B"]

    defs = tmp_path / "defs.txt"
    defs.write_text(
        "midpoint x a b\nx : a b\na b = diff a b\nx : coll x a b, cong x a x b\nmidpoint a b\n",
        encoding="utf-8",
    )
    d_decls = parse_defs(defs, tmp_path)
    assert len(d_decls) == 1
    assert d_decls[0].name == "midpoint"
    assert d_decls[0].kind == "construction"


def test_newclid_miner_fixture(tmp_path: Path) -> None:
    """Newclid AST miner extracts Rule definitions without importing."""
    py = tmp_path / "all_rules.py"
    py.write_text(
        'R13_ISO = Rule(id="r13", description="Iso", premises_txt=("cong O A O B",), conclusions_txt=("eqangle O A A B A B O B",))\n'
        "DEACTIVATED_RULES = set()\n",
        encoding="utf-8",
    )
    decls = parse_newclid_rules(py, tmp_path)
    assert len(decls) == 1
    assert decls[0].name == "r13"
    assert decls[0].extra["ag_rule"] == "r13"


def test_lean_miner_fixture(tmp_path: Path) -> None:
    """LeanEuclid parser extracts theorem, Euclid ref, and apply trace."""
    book = tmp_path / "Book"
    book.mkdir()
    prop = book / "Prop05.lean"
    prop.write_text(
        "namespace Elements.Book1\n"
        "theorem proposition_5 : ∀ (a b c : Point) (AB BC AC : Line),\n"
        "  formTriangle a b c AB BC AC ∧ (|(a─b)| = |(a─c)|) → (∠ a:b:c = ∠ a:c:b) :=\n"
        "by\n"
        "  euclid_intros\n"
        "  euclid_apply (proposition_4 a b c) as x\n"
        "  euclid_finish\n"
        "end Elements.Book1\n",
        encoding="utf-8",
    )
    decls = parse_lean_file(prop, tmp_path, tmp_path)
    assert len(decls) == 1
    assert decls[0].id == "Elements.Book1.proposition_5"
    assert decls[0].extra["euclid"] == "I.5"
    assert decls[0].uses == ["proposition_4"]


def test_euclid_miner_fixture(tmp_path: Path) -> None:
    """Euclid miner classifies items and marks books not yet in canon."""
    enun = tmp_path / "enunciations.json"
    enun.write_text(
        json.dumps({
            "I.def": "Book I Definitions",
            "I.1": "On a given finite straight line to construct an equilateral triangle.",
            "V.1": "If there be any number of magnitudes...",
        }),
        encoding="utf-8",
    )
    mined = mine_euclid(enun, tmp_path, not_yet_in_canon=("V",))
    assert len(mined.decls) == 2
    assert mined.decls[0].kind == "problem"
    assert mined.decls[0].extra["in_canon"] is True
    assert mined.decls[1].extra["in_canon"] is False


def test_sympy_miner_and_snapshot_determinism(tmp_path: Path) -> None:
    """SymPy miner runs and JSONL snapshots are byte-identical regardless of input order."""
    mined = mine_sympy()
    assert len(mined.decls) > 100
    d1 = tmp_path / "s1"
    d2 = tmp_path / "s2"
    p1 = write_snapshot(MinedSystem(system="test", decls=[Decl(system="test", id="b", name="b", kind="rule"), Decl(system="test", id="a", name="a", kind="rule")]), d1)
    p2 = write_snapshot(MinedSystem(system="test", decls=[Decl(system="test", id="a", name="a", kind="rule"), Decl(system="test", id="b", name="b", kind="rule")]), d2)
    assert p1.read_text() == p2.read_text()
    assert [d.id for d in load_snapshot("test", d1)] == ["a", "b"]


def test_fingerprint_invariant_under_relabeling() -> None:
    """Structural fingerprint is invariant under point relabeling and atom permutation."""
    fp1 = fingerprint_form(
        (Atom("cong", ("O", "A", "O", "B")), Atom("ncoll", ("O", "A", "B"))),
        (Atom("eq_angle", ("O", "A", "A", "B", "A", "B", "O", "B")),),
    )
    fp2 = fingerprint_form(
        (Atom("ncoll", ("Z", "X", "Y")), Atom("cong", ("Z", "X", "Z", "Y"))),
        (Atom("eq_angle", ("Z", "X", "X", "Y", "X", "Y", "Z", "Y")),),
    )
    assert fp1 == fp2
    assert fp1 != ""


def test_saved_catalog_standalone_and_complete() -> None:
    """Saved catalog loads without _refs and leaves zero unassigned base items."""
    ctx = ContextManifest.load()
    assert len(ctx.by_role("base")) == 6
    assert len(ctx.by_role("linked")) == 6
    cat = load_catalog()
    assert cat.stats["unassigned_items"] == 0
    assert cat.stats["principles"] > 100
    iso = cat.by_id("isosceles_base_angles")
    assert iso is not None
    assert {m.system for m in iso.members} >= {"euclid", "leaneuclid", "alphageometry", "newclid"}


def test_pilot_exact_verification() -> None:
    """All 20 pilot witness models verify with zero floats, plus 3 explicit gaps."""
    results = verify_pilot()
    verified = [r for r in results if r.status == "verified"]
    gaps = [r for r in results if r.status == "gap"]
    assert len(verified) == 20
    assert len(gaps) == 3


def test_cli_smoke() -> None:
    """CLI commands exit cleanly against packaged resources."""
    assert run_cli(["lexicon", "search", "midpoint"]) == 0
    assert run_cli(["principle", "pythagorean"]) == 0
    assert run_cli(["coverage"]) == 0
    assert run_cli(["search", "thales"]) == 0
