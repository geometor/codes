"""Command-line interface (`codes`) for GEOMETOR Codes."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Sequence

from rich.console import Console
from rich.markup import escape
from rich.table import Table

from geometor.codes.figures import build_all_figures
from geometor.codes.registry import CodesRegistry


def build_parser() -> argparse.ArgumentParser:
    """Build the `codes` CLI argument parser.

    Returns:
        Configured `argparse.ArgumentParser`.
    """
    parser = argparse.ArgumentParser(
        prog="codes",
        description="Comparative explorer of formal geometric languages, syntax, and opus.",
    )
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("summary", help="Display comparative table of all 11 surveyed systems.")

    dec = sub.add_parser("decode", help="Decode a formal symbol, operator, or tactic.")
    dec.add_argument("query", nargs="?", default="", help="Symbol or keyword to decode.")

    op = sub.add_parser("opus", help="Display opus topic coverage across systems.")
    op.add_argument("--domain", default="", help="Filter by domain slug or number.")

    ros = sub.add_parser("rosetta", help="Inspect side-by-side Rosetta Stone benchmarks.")
    ros.add_argument("benchmark", nargs="?", default="", help="Benchmark number or slug.")

    sub.add_parser("hierarchy", help="Display the 7-layer GEOMETOR ecosystem hierarchy.")

    fig = sub.add_parser("build-figures", help="Generate all exact .euclid-graphic SVGs.")
    fig.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Optional directory for generated SVG diagrams.",
    )
    return parser


def _cmd_summary(reg: CodesRegistry, console: Console) -> int:
    table = Table(
        title=f"GEOMETOR Codes — {len(reg.systems)} Formal, Visual & Symbolic Geometric Systems"
    )
    table.add_column("ID", style="cyan bold")
    table.add_column("System", style="white bold")
    table.add_column("Paradigm", style="magenta")
    table.add_column("Metric / Angle", style="yellow")
    table.add_column("License", style="green")
    table.add_column("Local Ref", style="dim")

    for sys_prof in reg.systems:
        loc = "present" if sys_prof.check_local_path() is not None else "ci-offline"
        table.add_row(
            sys_prof.id,
            sys_prof.name,
            sys_prof.paradigm,
            sys_prof.metric_treatment,
            sys_prof.license,
            loc,
        )
    console.print(table)
    return 0


def _cmd_decode(reg: CodesRegistry, query: str, console: Console) -> int:
    matches = reg.decode(query)
    if not matches:
        console.print(f"[red]No lexicon entries matched {query!r}.[/red]")
        return 1
    table = Table(title=f"Syntax Decoder ({len(matches)} match(es))")
    table.add_column("Symbol", style="cyan bold")
    table.add_column("Systems", style="magenta")
    table.add_column("Reading & Plain Meaning", style="white")
    table.add_column("GEOMETOR Equivalent", style="green")
    for entry in matches:
        table.add_row(
            escape(entry.symbol),
            ", ".join(entry.system_ids),
            f"[bold]{escape(entry.pronunciation)}[/bold]: {escape(entry.plain_meaning)}",
            escape(entry.geometor_equivalent),
        )
    console.print(table)
    return 0


def _cmd_opus(reg: CodesRegistry, domain_filter: str, console: Console) -> int:
    counts = reg.opus_coverage_counts()
    summary_tbl = Table(
        title=f"Opus Coverage Summary ({len(reg.topics)} Canonical Topics Across {len(reg.domains)} Domains)"
    )
    summary_tbl.add_column("System", style="cyan bold")
    summary_tbl.add_column("Native", justify="right", style="green")
    summary_tbl.add_column("Derived", justify="right", style="blue")
    summary_tbl.add_column("Partial", justify="right", style="yellow")
    summary_tbl.add_column("Broken", justify="right", style="red bold")
    summary_tbl.add_column("Absent", justify="right", style="dim")
    for sys_prof in reg.systems:
        c = counts[sys_prof.id]
        summary_tbl.add_row(
            sys_prof.name,
            str(c["native"]),
            str(c["derived"]),
            str(c["partial"]),
            str(c["broken"]),
            str(c["absent"]),
        )
    console.print(summary_tbl)

    if domain_filter:
        filt = domain_filter.strip().lower()
        for dom in reg.domains:
            if filt in (dom.id.lower(), str(dom.number)):
                dtbl = Table(title=f"Domain {dom.number}: {dom.title}")
                dtbl.add_column("Topic (`snake_case`)", style="cyan bold")
                dtbl.add_column("Role", style="magenta")
                dtbl.add_column("GEOMETOR", style="green")
                dtbl.add_column("Byrne", style="red")
                dtbl.add_column("SymPy", style="yellow")
                dtbl.add_column("Mathlib4", style="blue")
                dtbl.add_column("LeanEuclid", style="white")
                for t in reg.topics:
                    if t.domain_id == dom.id:
                        dtbl.add_row(
                            t.id,
                            t.role,
                            t.coverage["geometor_model"].status,
                            t.coverage["byrne_1847"].status,
                            t.coverage["sympy_geometry"].status,
                            t.coverage["mathlib4"].status,
                            t.coverage["leaneuclid"].status,
                        )
                console.print(dtbl)
    return 0


def _cmd_rosetta(reg: CodesRegistry, bench_query: str, console: Console) -> int:
    q = bench_query.strip().lower()
    selected = [
        b
        for b in reg.benchmarks
        if not q or q in (b.id.lower(), str(b.number), f"0{b.number}")
    ]
    if not selected:
        console.print(f"[red]No Rosetta benchmark matched {bench_query!r}.[/red]")
        return 1
    for b in selected:
        console.print(
            f"\n[bold cyan]Benchmark {b.number}: {b.title}[/bold cyan] "
            f"([green]{b.geometor_signature}[/green] | {b.euclid_ref})"
        )
        console.print(f"  {b.geometric_essence}")
        if q:
            for sys_id, imp in b.implementations.items():
                console.print(f"  • [magenta]{sys_id}[/magenta] ({escape(imp.source_ref)}):")
                for line in imp.code.splitlines():
                    console.print(f"      {escape(line)}")
    return 0


def _cmd_hierarchy(reg: CodesRegistry, console: Console) -> int:
    table = Table(title="GEOMETOR 7-Layer Ecosystem Hierarchy")
    table.add_column("Layer", style="cyan bold")
    table.add_column("Epistemic Role", style="white")
    table.add_column("Repositories", style="green")
    for lyr in reg.layers:
        repos_str = ", ".join(r.name for r in lyr.repos)
        table.add_row(f"L{lyr.layer_index}: {lyr.title}", lyr.epistemic_role, repos_str)
    console.print(table)
    return 0


def run_cli(argv: Sequence[str] | None = None) -> int:
    """Execute the `codes` CLI and return an exit status code.

    Args:
        argv: Optional sequence of command-line arguments.

    Returns:
        Process exit code (`0` on success).
    """
    parser = build_parser()
    args = parser.parse_args(argv)
    console = Console()

    if args.command == "build-figures":
        written = build_all_figures(output_dir=args.output_dir)
        console.print(
            f"[green]Built and verified {len(written)} exact .euclid-graphic SVG figures.[/green]"
        )
        for p in written:
            console.print(f"  • {p}")
        return 0

    reg = CodesRegistry()
    if args.command in (None, "summary"):
        return _cmd_summary(reg, console)
    if args.command == "decode":
        return _cmd_decode(reg, args.query, console)
    if args.command == "opus":
        return _cmd_opus(reg, args.domain, console)
    if args.command == "rosetta":
        return _cmd_rosetta(reg, args.benchmark, console)
    if args.command == "hierarchy":
        return _cmd_hierarchy(reg, console)
    return 0
