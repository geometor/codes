:navigation: header
:order: 50

.. _opus-index:

=============================================
Opus Coverage Matrix (69 Topics x 11 Systems)
=============================================

What portion of the classical and modern geometric canon—the **Opus**—has actually been formalized across interactive theorem provers, Olympiad deduction engines, Clifford algebras, visual pseudocodes, and symbolic CAS libraries? Below is our complete **69-topic across 8 domains** audit (``759`` cells), using canonical ``snake_case`` identifiers aligned with GEOMETOR's *Principles of Geometry* (``elements`` 2.0).

Quantitative Coverage Scoreboard (Across 69 Canonical Topics)
-------------------------------------------------------------

.. list-table::
   :widths: 28 14 14 14 14 16
   :header-rows: 1

   * - System
     - Native
     - Derived
     - Partial
     - Broken
     - Absent
   * - **LeanEuclid & Formal System E** (``leaneuclid``)
     - **19**
     - 2
     - 2
     - 0
     - 46
   * - **GeoCoq (Tarski / Hilbert / Euclid)** (``geocoq``)
     - **27**
     - 8
     - 9
     - 0
     - 25
   * - **Lean 4 Mathlib (Euclidean & Affine)** (``mathlib4``)
     - **34**
     - 6
     - 9
     - 0
     - 20
   * - **AlphaGeometry (DD + AR)** (``alphageometry``)
     - **23**
     - 4
     - 22
     - 0
     - 20
   * - **Newclid & Yuclid** (``newclid``)
     - **30**
     - 4
     - 21
     - 0
     - 14
   * - **Java Geometry Expert (JGEX / Area Method)** (``jgex``)
     - **48**
     - 3
     - 4
     - 0
     - 14
   * - **Projective & Conformal Geometric Algebra (kingdon / galgebra)** (``pga_cga``)
     - **36**
     - 22
     - 4
     - 0
     - 7
   * - **CindyJS (Complex Projective CP^2 & Cayley-Klein)** (``cindyjs``)
     - **44**
     - 14
     - 6
     - 0
     - 5
   * - **SymPy Geometry (sympy.geometry 1.14.0)** (``sympy_geometry``)
     - **22**
     - 13
     - 7
     - 2
     - 25
   * - **Oliver Byrne's Coloured Euclid (1847 / Rougeux)** (``byrne_1847``)
     - **27**
     - 1
     - 11
     - 0
     - 30
   * - **GEOMETOR (geometor.model + Ecosystem)** (``geometor_model``)
     - **53**
     - 10
     - 6
     - 0
     - 0

Six Structural Blind Spots Exposed by the Opus Matrix
-----------------------------------------------------

1. **The Golden Ratio & Polyhedral Blind Spot (Domain 8)**: Across ``LeanEuclid``, ``GeoCoq``, ``mathlib4`` Geometry, ``AlphaGeometry``, and ``Newclid``, division in extreme and mean ratio (:math:`\phi`, Euclid ``II.11`` & ``VI.30``), the 5-step vesica golden chain, and the five Platonic solids (``Book XIII``) have **zero** geometric theorems—whereas :person:`Oliver Byrne <byrne>` (``1847``) formalized ``II.11``, ``IV.10–11``, and ``VI.30`` in primary colors, and GEOMETOR (``model``, ``fundamentals``, ``divine``, ``pacioli``, ``kepler``, ``euclid``) treats :math:`\mathbb{Q}(\phi)` as foundational DNA.
2. **The General Conic Desert (Domain 6)**: Among all 10 external systems, **only ``CindyJS``** represents general rotated ellipses, parabolas, and hyperbolas uniformly via :math:`3\times 3` symmetric matrices and Plücker 5-point pencils (``ConicBy5``). ``sympy.geometry`` lacks ``Hyperbola`` altogether and raises ``NotImplementedError`` on rotated ``Ellipse``.
3. **The Coaxial & Inversive Gap (Domain 4)**: ``GeoCoq`` (``4,671`` lemmas) and ``sympy.geometry`` have **zero** circle power, radical axis, inversion, or pole–polar support, and even ``mathlib4`` (which shines on ``Sphere.power`` and ``PolePolar``) omits ``radicalAxis``! Meanwhile, 2D CGA (``kingdon``) expresses radical axis as ``kappa1 - kappa2`` and circle inversion as ``C >> P``.
4. **The Projective Cross-Ratio & Pappus Wall (Domain 6)**: ``mathlib4`` and ``sympy.geometry`` both lack ``cross_ratio``, ``Pappus``, ``Desargues``, and ``Menelaus``, while bare ``AlphaGeometry`` ``DD+AR`` cannot prove Pappus without auxiliary parallel lines.
5. **Triangle Centers Beyond Textbook Classics (Domain 5)**: External systems top out between ``0`` centers (``LeanEuclid``), ``2`` (``Byrne``), ``4`` (``GeoCoq``), and ``6`` (``mathlib4``, ``AlphaGeometry``), and ``sympy.geometry`` ``1.14.0`` has a **live double bug in ``Triangle.excenters``**—leaving ``geometor.etc`` (``X(1)``–``X(53144)``) unmatched.
6. **Operational Construction Complexity (Domain 7)**: Zero external systems measure :person:`Émile Lemoine <lemoine>`'s *Géométrographie* (``R1, R2, C1, C2, C3``), positioning ``geometor.model`` + ``geometor/lemoine`` to own constructive complexity analysis.


Domain 1 — Axiomatic & Topological Foundations
----------------------------------------------

Points, lines, circles, betweenness, plane separation (Pasch), continuity intersections, and root selection.

