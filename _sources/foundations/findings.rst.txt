.. _foundations-findings:

Findings
========

Results of the source audits behind CODES. Each finding is tied to a file and
line in a pinned clone of the system's repository (see the
:doc:`system cards <cards/index>` for links).

Truth-foundation audit (November 2026)
--------------------------------------

The audit asked one question of every system: *what must be trusted for a
certified statement to be true?*

1. **LeanEuclid's automation rests on an inconsistent axiom.** ``euclid_finish``
   closes goals with ``axiom SMT_VERIF (P : Prop) : P``
   (``SystemE/Meta/Smt/Solver.lean:44-54``). When the solver times out, the goal
   is closed with ``sorry``. The SMT background theory
   (``Meta/Smt/EuclidTheory.lean``) is written by hand, not derived from the
   Lean axioms. Kernel checking therefore covers the rule applications but not
   the premises the oracle discharges, which places LeanEuclid at **L3** on the
   :ref:`Truth Ladder <foundations-index>`, not L4.
2. **mathlib4 is the only surveyed system with no geometric axioms.**
   ``Geometry/Euclidean`` and ``LinearAlgebra/AffineSpace`` contain no ``axiom``,
   ``sorry``, or ``native_decide``. Geometry is defined from real inner-product
   spaces (**L5**).
3. **GeoCoq makes its axioms explicit as type-class hypotheses.** Every theorem
   is relative to its class: Tarski, Hilbert, or Euclid/Beeson. The classes are
   proved to interpret one another and to hold over any real closed field.
4. **The rule engines decide their side conditions numerically.**
   AlphaGeometry decides ``ncoll``, ``npara``, ``nperp`` and ``sameside`` on a
   random float diagram (``dd.py:864-892``) and resamples it until the goal holds
   (``graph.py:500-523``). Newclid checks every predicate numerically first, with
   ``REL_TOL = 0.001``.
5. **geometor.model is exact on almost every path, with one numeric acceptance
   branch.** ``zero_test`` (``algebra.py:160-253``) decides by exact expansion,
   ℚ(φ)/ℚ(√φ) field arithmetic, and ``minimal_polynomial``. For large constant
   expressions, however, it accepts ``|evalf(80)| < 1e-65`` as zero
   (``algebra.py:247-251``). This is a candidate for a strict mode in
   ``geometor.model``.
6. **CindyJS's "prover" is randomized.** It guesses incidences within ``1e-6``,
   perturbs the free elements three times, and keeps the conjectures that survive
   (``libgeo/Prover.js``). This places it at **L0**.
7. **An exact instance becomes a generic proof once the coordinates are free.**
   The :doc:`showcase </showcase/index>` lifts four ``geometor.model`` witnesses
   (I.5, I.47, III.31, Simson) from L1 to L2. Each uses free symbolic
   parameters, and its conclusion polynomial reduces exactly to zero. Pasch
   cannot be lifted this way: it is a statement about order, which needs an
   ordered field.

Headline forensic discoveries (2025 survey)
-------------------------------------------

