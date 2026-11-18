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

    lex = sub.add_parser("lexicon", help="Inspect or audit the canonical lexicon.")
    lex.add_argument("action", choices=("audit", "search"), help="Lexicon action.")
    lex.add_argument("query", nargs="?", default="", help="Search query when action=search.")

    sub.add_parser("mine", help="Mine all base-context systems into resources/mined/.")
    sub.add_parser("discover", help="Cluster base items and match linked libraries.")

    pr = sub.add_parser("principle", help="Display an ETC-style card for one principle.")
    pr.add_argument("id", help="Canonical principle ID (e.g. isosceles_base_angles).")

    srch = sub.add_parser("search", help="Search discovered principles.")
    srch.add_argument("query", help="Keyword to search in IDs, titles, statements, and forms.")

    sub.add_parser("coverage", help="Display base-item and multi-system coverage stats.")
    sub.add_parser("verify", help="Run exact geometor.model verification on pilot principles.")
    sub.add_parser("build-site", help="Generate docsrc/ foundations, showcase, and catalog pages.")
    sub.add_parser("build-principles", help="Alias of build-site (backward compatible).")
    sub.add_parser("foundations", help="Show the Truth Ladder and audit foundations/showcase data.")
    sub.add_parser("generic", help="Run symbolic-parameter (L2) witnesses for showcase theorems.")
    return parser


def _cmd_foundations(console: Console) -> int:
    from geometor.codes.foundations import audit_foundations, load_foundations, load_showcase

    fnd = load_foundations()
    showcase = load_showcase()
    table = Table(title="Truth Ladder — what each system certifies")
    table.add_column("Level", style="bold")
    table.add_column("Claim", style="magenta")
    table.add_column("Systems", style="cyan")
    table.add_column("Trusted core", style="yellow")
    for lv in sorted(fnd.levels, key=lambda x: -x.rank):
        members = fnd.systems_at(lv.id)
        cores = sorted({t for s in members for t in s.trusts})
        table.add_row(
            f"{lv.id} {lv.name}",
            lv.claim,
            ", ".join(s.short for s in members) or "—",
            ", ".join(cores) or "—",
        )
    console.print(table)
    problems = audit_foundations(fnd, showcase)
    for p in problems:
        console.print(f"[red]✗[/red] {escape(p)}")
    if not problems:
        console.print(
            f"[green]✓ {len(fnd.systems)} systems, {len(fnd.bridges)} bridges, "
            f"{len(showcase)} showcase theorems — consistent[/green]"
        )
    return 1 if problems else 0


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


def _cmd_lexicon(action: str, query: str, console: Console) -> int:
    from geometor.codes.lexicon import Lexicon, audit_lexicon

    if action == "audit":
        rep = audit_lexicon()
        console.print(
            f"[cyan]Lexicon:[/cyan] {rep.stats['entries']} entries, {rep.stats['aliases']} aliases, "
            f"{rep.stats['etc_functions']} etc ops functions, {rep.stats['files_scanned']} files scanned."
        )
        if rep.problems or rep.etc_missing or rep.unresolved_sympy:
            for item in rep.problems + rep.etc_missing + rep.unresolved_sympy:
                console.print(f"[red]  ! {escape(item)}[/red]")
            return 1
        tbl = Table(title=f"Canonical Rename Proposals ({len(rep.proposals)})")
        tbl.add_column("System", style="magenta")
        tbl.add_column("Current", style="yellow")
        tbl.add_column("Canonical", style="green bold")
        tbl.add_column("Where", style="dim")
        for p in rep.proposals:
            tbl.add_row(p.system, p.current, p.canonical, p.where)
        console.print(tbl)
        return 0

    lex = Lexicon.load()
    hits = lex.search(query)
    tbl = Table(title=f"Lexicon Search ({len(hits)} match(es))")
    tbl.add_column("Canonical", style="cyan bold")
    tbl.add_column("Kind", style="magenta")
    tbl.add_column("Summary", style="white")
    for e in hits:
        tbl.add_row(e.name, e.kind, escape(e.summary))
    console.print(tbl)
    return 0