.. list-table::
   :header-rows: 1

   * - Canonical Topic (``snake_case``)
     - LeanEuc
     - GeoCoq
     - Mathlib
     - AlphaG
     - Newclid
     - JGEX
     - PGA/CGA
     - CindyJS
     - SymPy
     - Byrne
     - GEOMETOR
   * - **Point Primitive & Constructibility** (``point_primitive``)
     - **native**: Point : Type
     - **native**: Tpoint : Type
     - **native**: P : Type\* [NormedAddTorsor V P]
     - **native**: gm.Point / free
     - **native**: Point / free
     - **native**: POINT
     - **native**: bivector (PGA) / null vector (CGA)
     - **native**: homog [x, y, z] in CP^2
     - **native**: Point2D / Point3D
     - *partial*: Implicit vertex intersections (no point glyph!)
     - **native**: Model.set\_point (exact Q/ANP)
   * - **Line Joining Two Distinct Points (Postulate 1)** (``line_join``)
     - **native**: Lines.from\_points
     - derived: Col A B X (point-only)
     - **native**: line[ℝ, p₁, p₂]
     - **native**: on\_line / gm.Line
     - **native**: on\_line
     - **native**: LINE / ON\_LINE
     - **native**: P1 & P2 (PGA) / P1^P2^ni (CGA)
     - **native**: List.cross(A, B)
     - **native**: Line(p1, p2)
     - **native**: Byrne Postulate 1 ([coloured ━━] glyph)
     - **native**: Model.construct\_line
   * - **Circle from Center and Radius Point (Postulate 3)** (``circle_center_point``)
     - **native**: Circles.from\_points
     - derived: Cong O X O A / OnCirc
     - **native**: Sphere.mk center radius
     - **native**: on\_circle
     - **native**: on\_circle
     - **native**: CIRCLE / ON\_CIRCLE
     - **native**: A - 0.5\*q\*ni (2D CGA)
     - **native**: CircleMP(A, B)
     - **native**: Circle(A, A.distance(B))
     - **native**: Byrne Postulate 3 (coloured circle/ring)
     - **native**: Model.construct\_circle
   * - **Collinear Betweenness Order** (``collinear_betweenness``)
     - **native**: between a b c (strict)
     - **native**: Bet A B C (non-strict)
     - **native**: Wbtw ℝ a b c / Sbtw ℝ a b c
     - *partial*: sameside (float guard)
     - derived: between / sameside (float)
     - derived: LRATIO / signed r
     - derived: oriented weight ratio
     - *partial*: real-part param check
     - derived: Segment(a, c).contains(b)
     - *partial*: Visual diagram inspection only
     - **native**: between=(a, c) exact selector
   * - **Plane Separation & Pasch's Axiom** (``plane_separation_pasch``)
     - **native**: Point.sameSide / opposingSides
     - **native**: outer\_pasch / OS / TS
     - derived: AffineSubspace.SameSide / WeakSameSide
     - *partial*: sameclock (float guard)
     - *partial*: sameclock / nsameside (float)
     - derived: sign(S\_ABP \* S\_ABQ)
     - derived: sign((l ^ P) \* ~(l ^ Q))
     - *partial*: orientation det sign
     - —: No half-plane / Pasch API
     - *partial*: Implicit chromatic region topology
     - **native**: side\_of=(a, b, ±1) via signed\_area2
   * - **Line-Circle Intersection Existence** (``line_circle_continuity``)
     - **native**: Intersections.intersect\_line\_circle
     - **native**: segment\_circle (continuity\_axioms.v)
     - *partial*: Sphere.secondInter (analytic)
     - **native**: intersection\_lc (float sketch)
     - **native**: intersection\_lc
     - **native**: INTERSECTION\_LC
     - **native**: (L.dual() ^ kappa).dual() (CGA)
     - **native**: IntersectLC (always 2 in CP^2)
     - derived: Circle.intersection(Line) via solve()
     - *partial*: Visual diagram intersection
     - **native**: exact\_intersect\_line\_circle
   * - **Circle-Circle Intersection Existence (Euclid I.1 Gap)** (``circle_circle_continuity``)
     - **native**: Intersections.intersect\_circles
     - **native**: circle\_circle <-> segment\_circle
     - —: No 2D 2-point construction
     - **native**: intersection\_cc / HoleCircle
     - **native**: intersection\_cc
     - **native**: INTERSECTION\_CC
     - **native**: (kA ^ kB).dual() point-pair (CGA)
     - **native**: IntersectCirCir (via radical axis)
     - derived: Circle.intersection(Circle) via solve()
     - *partial*: Byrne I.1 visual circle overlap
     - **native**: exact\_intersect\_circle\_circle
   * - **Deterministic Quadratic Root Disambiguation** (``topological_root_selection``)
     - **native**: intersect\_circles\_same\_side / opposing
     - derived: TS / OS witness selection
     - *partial*: Sphere.secondInter (other\_than only)
     - *partial*: HoleCircle puncturing + @x\_y pin
     - *partial*: HoleCircle puncturing
     - *partial*: ordered root index
     - derived: projector (T ± sqrt(T^2))\*(T\|ni)
     - **native**: Tracing.js Riemann homotopy
     - —: Arbitrary solve() list order
     - **native**: Unique colour/stroke token disambiguation
     - **native**: side\_of, between, beyond, on\_ray, other\_than


Domain 2 — Congruence, Orthogonality & Metric Laws
--------------------------------------------------

Segment congruence, triangle congruence (SAS/SSS/ASA/HL), bisectors, perpendiculars, quadrance/spread, Pythagoras, and Stewart.

