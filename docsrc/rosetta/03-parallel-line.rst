:order: 3

.. _rosetta-03-parallel-line:

====================================================
Benchmark 3: Parallel Line Through an External Point
====================================================

* **Canonical GEOMETOR Signature**: ``parallel_line(line_AB, P) -> line_parallel``
* **Classical Citation**: *Euclid Book I, Proposition 31*
* **Core Phenomenon**: Construct the unique Euclidean line through external point P parallel to line AB. Exposes how each system treats the Parallel Postulate, points at infinity, alternate interior angles, or rhombus symmetry.

.. figure:: /_static/figures/02-topological-selectors.svg
   :align: center
   :width: 100%

   Exact float-free ``geometor.model`` construction illustrating **Parallel Line Through an External Point** (``parallel_line(line_AB, P) -> line_parallel``).

Cross-System Revelation Matrix
------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - System
     - What This Encoding Reveals
     - What This Encoding Hides
   * - **LeanEuclid & Formal System E**
     - Proves existence of a non-intersecting line in pure neutral geometry (Prop 27 alternate interior angles—Playfair uniqueness is not needed until Prop 29/30!).
     - Euclid's angle-copying construction (via I.23 -> I.22) has much higher Lemoine complexity than rhombus or double-perpendicular constructions.
   * - **GeoCoq (Tarski / Hilbert / Euclid)**
     - Cleanly separates neutral parallel existence (central reflection across a midpoint!) from the 34 equivalent parallel-uniqueness postulates cataloged in parallel\_postulates.v.
     - Representing the output line requires two existential witness points C, D with C <> D and Col P C D.
   * - **Lean 4 Mathlib (Euclidean & Affine)**
     - In an affine torsor, a parallel subspace through p is tautologically mk' p s.direction—Playfair's postulate is baked directly into linear-algebraic coset structure!
     - Cannot study non-Euclidean neutral geometry without abandoning AffineSpace.
   * - **AlphaGeometry (DD + AR)**
     - Rule r00 (AB ⊥ CF ∧ CD ⊥ CF => AB \|\| CD) gives an immediate 1-step synthetic proof.
     - Conflates parallel existence and Playfair uniqueness (r28: para A B A C => coll A B C).
   * - **Newclid & Yuclid**
     - Direct 1-rule verification via R00\_PERPENDICULARS\_GIVE\_PARALLEL.
     - Assumes Euclidean metric direction group ℝ/πℤ.
   * - **Java Geometry Expert (JGEX / Area Method)**
     - Dualizes 90-degree rotation (TRATIO) directly between signed area S\_CABD and Pythagoras difference P\_AFBC!
     - Requires choosing auxiliary ratio parameter r != 0 along the perpendicular.
   * - **Projective & Conformal Geometric Algebra (kingdon / galgebra)**
     - Reveals the projective essence of parallelism: a parallel line through P is simply the join (&) of P with L's ideal point at infinity (L ^ e0)!
     - Requires degenerate generator e0^2 = 0.
   * - **CindyJS (Complex Projective CP^2 & Cayley-Klein)**
     - Identical projective elegance in CP^2: cross(linf, L) is the ideal point of L on z=0, and crossing with P joins it to P in 6 multiplications.
     - Euclidean vs hyperbolic parallelism depends on the chosen fundamental conic.
   * - **SymPy Geometry (sympy.geometry 1.14.0)**
     - One-method vector translation P + L.direction.
     - Parallel lines have L.intersection(L\_para) == [], losing the ideal point at infinity.
   * - **Oliver Byrne's Coloured Euclid (1847 / Rougeux)**
     - Replaces Euclid's six vertex pointers (A, B, C, D, E, F) with two coloured angle wedges [red ◣] = [blue ◣], making the alternate-interior-angle mechanism instantaneous.
     - Notice Byrne MUST print a tiny black dot/star for the given external point because pure 0D points have no coloured line/region glyph!
   * - **GEOMETOR (geometor.model + Ecosystem)**
     - Achieves parallel construction in just 3 congruent-radius circles (rhombus APDQ) and certifies exact parallelism via rational line\_spread == 0.
     - Could also expose a 1-line projective bridge cross(cross(linf, l\_ab), p) in geometor.pappus.

