#!/usr/bin/env python3
"""Create an immutable reader-facing enum-cleanup Special source revision.

Only machine event labels in already-derived Technical Notes are normalized. The
underlying Evidence, Japanese claim/limitation summaries, article prose, URLs,
and chronology dates remain unchanged.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any

EVENT_LABELS = {
    "OFFICIAL_PUBLICATION": "公式公開",
    "PRODUCT_RELEASE": "製品公開",
    "PRODUCT_UPDATE": "製品更新",
    "AGENT_RELEASE": "Agent公開",
    "AGENT_UPDATE": "Agent更新",
    "FRAMEWORK_RELEASE": "Framework公開",
    "FRAMEWORK_UPDATE": "Framework更新",
    "PROJECT_RELEASE": "プロジェクト公開",
    "MODEL_RELEASE": "モデル公開",
    "MODEL_UPDATE": "モデル更新",
    "MEDIA_MODEL_RELEASE": "メディアモデル公開",
    "OPEN_WEIGHT_RELEASE": "オープンウェイト公開",
    "PAPER_RELEASE": "論文公開",
    "RESEARCH_RELEASE": "研究公開",
    "EVALUATION_RELEASE": "評価公開",
    "SAFETY_EVENT": "安全性事象",
    "API_RELEASE": "API公開",
    "API_UPDATE": "API更新",
}
RAW_ENUM_RE = re.compile(r"\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def forms(value: str) -> tuple[str, ...]:
    escaped = value.replace("_", r"\_")
    return (value, escaped) if escaped != value else (value,)


def normalize(text: str) -> tuple[str, int]:
    count = 0
    for raw, label in sorted(EVENT_LABELS.items(), key=lambda item: len(item[0]), reverse=True):
        for form in forms(raw):
            occurrences = text.count(form)
            if occurrences:
                text = text.replace(form, label)
                count += occurrences
    return text, count


def remaining_machine_enums(text: str) -> list[str]:
    # Convert TeX-escaped underscores to plain underscores for deterministic scanning.
    normalized = text.replace(r"\_", "_")
    return sorted(set(RAW_ENUM_RE.findall(normalized)))


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise ValueError("reader enum cleanup requires RELEASE_CANDIDATE")
    if gates.get("latex_build") != "passed" or gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("reader enum cleanup requires built, unapproved release candidate")

    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    constraints = marker.get("constraints") or {}
    changes = marker.get("layout_changes") or {}
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("layout marker mismatch")
    if constraints.get("new_external_evidence_allowed") is not False or constraints.get("reader_content_changed") is not False or constraints.get("selected_evidence_only") is not True:
        raise ValueError("reader enum cleanup must be content-neutral and selected-Evidence-only")
    if changes.get("normalize_reader_event_enums") is not True:
        raise ValueError("normalize_reader_event_enums marker is required")

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

    articles = [dict(x) for x in current_manifest.get("articles") or []]
    changed_files: list[dict[str, Any]] = []
    total_replacements = 0
    for article in articles:
        rel = str(article.get("technical_notes_path") or "")
        if not rel:
            continue
        target = out / rel
        before = target.read_text(encoding="utf-8")
        after, count = normalize(before)
        findings = remaining_machine_enums(after)
        if findings:
            raise ValueError(f"unmapped reader-facing event enums remain in {rel}: {findings}")
        if count:
            target.write_text(after, encoding="utf-8")
            total_replacements += count
            changed_files.append({"path": rel, "replacement_count": count, "before_sha256": sha(current_dir / rel), "after_sha256": sha(target)})
        article["technical_notes_sha256"] = sha(target)
    if total_replacements < 1:
        raise ValueError("reader enum cleanup found no machine event labels to replace")

    # Non-Technical-Notes reader content must remain byte-identical.
    for old, new in zip(current_manifest.get("articles") or [], articles):
        section = out / str(old["article_section_path"])
        if sha(section) != old["article_section_sha256"]:
            raise ValueError(f"article prose changed unexpectedly: {old['package_id']}")
    for synth in current_manifest.get("theme_synthesis") or []:
        path = out / str(synth["path"])
        if sha(path) != synth["sha256"]:
            raise ValueError(f"theme synthesis changed unexpectedly: {synth.get('package_id')}")

    new_manifest = dict(current_manifest)
    new_manifest["source_version"] = source_version
    new_manifest["status"] = "VALIDATED_READER_ENUM_CLEANUP_REVISION"
    new_manifest["derivation"] = (
        "Layout/presentation-only revision of the prior validated source. Machine event enums in Technical Notes "
        "are replaced by reader-facing labels; Evidence, chronology dates, Japanese summaries and article wording are unchanged."
    )
    new_manifest["basis"] = dict(current_manifest.get("basis") or {})
    new_manifest["basis"]["previous_source_manifest_path"] = current["path"]
    new_manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]
    new_manifest["articles"] = articles
    main_path = out / str((current_manifest.get("main_tex") or {}).get("path") or "main.tex")
    new_manifest["main_tex"] = dict(current_manifest.get("main_tex") or {})
    new_manifest["main_tex"]["sha256"] = sha(main_path)
    new_manifest["reader_facing_technical_notes"] = dict(current_manifest.get("reader_facing_technical_notes") or {})
    new_manifest["reader_facing_technical_notes"]["machine_enum_policy"] = "reader-facing-labels-v4"
    new_manifest["reader_facing_technical_notes"]["enum_cleanup_files"] = changed_files
    new_manifest["layout_revision"] = {
        "from_source_version": current_manifest.get("source_version"),
        "reader_content_changed": False,
        "new_external_evidence": False,
        "normalize_reader_event_enums": True,
        "machine_event_enum_replacement_count": total_replacements,
        "article_sections_changed": False,
        "theme_synthesis_changed": False,
        "bibliography_data_changed": False,
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
    new_prov = dict(current)
    new_prov.update({
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": source_version,
        "layout_revision_sha256": sha(marker_path),
        "reader_facing_technical_notes": True,
    })
    state["provenance"]["validated_issue_source"] = new_prov
    state["provenance"].pop("latex_build", None)
    state["provenance"]["reader_layout_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": sha(marker_path),
        "reason": str(marker.get("reason") or "Normalize reader-facing event labels after render QA."),
    }
    write_json(state_path, state)
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "source_version": source_version,
        "previous_source_version": current_manifest.get("source_version"),
        "source_manifest_sha256": manifest_sha,
        "changed_file_count": len(changed_files),
        "replacement_count": total_replacements,
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
    a = p.parse_args()
    print(json.dumps(build(Path(a.repo_root).resolve(), a.special_slug, a.issue_id, a.source_version), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
