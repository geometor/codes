.. _betweenness_symmetry:

betweenness_symmetry
====================

**betweenness symmetry** · kind: ``axiom`` · family: ``order`` · verification: ``gap``

.. admonition:: Statement
   :class: note

   between axioms If b is between a and c then b is between c and a, a != b, a != c, and a is not a. between bnd c

Canonical Form
--------------

.. code-block:: text

   between(a, b, c) => between(c, b, a), between(b, a, c)

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
     - ``between_symm``
     - ∀ (a b c : Point), between a b c → (between c b a) ∧ (a ≠ b) ∧ (a ≠ c) ∧ ¬(between b a c)
