.. role:: raw-html(raw)
   :format: html

.. _foundations-compare:

Side by Side
============

The same questions asked of every system. Systems are ordered from the strongest claim (top of the ladder) down. For an interactive version, use the Atlas on the :doc:`home page </index>`.

Comparison axes
---------------

.. list-table::
   :header-rows: 1
   :class: codes-compare

   * - System
     - Logic / calculus
     - Exact vs numeric
     - Decision procedure
     - Role of the diagram
     - Degeneracy handling
     - Trusted base (size)
   * - :raw-html:`<span class="codes-status" style="background:#e8d9b5">H</span>` :doc:`Euclid <cards/euclid>`
     - Informal deductive
     - Exact (no numbers)
     - None
     - Essential and tacit
     - Ignored
     - Human
   * - :raw-html:`<span class="codes-status" style="background:#c5b3e6">L5</span>` :doc:`mathlib4 <cards/mathlib4>`
     - Dependent type theory
     - Exact (real analysis)
     - Tactic search; kernel checks result
     - None
     - Junk values or explicit hypotheses
     - ~8k lines (kernel)
   * - :raw-html:`<span class="codes-status" style="background:#9fd8a8">L4</span>` :doc:`GeoCoq <cards/geocoq>`
     - Calculus of Inductive Constructions
     - Exact (synthetic)
     - Reflective Col/Cong deciders; nsatz
     - None (diagram facts are proved)
     - Explicit (~Col, A <> B); degenerate-tolerant Bet
     - ~10-30k lines (kernel)
   * - :raw-html:`<span class="codes-status" style="background:#f6b26b">L3</span>` :doc:`AlphaGeometry <cards/alphageometry>`
     - Horn-clause forward chaining
     - Exact algebra; numeric side conditions
     - Saturation over a finite rule set
     - Essential: decides side conditions
     - Numeric filters; no NDG output
     - ~9.7k lines Python
   * - :raw-html:`<span class="codes-status" style="background:#f6b26b">L3</span>` :doc:`LeanEuclid <cards/leaneuclid>`
     - Dependent type theory + axioms
     - Exact (symbolic)
     - SMT on the diagrammatic fragment (oracle)
     - Formalized: 36 diagrammatic + 23 transfer axioms
     - Explicit hypotheses (formTriangle, a ≠ b)
     - Lean kernel + SMT stack (unbounded)
   * - :raw-html:`<span class="codes-status" style="background:#f6b26b">L3</span>` :doc:`Newclid <cards/newclid>`
     - Horn-clause forward chaining
     - Exact algebra; numeric side conditions
     - Saturation over a finite rule set
     - Essential: every predicate checked numerically first
     - Numeric filters
     - ~15.4k lines Python (+15k C++)
   * - :raw-html:`<span class="codes-status" style="background:#7fd1c7">L2</span>` :doc:`JGEX <cards/jgex>`
     - Polynomial ideal membership
     - Exact (BigInteger polynomials)
     - Yes, for equational statements (generic truth)
     - Input and display only
     - Explicit NDG conditions
     - ~38k lines Java
   * - :raw-html:`<span class="codes-status" style="background:#7fd1c7">L2</span>` :doc:`galgebra <cards/galgebra>`
     - Algebraic identity
     - Exact symbolic
     - Heuristic (simplify)
     - None
     - Degenerate metrics unsupported in dual
     - ~9.5k lines + SymPy
   * - :raw-html:`<span class="codes-status" style="background:#7fd1c7">L2</span>` :doc:`kingdon <cards/kingdon>`
     - Algebraic identity
     - Exact symbolic or float
     - Polynomial expansion (no division)
     - None
     - Appears as zero / ideal elements
     - ~5.2k lines + SymPy
   * - :raw-html:`<span class="codes-status" style="background:#9cc3f0">L1</span>` :doc:`geometor.model <cards/geometor_model>`
     - Evaluation on an exact instance
     - Exact (one numeric acceptance branch)
     - Yes for constant algebraic expressions (minimal polynomial)
     - The figure is the proof object
     - Visible in the instance
     - ~3.5k lines + SymPy
   * - :raw-html:`<span class="codes-status" style="background:#9cc3f0">L1</span>` :doc:`SymPy <cards/sympy>`
     - Evaluation
     - Exact inputs; heuristic zero tests
     - Heuristic (simplify)
     - The object is the computation
     - Visible in the instance
     - ~12k lines + SymPy core
   * - :raw-html:`<span class="codes-status" style="background:#dcdcdc">L0</span>` :doc:`CindyJS <cards/cindyjs>`
     - None (numeric evidence)
     - Float
     - Probabilistic
     - The diagram is the system
     - Singularity heuristics in tracing
     - ~5.8k lines JS (float)

