.. _system-jgex:

====================================================================
Java Geometry Expert (JGEX) & Chou–Gao–Zhang's Area Method
====================================================================

* **Repository**: ``_refs/Java-Geometry-Expert`` (`https://github.com/yezheng1981/Java-Geometry-Expert`, GPL-3.0-only, :cite:`ChouGaoZhang1994`, :cite:`YeChouGao2011`)
* **Scale Audited**: ``src/main/java/gprover/`` (`GDD`, `Full`, `Area`, `Elim`, `CharSet` Wu, `PanelGB` Gröbner) + hundreds of `.gex` theorems (`exs-book/`, `3_JAR/`, `4_PYTH/`)
* **Mathematical Foundation**: Multi-engine synthesis uniting Deductive Databases, Full-Angles, Coordinate-Free Area/Pythagoras Elimination, Ritt–Wu Characteristic Sets, and Gröbner Bases

1. Historical Mother-Ship of Automated Geometry
------------------------------------------------

``Java-Geometry-Expert`` (`JGEX`), created by Zheng Ye, :person:`Shang-Ching Chou <chou>`, and :person:`Xiao-Shan Gao <gao>`, is the direct ancestor from which ``AlphaGeometry`` and ``Newclid`` inherited both their clause DSL and their 43 ``GDD`` Horn rules. Crucially, however, ``JGEX`` was designed around **five complementary reasoning engines** so that when forward Horn saturation (`GDD`) stalls, coordinate-free invariant elimination (`Area` / `Full-Angle`) or algebraic triangulation (`Wu` / `Gröbner`) takes over.

2. Mathematical Jewel: The Coordinate-Free Area Method
------------------------------------------------------

Formulated by Chou, Gao, and :person:`Jing-Zhong Zhang <zhang>` (:cite:`ChouGaoZhang1994`), the :term:`Area Method` proves theorems **without introducing Cartesian coordinates** and **without guessing auxiliary points**, using three coordinate-free geometric quantities:

1. **Signed Parallel Ratio** :math:`r = \overline{AB} / \overline{CD}` for parallel directed segments :math:`AB \parallel CD`.
2. **Signed Polygon Area** :math:`S_{ABC}` (and quadrilateral :math:`S_{ABCD} = S_{ABC} + S_{ACD}`), vanishing iff :math:`A, B, C` are collinear and satisfying the **Co-Side Theorem**: if :math:`M = AB \cap PQ`, then :math:`\overline{PM}/\overline{QM} = S_{PAB}/S_{QAB}`.
3. **Pythagoras Difference** (:term:`Pythagoras difference`):

   .. math::

      P_{ABC} = |AB|^2 + |BC|^2 - |AC|^2, \qquad P_{ABCD} = |AB|^2 + |CD|^2 - |BC|^2 - |DA|^2 = 2\,\overrightarrow{AC}\cdot\overrightarrow{BD}

Look at what happens immediately in this basis:

* **Pythagoras (`Euclid I.47`) is 0 steps**: :math:`AB \perp BC \iff P_{ABC} = 0` *by definition*!
* **Orthocenter Concurrency is 0 steps**: For any four points :math:`A, B, C, H`, expanding squares gives the Jacobi-like identity :math:`P_{ACHB} + P_{BAHC} + P_{CBAH} \equiv 0`. If :math:`AH \perp BC` (:math:`P_{BAHC} = 0`) and :math:`BH \perp AC` (:math:`P_{CBAH} = 0`), then :math:`P_{ACHB} = 0` (:math:`CH \perp AB`) instantaneously!
* **Pappus, Ceva, Menelaus, Cross-Ratio & La Hire Inversion**: Given a constructive sequence of points (`INTERSECTION_LL`, `FOOT`, `PRATIO`, `TRATIO`, `INVERSION`), each constructed point :math:`Y` appears *linearly* in :math:`S` and :math:`P` (`Elim.java`) and is eliminated backward in one rational substitution step—proving Pappus (`exs-book/ch2:40`) and La Hire pole–polar (`exs-book/ch3:49`) with **zero auxiliary points** while automatically extracting exact **Non-Degeneracy Conditions (`NDGs`)**!

3. Forensic Surprise: ``Area.java`` Left Unfinished in ``JGEX``!
----------------------------------------------------------------

Inspecting the actual Java source tree in ``_refs/Java-Geometry-Expert/src/main/java/`` revealed a major surprise: while the elimination kernel helpers live in ``gprover/Elim.java``, ``gprover/Area.java`` (`213` lines) is an **incomplete port from C**, and in ``wprover/PanelProve.java:112-116`` the GUI Area-Method tab is literally commented out:

.. code-block:: java

   // wprover/PanelProve.java:112-116
   // TODO: Implement the area method
   // panelMethod.addTab("A", ...);

In the shipping Java GUI, users only have interactive access to ``GDD``, ``Full-Angle``, ``Wu`` (`CharSet.java`), and ``Gröbner`` (`PanelGB.java` using Rabinowitsch saturation :math:`1 - u_k g_k = 0`).

4. Takeaway for GEOMETOR
------------------------

``geometor.model`` already has exact ``signed_area2`` and ``quadrance``! Adding ``pythagoras_diff`` and completing Chou–Gao–Zhang's backward point eliminator in clean Python 3.13 / SymPy (`Blueprint 6`) finishes the exact readable-proof engine that ``JGEX`` left unfinished in Java.
