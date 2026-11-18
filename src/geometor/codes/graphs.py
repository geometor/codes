"""Graphviz DOT builders for the foundations views.

Every function returns a DOT source string suitable for Sphinx's
``.. graphviz::`` directive (rendered to SVG). Graphs are theme-neutral:
transparent background, filled nodes with dark text, grey edges.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations

from geometor.codes.foundations import LAYERS, Foundations, Showcase, System

_FONT = "Helvetica"
_EDGE = "#8a8f98"
_TEXT = "#1d1f23"

BRIDGE_STYLES: dict[str, tuple[str, str]] = {
    "lineage": ("#d08c3a", "solid"),
    "embeds": ("#6a5acd", "solid"),
    "formalizes": ("#2e8b57", "solid"),
    "translates": ("#3a7bd5", "dashed"),
    "proves": ("#2e8b57", "bold"),
    "benchmark": ("#8a8f98", "dotted"),
    "builds_on": ("#b5651d", "solid"),
}
"""Edge color and style per bridge kind."""

STATUS_COLORS: dict[str, str] = {
    "theorem": "#9fd8a8",
    "axiom": "#f4d58d",
    "rule": "#f6b26b",
    "witness": "#9cc3f0",
    "generic": "#7fd1c7",
    "gap": "#f19c9c",
    "absent": "#dddddd",
    "prose": "#e8d9b5",
}
"""Node fill per showcase realization status."""


def _q(text: str) -> str:
    escaped = text.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
    return f'"{escaped}"'


def _header(name: str, rankdir: str = "LR", extra: str = "") -> list[str]:
    return [
        f"digraph {name} {{",
        f'  graph [rankdir={rankdir}, bgcolor="transparent", fontname="{_FONT}", '
        f'fontcolor="{_EDGE}", nodesep=0.25, ranksep=0.45{extra}];',
        f'  node [fontname="{_FONT}", fontsize=11, style="filled,rounded", shape=box, '
        f'color="#555a62", fontcolor="{_TEXT}", penwidth=0.8];',
        f'  edge [fontname="{_FONT}", fontsize=9, color="{_EDGE}", fontcolor="{_EDGE}", arrowsize=0.6];',
    ]


def _level_color(fnd: Foundations, level_id: str) -> str:
    lv = fnd.level(level_id)
    return lv.color if lv else "#eeeeee"


def _card_url(system_id: str, depth: int) -> str:
    return "../" * depth + f"foundations/cards/{system_id}.html"


def ladder_graph(fnd: Foundations, depth: int = 1) -> str:
    """Truth Ladder: rungs bottom-to-top with systems placed on each rung.

    Dashed edges show *lifts* — routes by which a system's claims could climb.

    Args:
        fnd: Loaded foundations.
        depth: Directory depth of the page embedding the graph (for node links).

    Returns:
        DOT source.
    """
    lines = _header("ladder", rankdir="BT", extra=", ranksep=0.35, newrank=true")
    ordered = sorted(fnd.levels, key=lambda lv: lv.rank)
    for lv in ordered:
        label = f"{lv.id}  {lv.name}\n{lv.claim}"
        style = "filled,dashed" if lv.id == "H" else "filled"
        lines.append(
            f'  lvl_{lv.id} [label={_q(label)}, fillcolor="{lv.color}", shape=box, '
            f'style="{style}", width=2.6, fontsize=10];'
        )
    spine = [lv for lv in ordered if lv.id != "H"]
    for a, b in zip(spine, spine[1:], strict=False):
        lines.append(f"  lvl_{a.id} -> lvl_{b.id} [arrowhead=none, penwidth=3, color=\"#c9ccd1\"];")
    if spine and fnd.level("H") is not None:
        # Human checking sits outside the ordering: drawn above the spine, unconnected.
        lines.append(f"  lvl_{spine[-1].id} -> lvl_H [style=invis];")
    for lv in ordered:
        members = fnd.systems_at(lv.id)
        if not members:
            continue
        ids = " ".join(f"sys_{s.id}" for s in members)
        lines.append(f"  {{ rank=same; lvl_{lv.id}; {ids} }}")
        for s in members:
            pen = "1.6" if s.core else "0.8"
            lines.append(
                f'  sys_{s.id} [label={_q(s.short)}, fillcolor="{lv.color}", penwidth={pen}, '
                f'URL="{_card_url(s.id, depth)}", target="_top", tooltip={_q(s.summary)}];'
            )
            lines.append(f"  lvl_{lv.id} -> sys_{s.id} [style=invis];")
    for lf in fnd.lifts:
        tgt = f"lvl_{lf.to_level}"
        style = "dashed" if lf.status != "realized" else "solid"
        lines.append(
            f'  sys_{lf.system} -> {tgt} [style={style}, color="#3a7bd5", fontcolor="#3a7bd5", '
            f"label={_q(lf.via)}, constraint=false];"
        )
    lines.append("}")
    return "\n".join(lines)


def chain_graph(fnd: Foundations, system: System) -> str:
    """Trust chain for one system: the seven Trust Stack layers left to right.

    The ``checker`` node (what must be trusted) is emphasized.

    Args:
        fnd: Loaded foundations.
        system: The system to draw.

    Returns:
        DOT source.
    """
    lines = _header(f"chain_{system.id}", rankdir="LR", extra=", nodesep=0.15, ranksep=0.25")
    color = _level_color(fnd, system.ladder)
    prev = None
    for key, label, _ in LAYERS:
        text = system.stack.get(key, "—")
        short = text if len(text) <= 96 else text[:93].rsplit(" ", 1)[0] + " …"
        wrapped = _wrap(short, 24)
        is_checker = key == "checker"
        fill = color if is_checker else "#f4f5f7"
        pen = "2.2" if is_checker else "0.8"
        lines.append(
            f'  {key} [label=<<b>{label}</b><br/><font point-size="9">{wrapped}</font>>, '
            f'fillcolor="{fill}", penwidth={pen}, width=1.4];'
        )
        if prev:
            lines.append(f"  {prev} -> {key};")
        prev = key
    lines.append("}")
    return "\n".join(lines)


def trust_graph(fnd: Foundations, depth: int = 1) -> str:
    """Who trusts what: systems on the left, trusted components on the right.

    Shared components (e.g. the Lean kernel) become visible hubs.

    Args:
        fnd: Loaded foundations.
        depth: Directory depth of the embedding page.

    Returns:
        DOT source.
    """
    lines = _header("trust", rankdir="LR", extra=", ranksep=1.1")
    kinds = {
        "kernel": "#9fd8a8",
        "solver": "#f4d58d",
        "engine": "#f6b26b",
        "cas": "#9cc3f0",
        "float": "#dddddd",
        "human": "#e8d9b5",
    }
    lines.append("  subgraph cluster_sys { label=\"systems\"; style=invis;")
    for s in fnd.systems:
        lines.append(
            f'    sys_{s.id} [label={_q(s.short)}, fillcolor="{_level_color(fnd, s.ladder)}", '
            f'URL="{_card_url(s.id, depth)}", target="_top", tooltip={_q(s.summary)}];'
        )
    lines.append("  }")
    lines.append("  subgraph cluster_tcb { label=\"trusted components\"; style=invis;")
    for t in fnd.trusted:
        label = f"{t.name}\n{t.size}" if t.size else t.name
        lines.append(
            f'    tcb_{t.id} [label={_q(label)}, shape=cylinder, style=filled, '
            f'fillcolor="{kinds.get(t.kind, "#eeeeee")}", tooltip={_q(t.note)}];'
        )
    lines.append("  }")
    for s in fnd.systems:
        for t in s.trusts:
            lines.append(f"  sys_{s.id} -> tcb_{t};")
    lines.append("}")
    return "\n".join(lines)


def bridges_graph(fnd: Foundations, depth: int = 1) -> str:
    """Translations, embeddings, and lineage between systems.

    Args:
        fnd: Loaded foundations.
        depth: Directory depth of the embedding page.

    Returns:
        DOT source.
    """
    lines = _header("bridges", rankdir="LR", extra=", ranksep=0.9, nodesep=0.35")
    used = {b.source for b in fnd.bridges} | {b.target for b in fnd.bridges}
    for s in fnd.systems:
        if s.id not in used:
            continue
        lines.append(
            f'  {s.id} [label={_q(s.short + "  (" + s.ladder + ")")}, '
            f'fillcolor="{_level_color(fnd, s.ladder)}", URL="{_card_url(s.id, depth)}", '
            f'target="_top", tooltip={_q(s.summary)}];'
        )
    for b in fnd.bridges:
        color, style = BRIDGE_STYLES.get(b.kind, (_EDGE, "solid"))
        if b.status == "proposed":
            style = "dotted"
        url = f', URL="{b.evidence}", target="_blank"' if b.evidence.startswith("http") else ""
        lines.append(
            f'  {b.source} -> {b.target} [label={_q(b.label)}, color="{color}", '
            f'fontcolor="{color}", style={style}{url}];'
        )
    lines.append("}")
    return "\n".join(lines)


def ontology_graph(fnd: Foundations) -> str:
    """Systems linked to the primitive sorts of their ontology.

    Args:
        fnd: Loaded foundations.

    Returns:
        DOT source (undirected).
    """
    counts = Counter(p for s in fnd.systems for p in s.primitives)
    lines = [
        "graph ontology {",
        f'  graph [layout=neato, overlap=false, splines=true, bgcolor="transparent", '
        f'fontname="{_FONT}", sep="+6"];',
        f'  node [fontname="{_FONT}", fontsize=10, style="filled,rounded", shape=box, '
        f'color="#555a62", fontcolor="{_TEXT}", penwidth=0.8];',
        f'  edge [color="{_EDGE}", penwidth=0.7];',
    ]
    for prim, n in counts.items():
        size = 9 + min(n, 8)
        lines.append(
            f'  "p_{prim}" [label={_q(prim)}, shape=ellipse, style=filled, '
            f'fillcolor="#ffffff", fontsize={size}];'
        )
    for s in fnd.systems:
        lines.append(f'  "s_{s.id}" [label={_q(s.short)}, fillcolor="{_level_color(fnd, s.ladder)}"];')
        for p in s.primitives:
            lines.append(f'  "s_{s.id}" -- "p_{p}";')
    lines.append("}")
    return "\n".join(lines)


def overlap_graph(fnd: Foundations, shared: dict[tuple[str, str], int], totals: dict[str, int]) -> str:
    """Shared-principle graph: edge weight = principles realized in both systems.

    Args:
        fnd: Loaded foundations (for colors and labels).
        shared: Mapping of sorted system-id pairs to shared principle counts.
        totals: Principle counts per system (node labels).

    Returns:
        DOT source (undirected, neato layout).
    """
    lines = [
        "graph overlap {",
        f'  graph [layout=neato, overlap=false, splines=true, sep="+12", bgcolor="transparent", '
        f'fontname="{_FONT}"];',
        f'  node [fontname="{_FONT}", fontsize=11, style="filled,rounded", shape=box, '
        f'color="#555a62", fontcolor="{_TEXT}"];',
        f'  edge [fontname="{_FONT}", fontsize=10, color="{_EDGE}", fontcolor="#3a7bd5"];',
    ]
    peak = max(shared.values(), default=1)
    for sid, n in totals.items():
        s = fnd.system(sid)
        label = f"{s.short if s else sid}\n{n} principles"
        color = _level_color(fnd, s.ladder) if s else "#eeeeee"
        lines.append(f"  {sid} [label={_q(label)}, fillcolor=\"{color}\"];")
    for (a, b), n in sorted(shared.items()):
        width = 0.6 + 5.0 * n / peak
        length = 4.2 - 2.4 * n / peak
        lines.append(f'  {a} -- {b} [label="{n}", penwidth={width:.2f}, len={length:.2f}];')
    lines.append("}")
    return "\n".join(lines)


def showcase_graph(fnd: Foundations, sc: Showcase, depth: int = 2) -> str:
    """Star graph for one showcase theorem: realizations colored by status.

    Args:
        fnd: Loaded foundations.
        sc: Showcase theorem.
        depth: Directory depth of the embedding page.

    Returns:
        DOT source.
    """
    lines = _header(f"showcase_{sc.id}", rankdir="LR", extra=", ranksep=0.8")
    title = f"{sc.euclid}  {sc.title}" if sc.euclid else sc.title
    lines.append(f'  thm [label={_q(title)}, shape=ellipse, style=filled, fillcolor="#ffffff", penwidth=1.6];')
    for i, r in enumerate(sc.realizations):
        s = fnd.system(r.system)
        name = s.short if s else r.system
        ident = r.ident if len(r.ident) <= 34 else r.ident[:31] + "…"
        label = f"<<b>{name}</b><br/><font point-size=\"9\">{_html(ident)}<br/><i>{r.status}</i></font>>"
        lines.append(
            f'  r{i} [label={label}, fillcolor="{STATUS_COLORS.get(r.status, "#eeeeee")}", '
            f'URL="{_card_url(r.system, depth)}", target="_top", tooltip={_q(r.note)}];'
        )
        style = "dashed" if r.status in {"gap", "absent"} else "solid"
        lines.append(f"  thm -> r{i} [style={style}];")
    lines.append("}")
    return "\n".join(lines)


def shared_principles(
    members_by_principle: dict[str, set[str]],
) -> tuple[dict[tuple[str, str], int], dict[str, int]]:
    """Count principles shared by each pair of systems.

    Args:
        members_by_principle: Principle id → set of system ids realizing it.

    Returns:
        ``(shared, totals)`` where ``shared`` maps sorted system pairs to counts
        and ``totals`` maps each system to its principle count.
    """
    shared: Counter[tuple[str, str]] = Counter()
    totals: Counter[str] = Counter()
    for systems in members_by_principle.values():
        for s in systems:
            totals[s] += 1
        for a, b in combinations(sorted(systems), 2):
            shared[(a, b)] += 1
    return dict(shared), dict(totals)


def _html(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _wrap(text: str, width: int) -> str:
    words = _html(text).split()
    out: list[str] = []
    cur = ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width:
            out.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        out.append(cur)
    return "<br/>".join(out)
