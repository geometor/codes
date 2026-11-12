.. _system-leaneuclid:

==============================
LeanEuclid & Formal System E
==============================

* **Repository**: ``_refs/LeanEuclid`` (`https://github.com/loganrjmurphy/LeanEuclid`, MIT, :cite:`Murphy2024`)
* **Scale Audited**: `235` ``.lean`` files, `206` theorems, `108` axioms (`SystemE/`, `Book/Prop01.lean`–`Prop48.lean`, `UniGeo/`)
* **Mathematical Foundation**: :person:`Jeremy Avigad <avigad>`, Edward Dean, and John Mumma's :term:`Formal System E` (:cite:`AvigadDeanMumma2009`)

1. Ontological & Deductive Architecture
---------------------------------------

For two centuries after Pasch and :person:`David Hilbert <hilbert>`, logicians treated :person:`Euclid <euclid>`'s reliance on diagrams—such as assuming in `Book I, Proposition 1` that two congruent circles intersect—as a logical flaw. Avigad, Dean, and Mumma (`2009`) overturned that verdict: Euclid's diagrammatic inferences are governed by a **decidable, purely topological algebra of plane separation** that can be separated cleanly from explicit ruler-and-compass constructions and linear magnitude equations.

``LeanEuclid`` embeds Formal System E into Lean 4 across three distinct axiom strata (`SystemE/Theory/`):

1. **Six Primitive Sorts** (`Point`, `Line`, `Circle`, `Segment`, `Angle`, `Triangle`) + **30 Construction Rules** (`Constructions/Points.lean`, `Lines.lean`, `Circles.lean`, `Intersections.lean`) invoked explicitly by the user via ``euclid_apply (...) as x``.
2. **36 Diagrammatic / Topological Axioms** (`Axioms/Diagrammatic.lean`): strict collinear ``between a b c``, half-plane ``a.sameSide b L`` / ``a.opposingSides b L``, and circle containment ``a.insideCircle α`` / ``a.outsideCircle α``.
3. **35 Metric & Transfer Axioms** (`Relations.lean`, `Axioms/Metric.lean`): mapping geometric objects to linear real magnitudes ``|(a─b)| : ℝ`` (length), ``∠(a:b:c) : ℝ`` (angle), ``∟ : ℝ`` (right angle), and ``△(a:b:c) : ℝ`` (triangle area)—deliberately avoiding nonlinear trigonometry or coordinate multiplication.

2. Exact Isomorphism with ``geometor.model.intersect``
------------------------------------------------------

Inspecting ``SystemE/Theory/Constructions/Intersections.lean`` reveals a **1-to-1 structural isomorphism** with ``geometor.model.intersect``'s deterministic root selectors:

.. code-block:: lean4

   -- SystemE/Theory/Constructions/Intersections.lean (excerpt)
   axiom intersect_circles_same_side : ∀ (α β : Circle) (c d a b : Point) (AB : Line),
     α.intersectsCircle β ∧ distinctPointsOnLine a b AB ∧ c.isCentre α ∧ a.onLine AB ∧ ... →
     ∃ e : Point, e.onCircle α ∧ e.onCircle β ∧ e.sameSide d AB

Every disambiguated intersection rule (`intersect_circles_same_side`, `intersect_circles_opposing_sides`, `intersect_line_circle_between`, `intersect_line_circle_extending`) corresponds directly to ``geometor.model``'s ``side_of=(A, B, ±1)``, ``between=(A, B)``, and ``beyond=(A, B)``!

3. Forensic Findings: ``SMT_VERIF`` & Six Missed Lemmas in ``Prop47``
---------------------------------------------------------------------

Our source audit uncovered three critical findings that do not appear in high-level summaries:

* **The Unverified Trust Oracle (`SMT_VERIF`)**: When ``euclid_finish`` is called at the end of a proof, ``SystemE/Meta/Smt/Solver.lean:44-55`` translates the context to SMT-LIB2, invokes external Z3/CVC5, and—if the solver returns ``unsat``—closes the Lean goal via an unverified axiom:

  .. code-block:: lean4

     -- SystemE/Meta/Smt/Solver.lean:44-46
     /-- Dangerous! Should only be invoked after verifying unsat from an external solver -/
     private axiom SMT_VERIF (P : Prop) : P

  Consequently, ``#print axioms Book.Prop01.proposition_1`` depends on ``SMT_VERIF`` rather than reconstructing a kernel-checked Lean proof term.
* **Six Topological Lemmas Missed by Euclid (`Book/Prop47.lean:25-60`)**: In formalizing the Bride's Chair proof of the Pythagorean Theorem (`I.47`), ``LeanEuclid`` had to isolate **six auxiliary lemmas explicitly marked ``-- Missed by Euclid``** proving that squares erected *outwardly* on the sides of right triangle :math:`ABC` do not fold across the interior of the triangle and that the altitude parallel splits the hypotenuse square strictly between its vertices.
* **Zero Circles Across ``UniGeo`` (`100` Files)**: Auditing all `100` benchmark files in ``UniGeo/`` (`Congruent`, `Parallel`, `Quadrilateral`, `Similarity`, `Triangle`) reveals **zero occurrences of ``Circle``**—the entire ``UniGeo`` benchmark suite tests rectilinear line/angle/triangle theorems only, and ``LeanEuclid`` stops abruptly after `Book I, Proposition 48`.

4. Takeaway for GEOMETOR
------------------------

By persisting the structured selector tuple (`side_of`, `between`, `beyond`, `on_ray`, `other_than`) on ``geometor.model.Step``, GEOMETOR can emit 1-to-1 ``LeanEuclid`` ``euclid_apply`` construction transcripts automatically—while certifying exact algebraic equality inside SymPy's ``ANP`` fields without relying on ``SMT_VERIF``.
