.. role:: raw-html(raw)
   :format: html

.. _showcase-thales_semicircle:

III.31 · Angle in a semicircle
==============================

.. admonition:: Statement
   :class: note

   An angle inscribed in a semicircle is a right angle.

**Why this theorem:** A theorem in one system is an axiom in another: in GeoCoq's neutral geometry, Thales' statement is one of the equivalent forms of the parallel postulate.

.. graphviz::
   :align: center
   :alt: Angle in a semicircle realizations

   digraph showcase_thales_semicircle {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, ranksep=0.8];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     thm [label="III.31  Angle in a semicircle", shape=ellipse, style=filled, fillcolor="#ffffff", penwidth=1.6];
     r0 [label=<<b>Euclid</b><br/><font point-size="9">Elements III.31<br/><i>prose</i></font>>, fillcolor="#e8d9b5", URL="../foundations/cards/euclid.html", target="_top", tooltip="Depends on I.32 (angle sum), hence on the parallel postulate."];
     thm -> r0 [style=solid];
     r1 [label=<<b>GeoCoq</b><br/><font point-size="9">thales_postulate<br/><i>axiom</i></font>>, fillcolor="#f4d58d", URL="../foundations/cards/geocoq.html", target="_top", tooltip="Proved equivalent to Euclid's fifth postulate over neutral geometry — a postulate, not a lemma."];
     thm -> r1 [style=solid];
     r2 [label=<<b>mathlib4</b><br/><font point-size="9">EuclideanGeometry.Sphere.angle_…<br/><i>theorem</i></font>>, fillcolor="#9fd8a8", URL="../foundations/cards/mathlib4.html", target="_top", tooltip="Iff form, any dimension; proved from the inner product."];
     thm -> r2 [style=solid];
     r3 [label=<<b>AlphaGeometry</b><br/><font point-size="9">rules.txt r20<br/><i>rule</i></font>>, fillcolor="#f6b26b", URL="../foundations/cards/alphageometry.html", target="_top", tooltip="An assumed inference rule."];
     thm -> r3 [style=solid];
     r4 [label=<<b>Newclid</b><br/><font point-size="9">R20_DIAMETER_IS_HYPOTENUSE<br/><i>rule</i></font>>, fillcolor="#f6b26b", URL="../foundations/cards/newclid.html", target="_top", tooltip="Inherited from AlphaGeometry r20."];
     thm -> r4 [style=solid];
     r5 [label=<<b>LeanEuclid</b><br/><font point-size="9">—<br/><i>absent</i></font>>, fillcolor="#dddddd", URL="../foundations/cards/leaneuclid.html", target="_top", tooltip="LeanEuclid formalizes Book I only; III.31 is outside its benchmark."];
     thm -> r5 [style=dashed];
     r6 [label=<<b>geometor.model</b><br/><font point-size="9">verify._build_thales_semicircle<br/><i>witness</i></font>>, fillcolor="#9cc3f0", URL="../foundations/cards/geometor_model.html", target="_top", tooltip="Exact check on the 3-4-5 point of the radius-5 circle (L1)."];
     thm -> r6 [style=solid];
   }

Realizations
------------