Layer by layer
--------------

Ontology — What exists?
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 18 82

   * - :doc:`Euclid <cards/euclid>`
     - Points, straight lines, circles, angles, and plane figures.
   * - :doc:`mathlib4 <cards/mathlib4>`
     - Real inner-product space V acting on a metric space P (NormedAddTorsor); AffineSubspace, Sphere, Affine.Simplex.
   * - :doc:`GeoCoq <cards/geocoq>`
     - Tarski: one sort of points with Bet (3-ary) and Cong (4-ary); Hilbert: points, lines, planes with incidence, order, congruence.
   * - :doc:`AlphaGeometry <cards/alphageometry>`
     - Named points with predicates (coll, para, perp, cong, eqangle, eqratio, cyclic, midp, simtri); hidden float coordinates.
   * - :doc:`LeanEuclid <cards/leaneuclid>`
     - Axiomatized sorts Point, Line, Circle (+ Segment, Angle, Triangle); opaque relations onLine, sameSide, between, onCircle; magnitudes in ℝ.
   * - :doc:`Newclid <cards/newclid>`
     - AG predicates plus metric ones (pythagoras, obtuse\_angle, sameclock).
   * - :doc:`JGEX <cards/jgex>`
     - Constructed points; hypotheses become polynomials with BigInteger coefficients.
   * - :doc:`galgebra <cards/galgebra>`
     - Multivectors over Ga with an arbitrary metric tensor and coordinates; geometric calculus operators.
   * - :doc:`kingdon <cards/kingdon>`
     - Multivectors of Cl(p, q, r): points, lines, circles as blades (PGA / CGA).
   * - :doc:`geometor.model <cards/geometor_model>`
     - Exact SymPy points, lines, circles, polygons in a construction DAG; coordinates in ℚ, ℚ(√d), ℚ(φ), radical towers.
   * - :doc:`SymPy <cards/sympy>`
     - Coordinate entities: Point, Line, Segment, Circle, Polygon over SymPy expressions.
   * - :doc:`CindyJS <cards/cindyjs>`
     - Homogeneous complex projective coordinates (ℂP²): points, lines, conics.

Language — How is a statement written?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 18 82

   * - :doc:`Euclid <cards/euclid>`
     - Greek prose enunciations: protasis, ekthesis, diorismos, construction, proof, conclusion.
   * - :doc:`mathlib4 <cards/mathlib4>`
     - Lean 4 propositions over P: dist p₁ p₂ = dist p₁ p₃ → ∠ p₁ p₂ p₃ = ∠ p₁ p₃ p₂.
   * - :doc:`GeoCoq <cards/geocoq>`
     - Coq propositions inside an axiom-class context: forall A B C, isosceles A B C -> CongA A B C A C B.
   * - :doc:`AlphaGeometry <cards/alphageometry>`
     - Construction clauses and a goal: a b c = triangle a b c; h = orthocenter h a b c; ? perp a h b c.
   * - :doc:`LeanEuclid <cards/leaneuclid>`
     - Lean 4 propositions in System E syntax: ∀ a b c : Point, formTriangle … → ∠ a:b:c = ∠ a:c:b.
   * - :doc:`Newclid <cards/newclid>`
     - JGEX/AG-style construction text wrapped in Python (JGEXFormulation.from\_text).
   * - :doc:`JGEX <cards/jgex>`
     - Text problems: POINT A B C O D … CIRCUMCENTER O A B C … SHOW: COLLINEAR P Q R.
   * - :doc:`galgebra <cards/galgebra>`
     - Python: o3d = Ga('e', g=[1, 1, 1], coords=symbols('x y z', real=True)).
   * - :doc:`kingdon <cards/kingdon>`
     - Python operators: alg = Algebra(3, 0, 1); b.cp(v); a ^ b; C >> P.
   * - :doc:`geometor.model <cards/geometor_model>`
     - Python construction + assertions: m.assert\_collinear(A, B, C, by="I.1").
   * - :doc:`SymPy <cards/sympy>`
     - Python predicates: Point.is\_collinear(A, B, C), Point.is\_concyclic(…).
   * - :doc:`CindyJS <cards/cindyjs>`
     - Declarative scene ({type: "Meet", args: ["a", "b"]}) or CindyScript: meet(join(A, B), …).

