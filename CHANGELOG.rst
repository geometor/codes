=========
Changelog
=========

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
