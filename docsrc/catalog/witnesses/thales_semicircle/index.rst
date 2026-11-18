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
   * - :doc:`euclid </foundations/cards/euclid>`
     - ``III.31``
     - III.31
   * - :doc:`alphageometry </foundations/cards/alphageometry>`
     - ``rule.r20``
     - circle O A B C, coll O A C => perp A B B C
   * - :doc:`newclid </foundations/cards/newclid>`
     - ``R20_DIAMETER_IS_HYPOTENUSE``
     - circle O A B C, coll O A C => perp A B B C

Linked Library Entries
----------------------

Name-matched entries with confidence ≥ 0.7 (lower-confidence token matches are omitted).

.. list-table::
   :header-rows: 1
   :widths: 14 40 12 34

   * - Library
     - Declaration
     - Confidence
     - Evidence
   * - ``mathlib4``
     - `angle\_eq\_pi\_div\_two\_iff\_mem\_sphere\_of\_isDiameter <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Sphere.lean#L79>`__
     - 0.7
     - tokens:2
