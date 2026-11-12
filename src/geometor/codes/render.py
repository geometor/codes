"""Interactive `.euclid-graphic` SVG renderer for GEOMETOR Codes.

Renders exact `geometor.model.Model` constructions with two-way `data-ref` <-> `:g:`
hover highlighting, exact symbolic `data-latex-xy` / `data-quadrance` telemetry,
callout badges, and interactive pan/zoom/guide controls.
"""

from __future__ import annotations

import math
from pathlib import Path
from xml.sax.saxutils import escape

import sympy as sp
import sympy.geometry as spg
from geometor.model import Model

Point = spg.Point
Line = spg.Line
Circle = spg.Circle
Polygon = (spg.Polygon, spg.Triangle)
Segment = spg.Segment

CODES_SVG_CSS = """
svg.codes-diagram {
    background-color: #111318;
    border: 1px solid #2e3440;
    border-radius: 6px;
    width: 100%;
    height: auto;
    max-height: 560px;
    display: block;
    margin: 0.75rem auto;
    user-select: none;
    overflow: hidden;
    cursor: grab;
}
svg.codes-diagram:active {
    cursor: grabbing;
}
@media (prefers-color-scheme: light) {
    svg.codes-diagram {
        background-color: #fbfbfd;
        border-color: #d8dee9;
    }
    svg.codes-diagram .Point {
        stroke: #fbfbfd !important;
    }
    svg.codes-diagram .Point.given {
        fill: #1a1d24 !important;
    }
    svg.codes-diagram .label-halo {
        stroke: #fbfbfd !important;
    }
    svg.codes-diagram .label-fill {
        fill: #1a1d24 !important;
    }
    svg.codes-diagram .Line,
    svg.codes-diagram .Segment {
        stroke: #4c566a;
    }
    svg.codes-diagram .callout-box {
        fill: rgba(255, 255, 255, 0.92);
    }
    svg.codes-diagram .callout-text {
        fill: #1a1d24;
    }
}
.Line, .Segment {
    stroke: #9aa5b4;
    stroke-linecap: round;
    vector-effect: non-scaling-stroke;
    stroke-width: 1.35px;
    fill: none;
    opacity: 0.84;
    transition: stroke-width 0.15s ease, opacity 0.15s ease, filter 0.15s ease;
}
.Circle {
    stroke: #c678dd;
    vector-effect: non-scaling-stroke;
    stroke-width: 1.45px;
    fill: none;
    opacity: 0.86;
    transition: stroke-width 0.15s ease, opacity 0.15s ease, filter 0.15s ease;
}
.Polygon {
    fill: rgba(97, 175, 239, 0.09);
    stroke: #61afef;
    vector-effect: non-scaling-stroke;
    stroke-width: 1.85px;
    stroke-linejoin: round;
    transition: stroke-width 0.15s ease, fill-opacity 0.15s ease;
}
.Polygon.golden {
    fill: rgba(229, 192, 123, 0.14);
    stroke: #e5c07b;
}
.Point {
    fill: #e5c07b;
    stroke: #111318;
    vector-effect: non-scaling-stroke;
    stroke-width: 1.4px;
    transition: r 0.15s ease, filter 0.15s ease;
}
.Point.given {
    fill: #ffffff;
}
.Point.result, .Point.center, .Point.target {
    fill: #00e5ff;
}
.Point.golden {
    fill: #f0c674;
}
.Point.midpoint, .Point.foot {
    fill: #98c379;
}
.Line.guide, .Circle.guide, .Segment.guide, .Point.guide {
    stroke-dasharray: 4 4;
    opacity: 0.42;
    stroke-width: 0.95px;
}
.Line.axis, .Segment.axis, .Line.euler, .Segment.euler {
    stroke: #e06c75;
    stroke-width: 1.9px;
    opacity: 0.94;
}
.Line.bisector, .Segment.bisector, .Line.altitude, .Segment.altitude, .Line.median, .Segment.median {
    stroke: #98c379;
    stroke-width: 1.5px;
    opacity: 0.88;
}
.Line.golden, .Segment.golden, .Circle.golden {
    stroke: #e5c07b;
    stroke-width: 1.85px;
}
.Circle.circumcircle {
    stroke: #e06c75;
    stroke-width: 1.55px;
}
.Circle.ninepoint {
    stroke: #61afef;
    stroke-width: 1.65px;
}
.Circle.incircle {
    stroke: #e5c07b;
    stroke-width: 1.55px;
}
.callout-box {
    fill: rgba(24, 28, 36, 0.88);
    stroke: #61afef;
    vector-effect: non-scaling-stroke;
    stroke-width: 1px;
    rx: 3px;
}
.callout-box.spread-box {
    stroke: #e5c07b;
}
.callout-box.paradigm-box {
    stroke: #c678dd;
}
.callout-text {
    fill: #eceff4;
    font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
    font-weight: 600;
    text-anchor: middle;
    dominant-baseline: central;
    pointer-events: none;
}
.element-group {
    cursor: pointer;
}
.element-group.svg-hovered .Line,
.element-group.svg-hovered .Segment,
.element-group.svg-hovered .Circle,
.element-group.svg-hovered .Polygon {
    stroke: #00e5ff !important;
    stroke-width: 2.8px !important;
    opacity: 1.0 !important;
    filter: drop-shadow(0 0 5px rgba(0, 229, 255, 0.75));
}
.element-group.svg-hovered .Point {
    fill: #00e5ff !important;
    filter: drop-shadow(0 0 6px rgba(0, 229, 255, 0.9));
}
.svg-control-btn {
    cursor: pointer;
}
.svg-control-btn rect {
    fill: rgba(30, 34, 42, 0.85);
    stroke: #5c6370;
    stroke-width: 1px;
    vector-effect: non-scaling-stroke;
    rx: 3px;
}
.svg-control-btn:hover rect {
    fill: rgba(55, 62, 76, 0.95);
    stroke: #00e5ff;
}
.svg-control-btn text {
    fill: #e5e9f0;
    font-family: sans-serif;
    font-weight: 600;
    text-anchor: middle;
    dominant-baseline: central;
    pointer-events: none;
}
svg.hide-labels .labels-layer,
svg.hide-labels .callouts-layer {
    display: none;
}
svg.hide-guides .guide {
    display: none;
}
"""

