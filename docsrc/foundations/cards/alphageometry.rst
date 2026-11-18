.. role:: raw-html(raw)
   :format: html

.. _card-alphageometry:

AlphaGeometry
=============

:raw-html:`<span class="codes-status" style="background:#f6b26b">L3 Rule-closed</span>` · **Archetype:** ``rule-engine`` · `upstream <https://github.com/google-deepmind/alphageometry>`__ · :doc:`dossier </systems/alphageometry-newclid>`

.. epigraph::

   Believe it because a deduction engine derived it from 43 assumed rules — with side conditions (non-collinear, same side) read off a random numeric diagram.

Trust chain
-----------

.. graphviz::
   :align: center
   :alt: AlphaGeometry trust chain

   digraph chain_alphageometry {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, nodesep=0.15, ranksep=0.25];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     ontology [label=<<b>Ontology</b><br/><font point-size="9">Named points with<br/>predicates (coll, para,<br/>perp, cong, eqangle,<br/>eqratio, cyclic, midp, …</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language [label=<<b>Language</b><br/><font point-size="9">Construction clauses and<br/>a goal: a b c = triangle<br/>a b c; h = orthocenter h<br/>a b c; ? perp a h …</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     ontology -> language;
     assumptions [label=<<b>Assumptions</b><br/><font point-size="9">43 Horn rules<br/>(rules.txt) + ~71<br/>construction definitions<br/>(defs.txt).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language -> assumptions;
     engine [label=<<b>Engine</b><br/><font point-size="9">DD+AR: forward chaining<br/>to a fixpoint + Gaussian<br/>elimination over exact<br/>Fractions; LM …</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     assumptions -> engine;
     certificate [label=<<b>Certificate</b><br/><font point-size="9">Deduction trace naming<br/>the rule for each step.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     engine -> certificate;
     checker [label=<<b>Checker</b><br/><font point-size="9">Python engine + rule<br/>soundness + numeric<br/>diagram (tol 1e-12).</font>>, fillcolor="#f6b26b", penwidth=2.2, width=1.4];
     certificate -> checker;
     semantics [label=<<b>Semantics</b><br/><font point-size="9">The real Euclidean<br/>plane, sampled as one<br/>random float diagram;<br/>directed angles mod π.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     checker -> semantics;
   }

.. list-table::
   :widths: 18 82

   * - **Ontology**
     - Named points with predicates (coll, para, perp, cong, eqangle, eqratio, cyclic, midp, simtri); hidden float coordinates.  *(What exists?)*
   * - **Language**
     - Construction clauses and a goal: a b c = triangle a b c; h = orthocenter h a b c; ? perp a h b c.  *(How is a statement written?)*
   * - **Assumptions**
     - 43 Horn rules (rules.txt) + ~71 construction definitions (defs.txt).  *(What is taken as given?)*
   * - **Engine**
     - DD+AR: forward chaining to a fixpoint + Gaussian elimination over exact Fractions; LM proposes auxiliaries.  *(How are new truths derived?)*
   * - **Certificate**
     - Deduction trace naming the rule for each step.  *(What evidence is left behind?)*
   * - **Checker**
     - Python engine + rule soundness + numeric diagram (tol 1e-12).  *(What must be trusted?)*
   * - **Semantics**
     - The real Euclidean plane, sampled as one random float diagram; directed angles mod π.  *(What model makes it sound?)*

At a glance
-----------

:Logic / calculus: Horn-clause forward chaining
:Exact vs numeric: Exact algebra; numeric side conditions
:Decision procedure: Saturation over a finite rule set
:Role of the diagram: Essential: decides side conditions
:Degeneracy handling: Numeric filters; no NDG output
:Trusted base (size): ~9.7k lines Python
:Trusts: AG DD+AR engine (~9.7k lines Python) · Numeric diagram (tol 1e-12 (AG) · rel 1e-3 (Newclid))
:Catalog: 108 principles (50 shared with other systems) — :doc:`search </catalog/index>`

A statement in its own language
-------------------------------

.. code-block:: text

   cong O A O B, ncoll O A B => eqangle O A A B A B O B

Source: `rules.txt <https://github.com/google-deepmind/alphageometry/blob/6777cb586cbb46beed28db12dc72c69770b68337/rules.txt>`__

Findings
--------

- ncoll, npara, nperp, and sameside premises are decided numerically (dd.py:864-892), not deduced.
- build\_problem resamples the diagram until the goal holds numerically (graph.py:500-523).
- The AR algebra is linear over angle/ratio/distance tables, so a² + b² = c² is not expressible.
- The language model only proposes auxiliary points; it is outside the trusted core.

In the showcase
---------------

- :doc:`I.5 Pons asinorum </showcase/isosceles_base_angles>` — :raw-html:`<span class="codes-status" style="background:#f6b26b">rule</span>` ``rules.txt r13``
- :doc:`I.47 Pythagorean theorem </showcase/pythagorean>` — :raw-html:`<span class="codes-status" style="background:#f19c9c">gap</span>` ``—``
- :doc:`III.31 Angle in a semicircle </showcase/thales_semicircle>` — :raw-html:`<span class="codes-status" style="background:#f6b26b">rule</span>` ``rules.txt r20``
- :doc:`Pasch's axiom </showcase/pasch>` — :raw-html:`<span class="codes-status" style="background:#f19c9c">gap</span>` ``—``

References
----------

- `Trinh et al., Solving olympiad geometry without human demonstrations (Nature 2024) <https://doi.org/10.1038/s41586-023-06747-5>`__
