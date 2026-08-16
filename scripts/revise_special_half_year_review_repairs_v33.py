#!/usr/bin/env python3
"""Layer hash-bound Half-year Technical Note overrides without mutating prior revisions.

Issue #191 tightened the historical event-window extractor in V32. That fail-closed boundary
can expose older cards whose already-reviewed reader-facing details intentionally came from a
hash-bound editorial override. A new revision may also need a small revision-specific override,
but rewriting the historical override artifact would break immutable-revision provenance.

V33 therefore allows a revision marker to combine:

* ``technical_note_detail_overrides_path``: the existing immutable base override artifact; and
* ``technical_note_detail_overrides_overlay_path``: a revision-local additive overlay.

Both artifacts remain independently bound to an accepted Screening verification-queue digest.
Overlay titles must be new; duplicate titles fail closed instead of silently replacing the base.
All V32 event-window hardening and earlier entity-binding protections remain inherited.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v6 as override_layer
from scripts import revise_special_half_year_review_repairs_v32 as base

_ORIGINAL_LOAD_OVERRIDES = override_layer._load_overrides
_OVERRIDE_LAYER_CONTRACT = "HASH_BOUND_BASE_PLUS_ADDITIVE_OVERLAY_V1"


def _load_overrides_with_overlay(
    repo_root: Path,
    issue_id: str,
    source_version: str,
) -> dict[str, dict[str, Any]]:
    result = dict(_ORIGINAL_LOAD_OVERRIDES(repo_root, issue_id, source_version))

    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = override_layer._load_json(marker_path)
    changes = marker.get("layout_changes") or {}
    rel = str(changes.get("technical_note_detail_overrides_overlay_path") or "").strip()
    if not rel:
        return result

    path = repo_root / rel
    payload = override_layer._load_json(path)
    if str(payload.get("issue_id") or "") != issue_id:
        raise ValueError(f"Technical Notes detail overlay issue mismatch: {path}")

    expected_queue_sha = str(payload.get("screening_verification_queue_sha256") or "").strip()
    if not expected_queue_sha:
        raise ValueError(f"{path}: screening_verification_queue_sha256 is required")

    entries = payload.get("entries") or {}
    if not isinstance(entries, dict):
        raise ValueError(f"{path}: entries must be an object")

    for title, entry in entries.items():
        canonical_title = str(title)
        if canonical_title in result:
            raise ValueError(
                "Technical Notes detail overlay must be additive; duplicate base title: "
                f"{canonical_title}"
            )
        if not isinstance(entry, dict):
            raise ValueError(f"{path}: overlay entry must be an object: {canonical_title}")
        value = dict(entry)
        value["_expected_queue_sha256"] = expected_queue_sha
        result[canonical_title] = value
    return result


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous_loader = override_layer._load_overrides
    override_layer._load_overrides = _load_overrides_with_overlay
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        override_layer._load_overrides = previous_loader

    if isinstance(result, dict):
        result = dict(result)
        result["technical_note_detail_override_layer_contract"] = _OVERRIDE_LAYER_CONTRACT
    return result


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
