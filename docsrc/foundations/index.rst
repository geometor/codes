:navigation: header
:order: 1
:nav_title: Foundations

.. role:: raw-html(raw)
   :format: html

.. _foundations-index:

Truth Foundations
=================

Every geometric system answers one question differently: why should I believe this is true? CODES compares systems by their truth foundation — what exists, what is assumed, how truths are derived, what evidence remains, and what must be trusted.

Two lenses organize the comparison: the **Truth Ladder** ranks the *strength of the claim* a system certifies, and the **Trust Stack** decomposes *how* it certifies it. The interactive Atlas on the :doc:`home page </index>` shows both at once.

Truth Ladder
------------

Rungs rank claims, not quality: a CAS witness (L1) and a kernel-checked proof (L4) answer different questions. Dashed blue edges are *lifts* — routes by which a system's claims could climb. Click a system to open its card.

.. graphviz::
   :align: center
   :alt: Truth Ladder

   digraph ladder {
     graph [rankdir=BT, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, ranksep=0.35, newrank=true];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     lvl_L0 [label="L0  Plausible\nlooks true numerically", fillcolor="#dcdcdc", shape=box, style="filled", width=2.6, fontsize=10];
     lvl_L1 [label="L1  Instance\ntrue for this exact figure", fillcolor="#9cc3f0", shape=box, style="filled", width=2.6, fontsize=10];
     lvl_L2 [label="L2  Generic\ntrue off a degenerate set (NDG)", fillcolor="#7fd1c7", shape=box, style="filled", width=2.6, fontsize=10];
     lvl_L3 [label="L3  Rule-closed\nderivable from an assumed rule list", fillcolor="#f6b26b", shape=box, style="filled", width=2.6, fontsize=10];
     lvl_L4 [label="L4  Axiom-checked\nkernel-checked from geometric axioms", fillcolor="#9fd8a8", shape=box, style="filled", width=2.6, fontsize=10];
     lvl_L5 [label="L5  Foundational\ngeometry derived; no geometric axioms", fillcolor="#c5b3e6", shape=box, style="filled", width=2.6, fontsize=10];
     lvl_H [label="H  Human\nchecked by readers from postulates", fillcolor="#e8d9b5", shape=box, style="filled,dashed", width=2.6, fontsize=10];
     lvl_L0 -> lvl_L1 [arrowhead=none, penwidth=3, color="#c9ccd1"];
     lvl_L1 -> lvl_L2 [arrowhead=none, penwidth=3, color="#c9ccd1"];
     lvl_L2 -> lvl_L3 [arrowhead=none, penwidth=3, color="#c9ccd1"];
     lvl_L3 -> lvl_L4 [arrowhead=none, penwidth=3, color="#c9ccd1"];
     lvl_L4 -> lvl_L5 [arrowhead=none, penwidth=3, color="#c9ccd1"];
     lvl_L5 -> lvl_H [style=invis];
     { rank=same; lvl_L0; sys_cindyjs }
     sys_cindyjs [label="CindyJS", fillcolor="#dcdcdc", penwidth=0.8, URL="../foundations/cards/cindyjs.html", target="_top", tooltip="Believe it because it keeps looking true while you drag — floating-point projective geometry with randomized conjecture checks, and no proof."];
     lvl_L0 -> sys_cindyjs [style=invis];
     { rank=same; lvl_L1; sys_sympy sys_geometor_model }
     sys_sympy [label="SymPy", fillcolor="#9cc3f0", penwidth=0.8, URL="../foundations/cards/sympy.html", target="_top", tooltip="Believe it because exact arithmetic on concrete coordinates evaluates the predicate to True — subject to SymPy's simplification heuristics."];
     lvl_L1 -> sys_sympy [style=invis];
     sys_geometor_model [label="geometor.model", fillcolor="#9cc3f0", penwidth=1.6, URL="../foundations/cards/geometor_model.html", target="_top", tooltip="Believe it because the figure is built exactly — algebraic coordinates from ruler-and-compass intersections — and every asserted relation reduces to zero."];
     lvl_L1 -> sys_geometor_model [style=invis];
     { rank=same; lvl_L2; sys_jgex sys_kingdon sys_galgebra }
     sys_jgex [label="JGEX", fillcolor="#7fd1c7", penwidth=1.6, URL="../foundations/cards/jgex.html", target="_top", tooltip="Believe it because the hypothesis polynomials reduce the conclusion to zero (Wu / Gröbner) — true generically, provided the printed non-degeneracy conditions hold."];
     lvl_L2 -> sys_jgex [style=invis];
     sys_kingdon [label="kingdon", fillcolor="#7fd1c7", penwidth=0.8, URL="../foundations/cards/kingdon.html", target="_top", tooltip="Believe it because the identity expands to zero in the Clifford algebra — universally, when computed symbolically without division."];
     lvl_L2 -> sys_kingdon [style=invis];
     sys_galgebra [label="galgebra", fillcolor="#7fd1c7", penwidth=0.8, URL="../foundations/cards/galgebra.html", target="_top", tooltip="Believe it because the multivector difference simplifies to zero for an arbitrary (possibly symbolic) metric — as far as SymPy's simplify can tell."];
     lvl_L2 -> sys_galgebra [style=invis];
     { rank=same; lvl_L3; sys_leaneuclid sys_alphageometry sys_newclid }
     sys_leaneuclid [label="LeanEuclid", fillcolor="#f6b26b", penwidth=1.6, URL="../foundations/cards/leaneuclid.html", target="_top", tooltip="Believe it because Lean's kernel checked every rule application from System E's axioms — except that premise-discharging steps are admitted by an SMT oracle axiom."];
     lvl_L3 -> sys_leaneuclid [style=invis];
     sys_alphageometry [label="AlphaGeometry", fillcolor="#f6b26b", penwidth=1.6, URL="../foundations/cards/alphageometry.html", target="_top", tooltip="Believe it because a deduction engine derived it from 43 assumed rules — with side conditions (non-collinear, same side) read off a random numeric diagram."];
     lvl_L3 -> sys_alphageometry [style=invis];
     sys_newclid [label="Newclid", fillcolor="#f6b26b", penwidth=0.8, URL="../foundations/cards/newclid.html", target="_top", tooltip="Believe it because the DDARN engine derived it from a curated rule set descended from AlphaGeometry — again with numerically checked side conditions."];
     lvl_L3 -> sys_newclid [style=invis];
     { rank=same; lvl_L4; sys_geocoq }
     sys_geocoq [label="GeoCoq", fillcolor="#9fd8a8", penwidth=1.6, URL="../foundations/cards/geocoq.html", target="_top", tooltip="Believe it because the Coq kernel checked it from Tarski's (or Hilbert's, or Euclid's) axioms — and GeoCoq proves those axiom systems interpret one another and hold in ℝ²."];
     lvl_L4 -> sys_geocoq [style=invis];
     { rank=same; lvl_L5; sys_mathlib4 }
     sys_mathlib4 [label="mathlib4", fillcolor="#c5b3e6", penwidth=1.6, URL="../foundations/cards/mathlib4.html", target="_top", tooltip="Believe it because geometry is defined from real inner-product spaces and every theorem is a kernel-checked consequence of Lean's logic alone."];
     lvl_L5 -> sys_mathlib4 [style=invis];
     { rank=same; lvl_H; sys_euclid }
     sys_euclid [label="Euclid", fillcolor="#e8d9b5", penwidth=1.6, URL="../foundations/cards/euclid.html", target="_top", tooltip="Believe it because it follows, step by step, from five postulates and five common notions — as checked by readers, with the diagram doing silent work."];
     lvl_H -> sys_euclid [style=invis];
     sys_geometor_model -> lvl_L2 [style=dashed, color="#3a7bd5", fontcolor="#3a7bd5", label="symbolic parameters", constraint=false];
     sys_geometor_model -> lvl_L5 [style=dashed, color="#3a7bd5", fontcolor="#3a7bd5", label="Lean certificate export", constraint=false];
     sys_leaneuclid -> lvl_L4 [style=dashed, color="#3a7bd5", fontcolor="#3a7bd5", label="SMT proof reconstruction", constraint=false];
     sys_alphageometry -> lvl_L5 [style=dashed, color="#3a7bd5", fontcolor="#3a7bd5", label="rules proved in mathlib", constraint=false];
   }

