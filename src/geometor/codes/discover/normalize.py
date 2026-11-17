"""Normalize base declarations into canonical predicate atoms."""

from __future__ import annotations

import re
from dataclasses import dataclass

from geometor.codes.lexicon import Lexicon
from geometor.codes.mine.schema import Decl

# Map raw AG / Newclid predicate names to canonical predicate symbols.
_AG_PRED_MAP = {
    "coll": "coll",
    "ncoll": "ncoll",
    "cyclic": "cyclic",
    "para": "para",
    "npara": "npara",
    "perp": "perp",
    "nperp": "nperp",
    "cong": "cong",
    "eqangle": "eq_angle",
    "eqangle6": "eq_angle",
    "eqratio": "eq_ratio",
    "eqratio3": "eq_ratio",
    "eqratio6": "eq_ratio",
    "midp": "midp",
    "sameside": "same_side",
    "nsameside": "not_same_side",
    "simtri": "sim_tri",
    "simtri2": "sim_tri",
    "simtrir": "sim_tri",
    "contri": "con_tri",
    "contri2": "con_tri",
    "contrir": "con_tri",
    "circle": "circle_center",
    "diff": "diff",
    "sameclock": "same_clock",
    "rconst": "ratio_const",
    "obtuse_angle": "obtuse_angle",
}

_SYM_CONG = re.compile(r"\|\(\s*([A-Za-z0-9_']+)\s*─\s*([A-Za-z0-9_']+)\s*\)\|\s*=\s*\|\(\s*([A-Za-z0-9_']+)\s*─\s*([A-Za-z0-9_']+)\s*\)\|")
_SYM_ANGLE = re.compile(r"∠\s*([A-Za-z0-9_']+):([A-Za-z0-9_']+):([A-Za-z0-9_']+)\s*=\s*∠\s*([A-Za-z0-9_']+):([A-Za-z0-9_']+):([A-Za-z0-9_']+)")
_SYM_BETWEEN = re.compile(r"\bbetween\s+([A-Za-z0-9_']+)\s+([A-Za-z0-9_']+)\s+([A-Za-z0-9_']+)")
_SYM_COLL = re.compile(r"\bcollinear\s+([A-Za-z0-9_']+)\s+([A-Za-z0-9_']+)\s+([A-Za-z0-9_']+)")
_SYM_ONLINE = re.compile(r"\b([A-Za-z0-9_']+)\.onLine\s+([A-Za-z0-9_']+)")
_SYM_ONCIRCLE = re.compile(r"\b([A-Za-z0-9_']+)\.onCircle\s+([A-Za-z0-9_']+)")
_SYM_SAMESIDE = re.compile(r"\b([A-Za-z0-9_']+)\.sameSide\s+([A-Za-z0-9_']+)\s+([A-Za-z0-9_']+)")
_SYM_OPPSIDE = re.compile(r"\b([A-Za-z0-9_']+)\.opposingSides\s+([A-Za-z0-9_']+)\s+([A-Za-z0-9_']+)")
_SYM_CENTRE = re.compile(r"\b([A-Za-z0-9_']+)\.isCentre\s+([A-Za-z0-9_']+)")
_SYM_FORM_TRI = re.compile(r"\bformTriangle\s+([A-Za-z0-9_']+)\s+([A-Za-z0-9_']+)\s+([A-Za-z0-9_']+)\s+([A-Za-z0-9_']+)\s+([A-Za-z0-9_']+)\s+([A-Za-z0-9_']+)")
_SYM_NOT_INTERSECT = re.compile(r"¬\s*\(?\s*([A-Za-z0-9_']+)\.intersectsLine\s+([A-Za-z0-9_']+)\s*\)?")
_SYM_INTERSECT = re.compile(r"\b([A-Za-z0-9_']+)\.intersectsLine\s+([A-Za-z0-9_']+)")
_SYM_CON_TRI = re.compile(r"\(?\s*△\s*([A-Za-z0-9_']+):([A-Za-z0-9_']+):([A-Za-z0-9_']+)\s*\)?\.congruent\s+\(?\s*△\s*([A-Za-z0-9_']+):([A-Za-z0-9_']+):([A-Za-z0-9_']+)\s*\)?")
_SYM_SIM_TRI = re.compile(r"\(?\s*△\s*([A-Za-z0-9_']+):([A-Za-z0-9_']+):([A-Za-z0-9_']+)\s*\)?\.similar\s+\(?\s*△\s*([A-Za-z0-9_']+):([A-Za-z0-9_']+):([A-Za-z0-9_']+)\s*\)?")


