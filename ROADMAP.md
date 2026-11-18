# GEOMETOR Codes Roadmap

## Phase 1 — Initial Comparative Study (`v0.1.0`, Complete)

- [x] Deep forensic source audit across 11 formal, visual, and symbolic geometry systems (`LeanEuclid`, `GeoCoq`, `mathlib4`, `AlphaGeometry`, `Newclid`/`Yuclid`, `JGEX`, `kingdon`/`galgebra` PGA & CGA, `CindyJS`, `sympy.geometry` 1.14.0, `Byrne 1847 / Rougeux`, and `geometor.model`).
- [x] Structured JSON registries (`systems.json`, `syntax_lexicon.json`, `opus_matrix.json`, `rosetta_benchmarks.json`, `geometor_hierarchy.json`) + typed `CodesRegistry` API and `codes` CLI.
- [x] Nine 100% exact float-free `geometor.model` `.euclid-graphic` SVGs with algebraic `zero_test` and Rational Trigonometry verification.
- [x] Complete Sphinx codex (`docsrc/` -> `publish build`) covering Hierarchy, Syntax Field Guide, System Dossiers, Rosetta Benchmarks, and 8-Domain Opus Matrix.

## Phase 1b — Principles Catalog (`v0.2.0`, Complete)

- [x] Canonical Lexicon, base-context miners, discovery pipeline (1,425 items → 667 principles, 107 multi-system), linked-library indexers, and 20 exact pilot witnesses.

## Phase 1c — Truth Foundations (`v0.3.0`, Complete)

- [x] Seven-layer **Trust Stack** and **Truth Ladder** (L0 Plausible → L5 Foundational, plus H Human) over 12 systems (`resources/foundations.toml`, `geometor.codes.foundations`).
- [x] Interactive Atlas, system cards, comparison axes, and Graphviz graphs (ladder, trust, bridges, lifts, ontologies, shared principles).
- [x] Showcase: one theorem, many foundations (I.5, I.47, III.31, Simson, Pasch) with commit-pinned source excerpts and build-time **L2 generic witnesses** (`geometor.codes.generic`).
- [x] Catalog demoted to one searchable appendix; legacy `docsrc/principles/` retired.

## Next — Climbing the Ladder

- [ ] **model strict mode**: an opt-in `zero_test` with no numeric acceptance branch (currently `|evalf(80)| < 1e-65` in `geometor.model.algebra`) so L1 witnesses are fully exact. To be implemented in `model`, not here.
- [ ] **L1 → L2 lift**: generalize `geometor.codes.generic` from hand-built parametrizations to automatic symbolic re-parametrization of `Model` DAGs, with NDG conditions reported.
- [ ] **Lean certificate export** (L2 → L4/L5): emit `linear_combination` / `polyrith`-style certificates for mathlib from generic witnesses.
- [ ] **LeanEuclid SMT reconstruction** watch: track whether `SMT_VERIF` is replaced by kernel-checked proof reconstruction (would move LeanEuclid from L3 to L4).
- [ ] Extend the showcase beyond five theorems, and the Atlas with mined coverage per system.

## Phase 2 — Cross-System Transpilers & Live Translators

- [ ] **System E Proof Emitter**: Translate `geometor.model.Model` construction DAGs (with persisted `side_of` / `between` / `beyond` selector ASTs) directly into `LeanEuclid` `euclid_apply` scripts.
- [ ] **JGEX / Newclid Clause Exporter**: Emit 1-line `defs.txt` / Newclid problem clauses from `geometor.elements` constructions for automated `DD+AR` cross-checking.
- [ ] **Byrne Inline Micro-Glyph Extension**: Prototype optional inline 14px SVG stroke/wedge/polygon badges for `:g:` roles in `photon-platform/publish`.

## Phase 3 — Downstream GEOMETOR Kernel & Library Upgrades

- [ ] Implement constructive BFMSS root-separation bounds in `geometor.model.algebra.zero_test`.
- [ ] Add `geometor.model.inversion` (Steiner power, radical axis, circle inversion, pole–polar) and `ProjectiveConic` $3 \times 3$ matrices in `geometor.pappus`.
- [ ] Complete Chou–Gao–Zhang's coordinate-free Area-Method eliminator (`signed_area2` + `pythagoras_diff`) in `geometor.wildberger`.
- [ ] Submit upstream bug-fix PRs to `sympy/sympy` for `Triangle.excenters` and `Point.affine_rank`.
