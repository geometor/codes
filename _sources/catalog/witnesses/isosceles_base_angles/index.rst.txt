.. _isosceles_base_angles:

isosceles_base_angles
=====================

**isosceles base angles** · kind: ``theorem`` · family: ``congruence`` · verification: ``verified``

**Euclid:** ``I.5``

.. admonition:: Statement
   :class: note

   In isosceles triangles the angles at the base are equal to one another, and, if the equal straight lines be produced further, the angles under the base will be equal to one another.

Canonical Form
--------------

.. code-block:: text

   cong(a, b, a, c), between(a, b, d), between(a, c, e), form_triangle(a, b, c, AB, BC, AC) => eq_angle(a, b, c, a, c, b), eq_angle(c, b, d, b, c, e)

Exact Witness Figure
--------------------

.. figure:: isosceles_base_angles.svg
   :alt: isosceles_base_angles
   :align: center

   Exact witness verified (3 points, 0 lines, 0 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - :doc:`euclid </foundations/cards/euclid>`
     - ``I.5``
     - I.5
   * - :doc:`leaneuclid </foundations/cards/leaneuclid>`
     - ``Elements.Book1.proposition_5``
     - ∀ (a b c d e : Point) (AB BC AC : Line), formTriangle a b c AB BC AC ∧ (\|(a─b)\| = \|(a─c)\|) ∧ (between a b d) ∧ (between a c e) → (∠ a:b:c = ∠ a:c:b) ∧ (∠ c:b:d = ∠ b:c:e)
   * - :doc:`leaneuclid </foundations/cards/leaneuclid>`
     - ``Elements.Book1.proposition_5'``
     - ∀ (a b c : Point) (AB BC AC : Line), formTriangle a b c AB BC AC ∧ (\|(a─b)\| = \|(a─c)\|) → (∠ a:b:c = ∠ a:c:b)
   * - :doc:`alphageometry </foundations/cards/alphageometry>`
     - ``rule.r13``
     - cong O A O B, ncoll O A B => eqangle O A A B A B O B
   * - :doc:`newclid </foundations/cards/newclid>`
     - ``R13_ISOSCELES_TRIANGLE_EQUAL_ANGLES``
     - cong O A O B, ncoll O A B => eqangle O A A B A B O B

Proof Traces
------------

.. collapse:: LeanEuclid ``Elements.Book1.proposition_5`` (10 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply (point_between_points_shorter_than AB b d (c─e)) as f
      euclid_apply (proposition_3 a e f a AC AB) as g
      euclid_apply (line_from_points c f) as FC
      euclid_apply (line_from_points b g) as GB
      euclid_apply (proposition_4 a f c a g b AB FC AC AC GB AB)
      euclid_apply (proposition_4 f b c g c b AB BC FC AC BC GB)
      euclid_apply (sum_angles_onlyif b a g c AB GB)
      euclid_apply (sum_angles_onlyif c a f b AC FC)
      euclid_finish

.. collapse:: LeanEuclid ``Elements.Book1.proposition_5'`` (5 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply (extend_point AB a b) as d
      euclid_apply (extend_point AC a c) as e
      euclid_apply (proposition_5 a b c d e AB BC AC)
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
   * - ``mathlib4``
     - `abs\_oangle\_left\_toReal\_lt\_pi\_div\_two\_of\_dist\_eq <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Oriented/Affine.lean#L379>`__
     - 0.7
     - tokens:2
   * - ``mathlib4``
     - `abs\_oangle\_right\_toReal\_lt\_pi\_div\_two\_of\_dist\_eq <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Oriented/Affine.lean#L372>`__
     - 0.7
     - tokens:2
   * - ``mathlib4``
     - `abs\_oangle\_sub\_left\_toReal\_lt\_pi\_div\_two <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Oriented/Basic.lean#L1026>`__
     - 0.7
     - tokens:2