@dataclass(frozen=True)
class Atom:
    """One canonical predicate atom ``pred(arg1, arg2, ...)``."""

    pred: str
    args: tuple[str, ...]

    def format(self) -> str:
        """Return ``pred(a, b, ...)`` string."""
        return f"{self.pred}({', '.join(self.args)})"


@dataclass(frozen=True)
class CanonicalForm:
    """Normalized ``premises => conclusions`` representation of a declaration."""

    premises: tuple[Atom, ...]
    conclusions: tuple[Atom, ...]
    lexicon_concept: str = ""

    def format(self) -> str:
        """Return a readable canonical formula."""
        lhs = ", ".join(a.format() for a in self.premises)
        rhs = ", ".join(a.format() for a in self.conclusions)
        if lhs and rhs:
            return f"{lhs} => {rhs}"
        return rhs or lhs or self.lexicon_concept


def _parse_ag_atom(raw: str) -> Atom | None:
    parts = raw.strip().split()
    if not parts:
        return None
    raw_pred = parts[0]
    pred = _AG_PRED_MAP.get(raw_pred, raw_pred)
    args = tuple(p.upper() if len(p) == 1 and p.isalpha() else p for p in parts[1:])
    # Normalize 6-arg eqangle/eqratio to 8-arg form where possible? Keep exact args
    # for faithful representation; eqangle6 A B C D E F -> (A,B, B,C, D,E, E,F)
    if raw_pred == "eqangle6" and len(args) == 6:
        a, b, c, d, e, f = args
        args = (a, b, b, c, d, e, e, f)
    elif raw_pred == "eqratio6" and len(args) == 6:
        a, b, c, d, e, f = args
        args = (a, b, c, d, e, f)
    return Atom(pred=pred, args=args)


def _extract_lean_atoms(clause: str) -> tuple[Atom, ...]:
    """Extract canonical atoms from one side of a Lean implication."""
    atoms: list[Atom] = []
    for rx, pred in (
        (_SYM_CONG, "cong"),
        (_SYM_ANGLE, "eq_angle"),
        (_SYM_BETWEEN, "between"),
        (_SYM_COLL, "coll"),
        (_SYM_ONLINE, "on_line"),
        (_SYM_ONCIRCLE, "on_circle"),
        (_SYM_SAMESIDE, "same_side"),
        (_SYM_OPPSIDE, "opposite_sides"),
        (_SYM_CENTRE, "is_center"),
        (_SYM_FORM_TRI, "form_triangle"),
        (_SYM_NOT_INTERSECT, "para"),
        (_SYM_CON_TRI, "con_tri"),
        (_SYM_SIM_TRI, "sim_tri"),
    ):
        for m in rx.finditer(clause):
            atoms.append(Atom(pred=pred, args=tuple(m.groups())))
    if not _SYM_NOT_INTERSECT.search(clause):
        for m in _SYM_INTERSECT.finditer(clause):
            atoms.append(Atom(pred="npara", args=tuple(m.groups())))
    return tuple(atoms)


def normalize_decl(decl: Decl, lexicon: Lexicon | None = None) -> CanonicalForm:
    """Normalize a mined `Decl` into a `CanonicalForm`.

    Args:
        decl: Mined declaration.
        lexicon: Optional loaded `Lexicon` for concept resolution.

    Returns:
        A `CanonicalForm` (possibly empty if the declaration is purely
        natural-language or non-equational).
    """
    concept = ""
    if lexicon is not None:
        sys_key = "system_e" if decl.system == "leaneuclid" else (
            "model" if decl.system == "geometor_model" else decl.system
        )
        entry = lexicon.resolve(sys_key, decl.name) or lexicon.resolve(sys_key, decl.id)
        if entry is not None:
            concept = entry.name

    if decl.system in ("alphageometry", "newclid"):
        premises = tuple(a for raw in decl.premises if (a := _parse_ag_atom(raw)) is not None)
        conclusions = tuple(a for raw in decl.conclusions if (a := _parse_ag_atom(raw)) is not None)
        return CanonicalForm(premises=premises, conclusions=conclusions, lexicon_concept=concept)

    if decl.system == "leaneuclid" and decl.statement:
        stmt = decl.statement
        if "→" in stmt:
            lhs, rhs = stmt.rsplit("→", 1)
            return CanonicalForm(
                premises=_extract_lean_atoms(lhs),
                conclusions=_extract_lean_atoms(rhs),
                lexicon_concept=concept,
            )
        return CanonicalForm(
            premises=(),
            conclusions=_extract_lean_atoms(stmt),
            lexicon_concept=concept,
        )

    return CanonicalForm(premises=(), conclusions=(), lexicon_concept=concept)