.. container:: codes-tabs

   .. container:: codes-tab status-prose

      .. rubric:: Euclid

      :raw-html:`<span class="codes-status" style="background:#e8d9b5">prose</span>` ``Elements III.31`` — :doc:`Euclid card </foundations/cards/euclid>`

      .. code-block:: text

         In a circle the angle in the semicircle is right, that in a greater segment less than
         a right angle, and that in a less segment greater than a right angle; ...

      Depends on I.32 (angle sum), hence on the parallel postulate.

      Source: ``euclid/resources/heath/enunciations.json``

   .. container:: codes-tab status-axiom

      .. rubric:: GeoCoq

      :raw-html:`<span class="codes-status" style="background:#f4d58d">axiom</span>` ``thales_postulate`` — :doc:`GeoCoq card </foundations/cards/geocoq>`

      .. code-block:: coq

         Definition thales_postulate := forall A B C M,
           Midpoint M A B -> Cong M A M C -> Per A C B.

      Proved equivalent to Euclid's fifth postulate over neutral geometry — a postulate, not a lemma.

      Source: `parallel\_postulates.v#L198-L199 <https://github.com/GeoCoq/GeoCoq/blob/87e8f9c3bc9cb2f782b86153bcf8d5bac52d7ef6/theories/Axioms/parallel_postulates.v#L198-L199>`__

   .. container:: codes-tab status-theorem

      .. rubric:: mathlib4

      :raw-html:`<span class="codes-status" style="background:#9fd8a8">theorem</span>` ``EuclideanGeometry.Sphere.angle_eq_pi_div_two_iff_mem_sphere_of_isDiameter`` — :doc:`mathlib4 card </foundations/cards/mathlib4>`

      .. code-block:: lean

         /-- **Thales' theorem**: The angle inscribed in a semicircle is a right angle. -/
         theorem angle_eq_pi_div_two_iff_mem_sphere_of_isDiameter {p₁ p₂ p₃ : P} {s : Sphere P}
             (hd : s.IsDiameter p₁ p₃) :
             ∠ p₁ p₂ p₃ = π / 2 ↔ p₂ ∈ s := by

      Iff form, any dimension; proved from the inner product.

      Source: `Sphere.lean#L78-L81 <https://github.com/leanprover-community/mathlib4/blob/b97762998b0ee14aea85f37006d06dfff25a6afa/Mathlib/Geometry/Euclidean/Angle/Sphere.lean#L78-L81>`__

   .. container:: codes-tab status-rule

      .. rubric:: AlphaGeometry

      :raw-html:`<span class="codes-status" style="background:#f6b26b">rule</span>` ``rules.txt r20`` — :doc:`AlphaGeometry card </foundations/cards/alphageometry>`

      .. code-block:: text

         circle O A B C, coll O A C => perp A B B C

      An assumed inference rule.

      Source: `rules.txt <https://github.com/google-deepmind/alphageometry/blob/6777cb586cbb46beed28db12dc72c69770b68337/rules.txt>`__

   .. container:: codes-tab status-rule

      .. rubric:: Newclid

      :raw-html:`<span class="codes-status" style="background:#f6b26b">rule</span>` ``R20_DIAMETER_IS_HYPOTENUSE`` — :doc:`Newclid card </foundations/cards/newclid>`

      .. code-block:: python

         premises:    circle O A B C, coll O A C
         conclusions: perp A B B C

      Inherited from AlphaGeometry r20.

      Source: `all\_rules.py <https://github.com/LMCRC/Newclid/blob/ac6550732a950564cf7614d605b5bf1eadd29701/newclid/src/newclid/all_rules.py>`__

   .. container:: codes-tab status-absent

      .. rubric:: LeanEuclid

      :raw-html:`<span class="codes-status" style="background:#dddddd">absent</span>` — :doc:`LeanEuclid card </foundations/cards/leaneuclid>`

      LeanEuclid formalizes Book I only; III.31 is outside its benchmark.

   .. container:: codes-tab status-witness

      .. rubric:: geometor.model

      :raw-html:`<span class="codes-status" style="background:#9cc3f0">witness</span>` ``verify._build_thales_semicircle`` — :doc:`geometor.model card </foundations/cards/geometor_model>`

      .. code-block:: python

         O, A, B, P = m.set_point(0, 0), m.set_point(-5, 0), m.set_point(5, 0), m.set_point(3, 4)
         m.assert_collinear(A, O, B, by="Given", label="AB is a diameter")
         m.assert_perpendicular(m.construct_line(A, P), m.construct_line(B, P), by="III.31")

      Exact check on the 3-4-5 point of the radius-5 circle (L1).

      Source: ``codes/src/geometor/codes/verify.py``

Climbing the ladder in GEOMETOR
-------------------------------

**L1 — exact instance.** ``geometor.model`` builds one figure with exact coordinates and checks the conclusion by ``zero_test``: *Exact witness verified (5 points, 2 lines, 1 circles)* (status ``verified``). See the :ref:`witness entry <thales_semicircle>`.

.. figure:: thales_semicircle.svg
   :alt: thales_semicircle
   :align: center
   :width: 70%

**L2 — generic.** Replace the coordinates by free symbols ``r, t``. AB is a diameter of the circle radius r about the origin; P = r((1-t^2)/(1+t^2), 2t/(1+t^2)). The conclusion's numerator reduces to **0**, so the theorem holds for every configuration outside the degenerate set:

- r != 0
- t != 0 (P != B); t finite (P != A)

Computed at build time by :py:func:`geometor.codes.generic.generic_witness`.