.. list-table::
   :header-rows: 1
   :widths: 8 16 36 40

   * - Level
     - Name
     - Claim certified
     - Systems
   * - :raw-html:`<span class="codes-status" style="background:#dcdcdc">L0</span>`
     - Plausible
     - looks true numerically
     - :doc:`CindyJS <cards/cindyjs>`
   * - :raw-html:`<span class="codes-status" style="background:#9cc3f0">L1</span>`
     - Instance
     - true for this exact figure
     - :doc:`SymPy <cards/sympy>`, :doc:`geometor.model <cards/geometor_model>`
   * - :raw-html:`<span class="codes-status" style="background:#7fd1c7">L2</span>`
     - Generic
     - true off a degenerate set (NDG)
     - :doc:`JGEX <cards/jgex>`, :doc:`kingdon <cards/kingdon>`, :doc:`galgebra <cards/galgebra>`
   * - :raw-html:`<span class="codes-status" style="background:#f6b26b">L3</span>`
     - Rule-closed
     - derivable from an assumed rule list
     - :doc:`LeanEuclid <cards/leaneuclid>`, :doc:`AlphaGeometry <cards/alphageometry>`, :doc:`Newclid <cards/newclid>`
   * - :raw-html:`<span class="codes-status" style="background:#9fd8a8">L4</span>`
     - Axiom-checked
     - kernel-checked from geometric axioms
     - :doc:`GeoCoq <cards/geocoq>`
   * - :raw-html:`<span class="codes-status" style="background:#c5b3e6">L5</span>`
     - Foundational
     - geometry derived; no geometric axioms
     - :doc:`mathlib4 <cards/mathlib4>`
   * - :raw-html:`<span class="codes-status" style="background:#e8d9b5">H</span>`
     - Human
     - checked by readers from postulates
     - :doc:`Euclid <cards/euclid>`

