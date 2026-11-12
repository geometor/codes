:order: 5

.. _rosetta-05-triangle-centers:

==============================================================
Benchmark 5: Classical Triangle Centers X(1)-X(5) & Euler Line
==============================================================

* **Canonical GEOMETOR Signature**: ``triangle_centers(A, B, C) -> (X1, X2, X3, X4, X5, euler_line)``
* **Classical Citation**: *Euclid Book IV.4-5 + Euler (1765) + Feuerbach (1822) + Kimberling ETC*
* **Core Phenomenon**: Construct Incenter X(1), Centroid X(2), Circumcenter X(3), Orthocenter X(4), and Nine-Point Center X(5), verifying concurrency of bisectors/medians/altitudes, the 9-point circle, and the Euler line relation X(4) - X(3) = 3(X(2) - X(3)).

.. figure:: /_static/figures/08-rosetta-centers-euler.svg
   :align: center
   :width: 100%

   Exact float-free ``geometor.model`` construction illustrating **Classical Triangle Centers X(1)-X(5) & Euler Line** (``triangle_centers(A, B, C) -> (X1, X2, X3, X4, X5, euler_line)``).

Cross-System Revelation Matrix
------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - System
     - What This Encoding Reveals
     - What This Encoding Hides
   * - **LeanEuclid & Formal System E**
     - Exposes the sharp scope boundary of Book-I-only formalizations.
     - All classical triangle geometry beyond congruence and parallelograms.
   * - **GeoCoq (Tarski / Hilbert / Euclid)**
     - Proves X(1)-X(4) concurrencies and Euler collinearity in pure synthetic Tarski geometry.
     - Omits the Nine-Point Circle X(5), omits the 2:1 Euler ratio in euler\_line.v, and stops at 4 centers.
   * - **Lean 4 Mathlib (Euclidean & Affine)**
     - Breathtaking n-dimensional unification: proves the Monge point, Euler vector ratio 3:1, and 3(n+1)-point sphere simultaneously for triangles, tetrahedra, and n-simplices!
     - Noncomputable (uses Classical.choose on circumsphere); stops after ~6 centers (plus SouthPole/Brocard).
   * - **AlphaGeometry (DD + AR)**
     - Proves Euler line and 9-point concyclicity automatically once feet/midpoints are present; also reveals two subtle ceilings: 3-median concurrency needs 1 aux mirror point, and incenter = excenter mod π!
     - Lacks Hypotenuse-Leg congruence rule in r00-r42 for bare 2-bisector incenter proof.
   * - **Newclid & Yuclid**
     - Closes AlphaGeometry's center-concurrency and Hypotenuse-Leg rule gaps cleanly.
     - Limited to classical Olympiad centers.
   * - **Java Geometry Expert (JGEX / Area Method)**
     - Gives the shortest algebraic proof of orthocenter concurrency in all of mathematics: the 3-term Jacobi identity on P\_ABCD!
     - Incenter requires square-root side lengths, outside rational Area-Method polynomials.
   * - **Projective & Conformal Geometric Algebra (kingdon / galgebra)**
     - In 2D CGA, the circumcenter of A, B, C is literally the reflection of the point at infinity ni in the circle blade A ^ B ^ C!
     - Barycentric centers beyond X(1)-X(5) must be lifted back onto the null cone via S - 0.5\*(S\|S)\*ni.
   * - **CindyJS (Complex Projective CP^2 & Cayley-Klein)**
     - In CP^2, the center of ANY circle or conic C is simply adj(C) \* linf—the pole of the line at infinity!
     - Numerical float coordinates.
   * - **SymPy Geometry (sympy.geometry 1.14.0)**
     - Built-in X(1)-X(5) and eulerline—AND exposes a critical live double bug in Triangle.excenters (missing parentheses + wrong vertex index)!
     - Eager simplify() slows symbolic triangles; stops at classical textbook centers.
   * - **Oliver Byrne's Coloured Euclid (1847 / Rougeux)**
     - Elegantly visualizes IV.4 incircle and IV.5 circumcircle radii congruence.
     - Exposes Byrne's combinatorial palette wall: overlaid classical centers (X(1)..X(5) + 9-point circle + 3 medians + 3 altitudes) exceed 4-colour perceptual disambiguation.
   * - **GEOMETOR (geometor.model + Ecosystem)**
     - Unites pure compass-and-straightedge construction of X(1)-X(5) (verified over Q on the 13-14-15 Heronian triangle!) with geometor.etc's encyclopedic symbolic registry of tens of thousands of centers.
     - None—GEOMETOR leads every surveyed system in symbolic triangle-center breadth.

