.. _system-mathlib4:

======================================================
Lean 4 Mathlib: Dimension-Polymorphic Affine Torsors
======================================================

* **Repository**: ``_refs/mathlib4`` (`https://github.com/leanprover-community/mathlib4`, Apache-2.0, :cite:`Mathlib2020`)
* **Scale Audited**: `46` files (`16,844` LOC) in ``Mathlib/Geometry/Euclidean/`` + `24` files (`11,708` LOC) in ``Mathlib/LinearAlgebra/AffineSpace/``
* **Mathematical Foundation**: Dependent type-theoretic :term:`affine torsor` ``NormedAddTorsor V P`` over a real ``InnerProductSpace ℝ V``

1. Why Points and Vectors Are Separate Types
--------------------------------------------

In Cartesian software (`sympy.geometry`), a point :math:`(x, y)` and a displacement vector :math:`\langle dx, dy \rangle` share coordinates relative to a privileged origin :math:`(0, 0)`. ``mathlib4`` enforces coordinate-free discipline through the typeclass stack:

.. code-block:: lean4

   variable {V : Type*} {P : Type*}
     [NormedAddCommGroup V] [InnerProductSpace ℝ V] [MetricSpace P] [NormedAddTorsor V P]

Here ``p₁ + p₂`` is a **compile-time type error**! You may only subtract two points to obtain a vector (``p₁ -ᵥ p₂ : V``), translate a point by a vector (``v +ᵥ p : P``), or form weighted affine combinations (`Finset.centroid`, `midpoint`, `AffineMap.lineMap`) whose weights sum to `1`.

2. Where Affine Torsors Shine: Arbitrary Dimension :math:`n`
------------------------------------------------------------

Because ``V`` need not have dimension `2`, ``Mathlib/Geometry/Euclidean/`` achieves breathtaking generality across dimensions:

* **Monge Point & :math:`3(n+1)`-Point Sphere (`MongePoint.lean`, `NinePointCircle.lean`)**: Instead of proving altitude concurrency only for planar triangles, ``Simplex.mongePoint`` generalizes the orthocenter to an arbitrary :math:`n`-simplex in :math:`\mathbb{R}^n`, and ``NinePointCircle.lean`` proves Feuerbach's nine-point circle as the :math:`n`-dimensional **:math:`3(n+1)`-point sphere**!
* **Directed Twice-Angles Modulo :math:`2\pi` (`Angle/Oriented/Basic.lean`)**: When `[Module.Oriented ℝ V (Fin 2)]` and `[Fact (Module.finrank ℝ V = 2)]` are added for 2D plane geometry, ``oangle x y z`` (`∡ x y z : Real.Angle`) lives in :math:`\mathbb{R} / 2\pi\mathbb{Z}`. Multiplying by `(2 : ℤ) • ∡ p₁ p₂ p₃` kills ray-reversal (`π` becomes `2π = 0`), encoding **directed line angles** cleanly and proving inscribed-angle concyclicity (`Sphere/Basic.lean`) without case splits!
* **1-Line La Hire Pole–Polar Reciprocity (`Sphere/PolePolar.lean`)**: Defines ``Sphere.power s p := dist p s.center ^ 2 - s.radius ^ 2`` and ``Sphere.polar s p := mk' (inversion s.center s.radius p) (ℝ ∙ (p -ᵥ s.center))ᗮ``, proving :person:`Philippe de La Hire <lahire>`'s reciprocity ``q ∈ s.polar p ↔ p ∈ s.polar q`` in a handful of inner-product rewrite steps across all dimensions!
* **Compositional Naming Grammar**: Theorems read like self-documenting sentences (`conclusion_of_hypothesis`, e.g., ``mul_dist_add_mul_dist_eq_mul_dist_of_cospherical`` in ``Sphere/Ptolemy.lean``).

3. Forensic Blind Spots: Noncomputability, Cyclic Order & Projective Gaps
-------------------------------------------------------------------------

1. **Pervasive ``noncomputable`` Definitions**: ``Simplex.circumsphere`` uses ``Classical.choose`` on an existence proof, and ``EuclideanGeometry.angle`` invokes noncomputable ``Real.arccos``. You **cannot execute** a ``mathlib4`` Euclidean construction to inspect exact symbolic coordinates!
2. **No Constructive ``Euclid I.1`` & Awkward Cyclic Order**: Because two spheres in :math:`\mathbb{R}^3` meet in a circle rather than two points, ``mathlib4`` has no planar compass-and-straightedge ``Euclid I.1`` theorem. Moreover, ``Sphere/Ptolemy.lean:22-41`` contains a candid **20-line ``TODO`` block** lamenting the lack of a clean cyclic-order predicate on circles in vector-torsor geometry.
3. **Wide-Open Projective & Coaxial Omissions**: Despite defining ``Projectivization K V`` in ``LinearAlgebra/Projective/Basic.lean``, ``mathlib4`` currently has **zero** ``radicalAxis``, **zero** ``crossRatio``, **zero** ``Menelaus`` (despite having ``Ceva.lean``!), **zero** ``Pappus``, **zero** ``Desargues``, **zero** general conics in ``Geometry/Euclidean/``, and **zero** geometric theorems on ``Real.goldenRatio`` or Platonic solids.

4. Takeaway for GEOMETOR
------------------------

Adopt ``mathlib4``'s ``conclusion_of_hypothesis`` naming discipline and its crystal-clear ``power`` / ``inversion`` / ``polar`` conceptual factoring in ``geometor.elements`` 2.0 and ``geometor.model.inversion``, while retaining 100% computable ``ANP`` coordinates and full projective/golden coverage.
