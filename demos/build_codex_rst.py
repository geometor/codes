"""Compile data-driven RST chapters (`syntax/`, `rosetta/`, `opus/`) from `resources/*.json`."""

from __future__ import annotations

from pathlib import Path
import re
import sys

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT / "src") not in sys.path:
    sys.path.insert(0, str(REPO_ROOT / "src"))

from geometor.codes.registry import CodesRegistry, RosettaBenchmark  # noqa: E402

DOCSRC = REPO_ROOT / "docsrc"

STATUS_BADGE: dict[str, str] = {
    "native": "**native**",
    "derived": "derived",
    "partial": "*partial*",
    "broken": "**BROKEN**",
    "absent": "—",
}

_BACKTICK_RE = re.compile(r"`([^`\n]+)`")


def _esc_plain(segment: str) -> str:
    return (
        segment.replace("\\", "\\\\")
        .replace("|", "\\|")
        .replace("*", "\\*")
        .replace("_", "\\_")
        .replace("`", "\\`")
    )


def _esc_rst(text: str) -> str:
    """Escape plain-text JSON prose for RST while turning balanced `` `code` `` into `` ``code`` ``."""
    parts = _BACKTICK_RE.split(text)
    out: list[str] = []
    for idx, part in enumerate(parts):
        if idx % 2 == 1:
            out.append(f"``{part}``")
        else:
            out.append(_esc_plain(part))
    return "".join(out)


def _h(title: str, char: str, overline: bool = False) -> str:
    bar = char * len(title)
    if overline:
        return f"{bar}\n{title}\n{bar}"
    return f"{title}\n{bar}"


