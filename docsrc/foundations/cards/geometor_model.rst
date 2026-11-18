.. role:: raw-html(raw)
   :format: html

.. _card-geometor_model:

geometor.model
==============

:raw-html:`<span class="codes-status" style="background:#9cc3f0">L1 Instance</span>` · **Archetype:** ``analytic-cas`` · `upstream <https://github.com/geometor/model>`__ · :doc:`dossier </systems/geometor-model>`

.. epigraph::

   Believe it because the figure is built exactly — algebraic coordinates from ruler-and-compass intersections — and every asserted relation reduces to zero.

Trust chain
-----------

.. graphviz::
   :align: center
   :alt: geometor.model trust chain

   digraph chain_geometor_model {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, nodesep=0.15, ranksep=0.25];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     ontology [label=<<b>Ontology</b><br/><font point-size="9">Exact SymPy points,<br/>lines, circles, polygons<br/>in a construction DAG;<br/>coordinates in ℚ, ℚ(√d),<br/>…</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language [label=<<b>Language</b><br/><font point-size="9">Python construction +<br/>assertions:<br/>m.assert_collinear(A, B,<br/>C, by="I.1").</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     ontology -> language;
     assumptions [label=<<b>Assumptions</b><br/><font point-size="9">Exact algebraic numbers;<br/>closed-form<br/>ruler-and-compass<br/>intersections.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language -> assumptions;
     engine [label=<<b>Engine</b><br/><font point-size="9">Exact construction +<br/>quadrance / spread /<br/>determinant identities<br/>reduced by zero_test.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     assumptions -> engine;
     certificate [label=<<b>Certificate</b><br/><font point-size="9">Step ledger of<br/>assertions (citations<br/>unchecked) and the exact<br/>figure.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     engine -> certificate;
     checker [label=<<b>Checker</b><br/><font point-size="9">zero_test (exact tiers +<br/>numeric acceptance<br/>branch) + SymPy.</font>>, fillcolor="#9cc3f0", penwidth=2.2, width=1.4];
     certificate -> checker;
     semantics [label=<<b>Semantics</b><br/><font point-size="9">One exact figure in ℝ²<br/>over real algebraic<br/>numbers.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     checker -> semantics;
   }

.. list-table::
   :widths: 18 82

   * - **Ontology**
     - Exact SymPy points, lines, circles, polygons in a construction DAG; coordinates in ℚ, ℚ(√d), ℚ(φ), radical towers.  *(What exists?)*
   * - **Language**
     - Python construction + assertions: m.assert\_collinear(A, B, C, by="I.1").  *(How is a statement written?)*
   * - **Assumptions**
     - Exact algebraic numbers; closed-form ruler-and-compass intersections.  *(What is taken as given?)*
   * - **Engine**
     - Exact construction + quadrance / spread / determinant identities reduced by zero\_test.  *(How are new truths derived?)*
   * - **Certificate**
     - Step ledger of assertions (citations unchecked) and the exact figure.  *(What evidence is left behind?)*
   * - **Checker**
     - zero\_test (exact tiers + numeric acceptance branch) + SymPy.  *(What must be trusted?)*
   * - **Semantics**
     - One exact figure in ℝ² over real algebraic numbers.  *(What model makes it sound?)*

At a glance
-----------

:Logic / calculus: Evaluation on an exact instance
:Exact vs numeric: Exact (one numeric acceptance branch)
:Decision procedure: Yes for constant algebraic expressions (minimal polynomial)
:Role of the diagram: The figure is the proof object
:Degeneracy handling: Visible in the instance
:Trusted base (size): ~3.5k lines + SymPy
:Trusts: model zero_test (~3.5k lines + SymPy) · SymPy simplification (core heuristics + mpmath)
:Catalog: 47 principles (13 shared with other systems) — :doc:`search </catalog/index>`

A statement in its own language
-------------------------------

.. code-block:: python

   m = Model("I.5", auto_intersect=False)
   A, B, C = m.set_point(2, 3), m.set_point(0, 0), m.set_point(4, 0)
   m.assert_equal((A, B), (A, C), by="Given")
   m.assert_spread_equal((A, B, C), (A, C, B), by="I.5")

Source: ``codes/src/geometor/codes/verify.py``

Findings
--------

- zero\_test is the single truth oracle for every assert\_\*; \`by=\` citations are recorded, not checked.
- zero\_test is exact on most paths (expansion, ℚ(φ)/ℚ(√φ) field arithmetic, minimal\_polynomial) but accepts \|evalf(80)\| < 1e-65 for large constant expressions (algebra.py:247-251) — a candidate for a strict mode.
- A witness certifies one figure (L1); with free symbolic coordinates the same check certifies generic truth (L2) — see the showcase generic witnesses.
- No order predicates (betweenness, same side): Pasch-type statements are out of reach.

In the showcase
---------------

- :doc:`I.5 Pons asinorum </showcase/isosceles_base_angles>` — :raw-html:`<span class="codes-status" style="background:#9cc3f0">witness</span>` ``verify._build_isosceles_base_angles``
- :doc:`I.47 Pythagorean theorem </showcase/pythagorean>` — :raw-html:`<span class="codes-status" style="background:#9cc3f0">witness</span>` ``verify._build_pythagorean``
- :doc:`III.31 Angle in a semicircle </showcase/thales_semicircle>` — :raw-html:`<span class="codes-status" style="background:#9cc3f0">witness</span>` ``verify._build_thales_semicircle``
- :doc:`Simson line </showcase/simson_line>` — :raw-html:`<span class="codes-status" style="background:#9cc3f0">witness</span>` ``verify._build_simson_line``
- :doc:`Pasch's axiom </showcase/pasch>` — :raw-html:`<span class="codes-status" style="background:#f19c9c">gap</span>` ``KNOWN_GAPS['pasch']``

References
----------

- `geometor.model <https://github.com/geometor/model>`__
- `algebra.zero\_test <https://github.com/geometor/model/blob/0dbd464e6e5660e2882febd20bb559f8ade1d10e/src/geometor/model/algebra.py#L160-L253>`__
