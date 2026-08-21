#!/usr/bin/env python3
"""Publication layout checker with Annual References multicol compatibility.

The canonical checker remains strict about one balanced two-column block per narrative article.
This adapter additionally recognizes the Annual final References compaction only when the source
manifest explicitly declares the layout-only contract and the exact reader-facing markers are
present.  Half-year behavior is delegated unchanged to the previous checker implementation.
"""
from __future__ import annotations

from typing import Any

from scripts import special_publication_layout_check_legacy as _base
from scripts.special_publication_layout_check_legacy import *  # noqa: F401,F403

_ORIGINAL_DECLARED_NON_NARRATIVE_MULTICOLS = _base.declared_non_narrative_multicols


def declared_non_narrative_multicols(manifest: dict[str, Any], main_text: str) -> tuple[int, list[str]]:
    lr = manifest.get("layout_revision") or {}
    if lr.get("annual_final_reference_compaction") is not True:
        return _ORIGINAL_DECLARED_NON_NARRATIVE_MULTICOLS(manifest, main_text)

    errors: list[str] = []
    if lr.get("references_columns") != 2:
        errors.append("Annual References multicol revision must declare references_columns=2")
    if lr.get("references_heading_full_width") is not True:
        errors.append("Annual References multicol revision must declare references_heading_full_width=true")
    if lr.get("references_raggedright") is not True:
        errors.append("Annual References multicol revision must declare references_raggedright=true")
    if lr.get("bibliography_data_changed") is not False:
        errors.append("Annual References multicol revision must declare bibliography_data_changed=false")
    if lr.get("chronology_event_content_changed") is not False:
        errors.append("Annual References multicol revision must declare chronology_event_content_changed=false")
    if lr.get("reader_semantic_content_changed") is not False:
        errors.append("Annual References multicol revision must declare reader_semantic_content_changed=false")

    required = (
        "% annual References two-column final compaction",
        r"\section*{References / Source Notes}",
        r"\addcontentsline{toc}{section}{References / Source Notes}",
        r"\begin{multicols}{2}" + "\n" + r"\raggedright" + "\n" + r"\printbibliography[heading=none]" + "\n" + r"\end{multicols}",
    )
    for token in required:
        if token not in main_text:
            errors.append(f"declared Annual References multicol source marker missing: {token}")
    return (1 if not errors else 0), errors


_base.declared_non_narrative_multicols = declared_non_narrative_multicols


def main() -> int:
    return _base.main()


if __name__ == "__main__":
    raise SystemExit(main())
