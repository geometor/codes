Family: points
==============

10 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``geometor_model_pointsmixin_given_point``
     - ``construction``
     - geometor_model
     - Register an initial given point in the model with ``"given"`` classification.
   * - ``geometor_model_pointsmixin_set_point``
     - ``construction``
     - geometor_model
     - Add a point to the model, find duplicates, clean values, and set parents and classes.
   * - ``leaneuclid_arbitrary_point``
     - ``axiom``
     - leaneuclid
     - ∃ _ : Point, true
   * - ``leaneuclid_distinct_points``
     - ``axiom``
     - leaneuclid
     - ∀ p₁ : Point, ∃ p₂ : Point, p₁ ≠ p₂
   * - ``leaneuclid_exists_distinct_point_inside_circle``
     - ``axiom``
     - leaneuclid
     - ∀ (α : Circle) (b : Point), ∃ a : Point, a ≠ b ∧ a.insideCircle α
   * - ``leaneuclid_exists_distinct_point_on_circle``
     - ``axiom``
     - leaneuclid
     - ∀ (α : Circle) (b : Point), ∃ a : Point, a ≠ b ∧ (a.onCircle α)
   * - ``leaneuclid_exists_distinct_point_outside_circle``
     - ``axiom``
     - leaneuclid
     - ∀ (α : Circle) (b : Point), ∃ a : Point, a ≠ b ∧ a.outsideCircle α
   * - ``leaneuclid_exists_point_inside_circle``
     - ``axiom``
     - leaneuclid
     - ∀ (α : Circle), ∃ a : Point, a.insideCircle α
   * - ``leaneuclid_exists_point_on_circle``
     - ``axiom``
     - leaneuclid
     - ∀ (α : Circle), ∃ a : Point, a.onCircle α
   * - ``leaneuclid_exists_point_outside_circle``
     - ``axiom``
     - leaneuclid
     - ∀ (α : Circle), ∃ a : Point, a.outsideCircle α
