.. role:: raw-html(raw)
   :format: html

.. _card-sympy:

SymPy geometry
==============

:raw-html:`<span class="codes-status" style="background:#9cc3f0">L1 Instance</span>` · **Archetype:** ``analytic-cas`` · `upstream <https://github.com/sympy/sympy>`__ · :doc:`dossier </systems/sympy-geometry>`

.. epigraph::

   Believe it because exact arithmetic on concrete coordinates evaluates the predicate to True — subject to SymPy's simplification heuristics.

Trust chain
-----------

.. graphviz::
   :align: center
   :alt: SymPy trust chain

   digraph chain_sympy {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, nodesep=0.15, ranksep=0.25];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     ontology [label=<<b>Ontology</b><br/><font point-size="9">Coordinate entities:<br/>Point, Line, Segment,<br/>Circle, Polygon over<br/>SymPy expressions.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language [label=<<b>Language</b><br/><font point-size="9">Python predicates:<br/>Point.is_collinear(A, B,<br/>C),<br/>Point.is_concyclic(…).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     ontology -> language;
     assumptions [label=<<b>Assumptions</b><br/><font point-size="9">Field arithmetic over<br/>exact SymPy numbers.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language -> assumptions;
     engine [label=<<b>Engine</b><br/><font point-size="9">Expression evaluation;<br/>simplify / equals; rank<br/>with a numeric zero<br/>test.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     assumptions -> engine;
     certificate [label=<<b>Certificate</b><br/><font point-size="9">A boolean.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     engine -> certificate;
     checker [label=<<b>Checker</b><br/><font point-size="9">SymPy simplification<br/>heuristics + mpmath.</font>>, fillcolor="#9cc3f0", penwidth=2.2, width=1.4];
     certificate -> checker;
     semantics [label=<<b>Semantics</b><br/><font point-size="9">One concrete figure (or<br/>symbolic coordinates).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     checker -> semantics;
   }

.. list-table::
   :widths: 18 82

   * - **Ontology**
     - Coordinate entities: Point, Line, Segment, Circle, Polygon over SymPy expressions.  *(What exists?)*
   * - **Language**
     - Python predicates: Point.is\_collinear(A, B, C), Point.is\_concyclic(…).  *(How is a statement written?)*
   * - **Assumptions**
     - Field arithmetic over exact SymPy numbers.  *(What is taken as given?)*
   * - **Engine**
     - Expression evaluation; simplify / equals; rank with a numeric zero test.  *(How are new truths derived?)*
   * - **Certificate**
     - A boolean.  *(What evidence is left behind?)*
   * - **Checker**
     - SymPy simplification heuristics + mpmath.  *(What must be trusted?)*
   * - **Semantics**
     - One concrete figure (or symbolic coordinates).  *(What model makes it sound?)*

At a glance
-----------

:Logic / calculus: Evaluation
:Exact vs numeric: Exact inputs; heuristic zero tests
:Decision procedure: Heuristic (simplify)
:Role of the diagram: The object is the computation
:Degeneracy handling: Visible in the instance
:Trusted base (size): ~12k lines + SymPy core
:Trusts: SymPy simplification (core heuristics + mpmath)
:Catalog: 109 principles (23 shared with other systems) — :doc:`search </catalog/index>`

A statement in its own language
-------------------------------

.. code-block:: python

   from sympy import Point
   Point.is_collinear(Point(0, 0), Point(1, 1), Point(2, 2))   # True

Source: `point.py <https://github.com/sympy/sympy/blob/master/sympy/geometry/point.py>`__

Findings
--------

- Point.affine\_rank (behind is\_collinear) zero-tests with abs(x.n(2)) < 1e-12 — a 2-digit numeric test, marked 'XXX fragile' (point.py:333-334).
- Float inputs are silently rationalized via nsimplify (point.py:165-168).
- Triangle.excenters has a live formula bug (polygon.py:2714-2726).

References
----------

- `sympy.geometry 1.14.0 <https://docs.sympy.org/latest/modules/geometry/index.html>`__
