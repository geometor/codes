.. _hierarchy-paradigms:

=================================================
The Eight Paradigms of Formal & Visual Geometry
=================================================

Why do eleven major formalizations of Euclidean and projective geometry look as if they come from eleven different planets? Because a formal language for geometry must simultaneously answer four questions that pull in opposite directions:

1. **Ontology** — Are lines, circles, and conics primitive types, predicates over points, affine vector cosets, graded Clifford blades, :math:`3 \times 3` complex matrices, or inline colored visual glyphs?
2. **Continuity & Root Selection** — When two circles intersect, how does the system know an intersection exists, and how does it distinguish the *upper* pole :g:`F` from the *lower* pole :g:`E`?
3. **Metric Representation** — Does the language measure length and angle via real square roots and ``arccos``, synthetic ``Cong`` equivalence classes, linear angles mod :math:`\pi` and log-ratios, coordinate-free areas :math:`S_{ABC}` and :term:`Pythagoras difference` :math:`P_{ABC}`, or polynomial :term:`quadrance` :math:`Q` and :term:`spread` :math:`s`?
4. **Epistemic Certificate** — Is geometric truth certified by a small dependent-type kernel (Coq, Lean 4), an external SMT solver, sparse Gaussian saturation, polynomial triangulation, randomized complex evaluation, human visual perception, or exact :term:`Algebraic Number Polynomial` (`ANP`) canonicalization?

.. figure:: /_static/figures/01-seven-ontologies.svg
   :align: center
   :width: 100%

   **Figure 1 — The Vesica Piscis Across Paradigms** (:g:`A`, :g:`B`, :g:`[ A B ]`, :g:`( A B )`, :g:`( B A )`, :g:`F`, :g:`E`). Every paradigm encodes this single opening figure of :person:`Euclid <euclid>`'s *Elements* (`I.1`) through a fundamentally different mathematical substrate.

Comparative Taxonomy of the Eight Paradigms
-------------------------------------------

