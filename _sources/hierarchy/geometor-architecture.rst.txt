.. _hierarchy-geometor:

====================================================================
The 7-Layer GEOMETOR Architecture & 11 Blueprints from ``codes``
====================================================================

How do 33 repositories—ranging from polytonic Greek treatises of :person:`Aristotle <aristotle>` and :person:`Proclus <proclus>` to four-color plates of :person:`Oliver Byrne <byrne>`, 53,000 triangle centers of :person:`Clark Kimberling <kimberling>`, Rational Trigonometry of :person:`Norman J. Wildberger <wildberger>`, botanical phyllotaxis, and multi-agent program synthesis (`seer`)—cohere into a single architecture?

Our audit organizes the entire **GEOMETOR** workspace into **seven epistemic and computational layers**, placing ``geometor/codes`` at **Layer 2** as the translational bridge between the primary historical canon (**Layers 0–1**) and the executable symbolic software stack (**Layers 3–6**).

.. figure:: /_static/figures/07-vesica-golden-poles.svg
   :align: center
   :width: 100%

   **Figure 7 — Just-In-Time Emergence of the Golden Chain from the Two-Point Seed** (:g:`A`, :g:`B`, poles :g:`F` and :g:`E`, bisector :g:`[ E F ]`, midpoint :g:`M`, and golden section points :g:`J` and :g:`I` on :g:`[ E F ]` satisfying :math:`Q(E, J)/Q(E, F) = \phi^2`). Whereas ``LeanEuclid``, ``GeoCoq``, ``mathlib4``, ``AlphaGeometry``, and ``Newclid`` omit the golden ratio altogether, GEOMETOR unfolds exact :math:`\mathbb{Q}(\phi, \sqrt{3})` harmonics in five elementary compass steps from ``(A, B)``.

The Seven Layers of GEOMETOR (33 Repositories)
----------------------------------------------

Layer 0 — Noetic & Epistemological Grounding (6 Repos)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Establishes what a geometric object is, how universal necessity is intuited in the concrete constructed diagram (*abstractio formalis intuitiva*), and how axiom groups factor independently:

* **aristotle** — Synchronized Bekker Greek and Oxford English Book Codex of *Posterior Analytics*, *Physics*, *Metaphysics* (:math:`\Theta.9` diagram actualization), and *De Anima*.
* **proclus** — Multi-track Book Codex and Friedlein concordance of Proclus's *Commentary on Book I*, codifying the 6-part proposition anatomy (*protasis* :math:`\to` *symperasma*) mirrored in ``LeanEuclid``, ``defs.txt``, and ``@proposition``.
* **aquinas** — Bilingual Latin/English Book Codex on *materia intelligibilis* and *resolutio ad phantasmata*.
* **hoenen** — Bilingual Book Codex of *De Noetica Geometriae* (:cite:`Hoenen1954`), grounding diagrammatic necessity in ``System E`` and ``geometor.model`` selectors.
* **hilbert** — Bilingual German/English Book Codex of *Grundlagen der Geometrie* (:cite:`Hilbert1899`), linked directly to ``GeoCoq``'s ``hilbert_axioms.v <-> tarski_axioms.v`` equivalence proofs.
* **bertrand-russell** — Scholarly Book Codex of *Foundations of Geometry* (1897) and *Principles of Mathematics* Part VI (1903), connecting relational space to ``mathlib4`` torsors and ``CindyJS`` Cayley–Klein polarity.

Layer 1 — Primary Classical & Constructive Scriptorium (8 Repos)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Folio-verified multi-track Book Codices (``:layout: book``) with calibrated ``.euclid-graphic`` SVGs and strict content/code separation (zero embedded Python scripts):

* **euclid** — Folio-verified 3-volume Heath Edition of Euclid's *Elements* (Books I–XIII, 831 calibrated SVGs).
* **byrne** — Visual-symbolic Book Codex of :person:`Oliver Byrne <byrne>`'s 1847 *Coloured Euclid* (Books I–VI), pairing four-color pointer-free glyph pseudocode with interactive SVG illumination.
* **archimedes** — Scholarly Book Codex of Heath's *Works of Archimedes* (exhaustion, spirals, *The Method*).
* **apollonius** — Scholarly Book Codex of Heath's *Treatise on Conic Sections* (symptomata, conjugate diameters, pole–polar).
* **pacioli** — Multi-track Italian/English/German facsimile codex of *De Divina Proportione* (1509) with Leonardo's polyhedral plates.
* **kepler** — Scholarly Book Codex of *Harmonices Mundi* (Books I–II & V) on constructible polygons, star tilings, and :math:`\mathbb{Q}(\phi)`.
* **lemoine** — Bilingual French/English Book Codex of *La Géométrographie* (:cite:`Lemoine1902`), supplying operational ruler-and-compass complexity (:math:`R_1, R_2, C_1, C_2, C_3`).
* **altshiller-court** — Two-track Book Codex of *College Geometry* (1952), anchoring Domain 4 (circle power, coaxial pencils, inversion, poles/polars).

