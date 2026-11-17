.. _betweenness_transitivity:

betweenness_transitivity
========================

**betweenness transitivity** · kind: ``axiom`` · family: ``order`` · verification: ``gap``

.. admonition:: Statement
   :class: note

   If b is between a and c and d is between a and b then d is between a and c

Canonical Form
--------------

.. code-block:: text

   between(a, b, c), between(a, d, b) => between(a, d, c)

.. admonition:: Verification Gap
   :class: warning

   Requires ternary between(A, B, C) order relation in geometor.model.proof.

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - ``leaneuclid``
     - ``between_trans_in``
     - ∀ (a b c d : Point), (between a b c) ∧ (between a d b) → between a d c
   * - ``leaneuclid``
     - ``between_trans_out``
     - ∀ (a b c d : Point), (between a b c) ∧ (between b c d) → (between a b d)

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
     - ``bet_inner_transitivity``
     - 0.35 (tokens:1)
     - `bet_inner_transitivity <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Algebraic/Counter_models/Planar/counter_model_bet_inner_transitivity.v#L11>`_
   * - ``geocoq``
     - ``cong_inner_transitivity``
     - 0.35 (tokens:1)
     - `cong_inner_transitivity <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Algebraic/Counter_models/Planar/counter_model_bet_inner_transitivity.v#L31>`_
   * - ``geocoq``
     - ``bet_inner_transitivity``
     - 0.35 (tokens:1)
     - `bet_inner_transitivity <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Algebraic/Counter_models/Planar/counter_model_bet_symmetry.v#L113>`_
