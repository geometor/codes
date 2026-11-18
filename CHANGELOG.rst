=========
Changelog
=========

0.3.0 (2026-11-18)
------------------

- **added** Truth Foundations model (`resources/foundations.toml`,
  `geometor.codes.foundations`): a seven-layer Trust Stack and a Truth Ladder
  (L0 Plausible → L5 Foundational, plus H Human) placing 12 systems, 12 trusted
  components, 11 bridges, and 4 lifts, with `codes foundations` audit.
- **added** Graphviz graph builders (`geometor.codes.graphs`): truth ladder,
  per-system trust chains, who-trusts-what, bridges, ontology map, shared
  principle overlap, and per-theorem realization graphs.
- **added** Showcase (`resources/showcase.toml`): Euclid I.5, I.47, III.31, the
  Simson line, and Pasch realized side by side with commit-pinned source excerpts.
- **added** L2 generic witnesses in exact SymPy (`geometor.codes.generic`,
  `codes generic`) for four showcase theorems; Pasch recorded as an order gap.
- **changed** Site restructured around an interactive Atlas, system cards,
  comparison axes, connections, and findings; the 667-principle catalog is now a
  single searchable appendix (`codes build-site`; `build-principles` kept as an
  alias). Legacy `docsrc/principles/` pages removed.
- **changed** Header navigation leads with Foundations, Showcase, Catalog, and
  Systems; Hierarchy, Syntax, Rosetta, and Opus moved to the footer.
- **fixed** Sphinx build now reports 0 warnings (napoleon `ivar` duplicates,
  heading lengths, docstring formatting).

0.2.0 (2026-11-17)
------------------

- **added** Canonical Lexicon (`resources/lexicon/lexicon.toml`, `conventions.md`,
  `geometor.codes.lexicon`) with 127 concepts, 271 cross-system aliases seeded
  from `geometor.etc` `ops.py`, and `codes lexicon audit`.
- **added** Base-context miners (`geometor.codes.mine`) for Euclid (628),
  LeanEuclid (309), AlphaGeometry (115), Newclid (87), SymPy (218), and
  `geometor.model` (68) with deterministic JSONL snapshots in `resources/mined/`.
- **added** Discovery pipeline (`geometor.codes.discover`) normalizing predicates
  and clustering all 1,425 base items into 667 candidate principles (107
  multi-system, 0 unassigned) with relabeling-invariant fingerprints.
- **added** Linked-library indexers and matchers (`geometor.codes.link`) across
  GeoCoq (5,435), mathlib4 (1,567), JGEX (791), kingdon (94), galgebra (107),
  and CindyJS (937).
- **added** Exact `geometor.model` verification (`geometor.codes.verify`) for 20
  pilot principles (plus 3 explicit order/betweenness gaps) and ETC-style
  Codex presentation under `docsrc/principles/` with `.euclid-graphic` SVGs.
- **added** CLI commands: `lexicon`, `mine`, `discover`, `principle`, `search`,
  `coverage`, `verify`, and `build-principles`.

0.1.1 (2026-11-15)
------------------

- Ensure canonical GEOMETOR ``logo.png`` and ``favicon.ico`` brand assets are provisioned in ``docsrc/_static/`` and rendered in site headers and browser tabs.

0.1.0 (2026-11-12)
------------------

- Initial comparative study and executable registry of **10 formal geometric
  languages, theorem provers, deduction engines, and algebraic calculi**
  (``LeanEuclid`` / System :math:`\mathbf{E}`, ``GeoCoq``, ``mathlib4``,
  ``AlphaGeometry``, ``Newclid``, ``Java-Geometry-Expert``, ``kingdon`` &
  ``galgebra`` PGA/CGA, ``CindyJS`` :math:`\mathbb{CP}^2`, ``sympy.geometry``,
  and ``geometor.model`` + ``wildberger``).
- Added structured JSON datasets in ``resources/``: ``systems.json``,
  ``syntax_lexicon.json``, ``opus_matrix.json``, ``rosetta_benchmarks.json``,
  and ``geometor_hierarchy.json``.
- Implemented ``geometor.codes.registry``, ``geometor.codes.figures``,
  ``geometor.codes.render``, and ``codes`` CLI (``summary``, ``decode``,
  ``opus``, ``rosetta``, ``hierarchy``, ``build-figures``).
- Authored Sphinx codex covering the **7 Paradigms**, **GEOMETOR 7-Layer
  Ecosystem Hierarchy**, **Strange-Symbol Syntax Field Guide**, **9 Deep System
  Dossiers**, **7 Rosetta Stone Benchmarks**, and **8-Domain Opus Matrix**.
