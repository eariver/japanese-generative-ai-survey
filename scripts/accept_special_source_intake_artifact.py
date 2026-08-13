#!/usr/bin/env python3
"""Accept one reviewed Special source-intake artifact append-only into its canonical work tree."""
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
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def discover_files(source_root: Path) -> list[tuple[Path, Path, str]]:
    values: list[tuple[Path, Path, str]] = []
    for path in sorted(source_root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"symlink forbidden: {path}")
        if not path.is_file():
            continue
        relative = path.relative_to(source_root)
        if "raw" in relative.parts:
            kind = "RAW"
        elif relative.name == "collector-run.json":
            kind = "COLLECTOR_RUN"
        elif relative.name == "summary.json":
            kind = "SUMMARY"
        else:
            raise ValueError(f"unexpected collector file: {relative}")
        values.append((path, relative, kind))
    if not values:
        raise ValueError("collector tree contains no files")
    return values


def build_state(edition: dict[str, Any], plan: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_version": "1.0",
        "issue_id": edition["special_id"],
        "edition_kind": edition["edition_kind"],
        "lifecycle_state": "DISCOVERY_COLLECTED",
        "revision": "v0.1",
        "calendar": {
            "editorial_cutoff": plan["editorial_cutoff"],
            "cutoff_timezone": plan["cutoff_timezone"],
            "collection_window_start": plan["collection_window_start"],
            "collection_window_end": plan["collection_window_end"],
            "collection_anchor_at": plan["collection_window_end"],
            "retrospective_as_of": plan["retrospective_as_of"],
            "frozen_at": None,
        },
        "gates": {
            "raw_sources_preserved": "passed",
            "candidate_inventory": "pending",
            "evidence_normalized": "pending",
            "candidate_selection": "pending",
            "issue_architecture": "pending",
            "article_draft": "pending",
            "claim_and_chronology_validation": "pending",
            "latex_build": "pending",
            "visual_review": "pending",
            "freeze": "pending",
        },
        "automation": {
            "human_gate_model": "ARCHITECTURE_PUBLICATION_PREVIEW_WITH_EXCEPTION",
            "unattended_public_release": False,
            "human_gate_required_for_selection": False,
            "human_gate_required_for_architecture": True,
            "human_gate_required_for_publication_preview": True,
            "human_gate_required_for_visual_review": False,
            "human_gate_required_for_freeze": False,
            "human_gate_required_for_public_release": False,
            "publication_preview_authorizes": [
                "visual_review",
                "freeze",
                "work_pr_merge",
                "public_release",
            ],
            "exception_gate": "ON_DEMAND",
        },
        "provenance": {"edition_manifest": f"specials/{edition['special_slug']}/edition.json"},
    }


def build_initial_state(edition: dict[str, Any], plan: dict[str, Any]) -> dict[str, Any]:
    """Return the exact deterministic pre-intake state for this accepted plan."""
    state = build_state(edition, plan)
    state["lifecycle_state"] = "ISSUE_INITIALIZED"
    state["calendar"]["collection_anchor_at"] = None
    state["gates"]["raw_sources_preserved"] = "pending"
    return state


