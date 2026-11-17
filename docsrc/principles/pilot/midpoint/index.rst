.. _midpoint:

midpoint
========

**midpoint** · kind: ``construction`` · family: ``incidence`` · verification: ``verified``

**Euclid:** ``I.10``

.. admonition:: Statement
   :class: note

   To bisect a given finite straight line.

Canonical Form
--------------

.. code-block:: text

   cong(a, d, d, b), between(a, d, b)

Exact Witness Figure
--------------------

.. figure:: midpoint.svg
   :alt: midpoint
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
     - ``I.10``
     - I.10
   * - ``leaneuclid``
     - ``Elements.Book1.proposition_10``
     - ∀ (a b : Point) (AB : Line), distinctPointsOnLine a b AB → ∃ d : Point, (between a d b) ∧ (\|(a─d)\| = \|(d─b)\|)
   * - ``alphageometry``
     - ``def.midpoint``
     - midpoint x a b
   * - ``sympy``
     - ``Point.midpoint``
     - Point.midpoint(self, p)
   * - ``sympy``
     - ``Segment.midpoint``
     - @property Segment.midpoint

Proof Traces
------------

.. collapse:: LeanEuclid ``Elements.Book1.proposition_10`` (10 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply (proposition_1 a b AB) as c
      euclid_apply (line_from_points c a) as AC
      euclid_apply (line_from_points c b ) as BC
      euclid_apply (proposition_9' c a b AC BC) as d'
      euclid_apply (line_from_points c d') as CD
      euclid_apply (intersection_lines CD AB) as d
      euclid_apply (proposition_4 c a d c b d AC AB CD BC AB CD)
      use d
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
     - ``proposition_10``
     - 1.0 (euclid_ref:proposition_10)
     - `proposition_10 <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Elements/OriginalProofs/proposition_10.v#L10>`_
   * - ``geocoq``
     - ``bet'_midpoint``
     - 0.95 (lexicon:Midpoint)
     - `bet'_midpoint <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Algebraic/Counter_models/nD/counter_model_bet_inner_transitivity.v#L40>`_
   * - ``geocoq``
     - ``coplanar_midpoint``
     - 0.95 (lexicon:Midpoint)
     - `coplanar_midpoint <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Algebraic/Counter_models/nD/counter_model_bet_inner_transitivity.v#L181>`_
   * - ``mathlib4``
     - ``dist_eq_iff_eq_smul_rotation_pi_div_two_vadd_midpoint``
     - 0.95 (lexicon:midpoint)
     - `dist_eq_iff_eq_smul_rotation_pi_div_two_vadd_midpoint <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Oriented/Affine.lean#L727>`_
   * - ``mathlib4``
     - ``eulerPoint_eq_midpoint``
     - 0.95 (lexicon:midpoint)
     - `eulerPoint_eq_midpoint <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/NinePointCircle.lean#L226>`_
   * - ``mathlib4``
     - ``oangle_midpoint_left``
     - 0.35 (tokens:1)
     - `oangle_midpoint_left <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Oriented/Affine.lean#L649>`_
   * - ``cindyjs``
     - ``midpoint``
     - 0.35 (tokens:1)
     - `midpoint <https://github.com/CindyJS/CindyJS/blob/c5b87a373e574c0da6137cc95fbe48a8d6e534c5/src/js/libgeo/GeoOps.js#L218>`_