def build_syntax_page(reg: CodesRegistry) -> None:
    """Write ``docsrc/syntax/index.rst`` combining narrative field guide + 60-symbol lexicon."""
    lines: list[str] = [
        ":navigation: header",
        ":order: 20",
        "",
        ".. _syntax-index:",
        "",
        _h("Syntax Field Guide & Symbol Decoder", "=", overline=True),
        "",
        "To a working geometer or Python engineer, opening a file in ``LeanEuclid``, ``GeoCoq``, ``mathlib4``, ``AlphaGeometry``, ``kingdon``, or :person:`Oliver Byrne <byrne>`'s 1847 *Coloured Euclid* can feel like reading cuneiform. Symbols like ``-ᵥ``, ``(2 : ℤ) • ∡``, ``|(a─b)|``, ``Bet``, ``FSC``, ``eqangle``, ``&``, ``>>``, and ``::`` compress entire philosophical commitments into two or three keystrokes.",
        "",
        "This Field Guide decodes every strange symbol from first principles, pairs each syntactic family with an exact ``geometor.model`` ``.euclid-graphic`` diagram, and concludes with the complete **60-Symbol Master Decoder Reference**.",
        "",
        _h("1. Pointer Dereferencing vs. Byrne's Chromatic Value-Tokens", "-"),
        "",
        "The deepest syntactic divide in the history of geometry is **how prose refers to a geometric locus**:",
        "",
        "* **Symbolic Pointer / Identifier Binding** (Euclid, ``LeanEuclid``, ``GeoCoq``, ``mathlib4``, ``AlphaGeometry``, ``geometor.model``): Points are bound to alphanumeric identifiers (``A``, ``B``, ``C``), and higher-dimensional objects are addressed indirectly as compound pointer expressions (``Segment(A, B)``, ``|(a─b)|``, ``∠ p₁ p₂ p₃``). This scales to arbitrary complexity and plain-text verification, but forces the human reader to perform constant *visual pointer-chasing* between prose text and diagram labels.",
        "* **Pointer-Free Chromatic Value-Tokens** (:ref:`Byrne 1847 / Rougeux 2018 <system-byrne-1847>`): :person:`Oliver Byrne <byrne>` eliminated vertex letters across Books I–VI (:cite:`Byrne1847`), embedding miniature colored segments ``[━━]``, angle wedges ``[◣]``, squares ``[□]``, and circles ``[○]`` directly as *r-values* inside vertical ``Given`` / ``To Prove`` / ``Construction`` / ``Proof`` equations (with Oughtred's ``::`` proportion and Rahn's ``∴`` discharge). Similarly, 2D :term:`Projective Geometric Algebra` (``PGA``) manipulates whole line blades ``l1 ^ l2`` without referencing vertex coordinates.",
        "* **GEOMETOR's Bidirectional Synthesis** (``:g:`` :math:`\\leftrightarrow` ``data-ref``): Following :person:`Nicholas Rougeux <rougeux>`'s interactive web edition (:cite:`Rougeux2018`), GEOMETOR's ``:g:`` role (e.g., :g:`[ A B ]`, :g:`( A B )`, :g:`F`) retains exact symbolic identifiers while illuminating the matching SVG locus on hover—uniting unlimited symbolic arity with zero-dereference visual perception.",
        "",
        _h("2. Dependent Type Binders & Logical Quantifiers (Lean 4 & Coq)", "-"),
        "",
        "Interactive theorem provers (``LeanEuclid``, ``mathlib4``, ``GeoCoq``) use the **Curry–Howard correspondence**: a theorem is a *type*, and a proof is a *functional program* constructing an inhabitant of that type.",
        "",
        "* **Explicit vs. Implicit vs. Typeclass Binders**:",
        "  - ``(a b : Point)`` — **Explicit arguments** you pass by hand when applying a lemma.",
        "  - ``{V P : Type*}`` — **Implicit arguments** inferred automatically by unification from later arguments.",
        "  - ``[NormedAddTorsor V P]`` (Lean 4) or ``Context `{TnEQD : Tarski_neutral_dimensionless_with_decidable_point_equality}`` (Coq) — **Typeclass instances** synthesized automatically in the background to endow ``P`` with geometric structure.",
        "* **Quantifiers & Connectives**: ``∀`` / ``forall`` introduces arbitrary givens; ``∃`` / ``exists`` demands an explicit constructive witness (unless bypassed via ``Classical.choose``); ``→`` / ``->`` chains hypotheses to conclusions; ``∧`` / ``/\\`` bundles conjunctions; ``¬`` / ``~`` negates degeneracies such as ``¬ Col A B C``.",
        "",
        _h("3. Diagrammatic System E & Topological Root Selectors", "-"),
        "",
        "When a line meets a circle or two circles meet, algebra yields a degree-2 quadratic equation with **two roots**. How does a formal language pick the right one without floating-point coordinates?",
        "",
        ".. figure:: /_static/figures/02-topological-selectors.svg",
        "   :align: center",
        "   :width: 100%",
        "",
        "   **Figure 2 — 1-to-1 Isomorphism Between System E Rules and ``geometor.model`` Selectors**: ``side_of=(A, B, +1)`` selects :g:`F` vs. :g:`E`; ``between=(A, B)`` selects midpoint :g:`M`; ``beyond=(A, B)`` and ``beyond=(B, A)`` select the exterior diameter extensions :g:`R2` and :g:`R1` on :g:`[ A B ]`.",
        "",
        "In ``LeanEuclid`` (:cite:`AvigadDeanMumma2009`, :cite:`Murphy2024`), ``SystemE/Theory/Constructions/Intersections.lean`` provides seven constructive rules (``intersect_circles_same_side``, ``intersect_circles_opposing_sides``, ``intersect_line_circle_between``, ``intersect_line_circle_extending``), while linear metric terms are written ``|(a─b)|`` (length), ``∠(a:b:c)`` (angle), ``∟`` (right angle), and ``△(a:b:c)`` (area). ``geometor.model.intersect`` implements the exact algebraic counterparts via ``signed_area2`` and dot-product ordering—without ``LeanEuclid``'s unverified ``SMT_VERIF`` axiom!",
        "",
        _h("4. Tarski's Point-Only Predicates (GeoCoq)", "-"),
        "",
        "In :person:`Alfred Tarski <tarski>`'s minimalist language (:cite:`Schwabhauser1983`, :cite:`Boutry2019`), **lines, circles, and angles do not exist as types**. Every geometric statement is built from points (``Tpoint``) and two predicates:",
        "",
        "* ``Bet A B C`` — *Non-strict* collinear betweenness (``Bet A A B`` is always true!). Collinearity ``Col A B C`` is simply ``Bet A B C \\/ Bet B C A \\/ Bet C A B``.",
        "* ``Cong A B C D`` — Segment ``AB`` is congruent to ``CD``.",
        "* ``Per A B C`` — Right angle ``∠ABC`` defined **without angles**: there exists ``C'`` such that ``B`` is the midpoint of ``C`` and ``C'`` and ``Cong A C A C'``!",
        "* ``FSC`` — Tarski's angle-free :term:`Five-Segment Configuration` replacing Euclid's SAS (``I.4``).",
        "",
        ".. figure:: /_static/figures/03-tarski-five-segment.svg",
        "   :align: center",
        "   :width: 100%",
        "",
        "   **Figure 3 — Tarski's Point-Only World**: Non-strict ``Bet`` along :g:`[ A C ]`, angle-free right angle ``Per D B C`` via reflected witness :g:`C1`, and the ``FSC`` transmission of congruence to the fifth segment.",
        "",
        _h("5. Affine Torsors, Directed Angles & Rational Spreads", "-"),
        "",
        "``mathlib4`` separates points ``P`` from vectors ``V`` via ``NormedAddTorsor V P``: subtracting two points ``p₁ -ᵥ p₂`` yields a vector in ``V``, while ``v +ᵥ p`` translates a point by a vector (note ``p₁ + p₂`` is a type error!). For angles, ``mathlib4`` distinguishes unoriented ``∠ p₁ p₂ p₃ ∈ [0, π]`` from oriented ``∡ x y z ∈ ℝ / 2πℤ``, using twice-angles ``(2 : ℤ) • ∡ x y z`` to represent **directed line angles modulo π**—the exact same group used by ``eqangle`` in ``AlphaGeometry``/``JGEX``! In ``geometor.model`` and ``geometor.wildberger``, both transcendental angles and square-root norms are replaced by rational :term:`quadrance` :math:`Q` and :term:`spread` :math:`s = \\sin^2\\theta`.",
        "",
        ".. figure:: /_static/figures/04-torsor-oangle-spread.svg",
        "   :align: center",
        "   :width: 100%",
        "",
        "   **Figure 4 — Torsor Subtraction, Directed Twice-Angles & Rational Spreads** on cyclic configuration :g:`A`, :g:`B`, :g:`C`, :g:`D` around circle :g:`( O A )`.",
        "",
        _h("6. Olympiad Clause Stanzas & Coordinate-Free Area Elimination", "-"),
        "",
        "``AlphaGeometry`` and ``Newclid`` read compact 1-line problem clauses (``premises ? goal``) backed by 5-line macro stanzas in ``defs.txt`` (``signature``, ``dependency``, ``non-degeneracy``, ``postconditions``, ``compass realization``). Watch out for two forensic traps we uncovered in ``alphageometry``: post-semicolon clauses without a ``x :`` prefix in ``defs.txt`` are **silently dropped** by ``Graph.add_clause``, and ``RatioTable.add_const_ratio`` in ``ar.py:425-431`` encodes :math:`m \\log|s_1| = n \\log|s_2|` instead of :math:`|s_1|/|s_2| = m/n`!",
        "",
        "Meanwhile, ``JGEX``'s coordinate-free :term:`Area Method` eliminates constructed points backward from signed parallel ratios :math:`r`, signed areas :math:`S_{ABC}`, and :term:`Pythagoras difference` :math:`P_{ABC} = AB^2 + BC^2 - AC^2` using the **Co-Side Theorem**: :math:`PM / QM = S_{PAB} / S_{QAB}`.",
        "",
        ".. figure:: /_static/figures/05-area-method-elimination.svg",
        "   :align: center",
        "   :width: 100%",
        "",
        "   **Figure 5 — Coordinate-Free Area & Pythagoras Elimination**: Intersection :g:`M` of :g:`[ A B ]` and :g:`[ P Q ]` is eliminated linearly via signed area ratio :math:`S_{PAB} / S_{QAB}`, while foot :g:`H` is eliminated via Pythagoras ratio :math:`P_{PAB} / P_{ABA}`.",
        "",
        _h("7. Clifford Blades (PGA/CGA) & Homogeneous CP^2 Matrices", "-"),
        "",
        "In ``kingdon``'s 2D :term:`Projective Geometric Algebra` (``Algebra(2, 0, 1)``), lines are grade-1 vectors, points are grade-2 bivectors, ``^`` is **meet**, and ``&`` is **join**. In 2D :term:`Conformal Geometric Algebra` (``Algebra(3, 1)``), points lift onto the 4D null cone :math:`P = x e_1 + y e_2 + \\tfrac{1}{2}(x^2+y^2)n_\\infty + n_o`, so ``P1 ^ P2 ^ P3`` is the circle through three points, ``-2*(kappa | P)`` is Steiner power, ``kappa1 - kappa2`` is the radical axis, and ``C >> P`` is circle inversion! *(Critical warning: in ``galgebra``, ``>>`` is the commutator product, ``&`` is missing, and ``.dual()`` crashes when :math:`I^2 = 0`!)* In ``CindyJS``'s :math:`\\mathbb{CP}^2`, ``cross(u, v)`` computes both join and meet, ``C * p`` is the polar line, and ``adjoint3(C) * l`` is the pole.",
        "",
        ".. figure:: /_static/figures/06-pga-cga-inversion.svg",
        "   :align: center",
        "   :width: 100%",
        "",
        "   **Figure 6 — Conformal Circle Inversion & Pole–Polar Reciprocity**: External point :g:`P`, tangent touchpoints :g:`T1` and :g:`T2` on circle :g:`( O R0 )`, polar line :g:`[ T1 T2 ]`, inverse point :g:`P1` (``C >> P``), and harmonic range :math:`\\operatorname{CR}(R_-, R_+; P_1, P) = -1`.",
        "",
        _h("8. Master 60-Symbol Decoder Reference", "-"),
        "",
    ]

    categories: list[str] = []
    for entry in reg.lexicon:
        if entry.category not in categories:
            categories.append(entry.category)

    for cat in categories:
        lines.extend(["", _h(cat, "~"), ""])
        lines.extend(
            [
                ".. list-table::",
                "   :widths: 16 16 26 22 20",
                "   :header-rows: 1",
                "",
                "   * - Symbol / Token",
                "     - Systems",
                "     - Pronunciation & Plain Meaning",
                "     - Formal Semantics & Example",
                "     - GEOMETOR Equivalent",
            ]
        )
        for entry in reg.lexicon:
            if entry.category != cat:
                continue
            sys_str = ", ".join(f"``{s}``" for s in entry.system_ids)
            ex_clean = " / ".join(s.strip() for s in entry.example_snippet.splitlines() if s.strip())
            lines.extend(
                [
                    f"   * - ``{entry.symbol}``",
                    f"     - {sys_str}",
                    f"     - *{_esc_rst(entry.pronunciation)}* — {_esc_rst(entry.plain_meaning)}",
                    f"     - {_esc_rst(entry.formal_semantics)} Example: ``{ex_clean}``",
                    f"     - {_esc_rst(entry.geometor_equivalent)}",
                ]
            )

    out = DOCSRC / "syntax" / "index.rst"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def _build_single_rosetta(reg: CodesRegistry, bench: RosettaBenchmark) -> None:
    title = f"Benchmark {bench.number}: {bench.title}"
    lines: list[str] = [
        f":order: {bench.number}",
        "",
        f".. _rosetta-{bench.id}:",
        "",
        _h(title, "=", overline=True),
        "",
        f"* **Canonical GEOMETOR Signature**: ``{bench.geometor_signature}``",
        f"* **Classical Citation**: *{_esc_rst(bench.euclid_ref)}*",
        f"* **Core Phenomenon**: {_esc_rst(bench.geometric_essence)}",
        "",
    ]
    if bench.figure_svg:
        lines.extend(
            [
                f".. figure:: /_static/figures/{bench.figure_svg}",
                "   :align: center",
                "   :width: 100%",
                "",
                f"   Exact float-free ``geometor.model`` construction illustrating **{bench.title}** (``{bench.geometor_signature}``).",
                "",
            ]
        )

    lines.extend(
        [
            _h("Cross-System Revelation Matrix", "-"),
            "",
            ".. list-table::",
            "   :widths: 20 40 40",
            "   :header-rows: 1",
            "",
            "   * - System",
            "     - What This Encoding Reveals",
            "     - What This Encoding Hides",
        ]
    )
    for sys_prof in reg.systems:
        imp = bench.implementations[sys_prof.id]
        lines.extend(
            [
                f"   * - **{sys_prof.name}**",
                f"     - {_esc_rst(imp.reveals)}",
                f"     - {_esc_rst(imp.hides)}",
            ]
        )

    lines.extend(["", _h("Side-by-Side Formal & Visual Implementations (11 Systems)", "-"), ""])
    for sys_prof in reg.systems:
        imp = bench.implementations[sys_prof.id]
        sub = f"{sys_prof.name} (``{sys_prof.id}``)"
        lines.extend(
            [
                _h(sub, "~"),
                "",
                f"*Source / Reference*: ``{imp.source_ref}``",
                "",
                f".. code-block:: {imp.language}",
                "",
            ]
        )
        for cline in imp.code.splitlines():
            lines.append(f"   {cline}" if cline else "")
        lines.extend(
            [
                "",
                f"* **Reveals**: {_esc_rst(imp.reveals)}",
                f"* **Hides**: {_esc_rst(imp.hides)}",
                "",
            ]
        )

    out = DOCSRC / "rosetta" / f"{bench.id}.rst"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_rosetta_pages(reg: CodesRegistry) -> None:
    """Write ``docsrc/rosetta/index.rst`` and all 7 side-by-side Rosetta Stone pages."""
    lines: list[str] = [
        ":navigation: header",
        ":order: 40",
        "",
        ".. _rosetta-index:",
        "",
        _h("Rosetta Stone Benchmarks", "=", overline=True),
        "",
        "Abstract descriptions of formal languages only go so far. To expose the true ontology, elegance, verbosity, and expressiveness ceilings of each architecture, we encode **seven canonical geometric constructions and theorems** side-by-side across all **11 surveyed systems** (``77`` annotated implementations) paired with exact ``geometor.model`` ``.euclid-graphic`` SVGs.",
        "",
        ".. list-table::",
        "   :widths: 8 28 30 34",
        "   :header-rows: 1",
        "",
        "   * - #",
        "     - Benchmark",
        "     - GEOMETOR Signature",
        "     - Architectural Stress Test",
    ]
    for b in reg.benchmarks:
        lines.extend(
            [
                f"   * - {b.number}",
                f"     - :ref:`{b.title} <rosetta-{b.id}>`",
                f"     - ``{b.geometor_signature}``",
                f"     - {_esc_rst(b.geometric_essence)}",
            ]
        )

    lines.extend(["", ".. toctree::", "   :maxdepth: 1", "   :hidden:", ""])
    for b in reg.benchmarks:
        lines.append(f"   {b.id}")
        _build_single_rosetta(reg, b)

    out = DOCSRC / "rosetta" / "index.rst"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_opus_page(reg: CodesRegistry) -> None:
    """Write ``docsrc/opus/index.rst`` with the 69-topic x 11-system Opus Matrix."""
    counts = reg.opus_coverage_counts()
    lines: list[str] = [
        ":navigation: header",
        ":order: 50",
        "",
        ".. _opus-index:",
        "",
        _h("Opus Coverage Matrix (69 Topics x 11 Systems)", "=", overline=True),
        "",
        "What portion of the classical and modern geometric canon—the **Opus**—has actually been formalized across interactive theorem provers, Olympiad deduction engines, Clifford algebras, visual pseudocodes, and symbolic CAS libraries? Below is our complete **69-topic across 8 domains** audit (``759`` cells), using canonical ``snake_case`` identifiers aligned with GEOMETOR's *Principles of Geometry* (``elements`` 2.0).",
        "",
        _h("Quantitative Coverage Scoreboard (Across 69 Canonical Topics)", "-"),
        "",
        ".. list-table::",
        "   :widths: 28 14 14 14 14 16",
        "   :header-rows: 1",
        "",
        "   * - System",
        "     - Native",
        "     - Derived",
        "     - Partial",
        "     - Broken",
        "     - Absent",
    ]
    for s in reg.systems:
        c = counts[s.id]
        lines.extend(
            [
                f"   * - **{s.name}** (``{s.id}``)",
                f"     - **{c['native']}**",
                f"     - {c['derived']}",
                f"     - {c['partial']}",
                f"     - {c['broken']}",
                f"     - {c['absent']}",
            ]
        )

    lines.extend(
        [
            "",
            _h("Six Structural Blind Spots Exposed by the Opus Matrix", "-"),
            "",
            "1. **The Golden Ratio & Polyhedral Blind Spot (Domain 8)**: Across ``LeanEuclid``, ``GeoCoq``, ``mathlib4`` Geometry, ``AlphaGeometry``, and ``Newclid``, division in extreme and mean ratio (:math:`\\phi`, Euclid ``II.11`` & ``VI.30``), the 5-step vesica golden chain, and the five Platonic solids (``Book XIII``) have **zero** geometric theorems—whereas :person:`Oliver Byrne <byrne>` (``1847``) formalized ``II.11``, ``IV.10–11``, and ``VI.30`` in primary colors, and GEOMETOR (``model``, ``fundamentals``, ``divine``, ``pacioli``, ``kepler``, ``euclid``) treats :math:`\\mathbb{Q}(\\phi)` as foundational DNA.",
            "2. **The General Conic Desert (Domain 6)**: Among all 10 external systems, **only ``CindyJS``** represents general rotated ellipses, parabolas, and hyperbolas uniformly via :math:`3\\times 3` symmetric matrices and Plücker 5-point pencils (``ConicBy5``). ``sympy.geometry`` lacks ``Hyperbola`` altogether and raises ``NotImplementedError`` on rotated ``Ellipse``.",
            "3. **The Coaxial & Inversive Gap (Domain 4)**: ``GeoCoq`` (``4,671`` lemmas) and ``sympy.geometry`` have **zero** circle power, radical axis, inversion, or pole–polar support, and even ``mathlib4`` (which shines on ``Sphere.power`` and ``PolePolar``) omits ``radicalAxis``! Meanwhile, 2D CGA (``kingdon``) expresses radical axis as ``kappa1 - kappa2`` and circle inversion as ``C >> P``.",
            "4. **The Projective Cross-Ratio & Pappus Wall (Domain 6)**: ``mathlib4`` and ``sympy.geometry`` both lack ``cross_ratio``, ``Pappus``, ``Desargues``, and ``Menelaus``, while bare ``AlphaGeometry`` ``DD+AR`` cannot prove Pappus without auxiliary parallel lines.",
            "5. **Triangle Centers Beyond Textbook Classics (Domain 5)**: External systems top out between ``0`` centers (``LeanEuclid``), ``2`` (``Byrne``), ``4`` (``GeoCoq``), and ``6`` (``mathlib4``, ``AlphaGeometry``), and ``sympy.geometry`` ``1.14.0`` has a **live double bug in ``Triangle.excenters``**—leaving ``geometor.etc`` (``X(1)``–``X(53144)``) unmatched.",
            "6. **Operational Construction Complexity (Domain 7)**: Zero external systems measure :person:`Émile Lemoine <lemoine>`'s *Géométrographie* (``R1, R2, C1, C2, C3``), positioning ``geometor.model`` + ``geometor/lemoine`` to own constructive complexity analysis.",
            "",
        ]
    )

    short_cols = (
        ("leaneuclid", "LeanEuc"),
        ("geocoq", "GeoCoq"),
        ("mathlib4", "Mathlib"),
        ("alphageometry", "AlphaG"),
        ("newclid", "Newclid"),
        ("jgex", "JGEX"),
        ("pga_cga", "PGA/CGA"),
        ("cindyjs", "CindyJS"),
        ("sympy_geometry", "SymPy"),
        ("byrne_1847", "Byrne"),
        ("geometor_model", "GEOMETOR"),
    )

    for dom in reg.domains:
        lines.extend(["", _h(dom.title, "-"), "", _esc_rst(dom.summary), ""])
        lines.extend(
            [
                ".. list-table::",
                "   :header-rows: 1",
                "",
                "   * - Canonical Topic (``snake_case``)",
            ]
        )
        for _, label in short_cols:
            lines.append(f"     - {label}")
        for t in reg.topics:
            if t.domain_id != dom.id:
                continue
            lines.append(f"   * - **{_esc_rst(t.title)}** (``{t.id}``)")
            for sys_id, _ in short_cols:
                cell = t.coverage[sys_id]
                badge = STATUS_BADGE[cell.status]
                lines.append(f"     - {badge}: {_esc_rst(cell.ref)}")
        lines.append("")

    out = DOCSRC / "opus" / "index.rst"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    """Generate data-backed RST chapters from ``CodesRegistry``."""
    reg = CodesRegistry()
    build_syntax_page(reg)
    build_rosetta_pages(reg)
    build_opus_page(reg)
    print("Compiled syntax/index.rst, rosetta/*.rst (8 files), and opus/index.rst.")


if __name__ == "__main__":
    main()