.. list-table::
   :header-rows: 1

   * - Canonical Topic (``snake_case``)
     - LeanEuc
     - GeoCoq
     - Mathlib
     - AlphaG
     - Newclid
     - JGEX
     - PGA/CGA
     - CindyJS
     - SymPy
     - Byrne
     - GEOMETOR
   * - **Equilateral Triangle Construction (Euclid I.1)** (``equilateral_triangle``)
     - **native**: Prop01.proposition\_1 / proposition\_1'
     - **native**: proposition\_01 / l10\_15
     - —: No constructive existence lemma
     - **native**: eq\_triangle / ieq\_triangle
     - **native**: eq\_triangle / ieq\_triangle
     - **native**: INTERSECTION\_CC + r13
     - **native**: CGA circle split / PGA pi/3 rotor
     - **native**: IntersectCirCir
     - derived: RegularPolygon / Circle.intersection
     - **native**: Byrne Book I, Prop. 1 (red/blue/black)
     - **native**: equidistant\_poles (figures.py)
   * - **Non-Collapsing Compass Segment Transfer (Euclid I.2-I.3)** (``segment_transfer``)
     - **native**: Prop02 / Prop03
     - **native**: segment\_construction (primitive axiom!)
     - derived: norm-scaled vadd
     - **native**: eqdistance
     - **native**: eqdistance / lconst
     - **native**: LRATIO / EQDISTANCE
     - **native**: translator / motor sandwich
     - **native**: Compass / CircleMP
     - derived: Circle(C, A.distance(B))
     - **native**: Byrne Book I, Props. 2-3
     - **native**: construct\_circle\_by\_length / I.2
   * - **Triangle Congruence (SAS, SSS, ASA / Euclid I.4, I.8, I.26)** (``triangle_congruence_sas_sss_asa``)
     - **native**: Prop04, Prop08, Prop26
     - **native**: l11\_49 (SAS), l11\_51 (SSS), l11\_50 (ASA)
     - **native**: Congruence.lean (dist/angle eq)
     - **native**: r32 (SSS), r33 (SAS), r36/r37 (ASA)
     - **native**: R64-R67 + R36-R37 (orientation split)
     - **native**: GDD contri rules
     - derived: isometry versor existence
     - derived: Prover.js metric identity
     - derived: Polygon congruence manual check
     - **native**: Byrne Book I, Props. 4, 8, 26
     - **native**: Model.assert\_congruent (Q + signed s)
   * - **Isosceles Base Angles — Pons Asinorum (Euclid I.5-I.6)** (``isosceles_pons_asinorum``)
     - **native**: Prop05 / Prop06
     - **native**: l11\_44\_1 / l11\_44\_2
     - **native**: angle\_eq\_angle\_of\_dist\_eq (Isosceles)
     - **native**: r13 / r14
     - **native**: R13 / R14
     - **native**: GDD r13 / Full-Angle
     - derived: reflection symmetry in bisector blade
     - derived: Laguerre angle symmetry
     - **native**: Triangle.is\_isosceles
     - **native**: Byrne Book I, Props. 5-6 (wedge sum)
     - **native**: Equal quadrance <=> equal spread
   * - **Right-Triangle Hypotenuse-Leg Congruence (HL)** (``hypotenuse_leg_congruence``)
     - derived: Via Prop47 + Prop08
     - **native**: Ch08 / Ch11 right congruence
     - derived: Via Pythagoras + SSS
     - —: Missing in r00-r42 (blocks bare incenter!)
     - **native**: R52 / R53 (explicitly added!)
     - **native**: Pythagoras difference P\_ABC
     - derived: Orthogonal quadrance subtraction
     - derived: Algebraic consequence
     - derived: Via distance/Pythagoras
     - derived: Via Byrne I.47 + I.8
     - **native**: Pythagoras Q\_b = Q\_c - Q\_a + assert\_congruent
   * - **Rectilinear Angle Bisector (Euclid I.9)** (``angle_bisector_construction``)
     - **native**: Prop09.proposition\_9 / proposition\_9'
     - **native**: angle\_bisector (Ch11\_angles.v)
     - **native**: Incenter/Basic.lean (oangle bisector)
     - *partial*: angle\_bisector (conflates ext bisector mod pi!)
     - *partial*: angle\_bisector (mod pi)
     - *partial*: BISECT (full-angle mod pi)
     - **native**: l1.normalized() ± l2.normalized() (PGA)
     - **native**: AngularBisector (2 orthogonal lines)
     - **native**: Line.bisectors() / Triangle.bisectors()
     - **native**: Byrne Book I, Prop. 9
     - **native**: Compass equilateral/midpoint bisector
   * - **Midpoint & Perpendicular Bisector (Euclid I.10-I.11)** (``midpoint_perpendicular_bisector``)
     - **native**: Prop10 / Prop11
     - **native**: midpoint\_existence (neutral, no circles!)
     - **native**: midpoint / perpBisector
     - **native**: midpoint / on\_bline / r22-r23
     - **native**: midpoint / on\_bline / R54
     - **native**: MIDPOINT / BLINE
     - **native**: (A&B)\|(A+B) (PGA) / A - B (CGA)
     - **native**: Midpoint / Perp
     - **native**: Segment.midpoint / perpendicular\_bisector
     - **native**: Byrne Book I, Props. 10-11
     - **native**: \_midpoint\_via\_vesica
   * - **Perpendicular Foot onto a Line (Euclid I.12)** (``dropped_perpendicular_foot``)
     - **native**: Prop12.proposition\_12
     - **native**: l8\_18\_existence (Ch08\_orthogonality.v)
     - **native**: orthogonalProjection s p
     - **native**: foot (defs.txt:61)
     - **native**: foot
     - **native**: FOOT (linear P\_PUV/P\_UVU elim!)
     - **native**: (l \| P) ^ l (2D PGA)
     - **native**: meet(L, perp(L, P))
     - **native**: Line.projection(P)
     - **native**: Byrne Book I, Prop. 12
     - **native**: Mirror-chord + vesica foot
   * - **Rational Quadrance & Spread Calculus (Wildberger)** (``quadrance_and_spread``)
     - —: Uses real length \|(a─b)\| & ∠(a:b:c)
     - —: Synthetic Cong & Angle CongA
     - derived: dist^2 & sin^2(angle) over R
     - —: Log-ratios & angles mod pi
     - *partial*: l2const / r2const (squared lengths only)
     - derived: P\_ABA = 2\*Q(A,B) & S\_ABC^2
     - derived: (l\|l) & (l1^l2)^2 / ((l1\|l1)\*(l2\|l2))
     - derived: Rational Cayley-Klein cross-ratio
     - —: Uses sqrt distance & acos angle
     - —: Visual segment/wedge icons, not polynomial Q/s
     - **native**: quadrance, line\_spread, vertex\_spread + wildberger
   * - **Pythagorean Theorem (Euclid I.47-I.48)** (``pythagorean_theorem``)
     - **native**: Prop47 / Prop48 (+ 6 missed lemmas)
     - **native**: pythagoras (Ch15\_lengths.v)
     - **native**: dist\_sq\_eq\_dist\_sq\_add\_dist\_sq\_iff...
     - *partial*: Cannot state a^2+b^2=c^2! (only AB^2=BH\*BC)
     - **native**: Yuclid squared-length AR + R85
     - **native**: Definitional P\_ACB = 0 + 4\_PYTH/
     - **native**: (lc\|lc) == (la\|la) + (lb\|lb)
     - derived: Euclidean metric norm
     - **native**: Triangle.is\_right / distance\*\*2
     - **native**: Byrne Book I, Prop. 47 (iconic 4-colour squares!)
     - **native**: Pythagoras Q\_c = Q\_a + Q\_b + assert\_area\_equal
   * - **Stewart's Theorem & Apollonius's Median Law** (``stewart_apollonius_median``)
     - —: Requires Book II / quadratic algebra
     - derived: Derivable in Ch15 segment field
     - **native**: dist\_sq\_mul\_dist\_add... (Stewart / BritishFlag)
     - —: Unexpressible in multiplicative AR
     - *partial*: R89\_LENGTH\_OF\_MEDIAN (in C++ Yuclid)
     - **native**: Linear LRATIO elimination on P\_AYB
     - derived: Null inner-product expansion (2D CGA)
     - derived: Polynomial identity in Prover.js
     - derived: Manual symbolic simplify()
     - *partial*: Book II Props. 9-10, 12-13 (cosine precursors)
     - **native**: Triple-Quad / Stewart polynomial identity


Domain 3 — Parallelism, Similarity & Proportion
-----------------------------------------------

Parallel postulate variants, parallelograms, cut-and-paste area, Thales intercept, AA/SAS/SSS similarity, Ceva, and Menelaus.

