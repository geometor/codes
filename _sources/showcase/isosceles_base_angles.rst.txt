.. role:: raw-html(raw)
   :format: html

.. _showcase-isosceles_base_angles:

I.5 · Pons asinorum
===================

.. admonition:: Statement
   :class: note

   In an isosceles triangle the angles at the base are equal.

**Why this theorem:** Every system can say it, so it is the clean baseline. The differences are entirely in *why* each system believes it: a proof, a rule, a junk-value convention, or an exact figure.

.. graphviz::
   :align: center
   :alt: Pons asinorum realizations

   digraph showcase_isosceles_base_angles {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, ranksep=0.8];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     thm [label="I.5  Pons asinorum", shape=ellipse, style=filled, fillcolor="#ffffff", penwidth=1.6];
     r0 [label=<<b>Euclid</b><br/><font point-size="9">Elements I.5<br/><i>prose</i></font>>, fillcolor="#e8d9b5", URL="../foundations/cards/euclid.html", target="_top", tooltip="Proved from I.4 (SAS) on the produced sides; checked by readers, relies on the diagram for order facts."];
     thm -> r0 [style=solid];
     r1 [label=<<b>LeanEuclid</b><br/><font point-size="9">proposition_5<br/><i>theorem</i></font>>, fillcolor="#9fd8a8", URL="../foundations/cards/leaneuclid.html", target="_top", tooltip="Kernel checks each euclid_apply rule step, but premises are discharged by euclid_finish → SMT_VERIF (an unsound oracle axiom)."];
     thm -> r1 [style=solid];
     r2 [label=<<b>GeoCoq</b><br/><font point-size="9">proposition_05<br/><i>theorem</i></font>>, fillcolor="#9fd8a8", URL="../foundations/cards/geocoq.html", target="_top", tooltip="Kernel-checked from the Beeson-style Euclid axiom class (via proposition_04), relative to the class hypotheses."];
     thm -> r2 [style=solid];
     r3 [label=<<b>mathlib4</b><br/><font point-size="9">EuclideanGeometry.angle_eq_angl…<br/><i>theorem</i></font>>, fillcolor="#9fd8a8", URL="../foundations/cards/mathlib4.html", target="_top", tooltip="No geometric axioms and no distinctness hypothesis: degenerate angles take the junk value π/2, so the degenerate cases hold by convention."];
     thm -> r3 [style=solid];
     r4 [label=<<b>AlphaGeometry</b><br/><font point-size="9">rules.txt r13<br/><i>rule</i></font>>, fillcolor="#f6b26b", URL="../foundations/cards/alphageometry.html", target="_top", tooltip="Not proved: it is one of the 43 inference rules the DD engine assumes."];
     thm -> r4 [style=solid];
     r5 [label=<<b>Newclid</b><br/><font point-size="9">R13_ISOSCELES_TRIANGLE_EQUAL_AN…<br/><i>rule</i></font>>, fillcolor="#f6b26b", URL="../foundations/cards/newclid.html", target="_top", tooltip="Inherited verbatim from AlphaGeometry r13."];
     thm -> r5 [style=solid];
     r6 [label=<<b>geometor.model</b><br/><font point-size="9">verify._build_isosceles_base_an…<br/><i>witness</i></font>>, fillcolor="#9cc3f0", URL="../foundations/cards/geometor_model.html", target="_top", tooltip="Exact zero-test on one concrete figure (L1). The generic witness below lifts it to L2."];
     thm -> r6 [style=solid];
   }

Realizations
------------

