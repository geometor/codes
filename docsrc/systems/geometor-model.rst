.. _system-geometor:

========================================================================
GEOMETOR (``geometor.model`` + Ecosystem): Exact Constructive Synthesis
========================================================================

* **Core Kernel**: ``model/src/geometor/model/`` (`v0.6.0`, MIT) + 32 sister repositories across 7 layers
* **Mathematical Foundation**: Targeted constructive ancestral DAGs (``Model(..., auto_intersect=False)``) over exact SymPy :term:`Algebraic Number Polynomial` (`ANP`) fields, System-E-equivalent topological selectors, :person:`Norman J. Wildberger <wildberger>`'s Rational Trigonometry invariants, and Byrne/Rougeux-inspired ``:g:`` :math:`\leftrightarrow` ``.euclid-graphic`` SVGs

1. Core Kernel Architecture (``geometor.model``)
------------------------------------------------

Auditing all modules in ``model/src/geometor/model/`` confirms how GEOMETOR avoids the traps that afflict generic CAS libraries and floating-point sketchers:

1. **Strict Zero-Float Gate (`model.py`)**: ``Model.__setitem__`` inspects every coordinate expression and rejects ``float`` / ``sp.Float`` contamination at insertion time, guaranteeing 100% exact symbolic lineage across :math:`\mathbb{Q}`, :math:`\mathbb{Q}(\sqrt{d})`, :math:`\mathbb{Q}(\phi)`, and nested quadratic towers.
2. **Targeted Ancestral DAG & Closed-Form Intersections (`intersections.py`)**: Setting ``auto_intersect=False`` replaces :math:`O(N^2)` combinatorial intersection explosion with explicit ``model.intersect(el1, el2, ...)`` calls solved via **closed-form radical-axis quadratic formulas**—never invoking SymPy's slow ``Circle.intersection`` / ``solve()``—and folded cleanly via ``with model.subconstruction(...) as scope: scope.keep(...)``.
3. **Deterministic Topological Selectors**: ``side_of=(p1, p2, ±1)`` (via exact ``signed_area2``), ``between=(p1, p2)``, ``beyond=(p1, p2)``, ``on_ray=(p1, p2)``, and ``other_than=pt`` disambiguate quadratic roots without floating-point branch jumping.
4. **Canonical ``ANP`` Zero-Testing & Rational Trigonometry (`algebra.py`, `invariants.py`, `proof.py`)**: ``zero_test`` reduces nested radical expressions inside ``sp.QQ.algebraic_field`` via ``primitive_element``, powering ``@proposition`` assertions (``assert_equal``, ``assert_spread_equal``, ``assert_perpendicular``, ``assert_parallel``, ``assert_congruent``, ``assert_area_equal``) alongside polynomial ``quadrance``, ``line_spread``, ``vertex_spread``, ``signed_area2``, and ``cross_ratio``.

.. figure:: /_static/figures/08-rosetta-centers-euler.svg
   :align: center
   :width: 100%

   **Figure 8 — Exact Rational Triangle Centers & Nine-Point Circle on the 13-14-15 Heronian Triangle**: Constructed purely by compass and straightedge in ``geometor.codes.figures``, yielding exact rational coordinates :g:`X1` ``= (6, 4)``, :g:`X2` ``= (19/3, 4)``, :g:`X3` ``= (7, 33/8)``, :g:`X4` ``= (5, 15/4)``, and :g:`X5` ``= (6, 63/16)`` on the Euler line :g:`[ X3 X4 ]`.

.. figure:: /_static/figures/09-rosetta-pappus-harmonic.svg
   :align: center
   :width: 100%

   **Figure 9 — Exact Projective Pappus Hexagon & Harmonic Range**: Verifying ``signed_area2(X, Y, Z) == 0`` along Pappus axis :g:`[ X Z ]` and ``cross_ratio(O, B1, A1, C1) == -1`` on :g:`[ O C1 ]`.

2. Honest Self-Audit & Synthesis Roadmap
----------------------------------------

Comparing ``geometor.model`` (`v0.6.0`) against our 10 peer systems highlights three honest internal limitations—each directly addressed by our :ref:`11 Architectural Blueprints <hierarchy-geometor>`:

1. **High-Complexity Fallback in ``algebra.zero_test`` (`lines 247-251`)**: When ``count_ops(expr) > 25``, ``zero_test`` skips ``primitive_element`` and falls back to ``abs(expr.evalf(80)) < 1e-65``. Upgrading this to constructive **BFMSS root-separation bounds** (`Blueprint 1`) achieves 100% mathematical soundness at arbitrary tower depth.
2. **Step AST & Géométrographie Telemetry**: Recording structured selector ASTs (`Blueprint 2`) and :person:`Émile Lemoine <lemoine>`'s :math:`(R_1, R_2, C_1, C_2, C_3)` operational counts (`Blueprint 3`) on ``Step`` turns every ``Model`` into both a ``LeanEuclid`` proof generator and a quantitative complexity benchmark.
3. **First-Class Inversion, :math:`3 \times 3` Conics & Area Elimination**: Promoting ``geometor.model.inversion`` (`Blueprint 4`), ``ProjectiveConic`` :math:`3 \times 3` symmetric matrices in ``geometor.pappus`` (`Blueprint 5`), and Chou–Gao–Zhang backward elimination in ``geometor.wildberger`` (`Blueprint 6`) completes a unified multi-lens engine unmatched by any single external system.
