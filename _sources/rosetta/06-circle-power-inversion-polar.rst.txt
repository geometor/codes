:order: 6

.. _rosetta-06-circle-power-inversion-polar:

===============================================================
Benchmark 6: Circle Power, Radical Axis, Inversion & Pole-Polar
===============================================================

* **Canonical GEOMETOR Signature**: ``circle_inversion_polar(omega, P) -> (power, P_inv, polar_line)``
* **Classical Citation**: *Euclid III.35-36 + Steiner (1826) + Poncelet / La Hire Pole-Polar Reciprocity*
* **Core Phenomenon**: For circle Ω(O, R) and point P: Steiner power \|OP\|^2 - R^2, radical axis of two circles, inverse point P' on ray OP with \|OP\|·\|OP'\| = R^2, and polar line through P' perpendicular to OP satisfying La Hire's reciprocity (Q on polar(P) <=> P on polar(Q)) and harmonic range (R-, R+; P', P) = -1.

.. figure:: /_static/figures/06-pga-cga-inversion.svg
   :align: center
   :width: 100%

   Exact float-free ``geometor.model`` construction illustrating **Circle Power, Radical Axis, Inversion & Pole-Polar** (``circle_inversion_polar(omega, P) -> (power, P_inv, polar_line)``).

Cross-System Revelation Matrix
------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - System
     - What This Encoding Reveals
     - What This Encoding Hides
   * - **LeanEuclid & Formal System E**
     - System E would require nonlinear metric product axioms \|PA\| \* \|PB\| = \|PC\| \* \|PD\| to reach Book III.35.
     - All quadratic circle invariants.
   * - **GeoCoq (Tarski / Hilbert / Euclid)**
     - Reveals that even the largest synthetic Coq geometry library (4,671 lemmas) never formalized 19th-century inversive/coaxial geometry.
     - Entire inversive and pole-polar canon.
   * - **Lean 4 Mathlib (Euclidean & Affine)**
     - Masterclass in n-dimensional clarity: defines polar via sphere inversion and proves La Hire's symmetric reciprocity q ∈ s.polar p ↔ p ∈ s.polar q in lines using inner products! (Yet omits radicalAxis!)
     - Omits radicalAxis / coaxial pencils and specializes pole/polar to spheres rather than general conics.
   * - **AlphaGeometry (DD + AR)**
     - Clever synthetic encoding of external inversion via tangent touchpoint t + perpendicular foot p1 (so OP \* OP1 = OT^2 = R^2 via SAS similarity r39!).
     - Fails for internal points P inside Ω unless rewritten via anti-parallels, and CANNOT state disjoint-circle radical axis PO1^2 - PO2^2 = R1^2 - R2^2!
   * - **Newclid & Yuclid**
     - Generalized Pythagoras R85 provides the exact algebraic engine needed for radical axes of non-intersecting circles.
     - No first-class inversion or polar constructor.
   * - **Java Geometry Expert (JGEX / Area Method)**
     - JGEX has first-class C\_INVERSION and C\_RADICAL constructors, and the Area Method eliminates inverse points rationally in 2 lines!
     - Limited to circles rather than general conics.
   * - **Projective & Conformal Geometric Algebra (kingdon / galgebra)**
     - CGA's supreme triumph: Steiner power is an inner product, radical axis is subtraction kappa1 - kappa2 (even for disjoint circles!), and circle inversion is a sandwich product!
     - Requires 4D Cl(3,1) null-cone embedding.
   * - **CindyJS (Complex Projective CP^2 & Cayley-Klein)**
     - Generalizes pole-polar to EVERY conic via 1 matrix-vector product l = C\*p, and computes circle inversion rationally as meet(join(O1, p), C1\*p)!
     - Complex float representation.
   * - **SymPy Geometry (sympy.geometry 1.14.0)**
     - Exposes SymPy's single biggest classical geometry gap—making geometor.model.inversion a high-impact contribution.
     - Zero native inversive or coaxial support.
   * - **Oliver Byrne's Coloured Euclid (1847 / Rougeux)**
     - Captures Euclid's area-theoretic ancestor of Steiner circle power (rectangle of secant segments equals square of tangent) using Book II visual algebra!
     - Stops before 19th-century signed circle power \|OP\|^2 - R^2, radical axes, circle inversion, and La Hire pole-polar reciprocity.
   * - **GEOMETOR (geometor.model + Ecosystem)**
     - Constructs exact tangent touchpoints T1, T2, polar [T1 T2], and inverse P1 by pure compass & straightedge while verifying \|OP\|·\|OP1\| = R^2 AND harmonic conjugacy (R-, R+; P1, P) = -1!
     - Should be promoted to first-class geometor.model.inversion helpers that also work for internal points P inside Ω.

Side-by-Side Formal & Visual Implementations (11 Systems)
---------------------------------------------------------

LeanEuclid & Formal System E (``leaneuclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``ABSENT across LeanEuclid``

.. code-block:: lean4

   -- OMITTED: Book III (chords/tangents III.35-36) and modern circle inversion /
   -- pole-polar geometry are outside LeanEuclid's Book-I scope.

* **Reveals**: System E would require nonlinear metric product axioms \|PA\| \* \|PB\| = \|PC\| \* \|PD\| to reach Book III.35.
* **Hides**: All quadratic circle invariants.

GeoCoq (Tarski / Hilbert / Euclid) (``geocoq``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``ABSENT in GeoCoq (Annexes/circles.v has basic tangency only)``

.. code-block:: coq

   (* OMITTED: GeoCoq contains basic chord/tangent definitions in Annexes/circles.v,
      but lacks Steiner circle power, radical axis, circle inversion, and pole-polar! *)

* **Reveals**: Reveals that even the largest synthetic Coq geometry library (4,671 lemmas) never formalized 19th-century inversive/coaxial geometry.
* **Hides**: Entire inversive and pole-polar canon.

Lean 4 Mathlib (Euclidean & Affine) (``mathlib4``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Mathlib/Geometry/Euclidean/Sphere/{Power,PolePolar}.lean & Inversion/Basic.lean``

.. code-block:: lean4

   def power (s : Sphere P) (p : P) : ℝ := dist p s.center ^ 2 - s.radius ^ 2
   def polar (s : Sphere P) (p : P) : AffineSubspace ℝ P :=
     mk' (inversion s.center s.radius p) (ℝ ∙ (p -ᵥ s.center))ᗮ
   theorem mem_polar_iff (s : Sphere P) {p q : P} ... : q ∈ s.polar p ↔ p ∈ s.polar q

* **Reveals**: Masterclass in n-dimensional clarity: defines polar via sphere inversion and proves La Hire's symmetric reciprocity q ∈ s.polar p ↔ p ∈ s.polar q in lines using inner products! (Yet omits radicalAxis!)
* **Hides**: Omits radicalAxis / coaxial pencils and specializes pole/polar to spheres rather than general conics.

AlphaGeometry (DD + AR) (``alphageometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Tangent-foot construction (defs.txt:397, 61); disjoint radical axis unexpressible!``

.. code-block:: text

   # Tangent-foot construction of inverse p1 & La Hire pole-polar reciprocity:
   o a p = triangle o a p; t s = tangent t s p o a; p1 = foot p1 t o p; q = on_tline q p1 o p; u v = tangent u v q o a; q1 = foot q1 u o q ? perp p q1 o q

* **Reveals**: Clever synthetic encoding of external inversion via tangent touchpoint t + perpendicular foot p1 (so OP \* OP1 = OT^2 = R^2 via SAS similarity r39!).
* **Hides**: Fails for internal points P inside Ω unless rewritten via anti-parallels, and CANNOT state disjoint-circle radical axis PO1^2 - PO2^2 = R1^2 - R2^2!

Newclid & Yuclid (``newclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Newclid R85 (Generalized Pythagoras) + Yuclid squared-length AR``

.. code-block:: text

   # Disjoint radical axis orthogonality PO1^2 - PO2^2 = HO1^2 - HO2^2 via R85:
   o1 o2 = segment o1 o2; p = free p; h = on_tline h p o1 o2 ? lequation 1/1 p o1 * p o1 -1/1 h o1 * h o1 -1/1 p o2 * p o2 1/1 h o2 * h o2 0

* **Reveals**: Generalized Pythagoras R85 provides the exact algebraic engine needed for radical axes of non-intersecting circles.
* **Hides**: No first-class inversion or polar constructor.

Java Geometry Expert (JGEX / Area Method) (``jgex``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Java-Geometry-Expert/.../exs-book/ch3:49-58 (native INVERSION!)``

.. code-block:: text

   POINT O A P; INVERSION P1 P O A; ON_TLINE Q P1 O P; INVERSION Q1 Q O A;
   SHOW: PERPENDICULAR P Q1 O Q.
   # Eliminates P1 via OP1 = (P_OAO / P_OPO) OP -> 2-line coordinate-free La Hire proof!

* **Reveals**: JGEX has first-class C\_INVERSION and C\_RADICAL constructors, and the Area Method eliminates inverse points rationally in 2 lines!
* **Hides**: Limited to circles rather than general conics.

Projective & Conformal Geometric Algebra (kingdon / galgebra) (``pga_cga``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``2D CGA Cl(3,1) in kingdon — CGA's Crown Jewel!``

.. code-block:: python

   power_P = -2 * (kappa1 | P).e              # 1. Steiner power = inner product!
   lam_rad = kappa1 - kappa2                  # 2. Radical axis = vector subtraction!
   P_inv   = norm_pt(-kappa1 * P * kappa1)    # 3. Circle inversion = rational sandwich!
   lam_pol = kappa1 + (P ^ ni) | kappa1       # 4. Polar line = contraction!

* **Reveals**: CGA's supreme triumph: Steiner power is an inner product, radical axis is subtraction kappa1 - kappa2 (even for disjoint circles!), and circle inversion is a sandwich product!
* **Hides**: Requires 4D Cl(3,1) null-cone embedding.

CindyJS (Complex Projective CP^2 & Cayley-Klein) (``cindyjs``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``CindyJS/src/js/libgeo/GeoOps.js:1910-1931 & 2044-2049``

.. code-block:: javascript

   l_polar = C1 * p;                          // Polar of p wrt ANY conic C1!
   p_pole  = adjoint3(C1) * l;                // Pole of l wrt ANY conic C1!
   O1      = adjoint3(C1) * linf;             // Center of circle C1
   p_inv   = cross(cross(O1, p), C1 * p);     // Inverse = meet(diameter, polar)!

* **Reveals**: Generalizes pole-polar to EVERY conic via 1 matrix-vector product l = C\*p, and computes circle inversion rationally as meet(join(O1, p), C1\*p)!
* **Hides**: Complex float representation.

SymPy Geometry (sympy.geometry 1.14.0) (``sympy_geometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``ALL FOUR MISSING in sympy.geometry 1.14.0!``

.. code-block:: python

   # MISSING: Circle has NO .power(), .radical_axis(), .invert(), .polar(), or .pole()!
   # Must hand-roll via Cir1.equation(x, y) subtraction and manual vector scaling.

* **Reveals**: Exposes SymPy's single biggest classical geometry gap—making geometor.model.inversion a high-impact contribution.
* **Hides**: Zero native inversive or coaxial support.

Oliver Byrne's Coloured Euclid (1847 / Rougeux) (``byrne_1847``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Byrne (1847) Book III, Props. 35 & 36 (Chord/Tangent-Secant Power only)``

.. code-block:: text

   # Byrne Book III, Prop. 36 (Tangent-Secant Power of a Point):
   To Prove:     ▭([whole secant ━━], [external ━━]) = □([red tangent ━━])
   Proof:        Via Book II.6 gnomon-square identity + Byrne I.47 right radii!
   # OMITTED: Radical axis of disjoint circles, Möbius inversion, and Pole-Polar.

* **Reveals**: Captures Euclid's area-theoretic ancestor of Steiner circle power (rectangle of secant segments equals square of tangent) using Book II visual algebra!
* **Hides**: Stops before 19th-century signed circle power \|OP\|^2 - R^2, radical axes, circle inversion, and La Hire pole-polar reciprocity.

GEOMETOR (geometor.model + Ecosystem) (``geometor_model``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``geometor/codes/figures.py:274-310 (Thales tangent polar + harmonic check)``

.. code-block:: python

   thales = m.construct_circle(r0, o, guide=True)
   t1 = m.intersect(omega, thales, side_of=(o, p, +1), ID="T1")
   t2 = m.intersect(omega, thales, side_of=(o, p, -1), ID="T2")
   polar = m.construct_line(t1, t2, ID="[ T1 T2 ]")
   p_inv = m.intersect(l_op, polar, between=(o, r0), ID="P1")
   assert zero_test(cross_ratio(r_neg, r0, p_inv, p) + 1)  # exact harmonic -1!

* **Reveals**: Constructs exact tangent touchpoints T1, T2, polar [T1 T2], and inverse P1 by pure compass & straightedge while verifying \|OP\|·\|OP1\| = R^2 AND harmonic conjugacy (R-, R+; P1, P) = -1!
* **Hides**: Should be promoted to first-class geometor.model.inversion helpers that also work for internal points P inside Ω.