.. container:: codes-tabs

   .. container:: codes-tab status-prose

      .. rubric:: Euclid

      :raw-html:`<span class="codes-status" style="background:#e8d9b5">prose</span>` ``Elements I.5`` — :doc:`Euclid card </foundations/cards/euclid>`

      .. code-block:: text

         In isosceles triangles the angles at the base are equal to one another, and, if the
         equal straight lines be produced further, the angles under the base will be equal to
         one another.

      Proved from I.4 (SAS) on the produced sides; checked by readers, relies on the diagram for order facts.

      Source: ``euclid/resources/heath/enunciations.json``

   .. container:: codes-tab status-theorem

      .. rubric:: LeanEuclid

      :raw-html:`<span class="codes-status" style="background:#9fd8a8">theorem</span>` ``proposition_5`` — :doc:`LeanEuclid card </foundations/cards/leaneuclid>`

      .. code-block:: lean

         theorem proposition_5 : ∀ (a b c d e : Point) (AB BC AC : Line),
           formTriangle a b c AB BC AC ∧ (|(a─b)| = |(a─c)|) ∧
           (between a b d) ∧ (between a c e) →
           (∠ a:b:c = ∠ a:c:b) ∧ (∠ c:b:d = ∠ b:c:e) :=

      Kernel checks each euclid\_apply rule step, but premises are discharged by euclid\_finish → SMT\_VERIF (an unsound oracle axiom).

      Source: `Prop05.lean#L7-L10 <https://github.com/loganrjmurphy/LeanEuclid/blob/33a72c0fa83914202532998a2e7b8771295c3cc7/Book/Prop05.lean#L7-L10>`__

   .. container:: codes-tab status-theorem

      .. rubric:: GeoCoq

      :raw-html:`<span class="codes-status" style="background:#9fd8a8">theorem</span>` ``proposition_05`` — :doc:`GeoCoq card </foundations/cards/geocoq>`

      .. code-block:: coq

         Context `{Ax:euclidean_neutral_ruler_compass}.

         Lemma proposition_05 :
            forall A B C,
            isosceles A B C ->
            CongA A B C A C B.

      Kernel-checked from the Beeson-style Euclid axiom class (via proposition\_04), relative to the class hypotheses.

      Source: `proposition\_05.v#L6-L11 <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Elements/OriginalProofs/proposition_05.v#L6-L11>`__

   .. container:: codes-tab status-theorem

      .. rubric:: mathlib4

      :raw-html:`<span class="codes-status" style="background:#9fd8a8">theorem</span>` ``EuclideanGeometry.angle_eq_angle_of_dist_eq`` — :doc:`mathlib4 card </foundations/cards/mathlib4>`

      .. code-block:: lean

         /-- **Isosceles Triangle Theorem**: Pons asinorum, angle-at-point form. -/
         theorem angle_eq_angle_of_dist_eq {p₁ p₂ p₃ : P} (h : dist p₁ p₂ = dist p₁ p₃) :
             ∠ p₁ p₂ p₃ = ∠ p₁ p₃ p₂ := by

      No geometric axioms and no distinctness hypothesis: degenerate angles take the junk value π/2, so the degenerate cases hold by convention.

      Source: `Triangle.lean#L280-L282 <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Triangle.lean#L280-L282>`__

   .. container:: codes-tab status-rule

      .. rubric:: AlphaGeometry

      :raw-html:`<span class="codes-status" style="background:#f6b26b">rule</span>` ``rules.txt r13`` — :doc:`AlphaGeometry card </foundations/cards/alphageometry>`

      .. code-block:: text

         cong O A O B, ncoll O A B => eqangle O A A B A B O B

      Not proved: it is one of the 43 inference rules the DD engine assumes.

      Source: `rules.txt <https://github.com/google-deepmind/alphageometry/blob/6777cb586cbb46beed28db12dc72c69770b68337/rules.txt>`__

   .. container:: codes-tab status-rule

      .. rubric:: Newclid

      :raw-html:`<span class="codes-status" style="background:#f6b26b">rule</span>` ``R13_ISOSCELES_TRIANGLE_EQUAL_ANGLES`` — :doc:`Newclid card </foundations/cards/newclid>`

      .. code-block:: python

         premises:    cong O A O B, ncoll O A B
         conclusions: eqangle O A A B A B O B

      Inherited verbatim from AlphaGeometry r13.

      Source: `all\_rules.py <https://github.com/LMCRC/Newclid/blob/ac6550732a950564cf7614d605b5bf1eadd29701/newclid/src/newclid/all_rules.py>`__

   .. container:: codes-tab status-witness

      .. rubric:: geometor.model

      :raw-html:`<span class="codes-status" style="background:#9cc3f0">witness</span>` ``verify._build_isosceles_base_angles`` — :doc:`geometor.model card </foundations/cards/geometor_model>`

      .. code-block:: python

         A = m.set_point(2, 3, label="A")
         B = m.set_point(0, 0, label="B")
         C = m.set_point(4, 0, label="C")
         m.assert_equal((A, B), (A, C), by="Given", label="AB = AC")
         m.assert_spread_equal((A, B, C), (A, C, B), by="I.5", label="angle B = angle C")

      Exact zero-test on one concrete figure (L1). The generic witness below lifts it to L2.

      Source: ``codes/src/geometor/codes/verify.py``

Climbing the ladder in GEOMETOR
-------------------------------

**L1 — exact instance.** ``geometor.model`` builds one figure with exact coordinates and checks the conclusion by ``zero_test``: *Exact witness verified (3 points, 0 lines, 0 circles)* (status ``verified``). See the :ref:`witness entry <isosceles_base_angles>`.

.. figure:: isosceles_base_angles.svg
   :alt: isosceles_base_angles
   :align: center
   :width: 70%

**L2 — generic.** Replace the coordinates by free symbols ``u, v``. AB = AC is built in: A lies on the perpendicular bisector x = u of BC. The conclusion's numerator reduces to **0**, so the theorem holds for every configuration outside the degenerate set:

- u != 0 (B != C)
- v != 0 (A not on BC)

Computed at build time by :py:func:`geometor.codes.generic.generic_witness`.
