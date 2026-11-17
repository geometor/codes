.. _parallel_alternate_angles:

parallel_alternate_angles
=========================

**parallel alternate angles** · kind: ``theorem`` · family: ``parallel`` · verification: ``verified``

**Euclid:** ``I.29``

.. admonition:: Statement
   :class: note

   A straight line falling on parallel straight lines makes the alternate angles equal to one another, the exterior angle equal to the interior and opposite angle, and the interior angles on the same side equal to two right angles.

Canonical Form
--------------

.. code-block:: text

   between(a, g, b), between(c, h, d), between(e, g, h), between(g, h, f), same_side(b, d, EF), para(AB, CD) => eq_angle(a, g, h, g, h, d), eq_angle(e, g, b, g, h, d)

Exact Witness Figure
--------------------

.. figure:: parallel_alternate_angles.svg
   :alt: parallel_alternate_angles
   :align: center

   Exact witness verified (6 points, 3 lines, 0 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - ``euclid``
     - ``I.29``
     - I.29
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_29``
     - ∀ (a b c d e f g h : Point) (AB CD EF : Line), distinctPointsOnLine a b AB ∧ distinctPointsOnLine c d CD ∧ distinctPointsOnLine e f EF ∧ (between a g b) ∧ (between c h d) ∧ (betwee
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_29'``
     - ∀ (a b c d e g h : Point) (AB CD EF : Line), distinctPointsOnLine a b AB ∧ distinctPointsOnLine c d CD ∧ distinctPointsOnLine g h EF ∧ (between a g b) ∧ (between c h d) ∧ (between 
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_29''``
     - ∀ (a b d g h : Point) (AB CD GH : Line), distinctPointsOnLine a b AB ∧ distinctPointsOnLine h d CD ∧ distinctPointsOnLine g h GH ∧ (between a g b) ∧ (b.sameSide d GH) ∧ ¬(AB.inters
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_29'''``
     - ∀ (a d g h : Point) (AB CD GH : Line), distinctPointsOnLine a g AB ∧ distinctPointsOnLine h d CD ∧ distinctPointsOnLine g h GH ∧ a.opposingSides d GH ∧ ¬(AB.intersectsLine CD) → ∠ 
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_29''''``
     - ∀ (b d e g h : Point) (AB CD EF : Line), distinctPointsOnLine g b AB ∧ distinctPointsOnLine h d CD ∧ distinctPointsOnLine e h EF ∧ between e g h ∧ b.sameSide d EF ∧ ¬(AB.intersects
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_29'''''``
     - ∀ (b d g h : Point) (AB CD EF : Line), distinctPointsOnLine g b AB ∧ distinctPointsOnLine h d CD ∧ distinctPointsOnLine g h EF ∧ b.sameSide d EF ∧ ¬(AB.intersectsLine CD) → ∠ b:g:h

Proof Traces
------------

.. collapse:: LeanEuclid ``Elements.Book1.proposition_29`` (17 steps)

   .. code-block:: lean

      euclid_intros
      have : ∠ a:g:h = ∠ g:h:d := by
      by_contra
      by_cases ∠ a:g:h > ∠ g:h:d
      · euclid_assert ∠ a:g:h + ∠ b:g:h > ∠ b:g:h + ∠ g:h:d
      euclid_apply (proposition_13 h g a b EF AB)
      euclid_assert ∠ b:g:h + ∠ g:h:d < ∟ + ∟
      euclid_finish
      · -- Omitted by Euclid.
      euclid_assert ∠ a:g:h < ∠ g:h:d
      euclid_assert ∠ a:g:h + ∠ c:h:g < ∠ g:h:d + ∠ c:h:g
      euclid_apply (proposition_13 g h c d EF CD)
      euclid_assert ∠ a:g:h + ∠ c:h:g < ∟ + ∟
      euclid_finish
      euclid_apply (proposition_15 a b e h g AB EF)
      euclid_apply (proposition_13 b g e h AB EF)
      euclid_finish

.. collapse:: LeanEuclid ``Elements.Book1.proposition_29'`` (4 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply (extend_point EF g h) as f
      euclid_apply (proposition_29 a b c d e f g h AB CD EF)
      euclid_finish

.. collapse:: LeanEuclid ``Elements.Book1.proposition_29''`` (6 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply (extend_point GH g h) as f
      euclid_apply (extend_point GH h g) as e
      euclid_apply (extend_point CD d h) as c
      euclid_apply (proposition_29 a b c d e f g h AB CD GH)
      euclid_finish

.. collapse:: LeanEuclid ``Elements.Book1.proposition_29'''`` (4 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply (extend_point AB a g) as b
      euclid_apply (proposition_29'' a b d g h AB CD GH)
      euclid_finish

.. collapse:: LeanEuclid ``Elements.Book1.proposition_29''''`` (6 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply (extend_point AB b g) as a
      euclid_apply (extend_point CD d h) as c
      euclid_apply (extend_point EF g h) as f
      euclid_apply (proposition_29 a b c d e f g h AB CD EF)
      euclid_finish

.. collapse:: LeanEuclid ``Elements.Book1.proposition_29'''''`` (7 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply (extend_point AB b g) as a
      euclid_apply (extend_point CD d h) as c
      euclid_apply (extend_point EF g h) as f
      euclid_apply (extend_point EF h g) as e
      euclid_apply (proposition_29 a b c d e f g h AB CD EF)
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
     - ``proposition_29``
     - 1.0 (euclid_ref:proposition_29)
     - `proposition_29 <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Elements/OriginalProofs/proposition_29.v#L11>`_
   * - ``geocoq``
     - ``alternate_interior_angles_postulate``
     - 0.7 (tokens:2)
     - `alternate_interior_angles_postulate <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Axioms/parallel_postulates.v#L70>`_
   * - ``geocoq``
     - ``alternative_strong_parallel_postulate``
     - 0.35 (tokens:1)
     - `alternative_strong_parallel_postulate <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Axioms/parallel_postulates.v#L160>`_
   * - ``mathlib4``
     - ``parallel_of_two_zsmul_oangle``
     - 0.7 (tokens:2)
     - `parallel_of_two_zsmul_oangle <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Oriented/Affine.lean#L301>`_
   * - ``mathlib4``
     - ``two_zsmul_oangle_iff_parallel``
     - 0.7 (tokens:2)
     - `two_zsmul_oangle_iff_parallel <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Oriented/Affine.lean#L310>`_
   * - ``mathlib4``
     - ``two_zsmul_oangle_of_parallel``
     - 0.7 (tokens:2)
     - `two_zsmul_oangle_of_parallel <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Oriented/Affine.lean#L244>`_
   * - ``jgex``
     - ``Angles``
     - 0.35 (tokens:1)
     - `Angles <https://github.com/kovzol/Java-Geometry-Expert/blob/5489aacb40afc91b5c5ca539db853cca216e1165/src/main/java/gprover/Angles.java#L8>`_