1. **Unverified Trust Oracle & Six Missing Lemmas in LeanEuclid**: ``LeanEuclid`` (:cite:`Murphy2024`) faithfully separates constructive steps (``euclid_apply``) from diagrammatic topology, and its 7 rules in ``Intersections.lean`` correspond 1-to-1 with ``geometor.model.intersect``'s selectors (``side_of``, ``between``, ``beyond``). Yet source inspection of ``SystemE/Meta/Smt/Solver.lean:44-55`` reveals that ``euclid_finish`` closes goals via ``private axiom SMT_VERIF (P : Prop) : P`` without reconstructing proof terms in the Lean 4 kernel, while ``Book/Prop47.lean:25-60`` isolates **six topological square-orientation lemmas missed by Euclid** in the Bride's Chair proof.
2. **Metatheoretic Gold & Classical Gaps in GeoCoq**: Across `481` Coq files and `4,671` kernel-checked lemmas (:cite:`Boutry2019`), ``GeoCoq`` proves bidirectional equivalences between Tarski, Hilbert, and Euclid, **34 equivalent parallel postulates**, neutral-geometry midpoint existence *without circles*, and an explicit proof of ``False`` when non-collinearity is omitted from cut-and-paste area axioms—yet omits the Nine-Point Circle ``X(5)``, Steiner circle power, radical axes, circle inversion, pole–polar reciprocity, conics, and the golden ratio.
3. **Dimension-Polymorphic Elegance vs. Noncomputable Projective Gaps in Mathlib4**: ``Mathlib/Geometry/Euclidean/`` (:cite:`Mathlib2020`) generalizes the orthocenter (``mongePoint``), the :math:`3(n+1)`-point Feuerbach sphere, ``Sphere.power``, ``inversion``, and 1-line La Hire pole–polar reciprocity to arbitrary dimension :math:`n`—yet is pervasively ``noncomputable``, lacks a constructive ``Euclid I.1`` theorem, documents a 20-line cyclic-order ``TODO`` in ``Sphere/Ptolemy.lean:22-41``, and contains **zero** ``radicalAxis``, ``crossRatio``, ``Menelaus``, ``Pappus``, or ``Desargues``.
4. **Log-Ratio Bug & Expressiveness Walls in AlphaGeometry / Newclid**: Source audit of ``alphageometry/ar.py:425-431, 570-574`` (:cite:`Trinh2024`) uncovers a live bug where ``RatioTable.add_const_ratio`` encodes :math:`m \log|s_1| - n \log|s_2| = 0` (:math:`|s_1|^m = |s_2|^n` instead of :math:`|s_1|/|s_2| = m/n`), alongside silent drops of unprefixed post-``;`` clauses in 12 ``defs.txt`` stanzas. Architecturally, pure ``DD+AR`` cannot state :math:`a^2 + b^2 = c^2` or disjoint radical axes (fixed in C++ ``Yuclid``'s squared-length AR) and **cannot prove Pappus or Desargues without auxiliary parallel lines** (forcing ``Newclid`` to hardcode ``R44_PAPPUS_THEOREM`` and ``R70_PROJECTIVE_HARMONIC_CONJUGATE`` as axioms).
5. **The Unfinished Area Method in JGEX**: :person:`Shang-Ching Chou <chou>`, :person:`Xiao-Shan Gao <gao>`, and :person:`Jing-Zhong Zhang <zhang>`'s coordinate-free :term:`Area Method` (:cite:`ChouGaoZhang1994`) proves Pythagoras in 0 steps (``P_BAC = 0`` by definition), Orthocenter in 0 steps (Jacobi identity), and Pappus/La Hire/Cross-Ratio with zero auxiliary points—yet in ``Java-Geometry-Expert``'s Java codebase, ``Area.java`` (`213` lines) is an unfinished port whose GUI tab is commented out in ``PanelProve.java:112-116`` (``TODO: Implement the area method``).
6. **Clifford Dual Traps in GAlgebra vs. Conformal Triumphs in Kingdon**: ``galgebra`` crashes with ``AttributeError`` on ``.dual()`` for every degenerate :term:`Projective Geometric Algebra` (:math:`I^2 = 0`), omits the regressive join ``&``, and overloads ``>>`` as a commutator rather than a sandwich product. By contrast, ``kingdon`` compiles exact SymPy polynomial blades where 2D CGA circle power is ``-2*(kappa | P)``, radical axis is ``kappa1 - kappa2``, circumcenter is ``C * ni * ~C``, and circle inversion is ``C >> P``.
7. **Live Symbolic Bugs in SymPy Geometry (`1.14.0`)**: Source inspection of ``sympy/geometry/`` reveals (a) a **double live bug in ``Triangle.excenters``** (`polygon.py:2714-2726`: missing numerator parentheses ``-a*x[0] + b*x[1] + c*x[2]/(-a+b+c)`` *plus* wrong side-vertex pairing) and (b) a **2-digit float zero-test bug in ``Point.affine_rank``** (`point.py:331-335`: ``abs(x.n(2)) < 1e-12``) causing exact rational non-collinear points to falsely test collinear, alongside ``solve()`` bottlenecks and missing ``Hyperbola``, ``inversion``, ``radical_axis``, ``polar``, and ``cross_ratio``.
8. **Byrne's Pointer-Free Visual Pseudocode & The Universal Golden Blind Spot**: Across ``LeanEuclid``, ``GeoCoq``, ``mathlib4`` Geometry, ``AlphaGeometry``, and ``Newclid``, the **Golden Ratio** (:math:`\phi`) and **Book XIII Platonic Solids** have **zero** geometric coverage. Remarkably, :person:`Oliver Byrne <byrne>`'s 1847 *Coloured Euclid* (:cite:`Byrne1847`; revived interactively by :person:`Nicholas Rougeux <rougeux>`, :cite:`Rougeux2018`) not only pioneered pointer-free visual pseudocode (`Given` / `To Prove` / `Construction` / `Proof` with inline chromatic value-tokens), it also formalized Book II gnomons, Book III circle power, Book IV pentagons, and Book VI golden-ratio cuts—directly inspiring GEOMETOR's synthesis of exact symbolic identifiers with interactive visual tokens.
