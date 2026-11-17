"""Euclid (Heath) loader: every enunciation as a base declaration."""

from __future__ import annotations

import json
import re
from pathlib import Path

from geometor.codes.mine.schema import Decl, MinedSystem, git_head

_KEY = re.compile(r"^(?P<book>[IVX]+)(?:\.(?P<part>def(?:\.[iv]+)?|post|cn))?\.(?P<n>\d+)$")
_PROBLEM = re.compile(
    r"\b(to|it is required to) (construct|draw|bisect|find|place|cut off|cut|describe|"
    r"inscribe|circumscribe|apply|set out|set up|produce|divide|add|erect|make|comprehend)\b",
    re.IGNORECASE,
)
_ROMAN = {"I": 1, "V": 5, "X": 10}

_PART_KIND = {"post": "postulate", "cn": "common_notion"}


def roman_to_int(s: str) -> int:
    """Convert a Roman numeral (I–XIII) to an integer.

    Args:
        s: Roman numeral.

    Returns:
        Integer value.
    """
    total = 0
    for i, ch in enumerate(s):
        v = _ROMAN[ch]
        total += -v if i + 1 < len(s) and _ROMAN[s[i + 1]] > v else v
    return total


def mine_euclid(
    source: Path, workspace_root: Path, not_yet_in_canon: tuple[str, ...] = ()
) -> MinedSystem:
    """Load Heath enunciations into declarations.

    Args:
        source: Path to ``enunciations.json``.
        workspace_root: Workspace root, for relative source paths.
        not_yet_in_canon: Book numerals marked as not yet in the code canon.

    Returns:
        A `MinedSystem` with one `Decl` per definition, postulate, common
        notion and proposition (section headers are skipped).
    """
    data: dict[str, str] = json.loads(source.read_text(encoding="utf-8"))
    rel = str(source.relative_to(workspace_root))
    decls: list[Decl] = []
    for key, text in data.items():
        m = _KEY.match(key)
        if not m:
            continue  # section header such as "I.def"
        book, part, n = m["book"], m["part"], int(m["n"])
        if part is None:
            kind = "problem" if _PROBLEM.search(text) else "theorem"
            family = f"Book {book} Propositions"
        elif part.startswith("def"):
            kind = "definition"
            family = f"Book {book} Definitions"
        else:
            kind = _PART_KIND[part]
            family = f"Book {book} " + ("Postulates" if part == "post" else "Common Notions")
        decls.append(
            Decl(
                system="euclid",
                id=key,
                name=key,
                kind=kind,
                module=f"Book {book}",
                family=family,
                text=text,
                source=rel,
                extra={
                    "book": book,
                    "book_number": roman_to_int(book),
                    "number": n,
                    "in_canon": book not in not_yet_in_canon,
                },
            )
        )
    order = {k: i for i, k in enumerate(data)}
    decls.sort(key=lambda d: order[d.id])
    return MinedSystem(
        system="euclid",
        decls=decls,
        source=rel,
        commit=git_head(source.parent),
    )
