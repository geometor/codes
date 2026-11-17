"""Phase 4: Exact symbolic verification of principles in geometor.model.

Every witness configuration uses exact rational or quadratic SymPy coordinates
(never ``float`` or ``sp.Float``) and checks conclusions with ``Model.assert_*``
and ``Model.conclude()``. Principles that cannot yet be expressed natively
in ``geometor.model`` are recorded with an explicit ``gap`` explanation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

import sympy as sp
import sympy.geometry as spg

from geometor.model import Model
from geometor.model.invariants import quadrance


@dataclass(frozen=True)
class VerificationResult:
    """Outcome of verifying one principle in ``geometor.model``."""

    principle_id: str
    status: str  # "verified" | "gap"
    summary: str
    gap_reason: str = ""


def _build_equilateral_apex() -> Model:
    m = Model("I.1 equilateral_apex", auto_intersect=False)
    A = m.set_point(0, 0, label="A")
    B = m.set_point(2, 0, label="B")
    s_ab = m.set_segment(A, B)
    c1 = m.construct_circle(A, B)
    c2 = m.construct_circle(B, A)
    C = m.intersect(c1, c2)
    s_ac = m.set_segment(A, C)
    s_bc = m.set_segment(B, C)
    m.assert_equal(s_ab, s_ac, s_bc, by="I.1", label="AB = AC = BC")
    m.conclude(C, s_ac, s_bc, kind="qef", by="I.1")
    return m


def _build_sas_congruence() -> Model:
    m = Model("I.4 sas_congruence", auto_intersect=False)
    A = m.set_point(0, 0, label="A")
    B = m.set_point(3, 0, label="B")
    C = m.set_point(0, 4, label="C")
    D = m.set_point(5, 0, label="D")
    E = m.set_point(8, 0, label="E")
    F = m.set_point(5, 4, label="F")
    t1 = m.set_polygon([A, B, C])
    t2 = m.set_polygon([D, E, F])
    m.assert_congruent(t1, t2, by="I.4", label="SAS witness triangles are congruent")
    m.conclude(t1, t2, by="I.4")
    return m


def _build_isosceles_base_angles() -> Model:
    m = Model("I.5 isosceles_base_angles", auto_intersect=False)
    A = m.set_point(2, 3, label="A")
    B = m.set_point(0, 0, label="B")
    C = m.set_point(4, 0, label="C")
    t = m.set_polygon([A, B, C])
    m.assert_equal((A, B), (A, C), by="Given", label="AB = AC")
    m.assert_spread_equal((A, B, C), (A, C, B), by="I.5", label="angle B = angle C")
    m.conclude(t, by="I.5")
    return m


def _build_sss_congruence() -> Model:
    m = Model("I.8 sss_congruence", auto_intersect=False)
    A, B, C = m.set_point(0, 0, label="A"), m.set_point(3, 0, label="B"), m.set_point(0, 4, label="C")
    D, E, F = m.set_point(5, 1, label="D"), m.set_point(8, 1, label="E"), m.set_point(5, 5, label="F")
    t1 = m.set_polygon([A, B, C])
    t2 = m.set_polygon([D, E, F])
    m.assert_congruent(t1, t2, by="I.8", label="SSS 3-4-5 triangles are congruent")
    m.conclude(t1, t2, by="I.8")
    return m


def _build_asa_aas_congruence() -> Model:
    m = Model("I.26 asa_aas_congruence", auto_intersect=False)
    A, B, C = m.set_point(0, 0, label="A"), m.set_point(4, 0, label="B"), m.set_point(1, 3, label="C")
    D, E, F = m.set_point(6, 0, label="D"), m.set_point(10, 0, label="E"), m.set_point(7, 3, label="F")
    t1 = m.set_polygon([A, B, C])
    t2 = m.set_polygon([D, E, F])
    m.assert_congruent(t1, t2, by="I.26", label="ASA witness triangles")
    m.conclude(t1, t2, by="I.26")
    return m


def _build_parallel_alternate_angles() -> Model:
    m = Model("I.29 parallel_alternate_angles", auto_intersect=False)
    A, B = m.set_point(0, 2, label="A"), m.set_point(4, 2, label="B")
    C, D = m.set_point(0, 0, label="C"), m.set_point(4, 0, label="D")
    E, F = m.set_point(1, 0, label="E"), m.set_point(3, 2, label="F")
    l1 = m.construct_line(A, B)
    l2 = m.construct_line(C, D)
    l3 = m.construct_line(E, F)
    m.assert_parallel(l1, l2, by="Given", label="AB || CD")
    m.assert_spread_equal((A, F, E), (D, E, F), by="I.29", label="alternate spreads equal")
    m.conclude(l1, l2, l3, by="I.29")
    return m


def _build_triangle_angle_sum() -> Model:
    m = Model("I.32 triangle_angle_sum", auto_intersect=False)
    A, B, C = m.set_point(0, 0, label="A"), m.set_point(4, 0, label="B"), m.set_point(1, 3, label="C")
    D = m.set_point(-3, 3, label="D")
    t = m.set_polygon([A, B, C])
    l_ab = m.construct_line(A, B)
    l_cd = m.construct_line(C, D)
    m.assert_parallel(l_ab, l_cd, by="I.31", label="CD || AB through C")
    m.assert_spread_equal((C, A, B), (A, C, D), by="I.29", label="alternate angle at A = ACD")
    m.conclude(t, by="I.32")
    return m


def _build_pythagorean() -> Model:
    m = Model("I.47 pythagorean", auto_intersect=False)
    A = m.set_point(0, 0, label="A")
    B = m.set_point(3, 0, label="B")
    C = m.set_point(0, 4, label="C")
    t = m.set_polygon([A, B, C])
    m.assert_perpendicular(m.construct_line(A, B), m.construct_line(A, C), by="Given", label="right angle at A")
    if sp.simplify(quadrance(A, B) + quadrance(A, C) - quadrance(B, C)) != 0:
        raise AssertionError("Pythagorean quadrance identity failed")
    m.conclude(t, by="I.47", label="Q(AB) + Q(AC) = Q(BC)")
    return m


def _build_inscribed_angles_same_arc() -> Model:
    m = Model("III.21 inscribed_angles_same_arc", auto_intersect=False)
    A = m.set_point(5, 0, label="A")
    B = m.set_point(0, 5, label="B")
    P = m.set_point(-3, 4, label="P")
    Q = m.set_point(-4, -3, label="Q")
    m.assert_concyclic(A, B, P, Q, by="Given", label="A, B, P, Q lie on circle x^2+y^2=25")
    m.assert_spread_equal((A, P, B), (A, Q, B), signed=False, by="III.21", label="spread(APB) = spread(AQB)")
    m.conclude(A, B, P, Q, by="III.21")
    return m


def _build_thales_semicircle() -> Model:
    m = Model("III.31 thales_semicircle", auto_intersect=False)
    O = m.set_point(0, 0, label="O")
    A = m.set_point(-5, 0, label="A")
    B = m.set_point(5, 0, label="B")
    P = m.set_point(3, 4, label="P")
    Q = m.set_point(-3, -4, label="Q")
    c = m.construct_circle(O, A)
    m.assert_collinear(A, O, B, by="Given", label="AB is a diameter")
    m.assert_concyclic(A, B, P, Q, by="Given", label="P on circle")
    l_ap = m.construct_line(A, P)
    l_bp = m.construct_line(B, P)
    m.assert_perpendicular(l_ap, l_bp, by="III.31", label="AP perp BP")
    m.conclude(c, l_ap, l_bp, by="III.31")
    return m


def _build_thales_intercept() -> Model:
    m = Model("VI.2 thales_intercept", auto_intersect=False)
    O = m.set_point(0, 0, label="O")
    A = m.set_point(2, 0, label="A")
    C = m.set_point(6, 0, label="C")
    B = m.set_point(1, 2, label="B")
    D = m.set_point(3, 6, label="D")
    l_ab = m.construct_line(A, B)
    l_cd = m.construct_line(C, D)
    m.assert_parallel(l_ab, l_cd, by="Given", label="AB || CD")
    if sp.simplify(quadrance(O, C) * quadrance(A, B) - quadrance(O, A) * quadrance(C, D)) != 0:
        raise AssertionError("Thales intercept ratio failed")
    m.conclude(l_ab, l_cd, by="VI.2", label="OC/OA = CD/AB")
    return m


def _build_aa_similarity() -> Model:
    m = Model("VI.4 aa_similarity", auto_intersect=False)
    A, B, C = m.set_point(0, 0, label="A"), m.set_point(3, 0, label="B"), m.set_point(0, 4, label="C")
    D, E, F = m.set_point(5, 0, label="D"), m.set_point(11, 0, label="E"), m.set_point(5, 8, label="F")
    t1 = m.set_polygon([A, B, C])
    t2 = m.set_polygon([D, E, F])
    m.assert_spread_equal((B, A, C), (E, D, F), by="Given", label="angle A = angle D")
    m.assert_spread_equal((A, B, C), (D, E, F), by="Given", label="angle B = angle E")
    if sp.simplify(quadrance(D, E) * quadrance(A, C) - quadrance(A, B) * quadrance(D, F)) != 0:
        raise AssertionError("AA similarity proportion failed")
    m.conclude(t1, t2, by="VI.4", label="DE/AB = DF/AC")
    return m


def _build_simson_line() -> Model:
    m = Model("simson_line", auto_intersect=False)
    A = m.set_point(5, 0, label="A")
    B = m.set_point(-5, 0, label="B")
    C = m.set_point(3, 4, label="C")
    P = m.set_point(0, 5, label="P")
    l_ab = spg.Line(A, B)
    l_bc = spg.Line(B, C)
    l_ca = spg.Line(C, A)
    p1 = l_ab.projection(P)
    p2 = l_bc.projection(P)
    p3 = l_ca.projection(P)
    F1 = m.set_point(p1.x, p1.y, label="F_ab")
    F2 = m.set_point(p2.x, p2.y, label="F_bc")
    F3 = m.set_point(p3.x, p3.y, label="F_ca")
    m.set_polygon([A, B, C])
    m.assert_concyclic(A, B, C, P, by="Given", label="P lies on circumcircle of ABC")
    m.assert_collinear(F1, F2, F3, by="Simson", label="pedal feet F_ab, F_bc, F_ca are collinear")
    l_simson = m.construct_line(F1, F3)
    m.conclude(l_simson, F1, F2, F3, label="Simson line")
    return m


def _build_orthocenter_concurrence() -> Model:
    m = Model("orthocenter_concurrence", auto_intersect=False)
    A = m.set_point(0, 0, label="A")
    B = m.set_point(6, 0, label="B")
    C = m.set_point(2, 4, label="C")
    tri = spg.Triangle(A, B, C)
    h_pt = tri.orthocenter
    H = m.set_point(h_pt.x, h_pt.y, label="H")
    m.set_polygon([A, B, C])
    m.assert_perpendicular(m.construct_line(A, H), m.construct_line(B, C), label="AH perp BC")
    m.assert_perpendicular(m.construct_line(B, H), m.construct_line(A, C), label="BH perp AC")
    m.assert_perpendicular(m.construct_line(C, H), m.construct_line(A, B), label="CH perp AB")
    m.conclude(H, label="three altitudes concur at H")
    return m


def _build_midpoint() -> Model:
    m = Model("midpoint", auto_intersect=False)
    A = m.set_point(0, 0, label="A")
    B = m.set_point(4, 2, label="B")
    M = m.set_point(2, 1, label="M")
    m.set_segment(A, B)
    m.assert_collinear(A, M, B, label="M on AB")
    m.assert_equal((A, M), (M, B), label="AM = MB")
    m.conclude(M, kind="qef", by="I.10")
    return m


def _build_circumcenter_concurrence() -> Model:
    m = Model("circumcenter_concurrence", auto_intersect=False)
    A = m.set_point(0, 0, label="A")
    B = m.set_point(6, 0, label="B")
    C = m.set_point(0, 8, label="C")
    O = m.set_point(3, 4, label="O")
    m.set_polygon([A, B, C])
    m.assert_equal((O, A), (O, B), (O, C), label="OA = OB = OC")
    m.conclude(O, label="circumcenter O")
    return m


def _build_centroid_concurrence() -> Model:
    m = Model("centroid_concurrence", auto_intersect=False)
    A = m.set_point(0, 0, label="A")
    B = m.set_point(6, 0, label="B")
    C = m.set_point(0, 6, label="C")
    G = m.set_point(2, 2, label="G")
    Ma = m.set_point(3, 3, label="Ma")
    Mb = m.set_point(0, 3, label="Mb")
    Mc = m.set_point(3, 0, label="Mc")
    m.set_polygon([A, B, C])
    m.assert_collinear(A, G, Ma, label="median A-Ma through G")
    m.assert_collinear(B, G, Mb, label="median B-Mb through G")
    m.assert_collinear(C, G, Mc, label="median C-Mc through G")
    m.conclude(G, label="three medians concur at G")
    return m


def _build_incenter_concurrence() -> Model:
    m = Model("incenter_concurrence", auto_intersect=False)
    # 3-4-5 right triangle has integer incenter (1, 1) and inradius 1
    A = m.set_point(0, 0, label="A")
    B = m.set_point(4, 0, label="B")
    C = m.set_point(0, 3, label="C")
    I = m.set_point(1, 1, label="I")
    m.set_polygon([A, B, C])
    m.assert_spread_equal((B, A, I), (C, A, I), label="AI bisects A")
    m.assert_spread_equal((A, B, I), (C, B, I), label="BI bisects B")
    m.assert_spread_equal((A, C, I), (B, C, I), label="CI bisects C")
    m.conclude(I, label="three angle bisectors concur at I")
    return m


def _build_perpendicular_foot() -> Model:
    m = Model("perpendicular_foot", auto_intersect=False)
    A = m.set_point(0, 0, label="A")
    B = m.set_point(4, 0, label="B")
    P = m.set_point(2, 3, label="P")
    F = m.set_point(2, 0, label="F")
    l_ab = m.construct_line(A, B)
    l_pf = m.construct_line(P, F)
    m.assert_collinear(A, F, B, label="F lies on AB")
    m.assert_perpendicular(l_pf, l_ab, label="PF perp AB")
    m.conclude(F, kind="qef", by="I.12")
    return m


def _build_angle_bisector() -> Model:
    m = Model("angle_bisector", auto_intersect=False)
    O = m.set_point(0, 0, label="O")
    A = m.set_point(1, 0, label="A")
    B = m.set_point(0, 1, label="B")
    D = m.set_point(1, 1, label="D")
    m.construct_line(O, A)
    m.construct_line(O, B)
    l_od = m.construct_line(O, D)
    m.assert_spread_equal((A, O, D), (D, O, B), label="OD bisects AOB")
    m.conclude(l_od, kind="qef", by="I.9")
    return m


PILOT_BUILDERS: dict[str, Callable[[], Model]] = {
    "equilateral_apex": _build_equilateral_apex,
    "sas_congruence": _build_sas_congruence,
    "isosceles_base_angles": _build_isosceles_base_angles,
    "sss_congruence": _build_sss_congruence,
    "asa_aas_congruence": _build_asa_aas_congruence,
    "parallel_alternate_angles": _build_parallel_alternate_angles,
    "triangle_angle_sum": _build_triangle_angle_sum,
    "pythagorean": _build_pythagorean,
    "inscribed_angles_same_arc": _build_inscribed_angles_same_arc,
    "thales_semicircle": _build_thales_semicircle,
    "thales_intercept": _build_thales_intercept,
    "aa_similarity": _build_aa_similarity,
    "simson_line": _build_simson_line,
    "orthocenter_concurrence": _build_orthocenter_concurrence,
    "midpoint": _build_midpoint,
    "circumcenter_concurrence": _build_circumcenter_concurrence,
    "centroid_concurrence": _build_centroid_concurrence,
    "incenter_concurrence": _build_incenter_concurrence,
    "perpendicular_foot": _build_perpendicular_foot,
    "angle_bisector": _build_angle_bisector,
}

KNOWN_GAPS: dict[str, str] = {
    "pasch": "Requires 1D betweenness / half-plane order predicates not yet native in geometor.model.proof.",
    "betweenness_symmetry": "Requires ternary between(A, B, C) order relation in geometor.model.proof.",
    "betweenness_transitivity": "Requires ternary between(A, B, C) order relation in geometor.model.proof.",
}


def build_pilot_model(principle_id: str) -> Model | None:
    """Build and assert the exact ``geometor.model`` witness for ``principle_id``."""
    builder = PILOT_BUILDERS.get(principle_id)
    return builder() if builder else None


def verify_principle(principle_id: str) -> VerificationResult:
    """Verify a principle exactly in ``geometor.model`` or report its gap.

    Args:
        principle_id: Canonical principle identifier.

    Returns:
        A `VerificationResult`.
    """
    if principle_id in KNOWN_GAPS:
        return VerificationResult(
            principle_id=principle_id,
            status="gap",
            summary="Not yet expressible in geometor.model.proof",
            gap_reason=KNOWN_GAPS[principle_id],
        )
    builder = PILOT_BUILDERS.get(principle_id)
    if builder is None:
        return VerificationResult(
            principle_id=principle_id,
            status="gap",
            summary="No witness builder registered yet",
            gap_reason="Pending witness construction.",
        )
    model = builder()
    for pt in model.points:
        if any(isinstance(c, sp.Float) for c in (pt.x, pt.y)):
            raise AssertionError(f"sp.Float leaked into {principle_id}: {pt}")
    return VerificationResult(
        principle_id=principle_id,
        status="verified",
        summary=f"Exact witness verified ({len(model.points)} points, {len(model.lines)} lines, {len(model.circles)} circles)",
    )


def verify_pilot() -> list[VerificationResult]:
    """Run exact verification on all pilot principles (verified + known gaps)."""
    ids = list(PILOT_BUILDERS) + list(KNOWN_GAPS)
    return [verify_principle(pid) for pid in ids]
