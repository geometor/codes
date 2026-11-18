.. role:: raw-html(raw)
   :format: html

.. _card-leaneuclid:

LeanEuclid (System E in Lean 4)
===============================

:raw-html:`<span class="codes-status" style="background:#f6b26b">L3 Rule-closed</span>` · **Archetype:** ``synthetic-formal`` · `upstream <https://github.com/loganrjmurphy/LeanEuclid>`__ · :doc:`dossier </systems/leaneuclid>`

.. epigraph::

   Believe it because Lean's kernel checked every rule application from System E's axioms — except that premise-discharging steps are admitted by an SMT oracle axiom.

Trust chain
-----------

.. graphviz::
   :align: center
   :alt: LeanEuclid trust chain

   digraph chain_leaneuclid {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, nodesep=0.15, ranksep=0.25];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     ontology [label=<<b>Ontology</b><br/><font point-size="9">Axiomatized sorts Point,<br/>Line, Circle (+ Segment,<br/>Angle, Triangle); opaque<br/>relations onLine, …</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language [label=<<b>Language</b><br/><font point-size="9">Lean 4 propositions in<br/>System E syntax: ∀ a b c<br/>: Point, formTriangle …<br/>→ ∠ a:b:c = ∠ a:c:b.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     ontology -> language;
     assumptions [label=<<b>Assumptions</b><br/><font point-size="9">System E as 101 Lean<br/>axiom declarations<br/>(construction,<br/>diagrammatic, metric,<br/>transfer, …</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language -> assumptions;
     engine [label=<<b>Engine</b><br/><font point-size="9">euclid_apply<br/>(kernel-checked rule<br/>instance) with premises<br/>closed by euclid_finish<br/>→ z3/cvc5.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     assumptions -> engine;
     certificate [label=<<b>Certificate</b><br/><font point-size="9">Lean proof term with<br/>opaque SMT_VERIF leaves.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     engine -> certificate;
     checker [label=<<b>Checker</b><br/><font point-size="9">Lean 4 kernel +<br/>SMT_VERIF oracle<br/>(solver, translator,<br/>hand-written theory).</font>>, fillcolor="#f6b26b", penwidth=2.2, width=1.4];
     certificate -> checker;
     semantics [label=<<b>Semantics</b><br/><font point-size="9">Avigad–Dean–Mumma: E is<br/>sound and complete for<br/>ruler-and-compass<br/>Euclidean planes (not …</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     checker -> semantics;
   }

.. list-table::
   :widths: 18 82

   * - **Ontology**
     - Axiomatized sorts Point, Line, Circle (+ Segment, Angle, Triangle); opaque relations onLine, sameSide, between, onCircle; magnitudes in ℝ.  *(What exists?)*
   * - **Language**
     - Lean 4 propositions in System E syntax: ∀ a b c : Point, formTriangle … → ∠ a:b:c = ∠ a:c:b.  *(How is a statement written?)*
   * - **Assumptions**
     - System E as 101 Lean axiom declarations (construction, diagrammatic, metric, transfer, superposition) + hand-written SMT theory.  *(What is taken as given?)*
   * - **Engine**
     - euclid\_apply (kernel-checked rule instance) with premises closed by euclid\_finish → z3/cvc5.  *(How are new truths derived?)*
   * - **Certificate**
     - Lean proof term with opaque SMT\_VERIF leaves.  *(What evidence is left behind?)*
   * - **Checker**
     - Lean 4 kernel + SMT\_VERIF oracle (solver, translator, hand-written theory).  *(What must be trusted?)*
   * - **Semantics**
     - Avigad–Dean–Mumma: E is sound and complete for ruler-and-compass Euclidean planes (not formalized in LeanEuclid).  *(What model makes it sound?)*

At a glance
-----------

:Logic / calculus: Dependent type theory + axioms
:Exact vs numeric: Exact (symbolic)
:Decision procedure: SMT on the diagrammatic fragment (oracle)
:Role of the diagram: Formalized: 36 diagrammatic + 23 transfer axioms
:Degeneracy handling: Explicit hypotheses (formTriangle, a ≠ b)
:Trusted base (size): Lean kernel + SMT stack (unbounded)
:Trusts: Lean 4 kernel (~8k lines C++ (estimate)) · SMT_VERIF oracle (z3/cvc5 + hand-written E theory)
:Catalog: 256 principles (65 shared with other systems) — :doc:`search </catalog/index>`

A statement in its own language
-------------------------------

.. code-block:: lean

   theorem proposition_5 : ∀ (a b c d e : Point) (AB BC AC : Line),
     formTriangle a b c AB BC AC ∧ (|(a─b)| = |(a─c)|) ∧
     (between a b d) ∧ (between a c e) →
     (∠ a:b:c = ∠ a:c:b) ∧ (∠ c:b:d = ∠ b:c:e) :=

Source: `Prop05.lean#L7-L10 <https://github.com/loganrjmurphy/LeanEuclid/blob/33a72c0fa83914202532998a2e7b8771295c3cc7/Book/Prop05.lean#L7-L10>`__

Findings
--------

- euclid\_finish closes goals with \`axiom SMT\_VERIF (P : Prop) : P\` (SystemE/Meta/Smt/Solver.lean:44-54) — inconsistent as a Lean axiom; solver timeouts fall back to \`sorry\`.
- The SMT background theory (Meta/Smt/EuclidTheory.lean, ~111 asserts) is hand-written, not derived from the Lean axioms.
- 104 \`axiom\` declarations under SystemE/Theory: 3 sorts + 101 rules (36 diagrammatic, 23 transfer, 21+7+2 construction, 11 metric, 1 superposition).
- Book/Prop47.lean isolates orientation lemmas Euclid's Bride's Chair leaves implicit.

In the showcase
---------------

- :doc:`I.5 Pons asinorum </showcase/isosceles_base_angles>` — :raw-html:`<span class="codes-status" style="background:#9fd8a8">theorem</span>` ``proposition_5``
- :doc:`I.47 Pythagorean theorem </showcase/pythagorean>` — :raw-html:`<span class="codes-status" style="background:#9fd8a8">theorem</span>` ``proposition_47``
- :doc:`III.31 Angle in a semicircle </showcase/thales_semicircle>` — :raw-html:`<span class="codes-status" style="background:#dddddd">absent</span>` ``—``
- :doc:`Pasch's axiom </showcase/pasch>` — :raw-html:`<span class="codes-status" style="background:#f4d58d">axiom</span>` ``pasch_1``

References
----------

- `Murphy et al., Autoformalizing Euclidean Geometry (ICML 2024) <https://arxiv.org/abs/2405.17216>`__
- `Avigad, Dean, Mumma, A formal system for Euclid's Elements (RSL 2009) <https://doi.org/10.1017/S1755020309990098>`__
- `Solver.lean SMT\_VERIF <https://github.com/loganrjmurphy/LeanEuclid/blob/33a72c0fa83914202532998a2e7b8771295c3cc7/SystemE/Meta/Smt/Solver.lean#L44-L54>`__
