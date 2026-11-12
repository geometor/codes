:navigation: header
:order: 20

.. _syntax-index:

===================================
Syntax Field Guide & Symbol Decoder
===================================

To a working geometer or Python engineer, opening a file in ``LeanEuclid``, ``GeoCoq``, ``mathlib4``, ``AlphaGeometry``, ``kingdon``, or :person:`Oliver Byrne <byrne>`'s 1847 *Coloured Euclid* can feel like reading cuneiform. Symbols like ``-ᵥ``, ``(2 : ℤ) • ∡``, ``|(a─b)|``, ``Bet``, ``FSC``, ``eqangle``, ``&``, ``>>``, and ``::`` compress entire philosophical commitments into two or three keystrokes.

This Field Guide decodes every strange symbol from first principles, pairs each syntactic family with an exact ``geometor.model`` ``.euclid-graphic`` diagram, and concludes with the complete **60-Symbol Master Decoder Reference**.

1. Pointer Dereferencing vs. Byrne's Chromatic Value-Tokens
-----------------------------------------------------------

The deepest syntactic divide in the history of geometry is **how prose refers to a geometric locus**:

* **Symbolic Pointer / Identifier Binding** (Euclid, ``LeanEuclid``, ``GeoCoq``, ``mathlib4``, ``AlphaGeometry``, ``geometor.model``): Points are bound to alphanumeric identifiers (``A``, ``B``, ``C``), and higher-dimensional objects are addressed indirectly as compound pointer expressions (``Segment(A, B)``, ``|(a─b)|``, ``∠ p₁ p₂ p₃``). This scales to arbitrary complexity and plain-text verification, but forces the human reader to perform constant *visual pointer-chasing* between prose text and diagram labels.
* **Pointer-Free Chromatic Value-Tokens** (:ref:`Byrne 1847 / Rougeux 2018 <system-byrne-1847>`): :person:`Oliver Byrne <byrne>` eliminated vertex letters across Books I–VI (:cite:`Byrne1847`), embedding miniature colored segments ``[━━]``, angle wedges ``[◣]``, squares ``[□]``, and circles ``[○]`` directly as *r-values* inside vertical ``Given`` / ``To Prove`` / ``Construction`` / ``Proof`` equations (with Oughtred's ``::`` proportion and Rahn's ``∴`` discharge). Similarly, 2D :term:`Projective Geometric Algebra` (``PGA``) manipulates whole line blades ``l1 ^ l2`` without referencing vertex coordinates.
* **GEOMETOR's Bidirectional Synthesis** (``:g:`` :math:`\leftrightarrow` ``data-ref``): Following :person:`Nicholas Rougeux <rougeux>`'s interactive web edition (:cite:`Rougeux2018`), GEOMETOR's ``:g:`` role (e.g., :g:`[ A B ]`, :g:`( A B )`, :g:`F`) retains exact symbolic identifiers while illuminating the matching SVG locus on hover—uniting unlimited symbolic arity with zero-dereference visual perception.

2. Dependent Type Binders & Logical Quantifiers (Lean 4 & Coq)
--------------------------------------------------------------

Interactive theorem provers (``LeanEuclid``, ``mathlib4``, ``GeoCoq``) use the **Curry–Howard correspondence**: a theorem is a *type*, and a proof is a *functional program* constructing an inhabitant of that type.

* **Explicit vs. Implicit vs. Typeclass Binders**:
  - ``(a b : Point)`` — **Explicit arguments** you pass by hand when applying a lemma.
  - ``{V P : Type*}`` — **Implicit arguments** inferred automatically by unification from later arguments.
  - ``[NormedAddTorsor V P]`` (Lean 4) or ``Context `{TnEQD : Tarski_neutral_dimensionless_with_decidable_point_equality}`` (Coq) — **Typeclass instances** synthesized automatically in the background to endow ``P`` with geometric structure.
* **Quantifiers & Connectives**: ``∀`` / ``forall`` introduces arbitrary givens; ``∃`` / ``exists`` demands an explicit constructive witness (unless bypassed via ``Classical.choose``); ``→`` / ``->`` chains hypotheses to conclusions; ``∧`` / ``/\`` bundles conjunctions; ``¬`` / ``~`` negates degeneracies such as ``¬ Col A B C``.

3. Diagrammatic System E & Topological Root Selectors
-----------------------------------------------------

When a line meets a circle or two circles meet, algebra yields a degree-2 quadratic equation with **two roots**. How does a formal language pick the right one without floating-point coordinates?

.. figure:: /_static/figures/02-topological-selectors.svg
   :align: center
   :width: 100%

   **Figure 2 — 1-to-1 Isomorphism Between System E Rules and ``geometor.model`` Selectors**: ``side_of=(A, B, +1)`` selects :g:`F` vs. :g:`E`; ``between=(A, B)`` selects midpoint :g:`M`; ``beyond=(A, B)`` and ``beyond=(B, A)`` select the exterior diameter extensions :g:`R2` and :g:`R1` on :g:`[ A B ]`.

In ``LeanEuclid`` (:cite:`AvigadDeanMumma2009`, :cite:`Murphy2024`), ``SystemE/Theory/Constructions/Intersections.lean`` provides seven constructive rules (``intersect_circles_same_side``, ``intersect_circles_opposing_sides``, ``intersect_line_circle_between``, ``intersect_line_circle_extending``), while linear metric terms are written ``|(a─b)|`` (length), ``∠(a:b:c)`` (angle), ``∟`` (right angle), and ``△(a:b:c)`` (area). ``geometor.model.intersect`` implements the exact algebraic counterparts via ``signed_area2`` and dot-product ordering—without ``LeanEuclid``'s unverified ``SMT_VERIF`` axiom!

4. Tarski's Point-Only Predicates (GeoCoq)
------------------------------------------

In :person:`Alfred Tarski <tarski>`'s minimalist language (:cite:`Schwabhauser1983`, :cite:`Boutry2019`), **lines, circles, and angles do not exist as types**. Every geometric statement is built from points (``Tpoint``) and two predicates:

* ``Bet A B C`` — *Non-strict* collinear betweenness (``Bet A A B`` is always true!). Collinearity ``Col A B C`` is simply ``Bet A B C \/ Bet B C A \/ Bet C A B``.
* ``Cong A B C D`` — Segment ``AB`` is congruent to ``CD``.
* ``Per A B C`` — Right angle ``∠ABC`` defined **without angles**: there exists ``C'`` such that ``B`` is the midpoint of ``C`` and ``C'`` and ``Cong A C A C'``!
* ``FSC`` — Tarski's angle-free :term:`Five-Segment Configuration` replacing Euclid's SAS (``I.4``).