INTERACTIVE_CODES_JS = """
(function() {
  if (window.__codesSvgInit) return;
  window.__codesSvgInit = true;

  function initDiagram(svg) {
    if (svg.dataset.initialized) return;
    svg.dataset.initialized = "true";
    const vp = svg.querySelector(".svg-viewport");
    if (!vp) return;

    let scale = 1, tx = 0, ty = 0;
    let dragging = false, startX = 0, startY = 0;

    function applyTransform() {
      vp.setAttribute("transform", `translate(${tx},${ty}) scale(${scale})`);
    }

    svg.addEventListener("wheel", function(e) {
      e.preventDefault();
      const rect = svg.getBoundingClientRect();
      const vb = svg.viewBox.baseVal;
      const mx = vb.x + ((e.clientX - rect.left) / rect.width) * vb.width;
      const my = vb.y + ((e.clientY - rect.top) / rect.height) * vb.height;
      const factor = e.deltaY > 0 ? 1 / 1.15 : 1.15;
      const newScale = Math.min(Math.max(scale * factor, 0.25), 12);
      tx = mx - (mx - tx) * (newScale / scale);
      ty = my - (my - ty) * (newScale / scale);
      scale = newScale;
      applyTransform();
    }, { passive: false });

    svg.addEventListener("mousedown", function(e) {
      if (e.target.closest(".svg-controls")) return;
      dragging = true;
      startX = e.clientX;
      startY = e.clientY;
    });

    window.addEventListener("mousemove", function(e) {
      if (!dragging) return;
      const rect = svg.getBoundingClientRect();
      const vb = svg.viewBox.baseVal;
      const dx = ((e.clientX - startX) / rect.width) * vb.width;
      const dy = ((e.clientY - startY) / rect.height) * vb.height;
      startX = e.clientX;
      startY = e.clientY;
      tx += dx;
      ty += dy;
      applyTransform();
    });

    window.addEventListener("mouseup", function() {
      dragging = false;
    });

    svg.querySelectorAll(".svg-control-btn").forEach(function(btn) {
      btn.addEventListener("click", function(e) {
        e.stopPropagation();
        const action = btn.dataset.action;
        if (action === "zoom-in") { scale = Math.min(scale * 1.25, 12); applyTransform(); }
        else if (action === "zoom-out") { scale = Math.max(scale / 1.25, 0.25); applyTransform(); }
        else if (action === "reset") { scale = 1; tx = 0; ty = 0; applyTransform(); }
        else if (action === "labels") { svg.classList.toggle("hide-labels"); }
        else if (action === "guides") { svg.classList.toggle("hide-guides"); }
      });
    });
  }

  function setupHoverSync() {
    document.querySelectorAll("svg.codes-diagram").forEach(initDiagram);

    document.addEventListener("mouseover", function(e) {
      const refEl = e.target.closest("[data-ref]");
      if (!refEl) return;
      const ref = refEl.dataset.ref;
      if (!ref) return;
      document.querySelectorAll(`.element-group[data-ref="${CSS.escape(ref)}"]`).forEach(el => el.classList.add("svg-hovered"));
      document.querySelectorAll(`.geom-ref[data-ref="${CSS.escape(ref)}"]`).forEach(el => el.classList.add("ref-hovered"));
    });

    document.addEventListener("mouseout", function(e) {
      const refEl = e.target.closest("[data-ref]");
      if (!refEl) return;
      const ref = refEl.dataset.ref;
      if (!ref) return;
      document.querySelectorAll(`.element-group[data-ref="${CSS.escape(ref)}"]`).forEach(el => el.classList.remove("svg-hovered"));
      document.querySelectorAll(`.geom-ref[data-ref="${CSS.escape(ref)}"]`).forEach(el => el.classList.remove("ref-hovered"));
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setupHoverSync);
  } else {
    setupHoverSync();
  }
})();
"""


