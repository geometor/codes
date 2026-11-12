:navigation: header
:order: 60

.. _glossary:

========
Glossary
========

Foundational terms, logical paradigms, and algebraic invariants referenced across **GEOMETOR Codes**.

.. glossary::
   :sorted:

   Formal System E
      The six-sorted constructive and diagrammatic formal system (`Point`, `Line`, `Circle`, `Segment`, `Angle`, `Triangle`) formulated by Jeremy Avigad, Edward Dean, and John Mumma (2009) and mechanized in ``LeanEuclid``, separating explicit ruler-and-compass construction rules from diagrammatic plane-topology inferences and linear real metric transfer axioms.

   point-only ontology
      Alfred Tarski's minimalist first-order geometric signature (formalized in ``GeoCoq``) in which the universe contains a single sort ``Tpoint`` and two primitive relations—ternary non-strict betweenness ``Bet A B C`` and quaternary segment equidistance ``Cong A B C D``—eliminating lines, circles, and angles as primitive types.

   Five-Segment Configuration
      Tarski's angle-free replacement (``FSC`` / ``outer_five_segment``) for Euclid's Side-Angle-Side congruence criterion (`I.4`), asserting that two collinear 4-tuples with matching base congruences transmit congruence to the fifth segment joining an apex.

   affine torsor
      A point space :math:`P` acted upon freely and transitively by a vector space :math:`V` (``NormedAddTorsor V P`` in ``mathlib4``), allowing vector subtraction :math:`p_1 -_v p_2 \in V` and vector translation :math:`v +_v p \in P` without privileging an arbitrary coordinate origin :math:`(0, 0)`.

   directed full-angle
      An angle modulo :math:`\pi` between ordered pairs of *lines* rather than rays—written ``eqangle`` in ``JGEX``/``AlphaGeometry``/``Newclid`` and :math:`(2 : \mathbb{Z}) \bullet \measuredangle x y z` in ``mathlib4``—which eliminates acute/obtuse and supplementary case splits in cyclic quadrilateral proofs.

   Deductive Database
      Forward-chaining Horn-clause saturation (``GDD`` in ``JGEX``, ``dd.py`` in ``AlphaGeometry``) computing the finite relational fixed point of synthetic congruence, parallelism, perpendicularity, similarity, and concyclicity rules without branching search.

   Algebraic Reasoning
      Sparse rational Gaussian elimination (``ar.py`` in ``AlphaGeometry``, ``SympyAR`` / ``Yuclid`` in ``Newclid``) maintaining linear equivalence tables over directed angles modulo :math:`\pi`, logarithmic segment ratios, collinear distances, and (in ``Yuclid``) squared lengths.

   Area Method
      The coordinate-free decision and readable-proof procedure of Chou, Gao, and Zhang (1994) that eliminates constructed points in reverse order from rational expressions in three geometric invariants: parallel signed ratios :math:`r`, signed areas :math:`S_{ABC}`, and Pythagoras differences :math:`P_{ABC}`.

   Pythagoras difference
      The coordinate-free quadratic invariant :math:`P_{ABC} = |AB|^2 + |BC|^2 - |AC|^2` (generalized to four points as :math:`P_{ABCD} = |AB|^2 + |CD|^2 - |BC|^2 - |DA|^2 = 2\overrightarrow{AC}\cdot\overrightarrow{BD}`), which vanishes if and only if :math:`AB \perp BC` (respectively :math:`AC \perp BD`).

   Projective Geometric Algebra
      The degenerate Clifford algebra :math:`\mathbb{R}_{2,0,1}^*` (`Algebra(2, 0, 1)` in ``kingdon``) whose basis vector :math:`e_0` squares to :math:`0`, representing planar lines as grade-1 vectors, finite and ideal points uniformly as grade-2 bivectors, meets via ``^``, joins via ``&``, and Euclidean isometries via versor sandwich products.

   Conformal Geometric Algebra
      The Minkowski Clifford algebra :math:`\mathbb{R}_{3,1}` (`Algebra(3, 1)` in ``kingdon``) embedding each planar point :math:`(x, y)` onto the 4D null cone :math:`P = x e_1 + y e_2 + \tfrac{1}{2}(x^2 + y^2)n_\infty + n_o`, unifying lines and circles so Steiner power is an inner product ``-2*(kappa | P)``, radical axis is ``kappa1 - kappa2``, and circle inversion is a sandwich product ``C >> X``.

   versor sandwich product
      The universal Clifford transformation law :math:`V \gg X = \pm V X \widetilde{V}` applying reflections, rotations, translations, dilations, and conformal circle inversions uniformly across blades of every grade.

   circular points at infinity
      The conjugate complex projective pair :math:`I = (1, i, 0)` and :math:`J = (1, -i, 0)` on the ideal line :math:`\ell_\infty = [0, 0, 1]` in :math:`\mathbb{CP}^2` (``CindyJS``), through which every Euclidean circle passes and relative to which Laguerre's cross-ratio recovers Euclidean angle.

   chromatic value-token
      An inline colored geometric glyph (segment, angle wedge, polygon, or circle in primary red, blue, yellow, or black) used directly inside algebraic-logical proof equations in Oliver Byrne's 1847 *Coloured Euclid*, eliminating indirect vertex-letter pointer dereferencing.

   quadrance
      Norman Wildberger's polynomial squared separation :math:`Q(A, B) = (x_2 - x_1)^2 + (y_2 - y_1)^2` in ``geometor.model`` and ``geometor.wildberger``, avoiding irrational square roots so metric laws remain inside the base number field.

   spread
      Wildberger's rational squared-sine invariant :math:`s(\ell_1, \ell_2) \in [0, 1]` between two lines (:math:`0` when parallel, :math:`3/4` at :math:`60^\circ`, :math:`1` when perpendicular), replacing transcendental ``arccos``/``atan2`` angles with exact rational algebra.

   Algebraic Number Polynomial
      SymPy's exact minimal-polynomial field element representation (`ANP` inside ``QQ.algebraic_field(ext)``) used by ``geometor.model.algebra`` to canonicalize coordinates over :math:`\mathbb{Q}(\phi)`, :math:`\mathbb{Q}(\sqrt{d})`, and radical towers without floating-point approximation.

   Géométrographie
      Émile Lemoine's 1902 operational complexity calculus counting the five physical straightedge and compass primitives (:math:`R_1, R_2, C_1, C_2, C_3`) of any geometric construction via its **Simplicity** :math:`S = \sum` and **Exactitude** :math:`E = R_1 + C_1 + C_2`.
