#!/usr/bin/env python3
"""Create an immutable Half-year reader-surface quality cleanup revision.

The pass is designed for a fully evidence-validated Special whose PDF visual review exposed only
reader-surface defects. It does not alter Evidence cards, accepted Article Drafts, Half-year analysis,
Detailed Chronology event content, citations, or bibliography data. It may:

* remove an exact technical-point suffix accidentally appended twice to a Technical Notes fact;
* render undated reader chronology metadata explicitly instead of a bare dash and sort date lists;
* add a Needspace guard before each reader-facing Technical Notes card;
* compact bibliography typography from footnote to script size.
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

TECH_BEGIN = r"\begin{technicalnote}"
NEEDSPACE = r"\Needspace{0.38\textheight}"
DATE_LIST_RE = re.compile(r"\d{4}-\d{2}-\d{2}(?:,\s*\d{4}-\d{2}-\d{2})+")
FACT_RE = re.compile(r"^(\\item \\textbf\{一次情報で確認できる事実\}: )(.*)$", re.MULTILINE)


def _dedup_fact_payload(payload: str) -> tuple[str, int]:
    """Remove only an exact repeated suffix separated from its first copy by whitespace."""
    current = payload
    removed = 0
    for match in list(re.finditer(r"\s+", current)):
        suffix = current[match.end():].strip()
        prefix = current[:match.start()].rstrip()
        if len(suffix) < 24:
            continue
        if prefix.endswith(suffix):
            current = prefix
            removed += 1
            break
    return current, removed


def _dedup_facts(text: str) -> tuple[str, int]:
    count = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal count
        payload, removed = _dedup_fact_payload(match.group(2))
        count += removed
        return match.group(1) + payload

    return FACT_RE.sub(repl, text), count


def _normalize_chronology_metadata(text: str) -> tuple[str, int, int]:
    dash_replacements = 0
    sorted_lists = 0
    lines: list[str] = []
    for line in text.splitlines(keepends=True):
        original = line
        # Card metadata rows and Theme-at-a-glance chronology cells use the same reader-facing
        # vocabulary. Replace only an isolated chronology dash, never arbitrary em dashes in prose.
        if "時系列" in line:
            revised = re.sub(r"(&\s*)—(\s*\\\\)", r"\1年表対象日付なし\2", line)
            if revised != line:
                dash_replacements += 1
                line = revised
        elif " & — " in line and line.rstrip().endswith(r"\\"):
            line = line.replace(" & — ", " & 年表対象日付なし ", 1)
            dash_replacements += 1

        def sort_dates(match: re.Match[str]) -> str:
            nonlocal sorted_lists
            raw = match.group(0)
            dates = [part.strip() for part in raw.split(",")]
            ordered = sorted(dates)
            rendered = ", ".join(ordered)
            if rendered != raw:
                sorted_lists += 1
            return rendered

        line = DATE_LIST_RE.sub(sort_dates, line)
        lines.append(line)
    return "".join(lines), dash_replacements, sorted_lists


def _guard_cards(text: str) -> tuple[str, int]:
    begins = text.count(TECH_BEGIN)
    if begins == 0:
        return text, 0
    # Idempotently strip our exact guard before rebuilding one guard per card.
    text = text.replace(NEEDSPACE + "\n" + TECH_BEGIN, TECH_BEGIN)
    revised = text.replace(TECH_BEGIN, NEEDSPACE + "\n" + TECH_BEGIN)
    if revised.count(NEEDSPACE) != begins:
        raise ValueError("Technical Notes Needspace cardinality mismatch")
    return revised, begins


def _ensure_needspace_package(main: str) -> str:
    token = r"\usepackage{needspace}"
    if token in main:
        return main
    anchor = r"\usepackage{multicol}"
    if anchor not in main:
        raise ValueError("cannot add needspace: multicol package anchor missing")
    return main.replace(anchor, anchor + "\n" + token, 1)


def _compact_references(main: str) -> tuple[str, bool]:
    marker = "% half-year final bibliography compaction"
    at = main.find(marker)
    if at < 0:
        raise ValueError("v0.6 bibliography compaction marker missing")
    tail = main[at:]
    if r"\scriptsize" in tail.split(r"\endgroup", 1)[0]:
        return main, False
    target = r"\footnotesize"
    segment = tail.split(r"\endgroup", 1)[0]
    if segment.count(target) != 1:
        raise ValueError("expected one footnotesize bibliography command")
    revised_segment = segment.replace(target, r"\scriptsize", 1)
    return main[:at] + revised_segment + tail[len(segment):], True


def _validate_marker(marker: dict[str, Any], issue_id: str, source_version: str) -> None:
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("reader-quality marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("half_year_reader_quality_cleanup") is not True:
        raise ValueError("marker does not request half_year_reader_quality_cleanup")
    constraints = marker.get("constraints") or {}
    for key in (
        "new_external_evidence_allowed",
        "accepted_article_claims_changed",
        "evidence_cards_mutated",
        "half_year_analysis_content_changed",
        "chronology_event_content_changed",
        "bibliography_data_changed",
    ):
        if constraints.get(key) is not False:
            raise ValueError(f"reader-quality cleanup requires {key}=false")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("reader-quality cleanup must remain selected-Evidence-only")


def _reset_pdf_gate(state: dict[str, Any]) -> None:
    gates = state.get("gates") or {}
    lifecycle = str(state.get("lifecycle_state") or "")
    if lifecycle == "RELEASE_CANDIDATE":
        old_build = deepcopy((state.get("provenance") or {}).get("latex_build") or {})
        if not old_build:
            raise ValueError("RELEASE_CANDIDATE has no prior latex_build provenance")
        state.setdefault("provenance_history", {}).setdefault("latex_build", []).append(old_build)
        state.setdefault("provenance", {}).pop("latex_build", None)
    elif lifecycle != "VALIDATED_DRAFT":
        raise ValueError(f"reader-quality cleanup requires RELEASE_CANDIDATE or VALIDATED_DRAFT, got {lifecycle}")
    state["lifecycle_state"] = "VALIDATED_DRAFT"
    gates["latex_build"] = "pending"
    gates["visual_review"] = "pending"
    gates["freeze"] = "pending"


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = visual.load_json(marker_path)
    _validate_marker(marker, issue_id, source_version)

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = visual.load_json(state_path)
    if state.get("gates", {}).get("claim_and_chronology_validation") != "passed":
        raise ValueError("reader-quality cleanup requires passed claim/chronology validation")
    if state.get("gates", {}).get("visual_review") != "pending" or state.get("gates", {}).get("freeze") != "pending":
        raise ValueError("reader-quality cleanup cannot run after Visual Review or Freeze")

    current = deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    parent_manifest_path = repo_root / str(current.get("path") or "")
    if not parent_manifest_path.is_file() or visual.sha(parent_manifest_path) != str(current.get("sha256") or ""):
        raise ValueError("state-pinned parent source manifest missing or SHA mismatch")
    parent_manifest = visual.load_json(parent_manifest_path)
    if parent_manifest.get("source_version") == source_version:
        raise ValueError("reader-quality cleanup must create a new immutable source version")
    reader = parent_manifest.get("reader_facing_technical_notes") or {}
    if reader.get("generic_fallback_findings") != 0:
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

    total_cards = 0
    duplicate_suffixes_removed = 0
    chronology_dash_replacements = 0
    chronology_date_lists_sorted = 0
    note_files_changed = 0
    for article in manifest.get("articles") or []:
        if not isinstance(article, dict):
            continue
        rel = str(article.get("technical_notes_path") or "")
        if not rel:
            continue
        path = output_dir / rel
        if not path.is_file():
            raise ValueError(f"Technical Notes missing: {rel}")
        original = path.read_text(encoding="utf-8")
        text, removed = _dedup_facts(original)
        duplicate_suffixes_removed += removed
        text, dash_count, sort_count = _normalize_chronology_metadata(text)
        chronology_dash_replacements += dash_count
        chronology_date_lists_sorted += sort_count
        text, cards = _guard_cards(text)
        total_cards += cards
        if text != original:
            path.write_text(text, encoding="utf-8")
            note_files_changed += 1
        article["technical_notes_sha256"] = visual.sha(path)

    if duplicate_suffixes_removed < 1:
        raise ValueError("reader-quality cleanup expected at least one duplicated technical-point suffix")
    if chronology_dash_replacements < 1:
        raise ValueError("reader-quality cleanup expected at least one undated chronology reader cell")
    if chronology_date_lists_sorted < 1:
        raise ValueError("reader-quality cleanup expected at least one nonascending reader date list")
    if total_cards < 1:
        raise ValueError("reader-quality cleanup found no Technical Notes cards")

    # Fail closed on the two #54 patterns after normalization.
    for article in manifest.get("articles") or []:
        if not isinstance(article, dict):
            continue
        rel = str(article.get("technical_notes_path") or "")
        if not rel:
            continue
        text = (output_dir / rel).read_text(encoding="utf-8")
        if re.search(r"時系列\s*&\s*—\s*\\\\", text):
            raise ValueError(f"bare chronology dash remains: {rel}")
        for match in DATE_LIST_RE.finditer(text):
            dates = [part.strip() for part in match.group(0).split(",")]
            if dates != sorted(dates):
                raise ValueError(f"nonascending chronology date list remains: {rel}: {match.group(0)}")
        if text.count(NEEDSPACE) != text.count(TECH_BEGIN):
            raise ValueError(f"Needspace/card count mismatch after cleanup: {rel}")

    main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_path = output_dir / main_rel
    main = main_path.read_text(encoding="utf-8")
    main = _ensure_needspace_package(main)
    main, references_compacted = _compact_references(main)
    main_path.write_text(main, encoding="utf-8")
    manifest["main_tex"] = {"path": main_rel, "sha256": visual.sha(main_path)}

    lr = dict(manifest.get("layout_revision") or {})
    lr.update(
        {
            "from_source_version": parent_manifest.get("source_version"),
            "half_year_reader_quality_cleanup": True,
            "reader_quality_issue_refs": [54, 55, 139, 140],
            "reader_quality_semantic_source_changed": False,
            "new_external_evidence": False,
            "selected_evidence_only": True,
            "accepted_article_sections_changed": False,
            "evidence_cards_changed": False,
            "half_year_analysis_changed_by_reader_quality_cleanup": False,
            "chronology_event_content_changed": False,
            "bibliography_data_changed": False,
            "technical_note_files_changed": note_files_changed,
            "technical_note_card_needspace_guards": total_cards,
            "technical_note_duplicate_suffixes_removed": duplicate_suffixes_removed,
            "chronology_dash_replacements": chronology_dash_replacements,
            "chronology_date_lists_sorted": chronology_date_lists_sorted,
            "references_entry_font": "scriptsize",
            "references_bibitemsep": "0pt",
            "references_typography_compacted": references_compacted,
        }
    )
    manifest["layout_revision"] = lr
    visual.write_json(manifest_path, manifest)
    manifest_sha = visual.sha(manifest_path)

    state.setdefault("provenance_history", {}).setdefault("validated_issue_source", []).append(current)
    next_source = deepcopy(current)
    next_source.update(
        {
            "path": manifest_path.relative_to(repo_root).as_posix(),
            "sha256": manifest_sha,
            "source_version": source_version,
        }
    )
    state.setdefault("provenance", {})["validated_issue_source"] = next_source
    state["provenance"]["reader_quality_cleanup_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": visual.sha(marker_path),
        "technical_note_card_needspace_guards": total_cards,
        "technical_note_duplicate_suffixes_removed": duplicate_suffixes_removed,
        "chronology_dash_replacements": chronology_dash_replacements,
        "chronology_date_lists_sorted": chronology_date_lists_sorted,
        "references_entry_font": "scriptsize",
        "reader_semantic_source_changed": False,
    }
    _reset_pdf_gate(state)
    visual.write_json(state_path, state)

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "source_version": source_version,
        "previous_source_version": parent_manifest.get("source_version"),
        "source_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "source_manifest_sha256": manifest_sha,
        "technical_note_card_needspace_guards": total_cards,
        "technical_note_duplicate_suffixes_removed": duplicate_suffixes_removed,
        "chronology_dash_replacements": chronology_dash_replacements,
        "chronology_date_lists_sorted": chronology_date_lists_sorted,
        "references_entry_font": "scriptsize",
        "reader_semantic_source_changed": False,
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
