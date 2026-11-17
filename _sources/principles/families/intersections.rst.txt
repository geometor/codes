Family: intersections
=====================

5 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``geometor_model_intersections_intersect_2d``
     - ``construction``
     - geometor_model
     - Compute exact symbolic intersections of 2D lines, circles, and segments.
   * - ``geometor_model_intersections_proposition``
     - ``construction``
     - geometor_model
     - Decorator marking a Euclidean construction function as a composable proposition.
   * - ``geometor_model_intersectionsmixin_intersect_all``
     - ``construction``
     - geometor_model
     - Compute and register all real intersections between ``s1`` and ``s2``.
   * - ``geometor_model_intersectionsmixin_subconstruction``
     - ``construction``
     - geometor_model
     - Execute a scoped sub-construction block with automatic guide encapsulation.
   * - ``leaneuclid_intersection_circles``
     - ``axiom``
     - leaneuclid
     - ∀ (α β : Circle), α.intersectsCircle β → ∃ a : Point, (a.onCircle α) ∧ (a.onCircle β)
