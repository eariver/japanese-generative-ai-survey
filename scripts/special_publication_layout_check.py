#!/usr/bin/env python3
"""Publication layout checker with Annual References multicol compatibility.

The canonical checker remains strict about one balanced two-column block per narrative article.
This adapter additionally recognizes Annual final References compaction descendants only when the
source manifest explicitly declares their layout-only contract and the exact reader-facing markers
are present.  Half-year behavior is delegated unchanged to the previous checker implementation.

Annual pagination v3 renders only the References body in three columns.  The legacy checker counts
``multicols{2}`` starts because narrative bodies are always two-column, so after validating the v3
contract this adapter normalizes that one References start marker to ``multicols{2}`` *for checker
input only*.  Publication source bytes are never modified by this compatibility layer.
"""
from __future__ import annotations

import copy
from typing import Any

from scripts import special_publication_layout_check_legacy as _base
from scripts.special_publication_layout_check_legacy import *  # noqa: F401,F403

_ORIGINAL_DECLARED_NON_NARRATIVE_MULTICOLS = _base.declared_non_narrative_multicols
_ORIGINAL_INSPECT_LAYOUT = _base.inspect_layout


def _common_annual_reference_errors(lr: dict[str, Any]) -> list[str]:
    errors: list[str] = []
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
    return errors


def _annual_v3_errors(lr: dict[str, Any], main_text: str) -> list[str]:
    errors = _common_annual_reference_errors(lr)
    if lr.get("references_columns") != 3:
        errors.append("Annual References pagination v3 must declare references_columns=3")
    if lr.get("annual_reference_pagination_v3_issue_refs") != [140]:
        errors.append("Annual References pagination v3 must be scoped to issue_refs=[140]")
    if lr.get("references_entry_font") != "6.8pt/7.4pt":
        errors.append("Annual References pagination v3 must declare references_entry_font=6.8pt/7.4pt")

    required = (
        r"\section*{References / Source Notes}",
        r"\addcontentsline{toc}{section}{References / Source Notes}",
        r"\begin{multicols}{3}" + "\n" + r"\raggedright" + "\n" + r"\printbibliography[heading=none]" + "\n" + r"\end{multicols}",
    )
    for token in required:
        if token not in main_text:
            errors.append(f"declared Annual References pagination v3 source marker missing: {token}")
    if main_text.count(r"\begin{multicols}{3}") != 1:
        errors.append("Annual References pagination v3 must contain exactly one multicols{3} block")
    if main_text.count(r"\printbibliography") != 1:
        errors.append("Annual References pagination v3 must contain exactly one printbibliography")
    return errors


def declared_non_narrative_multicols(manifest: dict[str, Any], main_text: str) -> tuple[int, list[str]]:
    lr = manifest.get("layout_revision") or {}
    if lr.get("annual_final_reference_compaction") is not True:
        return _ORIGINAL_DECLARED_NON_NARRATIVE_MULTICOLS(manifest, main_text)

    if lr.get("annual_reference_pagination_v3") is True:
        errors = _annual_v3_errors(lr, main_text)
        return (1 if not errors else 0), errors

    errors = _common_annual_reference_errors(lr)
    if lr.get("references_columns") != 2:
        errors.append("Annual References multicol revision must declare references_columns=2")
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


def inspect_layout(
    manifest: dict[str, Any],
    main_text: str,
    architecture: dict[str, Any],
) -> list[str]:
    lr = manifest.get("layout_revision") or {}
    if lr.get("annual_reference_pagination_v3") is not True:
        return _ORIGINAL_INSPECT_LAYOUT(manifest, main_text, architecture)

    # Validate the real reader-facing three-column block before any compatibility normalization.
    v3_errors = _annual_v3_errors(lr, main_text)
    if v3_errors:
        return v3_errors

    # The legacy checker intentionally models all admitted multicols as two-column narrative-style
    # blocks.  Normalize only the single already-validated References start marker for checker input.
    shim_manifest = copy.deepcopy(manifest)
    shim_lr = shim_manifest.setdefault("layout_revision", {})
    shim_lr["annual_reference_pagination_v3"] = False
    shim_lr["references_columns"] = 2
    shim_text = main_text.replace(r"\begin{multicols}{3}", r"\begin{multicols}{2}", 1)
    return _ORIGINAL_INSPECT_LAYOUT(shim_manifest, shim_text, architecture)


_base.declared_non_narrative_multicols = declared_non_narrative_multicols
_base.inspect_layout = inspect_layout


def main() -> int:
    return _base.main()


if __name__ == "__main__":
    raise SystemExit(main())
