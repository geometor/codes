.. _aa_similarity:

aa_similarity
=============

**aa similarity** · kind: ``theorem`` · family: ``similarity`` · verification: ``verified``

**Euclid:** ``VI.4``

.. admonition:: Statement
   :class: note

   In equiangular triangles the sides about the equal angles are proportional, and those are corresponding sides which subtend the equal angles.

Canonical Form
--------------

.. code-block:: text

   eq_angle(B, A, B, C, Q, P, Q, R), eq_angle(C, A, C, B, R, P, R, Q), ncoll(A, B, C) => sim_tri(A, B, C, P, Q, R)

Exact Witness Figure
--------------------

.. figure:: aa_similarity.svg
   :alt: aa_similarity
   :align: center

   Exact witness verified (6 points, 0 lines, 0 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - :doc:`euclid </foundations/cards/euclid>`
     - ``VI.4``
     - VI.4
   * - :doc:`alphageometry </foundations/cards/alphageometry>`
     - ``rule.r34``
     - eqangle6 B A B C Q P Q R, eqangle6 C A C B R P R Q, ncoll A B C => simtri A B C P Q R
   * - :doc:`newclid </foundations/cards/newclid>`
     - ``R34_AA_SIMILARITY_OF_TRIANGLES_DIRECT``
     - eqangle B A B C Q P Q R, eqangle C A C B R P R Q, ncoll A B C, sameclock A B C P Q R, diff A B C, diff P Q R => simtri A B C P Q R
