.. role:: raw-html(raw)
   :format: html

.. _cards-index:

System Cards
============

One card per system, all with the same template: the seven-layer trust chain, comparison axes, a real statement in the system's own language, findings from source audits, and references.

.. list-table::
   :header-rows: 1
   :widths: 16 9 16 59

   * - System
     - Level
     - Trusted core
     - Why believe it?
   * - :doc:`Euclid <euclid>`
     - :raw-html:`<span class="codes-status" style="background:#e8d9b5">H</span>`
     - Human readers
     - Believe it because it follows, step by step, from five postulates and five common notions — as checked by readers, with the diagram doing silent work.
   * - :doc:`mathlib4 <mathlib4>`
     - :raw-html:`<span class="codes-status" style="background:#c5b3e6">L5</span>`
     - Lean 4 kernel
     - Believe it because geometry is defined from real inner-product spaces and every theorem is a kernel-checked consequence of Lean's logic alone.
   * - :doc:`GeoCoq <geocoq>`
     - :raw-html:`<span class="codes-status" style="background:#9fd8a8">L4</span>`
     - Coq kernel
     - Believe it because the Coq kernel checked it from Tarski's (or Hilbert's, or Euclid's) axioms — and GeoCoq proves those axiom systems interpret one another and hold in ℝ².
   * - :doc:`AlphaGeometry <alphageometry>`
     - :raw-html:`<span class="codes-status" style="background:#f6b26b">L3</span>`
     - AG DD+AR engine, Numeric diagram
     - Believe it because a deduction engine derived it from 43 assumed rules — with side conditions (non-collinear, same side) read off a random numeric diagram.
   * - :doc:`LeanEuclid <leaneuclid>`
     - :raw-html:`<span class="codes-status" style="background:#f6b26b">L3</span>`
     - Lean 4 kernel, SMT\_VERIF oracle
     - Believe it because Lean's kernel checked every rule application from System E's axioms — except that premise-discharging steps are admitted by an SMT oracle axiom.
   * - :doc:`Newclid <newclid>`
     - :raw-html:`<span class="codes-status" style="background:#f6b26b">L3</span>`
     - Newclid DDARN, SymPy simplification, Numeric diagram
     - Believe it because the DDARN engine derived it from a curated rule set descended from AlphaGeometry — again with numerically checked side conditions.
   * - :doc:`JGEX <jgex>`
     - :raw-html:`<span class="codes-status" style="background:#7fd1c7">L2</span>`
     - JGEX gprover
     - Believe it because the hypothesis polynomials reduce the conclusion to zero (Wu / Gröbner) — true generically, provided the printed non-degeneracy conditions hold.
   * - :doc:`galgebra <galgebra>`
     - :raw-html:`<span class="codes-status" style="background:#7fd1c7">L2</span>`
     - GA product engines, SymPy simplification
     - Believe it because the multivector difference simplifies to zero for an arbitrary (possibly symbolic) metric — as far as SymPy's simplify can tell.
   * - :doc:`kingdon <kingdon>`
     - :raw-html:`<span class="codes-status" style="background:#7fd1c7">L2</span>`
     - GA product engines, SymPy simplification
     - Believe it because the identity expands to zero in the Clifford algebra — universally, when computed symbolically without division.
   * - :doc:`geometor.model <geometor_model>`
     - :raw-html:`<span class="codes-status" style="background:#9cc3f0">L1</span>`
     - model zero\_test, SymPy simplification
     - Believe it because the figure is built exactly — algebraic coordinates from ruler-and-compass intersections — and every asserted relation reduces to zero.
   * - :doc:`SymPy <sympy>`
     - :raw-html:`<span class="codes-status" style="background:#9cc3f0">L1</span>`
     - SymPy simplification
     - Believe it because exact arithmetic on concrete coordinates evaluates the predicate to True — subject to SymPy's simplification heuristics.
   * - :doc:`CindyJS <cindyjs>`
     - :raw-html:`<span class="codes-status" style="background:#dcdcdc">L0</span>`
     - IEEE-754 floats
     - Believe it because it keeps looking true while you drag — floating-point projective geometry with randomized conjecture checks, and no proof.

.. toctree::
   :hidden:

   euclid
   mathlib4
   geocoq
   alphageometry
   leaneuclid
   newclid
   jgex
   galgebra
   kingdon
   geometor_model
   sympy
   cindyjs
