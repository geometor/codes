.. _system-pga-cga:

=======================================================================
Projective & Conformal Geometric Algebra (``kingdon`` vs ``galgebra``)
=======================================================================

* **Repositories**: ``_refs/kingdon`` (`https://github.com/tBuLi/kingdon`, MIT, :cite:`Gunn2020`) & ``_refs/galgebra`` (`https://github.com/pygae/galgebra`, BSD-3-Clause)
* **Mathematical Foundation**: :person:`Hermann Günther Grassmann <grassmann>` & :person:`William Kingdon Clifford <clifford>` multivector calculi—Plane-Based 2D :term:`Projective Geometric Algebra` :math:`\mathbb{R}_{2,0,1}^*` and Point-Based 2D :term:`Conformal Geometric Algebra` :math:`\mathbb{R}_{3,1}` (:cite:`DorstFontijneMann2007`)

1. Two Covariant Calculi: 2D PGA vs. 2D CGA
-------------------------------------------

Clifford algebra replaces ad-hoc vector cross/dot formulas with a single associative **geometric product** ``u * v = (u | v) + (u ^ v)`` over graded blades:

* **Plane-Based 2D PGA (`Algebra(2, 0, 1)`)**: Basis :math:`e_1^2 = e_2^2 = 1, \; e_0^2 = 0` (`e0` is the ideal line at infinity).

  - **Grade-1 vectors are Lines**: :math:`\ell = a e_1 + b e_2 + c e_0`.
  - **Grade-2 bivectors are Points & Ideal Directions**: :math:`P = e_{12} + x e_{20} + y e_{01}` (finite point) vs. :math:`D = dx\,e_{20} + dy\,e_{01}` (ideal point at infinity, weight :math:`e_{12} = 0`!).
  - **Division-Free Incidence & Metric**: ``l1 ^ l2`` is the **meet** of two lines (valid even when parallel!); ``P1 & P2`` is the **join** of two points; ``(l | P)`` is the line through ``P`` perpendicular to ``l``; and ``l >> X`` reflects *any* point or line across ``l``!

* **Point-Based 2D CGA (`Algebra(3, 1)`)**: Lifts 2D Euclidean point :math:`(x, y)` onto the 4D Minkowski null cone (:math:`n_o^2 = n_\infty^2 = 0, \; n_o \cdot n_\infty = -1`):

  .. math::

     P = x e_1 + y e_2 + \tfrac{1}{2}(x^2 + y^2)n_\infty + n_o, \qquad -2(P_1 \mid P_2) = (x_1 - x_2)^2 + (y_1 - y_2)^2 = Q(P_1, P_2)

  In 2D CGA (`kingdon` with SymPy symbolic scalars), **circle geometry collapses to 1-line linear/versor expressions**:

  .. code-block:: python

     C_circ    = P1 ^ P2 ^ P3                 # OPNS grade-3 circle through 3 points!
     X3        = norm_pt(C_circ * ni * ~C_circ)  # Circumcenter = reflection of infinity ni!
     kappa1    = C1.dual()                    # IPNS grade-1 dual circle O - (1/2)r^2 ni
     power_P   = -2 * (kappa1 | P).e          # Steiner power of P wrt C1!
     lam_rad   = kappa1 - kappa2              # Radical axis of ANY two circles (even disjoint)!
     P_inv     = norm_pt(C1.normalized() >> P) # Möbius circle inversion = sandwich product!

2. Forensic Audit: Three Critical Traps in ``galgebra``
-------------------------------------------------------

Comparing ``kingdon`` and ``galgebra`` source code side-by-side exposed three severe pitfalls in ``galgebra`` (`mv.py`) for projective geometry:

1. **Crash on Degenerate PGA Duality (`galgebra/mv.py:1104`)**: Calling ``A.dual()`` computes ``self * self.ga.I_inv()``, which raises ``AttributeError: 'Ga' object has no attribute 'i_inv'`` whenever :math:`I^2 = 0`—breaking Poincaré duality across **all** degenerate Projective Geometric Algebras (`Cl(2,0,1)` and `Cl(3,0,1)`)! ``kingdon`` (`operators.py:390-440`) dispatches cleanly to the metric-free right Hodge complement whenever :math:`r \ge 1`.
2. **Missing Regressive Join ``&``**: ``galgebra`` implements ``^`` (outer) and ``|`` (inner), but has **no regressive vee join ``&``**, preventing standard plane-based PGA point-joining ``P1 & P2``.
3. **Silent Operator Trap on ``>>``**: In ``kingdon``, ``V >> X`` is the **versor sandwich product** :math:`\pm V X \widetilde{V}`. In ``galgebra`` (`mv.py:809`), ``A >> B`` is the **commutator product** :math:`\tfrac{1}{2}(AB - BA)`! Writing ``L >> P`` in ``galgebra`` silently computes a Lie-bracket commutator instead of a reflection!

Furthermore, ``kingdon`` (`polynomial.py`, `codegen.py`) compiles symbolic blades through ``RationalPolynomial`` + ``poly_cse`` over exact ``sympy.Expr`` leaves—needing only ``simp_func=sp.cancel`` when dividing rational functions.

3. Takeaway for GEOMETOR
------------------------

Use ``kingdon``'s blade conventions (never ``galgebra``'s ``>>``) to expose lightweight 2D PGA and 2D CGA multivector projections over ``geometor.model`` elements—giving GEOMETOR division-free projective chains and 1-line conformal circle algebra while preserving ``Model``'s explicit step lineage.
