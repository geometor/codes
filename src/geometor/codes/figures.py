"""Exact `geometor.model` SVG figure generators for GEOMETOR Codes.

Every model is constructed strictly with `Model(..., auto_intersect=False)` and
100% exact SymPy coordinates (zero `sp.Float`), verified symbolically via
Rational Trigonometry (`quadrance`, `line_spread`, `vertex_spread`, `cross_ratio`),
and rendered as an interactive `.euclid-graphic` SVG in `docsrc/_static/figures/`.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import sympy as sp
import sympy.geometry as spg
from geometor.model import (
    Model,
    cross_ratio,
    is_harmonic,
    line_spread,
    quadrance,
    vertex_spread,
)
from geometor.model.algebra import zero_test
from geometor.model.invariants import signed_area2

from geometor.codes.render import render_svg


def _assert_scalar(actual: sp.Expr, expected: sp.Expr | int) -> None:
    """Verify exact symbolic equality `actual == expected` via `zero_test`.

    Args:
        actual: Exact SymPy expression produced by the geometric construction.
        expected: Target exact SymPy expression or integer.

    Raises:
        AssertionError: If `actual - expected` is symbolically non-zero.
    """
    diff = sp.sympify(actual) - sp.sympify(expected)
    if not zero_test(diff):
        msg = f"Exact symbolic mismatch: {actual} != {expected} (diff={sp.simplify(diff)})"
        raise AssertionError(msg)


@dataclass(frozen=True)
class FigureSpec:
    """Metadata and builder callable for a comparative ``.euclid-graphic`` figure."""

    slug: str
    title: str
    builder: Callable[[], tuple[Model, list[dict[str, object]]]]


def _midpoint_via_vesica(
    model: Model,
    p1: spg.Point,
    p2: spg.Point,
    mid_id: str,
    bisector_id: str = "",
    keep_bisector: bool = False,
) -> tuple[spg.Point, spg.Line]:
    """Construct exact midpoint and perpendicular bisector by pure compass & straightedge.

    Args:
        model: Target `Model`.
        p1: First endpoint.
        p2: Second endpoint.
        mid_id: Identifier for the midpoint.
        bisector_id: Optional identifier for the perpendicular bisector line.
        keep_bisector: If `True`, keep the perpendicular bisector visible (non-guide).

    Returns:
        Tuple `(midpoint, bisector_line)`.
    """
    with model.subconstruction(f"bisect_{mid_id}") as scope:
        base_line = model.construct_line(p1, p2, classes=["guide"], guide=True)
        c1 = model.construct_circle(p1, p2, classes=["guide"], guide=True)
        c2 = model.construct_circle(p2, p1, classes=["guide"], guide=True)
        e_pt = model.intersect(c1, c2, side_of=(p1, p2, 1), guide=True)
        f_pt = model.intersect(c1, c2, side_of=(p1, p2, -1), guide=True)
        bis_cls = ["bisector"] if keep_bisector else ["guide"]
        bis = model.construct_line(
            e_pt,
            f_pt,
            classes=bis_cls,
            ID=bisector_id,
            guide=not keep_bisector,
        )
        mid = model.intersect(
            base_line,
            bis,
            between=(p1, p2),
            ID=mid_id,
            classes=["midpoint"],
        )
        if keep_bisector:
            scope.keep(mid, bis)
        else:
            scope.keep(mid)
        return mid, bis


def build_01_seven_ontologies() -> tuple[Model, list[dict[str, object]]]:
    """Build Figure 1: The 7 Ontologies of a Line & Circle (`I.1` Vesica Locus).

    Returns:
        Tuple of exact `Model` and SVG callout annotations.
    """
    m = Model("seven_ontologies", auto_intersect=False, enable_logging=False)
    a = m.set_point(0, 0, classes=["given"], ID="A")
    b = m.set_point(2, 0, classes=["given"], ID="B")
    l_ab = m.construct_line(a, b, ID="[ A B ]")
    c_a = m.construct_circle(a, b, ID="( A B )")
    c_b = m.construct_circle(b, a, classes=["guide"], ID="( B A )", guide=True)
    f = m.intersect(c_a, c_b, side_of=(a, b, 1), classes=["result"], ID="F")
    s_af = m.construct_segment(a, f, ID="/ A F /")
    s_bf = m.construct_segment(b, f, ID="/ B F /")
    m.construct_polygon([a, b, f], ID="< A B F >")

    m.assert_equal((a, b), s_af, s_bf, by="I.1")
    _assert_scalar(quadrance(a, b), 4)
    _assert_scalar(vertex_spread(b, a, f), sp.Rational(3, 4))
    del l_ab

    anns: list[dict[str, object]] = [
        {"x": 1, "y": sp.Rational(5, 2), "text": "System E: F = intersect_same_side", "kind": "paradigm", "ref": "F"},
        {"x": -sp.Rational(3, 2), "y": sp.Rational(3, 2), "text": "Tarski: Cong A B A F /\\ Cong B A B F", "kind": "paradigm", "ref": "( A B )"},
        {"x": sp.Rational(7, 2), "y": sp.Rational(3, 2), "text": "Mathlib4: dist F A = dist A B", "kind": "paradigm", "ref": "/ B F /"},
        {"x": -sp.Rational(3, 2), "y": -sp.Rational(5, 4), "text": "2DCGA: C = P1 ^ P2 ^ P3", "kind": "paradigm", "ref": "( A B )"},
        {"x": sp.Rational(7, 2), "y": -sp.Rational(5, 4), "text": "CP^2: conic through I, J", "kind": "paradigm", "ref": "[ A B ]"},
        {"x": 1, "y": -sp.Rational(9, 4), "text": "GEOMETOR: Q(A,F)=Q(B,F)=4, s=3/4", "kind": "spread", "ref": "< A B F >"},
    ]
    return m, anns


def build_02_topological_selectors() -> tuple[Model, list[dict[str, object]]]:
    """Build Figure 2: Diagrammatic Selectors (`LeanEuclid` System E == `geometor.model`).

    Returns:
        Tuple of exact `Model` and SVG callout annotations.
    """
    m = Model("topological_selectors", auto_intersect=False, enable_logging=False)
    a = m.set_point(0, 0, classes=["given"], ID="A")
    b = m.set_point(2, 0, classes=["given"], ID="B")
    l_ab = m.construct_line(a, b, ID="[ A B ]")
    c_a = m.construct_circle(a, b, ID="( A B )")
    c_b = m.construct_circle(b, a, ID="( B A )")

    f = m.intersect(c_a, c_b, side_of=(a, b, 1), classes=["result"], ID="F")
    e = m.intersect(c_a, c_b, side_of=(a, b, -1), classes=["result"], ID="E")
    c = m.intersect(l_ab, c_a, other_than=b, classes=["target"], ID="C")
    d = m.intersect(l_ab, c_b, beyond=(a, b), classes=["target"], ID="D")
    l_ef = m.construct_line(e, f, classes=["bisector"], ID="[ E F ]")
    mid = m.intersect(l_ab, l_ef, between=(a, b), classes=["midpoint"], ID="M")

    m.assert_equal((a, mid), (mid, b), by="I.10")
    m.assert_perpendicular(l_ab, l_ef, at=mid, by="I.11")
    _assert_scalar(quadrance(a, mid), 1)
    _assert_scalar(line_spread(l_ab, l_ef), 1)
    _assert_scalar(quadrance(c, d), 36)

    anns: list[dict[str, object]] = [
        {"x": 1, "y": sp.Rational(12, 5), "text": "side_of=(A,B,+1) | sameSide", "kind": "paradigm", "ref": "F"},
        {"x": 1, "y": -sp.Rational(12, 5), "text": "side_of=(A,B,-1) | opposingSides", "kind": "paradigm", "ref": "E"},
        {"x": 1, "y": -sp.Rational(3, 5), "text": "between=(A,B)", "kind": "spread", "ref": "M"},
        {"x": 4, "y": sp.Rational(4, 5), "text": "beyond=(A,B)", "kind": "quadrance", "ref": "D"},
        {"x": -2, "y": sp.Rational(4, 5), "text": "other_than=B", "kind": "quadrance", "ref": "C"},
    ]
    return m, anns


def build_03_tarski_five_segment() -> tuple[Model, list[dict[str, object]]]:
    """Build Figure 3: Tarski's Point-Only `FSC` & Right-Angle `Per` via Midpoint.

    Returns:
        Tuple of exact `Model` and SVG callout annotations.
    """
    m = Model("tarski_five_segment", auto_intersect=False, enable_logging=False)
    a = m.set_point(-2, 0, classes=["given"], ID="A")
    b = m.set_point(0, 0, classes=["given"], ID="B")
    l_base = m.construct_line(a, b, classes=["guide"], ID="[ A B ]", guide=True)
    c_ba = m.construct_circle(b, a, classes=["guide"], guide=True)
    a_prime = m.intersect(l_base, c_ba, beyond=(a, b), classes=["midpoint"], ID="A1")
    c = m.set_point(4, 0, classes=["given"], ID="C")
    d = m.set_point(0, 3, classes=["result"], ID="D")

    m.construct_segment(a, c, classes=["axis"], ID="/ A C /")
    s_ad = m.construct_segment(a, d, ID="/ A D /")
    s_a1d = m.construct_segment(a_prime, d, classes=["guide"], ID="/ A1 D /")
    m.construct_segment(b, d, classes=["bisector"], ID="/ B D /")
    m.construct_segment(c, d, classes=["golden"], ID="/ C D /")
    m.construct_polygon([a, c, d], ID="< A C D >")

    # Tarski Per(A, B, D): B is midpoint of (A, A1) and Q(A, D) == Q(A1, D) == 13
    m.assert_equal((a, b), (b, a_prime), by="Midpoint")
    m.assert_equal(s_ad, s_a1d, by="Per")
    _assert_scalar(quadrance(a, d), 13)
    # 5th segment CD determined uniquely by (AB, BC, AD, BD): Q(C, D) = 16 + 9 = 25
    _assert_scalar(quadrance(c, d), 25)

    anns: list[dict[str, object]] = [
        {"x": 0, "y": -sp.Rational(4, 5), "text": "Bet A B C (collinear order)", "kind": "paradigm", "ref": "/ A C /"},
        {"x": -sp.Rational(9, 5), "y": sp.Rational(9, 5), "text": "Per A B D := Midpoint B A A1 /\\ Cong A D A1 D", "kind": "paradigm", "ref": "/ B D /"},
        {"x": sp.Rational(14, 5), "y": sp.Rational(9, 5), "text": "5th Segment: Q(C,D) = 25 (|CD|=5)", "kind": "spread", "ref": "/ C D /"},
    ]
    return m, anns


def build_04_torsor_oangle_spread() -> tuple[Model, list[dict[str, object]]]:
    """Build Figure 4: Affine Torsor `C -ᵥ A`, Directed `oangle` & Rational `spread`.

    Returns:
        Tuple of exact `Model` and SVG callout annotations.
    """
    m = Model("torsor_oangle_spread", auto_intersect=False, enable_logging=False)
    a = m.set_point(0, 0, classes=["given"], ID="A")
    b = m.set_point(4, 0, classes=["given"], ID="B")
    c = m.set_point(1, 3, classes=["given"], ID="C")

    l_ab = m.construct_line(a, b, classes=["guide"], guide=True)
    # Drop perpendicular from C to AB via circle centered at C through A
    with m.subconstruction("drop_perp_H") as scope:
        c_ca = m.construct_circle(c, a, classes=["guide"], guide=True)
        a2 = m.intersect(l_ab, c_ca, other_than=a, guide=True)
        h, l_ch = _midpoint_via_vesica(m, a, a2, "H", "[ C H ]", keep_bisector=True)
        scope.keep(h, l_ch)

    m.construct_segment(a, b, classes=["axis"], ID="/ A B /")
    m.construct_segment(a, c, classes=["golden"], ID="/ A C /")
    m.construct_segment(b, c, ID="/ B C /")
    m.construct_segment(c, h, classes=["altitude"], ID="/ C H /")
    m.construct_polygon([a, b, c], ID="< A B C >")

    m.assert_perpendicular(l_ab, l_ch, at=h, by="I.12")
    _assert_scalar(quadrance(a, b), 16)
    _assert_scalar(quadrance(a, c), 10)
    _assert_scalar(quadrance(b, c), 18)
    _assert_scalar(vertex_spread(b, a, c), sp.Rational(9, 10))
    _assert_scalar(line_spread(l_ab, l_ch), 1)

    anns: list[dict[str, object]] = [
        {"x": -sp.Rational(3, 5), "y": sp.Rational(8, 5), "text": "v = C -v A = (1, 3), Q=10", "kind": "paradigm", "ref": "/ A C /"},
        {"x": 2, "y": -sp.Rational(7, 10), "text": "u = B -v A = (4, 0), Q=16", "kind": "quadrance", "ref": "/ A B /"},
        {"x": sp.Rational(16, 5), "y": sp.Rational(11, 5), "text": "s(BAC) = 9/10 | S_A = 4 > 0", "kind": "spread", "ref": "< A B C >"},
        {"x": sp.Rational(9, 5), "y": 1, "text": "oangle mod 2pi vs eqangle mod pi", "kind": "paradigm", "ref": "/ C H /"},
    ]
    return m, anns


def build_05_area_method_elimination() -> tuple[Model, list[dict[str, object]]]:
    """Build Figure 5: Chou-Gao-Zhang Area-Method Elimination (`S_ABC` & `P_ABC`).

    Returns:
        Tuple of exact `Model` and SVG callout annotations.
    """
    m = Model("area_method_elimination", auto_intersect=False, enable_logging=False)
    a = m.set_point(0, 0, classes=["given"], ID="A")
    b = m.set_point(6, 0, classes=["given"], ID="B")
    c = m.set_point(2, 6, classes=["given"], ID="C")

    ma, _ = _midpoint_via_vesica(m, b, c, "Ma")
    mb, _ = _midpoint_via_vesica(m, a, c, "Mb")
    mc, _ = _midpoint_via_vesica(m, a, b, "Mc")

    med_a = m.construct_line(a, ma, classes=["median"], ID="[ A Ma ]")
    med_b = m.construct_line(b, mb, classes=["median"], ID="[ B Mb ]")
    med_c = m.construct_line(c, mc, classes=["median"], ID="[ C Mc ]")
    g = m.intersect(med_a, med_b, classes=["result"], ID="G")

    m.construct_polygon([a, b, c], ID="< A B C >")

    # Verify G lies on 3rd median and AG / GMa = S_ABC / S_MaBC = 2
    del med_c
    _assert_scalar(signed_area2(c, mc, g), 0)
    _assert_scalar(quadrance(a, g), 4 * quadrance(g, ma))
    _assert_scalar(signed_area2(a, b, c), 36)  # 2 * Area = 36 -> S_ABC = 18

    anns: list[dict[str, object]] = [
        {"x": 3, "y": -sp.Rational(9, 10), "text": "S_ABC = 18 (signed area invariant)", "kind": "quadrance", "ref": "< A B C >"},
        {"x": sp.Rational(16, 5), "y": sp.Rational(23, 5), "text": "Co-side Elimination: AG / GMa = S_ABC / S_MaBC = 2", "kind": "paradigm", "ref": "G"},
        {"x": sp.Rational(7, 5), "y": sp.Rational(11, 5), "text": "P_ABC = Q(A,B)+Q(B,C)-Q(A,C)", "kind": "spread", "ref": "[ B Mb ]"},
    ]
    return m, anns


def build_06_pga_cga_inversion() -> tuple[Model, list[dict[str, object]]]:
    """Build Figure 6: 2D PGA/CGA Circle Inversion `C >> P` & `CP^2` Pole-Polar.

    Returns:
        Tuple of exact `Model` and SVG callout annotations.
    """
    m = Model("pga_cga_inversion", auto_intersect=False, enable_logging=False)
    o = m.set_point(0, 0, classes=["given"], ID="O")
    r0 = m.set_point(2, 0, classes=["midpoint"], ID="R0")
    p = m.set_point(4, 0, classes=["given"], ID="P")

    l_op = m.construct_line(o, p, classes=["axis"], ID="[ O P ]")
    omega = m.construct_circle(o, r0, classes=["circumcircle"], ID="( O R0 )")

    # Thales circle on OP centered at R0(2,0) intersects omega at tangent points T1, T2
    thales = m.construct_circle(r0, o, classes=["guide"], ID="( R0 O )", guide=True)
    t1 = m.intersect(omega, thales, side_of=(o, p, 1), classes=["target"], ID="T1")
    t2 = m.intersect(omega, thales, side_of=(o, p, -1), classes=["target"], ID="T2")

    polar = m.construct_line(t1, t2, classes=["bisector"], ID="[ T1 T2 ]")
    p_inv = m.intersect(l_op, polar, between=(o, r0), classes=["result"], ID="P1")
    s_pt1 = m.construct_segment(p, t1, classes=["golden"], ID="/ P T1 /")
    s_pt2 = m.construct_segment(p, t2, classes=["golden"], ID="/ P T2 /")

    # Verify inversion |OP| * |OP1| = R^2 => Q(O,P)*Q(O,P1) = 16*1 = 16 = R^4
    m.assert_equal(s_pt1, s_pt2, by="III.17")
    m.assert_perpendicular(l_op, polar, at=p_inv, by="Polar")
    _assert_scalar(quadrance(o, p) * quadrance(o, p_inv), quadrance(o, r0) ** 2)
    _assert_scalar(line_spread(l_op, polar), 1)
    # Verify harmonic conjugacy (-2, 2; 1, 4) = -1 along diameter!
    r_neg = m.intersect(l_op, omega, other_than=r0, classes=["midpoint"], ID="R1")
    _assert_scalar(cross_ratio(r_neg, r0, p_inv, p), -1)

    anns: list[dict[str, object]] = [
        {"x": 1, "y": sp.Rational(13, 5), "text": "CP^2 Polar: l = C * P (x = 1)", "kind": "paradigm", "ref": "[ T1 T2 ]"},
        {"x": sp.Rational(11, 5), "y": -sp.Rational(12, 5), "text": "2DCGA Inversion: P1 = Omega >> P", "kind": "paradigm", "ref": "P1"},
        {"x": sp.Rational(9, 5), "y": -sp.Rational(7, 10), "text": "(R1, R0; P1, P) = -1 (harmonic)", "kind": "spread", "ref": "P"},
    ]
    return m, anns


def build_07_vesica_golden_poles() -> tuple[Model, list[dict[str, object]]]:
    """Build Figure 7: Just-In-Time Emergence from `fundamental(A, B)` to Golden Chain.

    Returns:
        Tuple of exact `Model` and SVG callout annotations.
    """
    m = Model("vesica_golden_poles", auto_intersect=False, enable_logging=False)
    a = m.set_point(0, 0, classes=["given"], ID="A")
    b = m.set_point(1, 0, classes=["given"], ID="B")

    l_ab = m.construct_line(a, b, ID="[ A B ]")
    c_ab = m.construct_circle(a, b, ID="( A B )")
    c_ba = m.construct_circle(b, a, ID="( B A )")

    c = m.intersect(l_ab, c_ab, other_than=b, classes=["midpoint"], ID="C")
    d = m.intersect(l_ab, c_ba, beyond=(a, b), classes=["midpoint"], ID="D")
    f = m.intersect(c_ab, c_ba, side_of=(a, b, 1), classes=["result"], ID="F")
    e = m.intersect(c_ab, c_ba, side_of=(a, b, -1), classes=["result"], ID="E")

    l_ef = m.construct_line(e, f, classes=["bisector"], ID="[ E F ]")
    mid = m.intersect(l_ab, l_ef, between=(a, b), classes=["midpoint"], ID="M")

    c_ad = m.construct_circle(a, d, classes=["guide"], ID="( A D )", guide=True)
    c_bc = m.construct_circle(b, c, classes=["guide"], ID="( B C )", guide=True)
    j = m.intersect(l_ef, c_ad, side_of=(a, b, 1), classes=["golden"], ID="J")
    i = m.intersect(l_ef, c_bc, side_of=(a, b, -1), classes=["golden"], ID="I")

    m.construct_segment(e, f, classes=["golden"], ID="/ E F /")
    s_fj = m.construct_segment(f, j, classes=["golden"], ID="/ F J /")
    s_ie = m.construct_segment(i, e, classes=["golden"], ID="/ I E /")

    phi = (1 + sp.sqrt(5)) / 2
    m.assert_equal(s_fj, s_ie, by="Symmetry")
    _assert_scalar(quadrance(a, mid), sp.Rational(1, 4))
    _assert_scalar(quadrance(e, f) / quadrance(f, j), phi**2)
    _assert_scalar(quadrance(e, j) / quadrance(e, f), phi**2)

    anns: list[dict[str, object]] = [
        {"x": sp.Rational(1, 2), "y": sp.Rational(12, 5), "text": "|EF| / |FJ| = phi, Q ratio = phi^2", "kind": "spread", "ref": "/ F J /"},
        {"x": sp.Rational(1, 2), "y": -sp.Rational(12, 5), "text": "Golden Chain / I E F J / in 5 steps!", "kind": "paradigm", "ref": "/ I E /"},
    ]
    return m, anns


def build_08_rosetta_centers_euler() -> tuple[Model, list[dict[str, object]]]:
    """Build Figure 8: Rosetta Benchmark 5 — 13-14-15 Triangle Centers `X(1)..X(5)`.

    Returns:
        Tuple of exact `Model` and SVG callout annotations.
    """
    m = Model("rosetta_centers_euler", auto_intersect=False, enable_logging=False)
    a = m.set_point(0, 0, classes=["given"], ID="A")
    b = m.set_point(14, 0, classes=["given"], ID="B")
    c = m.set_point(5, 12, classes=["given"], ID="C")
    m.construct_polygon([a, b, c], ID="< A B C >")

    # Construct midpoints & perpendicular bisectors -> Circumcenter X3 & Centroid X2
    ma, bis_bc = _midpoint_via_vesica(m, b, c, "Ma", keep_bisector=True)
    mb, bis_ac = _midpoint_via_vesica(m, a, c, "Mb", keep_bisector=False)
    mc, bis_ab = _midpoint_via_vesica(m, a, b, "Mc", keep_bisector=True)
    m[bis_bc].guide = True
    m[bis_ab].guide = True
    del bis_ac

    med_a = m.construct_line(a, ma, classes=["guide"], guide=True)
    med_b = m.construct_line(b, mb, classes=["guide"], guide=True)
    x2 = m.intersect(med_a, med_b, classes=["result"], ID="X2")
    x3 = m.intersect(bis_ab, bis_bc, classes=["result"], ID="X3")
    m.construct_circle(x3, a, classes=["circumcircle"], ID="( X3 A )")

    # Altitudes -> Orthocenter X4 (C -> AB has foot Hc(5,0))
    l_ab = m.construct_line(a, b, classes=["guide"], guide=True)
    l_bc = m.construct_line(b, c, classes=["guide"], guide=True)
    with m.subconstruction("altitudes_X4") as scope:
        c_ca = m.construct_circle(c, a, classes=["guide"], guide=True)
        a_mirror = m.intersect(l_ab, c_ca, other_than=a, guide=True)
        hc, alt_c = _midpoint_via_vesica(m, a, a_mirror, "Hc", keep_bisector=True)
        c_ab_alt = m.construct_circle(a, b, classes=["guide"], guide=True)
        b_mirror = m.intersect(l_bc, c_ab_alt, other_than=b, guide=True)
        _, alt_a = _midpoint_via_vesica(m, b, b_mirror, "Ha", keep_bisector=True)
        x4 = m.intersect(alt_c, alt_a, classes=["result"], ID="X4")
        scope.keep(hc, x4)

    # Nine-point center X5 = midpoint(X3, X4) + Nine-point circle through Mc
    x5, _ = _midpoint_via_vesica(m, x3, x4, "X5")
    m.construct_circle(x5, mc, classes=["ninepoint"], ID="( X5 Mc )")

    # Angle bisectors at A and B -> Incenter X1(6, 4) + Incircle through touchpoint T_c(6, 0)
    with m.subconstruction("incenter_X1") as scope:
        l_ac = m.construct_line(a, c, classes=["guide"], guide=True)
        c_unit_a = m.construct_circle(a, c, classes=["guide"], guide=True)
        p_ab = m.intersect(l_ab, c_unit_a, on_ray=(a, b), guide=True)
        qa, _ = _midpoint_via_vesica(m, c, p_ab, "Qa", keep_bisector=False)
        bis_ang_a = m.construct_line(a, qa, classes=["guide"], guide=True)

        c_unit_b = m.construct_circle(b, a, classes=["guide"], guide=True)
        p_bc = m.intersect(l_bc, c_unit_b, on_ray=(b, c), guide=True)
        qb, _ = _midpoint_via_vesica(m, a, p_bc, "Qb", keep_bisector=False)
        bis_ang_b = m.construct_line(b, qb, classes=["guide"], guide=True)
        x1 = m.intersect(bis_ang_a, bis_ang_b, classes=["golden"], ID="X1")

        # Foot of X1 on AB for incircle
        c_x1 = m.construct_circle(x1, hc, classes=["guide"], guide=True)
        h_mirror = m.intersect(l_ab, c_x1, other_than=hc, guide=True)
        tc, _ = _midpoint_via_vesica(m, hc, h_mirror, "Tc", keep_bisector=False)
        incirc = m.construct_circle(x1, tc, classes=["incircle"], ID="( X1 Tc )")
        del l_ac
        scope.keep(x1, incirc)

    euler = m.construct_line(x3, x4, classes=["euler"], ID="[ X3 X4 ]")
    del euler

    # Exact rational verifications on 13-14-15 triangle!
    m.assert_equal((x3, a), (x3, b), (x3, c), by="IV.5")
    m.assert_equal((x5, ma), (x5, mb), (x5, mc), (x5, hc), by="NinePoint")
    _assert_scalar(x1.x, 6)
    _assert_scalar(x1.y, 4)
    _assert_scalar(x2.x, sp.Rational(19, 3))
    _assert_scalar(x2.y, 4)
    _assert_scalar(x3.x, 7)
    _assert_scalar(x3.y, sp.Rational(33, 8))
    _assert_scalar(x4.x, 5)
    _assert_scalar(x4.y, sp.Rational(15, 4))
    _assert_scalar(x5.x, 6)
    _assert_scalar(x5.y, sp.Rational(63, 16))
    _assert_scalar(signed_area2(x2, x3, x4), 0)
    _assert_scalar(quadrance(x3, x4), 9 * quadrance(x3, x2))

    anns: list[dict[str, object]] = [
        {"x": 7, "y": -sp.Rational(9, 4), "text": "Heronian 13-14-15: X1..X5 all in Q!", "kind": "quadrance", "ref": "< A B C >"},
        {"x": sp.Rational(23, 2), "y": sp.Rational(19, 2), "text": "Euler Line: X4 - X3 = 3(X2 - X3)", "kind": "spread", "ref": "[ X3 X4 ]"},
    ]
    return m, anns


def build_09_rosetta_pappus_harmonic() -> tuple[Model, list[dict[str, object]]]:
    """Build Figure 9: Rosetta Benchmark 7 — Projective Pappus Hexagon & Harmonic Range.

    Returns:
        Tuple of exact `Model` and SVG callout annotations.
    """
    m = Model("rosetta_pappus_harmonic", auto_intersect=False, enable_logging=False)
    o = m.set_point(0, 0, classes=["given"], ID="O")
    a1 = m.set_point(2, 0, classes=["given"], ID="A1")
    b1 = m.set_point(3, 0, classes=["given"], ID="B1")
    c1 = m.set_point(6, 0, classes=["given"], ID="C1")

    a2 = m.set_point(1, 1, classes=["given"], ID="A2")
    b2 = m.set_point(sp.Rational(5, 2), sp.Rational(5, 2), classes=["given"], ID="B2")
    c2 = m.set_point(4, 4, classes=["given"], ID="C2")

    m.construct_line(o, c1, ID="[ O C1 ]")
    m.construct_line(o, c2, ID="[ O C2 ]")

    l_a1b2 = m.construct_line(a1, b2, classes=["guide"], ID="[ A1 B2 ]")
    l_a2b1 = m.construct_line(a2, b1, classes=["guide"], ID="[ A2 B1 ]")
    x = m.intersect(l_a1b2, l_a2b1, classes=["result"], ID="X")

    l_a1c2 = m.construct_line(a1, c2, classes=["guide"], ID="[ A1 C2 ]")
    l_a2c1 = m.construct_line(a2, c1, classes=["guide"], ID="[ A2 C1 ]")
    y = m.intersect(l_a1c2, l_a2c1, classes=["result"], ID="Y")

    l_b1c2 = m.construct_line(b1, c2, classes=["guide"], ID="[ B1 C2 ]")
    l_b2c1 = m.construct_line(b2, c1, classes=["guide"], ID="[ B2 C1 ]")
    z = m.intersect(l_b1c2, l_b2c1, classes=["result"], ID="Z")

    pappus_line = m.construct_line(x, z, classes=["axis"], ID="[ X Z ]")
    del pappus_line

    # Verify Pappus collinearity and exact harmonic range (O, B1; A1, C1) = -1
    _assert_scalar(signed_area2(x, y, z), 0)
    _assert_scalar(cross_ratio(o, b1, a1, c1), -1)
    if not is_harmonic(o, b1, a1, c1):
        msg = "Expected harmonic range (O, B1; A1, C1) == -1"
        raise AssertionError(msg)

    anns: list[dict[str, object]] = [
        {"x": sp.Rational(9, 2), "y": sp.Rational(11, 5), "text": "Pappus Axis: det[X, Y, Z] = 0", "kind": "paradigm", "ref": "[ X Z ]"},
        {"x": 3, "y": -sp.Rational(4, 5), "text": "Harmonic Range: CR(O, B1; A1, C1) = -1", "kind": "spread", "ref": "[ O C1 ]"},
    ]
    return m, anns


FIGURE_SPECS: tuple[FigureSpec, ...] = (
    FigureSpec("01-seven-ontologies", "The 7 Ontologies of a Line & Circle", build_01_seven_ontologies),
    FigureSpec("02-topological-selectors", "Diagrammatic Topological Selectors (System E == geometor.model)", build_02_topological_selectors),
    FigureSpec("03-tarski-five-segment", "Tarski's Point-Only Five-Segment Axiom (FSC) & Midpoint Orthogonality", build_03_tarski_five_segment),
    FigureSpec("04-torsor-oangle-spread", "Affine Torsor (C -v A), Directed oangle & Rational Spread", build_04_torsor_oangle_spread),
    FigureSpec("05-area-method-elimination", "Chou-Gao-Zhang Coordinate-Free Area Method (S_ABC & P_ABC)", build_05_area_method_elimination),
    FigureSpec("06-pga-cga-inversion", "2D PGA/CGA Circle Inversion (C >> P) & CP^2 Pole-Polar", build_06_pga_cga_inversion),
    FigureSpec("07-vesica-golden-poles", "Just-In-Time Emergence: From fundamental(A, B) to the Golden Chain", build_07_vesica_golden_poles),
    FigureSpec("08-rosetta-centers-euler", "Rosetta Benchmark 5: Heronian 13-14-15 Centers X(1)..X(5) & Euler Line", build_08_rosetta_centers_euler),
    FigureSpec("09-rosetta-pappus-harmonic", "Rosetta Benchmark 7: Projective Pappus Hexagon & Harmonic Range", build_09_rosetta_pappus_harmonic),
)


def default_figures_dir() -> Path:
    """Return the canonical `docsrc/_static/figures` directory inside `geometor/codes`.

    Returns:
        Absolute `Path` to `docsrc/_static/figures`.
    """
    repo_root = Path(__file__).resolve().parents[3]
    return repo_root / "docsrc" / "_static" / "figures"


def build_all_figures(output_dir: Path | None = None) -> list[Path]:
    """Construct, symbolically verify, and render all 9 `.euclid-graphic` SVG figures.

    Args:
        output_dir: Optional target directory; defaults to `docsrc/_static/figures`.

    Returns:
        List of written `.svg` file paths.
    """
    target_dir = output_dir if output_dir is not None else default_figures_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    for spec in FIGURE_SPECS:
        model, anns = spec.builder()
        svg_path = target_dir / f"{spec.slug}.svg"
        render_svg(model, svg_path, annotations=anns)
        written.append(svg_path)
    return written
