.. role:: raw-html(raw)
   :format: html

.. _foundations-connections:

Connections
===========

How the systems relate: who descends from whom, who formalizes whom, what they share in their ontology, and how much of the principle catalog they realize in common.

Bridges
-------

Solid edges are realized translations or lineage; dotted edges are proposed. Node labels carry the ladder level.

.. graphviz::
   :align: center
   :alt: Bridges between systems

   digraph bridges {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, ranksep=0.9, nodesep=0.35];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     euclid [label="Euclid  (H)", fillcolor="#e8d9b5", URL="../foundations/cards/euclid.html", target="_top", tooltip="Believe it because it follows, step by step, from five postulates and five common notions — as checked by readers, with the diagram doing silent work."];
     leaneuclid [label="LeanEuclid  (L3)", fillcolor="#f6b26b", URL="../foundations/cards/leaneuclid.html", target="_top", tooltip="Believe it because Lean's kernel checked every rule application from System E's axioms — except that premise-discharging steps are admitted by an SMT oracle axiom."];
     mathlib4 [label="mathlib4  (L5)", fillcolor="#c5b3e6", URL="../foundations/cards/mathlib4.html", target="_top", tooltip="Believe it because geometry is defined from real inner-product spaces and every theorem is a kernel-checked consequence of Lean's logic alone."];
     geocoq [label="GeoCoq  (L4)", fillcolor="#9fd8a8", URL="../foundations/cards/geocoq.html", target="_top", tooltip="Believe it because the Coq kernel checked it from Tarski's (or Hilbert's, or Euclid's) axioms — and GeoCoq proves those axiom systems interpret one another and hold in ℝ²."];
     alphageometry [label="AlphaGeometry  (L3)", fillcolor="#f6b26b", URL="../foundations/cards/alphageometry.html", target="_top", tooltip="Believe it because a deduction engine derived it from 43 assumed rules — with side conditions (non-collinear, same side) read off a random numeric diagram."];
     newclid [label="Newclid  (L3)", fillcolor="#f6b26b", URL="../foundations/cards/newclid.html", target="_top", tooltip="Believe it because the DDARN engine derived it from a curated rule set descended from AlphaGeometry — again with numerically checked side conditions."];
     jgex [label="JGEX  (L2)", fillcolor="#7fd1c7", URL="../foundations/cards/jgex.html", target="_top", tooltip="Believe it because the hypothesis polynomials reduce the conclusion to zero (Wu / Gröbner) — true generically, provided the printed non-degeneracy conditions hold."];
     sympy [label="SymPy  (L1)", fillcolor="#9cc3f0", URL="../foundations/cards/sympy.html", target="_top", tooltip="Believe it because exact arithmetic on concrete coordinates evaluates the predicate to True — subject to SymPy's simplification heuristics."];
     geometor_model [label="geometor.model  (L1)", fillcolor="#9cc3f0", URL="../foundations/cards/geometor_model.html", target="_top", tooltip="Believe it because the figure is built exactly — algebraic coordinates from ruler-and-compass intersections — and every asserted relation reduces to zero."];
     kingdon [label="kingdon  (L2)", fillcolor="#7fd1c7", URL="../foundations/cards/kingdon.html", target="_top", tooltip="Believe it because the identity expands to zero in the Clifford algebra — universally, when computed symbolically without division."];
     galgebra [label="galgebra  (L2)", fillcolor="#7fd1c7", URL="../foundations/cards/galgebra.html", target="_top", tooltip="Believe it because the multivector difference simplifies to zero for an arbitrary (possibly symbolic) metric — as far as SymPy's simplify can tell."];
     geocoq -> euclid [label="Book I (Beeson–Narboux–Wiedijk)", color="#2e8b57", fontcolor="#2e8b57", style=solid, URL="https://github.com/GeoCoq/GeoCoq/tree/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Elements/OriginalProofs", target="_blank"];
     leaneuclid -> euclid [label="Book I 1–48 in System E", color="#2e8b57", fontcolor="#2e8b57", style=solid, URL="https://github.com/loganrjmurphy/LeanEuclid/tree/33a72c0fa83914202532998a2e7b8771295c3cc7/Book", target="_blank"];
     mathlib4 -> leaneuclid [label="supplies ℝ only (sorts axiomatized)", color="#b5651d", fontcolor="#b5651d", style=solid, URL="https://github.com/loganrjmurphy/LeanEuclid/blob/33a72c0fa83914202532998a2e7b8771295c3cc7/SystemE/Theory/Sorts/Primitives.lean", target="_blank"];
     alphageometry -> newclid [label="rules r00–r42", color="#d08c3a", fontcolor="#d08c3a", style=solid, URL="https://github.com/LMCRC/Newclid/blob/ac6550732a950564cf7614d605b5bf1eadd29701/newclid/src/newclid/all_rules.py", target="_blank"];
     jgex -> alphageometry [label="construction language · jgex_ag_231", color="#d08c3a", fontcolor="#d08c3a", style=solid, URL="https://github.com/google-deepmind/alphageometry/blob/6777cb586cbb46beed28db12dc72c69770b68337/jgex_ag_231.txt", target="_blank"];
     jgex -> newclid [label="JGEXFormulation", color="#d08c3a", fontcolor="#d08c3a", style=solid, URL="https://github.com/LMCRC/Newclid", target="_blank"];
     sympy -> geometor_model [label="sympy.geometry + exact zero_test", color="#b5651d", fontcolor="#b5651d", style=solid, URL="https://github.com/geometor/model", target="_blank"];
     galgebra -> kingdon [label="interop Cl(p,q,r) factory", color="#3a7bd5", fontcolor="#3a7bd5", style=dashed, URL="https://github.com/pygae/galgebra/blob/master/galgebra/interop/kingdon.py", target="_blank"];
     geometor_model -> euclid [label="exact witnesses of propositions", color="#8a8f98", fontcolor="#8a8f98", style=dotted];
     geometor_model -> mathlib4 [label="certificate export (linear_combination)", color="#3a7bd5", fontcolor="#3a7bd5", style=dotted];
     alphageometry -> mathlib4 [label="prove the 43 rules as lemmas", color="#2e8b57", fontcolor="#2e8b57", style=dotted];
   }

