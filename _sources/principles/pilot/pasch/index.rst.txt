.. _pasch:

pasch
=====

**pasch** · kind: ``axiom`` · family: ``order`` · verification: ``gap``

.. admonition:: Statement
   :class: note

   If b is between a and c and a and c are on the same side of L, then a and b are on the same side of L

Canonical Form
--------------

.. code-block:: text

   between(a, b, c), same_side(a, c, L) => same_side(a, b, L)

.. admonition:: Verification Gap
   :class: warning

   Requires 1D betweenness / half-plane order predicates not yet native in geometor.model.proof.

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - ``leaneuclid``
     - ``pasch_1``
     - ∀ (a b c : Point) (L : Line), (between a b c) ∧ (a.sameSide c L) → a.sameSide b L
   * - ``leaneuclid``
     - ``pasch_2``
     - ∀ (a b c : Point) (L : Line), (between a b c) ∧ (a.onLine L) ∧ ¬(b.onLine L) → b.sameSide c L
   * - ``leaneuclid``
     - ``pasch_3``
     - ∀ (a b c : Point) (L : Line), (between a b c) ∧ (b.onLine L) → ¬(a.sameSide c L)
   * - ``leaneuclid``
     - ``pasch_4``
     - ∀ (a b c : Point) (L M : Line), (L ≠ M) ∧ (b.onLine L) ∧ (b.onLine M) ∧ distinctPointsOnLine a c M ∧ (a ≠ b) ∧ (c ≠ b) ∧ ¬(a.sameSide c L) → between a b c

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
     - ``inner_pasch``
     - 0.35 (tokens:1)
     - `inner_pasch <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Algebraic/Counter_models/Planar/counter_model_bet_inner_transitivity.v#L34>`_
   * - ``geocoq``
     - ``inner_pasch``
     - 0.35 (tokens:1)
     - `inner_pasch <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Algebraic/Counter_models/Planar/counter_model_bet_symmetry.v#L132>`_
   * - ``geocoq``
     - ``inner_pasch``
     - 0.35 (tokens:1)
     - `inner_pasch <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Algebraic/Counter_models/Planar/counter_model_cong_identity.v#L43>`_
