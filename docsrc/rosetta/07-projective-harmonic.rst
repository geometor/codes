:order: 7

.. _rosetta-07-projective-harmonic:

==================================================================
Benchmark 7: Projective Collinearity, Cross-Ratio & Pappus Hexagon
==================================================================

* **Canonical GEOMETOR Signature**: ``pappus_hexagon(A1, B1, C1, A2, B2, C2) -> collinear(X, Y, Z)``
* **Classical Citation**: *Pappus Synagoge VII.139 + Desargues (1639) + Projective Harmonic Ranges*
* **Core Phenomenon**: Given collinear triples (A1, B1, C1) and (A2, B2, C2), opposite-side intersections X = A1B2 ∩ A2B1, Y = A1C2 ∩ A2C1, Z = B1C2 ∩ B2C1 lie on the Pappus axis, and central projection preserves the 4-point cross-ratio CR(A, B; C, D). Separates projective-native engines from metric-bound ones!

.. figure:: /_static/figures/09-rosetta-pappus-harmonic.svg
   :align: center
   :width: 100%

   Exact float-free ``geometor.model`` construction illustrating **Projective Collinearity, Cross-Ratio & Pappus Hexagon** (``pappus_hexagon(A1, B1, C1, A2, B2, C2) -> collinear(X, Y, Z)``).

Cross-System Revelation Matrix
------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - System
     - What This Encoding Reveals
     - What This Encoding Hides
   * - **LeanEuclid & Formal System E**
     - Pure Book-I diagrammatic axioms lack Menelaus/projective invariants.
     - All projective geometry.
   * - **GeoCoq (Tarski / Hilbert / Euclid)**
     - Deep foundational role of Pappus (gives field commutativity ab = ba!) and Desargues (gives associativity!) in Hilbert-Tarski coordinatization.
     - Formalizes the affine parallel versions for segment multiplication rather than full RP^2 general-intersection Pappus or cross-ratio.
   * - **Lean 4 Mathlib (Euclidean & Affine)**
     - Major Opus discovery: despite world-class Euclidean sphere coverage, mathlib4 currently has a wide-open classical projective geometry gap!
     - Pappus, Desargues, Pascal, harmonic conjugates, and projective cross-ratio.
   * - **AlphaGeometry (DD + AR)**
     - Profound insight into DD+AR: Pappus and Desargues are 1-line statements, yet bare DD+AR cannot prove them without LM-invented auxiliary parallel lines because r00-r42 lack Menelaus!
     - General 4-factor cross-ratio also cannot be stated as a single 8-point eqratio unless specialized to harmonic range (-1).
   * - **Newclid & Yuclid**
     - Confirms the DD+AR projective ceiling: Newclid had to hardcode Pappus (R44) and Quadrangle Harmonic Conjugate (R70) directly into all\_rules.py as primitive Horn rules!
     - Adding projective theorems one-by-one as axioms does not provide general Grassmann-Plücker elimination.
   * - **Java Geometry Expert (JGEX / Area Method)**
     - Whereas DD+AR stalls on Pappus and cross-ratio, Chou-Gao-Zhang's Area Method eliminates intersection points linearly via S\_ABC ratios and proves both with ZERO auxiliary points!
     - Requires explicit NDG checks when opposite sides are parallel.
   * - **Projective & Conformal Geometric Algebra (kingdon / galgebra)**
     - Zero divisions, zero case splits: even if A1B2 \|\| A2B1, X is a valid ideal Direction bivector and (X & Y & Z).e == 0 still holds identically!
     - Pure polynomial algebra hides the synthetic Menelaus ratio chain.
   * - **CindyJS (Complex Projective CP^2 & Cayley-Klein)**
     - Identical 3D cross-product polynomial identity over CP^2, certified over C^3 by Prover.js.
     - Probabilistic float prover rather than symbolic polynomial expansion.
   * - **SymPy Geometry (sympy.geometry 1.14.0)**
     - Exposes both affine fragility (parallel lines crash Pappus) and the live 2-digit float zero-test bug in Point.affine\_rank!
     - Entire projective plane RP^2 / CP^2.
   * - **Oliver Byrne's Coloured Euclid (1847 / Rougeux)**
     - Sharp formal-language boundary: pure 0D point-incidence configurations (Pappus, Desargues) require symbolic point identifiers or homogeneous blades, not coloured regions.
     - All projective incidence and cross-ratio geometry.
   * - **GEOMETOR (geometor.model + Ecosystem)**
     - Combines exact affine DAG construction + cross\_ratio / is\_harmonic in geometor.model with full homogeneous RP^2 meet/join (handling ideal points at infinity) and Q(phi) projectivity in geometor.pappus!
     - Minor convention note: standardize cross\_ratio argument ordering across geometor.model.invariants and geometor.pappus.projective.

