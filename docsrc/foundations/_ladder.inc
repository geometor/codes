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
     sys_cindyjs [label="CindyJS", fillcolor="#dcdcdc", penwidth=0.8, URL="foundations/cards/cindyjs.html", target="_top", tooltip="Believe it because it keeps looking true while you drag — floating-point projective geometry with randomized conjecture checks, and no proof."];
     lvl_L0 -> sys_cindyjs [style=invis];
     { rank=same; lvl_L1; sys_sympy sys_geometor_model }
     sys_sympy [label="SymPy", fillcolor="#9cc3f0", penwidth=0.8, URL="foundations/cards/sympy.html", target="_top", tooltip="Believe it because exact arithmetic on concrete coordinates evaluates the predicate to True — subject to SymPy's simplification heuristics."];
     lvl_L1 -> sys_sympy [style=invis];
     sys_geometor_model [label="geometor.model", fillcolor="#9cc3f0", penwidth=1.6, URL="foundations/cards/geometor_model.html", target="_top", tooltip="Believe it because the figure is built exactly — algebraic coordinates from ruler-and-compass intersections — and every asserted relation reduces to zero."];
     lvl_L1 -> sys_geometor_model [style=invis];
     { rank=same; lvl_L2; sys_jgex sys_kingdon sys_galgebra }
     sys_jgex [label="JGEX", fillcolor="#7fd1c7", penwidth=1.6, URL="foundations/cards/jgex.html", target="_top", tooltip="Believe it because the hypothesis polynomials reduce the conclusion to zero (Wu / Gröbner) — true generically, provided the printed non-degeneracy conditions hold."];
     lvl_L2 -> sys_jgex [style=invis];
     sys_kingdon [label="kingdon", fillcolor="#7fd1c7", penwidth=0.8, URL="foundations/cards/kingdon.html", target="_top", tooltip="Believe it because the identity expands to zero in the Clifford algebra — universally, when computed symbolically without division."];
     lvl_L2 -> sys_kingdon [style=invis];
     sys_galgebra [label="galgebra", fillcolor="#7fd1c7", penwidth=0.8, URL="foundations/cards/galgebra.html", target="_top", tooltip="Believe it because the multivector difference simplifies to zero for an arbitrary (possibly symbolic) metric — as far as SymPy's simplify can tell."];
     lvl_L2 -> sys_galgebra [style=invis];
     { rank=same; lvl_L3; sys_leaneuclid sys_alphageometry sys_newclid }
     sys_leaneuclid [label="LeanEuclid", fillcolor="#f6b26b", penwidth=1.6, URL="foundations/cards/leaneuclid.html", target="_top", tooltip="Believe it because Lean's kernel checked every rule application from System E's axioms — except that premise-discharging steps are admitted by an SMT oracle axiom."];
     lvl_L3 -> sys_leaneuclid [style=invis];
     sys_alphageometry [label="AlphaGeometry", fillcolor="#f6b26b", penwidth=1.6, URL="foundations/cards/alphageometry.html", target="_top", tooltip="Believe it because a deduction engine derived it from 43 assumed rules — with side conditions (non-collinear, same side) read off a random numeric diagram."];
     lvl_L3 -> sys_alphageometry [style=invis];
     sys_newclid [label="Newclid", fillcolor="#f6b26b", penwidth=0.8, URL="foundations/cards/newclid.html", target="_top", tooltip="Believe it because the DDARN engine derived it from a curated rule set descended from AlphaGeometry — again with numerically checked side conditions."];
     lvl_L3 -> sys_newclid [style=invis];
     { rank=same; lvl_L4; sys_geocoq }
     sys_geocoq [label="GeoCoq", fillcolor="#9fd8a8", penwidth=1.6, URL="foundations/cards/geocoq.html", target="_top", tooltip="Believe it because the Coq kernel checked it from Tarski's (or Hilbert's, or Euclid's) axioms — and GeoCoq proves those axiom systems interpret one another and hold in ℝ²."];
     lvl_L4 -> sys_geocoq [style=invis];
     { rank=same; lvl_L5; sys_mathlib4 }
     sys_mathlib4 [label="mathlib4", fillcolor="#c5b3e6", penwidth=1.6, URL="foundations/cards/mathlib4.html", target="_top", tooltip="Believe it because geometry is defined from real inner-product spaces and every theorem is a kernel-checked consequence of Lean's logic alone."];
     lvl_L5 -> sys_mathlib4 [style=invis];
     { rank=same; lvl_H; sys_euclid }
     sys_euclid [label="Euclid", fillcolor="#e8d9b5", penwidth=1.6, URL="foundations/cards/euclid.html", target="_top", tooltip="Believe it because it follows, step by step, from five postulates and five common notions — as checked by readers, with the diagram doing silent work."];
     lvl_H -> sys_euclid [style=invis];
     sys_geometor_model -> lvl_L2 [style=dashed, color="#3a7bd5", fontcolor="#3a7bd5", label="symbolic parameters", constraint=false];
     sys_geometor_model -> lvl_L5 [style=dashed, color="#3a7bd5", fontcolor="#3a7bd5", label="Lean certificate export", constraint=false];
     sys_leaneuclid -> lvl_L4 [style=dashed, color="#3a7bd5", fontcolor="#3a7bd5", label="SMT proof reconstruction", constraint=false];
     sys_alphageometry -> lvl_L5 [style=dashed, color="#3a7bd5", fontcolor="#3a7bd5", label="rules proved in mathlib", constraint=false];
   }
