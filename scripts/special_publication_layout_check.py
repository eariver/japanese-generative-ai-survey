#!/usr/bin/env python3
"""Publication layout checker with Annual References multicol compatibility.

The canonical checker remains strict about one balanced two-column block per narrative article.
This adapter additionally recognizes fail-closed Annual References compaction descendants. Three-
column References are validated against their declared pagination contract, then normalized only in
checker input to the immutable legacy two-column model. Publication source bytes are never changed.
Half-year and normal Special behavior are delegated unchanged.
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


def _three_column_errors(
    lr: dict[str, Any],
    main_text: str,
    *,
    generation: str,
    expected_font: str,
    ragged_command: str = r"\raggedright",
) -> list[str]:
    errors = _common_annual_reference_errors(lr)
    if lr.get("references_columns") != 3:
        errors.append(f"Annual References pagination {generation} must declare references_columns=3")
    if lr.get(f"annual_reference_pagination_{generation}_issue_refs") != [140]:
        errors.append(f"Annual References pagination {generation} must be scoped to issue_refs=[140]")
    if lr.get("references_entry_font") != expected_font:
        errors.append(f"Annual References pagination {generation} must declare references_entry_font={expected_font}")
    required = (
        r"\section*{References / Source Notes}",
        r"\addcontentsline{toc}{section}{References / Source Notes}",
        r"\begin{multicols}{3}" + "\n" + ragged_command + "\n" + r"\printbibliography[heading=none]" + "\n" + r"\end{multicols}",
    )
    for token in required:
        if token not in main_text:
            errors.append(f"declared Annual References pagination {generation} source marker missing: {token}")
    if main_text.count(r"\begin{multicols}{3}") != 1:
        errors.append(f"Annual References pagination {generation} must contain exactly one multicols{{3}} block")
    if main_text.count(r"\printbibliography") != 1:
        errors.append(f"Annual References pagination {generation} must contain exactly one printbibliography")
    return errors


def _annual_v3_errors(lr: dict[str, Any], main_text: str) -> list[str]:
    return _three_column_errors(lr, main_text, generation="v3", expected_font="6.8pt/7.4pt")


def _annual_v4_errors(lr: dict[str, Any], main_text: str) -> list[str]:
    errors = _three_column_errors(lr, main_text, generation="v4", expected_font="6.0pt/6.5pt")
    if lr.get("annual_reference_pagination_v3") is not True:
        errors.append("Annual References pagination v4 must retain pagination v3 ancestry")
    return errors


def _annual_v5_errors(lr: dict[str, Any], main_text: str) -> list[str]:
    errors = _three_column_errors(lr, main_text, generation="v5", expected_font="6.0pt/6.5pt", ragged_command=r"\RaggedRight")
    if lr.get("annual_reference_pagination_v4") is not True or lr.get("annual_reference_pagination_v3") is not True:
        errors.append("Annual References pagination v5 must retain v3/v4 ancestry")
    if lr.get("references_columnsep") != "6pt":
        errors.append("Annual References pagination v5 must declare references_columnsep=6pt")
    if lr.get("references_raggedright_command") != "RaggedRight":
        errors.append("Annual References pagination v5 must declare RaggedRight")
    if lr.get("references_url_label_compacted") is not True:
        errors.append("Annual References pagination v5 must compact the URL label")
    if lr.get("references_urldate_label_compacted") is not True:
        errors.append("Annual References pagination v5 must compact the urldate label")
    if lr.get("references_metadata_values_changed") is not False:
        errors.append("Annual References pagination v5 must preserve reference metadata values")
    required = (
        r"\usepackage{ragged2e}",
        r"\DeclareFieldFormat{url}{\url{#1}}",
        r"\DeclareFieldFormat{urldate}{\mkbibparens{#1}}",
        r"\setlength{\columnsep}{6pt}",
    )
    for token in required:
        if token not in main_text:
            errors.append(f"declared Annual References pagination v5 source marker missing: {token}")
    return errors


def _annual_v6_errors(lr: dict[str, Any], main_text: str) -> list[str]:
    errors = _three_column_errors(lr, main_text, generation="v6", expected_font="6.0pt/6.5pt", ragged_command=r"\RaggedRight")
    if lr.get("annual_reference_pagination_v5") is not True or lr.get("annual_reference_pagination_v4") is not True or lr.get("annual_reference_pagination_v3") is not True:
        errors.append("Annual References pagination v6 must retain v3/v4/v5 ancestry")
    if lr.get("references_columnsep") != "6pt":
        errors.append("Annual References pagination v6 must declare references_columnsep=6pt")
    if lr.get("references_raggedright_command") != "RaggedRight":
        errors.append("Annual References pagination v6 must declare RaggedRight")
    if lr.get("references_url_label_compacted") is not True or lr.get("references_urldate_label_compacted") is not True:
        errors.append("Annual References pagination v6 must retain compact URL/urldate labels")
    if lr.get("references_metadata_values_changed") is not False:
        errors.append("Annual References pagination v6 must preserve reference metadata values")
    if lr.get("references_url_style") != "same":
        errors.append("Annual References pagination v6 must declare references_url_style=same")
    if lr.get("references_url_visible_value_changed") is not False:
        errors.append("Annual References pagination v6 must preserve visible URL values")
    if lr.get("references_url_hyperlink_target_changed") is not False:
        errors.append("Annual References pagination v6 must preserve URL hyperlink targets")
    for token in (r"\urlstyle{same}", r"\DeclareFieldFormat{url}{\url{#1}}", r"\DeclareFieldFormat{urldate}{\mkbibparens{#1}}"):
        if token not in main_text:
            errors.append(f"declared Annual References pagination v6 source marker missing: {token}")
    return errors


def _annual_v7_errors(lr: dict[str, Any], main_text: str) -> list[str]:
    errors = _annual_v6_errors(lr, main_text)
    if lr.get("annual_reference_pagination_v7_issue_refs") != [140]:
        errors.append("Annual References pagination v7 must be scoped to issue_refs=[140]")
    if lr.get("annual_reference_pagination_v6") is not True:
        errors.append("Annual References pagination v7 must retain pagination v6 ancestry")
    expected = {
        "annual_reference_heading_spacing_compacted": True,
        "references_needspace": "0.12textheight",
        "references_heading_preserved": True,
        "references_heading_toc_navigation": True,
        "references_heading_post_vspace": "-1.05baselineskip",
        "references_intro_pre_section_vspace": "-0.35em",
    }
    for key, value in expected.items():
        if lr.get(key) != value:
            errors.append(f"Annual References pagination v7 contract mismatch: {key}={value}")
    required = (
        r"\Needspace{0.12\textheight}",
        "% annual References compact final-heading spacing",
        r"\vspace{-0.35em}",
        r"\section*{References / Source Notes}",
        r"\addcontentsline{toc}{section}{References / Source Notes}",
        r"\vspace{-1.05\baselineskip}",
    )
    for token in required:
        if token not in main_text:
            errors.append(f"declared Annual References pagination v7 source marker missing: {token}")
    return errors


def declared_non_narrative_multicols(manifest: dict[str, Any], main_text: str) -> tuple[int, list[str]]:
    lr = manifest.get("layout_revision") or {}
    if lr.get("annual_final_reference_compaction") is not True:
        return _ORIGINAL_DECLARED_NON_NARRATIVE_MULTICOLS(manifest, main_text)
    if lr.get("annual_reference_pagination_v7") is True:
        errors = _annual_v7_errors(lr, main_text)
        return (1 if not errors else 0), errors
    if lr.get("annual_reference_pagination_v6") is True:
        errors = _annual_v6_errors(lr, main_text)
        return (1 if not errors else 0), errors
    if lr.get("annual_reference_pagination_v5") is True:
        errors = _annual_v5_errors(lr, main_text)
        return (1 if not errors else 0), errors
    if lr.get("annual_reference_pagination_v4") is True:
        errors = _annual_v4_errors(lr, main_text)
        return (1 if not errors else 0), errors
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


def inspect_layout(manifest: dict[str, Any], main_text: str, architecture: dict[str, Any]) -> list[str]:
    lr = manifest.get("layout_revision") or {}
    if lr.get("annual_reference_pagination_v7") is True:
        errors = _annual_v7_errors(lr, main_text)
    elif lr.get("annual_reference_pagination_v6") is True:
        errors = _annual_v6_errors(lr, main_text)
    elif lr.get("annual_reference_pagination_v5") is True:
        errors = _annual_v5_errors(lr, main_text)
    elif lr.get("annual_reference_pagination_v4") is True:
        errors = _annual_v4_errors(lr, main_text)
    elif lr.get("annual_reference_pagination_v3") is True:
        errors = _annual_v3_errors(lr, main_text)
    else:
        return _ORIGINAL_INSPECT_LAYOUT(manifest, main_text, architecture)
    if errors:
        return errors

    shim_manifest = copy.deepcopy(manifest)
    shim_lr = shim_manifest.setdefault("layout_revision", {})
    shim_lr["annual_reference_pagination_v7"] = False
    shim_lr["annual_reference_pagination_v6"] = False
    shim_lr["annual_reference_pagination_v5"] = False
    shim_lr["annual_reference_pagination_v4"] = False
    shim_lr["annual_reference_pagination_v3"] = False
    shim_lr["references_columns"] = 2
    shim_lr["references_columnsep"] = "8pt"
    shim_lr["references_raggedright_command"] = "raggedright"
    shim_text = main_text.replace(r"\begin{multicols}{3}", r"\begin{multicols}{2}", 1)
    shim_text = shim_text.replace(r"\RaggedRight", r"\raggedright", 1)
    shim_text = shim_text.replace(
        "% annual References compact final-heading spacing",
        "% annual References two-column final compaction",
        1,
    )
    return _ORIGINAL_INSPECT_LAYOUT(shim_manifest, shim_text, architecture)


_base.declared_non_narrative_multicols = declared_non_narrative_multicols
_base.inspect_layout = inspect_layout


def main() -> int:
    return _base.main()


if __name__ == "__main__":
    raise SystemExit(main())