.. list-table::
   :header-rows: 1

   * - Canonical Topic (``snake_case``)
     - LeanEuc
     - GeoCoq
     - Mathlib
     - AlphaG
     - Newclid
     - JGEX
     - PGA/CGA
     - CindyJS
     - SymPy
     - Byrne
     - GEOMETOR
   * - **Parallel Line Through a Point (Euclid I.27-I.31)** (``parallel_line_construction``)
     - **native**: Prop27-Prop31
     - **native**: parallel\_existence (Ch12\_parallel.v)
     - **native**: AffineSubspace.mk' p s.direction
     - **native**: on\_pline / r00 / r02
     - **native**: on\_pline / R00 / R02
     - **native**: ON\_PLINE / S\_CABD = 0
     - **native**: P & (L ^ e0) or (L \| P) \| P (PGA)
     - **native**: cross(cross(linf, L), P)
     - **native**: Line.parallel\_line(P)
     - **native**: Byrne Book I, Prop. 31
     - **native**: Compass rhombus + assert\_parallel
   * - **Axiomatic Equivalents of Euclid's Parallel Postulate** (``parallel_postulate_equivalents``)
     - *partial*: Assumes System E parallel postulate
     - **native**: 34 equivalents in parallel\_postulates.v!
     - —: Baked into vector space axioms
     - —: Baked into AngleTable mod pi
     - —: Baked into AnglesTable
     - —: Assumes Euclidean plane
     - *partial*: Switch signature Cl(2,0,1) vs Cl(2,1,0)/Cl(3,0)
     - **native**: Cayley-Klein switch (Euclidean/Hyperbolic/Elliptic)
     - —: Euclidean Cartesian only
     - *partial*: Byrne Axiom XII (two-wedge sum < 2[∟])
     - *partial*: Documented across euclid / hilbert / proclus
   * - **Triangle Interior Angle Sum = Two Right Angles (Euclid I.32)** (``triangle_angle_sum``)
     - **native**: Prop32.proposition\_32
     - **native**: trisuma\_\_bet (Ch12 / parallel\_postulates.v)
     - **native**: oangle\_add\_oangle\_add\_oangle\_eq\_pi
     - *partial*: Line directions mod pi (r09), no interior sum
     - *partial*: R09 full-angle cancellation mod pi
     - **native**: Full-Angle method
     - derived: Rotor product around vertices
     - derived: Laguerre cross-ratio product = 1
     - derived: sum(Triangle.angles.values()) == pi
     - **native**: Byrne Book I, Prop. 32 (red+yellow+blue = 2[∟])
     - **native**: Wildberger Triple Spread Law
   * - **Parallelogram & Cut-and-Paste Area Theory (Euclid I.33-I.45)** (``parallelogram_area_equivalence``)
     - **native**: Prop33-Prop45 (complete!)
     - **native**: euclidean\_area\_axioms.v (+ inconsistency bug proof!)
     - *partial*: MeasureTheory volume, no cut-and-paste
     - *partial*: parallelogram r25/r26; NO area predicate!
     - *partial*: R25/R26/R90; NO area predicate!
     - **native**: Signed area S\_ABC / S\_ABCD primitive!
     - **native**: Pseudoscalar moment (A & B & C).e012
     - derived: Determinant area formula
     - **native**: Polygon.area (signed shoelace)
     - **native**: Byrne Book I, Props. 33-45 (chromatic regions!)
     - **native**: signed\_area2 & Model.assert\_area\_equal
   * - **Geometric Algebra of Rectangles & Gnomons (Euclid Book II.1-II.14)** (``geometric_algebra_books_ii``)
     - —: Stops at Book I.48
     - *partial*: Algebraicized in Ch14-Ch15
     - derived: CommRing ring tactic
     - —: No area/gnomon predicates
     - *partial*: lequation polynomial identities
     - **native**: Area + Pythagoras polynomial identities
     - derived: Scalar Clifford expansion
     - derived: Algebraic polynomial check
     - derived: sp.expand()
     - **native**: Byrne Book II, Props. 1-14 (gnomons & squares!)
     - **native**: euclid Book II SVGs + assert\_area\_equal
   * - **Thales Parallel-Intercept Proportion (Euclid VI.2)** (``thales_intercept_theorem``)
     - —: Book VI omitted
     - **native**: thm\_thales (Ch13 / Ch14)
     - **native**: Affine/Similarity ratio lemmas
     - **native**: r07 / r27 / r41 / r42 (eqratio3)
     - **native**: R07 / R27 / R41 / R42
     - **native**: Co-side & parallel ratio lemma
     - **native**: PGA join/meet weight ratios
     - **native**: Projective perspectivity
     - derived: Triangle.is\_similar
     - **native**: Byrne Book VI, Prop. 2 (:: proportion)
     - **native**: Exact quadrance ratio Q1/Q2
   * - **Triangle Similarity Criteria (AA, SAS, SSS / Euclid VI.4-VI.7)** (``similar_triangles``)
     - —: Book VI omitted
     - derived: Ch15 length-ratio similarity
     - **native**: Geometry/Euclidean/Similarity.lean
     - **native**: r34-r35 (AA), r38 (SSS), r39 (SAS)
     - **native**: R34-R35, R60-R63 (explicit sameclock)
     - **native**: GDD SimTri rules
     - derived: Rotor-dilator (similarity versor)
     - derived: Complex similarity z -> a\*z + b
     - **native**: are\_similar / Triangle.is\_similar
     - **native**: Byrne Book VI, Props. 4-7
     - **native**: Equal spreads <=> proportional quadrances
   * - **Internal & External Angle Bisector Ratio Theorem (Euclid VI.3)** (``angle_bisector_ratio_theorem``)
     - —: Book VI omitted
     - derived: Highschool/incenter + Ch15
     - **native**: Angle bisector ratio in Incenter/Basic.lean
     - *partial*: r11 / r12 (r11 converse unsound on ext bisector!)
     - *partial*: R11 / R12 (full-angle mod pi)
     - **native**: GDD r11 / r12
     - derived: Normalized line-sum weight ratio
     - derived: Harmonic bisector cross-ratio
     - derived: Symbolic bisector intersection
     - **native**: Byrne Book VI, Prop. 3
     - **native**: Equal spread + quadrance ratio Q(BD)/Q(DC)=Q(AB)/Q(AC)
   * - **Ceva's Concurrency & Menelaus's Collinearity Theorems** (``ceva_and_menelaus``)
     - —: Omitted
     - —: Not in Highschool/
     - *partial*: Ceva.lean present; Menelaus ABSENT!
     - —: Missing in r00-r42 (blocks Pappus/Desargues!)
     - *partial*: Partial ratio helpers; no general signed Menelaus
     - **native**: exs-book/ch2 A\_310 (Menelaus) & back/ceva!
     - **native**: Grassmann-Cayley bivector ratio cancellation
     - **native**: Homogeneous determinant cancellation
     - —: Not implemented
     - —: Post-Euclidean (omitted)
     - **native**: pappus & signed\_area2 co-side cancellation


Domain 4 — Circle Geometry, Tangency, Power & Inversion
-------------------------------------------------------

Circumcircles, inscribed/tangent-chord angles, Ptolemy, common tangents, Steiner power, radical axis, circle inversion, and circle pole-polar.

