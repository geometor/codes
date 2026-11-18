"""Generate the CODES documentation views from curated data and the catalog.

The site is organized around *how each system knows* (truth foundations), not
around the raw principle catalog:

* ``foundations/`` — Truth Ladder, Trust Stack, trusted-component graph,
  one card per system, a side-by-side comparison, and the connections graphs.
* ``showcase/`` — a few theorems realized side by side ("one theorem, many
  foundations"), with exact L1 witnesses and symbolic L2 (generic) witnesses.
* ``catalog/`` — the discovered principle catalog as one searchable page plus
  the exact witness entries.

Everything is generated from ``resources/foundations.toml``,
``resources/showcase.toml``, and ``resources/discovered/catalog.json``.
"""

from __future__ import annotations

import json
import shutil
from dataclasses import asdict
from pathlib import Path

from geometor.codes.discover.cluster import Catalog, Principle, load_catalog
from geometor.codes.foundations import (
    AXES,
    LAYERS,
    Foundations,
    Showcase,
    System,
    load_foundations,
    load_showcase,
)
from geometor.codes.generic import GENERIC_GAPS, generic_witness
from geometor.codes.graphs import (
    STATUS_COLORS,
    bridges_graph,
    chain_graph,
    ladder_graph,
    ontology_graph,
    overlap_graph,
    shared_principles,
    showcase_graph,
    trust_graph,
)
from geometor.codes.mine.schema import load_manifest
from geometor.codes.registry import default_resources_dir
from geometor.codes.render import render_svg
from geometor.codes.verify import KNOWN_GAPS, PILOT_BUILDERS, build_pilot_model, verify_principle

PILOT_IDS: tuple[str, ...] = tuple(PILOT_BUILDERS) + tuple(KNOWN_GAPS)

_RAW_ROLE = [".. role:: raw-html(raw)", "   :format: html", ""]


def _nav(order: int, title: str) -> list[str]:
    """Docinfo fields that place a page in the publish header navigation."""
    return [":navigation: header", f":order: {order}", f":nav_title: {title}", ""]


# --------------------------------------------------------------------------- helpers


def _rst_heading(title: str, char: str = "=") -> str:
    return f"{title}\n{char * len(title)}\n"


def _escape_rst(text: str) -> str:
    """Collapse whitespace and escape RST inline markup characters."""
    flat = " ".join(str(text).split())
    for ch in ("\\", "*", "`", "|", "_"):
        flat = flat.replace(ch, "\\" + ch)
    return flat


def _graphviz(dot: str, caption: str = "", alt: str = "") -> list[str]:
    lines = [".. graphviz::", "   :align: center"]
    if caption:
        lines.append(f"   :caption: {caption}")
    if alt:
        lines.append(f"   :alt: {alt}")
    lines.append("")
    lines.extend(f"   {ln}" for ln in dot.splitlines())
    lines.append("")
    return lines


def _code(lang: str, code: str, indent: str = "") -> list[str]:
    lines = [f"{indent}.. code-block:: {lang or 'text'}", ""]
    lines.extend(f"{indent}   {ln}" if ln.strip() else "" for ln in code.splitlines())
    lines.append("")
    return lines


def _badge(text: str, color: str) -> str:
    return f':raw-html:`<span class="codes-status" style="background:{color}">{text}</span>`'


def _link(label: str, url: str) -> str:
    if not url:
        return _escape_rst(label)
    if url.startswith("http"):
        return f"`{_escape_rst(label)} <{url}>`__"
    return f"``{url}``"


def _json_block(element_id: str, payload: object) -> list[str]:
    raw = json.dumps(payload, ensure_ascii=False, indent=0).replace("</", "<\\/")
    return [
        ".. raw:: html",
        "",
        f'   <script type="application/json" id="{element_id}">',
        *(f"   {ln}" for ln in raw.splitlines()),
        "   </script>",
        "",
    ]


