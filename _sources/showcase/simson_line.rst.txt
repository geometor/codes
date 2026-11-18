.. role:: raw-html(raw)
   :format: html

.. _showcase-simson_line:

Simson line
===========

.. admonition:: Statement
   :class: note

   The feet of the perpendiculars from a point on the circumcircle to the sides of a triangle are collinear.

**Why this theorem:** Post-Euclidean and the native territory of algebraic provers. A rule engine can hard-code it, and Newclid then removes it again as redundant.

.. graphviz::
   :align: center
   :alt: Simson line realizations

   digraph showcase_simson_line {
     graph [rankdir=LR, bgcolor="transparent", fontname="Helvetica", fontcolor="#8a8f98", nodesep=0.25, ranksep=0.45, ranksep=0.8];
     node [fontname="Helvetica", fontsize=11, style="filled,rounded", shape=box, color="#555a62", fontcolor="#1d1f23", penwidth=0.8];
     edge [fontname="Helvetica", fontsize=9, color="#8a8f98", fontcolor="#8a8f98", arrowsize=0.6];
     thm [label="Simson line", shape=ellipse, style=filled, fillcolor="#ffffff", penwidth=1.6];
     r0 [label=<<b>Euclid</b><br/><font point-size="9">—<br/><i>absent</i></font>>, fillcolor="#dddddd", URL="../foundations/cards/euclid.html", target="_top", tooltip="Not in the Elements (Wallace, 1799)."];
     thm -> r0 [style=dashed];
     r1 [label=<<b>Newclid</b><br/><font point-size="9">R45_SIMSONS_LINE_THEOREM<br/><i>rule</i></font>>, fillcolor="#f6b26b", URL="../foundations/cards/newclid.html", target="_top", tooltip="Listed in TRIAGE_LEAVE_RULE_OUT: provable from other rules, so left out of the default rule set."];
     thm -> r1 [style=solid];
     r2 [label=<<b>JGEX</b><br/><font point-size="9">examples/Showcase/simson.gex<br/><i>generic</i></font>>, fillcolor="#7fd1c7", URL="../foundations/cards/jgex.html", target="_top", tooltip="A classic Wu-method / Gröbner example; certified off the non-degeneracy conditions."];
     thm -> r2 [style=solid];
     r3 [label=<<b>mathlib4</b><br/><font point-size="9">—<br/><i>absent</i></font>>, fillcolor="#dddddd", URL="../foundations/cards/mathlib4.html", target="_top", tooltip="No Simson line in Mathlib/Geometry/Euclidean at the surveyed commit."];
     thm -> r3 [style=dashed];
     r4 [label=<<b>geometor.model</b><br/><font point-size="9">verify._build_simson_line<br/><i>witness</i></font>>, fillcolor="#9cc3f0", URL="../foundations/cards/geometor_model.html", target="_top", tooltip="Exact on one cyclic quadrilateral (L1)."];
     thm -> r4 [style=solid];
   }

Realizations
------------

.. container:: codes-tabs

   .. container:: codes-tab status-absent

      .. rubric:: Euclid

      :raw-html:`<span class="codes-status" style="background:#dddddd">absent</span>` — :doc:`Euclid card </foundations/cards/euclid>`

      Not in the Elements (Wallace, 1799).

   .. container:: codes-tab status-rule

      .. rubric:: Newclid

      :raw-html:`<span class="codes-status" style="background:#f6b26b">rule</span>` ``R45_SIMSONS_LINE_THEOREM`` — :doc:`Newclid card </foundations/cards/newclid>`

      .. code-block:: python

         premises:    cyclic A B C P, coll A L C, perp P L A C,
                      coll M B C, perp P M B C, coll N A B, perp P N A B
         conclusions: coll L M N

      Listed in TRIAGE\_LEAVE\_RULE\_OUT: provable from other rules, so left out of the default rule set.

      Source: `all\_rules.py#L521-L534 <https://github.com/LMCRC/Newclid/blob/ac6550732a950564cf7614d605b5bf1eadd29701/newclid/src/newclid/all_rules.py#L521-L534>`__

   .. container:: codes-tab status-generic

      .. rubric:: JGEX

      :raw-html:`<span class="codes-status" style="background:#7fd1c7">generic</span>` ``examples/Showcase/simson.gex`` — :doc:`JGEX card </foundations/cards/jgex>`

      A classic Wu-method / Gröbner example; certified off the non-degeneracy conditions.

      Source: `examples <https://github.com/kovzol/Java-Geometry-Expert/tree/5489aacb40afc91b5c5ca539db853cca216e1165/src/main/resources/docs/examples>`__

   .. container:: codes-tab status-absent

      .. rubric:: mathlib4

      :raw-html:`<span class="codes-status" style="background:#dddddd">absent</span>` — :doc:`mathlib4 card </foundations/cards/mathlib4>`

      No Simson line in Mathlib/Geometry/Euclidean at the surveyed commit.

   .. container:: codes-tab status-witness

      .. rubric:: geometor.model

      :raw-html:`<span class="codes-status" style="background:#9cc3f0">witness</span>` ``verify._build_simson_line`` — :doc:`geometor.model card </foundations/cards/geometor_model>`

      .. code-block:: python

         A, B, C, P = (5, 0), (-5, 0), (3, 4), (0, 5)   # on x² + y² = 25
         F1, F2, F3 = feet of perpendiculars from P to AB, BC, CA
         m.assert_concyclic(A, B, C, P, by="Given")
         m.assert_collinear(F1, F2, F3, by="Simson")

      Exact on one cyclic quadrilateral (L1).

      Source: ``codes/src/geometor/codes/verify.py``

Climbing the ladder in GEOMETOR
-------------------------------

**L1 — exact instance.** ``geometor.model`` builds one figure with exact coordinates and checks the conclusion by ``zero_test``: *Exact witness verified (7 points, 1 lines, 0 circles)* (status ``verified``). See the :ref:`witness entry <simson_line>`.

.. figure:: simson_line.svg
   :alt: simson_line
   :align: center
   :width: 70%

**L2 — generic.** Replace the coordinates by free symbols ``s, t, w``. A, B, C on the unit circle via rational parameters s, t, w; P = (1, 0) (WLOG by rotation). The conclusion's numerator reduces to **0**, so the theorem holds for every configuration outside the degenerate set:

- s, t, w pairwise distinct (non-degenerate triangle)
- s, t, w != 0 (P not a vertex)

Computed at build time by :py:func:`geometor.codes.generic.generic_witness`.