.. list-table::
   :header-rows: 1

   * - Canonical Topic (``snake_case``)
     - LeanEuc
     - GeoCoq
     - Mathlib
     - AlphaG
     - Newclid
     - JGEX
     - PGA/CGA
     - CindyJS
     - SymPy
     - Byrne
     - GEOMETOR
   * - **Inscribed & Central Angle Theorem (Euclid III.20-III.22)** (``inscribed_angle_theorem``)
     - —: Book III omitted
     - *partial*: Basic chord/circle defs in Annexes/circles.v
     - **native**: Sphere/Basic.lean ((2:ℤ)•∡ mod 2pi!)
     - **native**: r03 / r04 / r17 / r18 (eqangle mod pi!)
     - **native**: R03 / R04 / R17 / R18
     - **native**: Full-Angle crown jewel (RF\_\*)
     - derived: Conformal rotor angle invariance
     - **native**: Cross-ratio on conic = const (Chasles)
     - —: No inscribed-angle theorem
     - **native**: Byrne Book III, Props. 20-22
     - **native**: Equal chord spread on circle
   * - **Thales's Semicircle Right-Angle Theorem (Euclid III.31)** (``thales_semicircle_theorem``)
     - —: Book III omitted
     - **native**: Annexes/circles.v / midpoint circumcenter
     - **native**: thales\_theorem (Angle/Oriented & Unoriented)
     - **native**: r19 / r20
     - **native**: R19 / R20
     - **native**: GDD r20 + Area P\_ABC = 0
     - **native**: CGA inner product on antipodal pair
     - **native**: Harmonic diameter orthogonality
     - derived: Circle / Line.is\_perpendicular
     - **native**: Byrne Book III, Prop. 31
     - **native**: figures.py:289 (Thales tangent construction)
   * - **Circle Tangent Lines from Point On or Outside Circle (Euclid III.16-III.17)** (``circle_tangents_external``)
     - —: Book III omitted
     - *partial*: Tangent predicate in Annexes/circles.v
     - **native**: Sphere tangent / PolePolar
     - **native**: lc\_tangent (L157) & tangent (L397), r15-r16
     - **native**: lc\_tangent & tangent, R15-R16
     - **native**: TANGENT
     - **native**: Polar meet circle: (kappa ^ lam\_pol).dual()
     - **native**: TangentFromPoint (polar meet conic)
     - **native**: Circle.tangent\_lines(P) (via solve())
     - **native**: Byrne Book III, Props. 16-17
     - **native**: Thales semicircle intersection (zero solve()!)
   * - **External & Internal Common Tangents to Two Circles** (``common_tangents_two_circles``)
     - —: Omitted
     - —: Omitted
     - —: Not in Geometry/Euclidean/Sphere/
     - *partial*: cc\_tangent / cc\_tangent0 (external only!)
     - **native**: cc\_tangent + cc\_itangent (external & internal!)
     - **native**: CC\_TANGENT
     - derived: Dual conic /homothetic center blade
     - **native**: Dual conic intersection adj(C1) ∩ adj(C2)!
     - —: Not implemented
     - —: Omitted in Euclid Book III
     - *partial*: Planned via homothetic centers in model/elements
   * - **Ptolemy's Cyclic Quadrilateral Theorem** (``ptolemy_theorem``)
     - —: Omitted
     - —: Omitted
     - **native**: Sphere/Ptolemy.lean (mul\_dist\_add\_mul\_dist...)
     - derived: Provable with 1 aux similarity point
     - derived: Provable with 1 aux similarity point
     - **native**: Wu / Gröbner / Inversion proof
     - **native**: 2D CGA inversion of cyclic 4-tuple to collinear!
     - derived: Complex cross-ratio identity
     - —: Not implemented
     - —: Almagest (post-Euclidean, omitted)
     - derived: Inversion / rational cyclic identity
   * - **Intersecting Chords & Steiner Power of a Point (Euclid III.35-III.36)** (``steiner_power_of_a_point``)
     - —: Omitted
     - —: Omitted
     - **native**: Sphere.power (Sphere/Power.lean)
     - *partial*: Multiplicative chord eqratio only
     - *partial*: Chord eqratio + R85
     - **native**: P\_POP - P\_OAO / chord ratios
     - **native**: -2 \* (kappa \| P).e (2D CGA inner product!)
     - **native**: p \* C \* p (monic circle matrix)
     - —: MISSING on sympy Circle!
     - **native**: Byrne Book III, Props. 35-36 (rectangle = square!)
     - derived: quadrance(P, O) - r\_quad (Rec 4 -> model)
   * - **Radical Axis, Radical Center & Coaxial Circle Pencils** (``radical_axis_coaxial_circles``)
     - —: Omitted
     - —: Omitted
     - —: SURPRISINGLY ABSENT in Sphere/Power.lean!
     - —: Cannot state disjoint PO1^2 - PO2^2 = c!
     - *partial*: Expressible via R85 lequation
     - **native**: C\_RADICAL
     - **native**: kappa1 - kappa2 (1 subtraction in 2D CGA!)
     - **native**: Monic circle matrix subtraction (GeoOps.js:2044)
     - —: MISSING in sympy.geometry!
     - —: 19th-century Steiner/Gaultier (omitted)
     - **native**: Used internally in exact\_intersect\_circle\_circle
   * - **Möbius Circle Inversion (Points, Lines & Circles)** (``circle_inversion``)
     - —: Omitted
     - —: Omitted
     - **native**: EuclideanGeometry.inversion (Inversion/Basic.lean)
     - *partial*: External tangent+foot idiom only
     - *partial*: External tangent+foot idiom
     - **native**: INVERSION (exs-book/ch3:53)
     - **native**: C >> P = -C \* P \* C.inv() (2D CGA sandwich!)
     - **native**: TrReflectionC / cross(cross(O,p), C\*p)
     - —: MISSING in sympy.geometry!
     - —: Omitted
     - derived: figures.py:294 + Rec 4 geometor.model.inversion
   * - **Circle Pole-Polar & La Hire's Reciprocity Theorem** (``circle_pole_polar_lahire``)
     - —: Omitted
     - —: Omitted
     - **native**: Sphere.polar / mem\_polar\_iff (PolePolar.lean)
     - derived: Provable via tangent+foot SAS similarity
     - derived: Provable via tangent+foot SAS similarity
     - **native**: 2-line Area-Method INVERSION proof
     - **native**: kappa + (P ^ ni) \| kappa (2D CGA)
     - **native**: l = C \* p, p = adj(C) \* l
     - —: MISSING in sympy.geometry!
     - —: Apollonius/La Hire (omitted)
     - **native**: figures.py:293 + pappus conic polarity


Domain 5 — Triangle Centers & Classical Configurations
------------------------------------------------------

Incenter X(1), Excenters, Centroid X(2), Circumcenter X(3), Orthocenter X(4), Nine-Point Circle X(5), Euler line, Simson, Miquel, and ETC.

