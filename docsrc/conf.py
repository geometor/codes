"""Sphinx configuration for GEOMETOR Codes."""

from __future__ import annotations

import os
from pathlib import Path
import re
import sys
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[1]
_WORKSPACE_ROOT = _REPO_ROOT.parent
for _extra_path in (
    _REPO_ROOT / "src",
    _WORKSPACE_ROOT / "model" / "src",
    _WORKSPACE_ROOT / ".venv" / "lib" / "python3.13" / "site-packages",
):
    if _extra_path.exists() and str(_extra_path) not in sys.path:
        sys.path.insert(0, str(_extra_path))

from photon_platform.publish.global_conf import *  # noqa: E402, F403

import geometor.codes as module  # noqa: E402

version = module.__version__

org = "geometor"
org_name = "GEOMETOR"

repo = "codes"
repo_name = "codes"

setup_globals(org, org_name, repo, repo_name)  # noqa: F405

# Configure offline-safe local intersphinx inventories across the GEOMETOR workspace
for _remote_key in list(intersphinx_mapping.keys()):  # noqa: F405
    _entry = intersphinx_mapping[_remote_key]  # noqa: F405
    if _entry[1] is None:
        intersphinx_mapping.pop(_remote_key, None)  # noqa: F405

for _sister in (
    "euclid",
    "elements",
    "fundamentals",
    "etc",
    "pacioli",
    "pappus",
    "wildberger",
    "hilbert",
    "hoenen",
    "proclus",
):
    _inv = _WORKSPACE_ROOT / _sister / "docs" / "objects.inv"
    if _inv.is_file():
        intersphinx_mapping[_sister] = (  # noqa: F405
            f"https://geometor.github.io/{_sister}",
            (os.fspath(_inv), None),
        )

html_theme = "foundation"
html_static_path: list[str] = ["_static"]
html_logo = None
autoapi_add_toctree_entry = False
if "intro.rst" not in exclude_patterns:  # noqa: F405
    exclude_patterns.append("intro.rst")  # noqa: F405
suppress_warnings = ["autoapi.python_import_resolution", "toc.not_included"]

_IMG_SVG_RE = re.compile(
    r'<img\b[^>]*?\bsrc="(?P<src>[^"]*?\.svg)"[^>]*?>'
)


def _inline_codes_svgs(
    app: Any,  # noqa: ANN401
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Any,  # noqa: ANN401
) -> None:
    """Replace `<img src="...svg">` for our `.euclid-graphic` figures with inline `<svg>`.

    Args:
        app: Sphinx application instance.
        pagename: Current document page name.
        templatename: Template name used to render the page.
        context: HTML template context dictionary.
        doctree: Document tree node.
    """
    del templatename, doctree
    body = context.get("body")
    if not body or ".svg" not in body:
        return

    outdir = Path(app.outdir)
    srcdir = Path(app.srcdir)

    def _repl(match: re.Match[str]) -> str:
        src = match.group("src")
        svg_name = Path(src).name
        if "graphviz" in src:
            return match.group(0)
        candidates = [
            outdir / pagename / ".." / src,
            srcdir / "_static" / "figures" / svg_name,
            srcdir / Path(pagename).parent / svg_name,
            outdir / "_images" / svg_name,
        ]
        for cand in candidates:
            try:
                resolved = cand.resolve()
                if resolved.exists() and resolved.suffix == ".svg":
                    raw_svg = resolved.read_text(encoding="utf-8")
                    if "euclid-graphic" not in raw_svg:
                        continue
                    idx = raw_svg.find("<svg")
                    if idx != -1:
                        return raw_svg[idx:]
            except OSError:
                continue
        return match.group(0)

    context["body"] = _IMG_SVG_RE.sub(_repl, body)


def setup(app: Any) -> None:  # noqa: ANN401
    """Register Sphinx build event hooks for GEOMETOR Codes.

    Args:
        app: Sphinx application instance.
    """
    app.connect("html-page-context", _inline_codes_svgs)