Layer 2 — Comparative Formal Languages & Symbolic Meta-Study (1 Repo)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **codes** (*this repository*) — Source-level audit of 11 formal, visual, and symbolic geometry architectures, 60-symbol syntax decoder, 69-topic Opus coverage matrix, and 7 Rosetta Stone benchmarks.

Layer 3 — Exact Symbolic Kernel & Visual Workbench (3 Repos)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **model** — Core 100% exact SymPy geometric kernel: ``Model(..., auto_intersect=False)``, closed-form radical-axis intersections, ``ANP`` algebraic fields, topological selectors, Rational Trigonometry invariants, and ``@proposition`` proofs.
* **explorer** — Interactive web-based SVG visualization workbench and theme-adaptive ``.euclid-graphic`` renderer.
* **trees** — Constructive dependency DAG and proof-hypergraph analysis.

Layer 4 — Canonical Constructive & Algebraic Standard Libraries (6 Repos)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **elements** — Executable dependency DAG, ``.. signature::`` / ``.. step::`` pseudocode, and exact constructions evolving into Function-First *Principles of Geometry*.
* **fundamentals** — Elementary compass-and-straightedge unfolding from the two-point seed ``(A, B)``.
* **wildberger** — Rational Trigonometry (*Divine Proportions*) formalized via exact polynomial :term:`quadrance` :math:`Q`, :term:`spread` :math:`s`, and Chromogeometry.
* **etc** — Semantic index and symbolic constructor (`CenterSymbolicRegistry`) for Kimberling's *Encyclopedia of Triangle Centers* (`X(1)`–`X(53144)`).
* **pappus** — Projective geometry library: Pappus Book VII, Desargues, Steiner, harmonic conjugates, cross-ratios, :math:`\mathbb{Q}(\phi)` projectivity, and Pascal's *Hexagrammum Mysticum*.
* **divine** — Automated discovery engine scanning symbolic models for golden sections (:math:`\phi`), harmonic ranges, and algebraic proportion chains.

Layer 5 — Natural Morphology, Cosmogony & Machine Reasoning (6 Repos)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **phyllotaxis** — Golden-angle divergence, parastichy lattices, and Fibonacci planar packing.
* **thompson** — Scholarly Book Codex of D'Arcy Thompson's *On Growth and Form* (1917) on conformal and projective grid transformations.
* **walter-russell** — Digital Book Codex of Walter and Lao Russell's *Home Study Course* with parametric 2D plates and 3D wave-field models.
* **seer**, **seer_navigator**, **seer_sessions** — Multi-agent neuro-symbolic Python program-synthesis engine, Textual TUI inspector, and 8,500-trial empirical archive.

Layer 6 — Portal & Platform Infrastructure (3 Repos)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **geometor.com**, **.config**, **.github** — Unified cross-corpus portal, canonical engineering standards (`STANDARDS.md`), agent skills (`geometor-construct`), and Python 3.13 CI/CD workflows.

Eleven Actionable Engineering Blueprints Flowing from ``codes``
---------------------------------------------------------------

Every external system audited in ``codes`` contributes a specific, high-leverage upgrade to GEOMETOR:

1. **Constructive BFMSS Root-Separation Bounds in ``geometor.model.algebra.zero_test``** (*Priority 1 — inspired by GeoCoq, Mathlib4, CindyJS*):
   Currently, ``algebra.zero_test`` (`lines 247-251`) falls back to ``abs(expr.evalf(80)) < 1e-65`` when ``count_ops(expr) > 25`` to avoid exponential ``primitive_element`` blowup. Replacing that heuristic threshold with constructive **Burnikel–Fleischer–Mehlhorn–Schirra (BFMSS)** algebraic degree/mahler-measure separation bounds turns ``evalf(N)`` into a **100% mathematically sound zero certificate** at arbitrary DAG depth.
2. **Persist Selector ASTs on ``Step`` & Emit ``LeanEuclid`` System E Proofs** (*Priority 2 — inspired by LeanEuclid*):
   Because ``geometor.model.intersect``'s five selectors (`side_of`, `between`, `beyond`, `on_ray`, `other_than`) map 1-to-1 onto ``LeanEuclid/SystemE/Theory/Constructions/Intersections.lean``, storing the structured selector tuple on ``Step.primitive`` enables a direct ``to_leaneuclid(model)`` transpiler.
