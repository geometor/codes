GEOMETOR • codes
================

**Visit the Online Archive:** https://geometor.github.io/codes/

.. image:: docsrc/_static/figures/01-seven-ontologies.svg
   :alt: GEOMETOR • codes featured geometric construction
   :target: https://geometor.github.io/codes/
   :align: center

**Geometric Codes • Theorem-Proving Engines & Symbolic Grammars • semantic digital archive**

Mission
-------

``geometor/codes`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It compares 12 geometric systems—from Euclid's prose to interactive theorem provers (LeanEuclid, GeoCoq, mathlib4), neuro-symbolic engines (AlphaGeometry, Newclid, JGEX), computer algebra (SymPy, ``geometor.model``), Clifford algebras (kingdon, galgebra), and dynamic geometry (CindyJS)—by their **truth foundation**: what exists, what is assumed, how new truths are derived, what evidence is left behind, and what must be trusted. Each system is placed on a seven-layer **Trust Stack** and a **Truth Ladder** (L0 Plausible → L5 Foundational).

Catalogs in This Archive
------------------------

- `Truth Foundations <https://geometor.github.io/codes/foundations/>`_ — The Truth Ladder, Trust Stack, system cards, comparison axes, and graphs of bridges, lifts, and shared trusted components.
- `Showcase <https://geometor.github.io/codes/showcase/>`_ — One theorem, many foundations: Euclid I.5, I.47, III.31, the Simson line, and Pasch side by side, with exact L1 and L2 witnesses.
- `Principle Catalog <https://geometor.github.io/codes/catalog/>`_ — 667 candidate principles mined from 1,425 declarations, searchable by text, family, and system.
- `Systems <https://geometor.github.io/codes/systems/>`_ — Architectural and forensic dossiers on 11 formal, visual, and neuro-symbolic geometry engines.
- `Opus Coverage Matrix <https://geometor.github.io/codes/opus/>`_, `Rosetta Stone Benchmarks <https://geometor.github.io/codes/rosetta/>`_, `Syntax Field Guide <https://geometor.github.io/codes/syntax/>`_, and `Hierarchy <https://geometor.github.io/codes/hierarchy/>`_ — the original v0.1 comparative study.


Repository Contents
-------------------

- ``docsrc/`` — RST catalog tracks, system dossiers, and benchmark analyses compiled by `PHOTON publish <https://github.com/photon-platform/publish>`_.
- ``resources/`` — Curated coverage matrices, syntax decoders, and benchmark manifests.
- ``src/geometor/codes/`` — Symbol decoder, benchmark evaluators, coverage matrix analyzers, and CLI tools.

Local Build & Verification
--------------------------

.. code-block:: bash

   publish build
   uv run --no-sync pytest

Part of the GEOMETOR Knowledge Archive
--------------------------------------

Explore all **74 Book Codices** and **11 Mathematical Catalogs** at https://geometor.com/books/.