.. list-table::
   :header-rows: 1

   * - Canonical Topic (``snake_case``)
     - LeanEuc
     - GeoCoq
     - Mathlib
     - AlphaG
     - Newclid
     - JGEX
     - PGA/CGA
     - CindyJS
     - SymPy
     - Byrne
     - GEOMETOR
   * - **Incenter X(1) & Incircle (Euclid IV.4)** (``incenter_and_incircle_x1``)
     - —: Book IV omitted
     - **native**: Highschool/incenter.v
     - **native**: Simplex.incenter / inradius (Incenter/Basic.lean)
     - *partial*: incenter / incenter2 (conflated w/ excenter mod pi)
     - **native**: incenter + R46\_INCENTER\_THEOREM
     - **native**: INCENTER
     - derived: Meet of normalized side-blade bisectors
     - **native**: a\*A + b\*B + c\*C in CP^2
     - **native**: Triangle.incenter / incircle
     - **native**: Byrne Book IV, Prop. 4
     - **native**: figures.py:410 + etc X(1)
   * - **Three Excenters & Excircles (J\_A, J\_B, J\_C)** (``excenters_and_excircles``)
     - —: Omitted
     - —: Not in Highschool/
     - *partial*: SouthPole.lean (bisector-circumcircle poles)
     - *partial*: excenter / excenter2 (identical predicates to incenter!)
     - *partial*: excenter / excenter2
     - **native**: EXCENTER
     - derived: Signed side-blade bisector meets
     - **native**: -a\*A + b\*B + c\*C in CP^2
     - **BROKEN**: LIVE DOUBLE BUG in Triangle.excenters (polygon.py:2714)!
     - —: Omitted
     - **native**: Exact external bisectors + etc excenters
   * - **Centroid X(2) & 2:1 Median Concurrency** (``centroid_x2``)
     - —: Omitted
     - **native**: Highschool/centroid.v
     - **native**: Finset.centroid (LinearAlgebra/AffineSpace/Centroid.lean)
     - *partial*: centroid macro; 3-median proof needs 1 aux mirror!
     - **native**: centroid + R48\_CENTROID\_THEOREM
     - **native**: CENTROID + 1-line co-side Area proof
     - **native**: A + B + C (2D PGA homogeneous sum!)
     - **native**: A + B + C in CP^2
     - **native**: Triangle.centroid / Polygon.centroid
     - —: Archimedes (omitted in Euclid I-VI)
     - **native**: figures.py:257 & 376 + etc X(2)
   * - **Circumcenter X(3) & Circumcircle (Euclid IV.5)** (``circumcenter_x3``)
     - —: Book IV omitted
     - **native**: Highschool/circumcenter.v
     - **native**: Simplex.circumcenter / circumsphere (n-dim!)
     - **native**: circle / circumcenter (defs.txt:13, 19)
     - **native**: circle + R47\_CIRCUMCENTER\_THEOREM
     - **native**: CIRCUMCENTER
     - **native**: C\_circ \* ni \* ~C\_circ (2D CGA!)
     - **native**: CircleBy3 + adjoint3(C)\*linf
     - **native**: Triangle.circumcenter / circumcircle
     - **native**: Byrne Book IV, Prop. 5
     - **native**: figures.py:377 + etc X(3)
   * - **Orthocenter X(4) & Altitude Concurrency** (``orthocenter_x4``)
     - —: Omitted
     - **native**: Highschool/orthocenter.v
     - **native**: Simplex.mongePoint / orthocenter (MongePoint.lean)
     - **native**: orthocenter (examples.txt:2; needs feet/aux)
     - **native**: orthocenter + R43\_ORTHOCENTER\_THEOREM
     - **native**: exs-book/ch3:3 ORTH (0-step Jacobi proof!)
     - **native**: ((B&C)\|A) ^ ((C&A)\|B) (rational 2D PGA!)
     - **native**: meet(perp(BC,A), perp(CA,B))
     - **native**: Triangle.orthocenter
     - —: Omitted in Euclid I-VI
     - **native**: figures.py:390 + etc X(4)
   * - **Nine-Point Center X(5) & Feuerbach's Nine-Point Circle** (``nine_point_circle_x5``)
     - —: Omitted
     - —: OMITTED in GeoCoq Highschool/!
     - **native**: NinePointCircle.lean (3(n+1)-point sphere!)
     - **native**: ninepoints (defs.txt:103) + DDAR concyclicity
     - **native**: ninepoints
     - **native**: ex-gao/back/nine-point-circle
     - **native**: Ma ^ Mb ^ Mc in 2D CGA
     - **native**: CircleBy3(Ma, Mb, Mc)
     - **native**: Triangle.nine\_point\_circle
     - —: Feuerbach 1822 (omitted)
     - **native**: figures.py:394 + etc X(5)
   * - **Euler Line Collinearity & 2:1 Ratio (O, G, N, H)** (``euler_line``)
     - —: Omitted
     - *partial*: Highschool/euler\_line.v (Col only, no 2:1 ratio)
     - **native**: mongePoint\_vsub\_circumcenter = 3 • (G -ᵥ O)
     - **native**: examples.txt:8
     - **native**: Supported
     - **native**: exs-book/ch3:117 A\_201
     - **native**: Linear bivector identity
     - **native**: Prover.js collinearity
     - **native**: Triangle.eulerline
     - —: Euler 1765 (omitted)
     - **native**: figures.py:420-436 (Q(X3,X4) = 9\*Q(X3,X2))
   * - **Simson-Wallace Line & Miquel Pivot Theorems** (``simson_wallace_miquel``)
     - —: Omitted
     - —: Omitted
     - derived: Derivable via (2:ℤ)•∡ cyclic lemmas
     - **native**: Signature strength of eqangle DD+AR!
     - **native**: R45\_SIMSONS\_LINE\_THEOREM + DDAR
     - **native**: 3\_JAR/simson & miq\_th1.gex (Full-Angle!)
     - derived: 2D CGA / complex Clifford identity
     - **native**: Prover.js
     - —: Not implemented
     - —: Omitted
     - derived: Constructible & verifiable via signed\_area2
   * - **Encyclopedia of Triangle Centers (X(6)-X(53144))** (``kimberling_etc_catalog``)
     - —: 0 centers
     - —: Stops at X(1)-X(4)
     - —: Stops at ~6 centers (+ Brocard)
     - —: Stops at X(1)-X(5) + excenter
     - —: Stops at X(1)-X(5) + excenter
     - —: Classical centers only
     - —: Manual barycentric lift required
     - —: Manual CindyScript formulas
     - —: Stops at X(1)-X(5) (+ broken excenters)
     - —: Stops at IV.4 incircle & IV.5 circumcircle
     - **native**: geometor.etc CenterSymbolicRegistry (X(1)-X(53144))!


Domain 6 — Projective Geometry & Conic Sections
-----------------------------------------------

Homogeneous points at infinity, cross-ratio, harmonic conjugates, Pappus, Desargues, general conics, 5-point conic, Pascal/Brianchon, and conic pole-polar.

