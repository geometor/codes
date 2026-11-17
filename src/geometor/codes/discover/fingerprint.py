"""Relabeling-invariant structural fingerprints for canonical forms."""

from __future__ import annotations

import itertools
from collections import defaultdict

from geometor.codes.discover.normalize import Atom, CanonicalForm

_MAX_PERMS = 120


def _encode(
    premises: tuple[Atom, ...],
    conclusions: tuple[Atom, ...],
    mapping: dict[str, str],
) -> str:
    def _fmt_side(atoms: tuple[Atom, ...]) -> str:
        mapped = sorted((a.pred, tuple(mapping[x] for x in a.args)) for a in atoms)
        return ";".join(f"{p}({','.join(args)})" for p, args in mapped)

    return f"{_fmt_side(premises)}=>{_fmt_side(conclusions)}"


def fingerprint_form(
    premises: tuple[Atom, ...],
    conclusions: tuple[Atom, ...],
) -> str:
    """Compute a structural fingerprint invariant under point relabeling.

    Args:
        premises: Premise `Atom`s.
        conclusions: Conclusion `Atom`s.

    Returns:
        A canonical string fingerprint, or ``""`` when both sides are empty.
    """
    if not premises and not conclusions:
        return ""

    sigs: dict[str, list[tuple[int, str, int, int]]] = defaultdict(list)
    for role, atoms in ((0, premises), (1, conclusions)):
        for atom in atoms:
            arity = len(atom.args)
            for idx, var in enumerate(atom.args):
                sigs[var].append((role, atom.pred, arity, idx))

    if not sigs:
        return _encode(premises, conclusions, {})

    # Group variables by their sorted structural signature.
    buckets: dict[tuple[tuple[int, str, int, int], ...], list[str]] = defaultdict(list)
    for var, occs in sigs.items():
        buckets[tuple(sorted(occs))].append(var)

    ordered_buckets = [sorted(buckets[k]) for k in sorted(buckets)]

    # Compute total permutations of tied buckets; cap for safety.
    total_perms = 1
    for b in ordered_buckets:
        for k in range(2, len(b) + 1):
            total_perms *= k

    if total_perms <= _MAX_PERMS:
        bucket_perms = [list(itertools.permutations(b)) for b in ordered_buckets]
        best = ""
        for combo in itertools.product(*bucket_perms):
            flat_vars = [v for grp in combo for v in grp]
            mapping = {v: f"P{i}" for i, v in enumerate(flat_vars)}
            cand = _encode(premises, conclusions, mapping)
            if not best or cand < best:
                best = cand
        return best

    # Fallback for large symmetric groups: deterministic order.
    flat_vars = [v for grp in ordered_buckets for v in grp]
    mapping = {v: f"P{i}" for i, v in enumerate(flat_vars)}
    return _encode(premises, conclusions, mapping)


def fingerprint_canonical(form: CanonicalForm) -> str:
    """Return the structural fingerprint of a `CanonicalForm`."""
    return fingerprint_form(form.premises, form.conclusions)
