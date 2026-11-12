:order: 2

.. _rosetta-02-perpendicular-bisector-midpoint:

==============================================
Benchmark 2: Perpendicular Bisector & Midpoint
==============================================

* **Canonical GEOMETOR Signature**: ``perpendicular_bisector(A, B) -> (bisector, midpoint)``
* **Classical Citation**: *Euclid Book I, Propositions 10 & 11*
* **Core Phenomenon**: Join the two equidistant vesica poles F and E of (A, B) and (B, A) to obtain the perpendicular bisector [E F] and intersect with [A B] to obtain the midpoint M. Contrasts synthetic kite/congruence proofs against 1-subtraction conformal duals.

.. figure:: /_static/figures/02-topological-selectors.svg
   :align: center
   :width: 100%

   Exact float-free ``geometor.model`` construction illustrating **Perpendicular Bisector & Midpoint** (``perpendicular_bisector(A, B) -> (bisector, midpoint)``).

Cross-System Revelation Matrix
------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - System
     - What This Encoding Reveals
     - What This Encoding Hides
   * - **LeanEuclid & Formal System E**
     - Follows Euclid's exact deductive chain (equilateral apex -> angle bisector I.9 -> Pasch line intersection -> SAS I.4) and proves d lies strictly between a and b!
     - Uses Euclid's 2-triangle angle-bisector construction rather than Lemoine's more economical 2-pole vesica chord [E F].
   * - **GeoCoq (Tarski / Hilbert / Euclid)**
     - Astonishing metatheoretic insight: unlike Euclid I.10 (which uses I.1 and thus circle-circle continuity), midpoint existence holds in pure Hilbert/Tarski neutral geometry over smaller Pythagorean fields!
     - Requires ~150 lines of intricate Tarski point-only lemmas in Ch08.
   * - **Lean 4 Mathlib (Euclidean & Affine)**
     - Defines the perpendicular bisector hyperplane in arbitrary dimension n as the orthogonal complement (p₁ -ᵥ p₂)ᗮ through midpoint ℝ p₁ p₂, and proves the equidistance locus iff in 8 lines.
     - Assumes 1/2 scalar division in ℝ up front (midpoint := lineMap p₁ p₂ (1/2)) rather than constructing it with a compass.
   * - **AlphaGeometry (DD + AR)**
     - Demonstrates AlphaGeometry's clever HoleCircle mechanism: once c is sampled at one lens pole, repeating the exact same clause for d automatically punctures c and selects the opposite pole d != c!
     - Relies on kite rule r23 + reflected congruence r37 rather than explicit half-plane opposition.
   * - **Newclid & Yuclid**
     - Explicitly links perpendicular-bisector intersection (on\_bline) to midpoint (R54) and sound constant ratio 1/2 (R51).
     - Treats on\_bline as a primitive 1-step locus rather than unfolding the two congruent circles.
   * - **Java Geometry Expert (JGEX / Area Method)**
     - 4-point Pythagoras difference P\_ACBD proves kite diagonal orthogonality in 1 subtraction without square roots!
     - Symmetric opposite-side orientation S\_CBD = S\_ACD must be supplied for the two circle roots.
   * - **Projective & Conformal Geometric Algebra (kingdon / galgebra)**
     - In 2D CGA, subtracting two unit null points A - B IS the dual perpendicular bisector hyperplane because their quadratic terms cancel to the equidistance locus!
     - Bypasses the vesica circle construction entirely.
   * - **CindyJS (Complex Projective CP^2 & Cayley-Klein)**
     - Shows Cayley-Klein orthogonality in action: multiplying line l\_AB by fundDual = diag(1,1,0) produces its orthogonal ideal point [a, b, 0], which is crossed with M.
     - Division-free affine shortcut rather than compass construction.
   * - **SymPy Geometry (sympy.geometry 1.14.0)**
     - Clean 2-line high-level API returning exact rational Point2D and Line2D whenever A, B are rational.
     - Triggers eager simplify() calls inside midpoint and Line coefficients.
   * - **Oliver Byrne's Coloured Euclid (1847 / Rougeux)**
     - Stroke grammar in action: solid strokes mark Given/target halves while dashed [black ╌╌╌] marks the auxiliary angle-bisector cut.
     - Follows Euclid's I.1 -> I.9 -> I.4 triangle chain rather than the direct 2-pole vesica chord [E F].
   * - **GEOMETOR (geometor.model + Ecosystem)**
     - Unfolds the genuine compass-and-straightedge vesica construction, cancels √3 identically when [E F] meets [A B] so M stays purely in Q(A, B), and folds auxiliary circles neatly via subconstruction!
     - Re-running 2 circles per midpoint adds construction steps unless cached as a reusable macro.