def _cmd_principle(pid: str, console: Console) -> int:
    from geometor.codes.discover import load_catalog

    cat = load_catalog()
    p = cat.by_id(pid)
    if p is None:
        console.print(f"[red]Principle {pid!r} not found.[/red]")
        return 1
    console.print(f"[bold cyan]{p.id}[/bold cyan] · {escape(p.title)} ([magenta]{p.kind}[/magenta], {p.family})")
    if p.euclid_refs:
        console.print(f"  [yellow]Euclid:[/yellow] {', '.join(p.euclid_refs)}")
    if p.statement:
        console.print(f"  [white]{escape(p.statement)}[/white]")
    if p.canonical_form:
        console.print(f"  [green]Canonical:[/green] {escape(p.canonical_form)}")
    tbl = Table(title=f"Realizations ({len(p.members)} base, {len(p.linked)} linked)")
    tbl.add_column("System", style="cyan")
    tbl.add_column("ID", style="white")
    tbl.add_column("Statement", style="dim")
    for m in p.members:
        tbl.add_row(m.system, m.id, escape((m.statement or m.canonical_form)[:100]))
    for lk in p.linked:
        tbl.add_row(f"{lk['system']} (linked)", lk["name"], escape(f"{lk['confidence']} {lk['evidence']}"))
    console.print(tbl)
    return 0


def _cmd_search_principles(query: str, console: Console) -> int:
    from geometor.codes.discover import load_catalog

    cat = load_catalog()
    q = query.lower()
    hits = [
        p
        for p in cat.principles
        if q in p.id.lower() or q in p.title.lower() or q in p.statement.lower() or q in p.canonical_form.lower()
    ]
    tbl = Table(title=f"Principles matching {query!r} ({len(hits)})")
    tbl.add_column("ID", style="cyan bold")
    tbl.add_column("Family", style="magenta")
    tbl.add_column("Systems", style="green")
    tbl.add_column("Statement", style="white")
    for p in hits[:30]:
        tbl.add_row(
            p.id,
            p.family,
            ", ".join(sorted({m.system for m in p.members})),
            escape((p.canonical_form or p.statement)[:90]),
        )
    console.print(tbl)
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

    if args.command == "lexicon":
        return _cmd_lexicon(args.action, args.query, console)

    if args.command == "mine":
        from geometor.codes.context import mine_all_base

        for res in mine_all_base():
            console.print(f"[green]{res.system:16s}[/green] {len(res.decls):4d}  {res.counts()}")
        return 0

    if args.command == "discover":
        from geometor.codes.discover import discover_principles, save_catalog
        from geometor.codes.link import index_all_linked, match_linked_to_catalog

        idx_counts = index_all_linked()
        cat = discover_principles()
        matched = match_linked_to_catalog(cat)
        out = save_catalog(cat)
        console.print(f"[green]Saved {out}[/green] stats={cat.stats}")
        console.print(f"Indexed={idx_counts} Matched={matched}")
        return 0

    if args.command == "principle":
        return _cmd_principle(args.id, console)

    if args.command == "search":
        return _cmd_search_principles(args.query, console)

    if args.command == "coverage":
        from geometor.codes.discover import load_catalog

        cat = load_catalog()
        console.print(f"[cyan]Catalog stats:[/cyan] {cat.stats}")
        return 0

    if args.command == "verify":
        import logging

        from geometor.codes.verify import verify_pilot

        logging.disable(logging.INFO)
        for r in verify_pilot():
            color = "green" if r.status == "verified" else "yellow"
            console.print(f"[{color}]{r.status:8s}[/{color}] {r.principle_id:28s} {escape(r.summary)}")
        return 0

    if args.command in ("build-site", "build-principles"):
        import logging

        from geometor.codes.present import build_site_docs

        logging.disable(logging.INFO)
        counts = build_site_docs()
        console.print(f"[green]Generated docsrc/ foundations, showcase, catalog:[/green] {counts}")
        return 0

    if args.command == "foundations":
        return _cmd_foundations(console)

    if args.command == "generic":
        from geometor.codes.generic import GENERIC_BUILDERS, GENERIC_GAPS

        for pid, builder in GENERIC_BUILDERS.items():
            w = builder()
            color = "green" if w.proved else "red"
            console.print(
                f"[{color}]{'proved' if w.proved else 'FAILED':7s}[/{color}] {pid:24s} "
                f"params={','.join(w.parameters)}  NDG: {escape('; '.join(w.ndg))}"
            )
        for pid, reason in GENERIC_GAPS.items():
            console.print(f"[yellow]gap    [/yellow] {pid:24s} {escape(reason)}")
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
