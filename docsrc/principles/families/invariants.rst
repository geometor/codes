Family: invariants
==================

12 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``geometor_model_angle_cross``
     - ``measure``
     - geometor_model
     - Exact rational trigonometry cross :math:`c(\angle BAC) = \cos^2\theta`.
   * - ``geometor_model_angle_degrees``
     - ``measure``
     - geometor_model
     - Interior angle measure in degrees.
   * - ``geometor_model_angle_radians``
     - ``measure``
     - geometor_model
     - Interior angle measure in radians in :math:`[0, \pi]`.
   * - ``geometor_model_invariants_cross``
     - ``measure``
     - geometor_model
     - Compute the exact rational cross :math:`c(l_1, l_2) = \cos^2\theta = 1 - s(l_1, l_2)`.
   * - ``geometor_model_invariants_cross_ratio``
     - ``measure``
     - geometor_model
     - Compute the exact projective cross-ratio :math:`(A, B; C, D) = \frac{\overline{AC}\cdot\overline{BD}}{\overline{BC}\cdot
   * - ``geometor_model_invariants_is_harmonic``
     - ``predicate``
     - geometor_model
     - Return ``True`` iff ``(A, B; C, D) == -1`` forms an exact harmonic range.
   * - ``geometor_model_invariants_line_spread``
     - ``measure``
     - geometor_model
     - Compute the exact rational spread :math:`s(l_1, l_2) = \sin^2\theta` between two lines.
   * - ``geometor_model_invariants_orientation``
     - ``measure``
     - geometor_model
     - Return ``+1`` if ``(A, B, C)`` is counter-clockwise, ``-1`` if clockwise, ``0`` if collinear.
   * - ``geometor_model_invariants_polygon_area2``
     - ``measure``
     - geometor_model
     - Compute exact unsigned twice-area :math:`\|2 \cdot \text{Area}\|` of a simple polygon via shoelace.
   * - ``geometor_model_invariants_signed_area2``
     - ``measure``
     - geometor_model
     - Return twice the signed area of triangle ``ABC``: :math:`(x_B - x_A)(y_C - y_A) - (y_B - y_A)(x_C - x_A)`.
   * - ``geometor_model_invariants_vertex_dot_sign``
     - ``measure``
     - geometor_model
     - Return ``+1`` if ``< B A C )`` is acute, ``0`` if right, or ``-1`` if obtuse.
   * - ``geometor_model_invariants_vertex_spread``
     - ``measure``
     - geometor_model
     - Compute the exact spread at vertex ``A`` between rays ``AB`` and ``AC`` (``< B A C )``).