Side-by-Side Formal & Visual Implementations (11 Systems)
---------------------------------------------------------

LeanEuclid & Formal System E (``leaneuclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``LeanEuclid/Book/Prop10.lean:9-33``

.. code-block:: lean4

   theorem proposition_10 : ∀ (a b : Point) (AB : Line),
       distinctPointsOnLine a b AB → ∃ d : Point, between a d b ∧ |(a─d)| = |(d─b)| := by
     euclid_intros
     euclid_apply (proposition_1' a b AB) as c
     euclid_apply (Prop09.proposition_9' b a c ...) as CD
     euclid_apply (Intersections.intersect_lines AB CD) as d
     euclid_apply (Prop04.proposition_4 c a d c b d)  -- SAS congruence
     euclid_finish

* **Reveals**: Follows Euclid's exact deductive chain (equilateral apex -> angle bisector I.9 -> Pasch line intersection -> SAS I.4) and proves d lies strictly between a and b!
* **Hides**: Uses Euclid's 2-triangle angle-bisector construction rather than Lemoine's more economical 2-pole vesica chord [E F].

GeoCoq (Tarski / Hilbert / Euclid) (``geocoq``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``GeoCoq/Main/Tarski_dev/Ch08_orthogonality.v (l8_22 / midpoint_existence)``

.. code-block:: coq

   Lemma midpoint_existence : forall A B, exists X, Midpoint X A B.
   (* Proven in neutral geometry WITHOUT circle-circle continuity via Gupta's
      clever perpendicular-projection construction! *)

* **Reveals**: Astonishing metatheoretic insight: unlike Euclid I.10 (which uses I.1 and thus circle-circle continuity), midpoint existence holds in pure Hilbert/Tarski neutral geometry over smaller Pythagorean fields!
* **Hides**: Requires ~150 lines of intricate Tarski point-only lemmas in Ch08.

Lean 4 Mathlib (Euclidean & Affine) (``mathlib4``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Mathlib/Geometry/Euclidean/PerpBisector.lean:38-66``

.. code-block:: lean4

   def perpBisector (p₁ p₂ : P) : AffineSubspace ℝ P :=
     mk' (midpoint ℝ p₁ p₂) (ℝ ∙ (p₁ -ᵥ p₂))ᗮ

   theorem mem_perpBisector_iff_dist_eq (p p₁ p₂ : P) :
       p ∈ perpBisector p₁ p₂ ↔ dist p p₁ = dist p p₂

* **Reveals**: Defines the perpendicular bisector hyperplane in arbitrary dimension n as the orthogonal complement (p₁ -ᵥ p₂)ᗮ through midpoint ℝ p₁ p₂, and proves the equidistance locus iff in 8 lines.
* **Hides**: Assumes 1/2 scalar division in ℝ up front (midpoint := lineMap p₁ p₂ (1/2)) rather than constructing it with a compass.

AlphaGeometry (DD + AR) (``alphageometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``alphageometry/rules.txt:24 (r23) & numericals.py:1317 (HoleCircle)``

.. code-block:: text

   a b = segment a b; c = on_circle c a b, on_circle c b a; d = on_circle d a b, on_circle d b a; m = on_line m a b, on_line m c d ? midp m a b

* **Reveals**: Demonstrates AlphaGeometry's clever HoleCircle mechanism: once c is sampled at one lens pole, repeating the exact same clause for d automatically punctures c and selects the opposite pole d != c!
* **Hides**: Relies on kite rule r23 + reflected congruence r37 rather than explicit half-plane opposition.

Newclid & Yuclid (``newclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Newclid/newclid/src/newclid/all_rules.py (R22, R23, R54)``

.. code-block:: text

   a b = segment a b; m = on_line m a b, on_bline m a b ? midp m a b; rconst m a a b 1/2

* **Reveals**: Explicitly links perpendicular-bisector intersection (on\_bline) to midpoint (R54) and sound constant ratio 1/2 (R51).
* **Hides**: Treats on\_bline as a primitive 1-step locus rather than unfolding the two congruent circles.

Java Geometry Expert (JGEX / Area Method) (``jgex``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Java-Geometry-Expert Area Method``

.. code-block:: text

   POINT A B; INTERSECTION_CC C A B B A; INTERSECTION_CC D B A A B; INTERSECTION_LL M A B C D;
   SHOW: MIDPOINT M A B.
   # Area elimination: AM / MB = S_ACD / S_CBD = 1; Perp: P_ACBD = (AC^2 - BC^2) + (BD^2 - AD^2) = 0

* **Reveals**: 4-point Pythagoras difference P\_ACBD proves kite diagonal orthogonality in 1 subtraction without square roots!
* **Hides**: Symmetric opposite-side orientation S\_CBD = S\_ACD must be supplied for the two circle roots.

Projective & Conformal Geometric Algebra (kingdon / galgebra) (``pga_cga``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``2D PGA Cl(2,0,1) & 2D CGA Cl(3,1) in kingdon``

.. code-block:: python

   # 2D PGA (division-free & radical-free!):
   l_bis_pga = (A & B) | (A + B)
   M_pga = sp.Rational(1, 2) * (A + B)

   # 2D CGA (perpendicular bisector is literally A - B!):
   l_bis_dual = A - B   # -2*((A - B) | X) = |X - A|^2 - |X - B|^2 == 0!
   M_cga = sp.Rational(1, 2) * (A + B) + sp.Rational(1, 4) * (A | B) * ni

* **Reveals**: In 2D CGA, subtracting two unit null points A - B IS the dual perpendicular bisector hyperplane because their quadratic terms cancel to the equidistance locus!
* **Hides**: Bypasses the vesica circle construction entirely.

CindyJS (Complex Projective CP^2 & Cayley-Klein) (``cindyjs``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``CindyJS/src/js/libcs/Operators.js:2521-2540``

.. code-block:: javascript

   M = B_3 * A + A_3 * B;               // homogeneous midpoint [xA+xB, yA+yB, 2]
   l_AB = cross(A, B);                  // join(A, B)
   l_bis = cross(fundDual * l_AB, M);   // CindyScript: perp(join(A, B), midpoint(A, B))

* **Reveals**: Shows Cayley-Klein orthogonality in action: multiplying line l\_AB by fundDual = diag(1,1,0) produces its orthogonal ideal point [a, b, 0], which is crossed with M.
* **Hides**: Division-free affine shortcut rather than compass construction.

SymPy Geometry (sympy.geometry 1.14.0) (``sympy_geometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``sympy/geometry/line.py:1654-1680``

.. code-block:: python

   seg = Segment(A, B)
   M = seg.midpoint
   l_bis = seg.perpendicular_bisector()

* **Reveals**: Clean 2-line high-level API returning exact rational Point2D and Line2D whenever A, B are rational.
* **Hides**: Triggers eager simplify() calls inside midpoint and Line coefficients.

Oliver Byrne's Coloured Euclid (1847 / Rougeux) (``byrne_1847``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Byrne (1847) Book I, Props. 10 & 11 / Rougeux c82.net/euclid/book1#prop10``

.. code-block:: text

   Given:        [black ━━] = [yellow ━━] + [blue ━━]
   Construction: Construct equilateral △([red ━━], [red ━━], [black ━━])  (I.1)
                 Bisect apex wedge into [yellow ◣] = [red ◣] by [black ╌╌╌] (I.9)
   Proof:        [red ━━] = [red ━━],  [black ╌╌╌] common,  [yellow ◣] = [red ◣]
               ∴ [yellow ━━] = [blue ━━]                                  (I.4)

* **Reveals**: Stroke grammar in action: solid strokes mark Given/target halves while dashed [black ╌╌╌] marks the auxiliary angle-bisector cut.
* **Hides**: Follows Euclid's I.1 -> I.9 -> I.4 triangle chain rather than the direct 2-pole vesica chord [E F].

GEOMETOR (geometor.model + Ecosystem) (``geometor_model``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``geometor/codes/figures.py:45-91 (_midpoint_via_vesica)``

.. code-block:: python

   with m.subconstruction("bisect_AB") as scope:
       c1 = m.construct_circle(a, b, guide=True); c2 = m.construct_circle(b, a, guide=True)
       f = m.intersect(c1, c2, side_of=(a, b, +1), guide=True)
       e = m.intersect(c1, c2, side_of=(a, b, -1), guide=True)
       bis = m.construct_line(e, f, ID="[ E F ]")
       mid = m.intersect(l_ab, bis, between=(a, b), ID="M")
       scope.keep(mid, bis)

* **Reveals**: Unfolds the genuine compass-and-straightedge vesica construction, cancels √3 identically when [E F] meets [A B] so M stays purely in Q(A, B), and folds auxiliary circles neatly via subconstruction!
* **Hides**: Re-running 2 circles per midpoint adds construction steps unless cached as a reusable macro.

