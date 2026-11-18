.. _asa_aas_congruence:

asa_aas_congruence
==================

**asa aas congruence** · kind: ``theorem`` · family: ``congruence`` · verification: ``verified``

**Euclid:** ``I.26``

.. admonition:: Statement
   :class: note

   If two triangles have the two angles equal to two angles respectively, and one side equal to one side, namely, either the side adjoining the equal angles, or that subtending one of the equal angles, they will also have the remaining sides equal to the remaining sides and the remaining angle to the remaining angle.

Canonical Form
--------------

.. code-block:: text

   cong(b, c, e, f), cong(a, b, d, e), eq_angle(a, b, c, d, e, f), eq_angle(b, c, a, e, f, d), form_triangle(a, b, c, AB, BC, AC), form_triangle(d, e, f, DE, EF, DF) => cong(a, b, d, e), cong(b, c, e, f), cong(a, c, d, f), eq_angle(b, a, c, e, d, f)

Exact Witness Figure
--------------------

.. figure:: asa_aas_congruence.svg
   :alt: asa_aas_congruence
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
     - ``I.26``
     - I.26
   * - :doc:`leaneuclid </foundations/cards/leaneuclid>`
     - ``Elements.Book1.proposition_26``
     - ∀ (a b c d e f : Point) (AB BC AC DE EF DF : Line), formTriangle a b c AB BC AC ∧ formTriangle d e f DE EF DF ∧ (∠ a:b:c = ∠ d:e:f) ∧ (∠ b:c:a = ∠ e:f:d) ∧ (\|(b─c)\| = \|(e─f)\| ∨ \|(a
   * - :doc:`alphageometry </foundations/cards/alphageometry>`
     - ``rule.r36``
     - eqangle6 B A B C Q P Q R, eqangle6 C A C B R P R Q, ncoll A B C, cong A B P Q => contri A B C P Q R
   * - :doc:`newclid </foundations/cards/newclid>`
     - ``R36_ASA_CONGRUENCE_OF_TRIANGLES_DIRECT``
     - eqangle B A B C Q P Q R, eqangle C A C B R P R Q, ncoll A B C, cong A B P Q, sameclock A B C P Q R, diff A B C, diff P Q R => contri A B C P Q R

Proof Traces
------------

.. collapse:: LeanEuclid ``Elements.Book1.proposition_26`` (34 steps)

   .. code-block:: lean

      euclid_intros
      split_ors
      · have : (|(a─b)| = |(d─e)|) := by
      by_contra
      by_cases (|(a─b)| > |(d─e)|)
      · euclid_apply (proposition_3 b a e d AB DE) as g
      euclid_apply (line_from_points g c) as GC
      euclid_apply (proposition_4 b g c e d f AB GC BC DE DF EF)
      euclid_finish
      · -- Omitted by Euclid.
      euclid_assert (|(d─e)| > |(a─b)|)
      euclid_apply (proposition_3 e d b a DE AB) as g
      euclid_apply (line_from_points g f) as GF
      euclid_apply (proposition_4 e g f b a c DE GF EF AB AC BC)
      euclid_finish
      euclid_apply (proposition_4 b a c e d f AB AC BC DE DF EF)
      euclid_finish
      · have : (|(b─c)| = |(e─f)|) := by
      by_contra
      by_cases (|(b─c)| > |(e─f)|)
      · euclid_apply (proposition_3 b c e f BC EF) as h
      euclid_apply (line_from_points a h)  as AH
      euclid_apply (proposition_4 b a h e d f AB AH BC DE DF EF)
      euclid_apply (proposition_16 a c h b AC BC AH)
      euclid_finish
      · -- Omitted by Euclid.
      euclid_assert (|(e─f)| > |(b─c)|)
      euclid_apply (proposition_3 e f b c EF BC) as h
      euclid_apply (line_from_points d h) as DH
      euclid_apply (proposition_4 e d h b a c DE DH EF AB AC BC)
      euclid_apply (proposition_16 d f h e DF EF DH)
      euclid_finish
      euclid_apply (proposition_4 b a c e d f AB AC BC DE DF EF)
      euclid_finish
