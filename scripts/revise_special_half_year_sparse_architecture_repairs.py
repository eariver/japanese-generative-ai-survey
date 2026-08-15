#!/usr/bin/env python3
"""Apply current Half-year review repairs when Architecture omitted dedicated synthesis/chronology packages.

Some early retrospective editions were architected with a normal concluding article and no
WATCHLIST_CHRONOLOGY package.  The current Half-year repair chain correctly assumes the newer
architecture, so those editions could not reuse its source-specific Technical Notes, cross-period
analysis, chronology, taxonomy, and References contracts.

This compatibility layer creates *temporary provenance aliases* only while the current v30 repair
chain runs:

* the existing ``conclusion`` article is presented as ``synthesis`` to the legacy structural pass;
* a synthetic chronology Draft Package aggregates the already-selected Evidence from all accepted
  Draft Packages (deduplicated by Evidence Task id);
* no external Evidence is introduced and no accepted Draft Package/Evidence Card is mutated.

The temporary parent manifest is restored byte-for-byte in ``finally``.  The immutable derived
revision is then normalized back to ``conclusion``, receives a reader-facing Detailed Chronology
input before References, section-level TOC cleanup, and generic Technical Notes tail protection.
The underlying source-specific Technical Notes enrichment remains the current v30 fail-closed
Screening-backed/entity-bound implementation.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v3 as structural
from scripts import revise_special_half_year_review_repairs_v30 as current
from scripts.special_technical_note_tail_policy import apply_generic_tail_policy, unprotected_tail_titles


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def _write(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _aggregate_selected_evidence(repo_root: Path, manifest: dict[str, Any], issue_id: str) -> dict[str, Any]:
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    source_packages: list[dict[str, str]] = []
    for article in manifest.get("articles") or []:
        if not isinstance(article, dict):
            continue
        rel = str(article.get("draft_package_path") or "").strip()
        if not rel:
            continue
        path = repo_root / rel
        if not path.is_file():
            raise ValueError(f"Draft Package missing while deriving chronology: {rel}")
        expected = str(article.get("draft_package_sha256") or "").strip()
        actual = _sha(path)
        if expected and expected != actual:
            raise ValueError(f"Draft Package digest mismatch while deriving chronology: {rel}")
        package = _load(path)
        source_packages.append({"path": rel, "sha256": actual})
        for record in structural.evidence_records(package):
            task_id = str(record.get("evidence_task_id") or "").strip()
            if not task_id:
                raise ValueError(f"Evidence record without evidence_task_id in {rel}")
            if task_id in seen:
                continue
            seen.add(task_id)
            records.append(deepcopy(record))
    if not records:
        raise ValueError("cannot derive Half-year chronology: no selected Evidence in accepted Draft Packages")
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "package_id": "chronology",
        "draft_source_mode": "DERIVED_SELECTED_EVIDENCE_AGGREGATE",
        "execution_stage": "PUBLICATION_PREVIEW_REPAIR",
        "basis": {
            "selected_evidence_only": True,
            "new_external_evidence": False,
            "source_draft_packages": source_packages,
        },
        "package": {
            "title": "Detailed Chronology",
            "package_type": "WATCHLIST_CHRONOLOGY",
            "editorial_angle": "Reader-facing compact chronology derived from already-selected Half-year Evidence.",
            "boundaries": [
                "Derived chronology preserves the selected Evidence boundary and does not convert attributed claims into independent reproduction."
            ],
        },
        "primary_evidence": records,
        "supporting_evidence": [],
    }


def _compat_insert_half_year_analysis(main_text: str, analysis_rel: str) -> str:
    if rf"\input{{{analysis_rel}}}" in main_text:
        raise ValueError("half-year analysis already present")
    # Older H1 architecture calls the final article 結論/総括 rather than Half-year Synthesis.
    pattern = re.compile(r"(\\clearpage\s*\n)(\\section\{総括[^\n]*\})")
    match = pattern.search(main_text)
    if not match:
        # Keep the newer contract available if this compatibility layer is reused on a mixed source.
        return structural.insert_half_year_analysis(main_text, analysis_rel)
    insertion = (
        r"\clearpage" + "\n"
        + rf"\input{{{analysis_rel}}}" + "\n\n"
        + r"\clearpage" + "\n"
        + match.group(2)
    )
    return main_text[: match.start()] + insertion + main_text[match.end() :]


def _insert_chronology_before_references(main_text: str, chronology_rel: str) -> str:
    needle = rf"\input{{{chronology_rel}}}"
    if needle in main_text:
        return main_text
    bib = r"\printbibliography[title={References / Source Notes}]"
    if main_text.count(bib) != 1:
        raise ValueError("expected one References bibliography command while inserting Detailed Chronology")
    block = (
        r"\clearpage" + "\n"
        + r"\section{Detailed Chronology}" + "\n"
        + r"\label{sec:detailed-chronology}" + "\n"
        + needle + "\n\n"
        + r"\clearpage" + "\n"
        + bib
    )
    return main_text.replace(bib, block, 1)


def _postprocess_revision(repo_root: Path, issue_id: str, result: dict[str, Any]) -> dict[str, Any]:
    manifest_rel = str(result.get("source_manifest") or "")
    manifest_path = repo_root / manifest_rel
    if not manifest_rel or not manifest_path.is_file():
        raise ValueError("Half-year compatibility repair returned no source manifest")
    manifest = _load(manifest_path)
    out = manifest_path.parent

    chronology_article: dict[str, Any] | None = None
    conclusion_count = 0
    for article in manifest.get("articles") or []:
        if not isinstance(article, dict):
            continue
        package_id = str(article.get("package_id") or "")
        if package_id == "synthesis" and article.get("_sparse_architecture_alias") is True:
            article["package_id"] = "conclusion"
            article.pop("_sparse_architecture_alias", None)
            conclusion_count += 1
        elif package_id == "chronology" and article.get("_sparse_architecture_derived") is True:
            chronology_article = article
            article.pop("draft_package_path", None)
            article.pop("draft_package_sha256", None)
            article.pop("technical_notes_path", None)
            article.pop("technical_notes_sha256", None)
            article["technical_notes_reader_facing"] = False
            article["derived_reader_layer"] = True
            article["derivation"] = "Deduplicated chronology from selected Evidence already present in accepted Draft Packages."
    if conclusion_count != 1:
        raise ValueError(f"expected one sparse-architecture synthesis alias, got {conclusion_count}")
    if chronology_article is None:
        raise ValueError("derived chronology article missing after Half-year repair")

    main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_path = out / main_rel
    main_text = main_path.read_text(encoding="utf-8")
    chronology_rel = str(chronology_article.get("layout_body_path") or "layout-bodies/chronology.tex")
    main_text = _insert_chronology_before_references(main_text, Path(chronology_rel).with_suffix("").as_posix())
    main_path.write_text(main_text, encoding="utf-8")

    toc_removed = 0
    tail_groups = 0
    tail_cards = 0
    rendered_notes = 0
    for article in manifest.get("articles") or []:
        if not isinstance(article, dict):
            continue
        rel = str(article.get("technical_notes_path") or "").strip()
        if not rel or article.get("technical_notes_reader_facing") is not True:
            continue
        path = out / rel
        if not path.is_file():
            raise ValueError(f"reader-facing Technical Notes file missing: {rel}")
        text = path.read_text(encoding="utf-8")
        text, removed = re.subn(r"^\\addcontentsline\{toc\}\{subsection\}\{Theme at a glance\}\s*$\n?", "", text, flags=re.MULTILINE)
        toc_removed += removed
        tail = apply_generic_tail_policy(text)
        if unprotected_tail_titles(tail.text):
            raise ValueError(f"unprotected Technical Notes tail after compatibility repair: {rel}")
        path.write_text(tail.text, encoding="utf-8")
        article["technical_notes_sha256"] = _sha(path)
        tail_groups += tail.groups_added
        tail_cards += tail.card_count
        rendered_notes += 1

    # Theme-at-a-glance can also be emitted in non-note article bodies/standfirsts.
    for subdir in ("layout-bodies", "layout-standfirsts", "sections"):
        root = out / subdir
        if not root.is_dir():
            continue
        for path in root.glob("*.tex"):
            text = path.read_text(encoding="utf-8")
            revised, removed = re.subn(r"^\\addcontentsline\{toc\}\{subsection\}\{Theme at a glance\}\s*$\n?", "", text, flags=re.MULTILINE)
            if removed:
                path.write_text(revised, encoding="utf-8")
                toc_removed += removed
                for article in manifest.get("articles") or []:
                    if not isinstance(article, dict):
                        continue
                    for path_key, sha_key in (("layout_body_path", "layout_body_sha256"), ("layout_standfirst_path", "layout_standfirst_sha256")):
                        if str(article.get(path_key) or "") == path.relative_to(out).as_posix():
                            article[sha_key] = _sha(path)

    layout = dict(manifest.get("layout") or {})
    layout["toc_depth"] = "section"
    layout["chronology_policy"] = "compact ascending dated event list derived across selected Half-year Evidence; undated reader rows suppressed"
    layout["technical_note_tail_policy"] = "source heading/URL/boundary tail kept with preceding card content where feasible"
    manifest["layout"] = layout

    reader = dict(manifest.get("reader_facing_technical_notes") or {})
    reader["tail_policy"] = "generic-card-tail-guard-v1"
    reader["tail_policy_groups_added"] = tail_groups
    reader["rendered_note_file_count"] = rendered_notes
    manifest["reader_facing_technical_notes"] = reader

    revision = dict(manifest.get("layout_revision") or {})
    revision.update(
        {
            "sparse_half_year_architecture_compatibility": True,
            "sparse_half_year_architecture_contract": "DERIVED_CHRONOLOGY_AND_CONCLUSION_ALIAS_SELECTED_EVIDENCE_ONLY_V1",
            "reader_content_changed": True,
            "new_external_evidence": False,
            "accepted_article_sections_changed": False,
            "evidence_cards_changed": False,
            "compact_detailed_chronology_inserted": True,
            "chronology_undated_reader_rows_allowed": False,
            "chronology_sort_order": "event_date_ascending",
            "theme_at_a_glance_toc_entries_removed": toc_removed,
            "technical_note_tail_groups_added": tail_groups,
            "technical_note_card_count": tail_cards,
        }
    )
    manifest["layout_revision"] = revision
    manifest["main_tex"] = {"path": main_rel, "sha256": _sha(main_path)}

    _write(manifest_path, manifest)
    manifest_sha = _sha(manifest_path)
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = _load(state_path)
    source = (state.get("provenance") or {}).get("validated_issue_source") or {}
    if str(source.get("path") or "") != manifest_rel:
        raise ValueError("state/source mismatch after sparse Half-year compatibility repair")
    source["sha256"] = manifest_sha
    _write(state_path, state)

    result = dict(result)
    result.update(
        {
            "source_manifest_sha256": manifest_sha,
            "sparse_half_year_architecture_compatibility": True,
            "compact_detailed_chronology_inserted": True,
            "theme_at_a_glance_toc_entries_removed": toc_removed,
            "technical_note_tail_groups_added": tail_groups,
            "technical_note_card_count": tail_cards,
        }
    )
    return result


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = _load(marker_path)
    changes = marker.get("layout_changes") or {}
    if changes.get("sparse_half_year_architecture_repairs") is not True:
        raise ValueError("marker does not request sparse_half_year_architecture_repairs")
    if changes.get("half_year_review_repairs_v3") is not True:
        raise ValueError("sparse Half-year compatibility requires current half_year_review_repairs_v3 chain")

    constraints = marker.get("constraints") or {}
    if constraints.get("new_external_evidence_allowed") is not False or constraints.get("selected_evidence_only") is not True:
        raise ValueError("sparse Half-year compatibility must remain selected-Evidence-only")
    if constraints.get("accepted_article_claims_changed") is not False or constraints.get("evidence_cards_mutated") is not False:
        raise ValueError("sparse Half-year compatibility cannot mutate accepted Draft claims or Evidence cards")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = _load(state_path)
    current_source = deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    parent_manifest_path = repo_root / str(current_source.get("path") or "")
    if not parent_manifest_path.is_file() or _sha(parent_manifest_path) != str(current_source.get("sha256") or ""):
        raise ValueError("state-pinned parent source manifest mismatch")
    parent_bytes = parent_manifest_path.read_bytes()
    parent_manifest = _load(parent_manifest_path)

    articles = parent_manifest.get("articles") or []
    if any(str(a.get("package_id") or "") == "chronology" for a in articles if isinstance(a, dict)):
        raise ValueError("sparse Half-year compatibility is only for sources without a chronology package")
    conclusion = next((a for a in articles if isinstance(a, dict) and str(a.get("package_id") or "") == "conclusion"), None)
    if conclusion is None:
        raise ValueError("sparse Half-year compatibility requires a conclusion article")

    aggregate = _aggregate_selected_evidence(repo_root, parent_manifest, issue_id)
    with tempfile.TemporaryDirectory(prefix="half-year-sparse-") as tmp:
        temp_package = Path(tmp) / "chronology.json"
        _write(temp_package, aggregate)
        # chronology_records resolves paths against repo_root, so place a temporary file beneath
        # repo_root and remove it in finally.  It is never committed or retained as provenance.
        temp_rel = f"sources/{issue_id}/editorial/.derived-chronology-{source_version}.tmp.json"
        temp_repo_package = repo_root / temp_rel
        _write(temp_repo_package, aggregate)

        synthetic = {
            "package_id": "chronology",
            "draft_package_path": temp_rel,
            "draft_package_sha256": _sha(temp_repo_package),
            "layout_body_path": "layout-bodies/chronology.tex",
            "technical_notes_path": "",
            "technical_notes_reader_facing": False,
            "_sparse_architecture_derived": True,
        }
        conclusion["package_id"] = "synthesis"
        conclusion["_sparse_architecture_alias"] = True
        articles.append(synthetic)
        _write(parent_manifest_path, parent_manifest)

        original_insert = structural.insert_half_year_analysis
        original_remove = structural.remove_article_notes_input

        def compat_remove(main_text: str, technical_notes_path: str) -> str:
            if not str(technical_notes_path or "").strip():
                return main_text
            return original_remove(main_text, technical_notes_path)

        structural.insert_half_year_analysis = _compat_insert_half_year_analysis
        structural.remove_article_notes_input = compat_remove
        try:
            result = current.build(repo_root, special_slug, issue_id, source_version)
        finally:
            structural.insert_half_year_analysis = original_insert
            structural.remove_article_notes_input = original_remove
            parent_manifest_path.write_bytes(parent_bytes)
            temp_repo_package.unlink(missing_ok=True)

    return _postprocess_revision(repo_root, issue_id, result)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
