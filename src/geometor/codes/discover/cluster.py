"""Cluster normalized base declarations into proposed principles."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any

from geometor.codes.context import ContextManifest
from geometor.codes.discover.fingerprint import fingerprint_canonical, fingerprint_form
from geometor.codes.discover.normalize import CanonicalForm, normalize_decl
from geometor.codes.lexicon import Lexicon
from geometor.codes.mine.schema import Decl, load_snapshot
from geometor.codes.registry import default_resources_dir

# Curated cross-system links for canonical theorems where textual wording
# differs from symbolic rule syntax.
_EUCLID_THEOREM_SLUGS: dict[str, tuple[str, str, str]] = {
    "I.1": ("equilateral_apex", "construction", "congruence"),
    "I.2": ("transfer_segment", "construction", "congruence"),
    "I.3": ("cut_equal_segment", "construction", "congruence"),
    "I.4": ("sas_congruence", "theorem", "congruence"),
    "I.5": ("isosceles_base_angles", "theorem", "congruence"),
    "I.6": ("isosceles_converse", "theorem", "congruence"),
    "I.8": ("sss_congruence", "theorem", "congruence"),
    "I.9": ("angle_bisector", "construction", "congruence"),
    "I.10": ("midpoint", "construction", "incidence"),
    "I.11": ("perpendicular_line", "construction", "congruence"),
    "I.12": ("perpendicular_foot", "construction", "congruence"),
    "I.13": ("supplementary_adjacent_angles", "theorem", "congruence"),
    "I.15": ("vertical_angles", "theorem", "congruence"),
    "I.16": ("exterior_angle_inequality", "theorem", "order"),
    "I.20": ("triangle_inequality", "theorem", "order"),
    "I.23": ("copy_angle", "construction", "congruence"),
    "I.26": ("asa_aas_congruence", "theorem", "congruence"),
    "I.27": ("alternate_angles_parallel", "theorem", "parallel"),
    "I.29": ("parallel_alternate_angles", "theorem", "parallel"),
    "I.30": ("parallel_transitivity", "theorem", "parallel"),
    "I.31": ("parallel_line", "construction", "parallel"),
    "I.32": ("triangle_angle_sum", "theorem", "parallel"),
    "I.33": ("parallelogram_opposite_sides", "theorem", "parallel"),
    "I.34": ("parallelogram_properties", "theorem", "parallel"),
    "I.46": ("square_on_segment", "construction", "area"),
    "I.47": ("pythagorean", "theorem", "area"),
    "I.48": ("pythagorean_converse", "theorem", "area"),
    "I.post.1": ("line_through", "postulate", "incidence"),
    "I.post.2": ("extension", "postulate", "order"),
    "I.post.3": ("circle_through", "postulate", "circle"),
    "I.post.4": ("right_angles_equal", "postulate", "congruence"),
    "I.post.5": ("parallel_postulate", "postulate", "parallel"),
    "III.1": ("circle_center", "construction", "circle"),
    "III.17": ("tangent_lines", "construction", "circle"),
    "III.20": ("central_inscribed_angle", "theorem", "circle"),
    "III.21": ("inscribed_angles_same_arc", "theorem", "circle"),
    "III.22": ("cyclic_quadrilateral_angles", "theorem", "circle"),
    "III.31": ("thales_semicircle", "theorem", "circle"),
    "III.32": ("alternate_segment_angle", "theorem", "circle"),
    "III.35": ("intersecting_chords", "theorem", "circle"),
    "III.36": ("tangent_secant_power", "theorem", "circle"),
    "VI.2": ("thales_intercept", "theorem", "similarity"),
    "VI.3": ("angle_bisector_ratio", "theorem", "similarity"),
    "VI.4": ("aa_similarity", "theorem", "similarity"),
    "VI.5": ("sss_similarity", "theorem", "similarity"),
    "VI.6": ("sas_similarity", "theorem", "similarity"),
    "VI.11": ("third_proportional", "construction", "similarity"),
    "VI.13": ("mean_proportional", "construction", "similarity"),
}

_AG_NEWCLID_SLUGS: dict[str, tuple[str, str, str]] = {
    "r00": ("perpendiculars_parallel", "inference_rule", "parallel"),
    "r01": ("concyclic_equidistant", "definition", "circle"),
    "r02": ("parallel_from_inclination", "inference_rule", "parallel"),
    "r03": ("inscribed_angles_same_arc", "theorem", "circle"),
    "r04": ("concyclic_from_equal_angles", "theorem", "circle"),
    "r05": ("equal_arcs_equal_chords", "theorem", "circle"),
    "r06": ("midline_parallel", "theorem", "parallel"),
    "r07": ("thales_intercept", "theorem", "similarity"),
    "r09": ("triangle_angle_sum", "theorem", "parallel"),
    "r11": ("angle_bisector_ratio_converse", "theorem", "similarity"),
    "r12": ("angle_bisector_ratio", "theorem", "similarity"),
    "r13": ("isosceles_base_angles", "theorem", "congruence"),
    "r14": ("isosceles_converse", "theorem", "congruence"),
    "r15": ("alternate_segment_angle", "theorem", "circle"),
    "r16": ("alternate_segment_tangent", "theorem", "circle"),
    "r17": ("central_inscribed_angle", "theorem", "circle"),
    "r19": ("thales_semicircle_converse", "theorem", "circle"),
    "r20": ("thales_semicircle", "theorem", "circle"),
    "r25": ("parallelogram_diagonals_bisect", "theorem", "parallel"),
    "r33": ("sss_congruence", "theorem", "congruence"),
    "r34": ("aa_similarity", "theorem", "similarity"),
    "r36": ("asa_aas_congruence", "theorem", "congruence"),
    "r43": ("orthocenter_concurrence", "theorem", "triangle_center"),
    "r44": ("pappus_hexagon", "theorem", "projective"),
    "r45": ("simson_line", "theorem", "circle"),
    "r46": ("incenter_concurrence", "theorem", "triangle_center"),
    "r47": ("circumcenter_concurrence", "theorem", "triangle_center"),
    "r48": ("centroid_concurrence", "theorem", "triangle_center"),
    "r57": ("pythagorean", "theorem", "area"),
    "r60": ("sss_similarity", "theorem", "similarity"),
    "r62": ("sas_similarity", "theorem", "similarity"),
    "r64": ("sss_congruence", "theorem", "congruence"),
    "r66": ("sas_congruence", "theorem", "congruence"),
    "r70": ("harmonic_conjugate_projective", "theorem", "projective"),
}

_SYST_E_SLUGS: dict[str, tuple[str, str, str]] = {
    "pasch_1": ("pasch", "axiom", "order"),
    "pasch_2": ("pasch", "axiom", "order"),
    "pasch_3": ("pasch", "axiom", "order"),
    "pasch_4": ("pasch", "axiom", "order"),
    "between_symm": ("betweenness_symmetry", "axiom", "order"),
    "between_trans_in": ("betweenness_transitivity", "axiom", "order"),
    "between_trans_out": ("betweenness_transitivity", "axiom", "order"),
    "two_points_determine_line": ("line_uniqueness", "axiom", "incidence"),
    "parallel_line_unique": ("playfair_uniqueness", "axiom", "parallel"),
    "superposition": ("superposition", "axiom", "congruence"),
    "centre_unique": ("center_uniqueness", "axiom", "circle"),
}


@dataclass
class PrincipleMember:
    """One base-system declaration belonging to a principle."""

    key: str
    system: str
    id: str
    name: str
    kind: str
    statement: str = ""
    canonical_form: str = ""
    source: str = ""
    line: int = 0


@dataclass
class PrincipleRelation:
    """Directed relation between two principles."""

    relation: str
    target_id: str


@dataclass
class Principle:
    """A proposed or accepted geometric principle."""

    id: str
    title: str
    kind: str
    family: str
    statement: str = ""
    canonical_form: str = ""
    fingerprint: str = ""
    status: str = "proposed"
    euclid_refs: list[str] = field(default_factory=list)
    members: list[PrincipleMember] = field(default_factory=list)
    relations: list[PrincipleRelation] = field(default_factory=list)
    linked: list[dict[str, Any]] = field(default_factory=list)


@dataclass
class OutOfScopeItem:
    """A base declaration explicitly marked out of scope for the code canon."""

    key: str
    system: str
    id: str
    kind: str
    reason: str


@dataclass
class Catalog:
    """Complete discovery catalog covering 100% of base items."""

    principles: list[Principle]
    out_of_scope: list[OutOfScopeItem]
    stats: dict[str, int]

    def by_id(self, pid: str) -> Principle | None:
        """Return principle by ID."""
        for p in self.principles:
            if p.id == pid:
                return p
        return None


def _slugify(text: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")
    return s or "principle"


def _infer_family(decl: Decl, form: CanonicalForm, lexicon: Lexicon) -> str:
    if form.lexicon_concept and form.lexicon_concept in lexicon.entries:
        return lexicon.entries[form.lexicon_concept].family
    preds = {a.pred for a in (*form.premises, *form.conclusions)}
    if preds & {"between", "same_side", "opposite_sides"}:
        return "order"
    if preds & {"cyclic", "on_circle", "is_center", "circle_center"}:
        return "circle"
    if preds & {"para", "npara"}:
        return "parallel"
    if preds & {"sim_tri", "eq_ratio"}:
        return "similarity"
    if preds & {"cong", "eq_angle", "perp", "con_tri"}:
        return "congruence"
    if preds & {"coll", "ncoll", "on_line", "midp"}:
        return "incidence"
    if decl.family:
        return _slugify(decl.family)
    return "general"


def _cluster_key_for(
    decl: Decl,
    form: CanonicalForm,
    fp: str,
) -> tuple[str, str, str, str]:
    """Return ``(cluster_key, title, kind, family_hint)``."""
    # 1. Euclid direct mapping
    if decl.system == "euclid" and decl.id in _EUCLID_THEOREM_SLUGS:
        slug, kind, fam = _EUCLID_THEOREM_SLUGS[decl.id]
        return slug, slug.replace("_", " "), kind, fam

    # 2. LeanEuclid Book I -> Euclid I.N
    euclid_ref = str(decl.extra.get("euclid", ""))
    if decl.system == "leaneuclid" and euclid_ref in _EUCLID_THEOREM_SLUGS:
        slug, kind, fam = _EUCLID_THEOREM_SLUGS[euclid_ref]
        return slug, slug.replace("_", " "), kind, fam
    if decl.system == "leaneuclid" and euclid_ref:
        slug = f"euclid_{_slugify(euclid_ref)}"
        return slug, f"Euclid {euclid_ref}", "theorem", "general"

    # 3. System E named axioms
    if decl.system == "leaneuclid" and decl.name in _SYST_E_SLUGS:
        slug, kind, fam = _SYST_E_SLUGS[decl.name]
        return slug, slug.replace("_", " "), kind, fam

    # 4. AG / Newclid named rules
    if decl.system == "alphageometry" and decl.name in _AG_NEWCLID_SLUGS:
        slug, kind, fam = _AG_NEWCLID_SLUGS[decl.name]
        return slug, slug.replace("_", " "), kind, fam
    if decl.system == "newclid":
        ag_rule = str(decl.extra.get("ag_rule", ""))
        if ag_rule in _AG_NEWCLID_SLUGS:
            slug, kind, fam = _AG_NEWCLID_SLUGS[ag_rule]
            return slug, slug.replace("_", " "), kind, fam
        if decl.name in _AG_NEWCLID_SLUGS:
            slug, kind, fam = _AG_NEWCLID_SLUGS[decl.name]
            return slug, slug.replace("_", " "), kind, fam

    # 5. Lexicon concept
    if form.lexicon_concept:
        return form.lexicon_concept, form.lexicon_concept.replace("_", " "), decl.kind, ""

    # 6. Fingerprint cluster for formal rules without curated slug
    if fp:
        return f"fp:{fp}", decl.text or decl.name, decl.kind, ""

    # 7. Singleton fallback (Euclid items, UniGeo items, SymPy methods, etc.)
    if decl.system == "euclid":
        slug = f"euclid_{_slugify(decl.id)}"
        return slug, f"Euclid {decl.id}", decl.kind, ""
    slug = f"{decl.system}_{_slugify(decl.id)}"
    return slug, decl.text or decl.name, decl.kind, ""


def _out_of_scope_reason(decl: Decl) -> str:
    if decl.system == "euclid" and decl.extra.get("in_canon") is False:
        return "not_yet_in_code_canon"
    if decl.system == "geometor_model" and decl.kind in ("foundation", "method"):
        return "api_plumbing"
    if decl.system == "sympy" and decl.kind == "method":
        return "api_method"
    return ""


def discover_principles(
    snap_dir: Path | None = None,
    lexicon: Lexicon | None = None,
    manifest: ContextManifest | None = None,
) -> Catalog:
    """Run Phase 2 discovery across all mined base snapshots.

    Every base declaration is either assigned to a `Principle` cluster or
    recorded in `out_of_scope`.

    Args:
        snap_dir: Snapshot directory (defaults to ``resources/mined``).
        lexicon: Optional `Lexicon`.
        manifest: Optional `ContextManifest`.

    Returns:
        A `Catalog`.
    """
    res_dir = default_resources_dir()
    sdir = snap_dir or res_dir / "mined"
    lex = lexicon or Lexicon.load()
    ctx = manifest or ContextManifest.load()

    clusters: dict[str, list[tuple[Decl, CanonicalForm, str, str, str, str]]] = defaultdict(list)
    fp_to_key: dict[str, str] = {}
    out_of_scope: list[OutOfScopeItem] = []
    total_items = 0

    for sys_spec in ctx.by_role("base"):
        decls = load_snapshot(sys_spec.id, sdir)
        for decl in decls:
            total_items += 1
            reason = _out_of_scope_reason(decl)
            if reason:
                out_of_scope.append(
                    OutOfScopeItem(
                        key=decl.key,
                        system=decl.system,
                        id=decl.id,
                        kind=decl.kind,
                        reason=reason,
                    )
                )
                continue

            form = normalize_decl(decl, lex)
            fp = fingerprint_canonical(form)
            ckey, title, kind, fam_hint = _cluster_key_for(decl, form, fp)

            # Merge fingerprint duplicates into an existing named cluster if present.
            if fp and ckey.startswith("fp:") and fp in fp_to_key:
                ckey = fp_to_key[fp]
            elif fp and not ckey.startswith("fp:") and fp not in fp_to_key:
                fp_to_key[fp] = ckey

            clusters[ckey].append((decl, form, fp, title, kind, fam_hint))

    # Build Principle objects with stable, unique IDs.
    principles: list[Principle] = []
    fp_to_pid: dict[str, str] = {}
    used_ids: set[str] = set()
    fp_seq = 0

    for ckey in sorted(clusters):
        items = clusters[ckey]
        first_decl, first_form, first_fp, title, kind, fam_hint = items[0]
        if ckey.startswith("fp:"):
            fp_seq += 1
            base_id = _slugify(first_decl.text or first_decl.name)
            pid = base_id if base_id not in used_ids else f"{base_id}_{fp_seq}"
        else:
            pid = ckey
            if pid in used_ids:
                pid = f"{pid}_{len(used_ids)}"
        used_ids.add(pid)

        family = fam_hint or _infer_family(first_decl, first_form, lex)
        best_form = next((f.format() for _, f, _, _, _, _ in items if f.premises or f.conclusions), first_form.format())
        best_fp = next((fp for _, _, fp, _, _, _ in items if fp), "")
        if best_fp and best_fp not in fp_to_pid:
            fp_to_pid[best_fp] = pid

        statement = ""
        for d, _, _, _, _, _ in items:
            if d.system == "euclid" and d.text:
                statement = d.text
                break
        if not statement:
            for d, _, _, _, _, _ in items:
                if d.text:
                    statement = d.text
                    break
        if not statement:
            statement = first_decl.statement

        euclid_refs = sorted({
            d.id if d.system == "euclid" else str(d.extra.get("euclid", ""))
            for d, _, _, _, _, _ in items
            if (d.system == "euclid" or d.extra.get("euclid"))
        } - {""})

        members = [
            PrincipleMember(
                key=d.key,
                system=d.system,
                id=d.id,
                name=d.name,
                kind=d.kind,
                statement=d.statement,
                canonical_form=f.format(),
                source=d.source,
                line=d.line,
            )
            for d, f, _, _, _, _ in items
        ]

        principles.append(
            Principle(
                id=pid,
                title=title,
                kind=kind,
                family=family,
                statement=statement,
                canonical_form=best_form,
                fingerprint=best_fp,
                status="proposed",
                euclid_refs=euclid_refs,
                members=members,
            )
        )

    # Detect converse relations using normalized forms.
    form_by_pid: dict[str, CanonicalForm] = {}
    decl_index: dict[str, Decl] = {}
    for sys_spec in ctx.by_role("base"):
        for d in load_snapshot(sys_spec.id, sdir):
            decl_index[d.key] = d

    for p in principles:
        for m in p.members:
            d = decl_index.get(m.key)
            if d is None:
                continue
            f = normalize_decl(d, lex)
            if f.premises and f.conclusions:
                form_by_pid[p.id] = f
                break

    for p in principles:
        f = form_by_pid.get(p.id)
        if f is None:
            continue
        rev_fp = fingerprint_form(f.conclusions, f.premises)
        target = fp_to_pid.get(rev_fp)
        if target and target != p.id:
            p.relations.append(PrincipleRelation(relation="converse", target_id=target))

    principles.sort(key=lambda p: (p.family, p.id))
    assigned = sum(len(p.members) for p in principles)
    stats = {
        "total_base_items": total_items,
        "assigned_items": assigned,
        "out_of_scope_items": len(out_of_scope),
        "unassigned_items": total_items - assigned - len(out_of_scope),
        "principles": len(principles),
        "multi_system_principles": sum(
            1 for p in principles if len({m.system for m in p.members}) > 1
        ),
    }
    return Catalog(principles=principles, out_of_scope=out_of_scope, stats=stats)


def save_catalog(catalog: Catalog, path: Path | None = None) -> Path:
    """Write the discovered catalog deterministically to JSON."""
    out = path or default_resources_dir() / "discovered" / "catalog.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "stats": catalog.stats,
        "principles": [asdict(p) for p in catalog.principles],
        "out_of_scope": [asdict(o) for o in catalog.out_of_scope],
    }
    out.write_text(
        json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return out


def load_catalog(path: Path | None = None) -> Catalog:
    """Load a saved discovery catalog from JSON."""
    src = path or default_resources_dir() / "discovered" / "catalog.json"
    data = json.loads(src.read_text(encoding="utf-8"))
    principles = [
        Principle(
            id=p["id"],
            title=p["title"],
            kind=p["kind"],
            family=p["family"],
            statement=p.get("statement", ""),
            canonical_form=p.get("canonical_form", ""),
            fingerprint=p.get("fingerprint", ""),
            status=p.get("status", "proposed"),
            euclid_refs=p.get("euclid_refs", []),
            members=[PrincipleMember(**m) for m in p.get("members", [])],
            relations=[PrincipleRelation(**r) for r in p.get("relations", [])],
            linked=p.get("linked", []),
        )
        for p in data.get("principles", [])
    ]
    oos = [OutOfScopeItem(**o) for o in data.get("out_of_scope", [])]
    return Catalog(principles=principles, out_of_scope=oos, stats=data.get("stats", {}))
