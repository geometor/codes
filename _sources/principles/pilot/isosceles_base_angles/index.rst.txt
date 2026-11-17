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
   * - ``euclid``
     - ``I.5``
     - I.5
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_5``
     - ∀ (a b c d e : Point) (AB BC AC : Line), formTriangle a b c AB BC AC ∧ (\|(a─b)\| = \|(a─c)\|) ∧ (between a b d) ∧ (between a c e) → (∠ a:b:c = ∠ a:c:b) ∧ (∠ c:b:d = ∠ b:c:e)
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_5'``
     - ∀ (a b c : Point) (AB BC AC : Line), formTriangle a b c AB BC AC ∧ (\|(a─b)\| = \|(a─c)\|) → (∠ a:b:c = ∠ a:c:b)
   * - ``alphageometry``
     - ``rule.r13``
     - cong O A O B, ncoll O A B => eqangle O A A B A B O B
   * - ``newclid``
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

.. list-table::
   :header-rows: 1
   :widths: 14 28 12 46

   * - Library
     - Declaration
     - Confidence
     - Source
   * - ``geocoq``
     - ``alternate_interior_angles_postulate``
     - 0.35 (tokens:1)
     - `alternate_interior_angles_postulate <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Axioms/parallel_postulates.v#L70>`_
   * - ``geocoq``
     - ``consecutive_interior_angles_postulate``
     - 0.35 (tokens:1)
     - `consecutive_interior_angles_postulate <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Axioms/parallel_postulates.v#L76>`_
   * - ``geocoq``
     - ``postulate_of_existence_of_a_triangle_whose_angles_sum_to_two_rights``
     - 0.35 (tokens:1)
     - `postulate_of_existence_of_a_triangle_whose_angles_sum_to_two_rights <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Axioms/parallel_postulates.v#L175>`_
   * - ``mathlib4``
     - ``abs_oangle_left_toReal_lt_pi_div_two_of_dist_eq``
     - 0.7 (tokens:2)
     - `abs_oangle_left_toReal_lt_pi_div_two_of_dist_eq <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Oriented/Affine.lean#L379>`_
   * - ``mathlib4``
     - ``abs_oangle_right_toReal_lt_pi_div_two_of_dist_eq``
     - 0.7 (tokens:2)
     - `abs_oangle_right_toReal_lt_pi_div_two_of_dist_eq <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Oriented/Affine.lean#L372>`_
   * - ``mathlib4``
     - ``abs_oangle_sub_left_toReal_lt_pi_div_two``
     - 0.7 (tokens:2)
     - `abs_oangle_sub_left_toReal_lt_pi_div_two <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Oriented/Basic.lean#L1026>`_
   * - ``jgex``
     - ``Angles``
     - 0.35 (tokens:1)
     - `Angles <https://github.com/kovzol/Java-Geometry-Expert/blob/5489aacb40afc91b5c5ca539db853cca216e1165/src/main/java/gprover/Angles.java#L8>`_
   * - ``jgex``
     - ``Panel_Base``
     - 0.35 (tokens:1)
     - `Panel_Base <https://github.com/kovzol/Java-Geometry-Expert/blob/5489aacb40afc91b5c5ca539db853cca216e1165/src/main/java/wprover/CProperty.java#L806>`_
   * - ``galgebra``
     - ``BasisBaseSymbol``
     - 0.35 (tokens:1)
     - `BasisBaseSymbol <https://github.com/pygae/galgebra/blob/d160238c6ddbedce676e633d69840fdaab83ab86/galgebra/atoms.py#L89>`_
   * - ``galgebra``
     - ``BaseProductFunction``
     - 0.35 (tokens:1)
     - `BaseProductFunction <https://github.com/pygae/galgebra/blob/d160238c6ddbedce676e633d69840fdaab83ab86/galgebra/ga.py#L412>`_
   * - ``galgebra``
     - ``BladeProductFunction``
     - 0.35 (tokens:1)
     - `BladeProductFunction <https://github.com/pygae/galgebra/blob/d160238c6ddbedce676e633d69840fdaab83ab86/galgebra/ga.py#L212>`_
