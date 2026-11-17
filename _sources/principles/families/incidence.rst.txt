Family: incidence
=================

14 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``betweeness_condition_i``
     - ``rule``
     - newclid
     - coll(A, B, C), obtuse_angle(A, B, C) => lequation(1/1, A, B, 1/1, B, C, -1/1, A, C, 0)
   * - ``betweeness_condition_ii``
     - ``rule``
     - newclid
     - lequation(1/1, A, B, 1/1, B, C, -1/1, A, C, 0) => coll(A, B, C)
   * - ``collinear``
     - ``relation``
     - geometor_model, leaneuclid, sympy
     - collinear
   * - ``if_a_and_b_are_two_distinct_points_both_lying_on_a_given_line_l_with_a_given_a_point_c_also_lying_on_l_then_the_area_of_the_triangle_abc_is_zero``
     - ``axiom``
     - leaneuclid
     - on_line(c, L)
   * - ``intersect_lines``
     - ``axiom``
     - leaneuclid
     - npara(L, M) => on_line(a, L), on_line(a, M)
   * - ``intersection``
     - ``construction``
     - geometor_model, sympy
     - intersection
   * - ``intersections_circle_line``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(b, L)
   * - ``length_of_a_median_of_a_triangle``
     - ``rule``
     - newclid
     - midp(M, A, B), ncoll(A, B, C) => lequation(2/1, A, M, *, A, M, -2/1, B, C, *, B, C, -2/1, A, C, *, A, C, 1/1, A, B, *, A
   * - ``line_through``
     - ``postulate``
     - euclid, leaneuclid
     - on_line(a, L), on_line(b, L)
   * - ``line_uniqueness``
     - ``axiom``
     - leaneuclid
     - on_line(a, M), on_line(b, M)
   * - :ref:`midpoint <midpoint>`
     - ``construction``
     - alphageometry, euclid, leaneuclid, sympy
     - cong(a, d, d, b), between(a, d, b)
   * - ``midpoint_splits_in_two``
     - ``rule``
     - newclid
     - midp(M, A, B) => ratio_const(M, A, A, B, 1/2)
   * - ``on_line``
     - ``relation``
     - alphageometry, geometor_model, leaneuclid, sympy
     - diff(A, B) => coll(X, A, B)
   * - ``properties_of_midpoint_coll``
     - ``rule``
     - newclid
     - midp(M, A, B) => coll(M, A, B)
