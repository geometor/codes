"""Build and verify all exact `.euclid-graphic` SVG figures for GEOMETOR Codes."""

from __future__ import annotations

from pathlib import Path
import sys

_REPO_ROOT = Path(__file__).resolve().parents[1]
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from geometor.codes.figures import build_all_figures  # noqa: E402


def main() -> None:
    """Build all SVG diagrams and print summary."""
    paths = build_all_figures()
    print(f"Built {len(paths)} verified exact SVG figures:")
    for p in paths:
        print(f"  - {p.relative_to(_REPO_ROOT)}")


if __name__ == "__main__":
    main()
