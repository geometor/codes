.. _incenter_concurrence:

incenter_concurrence
====================

**incenter concurrence** · kind: ``theorem`` · family: ``triangle_center`` · verification: ``verified``

.. admonition:: Statement
   :class: note

   Incenter theorem

Canonical Form
--------------

.. code-block:: text

   eq_angle(A, B, A, X, A, X, A, C), eq_angle(B, A, B, X, B, X, B, C), ncoll(A, B, C) => eq_angle(C, B, C, X, C, X, C, A)

Exact Witness Figure
--------------------

.. figure:: incenter_concurrence.svg
   :alt: incenter_concurrence
   :align: center

   Exact witness verified (4 points, 0 lines, 0 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - :doc:`newclid </foundations/cards/newclid>`
     - ``R46_INCENTER_THEOREM``
     - eqangle A B A X A X A C, eqangle B A B X B X B C, ncoll A B C => eqangle C B C X C X C A
