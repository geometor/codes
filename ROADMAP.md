# GEOMETOR Codes Roadmap

## Phase 1 — Initial Comparative Study (`v0.1.0`, Complete)

- [x] Deep forensic source audit across 11 formal, visual, and symbolic geometry systems (`LeanEuclid`, `GeoCoq`, `mathlib4`, `AlphaGeometry`, `Newclid`/`Yuclid`, `JGEX`, `kingdon`/`galgebra` PGA & CGA, `CindyJS`, `sympy.geometry` 1.14.0, `Byrne 1847 / Rougeux`, and `geometor.model`).
- [x] Structured JSON registries (`systems.json`, `syntax_lexicon.json`, `opus_matrix.json`, `rosetta_benchmarks.json`, `geometor_hierarchy.json`) + typed `CodesRegistry` API and `codes` CLI.
- [x] Nine 100% exact float-free `geometor.model` `.euclid-graphic` SVGs with algebraic `zero_test` and Rational Trigonometry verification.
- [x] Complete Sphinx codex (`docsrc/` -> `publish build`) covering Hierarchy, Syntax Field Guide, System Dossiers, Rosetta Benchmarks, and 8-Domain Opus Matrix.

## Phase 2 — Cross-System Transpilers & Live Translators (`v0.2.0`)

- [ ] **System E Proof Emitter**: Translate `geometor.model.Model` construction DAGs (with persisted `side_of` / `between` / `beyond` selector ASTs) directly into `LeanEuclid` `euclid_apply` scripts.
- [ ] **JGEX / Newclid Clause Exporter**: Emit 1-line `defs.txt` / Newclid problem clauses from `geometor.elements` constructions for automated `DD+AR` cross-checking.
- [ ] **Byrne Inline Micro-Glyph Extension**: Prototype optional inline 14px SVG stroke/wedge/polygon badges for `:g:` roles in `photon-platform/publish`.

## Phase 3 — Downstream GEOMETOR Kernel & Library Upgrades (`v0.3.0`)

- [ ] Implement constructive BFMSS root-separation bounds in `geometor.model.algebra.zero_test`.
- [ ] Add `geometor.model.inversion` (Steiner power, radical axis, circle inversion, pole–polar) and `ProjectiveConic` $3 \times 3$ matrices in `geometor.pappus`.
- [ ] Complete Chou–Gao–Zhang's coordinate-free Area-Method eliminator (`signed_area2` + `pythagoras_diff`) in `geometor.wildberger`.
- [ ] Submit upstream bug-fix PRs to `sympy/sympy` for `Triangle.excenters` and `Point.affine_rank`.
