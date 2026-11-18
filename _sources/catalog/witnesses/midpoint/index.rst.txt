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
   * - :doc:`euclid </foundations/cards/euclid>`
     - ``I.10``
     - I.10
   * - :doc:`leaneuclid </foundations/cards/leaneuclid>`
     - ``Elements.Book1.proposition_10``
     - ∀ (a b : Point) (AB : Line), distinctPointsOnLine a b AB → ∃ d : Point, (between a d b) ∧ (\|(a─d)\| = \|(d─b)\|)
   * - :doc:`alphageometry </foundations/cards/alphageometry>`
     - ``def.midpoint``
     - midpoint x a b
   * - :doc:`sympy </foundations/cards/sympy>`
     - ``Point.midpoint``
     - Point.midpoint(self, p)
   * - :doc:`sympy </foundations/cards/sympy>`
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

Name-matched entries with confidence ≥ 0.7 (lower-confidence token matches are omitted).

.. list-table::
   :header-rows: 1
   :widths: 14 40 12 34

   * - Library
     - Declaration
     - Confidence
     - Evidence
   * - ``geocoq``
     - `proposition\_10 <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Elements/OriginalProofs/proposition_10.v#L10>`__
     - 1.0
     - euclid\_ref:proposition\_10
   * - ``geocoq``
     - `bet'\_midpoint <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Algebraic/Counter_models/nD/counter_model_bet_inner_transitivity.v#L40>`__
     - 0.95
     - lexicon:Midpoint
   * - ``geocoq``
     - `coplanar\_midpoint <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Algebraic/Counter_models/nD/counter_model_bet_inner_transitivity.v#L181>`__
     - 0.95
     - lexicon:Midpoint
   * - ``mathlib4``
     - `dist\_eq\_iff\_eq\_smul\_rotation\_pi\_div\_two\_vadd\_midpoint <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Oriented/Affine.lean#L727>`__
     - 0.95
     - lexicon:midpoint
   * - ``mathlib4``
     - `eulerPoint\_eq\_midpoint <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/NinePointCircle.lean#L226>`__
     - 0.95
     - lexicon:midpoint
