.. _system-sympy:

========================================================================
SymPy Geometry (``1.14.0``): Symbolic CAS Architecture & Live Bug Audit
========================================================================

* **Location Audited**: ``.venv/lib/python3.13/site-packages/sympy/geometry/`` (`11` modules, `12,071` LOC) + ``sympy/combinatorics/polyhedron.py`` (`1,020` LOC), BSD-3-Clause
* **Role in GEOMETOR**: Provides the base ``Point2D``, ``Line2D``, ``Segment2D``, ``Circle``, and ``Polygon`` entity classes wrapped—and strategically bypassed—by ``geometor.model``

1. Architectural Inventory & Solver Bottlenecks
-----------------------------------------------

``sympy.geometry`` models affine Cartesian entities over general ``sympy.Basic`` expressions (`point.py`, `line.py`, `ellipse.py`, `parabola.py`, `polygon.py`, `plane.py`, `curve.py`, `entity.py`, `util.py`). While intuitive for 1-step textbook exercises, our line-by-line audit explains **why naive ``sympy.geometry`` grinds to a halt after 3–4 compass steps**:

* **Generic ``solve()`` Inside ``Ellipse.intersection`` (`ellipse.py:676-691`)**: Intersecting two ``Circle`` objects substitutes quadratic Cartesian equations into SymPy's generic Buchberger/polynomial ``solve(...)`` instead of subtracting circles to form the linear radical axis—exploding exponentially on nested quadratic radicals :math:`\mathbb{Q}(\sqrt{5}, \sqrt{3}, \sqrt{10 - 2\sqrt{5}})`.
* **Pervasive Eager ``simplify()`` (`37` Call Sites)**: Methods across `line.py`, `ellipse.py`, and `polygon.py` invoke general heuristic ``simplify()`` on symbolic denominators rather than canonical arithmetic in an algebraic number field (`QQ.algebraic_field`).
* **Axis-Aligned Conic Prison & Missing ``Hyperbola``**: ``Ellipse`` only supports horizontal/vertical axes; calling ``Ellipse.rotate(theta)`` (`ellipse.py:1244-1255`) raises ``NotImplementedError("Only rotations of multiples of pi/2 are currently supported for Ellipse.")``, and **``Hyperbola`` does not exist at all**!
* **Total Absence of Inversive, Coaxial & Projective APIs**: ``Circle`` has **no** ``power``, ``radical_axis``, ``invert``, ``polar``, or ``pole``; parallel ``Line.intersection`` returns ``[]``; ``cross_ratio`` is absent; and ``combinatorics.Polyhedron`` stores vertex permutation groups only with **zero 3D geometric coordinates**.

2. Live Bug #1: Double Algebraic Bug in ``Triangle.excenters``!
---------------------------------------------------------------

Auditing ``sympy/geometry/polygon.py:2714-2726`` in SymPy `1.14.0` uncovered a **live double bug** in ``Triangle.excenters``:

.. code-block:: python

   # sympy/geometry/polygon.py:2714-2726 (LIVE BUG IN SYMPY 1.14.0!)
   excoords = {
       "a": (
           simplify(-a*x[0] + b*x[1] + c*x[2]/(-a + b + c)),  # <-- 1. MISSING PARENTHESES!
           simplify(-a*y[0] + b*y[1] + c*y[2]/(-a + b + c)),  # divides ONLY c*x[2] by (-a+b+c)!
       ), ...
   }
   # AND 2. WRONG VERTEX-SIDE PAIRING: s[0] = Segment(v[0], v[1]) has length c (opposite v[2]),
   # NOT opposite v[0]! Even SymPy's own test_polygon.py hardcoded the corrupted output!

For the standard `3-4-5` right triangle ``Triangle(Point(0, 0), Point(3, 0), Point(0, 4))``, the true excenter opposite `(0, 0)` is ``(-6, -6)``, whereas SymPy `1.14.0`'s ``Triangle.excenters[t.sides[0]]`` returns ``Point2D(12, 2)``—which does not even lie on the angle bisectors!

3. Live Bug #2: Float Collinearity False-Positive in ``Point.affine_rank``!
---------------------------------------------------------------------------

In ``sympy/geometry/point.py:331-335``, ``Point.affine_rank`` (called by ``Point.is_collinear``!) tests whether exact symbolic matrix entries vanish using a **2-digit floating-point threshold**:

.. code-block:: python

   # sympy/geometry/point.py:331-335 (LIVE PRECISION BUG!)
   # Exact non-collinear points Point(0,0), Point(1,0), Point(1, Rational(1, 10**13))
   # evaluate abs((10**-13).n(2)) < 1e-12 == True -> FALSELY RETURNS COLLINEAR!

4. Takeaway for GEOMETOR
------------------------

1. Validates ``geometor.model``'s architectural mandate to **never call ``Circle.intersection`` or ``Point.is_collinear``**, using closed-form radical-axis intersections (`intersections.py`), exact ``signed_area2 == 0``, and ``ANP`` canonicalization instead.
2. Gives GEOMETOR two crisp, high-impact **upstream SymPy pull requests** (`Blueprint 10`) fixing ``Triangle.excenters`` and ``Point.affine_rank``.
