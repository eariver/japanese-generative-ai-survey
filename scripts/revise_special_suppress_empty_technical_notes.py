#!/usr/bin/env python3
"""Create a layout-only Special revision that omits empty Technical Notes sections.

Only packages explicitly named by the review marker may be changed. The target
Technical Notes file must have zero Evidence records and contain only the
reader-facing heading/table scaffold. Source files and Evidence remain intact;
only the corresponding input line is removed from main.tex.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    lifecycle = state.get("lifecycle_state")
    if lifecycle == "RELEASE_CANDIDATE":
        if gates.get("latex_build") != "passed":
            raise ValueError("RELEASE_CANDIDATE revision requires latex_build passed")
    elif lifecycle == "VALIDATED_DRAFT":
        if gates.get("claim_and_chronology_validation") != "passed" or gates.get("latex_build") != "pending":
            raise ValueError("VALIDATED_DRAFT revision requires validated content and pending latex_build")
    else:
        raise ValueError("empty-Technical-Notes revision requires VALIDATED_DRAFT or RELEASE_CANDIDATE")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("revision requires unapproved Visual Review and Freeze")

    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("layout marker mismatch")
    constraints = marker.get("constraints") or {}
    changes = marker.get("layout_changes") or {}
    if constraints.get("new_external_evidence_allowed") is not False:
        raise ValueError("layout marker must forbid new external evidence")
    if constraints.get("reader_content_changed") is not False:
        raise ValueError("empty Technical Notes suppression must be reader-content neutral")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("layout marker must remain selected-Evidence-only")
    if changes.get("suppress_zero_evidence_technical_notes") is not True:
        raise ValueError("suppress_zero_evidence_technical_notes marker is required")
    targets = changes.get("package_ids") or []
    if not isinstance(targets, list) or not targets or not all(isinstance(x, str) and x for x in targets):
        raise ValueError("layout marker package_ids must be a non-empty string array")

    current = dict(state.get("provenance", {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha(current_manifest_path) != current.get("sha256"):
        raise ValueError("current source digest mismatch")
    current_manifest = load_json(current_manifest_path)
    current_dir = current_manifest_path.parent
    out = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if out.exists():
        raise ValueError(f"revision already exists: {out}")
    shutil.copytree(current_dir, out)

    articles = [x for x in (current_manifest.get("articles") or []) if isinstance(x, dict)]
    by_id = {str(x.get("package_id") or ""): x for x in articles}
    missing = [x for x in targets if x not in by_id]
    if missing:
        raise ValueError(f"unknown package_ids: {missing}")

    main_info = dict(current_manifest.get("main_tex") or {})
    main_rel = str(main_info.get("path") or "main.tex")
    main_path = out / main_rel
    main_text = main_path.read_text(encoding="utf-8")
    suppressed: list[str] = []
    revised_articles: list[dict[str, Any]] = []

    for article in articles:
        updated = dict(article)
        package_id = str(article.get("package_id") or "")
        if package_id in targets:
            if int(article.get("evidence_record_count") or 0) != 0:
                raise ValueError(f"{package_id}: suppression requires evidence_record_count=0")
            notes_rel = str(article.get("technical_notes_path") or "")
            notes_path = out / notes_rel
            if not notes_rel or not notes_path.is_file():
                raise ValueError(f"{package_id}: Technical Notes file missing")
            if sha(notes_path) != article.get("technical_notes_sha256"):
                raise ValueError(f"{package_id}: Technical Notes digest mismatch")
            notes_text = notes_path.read_text(encoding="utf-8")
            if r"\begin{technicalnote}" in notes_text:
                raise ValueError(f"{package_id}: Technical Notes contains Evidence cards")
            if "Theme at a glance" not in notes_text or "\\midrule\n\\bottomrule" not in notes_text:
                raise ValueError(f"{package_id}: Technical Notes is not the expected empty scaffold")
            token = r"\input{" + Path(notes_rel).with_suffix("").as_posix() + "}"
            if main_text.count(token) != 1:
                raise ValueError(f"{package_id}: expected exactly one Technical Notes input")
            main_text = main_text.replace(token, f"% omitted empty Technical Notes for {package_id}", 1)
            updated["technical_notes_rendered"] = False
            updated["technical_notes_rendering_reason"] = "zero-evidence reader scaffold suppressed"
            suppressed.append(package_id)
        revised_articles.append(updated)

    if sorted(suppressed) != sorted(targets):
        raise ValueError("not all requested packages were suppressed")
    main_path.write_text(main_text, encoding="utf-8")

    new_manifest = dict(current_manifest)
    new_manifest["source_version"] = source_version
    new_manifest["status"] = "VALIDATED_EMPTY_TECHNICAL_NOTES_SUPPRESSION_REVISION"
    new_manifest["derivation"] = (
        "Layout-only revision of the prior validated source. Zero-Evidence Technical Notes scaffolds are omitted "
        "from main.tex; accepted article wording, Evidence files, Technical Notes files, chronology, and bibliography are unchanged."
    )
    new_manifest["basis"] = dict(current_manifest.get("basis") or {})
    new_manifest["basis"]["previous_source_manifest_path"] = current["path"]
    new_manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]
    main_info["path"] = main_rel
    main_info["sha256"] = sha(main_path)
    new_manifest["main_tex"] = main_info
    new_manifest["articles"] = revised_articles
    new_manifest["layout_revision"] = {
        "from_source_version": current_manifest.get("source_version"),
        "reader_content_changed": False,
        "new_external_evidence": False,
        "suppress_zero_evidence_technical_notes": True,
        "suppressed_package_ids": suppressed,
        "article_sections_changed": False,
        "technical_note_files_changed": False,
        "chronology_changed": False,
        "bibliography_data_changed": False,
        "main_tex_changed": True,
    }
    manifest_path = out / "source-manifest.json"
    write_json(manifest_path, new_manifest)
    manifest_sha = sha(manifest_path)

    history = state.setdefault("provenance_history", {})
    history.setdefault("validated_issue_source", []).append(current)
    prior_build = dict(state.get("provenance", {}).get("latex_build") or {})
    if prior_build:
        history.setdefault("latex_build", []).append(prior_build)
    state["lifecycle_state"] = "VALIDATED_DRAFT"
    state["gates"]["latex_build"] = "pending"
    state["gates"]["visual_review"] = "pending"
    state["gates"]["freeze"] = "pending"
    new_source = dict(current)
    new_source.update({
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": source_version,
        "layout_mode": "zero-evidence-technical-notes-suppressed",
        "layout_revision_sha256": sha(marker_path),
    })
    state["provenance"]["validated_issue_source"] = new_source
    state["provenance"].pop("latex_build", None)
    state["provenance"]["reader_layout_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": sha(marker_path),
        "reason": str(marker.get("reason") or "Suppress an empty Technical Notes scaffold discovered during Publication Preview review."),
    }
    write_json(state_path, state)

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "source_version": source_version,
        "previous_source_version": current_manifest.get("source_version"),
        "source_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "source_manifest_sha256": manifest_sha,
        "suppressed_package_ids": suppressed,
        "reader_content_changed": False,
        "new_external_evidence": False,
        "lifecycle_state": state["lifecycle_state"],
        "latex_build_gate": state["gates"]["latex_build"],
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root", default=".")
    p.add_argument("--special-slug", required=True)
    p.add_argument("--issue-id", required=True)
    p.add_argument("--source-version", required=True)
    args = p.parse_args()
    print(json.dumps(build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