def _esc_attr(val: str) -> str:
    """Escape an XML attribute value including double quotes.

    Args:
        val: Raw attribute string.

    Returns:
        XML-escaped attribute string.
    """
    return escape(val, {'"': "&quot;"})


def _to_svg_coord(val: object) -> float:
    """Evaluate an exact SymPy expression to float strictly for SVG viewport projection.

    Args:
        val: Exact SymPy expression or int/float.

    Returns:
        Floating-point pixel coordinate for SVG rendering.
    """
    if isinstance(val, (int, float)):
        return float(val)
    return float(sp.N(val))  # type: ignore[arg-type]


def _format_svg_label(label: str) -> str:
    """Format an alphanumeric label such as `X1` or `M_a` cleanly for SVG `<text>`.

    Args:
        label: Raw element identifier.

    Returns:
        Escaped SVG label markup.
    """
    clean = label.strip()
    if "_" in clean:
        base, sub = clean.split("_", 1)
        sub = sub.strip("{}")
        return f'{escape(base)}<tspan dy="0.3em" font-size="74%">{escape(sub)}</tspan>'
    return escape(clean)


def render_svg(
    model: Model,
    output_path: Path,
    annotations: list[dict[str, object]] | None = None,
    padding_ratio: float = 0.20,
) -> Path:
    """Render an exact `geometor.model.Model` into an interactive `.euclid-graphic` SVG.

    Args:
        model: Populated exact `geometor.model.Model` (zero `sp.Float` coordinates).
        output_path: Target `.svg` file path.
        annotations: Optional callout dictionaries with `x`, `y`, `text`, `kind`, `ref`.
        padding_ratio: Fractional viewport padding around bounding points and circles.

    Returns:
        Written `output_path`.
    """
    pts_xy: list[tuple[float, float]] = []
    for el, info in model.items():
        if isinstance(el, Point) and not info.guide:
            xf = _to_svg_coord(el.x)
            yf = _to_svg_coord(el.y)
            if math.isfinite(xf) and math.isfinite(yf):
                pts_xy.append((xf, yf))
        elif isinstance(el, Circle) and not info.guide and "guide" not in info.classes:
            cx = _to_svg_coord(el.center.x)
            cy = _to_svg_coord(el.center.y)
            r = abs(_to_svg_coord(el.radius))
            if math.isfinite(r) and r < 40.0:
                pts_xy.extend([(cx - r, cy - r), (cx + r, cy + r)])

    if annotations:
        for ann in annotations:
            ax = _to_svg_coord(ann.get("x", 0))
            ay = _to_svg_coord(ann.get("y", 0))
            if math.isfinite(ax) and math.isfinite(ay):
                pts_xy.append((ax, ay))

    if not pts_xy:
        pts_xy = [(-2.0, -2.0), (6.0, 6.0)]

    min_x = min(p[0] for p in pts_xy)
    max_x = max(p[0] for p in pts_xy)
    min_y = min(p[1] for p in pts_xy)
    max_y = max(p[1] for p in pts_xy)

    span_x = max(max_x - min_x, 2.0)
    span_y = max(max_y - min_y, 2.0)
    span = max(span_x, span_y)
    pad = span * padding_ratio

    vb_x = min_x - pad
    vb_y = -(max_y + pad)
    vb_w = span_x + 2 * pad
    vb_h = span_y + 2 * pad

    unit = max(vb_w, vb_h) / 100.0
    pt_r = unit * 1.15
    font_sz = unit * 2.85

    polygons_svg: list[str] = []
    circles_svg: list[str] = []
    lines_svg: list[str] = []
    points_svg: list[str] = []
    labels_svg: list[str] = []
    callouts_svg: list[str] = []

    clip_min_x = min_x - span * 2.2
    clip_max_x = max_x + span * 2.2
    clip_min_y = min_y - span * 2.2
    clip_max_y = max_y + span * 2.2

    for el, info in model.items():
        label = info.ID or ""
        esc_ref = _esc_attr(label)
        cls_tokens = list(info.classes.keys())
        if info.guide and "guide" not in cls_tokens:
            cls_tokens.append("guide")
        cls_str = _esc_attr(" ".join(cls_tokens))

        if isinstance(el, Polygon):
            coord_pairs: list[str] = []
            for v in el.vertices:
                vx = _to_svg_coord(v.x)
                vy = -_to_svg_coord(v.y)
                coord_pairs.append(f"{vx:.4f},{vy:.4f}")
            pts_attr = " ".join(coord_pairs)
            polygons_svg.append(
                f'    <g class="element-group" data-ref="{esc_ref}">'
                f'<polygon class="Polygon {cls_str}" points="{pts_attr}">'
                f"<title>{escape(label)}</title></polygon></g>"
            )

        elif isinstance(el, Circle):
            cx = _to_svg_coord(el.center.x)
            cy = -_to_svg_coord(el.center.y)
            r = abs(_to_svg_coord(el.radius))
            q_exact = sp.simplify(el.radius**2)
            circles_svg.append(
                f'    <g class="element-group" data-ref="{esc_ref}">'
                f'<circle class="Circle {cls_str}" cx="{cx:.4f}" cy="{cy:.4f}" r="{r:.4f}" '
                f'data-quadrance="{_esc_attr(str(q_exact))}">'
                f"<title>{escape(label)} (Q = {escape(str(q_exact))})</title></circle></g>"
            )

        elif isinstance(el, Segment):
            p1, p2 = el.points
            mx = (_to_svg_coord(p1.x) + _to_svg_coord(p2.x)) / 2.0
            my = -(_to_svg_coord(p1.y) + _to_svg_coord(p2.y)) / 2.0
            x1, y1 = _to_svg_coord(p1.x), -_to_svg_coord(p1.y)
            x2, y2 = _to_svg_coord(p2.x), -_to_svg_coord(p2.y)
            q_seg = sp.simplify((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
            lines_svg.append(
                f'    <g class="element-group" data-ref="{esc_ref}">'
                f'<path class="Segment {cls_str}" d="M {x1:.4f},{y1:.4f} L {mx:.4f},{my:.4f} L {x2:.4f},{y2:.4f}" '
                f'data-quadrance="{_esc_attr(str(q_seg))}">'
                f"<title>{escape(label)} (Q = {escape(str(q_seg))})</title></path></g>"
            )

        elif isinstance(el, Line):
            p1, p2 = el.points
            x1, y1 = _to_svg_coord(p1.x), _to_svg_coord(p1.y)
            x2, y2 = _to_svg_coord(p2.x), _to_svg_coord(p2.y)
            dx, dy = x2 - x1, y2 - y1
            length = math.hypot(dx, dy)
            if length > 1e-9:
                ux, uy = dx / length, dy / length
                reach = span * 2.5
                lx1, ly1 = x1 - ux * reach, -(y1 - uy * reach)
                lx2, ly2 = x1 + ux * reach, -(y1 + uy * reach)
                if (
                    min(x1, x2) >= clip_min_x
                    and max(x1, x2) <= clip_max_x
                    and min(y1, y2) >= clip_min_y
                    and max(y1, y2) <= clip_max_y
                ):
                    lines_svg.append(
                        f'    <g class="element-group" data-ref="{esc_ref}">'
                        f'<line class="Line {cls_str}" x1="{lx1:.4f}" y1="{ly1:.4f}" '
                        f'x2="{lx2:.4f}" y2="{ly2:.4f}">'
                        f"<title>{escape(label)}</title></line></g>"
                    )

        elif isinstance(el, Point):
            if info.guide:
                continue
            px = _to_svg_coord(el.x)
            py = -_to_svg_coord(el.y)
            if not (math.isfinite(px) and math.isfinite(py)):
                continue
            r_use = pt_r * (
                1.25
                if (
                    "result" in info.classes
                    or "center" in info.classes
                    or "given" in info.classes
                )
                else 1.0
            )
            latex_xy = f"({sp.latex(el.x)}, {sp.latex(el.y)})"
            exact_xy = f"[{el.x}, {el.y}]"
            points_svg.append(
                f'    <g class="element-group" data-ref="{esc_ref}">'
                f'<circle class="Point {cls_str}" cx="{px:.4f}" cy="{py:.4f}" r="{r_use:.4f}" '
                f'data-latex-xy="{_esc_attr(latex_xy)}" data-exact-xy="{_esc_attr(exact_xy)}">'
                f"<title>{escape(label)} = {escape(exact_xy)}</title></circle></g>"
            )
            if label:
                lx = px + pt_r * 1.65
                ly = py - pt_r * 1.45
                inner_lbl = _format_svg_label(label)
                labels_svg.append(
                    f'    <g class="element-group" data-ref="{esc_ref}">'
                    f'<text class="label-halo" x="{lx:.4f}" y="{ly:.4f}" font-family="sans-serif" '
                    f'font-size="{font_sz:.4f}" font-weight="600" stroke="#111318" '
                    f'stroke-width="{font_sz * 0.25:.4f}" stroke-linejoin="round" fill="none">{inner_lbl}</text>'
                    f'<text class="label-fill" x="{lx:.4f}" y="{ly:.4f}" font-family="sans-serif" '
                    f'font-size="{font_sz:.4f}" font-weight="600" fill="#f0f4f8">{inner_lbl}</text>'
                    f"</g>"
                )

    if annotations:
        c_font = font_sz * 0.72
        for ann in annotations:
            ax = _to_svg_coord(ann.get("x", 0))
            ay = -_to_svg_coord(ann.get("y", 0))
            text = str(ann.get("text", ""))
            kind = str(ann.get("kind", "quadrance"))
            ref = str(ann.get("ref", ""))
            if kind == "spread":
                box_cls = "callout-box spread-box"
            elif kind == "paradigm":
                box_cls = "callout-box paradigm-box"
            else:
                box_cls = "callout-box"
            box_w = max(len(text) * c_font * 0.60 + c_font * 0.9, c_font * 2.6)
            box_h = c_font * 1.55
            bx = ax - box_w / 2.0
            by = ay - box_h / 2.0
            ref_attr = f' data-ref="{_esc_attr(ref)}"' if ref else ""
            grp_cls = "element-group" if ref else "callout-item"
            callouts_svg.append(
                f'    <g class="{grp_cls}"{ref_attr}>'
                f'<rect class="{box_cls}" x="{bx:.4f}" y="{by:.4f}" width="{box_w:.4f}" height="{box_h:.4f}" />'
                f'<text class="callout-text" x="{ax:.4f}" y="{ay:.4f}" font-size="{c_font:.4f}">{escape(text)}</text>'
                f"</g>"
            )

    btn_h = max(vb_w, vb_h) * 0.042
    btn_w = btn_h * 1.55
    gap = btn_h * 0.18
    buttons = [
        ("zoom-in", "+"),
        ("zoom-out", "−"),
        ("reset", "⟲"),
        ("labels", "Lbl"),
        ("guides", "Gde"),
    ]
    total_w = len(buttons) * btn_w + (len(buttons) - 1) * gap
    start_bx = vb_x + vb_w - total_w - gap * 1.5
    by_ctrl = vb_y + gap * 1.5
    controls_svg: list[str] = ['  <g class="svg-controls">']
    for i, (action, text) in enumerate(buttons):
        bx = start_bx + i * (btn_w + gap)
        cx_t = bx + btn_w / 2.0
        cy_t = by_ctrl + btn_h / 2.0
        controls_svg.append(
            f'    <g class="svg-control-btn" data-action="{action}">'
            f'<rect x="{bx:.4f}" y="{by_ctrl:.4f}" width="{btn_w:.4f}" height="{btn_h:.4f}" />'
            f'<text x="{cx_t:.4f}" y="{cy_t:.4f}" style="font-size:{btn_h * 0.45:.4f}px">{text}</text>'
            f"</g>"
        )
    controls_svg.append("  </g>")

    svg_lines: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" class="euclid-graphic codes-diagram" '
        f'viewBox="{vb_x:.4f} {vb_y:.4f} {vb_w:.4f} {vb_h:.4f}">',
        f"  <style>{CODES_SVG_CSS}</style>",
        '  <g class="svg-viewport">',
        '    <g class="polygons-layer">',
        *polygons_svg,
        "    </g>",
        '    <g class="circles-layer">',
        *circles_svg,
        "    </g>",
        '    <g class="lines-layer">',
        *lines_svg,
        "    </g>",
        '    <g class="points-layer">',
        *points_svg,
        "    </g>",
        '    <g class="callouts-layer">',
        *callouts_svg,
        "    </g>",
        '    <g class="labels-layer">',
        *labels_svg,
        "    </g>",
        "  </g>",
        *controls_svg,
        f"  <script>{INTERACTIVE_CODES_JS}</script>",
        "</svg>",
    ]

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(svg_lines) + "\n", encoding="utf-8")
    return output_path
