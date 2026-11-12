:navigation: header
:order: 40

.. _rosetta-index:

========================
Rosetta Stone Benchmarks
========================

Abstract descriptions of formal languages only go so far. To expose the true ontology, elegance, verbosity, and expressiveness ceilings of each architecture, we encode **seven canonical geometric constructions and theorems** side-by-side across all **11 surveyed systems** (``77`` annotated implementations) paired with exact ``geometor.model`` ``.euclid-graphic`` SVGs.

.. list-table::
   :widths: 8 28 30 34
   :header-rows: 1

   * - #
     - Benchmark
     - GEOMETOR Signature
     - Architectural Stress Test
   * - 1
     - :ref:`Equidistant Poles & Equilateral Triangle <rosetta-01-equidistant-poles>`
     - ``equidistant_poles(A, B) -> (F, E)``
     - From two distinct seed points A and B, construct the two congruent circles (A, B) and (B, A) and select their intersection poles F and E to form equilateral triangle ABF. Tests whether a system can actually prove circle-circle intersection existence and select one of the two quadratic roots.
   * - 2
     - :ref:`Perpendicular Bisector & Midpoint <rosetta-02-perpendicular-bisector-midpoint>`
     - ``perpendicular_bisector(A, B) -> (bisector, midpoint)``
     - Join the two equidistant vesica poles F and E of (A, B) and (B, A) to obtain the perpendicular bisector [E F] and intersect with [A B] to obtain the midpoint M. Contrasts synthetic kite/congruence proofs against 1-subtraction conformal duals.
   * - 3
     - :ref:`Parallel Line Through an External Point <rosetta-03-parallel-line>`
     - ``parallel_line(line_AB, P) -> line_parallel``
     - Construct the unique Euclidean line through external point P parallel to line AB. Exposes how each system treats the Parallel Postulate, points at infinity, alternate interior angles, or rhombus symmetry.
   * - 4
     - :ref:`Pythagorean Theorem & Right-Triangle Orthogonality <rosetta-04-pythagoras>`
     - ``pythagoras(A, B, C) -> Q(A, B) == Q(A, C) + Q(B, C)``
     - For right-angled triangle ABC (orthogonality at C), the quadrance on the hypotenuse equals the sum of the quadrances on the legs—and geometrically, the area of the hypotenuse square equals the sum of the two leg squares (Euclid's Bride's Chair). Exposes a stunning expressiveness cliff in AlphaGeometry!
   * - 5
     - :ref:`Classical Triangle Centers X(1)-X(5) & Euler Line <rosetta-05-triangle-centers>`
     - ``triangle_centers(A, B, C) -> (X1, X2, X3, X4, X5, euler_line)``
     - Construct Incenter X(1), Centroid X(2), Circumcenter X(3), Orthocenter X(4), and Nine-Point Center X(5), verifying concurrency of bisectors/medians/altitudes, the 9-point circle, and the Euler line relation X(4) - X(3) = 3(X(2) - X(3)).
   * - 6
     - :ref:`Circle Power, Radical Axis, Inversion & Pole-Polar <rosetta-06-circle-power-inversion-polar>`
     - ``circle_inversion_polar(omega, P) -> (power, P_inv, polar_line)``
     - For circle Ω(O, R) and point P: Steiner power \|OP\|^2 - R^2, radical axis of two circles, inverse point P' on ray OP with \|OP\|·\|OP'\| = R^2, and polar line through P' perpendicular to OP satisfying La Hire's reciprocity (Q on polar(P) <=> P on polar(Q)) and harmonic range (R-, R+; P', P) = -1.
   * - 7
     - :ref:`Projective Collinearity, Cross-Ratio & Pappus Hexagon <rosetta-07-projective-harmonic>`
     - ``pappus_hexagon(A1, B1, C1, A2, B2, C2) -> collinear(X, Y, Z)``
     - Given collinear triples (A1, B1, C1) and (A2, B2, C2), opposite-side intersections X = A1B2 ∩ A2B1, Y = A1C2 ∩ A2C1, Z = B1C2 ∩ B2C1 lie on the Pappus axis, and central projection preserves the 4-point cross-ratio CR(A, B; C, D). Separates projective-native engines from metric-bound ones!

.. toctree::
   :maxdepth: 1
   :hidden:

   01-equidistant-poles
   02-perpendicular-bisector-midpoint
   03-parallel-line
   04-pythagoras
   05-triangle-centers
   06-circle-power-inversion-polar
   07-projective-harmonic
