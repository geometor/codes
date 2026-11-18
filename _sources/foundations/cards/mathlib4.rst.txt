.. role:: raw-html(raw)
   :format: html

.. _card-mathlib4:

mathlib4 Euclidean geometry
===========================

:raw-html:`<span class="codes-status" style="background:#c5b3e6">L5 Foundational</span>` · **Archetype:** ``analytic-formal`` · `upstream <https://github.com/leanprover-community/mathlib4>`__ · :doc:`dossier </systems/mathlib4>`

.. epigraph::

   Believe it because geometry is defined from real inner-product spaces and every theorem is a kernel-checked consequence of Lean's logic alone.

Trust chain
-----------

.. graphviz::
   :align: center
   :alt: mathlib4 trust chain

   digraph chain_mathlib4 {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, nodesep=0.15, ranksep=0.25];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     ontology [label=<<b>Ontology</b><br/><font point-size="9">Real inner-product space<br/>V acting on a metric<br/>space P<br/>(NormedAddTorsor);<br/>AffineSubspace, …</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language [label=<<b>Language</b><br/><font point-size="9">Lean 4 propositions over<br/>P: dist p₁ p₂ = dist p₁<br/>p₃ → ∠ p₁ p₂ p₃ = ∠ p₁<br/>p₃ p₂.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     ontology -> language;
     assumptions [label=<<b>Assumptions</b><br/><font point-size="9">None geometric: only<br/>Lean's logical axioms<br/>(propext, choice,<br/>Quot.sound); ℝ is<br/>constructed.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language -> assumptions;
     engine [label=<<b>Engine</b><br/><font point-size="9">Tactics (simp, linarith,<br/>nlinarith, field_simp,<br/>linear_combination)<br/>producing kernel terms.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     assumptions -> engine;
     certificate [label=<<b>Certificate</b><br/><font point-size="9">Lean proof term.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     engine -> certificate;
     checker [label=<<b>Checker</b><br/><font point-size="9">Lean 4 kernel only.</font>>, fillcolor="#c5b3e6", penwidth=2.2, width=1.4];
     certificate -> checker;
     semantics [label=<<b>Semantics</b><br/><font point-size="9">By construction: any<br/>real inner-product<br/>affine space, including<br/>ℝⁿ.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     checker -> semantics;
   }

.. list-table::
   :widths: 18 82

   * - **Ontology**
     - Real inner-product space V acting on a metric space P (NormedAddTorsor); AffineSubspace, Sphere, Affine.Simplex.  *(What exists?)*
   * - **Language**
     - Lean 4 propositions over P: dist p₁ p₂ = dist p₁ p₃ → ∠ p₁ p₂ p₃ = ∠ p₁ p₃ p₂.  *(How is a statement written?)*
   * - **Assumptions**
     - None geometric: only Lean's logical axioms (propext, choice, Quot.sound); ℝ is constructed.  *(What is taken as given?)*
   * - **Engine**
     - Tactics (simp, linarith, nlinarith, field\_simp, linear\_combination) producing kernel terms.  *(How are new truths derived?)*
   * - **Certificate**
     - Lean proof term.  *(What evidence is left behind?)*
   * - **Checker**
     - Lean 4 kernel only.  *(What must be trusted?)*
   * - **Semantics**
     - By construction: any real inner-product affine space, including ℝⁿ.  *(What model makes it sound?)*

At a glance
-----------

:Logic / calculus: Dependent type theory
:Exact vs numeric: Exact (real analysis)
:Decision procedure: Tactic search; kernel checks result
:Role of the diagram: None
:Degeneracy handling: Junk values or explicit hypotheses
:Trusted base (size): ~8k lines (kernel)
:Trusts: Lean 4 kernel (~8k lines C++ (estimate))

A statement in its own language
-------------------------------

.. code-block:: lean

   /-- **Isosceles Triangle Theorem**: Pons asinorum, angle-at-point form. -/
   theorem angle_eq_angle_of_dist_eq {p₁ p₂ p₃ : P} (h : dist p₁ p₂ = dist p₁ p₃) :
       ∠ p₁ p₂ p₃ = ∠ p₁ p₃ p₂ := by

Source: `Triangle.lean#L280-L282 <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Triangle.lean#L280-L282>`__

Findings
--------

- Zero \`axiom\`, \`sorry\`, or \`native\_decide\` in Geometry/Euclidean and LinearAlgebra/AffineSpace.
- Junk values make statements total: angle 0 x = π/2, so pons asinorum needs no distinctness hypothesis.
- Dimension-polymorphic results (Monge point, sphere power, inversion) but no radical axis, cross ratio, Menelaus, Pappus, or Desargues.

In the showcase
---------------

- :doc:`I.5 Pons asinorum </showcase/isosceles_base_angles>` — :raw-html:`<span class="codes-status" style="background:#9fd8a8">theorem</span>` ``EuclideanGeometry.angle_eq_angle_of_dist_eq``
- :doc:`I.47 Pythagorean theorem </showcase/pythagorean>` — :raw-html:`<span class="codes-status" style="background:#9fd8a8">theorem</span>` ``EuclideanGeometry.dist_sq_eq_dist_sq_add_dist_sq_iff_angle_eq_pi_div_two``
- :doc:`III.31 Angle in a semicircle </showcase/thales_semicircle>` — :raw-html:`<span class="codes-status" style="background:#9fd8a8">theorem</span>` ``EuclideanGeometry.Sphere.angle_eq_pi_div_two_iff_mem_sphere_of_isDiameter``
- :doc:`Simson line </showcase/simson_line>` — :raw-html:`<span class="codes-status" style="background:#dddddd">absent</span>` ``—``

References
----------

- `Mathlib/Geometry/Euclidean <https://github.com/leanprover-community/mathlib4/tree/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean>`__
