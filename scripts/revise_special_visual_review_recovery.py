#!/usr/bin/env python3
"""Recover an immutable Special Visual Review revision after a failed PDF compile.

This recovery pass is intentionally narrow: it operates only on a validated derived
Visual Review source whose PDF build is still pending, removes TeX-invalid empty list
artifacts introduced by presentation-only tail grouping, and creates a new immutable
source revision. Evidence and accepted Article Draft sources are never mutated.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any


EMPTY_ITEMIZE_RE = re.compile(
    r"\\begin\{itemize\}(?:\[[^\]]*\])?\s*\\end\{itemize\}\s*",
    re.MULTILINE,
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
        raise ValueError("visual-review recovery marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("visual_review_recovery") is not True:
        raise ValueError("layout marker does not request visual_review_recovery")
    constraints = marker.get("constraints") or {}
    if constraints.get("new_external_evidence_allowed") is not False:
        raise ValueError("visual-review recovery must forbid new external Evidence")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("visual-review recovery must remain selected-Evidence-only")
    if constraints.get("reader_content_changed") is not False:
        raise ValueError("visual-review recovery must be reader-content-neutral")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "VALIDATED_DRAFT":
        raise ValueError("visual-review recovery requires VALIDATED_DRAFT after failed build")
    if gates.get("claim_and_chronology_validation") != "passed":
        raise ValueError("claim/chronology validation must remain passed")
    if gates.get("latex_build") != "pending":
        raise ValueError("visual-review recovery requires latex_build pending")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("Visual Review and Freeze must remain pending")

    current = dict(state.get("provenance", {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha(current_manifest_path) != current.get("sha256"):
        raise ValueError("current validated source manifest digest mismatch")
    current_manifest = load_json(current_manifest_path)
    current_layout_revision = current_manifest.get("layout_revision") or {}
    if current_layout_revision.get("visual_review_repairs") is not True:
        raise ValueError("recovery basis must be a Visual Review repair revision")
    if current_layout_revision.get("new_external_evidence") is not False:
        raise ValueError("recovery basis unexpectedly introduced external Evidence")

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(current_manifest_path.parent, output_dir)

    changed_files: list[str] = []
    empty_lists_removed = 0
    new_manifest = dict(current_manifest)
    articles = [dict(article) for article in current_manifest.get("articles") or []]
    new_manifest["articles"] = articles
    for article in articles:
        rel = str(article.get("technical_notes_path") or "")
        if not rel:
            continue
        path = output_dir / rel
        if not path.is_file():
            raise ValueError(f"Technical Notes missing: {rel}")
        text = path.read_text(encoding="utf-8")
        revised, count = EMPTY_ITEMIZE_RE.subn("", text)
        if count:
            path.write_text(revised, encoding="utf-8")
            changed_files.append(rel)
            empty_lists_removed += count
        if EMPTY_ITEMIZE_RE.search(path.read_text(encoding="utf-8")):
            raise ValueError(f"empty itemize remains after recovery: {rel}")
        article["technical_notes_sha256"] = sha(path)

    if empty_lists_removed < 1:
        raise ValueError("recovery found no empty itemize artifact to remove")

    # All other source bytes remain inherited from the prior immutable revision.
    main_path = output_dir / str((new_manifest.get("main_tex") or {}).get("path") or "main.tex")
    front_path = output_dir / str((new_manifest.get("frontmatter") or {}).get("path") or "sections/00-frontmatter.tex")
    refs_path = output_dir / str((new_manifest.get("references") or {}).get("path") or "references.bib")
    for label, path in (("main.tex", main_path), ("frontmatter", front_path), ("references", refs_path)):
        if not path.is_file():
            raise ValueError(f"{label} missing in recovery source")
    new_manifest["main_tex"] = {"path": main_path.relative_to(output_dir).as_posix(), "sha256": sha(main_path)}
    new_manifest["frontmatter"] = {"path": front_path.relative_to(output_dir).as_posix(), "sha256": sha(front_path)}
    new_manifest["references"] = {"path": refs_path.relative_to(output_dir).as_posix(), "sha256": sha(refs_path)}

    new_manifest["source_version"] = source_version
    new_manifest["status"] = "VALIDATED_VISUAL_REVIEW_RECOVERY_REVISION"
    new_manifest["derivation"] = (
        "Compile-recovery revision derived byte-for-byte from the prior Human Visual Review repair source, "
        "except for removal of TeX-invalid empty itemize environments left by selective Technical Notes "
        "tail grouping. Reader wording, bibliography metadata, selected Evidence, accepted Article Draft "
        "claims, TOC, and mixed-layout policy remain unchanged."
    )
    new_manifest["basis"] = dict(current_manifest.get("basis") or {})
    new_manifest["basis"]["previous_source_manifest_path"] = current["path"]
    new_manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]
    new_manifest["layout_revision"] = dict(current_layout_revision)
    new_manifest["layout_revision"].update(
        {
            "from_source_version": current_manifest.get("source_version"),
            "visual_review_recovery": True,
            "reader_content_changed": False,
            "new_external_evidence": False,
            "empty_itemize_removed": empty_lists_removed,
            "technical_notes_files_changed_for_compile_recovery": changed_files,
        }
    )

    manifest_path = output_dir / "source-manifest.json"
    write_json(manifest_path, new_manifest)
    manifest_sha = sha(manifest_path)

    history = state.setdefault("provenance_history", {})
    history.setdefault("validated_issue_source", []).append(current)
    state["provenance"]["validated_issue_source"] = {
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": source_version,
        "layout_mode": "balanced-local-multicol-visual-review-recovery",
        "layout_revision_sha256": sha(marker_path),
    }
    state["provenance"]["reader_layout_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": sha(marker_path),
        "reason": str(marker.get("reason") or "Recover Visual Review source after PDF compile failure."),
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
        "empty_itemize_removed": empty_lists_removed,
        "technical_notes_files_changed": changed_files,
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
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
