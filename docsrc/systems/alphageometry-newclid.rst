.. _system-alphageometry:

================================================================
AlphaGeometry, Newclid & Yuclid: Neuro-Symbolic Clause DD + AR
================================================================

* **Repositories**: ``_refs/alphageometry`` (`https://github.com/google-deepmind/alphageometry`, Apache-2.0, :cite:`Trinh2024`) & ``_refs/Newclid`` (`https://github.com/LMCRC/Newclid`, Apache-2.0, :cite:`Sicca2024`)
* **Scale Audited**: `68` construction stanzas (`defs.txt`), `43` Horn rules (`rules.txt`), `30` IMO benchmarks (`imo_ag_30.txt`), plus ``Newclid``'s `88` constructions, `92` rules, GeoGebra `.ggb` loader, and C++20 ``Yuclid`` engine

1. Architecture of ``DD + AR``
------------------------------

:person:`Trieu H. Trinh <trinh>` et al.'s ``AlphaGeometry`` splits Olympiad theorem proving into two halves:

1. **Deterministic Symbolic Closure (`DD + AR`)**: Forward-chaining :term:`Deductive Database` saturation over `43` Horn rules (`dd.py`) interleaved with sparse `Fraction` Gaussian elimination (`ar.py`) across three linear tables:

   * ``AngleTable`` — directed line angles modulo :math:`\pi` (`d(AB) - d(CD)`), making cyclic quadrilateral and parallel-angle chasing linear algebra;
   * ``RatioTable`` — logarithmic segment lengths (`log|AB| - log|CD|`), turning multiplicative ``eqratio`` proportions into linear equations;
   * ``DistanceTable`` — 1D abscissae along collinear lines (`midp`, collinear ``cong``).

2. **Heuristic Auxiliary Synthesis**: Whenever bare ``DD + AR`` saturates without reaching the goal, a transformer language model proposes a single auxiliary construction clause from ``defs.txt`` (`mirror`, `foot`, `circumcenter`, etc.) and re-saturates.

2. Forensic Catch #1: Live Log-Ratio Bug in ``alphageometry/ar.py``
-------------------------------------------------------------------

Auditing ``alphageometry/ar.py`` line-by-line uncovered a **severe mathematical bug** in ``RatioTable.add_const_ratio`` (`lines 425-431, 570-574`):

.. code-block:: python

   # _refs/alphageometry/ar.py:425-431 (LIVE BUG!)
   def add_const_ratio(self, l1: gm.Length, l2: gm.Length, m: float, n: float, deps) -> None:
       # l1 and l2 represent LOGARITHMS of segment lengths (l1 - l2 == log(|s1|/|s2|))!
       # Passing (l1, l2, m, n) to add_eq2 asserts:  m * log|s1| - n * log|s2| == 0,
       # i.e.  |s1|^m == |s2|^n   instead of   |s1| / |s2| == m / n !!
       self.add_eq2(l1, l2, m, n, deps)

``Newclid`` caught and fixed this exact bug in ``deductors/sympy_ar/ar_ratios.py`` by factoring :math:`\log(m) - \log(n)` over integer prime logarithms (verified by ``test_ar_ratio_hallucination``)!

3. Forensic Catch #2: Silent Post-Semicolon Drops in ``defs.txt``
-----------------------------------------------------------------

In ``alphageometry/problem.py:326-331`` and ``graph.py:2697-2705``, construction postconditions on Line 4 of ``defs.txt`` are split by ``;``; any post-semicolon clause lacking an explicit ``x :`` point prefix receives ``points = []`` and is **silently ignored**! This affects `12` stanzas in ``defs.txt``, including ``orthocenter`` (`line 76`), ``incenter`` (`line 88`), ``centroid`` (`line 97`), and ``eq_triangle`` (`line 40`).

4. Forensic Catch #3: Expressiveness Walls of ``DD + AR``
---------------------------------------------------------

Our Rosetta benchmarks pinpoint four sharp ceilings of pure ``DD + AR``:

* **No Additive Squared Lengths in ``AlphaGeometry``**: Because ``RatioTable`` is multiplicative (`log|s|`) and ``DistanceTable`` is 1D collinear, pure ``AlphaGeometry`` **cannot state or prove** :math:`a^2 + b^2 = c^2` (`Pythagoras`), Stewart's theorem, or disjoint-circle radical axes :math:`|PO_1|^2 - |PO_2|^2 = R_1^2 - R_2^2`! ``Newclid``'s C++20 engine ``Yuclid`` solves this by adding a fourth Gaussian table over **squared segment lengths** (`R85_GENERALIZED_PYTHAGORAS`).
* **Missing Hypotenuse–Leg Congruence & ``incenter == excenter`` Mod :math:`\pi`**: ``rules.txt`` (`r00`–`r42`) omits right-triangle HL congruence (added as `R52`/`R53` in ``Newclid``), and because ``eqangle`` operates modulo :math:`\pi`, ``incenter`` (`defs.txt:85`) and ``excenter`` (`defs.txt:121`) have **100% identical synthetic predicates**!
* **The Projective Wall (`Pappus`, `Desargues`, `Harmonic Conjugate`)**: Even though :person:`Pappus <pappus>`'s Hexagon Theorem is a 1-line ``coll`` statement, bare ``DD + AR`` **cannot prove it without auxiliary parallel lines** because `r00`–`r42` lack signed Menelaus/area cancellation—forcing ``Newclid`` to hardcode ``R44_PAPPUS_THEOREM`` and ``R70_PROJECTIVE_HARMONIC_CONJUGATE`` directly into ``all_rules.py`` as primitive axioms!
* **Float64 Numerical Sketch Fragility**: Both ``AlphaGeometry`` (`numericals.py`) and ``Newclid`` (`ATOM = 1e-7` `close_enough` pre-filtering) rely on random floating-point sketches to guard non-degeneracy (`ncoll`, `sameclock`, `sameside`).

5. Takeaway for GEOMETOR
------------------------

Use ``defs.txt``'s 68 clauses (and ``Newclid``'s 88 clauses) as a **functional completeness checklist** for ``geometor.elements`` 2.0, while building an **exact float-free symbolic ``DD + Quadrance/Spread/Area AR`` deductor** over ``geometor.model`` to power ``seer`` and ``divine``.
