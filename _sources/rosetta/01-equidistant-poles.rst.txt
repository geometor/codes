:order: 1

.. _rosetta-01-equidistant-poles:

=====================================================
Benchmark 1: Equidistant Poles & Equilateral Triangle
=====================================================

* **Canonical GEOMETOR Signature**: ``equidistant_poles(A, B) -> (F, E)``
* **Classical Citation**: *Euclid Book I, Proposition 1*
* **Core Phenomenon**: From two distinct seed points A and B, construct the two congruent circles (A, B) and (B, A) and select their intersection poles F and E to form equilateral triangle ABF. Tests whether a system can actually prove circle-circle intersection existence and select one of the two quadratic roots.

.. figure:: /_static/figures/01-seven-ontologies.svg
   :align: center
   :width: 100%

   Exact float-free ``geometor.model`` construction illustrating **Equidistant Poles & Equilateral Triangle** (``equidistant_poles(A, B) -> (F, E)``).

Cross-System Revelation Matrix
------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - System
     - What This Encoding Reveals
     - What This Encoding Hides
   * - **LeanEuclid & Formal System E**
     - Explicitly justifies why circles α and β must intersect via System E's diagrammatic circle-intersection axiom (filling Euclid's famous Book I.1 gap). Prop01.lean also proves proposition\_1' selecting the pole on a chosen side via intersect\_circles\_same\_side!
     - Delegates all interior/exterior circle-containment verification to external Z3/CVC5 via SMT\_VERIF, and yields no coordinates for c.
   * - **GeoCoq (Tarski / Hilbert / Euclid)**
     - Isolates the exact continuity axiom (circle\_circle, equivalent over Tarski neutral geometry to nested-circle continuity) required for I.1 to hold over Euclidean fields rather than Q^2.
     - In pure Tarski point-only files, circles do not exist as objects—circle\_circle is stated as a 6-point existential sentence on Bet and Cong.
   * - **Lean 4 Mathlib (Euclidean & Affine)**
     - Shows sharply that mathlib4 is an analytic deductive library over arbitrary dimension n (where two spheres in R^3 meet in a circle, not 2 points!), not a planar constructive system.
     - Cannot construct the two planar apexes without choosing an explicit 2D Orientation and invoking Orientation.rotation (π / 3).
   * - **AlphaGeometry (DD + AR)**
     - Compact 1-line locus intersection syntax; also exposes the silent ';' drop quirk in defs.txt:40 where the post-semicolon eqangle is ignored by Graph.add\_clause and re-proved by r13.
     - Cannot prove absolute angle π/3 (aconst a b a c 1 3) from circle intersections alone because AngleTable works modulo π without triangle interior-sum orientation!
   * - **Newclid & Yuclid**
     - Multi-goal ';' syntax after '?' verifies both side congruence and base-angle equality in a single run.
     - Which of the two poles c lands on depends on random float64 sampling inside the numerical sketcher.
   * - **Java Geometry Expert (JGEX / Area Method)**
     - Expresses the 60-degree cosine relation purely rationally via Pythagoras difference P\_CAB / P\_ABA = 1/2.
     - Root branch selection between upper and lower equilateral apexes.
   * - **Projective & Conformal Geometric Algebra (kingdon / galgebra)**
     - The circle-circle intersection is a single algebraic object—the grade-2 bivector point pair T = F ^ E—before splitting its two roots via idempotent projectors (T ± s)!
     - Requires lifting 2D plane into 4D Minkowski space R^{3,1} (since 2D PGA lacks circle blades).
   * - **CindyJS (Complex Projective CP^2 & Cayley-Klein)**
     - Maintains continuous identity of poles F and E under arbitrary dragging via Riemann-surface homotopy continuation.
     - Coordinates are complex floats (F = [1, 1.7320508..., 1]); requires PSLQ guess() to recover sqrt(3).
   * - **SymPy Geometry (sympy.geometry 1.14.0)**
     - Concise object-oriented syntax returning two exact symbolic Point2D instances over Q(sqrt(3)).
     - Calls generic Buchberger/CAS solve() under the hood (stalling on nested steps) and returns roots sorted arbitrarily without a half-plane selector.
   * - **Oliver Byrne's Coloured Euclid (1847 / Rougeux)**
     - Zero vertex letters! Every segment and circle is a direct coloured value-token whose equality follows visually from shared circle-radius membership.
     - Like classical Euclid, assumes visually that [red ○] and [blue ○] intersect without an explicit continuity axiom, and addresses the apex only as 'their intersection'.
   * - **GEOMETOR (geometor.model + Ecosystem)**
     - Combines closed-form radical-axis algebra (zero solve()), System E half-plane root selection side\_of=(a, b, ±1), exact Q(sqrt(3)) coordinates, and rational spread verification s = 3/4.
     - Currently 2D planar; selector AST should be persisted on Step for direct LeanEuclid export.

