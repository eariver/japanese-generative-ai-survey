#!/usr/bin/env python3
"""Build immutable per-package drafting inputs from an approved Architecture Plan."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from scripts import validate_issue_architecture as architecture_validator

ARTICLE_TYPES = {
    "LEAD", "FEATURE", "COMPARISON", "SECTION", "DEEP_DIVE", "PAPER_WATCH",
    "X_COMMUNITY", "LATE_BREAKING", "WATCHLIST_CHRONOLOGY",
}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    values: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as fh:
        for lineno, raw in enumerate(fh, start=1):
            line = raw.strip()
            if not line:
                continue
            value = json.loads(line)
            if not isinstance(value, dict):
                raise ValueError(f"{path}:{lineno}: expected JSON object")
            values.append(value)
    return values


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def mode_for(package_type: str) -> tuple[str, str, bool]:
    if package_type == "FRONTMATTER":
        return "ISSUE_SYNTHESIS", "POST_DRAFT_SUMMARY", False
    if package_type == "REFERENCES":
        return "REFERENCES_GENERATED", "REFERENCE_GENERATION", True
    if package_type in ARTICLE_TYPES:
        return "EVIDENCE_PACKAGE", "ARTICLE_DRAFTING", True
    raise ValueError(f"unsupported package_type: {package_type}")


def build(
    architecture_input_path: Path,
    architecture_plan_path: Path,
    evidence_reviewed_path: Path,
    output_dir: Path,
) -> tuple[dict[str, Any], bool]:
    report, passed = architecture_validator.validate(
        architecture_input_path, architecture_plan_path, require_approved=True
    )
    if not passed:
        raise ValueError(f"Architecture is not drafting-ready: {report['errors']}")

    plan = load_json(architecture_plan_path)
    reviewed = read_jsonl(evidence_reviewed_path)
    evidence_by_id: dict[str, dict[str, Any]] = {}
    for item in reviewed:
        task_id = item.get("evidence_task_id")
        if not isinstance(task_id, str) or not task_id:
            raise ValueError("evidence-reviewed item lacks evidence_task_id")
        if task_id in evidence_by_id:
            raise ValueError(f"duplicate evidence_task_id in reviewed evidence: {task_id}")
        if item.get("issue_id") != plan.get("issue_id"):
            raise ValueError(f"Evidence issue mismatch for {task_id}")
        evidence_by_id[task_id] = item

    output_dir.mkdir(parents=True, exist_ok=True)
    basis = {
        "architecture_plan_sha256": sha256_file(architecture_plan_path),
        "architecture_input_sha256": sha256_file(architecture_input_path),
        "evidence_reviewed_sha256": sha256_file(evidence_reviewed_path),
    }
    package_files: list[dict[str, Any]] = []
    errors: list[str] = []

    for package in sorted(plan["packages"], key=lambda p: p["drafting_order"]):
        package_id = package["package_id"]
        package_type = package["package_type"]
        source_mode, execution_stage, summary_forbidden = mode_for(package_type)
        primary_ids = package.get("primary_evidence_task_ids") or []
        supporting_ids = package.get("supporting_evidence_task_ids") or []
        missing_ids = sorted({*primary_ids, *supporting_ids} - set(evidence_by_id))
        if missing_ids:
            errors.append(f"{package_id}: Evidence items missing from evidence-reviewed.jsonl: {missing_ids}")
            continue

        value = {
            "schema_version": "1.0",
            "issue_id": plan["issue_id"],
            "package_id": package_id,
            "draft_source_mode": source_mode,
            "execution_stage": execution_stage,
            "basis": dict(basis),
            "package": {
                "title": package["title"],
                "package_type": package_type,
                "page_target": package["page_target"],
                "editorial_angle": package["editorial_angle"],
                "must_cover": package.get("must_cover") or [],
                "boundaries": package.get("boundaries") or [],
                "late_breaking": package["late_breaking"],
                "drafting_order": package["drafting_order"],
            },
            "primary_evidence": [evidence_by_id[task_id] for task_id in primary_ids],
            "supporting_evidence": [evidence_by_id[task_id] for task_id in supporting_ids],
            "drafting_constraints": {
                "language": "ja",
                "raw_sources_forbidden": True,
                "unknowns_remain_unknown": True,
                "citation_granularity": "EVENT_CLAIM_METRIC_LIMITATION",
                "cover_headline_finalization_forbidden": True,
                "this_week_summary_forbidden": summary_forbidden,
            },
        }
        path = output_dir / f"{package_id}.json"
        write_json(path, value)
        package_files.append({
            "package_id": package_id,
            "package_type": package_type,
            "draft_source_mode": source_mode,
            "execution_stage": execution_stage,
            "path": path.name,
            "sha256": sha256_file(path),
            "bytes": path.stat().st_size,
            "drafting_order": package["drafting_order"],
        })

    manifest = {
        "schema_version": "1.0",
        "issue_id": plan.get("issue_id"),
        "passed": not errors,
        "package_count": len(plan.get("packages") or []),
        "materialized_package_count": len(package_files),
        "article_drafting_count": sum(1 for item in package_files if item["execution_stage"] == "ARTICLE_DRAFTING"),
        "post_draft_summary_count": sum(1 for item in package_files if item["execution_stage"] == "POST_DRAFT_SUMMARY"),
        "reference_generation_count": sum(1 for item in package_files if item["execution_stage"] == "REFERENCE_GENERATION"),
        "basis": basis,
        "package_files": package_files,
        "errors": errors,
        "note": "ARTICLE_DRAFTING packages consume only selected Evidence Cards. FRONTMATTER is deferred until substantive drafts stabilize; REFERENCES is deterministic generation, not article prose drafting.",
    }
    write_json(output_dir / "draft-package-manifest.json", manifest)
    return manifest, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--architecture-input", required=True)
    parser.add_argument("--architecture-plan", required=True)
    parser.add_argument("--evidence-reviewed", required=True)
    parser.add_argument("--output-dir", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest, passed = build(
        Path(args.architecture_input), Path(args.architecture_plan),
        Path(args.evidence_reviewed), Path(args.output_dir),
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
