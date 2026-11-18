.. _centroid_concurrence:

centroid_concurrence
====================

**centroid concurrence** · kind: ``theorem`` · family: ``triangle_center`` · verification: ``verified``

.. admonition:: Statement
   :class: note

   Centroid theorem

Canonical Form
--------------

.. code-block:: text

   midp(M, A, B), coll(M, X, C), midp(N, B, C), coll(N, X, A), midp(P, C, A) => coll(X, P, B)

Exact Witness Figure
--------------------

.. figure:: centroid_concurrence.svg
   :alt: centroid_concurrence
   :align: center

   Exact witness verified (7 points, 0 lines, 0 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - :doc:`newclid </foundations/cards/newclid>`
     - ``R48_CENTROID_THEOREM``
     - midp M A B, coll M X C, midp N B C, coll N X A, midp P C A => coll X P B