.. list-table::
   :header-rows: 1
   :widths: 16 16 12 40 16

   * - From
     - To
     - Kind
     - Bridge
     - Status
   * - :doc:`GeoCoq <cards/geocoq>`
     - :doc:`Euclid <cards/euclid>`
     - ``formalizes``
     - `Book I (Beeson–Narboux–Wiedijk) <https://github.com/GeoCoq/GeoCoq/tree/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Elements/OriginalProofs>`__
     - realized
   * - :doc:`LeanEuclid <cards/leaneuclid>`
     - :doc:`Euclid <cards/euclid>`
     - ``formalizes``
     - `Book I 1–48 in System E <https://github.com/loganrjmurphy/LeanEuclid/tree/33a72c0fa83914202532998a2e7b8771295c3cc7/Book>`__
     - realized
   * - :doc:`mathlib4 <cards/mathlib4>`
     - :doc:`LeanEuclid <cards/leaneuclid>`
     - ``builds_on``
     - `supplies ℝ only (sorts axiomatized) <https://github.com/loganrjmurphy/LeanEuclid/blob/33a72c0fa83914202532998a2e7b8771295c3cc7/SystemE/Theory/Sorts/Primitives.lean>`__
     - realized
   * - :doc:`AlphaGeometry <cards/alphageometry>`
     - :doc:`Newclid <cards/newclid>`
     - ``lineage``
     - `rules r00–r42 <https://github.com/LMCRC/Newclid/blob/ac6550732a950564cf7614d605b5bf1eadd29701/newclid/src/newclid/all_rules.py>`__
     - realized
   * - :doc:`JGEX <cards/jgex>`
     - :doc:`AlphaGeometry <cards/alphageometry>`
     - ``lineage``
     - `construction language · jgex\_ag\_231 <https://github.com/google-deepmind/alphageometry/blob/6777cb586cbb46beed28db12dc72c69770b68337/jgex_ag_231.txt>`__
     - realized
   * - :doc:`JGEX <cards/jgex>`
     - :doc:`Newclid <cards/newclid>`
     - ``lineage``
     - `JGEXFormulation <https://github.com/LMCRC/Newclid>`__
     - realized
   * - :doc:`SymPy <cards/sympy>`
     - :doc:`geometor.model <cards/geometor_model>`
     - ``builds_on``
     - `sympy.geometry + exact zero\_test <https://github.com/geometor/model>`__
     - realized
   * - :doc:`galgebra <cards/galgebra>`
     - :doc:`kingdon <cards/kingdon>`
     - ``translates``
     - `interop Cl(p,q,r) factory <https://github.com/pygae/galgebra/blob/master/galgebra/interop/kingdon.py>`__
     - realized
   * - :doc:`geometor.model <cards/geometor_model>`
     - :doc:`Euclid <cards/euclid>`
     - ``benchmark``
     - exact witnesses of propositions
     - realized
   * - :doc:`geometor.model <cards/geometor_model>`
     - :doc:`mathlib4 <cards/mathlib4>`
     - ``translates``
     - certificate export (linear\_combination)
     - proposed
   * - :doc:`AlphaGeometry <cards/alphageometry>`
     - :doc:`mathlib4 <cards/mathlib4>`
     - ``proves``
     - prove the 43 rules as lemmas
     - proposed

