Family: unigeo_relations
========================

3 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``leaneuclid_formquadrilateral``
     - ``definition``
     - leaneuclid
     - (a b c d : Point) (AB CD AC BD : Line) : Prop
   * - ``leaneuclid_quadrilateralanglessum``
     - ``axiom``
     - leaneuclid
     - (a b c d : Point) (AB CD AC BD : Line) : formQuadrilateral a b c d AB CD AC BD → ∠ a:b:d + ∠ b:d:c + ∠ d:c:a + ∠ c:a:b =
   * - ``leaneuclid_twolinesintersectatpoint``
     - ``definition``
     - leaneuclid
     - (AB BC : Line) (b: Point) : Prop
