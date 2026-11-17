Family: congruence
==================

95 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``2l1c``
     - ``construction``
     - alphageometry
     - cong(O, A, O, B), ncoll(A, B, C) => a(B, C, O, Y, Z, I), y(:, A, B, C, O, X, Z, I), z(:, A, B, C, O, X, Y, I), i(:, A, B
   * - ``3peq``
     - ``construction``
     - alphageometry
     - ncoll(A, B, C) => b(C, Z), x(:, A, B, C, Z, Y), y(:, A, B, C, Z, X), coll(Z, B, C), x(Y, :, coll, X, A, B), coll(Y, A, C
   * - ``ab_ba_simp``
     - ``axiom``
     - leaneuclid
     - cong(a, b, b, a)
   * - :ref:`angle_bisector <angle_bisector>`
     - ``construction``
     - alphageometry, euclid, leaneuclid, sympy
     - eq_angle(b, a, f, c, a, f)
   * - ``angle_mirror``
     - ``construction``
     - alphageometry
     - ncoll(A, B, C) => eq_angle(B, A, B, C, B, C, B, X)
   * - :ref:`asa_aas_congruence <asa_aas_congruence>`
     - ``theorem``
     - alphageometry, euclid, leaneuclid, newclid
     - cong(b, c, e, f), cong(a, b, d, e), eq_angle(a, b, c, d, e, f), eq_angle(b, c, a, e, f, d), form_triangle(a, b, c, AB, B
   * - ``asa_congruence_of_triangles_reverse``
     - ``rule``
     - newclid
     - eq_angle(B, A, B, C, Q, R, Q, P), eq_angle(C, A, C, B, R, Q, R, P), ncoll(A, B, C), cong(A, B, P, Q), same_clock(A, B, C
   * - ``cc_tangent``
     - ``construction``
     - alphageometry
     - diff(O, A), diff(W, B), diff(O, W) => o(A, W, B, Y), y(:, O, A, W, B, X), z(:, O, A, W, B, I), i(:, O, A, W, B, Z), cong
   * - ``cc_tangent0``
     - ``construction``
     - alphageometry
     - diff(O, A), diff(W, B), diff(O, W) => o(A, W, B, Y), y(:, O, A, W, B, X), cong(O, X, O, A), cong(W, Y, W, B), perp(X, O,
   * - ``congruent_if``
     - ``axiom``
     - leaneuclid
     - cong(A, B, D, E), cong(B, C, E, F), cong(A, C, D, F), eq_angle(A, B, C, D, E, F), eq_angle(A, C, B, D, F, E), eq_angle(B
   * - ``congruent_segments``
     - ``predicate``
     - geometor_model
     - congruent_segments
   * - ``congruent_triangles``
     - ``definition``
     - geometor_model, leaneuclid
     - cong(A, B, D, E), cong(B, C, E, F), cong(C, A, F, D), cong(A, B, D, E), cong(B, C, E, F), cong(B, C, E, F), cong(C, A, F
   * - ``copy_angle``
     - ``construction``
     - euclid, leaneuclid
     - eq_angle(f, a, b, d, c, e)
   * - ``cut_equal_segment``
     - ``construction``
     - euclid, leaneuclid
     - between(a, e, b)
   * - ``definition_of_midpoint``
     - ``rule``
     - newclid
     - cong(M, A, M, B), coll(M, A, B) => midp(M, A, B)
   * - ``e5128``
     - ``construction``
     - alphageometry
     - cong(C, B, C, D), perp(B, C, B, A) => a(B, C, D, Y), y(:, A, B, C, D, X), cong(C, B, C, X), coll(Y, A, B), coll(X, Y, D)
   * - ``eq_trapezoid``
     - ``construction``
     - alphageometry
     - b(:), c(:), d(:, para, D, C, A, B), cong(D, A, B, C)
   * - ``eqangle2``
     - ``construction``
     - alphageometry
     - ncoll(A, B, C) => eq_angle(A, B, A, X, C, X, C, B)
   * - ``eqangle3``
     - ``construction``
     - alphageometry
     - ncoll(D, E, F), diff(A, B), diff(D, E), diff(E, F) => eq_angle(X, A, X, B, D, E, D, F)
   * - ``eqdistance``
     - ``construction``
     - alphageometry
     - diff(B, C) => cong(X, A, B, C)
   * - ``equal_angles``
     - ``axiom``
     - geometor_model, leaneuclid
     - between(b, a, b'), between(c, a, c'), on_line(a, L), on_line(b, L), on_line(b', L), on_line(a, M), on_line(c, M), on_lin
   * - :ref:`equilateral_apex <equilateral_apex>`
     - ``construction``
     - alphageometry, euclid, leaneuclid
     - cong(c, a, a, b), cong(c, b, a, b)
   * - ``excenter``
     - ``construction``
     - alphageometry
     - ncoll(A, B, C) => eq_angle(A, B, A, X, A, X, A, C), eq_angle(C, A, C, X, C, X, C, B), eq_angle(B, C, B, X, B, X, B, A)
   * - ``excenter2``
     - ``construction``
     - alphageometry
     - ncoll(A, B, C) => a(B, C), x(:, I, B, C), y(:, I, C, A), z(:, I, A, B), eq_angle(A, B, A, I, A, I, A, C), eq_angle(C, A,
   * - ``f_i_g_h_and_h_i_f_g_complete_the_proof_that_f_h_i_g_f_h``
     - ``theorem``
     - leaneuclid
     - cong(F, I, G, H), cong(H, I, F, G) => eq_angle(F, H, I, G, F, H)
   * - ``generalized_pythagorean_theorem_i``
     - ``rule``
     - newclid
     - perp(A, B, C, D) => lequation(1/1, A, C, *, A, C, 1/1, B, D, *, B, D, -1/1, A, D, *, A, D, -1/1, B, C, *, B, C, 0)
   * - ``generalized_pythagorean_theorem_ii``
     - ``rule``
     - newclid
     - lequation(1/1, A, C, *, A, C, 1/1, B, D, *, B, D, -1/1, A, D, *, A, D, -1/1, B, C, *, B, C, 0), ncoll(A, B, C) => perp(A
   * - ``given_g_i_bisects_h_g_j_and_h_j_complete_the_proof_that_g_j_g_h``
     - ``theorem``
     - leaneuclid
     - eq_angle(I, G, H, I, G, J), eq_angle(G, H, I, G, J, I) => cong(G, J, G, H)
   * - ``given_h_g_h_k_g_j_f_h_g_i_complete_the_proof_that_h_f_k_g_i_j``
     - ``theorem``
     - leaneuclid
     - cong(G, J, F, H), eq_angle(F, H, K, I, G, J), form_triangle(F, H, K, FH, HK, KF), form_triangle(G, I, J, GI, IJ, JG) => 
   * - ``given_i_f_and_k_g_complete_the_proof_that_i_k_f_g_j_k_g_h``
     - ``theorem``
     - leaneuclid
     - eq_angle(J, I, K, H, F, G), eq_angle(I, K, J, F, G, H), form_triangle(I, J, K, IJ, JK, KI), form_triangle(F, G, H, FG, G
   * - ``given_i_k_and_h_f_complete_the_proof_that_g_i_j_k_g_h_f_j``
     - ``theorem``
     - leaneuclid
     - eq_angle(G, I, H, J, K, F), eq_angle(G, H, I, J, F, K), form_triangle(I, G, H, IG, GH, HI), form_triangle(F, J, K, FJ, J
   * - ``given_p_r_bisects_q_p_s_and_p_r_bisects_q_r_s_complete_the_proof_that_r_s_q_r``
     - ``theorem``
     - leaneuclid
     - eq_angle(Q, P, R, S, P, R), eq_angle(P, R, Q, P, R, S) => cong(R, S, Q, R)
   * - ``given_r_t_r_v_q_t_r_u_s_t_complete_the_proof_that_r_u_v_q_s_t``
     - ``theorem``
     - leaneuclid
     - cong(Q, T, R, U), eq_angle(U, R, V, S, T, Q), form_triangle(Q, S, T, QS, ST, TQ), form_triangle(R, U, V, RU, UV, VR) => 
   * - ``given_r_u_and_t_q_complete_the_proof_that_r_t_q_u_p_t_q_s``
     - ``theorem``
     - leaneuclid
     - eq_angle(P, R, T, S, U, Q), eq_angle(P, T, R, S, Q, U), form_triangle(P, R, T, PR, RT, TP), form_triangle(S, U, Q, SU, U
   * - ``given_t_v_t_y_u_v_t_w_v_x_complete_the_proof_that_t_w_y_u_x_v``
     - ``theorem``
     - leaneuclid
     - cong(U, V, T, W), eq_angle(W, T, Y, U, V, X), form_triangle(T, W, Y, TW, WY, YT), form_triangle(U, V, X, UV, VX, XU) => 
   * - ``given_u_y_and_w_v_complete_the_proof_that_u_w_v_y_w_z_v_x``
     - ``theorem``
     - leaneuclid
     - eq_angle(W, U, Z, V, Y, X), eq_angle(U, W, Z, Y, V, X), form_triangle(U, W, Z, UW, WZ, ZU), form_triangle(V, X, Y, VX, X
   * - ``given_v_r_and_s_w_complete_the_proof_that_s_v_r_w_t_v_r_u``
     - ``theorem``
     - leaneuclid
     - eq_angle(S, V, T, W, R, U), eq_angle(V, S, T, R, W, U), form_triangle(S, T, V, ST, TV, VS), form_triangle(R, U, W, RU, U
   * - ``given_v_s_and_w_u_complete_the_proof_that_w_x_t_u_v_x_s_t``
     - ``theorem``
     - leaneuclid
     - eq_angle(W, V, X, U, S, T), eq_angle(V, W, X, S, U, T), form_triangle(V, W, X, VW, WX, XV), form_triangle(S, U, T, SU, U
   * - ``given_v_t_and_w_y_complete_the_proof_that_w_x_u_y_v_w_t_y``
     - ``theorem``
     - leaneuclid
     - eq_angle(X, V, W, U, T, Y), eq_angle(V, W, X, T, Y, U), form_triangle(V, W, X, VW, WX, XV), form_triangle(T, U, Y, TU, U
   * - ``given_x_v_w_x_s_v_u_x_t_v_complete_the_proof_that_u_w_x_t_s_v``
     - ``theorem``
     - leaneuclid
     - cong(S, V, U, X), eq_angle(U, X, W, T, V, S), form_triangle(U, W, X, UW, WX, XU), form_triangle(S, T, V, ST, TV, VS) => 
   * - ``given_y_u_and_t_w_complete_the_proof_that_v_y_u_x_t_v_w_x``
     - ``theorem``
     - leaneuclid
     - eq_angle(T, Y, V, W, U, X), eq_angle(Y, T, V, U, W, X), form_triangle(U, W, X, UW, WX, XU), form_triangle(T, V, Y, TV, V
   * - ``given_z_u_v_z_u_x_w_z_u_y_complete_the_proof_that_v_w_z_u_y_x``
     - ``theorem``
     - leaneuclid
     - cong(U, X, W, Z), eq_angle(V, Z, W, X, U, Y), form_triangle(U, X, Y, UX, XY, YU), form_triangle(V, W, Z, VW, WZ, ZV) => 
   * - ``ieq_triangle``
     - ``construction``
     - alphageometry
     - b(:), c(:, cong, A, B, B, C), cong(B, C, C, A), eq_angle(A, B, A, C, C, A, C, B), eq_angle(C, A, C, B, B, C, B, A)
   * - ``if_a_is_the_centre_of_and_b_is_on_c_is_on_and_ab_ac_then_if_a_point_x_is_the_centre_of_two_circles_c_and_d_and_given_points_b_and_d_such_that_b_is_on_c_and_c_is_on_d_and_the_straight_line_from_x_to_b_is_equal_to_the_straight_line_from_x_to_c_then_c_is_equal_to_d``
     - ``axiom``
     - leaneuclid
     - cong(a, b, a, c)
   * - ``if_a_point_x_is_the_centre_of_circle_c_and_a_point_b_is_on_c_then_given_some_point_c_on_c_the_straight_line_from_x_to_c_is_equal_to_the_straight_line_from_x_to_b``
     - ``axiom``
     - leaneuclid
     - cong(a, c, a, b)
   * - ``if_ab_a_b_bc_b_c_ca_c_a_abc_a_b_c_bca_b_c_a_and_cab_c_a_b_then_abc_a_b_c``
     - ``axiom``
     - leaneuclid
     - cong(a, b, a', b'), cong(b, c, b', c'), cong(c, a, c', a'), eq_angle(a, b, c, a', b', c'), eq_angle(b, c, a, b', c', a')
   * - ``intersection_cc``
     - ``construction``
     - alphageometry
     - ncoll(O, W, A) => cong(O, A, O, X), cong(W, A, W, X)
   * - ``intersection_lc``
     - ``construction``
     - alphageometry
     - diff(A, B), diff(O, B), nperp(B, O, B, A) => coll(X, A, B), cong(O, B, O, X)
   * - ``intersection_lt``
     - ``construction``
     - alphageometry
     - ncoll(A, B, C), nperp(A, B, D, E) => coll(X, A, B), perp(X, C, D, E)
   * - ``is_equilateral``
     - ``predicate``
     - sympy
     - is_equilateral
   * - ``is_isosceles``
     - ``predicate``
     - sympy
     - is_isosceles
   * - ``is_right``
     - ``predicate``
     - geometor_model, sympy
     - is_right
   * - ``is_scalene``
     - ``predicate``
     - sympy
     - is_scalene
   * - ``iso_triangle``
     - ``construction``
     - alphageometry
     - b(:), c(:, eqangle, B, A, B, C, C, B, C, A), cong(A, B, A, C)
   * - :ref:`isosceles_base_angles <isosceles_base_angles>`
     - ``theorem``
     - alphageometry, euclid, leaneuclid, newclid
     - cong(a, b, a, c), between(a, b, d), between(a, c, e), form_triangle(a, b, c, AB, BC, AC) => eq_angle(a, b, c, a, c, b), 
   * - ``isosceles_converse``
     - ``theorem``
     - alphageometry, euclid, leaneuclid, newclid
     - eq_angle(a, b, c, a, c, b), form_triangle(a, b, c, AB, BC, AC) => cong(a, b, a, c)
   * - ``j_k_h_i_and_h_k_i_j_complete_the_proof_that_k_i``
     - ``theorem``
     - leaneuclid
     - cong(J, K, H, I), cong(H, K, I, J) => eq_angle(H, K, J, H, I, J)
   * - ``lc_tangent``
     - ``construction``
     - alphageometry
     - diff(A, O) => perp(A, X, A, O)
   * - ``locate_midpoint_of_hypotenuse``
     - ``rule``
     - newclid
     - cong(A, M, B, M), coll(B, M, C), perp(A, B, A, C) => midp(M, B, C)
   * - ``mirror``
     - ``construction``
     - alphageometry
     - diff(A, B) => coll(X, A, B), cong(B, A, B, X)
   * - ``ninepoints``
     - ``construction``
     - alphageometry
     - ncoll(A, B, C) => b(C), y(:, C, A), z(:, A, B), i(:, X, Y, Z), coll(X, B, C), cong(X, B, X, C), y(:, coll, Y, C, A), con
   * - ``nsquare``
     - ``construction``
     - alphageometry
     - diff(A, B) => cong(X, A, A, B), perp(X, A, A, B)
   * - ``on_aline``
     - ``construction``
     - alphageometry
     - ncoll(C, D, E) => eq_angle(A, X, A, B, D, C, D, E)
   * - ``on_dia``
     - ``construction``
     - alphageometry
     - diff(A, B) => perp(X, A, X, B)
   * - ``perpendicular``
     - ``predicate``
     - geometor_model
     - perpendicular
   * - ``perpendicular_bisector``
     - ``construction``
     - alphageometry, sympy
     - diff(A, B) => cong(X, A, X, B), eq_angle(A, X, A, B, B, A, B, X)
   * - :ref:`perpendicular_foot <perpendicular_foot>`
     - ``construction``
     - alphageometry, euclid, leaneuclid
     - on_line(c, AB) => on_line(h, AB)
   * - ``perpendicular_line``
     - ``construction``
     - alphageometry, euclid, leaneuclid, sympy
     - between(a, c, b) => on_line(f, AB)
   * - ``properties_of_midpoint_cong``
     - ``rule``
     - newclid
     - midp(M, A, B) => cong(M, A, M, B)
   * - ``q_r_r_s_q_t_s_t_and_q_s_r_s_q_t_complete_the_proof_that_s_t_q_r``
     - ``theorem``
     - leaneuclid
     - eq_angle(Q, S, R, S, Q, T) => cong(S, T, Q, R)
   * - ``r22``
     - ``rule``
     - alphageometry, newclid
     - midp(M, A, B), perp(O, M, A, B) => cong(O, A, O, B)
   * - ``r23``
     - ``rule``
     - alphageometry, newclid
     - cong(A, P, B, P), cong(A, Q, B, Q) => perp(A, B, P, Q)
   * - ``r30``
     - ``rule``
     - alphageometry, newclid
     - eq_angle(A, B, P, Q, C, D, U, V), perp(P, Q, U, V) => perp(A, B, C, D)
   * - ``r32``
     - ``rule``
     - alphageometry
     - cong(A, B, P, Q), cong(B, C, Q, R), cong(C, A, R, P), ncoll(A, B, C) => contri*(A, B, C, P, Q, R)
   * - ``r37``
     - ``rule``
     - alphageometry
     - eq_angle(B, A, B, C, Q, R, Q, P), eq_angle(C, A, C, B, R, Q, R, P), ncoll(A, B, C), cong(A, B, P, Q) => con_tri(A, B, C,
   * - ``r_trapezoid``
     - ``construction``
     - alphageometry
     - b(:), c(:), d(:, para, A, B, C, D), perp(A, B, A, D)
   * - ``reflect``
     - ``construction``
     - alphageometry
     - diff(B, C), ncoll(A, B, C) => cong(B, A, B, X), cong(C, A, C, X), perp(B, C, A, X)
   * - ``right_angles_equal``
     - ``postulate``
     - euclid
     - That all right angles are equal to one another.
   * - ``risos``
     - ``construction``
     - alphageometry
     - b(:), c(:, perp, A, B, A, C), cong(A, B, A, C), eq_angle(B, A, B, C, C, B, C, A)
   * - ``s_q_t_q_s_r_s_t_q_t_and_q_r_r_s_complete_the_proof_that_r_s_q_t``
     - ``theorem``
     - leaneuclid
     - eq_angle(S, Q, T, Q, S, R) => cong(R, S, Q, T)
   * - :ref:`sas_congruence <sas_congruence>`
     - ``theorem``
     - euclid, leaneuclid, newclid
     - cong(a, b, d, e), cong(a, c, d, f), eq_angle(b, a, c, e, d, f), form_triangle(a, b, c, AB, BC, AC), form_triangle(d, e, 
   * - ``sas_congruence_of_triangles_reverse``
     - ``rule``
     - newclid
     - cong(A, B, P, Q), cong(B, C, Q, R), eq_angle(B, A, B, C, Q, R, Q, P), ncoll(A, B, C), same_clock(A, B, C, P, R, Q), diff
   * - ``shift``
     - ``construction``
     - alphageometry
     - diff(D, B) => cong(X, B, C, D), cong(X, C, B, D)
   * - ``similar_if``
     - ``axiom``
     - leaneuclid
     - cong(D, E, B, C), cong(D, E, B, C), cong(F, D, A, B), eq_angle(A, B, C, D, E, F), eq_angle(A, C, B, D, F, E), eq_angle(B
   * - :ref:`sss_congruence <sss_congruence>`
     - ``theorem``
     - alphageometry, euclid, leaneuclid, newclid
     - cong(a, b, d, e), cong(a, c, d, f), cong(b, c, e, f), form_triangle(a, b, c, AB, BC, AC), form_triangle(d, e, f, DE, EF,
   * - ``sss_congruence_of_triangles_reverse``
     - ``rule``
     - newclid
     - cong(A, B, P, Q), cong(B, C, Q, R), cong(C, A, R, P), ncoll(A, B, C), same_clock(A, B, C, P, R, Q), diff(A, B, C), diff(
   * - ``superposition``
     - ``axiom``
     - leaneuclid
     - on_line(h, L), form_triangle(a, b, c, AB, BC, AC) => cong(a, b, d, b'), cong(b, c, b', c'), cong(c, a, c', d), between(b
   * - ``supplementary_adjacent_angles``
     - ``theorem``
     - euclid, leaneuclid
     - between(d, b, c)
   * - ``t_v_u_v_t_w_t_u_u_v_and_v_w_t_w_complete_the_proof_that_t_u_v_w``
     - ``theorem``
     - leaneuclid
     - eq_angle(T, V, U, V, T, W) => cong(T, U, V, W)
   * - ``transfer_segment``
     - ``construction``
     - euclid, leaneuclid
     - cong(a, l, b, c)
   * - ``trisect``
     - ``construction``
     - alphageometry
     - ncoll(A, B, C) => a(B, C, Y), y(:, A, B, C, X), coll(X, A, C), coll(Y, A, C), eq_angle(B, A, B, X, B, X, B, Y), eq_angle
   * - ``trisegment``
     - ``construction``
     - alphageometry
     - diff(A, B) => a(B, Y), y(:, A, B, X), coll(X, A, B), coll(Y, A, B), cong(X, A, X, Y), cong(Y, X, Y, B)
   * - ``u_v_t_u_and_s_t_s_v_complete_the_proof_that_v_t``
     - ``theorem``
     - leaneuclid
     - cong(U, V, T, U), cong(S, T, S, V) => eq_angle(S, V, U, S, T, U)
   * - ``vertical_angles``
     - ``theorem``
     - euclid, leaneuclid
     - between(d, e, c), between(a, e, b), on_line(e, AB), on_line(e, CD) => eq_angle(a, e, c, d, e, b), eq_angle(c, e, b, a, e
   * - ``x_y_w_z_and_y_z_w_x_complete_the_proof_that_y_w_z_w_y_x``
     - ``theorem``
     - leaneuclid
     - cong(X, Y, W, Z), cong(Y, Z, W, X) => eq_angle(Y, W, Z, W, Y, X)
