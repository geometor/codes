.. _circumcenter_concurrence:

circumcenter_concurrence
========================

**circumcenter concurrence** · kind: ``theorem`` · family: ``triangle_center`` · verification: ``verified``

.. admonition:: Statement
   :class: note

   Circumcenter theorem

Canonical Form
--------------

.. code-block:: text

   midp(M, A, B), perp(X, M, A, B), midp(N, B, C), perp(X, N, B, C), midp(P, C, A) => perp(X, P, C, A)

Exact Witness Figure
--------------------

.. figure:: circumcenter_concurrence.svg
   :alt: circumcenter_concurrence
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
   * - ``newclid``
     - ``R47_CIRCUMCENTER_THEOREM``
     - midp M A B, perp X M A B, midp N B C, perp X N B C, midp P C A => perp X P C A
