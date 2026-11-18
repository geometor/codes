.. _orthocenter_concurrence:

orthocenter_concurrence
=======================

**orthocenter concurrence** · kind: ``theorem`` · family: ``triangle_center`` · verification: ``verified``

.. admonition:: Statement
   :class: note

   Orthocenter theorem

Canonical Form
--------------

.. code-block:: text

   perp(A, B, C, D), perp(A, C, B, D), ncoll(A, B, C) => perp(A, D, B, C)

Exact Witness Figure
--------------------

.. figure:: orthocenter_concurrence.svg
   :alt: orthocenter_concurrence
   :align: center

   Exact witness verified (4 points, 6 lines, 0 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - :doc:`newclid </foundations/cards/newclid>`
     - ``R43_ORTHOCENTER_THEOREM``
     - perp A B C D, perp A C B D, ncoll A B C => perp A D B C