Ladder lifts
------------

Routes by which a system's claims could climb the Truth Ladder.

.. list-table::
   :header-rows: 1
   :widths: 20 12 12 40 16

   * - System
     - From
     - To
     - Via
     - Status
   * - :doc:`geometor.model <cards/geometor_model>`
     - L1
     - L2
     - symbolic parameters
     - partial
   * - :doc:`geometor.model <cards/geometor_model>`
     - L1
     - L5
     - Lean certificate export
     - proposed
   * - :doc:`LeanEuclid <cards/leaneuclid>`
     - L3
     - L4
     - SMT proof reconstruction
     - proposed
   * - :doc:`AlphaGeometry <cards/alphageometry>`
     - L3
     - L5
     - rules proved in mathlib
     - proposed

Shared ontology
---------------

Each system linked to its primitive sorts. Hubs (Point, Line, Circle) are near-universal; the periphery shows what is distinctive — Tarski's betweenness and congruence, mathlib's vectors and spheres, multivectors, homogeneous coordinates.

.. graphviz::
   :align: center
   :alt: Ontology graph

   graph ontology {
     graph [layout=neato, overlap=false, splines=true, bgcolor="transparent", fontname="Helvetica", sep="+6"];
     node [fontname="Helvetica", fontsize=10, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [color="#8a8f98", penwidth=0.7];
     "p_Point" [label="Point", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=17];
     "p_Line" [label="Line", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=15];
     "p_Circle" [label="Circle", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=13];
     "p_Angle" [label="Angle", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=11];
     "p_Area" [label="Area", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=10];
     "p_Segment" [label="Segment", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=10];
     "p_Triangle" [label="Triangle", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=10];
     "p_Betweenness" [label="Betweenness", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=11];
     "p_Real number" [label="Real number", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=11];
     "p_Vector" [label="Vector", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=10];
     "p_Affine subspace" [label="Affine subspace", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=10];
     "p_Sphere" [label="Sphere", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=10];
     "p_Simplex" [label="Simplex", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=10];
     "p_Congruence" [label="Congruence", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=10];
     "p_Predicate" [label="Predicate", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=12];
     "p_Polynomial" [label="Polynomial", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=10];
     "p_Polygon" [label="Polygon", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=11];
     "p_Algebraic number" [label="Algebraic number", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=10];
     "p_Multivector" [label="Multivector", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=11];
     "p_Metric" [label="Metric", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=10];
     "p_Homogeneous coords" [label="Homogeneous coords", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=10];
     "p_Conic" [label="Conic", shape=ellipse, style=filled, fillcolor="#ffffff", fontsize=10];
     "s_euclid" [label="Euclid", fillcolor="#e8d9b5"];
     "s_euclid" -- "p_Point";
     "s_euclid" -- "p_Line";
     "s_euclid" -- "p_Circle";
     "s_euclid" -- "p_Angle";
     "s_euclid" -- "p_Area";
     "s_leaneuclid" [label="LeanEuclid", fillcolor="#f6b26b"];
     "s_leaneuclid" -- "p_Point";
     "s_leaneuclid" -- "p_Line";
     "s_leaneuclid" -- "p_Circle";
     "s_leaneuclid" -- "p_Segment";
     "s_leaneuclid" -- "p_Angle";
     "s_leaneuclid" -- "p_Triangle";
     "s_leaneuclid" -- "p_Betweenness";
     "s_leaneuclid" -- "p_Real number";
     "s_mathlib4" [label="mathlib4", fillcolor="#c5b3e6"];
     "s_mathlib4" -- "p_Point";
     "s_mathlib4" -- "p_Vector";
     "s_mathlib4" -- "p_Affine subspace";
     "s_mathlib4" -- "p_Sphere";
     "s_mathlib4" -- "p_Simplex";
     "s_mathlib4" -- "p_Real number";
     "s_geocoq" [label="GeoCoq", fillcolor="#9fd8a8"];
     "s_geocoq" -- "p_Point";
     "s_geocoq" -- "p_Betweenness";
     "s_geocoq" -- "p_Congruence";
     "s_geocoq" -- "p_Line";
     "s_alphageometry" [label="AlphaGeometry", fillcolor="#f6b26b"];
     "s_alphageometry" -- "p_Point";
     "s_alphageometry" -- "p_Predicate";
     "s_newclid" [label="Newclid", fillcolor="#f6b26b"];
     "s_newclid" -- "p_Point";
     "s_newclid" -- "p_Predicate";
     "s_jgex" [label="JGEX", fillcolor="#7fd1c7"];
     "s_jgex" -- "p_Point";
     "s_jgex" -- "p_Predicate";
     "s_jgex" -- "p_Polynomial";
     "s_sympy" [label="SymPy", fillcolor="#9cc3f0"];
     "s_sympy" -- "p_Point";
     "s_sympy" -- "p_Line";
     "s_sympy" -- "p_Circle";
     "s_sympy" -- "p_Polygon";
     "s_geometor_model" [label="geometor.model", fillcolor="#9cc3f0"];
     "s_geometor_model" -- "p_Point";
     "s_geometor_model" -- "p_Line";
     "s_geometor_model" -- "p_Circle";
     "s_geometor_model" -- "p_Polygon";
     "s_geometor_model" -- "p_Algebraic number";
     "s_kingdon" [label="kingdon", fillcolor="#7fd1c7"];
     "s_kingdon" -- "p_Multivector";
     "s_galgebra" [label="galgebra", fillcolor="#7fd1c7"];
     "s_galgebra" -- "p_Multivector";
     "s_galgebra" -- "p_Metric";
     "s_cindyjs" [label="CindyJS", fillcolor="#dcdcdc"];
     "s_cindyjs" -- "p_Homogeneous coords";
     "s_cindyjs" -- "p_Point";
     "s_cindyjs" -- "p_Line";
     "s_cindyjs" -- "p_Conic";
   }

Shared principles
-----------------

Edges join base systems that realize the same discovered principle; edge labels and widths count the shared principles. This replaces the long coverage matrix — drill into the :doc:`catalog </catalog/index>` with the system filters for the rows.

.. graphviz::
   :align: center
   :alt: Shared-principle graph

   graph overlap {
     graph [layout=neato, overlap=false, splines=true, sep="+12", bgcolor="transparent", fontname="Helvetica"];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23"];
     edge [fontname="Helvetica", fontsize=10, color="#8a8f98", fontcolor="#3a7bd5"];
     leaneuclid [label="LeanEuclid\n256 principles", fillcolor="#f6b26b"];
     geometor_model [label="geometor.model\n47 principles", fillcolor="#9cc3f0"];
     sympy [label="SymPy\n109 principles", fillcolor="#9cc3f0"];
     newclid [label="Newclid\n86 principles", fillcolor="#f6b26b"];
     euclid [label="Euclid\n205 principles", fillcolor="#e8d9b5"];
     alphageometry [label="AlphaGeometry\n108 principles", fillcolor="#f6b26b"];
     alphageometry -- euclid [label="18", penwidth=2.36, len=3.35];
     alphageometry -- geometor_model [label="2", penwidth=0.80, len=4.11];
     alphageometry -- leaneuclid [label="15", penwidth=2.07, len=3.49];
     alphageometry -- newclid [label="35", penwidth=4.03, len=2.55];
     alphageometry -- sympy [label="11", penwidth=1.68, len=3.68];
     euclid -- leaneuclid [label="51", penwidth=5.60, len=1.80];
     euclid -- newclid [label="16", penwidth=2.17, len=3.45];
     euclid -- sympy [label="4", penwidth=0.99, len=4.01];
     geometor_model -- leaneuclid [label="9", penwidth=1.48, len=3.78];
     geometor_model -- sympy [label="10", penwidth=1.58, len=3.73];
     leaneuclid -- newclid [label="7", penwidth=1.29, len=3.87];
     leaneuclid -- sympy [label="13", penwidth=1.87, len=3.59];
   }