.. list-table::
   :header-rows: 1

   * - Canonical Topic (``snake_case``)
     - LeanEuc
     - GeoCoq
     - Mathlib
     - AlphaG
     - Newclid
     - JGEX
     - PGA/CGA
     - CindyJS
     - SymPy
     - Byrne
     - GEOMETOR
   * - **Homogeneous Coordinates & Ideal Points at Infinity** (``homogeneous_ideal_points``)
     - —: Affine Euclidean only
     - *partial*: Annexes/projective.v (synthetic incidence)
     - **native**: Projectivization K V (LinearAlgebra/Projective/)
     - —: Parallel lines do not meet in point
     - —: Affine Euclidean only
     - —: Parallel ratio r instead of ideal points
     - **native**: Direction bivectors e12=0 in 2D PGA!
     - **native**: [x, y, 0] on linf=[0,0,1] in CP^2!
     - —: Parallel Line.intersection returns []
     - —: Affine Euclidean only
     - **native**: geometor.pappus homogeneous RP^2 points/lines
   * - **Projective Cross-Ratio CR(A, B; C, D) & Perspectivity Invariance** (``cross_ratio_invariance``)
     - —: Omitted
     - —: Omitted
     - —: SURPRISINGLY ABSENT in Mathlib Geometry!
     - *partial*: Only harmonic -1 case fits 8-pt eqratio
     - *partial*: R70 harmonic case only
     - **native**: exs-book/ch3:38 A\_353 (Area ratio cancellation!)
     - **native**: ((A&C)\|(B&D)) / ((A&D)\|(B&C)) in 2D PGA
     - **native**: crossratio(A, B, C, D) + Laguerre formula
     - —: MISSING in sympy.geometry!
     - —: Omitted
     - **native**: geometor.model.cross\_ratio + geometor.pappus
   * - **Harmonic Range & Complete Quadrangle Fourth-Harmonic Construction** (``harmonic_conjugate_quadrangle``)
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - derived: Expressible via quadrangle; unprovable by bare DD+AR
     - **native**: R70\_PROJECTIVE\_HARMONIC\_CONJUGATE (added as axiom!)
     - **native**: HARMONIC (exs-book/ch3:47)
     - **native**: Division-free PGA quadrangle meet/join
     - **native**: crossratio == -1
     - —: Omitted
     - —: Omitted
     - **native**: is\_harmonic + pappus harmonic conjugate
   * - **Pappus's Hexagon Theorem (Synagoge VII.139)** (``pappus_hexagon_theorem``)
     - —: Omitted
     - *partial*: Ch13\_5\_Pappus\_Pascal.v (affine parallel case!)
     - —: ABSENT in Mathlib!
     - *partial*: 1-line statement; UNPROVABLE without aux parallels!
     - **native**: R44\_PAPPUS\_THEOREM (hardcoded rule!)
     - **native**: exs-book/ch2:40 PAPPUS (0-aux Area proof!)
     - **native**: (X & Y & Z).e == 0 identically in 2D PGA!
     - **native**: det(X, Y, Z) == 0 in CP^2
     - **BROKEN**: Crashes if opposite sides parallel + affine\_rank bug!
     - —: Point-free glyph palette ill-suited to 9-pt Pappus
     - **native**: figures.py:444 + geometor.pappus flagship
   * - **Desargues's Perspective Triangles Theorem** (``desargues_perspective_triangles``)
     - —: Omitted
     - *partial*: Ch13\_6\_Desargues\_Hessenberg.v (affine parallel)
     - —: ABSENT in Mathlib!
     - *partial*: Unprovable by bare DD+AR without aux parallels
     - *partial*: Requires aux parallels
     - **native**: 0-aux Area-Method / Wu / GB proof
     - **native**: Grassmann-Cayley identity in 2D/3D PGA
     - **native**: det(P, Q, R) == 0 in CP^2
     - *partial*: Manual Line.intersection (fails at infinity)
     - —: Omitted
     - **native**: geometor.pappus Desargues configurations
   * - **General Conics: Ellipse, Parabola & Hyperbola (Apollonius)** (``general_conic_sections``)
     - —: Circles only
     - —: Circles only
     - —: Spheres only in Geometry/Euclidean/
     - —: Circles only
     - —: Circles only
     - *partial*: Algebraic equations in Wu/GB only
     - *partial*: Requires 6D Conic GA Cl(5,3)
     - **native**: 3x3 symmetric matrix C in CP^2 (all conics!)
     - *partial*: Axis-aligned Ellipse + Parabola; NO Hyperbola!
     - —: Circles only
     - *partial*: apollonius codex + Rec 5 ProjectiveConic
   * - **Braikenridge-Maclaurin / Plücker Conic Through 5 Points** (``conic_through_five_points``)
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - *partial*: Wedge of 5 points in 6D Cl(5,3)
     - **native**: ConicBy5 Plücker pencil (GeoOps.js:1032)!
     - —: Omitted
     - —: Omitted
     - derived: Pascal line locus in pappus + Rec 5 ConicBy5
   * - **Pascal's Hexagrammum Mysticum & Brianchon's Dual Theorem** (``pascal_and_brianchon``)
     - —: Omitted
     - —: Omitted (only circle/line Pappus)
     - —: Omitted
     - *partial*: Circle-only Pascal via cyclic eqangle
     - *partial*: Circle-only Pascal
     - **native**: exs-book/ch3:134 PASCAL & Wu/GB
     - derived: 6D Conic GA / projective invariant
     - **native**: Primal C & dual adj(C) in CP^2
     - —: Omitted
     - —: Omitted
     - **native**: geometor.pappus Hexagrammum Mysticum
   * - **General Conic Pole-Polar & Adjugate Dual Conic** (``conic_pole_polar_duality``)
     - —: Omitted
     - —: Omitted
     - *partial*: Spheres only (Sphere/PolePolar.lean)
     - —: Omitted
     - —: Omitted
     - —: Circles only
     - —: Circles only in 2D CGA
     - **native**: l = C \* p, p = adjoint3(C) \* l!
     - —: Omitted
     - —: Omitted
     - *partial*: geometor.pappus + Rec 5 ProjectiveConic


Domain 7 — Transformations, Coordinatization & Complexity
---------------------------------------------------------

Reflections, rotations, translations, spiral similarities, geometric field arithmetic, Area-Method invariants, and Géométrographie complexity.

.. list-table::
   :header-rows: 1

   * - Canonical Topic (``snake_case``)
     - LeanEuc
     - GeoCoq
     - Mathlib
     - AlphaG
     - Newclid
     - JGEX
     - PGA/CGA
     - CindyJS
     - SymPy
     - Byrne
     - GEOMETOR
   * - **Point Reflection (Central Symmetry) & Line Reflection** (``line_and_point_reflection``)
     - derived: Via Prop10 / Prop12
     - **native**: Ch07\_midpoint (l7\_\*) & Ch10\_line\_reflexivity.v!
     - **native**: LinearIsometryEquiv.reflection / pointReflection
     - **native**: mirror (L169) & reflect (L271)
     - **native**: mirror & reflect
     - **native**: MIRROR / REFLECT
     - **native**: l >> X (line) & P >> X (point) in 2D PGA!
     - **native**: TrReflectionL / TrReflectionP
     - *partial*: Entity.reflect (uses atan(slope) & fails on Ellipse!)
     - —: Static coloured diagrams
     - derived: Compass mirror/vesica + Rec 7 elements transforms
   * - **Euclidean Rotations, Translations & Rigid Motors** (``rotation_and_translation``)
     - —: Superposition hidden in SAS axiom
     - derived: Composition of 2 line reflections (Ch10)
     - **native**: Orientation.rotation / vadd (+ᵥ)
     - *partial*: shift (L295), psquare/nsquare (±90°), s\_angle
     - *partial*: shift, psquare, nsquare
     - **native**: PRATIO (translation) & TRATIO (90° rotation)
     - **native**: Rotors exp(-theta/2 \* P) & Translators 1 - D/2!
     - **native**: TrSimilarity / Euclidean projective matrices
     - *partial*: Entity.rotate / translate (Ellipse.rotate broken!)
     - *partial*: Superposition in Byrne I.4 / I.8
     - derived: Exact algebraic transforms + PGA motor lens
   * - **Homothety (Dilation) & Spiral Similarity** (``homothety_and_spiral_similarity``)
     - —: Omitted
     - derived: Ch14/Ch15 scaling
     - **native**: AffineMap.homothety (LinearAlgebra/AffineSpace/)
     - derived: simtri + eqratio
     - derived: simtri + eqratio
     - **native**: LRATIO / PRATIO / TRATIO
     - **native**: 2D CGA dilator exp(alpha \* (P ^ ni)) \* rotor!
     - **native**: TrSimilarity (complex multiplication)
     - **native**: Entity.scale
     - *partial*: Book VI similar-polygon construction (VI.18)
     - derived: Exact rational homothety + divine scaling
   * - **Hilbert-Tarski Geometric Segment Arithmetic & Coordinatization** (``synthetic_field_coordinatization``)
     - —: Maps directly to host R
     - **native**: Ch14\_sum, Ch14\_prod, Ch15\_lengths, Ch16\_coordinates!
     - —: Starts from host R vector space
     - —: Uses Python float / Fraction
     - —: Uses float / SymEngine
     - —: Uses rational polynomials
     - —: Uses host scalar ring
     - —: Uses complex floats
     - —: Uses SymPy Expr
     - *partial*: Book V ribbon magnitude ratios (V.1-V.25)
     - *partial*: hilbert codex + algebraic\_field Q(alpha)
   * - **Chou-Gao-Zhang Coordinate-Free Area & Pythagoras Elimination** (``coordinate_free_area_elimination``)
     - —: SMT translation instead
     - —: ColR/CongR only
     - —: Inner-product tactics
     - —: Forward DD + linear AR
     - —: Forward DD + linear AR
     - *partial*: Elim.java kernel present; Area.java GUI disabled!
     - derived: Analogous to Grassmann-Cayley bracket elimination
     - —: Randomized float Prover.js
     - —: Generic CAS solve()
     - *partial*: Visual precursor: cut-and-paste region equations!
     - derived: signed\_area2 + Rec 6 complete Area-Method prover
   * - **Wu's Characteristic Set & Gröbner Basis Theorem Proving** (``wu_grobner_polynomial_proving``)
     - *partial*: Z3/CVC5 nonlinear real arithmetic
     - *partial*: External GeoCoq algebraic tactics (nsatz)
     - *partial*: polyrith / grobner tactics
     - —: Deliberately avoids coordinate polynomials
     - —: Avoids coordinate polynomials
     - **native**: CharSet.java (PanelWu) & PanelGB.java (Rabinowitsch)!
     - derived: Symbolic blade expansion
     - *partial*: Schwartz-Zippel complex identity test (Prover.js)
     - *partial*: sympy.polys.groebner (manual)
     - —: Human visual verification
     - **native**: ANP minimal-polynomial canonicalization (algebra.py)
   * - **PSLQ Integer-Relation & Minimal-Polynomial Discovery** (``pslq_algebraic_relation_recovery``)
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - **native**: PSLQ.js + CindyScript guess(x) (degree <= 2)!
     - *partial*: nsimplify (via mpmath.pslq)
     - —: Omitted
     - derived: divine proportion scanner + Rec 9 mpmath PSLQ scout
   * - **Lemoine's Géométrographie Operational Complexity (R1, R2, C1, C2, C3)** (``lemoine_geometrographie_complexity``)
     - —: Counts proof lines, not ruler/compass ops
     - —: Omitted
     - —: Non-constructive
     - *partial*: Clause count only
     - *partial*: Clause count only
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Pre-Lemoine (1847 vs 1902)
     - **native**: lemoine codex + Model.steps (Rec 3 R1..C3 telemetry)


