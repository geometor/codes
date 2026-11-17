Family: parallel
================

41 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``alternate_angles_parallel``
     - ``theorem``
     - euclid, leaneuclid
     - eq_angle(a, e, f, e, f, d), opposite_sides(a, d, EF) => para(AE, FD)
   * - ``diagonals_of_parallelogram_ii``
     - ``rule``
     - newclid
     - midp(M, A, B), para(A, C, B, D), para(A, D, B, C), ncoll(A, B, C) => midp(M, C, D)
   * - ``equal_angles_in_an_isosceles_trapezoid``
     - ``rule``
     - newclid
     - cong(A, B, C, D), para(A, D, B, C), npara(A, B, C, D) => eq_angle(C, A, C, B, B, C, B, D)
   * - ``f_g_h_i_and_h_i_f_g_complete_the_proof_that_g_h_f_i``
     - ``theorem``
     - leaneuclid
     - cong(F, G, H, I), para(HI, FG) => cong(G, H, F, I)
   * - ``g_h_e_f_and_e_f_g_h_complete_the_proof_that_f_h``
     - ``theorem``
     - leaneuclid
     - cong(E, F, G, H), para(GH, EF) => eq_angle(E, F, G, E, H, G)
   * - ``given_i_j_g_h_g_h_i_j_complete_the_proof_that_h_i_g_j``
     - ``theorem``
     - leaneuclid
     - cong(I, J, G, H), para(GH, IJ) => cong(H, I, G, J)
   * - ``given_j_k_h_i_j_k_h_i_complete_the_proof_that_k_i``
     - ``theorem``
     - leaneuclid
     - cong(J, K, H, I), para(JK, HI) => eq_angle(H, K, J, H, I, J)
   * - ``if_points_a_and_b_are_both_centers_of_circle_then_a_b_axiom_centre_unique_a_b_point_circle_a_iscentre_b_iscentre_a_b_3_if_a_is_the_centre_of_then_a_is_inside_axiom_center_inside_circle_a_point_circle_a_iscentre_a_insidecircle_4_if_a_point_is_inside_circle_then_a_is_not_on_axiom_inside_not_on_circle_a_point_circle_a_insidecircle_a_oncircle_between_axioms_1_if_b_is_between_a_and_c_then_b_is_between_c_and_a_a_b_a_c_and_a_is_not_a_between_bnd_c_axiom_between_symm_a_b_c_point_between_a_b_c_between_c_b_a_a_b_a_c_between_b_a_c_2_if_b_is_between_a_and_c_a_is_on_l_and_b_is_on_l_then_c_is_on_l_axiom_between_same_line_out_a_b_c_point_l_line_between_a_b_c_a_online_l_b_online_l_c_online_l_3_if_b_is_between_a_and_c_a_is_on_l_and_c_is_on_l_then_b_is_on_l_axiom_between_same_line_in_a_b_c_point_l_line_between_a_b_c_a_online_l_c_online_l_b_online_l_4_if_b_is_between_a_and_c_and_d_is_between_a_and_b_then_d_is_between_a_and_c_axiom_between_trans_in_a_b_c_d_point_between_a_b_c_between_a_d_b_between_a_d_c_5_if_b_is_between_a_and_c_and_c_is_a_between_bnd_d_then_b_is_between_a_and_d_axiom_between_trans_out_a_b_c_d_point_between_a_b_c_between_b_c_d_between_a_b_d_6_if_a_b_and_c_are_distinct_points_on_a_line_l_then_then_either_b_is_between_a_and_c_or_a_is_a_between_bnd_c_or_c_is_between_a_and_b_axiom_between_points_a_b_c_point_l_line_a_b_b_c_c_a_a_online_l_b_online_l_c_online_l_between_a_b_c_between_b_a_c_between_a_c_b_7_if_b_is_between_a_and_c_and_b_is_between_a_and_d_then_b_is_not_between_c_and_d_axiom_between_not_trans_a_b_c_d_point_between_a_b_c_between_a_b_d_between_c_b_d_same_side_axioms_1_if_a_is_not_on_l_then_a_and_a_are_on_the_same_side_of_l_axiom_same_side_rfl_a_point_l_line_a_online_l_a_sameside_a_l_2_if_a_and_b_are_on_the_same_side_of_l_then_b_and_a_are_on_the_same_side_of_l_axiom_same_side_symm_a_b_point_l_line_a_sameside_b_l_b_sameside_a_l_3_if_a_and_b_are_on_the_same_side_of_l_then_a_is_not_on_l_axiom_same_side_not_on_line_a_b_point_l_line_a_sameside_b_l_a_online_l_4_if_a_and_b_are_on_the_same_side_of_l_and_a_and_c_are_on_the_same_side_of_l_then_b_and_c_are_on_the_same_side_of_l_axiom_same_side_trans_a_b_c_point_l_line_a_sameside_b_l_a_sameside_c_l_b_sameside_c_l_5_if_a_b_and_c_are_not_on_l_and_a_and_b_are_not_on_the_same_side_of_l_then_either_a_and_c_are_on_the_same_side_of_l_or_b_and_c_are_on_the_same_side_of_l_axiom_same_side_pigeon_hole_a_b_c_point_l_line_a_online_l_b_online_l_c_online_l_a_sameside_b_l_a_sameside_c_l_b_sameside_c_l_1_if_b_is_between_a_and_c_and_a_and_c_are_on_the_same_side_of_l_then_a_and_b_are_on_the_same_side_of_l_axiom_pasch_1_a_b_c_point_l_line_between_a_b_c_a_sameside_c_l_a_sameside_b_l_2_if_b_is_between_a_and_c_and_a_is_on_l_and_b_is_not_on_l_then_b_and_c_are_on_the_same_side_of_l_axiom_pasch_2_a_b_c_point_l_line_between_a_b_c_a_online_l_b_online_l_b_sameside_c_l_3_if_b_is_between_a_and_c_and_b_is_on_l_then_a_and_c_are_not_on_the_same_side_of_l_see_also_avigad_s_notes_on_this_rule_https_www_andrew_cmu_edu_user_avigad_papers_euclid_notes_htm_axiom_pasch_3_a_b_c_point_l_line_between_a_b_c_b_online_l_a_sameside_c_l_4_if_b_is_the_intersection_of_distinct_lines_l_and_m_a_and_c_are_distinct_points_on_m_a_b_c_b_and_a_and_c_are_not_on_the_same_side_of_l_then_b_is_between_a_and_c_axiom_pasch_4_a_b_c_point_l_m_line_l_m_b_online_l_b_online_m_distinctpointsonline_a_c_m_a_b_c_b_a_sameside_c_l_between_a_b_c_triple_incidence_axioms_1_if_l_m_and_n_are_lines_meeting_at_a_point_a_and_b_c_and_d_are_points_on_l_m_and_n_respectively_and_if_c_and_d_are_on_the_same_side_of_l_and_b_and_c_are_on_the_same_side_of_n_then_b_and_d_are_not_on_the_same_side_of_m_axiom_triple_incidence_1_l_m_n_line_a_b_c_d_point_a_online_l_a_online_m_a_online_n_b_online_l_c_online_m_d_online_n_c_sameside_d_l_b_sameside_c_n_b_sameside_d_m_2_if_l_m_and_n_are_lines_meeting_at_a_point_a_and_b_c_and_d_are_points_on_l_m_and_n_respectively_and_if_c_and_d_are_on_the_same_side_of_l_and_b_and_d_are_not_on_the_same_side_of_m_and_d_is_not_on_m_and_b_a_then_b_and_c_are_on_the_same_side_of_n_axiom_triple_incidence_2_l_m_n_line_a_b_c_d_point_a_online_l_a_online_m_a_online_n_b_online_l_c_online_m_d_online_n_c_sameside_d_l_b_sameside_d_m_d_online_m_b_a_b_sameside_c_n_3_if_l_m_and_n_are_lines_meeting_at_a_point_a_and_b_c_and_d_are_points_on_l_m_and_n_respectively_and_if_c_and_d_are_on_the_same_side_of_l_and_b_and_c_are_on_the_same_side_of_n_and_d_and_e_are_on_the_same_side_of_m_and_c_and_e_are_on_the_same_side_of_n_then_c_and_e_are_on_the_same_side_of_l_axiom_triple_incidence_3_l_m_n_line_a_b_c_d_e_point_a_online_l_a_online_m_a_online_n_b_online_l_c_online_m_d_online_n_c_sameside_d_l_b_sameside_c_n_d_sameside_e_m_c_sameside_e_n_c_sameside_e_l_circle_axioms_1_if_a_b_and_c_are_on_l_a_is_inside_b_and_c_are_on_and_b_c_then_a_is_a_between_bnd_c_axiom_circle_line_intersections_a_b_c_point_l_line_circle_a_online_l_b_online_l_c_online_l_a_insidecircle_b_oncircle_c_oncircle_b_c_between_b_a_c_2_if_a_and_b_are_each_inside_or_on_and_c_is_between_a_and_b_then_c_is_inside_axiom_circle_points_between_a_b_c_point_circle_a_outsidecircle_b_outsidecircle_between_a_c_b_c_insidecircle_3_if_a_is_inside_or_on_c_is_not_inside_and_c_is_between_a_and_b_then_b_is_neither_inside_nor_on_axiom_circle_points_extend_a_b_c_point_circle_a_outsidecircle_c_insidecircle_between_a_c_b_b_outsidecircle_4_let_and_be_distinct_circles_that_intersect_in_distinct_points_c_and_d_let_a_be_a_the_centre_of_let_b_be_the_centre_of_and_let_l_be_the_line_through_a_and_b_then_c_and_d_are_not_on_the_same_side_of_l_axiom_circles_intersections_diff_side_a_b_c_d_point_circle_l_line_c_oncircle_c_oncircle_d_oncircle_d_oncircle_c_d_a_iscentre_b_iscentre_a_online_l_b_online_l_c_sameside_d_l_intersection_rules_1_if_a_and_b_are_on_different_sides_of_l_and_m_is_the_line_through_a_and_b_then_l_and_m_intersect_axiom_intersection_lines_opposing_a_b_point_l_m_line_a_opposingsides_b_l_a_online_m_b_online_m_l_intersectsline_m_not_in_avigad_et_al_2009``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(a, M) => npara(L, M)
   * - ``if_points_a_and_b_are_both_centers_of_circle_then_a_b_axiom_centre_unique_a_b_point_circle_a_iscentre_b_iscentre_a_b_3_if_a_is_the_centre_of_then_a_is_inside_axiom_center_inside_circle_a_point_circle_a_iscentre_a_insidecircle_4_if_a_point_is_inside_circle_then_a_is_not_on_axiom_inside_not_on_circle_a_point_circle_a_insidecircle_a_oncircle_between_axioms_1_if_b_is_between_a_and_c_then_b_is_between_c_and_a_a_b_a_c_and_a_is_not_a_between_bnd_c_axiom_between_symm_a_b_c_point_between_a_b_c_between_c_b_a_a_b_a_c_between_b_a_c_2_if_b_is_between_a_and_c_a_is_on_l_and_b_is_on_l_then_c_is_on_l_axiom_between_same_line_out_a_b_c_point_l_line_between_a_b_c_a_online_l_b_online_l_c_online_l_3_if_b_is_between_a_and_c_a_is_on_l_and_c_is_on_l_then_b_is_on_l_axiom_between_same_line_in_a_b_c_point_l_line_between_a_b_c_a_online_l_c_online_l_b_online_l_4_if_b_is_between_a_and_c_and_d_is_between_a_and_b_then_d_is_between_a_and_c_axiom_between_trans_in_a_b_c_d_point_between_a_b_c_between_a_d_b_between_a_d_c_5_if_b_is_between_a_and_c_and_c_is_a_between_bnd_d_then_b_is_between_a_and_d_axiom_between_trans_out_a_b_c_d_point_between_a_b_c_between_b_c_d_between_a_b_d_6_if_a_b_and_c_are_distinct_points_on_a_line_l_then_then_either_b_is_between_a_and_c_or_a_is_a_between_bnd_c_or_c_is_between_a_and_b_axiom_between_points_a_b_c_point_l_line_a_b_b_c_c_a_a_online_l_b_online_l_c_online_l_between_a_b_c_between_b_a_c_between_a_c_b_7_if_b_is_between_a_and_c_and_b_is_between_a_and_d_then_b_is_not_between_c_and_d_axiom_between_not_trans_a_b_c_d_point_between_a_b_c_between_a_b_d_between_c_b_d_same_side_axioms_1_if_a_is_not_on_l_then_a_and_a_are_on_the_same_side_of_l_axiom_same_side_rfl_a_point_l_line_a_online_l_a_sameside_a_l_2_if_a_and_b_are_on_the_same_side_of_l_then_b_and_a_are_on_the_same_side_of_l_axiom_same_side_symm_a_b_point_l_line_a_sameside_b_l_b_sameside_a_l_3_if_a_and_b_are_on_the_same_side_of_l_then_a_is_not_on_l_axiom_same_side_not_on_line_a_b_point_l_line_a_sameside_b_l_a_online_l_4_if_a_and_b_are_on_the_same_side_of_l_and_a_and_c_are_on_the_same_side_of_l_then_b_and_c_are_on_the_same_side_of_l_axiom_same_side_trans_a_b_c_point_l_line_a_sameside_b_l_a_sameside_c_l_b_sameside_c_l_5_if_a_b_and_c_are_not_on_l_and_a_and_b_are_not_on_the_same_side_of_l_then_either_a_and_c_are_on_the_same_side_of_l_or_b_and_c_are_on_the_same_side_of_l_axiom_same_side_pigeon_hole_a_b_c_point_l_line_a_online_l_b_online_l_c_online_l_a_sameside_b_l_a_sameside_c_l_b_sameside_c_l_1_if_b_is_between_a_and_c_and_a_and_c_are_on_the_same_side_of_l_then_a_and_b_are_on_the_same_side_of_l_axiom_pasch_1_a_b_c_point_l_line_between_a_b_c_a_sameside_c_l_a_sameside_b_l_2_if_b_is_between_a_and_c_and_a_is_on_l_and_b_is_not_on_l_then_b_and_c_are_on_the_same_side_of_l_axiom_pasch_2_a_b_c_point_l_line_between_a_b_c_a_online_l_b_online_l_b_sameside_c_l_3_if_b_is_between_a_and_c_and_b_is_on_l_then_a_and_c_are_not_on_the_same_side_of_l_see_also_avigad_s_notes_on_this_rule_https_www_andrew_cmu_edu_user_avigad_papers_euclid_notes_htm_axiom_pasch_3_a_b_c_point_l_line_between_a_b_c_b_online_l_a_sameside_c_l_4_if_b_is_the_intersection_of_distinct_lines_l_and_m_a_and_c_are_distinct_points_on_m_a_b_c_b_and_a_and_c_are_not_on_the_same_side_of_l_then_b_is_between_a_and_c_axiom_pasch_4_a_b_c_point_l_m_line_l_m_b_online_l_b_online_m_distinctpointsonline_a_c_m_a_b_c_b_a_sameside_c_l_between_a_b_c_triple_incidence_axioms_1_if_l_m_and_n_are_lines_meeting_at_a_point_a_and_b_c_and_d_are_points_on_l_m_and_n_respectively_and_if_c_and_d_are_on_the_same_side_of_l_and_b_and_c_are_on_the_same_side_of_n_then_b_and_d_are_not_on_the_same_side_of_m_axiom_triple_incidence_1_l_m_n_line_a_b_c_d_point_a_online_l_a_online_m_a_online_n_b_online_l_c_online_m_d_online_n_c_sameside_d_l_b_sameside_c_n_b_sameside_d_m_2_if_l_m_and_n_are_lines_meeting_at_a_point_a_and_b_c_and_d_are_points_on_l_m_and_n_respectively_and_if_c_and_d_are_on_the_same_side_of_l_and_b_and_d_are_not_on_the_same_side_of_m_and_d_is_not_on_m_and_b_a_then_b_and_c_are_on_the_same_side_of_n_axiom_triple_incidence_2_l_m_n_line_a_b_c_d_point_a_online_l_a_online_m_a_online_n_b_online_l_c_online_m_d_online_n_c_sameside_d_l_b_sameside_d_m_d_online_m_b_a_b_sameside_c_n_3_if_l_m_and_n_are_lines_meeting_at_a_point_a_and_b_c_and_d_are_points_on_l_m_and_n_respectively_and_if_c_and_d_are_on_the_same_side_of_l_and_b_and_c_are_on_the_same_side_of_n_and_d_and_e_are_on_the_same_side_of_m_and_c_and_e_are_on_the_same_side_of_n_then_c_and_e_are_on_the_same_side_of_l_axiom_triple_incidence_3_l_m_n_line_a_b_c_d_e_point_a_online_l_a_online_m_a_online_n_b_online_l_c_online_m_d_online_n_c_sameside_d_l_b_sameside_c_n_d_sameside_e_m_c_sameside_e_n_c_sameside_e_l_circle_axioms_1_if_a_b_and_c_are_on_l_a_is_inside_b_and_c_are_on_and_b_c_then_a_is_a_between_bnd_c_axiom_circle_line_intersections_a_b_c_point_l_line_circle_a_online_l_b_online_l_c_online_l_a_insidecircle_b_oncircle_c_oncircle_b_c_between_b_a_c_2_if_a_and_b_are_each_inside_or_on_and_c_is_between_a_and_b_then_c_is_inside_axiom_circle_points_between_a_b_c_point_circle_a_outsidecircle_b_outsidecircle_between_a_c_b_c_insidecircle_3_if_a_is_inside_or_on_c_is_not_inside_and_c_is_between_a_and_b_then_b_is_neither_inside_nor_on_axiom_circle_points_extend_a_b_c_point_circle_a_outsidecircle_c_insidecircle_between_a_c_b_b_outsidecircle_4_let_and_be_distinct_circles_that_intersect_in_distinct_points_c_and_d_let_a_be_a_the_centre_of_let_b_be_the_centre_of_and_let_l_be_the_line_through_a_and_b_then_c_and_d_are_not_on_the_same_side_of_l_axiom_circles_intersections_diff_side_a_b_c_d_point_circle_l_line_c_oncircle_c_oncircle_d_oncircle_d_oncircle_c_d_a_iscentre_b_iscentre_a_online_l_b_online_l_c_sameside_d_l_intersection_rules_1_if_a_and_b_are_on_different_sides_of_l_and_m_is_the_line_through_a_and_b_then_l_and_m_intersect_axiom_intersection_lines_opposing_a_b_point_l_m_line_a_opposingsides_b_l_a_online_m_b_online_m_l_intersectsline_m_not_in_avigad_et_al_2009_axiom_intersection_lines_common_point_a_point_l_m_line_a_online_l_a_online_m_l_m_l_intersectsline_m_not_in_avigad_et_al_2009_axiom_parallel_line_unique_a_point_l_m_n_line_a_online_l_a_online_m_a_online_n_l_intersectsline_m_l_intersectsline_n_m_n_not_in_avigad_et_al_2009``
     - ``axiom``
     - leaneuclid
     - npara(L, M) => npara(M, L)
   * - ``intersection_ll``
     - ``construction``
     - alphageometry
     - npara(A, B, C, D), ncoll(A, B, C, D) => coll(X, A, B), coll(X, C, D)
   * - ``intersection_lp``
     - ``construction``
     - alphageometry
     - npara(M, N, A, B), ncoll(A, B, C), ncoll(C, M, N) => coll(X, A, B), para(C, X, M, N)
   * - ``intersection_pp``
     - ``construction``
     - alphageometry
     - diff(A, D), npara(B, C, E, F) => para(X, A, B, C), para(X, D, E, F)
   * - ``intersection_tt``
     - ``construction``
     - alphageometry
     - diff(A, D), npara(B, C, E, F) => perp(X, A, B, C), perp(X, D, E, F)
   * - ``isquare``
     - ``construction``
     - alphageometry
     - a(B), d(:, A, B, C), b(:), c(:, perp, A, B, B, C), cong(A, B, B, C), d(:, para, A, B, C, D), para(A, D, B, C), perp(A, D
   * - ``midline_parallel``
     - ``theorem``
     - alphageometry, newclid
     - midp(E, A, B), midp(F, A, C) => para(E, F, B, C)
   * - ``not_parallel``
     - ``relation``
     - leaneuclid
     - not_parallel
   * - ``parallel``
     - ``predicate``
     - geometor_model
     - parallel
   * - :ref:`parallel_alternate_angles <parallel_alternate_angles>`
     - ``theorem``
     - euclid, leaneuclid
     - between(a, g, b), between(c, h, d), between(e, g, h), between(g, h, f), same_side(b, d, EF), para(AB, CD) => eq_angle(a,
   * - ``parallel_from_collinear``
     - ``rule``
     - newclid
     - coll(A, B, C) => para(A, B, B, C), para(A, B, A, C)
   * - ``parallel_from_inclination``
     - ``inference_rule``
     - alphageometry, newclid
     - eq_angle(A, B, P, Q, C, D, P, Q) => para(A, B, C, D)
   * - ``parallel_line``
     - ``construction``
     - alphageometry, euclid, leaneuclid
     - on_line(a, BC) => on_line(a, EF), para(EF, BC)
   * - ``parallel_postulate``
     - ``postulate``
     - euclid
     - That, if a straight line falling on two straight lines make the interior angles on the same side less than two right ang
   * - ``parallel_transitivity``
     - ``theorem``
     - euclid, leaneuclid
     - para(AB, EF), para(CD, EF) => para(AB, CD)
   * - ``parallelogram``
     - ``construction``
     - alphageometry
     - ncoll(A, B, C) => para(A, B, C, X), para(A, X, B, C), cong(A, B, C, X), cong(A, X, B, C)
   * - ``parallelogram_diagonals_bisect``
     - ``theorem``
     - alphageometry, newclid
     - midp(M, A, B), midp(M, C, D) => para(A, C, B, D)
   * - ``parallelogram_law``
     - ``rule``
     - newclid
     - para(A, B, C, D), para(A, D, B, C), ncoll(A, B, C) => lequation(2/1, A, B, *, A, B, 2/1, B, C, *, B, C, -1/1, A, C, *, A
   * - ``parallelogram_opposite_sides``
     - ``theorem``
     - euclid, leaneuclid
     - cong(a, b, c, d), same_side(a, c, BD), para(AB, CD) => cong(a, c, b, d), para(AC, BD)
   * - ``parallelogram_properties``
     - ``theorem``
     - euclid, leaneuclid
     - cong(a, b, c, d), cong(a, c, b, d), eq_angle(a, b, d, a, c, d), eq_angle(b, a, c, c, d, b)
   * - ``perpendiculars_parallel``
     - ``inference_rule``
     - alphageometry, newclid
     - perp(A, B, C, D), perp(C, D, E, F), ncoll(A, B, E) => para(A, B, E, F)
   * - ``playfair_uniqueness``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(a, M), on_line(a, N), para(L, M), para(L, N)
   * - ``q_t_s_q_r_s_and_r_s_t_r_q_t_complete_the_proof_that_q_t_r_s``
     - ``theorem``
     - leaneuclid
     - eq_angle(Q, T, S, Q, R, S), eq_angle(R, S, T, R, Q, T) => para(QT, RS)
   * - ``r08``
     - ``rule``
     - alphageometry, newclid
     - perp(A, B, C, D), perp(E, F, G, H), npara(A, B, E, F) => eq_angle(A, B, E, F, C, D, G, H)
   * - ``r26``
     - ``rule``
     - alphageometry
     - midp(M, A, B), para(A, C, B, D), para(A, D, B, C) => midp(M, C, D)
   * - ``r28``
     - ``rule``
     - alphageometry, newclid
     - para(A, B, A, C) => coll(A, B, C)
   * - ``r42``
     - ``rule``
     - alphageometry
     - para(A, B, C, D), coll(M, A, D), coll(N, B, C), para(M, N, A, B) => eq_ratio(M, A, M, D, N, B, N, C)
   * - ``rectangle``
     - ``construction``
     - alphageometry
     - a(B, C), d(:, A, B, C), b(:), c(:, perp, A, B, B, C), d(:, para, A, B, C, D), para(A, D, B, C), perp(A, B, A, D), cong(A
   * - ``square``
     - ``construction``
     - alphageometry
     - diff(A, B) => a(B), y(:, A, B, X), perp(A, B, B, X), cong(A, B, B, X), y(:, para, A, B, X, Y), para(A, Y, B, X), perp(A,
   * - ``t_u_v_w_and_v_w_t_u_complete_the_proof_that_v_t_w_t_v_u``
     - ``theorem``
     - leaneuclid
     - cong(V, W, T, U), para(TU, VW) => eq_angle(V, T, W, T, V, U)
   * - ``thales_theorem_iv``
     - ``rule``
     - newclid
     - para(A, B, C, D), coll(M, A, D), coll(N, B, C), para(M, N, A, B), ncoll(A, B, C) => eq_ratio(M, A, M, D, N, B, N, C)
   * - :ref:`triangle_angle_sum <triangle_angle_sum>`
     - ``theorem``
     - alphageometry, euclid, leaneuclid, newclid
     - between(b, c, d), form_triangle(a, b, c, AB, BC, AC) => eq_angle(a, c, d, c, a, b)
   * - ``x_y_v_y_v_w_x_y_and_v_w_w_x_complete_the_proof_that_v_y_w_x``
     - ``theorem``
     - leaneuclid
     - para(VW, XY) => cong(V, Y, W, X)
