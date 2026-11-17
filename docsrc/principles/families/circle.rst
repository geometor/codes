Family: circle
==============

44 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``alternate_segment_angle``
     - ``theorem``
     - alphageometry, euclid, newclid
     - circle_center(O, A, B, C), perp(O, A, A, X) => eq_angle(A, X, A, B, C, A, C, B)
   * - ``alternate_segment_tangent``
     - ``theorem``
     - alphageometry, newclid
     - circle_center(O, A, B, C), eq_angle(A, X, A, B, C, A, C, B) => perp(O, A, A, X)
   * - ``any_diameter_of_a_circle_crosses_the_center``
     - ``rule``
     - newclid
     - midp(O, A, B), circle_center(O, A, B, C), cyclic(A, B, C, D), cong(A, B, C, D) => coll(O, C, D)
   * - ``center_uniqueness``
     - ``axiom``
     - leaneuclid
     - If points `a` and `b` are both centers of `(α : Circle)` then `a = b`
   * - ``central_inscribed_angle``
     - ``theorem``
     - alphageometry, euclid, newclid
     - circle_center(O, A, B, C), midp(M, B, C) => eq_angle(A, B, A, C, O, B, O, M)
   * - ``characterization_of_circumcenter_i``
     - ``rule``
     - newclid
     - cong(O, A, O, C), aequation(1/1, A, B, B, C, 1/1, C, A, A, O, 90o) => circle_center(O, A, B, C)
   * - ``characterization_of_circumcenter_ii``
     - ``rule``
     - newclid
     - circle_center(O, A, B, C) => aequation(1/1, A, B, B, C, 1/1, C, A, A, O, 90o)
   * - ``circle_center``
     - ``construction``
     - euclid
     - To find the centre of a given circle.
   * - ``circle_through``
     - ``postulate``
     - euclid, leaneuclid
     - To describe a circle with any centre and distance.
   * - ``circumcircle``
     - ``construction``
     - sympy
     - circumcircle
   * - ``concyclic``
     - ``predicate``
     - geometor_model, sympy
     - concyclic
   * - ``concyclic_equidistant``
     - ``definition``
     - alphageometry, newclid
     - cong(O, A, O, B), cong(O, B, O, C), cong(O, C, O, D) => cyclic(A, B, C, D)
   * - ``concyclic_from_equal_angles``
     - ``theorem``
     - alphageometry, newclid
     - eq_angle(P, A, P, B, Q, A, Q, B), ncoll(P, Q, A, B) => cyclic(A, B, P, Q)
   * - ``cyclic_quadrilateral_angles``
     - ``theorem``
     - euclid
     - The opposite angles of quadrilaterals in circles are equal to two right angles.
   * - ``definition_of_circle``
     - ``rule``
     - newclid
     - cong(O, A, O, B), cong(O, B, O, C) => circle_center(O, A, B, C)
   * - ``disassembling_a_circle``
     - ``rule``
     - newclid
     - circle_center(O, A, B, C) => cong(O, A, O, B), cong(O, B, O, C)
   * - ``equal_arcs_equal_chords``
     - ``theorem``
     - alphageometry, newclid
     - cyclic(A, B, C, P, Q, R), eq_angle(C, A, C, B, R, P, R, Q) => cong(A, B, P, Q)
   * - ``incircle``
     - ``construction``
     - sympy
     - incircle
   * - :ref:`inscribed_angles_same_arc <inscribed_angles_same_arc>`
     - ``theorem``
     - alphageometry, euclid, newclid
     - cyclic(A, B, P, Q) => eq_angle(P, A, P, B, Q, A, Q, B)
   * - ``inside_circle``
     - ``relation``
     - leaneuclid
     - inside_circle
   * - ``intersecting_chords``
     - ``theorem``
     - euclid
     - If in a circle two straight lines cut one another, the rectangle contained by the segments of the one is equal to the re
   * - ``intersection_of_angle_bisector_and_perpendicular_bisector``
     - ``rule``
     - newclid
     - eq_angle(C, A, C, D, C, D, C, B), cong(D, A, D, B), ncoll(A, B, C, D), nperp(A, B, C, D) => cyclic(A, B, C, D)
   * - ``is_center``
     - ``relation``
     - leaneuclid
     - is_center
   * - ``nine_point_circle``
     - ``construction``
     - sympy
     - nine_point_circle
   * - ``on_circle``
     - ``relation``
     - alphageometry, leaneuclid
     - diff(O, A) => cong(O, X, O, A)
   * - ``on_circum``
     - ``construction``
     - alphageometry
     - ncoll(A, B, C) => cyclic(A, B, C, X)
   * - ``r18``
     - ``rule``
     - alphageometry, newclid
     - circle_center(O, A, B, C), coll(M, B, C), eq_angle(A, B, A, C, O, B, O, M) => midp(M, B, C)
   * - ``r21``
     - ``rule``
     - alphageometry, newclid
     - cyclic(A, B, C, D), para(A, B, C, D) => eq_angle(A, D, C, D, C, D, C, B)
   * - ``r24``
     - ``rule``
     - alphageometry, newclid
     - cong(A, P, B, P), cong(A, Q, B, Q), cyclic(A, B, P, Q) => perp(P, A, A, Q)
   * - ``recognize_center_of_circle_cyclic``
     - ``rule``
     - newclid
     - circle_center(O, A, B, C), cyclic(A, B, C, D) => cong(O, A, O, D)
   * - ``recognize_center_of_cyclic_cong``
     - ``rule``
     - newclid
     - cyclic(A, B, C, D), cong(O, A, O, B), cong(O, C, O, D), npara(A, B, C, D) => cong(O, A, O, C)
   * - ``same_chord_same_arc_ii``
     - ``rule``
     - newclid
     - cyclic(A, B, C, P, Q, R), cong(A, B, P, Q), nperp(A, C, B, C), same_clock(C, B, A, R, P, Q), not_same_side(C, B, A, R, P
   * - ``same_chord_same_arc_iii``
     - ``rule``
     - newclid
     - cyclic(A, B, P, Q), cong(A, B, P, Q), npara(A, P, B, Q) => eq_angle(P, A, P, B, P, B, Q, B)
   * - ``same_chord_same_arc_iv``
     - ``rule``
     - newclid
     - cyclic(A, B, P, Q), cong(A, B, P, Q), same_clock(A, P, B, A, P, Q) => eq_angle(P, A, P, B, Q, B, P, B)
   * - :ref:`simson_line <simson_line>`
     - ``theorem``
     - newclid
     - cyclic(A, B, C, P), coll(A, L, C), perp(P, L, A, C), coll(M, B, C), perp(P, M, B, C), coll(N, A, B), perp(P, N, A, B) =>
   * - ``sympy_circle_equation``
     - ``construction``
     - sympy
     - The equation of the circle.
   * - ``sympy_circle_radius``
     - ``measure``
     - sympy
     - The radius of the circle.
   * - ``sympy_circle_reflect``
     - ``construction``
     - sympy
     - Override GeometryEntity.reflect since the radius
   * - ``sympy_circle_scale``
     - ``construction``
     - sympy
     - Override GeometryEntity.scale since the radius
   * - ``tangent``
     - ``construction``
     - alphageometry
     - diff(O, A), diff(O, B), diff(A, B) => cong(O, X, O, B), perp(A, X, O, X), y(:, cong, O, Y, O, B), perp(A, Y, O, Y)
   * - ``tangent_lines``
     - ``construction``
     - euclid, sympy
     - From a given point to draw a straight line touching a given circle.
   * - ``tangent_secant_power``
     - ``theorem``
     - euclid
     - If a point be taken outside a circle and from it there fall on the circle two straight lines, and if one of them cut the
   * - :ref:`thales_semicircle <thales_semicircle>`
     - ``theorem``
     - alphageometry, euclid, newclid
     - circle_center(O, A, B, C), coll(O, A, C) => perp(A, B, B, C)
   * - ``thales_semicircle_converse``
     - ``theorem``
     - alphageometry, newclid
     - perp(A, B, B, C), midp(M, A, C) => cong(A, M, B, M)