def _write(path: Path, lines: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def _sorted_systems(fnd: Foundations) -> list[System]:
    rank = {lv.id: lv.rank for lv in fnd.levels}
    return sorted(fnd.systems, key=lambda s: (-rank.get(s.ladder, 0), not s.core, s.short.lower()))


# --------------------------------------------------------------------------- foundations


def _atlas_include(fnd: Foundations) -> list[str]:
    return [
        ".. raw:: html",
        "",
        '   <div class="codes-atlas" data-src="codes-atlas-data"></div>',
        "",
        *_json_block("codes-atlas-data", fnd.to_json()),
    ]


def _write_foundations_index(fnd: Foundations, out: Path) -> None:
    lines = [
        ".. _foundations-index:",
        "",
        _rst_heading("Truth Foundations"),
        fnd.thesis,
        "",
        "Two lenses organize the comparison: the **Truth Ladder** ranks the *strength of the claim* a system "
        "certifies, and the **Trust Stack** decomposes *how* it certifies it. The interactive Atlas on the "
        ":doc:`home page </index>` shows both at once.",
        "",
        _rst_heading("Truth Ladder", "-"),
        "Rungs rank claims, not quality: a CAS witness (L1) and a kernel-checked proof (L4) answer different questions. "
        "Dashed blue edges are *lifts* — routes by which a system's claims could climb. Click a system to open its card.",
        "",
        *_graphviz(ladder_graph(fnd, depth=1), alt="Truth Ladder"),
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 8 16 36 40",
        "",
        "   * - Level",
        "     - Name",
        "     - Claim certified",
        "     - Systems",
    ]
    for lv in sorted(fnd.levels, key=lambda x: x.rank):
        members = ", ".join(f":doc:`{s.short} <cards/{s.id}>`" for s in fnd.systems_at(lv.id)) or "—"
        lines.extend([
            f"   * - {_badge(lv.id, lv.color)}",
            f"     - {lv.name}",
            f"     - {_escape_rst(lv.claim)}",
            f"     - {members}",
        ])
    lines.extend(["", _rst_heading("The Trust Stack", "-"),
                  "Every system is described by the same seven layers. The **checker** layer is the trusted core.", "",
                  ".. list-table::", "   :header-rows: 1", "   :widths: 20 80", "", "   * - Layer", "     - Question"])
    for _, label, question in LAYERS:
        lines.extend([f"   * - **{label}**", f"     - {question}"])
    lines.extend([
        "",
        _rst_heading("Who Trusts What", "-"),
        "Systems on the left, the components they must trust on the right. Shared hubs — the Lean kernel, SymPy, "
        "the numeric diagram — show where trust concentrates.",
        "",
        *_graphviz(trust_graph(fnd, depth=1), alt="Trusted components"),
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 18 9 18 18 37",
        "",
        "   * - Component",
        "     - Kind",
        "     - Size",
        "     - Trusted by",
        "     - Note",
    ])
    for t in fnd.trusted:
        users = ", ".join(f":doc:`{s.short} <cards/{s.id}>`" for s in fnd.systems if t.id in s.trusts) or "—"
        lines.extend([
            f"   * - **{_escape_rst(t.name)}**",
            f"     - {t.kind}",
            f"     - {_escape_rst(t.size)}",
            f"     - {users}",
            f"     - {_escape_rst(t.note)}",
        ])
    lines.extend([
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "",
        "   cards/index",
        "   compare",
        "   connections",
        "   findings",
        "",
    ])
    _write(out / "index.rst", _nav(1, "Foundations") + _RAW_ROLE + lines)


def _write_card(
    fnd: Foundations,
    s: System,
    showcase: list[Showcase],
    counts: dict[str, tuple[int, int]],
    out: Path,
) -> None:
    lv = fnd.level(s.ladder)
    lv_color = lv.color if lv else "#eeeeee"
    meta = [
        f"{_badge(s.ladder + ' ' + (lv.name if lv else ''), lv_color)}",
        f"**Archetype:** ``{s.archetype}``",
    ]
    if s.upstream:
        meta.append(_link("upstream", s.upstream))
    if s.dossier:
        meta.append(f":doc:`dossier </{s.dossier}>`")
    lines = [
        f".. _card-{s.id}:",
        "",
        _rst_heading(s.name),
        " · ".join(meta),
        "",
        ".. epigraph::",
        "",
        f"   {_escape_rst(s.summary)}",
        "",
        _rst_heading("Trust chain", "-"),
        *_graphviz(chain_graph(fnd, s), alt=f"{s.short} trust chain"),
        ".. list-table::",
        "   :widths: 18 82",
        "",
    ]
    for key, label, question in LAYERS:
        lines.extend([f"   * - **{label}**", f"     - {_escape_rst(s.stack.get(key, '—'))}  *({question})*"])
    lines.extend(["", _rst_heading("At a glance", "-")])
    for key, label in AXES:
        lines.append(f":{label}: {_escape_rst(s.axes.get(key, '—'))}")
    trusted = [fnd.trusted_component(t) for t in s.trusts]
    lines.append(":Trusts: " + (" · ".join(f"{t.name} ({_escape_rst(t.size)})" for t in trusted if t) or "—"))
    if s.id in counts:
        total, multi = counts[s.id]
        lines.append(f":Catalog: {total} principles ({multi} shared with other systems) — :doc:`search </catalog/index>`")
    lines.append("")
    if s.example_code:
        lines.extend([_rst_heading("A statement in its own language", "-"), *_code(s.example_lang, s.example_code)])
        if s.example_source:
            lines.extend([f"Source: {_link(s.example_source.rsplit('/', 1)[-1], s.example_source)}", ""])
    if s.findings:
        lines.append(_rst_heading("Findings", "-"))
        lines.extend(f"- {_escape_rst(f)}" for f in s.findings)
        lines.append("")
    appearances = [(sc, r) for sc in showcase for r in sc.realizations if r.system == s.id]
    if appearances:
        lines.extend([_rst_heading("In the showcase", "-")])
        for sc, r in appearances:
            label = f"{sc.euclid} {sc.title}".strip()
            lines.append(
                f"- :doc:`{_escape_rst(label)} </showcase/{sc.id}>` — "
                f"{_badge(r.status, STATUS_COLORS.get(r.status, '#eee'))} ``{r.ident}``"
            )
        lines.append("")
    if s.refs:
        lines.append(_rst_heading("References", "-"))
        lines.extend(f"- {_link(r['label'], r.get('url', ''))}" for r in s.refs)
        lines.append("")
    _write(out / f"{s.id}.rst", _RAW_ROLE + lines)


def _write_cards(fnd: Foundations, showcase: list[Showcase], cat: Catalog, out: Path) -> int:
    if out.exists():
        shutil.rmtree(out)
    counts: dict[str, tuple[int, int]] = {}
    for p in cat.principles:
        systems = {m.system for m in p.members}
        for sid in systems:
            total, multi = counts.get(sid, (0, 0))
            counts[sid] = (total + 1, multi + (1 if len(systems) > 1 else 0))
    ordered = _sorted_systems(fnd)
    for s in ordered:
        _write_card(fnd, s, showcase, counts, out)
    lines = [
        ".. _cards-index:",
        "",
        _rst_heading("System Cards"),
        "One card per system, all with the same template: the seven-layer trust chain, comparison axes, a real "
        "statement in the system's own language, findings from source audits, and references.",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 16 9 16 59",
        "",
        "   * - System",
        "     - Level",
        "     - Trusted core",
        "     - Why believe it?",
    ]
    for s in ordered:
        lv = fnd.level(s.ladder)
        core = ", ".join(t.name for t in (fnd.trusted_component(x) for x in s.trusts) if t)
        lines.extend([
            f"   * - :doc:`{s.short} <{s.id}>`",
            f"     - {_badge(s.ladder, lv.color if lv else '#eee')}",
            f"     - {_escape_rst(core)}",
            f"     - {_escape_rst(s.summary)}",
        ])
    lines.extend(["", ".. toctree::", "   :hidden:", "", *[f"   {s.id}" for s in ordered], ""])
    _write(out / "index.rst", _RAW_ROLE + lines)
    return len(ordered)


def _write_compare(fnd: Foundations, out: Path) -> None:
    ordered = _sorted_systems(fnd)
    lines = [
        ".. _foundations-compare:",
        "",
        _rst_heading("Side by Side"),
        "The same questions asked of every system. Systems are ordered from the strongest claim (top of the ladder) "
        "down. For an interactive version, use the Atlas on the :doc:`home page </index>`.",
        "",
        _rst_heading("Comparison axes", "-"),
        ".. list-table::",
        "   :header-rows: 1",
        "   :class: codes-compare",
        "",
        "   * - System",
        *[f"     - {label}" for _, label in AXES],
    ]
    for s in ordered:
        lv = fnd.level(s.ladder)
        lines.append(f"   * - {_badge(s.ladder, lv.color if lv else '#eee')} :doc:`{s.short} <cards/{s.id}>`")
        lines.extend(f"     - {_escape_rst(s.axes.get(k, '—'))}" for k, _ in AXES)
    lines.append("")
    lines.append(_rst_heading("Layer by layer", "-"))
    for key, label, question in LAYERS:
        lines.extend([_rst_heading(f"{label} — {question}", "~"), ".. list-table::", "   :widths: 18 82", ""])
        for s in ordered:
            lines.extend([f"   * - :doc:`{s.short} <cards/{s.id}>`", f"     - {_escape_rst(s.stack.get(key, '—'))}"])
        lines.append("")
    _write(out / "compare.rst", _RAW_ROLE + lines)


def _write_connections(fnd: Foundations, cat: Catalog, out: Path) -> None:
    members = {p.id: {m.system for m in p.members} for p in cat.principles}
    shared, totals = shared_principles(members)
    lines = [
        ".. _foundations-connections:",
        "",
        _rst_heading("Connections"),
        "How the systems relate: who descends from whom, who formalizes whom, what they share in their ontology, "
        "and how much of the principle catalog they realize in common.",
        "",
        _rst_heading("Bridges", "-"),
        "Solid edges are realized translations or lineage; dotted edges are proposed. Node labels carry the ladder level.",
        "",
        *_graphviz(bridges_graph(fnd, depth=1), alt="Bridges between systems"),
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 16 16 12 40 16",
        "",
        "   * - From",
        "     - To",
        "     - Kind",
        "     - Bridge",
        "     - Status",
    ]
    for b in fnd.bridges:
        src, tgt = fnd.system(b.source), fnd.system(b.target)
        label = _link(b.label, b.evidence) if b.evidence.startswith("http") else _escape_rst(b.label)
        lines.extend([
            f"   * - :doc:`{src.short if src else b.source} <cards/{b.source}>`",
            f"     - :doc:`{tgt.short if tgt else b.target} <cards/{b.target}>`",
            f"     - ``{b.kind}``",
            f"     - {label}",
            f"     - {b.status}",
        ])
    lines.extend([
        "",
        _rst_heading("Ladder lifts", "-"),
        "Routes by which a system's claims could climb the Truth Ladder.",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 20 12 12 40 16",
        "",
        "   * - System",
        "     - From",
        "     - To",
        "     - Via",
        "     - Status",
    ])
    for lf in fnd.lifts:
        s = fnd.system(lf.system)
        lines.extend([
            f"   * - :doc:`{s.short if s else lf.system} <cards/{lf.system}>`",
            f"     - {lf.from_level}",
            f"     - {lf.to_level}",
            f"     - {_escape_rst(lf.via)}",
            f"     - {lf.status}",
        ])
    lines.extend([
        "",
        _rst_heading("Shared ontology", "-"),
        "Each system linked to its primitive sorts. Hubs (Point, Line, Circle) are near-universal; the periphery "
        "shows what is distinctive — Tarski's betweenness and congruence, mathlib's vectors and spheres, "
        "multivectors, homogeneous coordinates.",
        "",
        *_graphviz(ontology_graph(fnd), alt="Ontology graph"),
        _rst_heading("Shared principles", "-"),
        "Edges join base systems that realize the same discovered principle; edge labels and widths count the "
        "shared principles. This replaces the long coverage matrix — drill into the :doc:`catalog </catalog/index>` "
        "with the system filters for the rows.",
        "",
        *_graphviz(overlap_graph(fnd, shared, totals), alt="Shared-principle graph"),
    ])
    _write(out / "connections.rst", _RAW_ROLE + lines)


# --------------------------------------------------------------------------- showcase


def _write_showcase_page(fnd: Foundations, sc: Showcase, out: Path) -> None:
    title = f"{sc.euclid} · {sc.title}" if sc.euclid else sc.title
    lines = [
        f".. _showcase-{sc.id}:",
        "",
        _rst_heading(title),
        ".. admonition:: Statement",
        "   :class: note",
        "",
        f"   {_escape_rst(sc.statement)}",
        "",
        f"**Why this theorem:** {sc.why}",
        "",
        *_graphviz(showcase_graph(fnd, sc, depth=1), alt=f"{sc.title} realizations"),
        _rst_heading("Realizations", "-"),
        ".. container:: codes-tabs",
        "",
    ]
    for r in sc.realizations:
        s = fnd.system(r.system)
        name = s.short if s else r.system
        ident = f" ``{r.ident}``" if r.ident.strip(" —-") else ""
        lines.extend([
            f"   .. container:: codes-tab status-{r.status}",
            "",
            f"      .. rubric:: {name}",
            "",
            f"      {_badge(r.status, STATUS_COLORS.get(r.status, '#eee'))}{ident} — "
            f":doc:`{name} card </foundations/cards/{r.system}>`",
            "",
        ])
        if r.code:
            lines.extend(_code(r.lang, r.code, indent="      "))
        if r.note:
            lines.extend([f"      {_escape_rst(r.note)}", ""])
        if r.source:
            lines.extend([f"      Source: {_link(r.source.rsplit('/', 1)[-1], r.source)}", ""])

    # Exact witnesses: L1 figure and L2 generic identity.
    lines.append(_rst_heading("Climbing the ladder in GEOMETOR", "-"))
    pid = sc.principle
    if pid in PILOT_BUILDERS:
        vres = verify_principle(pid)
        lines.extend([
            f"**L1 — exact instance.** ``geometor.model`` builds one figure with exact coordinates and checks the "
            f"conclusion by ``zero_test``: *{_escape_rst(vres.summary)}* (status ``{vres.status}``). "
            f"See the :ref:`witness entry <{pid}>`.",
            "",
        ])
        svg = out / f"{pid}.svg"
        model = build_pilot_model(pid)
        if model is not None:
            render_svg(model, svg)
            lines.extend([f".. figure:: {pid}.svg", f"   :alt: {pid}", "   :align: center", "   :width: 70%", ""])
    gw = generic_witness(pid)
    if gw is not None:
        verdict = "reduces to **0**" if gw.proved else f"leaves residual ``{gw.residual}``"
        lines.extend([
            f"**L2 — generic.** Replace the coordinates by free symbols ``{', '.join(gw.parameters)}``. "
            f"{_escape_rst(gw.construction)} The conclusion's numerator {verdict}, so the theorem holds for every "
            "configuration outside the degenerate set:",
            "",
        ])
        lines.extend(f"- {_escape_rst(c)}" for c in gw.ndg)
        lines.extend(["", "Computed at build time by :py:func:`geometor.codes.generic.generic_witness`.", ""])
    elif pid in GENERIC_GAPS:
        lines.extend([".. admonition:: No generic lift", "   :class: warning", "", f"   {GENERIC_GAPS[pid]}", ""])
    _write(out / f"{sc.id}.rst", _RAW_ROLE + lines)


def _write_showcase(fnd: Foundations, showcase: list[Showcase], out: Path) -> int:
    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    columns = [s for s in _sorted_systems(fnd) if any(r.system == s.id for sc in showcase for r in sc.realizations)]
    lines = [
        ".. _showcase-index:",
        "",
        _rst_heading("Showcase: One Theorem, Many Foundations"),
        "Each theorem is realized side by side. The cell says what kind of truth each system assigns to it — "
        "a proof, an axiom, an engine rule, an exact witness, a generic algebraic certificate — or why it cannot.",
        "",
        "Legend: " + " ".join(_badge(k, v) for k, v in STATUS_COLORS.items()),
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "",
        "   * - Theorem",
        *[f"     - :doc:`{s.short} </foundations/cards/{s.id}>`" for s in columns],
    ]
    for sc in showcase:
        by_sys = {r.system: r for r in sc.realizations}
        label = f"{sc.euclid} {sc.title}".strip()
        lines.append(f"   * - :doc:`{_escape_rst(label)} <{sc.id}>`")
        for s in columns:
            r = by_sys.get(s.id)
            lines.append(f"     - {_badge(r.status, STATUS_COLORS.get(r.status, '#eee'))}" if r else "     - ·")
    lines.extend(["", ".. toctree::", "   :maxdepth: 1", "", *[f"   {sc.id}" for sc in showcase], ""])
    _write(out / "index.rst", _nav(2, "Showcase") + _RAW_ROLE + lines)
    for sc in showcase:
        _write_showcase_page(fnd, sc, out)
    return len(showcase)


# --------------------------------------------------------------------------- catalog


def _write_witness_page(p: Principle, out_dir: Path, lean_traces: dict[str, list[str]]) -> None:
    pdir = out_dir / p.id
    pdir.mkdir(parents=True, exist_ok=True)

    vres = verify_principle(p.id)
    svg_written = False
    model = build_pilot_model(p.id)
    if model is not None:
        render_svg(model, pdir / f"{p.id}.svg")
        svg_written = True

    record = {**asdict(p), "verification": asdict(vres)}
    (pdir / f"{p.id}.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    lines: list[str] = [
        f".. _{p.id}:",
        "",
        _rst_heading(p.id, "="),
        f"**{_escape_rst(p.title)}** · kind: ``{p.kind}`` · family: ``{p.family}`` · verification: ``{vres.status}``",
        "",
    ]
    if p.euclid_refs:
        lines.extend(["**Euclid:** " + ", ".join(f"``{r}``" for r in p.euclid_refs), ""])
    if p.statement:
        lines.extend([".. admonition:: Statement", "   :class: note", "", f"   {_escape_rst(p.statement)}", ""])
    if p.canonical_form:
        lines.extend([_rst_heading("Canonical Form", "-"), *_code("text", p.canonical_form)])
    if svg_written:
        lines.extend([
            _rst_heading("Exact Witness Figure", "-"),
            f".. figure:: {p.id}.svg",
            f"   :alt: {p.id}",
            "   :align: center",
            "",
            f"   {_escape_rst(vres.summary)}",
            "",
        ])
    elif vres.gap_reason:
        lines.extend([".. admonition:: Verification Gap", "   :class: warning", "", f"   {vres.gap_reason}", ""])

    lines.extend([
        _rst_heading("Base System Realizations", "-"),
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 16 24 60",
        "",
        "   * - System",
        "     - Identifier",
        "     - Statement / Form",
    ])
    for m in p.members:
        stmt = _escape_rst((m.statement or m.canonical_form or m.name)[:180])
        lines.extend([f"   * - :doc:`{m.system} </foundations/cards/{m.system}>`", f"     - ``{m.id}``", f"     - {stmt}"])
    lines.append("")

    traces_for_p = [(m.id, lean_traces[m.key]) for m in p.members if m.key in lean_traces]
    if traces_for_p:
        lines.append(_rst_heading("Proof Traces", "-"))
        for mid, trace in traces_for_p:
            lines.extend([f".. collapse:: LeanEuclid ``{mid}`` ({len(trace)} steps)", "", "   .. code-block:: lean", ""])
            lines.extend(f"      {step}" for step in trace)
            lines.append("")

    strong = [lk for lk in p.linked if float(lk.get("confidence", 0) or 0) >= 0.7]
    if strong:
        lines.extend([
            _rst_heading("Linked Library Entries", "-"),
            "Name-matched entries with confidence ≥ 0.7 (lower-confidence token matches are omitted).",
            "",
            ".. list-table::",
            "   :header-rows: 1",
            "   :widths: 14 40 12 34",
            "",
            "   * - Library",
            "     - Declaration",
            "     - Confidence",
            "     - Evidence",
        ])
        for lk in strong:
            name = f"`{_escape_rst(lk['name'])} <{lk['url']}>`__" if lk.get("url") else f"``{lk['id']}``"
            lines.extend([
                f"   * - ``{lk['system']}``",
                f"     - {name}",
                f"     - {lk.get('confidence', '')}",
                f"     - {_escape_rst(lk.get('evidence', ''))}",
            ])
        lines.append("")
    if p.relations:
        lines.append(_rst_heading("Relations", "-"))
        lines.extend(f"* **{r.relation}**: :ref:`{r.target_id} <{r.target_id}>`" for r in p.relations)
        lines.append("")
    _write(pdir / "index.rst", lines)


def _catalog_payload(cat: Catalog, witnesses: set[str]) -> dict[str, object]:
    systems = sorted({m.system for p in cat.principles for m in p.members})
    rows = []
    for p in cat.principles:
        syss = sorted({m.system for m in p.members})
        form = " ".join((p.canonical_form or p.statement or "").split())[:220]
        search = " ".join([p.id, p.title, p.family, p.kind, form, " ".join(p.euclid_refs), " ".join(syss)]).lower()
        rows.append({
            "id": p.id,
            "title": p.title,
            "family": p.family,
            "kind": p.kind,
            "systems": syss,
            "euclid": list(p.euclid_refs),
            "form": form,
            "witness": p.id in witnesses,
            "search": search,
        })
    return {"systems": systems, "principles": rows}


def _write_catalog(cat: Catalog, out: Path, mined_dir: Path) -> int:
    wdir = out / "witnesses"
    if wdir.exists():
        shutil.rmtree(wdir)
    lean_traces: dict[str, list[str]] = {}
    lean_jsonl = mined_dir / "leaneuclid.jsonl"
    if lean_jsonl.exists():
        for raw in lean_jsonl.read_text(encoding="utf-8").splitlines():
            if raw.strip():
                d = json.loads(raw)
                trace = d.get("extra", {}).get("trace")
                if trace:
                    lean_traces[f"leaneuclid:{d['id']}"] = trace
    written: list[str] = []
    for pid in PILOT_IDS:
        p = cat.by_id(pid)
        if p is not None:
            _write_witness_page(p, wdir, lean_traces)
            written.append(pid)
    _write(wdir / "index.rst", [
        ".. _witnesses-index:",
        "",
        _rst_heading("Exact Witness Entries"),
        f"{len(written)} catalog principles with an exact ``geometor.model`` witness (or a documented gap).",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "",
        *[f"   {pid}/index" for pid in written],
    ])

    st = cat.stats
    manifest = load_manifest(mined_dir)
    lines = [
        ".. _catalog-index:",
        "",
        _rst_heading("Principle Catalog"),
        f"**{st.get('principles', len(cat.principles))}** candidate principles "
        f"(**{st.get('multi_system_principles', 0)}** realized in two or more systems), discovered from "
        f"**{st.get('total_base_items', 0)}** declarations mined from the base systems. Search by text, filter by "
        "family or system; principles with an exact witness link to their entry.",
        "",
        ".. raw:: html",
        "",
        '   <div class="codes-catalog" data-src="codes-catalog-data"></div>',
        "",
        *_json_block("codes-catalog-data", _catalog_payload(cat, set(written))),
        _rst_heading("Mined sources", "-"),
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 18 10 22 50",
        "",
        "   * - System",
        "     - Items",
        "     - Commit / Version",
        "     - By kind",
    ]
    for sys_id, info in sorted(manifest.items()):
        ver = info.get("version") or info.get("commit", "")[:10] or "local"
        breakdown = ", ".join(f"{k}: {v}" for k, v in sorted(info.get("by_kind", {}).items()))
        lines.extend([
            f"   * - :doc:`{sys_id} </foundations/cards/{sys_id}>`",
            f"     - {info.get('count', 0)}",
            f"     - ``{ver}``",
            f"     - {breakdown}",
        ])
    lines.extend(["", ".. toctree::", "   :maxdepth: 1", "", "   witnesses/index", ""])
    _write(out / "index.rst", _nav(3, "Catalog") + lines)
    return len(written)


# --------------------------------------------------------------------------- entry point


def build_site_docs(
    docsrc_dir: Path | None = None,
    catalog: Catalog | None = None,
    mined_dir: Path | None = None,
) -> dict[str, int]:
    """Generate ``foundations/``, ``showcase/``, and ``catalog/`` under ``docsrc``.

    Args:
        docsrc_dir: Sphinx source root (defaults to the repository ``docsrc``).
        catalog: Optional pre-loaded catalog.
        mined_dir: Optional mined-snapshot directory.

    Returns:
        Counts of generated items by category.
    """
    res_dir = default_resources_dir()
    root = docsrc_dir or res_dir.parent / "docsrc"
    mdir = mined_dir or res_dir / "mined"
    cat = catalog or load_catalog()
    fnd = load_foundations()
    showcase = load_showcase()

    fdir = root / "foundations"
    fdir.mkdir(parents=True, exist_ok=True)
    _write(fdir / "_atlas.inc", _atlas_include(fnd))
    _write(fdir / "_ladder.inc", _graphviz(ladder_graph(fnd, depth=0), alt="Truth Ladder"))
    _write_foundations_index(fnd, fdir)
    cards = _write_cards(fnd, showcase, cat, fdir / "cards")
    _write_compare(fnd, fdir)
    _write_connections(fnd, cat, fdir)
    shows = _write_showcase(fnd, showcase, root / "showcase")
    witnesses = _write_catalog(cat, root / "catalog", mdir)

    legacy = root / "principles"
    if legacy.exists():
        shutil.rmtree(legacy)

    return {"cards": cards, "showcase": shows, "witnesses": witnesses, "principles": len(cat.principles)}


build_principles_docs = build_site_docs
"""Backward-compatible alias for :func:`build_site_docs`."""
