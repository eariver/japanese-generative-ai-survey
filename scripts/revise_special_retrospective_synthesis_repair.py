#!/usr/bin/env python3
"""Create an immutable Special revision that repairs reader taxonomy and restores final synthesis.

This pass is intentionally post-build/pre-Freeze. It derives a new reader-facing source only
from the prior validated source plus a repository-tracked retrospective synthesis artifact.
Evidence records and accepted Article Drafts remain immutable.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any


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


def reader_taxonomy_leaks(text: str) -> list[str]:
    """Find machine-facing type labels in Technical Notes presentation rows.

    Covers both underscore enums and renderer-intermediate space forms such as
    ``SECURITY EVENT`` while allowing reader-facing abbreviations such as API.
    """
    leaks: set[str] = set()
    spaced_enum = re.compile(r"^[A-Z][A-Z0-9]*(?: [A-Z][A-Z0-9]*)+$")
    underscored_enum = re.compile(r"^[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+$")
    forbidden_singletons = {"OTHER", "PRODUCT"}

    def check(value: str) -> None:
        value = value.strip().replace(r"\_", "_")
        if value in forbidden_singletons or spaced_enum.fullmatch(value) or underscored_enum.fullmatch(value):
            leaks.add(value)

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("種別 & "):
            value = stripped[len("種別 & ") :].removesuffix(r"\\").strip()
            check(value)
            continue
        # Theme-at-a-glance rows have: title & role & type & chronology \\
        if (" & 主要資料 & " in stripped or " & 補足資料 & " in stripped) and stripped.endswith(r"\\"):
            parts = [part.strip() for part in stripped[:-2].split(" & ")]
            if len(parts) == 4:
                check(parts[2])
    return sorted(leaks)


def validate_synthesis_artifact(
    repo_root: Path,
    issue_id: str,
    changes: dict[str, Any],
) -> tuple[Path, Path, dict[str, Any]]:
    artifact_rel = str(changes.get("final_synthesis_artifact_path") or "")
    tex_rel = str(changes.get("final_synthesis_source_path") or "")
    if not artifact_rel or not tex_rel:
        raise ValueError("final synthesis artifact/source paths are required")
    artifact_path = repo_root / artifact_rel
    tex_path = repo_root / tex_rel
    if not artifact_path.is_file() or not tex_path.is_file():
        raise ValueError("final synthesis artifact/source missing")
    artifact = load_json(artifact_path)
    if artifact.get("issue_id") != issue_id:
        raise ValueError("final synthesis artifact issue mismatch")
    if artifact.get("selected_evidence_only") is not True:
        raise ValueError("final synthesis must remain selected-Evidence-only")
    if artifact.get("new_external_evidence") is not False:
        raise ValueError("final synthesis unexpectedly allows new external Evidence")
    if artifact.get("later_period_facts_used") is not False:
        raise ValueError("final synthesis may not use later-period facts for this repair")
    if str(artifact.get("tex_path") or "") != tex_rel:
        raise ValueError("final synthesis artifact tex_path mismatch")
    if str(artifact.get("tex_sha256") or "") != sha(tex_path):
        raise ValueError("final synthesis TeX digest mismatch")
    return artifact_path, tex_path, artifact


def validate_citations(tex: str, references: str) -> None:
    keys: set[str] = set()
    for match in re.finditer(r"\\(?:auto)?cite\{([^}]+)\}", tex):
        keys.update(key.strip() for key in match.group(1).split(",") if key.strip())
    if not keys:
        raise ValueError("final synthesis must cite selected Evidence")
    missing = sorted(key for key in keys if ("{" + key + ",") not in references)
    if missing:
        raise ValueError(f"final synthesis cites missing bibliography keys: {missing}")


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("retrospective synthesis repair marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("retrospective_final_synthesis_repair") is not True:
        raise ValueError("marker does not request retrospective_final_synthesis_repair")
    constraints = marker.get("constraints") or {}
    if constraints.get("new_external_evidence_allowed") is not False:
        raise ValueError("repair must forbid new external Evidence")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("repair must remain selected-Evidence-only")
    if constraints.get("evidence_and_draft_packages_immutable") is not True:
        raise ValueError("repair must keep Evidence and Draft Packages immutable")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise ValueError("retrospective synthesis repair requires RELEASE_CANDIDATE")
    if gates.get("latex_build") != "passed":
        raise ValueError("retrospective synthesis repair requires successful prior PDF build")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("Visual Review and Freeze must remain pending")

    current = dict(state.get("provenance", {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha(current_manifest_path) != current.get("sha256"):
        raise ValueError("current validated source manifest digest mismatch")
    current_manifest = load_json(current_manifest_path)
    current_dir = current_manifest_path.parent
    if (current_manifest.get("final_synthesis") or {}).get("tex_path"):
        raise ValueError("repair expects a source with missing final synthesis")

    artifact_path, synthesis_source_path, synthesis_artifact = validate_synthesis_artifact(
        repo_root, issue_id, changes
    )

    out = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if out.exists():
        raise ValueError(f"source revision already exists: {out}")
    shutil.copytree(current_dir, out)

    new_manifest = dict(current_manifest)
    articles = [dict(article) for article in current_manifest.get("articles") or []]
    new_manifest["articles"] = articles

    replacements = changes.get("reader_taxonomy_replacements") or {}
    if not isinstance(replacements, dict) or not replacements:
        raise ValueError("reader_taxonomy_replacements must be a non-empty object")
    replacement_counts: dict[str, int] = {str(key): 0 for key in replacements}
    changed_note_files: list[str] = []
    for article in articles:
        rel = str(article.get("technical_notes_path") or "")
        if not rel:
            continue
        path = out / rel
        text = path.read_text(encoding="utf-8")
        before = text
        for raw, label in replacements.items():
            raw_text = str(raw)
            label_text = str(label)
            count = text.count(raw_text)
            if count:
                text = text.replace(raw_text, label_text)
                replacement_counts[raw_text] += count
        leaks = reader_taxonomy_leaks(text)
        if leaks:
            raise ValueError(f"{rel}: machine-facing reader taxonomy remains: {leaks}")
        if text != before:
            path.write_text(text, encoding="utf-8")
            changed_note_files.append(rel)
        article["technical_notes_sha256"] = sha(path)
    missing_replacements = sorted(raw for raw, count in replacement_counts.items() if count < 1)
    if missing_replacements:
        raise ValueError(f"configured taxonomy replacement(s) not found: {missing_replacements}")

    final_dir = out / "final-synthesis"
    final_dir.mkdir(parents=True, exist_ok=True)
    final_path = final_dir / "70-retrospective-synthesis.tex"
    shutil.copyfile(synthesis_source_path, final_path)
    final_text = final_path.read_text(encoding="utf-8")
    if r"\section{" not in final_text or r"\label{sec:retrospective-synthesis}" not in final_text:
        raise ValueError("final synthesis must define a navigable section and canonical label")
    if "2026年4月" in final_text or "2026年5月" in final_text or "2026年6月" in final_text:
        raise ValueError("later-period factual month labels are forbidden in M03 final synthesis repair")

    refs_rel = str((new_manifest.get("references") or {}).get("path") or "references.bib")
    refs_path = out / refs_rel
    validate_citations(final_text, refs_path.read_text(encoding="utf-8"))

    main_path = out / str((new_manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_text = main_path.read_text(encoding="utf-8")
    final_input = r"\input{final-synthesis/70-retrospective-synthesis}"
    if final_input in main_text:
        raise ValueError("final synthesis input already present")
    bib = r"\printbibliography[title={References / Source Notes}]"
    if main_text.count(bib) != 1:
        raise ValueError("expected exactly one bibliography command")
    insertion = (
        r"\Needspace{0.40\textheight}"
        + "\n"
        + r"\bigskip"
        + "\n"
        + final_input
        + "\n"
        + r"\bigskip"
        + "\n"
        + bib
    )
    # Remove a preceding bibliography-only Needspace guard if present so the
    # synthesis, not References, owns the final chapter boundary.
    main_text = main_text.replace(
        r"\Needspace{0.30\textheight}" + "\n" + r"\bigskip" + "\n" + bib,
        insertion,
        1,
    )
    if final_input not in main_text:
        main_text = main_text.replace(bib, insertion, 1)
    if main_text.count(final_input) != 1 or main_text.index(final_input) > main_text.index(bib):
        raise ValueError("final synthesis must appear exactly once before References")
    main_path.write_text(main_text, encoding="utf-8")

    new_manifest["source_version"] = source_version
    new_manifest["status"] = "VALIDATED_RETROSPECTIVE_SYNTHESIS_REPAIR_REVISION"
    new_manifest["derivation"] = (
        "Pre-Freeze editorial repair derived from the prior validated preview, selected Evidence, and a "
        "repository-tracked retrospective synthesis artifact. Accepted Article Drafts and Evidence remain "
        "immutable. Reader-facing taxonomy is normalized and a cross-article final synthesis is restored "
        "before References."
    )
    new_manifest["basis"] = dict(current_manifest.get("basis") or {})
    new_manifest["basis"]["previous_source_manifest_path"] = current["path"]
    new_manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]
    new_manifest["basis"]["retrospective_synthesis_artifact_path"] = artifact_path.relative_to(repo_root).as_posix()
    new_manifest["basis"]["retrospective_synthesis_artifact_sha256"] = sha(artifact_path)
    new_manifest["main_tex"] = {"path": main_path.relative_to(out).as_posix(), "sha256": sha(main_path)}
    new_manifest["final_synthesis"] = {
        "required": True,
        "tex_path": final_path.relative_to(out).as_posix(),
        "tex_sha256": sha(final_path),
        "structured_source_path": artifact_path.relative_to(repo_root).as_posix(),
        "structured_source_sha256": sha(artifact_path),
        "selected_evidence_only": True,
        "new_external_evidence": False,
        "later_period_facts_used": False,
        "toc_navigation": True,
    }
    new_manifest["layout"] = dict(current_manifest.get("layout") or {})
    new_manifest["layout"]["final_synthesis_start_policy"] = "Needspace(0.40 textheight) before cross-article synthesis"
    new_manifest["layout"]["references_start_policy"] = "continue after final synthesis without forced clearpage"
    reader = dict(current_manifest.get("reader_facing_technical_notes") or {})
    reader["machine_enum_policy"] = "reader-facing-labels-v6-space-enum-guard"
    reader["review_taxonomy_replacements"] = replacement_counts
    reader["review_taxonomy_changed_files"] = changed_note_files
    new_manifest["reader_facing_technical_notes"] = reader
    new_manifest["layout_revision"] = {
        "from_source_version": current_manifest.get("source_version"),
        "retrospective_final_synthesis_repair": True,
        "issue_refs": [int(x) for x in marker.get("review_issues") or []],
        "reader_content_changed": True,
        "reader_content_change_scope": "reader taxonomy label plus cross-article retrospective synthesis",
        "new_external_evidence": False,
        "accepted_article_sections_changed": False,
        "evidence_and_draft_packages_changed": False,
        "technical_note_files_changed": changed_note_files,
        "reader_taxonomy_replacements": replacement_counts,
        "final_synthesis_added": True,
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
    state["provenance"]["validated_issue_source"] = {
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": source_version,
        "layout_mode": "balanced-local-multicol-retrospective-synthesis-repair",
        "layout_revision_sha256": sha(marker_path),
    }
    state["provenance"].pop("latex_build", None)
    state["provenance"]["reader_layout_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": sha(marker_path),
        "reason": str(marker.get("reason") or "Restore required retrospective synthesis and reader-facing taxonomy before Freeze."),
    }
    state["provenance"]["retrospective_synthesis_correction"] = {
        "path": artifact_path.relative_to(repo_root).as_posix(),
        "sha256": sha(artifact_path),
        "tex_sha256": sha(final_path),
        "selected_evidence_only": True,
        "later_period_facts_used": False,
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
        "taxonomy_replacements": replacement_counts,
        "final_synthesis_sha256": sha(final_path),
        "reader_content_changed": True,
        "new_external_evidence": False,
        "later_period_facts_used": False,
        "lifecycle_state": state["lifecycle_state"],
        "latex_build_gate": state["gates"]["latex_build"],
        "visual_review_gate": state["gates"]["visual_review"],
        "freeze_gate": state["gates"]["freeze"],
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root", default=".")
    p.add_argument("--special-slug", required=True)
    p.add_argument("--issue-id", required=True)
    p.add_argument("--source-version", required=True)
    a = p.parse_args()
    print(json.dumps(build(Path(a.repo_root).resolve(), a.special_slug, a.issue_id, a.source_version), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
