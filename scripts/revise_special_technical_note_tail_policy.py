#!/usr/bin/env python3
"""Create an immutable Special revision with generic Technical Notes tail grouping."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from scripts.special_technical_note_tail_policy import (
    apply_generic_tail_policy,
    unprotected_tail_titles,
)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("Technical Notes tail-policy marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("generic_technical_note_tail_policy") is not True:
        raise ValueError("layout marker does not request generic_technical_note_tail_policy")
    constraints = marker.get("constraints") or {}
    if constraints.get("new_external_evidence_allowed") is not False:
        raise ValueError("tail-policy revision must forbid new external Evidence")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("tail-policy revision must remain selected-Evidence-only")
    if constraints.get("reader_content_changed") is not False:
        raise ValueError("tail-policy revision must not change reader wording")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise ValueError("tail-policy revision requires RELEASE_CANDIDATE")
    if gates.get("latex_build") != "passed":
        raise ValueError("tail-policy revision requires a successful prior PDF build")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("tail-policy revision requires Visual Review and Freeze pending")

    current = dict(state.get("provenance", {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha(current_manifest_path) != current.get("sha256"):
        raise ValueError("current validated source manifest digest mismatch")
    current_manifest = load_json(current_manifest_path)

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(current_manifest_path.parent, output_dir)

    new_manifest = dict(current_manifest)
    articles = [dict(article) for article in current_manifest.get("articles") or []]
    new_manifest["articles"] = articles
    changed_files: list[str] = []
    groups_added = 0
    card_count = 0
    protected_card_count = 0

    for article in articles:
        rel = str(article.get("technical_notes_path") or "")
        if not rel:
            continue
        path = output_dir / rel
        if not path.is_file():
            raise ValueError(f"Technical Notes missing: {rel}")
        original = path.read_text(encoding="utf-8")
        result = apply_generic_tail_policy(original)
        revised = result.text
        groups_added += result.groups_added
        card_count += result.card_count
        protected_card_count += result.protected_card_count
        unprotected = unprotected_tail_titles(revised)
        if unprotected:
            raise ValueError(f"{rel}: unprotected Technical Notes tail(s): {unprotected}")
        if revised != original:
            path.write_text(revised, encoding="utf-8")
            changed_files.append(rel)
        article["technical_notes_sha256"] = sha(path)

    if card_count < 1:
        raise ValueError("tail-policy revision found no Technical Notes cards")
    if groups_added < 1:
        raise ValueError("tail-policy revision added no generic groups")
    if protected_card_count != card_count:
        raise ValueError(
            f"tail-policy coverage incomplete: protected={protected_card_count} cards={card_count}"
        )

    new_manifest["source_version"] = source_version
    new_manifest["status"] = "VALIDATED_TECHNICAL_NOTE_TAIL_POLICY_REVISION"
    new_manifest["derivation"] = (
        "Layout-only revision of the prior Human Visual Review candidate. Every Technical Notes card "
        "keeps its reader boundary/limitation and primary-source block together while the whole card "
        "remains breakable. Reader wording, selected Evidence, accepted Article Drafts, bibliography, "
        "TOC, mixed layout, and all other source bytes are inherited unchanged."
    )
    new_manifest["basis"] = dict(current_manifest.get("basis") or {})
    new_manifest["basis"]["previous_source_manifest_path"] = current["path"]
    new_manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]

    reader = dict(new_manifest.get("reader_facing_technical_notes") or {})
    reader.update(
        {
            "whole_card_unbreakable": False,
            "generic_boundary_source_tail_group": True,
            "generic_boundary_source_tail_scope": (
                "all Technical Notes cards: reader boundary + limitation + primary-source block"
            ),
            "generic_boundary_source_tail_validation": "all cards protected; no title allowlist",
            "generic_boundary_source_tail_card_count": card_count,
            "generic_boundary_source_tail_protected_card_count": protected_card_count,
        }
    )
    new_manifest["reader_facing_technical_notes"] = reader

    previous_layout_revision = dict(current_manifest.get("layout_revision") or {})
    previous_layout_revision.update(
        {
            "from_source_version": current_manifest.get("source_version"),
            "generic_technical_note_tail_policy": True,
            "reader_content_changed": False,
            "new_external_evidence": False,
            "selected_evidence_only": True,
            "technical_notes_files_changed": changed_files,
            "technical_note_card_count": card_count,
            "generic_tail_groups_added": groups_added,
            "generic_tail_protected_card_count": protected_card_count,
            "title_allowlist_required": False,
        }
    )
    new_manifest["layout_revision"] = previous_layout_revision

    manifest_path = output_dir / "source-manifest.json"
    write_json(manifest_path, new_manifest)
    manifest_sha = sha(manifest_path)

    history = state.setdefault("provenance_history", {})
    history.setdefault("validated_issue_source", []).append(current)
    previous_build = dict(state.get("provenance", {}).get("latex_build") or {})
    if previous_build:
        history.setdefault("latex_build", []).append(previous_build)
    state["lifecycle_state"] = "VALIDATED_DRAFT"
    state["gates"]["latex_build"] = "pending"
    state["gates"]["visual_review"] = "pending"
    state["gates"]["freeze"] = "pending"
    state["provenance"]["validated_issue_source"] = {
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": source_version,
        "layout_mode": "balanced-local-multicol-generic-technical-note-tail-policy",
        "layout_revision_sha256": sha(marker_path),
    }
    state["provenance"].pop("latex_build", None)
    state["provenance"]["reader_layout_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": sha(marker_path),
        "reason": str(marker.get("reason") or "Apply generic Technical Notes tail grouping after Human Visual Review."),
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
        "technical_notes_files_changed": changed_files,
        "technical_note_card_count": card_count,
        "generic_tail_groups_added": groups_added,
        "generic_tail_protected_card_count": protected_card_count,
        "reader_content_changed": False,
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
    print(
        json.dumps(
            build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version),
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
