"""Comparative Study of Formal Languages, Syntax, and Opus Across Geometric Logic.

Provides structured registries, strange-symbol decoders, cross-system Rosetta
benchmarks, opus coverage analytics, and exact ``geometor.model`` interactive
``.euclid-graphic`` SVG figure builders for ``geometor-codes``.
"""

from __future__ import annotations

from geometor.codes.cli import run_cli
from geometor.codes.figures import FIGURE_SPECS, FigureSpec, build_all_figures
from geometor.codes.registry import CodesRegistry
from geometor.codes.render import render_svg

__version__ = "0.1.0"

__all__ = [
    "FIGURE_SPECS",
    "CodesRegistry",
    "FigureSpec",
    "__version__",
    "build_all_figures",
    "render_svg",
    "run_cli",
]
