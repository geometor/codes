.. role:: raw-html(raw)
   :format: html

.. _card-kingdon:

kingdon (geometric algebra)
===========================

:raw-html:`<span class="codes-status" style="background:#7fd1c7">L2 Generic</span>` · **Archetype:** ``geometric-algebra`` · `upstream <https://github.com/tBuLi/kingdon>`__ · :doc:`dossier </systems/pga-cga>`

.. epigraph::

   Believe it because the identity expands to zero in the Clifford algebra — universally, when computed symbolically without division.

Trust chain
-----------

.. graphviz::
   :align: center
   :alt: kingdon trust chain

   digraph chain_kingdon {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, nodesep=0.15, ranksep=0.25];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     ontology [label=<<b>Ontology</b><br/><font point-size="9">Multivectors of Cl(p, q,<br/>r): points, lines,<br/>circles as blades (PGA /<br/>CGA).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language [label=<<b>Language</b><br/><font point-size="9">Python operators: alg =<br/>Algebra(3, 0, 1);<br/>b.cp(v); a ^ b; C<br/>&gt;&gt; P.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     ontology -> language;
     assumptions [label=<<b>Assumptions</b><br/><font point-size="9">Clifford algebra axioms<br/>with a diagonal metric<br/>signature.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     language -> assumptions;
     engine [label=<<b>Engine</b><br/><font point-size="9">Code-generated geometric<br/>products over symbolic<br/>or numeric coefficients.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     assumptions -> engine;
     certificate [label=<<b>Certificate</b><br/><font point-size="9">An expression (zero or<br/>not).</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     engine -> certificate;
     checker [label=<<b>Checker</b><br/><font point-size="9">kingdon codegen + SymPy<br/>simplify.</font>>, fillcolor="#7fd1c7", penwidth=2.2, width=1.4];
     certificate -> checker;
     semantics [label=<<b>Semantics</b><br/><font point-size="9">PGA / CGA models of the<br/>Euclidean plane or<br/>space.</font>>, fillcolor="#f4f5f7", penwidth=0.8, width=1.4];
     checker -> semantics;
   }

.. list-table::
   :widths: 18 82

   * - **Ontology**
     - Multivectors of Cl(p, q, r): points, lines, circles as blades (PGA / CGA).  *(What exists?)*
   * - **Language**
     - Python operators: alg = Algebra(3, 0, 1); b.cp(v); a ^ b; C >> P.  *(How is a statement written?)*
   * - **Assumptions**
     - Clifford algebra axioms with a diagonal metric signature.  *(What is taken as given?)*
   * - **Engine**
     - Code-generated geometric products over symbolic or numeric coefficients.  *(How are new truths derived?)*
   * - **Certificate**
     - An expression (zero or not).  *(What evidence is left behind?)*
   * - **Checker**
     - kingdon codegen + SymPy simplify.  *(What must be trusted?)*
   * - **Semantics**
     - PGA / CGA models of the Euclidean plane or space.  *(What model makes it sound?)*

At a glance
-----------

:Logic / calculus: Algebraic identity
:Exact vs numeric: Exact symbolic or float
:Decision procedure: Polynomial expansion (no division)
:Role of the diagram: None
:Degeneracy handling: Appears as zero / ideal elements
:Trusted base (size): ~5.2k lines + SymPy
:Trusts: GA product engines (kingdon ~5.2k · galgebra ~9.5k lines) · SymPy simplification (core heuristics + mpmath)

A statement in its own language
-------------------------------

.. code-block:: python

   alg = Algebra(3, 0, 1)
   b = alg.bivector(name='b'); v = alg.vector(name='v')
   b.cp(v)

Source: `README.rst <https://github.com/tBuLi/kingdon/blob/master/README.rst>`__

Findings
--------

- Generated product code over exact RationalPolynomial; default coefficient simplifier is sympy.simplify(sympy.expand(v)).
- 2D CGA: circle power is -2\*(kappa \| P), circumcenter C \* ni \* ~C, inversion C >> P.

References
----------

- `kingdon <https://github.com/tBuLi/kingdon>`__