Side-by-Side Formal & Visual Implementations (11 Systems)
---------------------------------------------------------

LeanEuclid & Formal System E (``leaneuclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``ABSENT across LeanEuclid``

.. code-block:: lean4

   -- OMITTED: Projective incidence theorems (Pappus, Desargues) and cross-ratios
   -- do not exist in LeanEuclid.

* **Reveals**: Pure Book-I diagrammatic axioms lack Menelaus/projective invariants.
* **Hides**: All projective geometry.

GeoCoq (Tarski / Hilbert / Euclid) (``geocoq``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``GeoCoq/Main/Tarski_dev/Ch13_5_Pappus_Pascal.v & Ch13_6_Desargues_Hessenberg.v``

.. code-block:: coq

   (* Proves AFFINE parallel-case Pappus & Desargues (where opposite sides are
      parallel Par A B' B A' /\ Par B C' C B' -> Par A C' C A') to bootstrap
      commutativity and associativity of Tarski's geometric field multiplication! *)

* **Reveals**: Deep foundational role of Pappus (gives field commutativity ab = ba!) and Desargues (gives associativity!) in Hilbert-Tarski coordinatization.
* **Hides**: Formalizes the affine parallel versions for segment multiplication rather than full RP^2 general-intersection Pappus or cross-ratio.

Lean 4 Mathlib (Euclidean & Affine) (``mathlib4``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``SURPRISINGLY ABSENT in Mathlib/Geometry/ & LinearAlgebra/Projective/!``

.. code-block:: lean4

   -- Mathlib defines Projectivization K V (LinearAlgebra/Projective/Basic.lean),
   -- yet has ZERO Pappus, ZERO Desargues, ZERO Menelaus, and ZERO crossRatio!

* **Reveals**: Major Opus discovery: despite world-class Euclidean sphere coverage, mathlib4 currently has a wide-open classical projective geometry gap!
* **Hides**: Pappus, Desargues, Pascal, harmonic conjugates, and projective cross-ratio.

AlphaGeometry (DD + AR) (``alphageometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Deductive Ceiling! Expressible in 1 line, UNPROVABLE by bare DD+AR!``

.. code-block:: text

   a b a1 b1 = quadrangle a b a1 b1; c = on_line c a b; c1 = on_line c1 a1 b1; p = intersection_ll p a b1 a1 b; q = intersection_ll q a c1 a1 c; s = intersection_ll s b c1 b1 c ? coll p q s
   # Bare DD+AR (r00-r42) FAILS to saturate: lacks Menelaus & signed-area ratios!

* **Reveals**: Profound insight into DD+AR: Pappus and Desargues are 1-line statements, yet bare DD+AR cannot prove them without LM-invented auxiliary parallel lines because r00-r42 lack Menelaus!
* **Hides**: General 4-factor cross-ratio also cannot be stated as a single 8-point eqratio unless specialized to harmonic range (-1).

Newclid & Yuclid (``newclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Newclid/newclid/tests/test_individual_rules.py:141 & 167 (R44 & R70!)``

.. code-block:: text

   # Added explicitly as primitive axioms R44_PAPPUS_THEOREM & R70_PROJECTIVE_HARMONIC_CONJUGATE!
   a b = segment a b; c = on_line c a b; p q = segment p q; r = on_line r p q; x = on_line x a q, on_line x p b; y = on_line y a r, on_line y p c; z = on_line z b r, on_line z c q ? coll x y z

* **Reveals**: Confirms the DD+AR projective ceiling: Newclid had to hardcode Pappus (R44) and Quadrangle Harmonic Conjugate (R70) directly into all\_rules.py as primitive Horn rules!
* **Hides**: Adding projective theorems one-by-one as axioms does not provide general Grassmann-Plücker elimination.

Java Geometry Expert (JGEX / Area Method) (``jgex``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Java-Geometry-Expert/.../exs-book/ch2:40-50 (PAPPUS) & ch3:38-48 (A_353)``

.. code-block:: text

   EXAMPLE A_353  # Projective Invariance of Harmonic Cross-Ratio:
     POINT O A B X Y; MRATIO C A B r; MRATIO D A B (-1 r);
     INTERSECTION_LL P O A X Y; INTERSECTION_LL Q O B X Y;
     INTERSECTION_LL R O C X Y; INTERSECTION_LL S O D X Y;
   SHOW: HARMONIC P Q S R.  # Automatic 0-aux-point Area-Method elimination!

* **Reveals**: Whereas DD+AR stalls on Pappus and cross-ratio, Chou-Gao-Zhang's Area Method eliminates intersection points linearly via S\_ABC ratios and proves both with ZERO auxiliary points!
* **Hides**: Requires explicit NDG checks when opposite sides are parallel.

Projective & Conformal Geometric Algebra (kingdon / galgebra) (``pga_cga``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``2D PGA Cl(2,0,1) in kingdon — Division-Free Grassmann-Cayley!``

.. code-block:: python

   X = (A1 & B2) ^ (A2 & B1)
   Y = (A1 & C2) ^ (A2 & C1)
   Z = (B1 & C2) ^ (B2 & C1)
   assert sp.expand((X & Y & Z).e) == 0   # holds even when opposite sides are parallel!
   cr = ((A & C) | (B & D)).e / ((A & D) | (B & C)).e

* **Reveals**: Zero divisions, zero case splits: even if A1B2 \|\| A2B1, X is a valid ideal Direction bivector and (X & Y & Z).e == 0 still holds identically!
* **Hides**: Pure polynomial algebra hides the synthetic Menelaus ratio chain.

CindyJS (Complex Projective CP^2 & Cayley-Klein) (``cindyjs``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``CindyJS/src/js/libcs/Operators.js:2474-2497 & Prover.js``

.. code-block:: javascript

   X = cross(cross(A1, B2), cross(A2, B1));
   Y = cross(cross(A1, C2), cross(A2, C1));
   Z = cross(cross(B1, C2), cross(B2, C1));
   det(X, Y, Z) == 0;                     // + native crossratio(A, B, C, D)

* **Reveals**: Identical 3D cross-product polynomial identity over CP^2, certified over C^3 by Prover.js.
* **Hides**: Probabilistic float prover rather than symbolic polynomial expansion.

SymPy Geometry (sympy.geometry 1.14.0) (``sympy_geometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``sympy/geometry/point.py:331-335 (Point.affine_rank BUG!)``

.. code-block:: python

   # 1. NO cross_ratio in sympy.geometry!
   # 2. Crashes with IndexError if A1B2 || A2B1 (Line.intersection returns []!)
   # 3. Point.is_collinear calls affine_rank with abs(x.n(2)) < 1e-12,
   #    falsely reporting Point(0,0), Point(1,0), Point(1, Rational(1, 10**13)) collinear!

* **Reveals**: Exposes both affine fragility (parallel lines crash Pappus) and the live 2-digit float zero-test bug in Point.affine\_rank!
* **Hides**: Entire projective plane RP^2 / CP^2.

Oliver Byrne's Coloured Euclid (1847 / Rougeux) (``byrne_1847``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``ABSENT (Byrne stops at Book VI; Books V-VI use :: ribbon proportions)``

.. code-block:: text

   # OMITTED: Projective Pappus, Desargues, and cross-ratios do not appear in Books I-VI.
   # Structural Language Insight: Pappus (9 points, 9 lines, 0 regions/angles) is the
   # worst-case adversarial figure for a point-free chromatic region/segment DSL!

* **Reveals**: Sharp formal-language boundary: pure 0D point-incidence configurations (Pappus, Desargues) require symbolic point identifiers or homogeneous blades, not coloured regions.
* **Hides**: All projective incidence and cross-ratio geometry.

GEOMETOR (geometor.model + Ecosystem) (``geometor_model``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``geometor/codes/figures.py:444-488 & geometor.pappus``

.. code-block:: python

   x = m.intersect(m.construct_line(a1, b2), m.construct_line(a2, b1), ID="X")
   y = m.intersect(m.construct_line(a1, c2), m.construct_line(a2, c1), ID="Y")
   z = m.intersect(m.construct_line(b1, c2), m.construct_line(b2, c1), ID="Z")
   assert zero_test(signed_area2(x, y, z))              # Pappus collinearity
   assert is_harmonic(o, b1, a1, c1)                    # CR == -1
   # Plus homogeneous RP^2 meet/join & Pascal's Mystic Hexagram in geometor.pappus!

* **Reveals**: Combines exact affine DAG construction + cross\_ratio / is\_harmonic in geometor.model with full homogeneous RP^2 meet/join (handling ideal points at infinity) and Q(phi) projectivity in geometor.pappus!
* **Hides**: Minor convention note: standardize cross\_ratio argument ordering across geometor.model.invariants and geometor.pappus.projective.