.. figure:: /_static/figures/03-tarski-five-segment.svg
   :align: center
   :width: 100%

   **Figure 3 — Tarski's Point-Only World**: Non-strict ``Bet`` along :g:`[ A C ]`, angle-free right angle ``Per D B C`` via reflected witness :g:`C1`, and the ``FSC`` transmission of congruence to the fifth segment.

5. Affine Torsors, Directed Angles & Rational Spreads
-----------------------------------------------------

``mathlib4`` separates points ``P`` from vectors ``V`` via ``NormedAddTorsor V P``: subtracting two points ``p₁ -ᵥ p₂`` yields a vector in ``V``, while ``v +ᵥ p`` translates a point by a vector (note ``p₁ + p₂`` is a type error!). For angles, ``mathlib4`` distinguishes unoriented ``∠ p₁ p₂ p₃ ∈ [0, π]`` from oriented ``∡ x y z ∈ ℝ / 2πℤ``, using twice-angles ``(2 : ℤ) • ∡ x y z`` to represent **directed line angles modulo π**—the exact same group used by ``eqangle`` in ``AlphaGeometry``/``JGEX``! In ``geometor.model`` and ``geometor.wildberger``, both transcendental angles and square-root norms are replaced by rational :term:`quadrance` :math:`Q` and :term:`spread` :math:`s = \sin^2\theta`.

.. figure:: /_static/figures/04-torsor-oangle-spread.svg
   :align: center
   :width: 100%

   **Figure 4 — Torsor Subtraction, Directed Twice-Angles & Rational Spreads** on cyclic configuration :g:`A`, :g:`B`, :g:`C`, :g:`D` around circle :g:`( O A )`.

6. Olympiad Clause Stanzas & Coordinate-Free Area Elimination
-------------------------------------------------------------

``AlphaGeometry`` and ``Newclid`` read compact 1-line problem clauses (``premises ? goal``) backed by 5-line macro stanzas in ``defs.txt`` (``signature``, ``dependency``, ``non-degeneracy``, ``postconditions``, ``compass realization``). Watch out for two forensic traps we uncovered in ``alphageometry``: post-semicolon clauses without a ``x :`` prefix in ``defs.txt`` are **silently dropped** by ``Graph.add_clause``, and ``RatioTable.add_const_ratio`` in ``ar.py:425-431`` encodes :math:`m \log|s_1| = n \log|s_2|` instead of :math:`|s_1|/|s_2| = m/n`!

Meanwhile, ``JGEX``'s coordinate-free :term:`Area Method` eliminates constructed points backward from signed parallel ratios :math:`r`, signed areas :math:`S_{ABC}`, and :term:`Pythagoras difference` :math:`P_{ABC} = AB^2 + BC^2 - AC^2` using the **Co-Side Theorem**: :math:`PM / QM = S_{PAB} / S_{QAB}`.

.. figure:: /_static/figures/05-area-method-elimination.svg
   :align: center
   :width: 100%

   **Figure 5 — Coordinate-Free Area & Pythagoras Elimination**: Intersection :g:`M` of :g:`[ A B ]` and :g:`[ P Q ]` is eliminated linearly via signed area ratio :math:`S_{PAB} / S_{QAB}`, while foot :g:`H` is eliminated via Pythagoras ratio :math:`P_{PAB} / P_{ABA}`.

7. Clifford Blades (PGA/CGA) & Homogeneous CP^2 Matrices
--------------------------------------------------------

In ``kingdon``'s 2D :term:`Projective Geometric Algebra` (``Algebra(2, 0, 1)``), lines are grade-1 vectors, points are grade-2 bivectors, ``^`` is **meet**, and ``&`` is **join**. In 2D :term:`Conformal Geometric Algebra` (``Algebra(3, 1)``), points lift onto the 4D null cone :math:`P = x e_1 + y e_2 + \tfrac{1}{2}(x^2+y^2)n_\infty + n_o`, so ``P1 ^ P2 ^ P3`` is the circle through three points, ``-2*(kappa | P)`` is Steiner power, ``kappa1 - kappa2`` is the radical axis, and ``C >> P`` is circle inversion! *(Critical warning: in ``galgebra``, ``>>`` is the commutator product, ``&`` is missing, and ``.dual()`` crashes when :math:`I^2 = 0`!)* In ``CindyJS``'s :math:`\mathbb{CP}^2`, ``cross(u, v)`` computes both join and meet, ``C * p`` is the polar line, and ``adjoint3(C) * l`` is the pole.

.. figure:: /_static/figures/06-pga-cga-inversion.svg
   :align: center
   :width: 100%

   **Figure 6 — Conformal Circle Inversion & Pole–Polar Reciprocity**: External point :g:`P`, tangent touchpoints :g:`T1` and :g:`T2` on circle :g:`( O R0 )`, polar line :g:`[ T1 T2 ]`, inverse point :g:`P1` (``C >> P``), and harmonic range :math:`\operatorname{CR}(R_-, R_+; P_1, P) = -1`.

8. Master 60-Symbol Decoder Reference
-------------------------------------


