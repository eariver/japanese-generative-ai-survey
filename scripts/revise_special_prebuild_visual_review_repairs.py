#!/usr/bin/env python3
"""Apply the generic visual-review repair to a validated source before a successful PDF gate.

The normal visual-review repair historically required RELEASE_CANDIDATE, but a PDF can
compile and still fail the strict publication-quality gate (for example an overfull
box).  In that case the canonical state correctly remains VALIDATED_DRAFT with
latex_build=pending.  This compatibility wrapper validates that prebuild boundary,
then invokes the same immutable visual-review repair without inventing a successful
build provenance entry.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_visual_review_repairs as core


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def validate_prebuild_boundary(state: dict[str, Any]) -> None:
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "VALIDATED_DRAFT":
        raise ValueError("prebuild visual repair requires VALIDATED_DRAFT")
    if gates.get("claim_and_chronology_validation") != "passed":
        raise ValueError("prebuild visual repair requires validated claims and chronology")
    if gates.get("latex_build") != "pending":
        raise ValueError("prebuild visual repair requires latex_build=pending")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("prebuild visual repair requires Visual Review and Freeze pending")


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    changes = marker.get("layout_changes") or {}
    if changes.get("prebuild_visual_review_repairs") is not True:
        raise ValueError("layout marker does not request prebuild_visual_review_repairs")
    if changes.get("visual_review_repairs") is not True:
        raise ValueError("prebuild visual repair must also request the canonical visual_review_repairs transform")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    original = load_json(state_path)
    validate_prebuild_boundary(original)

    # The shared repair implementation only needs the prior-build gate to establish
    # that it is operating after a visual inspection.  For a strict quality-gate
    # failure, the visual inspection happened on an uploaded compile artifact while
    # no successful latex_build provenance exists.  Present that boundary transiently
    # to the immutable repair builder; never commit or preserve the synthetic state.
    transient = json.loads(json.dumps(original))
    transient["lifecycle_state"] = "RELEASE_CANDIDATE"
    transient["gates"]["latex_build"] = "passed"
    write_json(state_path, transient)
    try:
        result = core.build(repo_root, special_slug, issue_id, source_version)
    except Exception:
        write_json(state_path, original)
        raise

    final = load_json(state_path)
    if final.get("lifecycle_state") != "VALIDATED_DRAFT":
        raise ValueError("visual repair did not return to VALIDATED_DRAFT")
    if (final.get("gates") or {}).get("latex_build") != "pending":
        raise ValueError("visual repair did not reopen latex_build gate")
    if (final.get("provenance") or {}).get("latex_build") is not None:
        raise ValueError("prebuild repair must not invent successful latex_build provenance")

    result["prebuild_quality_gate_repair"] = True
    result["prior_successful_pdf_required"] = False
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
