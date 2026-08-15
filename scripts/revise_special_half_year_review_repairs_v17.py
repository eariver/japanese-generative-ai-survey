#!/usr/bin/env python3
"""Allow explicit validated-draft -> validated-draft Half-year repair chaining.

A semantically rejected derived revision should not need to be compiled into a PDF merely to
become the immutable parent of the next source-only repair. The historical incremental
builder requires a built RELEASE_CANDIDATE. This wrapper preserves that default, but when a
layout marker explicitly opts in it also permits an *unbuilt* VALIDATED_DRAFT parent iff:

* latex_build, visual_review, and freeze are all pending;
* there is no current latex_build provenance to discard or reinterpret;
* the marker explicitly sets ``allow_unbuilt_incremental_parent`` true.

The existing v8 incremental builder is then reused unchanged. Its in-memory precondition is
satisfied temporarily; the persisted result still ends at VALIDATED_DRAFT with all three
gates pending, exactly as a source-only repair should.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v16 as base
from scripts import revise_special_half_year_review_repairs_v8 as incremental

_ORIGINAL_INCREMENTAL_BUILD = incremental._incremental_build


def _incremental_build_allow_unbuilt(
    repo_root: Path,
    special_slug: str,
    issue_id: str,
    source_version: str,
    marker: dict[str, Any],
    state: dict[str, Any],
    current: dict[str, Any],
    current_manifest: dict[str, Any],
) -> dict[str, Any]:
    changes = marker.get("layout_changes") or {}
    gates = state.get("gates") or {}
    lifecycle = str(state.get("lifecycle_state") or "")

    if lifecycle != "VALIDATED_DRAFT" or gates.get("latex_build") != "pending":
        return _ORIGINAL_INCREMENTAL_BUILD(
            repo_root,
            special_slug,
            issue_id,
            source_version,
            marker,
            state,
            current,
            current_manifest,
        )

    if changes.get("allow_unbuilt_incremental_parent") is not True:
        raise ValueError(
            "unbuilt incremental Half-year parent requires explicit allow_unbuilt_incremental_parent marker"
        )
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("unbuilt incremental Half-year parent requires visual_review/freeze pending")
    if (state.get("provenance") or {}).get("latex_build"):
        raise ValueError("unbuilt incremental Half-year parent must not carry current latex_build provenance")

    original_lifecycle = state.get("lifecycle_state")
    original_latex = gates.get("latex_build")
    # Satisfy only the legacy in-memory precondition. The reused builder writes the derived
    # state as VALIDATED_DRAFT/pending before persisting it.
    state["lifecycle_state"] = "RELEASE_CANDIDATE"
    gates["latex_build"] = "passed"
    try:
        result = _ORIGINAL_INCREMENTAL_BUILD(
            repo_root,
            special_slug,
            issue_id,
            source_version,
            marker,
            state,
            current,
            current_manifest,
        )
        state["lifecycle_state"] = original_lifecycle
        gates["latex_build"] = original_latex
        if isinstance(result, dict):
            result["incremental_parent_build_state"] = "UNBUILT_VALIDATED_DRAFT"
            result["unbuilt_parent_opt_in"] = True
        return result
    except Exception:
        state["lifecycle_state"] = original_lifecycle
        gates["latex_build"] = original_latex
        raise


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = incremental._incremental_build
    incremental._incremental_build = _incremental_build_allow_unbuilt
    try:
        return base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        incremental._incremental_build = previous


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
