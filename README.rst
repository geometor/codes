==============
GEOMETOR Codes
==============

*A Comparative Study of Formal Languages, Visual Pseudocodes, Symbolic Architectures, Syntax, and Canon ("Opus") Across Geometric Logic — and How They Inform GEOMETOR.*

``geometor-codes`` sits at **Layer 2** of the 33-repository **GEOMETOR** ecosystem, bridging the primary historical and philosophical codices (Euclid, Byrne, Proclus, Aristotle, Aquinas, Hoenen, Hilbert, Pacioli, Kepler, Apollonius, Archimedes, Lemoine) to GEOMETOR's exact symbolic software stack (``geometor.model``, ``geometor.elements``, ``geometor.wildberger``, ``geometor.pappus``, ``geometor.etc``, ``geometor.divine``, and ``geometor.seer``).

Systems Surveyed (11 Formal, Visual & Symbolic Architectures)
-------------------------------------------------------------

1. **LeanEuclid & Formal System E** (``leaneuclid``) — Avigad–Dean–Mumma diagrammatic axioms in Lean 4 + Z3/CVC5 SMT (``Book/Prop01``–``Prop48`` + ``UniGeo``).
2. **GeoCoq** (``geocoq``) — Tarski point-only synthetic axiomatics (``Bet``, ``Cong``), Hilbert & Euclid bi-interpretability, and 34 parallel postulates in Coq/Rocq.
3. **Lean 4 Mathlib** (``mathlib4``) — Dependent type-theoretic affine vector torsors (``NormedAddTorsor V P``) over :math:`n`-dimensional inner-product spaces.
4. **AlphaGeometry** (``alphageometry``) — Neuro-symbolic clause DSL (``defs.txt``, ``rules.txt``) with Deductive Database + Algebraic Reasoning (``DD + AR``).
5. **Newclid & Yuclid** (``newclid``) — Modular Python/SymPy + C++20 neuro-symbolic ``DD + AR`` fixing log-ratio bugs and adding squared-length Gaussian tables.
6. **Java Geometry Expert** (``jgex``) — Five-engine prover pioneering GDD, Full-Angle, Chou–Gao–Zhang's coordinate-free **Area Method** (``r``, ``S_ABC``, ``P_ABC``), Wu's Characteristic Sets, and Gröbner Bases.
7. **Projective & Conformal Geometric Algebra** (``pga_cga``) — Plane-based 2D PGA :math:`\mathbb{R}_{2,0,1}^*` and 2D Conformal GA :math:`\mathbb{R}_{3,1}` in ``kingdon`` and ``galgebra``.
8. **CindyJS** (``cindyjs``) — Complex projective homogeneous :math:`\mathbb{CP}^2`, Cayley–Klein circular points :math:`I, J`, Riemann-surface homotopy tracing, and PSLQ recovery.
9. **SymPy Geometry** (``sympy_geometry``) — Object-oriented affine Cartesian symbolic CAS (``sympy.geometry`` 1.14.0), audited down to exact solver bottlenecks and live bugs.
10. **Oliver Byrne's Coloured Euclid (1847 / Rougeux)** (``byrne_1847``) — The first pointer-free chromatic visual pseudocode for formal geometry (Books I–VI; revived interactively at ``c82.net/euclid``).
11. **GEOMETOR** (``geometor_model``) — Targeted constructive symbolic DAGs (``Model(..., auto_intersect=False)``), exact ``ANP`` number fields, Rational Trigonometry invariants, and bidirectional ``:g:`` :math:`\leftrightarrow` ``.euclid-graphic`` SVGs.

Installation & CLI Usage
------------------------

Managed with ``uv`` targeting Python 3.13:

.. code-block:: bash

   # Summarize all 11 surveyed systems
   python -m geometor.codes summary

   # Decode any formal symbol, binder, tactic, blade operator, or Byrne token
   python -m geometor.codes decode "-ᵥ"
   python -m geometor.codes decode "eqangle"
   python -m geometor.codes decode "::"

   # Inspect the 69-topic x 11-system Opus coverage matrix
   python -m geometor.codes opus --domain 4

   # View side-by-side Rosetta Stone benchmark implementations
   python -m geometor.codes rosetta 06-circle-power-inversion-polar

   # Inspect the 7-layer, 33-repository GEOMETOR ecosystem hierarchy
   python -m geometor.codes hierarchy

   # Rebuild all 9 exact float-free .euclid-graphic SVG diagrams
   python -m geometor.codes build-figures

Documentation
-------------

Compile the Sphinx codex locally via ``photon-platform/publish``:

.. code-block:: bash

   publish build
