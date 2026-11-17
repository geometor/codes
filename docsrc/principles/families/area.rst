Family: area
============

5 principles in this family.

.. list-table::
   :header-rows: 1
   :widths: 28 14 28 30

   * - Principle
     - Kind
     - Base Systems
     - Statement / Form
   * - ``area``
     - ``measure``
     - geometor_model, leaneuclid, sympy
     - area
   * - ``equal_area``
     - ``predicate``
     - geometor_model
     - equal_area
   * - :ref:`pythagorean <pythagorean>`
     - ``theorem``
     - euclid, leaneuclid, newclid
     - form_triangle(a, b, c, AB, BC, AC) => cong(b, c, b, a)
   * - ``pythagorean_converse``
     - ``theorem``
     - euclid, leaneuclid
     - cong(b, c, b, a), form_triangle(a, b, c, AB, BC, AC)
   * - ``square_on_segment``
     - ``construction``
     - euclid, leaneuclid
     - cong(d, e, a, b), cong(a, d, a, b), cong(b, e, a, b)
