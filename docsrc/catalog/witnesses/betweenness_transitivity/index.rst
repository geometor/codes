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
   * - :doc:`leaneuclid </foundations/cards/leaneuclid>`
     - ``between_trans_in``
     - ∀ (a b c d : Point), (between a b c) ∧ (between a d b) → between a d c
   * - :doc:`leaneuclid </foundations/cards/leaneuclid>`
     - ``between_trans_out``
     - ∀ (a b c d : Point), (between a b c) ∧ (between b c d) → (between a b d)
