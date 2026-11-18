.. _sss_congruence:

sss_congruence
==============

**sss congruence** · kind: ``theorem`` · family: ``congruence`` · verification: ``verified``

**Euclid:** ``I.8``

.. admonition:: Statement
   :class: note

   If two triangles have the two sides equal to two sides respectively, and have also the base equal to the base, they will also have the angles equal which are contained by the equal straight lines.

Canonical Form
--------------

.. code-block:: text

   cong(a, b, d, e), cong(a, c, d, f), cong(b, c, e, f), form_triangle(a, b, c, AB, BC, AC), form_triangle(d, e, f, DE, EF, DF) => eq_angle(b, a, c, e, d, f)

Exact Witness Figure
--------------------

.. figure:: sss_congruence.svg
   :alt: sss_congruence
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
     - ``I.8``
     - I.8
   * - :doc:`leaneuclid </foundations/cards/leaneuclid>`
     - ``Elements.Book1.proposition_8``
     - ∀ (a b c d e f : Point) (AB BC AC DE EF DF : Line), formTriangle a b c AB BC AC ∧ formTriangle d e f DE EF DF ∧ \|(a─b)\| = \|(d─e)\| ∧ \|(a─c)\| = \|(d─f)\| ∧ \|(b─c)\| = \|(e─f)\| → ∠ b:a:c
   * - :doc:`alphageometry </foundations/cards/alphageometry>`
     - ``rule.r33``
     - cong A B P Q, cong B C Q R, eqangle6 B A B C Q P Q R, ncoll A B C => contri\* A B C P Q R
   * - :doc:`newclid </foundations/cards/newclid>`
     - ``R64_SSS_CONGRUENCE_OF_TRIANGLES_DIRECT``
     - cong A B P Q, cong B C Q R, cong C A R P, ncoll A B C, sameclock A B C P Q R, diff A B C, diff P Q R => contri A B C P Q R

Proof Traces
------------

.. collapse:: LeanEuclid ``Elements.Book1.proposition_8`` (7 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply (superposition b c a e f d BC AC AB EF) as (c', g, CG', EG)
      euclid_assert c' = f
      by_cases d = g
      · euclid_finish
      · euclid_apply (proposition_7 e f d g EF DE DF EG CG')
      euclid_finish