def accept(*, artifact_root: Path, repo_root: Path, special_slug: str, workflow_run_id: int,
           artifact_id: int, artifact_name: str, artifact_digest: str, review_reference: str) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    artifact_root = artifact_root.resolve()
    edition_path = repo_root / "specials" / special_slug / "edition.json"
    if not edition_path.is_file():
        raise ValueError(f"Special edition manifest missing: {edition_path}")
    edition = load_json(edition_path)
    special_id = edition.get("special_id")
    if special_id != f"SP-{special_slug}":
        raise ValueError("edition special_id/slug mismatch")
    if edition.get("status") != "ACTIVE":
        raise ValueError("reviewed intake requires ACTIVE Special edition")
    if not review_reference.strip():
        raise ValueError("review_reference required")
    if not artifact_digest.startswith("sha256:") or len(artifact_digest) != 71:
        raise ValueError("artifact_digest must be sha256:<64hex>")
    int(artifact_digest.split(":", 1)[1], 16)

    report_path = artifact_root / "special-source-intake" / "source-intake-report.json"
    plan_path = artifact_root / "special-source-intake-control" / "plan.json"
    source_root = artifact_root / "special-source-intake" / "sources" / special_id / "collectors"
    if not report_path.is_file() or not plan_path.is_file() or not source_root.is_dir():
        raise ValueError("Special source-intake artifact structure incomplete")
    report, plan = load_json(report_path), load_json(plan_path)
    if report.get("issue_id") != special_id or report.get("overall_status") != "success":
        raise ValueError("source-intake report is not a successful run for this Special")
    if plan.get("issue_id") != special_id or plan.get("series") != "SPECIAL":
        raise ValueError("source plan is not for this Special")
    if plan.get("special_slug") != special_slug:
        raise ValueError("source plan special_slug mismatch")
    if plan.get("collection_window_start") != edition["coverage"]["start"]:
        raise ValueError("source plan coverage start differs from edition manifest")
    if plan.get("collection_window_end") != edition["coverage"]["end"]:
        raise ValueError("source plan coverage end differs from edition manifest")
    if plan.get("retrospective_as_of") != edition["coverage"]["retrospective_as_of"]:
        raise ValueError("source plan retrospective_as_of differs from edition manifest")
    if plan.get("community_research") != edition["community_research"]:
        raise ValueError("source plan community-research policy differs from edition manifest")

    discovered = discover_files(source_root)
    destination_root = repo_root / "sources" / special_id / "collectors"
    records: list[dict[str, Any]] = []
    raw_count = 0
    for source, relative, kind in discovered:
        destination = destination_root / relative
        sha, size = sha256_file(source), source.stat().st_size
        if destination.exists():
            if not destination.is_file() or sha256_file(destination) != sha or destination.stat().st_size != size:
                raise ValueError(f"append-only conflict at {destination}")
        else:
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, destination)
        records.append({"path": destination.relative_to(repo_root).as_posix(), "sha256": sha, "bytes": size, "kind": kind})
        raw_count += int(kind == "RAW")
    if raw_count == 0:
        raise ValueError("accepted Special intake contains no Raw files")

    state_path = repo_root / "sources" / special_id / "pipeline-state.json"
    expected_state = build_state(edition, plan)
    expected_initial_state = build_initial_state(edition, plan)
    if state_path.exists():
        existing = load_json(state_path)
        lifecycle = existing.get("lifecycle_state")
        if lifecycle == "ISSUE_INITIALIZED":
            if existing != expected_initial_state:
                raise ValueError("existing Special initialized state differs from exact accepted plan")
            state_path.write_text(json.dumps(expected_state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        elif lifecycle == "DISCOVERY_COLLECTED":
            if existing != expected_state:
                raise ValueError("existing Special discovery state differs from exact accepted plan")
        else:
            raise ValueError("Special source intake cannot change state after downstream work has begun")
    else:
        state_path.parent.mkdir(parents=True, exist_ok=True)
        state_path.write_text(json.dumps(expected_state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    acceptance = {
        "schema_version": "1.0",
        "special_id": special_id,
        "special_slug": special_slug,
        "status": "ACCEPTED",
        "source_actions": {
            "workflow_run_id": workflow_run_id,
            "artifact_id": artifact_id,
            "artifact_name": artifact_name,
            "artifact_digest": artifact_digest,
            "review_reference": review_reference.strip(),
        },
        "edition_manifest_sha256": sha256_file(edition_path),
        "source_plan_sha256": sha256_file(plan_path),
        "source_intake_report_sha256": sha256_file(report_path),
        "raw_file_count": raw_count,
        "files": sorted(records, key=lambda x: x["path"]),
        "state_transition": "ISSUE_INITIALIZED -> DISCOVERY_COLLECTED",
        "derived_screening_committed": False,
    }
    acceptance_path = repo_root / "sources" / special_id / "imports" / "source-intake" / f"actions-run-{workflow_run_id}.json"
    acceptance_path.parent.mkdir(parents=True, exist_ok=True)
    if acceptance_path.exists() and load_json(acceptance_path) != acceptance:
        raise ValueError("existing acceptance manifest differs")
    acceptance_path.write_text(json.dumps(acceptance, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return acceptance


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--artifact-root", required=True)
    p.add_argument("--repo-root", required=True)
    p.add_argument("--special-slug", required=True)
    p.add_argument("--workflow-run-id", required=True, type=int)
    p.add_argument("--artifact-id", required=True, type=int)
    p.add_argument("--artifact-name", required=True)
    p.add_argument("--artifact-digest", required=True)
    p.add_argument("--review-reference", required=True)
    p.add_argument("--report")
    args = p.parse_args()
    value = accept(
        artifact_root=Path(args.artifact_root), repo_root=Path(args.repo_root), special_slug=args.special_slug,
        workflow_run_id=args.workflow_run_id, artifact_id=args.artifact_id, artifact_name=args.artifact_name,
        artifact_digest=args.artifact_digest, review_reference=args.review_reference,
    )
    if args.report:
        Path(args.report).write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(value, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
