.. _equilateral_apex:

equilateral_apex
================

**equilateral apex** · kind: ``construction`` · family: ``congruence`` · verification: ``verified``

**Euclid:** ``I.1``

.. admonition:: Statement
   :class: note

   On a given finite straight line to construct an equilateral triangle.

Canonical Form
--------------

.. code-block:: text

   cong(c, a, a, b), cong(c, b, a, b)

Exact Witness Figure
--------------------

.. figure:: equilateral_apex.svg
   :alt: equilateral_apex
   :align: center

   Exact witness verified (3 points, 0 lines, 2 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - ``euclid``
     - ``I.1``
     - I.1
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_1``
     - ∀ (a b : Point) (AB : Line), distinctPointsOnLine a b AB → ∃ c : Point, \|(c─a)\| = \|(a─b)\| ∧ \|(c─b)\| = \|(a─b)\|
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_1'``
     - ∀ (a b x : Point) (AB : Line), distinctPointsOnLine a b AB ∧ ¬(x.onLine AB) → ∃ c : Point, \|(c─a)\| = \|(a─b)\| ∧ \|(c─b)\| = \|(a─b)\| ∧ (c.opposingSides x AB)
   * - ``alphageometry``
     - ``def.eq_triangle``
     - eq_triangle x b c

Proof Traces
------------

.. collapse:: LeanEuclid ``Elements.Book1.proposition_1`` (8 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply circle_from_points a b as BCD
      euclid_apply circle_from_points b a as ACE
      euclid_apply intersection_circles BCD ACE as c
      euclid_apply point_on_circle_onlyif a b c BCD
      euclid_apply point_on_circle_onlyif b a c ACE
      use c
      euclid_finish

.. collapse:: LeanEuclid ``Elements.Book1.proposition_1'`` (8 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply circle_from_points a b as BCD
      euclid_apply circle_from_points b a as ACE
      euclid_apply intersection_opposite_side BCD ACE x a b AB as c
      euclid_apply point_on_circle_onlyif a b c BCD
      euclid_apply point_on_circle_onlyif b a c ACE
      use c
      euclid_finish

Linked Library Entries
----------------------

.. list-table::
   :header-rows: 1
   :widths: 14 28 12 46

   * - Library
     - Declaration
     - Confidence
     - Source
   * - ``geocoq``
     - ``equilateral``
     - 0.35 (tokens:1)
     - `equilateral <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Elements/OriginalProofs/euclidean_defs.v#L35>`_
   * - ``geocoq``
     - ``conga3_equilateral``
     - 0.35 (tokens:1)
     - `conga3_equilateral <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Main/Highschool/triangles.v#L327>`_
   * - ``geocoq``
     - ``equilateral``
     - 0.35 (tokens:1)
     - `equilateral <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Main/Highschool/triangles.v#L101>`_
   * - ``mathlib4``
     - ``abs_oangle_center_left_toReal_lt_pi_div_two``
     - 0.35 (tokens:1)
     - `abs_oangle_center_left_toReal_lt_pi_div_two <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Sphere.lean#L325>`_
   * - ``mathlib4``
     - ``abs_oangle_center_right_toReal_lt_pi_div_two``
     - 0.35 (tokens:1)
     - `abs_oangle_center_right_toReal_lt_pi_div_two <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Sphere.lean#L331>`_
   * - ``mathlib4``
     - ``oangle_eq_pi_sub_two_zsmul_oangle_center_left``
     - 0.35 (tokens:1)
     - `oangle_eq_pi_sub_two_zsmul_oangle_center_left <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Sphere.lean#L271>`_
