.. _angle_bisector:

angle_bisector
==============

**angle bisector** · kind: ``construction`` · family: ``congruence`` · verification: ``verified``

**Euclid:** ``I.9``

.. admonition:: Statement
   :class: note

   To bisect a given rectilineal angle.

Canonical Form
--------------

.. code-block:: text

   eq_angle(b, a, f, c, a, f)

Exact Witness Figure
--------------------

.. figure:: angle_bisector.svg
   :alt: angle_bisector
   :align: center

   Exact witness verified (4 points, 3 lines, 0 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - :doc:`euclid </foundations/cards/euclid>`
     - ``I.9``
     - I.9
   * - :doc:`leaneuclid </foundations/cards/leaneuclid>`
     - ``Elements.Book1.proposition_9``
     - ∀ (a b c : Point) (AB AC : Line), formRectilinearAngle b a c AB AC ∧ AB ≠ AC → ∃ f : Point, f ≠ a ∧ (∠ b:a:f = ∠ c:a:f)
   * - :doc:`leaneuclid </foundations/cards/leaneuclid>`
     - ``Elements.Book1.proposition_9'``
     - ∀ (a b c : Point) (AB AC : Line), formRectilinearAngle b a c AB AC ∧ AB ≠ AC → ∃ f : Point, (f.sameSide c AB) ∧ (f.sameSide b AC) ∧ (∠ b:a:f = ∠ c:a:f)
   * - :doc:`alphageometry </foundations/cards/alphageometry>`
     - ``def.angle_bisector``
     - angle\_bisector x a b c
   * - :doc:`sympy </foundations/cards/sympy>`
     - ``Triangle.bisectors``
     - Triangle.bisectors(self)

Proof Traces
------------

.. collapse:: LeanEuclid ``Elements.Book1.proposition_9`` (21 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply point_between_points_shorter_than AB a b (a─c) as d
      euclid_apply (proposition_3 a c a d AC AB) as e
      euclid_apply (line_from_points d e) as DE
      euclid_apply (proposition_1' d e a DE) as f
      euclid_apply (line_from_points f e) as FE
      euclid_apply (line_from_points f d) as FD
      euclid_apply (line_from_points a f) as AF
      use f
      have : ¬(f.onLine AB) := by  -- Omitted by Euclid.
      euclid_intros
      euclid_apply (proposition_5' f d e AB DE FE)
      euclid_apply (proposition_5 a d e b c AB DE AC)
      euclid_finish
      have : ¬(f.onLine AC) := by  -- Omitted by Euclid.
      euclid_intros
      euclid_apply (proposition_5' f e d AC DE FD)
      euclid_apply (proposition_5 a d e b c AB DE AC)
      euclid_finish
      euclid_apply (proposition_8 a d f a e f AB FD AF AC FE AF)
      euclid_finish

.. collapse:: LeanEuclid ``Elements.Book1.proposition_9'`` (22 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply (point_between_points_shorter_than AB a b (a─c)) as d
      euclid_apply (proposition_3 a c a d AC AB) as e
      euclid_apply (line_from_points d e) as DE
      euclid_apply (proposition_1' d e a DE) as f
      euclid_apply (line_from_points f e) as FE
      euclid_apply (line_from_points f d) as FD
      euclid_apply (line_from_points a f) as AF
      use f
      have : ¬(f.onLine AB) := by  -- Omitted by Euclid.
      euclid_intros
      euclid_apply (proposition_5' f d e AB DE FE)
      euclid_apply (proposition_5 a d e b c AB DE AC)
      euclid_finish
      have : ¬(f.onLine AC) := by  -- Omitted by Euclid.
      euclid_intros
      euclid_apply (proposition_5' f e d AC DE FD)
      euclid_apply (proposition_5 a d e b c AB DE AC)
      euclid_finish
      euclid_apply (proposition_8 a d f a e f AB FD AF AC FE AF)
      euclid_apply (intersection_lines AF DE) as g
      euclid_finish

Linked Library Entries
----------------------

Name-matched entries with confidence ≥ 0.7 (lower-confidence token matches are omitted).

.. list-table::
   :header-rows: 1
   :widths: 14 40 12 34

   * - Library
     - Declaration
     - Confidence
     - Evidence
   * - ``geocoq``
     - `angle\_bisector <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Main/Tarski_dev/Ch11_angles.v#L9944>`__
     - 0.7
     - tokens:2