The Trust Stack
---------------

Every system is described by the same seven layers. The **checker** layer is the trusted core.

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Layer
     - Question
   * - **Ontology**
     - What exists?
   * - **Language**
     - How is a statement written?
   * - **Assumptions**
     - What is taken as given?
   * - **Engine**
     - How are new truths derived?
   * - **Certificate**
     - What evidence is left behind?
   * - **Checker**
     - What must be trusted?
   * - **Semantics**
     - What model makes it sound?

Who Trusts What
---------------

Systems on the left, the components they must trust on the right. Shared hubs — the Lean kernel, SymPy, the numeric diagram — show where trust concentrates.

.. graphviz::
   :align: center
   :alt: Trusted components

   digraph trust {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, ranksep=1.1];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     subgraph cluster_sys { label="systems"; style=invis;
       sys_euclid [label="Euclid", fillcolor="#e8d9b5", URL="../foundations/cards/euclid.html", target="_top", tooltip="Believe it because it follows, step by step, from five postulates and five common notions — as checked by readers, with the diagram doing silent work."];
       sys_leaneuclid [label="LeanEuclid", fillcolor="#f6b26b", URL="../foundations/cards/leaneuclid.html", target="_top", tooltip="Believe it because Lean's kernel checked every rule application from System E's axioms — except that premise-discharging steps are admitted by an SMT oracle axiom."];
       sys_mathlib4 [label="mathlib4", fillcolor="#c5b3e6", URL="../foundations/cards/mathlib4.html", target="_top", tooltip="Believe it because geometry is defined from real inner-product spaces and every theorem is a kernel-checked consequence of Lean's logic alone."];
       sys_geocoq [label="GeoCoq", fillcolor="#9fd8a8", URL="../foundations/cards/geocoq.html", target="_top", tooltip="Believe it because the Coq kernel checked it from Tarski's (or Hilbert's, or Euclid's) axioms — and GeoCoq proves those axiom systems interpret one another and hold in ℝ²."];
       sys_alphageometry [label="AlphaGeometry", fillcolor="#f6b26b", URL="../foundations/cards/alphageometry.html", target="_top", tooltip="Believe it because a deduction engine derived it from 43 assumed rules — with side conditions (non-collinear, same side) read off a random numeric diagram."];
       sys_newclid [label="Newclid", fillcolor="#f6b26b", URL="../foundations/cards/newclid.html", target="_top", tooltip="Believe it because the DDARN engine derived it from a curated rule set descended from AlphaGeometry — again with numerically checked side conditions."];
       sys_jgex [label="JGEX", fillcolor="#7fd1c7", URL="../foundations/cards/jgex.html", target="_top", tooltip="Believe it because the hypothesis polynomials reduce the conclusion to zero (Wu / Gröbner) — true generically, provided the printed non-degeneracy conditions hold."];
       sys_sympy [label="SymPy", fillcolor="#9cc3f0", URL="../foundations/cards/sympy.html", target="_top", tooltip="Believe it because exact arithmetic on concrete coordinates evaluates the predicate to True — subject to SymPy's simplification heuristics."];
       sys_geometor_model [label="geometor.model", fillcolor="#9cc3f0", URL="../foundations/cards/geometor_model.html", target="_top", tooltip="Believe it because the figure is built exactly — algebraic coordinates from ruler-and-compass intersections — and every asserted relation reduces to zero."];
       sys_kingdon [label="kingdon", fillcolor="#7fd1c7", URL="../foundations/cards/kingdon.html", target="_top", tooltip="Believe it because the identity expands to zero in the Clifford algebra — universally, when computed symbolically without division."];
       sys_galgebra [label="galgebra", fillcolor="#7fd1c7", URL="../foundations/cards/galgebra.html", target="_top", tooltip="Believe it because the multivector difference simplifies to zero for an arbitrary (possibly symbolic) metric — as far as SymPy's simplify can tell."];
       sys_cindyjs [label="CindyJS", fillcolor="#dcdcdc", URL="../foundations/cards/cindyjs.html", target="_top", tooltip="Believe it because it keeps looking true while you drag — floating-point projective geometry with randomized conjecture checks, and no proof."];
     }
     subgraph cluster_tcb { label="trusted components"; style=invis;
       tcb_reader [label="Human readers\n2,300 years", shape=cylinder, style=filled, fillcolor="#e8d9b5", tooltip="Proofs are checked by people; tacit diagram reasoning (order, continuity) is accepted without statement."];
       tcb_lean_kernel [label="Lean 4 kernel\n~8k lines C++ (estimate)", shape=cylinder, style=filled, fillcolor="#9fd8a8", tooltip="Type-checks dependent type theory terms; independent re-checkers exist (lean4lean, nanoda, lean4checker)."];
       tcb_smt_verif [label="SMT_VERIF oracle\nz3/cvc5 + hand-written E theory", shape=cylinder, style=filled, fillcolor="#f4d58d", tooltip="LeanEuclid SystemE/Meta/Smt/Solver.lean:44-54 — `axiom SMT_VERIF (P : Prop) : P` admits any goal the solver reports unsat; no proof reconstruction."];
       tcb_coq_kernel [label="Coq kernel\n~10-30k lines OCaml (estimate)", shape=cylinder, style=filled, fillcolor="#9fd8a8", tooltip="Checks CIC proof terms; GeoCoq's reflective tactics (ColR, CongR) also trust the VM conversion check."];
       tcb_ag_engine [label="AG DD+AR engine\n~9.7k lines Python", shape=cylinder, style=filled, fillcolor="#f6b26b", tooltip="Forward chaining over 43 rules plus Gaussian elimination over exact Fractions; premise selection uses float linprog."];
       tcb_newclid_engine [label="Newclid DDARN\n~15.4k lines Python (+~15k C++ Yuclid)", shape=cylinder, style=filled, fillcolor="#f6b26b", tooltip="Restructured AG loop; AR tables via sympy.solve; optional Yuclid C++ solver."];
       tcb_numeric_diagram [label="Numeric diagram\ntol 1e-12 (AG) · rel 1e-3 (Newclid)", shape=cylinder, style=filled, fillcolor="#dddddd", tooltip="ncoll / npara / nperp / sameside premises are decided numerically on a random float diagram, not deduced."];
       tcb_jgex_prover [label="JGEX gprover\n~38k lines Java", shape=cylinder, style=filled, fillcolor="#f6b26b", tooltip="GDD, full-angle, area, Wu characteristic sets, Gröbner bases over BigInteger polynomials."];
       tcb_sympy_cas [label="SymPy simplification\ncore heuristics + mpmath", shape=cylinder, style=filled, fillcolor="#9cc3f0", tooltip="simplify / expand / equals heuristics; sympy.geometry's affine_rank uses a 2-digit numeric zero test (point.py:333)."];
       tcb_model_zero_test [label="model zero_test\n~3.5k lines + SymPy", shape=cylinder, style=filled, fillcolor="#9cc3f0", tooltip="Tiered oracle (algebra.py:160-253): exact expansion, field arithmetic, minimal_polynomial — plus a numeric acceptance branch |evalf(80)| < 1e-65 for large expressions."];
       tcb_ga_codegen [label="GA product engines\nkingdon ~5.2k · galgebra ~9.5k lines", shape=cylinder, style=filled, fillcolor="#9cc3f0", tooltip="Clifford products expanded over SymPy; equality via expand/simplify (galgebra mv.py:479) or structural comparison (kingdon)."];
       tcb_ieee_float [label="IEEE-754 floats\neps 1e-10", shape=cylinder, style=filled, fillcolor="#dddddd", tooltip="All computation in double precision; CindyJS's prover keeps conjectures that survive 3 random perturbations."];
     }
     sys_euclid -> tcb_reader;
     sys_leaneuclid -> tcb_lean_kernel;
     sys_leaneuclid -> tcb_smt_verif;
     sys_mathlib4 -> tcb_lean_kernel;
     sys_geocoq -> tcb_coq_kernel;
     sys_alphageometry -> tcb_ag_engine;
     sys_alphageometry -> tcb_numeric_diagram;
     sys_newclid -> tcb_newclid_engine;
     sys_newclid -> tcb_sympy_cas;
     sys_newclid -> tcb_numeric_diagram;
     sys_jgex -> tcb_jgex_prover;
     sys_sympy -> tcb_sympy_cas;
     sys_geometor_model -> tcb_model_zero_test;
     sys_geometor_model -> tcb_sympy_cas;
     sys_kingdon -> tcb_ga_codegen;
     sys_kingdon -> tcb_sympy_cas;
     sys_galgebra -> tcb_ga_codegen;
     sys_galgebra -> tcb_sympy_cas;
     sys_cindyjs -> tcb_ieee_float;
   }