Assumptions — What is taken as given?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 18 82

   * - :doc:`Euclid <cards/euclid>`
     - 5 postulates, 5 common notions, 23 definitions (Book I).
   * - :doc:`mathlib4 <cards/mathlib4>`
     - None geometric: only Lean's logical axioms (propext, choice, Quot.sound); ℝ is constructed.
   * - :doc:`GeoCoq <cards/geocoq>`
     - Axiom classes: Tarski neutral (8) + dimension + Euclid + continuity options; Hilbert classes; Beeson's Euclid axioms.
   * - :doc:`AlphaGeometry <cards/alphageometry>`
     - 43 Horn rules (rules.txt) + ~71 construction definitions (defs.txt).
   * - :doc:`LeanEuclid <cards/leaneuclid>`
     - System E as 101 Lean axiom declarations (construction, diagrammatic, metric, transfer, superposition) + hand-written SMT theory.
   * - :doc:`Newclid <cards/newclid>`
     - 87 Rule objects; DEFAULT\_RULES = ALL − DEACTIVATED − TRIAGE (~58).
   * - :doc:`JGEX <cards/jgex>`
     - Field axioms over ℂ (Wu / Gröbner); GDD and full-angle rule sets for readable proofs.
   * - :doc:`galgebra <cards/galgebra>`
     - Clifford algebra axioms for the metric g.
   * - :doc:`kingdon <cards/kingdon>`
     - Clifford algebra axioms with a diagonal metric signature.
   * - :doc:`geometor.model <cards/geometor_model>`
     - Exact algebraic numbers; closed-form ruler-and-compass intersections.
   * - :doc:`SymPy <cards/sympy>`
     - Field arithmetic over exact SymPy numbers.
   * - :doc:`CindyJS <cards/cindyjs>`
     - IEEE-754 arithmetic (eps 1e-10, epsbig 1e-6).

Engine — How are new truths derived?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 18 82

   * - :doc:`Euclid <cards/euclid>`
     - Human deduction citing earlier propositions; constructions by ruler and compass.
   * - :doc:`mathlib4 <cards/mathlib4>`
     - Tactics (simp, linarith, nlinarith, field\_simp, linear\_combination) producing kernel terms.
   * - :doc:`GeoCoq <cards/geocoq>`
     - Ltac proofs; reflective deciders ColR / CongR (vm\_compute); nsatz (Gröbner) in coordinate chapters.
   * - :doc:`AlphaGeometry <cards/alphageometry>`
     - DD+AR: forward chaining to a fixpoint + Gaussian elimination over exact Fractions; LM proposes auxiliaries.
   * - :doc:`LeanEuclid <cards/leaneuclid>`
     - euclid\_apply (kernel-checked rule instance) with premises closed by euclid\_finish → z3/cvc5.
   * - :doc:`Newclid <cards/newclid>`
     - DDARN: rule matching + sympy.solve AR tables; optional Yuclid C++ solver.
   * - :doc:`JGEX <cards/jgex>`
     - Pseudo-division (Wu), Gröbner reduction, area-method elimination, forward chaining (GDD).
   * - :doc:`galgebra <cards/galgebra>`
     - Symbolic geometric products; equality by expand + simplify.
   * - :doc:`kingdon <cards/kingdon>`
     - Code-generated geometric products over symbolic or numeric coefficients.
   * - :doc:`geometor.model <cards/geometor_model>`
     - Exact construction + quadrance / spread / determinant identities reduced by zero\_test.
   * - :doc:`SymPy <cards/sympy>`
     - Expression evaluation; simplify / equals; rank with a numeric zero test.
   * - :doc:`CindyJS <cards/cindyjs>`
     - Numeric construction with complex tracing; randomized conjecture checking.

