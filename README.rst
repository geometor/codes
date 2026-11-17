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

``geometor/codes`` is part of the interconnected `GEOMETOR <https://geometor.com>`_ semantic digital archive. It provides a comprehensive comparative audit of 11 formal, visual, and symbolic geometric languages—from Euclid and Oliver Byrne's chromatic visual pseudocode to modern interactive theorem provers (LeanEuclid, GeoCoq, mathlib4), neuro-symbolic engines (AlphaGeometry, Newclid, JGEX), and Clifford algebras (PGA/CGA). By analyzing these systems across 69 canonical topics and side-by-side Rosetta Stone benchmarks, the archive establishes an empirical foundation for automated theorem proving and symbolic geometry across the GEOMETOR corpus.

Catalogs in This Archive
------------------------

- `Opus Coverage Matrix (69 Topics x 11 Systems) <https://geometor.github.io/codes/opus/>`_ — Comprehensive comparative coverage matrix mapping 69 classical and modern geometric theorems across 11 formal systems.
- `Rosetta Stone Benchmarks <https://geometor.github.io/codes/rosetta/>`_ — Canonical constructions and proofs implemented side-by-side across all 11 surveyed architectures with interactive vector figures.
- `Syntax Field Guide & Symbol Decoder <https://geometor.github.io/codes/syntax/>`_ — Systematic decoder for 60 formal binders, predicates, blade operators, and Byrne chromatic glyphs.
- `Systems <https://geometor.github.io/codes/systems/>`_ — Architectural and forensic dossiers on 11 formal, visual, and neuro-symbolic geometry engines.
- `Hierarchy <https://geometor.github.io/codes/hierarchy/>`_ — Eight foundational mathematical paradigms and structural hierarchy of geometric formalisms.

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
