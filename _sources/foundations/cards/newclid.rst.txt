.. role:: raw-html(raw)
   :format: html

.. _card-newclid:

Newclid
=======

:raw-html:`<span class="codes-status" style="background:#f6b26b">L3 Rule-closed</span>` · **Archetype:** ``rule-engine`` · `upstream <https://github.com/LMCRC/Newclid>`__ · :doc:`dossier </systems/alphageometry-newclid>`

.. epigraph::

   Believe it because the DDARN engine derived it from a curated rule set descended from AlphaGeometry — again with numerically checked side conditions.

Trust chain
-----------

.. graphviz::
   :align: center
   :alt: Newclid trust chain

   digraph chain_newclid {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, nodesep=0.15, ranksep=0.25];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     ontology [label=<<b>Ontology</b><br/><font point-size="9">AG predicates plus<br/>metric ones (pythagoras,<br/>obtuse_angle,<br/>sameclock).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language [label=<<b>Language</b><br/><font point-size="9">JGEX/AG-style<br/>construction text<br/>wrapped in Python<br/>(JGEXFormulation.from_text).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     ontology -> language;
     assumptions [label=<<b>Assumptions</b><br/><font point-size="9">87 Rule objects;<br/>DEFAULT_RULES = ALL −<br/>DEACTIVATED − TRIAGE<br/>(~58).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language -> assumptions;
     engine [label=<<b>Engine</b><br/><font point-size="9">DDARN: rule matching +<br/>sympy.solve AR tables;<br/>optional Yuclid C++<br/>solver.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     assumptions -> engine;
     certificate [label=<<b>Certificate</b><br/><font point-size="9">Justification graph and<br/>written proof.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     engine -> certificate;
     checker [label=<<b>Checker</b><br/><font point-size="9">Python + SymPy + rule<br/>soundness + numeric<br/>checks (rel tol 1e-3).</font>>, fillcolor="#f6b26b", penwidth=2.2, width=1.4];
     certificate -> checker;
     semantics [label=<<b>Semantics</b><br/><font point-size="9">As AlphaGeometry: one<br/>float diagram of the<br/>real plane.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     checker -> semantics;
   }

.. list-table::
   :widths: 18 82

   * - **Ontology**
     - AG predicates plus metric ones (pythagoras, obtuse\_angle, sameclock).  *(What exists?)*
   * - **Language**
     - JGEX/AG-style construction text wrapped in Python (JGEXFormulation.from\_text).  *(How is a statement written?)*
   * - **Assumptions**
     - 87 Rule objects; DEFAULT\_RULES = ALL − DEACTIVATED − TRIAGE (~58).  *(What is taken as given?)*
   * - **Engine**
     - DDARN: rule matching + sympy.solve AR tables; optional Yuclid C++ solver.  *(How are new truths derived?)*
   * - **Certificate**
     - Justification graph and written proof.  *(What evidence is left behind?)*
   * - **Checker**
     - Python + SymPy + rule soundness + numeric checks (rel tol 1e-3).  *(What must be trusted?)*
   * - **Semantics**
     - As AlphaGeometry: one float diagram of the real plane.  *(What model makes it sound?)*

At a glance
-----------

:Logic / calculus: Horn-clause forward chaining
:Exact vs numeric: Exact algebra; numeric side conditions
:Decision procedure: Saturation over a finite rule set
:Role of the diagram: Essential: every predicate checked numerically first
:Degeneracy handling: Numeric filters
:Trusted base (size): ~15.4k lines Python (+15k C++)
:Trusts: Newclid DDARN (~15.4k lines Python (+~15k C++ Yuclid)) · SymPy simplification (core heuristics + mpmath) · Numeric diagram (tol 1e-12 (AG) · rel 1e-3 (Newclid))
:Catalog: 86 principles (39 shared with other systems) — :doc:`search </catalog/index>`

A statement in its own language
-------------------------------

.. code-block:: python

   R45_SIMSONS_LINE_THEOREM = Rule(
       id="r45",
       premises_txt=("cyclic A B C P", "coll A L C", "perp P L A C",
                     "coll M B C", "perp P M B C", "coll N A B", "perp P N A B"),
       conclusions_txt=("coll L M N",),
   )

Source: `all\_rules.py#L521-L534 <https://github.com/LMCRC/Newclid/blob/ac6550732a950564cf7614d605b5bf1eadd29701/newclid/src/newclid/all_rules.py#L521-L534>`__

Findings
--------

- 87 live rules (r00–r42 from AlphaGeometry); about 58 active by default after DEACTIVATED and TRIAGE sets.
- R57 Pythagoras is deactivated; R45 Simson is left out as provable from other rules.
- Numeric tolerance REL\_TOL = 0.001 (numerical/\_\_init\_\_.py) — far looser than AG's 1e-12.

In the showcase
---------------

- :doc:`I.5 Pons asinorum </showcase/isosceles_base_angles>` — :raw-html:`<span class="codes-status" style="background:#f6b26b">rule</span>` ``R13_ISOSCELES_TRIANGLE_EQUAL_ANGLES``
- :doc:`I.47 Pythagorean theorem </showcase/pythagorean>` — :raw-html:`<span class="codes-status" style="background:#f6b26b">rule</span>` ``R57_PYTHAGORAS_THEOREM``
- :doc:`III.31 Angle in a semicircle </showcase/thales_semicircle>` — :raw-html:`<span class="codes-status" style="background:#f6b26b">rule</span>` ``R20_DIAMETER_IS_HYPOTENUSE``
- :doc:`Simson line </showcase/simson_line>` — :raw-html:`<span class="codes-status" style="background:#f6b26b">rule</span>` ``R45_SIMSONS_LINE_THEOREM``

References
----------

- `Newclid: a user-friendly replacement for AlphaGeometry (arXiv 2411.11938) <https://arxiv.org/abs/2411.11938>`__
