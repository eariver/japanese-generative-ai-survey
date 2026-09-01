#!/usr/bin/env python3
"""Create immutable SP-2022-Y v0.9 by replacing proximity-derived Technical Notes.

The parent v0.8 revision is already validated for the requested Annual publication-review
repairs. Current-main publication validation additionally forbids reader-facing facts derived
from a target-event proximity window. This repair copies v0.8 to v0.9 and replaces only the
explicitly listed affected Technical Note fact lines with hash-bound, selected-Screening-backed
facts from the editorial decision file.

It does not alter accepted article narrative, chronology, source URL sets, Evidence selection,
or any human gate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any

ISSUE_ID = "SP-2022-Y"
PARENT_VERSION = "v0.8"
SOURCE_VERSION = "v0.9"
ENTITY_CONTRACT = "SUBJECT_COMPONENT_VARIANT_PROPERTY_BINDING_V3"
DIRECT_BINDING_MODE = "DIRECT_SCREENING_SUMMARY_OVERRIDE"
PROXIMITY_PHRASE = "対象event近傍の一次資料から"
FACT_PREFIX = r"\item \textbf{一次情報で確認できる事実}: "
BLOCK_RE = re.compile(
    r"(?P<open>\\begin\{technicalnote\}\{(?P<title>[^{}]+)\}\{[^{}]*\})(?P<body>.*?)(?P<close>\\end\{technicalnote\})",
    re.DOTALL,
)
FACT_RE = re.compile(r"^\\item \\textbf\{一次情報で確認できる事実\}: .*?$", re.MULTILINE)
URL_RE = re.compile(r"\\url\{([^{}]+)\}")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def replace_blocks(note_path: Path, entries: dict[str, Any], counts: dict[str, int]) -> None:
    original = note_path.read_text(encoding="utf-8")

    def repl(match: re.Match[str]) -> str:
        title = match.group("title")
        if title not in entries:
            return match.group(0)
        body = match.group("body")
        decision = entries[title]
        actual_urls = URL_RE.findall(body)
        expected_urls = decision["source_urls"]
        if actual_urls != expected_urls:
            raise ValueError(
                f"Technical Note URL identity mismatch for {title}: actual={actual_urls!r} expected={expected_urls!r}"
            )
        facts = FACT_RE.findall(body)
        if len(facts) != 1:
            raise ValueError(f"Expected exactly one reader fact for {title}; found={len(facts)}")
        replacement = FACT_PREFIX + decision["fact"]
        body = FACT_RE.sub(lambda _m: replacement, body, count=1)
        counts[title] = counts.get(title, 0) + 1
        return match.group("open") + body + match.group("close")

    updated = BLOCK_RE.sub(repl, original)
    note_path.write_text(updated, encoding="utf-8")


def build(repo_root: Path) -> dict[str, Any]:
    state_path = repo_root / "sources" / ISSUE_ID / "pipeline-state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    if state["lifecycle_state"] != "VALIDATED_DRAFT":
        raise ValueError(f"Unexpected lifecycle_state: {state['lifecycle_state']}")
    if state["gates"]["latex_build"] != "pending":
        raise ValueError("v0.9 repair requires latex_build=pending")
    if "publication_preview" in state.get("provenance", {}):
        raise ValueError("Publication Preview approval must remain unset during this repair")

    current = state["provenance"]["validated_issue_source"]
    if current.get("source_version") != PARENT_VERSION:
        raise ValueError(f"Expected parent {PARENT_VERSION}; got {current!r}")
    parent_manifest_path = repo_root / current["path"]
    if sha256(parent_manifest_path) != current["sha256"]:
        raise ValueError("Parent source-manifest SHA does not match pipeline state")

    decision_path = repo_root / "sources" / ISSUE_ID / "editorial" / "technical-notes-proximity-fallback-overrides-v0.9.json"
    decision = json.loads(decision_path.read_text(encoding="utf-8"))
    if decision["issue_id"] != ISSUE_ID or decision["source_version"] != SOURCE_VERSION:
        raise ValueError("Unexpected direct-binding decision identity")
    if decision["parent_source_version"] != PARENT_VERSION:
        raise ValueError("Unexpected decision parent")
    if decision.get("new_external_evidence") or decision.get("accepted_article_claims_changed") or decision.get("publication_preview_approval_recorded"):
        raise ValueError("Direct-binding decision crosses an editorial or human-gate boundary")

    parent_dir = parent_manifest_path.parent
    new_dir = parent_dir.parent / SOURCE_VERSION
    if new_dir.exists():
        raise ValueError(f"Immutable target already exists: {new_dir}")
    shutil.copytree(parent_dir, new_dir)

    manifest_path = new_dir / "source-manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("source_version") != PARENT_VERSION:
        raise ValueError("Copied manifest does not identify v0.8")

    entries = decision["entries"]
    counts: dict[str, int] = {}
    note_paths: list[Path] = []
    for article in manifest["articles"]:
        rel = article.get("technical_notes_path")
        if not rel:
            continue
        path = new_dir / rel
        if path.is_file():
            note_paths.append(path)
            replace_blocks(path, entries, counts)

    for title, item in entries.items():
        expected = int(item["expected_occurrences"])
        actual = counts.get(title, 0)
        if actual != expected:
            raise ValueError(f"Direct-binding occurrence mismatch for {title}: actual={actual} expected={expected}")
    total = sum(counts.values())
    if total != int(decision["expected_rendered_occurrence_count"]):
        raise ValueError(f"Total direct-binding occurrence mismatch: {total}")

    combined = "\n".join(path.read_text(encoding="utf-8") for path in note_paths)
    if PROXIMITY_PHRASE in combined:
        raise ValueError("Reader-facing proximity fallback remains after v0.9 repair")
    for title, item in entries.items():
        rendered = combined.count(FACT_PREFIX + item["fact"])
        if rendered != int(item["expected_occurrences"]):
            raise ValueError(f"Rendered direct fact mismatch for {title}: {rendered}")

    audit = {
        "schema_version": "1.0",
        "issue_id": ISSUE_ID,
        "source_version": SOURCE_VERSION,
        "contract": ENTITY_CONTRACT,
        "scope": "reader-facing Technical Note entity/property binding after removal of target-event proximity synthesis",
        "policy": "Model scale, architecture, training, data, and release-form facts are bound directly to the selected artifact's accepted primary-source set; no neighboring-event signal is eligible for reader-facing synthesis.",
        "artifact_count": len(entries),
        "accepted_entity_bound_signal_count": 0,
        "rejected_entity_bound_signal_count": 0,
        "direct_screening_binding_count": len(entries),
        "direct_screening_rendered_occurrence_count": total,
        "artifacts": [
            {
                "title": title,
                "anchor": title,
                "extraction_calls": 0,
                "accepted_entity_bound_signals": [],
                "rejected_entity_bound_signals": [],
                "empty_window_calls": 0,
                "binding_mode": DIRECT_BINDING_MODE,
                "source_urls": item["source_urls"],
                "rendered_occurrence_count": counts[title],
            }
            for title, item in entries.items()
        ],
    }
    audit_name = "technical-note-entity-binding-audit-v0.9.json"
    audit_path = new_dir / audit_name
    write_json(audit_path, audit)

    manifest["source_version"] = SOURCE_VERSION
    manifest["status"] = "VALIDATED_ANNUAL_DIRECT_ENTITY_BINDING_REPAIR"
    manifest["derivation"] = (
        "Current-main Technical Note entity-binding repair: removed all reader-facing target-event proximity synthesis and replaced the affected artifacts with direct, selected-Screening-backed facts without changing article narrative, source URL sets, chronology, or Evidence selection."
    )
    manifest.setdefault("basis", {})["previous_source_manifest_path"] = current["path"]
    manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]
    manifest["basis"]["direct_binding_decision_path"] = decision_path.relative_to(repo_root).as_posix()
    manifest["basis"]["direct_binding_decision_sha256"] = sha256(decision_path)

    for article in manifest["articles"]:
        rel = article.get("technical_notes_path")
        if rel and (new_dir / rel).is_file():
            article["technical_notes_sha256"] = sha256(new_dir / rel)

    for key in ("main_tex", "frontmatter", "references"):
        item = manifest.get(key)
        if item and item.get("path") and (new_dir / item["path"]).is_file():
            item["sha256"] = sha256(new_dir / item["path"])

    reader = manifest.setdefault("reader_facing_technical_notes", {})
    reader["entity_binding_contract"] = ENTITY_CONTRACT
    reader["entity_binding_audit_path"] = audit_name
    reader["entity_binding_audit_sha256"] = sha256(audit_path)
    reader["entity_binding_audited_artifact_count"] = len(entries)
    reader["entity_binding_accepted_signal_count"] = 0
    reader["entity_binding_rejected_signal_count"] = 0
    reader["entity_binding_coverage_population_count"] = int(reader.get("source_specific_detail_visible_card_count", 42)) - 7
    reader["source_specific_detail_override_count"] = int(reader.get("source_specific_detail_override_count", 27)) + len(entries)
    reader["proximity_fallback_override_count"] = len(entries)
    reader["proximity_fallback_rendered_occurrence_count"] = total
    reader["proximity_fallback_findings"] = 0
    reader["direct_binding_mode"] = DIRECT_BINDING_MODE

    write_json(manifest_path, manifest)
    manifest_sha = sha256(manifest_path)

    editorial_audit = {
        "schema_version": "1.0",
        "issue_id": ISSUE_ID,
        "source_version": SOURCE_VERSION,
        "parent_source_version": PARENT_VERSION,
        "parent_source_manifest_path": current["path"],
        "parent_source_manifest_sha256": current["sha256"],
        "source_manifest_path": manifest_path.relative_to(repo_root).as_posix(),
        "source_manifest_sha256": manifest_sha,
        "decision_path": decision_path.relative_to(repo_root).as_posix(),
        "decision_sha256": sha256(decision_path),
        "entity_binding_contract": ENTITY_CONTRACT,
        "direct_binding_artifact_count": len(entries),
        "direct_binding_rendered_occurrence_count": total,
        "proximity_fallback_findings": 0,
        "new_external_evidence": False,
        "accepted_article_claims_changed": False,
        "chronology_changed": False,
        "source_url_sets_changed": False,
        "publication_preview_approval_recorded": False,
    }
    editorial_audit_path = repo_root / "sources" / ISSUE_ID / "editorial" / "proximity-binding-repair-v0.9.json"
    write_json(editorial_audit_path, editorial_audit)

    history = state.setdefault("provenance_history", {}).setdefault("validated_issue_source", [])
    if not any(item.get("source_version") == PARENT_VERSION and item.get("sha256") == current["sha256"] for item in history):
        history.append(dict(current))
    state["provenance"]["validated_issue_source"] = {
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": SOURCE_VERSION,
        "layout_mode": "annual-direct-entity-binding-repair",
    }
    state["provenance"]["reader_layout_revision"] = {
        "source_version": SOURCE_VERSION,
        "proximity_binding_repair_path": editorial_audit_path.relative_to(repo_root).as_posix(),
        "proximity_binding_repair_sha256": sha256(editorial_audit_path),
        "issue_refs": [54, 78, 122, 139, 140, 191, 271, 272],
    }
    state["lifecycle_state"] = "VALIDATED_DRAFT"
    state["gates"]["latex_build"] = "pending"
    state["gates"]["visual_review"] = "pending"
    state["gates"]["freeze"] = "pending"
    state.get("provenance", {}).pop("latex_build", None)
    state.get("provenance", {}).pop("publication_preview", None)
    write_json(state_path, state)

    return {
        "issue_id": ISSUE_ID,
        "source_version": SOURCE_VERSION,
        "source_manifest_path": manifest_path.relative_to(repo_root).as_posix(),
        "source_manifest_sha256": manifest_sha,
        "direct_binding_artifact_count": len(entries),
        "direct_binding_rendered_occurrence_count": total,
        "proximity_fallback_findings": 0,
        "publication_preview_approval_recorded": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    args = parser.parse_args()
    print(json.dumps(build(Path(args.repo_root)), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
