.. role:: raw-html(raw)
   :format: html

.. _card-geocoq:

GeoCoq
======

:raw-html:`<span class="codes-status" style="background:#9fd8a8">L4 Axiom-checked</span>` · **Archetype:** ``synthetic-formal`` · `upstream <https://github.com/GeoCoq/GeoCoq>`__ · :doc:`dossier </systems/geocoq>`

.. epigraph::

   Believe it because the Coq kernel checked it from Tarski's (or Hilbert's, or Euclid's) axioms — and GeoCoq proves those axiom systems interpret one another and hold in ℝ².

Trust chain
-----------

.. graphviz::
   :align: center
   :alt: GeoCoq trust chain

   digraph chain_geocoq {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, nodesep=0.15, ranksep=0.25];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     ontology [label=<<b>Ontology</b><br/><font point-size="9">Tarski: one sort of<br/>points with Bet (3-ary)<br/>and Cong (4-ary);<br/>Hilbert: points, lines,<br/>planes …</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language [label=<<b>Language</b><br/><font point-size="9">Coq propositions inside<br/>an axiom-class context:<br/>forall A B C, isosceles<br/>A B C -&gt; CongA A B C<br/>…</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     ontology -> language;
     assumptions [label=<<b>Assumptions</b><br/><font point-size="9">Axiom classes: Tarski<br/>neutral (8) + dimension<br/>+ Euclid + continuity<br/>options; Hilbert …</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language -> assumptions;
     engine [label=<<b>Engine</b><br/><font point-size="9">Ltac proofs; reflective<br/>deciders ColR / CongR<br/>(vm_compute); nsatz<br/>(Gröbner) in coordinate<br/>…</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     assumptions -> engine;
     certificate [label=<<b>Certificate</b><br/><font point-size="9">Coq proof term (.vo).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     engine -> certificate;
     checker [label=<<b>Checker</b><br/><font point-size="9">Coq kernel (+ VM<br/>conversion for<br/>reflective steps).</font>>, fillcolor="#9fd8a8", penwidth=2.2, width=1.4];
     certificate -> checker;
     semantics [label=<<b>Semantics</b><br/><font point-size="9">Formal models: Tarski ⇐<br/>ℝⁿ over any real closed<br/>field; independence<br/>counter-models.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     checker -> semantics;
   }

.. list-table::
   :widths: 18 82

   * - **Ontology**
     - Tarski: one sort of points with Bet (3-ary) and Cong (4-ary); Hilbert: points, lines, planes with incidence, order, congruence.  *(What exists?)*
   * - **Language**
     - Coq propositions inside an axiom-class context: forall A B C, isosceles A B C -> CongA A B C A C B.  *(How is a statement written?)*
   * - **Assumptions**
     - Axiom classes: Tarski neutral (8) + dimension + Euclid + continuity options; Hilbert classes; Beeson's Euclid axioms.  *(What is taken as given?)*
   * - **Engine**
     - Ltac proofs; reflective deciders ColR / CongR (vm\_compute); nsatz (Gröbner) in coordinate chapters.  *(How are new truths derived?)*
   * - **Certificate**
     - Coq proof term (.vo).  *(What evidence is left behind?)*
   * - **Checker**
     - Coq kernel (+ VM conversion for reflective steps).  *(What must be trusted?)*
   * - **Semantics**
     - Formal models: Tarski ⇐ ℝⁿ over any real closed field; independence counter-models.  *(What model makes it sound?)*

At a glance
-----------

:Logic / calculus: Calculus of Inductive Constructions
:Exact vs numeric: Exact (synthetic)
:Decision procedure: Reflective Col/Cong deciders; nsatz
:Role of the diagram: None (diagram facts are proved)
:Degeneracy handling: Explicit (~Col, A <> B); degenerate-tolerant Bet
:Trusted base (size): ~10-30k lines (kernel)
:Trusts: Coq kernel (~10-30k lines OCaml (estimate))

A statement in its own language
-------------------------------

.. code-block:: coq

   Lemma proposition_05 :
      forall A B C,
      isosceles A B C ->
      CongA A B C A C B.

Source: `proposition\_05.v#L8-L11 <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Elements/OriginalProofs/proposition_05.v#L8-L11>`__

Findings
--------

- No Coq \`Axiom\`, \`Parameter\`, or \`Admitted\` in theories/: axiom systems are type-class fields, so every theorem is relative to its class.
- Mutual interpretation Tarski ⇔ Hilbert ⇔ Euclid (Beeson axioms); Book I proofs in Elements/OriginalProofs.
- 35 parallel-postulate variants proved equivalent in the Euclidean context; Thales' theorem is one of them.
- Models: Tarski's axioms hold in coordinate spaces over any real closed field (Algebraic/POF\_to\_Tarski.v).

In the showcase
---------------

- :doc:`I.5 Pons asinorum </showcase/isosceles_base_angles>` — :raw-html:`<span class="codes-status" style="background:#9fd8a8">theorem</span>` ``proposition_05``
- :doc:`I.47 Pythagorean theorem </showcase/pythagorean>` — :raw-html:`<span class="codes-status" style="background:#9fd8a8">theorem</span>` ``proposition_47``
- :doc:`III.31 Angle in a semicircle </showcase/thales_semicircle>` — :raw-html:`<span class="codes-status" style="background:#f4d58d">axiom</span>` ``thales_postulate``
- :doc:`Pasch's axiom </showcase/pasch>` — :raw-html:`<span class="codes-status" style="background:#f4d58d">axiom</span>` ``Tarski_neutral_dimensionless.inner_pasch``

References
----------

- `Boutry, Gries, Narboux et al., GeoCoq <https://geocoq.github.io/GeoCoq/>`__
- `tarski\_axioms.v <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Axioms/tarski_axioms.v>`__
