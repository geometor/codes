.. _system-geocoq:

=========================================================
GeoCoq: Tarski, Hilbert, Euclid & 34 Parallel Postulates
=========================================================

* **Repository**: ``_refs/GeoCoq`` (`https://github.com/GeoCoq/GeoCoq`, LGPL-3.0-only, :cite:`Boutry2019`)
* **Scale Audited**: `481` ``.v`` files, `4,671` ``Lemma``/``Theorem`` proofs, `42` axiomatic ``Class`` strata
* **Mathematical Foundation**: :person:`Alfred Tarski <tarski>`'s first-order geometry (:cite:`Schwabhauser1983`) bridged bidirectionally to :person:`David Hilbert <hilbert>` (:cite:`Hilbert1899`) and :person:`Euclid <euclid>`

1. Tarski's Radical Point-Only Ontology
---------------------------------------

``GeoCoq`` is the monument of foundational rigor in synthetic geometry. Its core (`theories/Axioms/tarski_axioms.v`) strips Euclidean ontology down to **one single type** (``Tpoint : Type``) and **two predicates**:

.. code-block:: coq

   (* theories/Axioms/tarski_axioms.v *)
   Class Tarski_neutral_dimensionless := {
     Tpoint : Type;
     Bet : Tpoint -> Tpoint -> Tpoint -> Prop;
     Cong : Tpoint -> Tpoint -> Tpoint -> Tpoint -> Prop;
     cong_pseudo_reflexivity : forall A B, Cong A B B A;
     cong_inner_transitivity : forall A B C D E F, Cong A B C D -> Cong A B E F -> Cong C D E F;
     cong_identity : forall A B C, Cong A B C C -> A = B;
     segment_construction : forall A B C D, exists E, Bet A B E /\ Cong B E C D;
     five_segment : forall A A' B B' C C' D D', ... -> Cong C D C' D';
     between_identity : forall A B, Bet A B A -> A = B;
     inner_pasch : forall A B C P Q, Bet A P C -> Bet B Q C -> exists X, Bet P X B /\ Bet Q X A;
     ...
   }.

Everything else is a defined macro over points:

* **Collinearity**: ``Col A B C := Bet A B C \/ Bet B C A \/ Bet C A B`` (non-strict: ``Bet A A B`` holds!).
* **Right Angle without Angles**: ``Per A B C := exists C', Midpoint B C C' /\ Cong A C A C'``.
* **SAS Congruence without Angles**: Replaced by Tarski's :term:`Five-Segment Configuration` (``five_segment`` / ``FSC``).
* **Certified Reflection Tactics**: Unlike ``LeanEuclid``'s external SMT oracle, ``GeoCoq``'s ``ColR``, ``CongR``, and ``CoincR`` tactics construct **100% Coq-kernel-checked proof terms** via certified boolean reflection.

2. Unrivaled Metatheoretic Opus
-------------------------------

No other software system in the world comes close to ``GeoCoq``'s metatheoretic breadth (`theories/Main/Meta_theory/`):

* **Axiomatic Bi-Interpretability**: Proves two-way deductive equivalence across Tarski's axioms, Hilbert's five axiom groups (`hilbert_axioms.v`), and System-E-style Euclidean postulates (`Elements/OriginalProofs/`, covering all 48 Book I propositions).
* **34 Equivalent Parallel Postulates (`parallel_postulates.v`)**: Proves mutual equivalence over neutral geometry of 34 historical formulations—Playfair, Proclus, Posidonius equidistant lines, triangle angle sum, Wallis similarity, Saccheri/Lambert right rectangles, circumcircle existence for every non-collinear triple, and Bachmann's Lotensatz.
* **Neutral Midpoint Existence Without Circles (`Ch08_orthogonality.v`)**: Using Gupta's construction, ``midpoint_existence`` constructs the midpoint of ``A B`` in pure neutral geometry *without* circle–circle continuity (working over Pythagorean fields smaller than Euclidean fields!).
* **Cut-and-Paste Area Inconsistency Catch (`euclidean_area_axioms.v`)**: Explicitly proves ``area_inconsistent : False`` when the non-collinearity guard is omitted from cut-and-paste area decomposition!
* **Synthetic Field Arithmetic (`Ch13`–`Ch16`)**: Proves affine parallel Pappus (`Ch13_5_Pappus_Pascal.v`) and Desargues (`Ch13_6_Desargues_Hessenberg.v`) to establish commutativity and associativity of geometric segment multiplication on a line, culminating in full coordinatization over an ordered Euclidean field.

3. Classical & Constructive Blind Spots
---------------------------------------

Because every line and circle must be unpacked into point quantifiers, ``GeoCoq`` slows dramatically once geometry moves past Book I and affine coordinatization:

* ``Main/Highschool/`` covers ``incenter.v``, ``centroid.v``, ``circumcenter.v``, ``orthocenter.v``, and ``euler_line.v`` (collinearity only, omitting the :math:`2:1` ratio), **stopping short of Feuerbach's Nine-Point Circle (`X(5)`)**.
* **Zero coverage** across all `481` files of Steiner circle power, radical axes, circle inversion, pole–polar reciprocity, general conics, projective cross-ratios, the **Golden Ratio (:math:`\phi`)**, regular pentagons, or Platonic solids.

4. Takeaway for GEOMETOR
------------------------

``GeoCoq`` teaches GEOMETOR to record the **minimal axiomatic stratum** of each theorem (`neutral`, `parallel`, `circle-continuity`) while confirming why a practical discovery and publishing engine must keep lines, circles, conics, and algebraic coordinates as first-class citizens.
