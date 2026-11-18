.. role:: raw-html(raw)
   :format: html

.. _card-euclid:

Euclid, Elements (Heath)
========================

:raw-html:`<span class="codes-status" style="background:#e8d9b5">H Human</span>` · **Archetype:** ``synthetic-human`` · `upstream <https://geometor.github.io/euclid>`__

.. epigraph::

   Believe it because it follows, step by step, from five postulates and five common notions — as checked by readers, with the diagram doing silent work.

Trust chain
-----------

.. graphviz::
   :align: center
   :alt: Euclid trust chain

   digraph chain_euclid {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, nodesep=0.15, ranksep=0.25];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     ontology [label=<<b>Ontology</b><br/><font point-size="9">Points, straight lines,<br/>circles, angles, and<br/>plane figures.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language [label=<<b>Language</b><br/><font point-size="9">Greek prose<br/>enunciations: protasis,<br/>ekthesis, diorismos,<br/>construction, proof,<br/>conclusion.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     ontology -> language;
     assumptions [label=<<b>Assumptions</b><br/><font point-size="9">5 postulates, 5 common<br/>notions, 23 definitions<br/>(Book I).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language -> assumptions;
     engine [label=<<b>Engine</b><br/><font point-size="9">Human deduction citing<br/>earlier propositions;<br/>constructions by ruler<br/>and compass.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     assumptions -> engine;
     certificate [label=<<b>Certificate</b><br/><font point-size="9">The written proof.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     engine -> certificate;
     checker [label=<<b>Checker</b><br/><font point-size="9">The reader.</font>>, fillcolor="#e8d9b5", penwidth=2.2, width=1.4];
     certificate -> checker;
     semantics [label=<<b>Semantics</b><br/><font point-size="9">Intended: the physical<br/>plane; modern reading: a<br/>Euclidean plane over a<br/>Euclidean field …</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     checker -> semantics;
   }

.. list-table::
   :widths: 18 82

   * - **Ontology**
     - Points, straight lines, circles, angles, and plane figures.  *(What exists?)*
   * - **Language**
     - Greek prose enunciations: protasis, ekthesis, diorismos, construction, proof, conclusion.  *(How is a statement written?)*
   * - **Assumptions**
     - 5 postulates, 5 common notions, 23 definitions (Book I).  *(What is taken as given?)*
   * - **Engine**
     - Human deduction citing earlier propositions; constructions by ruler and compass.  *(How are new truths derived?)*
   * - **Certificate**
     - The written proof.  *(What evidence is left behind?)*
   * - **Checker**
     - The reader.  *(What must be trusted?)*
   * - **Semantics**
     - Intended: the physical plane; modern reading: a Euclidean plane over a Euclidean field (Hilbert, Tarski).  *(What model makes it sound?)*

At a glance
-----------

:Logic / calculus: Informal deductive
:Exact vs numeric: Exact (no numbers)
:Decision procedure: None
:Role of the diagram: Essential and tacit
:Degeneracy handling: Ignored
:Trusted base (size): Human
:Trusts: Human readers (2,300 years)
:Catalog: 205 principles (61 shared with other systems) — :doc:`search </catalog/index>`

A statement in its own language
-------------------------------

.. code-block:: text

   I.5  In isosceles triangles the angles at the base are equal to one another, and, if
        the equal straight lines be produced further, the angles under the base will be
        equal to one another.

Source: ``euclid/resources/heath/enunciations.json``

Findings
--------

- Order and continuity facts (Pasch, circle–circle intersection in I.1) are read off the diagram, never stated.
- Equality of areas (I.35–I.47) is a primitive notion, not a number.

In the showcase
---------------

- :doc:`I.5 Pons asinorum </showcase/isosceles_base_angles>` — :raw-html:`<span class="codes-status" style="background:#e8d9b5">prose</span>` ``Elements I.5``
- :doc:`I.47 Pythagorean theorem </showcase/pythagorean>` — :raw-html:`<span class="codes-status" style="background:#e8d9b5">prose</span>` ``Elements I.47``
- :doc:`III.31 Angle in a semicircle </showcase/thales_semicircle>` — :raw-html:`<span class="codes-status" style="background:#e8d9b5">prose</span>` ``Elements III.31``
- :doc:`Simson line </showcase/simson_line>` — :raw-html:`<span class="codes-status" style="background:#dddddd">absent</span>` ``—``
- :doc:`Pasch's axiom </showcase/pasch>` — :raw-html:`<span class="codes-status" style="background:#f19c9c">gap</span>` ``—``

References
----------

- `Heath edition (GEOMETOR) <https://geometor.github.io/euclid>`__
