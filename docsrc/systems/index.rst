:navigation: header
:order: 30

.. _systems-index:

=======
Systems
=======

Deep architectural and forensic dossiers on all **11 formal, visual, and symbolic geometry systems** surveyed in **GEOMETOR Codes**—each audited directly from source code on disk down to exact file paths, line numbers, verification kernels, opus coverage, and live bugs.

.. list-table::
   :widths: 26 30 22 22
   :header-rows: 1

   * - Dossier
     - Paradigm
     - Verification Substrate
     - Headline Forensic Catch
   * - :ref:`LeanEuclid & System E <system-leaneuclid>`
     - Diagrammatic System E + SMT
     - Lean 4 + Z3/CVC5
     - ``SMT_VERIF`` trust axiom + 6 missed Euclid lemmas in ``Prop47``
   * - :ref:`GeoCoq <system-geocoq>`
     - Point-Only Synthetic Axiomatics
     - Coq Kernel + ``ColR``/``CongR``
     - 34 parallel postulates & neutral midpoint; omits ``X(5)``, inversion, :math:`\phi`
   * - :ref:`Lean 4 Mathlib <system-mathlib4>`
     - Dependent Affine Torsors
     - Lean 4 Kernel (`noncomputable`)
     - :math:`n`-dim Monge/Feuerbach/La Hire; omits ``Euclid I.1``, ``crossRatio``, ``Pappus``
   * - :ref:`AlphaGeometry & Newclid <system-alphageometry>`
     - Neuro-Symbolic Clause ``DD + AR``
     - Python/C++ Gaussian `AR` + LM
     - ``rconst`` log-ratio bug (`ar.py:425`), `;` drops, and ``Pappus`` ``DD+AR`` wall
   * - :ref:`JGEX & Area Method <system-jgex>`
     - Coordinate-Free Invariant Elimination
     - Java (`GDD`, `Full`, `Area`, `Wu`, `GB`)
     - 0-step Pythagoras/Orthocenter; ``Area.java`` tab disabled in GUI!
   * - :ref:`PGA & CGA (kingdon / galgebra) <system-pga-cga>`
     - Covariant Clifford Multivector Calculi
     - ``kingdon`` SymPy CSE compiler
     - ``C >> P`` inversion in ``kingdon`` vs. ``.dual()`` crash & ``>>`` trap in ``galgebra``
   * - :ref:`CindyJS (CP^2 & PSLQ) <system-cindyjs>`
     - Complex Projective & Riemann Tracing
     - Schwartz–Zippel + ``PSLQ.js``
     - Semicircle homotopy continuation (`Tracing.js`) + ``ConicBy5`` Plücker pencils
   * - :ref:`SymPy Geometry (1.14.0) <system-sympy>`
     - Affine Cartesian Symbolic CAS
     - ``simplify()`` + generic ``solve()``
     - Live double bug in ``Triangle.excenters`` + ``Point.affine_rank`` float bug
   * - :ref:`Oliver Byrne (1847 / Rougeux) <system-byrne-1847>`
     - Pointer-Free Visual Pseudocode
     - Chromatic value-tokens + SVG hover
     - Eliminates vertex pointers across Books I–VI (including :math:`\phi` in `II.11`/`VI.30`)
   * - :ref:`GEOMETOR (geometor.model) <system-geometor>`
     - Exact Constructive Symbolic DAG
     - SymPy ``ANP`` + Rational Trig
     - 100% float-free radical towers + ``ETC`` `X(1)`–`X(53144)` + 11 roadmap upgrades

.. toctree::
   :maxdepth: 1
   :hidden:

   leaneuclid
   geocoq
   mathlib4
   alphageometry-newclid
   jgex-area-method
   pga-cga
   cindyjs
   sympy-geometry
   byrne-1847
   geometor-model
