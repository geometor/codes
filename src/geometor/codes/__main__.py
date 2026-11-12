"""Executable module entry point (`python -m geometor.codes`)."""

from __future__ import annotations

import sys

from geometor.codes.cli import run_cli


def main() -> None:
    """Invoke the `codes` CLI entry point."""
    raise SystemExit(run_cli(sys.argv[1:]))


if __name__ == "__main__":
    main()
