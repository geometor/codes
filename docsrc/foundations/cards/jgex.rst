.. role:: raw-html(raw)
   :format: html

.. _card-jgex:

Java Geometry Expert (JGEX)
===========================

:raw-html:`<span class="codes-status" style="background:#7fd1c7">L2 Generic</span>` · **Archetype:** ``algebraic-decision`` · `upstream <https://github.com/kovzol/Java-Geometry-Expert>`__ · :doc:`dossier </systems/jgex-area-method>`

.. epigraph::

   Believe it because the hypothesis polynomials reduce the conclusion to zero (Wu / Gröbner) — true generically, provided the printed non-degeneracy conditions hold.

Trust chain
-----------

.. graphviz::
   :align: center
   :alt: JGEX trust chain

   digraph chain_jgex {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, nodesep=0.15, ranksep=0.25];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     ontology [label=<<b>Ontology</b><br/><font point-size="9">Constructed points;<br/>hypotheses become<br/>polynomials with<br/>BigInteger coefficients.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language [label=<<b>Language</b><br/><font point-size="9">Text problems: POINT A B<br/>C O D … CIRCUMCENTER O A<br/>B C … SHOW: COLLINEAR P<br/>Q R.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     ontology -> language;
     assumptions [label=<<b>Assumptions</b><br/><font point-size="9">Field axioms over ℂ (Wu<br/>/ Gröbner); GDD and<br/>full-angle rule sets for<br/>readable proofs.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language -> assumptions;
     engine [label=<<b>Engine</b><br/><font point-size="9">Pseudo-division (Wu),<br/>Gröbner reduction,<br/>area-method elimination,<br/>forward chaining (GDD).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     assumptions -> engine;
     certificate [label=<<b>Certificate</b><br/><font point-size="9">Remainder-zero chain +<br/>NDG list; readable proof<br/>trees for GDD /<br/>full-angle.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     engine -> certificate;
     checker [label=<<b>Checker</b><br/><font point-size="9">JGEX Java prover (~38k<br/>lines).</font>>, fillcolor="#7fd1c7", penwidth=2.2, width=1.4];
     certificate -> checker;
     semantics [label=<<b>Semantics</b><br/><font point-size="9">Generic truth over an<br/>algebraically closed<br/>field, conditional on<br/>NDGs.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     checker -> semantics;
   }

.. list-table::
   :widths: 18 82

   * - **Ontology**
     - Constructed points; hypotheses become polynomials with BigInteger coefficients.  *(What exists?)*
   * - **Language**
     - Text problems: POINT A B C O D … CIRCUMCENTER O A B C … SHOW: COLLINEAR P Q R.  *(How is a statement written?)*
   * - **Assumptions**
     - Field axioms over ℂ (Wu / Gröbner); GDD and full-angle rule sets for readable proofs.  *(What is taken as given?)*
   * - **Engine**
     - Pseudo-division (Wu), Gröbner reduction, area-method elimination, forward chaining (GDD).  *(How are new truths derived?)*
   * - **Certificate**
     - Remainder-zero chain + NDG list; readable proof trees for GDD / full-angle.  *(What evidence is left behind?)*
   * - **Checker**
     - JGEX Java prover (~38k lines).  *(What must be trusted?)*
   * - **Semantics**
     - Generic truth over an algebraically closed field, conditional on NDGs.  *(What model makes it sound?)*

At a glance
-----------

:Logic / calculus: Polynomial ideal membership
:Exact vs numeric: Exact (BigInteger polynomials)
:Decision procedure: Yes, for equational statements (generic truth)
:Role of the diagram: Input and display only
:Degeneracy handling: Explicit NDG conditions
:Trusted base (size): ~38k lines Java
:Trusts: JGEX gprover (~38k lines Java)

A statement in its own language
-------------------------------

.. code-block:: text

   POINT A B C O D R P Q
   CIRCUMCENTER O A B C
   ON_CIRCLE D O A
   FOOT R D A B ...
   SHOW: COLLINEAR P Q R

Source: `3\_JAR <https://github.com/kovzol/Java-Geometry-Expert/tree/5489aacb40afc91b5c5ca539db853cca216e1165/src/main/resources/docs/examples/3_JAR>`__

Findings
--------

- Five methods: GDD deductive database (43 rules), full-angle (29 rules), area, Wu characteristic sets, Gröbner bases.
- Wu prints the pseudo-remainder chain ending in 'Remainder = 0' together with NDG conditions.
- Area.java is an unfinished port; its GUI tab is commented out (PanelProve.java).

In the showcase
---------------

- :doc:`I.47 Pythagorean theorem </showcase/pythagorean>` — :raw-html:`<span class="codes-status" style="background:#7fd1c7">generic</span>` ``examples/visual-proofs/pythagoras.gex``
- :doc:`Simson line </showcase/simson_line>` — :raw-html:`<span class="codes-status" style="background:#7fd1c7">generic</span>` ``examples/Showcase/simson.gex``

References
----------

- `Chou, Gao, Zhang, Machine Proofs in Geometry (1994) <https://doi.org/10.1142/2196>`__
