.. _system-cindyjs:

======================================================================
CindyJS: Complex Projective :math:`\mathbb{CP}^2`, Cayley–Klein & PSLQ
======================================================================

* **Repository**: ``_refs/CindyJS`` (`https://github.com/CindyJS/CindyJS`, Apache-2.0, :cite:`RichterGebert2011`)
* **Scale Audited**: ``src/js/libgeo/`` (`GeoOps.js`, `Conics.js`, `Tracing.js`, `Prover.js`) + ``src/js/libcs/`` (`List.js`, `PSLQ.js`)
* **Mathematical Foundation**: :person:`Arthur Cayley <cayley>`, :person:`Felix Klein <klein>`, and :person:`Jürgen Richter-Gebert <richtergebert>`'s complex projective geometry over :math:`\mathbb{CP}^2` with Riemann-surface homotopy continuation

1. Total Duality in :math:`\mathbb{CP}^2` & Circular Points :math:`I, J`
------------------------------------------------------------------------

``CindyJS`` embeds every planar point :math:`p = [x, y, z]` and every line :math:`\ell = [a, b, c]` in the **complex projective plane** :math:`\mathbb{CP}^2` (`List.js`):

* **Unified Join & Meet**: Joining two points and intersecting two lines are the **exact same 3D vector cross product** ``List.cross(u, v)`` (`GeoOps.js:156-202`), handling parallel lines (`z = 0`) seamlessly with zero conditionals.
* **First-Class General Conics (`Conics.js`, `GeoOps.js:1032`)**: Unlike every ITP and ``sympy.geometry``, ``CindyJS`` represents *all* conics (circles, rotated ellipses, parabolas, hyperbolas, and degenerate line pairs) uniformly as :math:`3 \times 3` complex symmetric matrices :math:`C`:

  - **Polar of point** :math:`p`: matrix-vector product ``l = C * p``;
  - **Dual envelope conic**: cofactor adjugate ``C_dual = List.adjoint3(C)`` (division-free even on rank-2 degenerate conics!);
  - **Pole of line** :math:`\ell`: ``p = adjoint3(C) * l``;
  - **5-Point Conic (`ConicBy5`)**: Plücker linear combination :math:`C = \mu D_1 - \lambda D_2` of two rank-2 line-pair matrices in pure multiplication/subtraction!

* **Cayley–Klein Metric via Circular Points at Infinity (`List.js:111-126`)**: Defining :term:`circular points at infinity` ``List.ii = [1, i, 0]`` and ``List.jj = [1, -i, 0]``, **every Euclidean circle is simply a conic passing through** :math:`I` **and** :math:`J` (`CircleMP` calls `ConicBy5` with `ii` and `jj`!), perpendicularity is harmonic conjugacy ``l1 * diag(1,1,0) * l2 == 0``, and Euclidean angle is **Laguerre's cross-ratio formula** :math:`\theta = \frac{i}{2}\ln\operatorname{CR}(A_\infty, B_\infty; I, J)`!

2. Three Algorithmic Gems in ``Tracing.js``, ``Prover.js`` & ``PSLQ.js``
------------------------------------------------------------------------

1. **Riemann-Surface Semicircle Homotopy (`Tracing.js:198-200`)**: In ordinary dynamic geometry, dragging two intersecting circles apart until they become disjoint and bringing them back causes quadratic ``sqrt`` branches to swap unpredictably (*the jumping-elements bug*). ``CindyJS`` keeps complex-conjugate intersections alive over :math:`\mathbb{C}^3` and detours each parameter step :math:`t \in [0, 1]` along an **upper-half-plane complex semicircle**:

   .. code-block:: javascript

      // src/js/libgeo/Tracing.js:198-200 (complex semicircle detour around branch points!)
      var alpha = t * Math.PI;
      var tc = CSNumber.complex(0.5 - 0.5 * Math.cos(alpha), 0.5 * Math.sin(alpha));

   Passing *around* real branch-point singularities on the Riemann surface makes element identity globally continuous!
2. **Randomized Complex Theorem Proving (`Prover.js`)**: Evaluates construction DAGs at 3 random complex perturbations (`Schwartz–Zippel lemma`) to auto-discover concurrencies and incidences at interactive frame rates.
3. **Live Integer-Relation Surd Recovery (`PSLQ.js:1-215`)**: Implements Ferguson–Bailey PSLQ (`guess(x)`), recovering rationals and quadratic surds like ``3/2 + 1/2*sqrt(5)`` from floating-point coordinates—capped at vector dimension ``n = 3`` (degree :math:`\le 2`).

3. Takeaway for GEOMETOR
------------------------

Port ``CindyJS``'s :math:`3 \times 3` symmetric conic matrix, ``adjoint3`` dual, and ``ConicBy5`` Plücker pencil directly into **exact SymPy arithmetic** in ``geometor.pappus`` (`Blueprint 5`), and generalize ``PSLQ.js``'s `n=3` ``guess(x)`` to arbitrary algebraic degree :math:`d` via 100-digit ``mpmath.pslq`` in ``geometor.divine`` (`Blueprint 9`).