.. list-table::
   :widths: 18 18 22 22 20
   :header-rows: 1

   * - Paradigm
     - Exemplars
     - Ontological Primitives
     - Crown Jewel Capability
     - Structural Ceiling
   * - **1. Pointer-Free Visual Pseudocode**
     - :ref:`Byrne (1847) / Rougeux <system-byrne-1847>`
     - Coloured inline glyphs (`[━━]`, `[◣]`, `[□]`, `[○]`) + `=`, `::`, `∴`
     - Zero vertex-pointer dereferencing; Books I–VI including Book II gnomons & :math:`\phi` (`VI.30`)
     - 4-color palette saturates on dense 9-point / projective figures; 0D points lack glyphs
   * - **2. Diagrammatic Formal System + SMT**
     - :ref:`LeanEuclid <system-leaneuclid>`
     - 6 sorts (`Point`, `Line`, `Circle`, `Segment`, `Angle`, `Triangle`)
     - Formalizes Euclidean plane separation & circle intersections (`Intersections.lean`)
     - Relies on unverified `SMT_VERIF` trust oracle; stops at Book I (`Prop48`)
   * - **3. First-Order Point-Only Axiomatics**
     - :ref:`GeoCoq <system-geocoq>`
     - `Tpoint` + `Bet A B C` + `Cong A B C D`
     - 100% kernel-checked `Tarski <-> Hilbert <-> Euclid` & 34 parallel postulates
     - Circles/lines require existential point witnesses; omits `X(5)`, inversion, conics, :math:`\phi`
   * - **4. Dependent Affine Vector Torsors**
     - :ref:`Mathlib4 <system-mathlib4>`
     - `P : Type*`, `V : Type*`, `[NormedAddTorsor V P]`
     - Arbitrary dimension :math:`n` (`mongePoint`, :math:`3(n+1)`-pt sphere, La Hire polar)
     - `noncomputable` (`Real.arccos`, `Classical.choose`); omits `Euclid I.1`, `crossRatio`, `Pappus`
   * - **5. Neuro-Symbolic Clause DD + AR**
     - :ref:`AlphaGeometry & Newclid <system-alphageometry>`
     - Clauses (`defs.txt`), Horn rules (`rules.txt`), sparse `AR` matrices
     - Solves 25/30 IMO problems via directed `eqangle` mod :math:`\pi` + LM auxiliary search
     - Float64 sketch guards; bare `DD+AR` cannot prove `Pappus` or state :math:`a^2+b^2=c^2` (`AG`)
   * - **6. Coordinate-Free Invariant Elimination**
     - :ref:`JGEX Area Method <system-jgex>`
     - Constructive point sequence + :math:`\{r, S_{ABC}, P_{ABC}\}`
     - Human-readable 0-aux-point proofs of Pythagoras, Orthocenter, Ceva, Menelaus, Pappus, Inversion
     - `Area.java` left unfinished/disabled in JGEX GUI; limited to rational constructions
   * - **7. Covariant Clifford & Projective Matrices**
     - :ref:`PGA / CGA <system-pga-cga>`, :ref:`CindyJS <system-cindyjs>`
     - Graded blades (`Cl(2,0,1)`, `Cl(3,1)`) or :math:`\mathbb{CP}^2` vectors & :math:`3\times 3` conics
     - Division-free projective joins/meets, 1-line circle power/radical-axis/inversion (`C >> P`), general conics
     - Pure blade/matrix algebra erases Euclidean compass-and-straightedge step history; `CindyJS` uses floats
   * - **8. Exact Constructive Symbolic DAG**
     - :ref:`GEOMETOR <system-geometor>` (extending :ref:`SymPy <system-sympy>`)
     - Ancestral `Model` DAG + exact `ANP` coordinates + `quadrance` / `spread` + `:g:` SVG
     - 100% float-free radical towers (:math:`\mathbb{Q}(\phi)`, :math:`\mathbb{Q}(\sqrt{d})`), System E selectors, `ETC` `X(1)`–`X(53144)`
     - Needs BFMSS root-separation bounds (`count_ops > 25`), native inversion/conic matrices, and `Step` AST export

The Noetic Tension: Symbolic Rigor vs. Intuitive Nexus
------------------------------------------------------

In *De Noetica Geometriae* (:cite:`Hoenen1954`), :person:`Peter H. J. Hoenen <hoenen>` observed that geometric knowledge neither floats in pure imageless logic nor reduces to empirical measurement of ink on paper. Rather, human reason grasps universal necessity *inside* the concrete spatial *Nexus* of the constructed figure (*abstractio formalis intuitiva*).

Viewed through Hoenen's lens, the history of formal geometry over the last century splits into two halves that rarely speak to one another:

* **Imageless Deductive Engines** (`GeoCoq`, `mathlib4`) achieve unassailable logical certainty inside a proof assistant's type kernel, yet sever the link to executable coordinates and visual diagrams: `mathlib4` cannot compute the coordinates of an equilateral apex without `noncomputable` choice, and `GeoCoq` dissolves lines and circles into six-quantifier point formulas.
* **Numeric Sketch Engines** (`CindyJS`, `AlphaGeometry`'s `numericals.py`) embrace concrete coordinates to prune branches and draw diagrams, yet fall back to IEEE-754 floating-point approximations (`1e-7` tolerances in `Newclid`, randomized complex floats in `CindyJS`), losing exact algebraic identity over :math:`\mathbb{Q}(\phi)` or nested quadratic towers.

**GEOMETOR's foundational thesis** is that *exact symbolic algebra* (`QQ.algebraic_field` + closed-form radical-axis intersections + topological root selectors + Rational Trigonometry invariants + interactive `.euclid-graphic` SVGs) heals this split: the concrete constructed diagram **is** an exact algebraic object in :math:`\overline{\mathbb{Q}}^2`, carrying both visual immediacy and deductive necessity.