Logic & Quantifiers
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 16 16 26 22 20
   :header-rows: 1

   * - Symbol / Token
     - Systems
     - Pronunciation & Plain Meaning
     - Formal Semantics & Example
     - GEOMETOR Equivalent
   * - ``∀``
     - ``leaneuclid``, ``mathlib4``, ``geocoq``
     - *for all* — Universal quantification: states that a geometric property holds for every choice of objects of the given types.
     - Dependent Pi-type binder Π (x : A), P x in Lean 4 / Coq; proof is a function mapping any witness x : A to a proof of P x. Example: ``∀ (a b : Point) (AB : Line), distinctPointsOnLine a b AB → ...``
     - Function parameters on @proposition def prop\_name(model: Model, a: Point, b: Point)
   * - ``∃``
     - ``leaneuclid``, ``mathlib4``, ``geocoq``
     - *there exists* — Existential quantification: asserts that a new geometric point, line, or circle can be constructed satisfying given conditions.
     - Inductive proposition Exists (λ x : A => P x) in Prop; eliminated via obtain / destruct / euclid\_apply to introduce a fresh witness. Example: ``∃ c : Point, |(a─c)| = |(a─b)| ∧ |(b─c)| = |(b─a)|``
     - Explicit witness returned by model.intersect(...) or model.construct\_line(...)
   * - ``→``
     - ``leaneuclid``, ``mathlib4``, ``geocoq``
     - *implies / maps to* — Logical implication ('if P then Q') or function arrow ('takes type A, returns type B'); right-associative.
     - Non-dependent special case of Π (\_ : P), Q under Curry-Howard propositions-as-types. Example: ``a ≠ b → Col A B C → Bet A B C ∨ Bet B C A ∨ Bet C A B``
     - Precondition guards in Given(...) -> assertions in Demonstrate(...)
   * - ``↔``
     - ``leaneuclid``, ``mathlib4``, ``geocoq``
     - *if and only if* — Logical equivalence: both directions P → Q and Q → P hold, allowing rewrite substitution.
     - Structure Iff P Q bundling mp : P → Q and mpr : Q → P; usable directly by rw / simp. Example: ``∠ p₁ p₂ p₃ = π / 2 ↔ dist p₁ p₃ ^ 2 = dist p₁ p₂ ^ 2 + dist p₃ p₂ ^ 2``
     - zero\_test(lhs - rhs) equivalence between algebraic invariants
   * - ``∧``
     - ``leaneuclid``, ``mathlib4``, ``geocoq``
     - *and* — Logical conjunction: both geometric conditions hold simultaneously.
     - Product structure And P Q with projections .left (.1) and .right (.2); unpacked in GeoCoq by spliter. Example: ``Bet A M B /\ Cong A M M B``
     - Sequential assertions model.assert\_equal(...); model.assert\_perpendicular(...)
   * - ``∨``
     - ``leaneuclid``, ``mathlib4``, ``geocoq``
     - *or* — Logical disjunction: at least one of two geometric configurations holds (e.g., case split on point order).
     - Sum inductive Or P Q with constructors Or.inl and Or.inr. Example: ``a.onLine L ∨ ¬(a.onLine L)``
     - Selector branch selection in model.intersect(..., side\_of=...)
   * - ``¬``
     - ``leaneuclid``, ``mathlib4``, ``geocoq``
     - *not* — Logical negation: states that a configuration is impossible (e.g., ~ Col A B C means non-collinear).
     - Defined constructively as P → False. Example: ``~ Col A B C -> exists X, Cong X A X B /\ Cong X B X C``
     - not zero\_test(signed\_area2(a, b, c)) non-degeneracy check
   * - ``≠``
     - ``leaneuclid``, ``mathlib4``, ``geocoq``
     - *not equal to* — Point or line distinctness precondition required to span a unique line or non-degenerate circle.
     - Shorthand for ¬(x = y), i.e. (x = y) → False (written x <> y in Coq). Example: ``(hne : p₁ ≠ p₂)``
     - quadrance(p1, p2) != 0 validated inside Model.construct\_line / construct\_circle

Type Theory & Binders
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 16 16 26 22 20
   :header-rows: 1

   * - Symbol / Token
     - Systems
     - Pronunciation & Plain Meaning
     - Formal Semantics & Example
     - GEOMETOR Equivalent
   * - ``{V : Type*}``
     - ``mathlib4``, ``leaneuclid``
     - *implicit universe-polymorphic type V* — Declares an ambient space type V that Lean infers automatically from later arguments without making the user pass V by hand.
     - Curly braces {...} mark an implicit Pi-binder solved by unification; Type\* expands to Sort (u + 1) for fresh universe u. Example: ``variable {V : Type*} {P : Type*}``
     - Python generic type annotations / ambient 2D SymPy coordinate domain
   * - ``[NormedAddTorsor V P]``
     - ``mathlib4``
     - *typeclass instance: P is a normed affine torsor over vector space V* — Equips points P with origin-free subtraction (producing a vector in V) and vector translation (producing a point in P) compatible with metric distance.
     - Square brackets [...] trigger Lean's backward typeclass synthesis for AddTorsor V P + dist\_eq\_norm\_vsub. Example: ``[NormedAddCommGroup V] [InnerProductSpace ℝ V] [MetricSpace P] [NormedAddTorsor V P]``
     - spg.Point2D affine arithmetic paired with geometor.model.invariants.quadrance
   * - ``QQ.algebraic_field``
     - ``geometor_model``
     - *exact rational algebraic number field Q(α)* — Represents nested radicals (such as golden ratio φ or √3) as canonical modulo-minimal-polynomial elements in Q[α]/(m(α)), reducing multi-step radical expressions to 0 deterministically.
     - SymPy Polys AlgebraicField constructed via sp.primitive\_element in geometor.model.algebra. Example: ``K = sp.QQ.algebraic_field(sp.GoldenRatio)``
     - Core canonicalizer inside geometor.model.algebra.zero\_test

System E Diagrammatic
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 16 16 26 22 20
   :header-rows: 1

   * - Symbol / Token
     - Systems
     - Pronunciation & Plain Meaning
     - Formal Semantics & Example
     - GEOMETOR Equivalent
   * - ``|(a─b)|``
     - ``leaneuclid``
     - *length of segment a b* — Real non-negative length assigned to the segment between points a and b in Formal System E.
     - Custom Lean 4 notation (Relations.lean) mapping Point × Point → ℝ with symmetry \|(a─b)\| = \|(b─a)\| and positivity \|(a─b)\| > 0 ↔ a ≠ b. Example: ``∃ c : Point, |(a─c)| = |(a─b)| ∧ |(b─c)| = |(b─a)|``
     - quadrance(a, b) (rational squared length) or spg.Segment(a, b).length
   * - ``∠(a:b:c)``
     - ``leaneuclid``
     - *measure of rectilinear angle a-b-c at vertex b* — Real measure of the interior angle formed by rays ba and bc, bounded between 0 and two RightAngles.
     - System E metric sort map Angle.ofPoints a b c : ℝ obeying diagrammatic ray-splitting additivity when d lies between a and c. Example: ``∠(a:b:c) + ∠(b:c:a) + ∠(c:a:b) = ∟ + ∟``
     - vertex\_spread(a, b, c) + vertex\_dot\_sign(a, b, c) in geometor.model
   * - ``△(a:b:c)``
     - ``leaneuclid``
     - *area of triangle a b c* — Unsigned real area of triangle abc in System E, additive under interior cevians and invariant under SAS congruence.
     - Function Triangle.area (Triangle.ofPoints a b c) : ℝ; equals 0 when a, b, c are collinear. Example: ``△(a:b:c) + △(a:c:d) = △(b:a:d) + △(b:d:c)``
     - abs(signed\_area2(a, b, c)) / 2 or model.assert\_area\_equal(poly1, poly2)
   * - ``∟``
     - ``leaneuclid``
     - *RightAngle* — Euclid's Postulate 4 unit of angular measure (all right angles are equal), avoiding transcendental π.
     - Positive real constant RightAngle : ℝ in SystemE/Theory/Relations.lean; straight angle equals ∟ + ∟. Example: ``∠(d:c:a) = ∟``
     - line\_spread(l1, l2) == 1 or model.assert\_perpendicular(l1, l2)
   * - ``Point.sameSide``
     - ``leaneuclid``
     - *points p and q lie on the same side of line L* — Topological half-plane relation: neither p nor q lies on L, and segment pq does not intersect L.
     - Primitive diagrammatic predicate Point.sameSide p q L : Prop governed by Pasch/plane-separation axioms. Example: ``p.sameSide q AB``
     - side\_of=(a, b, +1) selector in model.intersect(...)
   * - ``Point.opposingSides``
     - ``leaneuclid``
     - *points p and q lie on opposite sides of line L* — Topological separation: p and q lie off L and the open segment pq intersects L.
     - Defined in Relations.lean as ¬(p.onLine L) ∧ ¬(q.onLine L) ∧ ¬(p.sameSide q L). Example: ``c.opposingSides d AB``
     - side\_of=(a, b, -1) selector in model.intersect(...)

