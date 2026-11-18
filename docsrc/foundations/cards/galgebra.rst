.. role:: raw-html(raw)
   :format: html

.. _card-galgebra:

galgebra (geometric algebra)
============================

:raw-html:`<span class="codes-status" style="background:#7fd1c7">L2 Generic</span>` · **Archetype:** ``geometric-algebra`` · `upstream <https://github.com/pygae/galgebra>`__ · :doc:`dossier </systems/pga-cga>`

.. epigraph::

   Believe it because the multivector difference simplifies to zero for an arbitrary (possibly symbolic) metric — as far as SymPy's simplify can tell.

Trust chain
-----------

.. graphviz::
   :align: center
   :alt: galgebra trust chain

   digraph chain_galgebra {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, nodesep=0.15, ranksep=0.25];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     ontology [label=<<b>Ontology</b><br/><font point-size="9">Multivectors over Ga<br/>with an arbitrary metric<br/>tensor and coordinates;<br/>geometric calculus …</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language [label=<<b>Language</b><br/><font point-size="9">Python: o3d = Ga('e',<br/>g=[1, 1, 1],<br/>coords=symbols('x y z',<br/>real=True)).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     ontology -> language;
     assumptions [label=<<b>Assumptions</b><br/><font point-size="9">Clifford algebra axioms<br/>for the metric g.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language -> assumptions;
     engine [label=<<b>Engine</b><br/><font point-size="9">Symbolic geometric<br/>products; equality by<br/>expand + simplify.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     assumptions -> engine;
     certificate [label=<<b>Certificate</b><br/><font point-size="9">An expression.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     engine -> certificate;
     checker [label=<<b>Checker</b><br/><font point-size="9">galgebra core + SymPy<br/>simplify.</font>>, fillcolor="#7fd1c7", penwidth=2.2, width=1.4];
     certificate -> checker;
     semantics [label=<<b>Semantics</b><br/><font point-size="9">Geometric algebra over a<br/>symbolic metric.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     checker -> semantics;
   }

.. list-table::
   :widths: 18 82

   * - **Ontology**
     - Multivectors over Ga with an arbitrary metric tensor and coordinates; geometric calculus operators.  *(What exists?)*
   * - **Language**
     - Python: o3d = Ga('e', g=[1, 1, 1], coords=symbols('x y z', real=True)).  *(How is a statement written?)*
   * - **Assumptions**
     - Clifford algebra axioms for the metric g.  *(What is taken as given?)*
   * - **Engine**
     - Symbolic geometric products; equality by expand + simplify.  *(How are new truths derived?)*
   * - **Certificate**
     - An expression.  *(What evidence is left behind?)*
   * - **Checker**
     - galgebra core + SymPy simplify.  *(What must be trusted?)*
   * - **Semantics**
     - Geometric algebra over a symbolic metric.  *(What model makes it sound?)*

At a glance
-----------

:Logic / calculus: Algebraic identity
:Exact vs numeric: Exact symbolic
:Decision procedure: Heuristic (simplify)
:Role of the diagram: None
:Degeneracy handling: Degenerate metrics unsupported in dual
:Trusted base (size): ~9.5k lines + SymPy
:Trusts: GA product engines (kingdon ~5.2k · galgebra ~9.5k lines) · SymPy simplification (core heuristics + mpmath)

A statement in its own language
-------------------------------

.. code-block:: python

   o3d = Ga('e', g=[1, 1, 1], coords=symbols('x,y,z', real=True))

Source: `README.md <https://github.com/pygae/galgebra/blob/master/README.md>`__

Findings
--------

- Mv.\_\_eq\_\_ computes (self - A).expand().simplify() and compares with zero (mv.py:479-483).
- .dual() fails for degenerate metrics (PGA, I² = 0); no regressive join.

References
----------

- `galgebra <https://github.com/pygae/galgebra>`__
