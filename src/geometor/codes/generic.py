"""Generic (L2) witnesses: showcase theorems checked with free symbolic parameters.

A ``geometor.model`` witness certifies a theorem for *one* exact figure (Truth
Ladder L1). Replacing the concrete coordinates by free symbols and reducing the
conclusion to ``0`` certifies it for *every* figure outside a degenerate set
(L2) — the regime of Wu's method and Gröbner bases. Hypotheses are satisfied
*by construction* (coordinates are chosen so the hypotheses hold identically);
the degenerate set is recorded as explicit non-degeneracy conditions (NDG).

Everything is exact SymPy: no floats are introduced.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field

import sympy as sp

Vec = tuple[sp.Expr, sp.Expr]


@dataclass
class GenericWitness:
    """Result of a symbolic-parameter check.

    Attributes:
        principle: Catalog principle id.
        parameters: Free symbols of the configuration.
        construction: How the hypotheses are built into the coordinates.
        conclusion: The conclusion polynomial / rational expression (as text).
        residual: Simplified conclusion; ``"0"`` when proved.
        ndg: Non-degeneracy conditions under which the identity is meaningful.
        proved: Whether the residual simplified to exactly zero.
    """

    principle: str
    parameters: list[str]
    construction: str
    conclusion: str
    residual: str
    ndg: list[str] = field(default_factory=list)
    proved: bool = False


def _sub(p: Vec, q: Vec) -> Vec:
    return (p[0] - q[0], p[1] - q[1])


def _dot(u: Vec, v: Vec) -> sp.Expr:
    return u[0] * v[0] + u[1] * v[1]


def _cross(u: Vec, v: Vec) -> sp.Expr:
    return u[0] * v[1] - u[1] * v[0]


def _quadrance(p: Vec, q: Vec) -> sp.Expr:
    d = _sub(p, q)
    return _dot(d, d)


def _spread(vertex: Vec, p: Vec, q: Vec) -> sp.Expr:
    """Spread at ``vertex`` between rays to ``p`` and ``q`` (Wildberger)."""
    u, v = _sub(p, vertex), _sub(q, vertex)
    return _cross(u, v) ** 2 / (_dot(u, u) * _dot(v, v))


def _circle_point(t: sp.Symbol) -> Vec:
    """Rational parametrization of the unit circle (exact, no trig)."""
    den = 1 + t**2
    return ((1 - t**2) / den, 2 * t / den)


def _foot(p: Vec, a: Vec, b: Vec) -> Vec:
    """Foot of the perpendicular from ``p`` to line ``ab`` (coordinates cancelled)."""
    d = _sub(b, a)
    k = sp.cancel(_dot(_sub(p, a), d) / _dot(d, d))
    return (sp.cancel(a[0] + k * d[0]), sp.cancel(a[1] + k * d[1]))


def _finish(
    principle: str,
    params: list[sp.Symbol],
    construction: str,
    expr: sp.Expr,
    ndg: list[str],
) -> GenericWitness:
    """Reduce ``expr`` to its numerator polynomial and expand it exactly."""
    numerator, _ = sp.fraction(sp.together(expr))
    residual = sp.expand(numerator)
    text = str(expr)
    return GenericWitness(
        principle=principle,
        parameters=[str(s) for s in params],
        construction=construction,
        conclusion=text if len(text) < 400 else text[:397] + "...",
        residual=str(residual) if residual == 0 else str(sp.factor(residual)),
        ndg=ndg,
        proved=residual == 0,
    )


def isosceles_base_angles() -> GenericWitness:
    """Euclid I.5 with apex ``A = (u, v)`` over base ``B = (0, 0)``, ``C = (2u, 0)``."""
    u, v = sp.symbols("u v", real=True)
    a, b, c = (u, v), (sp.Integer(0), sp.Integer(0)), (2 * u, sp.Integer(0))
    expr = _spread(b, a, c) - _spread(c, a, b)
    return _finish(
        "isosceles_base_angles",
        [u, v],
        "AB = AC is built in: A lies on the perpendicular bisector x = u of BC.",
        expr,
        ["u != 0 (B != C)", "v != 0 (A not on BC)"],
    )


def pythagorean() -> GenericWitness:
    """Euclid I.47 with ``A = (x, y)``, ``B = A + (p, q)``, ``C = A + t(-q, p)``."""
    x, y, p, q, t = sp.symbols("x y p q t", real=True)
    a = (x, y)
    b = (x + p, y + q)
    c = (x - t * q, y + t * p)
    expr = _quadrance(b, c) - _quadrance(a, b) - _quadrance(a, c)
    return _finish(
        "pythagorean",
        [x, y, p, q, t],
        "The right angle at A is built in: AC is AB rotated by 90 degrees and scaled by t.",
        expr,
        ["(p, q) != (0, 0) (A != B)", "t != 0 (A != C)"],
    )


def thales_semicircle() -> GenericWitness:
    """Euclid III.31 on the circle of radius ``r`` with ``P`` rationally parametrized."""
    r, t = sp.symbols("r t", real=True)
    a, b = (-r, sp.Integer(0)), (r, sp.Integer(0))
    unit = _circle_point(t)
    p = (r * unit[0], r * unit[1])
    expr = _dot(_sub(a, p), _sub(b, p))
    return _finish(
        "thales_semicircle",
        [r, t],
        "AB is a diameter of the circle radius r about the origin; P = r((1-t^2)/(1+t^2), 2t/(1+t^2)).",
        expr,
        ["r != 0", "t != 0 (P != B); t finite (P != A)"],
    )


def simson_line() -> GenericWitness:
    """Simson line: pedal feet of ``P`` on the circumcircle of ``ABC`` are collinear."""
    s, t, w = sp.symbols("s t w", real=True)
    a, b, c = _circle_point(s), _circle_point(t), _circle_point(w)
    p: Vec = (sp.Integer(1), sp.Integer(0))
    f1, f2, f3 = _foot(p, b, c), _foot(p, c, a), _foot(p, a, b)
    expr = _cross(_sub(f2, f1), _sub(f3, f1))
    return _finish(
        "simson_line",
        [s, t, w],
        "A, B, C on the unit circle via rational parameters s, t, w; P = (1, 0) (WLOG by rotation).",
        expr,
        ["s, t, w pairwise distinct (non-degenerate triangle)", "s, t, w != 0 (P not a vertex)"],
    )


GENERIC_BUILDERS: dict[str, Callable[[], GenericWitness]] = {
    "isosceles_base_angles": isosceles_base_angles,
    "pythagorean": pythagorean,
    "thales_semicircle": thales_semicircle,
    "simson_line": simson_line,
}
"""Principle id → generic (symbolic-parameter) witness builder."""

GENERIC_GAPS: dict[str, str] = {
    "pasch": (
        "Pasch is an order statement (betweenness / same side). Polynomial identities over a field "
        "cannot express order; certifying it needs an ordered (real closed) field and inequalities, "
        "i.e. a different foundation from Wu / Groebner methods."
    ),
}
"""Principles that cannot be lifted to L2 by polynomial identities, with reasons."""


def generic_witness(principle_id: str) -> GenericWitness | None:
    """Build the generic witness for ``principle_id`` if one is defined.

    Args:
        principle_id: Catalog principle id.

    Returns:
        The witness, or ``None`` when no generic builder exists.
    """
    builder = GENERIC_BUILDERS.get(principle_id)
    return builder() if builder else None
