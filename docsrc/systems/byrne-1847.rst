.. _system-byrne-1847:

====================================================================
Oliver Byrne (1847) & Rougeux (2018): Pointer-Free Visual Pseudocode
====================================================================

* **Primary Editions**: :person:`Oliver Byrne <byrne>`, *The First Six Books of the Elements of Euclid in which Coloured Diagrams and Symbols are Used Instead of Letters for the Greater Ease of Learners* (Pickering / Chiswick Press, 1847, :cite:`Byrne1847`); interactive SVG/CSS reconstruction by :person:`Nicholas Rougeux <rougeux>` (`https://www.c82.net/euclid/`, 2018, :cite:`Rougeux2018`)
* **Sibling GEOMETOR Codex**: ``geometor/byrne`` (*Layer 1 Digital Scriptorium*)
* **Paradigm**: **Pointer-Free Chromatic Visual Pseudocode & Inline Value-Token Calculus**

1. Why Byrne (1847) Is a Formal Language Breakthrough
-----------------------------------------------------

Art historians celebrate Byrne's 1847 *Euclid* as a Victorian typographic marvel anticipating Bauhaus and Mondrian. Viewed through programming-language theory, however, Byrne achieved something far more radical: **he invented the first pointer-free (tacit) visual pseudocode for deductive geometry**.

In classical :person:`Euclid <euclid>` (and in ``LeanEuclid``, ``GeoCoq``, ``mathlib4``, and ``AlphaGeometry``), geometric objects have no direct inline representation in text; instead, 0D points are bound to symbolic variable names (``A``, ``B``, ``C``), and segments, angles, and polygons are dereferenced via multi-letter pointer tuples (``AB``, ``∠ABC``, ``△ABC``). Every equation forces the human reader to execute a mental *pointer lookup*: scan ``"∠BDF = ∠FEC"`` in text :math:`\to` hunt for ``B``, ``D``, ``F`` on the figure :math:`\to` trace the angle :math:`\to` hunt for ``F``, ``E``, ``C`` :math:`\to` jump back to the text without losing the line!

Byrne replaced indirect pointer dereferencing with **direct inline chromatic value-tokens**:

1. **Four-Color + Three-Stroke Token Alphabet**: Miniature woodblock shapes in primary **red**, **blue**, **yellow**, and **black** combined with **solid** (``━━``, `Given` loci), **dashed** (``╌╌╌``, primary `Construction` loci), and **dotted** (``┈┈┈``, secondary auxiliary loci) strokes sit directly inside the mathematical line as typed visual values (`Segment`, `Angle Wedge`, `Triangle`, `Square/Rectangle`, `Circle/Arc`).
2. **Structured Pseudocode Block Grammar**: Every proposition is refactored out of Euclid's continuous Greek prose paragraph into four explicit blocks anticipating ``@proposition`` (`Given` :math:`\to` `Construct` :math:`\to` `Demonstrate`) by 175 years:

   * Enunciation + Main Diagram,
   * Visual Specification (`Given` / `To Prove` or `To Construct`),
   * Imperative `Construction` block (introducing dashed/dotted colored loci),
   * Vertical `Proof` block of aligned algebraic-logical equations using Oughtred's ``=``, ``+``, ``-``, ``>``, ``<``, four-term proportion ``A : B :: C : D``, and Rahn's ``∴`` (*therefore*) with marginal citations ``(I.4)``, ``(Ax. 1)``.

2. Byrne's Surprising Opus Victory: Book II Gnomons & The Golden Ratio!
-----------------------------------------------------------------------

Comparing Byrne (`1847`) against modern theorem provers in our :ref:`Opus Matrix <opus-index>` yields an astonishing result. Whereas ``LeanEuclid``, ``GeoCoq``, ``mathlib4`` Geometry, ``AlphaGeometry``, and ``Newclid`` **all omit the Golden Ratio (:math:`\phi`) and Book II gnomonic algebra**, Byrne's 268-page opus covers **all of Books I–VI**, including:

* **Book I (`Props. 1–48`)**: culminating in the iconic four-color Bride's Chair (`I.47`), where ``[red □] + [blue □] = [yellow ▭] + [black ▭]`` becomes visually transparent;
* **Book II (`Props. 1–14`)**: geometric algebra of colored rectangles and gnomons, including **Book II, Prop. 11** (*cutting a line so the rectangle of whole and lesser equals the square on the greater*);
* **Book III (`Props. 1–37`)**: circle chords, inscribed wedges (`III.20–22`), external tangents (`III.17`), and **intersecting-chord / tangent-secant circle power (`III.35–36`)**;
* **Book IV (`Props. 1–16`)**: incircle (`IV.4`), circumcircle (`IV.5`), **regular pentagon (`IV.10–11`)**, and regular 15-gon (`IV.16`);
* **Book V (`Props. 1–25`) & Book VI (`Props. 1–33`)**: Eudoxian four-term ``::`` ribbon proportions, Thales intercept (`VI.2`), similar polygons, and **Book VI, Prop. 30** (*dividing a segment in Extreme and Mean Ratio* :math:`\phi`!).

3. Structural Ceilings of Pure Chromatic Tokens
-----------------------------------------------

Why did Byrne stop at Book VI, and where does pure pointer-free color notation hit a formal ceiling?

1. **Combinatorial Palette Exhaustion (~12 Tokens)**: Four colors :math:`\times` three stroke styles distinguish roughly a dozen concurrent elements cleanly. Dense configurations like the Nine-Point Circle (`X(1)`–`X(5)` + 3 medians + 3 altitudes + 9 concyclic feet/midpoints) overwhelm chromatic discrimination.
2. **0D Point Erasure**: Points have almost no visual area! Whenever Euclid must speak of an isolated point (`I.31` external point, or the 9 collinearity points of :person:`Pappus <pappus>`'s Hexagon), Byrne must either print an ad-hoc black dot/star or write circumlocutions (*"the point where [red] meets [blue]"*). Pure point-incidence geometry (`Pappus`, `Desargues`, Tarski `Bet`) cannot live without point identifiers.
3. **Plain-Text Greppability & Machine Checking**: Pure woodblock icons cannot be typed in ASCII or checked by a compiler *unless* backed by a symbolic DOM layer—which is precisely what :person:`Nicholas Rougeux <rougeux>` engineered in `2018` (`c82.net/euclid`) by encoding every inline Byrne glyph as an ``<svg>`` element linked via JavaScript/CSS hover classes to the main diagram!

4. How Byrne & Rougeux Directly Inform GEOMETOR
-----------------------------------------------

GEOMETOR resolves the 2,300-year tension between **Euclid's symbolic pointers** and **Byrne's chromatic immediacy**:

* In ``photon-platform/publish`` and ``geometor/codes``, every ``:g:`` token (such as :g:`[ A B ]`, :g:`( A B )`, :g:`F`) preserves **100% unambiguous symbolic pointer identity** (`data-ref="[ A B ]"` matched to ``geometor.model``'s exact algebraic `Model`) *while* providing **Rougeux-style bidirectional hover illumination** on the inline `.euclid-graphic` SVG!
* Even further (`Blueprint 11`), ``publish`` can optionally emit **inline 14px Byrne micro-glyph SVG badges** right beside ``:g:`` tokens inside ``.. step::`` blocks—giving readers both machine-verified symbolic precision and zero-dereference visual scanning.
