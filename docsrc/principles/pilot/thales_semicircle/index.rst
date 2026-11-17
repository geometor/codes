.. _thales_semicircle:

thales_semicircle
=================

**thales semicircle** · kind: ``theorem`` · family: ``circle`` · verification: ``verified``

**Euclid:** ``III.31``

.. admonition:: Statement
   :class: note

   In a circle the angle in the semicircle is right, that in a greater segment less than a right angle, and that in a less segment greater than a right angle; and further the angle of the greater segment is greater than a right angle, and the angle of the less segment less than a right angle.

Canonical Form
--------------

.. code-block:: text

   circle_center(O, A, B, C), coll(O, A, C) => perp(A, B, B, C)

Exact Witness Figure
--------------------

.. figure:: thales_semicircle.svg
   :alt: thales_semicircle
   :align: center

   Exact witness verified (5 points, 2 lines, 1 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - ``euclid``
     - ``III.31``
     - III.31
   * - ``alphageometry``
     - ``rule.r20``
     - circle O A B C, coll O A C => perp A B B C
   * - ``newclid``
     - ``R20_DIAMETER_IS_HYPOTENUSE``
     - circle O A B C, coll O A C => perp A B B C

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
     - ``existential_thales_postulate``
     - 0.35 (tokens:1)
     - `existential_thales_postulate <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Axioms/parallel_postulates.v#L208>`_
   * - ``geocoq``
     - ``thales_converse_postulate``
     - 0.35 (tokens:1)
     - `thales_converse_postulate <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Axioms/parallel_postulates.v#L203>`_
   * - ``geocoq``
     - ``thales_postulate``
     - 0.35 (tokens:1)
     - `thales_postulate <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Axioms/parallel_postulates.v#L198>`_
   * - ``mathlib4``
     - ``angle_eq_pi_div_two_iff_mem_sphere_of_isDiameter``
     - 0.7 (tokens:2)
     - `angle_eq_pi_div_two_iff_mem_sphere_of_isDiameter <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Sphere.lean#L79>`_