Topological Selectors
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 16 16 26 22 20
   :header-rows: 1

   * - Symbol / Token
     - Systems
     - Pronunciation & Plain Meaning
     - Formal Semantics & Example
     - GEOMETOR Equivalent
   * - ``between``
     - ``leaneuclid``, ``geometor_model``
     - *strictly between* — Strict collinear order: point b lies on line ac strictly inside open segment (a, c).
     - In LeanEuclid: strict ternary predicate between a b c (implies a ≠ b, b ≠ c, ¬between b a c). In geometor.model: intersect(..., between=(a, c)) selects root with 0 < t < 1. Example: ``m = model.intersect(l_ab, l_ef, between=(a, b), ID='M')``
     - model.intersect(e1, e2, between=(p1, p2))
   * - ``side_of``
     - ``geometor_model``
     - *exact algebraic topological root selector* — Selects a deterministic intersection point from a quadratic line-circle or circle-circle step using exact sign of oriented area (side\_of), dot-product order (between, beyond, on\_ray), or known-point exclusion (other\_than).
     - Evaluated in geometor.model.intersections.intersect (lines 382-620) without floating-point branch ambiguity. Example: ``f = m.intersect(c_a, c_b, side_of=(a, b, 1), ID='F')``
     - Native geometor.model.Model.intersect(..., side\_of=(p1, p2, +1))

Tactics & Solvers
~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 16 16 26 22 20
   :header-rows: 1

   * - Symbol / Token
     - Systems
     - Pronunciation & Plain Meaning
     - Formal Semantics & Example
     - GEOMETOR Equivalent
   * - ``euclid_apply``
     - ``leaneuclid``
     - *apply Euclidean construction or proposition rule* — Executes a compass-and-straightedge construction rule or prior proposition, introducing a fresh geometric object into context while discharging preconditions via SMT.
     - Lean 4 tactic macro in SystemE/Tactics/ translating context + negated precondition to SMT-LIB2 for Z3/CVC5. Example: ``euclid_apply (Intersections.intersect_circles α β) as c``
     - c = model.intersect(alpha, beta, side\_of=(a, b, 1))
   * - ``SMT_VERIF``
     - ``leaneuclid``
     - *unsound external SMT verification axiom* — Internal trust-oracle axiom used by LeanEuclid whenever external Z3/CVC5 reports 'unsat', closing the Lean goal without a kernel proof term.
     - axiom SMT\_VERIF (P : Prop) : P in SystemE/Meta/Smt/Solver.lean:44-55 (explicitly marked 'Dangerous!'). Example: ``private axiom SMT_VERIF (P : Prop) : P``
     - Avoided in GEOMETOR: algebraic identities are reduced symbolically via SymPy ANP fields
   * - ``ColR``
     - ``geocoq``
     - *certified Coq reflection tactic for collinearity / congruence* — Automatically proves collinearity or congruence goals by reifying context facts into an algebraic data structure inside Coq and running a verified decision procedure.
     - Kernel-checked computational reflection tactics in Meta\_theory/ / Tactics/Coinc/—zero external trust axioms! Example: ``intros; spliter; ColR.``
     - ExactDDARSolver / zero\_test(signed\_area2(...)) inside SymPy

Tarski Point-Only Axioms
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 16 16 26 22 20
   :header-rows: 1

   * - Symbol / Token
     - Systems
     - Pronunciation & Plain Meaning
     - Formal Semantics & Example
     - GEOMETOR Equivalent
   * - ``Bet``
     - ``geocoq``
     - *non-strict Tarski betweenness* — Point B lies on the closed line segment AC (allowing B = A or B = C!).
     - Primitive ternary relation Bet : Tpoint -> Tpoint -> Tpoint -> Prop in Tarski\_neutral\_dimensionless; Col A B C := Bet A B C \\/ Bet B C A \\/ Bet C A B. Example: ``assert (Bet A M B) by eBetween.``
     - zero\_test(signed\_area2(a, b, c)) and dot-product parameter 0 <= t <= 1
   * - ``Cong``
     - ``geocoq``, ``alphageometry``, ``newclid``
     - *four-point segment congruence* — The distance from A to B equals the distance from C to D, stated purely on four points without numbers or segment objects.
     - Primitive quaternary relation Cong : Tpoint -> Tpoint -> Tpoint -> Tpoint -> Prop (in AG/Newclid: cong A B C D). Example: ``Cong A B C D``
     - model.assert\_equal((a, b), (c, d))  # zero\_test(quadrance(a, b) - quadrance(c, d))
   * - ``FSC``
     - ``geocoq``
     - *Five-Segment Configuration* — Tarski's angle-free replacement for SAS triangle congruence: if collinear triples (A,B,C) and (A',B',C') have matching base segments and matching legs to apexes D, D', then the 5th segments CD and C'D' are congruent.
     - FSC A B C D A' B' C' D' := Col A B C /\\ Cong A B A' B' /\\ Cong B C B' C' /\\ Cong A D A' D' /\\ Cong B D B' D'. Example: ``Lemma l4_16 : FSC A B C D A' B' C' D' -> A <> B -> Cong C D C' D'.``
     - Stewart's / Triple-Quad polynomial determination of Q(C, D) from collinear base quadrances
   * - ``Per``
     - ``geocoq``
     - *Tarski right angle via midpoint reflection* — Angle ABC is a right angle iff reflecting C across B to C' makes A equidistant from C and C'—defining 90 degrees with zero angle primitives!
     - Definition Per A B C := exists C', Midpoint B C C' /\\ Cong A C A C' (Ch08\_orthogonality.v). Example: ``Per A B C <-> exists C', Midpoint B C C' /\ Cong A C A C'``
     - vertex\_spread(a, b, c) == 1 or model.assert\_perpendicular((a, b), (b, c), at=b)
   * - ``OS``
     - ``geocoq``
     - *one side / two sides of line AB* — TS A B P Q means segment PQ crosses line AB; OS A B P Q means P and Q lie on the same side because both lie opposite some witness R.
     - TS A B P Q := ~Col P A B /\\ ~Col Q A B /\\ exists T, Col T A B /\\ Bet P T Q; OS A B P Q := exists R, TS A B P R /\\ TS A B Q R. Example: ``OS A B P Q -> TS A B Q R -> TS A B P R``
     - sp.sign(signed\_area2(a, b, p) \* signed\_area2(a, b, q)) == +1 (OS) or -1 (TS)
   * - ``Par``
     - ``geocoq``
     - *coplanar parallel or coincident lines* — Par\_strict A B C D means coplanar lines AB and CD never meet; Par A B C D allows either strict parallelism or collinear coincidence.
     - Par A B C D := Par\_strict A B C D \\/ (A <> B /\\ C <> D /\\ Col A C D /\\ Col B C D) (Ch12\_parallel.v). Example: ``Par A B C D``
     - model.assert\_parallel(l1, l2)  # line\_spread(l1, l2) == 0
   * - ``Out``
     - ``geocoq``
     - *same open ray from vertex P* — Points A and B are distinct from P and lie on the same half-ray emanating from P (either Bet P A B or Bet P B A).
     - Out P A B := A <> P /\\ B <> P /\\ (Bet P A B \\/ Bet P B A) (Ch06\_out\_lines.v). Example: ``Out P A B``
     - on\_ray=(p, a) selector in model.intersect(...)

