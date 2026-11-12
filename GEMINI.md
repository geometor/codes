# GEOMETOR Codes (`geometor-codes`)

Comparative study, syntax lexicon, 69-topic Opus coverage matrix, 7 Rosetta Stone benchmarks, and exact `.euclid-graphic` SVG demonstrations across **11 formal, visual, and symbolic geometry architectures**.

## Purpose & Scope

`geometor/codes` occupies **Layer 2 (Comparative Formal Languages & Symbolic Meta-Study)** in the 7-layer, 33-repository GEOMETOR ecosystem. It audits external theorem provers, algebraic calculi, and visual pseudocodes so their strongest ideas directly inform `geometor.model`, `geometor.elements` 2.0 (*Principles of Geometry*), `geometor.wildberger`, `geometor.pappus`, `geometor.etc`, `geometor.divine`, and `geometor.seer`.

## Key Modules & Datasets

- `resources/systems.json` — Architectural profiles of all 11 systems (`leaneuclid`, `geocoq`, `mathlib4`, `alphageometry`, `newclid`, `jgex`, `pga_cga`, `cindyjs`, `sympy_geometry`, `byrne_1847`, `geometor_model`).
- `resources/syntax_lexicon.json` — 60-entry strange-symbol, binder, predicate, tactic, multivector blade, and visual-token decoder.
- `resources/opus_matrix.json` — 69 canonical `snake_case` geometric topics across 8 domains $\times$ 11 systems (`759` audited cells).
- `resources/rosetta_benchmarks.json` — 7 canonical geometric constructions/theorems encoded side-by-side across all 11 systems (`77` implementations).
- `resources/geometor_hierarchy.json` — Complete 7-layer, 33-repository GEOMETOR architecture map + 11 prioritized engineering recommendations.
- `src/geometor/codes/registry.py` — Immutable Python 3.13 dataclasses and `CodesRegistry` query engine (100% standalone on CI when `_refs/` clones are absent).
- `src/geometor/codes/figures.py` & `render.py` — 9 exact float-free `geometor.model.Model(..., auto_intersect=False)` builders and `.euclid-graphic` SVG exporters.
- `src/geometor/codes/cli.py` — Rich terminal CLI (`codes summary`, `decode`, `opus`, `rosetta`, `hierarchy`, `build-figures`).

## Verification Gates (Offline Sandbox)

```bash
/home/phi/PROJECTS/geometor/.venv/bin/python -m pytest
/home/phi/.local/bin/ruff check src tests demos
/home/phi/.local/bin/publish build
```
