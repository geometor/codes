.. raw:: html

   <div class="codes-atlas" data-src="codes-atlas-data"></div>

.. raw:: html

   <script type="application/json" id="codes-atlas-data">
   {
   "layers": [
   {
   "key": "ontology",
   "label": "Ontology",
   "question": "What exists?"
   },
   {
   "key": "language",
   "label": "Language",
   "question": "How is a statement written?"
   },
   {
   "key": "assumptions",
   "label": "Assumptions",
   "question": "What is taken as given?"
   },
   {
   "key": "engine",
   "label": "Engine",
   "question": "How are new truths derived?"
   },
   {
   "key": "certificate",
   "label": "Certificate",
   "question": "What evidence is left behind?"
   },
   {
   "key": "checker",
   "label": "Checker",
   "question": "What must be trusted?"
   },
   {
   "key": "semantics",
   "label": "Semantics",
   "question": "What model makes it sound?"
   }
   ],
   "axes": [
   {
   "key": "logic",
   "label": "Logic / calculus"
   },
   {
   "key": "exactness",
   "label": "Exact vs numeric"
   },
   {
   "key": "decidable",
   "label": "Decision procedure"
   },
   {
   "key": "diagram",
   "label": "Role of the diagram"
   },
   {
   "key": "degeneracy",
   "label": "Degeneracy handling"
   },
   {
   "key": "tcb_size",
   "label": "Trusted base (size)"
   }
   ],
   "levels": [
   {
   "id": "L0",
   "name": "Plausible",
   "claim": "looks true numerically",
   "color": "#dcdcdc",
   "rank": 0
   },
   {
   "id": "L1",
   "name": "Instance",
   "claim": "true for this exact figure",
   "color": "#9cc3f0",
   "rank": 1
   },
   {
   "id": "L2",
   "name": "Generic",
   "claim": "true off a degenerate set (NDG)",
   "color": "#7fd1c7",
   "rank": 2
   },
   {
   "id": "L3",
   "name": "Rule-closed",
   "claim": "derivable from an assumed rule list",
   "color": "#f6b26b",
   "rank": 3
   },
   {
   "id": "L4",
   "name": "Axiom-checked",
   "claim": "kernel-checked from geometric axioms",
   "color": "#9fd8a8",
   "rank": 4
   },
   {
   "id": "L5",
   "name": "Foundational",
   "claim": "geometry derived; no geometric axioms",
   "color": "#c5b3e6",
   "rank": 5
   },
   {
   "id": "H",
   "name": "Human",
   "claim": "checked by readers from postulates",
   "color": "#e8d9b5",
   "rank": 6
   }
   ],
   "trusted": [
   {
   "id": "reader",
   "name": "Human readers",
   "kind": "human",
   "size": "2,300 years",
   "note": "Proofs are checked by people; tacit diagram reasoning (order, continuity) is accepted without statement."
   },
   {
   "id": "lean_kernel",
   "name": "Lean 4 kernel",
   "kind": "kernel",
   "size": "~8k lines C++ (estimate)",
   "note": "Type-checks dependent type theory terms; independent re-checkers exist (lean4lean, nanoda, lean4checker)."
   },
   {
   "id": "smt_verif",
   "name": "SMT_VERIF oracle",
   "kind": "solver",
   "size": "z3/cvc5 + hand-written E theory",
   "note": "LeanEuclid SystemE/Meta/Smt/Solver.lean:44-54 — `axiom SMT_VERIF (P : Prop) : P` admits any goal the solver reports unsat; no proof reconstruction."
   },
   {
   "id": "coq_kernel",
   "name": "Coq kernel",
   "kind": "kernel",
   "size": "~10-30k lines OCaml (estimate)",
   "note": "Checks CIC proof terms; GeoCoq's reflective tactics (ColR, CongR) also trust the VM conversion check."
   },
   {
   "id": "ag_engine",
   "name": "AG DD+AR engine",
   "kind": "engine",
   "size": "~9.7k lines Python",
   "note": "Forward chaining over 43 rules plus Gaussian elimination over exact Fractions; premise selection uses float linprog."
   },
   {
   "id": "newclid_engine",
   "name": "Newclid DDARN",
   "kind": "engine",
   "size": "~15.4k lines Python (+~15k C++ Yuclid)",
   "note": "Restructured AG loop; AR tables via sympy.solve; optional Yuclid C++ solver."
   },
   {
   "id": "numeric_diagram",
   "name": "Numeric diagram",
   "kind": "float",
   "size": "tol 1e-12 (AG) · rel 1e-3 (Newclid)",
   "note": "ncoll / npara / nperp / sameside premises are decided numerically on a random float diagram, not deduced."
   },
   {
   "id": "jgex_prover",
   "name": "JGEX gprover",
   "kind": "engine",
   "size": "~38k lines Java",
   "note": "GDD, full-angle, area, Wu characteristic sets, Gröbner bases over BigInteger polynomials."
   },
   {
   "id": "sympy_cas",
   "name": "SymPy simplification",
   "kind": "cas",
   "size": "core heuristics + mpmath",
   "note": "simplify / expand / equals heuristics; sympy.geometry's affine_rank uses a 2-digit numeric zero test (point.py:333)."
   },
   {
   "id": "model_zero_test",
   "name": "model zero_test",
   "kind": "cas",
   "size": "~3.5k lines + SymPy",
   "note": "Tiered oracle (algebra.py:160-253): exact expansion, field arithmetic, minimal_polynomial — plus a numeric acceptance branch |evalf(80)| < 1e-65 for large expressions."
   },
   {
   "id": "ga_codegen",
   "name": "GA product engines",
   "kind": "cas",
   "size": "kingdon ~5.2k · galgebra ~9.5k lines",
   "note": "Clifford products expanded over SymPy; equality via expand/simplify (galgebra mv.py:479) or structural comparison (kingdon)."
   },
   {
   "id": "ieee_float",
   "name": "IEEE-754 floats",
   "kind": "float",
   "size": "eps 1e-10",
   "note": "All computation in double precision; CindyJS's prover keeps conjectures that survive 3 random perturbations."
   }
   ],
   "systems": [
   {
   "id": "euclid",
   "name": "Euclid, Elements (Heath)",
   "short": "Euclid",
   "ladder": "H",
   "archetype": "synthetic-human",
   "core": true,
   "summary": "Believe it because it follows, step by step, from five postulates and five common notions — as checked by readers, with the diagram doing silent work.",
   "trusts": [
   "reader"
   ],
   "stack": {
   "ontology": "Points, straight lines, circles, angles, and plane figures.",
   "language": "Greek prose enunciations: protasis, ekthesis, diorismos, construction, proof, conclusion.",
   "assumptions": "5 postulates, 5 common notions, 23 definitions (Book I).",
   "engine": "Human deduction citing earlier propositions; constructions by ruler and compass.",
   "certificate": "The written proof.",
   "checker": "The reader.",
   "semantics": "Intended: the physical plane; modern reading: a Euclidean plane over a Euclidean field (Hilbert, Tarski)."
   },
   "axes": {
   "logic": "Informal deductive",
   "exactness": "Exact (no numbers)",
   "decidable": "None",
   "diagram": "Essential and tacit",
   "degeneracy": "Ignored",
   "tcb_size": "Human"
   },
   "example_lang": "text",
   "example_code": "I.5  In isosceles triangles the angles at the base are equal to one another, and, if\n     the equal straight lines be produced further, the angles under the base will be\n     equal to one another.",
   "card": "foundations/cards/euclid"
   },
   {
   "id": "leaneuclid",
   "name": "LeanEuclid (System E in Lean 4)",
   "short": "LeanEuclid",
   "ladder": "L3",
   "archetype": "synthetic-formal",
   "core": true,
   "summary": "Believe it because Lean's kernel checked every rule application from System E's axioms — except that premise-discharging steps are admitted by an SMT oracle axiom.",
   "trusts": [
   "lean_kernel",
   "smt_verif"
   ],
   "stack": {
   "ontology": "Axiomatized sorts Point, Line, Circle (+ Segment, Angle, Triangle); opaque relations onLine, sameSide, between, onCircle; magnitudes in ℝ.",
   "language": "Lean 4 propositions in System E syntax: ∀ a b c : Point, formTriangle … → ∠ a:b:c = ∠ a:c:b.",
   "assumptions": "System E as 101 Lean axiom declarations (construction, diagrammatic, metric, transfer, superposition) + hand-written SMT theory.",
   "engine": "euclid_apply (kernel-checked rule instance) with premises closed by euclid_finish → z3/cvc5.",
   "certificate": "Lean proof term with opaque SMT_VERIF leaves.",
   "checker": "Lean 4 kernel + SMT_VERIF oracle (solver, translator, hand-written theory).",
   "semantics": "Avigad–Dean–Mumma: E is sound and complete for ruler-and-compass Euclidean planes (not formalized in LeanEuclid)."
   },
   "axes": {
   "logic": "Dependent type theory + axioms",
   "exactness": "Exact (symbolic)",
   "decidable": "SMT on the diagrammatic fragment (oracle)",
   "diagram": "Formalized: 36 diagrammatic + 23 transfer axioms",
   "degeneracy": "Explicit hypotheses (formTriangle, a ≠ b)",
   "tcb_size": "Lean kernel + SMT stack (unbounded)"
   },
   "example_lang": "lean",
   "example_code": "theorem proposition_5 : ∀ (a b c d e : Point) (AB BC AC : Line),\n  formTriangle a b c AB BC AC ∧ (|(a─b)| = |(a─c)|) ∧\n  (between a b d) ∧ (between a c e) →\n  (∠ a:b:c = ∠ a:c:b) ∧ (∠ c:b:d = ∠ b:c:e) :=",
   "card": "foundations/cards/leaneuclid"
   },
   {
   "id": "mathlib4",
   "name": "mathlib4 Euclidean geometry",
   "short": "mathlib4",
   "ladder": "L5",
   "archetype": "analytic-formal",
   "core": true,
   "summary": "Believe it because geometry is defined from real inner-product spaces and every theorem is a kernel-checked consequence of Lean's logic alone.",
   "trusts": [
   "lean_kernel"
   ],
   "stack": {
   "ontology": "Real inner-product space V acting on a metric space P (NormedAddTorsor); AffineSubspace, Sphere, Affine.Simplex.",
   "language": "Lean 4 propositions over P: dist p₁ p₂ = dist p₁ p₃ → ∠ p₁ p₂ p₃ = ∠ p₁ p₃ p₂.",
   "assumptions": "None geometric: only Lean's logical axioms (propext, choice, Quot.sound); ℝ is constructed.",
   "engine": "Tactics (simp, linarith, nlinarith, field_simp, linear_combination) producing kernel terms.",
   "certificate": "Lean proof term.",
   "checker": "Lean 4 kernel only.",
   "semantics": "By construction: any real inner-product affine space, including ℝⁿ."
   },
   "axes": {
   "logic": "Dependent type theory",
   "exactness": "Exact (real analysis)",
   "decidable": "Tactic search; kernel checks result",
   "diagram": "None",
   "degeneracy": "Junk values or explicit hypotheses",
   "tcb_size": "~8k lines (kernel)"
   },
   "example_lang": "lean",
   "example_code": "/-- **Isosceles Triangle Theorem**: Pons asinorum, angle-at-point form. -/\ntheorem angle_eq_angle_of_dist_eq {p₁ p₂ p₃ : P} (h : dist p₁ p₂ = dist p₁ p₃) :\n    ∠ p₁ p₂ p₃ = ∠ p₁ p₃ p₂ := by",
   "card": "foundations/cards/mathlib4"
   },
   {
   "id": "geocoq",
   "name": "GeoCoq",
   "short": "GeoCoq",
   "ladder": "L4",
   "archetype": "synthetic-formal",
   "core": true,
   "summary": "Believe it because the Coq kernel checked it from Tarski's (or Hilbert's, or Euclid's) axioms — and GeoCoq proves those axiom systems interpret one another and hold in ℝ².",
   "trusts": [
   "coq_kernel"
   ],
   "stack": {
   "ontology": "Tarski: one sort of points with Bet (3-ary) and Cong (4-ary); Hilbert: points, lines, planes with incidence, order, congruence.",
   "language": "Coq propositions inside an axiom-class context: forall A B C, isosceles A B C -> CongA A B C A C B.",
   "assumptions": "Axiom classes: Tarski neutral (8) + dimension + Euclid + continuity options; Hilbert classes; Beeson's Euclid axioms.",
   "engine": "Ltac proofs; reflective deciders ColR / CongR (vm_compute); nsatz (Gröbner) in coordinate chapters.",
   "certificate": "Coq proof term (.vo).",
   "checker": "Coq kernel (+ VM conversion for reflective steps).",
   "semantics": "Formal models: Tarski ⇐ ℝⁿ over any real closed field; independence counter-models."
   },
   "axes": {
   "logic": "Calculus of Inductive Constructions",
   "exactness": "Exact (synthetic)",
   "decidable": "Reflective Col/Cong deciders; nsatz",
   "diagram": "None (diagram facts are proved)",
   "degeneracy": "Explicit (~Col, A <> B); degenerate-tolerant Bet",
   "tcb_size": "~10-30k lines (kernel)"
   },
   "example_lang": "coq",
   "example_code": "Lemma proposition_05 :\n   forall A B C,\n   isosceles A B C ->\n   CongA A B C A C B.",
   "card": "foundations/cards/geocoq"
   },
   {
   "id": "alphageometry",
   "name": "AlphaGeometry",
   "short": "AlphaGeometry",
   "ladder": "L3",
   "archetype": "rule-engine",
   "core": true,
   "summary": "Believe it because a deduction engine derived it from 43 assumed rules — with side conditions (non-collinear, same side) read off a random numeric diagram.",
   "trusts": [
   "ag_engine",
   "numeric_diagram"
   ],
   "stack": {
   "ontology": "Named points with predicates (coll, para, perp, cong, eqangle, eqratio, cyclic, midp, simtri); hidden float coordinates.",
   "language": "Construction clauses and a goal: a b c = triangle a b c; h = orthocenter h a b c; ? perp a h b c.",
   "assumptions": "43 Horn rules (rules.txt) + ~71 construction definitions (defs.txt).",
   "engine": "DD+AR: forward chaining to a fixpoint + Gaussian elimination over exact Fractions; LM proposes auxiliaries.",
   "certificate": "Deduction trace naming the rule for each step.",
   "checker": "Python engine + rule soundness + numeric diagram (tol 1e-12).",
   "semantics": "The real Euclidean plane, sampled as one random float diagram; directed angles mod π."
   },
   "axes": {
   "logic": "Horn-clause forward chaining",
   "exactness": "Exact algebra; numeric side conditions",
   "decidable": "Saturation over a finite rule set",
   "diagram": "Essential: decides side conditions",
   "degeneracy": "Numeric filters; no NDG output",
   "tcb_size": "~9.7k lines Python"
   },
   "example_lang": "text",
   "example_code": "cong O A O B, ncoll O A B => eqangle O A A B A B O B",
   "card": "foundations/cards/alphageometry"
   },
   {
   "id": "newclid",
   "name": "Newclid",
   "short": "Newclid",
   "ladder": "L3",
   "archetype": "rule-engine",
   "core": false,
   "summary": "Believe it because the DDARN engine derived it from a curated rule set descended from AlphaGeometry — again with numerically checked side conditions.",
   "trusts": [
   "newclid_engine",
   "sympy_cas",
   "numeric_diagram"
   ],
   "stack": {
   "ontology": "AG predicates plus metric ones (pythagoras, obtuse_angle, sameclock).",
   "language": "JGEX/AG-style construction text wrapped in Python (JGEXFormulation.from_text).",
   "assumptions": "87 Rule objects; DEFAULT_RULES = ALL − DEACTIVATED − TRIAGE (~58).",
   "engine": "DDARN: rule matching + sympy.solve AR tables; optional Yuclid C++ solver.",
   "certificate": "Justification graph and written proof.",
   "checker": "Python + SymPy + rule soundness + numeric checks (rel tol 1e-3).",
   "semantics": "As AlphaGeometry: one float diagram of the real plane."
   },
   "axes": {
   "logic": "Horn-clause forward chaining",
   "exactness": "Exact algebra; numeric side conditions",
   "decidable": "Saturation over a finite rule set",
   "diagram": "Essential: every predicate checked numerically first",
   "degeneracy": "Numeric filters",
   "tcb_size": "~15.4k lines Python (+15k C++)"
   },
   "example_lang": "python",
   "example_code": "R45_SIMSONS_LINE_THEOREM = Rule(\n    id=\"r45\",\n    premises_txt=(\"cyclic A B C P\", \"coll A L C\", \"perp P L A C\",\n                  \"coll M B C\", \"perp P M B C\", \"coll N A B\", \"perp P N A B\"),\n    conclusions_txt=(\"coll L M N\",),\n)",
   "card": "foundations/cards/newclid"
   },
   {
   "id": "jgex",
   "name": "Java Geometry Expert (JGEX)",
   "short": "JGEX",
   "ladder": "L2",
   "archetype": "algebraic-decision",
   "core": true,
   "summary": "Believe it because the hypothesis polynomials reduce the conclusion to zero (Wu / Gröbner) — true generically, provided the printed non-degeneracy conditions hold.",
   "trusts": [
   "jgex_prover"
   ],
   "stack": {
   "ontology": "Constructed points; hypotheses become polynomials with BigInteger coefficients.",
   "language": "Text problems: POINT A B C O D … CIRCUMCENTER O A B C … SHOW: COLLINEAR P Q R.",
   "assumptions": "Field axioms over ℂ (Wu / Gröbner); GDD and full-angle rule sets for readable proofs.",
   "engine": "Pseudo-division (Wu), Gröbner reduction, area-method elimination, forward chaining (GDD).",
   "certificate": "Remainder-zero chain + NDG list; readable proof trees for GDD / full-angle.",
   "checker": "JGEX Java prover (~38k lines).",
   "semantics": "Generic truth over an algebraically closed field, conditional on NDGs."
   },
   "axes": {
   "logic": "Polynomial ideal membership",
   "exactness": "Exact (BigInteger polynomials)",
   "decidable": "Yes, for equational statements (generic truth)",
   "diagram": "Input and display only",
   "degeneracy": "Explicit NDG conditions",
   "tcb_size": "~38k lines Java"
   },
   "example_lang": "text",
   "example_code": "POINT A B C O D R P Q\nCIRCUMCENTER O A B C\nON_CIRCLE D O A\nFOOT R D A B ...\nSHOW: COLLINEAR P Q R",
   "card": "foundations/cards/jgex"
   },
   {
   "id": "sympy",
   "name": "SymPy geometry",
   "short": "SymPy",
   "ladder": "L1",
   "archetype": "analytic-cas",
   "core": false,
   "summary": "Believe it because exact arithmetic on concrete coordinates evaluates the predicate to True — subject to SymPy's simplification heuristics.",
   "trusts": [
   "sympy_cas"
   ],
   "stack": {
   "ontology": "Coordinate entities: Point, Line, Segment, Circle, Polygon over SymPy expressions.",
   "language": "Python predicates: Point.is_collinear(A, B, C), Point.is_concyclic(…).",
   "assumptions": "Field arithmetic over exact SymPy numbers.",
   "engine": "Expression evaluation; simplify / equals; rank with a numeric zero test.",
   "certificate": "A boolean.",
   "checker": "SymPy simplification heuristics + mpmath.",
   "semantics": "One concrete figure (or symbolic coordinates)."
   },
   "axes": {
   "logic": "Evaluation",
   "exactness": "Exact inputs; heuristic zero tests",
   "decidable": "Heuristic (simplify)",
   "diagram": "The object is the computation",
   "degeneracy": "Visible in the instance",
   "tcb_size": "~12k lines + SymPy core"
   },
   "example_lang": "python",
   "example_code": "from sympy import Point\nPoint.is_collinear(Point(0, 0), Point(1, 1), Point(2, 2))   # True",
   "card": "foundations/cards/sympy"
   },
   {
   "id": "geometor_model",
   "name": "geometor.model",
   "short": "geometor.model",
   "ladder": "L1",
   "archetype": "analytic-cas",
   "core": true,
   "summary": "Believe it because the figure is built exactly — algebraic coordinates from ruler-and-compass intersections — and every asserted relation reduces to zero.",
   "trusts": [
   "model_zero_test",
   "sympy_cas"
   ],
   "stack": {
   "ontology": "Exact SymPy points, lines, circles, polygons in a construction DAG; coordinates in ℚ, ℚ(√d), ℚ(φ), radical towers.",
   "language": "Python construction + assertions: m.assert_collinear(A, B, C, by=\"I.1\").",
   "assumptions": "Exact algebraic numbers; closed-form ruler-and-compass intersections.",
   "engine": "Exact construction + quadrance / spread / determinant identities reduced by zero_test.",
   "certificate": "Step ledger of assertions (citations unchecked) and the exact figure.",
   "checker": "zero_test (exact tiers + numeric acceptance branch) + SymPy.",
   "semantics": "One exact figure in ℝ² over real algebraic numbers."
   },
   "axes": {
   "logic": "Evaluation on an exact instance",
   "exactness": "Exact (one numeric acceptance branch)",
   "decidable": "Yes for constant algebraic expressions (minimal polynomial)",
   "diagram": "The figure is the proof object",
   "degeneracy": "Visible in the instance",
   "tcb_size": "~3.5k lines + SymPy"
   },
   "example_lang": "python",
   "example_code": "m = Model(\"I.5\", auto_intersect=False)\nA, B, C = m.set_point(2, 3), m.set_point(0, 0), m.set_point(4, 0)\nm.assert_equal((A, B), (A, C), by=\"Given\")\nm.assert_spread_equal((A, B, C), (A, C, B), by=\"I.5\")",
   "card": "foundations/cards/geometor_model"
   },
   {
   "id": "kingdon",
   "name": "kingdon (geometric algebra)",
   "short": "kingdon",
   "ladder": "L2",
   "archetype": "geometric-algebra",
   "core": false,
   "summary": "Believe it because the identity expands to zero in the Clifford algebra — universally, when computed symbolically without division.",
   "trusts": [
   "ga_codegen",
   "sympy_cas"
   ],
   "stack": {
   "ontology": "Multivectors of Cl(p, q, r): points, lines, circles as blades (PGA / CGA).",
   "language": "Python operators: alg = Algebra(3, 0, 1); b.cp(v); a ^ b; C >> P.",
   "assumptions": "Clifford algebra axioms with a diagonal metric signature.",
   "engine": "Code-generated geometric products over symbolic or numeric coefficients.",
   "certificate": "An expression (zero or not).",
   "checker": "kingdon codegen + SymPy simplify.",
   "semantics": "PGA / CGA models of the Euclidean plane or space."
   },
   "axes": {
   "logic": "Algebraic identity",
   "exactness": "Exact symbolic or float",
   "decidable": "Polynomial expansion (no division)",
   "diagram": "None",
   "degeneracy": "Appears as zero / ideal elements",
   "tcb_size": "~5.2k lines + SymPy"
   },
   "example_lang": "python",
   "example_code": "alg = Algebra(3, 0, 1)\nb = alg.bivector(name='b'); v = alg.vector(name='v')\nb.cp(v)",
   "card": "foundations/cards/kingdon"
   },
   {
   "id": "galgebra",
   "name": "galgebra (geometric algebra)",
   "short": "galgebra",
   "ladder": "L2",
   "archetype": "geometric-algebra",
   "core": false,
   "summary": "Believe it because the multivector difference simplifies to zero for an arbitrary (possibly symbolic) metric — as far as SymPy's simplify can tell.",
   "trusts": [
   "ga_codegen",
   "sympy_cas"
   ],
   "stack": {
   "ontology": "Multivectors over Ga with an arbitrary metric tensor and coordinates; geometric calculus operators.",
   "language": "Python: o3d = Ga('e', g=[1, 1, 1], coords=symbols('x y z', real=True)).",
   "assumptions": "Clifford algebra axioms for the metric g.",
   "engine": "Symbolic geometric products; equality by expand + simplify.",
   "certificate": "An expression.",
   "checker": "galgebra core + SymPy simplify.",
   "semantics": "Geometric algebra over a symbolic metric."
   },
   "axes": {
   "logic": "Algebraic identity",
   "exactness": "Exact symbolic",
   "decidable": "Heuristic (simplify)",
   "diagram": "None",
   "degeneracy": "Degenerate metrics unsupported in dual",
   "tcb_size": "~9.5k lines + SymPy"
   },
   "example_lang": "python",
   "example_code": "o3d = Ga('e', g=[1, 1, 1], coords=symbols('x,y,z', real=True))",
   "card": "foundations/cards/galgebra"
   },
   {
   "id": "cindyjs",
   "name": "CindyJS",
   "short": "CindyJS",
   "ladder": "L0",
   "archetype": "numeric-interactive",
   "core": false,
   "summary": "Believe it because it keeps looking true while you drag — floating-point projective geometry with randomized conjecture checks, and no proof.",
   "trusts": [
   "ieee_float"
   ],
   "stack": {
   "ontology": "Homogeneous complex projective coordinates (ℂP²): points, lines, conics.",
   "language": "Declarative scene ({type: \"Meet\", args: [\"a\", \"b\"]}) or CindyScript: meet(join(A, B), …).",
   "assumptions": "IEEE-754 arithmetic (eps 1e-10, epsbig 1e-6).",
   "engine": "Numeric construction with complex tracing; randomized conjecture checking.",
   "certificate": "None.",
   "checker": "Floating-point arithmetic.",
   "semantics": "Continuous configuration space over ℂP²."
   },
   "axes": {
   "logic": "None (numeric evidence)",
   "exactness": "Float",
   "decidable": "Probabilistic",
   "diagram": "The diagram is the system",
   "degeneracy": "Singularity heuristics in tracing",
   "tcb_size": "~5.8k lines JS (float)"
   },
   "example_lang": "javascript",
   "example_code": "{ name: \"D\", type: \"Meet\", args: [\"a\", \"b\"] }",
   "card": "foundations/cards/cindyjs"
   }
   ]
   }
   </script>
