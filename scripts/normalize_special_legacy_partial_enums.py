#!/usr/bin/env python3
"""Normalize legacy partially translated Technical Notes event labels.

Older derived Special revisions could contain labels such as ``モデル\_RELEASE``
after an early reader-facing pass translated only the enum prefix.  This migration
helper is intentionally limited to PDF-facing Technical Notes: immutable Evidence
cards and Draft Packages are never changed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

LEGACY_PARTIAL_EVENT_LABELS = {
    r"モデル\_RELEASE": "モデル公開",
    "モデル_RELEASE": "モデル公開",
    r"モデル\_UPDATE": "モデル更新",
    "モデル_UPDATE": "モデル更新",
    r"研究\_RELEASE": "研究公開",
    "研究_RELEASE": "研究公開",
    r"論文\_RELEASE": "論文公開",
    "論文_RELEASE": "論文公開",
    r"Framework\_RELEASE": "Framework公開",
    "Framework_RELEASE": "Framework公開",
    r"Agent\_RELEASE": "Agent公開",
    "Agent_RELEASE": "Agent公開",
    r"API\_RELEASE": "API公開",
    "API_RELEASE": "API公開",
    r"API\_UPDATE": "API更新",
    "API_UPDATE": "API更新",
    r"オープンウェイト\_RELEASE": "オープンウェイト公開",
    "オープンウェイト_RELEASE": "オープンウェイト公開",
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def normalize_text(text: str) -> tuple[str, int]:
    total = 0
    for old, new in LEGACY_PARTIAL_EVENT_LABELS.items():
        count = text.count(old)
        if count:
            text = text.replace(old, new)
            total += count
    return text, total


def apply(root: Path, issue_id: str, special_slug: str, source_version: str) -> dict[str, Any]:
    state_path = root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    source = state.get("provenance", {}).get("validated_issue_source") or {}
    manifest_path = root / str(source.get("path") or "")
    expected = root / "surveys" / "special" / special_slug / "revisions" / source_version / "source-manifest.json"
    if manifest_path != expected:
        raise ValueError("state-pinned source is not the requested Special revision")
    if not manifest_path.is_file() or sha(manifest_path) != source.get("sha256"):
        raise ValueError("state-pinned source manifest missing or SHA mismatch")

    manifest = load_json(manifest_path)
    changed_files: list[dict[str, Any]] = []
    total = 0
    for article in manifest.get("articles") or []:
        rel = str(article.get("technical_notes_path") or "")
        if not rel:
            continue
        path = manifest_path.parent / rel
        before = sha(path)
        revised, count = normalize_text(path.read_text(encoding="utf-8"))
        if count:
            path.write_text(revised, encoding="utf-8")
            after = sha(path)
            article["technical_notes_sha256"] = after
            changed_files.append({"path": rel, "before_sha256": before, "after_sha256": after, "replacement_count": count})
            total += count

    if total == 0:
        raise ValueError("no legacy partially translated event enums were found")

    reader = dict(manifest.get("reader_facing_technical_notes") or {})
    reader["legacy_partial_enum_migration"] = {
        "applied": True,
        "replacement_count": total,
        "changed_files": changed_files,
        "scope": "derived PDF-facing Technical Notes only",
    }
    manifest["reader_facing_technical_notes"] = reader
    write_json(manifest_path, manifest)
    source["sha256"] = sha(manifest_path)
    source["legacy_partial_enum_migration"] = True
    write_json(state_path, state)
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "source_version": source_version,
        "replacement_count": total,
        "changed_file_count": len(changed_files),
        "source_manifest_sha256": source["sha256"],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--issue-id", required=True)
    ap.add_argument("--special-slug", required=True)
    ap.add_argument("--source-version", required=True)
    args = ap.parse_args()
    report = apply(Path(args.repo_root).resolve(), args.issue_id, args.special_slug, args.source_version)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
