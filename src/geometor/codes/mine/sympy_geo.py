"""SymPy geometry miner: inspect ``sympy.geometry`` classes, methods, and functions."""

from __future__ import annotations

import inspect
from typing import Any

import sympy
import sympy.geometry as spg

from geometor.codes.mine.schema import Decl, MinedSystem

TARGET_CLASSES = (
    "Point",
    "Point2D",
    "Line",
    "Line2D",
    "Segment",
    "Segment2D",
    "Ray",
    "Ray2D",
    "Circle",
    "Ellipse",
    "Parabola",
    "Polygon",
    "Triangle",
    "RegularPolygon",
    "Curve",
    "Plane",
)

TOP_FUNCTIONS = (
    "intersection",
    "centroid",
    "are_similar",
    "closest_points",
    "convex_hull",
    "farthest_points",
)

# Generic SymPy / Python plumbing inherited from Basic/GeometryEntity that is
# not a geometric operation or predicate.
_SKIP_MEMBERS = frozenset({
    "ambient_dimension",
    "args",
    "atoms",
    "compare",
    "copy",
    "count",
    "doit",
    "dummy_eq",
    "evalf",
    "find",
    "free_symbols",
    "func",
    "has",
    "is_number",
    "is_zero",
    "match",
    "n",
    "plot_interval",
    "replace",
    "rewrite",
    "simplify",
    "sort_key",
    "subs",
    "xreplace",
})

_PREDICATES = frozenset({"contains", "encloses", "encloses_point", "equals"})
_MEASURES = frozenset({
    "angle_between",
    "area",
    "circumradius",
    "distance",
    "eccentricity",
    "inradius",
    "length",
    "perimeter",
    "radius",
    "slope",
    "smallest_angle_between",
    "taxicab_distance",
    "canberra_distance",
})
_CONSTRUCTIONS = frozenset({
    "altitudes",
    "bisectors",
    "bounds",
    "centroid",
    "circumcenter",
    "circumcircle",
    "cut_section",
    "equation",
    "eulerline",
    "excenters",
    "exradii",
    "incenter",
    "incircle",
    "intersection",
    "medial",
    "medians",
    "midpoint",
    "nine_point_circle",
    "normal_lines",
    "orthocenter",
    "parallel_line",
    "perpendicular_bisector",
    "perpendicular_line",
    "perpendicular_segment",
    "projection",
    "random_point",
    "reflect",
    "rotate",
    "scale",
    "tangent_lines",
    "translate",
})


def _classify_member(name: str) -> str:
    if name.startswith(("is_", "are_")) or name in _PREDICATES:
        return "predicate"
    if name in _MEASURES:
        return "measure"
    if name in _CONSTRUCTIONS:
        return "construction"
    return "method"


def _first_doc_line(obj: object) -> str:
    doc = inspect.getdoc(obj) or ""
    for ln in doc.splitlines():
        s = ln.strip()
        if s:
            return s
    return ""


def _safe_sig(obj: object) -> str:
    try:
        return str(inspect.signature(obj))  # type: ignore[arg-type]
    except (ValueError, TypeError):
        return ""


def mine_sympy() -> MinedSystem:
    """Mine the installed ``sympy.geometry`` API.

    Returns:
        A `MinedSystem` covering geometric classes, their own geometric
        methods/properties, and module-level geometric functions.
    """
    decls: list[Decl] = []

    for cls_name in TARGET_CLASSES:
        cls = getattr(spg, cls_name, None)
        if cls is None:
            continue
        decls.append(
            Decl(
                system="sympy",
                id=cls_name,
                name=cls_name,
                kind="sort",
                module="sympy.geometry",
                family=cls_name,
                statement=f"class {cls_name}{_safe_sig(cls)}",
                text=_first_doc_line(cls),
                source=f"sympy.geometry.{cls_name}",
            )
        )
        # Inspect members defined directly on cls (not inherited object/Basic noise)
        for member_name, raw_val in sorted(cls.__dict__.items()):
            if member_name.startswith("_") or member_name in _SKIP_MEMBERS:
                continue
            attr = getattr(cls, member_name, None)
            if attr is None:
                continue
            is_prop = isinstance(raw_val, property)
            sig = "" if is_prop else _safe_sig(attr)
            kind = _classify_member(member_name)
            decls.append(
                Decl(
                    system="sympy",
                    id=f"{cls_name}.{member_name}",
                    name=member_name,
                    kind=kind,
                    module=f"sympy.geometry.{cls_name}",
                    family=cls_name,
                    statement=f"{cls_name}.{member_name}{sig}" if not is_prop else f"@property {cls_name}.{member_name}",
                    text=_first_doc_line(attr),
                    source=f"sympy.geometry.{cls_name}.{member_name}",
                )
            )

    for fn_name in TOP_FUNCTIONS:
        fn = getattr(spg, fn_name, None)
        if fn is None:
            continue
        kind = "predicate" if fn_name.startswith(("is_", "are_")) else "construction"
        decls.append(
            Decl(
                system="sympy",
                id=fn_name,
                name=fn_name,
                kind=kind,
                module="sympy.geometry",
                family="Module Functions",
                statement=f"{fn_name}{_safe_sig(fn)}",
                text=_first_doc_line(fn),
                source=f"sympy.geometry.{fn_name}",
            )
        )

    return MinedSystem(
        system="sympy",
        decls=decls,
        source="python:sympy.geometry",
        version=sympy.__version__,
    )
