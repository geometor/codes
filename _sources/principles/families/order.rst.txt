Family: order
=============

109 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``3_if_b_is_between_a_and_c_a_is_on_l_and_c_is_on_l_then_b_is_on_l``
     - ``axiom``
     - leaneuclid
     - between(a, b, c), on_line(a, L), on_line(c, L) => on_line(b, L)
   * - ``4_let_and_be_distinct_circles_that_intersect_in_distinct_points_c_and_d_let_a_be_a_the_centre_of_let_b_be_the_centre_of_and_let_l_be_the_line_through_a_and_b_then_c_and_d_are_not_on_the_same_side_of_l``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(b, L) => same_side(c, d, L)
   * - ``a_stronger_version_of_the_points_construction_rule_6_in_avigad_et_al_2009_which_is_convenient_for_proving_some_propositions``
     - ``axiom``
     - leaneuclid
     - on_line(b, L), npara(L, M) => on_line(a, M), same_side(a, b, L)
   * - ``between``
     - ``relation``
     - leaneuclid
     - between
   * - :ref:`betweenness_symmetry <betweenness_symmetry>`
     - ``axiom``
     - leaneuclid
     - between(a, b, c) => between(c, b, a), between(b, a, c)
   * - :ref:`betweenness_transitivity <betweenness_transitivity>`
     - ``axiom``
     - leaneuclid
     - between(a, b, c), between(a, d, b) => between(a, d, c)
   * - ``circle_axioms_if_a_b_and_c_are_on_l_a_is_inside_b_and_c_are_on_and_b_c_then_a_is_a_between_bnd_c``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(b, L), on_line(c, L) => between(b, a, c)
   * - ``diagram_angle_transfer_axioms_suppose_a_b_a_c_a_is_on_l_and_b_is_on_l_then_c_is_on_l_and_a_is_not_between_b_and_c_if_and_only_if_bac_0_given_points_a_b_and_c_such_that_a_is_not_equal_to_b_and_a_is_not_equal_to_c_and_line_l_such_that_a_b_and_c_are_all_on_l_and_a_is_not_between_b_and_c_then_the_angle_bac_has_degree_zero``
     - ``axiom``
     - leaneuclid
     - between(b, a, c), on_line(a, L), on_line(b, L), on_line(c, L)
   * - ``distinct_point_same_side``
     - ``axiom``
     - leaneuclid
     - on_line(b, L) => same_side(a, b, L)
   * - ``exists_distinct_point_opposite_side``
     - ``axiom``
     - leaneuclid
     - on_line(b, L) => opposite_sides(a, b, L)
   * - ``exists_point_between_points_not_on_line``
     - ``axiom``
     - leaneuclid
     - between(b, a, c), on_line(a, L), on_line(a, M)
   * - ``exists_point_between_points_on_line``
     - ``axiom``
     - leaneuclid
     - between(b, a, c), on_line(a, L)
   * - ``extend_point_not_on_line``
     - ``axiom``
     - leaneuclid
     - between(b, c, a), on_line(a, L), on_line(a, M)
   * - ``extension``
     - ``postulate``
     - euclid, leaneuclid
     - between(b, c, a), on_line(a, L)
   * - ``exterior_angle_inequality``
     - ``theorem``
     - euclid, leaneuclid
     - between(b, c, d), form_triangle(a, b, c, AB, BC, AC)
   * - ``f_g_g_h_e_g_g_i_complete_the_proof_that_e_f_g_i_h_g``
     - ``theorem``
     - leaneuclid
     - cong(G, H, E, G), between(E, G, I), between(F, G, H), form_triangle(E, F, G, EF, FH, EI), form_triangle(H, I, G, HI, EI,
   * - ``g_is_the_midpoint_of_f_h_g_j_f_i_and_g_i_h_j_complete_the_proof_that_j_i``
     - ``theorem``
     - leaneuclid
     - cong(F, G, H, G), cong(G, J, F, I), cong(G, I, H, J), between(F, G, H), same_side(I, J, FH), form_triangle(F, I, G, FI, 
   * - ``g_j_g_h_g_k_g_i_complete_the_proof_that_g_j_k_g_h_i``
     - ``theorem``
     - leaneuclid
     - cong(G, H, G, K), between(G, J, H), between(G, K, I), form_triangle(G, H, I, GH, HI, GI), form_triangle(G, J, K, GH, JK,
   * - ``g_k_h_j_complete_the_proof_that_g_k_g_h_k_180_without_using_the_triangle_angle_sum_theorem``
     - ``theorem``
     - leaneuclid
     - between(G, H, I), on_line(H, GI), same_side(J, K, GI), para(GK, HJ)
   * - ``given_e_h_bisects_f_e_g_and_e_g_e_f_complete_the_proof_that_g_h_f_h``
     - ``theorem``
     - leaneuclid
     - cong(E, G, E, F), eq_angle(H, E, F, H, E, G), between(F, H, G), on_line(H, FG), form_triangle(E, F, G, EF, FG, GE), npar
   * - ``given_g_e_complete_the_proof_that_g_h_i_e_f_i``
     - ``theorem``
     - leaneuclid
     - eq_angle(H, G, I, F, E, I), between(E, I, G), between(H, I, F), form_triangle(E, F, I, EF, FH, EG), form_triangle(G, H, 
   * - ``given_g_i_f_h_and_h_i_f_i_complete_the_proof_that_f_h_i_i_h_g``
     - ``theorem``
     - leaneuclid
     - between(F, G, H), form_triangle(F, G, I, FH, GI, FI), form_triangle(G, H, I, FH, HI, GI) => sim_tri(F, H, I, I, H, G)
   * - ``given_g_j_h_k_and_k_j_g_j_h_k_complete_the_proof_that_h_i_k_g_h_j``
     - ``theorem``
     - leaneuclid
     - cong(G, J, H, K), eq_angle(H, K, I, G, J, H), between(G, H, I), same_side(J, K, GI), form_triangle(G, J, H, GJ, JH, GI),
   * - ``given_g_j_i_j_and_h_j_g_i_complete_the_proof_that_h_i_j_h_j_g``
     - ``theorem``
     - leaneuclid
     - between(G, H, I), form_triangle(G, H, J, GI, HJ, GJ), form_triangle(H, I, J, GI, IJ, HJ) => sim_tri(H, I, J, H, J, G)
   * - ``given_h_j_h_i_k_is_the_midpoint_of_i_j_complete_the_proof_that_h_k_j_h_k_i``
     - ``theorem``
     - leaneuclid
     - cong(H, I, H, J), cong(K, I, K, J), between(I, K, J), on_line(K, IJ), form_triangle(H, I, J, HI, IJ, JH), npara(IJ, HK) 
   * - ``given_h_j_w_y_and_t_v_h_j_complete_the_proof_that_s_x_y_t_u_z``
     - ``theorem``
     - leaneuclid
     - between(H, I, J), between(S, U, X), between(W, X, Y), between(U, X, I), between(T, U, V), between(X, I, Z), same_side(V,
   * - ``given_h_k_bisects_i_h_j_and_h_i_h_j_complete_the_proof_that_h_k_i_h_k_j``
     - ``theorem``
     - leaneuclid
     - cong(H, I, H, J), eq_angle(I, H, K, J, H, K), between(I, K, J), on_line(K, IJ), form_triangle(H, I, J, HI, IJ, JH), npar
   * - ``given_i_f_complete_the_proof_that_g_h_i_g_e_f``
     - ``theorem``
     - leaneuclid
     - eq_angle(H, I, G, E, F, G), between(E, G, I), between(F, G, H), form_triangle(E, F, G, EF, FH, EI), form_triangle(H, I, 
   * - ``given_i_k_h_j_and_h_i_i_j_complete_the_proof_that_i_j_k_h_i_k``
     - ``theorem``
     - leaneuclid
     - between(H, K, J), form_triangle(H, I, K, HI, IK, HJ), form_triangle(I, J, K, IJ, HJ, IK) => sim_tri(I, J, K, H, I, K)
   * - ``given_p_r_q_s_complete_the_proof_that_p_r_t_s_q_t``
     - ``theorem``
     - leaneuclid
     - between(P, T, S), between(Q, T, R), form_triangle(P, R, T, PR, QR, PS), form_triangle(Q, S, T, QS, PS, QR), para(PR, QS)
   * - ``given_p_r_s_t_r_s_and_s_t_p_t_complete_the_proof_that_r_s_t_p_t_s``
     - ``theorem``
     - leaneuclid
     - eq_angle(S, P, T, T, R, S), same_side(P, R, ST), form_triangle(P, S, T, PS, ST, PT), form_triangle(R, S, T, RS, ST, RT) 
   * - ``given_p_s_complete_the_proof_that_p_r_t_s_r_q``
     - ``theorem``
     - leaneuclid
     - eq_angle(R, P, T, R, S, Q), between(P, R, Q), between(S, R, T), form_triangle(P, R, T, PQ, ST, PT), form_triangle(Q, S, 
   * - ``given_points_a_and_b_both_lying_on_a_given_line_l_and_point_c_lying_between_a_and_b_and_point_d_not_on_l_such_that_the_angle_acd_is_a_right_angle_then_the_angle_acd_is_equal_to_the_angle_dcb``
     - ``axiom``
     - leaneuclid
     - between(a, c, b), on_line(a, L), on_line(b, L), on_line(d, L) => eq_angle(a, c, d, d, c, b)
   * - ``given_points_a_b_and_c_such_that_a_is_not_equal_to_b_and_a_is_not_equal_to_c_and_line_l_such_that_a_and_b_are_on_l_and_the_angle_formed_by_b_a_c_has_degree_zero_then_c_is_on_l_and_a_is_not_between_b_and_c``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(b, L) => between(b, a, c), on_line(c, L)
   * - ``given_points_a_b_and_c_such_that_a_is_not_equal_to_b_and_a_is_not_equal_to_c_and_line_l_such_that_a_and_b_are_on_l_and_the_angle_formed_by_b_a_c_has_degree_zero_then_c_is_on_l_and_a_is_not_between_b_and_c_axiom_degenerated_angle_onlyif_a_b_c_point_l_line_a_b_a_c_a_online_l_b_online_l_b_a_c_0_c_online_l_between_b_a_c_suppose_a_is_on_l_and_m_b_is_on_l_c_is_on_m_a_b_a_c_d_is_not_on_l_or_m_and_l_m_then_bac_bad_dac_if_and_only_if_b_and_d_are_on_the_same_side_of_m_and_c_and_d_are_on_the_same_side_of_l_given_point_on_a_given_lines_l_and_m_point_b_on_l_and_point_c_on_m_with_a_distinct_from_b_a_distinct_from_c_point_d_not_on_l_or_m_and_l_distinct_from_m_then_the_angle_bac_is_equal_to_the_sum_of_angles_bad_and_dac_only_if_b_and_d_are_on_the_same_side_of_m_and_c_and_d_are_on_the_same_side_of_l_kaiyu_jeremy_s_typo_here``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(a, M), on_line(b, L), on_line(c, M), on_line(d, L), on_line(d, M) => same_side(b, d, M), same_sid
   * - ``given_q_r_u_q_u_r_and_s_t_r_u_complete_the_proof_that_r_s_t_t``
     - ``theorem``
     - leaneuclid
     - eq_angle(Q, R, U, Q, U, R), between(Q, R, S), between(Q, U, T), on_line(R, QS), on_line(U, QT), para(ST, RU) => eq_angle
   * - ``given_q_s_q_t_and_q_s_r_s_u_is_the_midpoint_of_q_s_complete_the_proof_that_q_t_u_s_r_u``
     - ``theorem``
     - leaneuclid
     - cong(Q, U, S, U), between(Q, U, S), between(R, U, T), form_triangle(Q, T, U, QT, RT, QS), form_triangle(R, S, U, RS, QS,
   * - ``given_r_q_s_s_p_t_and_p_t_q_r_p_q_s_is_equilateral_complete_the_proof_that_p_s_t_q_s_r``
     - ``theorem``
     - leaneuclid
     - cong(P, T, Q, R), cong(P, Q, Q, S), cong(Q, S, S, P), eq_angle(R, Q, S, S, P, T), same_side(Q, R, PS), same_side(P, T, Q
   * - ``given_r_s_q_s_and_q_s_q_t_u_is_the_midpoint_of_q_s_complete_the_proof_that_r_s_u_t_q_u``
     - ``theorem``
     - leaneuclid
     - cong(S, U, Q, U), between(Q, U, S), between(R, U, T), form_triangle(Q, T, U, QT, RT, QS), form_triangle(R, S, U, RS, QS,
   * - ``given_r_s_q_t_and_q_q_t_u_complete_the_proof_that_s_s_r_u``
     - ``theorem``
     - leaneuclid
     - eq_angle(T, Q, U, Q, T, U), between(Q, U, S), between(R, U, T), para(RS, QT) => eq_angle(R, S, U, S, R, U)
   * - ``given_r_t_q_t_r_u_complete_the_proof_that_p_r_u_p_t_q``
     - ``theorem``
     - leaneuclid
     - cong(Q, T, R, U), eq_angle(P, R, U, P, T, Q), between(P, Q, R), between(P, U, T), form_triangle(P, R, U, PR, RU, PT), fo
   * - ``given_r_t_s_and_v_w_y_are_supplementary_complete_the_proof_that_v_x_s_u``
     - ``theorem``
     - leaneuclid
     - between(S, T, U), between(T, W, Y), between(V, W, X), between(R, T, W), same_side(V, S, RY), same_side(X, U, RY) => para
   * - ``given_r_t_u_w_complete_the_proof_that_t_s_v_s_v_w_180``
     - ``theorem``
     - leaneuclid
     - between(R, S, T), between(Q, S, V), between(U, V, W), between(S, V, X), same_side(T, W, QX), same_side(R, U, QX), para(R
   * - ``given_s_t_r_s_and_q_r_r_s_and_q_s_r_p_s_t_and_p_t_s_t_complete_the_proof_that_p_t_q_r``
     - ``theorem``
     - leaneuclid
     - cong(S, T, R, S), eq_angle(Q, S, R, P, S, T), same_side(Q, R, PS), same_side(P, T, QS), opposite_sides(P, R, QS), opposi
   * - ``given_s_t_r_t_and_s_t_r_u_and_r_u_r_t_complete_the_proof_that_s_t_v_u_r_v``
     - ``theorem``
     - leaneuclid
     - cong(S, T, R, U), between(R, V, T), between(S, V, U), form_triangle(R, U, V, RU, SU, RT), form_triangle(S, T, V, ST, RT,
   * - ``given_s_t_w_and_t_w_v_are_supplementary_complete_the_proof_that_s_u_v_x``
     - ``theorem``
     - leaneuclid
     - between(S, T, U), between(R, T, W), between(V, W, X), between(T, W, Y), same_side(V, S, RY), same_side(U, X, RY) => para
   * - ``given_t_and_t_v_u_are_supplementary_complete_the_proof_that_u_v_w_s_t_w``
     - ``theorem``
     - leaneuclid
     - between(S, U, W), between(T, V, W), form_triangle(S, T, W, ST, TW, SW), form_triangle(U, V, W, UV, TW, SW) => sim_tri(U,
   * - ``given_t_u_r_s_r_s_t_u_complete_the_proof_that_r_t_u_t_r_s``
     - ``theorem``
     - leaneuclid
     - cong(T, U, R, S), opposite_sides(S, U, RT), form_triangle(R, S, T, RS, ST, RT), form_triangle(R, T, U, RT, TU, RU), para
   * - ``given_t_u_v_w_t_u_v_w_complete_the_proof_that_t_u_v_v_w_t``
     - ``theorem``
     - leaneuclid
     - cong(T, U, V, W), opposite_sides(U, W, TV), form_triangle(T, U, V, TU, UV, TV), form_triangle(T, V, W, TV, VW, TW), para
   * - ``given_t_u_w_u_t_w_and_s_v_t_u_complete_the_proof_that_v_s``
     - ``theorem``
     - leaneuclid
     - eq_angle(T, U, W, U, T, W), between(S, W, U), between(T, W, V), para(SV, TU) => eq_angle(W, V, S, W, S, V)
   * - ``given_t_u_x_w_and_u_x_v_w_complete_the_proof_that_u_v_w_w``
     - ``theorem``
     - leaneuclid
     - eq_angle(T, U, X, T, W, V), between(T, U, V), between(T, X, W), on_line(U, TV), on_line(X, TW), para(UX, VW) => eq_angle
   * - ``given_u_v_s_t_complete_the_proof_that_r_u_v_r_t_s``
     - ``theorem``
     - leaneuclid
     - between(T, R, U), between(S, R, V), form_triangle(S, T, R, ST, TU, SV), form_triangle(U, V, R, UV, SV, TU), para(UV, ST)
   * - ``given_u_y_v_x_and_w_x_u_v_and_x_y_u_v_v_x_u_w_complete_the_proof_that_v_w_x_u_x_w``
     - ``theorem``
     - leaneuclid
     - cong(V, X, U, W), opposite_sides(Y, W, UX), para(UY, VX), para(WX, UV), para(XY, UV) => eq_angle(V, W, X, U, X, W)
   * - ``given_v_w_u_w_and_t_w_u_v_complete_the_proof_that_t_u_w_t_w_v``
     - ``theorem``
     - leaneuclid
     - between(U, T, V), form_triangle(T, V, W, UV, VW, TW), form_triangle(T, U, W, UV, UW, TW) => sim_tri(T, U, W, T, W, V)
   * - ``given_v_x_g_i_and_g_i_s_u_complete_the_proof_that_x_w_y_r_t_u_180``
     - ``theorem``
     - leaneuclid
     - between(G, H, I), between(R, H, T), between(S, T, U), between(H, T, W), between(V, W, X), between(T, W, Y), same_side(G,
   * - ``given_v_x_s_u_complete_the_proof_that_s_t_w_t_w_x``
     - ``theorem``
     - leaneuclid
     - between(S, T, U), between(T, W, Y), between(V, W, X), between(R, T, W), same_side(V, S, RY), same_side(X, U, RY), para(V
   * - ``given_v_x_s_u_complete_the_proof_that_t_w_x_s_t_w``
     - ``theorem``
     - leaneuclid
     - between(S, T, U), between(R, T, W), between(V, W, X), between(T, W, Y), same_side(U, X, RY), same_side(V, S, RY), para(V
   * - ``given_w_u_y_is_the_midpoint_of_u_w_complete_the_proof_that_v_w_y_x_u_y``
     - ``theorem``
     - leaneuclid
     - cong(W, Y, U, Y), eq_angle(V, W, Y, X, U, Y), between(U, Y, W), between(V, Y, X), form_triangle(U, X, Y, UX, VX, UW), fo
   * - ``given_w_x_v_y_and_y_v_z_y_complete_the_proof_that_x_w_z_w_x_z``
     - ``theorem``
     - leaneuclid
     - eq_angle(Y, V, Z, Z, Y, V), between(W, Z, Y), between(V, Z, X), para(WX, VY) => eq_angle(X, W, Z, W, X, Z)
   * - ``given_w_x_v_y_complete_the_proof_that_u_w_x_u_v_y``
     - ``theorem``
     - leaneuclid
     - between(V, U, W), between(X, U, Y), form_triangle(U, V, Y, VW, VY, XY), form_triangle(U, W, X, VW, WX, XY), para(WX, VY)
   * - ``given_w_x_y_z_w_x_y_z_complete_the_proof_that_w_y_z_y_w_x``
     - ``theorem``
     - leaneuclid
     - cong(W, X, Y, Z), opposite_sides(X, Z, WY), form_triangle(W, X, Y, WX, XY, WY), form_triangle(W, Y, Z, WY, YZ, WZ), para
   * - ``given_w_x_z_and_s_u_t_are_supplementary_complete_the_proof_that_w_y_t_v``
     - ``theorem``
     - leaneuclid
     - between(T, U, V), between(S, U, X), between(W, X, Y), between(U, X, Z), same_side(T, W, SZ), same_side(V, Y, SZ) => para
   * - ``given_w_y_complete_the_proof_that_w_x_z_y_v_z``
     - ``theorem``
     - leaneuclid
     - eq_angle(X, W, Z, V, Y, Z), between(V, Z, W), between(X, Z, Y), form_triangle(V, Y, Z, VY, XY, VW), form_triangle(W, X, 
   * - ``given_w_y_p_r_and_t_v_p_r_complete_the_proof_that_w_y_t_v``
     - ``theorem``
     - leaneuclid
     - between(P, Q, R), between(S, Q, U), between(T, U, V), between(Q, U, X), between(W, X, Y), between(U, X, Z), same_side(R,
   * - ``given_x_y_v_w_complete_the_proof_that_x_y_z_w_v_z``
     - ``theorem``
     - leaneuclid
     - between(W, X, Z), between(V, Y, Z), form_triangle(V, W, Z, VW, WZ, VZ), form_triangle(X, Y, Z, XY, VZ, WZ), para(XY, VW)
   * - ``given_x_y_w_z_and_y_w_x_y_complete_the_proof_that_v_w_z_v_z_w``
     - ``theorem``
     - leaneuclid
     - eq_angle(V, Y, X, W, X, Y), between(V, W, X), between(V, Z, Y), on_line(W, VX), on_line(Z, VY), para(XY, WZ) => eq_angle
   * - ``given_y_is_the_midpoint_of_u_w_and_u_x_v_w_y_is_the_midpoint_of_v_x_complete_the_proof_that_w_u``
     - ``theorem``
     - leaneuclid
     - cong(U, Y, W, Y), cong(U, X, V, W), cong(X, Y, V, Y), between(U, Y, W), between(V, Y, X), form_triangle(U, X, Y, UX, VX,
   * - ``given_y_v_z_v_y_z_and_w_x_v_y_complete_the_proof_that_w_x``
     - ``theorem``
     - leaneuclid
     - between(W, Z, X), between(W, Z, Y), para(WX, VY)
   * - ``given_y_x_and_u_x_v_y_u_x_v_y_complete_the_proof_that_v_w_y_u_v_x``
     - ``theorem``
     - leaneuclid
     - cong(U, X, V, Y), eq_angle(V, Y, W, U, X, V), between(U, V, W), same_side(X, Y, UW), form_triangle(U, V, X, UW, VX, UX),
   * - ``i_is_the_midpoint_of_e_g_and_e_h_f_g_complete_the_proof_that_h_i_f_i``
     - ``theorem``
     - leaneuclid
     - cong(E, I, G, I), between(E, I, G), between(F, I, H), form_triangle(E, H, I, EH, FH, EG), form_triangle(F, G, I, FG, EG,
   * - ``if_a_and_b_are_on_the_same_side_of_l_and_a_and_c_are_on_the_same_side_of_l_then_b_and_c_are_on_the_same_side_of_l``
     - ``axiom``
     - leaneuclid
     - same_side(a, b, L), same_side(a, c, L) => same_side(b, c, L)
   * - ``if_a_and_b_are_on_the_same_side_of_l_then_a_is_not_on_l``
     - ``axiom``
     - leaneuclid
     - same_side(a, b, L) => on_line(a, L)
   * - ``if_a_and_b_are_on_the_same_side_of_l_then_b_and_a_are_on_the_same_side_of_l``
     - ``axiom``
     - leaneuclid
     - same_side(a, b, L) => same_side(b, a, L)
   * - ``if_a_b_and_c_are_distinct_points_on_a_line_l_then_then_either_b_is_between_a_and_c_or_a_is_a_between_bnd_c_or_c_is_between_a_and_b``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(b, L), on_line(c, L) => between(a, b, c), between(b, a, c), between(a, c, b)
   * - ``if_a_b_and_c_are_not_on_l_and_a_and_b_are_not_on_the_same_side_of_l_then_either_a_and_c_are_on_the_same_side_of_l_or_b_and_c_are_on_the_same_side_of_l``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(b, L), on_line(c, L) => same_side(a, b, L), same_side(a, c, L), same_side(b, c, L)
   * - ``if_a_b_c_are_all_on_a_given_line_point_l_and_distinct_from_one_another_and_d_is_not_on_l_and_c_is_between_a_and_b_then_the_sum_of_the_areas_of_triangles_acd_and_dcb_is_equal_to_the_area_of_triangle_adb``
     - ``axiom``
     - leaneuclid
     - between(a, c, b), on_line(a, L), on_line(b, L), on_line(c, L), on_line(d, L)
   * - ``if_a_b_c_are_all_on_a_given_line_point_l_and_distinct_from_one_another_and_d_is_not_on_l_and_the_sum_of_the_areas_of_triangles_acd_and_dcb_is_equal_to_the_area_of_triangle_adb_then_c_is_between_a_and_b``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(b, L), on_line(c, L), on_line(d, L) => between(a, c, b)
   * - ``if_b_is_between_a_and_c_a_is_on_l_and_b_is_on_l_then_c_is_on_l``
     - ``axiom``
     - leaneuclid
     - between(a, b, c), on_line(a, L), on_line(b, L) => on_line(c, L)
   * - ``if_b_is_between_a_and_c_and_b_is_between_a_and_d_then_b_is_not_between_c_and_d``
     - ``axiom``
     - leaneuclid
     - between(a, b, c), between(a, b, d) => between(c, b, d)
   * - ``if_l_m_and_n_are_lines_meeting_at_a_point_a_and_b_c_and_d_are_points_on_l_m_and_n_respectively_and_if_c_and_d_are_on_the_same_side_of_l_and_b_and_c_are_on_the_same_side_of_n_and_d_and_e_are_on_the_same_side_of_m_and_c_and_e_are_on_the_same_side_of_n_then_c_and_e_are_on_the_same_side_of_l``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(a, M), on_line(a, N), on_line(b, L), on_line(c, M), on_line(d, N), same_side(c, d, L), same_side(
   * - ``if_l_m_and_n_are_lines_meeting_at_a_point_a_and_b_c_and_d_are_points_on_l_m_and_n_respectively_and_if_c_and_d_are_on_the_same_side_of_l_and_b_and_d_are_not_on_the_same_side_of_m_and_d_is_not_on_m_and_b_a_then_b_and_c_are_on_the_same_side_of_n``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(a, M), on_line(a, N), on_line(b, L), on_line(c, M), on_line(d, N), on_line(d, M), same_side(c, d,
   * - ``if_points_a_and_b_are_both_centers_of_circle_then_a_b_axiom_centre_unique_a_b_point_circle_a_iscentre_b_iscentre_a_b_3_if_a_is_the_centre_of_then_a_is_inside_axiom_center_inside_circle_a_point_circle_a_iscentre_a_insidecircle_4_if_a_point_is_inside_circle_then_a_is_not_on_axiom_inside_not_on_circle_a_point_circle_a_insidecircle_a_oncircle_between_axioms_1_if_b_is_between_a_and_c_then_b_is_between_c_and_a_a_b_a_c_and_a_is_not_a_between_bnd_c_axiom_between_symm_a_b_c_point_between_a_b_c_between_c_b_a_a_b_a_c_between_b_a_c_2_if_b_is_between_a_and_c_a_is_on_l_and_b_is_on_l_then_c_is_on_l_axiom_between_same_line_out_a_b_c_point_l_line_between_a_b_c_a_online_l_b_online_l_c_online_l_3_if_b_is_between_a_and_c_a_is_on_l_and_c_is_on_l_then_b_is_on_l_axiom_between_same_line_in_a_b_c_point_l_line_between_a_b_c_a_online_l_c_online_l_b_online_l_4_if_b_is_between_a_and_c_and_d_is_between_a_and_b_then_d_is_between_a_and_c_axiom_between_trans_in_a_b_c_d_point_between_a_b_c_between_a_d_b_between_a_d_c_5_if_b_is_between_a_and_c_and_c_is_a_between_bnd_d_then_b_is_between_a_and_d_axiom_between_trans_out_a_b_c_d_point_between_a_b_c_between_b_c_d_between_a_b_d_6_if_a_b_and_c_are_distinct_points_on_a_line_l_then_then_either_b_is_between_a_and_c_or_a_is_a_between_bnd_c_or_c_is_between_a_and_b_axiom_between_points_a_b_c_point_l_line_a_b_b_c_c_a_a_online_l_b_online_l_c_online_l_between_a_b_c_between_b_a_c_between_a_c_b_7_if_b_is_between_a_and_c_and_b_is_between_a_and_d_then_b_is_not_between_c_and_d_axiom_between_not_trans_a_b_c_d_point_between_a_b_c_between_a_b_d_between_c_b_d_same_side_axioms_1_if_a_is_not_on_l_then_a_and_a_are_on_the_same_side_of_l_axiom_same_side_rfl_a_point_l_line_a_online_l_a_sameside_a_l_2_if_a_and_b_are_on_the_same_side_of_l_then_b_and_a_are_on_the_same_side_of_l_axiom_same_side_symm_a_b_point_l_line_a_sameside_b_l_b_sameside_a_l_3_if_a_and_b_are_on_the_same_side_of_l_then_a_is_not_on_l_axiom_same_side_not_on_line_a_b_point_l_line_a_sameside_b_l_a_online_l_4_if_a_and_b_are_on_the_same_side_of_l_and_a_and_c_are_on_the_same_side_of_l_then_b_and_c_are_on_the_same_side_of_l_axiom_same_side_trans_a_b_c_point_l_line_a_sameside_b_l_a_sameside_c_l_b_sameside_c_l_5_if_a_b_and_c_are_not_on_l_and_a_and_b_are_not_on_the_same_side_of_l_then_either_a_and_c_are_on_the_same_side_of_l_or_b_and_c_are_on_the_same_side_of_l_axiom_same_side_pigeon_hole_a_b_c_point_l_line_a_online_l_b_online_l_c_online_l_a_sameside_b_l_a_sameside_c_l_b_sameside_c_l_1_if_b_is_between_a_and_c_and_a_and_c_are_on_the_same_side_of_l_then_a_and_b_are_on_the_same_side_of_l_axiom_pasch_1_a_b_c_point_l_line_between_a_b_c_a_sameside_c_l_a_sameside_b_l_2_if_b_is_between_a_and_c_and_a_is_on_l_and_b_is_not_on_l_then_b_and_c_are_on_the_same_side_of_l_axiom_pasch_2_a_b_c_point_l_line_between_a_b_c_a_online_l_b_online_l_b_sameside_c_l_3_if_b_is_between_a_and_c_and_b_is_on_l_then_a_and_c_are_not_on_the_same_side_of_l_see_also_avigad_s_notes_on_this_rule_https_www_andrew_cmu_edu_user_avigad_papers_euclid_notes_htm_axiom_pasch_3_a_b_c_point_l_line_between_a_b_c_b_online_l_a_sameside_c_l_4_if_b_is_the_intersection_of_distinct_lines_l_and_m_a_and_c_are_distinct_points_on_m_a_b_c_b_and_a_and_c_are_not_on_the_same_side_of_l_then_b_is_between_a_and_c_axiom_pasch_4_a_b_c_point_l_m_line_l_m_b_online_l_b_online_m_distinctpointsonline_a_c_m_a_b_c_b_a_sameside_c_l_between_a_b_c_triple_incidence_axioms_1_if_l_m_and_n_are_lines_meeting_at_a_point_a_and_b_c_and_d_are_points_on_l_m_and_n_respectively_and_if_c_and_d_are_on_the_same_side_of_l_and_b_and_c_are_on_the_same_side_of_n_then_b_and_d_are_not_on_the_same_side_of_m_axiom_triple_incidence_1_l_m_n_line_a_b_c_d_point_a_online_l_a_online_m_a_online_n_b_online_l_c_online_m_d_online_n_c_sameside_d_l_b_sameside_c_n_b_sameside_d_m_2_if_l_m_and_n_are_lines_meeting_at_a_point_a_and_b_c_and_d_are_points_on_l_m_and_n_respectively_and_if_c_and_d_are_on_the_same_side_of_l_and_b_and_d_are_not_on_the_same_side_of_m_and_d_is_not_on_m_and_b_a_then_b_and_c_are_on_the_same_side_of_n_axiom_triple_incidence_2_l_m_n_line_a_b_c_d_point_a_online_l_a_online_m_a_online_n_b_online_l_c_online_m_d_online_n_c_sameside_d_l_b_sameside_d_m_d_online_m_b_a_b_sameside_c_n_3_if_l_m_and_n_are_lines_meeting_at_a_point_a_and_b_c_and_d_are_points_on_l_m_and_n_respectively_and_if_c_and_d_are_on_the_same_side_of_l_and_b_and_c_are_on_the_same_side_of_n_and_d_and_e_are_on_the_same_side_of_m_and_c_and_e_are_on_the_same_side_of_n_then_c_and_e_are_on_the_same_side_of_l_axiom_triple_incidence_3_l_m_n_line_a_b_c_d_e_point_a_online_l_a_online_m_a_online_n_b_online_l_c_online_m_d_online_n_c_sameside_d_l_b_sameside_c_n_d_sameside_e_m_c_sameside_e_n_c_sameside_e_l_circle_axioms_1_if_a_b_and_c_are_on_l_a_is_inside_b_and_c_are_on_and_b_c_then_a_is_a_between_bnd_c_axiom_circle_line_intersections_a_b_c_point_l_line_circle_a_online_l_b_online_l_c_online_l_a_insidecircle_b_oncircle_c_oncircle_b_c_between_b_a_c_2_if_a_and_b_are_each_inside_or_on_and_c_is_between_a_and_b_then_c_is_inside_axiom_circle_points_between_a_b_c_point_circle_a_outsidecircle_b_outsidecircle_between_a_c_b_c_insidecircle_3_if_a_is_inside_or_on_c_is_not_inside_and_c_is_between_a_and_b_then_b_is_neither_inside_nor_on_axiom_circle_points_extend_a_b_c_point_circle_a_outsidecircle_c_insidecircle_between_a_c_b_b_outsidecircle_4_let_and_be_distinct_circles_that_intersect_in_distinct_points_c_and_d_let_a_be_a_the_centre_of_let_b_be_the_centre_of_and_let_l_be_the_line_through_a_and_b_then_c_and_d_are_not_on_the_same_side_of_l_axiom_circles_intersections_diff_side_a_b_c_d_point_circle_l_line_c_oncircle_c_oncircle_d_oncircle_d_oncircle_c_d_a_iscentre_b_iscentre_a_online_l_b_online_l_c_sameside_d_l_intersection_rules_1_if_a_and_b_are_on_different_sides_of_l_and_m_is_the_line_through_a_and_b_then_l_and_m_intersect_axiom_intersection_lines_opposing_a_b_point_l_m_line_a_opposingsides_b_l_a_online_m_b_online_m_l_intersectsline_m_not_in_avigad_et_al_2009_axiom_intersection_lines_common_point_a_point_l_m_line_a_online_l_a_online_m_l_m_l_intersectsline_m_not_in_avigad_et_al_2009_axiom_parallel_line_unique_a_point_l_m_n_line_a_online_l_a_online_m_a_online_n_l_intersectsline_m_l_intersectsline_n_m_n_not_in_avigad_et_al_2009_axiom_intersection_symm_l_m_line_l_intersectsline_m_m_intersectsline_l_2_if_a_is_on_or_inside_b_is_on_or_inside_and_a_and_b_are_on_different_sides_of_l_then_l_and_intersect_axiom_intersection_circle_line_1_a_b_point_circle_l_line_a_outsidecircle_b_outsidecircle_a_opposingsides_b_l_l_intersectscircle_3_if_a_is_inside_and_on_l_then_l_and_intersect_axiom_intersection_circle_line_2_a_point_circle_l_line_a_insidecircle_a_online_l_l_intersectscircle_4_if_a_is_on_or_inside_b_is_on_or_inside_a_is_inside_and_b_is_outside_then_and_intersect_axiom_intersection_circle_circle_1_a_b_point_circle_a_oncircle_b_outsidecircle_a_insidecircle_b_outsidecircle_intersectscircle_5_if_a_is_on_b_is_in_a_is_in_and_b_is_on_then_and_intersect_axiom_intersection_circle_circle_2_a_b_point_circle_a_oncircle_b_insidecircle_a_insidecircle_b_oncircle_intersectscircle_parallelogram_rules_not_in_avigad_et_al_2009``
     - ``axiom``
     - leaneuclid
     - same_side(b, d, AC), same_side(c, d, AB), same_side(a, b, CD)
   * - ``intersection_circle_line_between_points``
     - ``axiom``
     - leaneuclid
     - on_line(b, L), on_line(c, L) => between(b, a, c), on_line(a, L)
   * - ``intersection_circle_line_extending_points``
     - ``axiom``
     - leaneuclid
     - between(a, b, c), on_line(a, L)
   * - ``intersection_opposite_side``
     - ``axiom``
     - leaneuclid
     - on_line(c, L), on_line(d, L), on_line(b, L) => opposite_sides(a, b, L)
   * - ``intersection_rules_if_a_and_b_are_on_different_sides_of_l_and_m_is_the_line_through_a_and_b_then_l_and_m_intersect``
     - ``axiom``
     - leaneuclid
     - on_line(a, M), on_line(b, M), opposite_sides(a, b, L) => npara(L, M)
   * - ``intersection_same_side``
     - ``axiom``
     - leaneuclid
     - on_line(c, L), on_line(d, L), on_line(b, L) => same_side(a, b, L)
   * - ``not_in_avigad_et_al_2009_given_a_parallelogram_formed_from_points_a_b_c_and_d_and_given_points_e_and_f_such_that_e_is_betwen_a_and_b_and_f_is_between_c_and_d_then_the_sum_of_the_areas_of_the_triangles_acf_afe_efd_and_edb_is_equal_to_the_sum_of_the_areas_of_triangles_acd_and_adb``
     - ``axiom``
     - leaneuclid
     - between(a, e, b), between(c, f, d)
   * - ``opposite_sides``
     - ``definition``
     - leaneuclid
     - opposite_sides
   * - :ref:`pasch <pasch>`
     - ``axiom``
     - leaneuclid
     - between(a, b, c), same_side(a, c, L) => same_side(a, b, L)
   * - ``r27``
     - ``rule``
     - alphageometry, newclid
     - eq_ratio(O, A, A, C, O, B, B, D), coll(O, A, C), coll(O, B, D), ncoll(A, B, C), same_side(A, O, C, B, O, D) => para(A, B
   * - ``r41``
     - ``rule``
     - alphageometry, newclid
     - para(A, B, C, D), coll(M, A, D), coll(N, B, C), eq_ratio(M, A, M, D, N, B, N, C), same_side(M, A, D, N, B, C) => para(M,
   * - ``r_u_s_u_t_u_q_u_complete_the_proof_that_r_t_u_s_q_u``
     - ``theorem``
     - leaneuclid
     - cong(S, U, T, U), between(Q, T, U), between(S, R, U), form_triangle(Q, S, U, QS, SU, QU), form_triangle(R, T, U, RT, QU,
   * - ``resolution_of_ratios``
     - ``rule``
     - newclid
     - eq_ratio(A, B, A, C, D, E, D, F), coll(A, B, C), coll(D, E, F), same_side(A, B, C, D, E, F) => eq_ratio(A, B, B, C, D, E
   * - ``same_chord_same_arc_i``
     - ``rule``
     - newclid
     - cyclic(A, B, C, P, Q, R), cong(A, B, P, Q), nperp(A, C, B, C), same_clock(C, A, B, R, P, Q), same_side(C, A, B, R, P, Q)
   * - ``same_side``
     - ``relation``
     - leaneuclid
     - same_side
   * - ``same_side_axioms_if_a_is_not_on_l_then_a_and_a_are_on_the_same_side_of_l``
     - ``axiom``
     - leaneuclid
     - on_line(a, L) => same_side(a, a, L)
   * - ``suppose_a_and_b_are_on_l_b_and_c_are_on_m_and_c_and_d_are_on_n_suppose_also_that_b_c_a_and_d_are_on_the_same_side_of_m_and_abc_bcd_right_angle_right_angle_then_l_and_n_intersect_and_if_e_is_on_l_and_n_then_e_and_a_are_on_the_same_side_of_m_given_lines_a_b_c_and_d_such_that_a_and_b_are_both_on_a_given_line_l_b_and_c_are_both_on_a_given_line_m_c_and_d_are_both_on_a_given_line_n_b_is_distinct_from_c_a_and_d_are_on_the_same_side_of_m_and_the_sum_of_angles_abc_and_bcd_is_less_than_the_sum_of_two_right_angles_then_there_is_a_point_e_such_that_e_is_on_l_and_n_and_e_is_on_the_same_side_of_m_as_a``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(b, L), on_line(b, M), on_line(c, M), on_line(c, N), on_line(d, N), same_side(a, d, M) => on_line(
   * - ``suppose_a_and_b_are_points_on_l_c_is_between_a_and_b_and_d_is_not_on_l_then_acd_dcb_if_and_only_if_acd_is_equal_to_right_angle_given_points_a_and_b_both_lying_on_a_given_line_l_and_point_c_lying_between_a_and_b_and_point_d_not_on_l_such_that_the_angle_acd_is_equal_to_the_angle_dcb_then_the_angle_acd_is_a_right_angle``
     - ``axiom``
     - leaneuclid
     - eq_angle(a, c, d, d, c, b), between(a, c, b), on_line(a, L), on_line(b, L), on_line(d, L)
   * - ``transfer_inferences_defined_in_sec_3_6_of_avigad_et_al_2009_diagram_segment_transfer_axioms_if_b_is_between_a_and_c_then_ab_bc_ac_between_if_equal_circles_point_on_circle_if_point_on_circle_onlyif_sum_angles_if_sum_angles_onlyif_perpendicudlar_if_sum_areas_if_given_any_points_a_b_and_c_such_that_b_is_between_a_and_c_then_the_straight_line_from_a_to_c_is_equal_to_the_sum_of_the_straight_lines_from_a_to_b_and_from_b_to_c``
     - ``axiom``
     - leaneuclid
     - between(a, b, c) => cong(b, c, a, c)
   * - ``triangle_inequality``
     - ``theorem``
     - euclid, leaneuclid
     - form_triangle(a, b, c, AB, BC, AC)
   * - ``triple_incidence_axioms_if_l_m_and_n_are_lines_meeting_at_a_point_a_and_b_c_and_d_are_points_on_l_m_and_n_respectively_and_if_c_and_d_are_on_the_same_side_of_l_and_b_and_c_are_on_the_same_side_of_n_then_b_and_d_are_not_on_the_same_side_of_m``
     - ``axiom``
     - leaneuclid
     - on_line(a, L), on_line(a, M), on_line(a, N), on_line(b, L), on_line(c, M), on_line(d, N), same_side(c, d, L), same_side(
   * - ``u_is_the_midpoint_of_s_t_and_r_s_r_t_complete_the_proof_that_t_s``
     - ``theorem``
     - leaneuclid
     - cong(S, U, T, U), cong(R, S, R, T), between(S, U, T), form_triangle(R, S, U, RS, ST, RU), form_triangle(R, T, U, RT, ST,
   * - ``u_is_the_midpoint_of_s_t_and_r_u_s_t_complete_the_proof_that_t_r_u_s_r_u``
     - ``theorem``
     - leaneuclid
     - cong(S, U, T, U), between(S, U, T), on_line(U, ST), form_triangle(R, S, T, RS, ST, TR), npara(ST, RU) => eq_angle(T, R, 
   * - ``u_v_s_v_u_s_v_s_u_t_and_s_t_t_u_complete_the_proof_that_u_v_s_t``
     - ``theorem``
     - leaneuclid
     - eq_angle(U, S, V, S, U, T), opposite_sides(V, T, SU), form_triangle(S, T, U, ST, TU, SU), form_triangle(S, U, V, SU, UV,
   * - ``u_v_t_v_and_s_v_r_v_complete_the_proof_that_r_u_s_t``
     - ``theorem``
     - leaneuclid
     - cong(U, V, T, V), cong(S, V, R, V), between(R, V, T), between(S, V, U), form_triangle(R, U, V, RU, SU, RT), form_triangl
   * - ``u_v_u_w_u_x_u_y_complete_the_proof_that_u_v_x_u_w_y``
     - ``theorem``
     - leaneuclid
     - cong(U, W, U, X), between(V, U, Y), between(W, U, X), form_triangle(U, V, X, VY, VX, WX), form_triangle(U, W, Y, WX, WY,
   * - ``v_w_and_u_x_v_w_complete_the_proof_that_u_w_u_v``
     - ``theorem``
     - leaneuclid
     - eq_angle(U, V, W, U, W, V), between(V, X, W), on_line(X, VW), form_triangle(U, V, W, UV, VW, WU), npara(VW, UX) => cong(
   * - ``w_z_w_x_v_w_w_y_complete_the_proof_that_v_w_z_y_w_x``
     - ``theorem``
     - leaneuclid
     - cong(W, X, V, W), between(V, W, Y), between(X, W, Z), form_triangle(V, W, Z, VY, XZ, VZ), form_triangle(W, X, Y, XZ, XY,
