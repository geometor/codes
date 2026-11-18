.. role:: raw-html(raw)
   :format: html

.. _card-cindyjs:

CindyJS
=======

:raw-html:`<span class="codes-status" style="background:#dcdcdc">L0 Plausible</span>` · **Archetype:** ``numeric-interactive`` · `upstream <https://github.com/CindyJS/CindyJS>`__ · :doc:`dossier </systems/cindyjs>`

.. epigraph::

   Believe it because it keeps looking true while you drag — floating-point projective geometry with randomized conjecture checks, and no proof.

Trust chain
-----------

.. graphviz::
   :align: center
   :alt: CindyJS trust chain

   digraph chain_cindyjs {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, nodesep=0.15, ranksep=0.25];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     ontology [label=<<b>Ontology</b><br/><font point-size="9">Homogeneous complex<br/>projective coordinates<br/>(ℂP²): points, lines,<br/>conics.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language [label=<<b>Language</b><br/><font point-size="9">Declarative scene<br/>({type: "Meet", args:<br/>["a", "b"]}) or<br/>CindyScript:<br/>meet(join(A, B), …).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     ontology -> language;
     assumptions [label=<<b>Assumptions</b><br/><font point-size="9">IEEE-754 arithmetic (eps<br/>1e-10, epsbig 1e-6).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language -> assumptions;
     engine [label=<<b>Engine</b><br/><font point-size="9">Numeric construction<br/>with complex tracing;<br/>randomized conjecture<br/>checking.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     assumptions -> engine;
     certificate [label=<<b>Certificate</b><br/><font point-size="9">None.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     engine -> certificate;
     checker [label=<<b>Checker</b><br/><font point-size="9">Floating-point<br/>arithmetic.</font>>, fillcolor="#dcdcdc", penwidth=2.2, width=1.4];
     certificate -> checker;
     semantics [label=<<b>Semantics</b><br/><font point-size="9">Continuous configuration<br/>space over ℂP².</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     checker -> semantics;
   }

.. list-table::
   :widths: 18 82

   * - **Ontology**
     - Homogeneous complex projective coordinates (ℂP²): points, lines, conics.  *(What exists?)*
   * - **Language**
     - Declarative scene ({type: "Meet", args: ["a", "b"]}) or CindyScript: meet(join(A, B), …).  *(How is a statement written?)*
   * - **Assumptions**
     - IEEE-754 arithmetic (eps 1e-10, epsbig 1e-6).  *(What is taken as given?)*
   * - **Engine**
     - Numeric construction with complex tracing; randomized conjecture checking.  *(How are new truths derived?)*
   * - **Certificate**
     - None.  *(What evidence is left behind?)*
   * - **Checker**
     - Floating-point arithmetic.  *(What must be trusted?)*
   * - **Semantics**
     - Continuous configuration space over ℂP².  *(What model makes it sound?)*

At a glance
-----------

:Logic / calculus: None (numeric evidence)
:Exact vs numeric: Float
:Decision procedure: Probabilistic
:Role of the diagram: The diagram is the system
:Degeneracy handling: Singularity heuristics in tracing
:Trusted base (size): ~5.8k lines JS (float)
:Trusts: IEEE-754 floats (eps 1e-10)

A statement in its own language
-------------------------------

.. code-block:: javascript

   { name: "D", type: "Meet", args: ["a", "b"] }

Source: `CindyJS <https://github.com/CindyJS/CindyJS>`__

Findings
--------

- The 'prover' guesses incidences within 1e-6, perturbs free elements 3 times, and keeps survivors (libgeo/Prover.js).
- Complex tracing keeps branches continuous across singularities (libgeo/Tracing.js).

References
----------

- `CindyJS <https://cindyjs.org>`__
