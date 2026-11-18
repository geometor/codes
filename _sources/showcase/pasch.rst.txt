.. role:: raw-html(raw)
   :format: html

.. _showcase-pasch:

Pasch's axiom
=============

.. admonition:: Statement
   :class: note

   A line entering a triangle through one side, and missing the vertices, leaves through another side.

**Why this theorem:** The foundations themselves disagree. Euclid uses it silently, System E and Tarski assume it, a rule engine sees order only numerically, and exact algebra over a field cannot express it at all.

.. graphviz::
   :align: center
   :alt: Pasch's axiom realizations

   digraph showcase_pasch {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, ranksep=0.8];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     thm [label="Pasch's axiom", shape=ellipse, style=filled, fillcolor="#ffffff", penwidth=1.6];
     r0 [label=<<b>Euclid</b><br/><font point-size="9">—<br/><i>gap</i></font>>, fillcolor="#f19c9c", URL="../foundations/cards/euclid.html", target="_top", tooltip="Used tacitly via the diagram; not among Euclid's postulates. Pasch made it explicit in 1882."];
     thm -> r0 [style=dashed];
     r1 [label=<<b>LeanEuclid</b><br/><font point-size="9">pasch_1<br/><i>axiom</i></font>>, fillcolor="#f4d58d", URL="../foundations/cards/leaneuclid.html", target="_top", tooltip="One of System E's 36 diagrammatic inference axioms."];
     thm -> r1 [style=solid];
     r2 [label=<<b>GeoCoq</b><br/><font point-size="9">Tarski_neutral_dimensionless.in…<br/><i>axiom</i></font>>, fillcolor="#f4d58d", URL="../foundations/cards/geocoq.html", target="_top", tooltip="A field of the Tarski axiom class (inner form of Pasch)."];
     thm -> r2 [style=solid];
     r3 [label=<<b>AlphaGeometry</b><br/><font point-size="9">—<br/><i>gap</i></font>>, fillcolor="#f19c9c", URL="../foundations/cards/alphageometry.html", target="_top", tooltip="No order predicates in the rule language; side and betweenness facts come only from the numeric diagram."];
     thm -> r3 [style=dashed];
     r4 [label=<<b>geometor.model</b><br/><font point-size="9">KNOWN_GAPS['pasch']<br/><i>gap</i></font>>, fillcolor="#f19c9c", URL="../foundations/cards/geometor_model.html", target="_top", tooltip="No betweenness or half-plane predicate. Order needs an ordered field, which polynomial identities cannot express."];
     thm -> r4 [style=dashed];
   }

Realizations
------------

.. container:: codes-tabs

   .. container:: codes-tab status-gap

      .. rubric:: Euclid

      :raw-html:`<span class="codes-status" style="background:#f19c9c">gap</span>` — :doc:`Euclid card </foundations/cards/euclid>`

      Used tacitly via the diagram; not among Euclid's postulates. Pasch made it explicit in 1882.

   .. container:: codes-tab status-axiom

      .. rubric:: LeanEuclid

      :raw-html:`<span class="codes-status" style="background:#f4d58d">axiom</span>` ``pasch_1`` — :doc:`LeanEuclid card </foundations/cards/leaneuclid>`

      .. code-block:: lean

         axiom pasch_1: ∀ (a b c : Point) (L : Line),
           (between a b c) ∧ (a.sameSide c L) → a.sameSide b L

      One of System E's 36 diagrammatic inference axioms.

      Source: `Diagrammatic.lean#L145-L146 <https://github.com/loganrjmurphy/LeanEuclid/blob/33a72c0fa83914202532998a2e7b8771295c3cc7/SystemE/Theory/Inferences/Diagrammatic.lean#L145-L146>`__

   .. container:: codes-tab status-axiom

      .. rubric:: GeoCoq

      :raw-html:`<span class="codes-status" style="background:#f4d58d">axiom</span>` ``Tarski_neutral_dimensionless.inner_pasch`` — :doc:`GeoCoq card </foundations/cards/geocoq>`

      .. code-block:: coq

         inner_pasch : forall A B C P Q,
            Bet A P C -> Bet B Q C ->
            exists X, Bet P X B /\ Bet Q X A;

      A field of the Tarski axiom class (inner form of Pasch).

      Source: `tarski\_axioms.v#L29-L31 <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Axioms/tarski_axioms.v#L29-L31>`__

   .. container:: codes-tab status-gap

      .. rubric:: AlphaGeometry

      :raw-html:`<span class="codes-status" style="background:#f19c9c">gap</span>` — :doc:`AlphaGeometry card </foundations/cards/alphageometry>`

      No order predicates in the rule language; side and betweenness facts come only from the numeric diagram.

   .. container:: codes-tab status-gap

      .. rubric:: geometor.model

      :raw-html:`<span class="codes-status" style="background:#f19c9c">gap</span>` ``KNOWN_GAPS['pasch']`` — :doc:`geometor.model card </foundations/cards/geometor_model>`

      No betweenness or half-plane predicate. Order needs an ordered field, which polynomial identities cannot express.

Climbing the ladder in GEOMETOR
-------------------------------

.. admonition:: No generic lift
   :class: warning

   Pasch is an order statement (betweenness / same side). Polynomial identities over a field cannot express order; certifying it needs an ordered (real closed) field and inequalities, i.e. a different foundation from Wu / Groebner methods.
