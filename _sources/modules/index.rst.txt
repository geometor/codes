:navigation: header
:order: 95

=======
Modules
=======

``geometor.codes`` is organized into focused data-registry, exact symbolic modeling, SVG rendering, and CLI exploration modules:

- :mod:`geometor.codes` — Public package interface exporting :class:`~geometor.codes.registry.CodesRegistry`, :data:`~geometor.codes.figures.FIGURE_SPECS`, :func:`~geometor.codes.figures.build_all_figures`, :func:`~geometor.codes.render.render_svg`, and :func:`~geometor.codes.cli.run_cli`.
- :mod:`geometor.codes.registry` — Immutable Python 3.13 dataclasses (:class:`~geometor.codes.registry.SystemProfile`, :class:`~geometor.codes.registry.SyntaxEntry`, :class:`~geometor.codes.registry.OpusDomain`, :class:`~geometor.codes.registry.OpusTopic`, :class:`~geometor.codes.registry.RosettaBenchmark`, :class:`~geometor.codes.registry.HierarchyLayer`, :class:`~geometor.codes.registry.ArchitecturalRecommendation`) and standalone offline-resilient query engine over ``resources/*.json``.
- :mod:`geometor.codes.figures` — Nine 100% exact float-free ``geometor.model.Model(..., auto_intersect=False)`` construction builders verified via ``zero_test``, ``quadrance``, ``line_spread``, ``vertex_spread``, ``signed_area2``, and ``cross_ratio``.
- :mod:`geometor.codes.render` — Interactive dark-canvas ``.euclid-graphic.codes-diagram`` SVG renderer supporting pan/zoom, guide/label toggles, and two-way ``:g:`` :math:`\leftrightarrow` ``data-ref`` hover illumination.
- :mod:`geometor.codes.cli` — Rich terminal explorer (``codes summary``, ``codes decode``, ``codes opus``, ``codes rosetta``, ``codes hierarchy``, ``codes build-figures``).
