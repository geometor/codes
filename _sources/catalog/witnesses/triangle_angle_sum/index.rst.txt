.. _triangle_angle_sum:

triangle_angle_sum
==================

**triangle angle sum** · kind: ``theorem`` · family: ``parallel`` · verification: ``verified``

**Euclid:** ``I.32``

.. admonition:: Statement
   :class: note

   In any triangle, if one of the sides be produced, the exterior angle is equal to the two interior and opposite angles, and the three interior angles of the triangle are equal to two right angles.

Canonical Form
--------------

.. code-block:: text

   between(b, c, d), form_triangle(a, b, c, AB, BC, AC) => eq_angle(a, c, d, c, a, b)

Exact Witness Figure
--------------------

.. figure:: triangle_angle_sum.svg
   :alt: triangle_angle_sum
   :align: center

   Exact witness verified (4 points, 2 lines, 0 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - :doc:`euclid </foundations/cards/euclid>`
     - ``I.32``
     - I.32
   * - :doc:`leaneuclid </foundations/cards/leaneuclid>`
     - ``Elements.Book1.proposition_32``
     - ∀ (a b c d : Point) (AB BC AC : Line), formTriangle a b c AB BC AC ∧ (between b c d) → ∠ a:c:d = ∠ c:a:b + ∠ a:b:c ∧ ∠ a:b:c + ∠ b:c:a + ∠ c:a:b = ∟ + ∟
   * - :doc:`alphageometry </foundations/cards/alphageometry>`
     - ``rule.r09``
     - eqangle a b c d m n p q, eqangle c d e f p q r u => eqangle a b e f m n r u
   * - :doc:`newclid </foundations/cards/newclid>`
     - ``R09_SUM_OF_ANGLES_OF_A_TRIANGLE``
     - eqangle A B C D M N P Q, eqangle C D E F P Q R U, npara A B E F => eqangle A B E F M N R U

Proof Traces
------------

.. collapse:: LeanEuclid ``Elements.Book1.proposition_32`` (11 steps)

   .. code-block:: lean

      euclid_intros
      have : (∠ a:c:d : ℝ) = (∠ c:a:b) + (∠ a:b:c) := by
      euclid_apply (proposition_31 c a b AB ) as CE
      euclid_apply (point_on_line_same_side BC CE a ) as e
      euclid_apply (proposition_29''' b e a c AB CE AC)
      euclid_apply (proposition_29'''' e a d c b CE AB BC)
      euclid_finish
      constructor
      · assumption
      · euclid_apply (proposition_13 a c b d AC BC)
      euclid_finish

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
   * - ``geocoq``
     - `proposition\_32 <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Elements/OriginalProofs/proposition_32.v#L10>`__
     - 1.0
     - euclid\_ref:proposition\_32
   * - ``mathlib4``
     - `angle\_excenter\_singleton <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Incenter.lean#L330>`__
     - 0.7
     - tokens:2
   * - ``mathlib4``
     - `angle\_excenter\_singleton\_eq\_angle\_add\_pi\_div\_two <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Incenter.lean#L338>`__
     - 0.7
     - tokens:2
   * - ``mathlib4``
     - `angle\_excenter\_singleton\_eq\_angle\_div\_two <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Incenter.lean#L307>`__
     - 0.7
     - tokens:2
