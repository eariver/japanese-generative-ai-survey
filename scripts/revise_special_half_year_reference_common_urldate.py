#!/usr/bin/env python3
"""Create an immutable layout-only Half-year common access-date consolidation.

All bibliography data remains byte-identical. This pass first proves that every bibliography entry
has the same ``urldate`` and then suppresses the repeated per-entry display at render time while
stating the common access date once in the reader-facing References introduction.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts import revise_special_visual_review_repairs as visual

ENTRY_RE = re.compile(r"@\w+\{.*?\n\}", re.DOTALL)
URLDATE_RE = re.compile(r"\n\s*urldate\s*=\s*\{([^}]*)\},")
OLD_INTRO = (
    r"\noindent{\small\textit{以下のReferencesは本号のchronology・技術確認・横断分析に用いた一次資料である。"
    r"各entryでは識別・追跡に必要な資料名、組織、URL、参照日を示す。}}\par"
)
HOOK_MARKER = "% half-year common References access date"
PRINT_BIB = r"\printbibliography[heading=none]"


def common_urldate(bib_text: str) -> tuple[str, int]:
    entries = ENTRY_RE.findall(bib_text)
    if not entries:
        raise ValueError("bibliography has no entries")
    dates: list[str] = []
    for index, entry in enumerate(entries, start=1):
        match = URLDATE_RE.search(entry)
        if match is None:
            raise ValueError(f"bibliography entry {index} has no urldate")
        dates.append(match.group(1).strip())
    unique = sorted(set(dates))
    if len(unique) != 1:
        raise ValueError(f"bibliography urldate is not common: {unique}")
    return unique[0], len(entries)


def rewrite_main(main_path: Path, access_date: str) -> bool:
    text = main_path.read_text(encoding="utf-8")
    if HOOK_MARKER in text:
        return False
    if text.count(OLD_INTRO) != 1:
        raise ValueError("expected v0.9 References introduction not found exactly once")
    if text.count(PRINT_BIB) != 1:
        raise ValueError("expected exactly one printbibliography")
    new_intro = (
        r"\noindent{\small\textit{以下のReferencesは本号のchronology・技術確認・横断分析に用いた一次資料である。"
        r"各entryでは識別・追跡に必要な資料名、組織、URLを示す。全URLの参照日は"
        + access_date
        + r"である。}}\par"
    )
    hook = (
        HOOK_MARKER
        + "\n"
        + r"\AtEveryBibitem{\clearfield{urldate}\clearfield{urlyear}\clearfield{urlmonth}\clearfield{urlday}}"
        + "\n"
        + PRINT_BIB
    )
    revised = text.replace(OLD_INTRO, new_intro, 1).replace(PRINT_BIB, hook, 1)
    if access_date not in revised or revised.count(HOOK_MARKER) != 1:
        raise ValueError("common urldate rewrite failed")
    main_path.write_text(revised, encoding="utf-8")
    return True


def validate_marker(marker: dict[str, Any], issue_id: str, source_version: str) -> None:
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("common-urldate marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("half_year_reference_common_urldate_consolidation") is not True:
        raise ValueError("marker does not request common urldate consolidation")
    constraints = marker.get("constraints") or {}
    for key in (
        "new_external_evidence_allowed",
        "accepted_article_claims_changed",
        "evidence_cards_mutated",
        "technical_notes_content_changed",
        "half_year_analysis_content_changed",
        "chronology_event_content_changed",
        "bibliography_data_changed",
    ):
        if constraints.get(key) is not False:
            raise ValueError(f"common urldate consolidation requires {key}=false")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("common urldate consolidation must remain selected-Evidence-only")


def reset_pdf_gate(state: dict[str, Any]) -> None:
    gates = state.get("gates") or {}
    lifecycle = str(state.get("lifecycle_state") or "")
    if lifecycle == "RELEASE_CANDIDATE":
        old_build = deepcopy((state.get("provenance") or {}).get("latex_build") or {})
        if not old_build:
            raise ValueError("RELEASE_CANDIDATE has no prior latex_build provenance")
        state.setdefault("provenance_history", {}).setdefault("latex_build", []).append(old_build)
        state.setdefault("provenance", {}).pop("latex_build", None)
    elif lifecycle != "VALIDATED_DRAFT":
        raise ValueError(f"common urldate consolidation requires RELEASE_CANDIDATE or VALIDATED_DRAFT, got {lifecycle}")
    state["lifecycle_state"] = "VALIDATED_DRAFT"
    gates["latex_build"] = "pending"
    gates["visual_review"] = "pending"
    gates["freeze"] = "pending"


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = visual.load_json(marker_path)
    validate_marker(marker, issue_id, source_version)
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = visual.load_json(state_path)
    if state.get("gates", {}).get("claim_and_chronology_validation") != "passed":
        raise ValueError("common urldate consolidation requires passed claim/chronology validation")
    if state.get("gates", {}).get("visual_review") != "pending" or state.get("gates", {}).get("freeze") != "pending":
        raise ValueError("common urldate consolidation cannot run after Visual Review or Freeze")

    current = deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    parent_manifest_path = repo_root / str(current.get("path") or "")
    if not parent_manifest_path.is_file() or visual.sha(parent_manifest_path) != str(current.get("sha256") or ""):
        raise ValueError("state-pinned parent source manifest missing or SHA mismatch")
    parent_manifest = visual.load_json(parent_manifest_path)
    if parent_manifest.get("source_version") == source_version:
        raise ValueError("common urldate consolidation must create a new immutable source version")
    parent_lr = parent_manifest.get("layout_revision") or {}
    if parent_lr.get("half_year_reference_raggedright_compaction") is not True:
        raise ValueError("common urldate consolidation requires validated ragged-right References lineage")
    if (parent_manifest.get("reader_facing_technical_notes") or {}).get("generic_fallback_findings") != 0:
        raise ValueError("parent must have zero generic Technical Notes fallbacks")

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(parent_manifest_path.parent, output_dir)
    manifest_path = output_dir / "source-manifest.json"
    manifest = visual.load_json(manifest_path)
    manifest["source_version"] = source_version
    basis = dict(manifest.get("basis") or {})
    basis["previous_source_manifest_path"] = str(current.get("path") or "")
    basis["previous_source_manifest_sha256"] = str(current.get("sha256") or "")
    manifest["basis"] = basis

    references_rel = str((manifest.get("references") or {}).get("path") or "references.bib")
    references_path = output_dir / references_rel
    references_sha = visual.sha(references_path)
    access_date, entry_count = common_urldate(references_path.read_text(encoding="utf-8"))
    main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_path = output_dir / main_rel
    changed = rewrite_main(main_path, access_date)
    if visual.sha(references_path) != references_sha:
        raise ValueError("common urldate consolidation changed bibliography data")
    manifest["main_tex"] = {"path": main_rel, "sha256": visual.sha(main_path)}

    lr = dict(manifest.get("layout_revision") or {})
    lr.update({
        "from_source_version": parent_manifest.get("source_version"),
        "half_year_reference_common_urldate_consolidation": True,
        "reference_common_urldate_issue_refs": [140],
        "reference_common_urldate_reader_semantic_content_changed": False,
        "new_external_evidence": False,
        "selected_evidence_only": True,
        "accepted_article_sections_changed": False,
        "evidence_cards_changed": False,
        "technical_notes_changed_by_common_urldate": False,
        "half_year_analysis_changed_by_common_urldate": False,
        "chronology_event_content_changed": False,
        "bibliography_data_changed": False,
        "bibliography_sha256_before": references_sha,
        "bibliography_sha256_after": visual.sha(references_path),
        "bibliography_entry_count": entry_count,
        "common_urldate": access_date,
        "common_urldate_entry_count": entry_count,
        "per_entry_urldate_render_suppressed": True,
        "references_columns": 2,
        "references_raggedright": True,
        "references_layout_changed": changed,
    })
    manifest["layout_revision"] = lr
    visual.write_json(manifest_path, manifest)
    manifest_sha = visual.sha(manifest_path)

    state.setdefault("provenance_history", {}).setdefault("validated_issue_source", []).append(current)
    next_source = deepcopy(current)
    next_source.update({
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": source_version,
    })
    state.setdefault("provenance", {})["validated_issue_source"] = next_source
    state["provenance"]["reference_common_urldate_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": visual.sha(marker_path),
        "bibliography_sha256": references_sha,
        "bibliography_entry_count": entry_count,
        "common_urldate": access_date,
        "reader_semantic_content_changed": False,
    }
    reset_pdf_gate(state)
    visual.write_json(state_path, state)
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "source_version": source_version,
        "previous_source_version": parent_manifest.get("source_version"),
        "source_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "source_manifest_sha256": manifest_sha,
        "bibliography_sha256": references_sha,
        "bibliography_entry_count": entry_count,
        "common_urldate": access_date,
        "per_entry_urldate_render_suppressed": True,
        "reader_semantic_content_changed": False,
        "new_external_evidence": False,
        "lifecycle_state": state["lifecycle_state"],
        "latex_build_gate": state["gates"]["latex_build"],
        "visual_review_gate": state["gates"]["visual_review"],
        "freeze_gate": state["gates"]["freeze"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    print(json.dumps(build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