Domain 8 — Golden Section, Constructible Polygons & 3D Solids
-------------------------------------------------------------

Extreme and mean ratio (phi), golden vesica chain, regular pentagon/decagon, 3D lines/planes/spheres, and the five Platonic solids.

.. list-table::
   :header-rows: 1

   * - Canonical Topic (``snake_case``)
     - LeanEuc
     - GeoCoq
     - Mathlib
     - AlphaG
     - Newclid
     - JGEX
     - PGA/CGA
     - CindyJS
     - SymPy
     - Byrne
     - GEOMETOR
   * - **Golden Ratio (phi) — Division in Extreme & Mean Ratio (Euclid II.11, VI.30)** (``golden_ratio_extreme_mean_cut``)
     - —: Omitted
     - —: OMITTED across all 481 GeoCoq files!
     - —: Real.goldenRatio in NumberTheory only, 0 in Geometry!
     - —: OMITTED in defs.txt & rules.txt!
     - —: Omitted
     - —: Omitted
     - —: Not built-in
     - *partial*: guess() recovers (1+sqrt(5))/2 numerically
     - —: sp.GoldenRatio in core only, 0 in sympy.geometry
     - **native**: Byrne Book II.11 & Book VI.30 (in 4 colours!)
     - **native**: Core DNA: Q(phi) ANP, fundamentals, divine, pacioli!
   * - **5-Step Vesica Golden Chain (/ I E F J / Harmonics)** (``vesica_golden_poles_chain``)
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - —: Uses classical II.11 square-gnomon cut
     - **native**: figures.py:313 + fundamentals + divine
   * - **Constructible Regular Pentagon & Decagon (Euclid IV.10-IV.14, XIII.1-XIII.10)** (``regular_pentagon_and_decagon``)
     - —: Omitted
     - —: Omitted
     - *partial*: Angle/Cosine values of pi/5; no compass construction
     - *partial*: pentagon (L235) is 5 unconstrained free points!
     - *partial*: pentagon = 5 free points
     - —: Omitted
     - derived: 2\*pi/5 rotor over Q(phi, sqrt(5))
     - derived: Complex 5th roots of unity
     - **native**: RegularPolygon(O, r, 5) (exact cos(pi/5) radicals)
     - **native**: Byrne Book IV, Props. 10-14 (golden isosceles!)
     - **native**: euclid IV.11 / XIII + kepler + elements
   * - **Constructible n-gons (3, 4, 5, 6, 15, 17 / Gauss-Wantzel)** (``constructible_polygons_gauss_wantzel``)
     - —: Omitted
     - *partial*: Annexes/quadrilaterals.v & regular\_polygons (partial)
     - *partial*: Field theory degree-2 tower lemmas; not linked to geom
     - *partial*: isquare, eq\_triangle; trisect (L349) cheats w/ trig!
     - *partial*: isquare, eq\_triangle, trisect
     - —: Omitted
     - derived: Pin(2) rotor towers
     - derived: Regular polygon macro
     - **native**: RegularPolygon(O, r, n)
     - **native**: Byrne Book IV (3, 4, 5, 6, 15-gon in IV.16!)
     - **native**: kepler Harmonices Mundi Book I + Q(alpha) towers
   * - **3D Lines, Planes, Orthogonality & Spheres (Euclid Books XI-XII)** (``euclidean_3d_lines_planes_spheres``)
     - —: Strictly 2D planar
     - **native**: Tarski\_3D / dimension-free Ch02-Ch12!
     - **native**: n-dimensional throughout Geometry/Euclidean/!
     - —: Strictly 2D planar
     - —: Strictly 2D planar
     - —: Strictly 2D planar
     - **native**: 3D PGA Cl(3,0,1) & 3D CGA Cl(4,1) in kingdon!
     - *partial*: Cindy3D WebGL plugin
     - **native**: Point3D, Line3D, Plane (no Sphere!)
     - —: Stops at Book VI (Books XI-XII omitted)
     - *partial*: euclid XI-XII + archimedes + walter-russell 3D
   * - **Five Platonic Solids & Golden Polyhedral Coordinates (Euclid XIII, Pacioli, Kepler)** (``platonic_and_archimedean_solids``)
     - —: Omitted
     - —: Omitted
     - —: OMITTED in Mathlib/Geometry/!
     - —: Omitted
     - —: Omitted
     - —: Omitted
     - *partial*: 3D PGA motor symmetry groups
     - *partial*: Cindy3D polyhedra demos
     - *partial*: combinatorics.Polyhedron (permutations only, NO 3D coords!)
     - —: Stops at Book VI (Book XIII omitted)
     - **native**: euclid XIII + pacioli + kepler + walter-russell