3. **Lemoine Géométrographie Complexity Telemetry (:math:`R_1, R_2, C_1, C_2, C_3`)** (*Priority 3 — inspired by Lemoine & AlphaGeometry*):
   Zero surveyed external systems track :person:`Émile Lemoine <lemoine>`'s operational ruler-and-compass cost. Instrumenting ``Model.construct_line`` (:math:`2 R_1 + R_2`) and ``Model.construct_circle`` (:math:`C_1 + C_2 + C_3` or :math:`2 C_1 + C_3`) computes **Simplicity** :math:`S` and **Exactitude** :math:`E` automatically on every ``Model``.
4. **First-Class Circle Power, Radical Axis, Inversion & Pole–Polar Module** (*Priority 4 — inspired by Mathlib4, 2D CGA, CindyJS, JGEX*):
   Fills ``sympy.geometry``'s and ``GeoCoq``'s largest classical gap via ``geometor.model.inversion``: exact polynomial ``circle_power``, ``radical_axis`` (working seamlessly on disjoint circles!), ``invert_point``, ``invert_line_or_circle``, and ``polar_line``.
5. **Exact :math:`3 \times 3` Symmetric Conic Matrices & Plücker 5-Point Pencils in ``geometor.pappus``** (*Priority 5 — inspired by CindyJS & Apollonius*):
   Shatters ``sympy.geometry``'s axis-aligned ``Ellipse`` limitation (and missing ``Hyperbola``) by representing general conics over SymPy rings as :math:`3 \times 3` symmetric matrices :math:`C` with division-free adjugate duals :math:`C^\Delta = \operatorname{adj}(C)`, polar :math:`\ell = C p`, pole :math:`p = C^\Delta \ell`, and ``ConicBy5`` Plücker pencils.
6. **Complete Coordinate-Free Area-Method Eliminator in ``geometor.wildberger``** (*Priority 6 — inspired by JGEX*):
   Finishes what ``JGEX`` left disabled in ``Area.java`` (`PanelProve.java:112-116`): backward point elimination over ``signed_area2`` (:math:`S_{ABC}`) and ``pythagoras_diff`` (:math:`P_{ABC}`) producing short, human-readable algebraic proofs with automatic non-degeneracy conditions (`NDGs`).
7. **Function-First *Principles of Geometry* (`elements` 2.0) & Cross-System Concordance** (*Priority 7 — inspired by Mathlib4 & AlphaGeometry*):
   Retires opaque ``G.1``–``G.601`` serial numbers in favor of ``snake_case`` construction functions (``equidistant_poles``, ``perpendicular_bisector``, ``parallel_line``), ``mathlib4``-style ``conclusion_of_hypothesis`` theorem names, ``@earns`` tags, ``defs.txt`` 68-clause completeness, and ``concordance={...}`` links.
8. **100% Exact Symbolic ``DD + Quadrance/Spread AR`` Closure Engine for ``seer``** (*Priority 8 — inspired by AlphaGeometry & Newclid*):
   Replaces ``AlphaGeometry``'s buggy ``rconst`` log-table and float64 guards with an exact symbolic Horn-clause + sparse rational Gaussian ``AR`` engine over ``geometor.model`` quadrances, spreads, and signed areas.
9. **Arbitrary-Precision ``mpmath.pslq`` Minimal-Polynomial Conjecture Scout in ``divine``** (*Priority 9 — inspired by CindyJS `PSLQ.js`*):
   Extends ``CindyJS``'s quadratic (`n=3`) float ``guess(x)`` to arbitrary algebraic degree :math:`d` using 100-digit ``mpmath.pslq``, immediately certifying candidate golden/cyclotomic relations in ``QQ.algebraic_field``.
10. **Upstream ``sympy.geometry`` Bug-Fix Pull Requests** (*Priority 10 — audited in `sympy 1.14.0`*):
    Fixes the live missing-parentheses + wrong-vertex bug in ``Triangle.excenters`` (`polygon.py:2714-2726`) and the 2-digit float collinearity bug in ``Point.affine_rank`` (`point.py:331-335`).
11. **Dual Symbolic-Chromatic ``:g:`` Micro-Glyph Mode in ``photon-platform/publish``** (*Priority 11 — inspired by Byrne 1847 & Rougeux 2018*):
    Optionally renders inline 14px SVG stroke/wedge/polygon badges beside ``:g:`` tokens, uniting classical symbolic identifier precision with :person:`Oliver Byrne <byrne>`'s zero-dereference visual pseudocode.