Side-by-Side Formal & Visual Implementations (11 Systems)
---------------------------------------------------------

LeanEuclid & Formal System E (``leaneuclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``LeanEuclid/Book/Prop01.lean:9-24``

.. code-block:: lean4

   theorem proposition_1 : ∀ (a b : Point) (AB : Line),
       distinctPointsOnLine a b AB →
       ∃ c : Point, |(a─c)| = |(a─b)| ∧ |(b─c)| = |(b─a)| ∧ ¬(c.onLine AB) := by
     euclid_intros
     euclid_apply (Circles.from_points a b) as α
     euclid_apply (Circles.from_points b a) as β
     euclid_apply (Intersections.intersect_circles α β) as c
     use c
     euclid_finish

* **Reveals**: Explicitly justifies why circles α and β must intersect via System E's diagrammatic circle-intersection axiom (filling Euclid's famous Book I.1 gap). Prop01.lean also proves proposition\_1' selecting the pole on a chosen side via intersect\_circles\_same\_side!
* **Hides**: Delegates all interior/exterior circle-containment verification to external Z3/CVC5 via SMT\_VERIF, and yields no coordinates for c.

GeoCoq (Tarski / Hilbert / Euclid) (``geocoq``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``GeoCoq/Elements/OriginalProofs/proposition_01.v:7-32``

.. code-block:: coq

   Theorem proposition_01 :
     forall A B, neq A B -> exists X, equilateral A B X /\ Triangle A B X.
   Proof.
     intros.
     pose proof (postulate_Euclid3 A B H) as [J HJ].
     pose proof (postulate_Euclid3 B A (neq_sym _ _ H)) as [K HK].
     ... (* applies postulate_circle_circle to obtain witness C *)

* **Reveals**: Isolates the exact continuity axiom (circle\_circle, equivalent over Tarski neutral geometry to nested-circle continuity) required for I.1 to hold over Euclidean fields rather than Q^2.
* **Hides**: In pure Tarski point-only files, circles do not exist as objects—circle\_circle is stated as a 6-point existential sentence on Bet and Cong.

Lean 4 Mathlib (Euclidean & Affine) (``mathlib4``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Absent constructively (cf. Geometry/Euclidean/Angle/Unoriented/Affine.lean)``

.. code-block:: lean4

   -- NO constructive Euclid I.1 existence theorem in Mathlib/Geometry/Euclidean/!
   -- Equilateral triangles appear only hypothetically as dist-equality assumptions:
   variable {V P : Type*} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
     [MetricSpace P] [NormedAddTorsor V P]
   -- Hypothesis form: dist a b = r ∧ dist b c = r ∧ dist c a = r

* **Reveals**: Shows sharply that mathlib4 is an analytic deductive library over arbitrary dimension n (where two spheres in R^3 meet in a circle, not 2 points!), not a planar constructive system.
* **Hides**: Cannot construct the two planar apexes without choosing an explicit 2D Orientation and invoking Orientation.rotation (π / 3).

AlphaGeometry (DD + AR) (``alphageometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``alphageometry/defs.txt:37-41 & rules.txt:14 (r13)``

.. code-block:: text

   # Primitive two-circle locus intersection + Pons Asinorum (r13):
   a b = segment a b; c = on_circle c a b, on_circle c b a ? eqangle a b a c b c b a

   # Or macro stanza in defs.txt:37-41:
   eq_triangle x a b
   x : a b
   a b = diff a b
   x : cong x a a b, cong x b a b; eqangle a b a x b x b a

* **Reveals**: Compact 1-line locus intersection syntax; also exposes the silent ';' drop quirk in defs.txt:40 where the post-semicolon eqangle is ignored by Graph.add\_clause and re-proved by r13.
* **Hides**: Cannot prove absolute angle π/3 (aconst a b a c 1 3) from circle intersections alone because AngleTable works modulo π without triangle interior-sum orientation!

Newclid & Yuclid (``newclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Newclid/newclid/src/newclid/jgex/constructions/``

.. code-block:: text

   a b = segment a b; c = on_circle c a b, on_circle c b a ? cong c a c b; eqangle a b a c b c b a

* **Reveals**: Multi-goal ';' syntax after '?' verifies both side congruence and base-angle equality in a single run.
* **Hides**: Which of the two poles c lands on depends on random float64 sampling inside the numerical sketcher.

Java Geometry Expert (JGEX / Area Method) (``jgex``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Java-Geometry-Expert Area Method / GDD``

.. code-block:: text

   EXAMPLE EUCLID_I_1
   HYPOTHESES:
     POINT A B;
     INTERSECTION_CC C A B B A;
   SHOW: EQANGLE C A B A B C.
   # Area/Pythagoras encoding: P_CAC = P_BAB, P_CBC = P_BAB => P_CAB = AB^2 = (1/2) P_ABA

* **Reveals**: Expresses the 60-degree cosine relation purely rationally via Pythagoras difference P\_CAB / P\_ABA = 1/2.
* **Hides**: Root branch selection between upper and lower equilateral apexes.

Projective & Conformal Geometric Algebra (kingdon / galgebra) (``pga_cga``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``2D CGA Cl(3,1) in kingdon (Algebra(3, 1))``

.. code-block:: python

   q_AB = -2 * (A | B)                        # exact quadrance |A - B|^2
   kA = A - sp.Rational(1, 2) * q_AB * ni     # dual circle centered at A through B
   kB = B - sp.Rational(1, 2) * q_AB * ni     # dual circle centered at B through A
   T = (kA ^ kB).dual()                       # OPNS grade-2 point pair F ^ E
   s = sp.sqrt((T * T).e)                     # invariant scalar separation
   F = norm_pt((T + s) * (T | ni))            # upper pole via projector split
   E = norm_pt((T - s) * (T | ni))            # lower pole via projector split

* **Reveals**: The circle-circle intersection is a single algebraic object—the grade-2 bivector point pair T = F ^ E—before splitting its two roots via idempotent projectors (T ± s)!
* **Hides**: Requires lifting 2D plane into 4D Minkowski space R^{3,1} (since 2D PGA lacks circle blades).

CindyJS (Complex Projective CP^2 & Cayley-Klein) (``cindyjs``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``CindyJS/src/js/libgeo/GeoOps.js:2038-2068 & Tracing.js``

.. code-block:: javascript

   create(["c1", "CircleMP", ["A", "B"]]);
   create(["c2", "CircleMP", ["B", "A"]]);
   create(["F", "E"], "IntersectCirCir", ["c1", "c2"]);
   // Subtracts monic 3x3 circle matrices to get radical axis, then splits rank-1 skew matrix;
   // Tracing.js tracks F and E continuously over C^3 when A or B is dragged!

* **Reveals**: Maintains continuous identity of poles F and E under arbitrary dragging via Riemann-surface homotopy continuation.
* **Hides**: Coordinates are complex floats (F = [1, 1.7320508..., 1]); requires PSLQ guess() to recover sqrt(3).

SymPy Geometry (sympy.geometry 1.14.0) (``sympy_geometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``sympy/geometry/ellipse.py:676-691``

.. code-block:: python

   r = A.distance(B)
   E, F = Circle(A, r).intersection(Circle(B, r))  # invokes generic CAS solve()!

* **Reveals**: Concise object-oriented syntax returning two exact symbolic Point2D instances over Q(sqrt(3)).
* **Hides**: Calls generic Buchberger/CAS solve() under the hood (stalling on nested steps) and returns roots sorted arbitrarily without a half-plane selector.

Oliver Byrne's Coloured Euclid (1847 / Rougeux) (``byrne_1847``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Byrne (1847) Book I, Prop. 1 / Rougeux c82.net/euclid/book1#prop1``

.. code-block:: text

   Given:        [black ━━]                       (seed segment)
   To Construct: △([black ━━], [red ━━], [yellow ━━]) equilateral
   Construction: Describe [red ○] about left end with radius [black ━━]   (Post. 3)
                 Describe [blue ○] about right end with radius [black ━━] (Post. 3)
                 From intersection draw [red ━━] and [yellow ━━]          (Post. 1)
   Proof:        [red ━━]    = [black ━━]   (radii of [red ○], Def. 15)
                 [yellow ━━] = [black ━━]   (radii of [blue ○], Def. 15)
               ∴ [red ━━] = [yellow ━━] = [black ━━]                      (Ax. 1)

* **Reveals**: Zero vertex letters! Every segment and circle is a direct coloured value-token whose equality follows visually from shared circle-radius membership.
* **Hides**: Like classical Euclid, assumes visually that [red ○] and [blue ○] intersect without an explicit continuity axiom, and addresses the apex only as 'their intersection'.

GEOMETOR (geometor.model + Ecosystem) (``geometor_model``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``geometor/codes/figures.py:100-115 (geometor.model)``

.. code-block:: python

   m = Model("equidistant_poles", auto_intersect=False)
   a = m.set_point(0, 0, ID="A"); b = m.set_point(2, 0, ID="B")
   c_a = m.construct_circle(a, b, ID="( A B )")
   c_b = m.construct_circle(b, a, ID="( B A )")
   f = m.intersect(c_a, c_b, side_of=(a, b, +1), ID="F")  # exact (1, sqrt(3))
   e = m.intersect(c_a, c_b, side_of=(a, b, -1), ID="E")  # exact (1, -sqrt(3))
   m.assert_equal((a, b), (a, f), (b, f), by="I.1")       # Q = 4, spread = 3/4

* **Reveals**: Combines closed-form radical-axis algebra (zero solve()), System E half-plane root selection side\_of=(a, b, ±1), exact Q(sqrt(3)) coordinates, and rational spread verification s = 3/4.
* **Hides**: Currently 2D planar; selector AST should be persisted on Step for direct LeanEuclid export.

