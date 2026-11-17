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
   * - ``euclid``
     - ``I.32``
     - I.32
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_32``
     - ∀ (a b c d : Point) (AB BC AC : Line), formTriangle a b c AB BC AC ∧ (between b c d) → ∠ a:c:d = ∠ c:a:b + ∠ a:b:c ∧ ∠ a:b:c + ∠ b:c:a + ∠ c:a:b = ∟ + ∟
   * - ``alphageometry``
     - ``rule.r09``
     - eqangle a b c d m n p q, eqangle c d e f p q r u => eqangle a b e f m n r u
   * - ``newclid``
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

.. list-table::
   :header-rows: 1
   :widths: 14 28 12 46

   * - Library
     - Declaration
     - Confidence
     - Source
   * - ``geocoq``
     - ``proposition_32``
     - 1.0 (euclid_ref:proposition_32)
     - `proposition_32 <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Elements/OriginalProofs/proposition_32.v#L10>`_
   * - ``geocoq``
     - ``postulate_of_existence_of_a_triangle_whose_angles_sum_to_two_rights``
     - 0.35 (tokens:1)
     - `postulate_of_existence_of_a_triangle_whose_angles_sum_to_two_rights <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Axioms/parallel_postulates.v#L175>`_
   * - ``geocoq``
     - ``triangle_circumscription_principle``
     - 0.35 (tokens:1)
     - `triangle_circumscription_principle <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Axioms/parallel_postulates.v#L126>`_
   * - ``mathlib4``
     - ``angle_excenter_singleton``
     - 0.7 (tokens:2)
     - `angle_excenter_singleton <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Incenter.lean#L330>`_
   * - ``mathlib4``
     - ``angle_excenter_singleton_eq_angle_add_pi_div_two``
     - 0.7 (tokens:2)
     - `angle_excenter_singleton_eq_angle_add_pi_div_two <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Incenter.lean#L338>`_
   * - ``mathlib4``
     - ``angle_excenter_singleton_eq_angle_div_two``
     - 0.7 (tokens:2)
     - `angle_excenter_singleton_eq_angle_div_two <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Incenter.lean#L307>`_
   * - ``jgex``
     - ``angle_deduction``
     - 0.35 (tokens:1)
     - `angle_deduction <https://github.com/kovzol/Java-Geometry-Expert/blob/5489aacb40afc91b5c5ca539db853cca216e1165/src/main/java/gprover/Full.java#L2506>`_
   * - ``jgex``
     - ``check_angle_ls_90``
     - 0.35 (tokens:1)
     - `check_angle_ls_90 <https://github.com/kovzol/Java-Geometry-Expert/blob/5489aacb40afc91b5c5ca539db853cca216e1165/src/main/java/gprover/Gib.java#L1624>`_
   * - ``jgex``
     - ``Panel_Angle``
     - 0.35 (tokens:1)
     - `Panel_Angle <https://github.com/kovzol/Java-Geometry-Expert/blob/5489aacb40afc91b5c5ca539db853cca216e1165/src/main/java/wprover/CProperty.java#L654>`_
   * - ``cindyjs``
     - ``get_angle``
     - 0.35 (tokens:1)
     - `get_angle <https://github.com/CindyJS/CindyJS/blob/c5b87a373e574c0da6137cc95fbe48a8d6e534c5/src/js/libgeo/GeoOps.js#L645>`_
   * - ``cindyjs``
     - ``set_angle``
     - 0.35 (tokens:1)
     - `set_angle <https://github.com/CindyJS/CindyJS/blob/c5b87a373e574c0da6137cc95fbe48a8d6e534c5/src/js/libgeo/GeoOps.js#L417>`_
