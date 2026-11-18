.. _pythagorean:

pythagorean
===========

**pythagorean** · kind: ``theorem`` · family: ``area`` · verification: ``verified``

**Euclid:** ``I.47``

.. admonition:: Statement
   :class: note

   In right-angled triangles the square on the side subtending the right angle is equal to the squares on the sides containing the right angle.

Canonical Form
--------------

.. code-block:: text

   form_triangle(a, b, c, AB, BC, AC) => cong(b, c, b, a)

Exact Witness Figure
--------------------

.. figure:: pythagorean.svg
   :alt: pythagorean
   :align: center

   Exact witness verified (3 points, 2 lines, 0 circles)

Base System Realizations
------------------------

.. list-table::
   :header-rows: 1
   :widths: 16 24 60

   * - System
     - Identifier
     - Statement / Form
   * - :doc:`euclid </foundations/cards/euclid>`
     - ``I.47``
     - I.47
   * - :doc:`leaneuclid </foundations/cards/leaneuclid>`
     - ``Elements.Book1.proposition_47``
     - ∀ (a b c: Point) (AB BC AC : Line), formTriangle a b c AB BC AC ∧ (∠ b:a:c : ℝ) = ∟ → \|(b─c)\| \* \|(b─c)\| = \|(b─a)\| \* \|(b─a)\| + \|(a─c)\| \* \|(a─c)\|
   * - :doc:`newclid </foundations/cards/newclid>`
     - ``R57_PYTHAGORAS_THEOREM``
     - PythagoreanPremises A B C => PythagoreanConclusions A B C

Proof Traces
------------

.. collapse:: LeanEuclid ``Elements.Book1.proposition_47`` (60 steps)

   .. code-block:: lean

      euclid_intros
      euclid_apply (proposition_46' b a c AB) as (f, g, FG, BF, AG)
      euclid_apply (proposition_46' a c b AC) as (h, k, HK, AH, CK)
      euclid_apply (proposition_46' b c a BC) as (d, e, DE, BD, CE)
      have : (∠ a:b:c : ℝ) < ∟ := by
      euclid_apply (proposition_17 c a b AC AB BC)
      euclid_finish
      have : ¬(d.onLine AB) := by
      by_contra
      euclid_apply (proposition_13 c b a d BC AB)
      euclid_finish
      have : (d.sameSide c AB) := by
      euclid_apply (extend_point AB a b) as b'
      euclid_apply (proposition_16 c a b b' AC AB BC)
      euclid_assert (∠ c:b:b' : ℝ) > ∟
      euclid_finish
      have : (∠ a:c:b : ℝ) < ∟ := by
      euclid_apply (proposition_17 b c a BC AC AB)
      euclid_finish
      have : ¬(e.onLine AC) := by
      by_contra
      euclid_apply (proposition_13 b c a e BC AC)
      euclid_finish
      have : (e.sameSide b AC) := by
      euclid_apply (extend_point AC a c) as c'
      euclid_apply (proposition_16 b a c c' AB AC BC)
      euclid_assert (∠ b:c:c' : ℝ) > ∟
      euclid_finish
      euclid_apply (proposition_31 a b d BD) as AL
      euclid_apply (proposition_30 AL CE BD)
      euclid_apply (intersection_lines AL DE) as l
      euclid_apply (intersection_lines AL BC) as l'
      euclid_apply (line_from_points a d) as AD
      euclid_apply (line_from_points f c) as FC
      euclid_apply (proposition_14 b a c g AB AC AG)
      euclid_apply (proposition_14 c a b h AC AB AH)
      euclid_assert ((∠ d:b:a : ℝ) = ∠ f:b:c)
      euclid_assert ((∠ c:b:a : ℝ) + ∟ = ∠ c:b:f)
      euclid_apply (proposition_4 b d a b c f BD AD AB BC FC BF)
      euclid_assert ((Triangle.area △ a:b:d) = Triangle.area △ b:c:f)
      euclid_apply (proposition_41 l' b d l a AL BD BC DE AB AD)
      euclid_apply (proposition_41 g f b a c AG BF FG AB FC BC)
      euclid_assert ((Triangle.area △ g:f:b : ℝ) + (Triangle.area △ g:b:a) = (Triangle.area △ l':b:d) + (Triangle.area △ l':d:l))
      euclid_apply (line_from_points a e) as AE
      euclid_apply (line_from_points b k) as BK
      euclid_apply sum_angles_onlyif c e a b CE AC
      euclid_apply sum_angles_onlyif c k b a CK BC
      euclid_assert ((∠ e:c:a : ℝ) = (∠ k:c:b))
      euclid_apply (proposition_4 c e a c b k CE AE AC BC BK CK)
      euclid_assert ((Triangle.area △ a:c:e : ℝ) = Triangle.area △ c:b:k)
      euclid_apply (proposition_41 l' c e l a AL CE BC DE AC AE)
      euclid_apply (proposition_41 h k c a b AH CK HK AC BK BC)
      euclid_assert ((Triangle.area △ k:c:a : ℝ) + (Triangle.area △ k:a:h) = (Triangle.area △ l':c:e) + (Triangle.area △ l':e:l))
      euclid_apply (rectangle_area b c d e BC DE BD CE)
      euclid_apply (rectangle_area b a f g AB FG BF AG)
      euclid_apply (rectangle_area a c h k AC HK AH CK)
      euclid_apply sum_parallelograms_area b c d e l' l BC DE BD CE
      euclid_apply parallelogram_area b l' d l BC DE BD AL
      euclid_assert ((Triangle.area △ b:d:e : ℝ) + (Triangle.area △ b:e:c) = (Triangle.area △ g:f:b) + (Triangle.area △ g:b:a) + (Triangle.area △ k:c:a) + (Triangle.area △ k:a:h))
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
     - `proposition\_47 <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Elements/OriginalProofs/proposition_47.v#L10>`__
     - 1.0
     - euclid\_ref:proposition\_47