Side-by-Side Formal & Visual Implementations (11 Systems)
---------------------------------------------------------

LeanEuclid & Formal System E (``leaneuclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``LeanEuclid/Book/Prop31.lean:9-36``

.. code-block:: lean4

   theorem proposition_31 : ∀ (a b c : Point) (BC : Line),
       distinctPointsOnLine b c BC ∧ ¬(a.onLine BC) →
       ∃ EF : Line, a.onLine EF ∧ ¬(EF.intersectsLine BC) := by
     euclid_intros
     -- Picks d on BC, copies angle ∠(a:d:c) to vertex a via Prop23, applies Prop27:
     euclid_apply (Prop23.proposition_23_opposing ...) as e
     euclid_apply (Lines.from_points e a) as EF
     euclid_apply (Prop27.proposition_27 e a b c ...)
     euclid_finish

* **Reveals**: Proves existence of a non-intersecting line in pure neutral geometry (Prop 27 alternate interior angles—Playfair uniqueness is not needed until Prop 29/30!).
* **Hides**: Euclid's angle-copying construction (via I.23 -> I.22) has much higher Lemoine complexity than rhombus or double-perpendicular constructions.

GeoCoq (Tarski / Hilbert / Euclid) (``geocoq``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``GeoCoq/Main/Tarski_dev/Ch12_parallel.v (parallel_existence1) & parallel_postulates.v``

.. code-block:: coq

   Lemma parallel_existence : forall A B P, A <> B ->
     exists C, exists D, C <> D /\ Par A B C D /\ Col P C D.
   (* Existence proven in neutral geometry via double midpoint reflection;
      uniqueness proved equivalent to 34 distinct parallel postulates! *)

* **Reveals**: Cleanly separates neutral parallel existence (central reflection across a midpoint!) from the 34 equivalent parallel-uniqueness postulates cataloged in parallel\_postulates.v.
* **Hides**: Representing the output line requires two existential witness points C, D with C <> D and Col P C D.

Lean 4 Mathlib (Euclidean & Affine) (``mathlib4``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Mathlib/LinearAlgebra/AffineSpace/AffineSubspace.lean (Parallel)``

.. code-block:: lean4

   -- Parallelism s₁ ∥ s₂ means s₁.direction = s₂.direction (up to translation):
   def parallelThrough (s : AffineSubspace ℝ P) (p : P) : AffineSubspace ℝ P :=
     AffineSubspace.mk' p s.direction

* **Reveals**: In an affine torsor, a parallel subspace through p is tautologically mk' p s.direction—Playfair's postulate is baked directly into linear-algebraic coset structure!
* **Hides**: Cannot study non-Euclidean neutral geometry without abandoning AffineSpace.

AlphaGeometry (DD + AR) (``alphageometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``alphageometry/defs.txt:211 (on_pline) & rules.txt:1 (r00)``

.. code-block:: text

   # Synthetic double-perpendicular construction (1 deduction step via r00):
   a b c = triangle a b c; f = foot f c a b; d = on_tline d c c f ? para c d a b

* **Reveals**: Rule r00 (AB ⊥ CF ∧ CD ⊥ CF => AB \|\| CD) gives an immediate 1-step synthetic proof.
* **Hides**: Conflates parallel existence and Playfair uniqueness (r28: para A B A C => coll A B C).

Newclid & Yuclid (``newclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Newclid/newclid/tests/test_individual_rules.py:102 (R00)``

.. code-block:: text

   a = free a; b = free b; c = free c; d = on_tline d c a b; f = on_tline f c c d ? para a b c f

* **Reveals**: Direct 1-rule verification via R00\_PERPENDICULARS\_GIVE\_PARALLEL.
* **Hides**: Assumes Euclidean metric direction group ℝ/πℤ.

Java Geometry Expert (JGEX / Area Method) (``jgex``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Java-Geometry-Expert Area Method``

.. code-block:: text

   POINT A B C; FOOT F C A B; ON_TLINE D C C F; SHOW: PARALLEL C D A B.
   # Area goal: S_CABD = S_CAB - S_DAB = -(r/4) P_AFBC = 0 (since CF ⊥ AB => P_AFBC = 0)

* **Reveals**: Dualizes 90-degree rotation (TRATIO) directly between signed area S\_CABD and Pythagoras difference P\_AFBC!
* **Hides**: Requires choosing auxiliary ratio parameter r != 0 along the perpendicular.

Projective & Conformal Geometric Algebra (kingdon / galgebra) (``pga_cga``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``2D PGA Cl(2,0,1) in kingdon``

.. code-block:: python

   # Projective form: join P with the ideal point (L ^ e0) where L meets infinity!
   L_para = P & (L ^ e0)
   # Equivalent metric double-contraction (no explicit e0 needed):
   L_para_metric = (L | P) | P

* **Reveals**: Reveals the projective essence of parallelism: a parallel line through P is simply the join (&) of P with L's ideal point at infinity (L ^ e0)!
* **Hides**: Requires degenerate generator e0^2 = 0.

CindyJS (Complex Projective CP^2 & Cayley-Klein) (``cindyjs``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``CindyJS/src/js/libcs/Operators.js:2515``

.. code-block:: javascript

   L_para = cross(cross(linf, L), P);   // CindyScript: para(L, P)

* **Reveals**: Identical projective elegance in CP^2: cross(linf, L) is the ideal point of L on z=0, and crossing with P joins it to P in 6 multiplications.
* **Hides**: Euclidean vs hyperbolic parallelism depends on the chosen fundamental conic.

SymPy Geometry (sympy.geometry 1.14.0) (``sympy_geometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``sympy/geometry/line.py:1372-1395``

.. code-block:: python

   L_para = L.parallel_line(P)          # Line(P, P + L.direction)

* **Reveals**: One-method vector translation P + L.direction.
* **Hides**: Parallel lines have L.intersection(L\_para) == [], losing the ideal point at infinity.

Oliver Byrne's Coloured Euclid (1847 / Rougeux) (``byrne_1847``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Byrne (1847) Book I, Prop. 31 / Rougeux c82.net/euclid/book1#prop31``

.. code-block:: text

   Given:        Point • and line [black ━━]
   Construction: Draw transversal [yellow ╌╌╌] from • to [black ━━]       (Post. 1)
                 Copy alternate wedge [red ◣] = [blue ◣] via [red ━━]     (I.23)
   Proof:        Alternate wedges [red ◣] = [blue ◣]
               ∴ [red ━━] ∥ [black ━━]                                    (I.27)

* **Reveals**: Replaces Euclid's six vertex pointers (A, B, C, D, E, F) with two coloured angle wedges [red ◣] = [blue ◣], making the alternate-interior-angle mechanism instantaneous.
* **Hides**: Notice Byrne MUST print a tiny black dot/star for the given external point because pure 0D points have no coloured line/region glyph!

GEOMETOR (geometor.model + Ecosystem) (``geometor_model``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``geometor.model + Compass Rhombus Construction``

.. code-block:: python

   # Pure 3-circle compass rhombus (Lemoine-optimal) or double perpendicular:
   q = m.intersect(l_ab, m.construct_circle(a, p, guide=True), on_ray=(a, b), guide=True)
   d = m.intersect(m.construct_circle(p, a, guide=True), m.construct_circle(q, a, guide=True),
                   side_of=(a, p, -1), ID="D")
   l_para = m.construct_line(p, d, ID="[ P D ]")
   m.assert_parallel(l_ab, l_para, by="I.31")  # exact line_spread == 0

* **Reveals**: Achieves parallel construction in just 3 congruent-radius circles (rhombus APDQ) and certifies exact parallelism via rational line\_spread == 0.
* **Hides**: Could also expose a 1-line projective bridge cross(cross(linf, l\_ab), p) in geometor.pappus.

