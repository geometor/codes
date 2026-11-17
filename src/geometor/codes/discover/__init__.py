"""Discovery pipeline: normalize base declarations, fingerprint, and cluster into principles."""

from __future__ import annotations

from geometor.codes.discover.cluster import Catalog, Principle, discover_principles, load_catalog, save_catalog
from geometor.codes.discover.fingerprint import fingerprint_form
from geometor.codes.discover.normalize import Atom, CanonicalForm, normalize_decl

__all__ = [
    "Atom",
    "CanonicalForm",
    "Catalog",
    "Principle",
    "discover_principles",
    "fingerprint_form",
    "load_catalog",
    "normalize_decl",
    "save_catalog",
]
