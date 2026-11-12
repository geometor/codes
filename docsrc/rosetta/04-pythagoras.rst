:order: 4

.. _rosetta-04-pythagoras:

===============================================================
Benchmark 4: Pythagorean Theorem & Right-Triangle Orthogonality
===============================================================

* **Canonical GEOMETOR Signature**: ``pythagoras(A, B, C) -> Q(A, B) == Q(A, C) + Q(B, C)``
* **Classical Citation**: *Euclid Book I, Proposition 47*
* **Core Phenomenon**: For right-angled triangle ABC (orthogonality at C), the quadrance on the hypotenuse equals the sum of the quadrances on the legs—and geometrically, the area of the hypotenuse square equals the sum of the two leg squares (Euclid's Bride's Chair). Exposes a stunning expressiveness cliff in AlphaGeometry!

.. figure:: /_static/figures/04-torsor-oangle-spread.svg
   :align: center
   :width: 100%

   Exact float-free ``geometor.model`` construction illustrating **Pythagorean Theorem & Right-Triangle Orthogonality** (``pythagoras(A, B, C) -> Q(A, B) == Q(A, C) + Q(B, C)``).

Cross-System Revelation Matrix
------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - System
     - What This Encoding Reveals
     - What This Encoding Hides
   * - **LeanEuclid & Formal System E**
     - Formalizes Euclid's authentic cut-and-paste area proof (Bride's Chair) AND explicitly isolates 6 '-- Missed by Euclid' topological lemmas (Prop47.lean:25-60) proving the outward squares don't fold across the triangle!
     - Verbose 9-point, 10-line theorem signature because Square is an unbundled 12-argument relational macro.
   * - **GeoCoq (Tarski / Hilbert / Euclid)**
     - Proves a^2 + b^2 = c^2 purely synthetically inside Tarski's internal geometric segment field (Sum and Prod constructed on line OE with unit E via Pappus/Thales) with zero real numbers!
     - Requires carrying coordinate-line frame witnesses (O, E, E') through every arithmetic relation.
   * - **Lean 4 Mathlib (Euclidean & Affine)**
     - Immediate consequence of ‖u - v‖^2 = ‖u‖^2 + ‖v‖^2 - 2⟪u, v⟫ in any Hilbert/inner-product space of arbitrary dimension n, including degenerate endpoint disjuncts!
     - Reduces Euclid's deep geometric theorem to a 3-line inner-product expansion, hiding the constructive equivalence of geometric squares.
   * - **AlphaGeometry (DD + AR)**
     - Major architectural revelation: AlphaGeometry's RatioTable (log-lengths) and DistanceTable (collinear 1st-power lengths) CANNOT express a^2 + b^2 = c^2!
     - Any theorem requiring additive quadratic relations (Stewart, Apollonius median, disjoint radical axis) hits a hard wall in pure AlphaGeometry.
   * - **Newclid & Yuclid**
     - Shows exactly how Newclid/Yuclid broke past AlphaGeometry's ceiling by adding a dedicated additive squared-length Gaussian elimination table!
     - In Newclid's Python engine, lequation is not yet wired into SympyARDeductor (only active in C++ Yuclid).
   * - **Java Geometry Expert (JGEX / Area Method)**
     - By choosing P\_ACB = AC^2 + CB^2 - AB^2 as a primitive coordinate-free invariant, Chou-Gao-Zhang make Pythagoras literally 0 = 0, AND ship 20 visual dissection proofs in 4\_PYTH/!
     - Area.java GUI tab is disabled in the Java port.
   * - **Projective & Conformal Geometric Algebra (kingdon / galgebra)**
     - Both PGA line norms (l \| l) and CGA null-point contractions -2\*(A \| B) natively compute Wildberger quadrances without a single square root.
     - Algebraic expansion rather than geometric square dissection.
   * - **CindyJS (Complex Projective CP^2 & Cayley-Klein)**
     - Interprets perpendicularity projectively as conjugate polarity with respect to the circular points I, J at infinity.
     - Numeric complex float evaluation.
   * - **SymPy Geometry (sympy.geometry 1.14.0)**
     - Direct readable verification, though A.distance(B)\*\*2 first takes sqrt(...) and then squares it back!
     - Unnecessary sqrt-then-square roundtrip unless one manually computes dot products.
   * - **Oliver Byrne's Coloured Euclid (1847 / Rougeux)**
     - Byrne's most celebrated plate: turns Euclid's 40-letter Bride's Chair labyrinth into a self-evident chromatic conservation law [red □] + [blue □] = [yellow ▭] + [black ▭]!
     - Relies on visual outward-square orientation (the exact 6 topological lemmas LeanEuclid had to prove explicitly in Prop47.lean:25-60).
   * - **GEOMETOR (geometor.model + Ecosystem)**
     - Supports BOTH Wildberger's polynomial Pythagoras Law (s(CA, CB) = 1 <=> Q\_c = Q\_a + Q\_b) AND Euclid's exact polygon-area Bride's Chair proof (assert\_area\_equal)!
     - None—this dual algebraic + dissection capability is a signature strength of GEOMETOR.

Side-by-Side Formal & Visual Implementations (11 Systems)
---------------------------------------------------------

LeanEuclid & Formal System E (``leaneuclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``LeanEuclid/Book/Prop47.lean:160-290 (+ lines 25-60 missed lemmas!)``

.. code-block:: lean4

   theorem proposition_47 : ∀ (a b c d e f g h k : Point) (AB BC AC ... : Line),
       formTriangle a b c AB BC CA ∧ ∠(b:a:c) = ∟ ∧
       Square b c e d ... ∧ Square a b f g ... ∧ Square a c k h ... →
       (△(b:c:d) + △(c:e:d)) = (△(a:b:f) + △(b:g:f)) + (△(a:c:k) + △(c:h:k))

* **Reveals**: Formalizes Euclid's authentic cut-and-paste area proof (Bride's Chair) AND explicitly isolates 6 '-- Missed by Euclid' topological lemmas (Prop47.lean:25-60) proving the outward squares don't fold across the triangle!
* **Hides**: Verbose 9-point, 10-line theorem signature because Square is an unbundled 12-argument relational macro.

GeoCoq (Tarski / Hilbert / Euclid) (``geocoq``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``GeoCoq/Main/Tarski_dev/Ch15_lengths.v:260-310 (pythagoras)``

.. code-block:: coq

   Lemma pythagoras :
     forall O E E' A B C AC BC AB AC2 BC2 AB2,
     ~ Col O E E' -> Per A C B ->
     Length O E E' A C AC -> Length O E E' B C BC -> Length O E E' A B AB ->
     Prod O E E' AC AC AC2 -> Prod O E E' BC BC BC2 ->
     Sum O E E' AC2 BC2 AB2 -> Prod O E E' AB AB AB2.

* **Reveals**: Proves a^2 + b^2 = c^2 purely synthetically inside Tarski's internal geometric segment field (Sum and Prod constructed on line OE with unit E via Pappus/Thales) with zero real numbers!
* **Hides**: Requires carrying coordinate-line frame witnesses (O, E, E') through every arithmetic relation.

Lean 4 Mathlib (Euclidean & Affine) (``mathlib4``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Mathlib/Geometry/Euclidean/Angle/Unoriented/Affine.lean:245-268``

.. code-block:: lean4

   theorem dist_sq_eq_dist_sq_add_dist_sq_iff_angle_eq_pi_div_two (p₁ p₂ p₃ : P) :
       dist p₁ p₃ * dist p₁ p₃ = dist p₁ p₂ * dist p₁ p₂ + dist p₃ p₂ * dist p₃ p₂ ↔
         ∠ p₁ p₂ p₃ = π / 2 ∨ p₁ = p₂ ∨ p₃ = p₂

* **Reveals**: Immediate consequence of ‖u - v‖^2 = ‖u‖^2 + ‖v‖^2 - 2⟪u, v⟫ in any Hilbert/inner-product space of arbitrary dimension n, including degenerate endpoint disjuncts!
* **Hides**: Reduces Euclid's deep geometric theorem to a 3-line inner-product expansion, hiding the constructive equivalence of geometric squares.

AlphaGeometry (DD + AR) (``alphageometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Expressiveness Ceiling! (ar.py lacks squared lengths; uses eqratio / contri)``

.. code-block:: text

   # CANNOT state AB^2 + AC^2 = BC^2! Must reformulate multiplicatively as AB^2 = BH * BC:
   a b c = r_triangle a b c; h = foot h a b c ? eqratio b a b c b h b a
   # Or prove Bride's Chair triangle congruence ΔABD ≅ ΔFBC:
   a b c = r_triangle a b c; f g = square b a f g; d e = square b c d e ? contri a b d f b c

* **Reveals**: Major architectural revelation: AlphaGeometry's RatioTable (log-lengths) and DistanceTable (collinear 1st-power lengths) CANNOT express a^2 + b^2 = c^2!
* **Hides**: Any theorem requiring additive quadratic relations (Stewart, Apollonius median, disjoint radical axis) hits a hard wall in pure AlphaGeometry.

Newclid & Yuclid (``newclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Newclid/yuclid/README.md:78-84 & all_rules.py:1005 (R85)``

.. code-block:: text

   # C++ Yuclid additive squared-length AR table + Newclid lequation rule R85:
   a b = segment a b; c = free c; d = on_tline d c a b ? lequation 1/1 a c * a c 1/1 b d * b d -1/1 a d * a d -1/1 b c * b c 0

* **Reveals**: Shows exactly how Newclid/Yuclid broke past AlphaGeometry's ceiling by adding a dedicated additive squared-length Gaussian elimination table!
* **Hides**: In Newclid's Python engine, lequation is not yet wired into SympyARDeductor (only active in C++ Yuclid).

Java Geometry Expert (JGEX / Area Method) (``jgex``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Java-Geometry-Expert/src/main/java/gprover/Elim.java:134 & examples/4_PYTH/``

.. code-block:: text

   # In the Area Method, Pythagoras is a 0-step DEFINITIONAL identity:
   # P_ACB := AC^2 + CB^2 - AB^2, and PERPENDICULAR(C,A, C,B) <=> P_ACB = 0!
   SHOW: (AREA A B F G) + (AREA A C K H) = (AREA B C E D).  # 4-line TRATIO proof!

* **Reveals**: By choosing P\_ACB = AC^2 + CB^2 - AB^2 as a primitive coordinate-free invariant, Chou-Gao-Zhang make Pythagoras literally 0 = 0, AND ship 20 visual dissection proofs in 4\_PYTH/!
* **Hides**: Area.java GUI tab is disabled in the Java port.

Projective & Conformal Geometric Algebra (kingdon / galgebra) (``pga_cga``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``2D PGA Cl(2,0,1) & 2D CGA Cl(3,1) in kingdon``

.. code-block:: python

   # 2D PGA: squared norm of join line (A & B) IS Euclidean quadrance!
   la, lb, lc = B & C, C & A, A & B
   assert (la | lb).e == 0                                  # orthogonality
   assert sp.expand((lc | lc).e - (la | la).e - (lb | lb).e) == 0

   # 2D CGA: null inner product -2*(A | B) IS quadrance!
   assert ((C ^ A ^ ni) | (C ^ B ^ ni)).e == 0

* **Reveals**: Both PGA line norms (l \| l) and CGA null-point contractions -2\*(A \| B) natively compute Wildberger quadrances without a single square root.
* **Hides**: Algebraic expansion rather than geometric square dissection.

CindyJS (Complex Projective CP^2 & Cayley-Klein) (``cindyjs``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``CindyJS/src/js/libcs/List.js:125 (fundDual)``

.. code-block:: javascript

   l_CA = cross(C, A); l_CB = cross(C, B);
   is_ortho = (l_CA * fundDual * l_CB == 0);  // harmonic conjugacy wrt I=(1,i,0), J=(1,-i,0)

* **Reveals**: Interprets perpendicularity projectively as conjugate polarity with respect to the circular points I, J at infinity.
* **Hides**: Numeric complex float evaluation.

SymPy Geometry (sympy.geometry 1.14.0) (``sympy_geometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``sympy/geometry/polygon.py:2195 (Triangle.is_right)``

.. code-block:: python

   assert Triangle(A, B, C).is_right()
   assert sp.simplify(A.distance(B)**2 - (A.distance(C)**2 + B.distance(C)**2)) == 0

* **Reveals**: Direct readable verification, though A.distance(B)\*\*2 first takes sqrt(...) and then squares it back!
* **Hides**: Unnecessary sqrt-then-square roundtrip unless one manually computes dot products.

Oliver Byrne's Coloured Euclid (1847 / Rougeux) (``byrne_1847``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Byrne (1847) Book I, Prop. 47 / Rougeux c82.net/euclid/book1#prop47``

.. code-block:: text

   Given:        Right wedge [black ◣] = [∟]
   To Prove:     [red □] + [blue □] = [yellow+black □]
   Construction: Drop [yellow ╌╌╌] ∥ square side, splitting hypotenuse square
                 into [yellow ▭] + [black ▭]; draw shear diagonals [╌╌╌]
   Proof:        2 △_left = [red □]  and  2 △_shear = [yellow ▭]          (I.41)
                 △_left   = △_shear                                       (I.4)
               ∴ [red □]  = [yellow ▭],  likewise [blue □] = [black ▭]
               ∴ [red □] + [blue □] = [yellow ▭] + [black ▭]              (Ax. 2)

* **Reveals**: Byrne's most celebrated plate: turns Euclid's 40-letter Bride's Chair labyrinth into a self-evident chromatic conservation law [red □] + [blue □] = [yellow ▭] + [black ▭]!
* **Hides**: Relies on visual outward-square orientation (the exact 6 topological lemmas LeanEuclid had to prove explicitly in Prop47.lean:25-60).

GEOMETOR (geometor.model + Ecosystem) (``geometor_model``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``geometor.model.invariants & geometor.wildberger``

.. code-block:: python

   m.assert_perpendicular((c, a), (c, b), at=c, by="I.47")  # line_spread == 1
   assert zero_test(quadrance(a, b) - (quadrance(a, c) + quadrance(b, c)))
   # Plus cut-and-paste Bride's Chair area verification:
   m.assert_area_equal(hyp_square, leg_poly_union, by="I.47")

* **Reveals**: Supports BOTH Wildberger's polynomial Pythagoras Law (s(CA, CB) = 1 <=> Q\_c = Q\_a + Q\_b) AND Euclid's exact polygon-area Bride's Chair proof (assert\_area\_equal)!
* **Hides**: None—this dual algebraic + dissection capability is a signature strength of GEOMETOR.

