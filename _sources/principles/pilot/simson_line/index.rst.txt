.. _simson_line:

simson_line
===========

**simson line** · kind: ``theorem`` · family: ``circle`` · verification: ``verified``

.. admonition:: Statement
   :class: note

   Simson's line theorem

Canonical Form
--------------

.. code-block:: text

   cyclic(A, B, C, P), coll(A, L, C), perp(P, L, A, C), coll(M, B, C), perp(P, M, B, C), coll(N, A, B), perp(P, N, A, B) => coll(L, M, N)

Exact Witness Figure
--------------------

.. figure:: simson_line.svg
   :alt: simson_line
   :align: center

   Exact witness verified (7 points, 1 lines, 0 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - ``newclid``
     - ``R45_SIMSONS_LINE_THEOREM``
     - cyclic A B C P, coll A L C, perp P L A C, coll M B C, perp P M B C, coll N A B, perp P N A B => coll L M N
