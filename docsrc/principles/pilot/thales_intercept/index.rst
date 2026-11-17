.. _thales_intercept:

thales_intercept
================

**thales intercept** · kind: ``theorem`` · family: ``similarity`` · verification: ``verified``

**Euclid:** ``VI.2``

.. admonition:: Statement
   :class: note

   If a straight line be drawn parallel to one of the sides of a triangle, it will cut the sides of the triangle proportionally; and, if the sides of the triangle be cut proportionally, the line joining the points of section will be parallel to the remaining side of the triangle.

Canonical Form
--------------

.. code-block:: text

   para(A, B, C, D), coll(O, A, C), coll(O, B, D) => eq_ratio(A, B, C, D, O, O)

Exact Witness Figure
--------------------

.. figure:: thales_intercept.svg
   :alt: thales_intercept
   :align: center

   Exact witness verified (5 points, 2 lines, 0 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - ``euclid``
     - ``VI.2``
     - VI.2
   * - ``alphageometry``
     - ``rule.r07``
     - para A B C D, coll O A C, coll O B D => eqratio3 A B C D O O
   * - ``newclid``
     - ``R07_THALES_THEOREM_1``
     - para A B C D, coll O A C, coll O B D, ncoll O A B => simtri O A B O C D, eqratio O A C A O B B D, eqratio O C A C O D B D

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
     - 0.35 (tokens:1)
     - `angle_eq_pi_div_two_iff_mem_sphere_of_isDiameter <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Sphere.lean#L79>`_