Certificate — What evidence is left behind?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 18 82

   * - :doc:`Euclid <cards/euclid>`
     - The written proof.
   * - :doc:`mathlib4 <cards/mathlib4>`
     - Lean proof term.
   * - :doc:`GeoCoq <cards/geocoq>`
     - Coq proof term (.vo).
   * - :doc:`AlphaGeometry <cards/alphageometry>`
     - Deduction trace naming the rule for each step.
   * - :doc:`LeanEuclid <cards/leaneuclid>`
     - Lean proof term with opaque SMT\_VERIF leaves.
   * - :doc:`Newclid <cards/newclid>`
     - Justification graph and written proof.
   * - :doc:`JGEX <cards/jgex>`
     - Remainder-zero chain + NDG list; readable proof trees for GDD / full-angle.
   * - :doc:`galgebra <cards/galgebra>`
     - An expression.
   * - :doc:`kingdon <cards/kingdon>`
     - An expression (zero or not).
   * - :doc:`geometor.model <cards/geometor_model>`
     - Step ledger of assertions (citations unchecked) and the exact figure.
   * - :doc:`SymPy <cards/sympy>`
     - A boolean.
   * - :doc:`CindyJS <cards/cindyjs>`
     - None.

Checker — What must be trusted?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 18 82

   * - :doc:`Euclid <cards/euclid>`
     - The reader.
   * - :doc:`mathlib4 <cards/mathlib4>`
     - Lean 4 kernel only.
   * - :doc:`GeoCoq <cards/geocoq>`
     - Coq kernel (+ VM conversion for reflective steps).
   * - :doc:`AlphaGeometry <cards/alphageometry>`
     - Python engine + rule soundness + numeric diagram (tol 1e-12).
   * - :doc:`LeanEuclid <cards/leaneuclid>`
     - Lean 4 kernel + SMT\_VERIF oracle (solver, translator, hand-written theory).
   * - :doc:`Newclid <cards/newclid>`
     - Python + SymPy + rule soundness + numeric checks (rel tol 1e-3).
   * - :doc:`JGEX <cards/jgex>`
     - JGEX Java prover (~38k lines).
   * - :doc:`galgebra <cards/galgebra>`
     - galgebra core + SymPy simplify.
   * - :doc:`kingdon <cards/kingdon>`
     - kingdon codegen + SymPy simplify.
   * - :doc:`geometor.model <cards/geometor_model>`
     - zero\_test (exact tiers + numeric acceptance branch) + SymPy.
   * - :doc:`SymPy <cards/sympy>`
     - SymPy simplification heuristics + mpmath.
   * - :doc:`CindyJS <cards/cindyjs>`
     - Floating-point arithmetic.

Semantics — What model makes it sound?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 18 82

   * - :doc:`Euclid <cards/euclid>`
     - Intended: the physical plane; modern reading: a Euclidean plane over a Euclidean field (Hilbert, Tarski).
   * - :doc:`mathlib4 <cards/mathlib4>`
     - By construction: any real inner-product affine space, including ℝⁿ.
   * - :doc:`GeoCoq <cards/geocoq>`
     - Formal models: Tarski ⇐ ℝⁿ over any real closed field; independence counter-models.
   * - :doc:`AlphaGeometry <cards/alphageometry>`
     - The real Euclidean plane, sampled as one random float diagram; directed angles mod π.
   * - :doc:`LeanEuclid <cards/leaneuclid>`
     - Avigad–Dean–Mumma: E is sound and complete for ruler-and-compass Euclidean planes (not formalized in LeanEuclid).
   * - :doc:`Newclid <cards/newclid>`
     - As AlphaGeometry: one float diagram of the real plane.
   * - :doc:`JGEX <cards/jgex>`
     - Generic truth over an algebraically closed field, conditional on NDGs.
   * - :doc:`galgebra <cards/galgebra>`
     - Geometric algebra over a symbolic metric.
   * - :doc:`kingdon <cards/kingdon>`
     - PGA / CGA models of the Euclidean plane or space.
   * - :doc:`geometor.model <cards/geometor_model>`
     - One exact figure in ℝ² over real algebraic numbers.
   * - :doc:`SymPy <cards/sympy>`
     - One concrete figure (or symbolic coordinates).
   * - :doc:`CindyJS <cards/cindyjs>`
     - Continuous configuration space over ℂP².