Side-by-Side Formal & Visual Implementations (11 Systems)
---------------------------------------------------------

LeanEuclid & Formal System E (``leaneuclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``ABSENT across all 235 files in LeanEuclid!``

.. code-block:: lean4

   -- OMITTED: LeanEuclid stops at Euclid Book I Prop 48.
   -- Book IV (incenter IV.4, circumcenter IV.5) and Highschool centers
   -- (centroid, orthocenter, nine-point circle, Euler line) do not exist in LeanEuclid.

* **Reveals**: Exposes the sharp scope boundary of Book-I-only formalizations.
* **Hides**: All classical triangle geometry beyond congruence and parallelograms.

GeoCoq (Tarski / Hilbert / Euclid) (``geocoq``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``GeoCoq/Main/Highschool/{incenter,centroid,circumcenter,orthocenter,euler_line}.v``

.. code-block:: coq

   Theorem euler_line : forall A B C G O H,
     ~ Col A B C -> is_gravity_center G A B C ->
     is_circumcenter O A B C -> is_orthocenter H A B C -> Col O G H.
   (* X(1)..X(4) & Euler collinearity proven; X(5) Nine-Point Circle is ABSENT! *)

* **Reveals**: Proves X(1)-X(4) concurrencies and Euler collinearity in pure synthetic Tarski geometry.
* **Hides**: Omits the Nine-Point Circle X(5), omits the 2:1 Euler ratio in euler\_line.v, and stops at 4 centers.

Lean 4 Mathlib (Euclidean & Affine) (``mathlib4``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Mathlib/Geometry/Euclidean/{Circumcenter,Incenter/Basic,MongePoint,NinePointCircle}.lean``

.. code-block:: lean4

   -- Generalizes orthocenter (mongePoint) and 3(n+1)-point sphere to n-simplices!
   theorem ninePointCenter_eq_midpoint (t : Simplex ℝ P n) ... :
       t.ninePointCenter = midpoint ℝ t.circumcenter t.mongePoint
   theorem mongePoint_vsub_circumcenter (t : Triangle ℝ P) :
       t.mongePoint -ᵥ t.circumcenter = (3 : ℝ) • (centroid ℝ _ t.points -ᵥ t.circumcenter)

* **Reveals**: Breathtaking n-dimensional unification: proves the Monge point, Euler vector ratio 3:1, and 3(n+1)-point sphere simultaneously for triangles, tetrahedra, and n-simplices!
* **Hides**: Noncomputable (uses Classical.choose on circumsphere); stops after ~6 centers (plus SouthPole/Brocard).

AlphaGeometry (DD + AR) (``alphageometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``alphageometry/examples.txt:8 & defs.txt:73-108``

.. code-block:: text

   a b c = triangle a b c; h = orthocenter a b c; h1 = foot a b c; h2 = foot b c a; h3 = foot c a b; g1 g2 g3 g = centroid g1 g2 g3 g a b c; o = circle a b c ? coll h g o

* **Reveals**: Proves Euler line and 9-point concyclicity automatically once feet/midpoints are present; also reveals two subtle ceilings: 3-median concurrency needs 1 aux mirror point, and incenter = excenter mod π!
* **Hides**: Lacks Hypotenuse-Leg congruence rule in r00-r42 for bare 2-bisector incenter proof.

Newclid & Yuclid (``newclid``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Newclid/newclid/src/newclid/all_rules.py:553-623 (R43, R46, R47, R48)``

.. code-block:: text

   # Explicitly adds R43 (orthocenter), R46 (incenter), R47 (circumcenter), R48 (centroid)
   # plus R52/R53 Hypotenuse-Leg right congruence!
   a b c = triangle a b c; x = angle_bisector x b a c, angle_bisector x a b c ? eqangle c b c x c x c a

* **Reveals**: Closes AlphaGeometry's center-concurrency and Hypotenuse-Leg rule gaps cleanly.
* **Hides**: Limited to classical Olympiad centers.

Java Geometry Expert (JGEX / Area Method) (``jgex``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Java-Geometry-Expert/.../exs-book/ch3:3-10 (ORTH) & ch3:117-124 (A_201)``

.. code-block:: text

   # Orthocenter via Jacobi Pythagoras identity (ZERO elimination steps!):
   # P_ACHB + P_BAHC + P_CBAH == 0; given AH ⊥ BC (P_BAHC=0) & BH ⊥ AC (P_CBAH=0) => P_ACHB = 0!

* **Reveals**: Gives the shortest algebraic proof of orthocenter concurrency in all of mathematics: the 3-term Jacobi identity on P\_ABCD!
* **Hides**: Incenter requires square-root side lengths, outside rational Area-Method polynomials.

Projective & Conformal Geometric Algebra (kingdon / galgebra) (``pga_cga``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``2D PGA Cl(2,0,1) & 2D CGA Cl(3,1) in kingdon``

.. code-block:: python

   # 2D PGA division-free X3 & X4:
   la, lb = B & C, C & A
   X3 = (la | (B + C)) ^ (lb | (C + A))
   X4 = (la | A) ^ (lb | B)
   # 2D CGA Circumcenter = conformal reflection of infinity ni in circumcircle A ^ B ^ C!
   C_circ = A ^ B ^ C;  X3_cga = norm_pt(C_circ * ni * ~C_circ)

* **Reveals**: In 2D CGA, the circumcenter of A, B, C is literally the reflection of the point at infinity ni in the circle blade A ^ B ^ C!
* **Hides**: Barycentric centers beyond X(1)-X(5) must be lifted back onto the null cone via S - 0.5\*(S\|S)\*ni.

CindyJS (Complex Projective CP^2 & Cayley-Klein) (``cindyjs``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``CindyJS CP^2 Homogeneous Algebra``

.. code-block:: javascript

   X1 = dist(B,C)*A + dist(C,A)*B + dist(A,B)*C;
   X2 = A + B + C;
   X3 = adjoint3(CircleBy3(A, B, C)) * linf;  // pole of line at infinity!

* **Reveals**: In CP^2, the center of ANY circle or conic C is simply adj(C) \* linf—the pole of the line at infinity!
* **Hides**: Numerical float coordinates.

SymPy Geometry (sympy.geometry 1.14.0) (``sympy_geometry``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``sympy/geometry/polygon.py:2460-2765 (WARNING: excenters BUG at L2714!)``

.. code-block:: python

   tri = Triangle(A, B, C)
   X1, X2, X3, X4 = tri.incenter, tri.centroid, tri.circumcenter, tri.orthocenter
   X5 = tri.nine_point_circle.center
   # BUG in sympy 1.14.0 polygon.py:2714: tri.excenters omits parentheses:
   # simplify(-a*x[0] + b*x[1] + c*x[2]/(-a+b+c)) + wrong side-vertex index!

* **Reveals**: Built-in X(1)-X(5) and eulerline—AND exposes a critical live double bug in Triangle.excenters (missing parentheses + wrong vertex index)!
* **Hides**: Eager simplify() slows symbolic triangles; stops at classical textbook centers.

Oliver Byrne's Coloured Euclid (1847 / Rougeux) (``byrne_1847``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``Byrne (1847) Book IV, Props. 4 & 5 (Incircle & Circumcircle only)``

.. code-block:: text

   # Book IV.4 (Incircle) & Book IV.5 (Circumcircle) rendered in 4 colours:
   # Bisect two wedges -> drop 3 dashed perpendicular radii [red ╌╌╌] = [blue ╌╌╌] = [yellow ╌╌╌]
   # OMITTED: Centroid X(2), Orthocenter X(4), Nine-Point Circle X(5), Euler Line!

* **Reveals**: Elegantly visualizes IV.4 incircle and IV.5 circumcircle radii congruence.
* **Hides**: Exposes Byrne's combinatorial palette wall: overlaid classical centers (X(1)..X(5) + 9-point circle + 3 medians + 3 altitudes) exceed 4-colour perceptual disambiguation.

GEOMETOR (geometor.model + Ecosystem) (``geometor_model``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*Source / Reference*: ``geometor/codes/figures.py:356-441 & geometor.etc (X(1)-X(53144))``

.. code-block:: python

   # Heronian 13-14-15 triangle A(0,0), B(14,0), C(5,12) -> ALL X(1)..X(5) exact Rationals:
   # X1=(6, 4), X2=(19/3, 4), X3=(7, 33/8), X4=(5, 15/4), X5=(6, 63/16)
   m.assert_equal((x3, a), (x3, b), (x3, c), by="IV.5")
   m.assert_equal((x5, ma), (x5, mb), (x5, mc), (x5, hc), by="NinePoint")
   # Paired with geometor.etc CenterSymbolicRegistry spanning Kimberling X(1)..X(53144)!

* **Reveals**: Unites pure compass-and-straightedge construction of X(1)-X(5) (verified over Q on the 13-14-15 Heronian triangle!) with geometor.etc's encyclopedic symbolic registry of tens of thousands of centers.
* **Hides**: None—GEOMETOR leads every surveyed system in symbolic triangle-center breadth.

