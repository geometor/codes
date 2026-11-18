.. _equilateral_apex:

equilateral_apex
================

**equilateral apex** · kind: ``construction`` · family: ``congruence`` · verification: ``verified``

**Euclid:** ``I.1``

.. admonition:: Statement
   :class: note

   On a given finite straight line to construct an equilateral triangle.

Canonical Form
--------------

.. code-block:: text

   cong(c, a, a, b), cong(c, b, a, b)

Exact Witness Figure
--------------------

.. figure:: equilateral_apex.svg
   :alt: equilateral_apex
   :align: center

   Exact witness verified (3 points, 0 lines, 2 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - :doc:`euclid </foundations/cards/euclid>`
     - ``I.1``
     - I.1
   * - :doc:`leaneuclid </foundations/cards/leaneuclid>`
     - ``Elements.Book1.proposition_1``
     - ∀ (a b : Point) (AB : Line), distinctPointsOnLine a b AB → ∃ c : Point, \|(c─a)\| = \|(a─b)\| ∧ \|(c─b)\| = \|(a─b)\|
   * - :doc:`leaneuclid </foundations/cards/leaneuclid>`
     - ``Elements.Book1.proposition_1'``
     - ∀ (a b x : Point) (AB : Line), distinctPointsOnLine a b AB ∧ ¬(x.onLine AB) → ∃ c : Point, \|(c─a)\| = \|(a─b)\| ∧ \|(c─b)\| = \|(a─b)\| ∧ (c.opposingSides x AB)
   * - :doc:`alphageometry </foundations/cards/alphageometry>`
     - ``def.eq_triangle``
     - eq\_triangle x b c

Proof Traces
------------

.. collapse:: LeanEuclid ``Elements.Book1.proposition_1`` (8 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply circle_from_points a b as BCD
      euclid_apply circle_from_points b a as ACE
      euclid_apply intersection_circles BCD ACE as c
      euclid_apply point_on_circle_onlyif a b c BCD
      euclid_apply point_on_circle_onlyif b a c ACE
      use c
      euclid_finish

.. collapse:: LeanEuclid ``Elements.Book1.proposition_1'`` (8 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply circle_from_points a b as BCD
      euclid_apply circle_from_points b a as ACE
      euclid_apply intersection_opposite_side BCD ACE x a b AB as c
      euclid_apply point_on_circle_onlyif a b c BCD
      euclid_apply point_on_circle_onlyif b a c ACE
      use c
      euclid_finish
