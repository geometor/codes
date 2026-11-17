Family: metric
==============

9 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``leaneuclid_angle_range``
     - ``axiom``
     - leaneuclid
     - 0 ≤ \abc and \abc ≤ right-angle + right-angle. @[simp]
   * - ``leaneuclid_angle_symm``
     - ``axiom``
     - leaneuclid
     - ∀ (a b c : Point), (a ≠ b) ∧ (b ≠ c) → ((∠ a:b:c) = (∠ c:b:a))
   * - ``leaneuclid_area_gte_zero``
     - ``axiom``
     - leaneuclid
     - △abc ≥ 0. @[simp]
   * - ``leaneuclid_area_symm_1``
     - ``axiom``
     - leaneuclid
     - △abc = △cab and △abc = △acb. @[simp]
   * - ``leaneuclid_area_symm_2``
     - ``axiom``
     - leaneuclid
     - @[simp]
   * - ``leaneuclid_degenerated_area``
     - ``axiom``
     - leaneuclid
     - △aab = 0. △ @[simp]
   * - ``leaneuclid_segment_gte_zero``
     - ``axiom``
     - leaneuclid
     - ab ≥ 0 @[simp]
   * - ``leaneuclid_zero_segment_if``
     - ``axiom``
     - leaneuclid
     - Metric inferences defined in Sec. 3.5 of Avigad et al., 2009 Generally speaking, they are not used explicitly in the tac
   * - ``leaneuclid_zero_segment_onlyif``
     - ``axiom``
     - leaneuclid
     - ∀ (a b : Point), a = b → \|(a─b)\| = 0
