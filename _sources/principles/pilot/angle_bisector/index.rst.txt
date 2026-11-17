.. _angle_bisector:

angle_bisector
==============

**angle bisector** · kind: ``construction`` · family: ``congruence`` · verification: ``verified``

**Euclid:** ``I.9``

.. admonition:: Statement
   :class: note

   To bisect a given rectilineal angle.

Canonical Form
--------------

.. code-block:: text

   eq_angle(b, a, f, c, a, f)

Exact Witness Figure
--------------------

.. figure:: angle_bisector.svg
   :alt: angle_bisector
   :align: center

   Exact witness verified (4 points, 3 lines, 0 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - ``euclid``
     - ``I.9``
     - I.9
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_9``
     - ∀ (a b c : Point) (AB AC : Line), formRectilinearAngle b a c AB AC ∧ AB ≠ AC → ∃ f : Point, f ≠ a ∧ (∠ b:a:f = ∠ c:a:f)
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_9'``
     - ∀ (a b c : Point) (AB AC : Line), formRectilinearAngle b a c AB AC ∧ AB ≠ AC → ∃ f : Point, (f.sameSide c AB) ∧ (f.sameSide b AC) ∧ (∠ b:a:f = ∠ c:a:f)
   * - ``alphageometry``
     - ``def.angle_bisector``
     - angle_bisector x a b c
   * - ``sympy``
     - ``Triangle.bisectors``
     - Triangle.bisectors(self)

Proof Traces
------------

.. collapse:: LeanEuclid ``Elements.Book1.proposition_9`` (21 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply point_between_points_shorter_than AB a b (a─c) as d
      euclid_apply (proposition_3 a c a d AC AB) as e
      euclid_apply (line_from_points d e) as DE
      euclid_apply (proposition_1' d e a DE) as f
      euclid_apply (line_from_points f e) as FE
      euclid_apply (line_from_points f d) as FD
      euclid_apply (line_from_points a f) as AF
      use f
      have : ¬(f.onLine AB) := by  -- Omitted by Euclid.
      euclid_intros
      euclid_apply (proposition_5' f d e AB DE FE)
      euclid_apply (proposition_5 a d e b c AB DE AC)
      euclid_finish
      have : ¬(f.onLine AC) := by  -- Omitted by Euclid.
      euclid_intros
      euclid_apply (proposition_5' f e d AC DE FD)
      euclid_apply (proposition_5 a d e b c AB DE AC)
      euclid_finish
      euclid_apply (proposition_8 a d f a e f AB FD AF AC FE AF)
      euclid_finish

.. collapse:: LeanEuclid ``Elements.Book1.proposition_9'`` (22 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply (point_between_points_shorter_than AB a b (a─c)) as d
      euclid_apply (proposition_3 a c a d AC AB) as e
      euclid_apply (line_from_points d e) as DE
      euclid_apply (proposition_1' d e a DE) as f
      euclid_apply (line_from_points f e) as FE
      euclid_apply (line_from_points f d) as FD
      euclid_apply (line_from_points a f) as AF
      use f
      have : ¬(f.onLine AB) := by  -- Omitted by Euclid.
      euclid_intros
      euclid_apply (proposition_5' f d e AB DE FE)
      euclid_apply (proposition_5 a d e b c AB DE AC)
      euclid_finish
      have : ¬(f.onLine AC) := by  -- Omitted by Euclid.
      euclid_intros
      euclid_apply (proposition_5' f e d AC DE FD)
      euclid_apply (proposition_5 a d e b c AB DE AC)
      euclid_finish
      euclid_apply (proposition_8 a d f a e f AB FD AF AC FE AF)
      euclid_apply (intersection_lines AF DE) as g
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
     - ``angle_bisector``
     - 0.7 (tokens:2)
     - `angle_bisector <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Main/Tarski_dev/Ch11_angles.v#L9944>`_
   * - ``geocoq``
     - ``high_school_exterior_angle_theorem``
     - 0.35 (tokens:1)
     - `high_school_exterior_angle_theorem <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Main/Annexes/inscribed_angle.v#L65>`_
   * - ``geocoq``
     - ``inscribed_angle``
     - 0.35 (tokens:1)
     - `inscribed_angle <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Main/Annexes/inscribed_angle.v#L253>`_
   * - ``mathlib4``
     - ``abs_inner_vsub_altitudeFoot_lt_mul``
     - 0.35 (tokens:1)
     - `abs_inner_vsub_altitudeFoot_lt_mul <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Altitude.lean#L341>`_
   * - ``mathlib4``
     - ``dist_orthogonalProjection_eq_iff_angle_eq``
     - 0.35 (tokens:1)
     - `dist_orthogonalProjection_eq_iff_angle_eq <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Bisector.lean#L74>`_
   * - ``mathlib4``
     - ``dist_orthogonalProjection_eq_iff_angle_eq_aux``
     - 0.35 (tokens:1)
     - `dist_orthogonalProjection_eq_iff_angle_eq_aux <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Bisector.lean#L56>`_
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
