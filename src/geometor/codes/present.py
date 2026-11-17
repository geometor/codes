"""Phase 5: Generate ETC-style RST principle pages, exact SVGs, and catalog views."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path

from geometor.codes.discover.cluster import Catalog, Principle, load_catalog
from geometor.codes.mine.schema import load_manifest
from geometor.codes.registry import default_resources_dir
from geometor.codes.render import render_svg
from geometor.codes.verify import KNOWN_GAPS, PILOT_BUILDERS, build_pilot_model, verify_principle

PILOT_IDS: tuple[str, ...] = tuple(PILOT_BUILDERS) + tuple(KNOWN_GAPS)


def _rst_heading(title: str, char: str = "=") -> str:
    return f"{title}\n{char * len(title)}\n"


def _escape_rst(text: str) -> str:
    return " ".join(text.split()).replace("|", "\\|")


def _write_pilot_page(
    p: Principle,
    out_dir: Path,
    lean_traces: dict[str, list[str]],
) -> None:
    pdir = out_dir / "pilot" / p.id
    pdir.mkdir(parents=True, exist_ok=True)

    vres = verify_principle(p.id)
    svg_written = False
    model = build_pilot_model(p.id)
    if model is not None:
        render_svg(model, pdir / f"{p.id}.svg")
        svg_written = True

    record = {
        **asdict(p),
        "verification": asdict(vres),
    }
    (pdir / f"{p.id}.json").write_text(
        json.dumps(record, indent=2, ensure_ascii=False, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    lines: list[str] = [
        f".. _{p.id}:",
        "",
        _rst_heading(p.id, "="),
        f"**{p.title}** · kind: ``{p.kind}`` · family: ``{p.family}`` · verification: ``{vres.status}``",
        "",
    ]
    if p.euclid_refs:
        refs = ", ".join(f"``{r}``" for r in p.euclid_refs)
        lines.append(f"**Euclid:** {refs}")
        lines.append("")

    if p.statement:
        lines.extend([
            ".. admonition:: Statement",
            "   :class: note",
            "",
            f"   {_escape_rst(p.statement)}",
            "",
        ])

    if p.canonical_form:
        lines.extend([
            _rst_heading("Canonical Form", "-"),
            ".. code-block:: text",
            "",
            f"   {p.canonical_form}",
            "",
        ])

    if svg_written:
        lines.extend([
            _rst_heading("Exact Witness Figure", "-"),
            f".. figure:: {p.id}.svg",
            f"   :alt: {p.id}",
            "   :align: center",
            "",
            f"   {vres.summary}",
            "",
        ])
    elif vres.gap_reason:
        lines.extend([
            ".. admonition:: Verification Gap",
            "   :class: warning",
            "",
            f"   {vres.gap_reason}",
            "",
        ])

    # Realizations (base systems)
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
        stmt = _escape_rst(m.statement or m.canonical_form or m.name)[:180]
        lines.extend([
            f"   * - ``{m.system}``",
            f"     - ``{m.id}``",
            f"     - {stmt}",
        ])
    lines.append("")

    # Proof traces (summary + collapse)
    traces_for_p = [(m.id, lean_traces[m.key]) for m in p.members if m.key in lean_traces]
    if traces_for_p:
        lines.extend([_rst_heading("Proof Traces", "-")])
        for mid, trace in traces_for_p:
            lines.extend([
                f".. collapse:: LeanEuclid ``{mid}`` ({len(trace)} steps)",
                "",
                "   .. code-block:: lean",
                "",
            ])
            for step in trace:
                lines.append(f"      {step}")
            lines.append("")

    # Linked library matches
    if p.linked:
        lines.extend([
            _rst_heading("Linked Library Entries", "-"),
            ".. list-table::",
            "   :header-rows: 1",
            "   :widths: 14 28 12 46",
            "",
            "   * - Library",
            "     - Declaration",
            "     - Confidence",
            "     - Source",
        ])
        for lk in p.linked:
            src_cell = f"`{lk['name']} <{lk['url']}>`_" if lk.get("url") else f"``{lk['id']}``"
            lines.extend([
                f"   * - ``{lk['system']}``",
                f"     - ``{lk['name']}``",
                f"     - {lk.get('confidence', '')} ({lk.get('evidence', '')})",
                f"     - {src_cell}",
            ])
        lines.append("")

    if p.relations:
        lines.extend([_rst_heading("Relations", "-")])
        for r in p.relations:
            lines.append(f"* **{r.relation}**: :ref:`{r.target_id} <{r.target_id}>`")
        lines.append("")

    (pdir / "index.rst").write_text("\n".join(lines), encoding="utf-8")


def build_principles_docs(
    catalog: Catalog | None = None,
    docsrc_dir: Path | None = None,
    mined_dir: Path | None = None,
) -> dict[str, int]:
    """Generate ``docsrc/principles/`` pages, SVGs, and catalog views.

    Returns:
        Counts of generated pages by category.
    """
    cat = catalog or load_catalog()
    res_dir = default_resources_dir()
    mdir = mined_dir or res_dir / "mined"
    out_dir = docsrc_dir or res_dir.parent / "docsrc" / "principles"
    out_dir.mkdir(parents=True, exist_ok=True)

    # Load LeanEuclid traces for pilot collapse blocks.
    lean_traces: dict[str, list[str]] = {}
    lean_jsonl = mdir / "leaneuclid.jsonl"
    if lean_jsonl.exists():
        for raw in lean_jsonl.read_text(encoding="utf-8").splitlines():
            if not raw.strip():
                continue
            d = json.loads(raw)
            trace = d.get("extra", {}).get("trace")
            if trace:
                lean_traces[f"leaneuclid:{d['id']}"] = trace

    # 1. Pilot entry pages
    pilot_written: list[str] = []
    for pid in PILOT_IDS:
        p = cat.by_id(pid)
        if p is not None:
            _write_pilot_page(p, out_dir, lean_traces)
            pilot_written.append(pid)

    pilot_idx = [
        _rst_heading("Pilot Principles (ETC-Style Entries)", "="),
        f"Curated pilot of {len(pilot_written)} core geometric principles with exact ``geometor.model`` witnesses.",
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "",
    ]
    for pid in pilot_written:
        pilot_idx.append(f"   {pid}/index")
    pilot_idx.append("")
    (out_dir / "pilot" / "index.rst").write_text("\n".join(pilot_idx), encoding="utf-8")

    # 2. Family pages
    fam_dir = out_dir / "families"
    fam_dir.mkdir(parents=True, exist_ok=True)
    by_fam: dict[str, list[Principle]] = defaultdict(list)
    for p in cat.principles:
        by_fam[p.family].append(p)

    fam_idx = [
        _rst_heading("Principles by Family", "="),
        "",
        ".. toctree::",
        "   :maxdepth: 1",
        "",
    ]
    for fam in sorted(by_fam):
        slug = re.sub(r"[^a-z0-9_]+", "_", fam.lower()).strip("_") or "general"
        fam_idx.append(f"   {slug}")
        flines = [
            _rst_heading(f"Family: {fam}", "="),
            f"{len(by_fam[fam])} principles in this family.",
            "",
            ".. list-table::",
            "   :header-rows: 1",
            "   :widths: 28 14 28 30",
            "",
            "   * - Principle",
            "     - Kind",
            "     - Base Systems",
            "     - Statement / Form",
        ]
        for p in by_fam[fam]:
            systems = ", ".join(sorted({m.system for m in p.members}))
            pid_cell = f":ref:`{p.id} <{p.id}>`" if p.id in pilot_written else f"``{p.id}``"
            summary = _escape_rst(p.canonical_form or p.statement)[:120]
            flines.extend([
                f"   * - {pid_cell}",
                f"     - ``{p.kind}``",
                f"     - {systems}",
                f"     - {summary}",
            ])
        flines.append("")
        (fam_dir / f"{slug}.rst").write_text("\n".join(flines), encoding="utf-8")
    fam_idx.append("")
    (fam_dir / "index.rst").write_text("\n".join(fam_idx), encoding="utf-8")

    # 3. Coverage Matrix (multi-system principles)
    sys_cols = ["euclid", "leaneuclid", "alphageometry", "newclid", "sympy", "geometor_model", "geocoq", "mathlib4"]
    multi = [p for p in cat.principles if len({m.system for m in p.members}) >= 2]
    mlines = [
        _rst_heading("Multi-System Coverage Matrix", "="),
        f"{len(multi)} principles realized in 2 or more base systems.",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "",
        "   * - Principle",
        *[f"     - {s}" for s in sys_cols],
    ]
    for p in multi:
        present = {m.system for m in p.members} | {lk["system"] for lk in p.linked}
        pid_cell = f":ref:`{p.id} <{p.id}>`" if p.id in pilot_written else f"``{p.id}``"
        mlines.append(f"   * - {pid_cell}")
        for s in sys_cols:
            mlines.append(f"     - {'yes' if s in present else '—'}")
    mlines.append("")
    (out_dir / "matrix.rst").write_text("\n".join(mlines), encoding="utf-8")

    # 4. System Anatomy view
    manifest = load_manifest(mdir)
    alines = [
        _rst_heading("Base System Anatomy", "="),
        "Declaration counts by kind across the 6 mined base-context systems.",
        "",
        ".. list-table::",
        "   :header-rows: 1",
        "   :widths: 18 10 22 50",
        "",
        "   * - System",
        "     - Total",
        "     - Commit / Version",
        "     - Breakdown by Kind",
    ]
    for sys_id, info in sorted(manifest.items()):
        ver = info.get("version") or info.get("commit", "")[:10] or "local"
        breakdown = ", ".join(f"{k}: {v}" for k, v in sorted(info.get("by_kind", {}).items()))
        alines.extend([
            f"   * - ``{sys_id}``",
            f"     - {info.get('count', 0)}",
            f"     - ``{ver}``",
            f"     - {breakdown}",
        ])
    alines.append("")
    (out_dir / "anatomy.rst").write_text("\n".join(alines), encoding="utf-8")

    # 5. Root principles index
    st = cat.stats
    root_lines = [
        _rst_heading("Geometric Principles Catalog", "="),
        f"Discovered **{st.get('principles', len(cat.principles))}** candidate principles "
        f"({st.get('multi_system_principles', 0)} multi-system) from "
        f"**{st.get('total_base_items', 0)}** base declarations "
        f"(``{st.get('unassigned_items', 0)}`` unassigned).",
        "",
        ".. toctree::",
        "   :maxdepth: 2",
        "",
        "   pilot/index",
        "   families/index",
        "   matrix",
        "   anatomy",
        "",
    ]
    (out_dir / "index.rst").write_text("\n".join(root_lines), encoding="utf-8")

    return {
        "pilot": len(pilot_written),
        "families": len(by_fam),
        "matrix_rows": len(multi),
    }