Affine Torsors & Angles
~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 16 16 26 22 20
   :header-rows: 1

   * - Symbol / Token
     - Systems
     - Pronunciation & Plain Meaning
     - Formal Semantics & Example
     - GEOMETOR Equivalent
   * - ``-ᵥ``
     - ``mathlib4``
     - *vector subtraction of two points* — Subtracts base point p₂ from target point p₁ to produce the displacement vector from p₂ to p₁ (note: you can subtract points, never add points!).
     - VSub.vsub : P → P → V; p₁ -ᵥ p₂ represents the vector v such that v +ᵥ p₂ = p₁. Example: ``dist p₁ p₂ = ‖p₁ -ᵥ p₂‖``
     - sp.Matrix([p1.x - p2.x, p1.y - p2.y])
   * - ``+ᵥ``
     - ``mathlib4``
     - *vector translation of a point* — Translates point p by displacement vector v to yield a new point in P.
     - VAdd.vadd : V → P → P satisfying 0 +ᵥ p = p and (v₁ + v₂) +ᵥ p = v₁ +ᵥ (v₂ +ᵥ p). Example: ``v +ᵥ p``
     - spg.Point2D(p.x + vx, p.y + vy)
   * - ``⟪x, y⟫``
     - ``mathlib4``
     - *real inner (dot) product of vectors x and y* — Measures orthogonal projection and cosine similarity between displacement vectors in V.
     - Scoped RealInnerProductSpace notation for inner ℝ x y : ℝ. Example: ``⟪p₁ -ᵥ p₂, p₃ -ᵥ p₂⟫ = 0``
     - (p1.x - p2.x)\*(p3.x - p2.x) + (p1.y - p2.y)\*(p3.y - p2.y)
   * - ``line[ℝ, p₁, p₂]``
     - ``mathlib4``
     - *affine span (line) over ℝ through p₁ and p₂* — The 1-dimensional affine subspace spanned by points p₁ and p₂ (degenerating to a singleton {p₁} if p₁ = p₂).
     - Notation for affineSpan ℝ ({p₁, p₂} : Set P) : AffineSubspace ℝ P. Example: ``p₃ ∈ line[ℝ, p₁, p₂]``
     - model.construct\_line(p1, p2)
   * - ``ᗮ``
     - ``mathlib4``
     - *orthogonal complement submodule* — Given a vector subspace (such as a line's direction), returns the subspace of all vectors perpendicular to it.
     - Submodule.orthogonal K : Submodule ℝ V; used with mk' p s.directionᗮ to build perpendicular affine subspaces of codimension k. Example: ``AffineSubspace.mk' p s.directionᗮ``
     - Normal direction (-b, a) of line ax + by + c = 0
   * - ``∠``
     - ``mathlib4``
     - *unoriented Euclidean angle in [0, π]* — Classical unoriented angle at middle vertex p₂ in any inner-product dimension; returns junk value π/2 if p₁ = p₂ or p₃ = p₂.
     - InnerProductGeometry.angle (p₁ -ᵥ p₂) (p₃ -ᵥ p₂) := Real.arccos (⟪u, v⟫ / (‖u‖ \* ‖v‖)) ∈ [0, π]. Example: ``∠ p₁ p₂ p₃ = π / 2``
     - vertex\_spread(p1, p2, p3) + vertex\_dot\_sign(p1, p2, p3) (avoids transcendental arccos!)
   * - ``∡``
     - ``mathlib4``
     - *oriented 2D angle modulo 2π* — Counterclockwise angle from ray yx to ray yz in ℝ/(2πℤ); multiplying by 2 gives (2 : ℤ) • ∡ x y z, encoding directed line angles modulo π!
     - Orientation.oangle (x -ᵥ y) (z -ᵥ y) : Real.Angle (= QuotientAddGroup.Quotient (2πℤ)). Example: ``cospherical {p₁, p₂, p₃, p₄} ↔ (2 : ℤ) • ∡ p₁ p₂ p₄ = (2 : ℤ) • ∡ p₁ p₃ p₄``
     - eqangle modulo π / rational spread + signed orientation
   * - ``Sphere.power``
     - ``mathlib4``
     - *power / pole / polar of an n-dimensional Euclidean sphere* — Clean n-dimensional sphere API: s.power p = dist(p, s.center)^2 - s.radius^2, enabling 1-line proofs of intersecting chords and La Hire's pole-polar reciprocity.
     - Defined in Mathlib/Geometry/Euclidean/Sphere/{Power,SecondInter,PolePolar}.lean over arbitrary InnerProductSpace ℝ V. Example: ``s.power p = dist p s.center ^ 2 - s.radius ^ 2``
     - quadrance(p, c) - r\_quad (planned geometor.model.inversion.circle\_power)

Clause DSL & AR
~~~~~~~~~~~~~~~

.. list-table::
   :widths: 16 16 26 22 20
   :header-rows: 1

   * - Symbol / Token
     - Systems
     - Pronunciation & Plain Meaning
     - Formal Semantics & Example
     - GEOMETOR Equivalent
   * - ``?``
     - ``alphageometry``, ``newclid``
     - *hypothesis-to-goal separator ('prove that')* — Splits the ordered construction clauses on the left from the target predicate goal(s) on the right.
     - Parsed by Problem.from\_txt (problem.py:138); Newclid extends RHS to semicolon-separated multi-goals. Example: ``a b c = triangle a b c; h = orthocenter h a b c ? perp a h b c``
     - Transition from Construct(...) to Demonstrate(...) inside @proposition
   * - ``;``
     - ``alphageometry``, ``newclid``
     - *sequential construction step separator* — Separates sequential point-introducing clauses in a problem string; also separates plevel groups in Line 4 of defs.txt (with a silent-drop bug in AG if unprefixed!).
     - Splits Problem premises into ordered Clause objects (problem.py:140). Example: ``a b = segment a b; c = on_circle c a b, on_circle c b a``
     - Sequential Python statements appending Step entries to Model.steps
   * - ``,``
     - ``alphageometry``, ``newclid``
     - *simultaneous two-locus intersection* — Inside a single clause x = locus1, locus2, constrains point x to lie on both loci simultaneously (computing their intersection while puncturing pre-existing points via HoleCircle).
     - Evaluated in numericals.py:1297-1323 (nm.reduce) and injected conjunctively into Graph.add\_clause. Example: ``h = on_tline h b a c, on_tline h c a b``
     - h = model.intersect(alt\_b, alt\_c, other\_than=...)
   * - `` | ``
     - ``newclid``, ``pga_cga``
     - *auxiliary construction separator (Newclid) / inner product (PGA/CGA)* — In Newclid problem strings, separates given base clauses from agent-proposed auxiliary constructions before '?'. (In kingdon/galgebra Python code, A \| B is the metric inner product.)
     - Parsed in newclid/jgex/formulation.py:92-100 into base clauses vs auxiliary\_clauses. Example: ``a b c = triangle; h = on_tline b a c, on_tline c a b | e = on_line a c, on_line b h ? perp a h b c``
     - with model.subconstruction('aux'): ... auxiliary witness introduction
   * - ``@x_y``
     - ``alphageometry``, ``newclid``
     - *pinned float64 sketch coordinate* — Hardcodes floating-point (x, y) coordinates onto a free point in imo\_ag\_30.txt so random numerical sketching lands in the intended acute/obtuse topological branch.
     - Parsed in Clause.from\_txt (alphageometry/problem.py:88-91) via float(x), float(y). Example: ``a@-0.2205_0.5441 b@-0.6323_-0.1691 c@0.2647_-0.1691 = triangle a b c``
     - Exact symbolic seed coordinates model.set\_point(sp.Rational(...), ...)
   * - ``eqangle``
     - ``alphageometry``, ``newclid``, ``jgex``
     - *8-point directed full-angle equality modulo π* — The counterclockwise angle required to rotate line AB onto line CD equals the angle from line EF to line GH modulo 180 degrees.
     - d(CD) - d(AB) ≡ d(GH) - d(EF) (mod π) in AngleTable (ar.py:591-656); unifies inscribed angles without case splits, at the cost of conflating internal and external angle bisectors! Example: ``eqangle P A P B Q A Q B``
     - model.assert\_spread\_equal(...) (spread s = sin^2 θ is also π-periodic!)
   * - ``eqratio``
     - ``alphageometry``, ``newclid``, ``jgex``
     - *8-point segment length ratio equality* — The ratio of segment lengths \|AB\| / \|CD\| equals \|EF\| / \|GH\|.
     - Encoded in RatioTable as log\|AB\| - log\|CD\| - log\|EF\| + log\|GH\| = 0 (ar.py:576-586). Example: ``eqratio P A P C P D P B``
     - zero\_test(quadrance(p, a) \* quadrance(p, b) - quadrance(p, c) \* quadrance(p, d))
   * - ``rconst``
     - ``alphageometry``, ``newclid``
     - *constant rational segment ratio (buggy in AlphaGeometry!)* — States \|AB\| / \|CD\| = m / n. In AlphaGeometry ar.py:570-574, buggy add\_eq2 adds m\*log\|AB\| - n\*log\|CD\| = 0 (\|AB\|^m = \|CD\|^n!); fixed in Newclid via sp.log(m) - sp.log(n).
     - Intended: l(AB) - l(CD) = log(m/n). AlphaGeometry bug: m\*l(AB) - n\*l(CD) = 0. Example: ``rconst m a a b 1 2``
     - zero\_test(quadrance(m, a) \* 4 - quadrance(a, b) \* 1)
   * - ``cyclic``
     - ``alphageometry``, ``newclid``, ``mathlib4``
     - *concyclic points (lie on a common circle)* — Four or more points lie on a single circle, without needing to construct the circle's center first.
     - Merges points onto a gm.Circle node (graph.py:1317); linked to eqangle via inscribed-angle rules r03/r04. Example: ``cyclic A B P Q``
     - 4x4 Cayley-Menger /lifting determinant det([x\_i, y\_i, x\_i^2+y\_i^2, 1]) == 0
   * - ``simtri2``
     - ``alphageometry``, ``newclid``
     - *orientation-reversing (reflected) triangle similarity* — simtri means ΔABC and ΔPQR are directly similar (same clockwise orientation); simtri2 (simtrir in Newclid) means oppositely/reflectedly similar.
     - Checked via sameclock guard and expanded into 3 eqangle + 3 eqratio relations with reversed angle signs for simtri2 (graph.py:2350-2381). Example: ``simtri2 H B A A B C``
     - Equal spreads + opposite sign of signed\_area2(a, b, c) \* signed\_area2(p, q, r)

Area-Method Invariants
~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 16 16 26 22 20
   :header-rows: 1

   * - Symbol / Token
     - Systems
     - Pronunciation & Plain Meaning
     - Formal Semantics & Example
     - GEOMETOR Equivalent
   * - ``S_ABC``
     - ``jgex``, ``geometor_model``
     - *Chou-Gao-Zhang signed area of triangle ABC* — Coordinate-free oriented area invariant: vanishes iff A, B, C are collinear; S\_ABCD = S\_ABC + S\_ACD vanishes iff AB \|\| CD; co-side ratio AB/CD = S\_PAB/S\_PCD eliminates intersections linearly!
     - Var.nm = 2 in JGEX Poly.java:1767 / Elim.trim\_a; obeys Chasles identity S\_ABC = S\_PBC + S\_APC + S\_ABP. Example: ``G(Y) = (S_UPQ * G(V) - S_VPQ * G(U)) / S_UPVQ``
     - geometor.model.invariants.signed\_area2(a, b, c)  # exact 2 \* S\_ABC
   * - ``P_ABC``
     - ``jgex``
     - *Pythagoras difference invariant* — Coordinate-free metric invariant P\_ABC = AB^2 + BC^2 - AC^2 (= 2 BA · BC) and 4-point P\_ABCD = AB^2 + CD^2 - BC^2 - DA^2 (= 2 AC · BD); vanishes iff perpendicular!
     - Var.nm = 3 in JGEX Poly.java:1796 / Elim.trim\_g; satisfies Jacobi identity P\_ACHB + P\_BAHC + P\_CBAH = 0 (0-step orthocenter proof!). Example: ``PERPENDICULAR A B B C <=> P_ABC = 0``
     - quadrance(a, b) + quadrance(b, c) - quadrance(a, c)

Clifford Blades & Versors
~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 16 16 26 22 20
   :header-rows: 1

   * - Symbol / Token
     - Systems
     - Pronunciation & Plain Meaning
     - Formal Semantics & Example
     - GEOMETOR Equivalent
   * - ``^``
     - ``pga_cga``
     - *outer (wedge) product* — Antisymmetric subspace spanning product: in plane-based 2D PGA it computes the MEET of two lines (l1 ^ l2 = point); in point-based 2D CGA it computes the JOIN (P1 ^ P2 ^ P3 = circle; P1 ^ P2 ^ ni = line)!
     - Grade-(k+l) part <A \* B>\_{k+l} of the geometric product (kingdon/operators.py:202, galgebra/mv.py:785). Example: ``C_circ = P1 ^ P2 ^ P3  # 2D CGA circle through 3 points``
     - model.intersect(l1, l2) (in PGA) or circumcircle / construct\_line (in CGA)
   * - ``&``
     - ``pga_cga``
     - *regressive (vee) product* — Dual subspace intersection/join product (A\* ^ B\*)^{-\*}: in plane-based 2D PGA, P1 & P2 JOINS two points into a line and (P1 & P2 & P3).e is their 3x3 collinearity determinant! (Missing in galgebra!)
     - Implemented in kingdon/operators.py:215-241 via Hodge dual of outer product. Example: ``l_ab = A & B; pappus_zero = (P & Q & R).e``
     - model.construct\_line(a, b) and signed\_area2(p, q, r)
   * - ``A | B``
     - ``pga_cga``
     - *metric inner product of blades* — Computes metric projections, orthogonality, quadrances, and circle power: in 2D PGA, (l \| P) is the line through P perpendicular to l; in 2D CGA, -2\*(P1 \| P2) is quadrance \|p1-p2\|^2 and -2\*(kappa \| P) is Steiner power!
     - Grade \|k - l\| projection <A \* B>\_{\|k-l\|} (kingdon/operators.py:146; warning: galgebra returns 0 on grade-0 scalars!). Example: ``l_bis = (A & B) | (A + B)  # 2D PGA perpendicular bisector``
     - quadrance(p1, p2) / perpendicular construction
   * - ``>>``
     - ``pga_cga``
     - *versor sandwich product (kingdon) — WARNING: commutator in galgebra!* — Applies any reflection, rotation, translation, or circle inversion uniformly to points, lines, or circles via ±V \* X \* ~V! (Critical trap: in galgebra, >> is 0.5\*(AB - BA) commutator, NOT sandwich!)
     - In kingdon (operators.py:96-121): (-1)^{k\*l} V \* X \* ~V for unit versor V\*~V = 1. Example: ``P_inv = norm_pt(C1.normalized() >> P)  # 2D CGA circle inversion!``
     - Unified reflection / rotation / circle inversion transformation
   * - ``~A``
     - ``pga_cga``
     - *multivector reversion* — Reverses the multiplication order of basis vectors in every blade (flipping signs of bivectors and trivectors); acts like Hermitian adjoint for rotors (R \* ~R = 1).
     - Flips sign by (-1)^{k(k-1)/2} on grade-k blades (kingdon/operators.py:446). Example: ``X3 = norm_pt(C_circ * ni * ~C_circ)  # 2D CGA circumcenter!``
     - Conjugate / inverse orientation in versor composition
   * - ``.dual()``
     - ``pga_cga``
     - *Poincaré / Hodge duality* — Converts between direct OPNS blades (where ^ is join) and dual IPNS blades (where ^ is meet): e.g., dualizing C = P1^P2^P3 gives grade-1 dual circle kappa = O - 0.5\*r^2\*ni. (Crashes in galgebra when I^2 = 0!)
     - kingdon auto-dispatches metric polarity x \* I^{-1} when r=0 (CGA) and right Hodge complement when r>=1 (PGA). Example: ``kappa = (P1 ^ P2 ^ P3).dual(); lam_rad = kappa1 - kappa2``
     - Point-line projective duality / monic circle vector
   * - ``e0, ni, no``
     - ``pga_cga``
     - *ideal line e0 (PGA) / conformal infinity ni & origin no (CGA)* — Null basis vectors (squaring to 0) that linearize translations and circles: in 2D PGA, e0 is the line at infinity; in 2D CGA, ni represents infinity and no the origin with no \| ni = -1.
     - e0^2 = 0 in Cl(2,0,1); ni = e\_- + e\_+, no = (e\_- - e\_+)/2 with ni^2 = no^2 = 0, no·ni = -1 in Cl(3,1). Example: ``up = lambda x, y: x*e1 + y*e2 + sp.Rational(1, 2)*(x**2 + y**2)*ni + no``
     - Homogeneous z=0 ideal locus / parabolic lifting x^2 + y^2

Homogeneous Projective CP^2
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 16 16 26 22 20
   :header-rows: 1

   * - Symbol / Token
     - Systems
     - Pronunciation & Plain Meaning
     - Formal Semantics & Example
     - GEOMETOR Equivalent
   * - ``cross(u, v)``
     - ``cindyjs``, ``geometor_model``
     - *3D homogeneous cross product (unified Join and Meet)* — In homogeneous coordinates [x, y, z], the 3D vector cross product u × v simultaneously computes the line joining two points AND the intersection point of two lines—including parallel lines meeting at z = 0!
     - Bilinear map CP^2 × CP^2 -> CP^2 in CindyJS GeoOps.js:156-202 (and geometor.pappus). Example: ``P = cross(cross(A1, B2), cross(A2, B1));``
     - sp.Matrix(u).cross(sp.Matrix(v)) in geometor.pappus
   * - ``adjoint3(C)``
     - ``cindyjs``
     - *3x3 cofactor adjugate (dual envelope conic)* — Given symmetric 3x3 point-conic matrix C (p^T C p = 0), C \* p is the polar line of p, adj(C) is the division-free dual tangent conic, and adj(C) \* l is the pole of line l!
     - List.adjoint3(C) = det(C) \* C^{-1} over complex homogeneous coordinates (List.js:1386-1501). Example: ``l_polar = C1 * p; p_pole = adjoint3(C1) * l;``
     - C.adjugate() over exact SymPy Matrix(3, 3, ...)
   * - ``I, J``
     - ``cindyjs``
     - *Cayley-Klein circular points at infinity (1, ±i, 0)* — Every Euclidean circle is simply a projective conic passing through I=(1, i, 0) and J=(1, -i, 0)! Perpendicularity is harmonic conjugacy wrt I, J, and Euclidean angle is (i/2) ln CR(A\_inf, B\_inf; I, J).
     - List.ii = [1, i, 0], List.jj = [1, -i, 0], List.fundDual = diag(1, 1, 0) in List.js:111-126. Example: ``geoOps._helper.ConicBy5(el, a, b, List.ii, List.jj, p);``
     - Algebraic unification of Euclidean metric and projective cross-ratio
   * - ``cross_ratio``
     - ``geometor_model``, ``cindyjs``, ``pga_cga``
     - *projective cross-ratio of four collinear points* — Fundamental projective invariant preserved under central projection; equals -1 when (A, B; C, D) form a harmonic range (such as internal/external bisector feet or circle diameter + pole/inverse).
     - Signed ratio (AC \* BD) / (BC \* AD) (or (AC \* BD) / (AD \* BC) depending on pairing convention—explicitly audited across model vs pappus!). Example: ``assert is_harmonic(r_neg, r_pos, p_inv, p)  # CR == -1``
     - Native geometor.model.cross\_ratio / is\_harmonic

Rational Trigonometry
~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 16 16 26 22 20
   :header-rows: 1

   * - Symbol / Token
     - Systems
     - Pronunciation & Plain Meaning
     - Formal Semantics & Example
     - GEOMETOR Equivalent
   * - ``quadrance``
     - ``geometor_model``
     - *Wildberger quadrance (squared separation)* — Exact polynomial squared distance (x2 - x1)^2 + (y2 - y1)^2 between two points, avoiding square roots so geometry stays inside the base number field.
     - Pure degree-2 polynomial invariant in geometor.model.invariants.quadrance / geometor.wildberger. Example: ``q_ab = quadrance(a, b)  # exact SymPy Rational or ANP element``
     - Native geometor.model.quadrance(p1, p2)
   * - ``spread``
     - ``geometor_model``
     - *Wildberger spread (rational squared sine between lines)* — Exact rational invariant s(l1, l2) ∈ [0, 1] measuring line separation (= sin^2 θ): 0 for parallel lines, 1/2 for 45°, 3/4 for 60°, and 1 for perpendicular lines—with zero inverse trig functions!
     - (a1\*b2 - a2\*b1)^2 / ((a1^2 + b1^2)\*(a2^2 + b2^2)) in geometor.model.invariants.line\_spread. Example: ``s = vertex_spread(b, a, f)  # sp.Rational(3, 4) for equilateral apex``
     - Native geometor.model.line\_spread / vertex\_spread

Visual Pseudocode & Binding
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 16 16 26 22 20
   :header-rows: 1

   * - Symbol / Token
     - Systems
     - Pronunciation & Plain Meaning
     - Formal Semantics & Example
     - GEOMETOR Equivalent
   * - ``[━━] / [◣]``
     - ``byrne_1847``
     - *Byrne inline coloured value-token (segment / wedge / polygon / circle)* — Replaces symbolic vertex-letter pointers ('AB', '∠ABC', '△ABC') with miniature coloured geometric shapes (red, blue, yellow, black) set inline inside algebraic-logical equations, eliminating visual pointer-chasing!
     - Direct value-token binding (Pickering 1847 woodblocks; encoded as inline <svg> components with shared class hover listeners in Rougeux's c82.net/euclid). Example: ``[red ━━] = [blue ━━],  [yellow ━━] = [blue ━━]  ∴  [red ━━] = [yellow ━━]``
     - Bidirectional :g:``[ A B ]`` <-> .euclid-graphic data-ref hover highlighting
   * - ``A : B :: C : D``
     - ``byrne_1847``
     - *as A is to B, so is C to D (Oughtred-Byrne four-term proportion)* — Four-term Eudoxian geometric proportion introduced by William Oughtred (1631) and used across Byrne Books V-VI with coloured ribbon/segment glyphs (including extreme & mean golden ratio [whole] : [blue] :: [blue] : [red]!).
     - Eudoxian equimultiple proportion Definition V.5 over geometric magnitudes. Example: ``[red+blue ━━] : [blue ━━] :: [blue ━━] : [red ━━]  (Euclid VI.30 / φ)``
     - eqratio / cross\_ratio / geometor.divine golden proportion chains
   * - ``∴``
     - ``byrne_1847``
     - *therefore (deductive step discharge)* — Introduces each derived equation line in Byrne's vertical Proof block, paired with marginal proposition/axiom citations such as (I.4) or (Ax. 1).
     - Modus ponens inference marker introduced by Johann Rahn (1659) and standardized as vertical proof pseudocode in Byrne (1847). Example: ``∴ [red ◣] + [blue ◣] = 2 [∟]  (I.13)``
     - model.assert\_\*(..., by='I.13') and conclude(...) in @proposition
   * - ``╌╌╌ / ┈┈┈``
     - ``byrne_1847``, ``geometor_model``
     - *auxiliary construction stroke discriminator (dashed / dotted)* — Visually separates auxiliary loci introduced in the Construction block (dashed/dotted lines) from Given premise loci (solid lines) while multiplying 4 primary colors into ~12 distinct visual tokens.
     - Typographic modality distinguishing premise vs existential witness loci. Example: ``Draw [red ╌╌╌] parallel to [black ━━]  (Byrne I.31 Construction)``
     - classes=['guide'] / guide=True and model.subconstruction(...)
   * - ``:g:`...```
     - ``geometor_model``
     - *GEOMETOR interactive symbolic-visual token role* — Synthesizes classical symbolic pointer precision (:g:``A``, :g:``[ A B ]``, :g:``( A B )``) with Byrne/Rougeux zero-dereference visual perception via live two-way CSS/DOM data-ref hover illumination on inline .euclid-graphic SVGs.
     - Sphinx role in photon\_platform.publish.roles.geometry emitting <span class='geometor-ref' data-ref='...'>. Example: ``Join poles :g:`F` and :g:`E` along bisector :g:`[ E F ]`.``
     - Native GEOMETOR / Digital Scriptorium standard
   * - ``@proposition``
     - ``geometor_model``, ``byrne_1847``
     - *structured Given / Construct / Demonstrate proposition block* — Formalizes Proclus's 6-part Euclidean anatomy and Byrne's 4-block typographic layout (Given -> To Prove -> Construction -> Proof) as executable, machine-verified Python proof traces.
     - Decorator in geometor.model.proof recording structured Step phases and algebraic assertions. Example: ``@proposition('I.1') / def equilateral_triangle(m: Model): ...``
     - Native geometor.model.proof.@proposition
