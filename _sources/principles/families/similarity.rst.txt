Family: similarity
==================

26 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - :ref:`aa_similarity <aa_similarity>`
     - ``theorem``
     - alphageometry, euclid, newclid
     - eq_angle(B, A, B, C, Q, P, Q, R), eq_angle(C, A, C, B, R, P, R, Q), ncoll(A, B, C) => sim_tri(A, B, C, P, Q, R)
   * - ``aa_similarity_of_triangles_reverse``
     - ``rule``
     - newclid
     - eq_angle(B, A, B, C, Q, R, Q, P), eq_angle(C, A, C, B, R, Q, R, P), ncoll(A, B, C), same_clock(A, B, C, P, R, Q), diff(A
   * - ``angle_bisector_ratio``
     - ``theorem``
     - alphageometry, euclid, newclid
     - eq_angle(A, B, A, D, A, D, A, C), coll(D, B, C), ncoll(A, B, C) => eq_ratio(D, B, D, C, A, B, A, C)
   * - ``angle_bisector_ratio_converse``
     - ``theorem``
     - alphageometry, newclid
     - eq_ratio(D, B, D, C, A, B, A, C), coll(D, B, C), ncoll(A, B, C) => eq_angle(A, B, A, D, A, D, A, C)
   * - ``divide_congruence_equation_by_segment``
     - ``rule``
     - newclid
     - cong(A, B, C, D), diff(X, Y), diff(A, B), diff(C, D) => eq_ratio(A, B, X, Y, C, D, X, Y)
   * - ``is_golden``
     - ``predicate``
     - geometor_model
     - is_golden
   * - ``mean_proportional``
     - ``construction``
     - euclid
     - To two given straight lines to find a mean proportional.
   * - ``properties_of_congruent_triangles_direct``
     - ``rule``
     - newclid
     - con_tri(A, B, C, P, Q, R) => sim_tri(A, B, C, P, Q, R), cong(A, B, P, Q)
   * - ``properties_of_similar_triangles_direct``
     - ``rule``
     - newclid
     - sim_tri(A, B, C, P, Q, R), diff(A, B, C), diff(P, Q, R) => eq_angle(B, A, B, C, Q, P, Q, R), eq_angle(A, B, A, C, P, Q, 
   * - ``properties_of_similar_triangles_reverse``
     - ``rule``
     - newclid
     - sim_tri(A, B, C, P, Q, R), diff(A, B, C), diff(P, Q, R) => eq_angle(B, A, B, C, Q, R, Q, P), eq_angle(A, B, A, C, P, R, 
   * - ``r10``
     - ``rule``
     - alphageometry, newclid
     - eq_ratio(A, B, C, D, M, N, P, Q), eq_ratio(C, D, E, F, P, Q, R, U) => eq_ratio(A, B, E, F, M, N, R, U)
   * - ``r29``
     - ``rule``
     - alphageometry, newclid
     - midp(M, A, B), midp(N, C, D) => eq_ratio(M, A, A, B, N, C, C, D)
   * - ``r31``
     - ``rule``
     - alphageometry, newclid
     - eq_ratio(A, B, P, Q, C, D, U, V), cong(P, Q, U, V) => cong(A, B, C, D)
   * - ``r35``
     - ``rule``
     - alphageometry
     - eq_angle(B, A, B, C, Q, R, Q, P), eq_angle(C, A, C, B, R, Q, R, P), ncoll(A, B, C) => sim_tri(A, B, C, P, Q, R)
   * - ``r38``
     - ``rule``
     - alphageometry
     - eq_ratio(B, A, B, C, Q, P, Q, R), eq_ratio(C, A, C, B, R, P, R, Q), ncoll(A, B, C) => simtri*(A, B, C, P, Q, R)
   * - ``r39``
     - ``rule``
     - alphageometry
     - eq_ratio(B, A, B, C, Q, P, Q, R), eq_angle(B, A, B, C, Q, P, Q, R), ncoll(A, B, C) => simtri*(A, B, C, P, Q, R)
   * - ``r40``
     - ``rule``
     - alphageometry
     - eq_ratio(B, A, B, C, Q, P, Q, R), eq_ratio(C, A, C, B, R, P, R, Q), ncoll(A, B, C), cong(A, B, P, Q) => contri*(A, B, C,
   * - ``sas_similarity``
     - ``theorem``
     - euclid, newclid
     - eq_ratio(B, A, B, C, Q, P, Q, R), eq_angle(B, A, B, C, Q, P, Q, R), ncoll(A, B, C), same_clock(A, B, C, P, Q, R), diff(A
   * - ``sas_similarity_of_triangles_reverse``
     - ``rule``
     - newclid
     - eq_ratio(B, A, B, C, Q, P, Q, R), eq_angle(B, A, B, C, Q, R, Q, P), ncoll(A, B, C), same_clock(A, B, C, P, R, Q), diff(A
   * - ``similar_triangles``
     - ``definition``
     - leaneuclid, sympy
     - similar_triangles
   * - ``similarity_without_scaling_direct``
     - ``rule``
     - newclid
     - eq_ratio(B, A, B, C, Q, P, Q, R), eq_ratio(C, A, C, B, R, P, R, Q), ncoll(A, B, C), cong(A, B, P, Q), same_clock(A, B, C
   * - ``similarity_without_scaling_reverse``
     - ``rule``
     - newclid
     - eq_ratio(B, A, B, C, Q, P, Q, R), eq_ratio(C, A, C, B, R, P, R, Q), ncoll(A, B, C), cong(A, B, P, Q), same_clock(A, B, C
   * - ``sss_similarity``
     - ``theorem``
     - euclid, newclid
     - eq_ratio(B, A, B, C, Q, P, Q, R), eq_ratio(C, A, C, B, R, P, R, Q), ncoll(A, B, C), same_clock(A, B, C, P, Q, R), diff(A
   * - ``sss_similarity_of_triangles_reverse``
     - ``rule``
     - newclid
     - eq_ratio(B, A, B, C, Q, P, Q, R), eq_ratio(C, A, C, B, R, P, R, Q), ncoll(A, B, C), same_clock(A, B, C, P, R, Q), diff(A
   * - :ref:`thales_intercept <thales_intercept>`
     - ``theorem``
     - alphageometry, euclid, newclid
     - para(A, B, C, D), coll(O, A, C), coll(O, B, D) => eq_ratio(A, B, C, D, O, O)
   * - ``third_proportional``
     - ``construction``
     - euclid
     - To two given straight lines to find a third proportional.