.. list-table::
   :header-rows: 1
   :widths: 18 9 18 18 37

   * - Component
     - Kind
     - Size
     - Trusted by
     - Note
   * - **Human readers**
     - human
     - 2,300 years
     - :doc:`Euclid <cards/euclid>`
     - Proofs are checked by people; tacit diagram reasoning (order, continuity) is accepted without statement.
   * - **Lean 4 kernel**
     - kernel
     - ~8k lines C++ (estimate)
     - :doc:`LeanEuclid <cards/leaneuclid>`, :doc:`mathlib4 <cards/mathlib4>`
     - Type-checks dependent type theory terms; independent re-checkers exist (lean4lean, nanoda, lean4checker).
   * - **SMT\_VERIF oracle**
     - solver
     - z3/cvc5 + hand-written E theory
     - :doc:`LeanEuclid <cards/leaneuclid>`
     - LeanEuclid SystemE/Meta/Smt/Solver.lean:44-54 — \`axiom SMT\_VERIF (P : Prop) : P\` admits any goal the solver reports unsat; no proof reconstruction.
   * - **Coq kernel**
     - kernel
     - ~10-30k lines OCaml (estimate)
     - :doc:`GeoCoq <cards/geocoq>`
     - Checks CIC proof terms; GeoCoq's reflective tactics (ColR, CongR) also trust the VM conversion check.
   * - **AG DD+AR engine**
     - engine
     - ~9.7k lines Python
     - :doc:`AlphaGeometry <cards/alphageometry>`
     - Forward chaining over 43 rules plus Gaussian elimination over exact Fractions; premise selection uses float linprog.
   * - **Newclid DDARN**
     - engine
     - ~15.4k lines Python (+~15k C++ Yuclid)
     - :doc:`Newclid <cards/newclid>`
     - Restructured AG loop; AR tables via sympy.solve; optional Yuclid C++ solver.
   * - **Numeric diagram**
     - float
     - tol 1e-12 (AG) · rel 1e-3 (Newclid)
     - :doc:`AlphaGeometry <cards/alphageometry>`, :doc:`Newclid <cards/newclid>`
     - ncoll / npara / nperp / sameside premises are decided numerically on a random float diagram, not deduced.
   * - **JGEX gprover**
     - engine
     - ~38k lines Java
     - :doc:`JGEX <cards/jgex>`
     - GDD, full-angle, area, Wu characteristic sets, Gröbner bases over BigInteger polynomials.
   * - **SymPy simplification**
     - cas
     - core heuristics + mpmath
     - :doc:`Newclid <cards/newclid>`, :doc:`SymPy <cards/sympy>`, :doc:`geometor.model <cards/geometor_model>`, :doc:`kingdon <cards/kingdon>`, :doc:`galgebra <cards/galgebra>`
     - simplify / expand / equals heuristics; sympy.geometry's affine\_rank uses a 2-digit numeric zero test (point.py:333).
   * - **model zero\_test**
     - cas
     - ~3.5k lines + SymPy
     - :doc:`geometor.model <cards/geometor_model>`
     - Tiered oracle (algebra.py:160-253): exact expansion, field arithmetic, minimal\_polynomial — plus a numeric acceptance branch \|evalf(80)\| < 1e-65 for large expressions.
   * - **GA product engines**
     - cas
     - kingdon ~5.2k · galgebra ~9.5k lines
     - :doc:`kingdon <cards/kingdon>`, :doc:`galgebra <cards/galgebra>`
     - Clifford products expanded over SymPy; equality via expand/simplify (galgebra mv.py:479) or structural comparison (kingdon).
   * - **IEEE-754 floats**
     - float
     - eps 1e-10
     - :doc:`CindyJS <cards/cindyjs>`
     - All computation in double precision; CindyJS's prover keeps conjectures that survive 3 random perturbations.

.. toctree::
   :maxdepth: 1

   cards/index
   compare
   connections
   findings
