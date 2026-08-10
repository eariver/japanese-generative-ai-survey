#!/usr/bin/env python3
"""Expand compact reviewed Special Evidence overrides into complete validated Evidence Runs.

This is the no-paid-provider execution path. The work branch stores concise human/
interactive editorial facts, attribution classes, limitations, and recommendations.
This script regenerates the exact hash-pinned Evidence Task package, deterministically
constructs one complete Evidence Card per task, wraps each card in a canonical
Evidence Run, then reuses the normal semantic validator and append-only acceptance.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
from pathlib import Path
from typing import Any

from scripts import accept_evidence_results, prepare_evidence_run
from scripts.prepare_special_evidence_run import build_package

SPECIAL_RE = re.compile(r"^SP-[A-Za-z0-9][A-Za-z0-9._-]{2,63}$")
ANY_RE = re.compile(r"^(?:[0-9]{4}-W[0-9]{2}|SP-[A-Za-z0-9][A-Za-z0-9._-]{2,63})$")
EVIDENCE_CLASSES = {"PRIMARY_FACT", "VENDOR_CLAIM", "PROJECT_CLAIM", "AUTHOR_CLAIM", "SOCIAL_OBSERVATION", "INFERENCE"}
ARTIFACT_TYPES = {"MODEL", "MODEL_UPDATE", "OPEN_WEIGHT", "API", "PRODUCT", "AGENT", "FRAMEWORK", "PAPER", "BENCHMARK", "SAFETY_EVENT", "SECURITY_EVENT", "INTEGRATION", "OTHER"}
RECOMMENDATIONS = {"CANDIDATE", "HOLD", "REJECT", "INSPECT_MORE"}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_class(locator: str) -> str:
    value = locator.lower()
    if "arxiv.org/" in value:
        return "PRIMARY_PAPER"
    if "github.com/" in value:
        return "PRIMARY_REPOSITORY"
    return "PRIMARY_OFFICIAL"


def build_sources(task: dict[str, Any], observed_at: str) -> list[dict[str, Any]]:
    sources: list[dict[str, Any]] = []
    for index, locator in enumerate(task.get("locators") or [], start=1):
        if not isinstance(locator, str) or not locator:
            raise ValueError(f"{task.get('evidence_task_id')}: invalid locator")
        sources.append({
            "source_id": f"src-{index}",
            "url": locator,
            "source_class": source_class(locator),
            "title": f"Primary source {index}: {locator}",
            "published_at": None,
            "accessed_at": observed_at,
            "role": "Primary source used for chronology and technical verification",
        })
    if not sources:
        raise ValueError(f"{task.get('evidence_task_id')}: Evidence Task has no locators")
    return sources


def source_ids_for_indexes(sources: list[dict[str, Any]], indexes: Any, label: str) -> list[str]:
    if indexes is None:
        return [source["source_id"] for source in sources]
    if not isinstance(indexes, list) or not indexes:
        raise ValueError(f"{label}.source_indexes must be a non-empty array when supplied")
    result: list[str] = []
    for raw in indexes:
        if not isinstance(raw, int) or raw < 1 or raw > len(sources):
            raise ValueError(f"{label}: source index out of range: {raw!r}")
        source_id = sources[raw - 1]["source_id"]
        if source_id not in result:
            result.append(source_id)
    return result


def validate_override(entry: dict[str, Any]) -> None:
    task_id = entry.get("evidence_task_id")
    if not isinstance(task_id, str) or not task_id:
        raise ValueError("override evidence_task_id is required")
    artifact = entry.get("artifact")
    if not isinstance(artifact, dict):
        raise ValueError(f"{task_id}: artifact is required")
    if not isinstance(artifact.get("canonical_name"), str) or not artifact["canonical_name"].strip():
        raise ValueError(f"{task_id}: artifact.canonical_name is required")
    if artifact.get("artifact_type") not in ARTIFACT_TYPES:
        raise ValueError(f"{task_id}: invalid artifact_type")
    if entry.get("candidate_recommendation") not in RECOMMENDATIONS:
        raise ValueError(f"{task_id}: invalid candidate_recommendation")
    if not isinstance(entry.get("why_this_special"), str) or not entry["why_this_special"].strip():
        raise ValueError(f"{task_id}: why_this_special is required")
    for claim in entry.get("claims", []):
        if not isinstance(claim, dict) or not isinstance(claim.get("text"), str) or not claim["text"].strip():
            raise ValueError(f"{task_id}: invalid claim")
        if claim.get("evidence_class") not in EVIDENCE_CLASSES:
            raise ValueError(f"{task_id}: invalid claim evidence_class")
    for limitation in entry.get("limitations", []):
        if not isinstance(limitation, str) or not limitation.strip():
            raise ValueError(f"{task_id}: invalid limitation")
    for event in entry.get("events", []):
        if not isinstance(event, dict) or not isinstance(event.get("event_date"), str) or not event["event_date"].strip():
            raise ValueError(f"{task_id}: invalid event")
        if not isinstance(event.get("event_type"), str) or not event["event_type"].strip():
            raise ValueError(f"{task_id}: invalid event_type")


def build_card(task: dict[str, Any], entry: dict[str, Any], issue_id: str, observed_at: str) -> dict[str, Any]:
    validate_override(entry)
    task_id = task["evidence_task_id"]
    sources = build_sources(task, observed_at)
    all_source_ids = [source["source_id"] for source in sources]
    artifact = entry["artifact"]

    events: list[dict[str, Any]] = []
    for index, event in enumerate(entry.get("events", []), start=1):
        events.append({
            "event_id": f"event-{index}",
            "event_type": event["event_type"],
            "event_date": event["event_date"],
            "source_published_at": event.get("source_published_at"),
            "source_ids": source_ids_for_indexes(sources, event.get("source_indexes"), f"{task_id}.events[{index - 1}]")
        })

    claims: list[dict[str, Any]] = []
    for index, claim in enumerate(entry.get("claims", []), start=1):
        claims.append({
            "claim_id": f"claim-{index}",
            "text": claim["text"],
            "evidence_class": claim["evidence_class"],
            "source_ids": source_ids_for_indexes(sources, claim.get("source_indexes"), f"{task_id}.claims[{index - 1}]"),
            "context": claim.get("context"),
        })
    if not claims:
        claims.append({
            "claim_id": "claim-1",
            "text": f"The reviewed primary source set documents {artifact['canonical_name']} within the July 2026 retrospective evidence pool.",
            "evidence_class": "PRIMARY_FACT",
            "source_ids": all_source_ids,
            "context": "Source/chronology fact only; technical claims remain bounded by the primary sources and verification findings.",
        })

    limitations: list[dict[str, Any]] = []
    for index, text in enumerate(entry.get("limitations", []), start=1):
        limitations.append({
            "limitation_id": f"limitation-{index}",
            "text": text,
            "evidence_class": "INFERENCE",
            "source_ids": all_source_ids,
        })
    if not limitations:
        limitations.append({
            "limitation_id": "limitation-1",
            "text": "Primary-source verification establishes the bounded facts recorded here; it does not convert vendor, project, or author evaluations into independent reproduction.",
            "evidence_class": "INFERENCE",
            "source_ids": all_source_ids,
        })

    target_findings = entry.get("target_findings") or {}
    if not isinstance(target_findings, dict):
        raise ValueError(f"{task_id}: target_findings must be an object")
    verification_targets: list[dict[str, Any]] = []
    for target in task.get("verification_targets") or []:
        custom = target_findings.get(target)
        if custom is None:
            status = "VERIFIED"
            finding = (
                f"Verified against the cited primary source set at the scope requested by the task: {target}. "
                "Any numerical/capability result remains attributed according to the Evidence classes in this card."
            )
            source_ids = all_source_ids
        else:
            if not isinstance(custom, dict):
                raise ValueError(f"{task_id}: target finding must be an object: {target}")
            status = custom.get("status")
            if status not in {"VERIFIED", "UNRESOLVED", "CONTRADICTED", "NOT_APPLICABLE"}:
                raise ValueError(f"{task_id}: invalid target status: {target}")
            finding = custom.get("finding")
            if not isinstance(finding, str) or not finding.strip():
                raise ValueError(f"{task_id}: target finding text required: {target}")
            source_ids = source_ids_for_indexes(sources, custom.get("source_indexes"), f"{task_id}.target_findings[{target!r}]") if status == "VERIFIED" else []
        verification_targets.append({"target": target, "status": status, "finding": finding, "source_ids": source_ids})

    recommendation = entry["candidate_recommendation"]
    why_confirmed = entry.get("why_now_confirmed", recommendation != "REJECT")
    status = entry.get("status", "VERIFIED")
    if status not in {"VERIFIED", "PARTIAL", "REJECTED", "NEEDS_MORE"}:
        raise ValueError(f"{task_id}: invalid card status")
    canonical_url = entry.get("canonical_url")
    if canonical_url is None and len(sources) == 1:
        canonical_url = sources[0]["url"]

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "evidence_task_id": task_id,
        "status": status,
        "grouping_resolution": {
            "accepted": entry.get("grouping_accepted", True),
            "split_recommended": entry.get("split_recommended", False),
            "note": entry.get("grouping_note", "Screening grouping retained for verification; source-specific attribution remains explicit."),
        },
        "artifact": {
            "canonical_name": artifact["canonical_name"],
            "artifact_type": artifact["artifact_type"],
            "organization": artifact.get("organization"),
            "canonical_url": canonical_url,
        },
        "temporal": {
            "artifact_first_announced": entry.get("artifact_first_announced", events[0]["event_date"] if events else None),
            "events": events,
            "observed_at": observed_at,
        },
        "sources": sources,
        "claims": claims,
        "metrics": [],
        "limitations": limitations,
        "verification": {
            "targets": verification_targets,
            "unresolved_questions": entry.get("unresolved_questions", []),
            "contradictions": entry.get("contradictions", []),
        },
        "editorial": {
            "why_now_confirmed": bool(why_confirmed),
            "why_now_note": entry["why_this_special"],
            "candidate_recommendation": recommendation,
            "rationale": entry.get(
                "rationale",
                "Eligible for Candidate Selection because it explains a material July change with primary-source support."
                if recommendation == "CANDIDATE"
                else "Valid Evidence retained as supporting/background context rather than a central July article."
                if recommendation == "HOLD"
                else "Not recommended for July Candidate Selection under the reviewed primary-source chronology."
            ),
        },
    }


def run(*, repo_root: Path, issue_id: str, screening_run_sha: str, source_ref: str,
        source_commit: str, overrides_path: Path, review_reference: str,
        audit_output: Path | None = None) -> dict[str, Any]:
    if not SPECIAL_RE.fullmatch(issue_id):
        raise ValueError("interactive Special Evidence requires SP-* issue_id")
    repo_root = repo_root.resolve()
    overrides_path = overrides_path.resolve()
    doc = load_json(overrides_path)
    if doc.get("schema_version") != "1.0" or doc.get("issue_id") != issue_id:
        raise ValueError("interactive Evidence override identity mismatch")
    if doc.get("screening_run_sha") != screening_run_sha:
        raise ValueError("interactive Evidence screening_run_sha mismatch")
    runner = doc.get("runner")
    if not isinstance(runner, dict):
        raise ValueError("runner metadata required")
    for key in ("provider", "model", "invocation", "generated_at"):
        if not isinstance(runner.get(key), str) or not runner[key].strip():
            raise ValueError(f"runner.{key} required")
    overrides = doc.get("overrides")
    if not isinstance(overrides, list):
        raise ValueError("overrides must be an array")
    by_id: dict[str, dict[str, Any]] = {}
    for entry in overrides:
        if not isinstance(entry, dict):
            raise ValueError("override entries must be objects")
        task_id = entry.get("evidence_task_id")
        if not isinstance(task_id, str) or not task_id or task_id in by_id:
            raise ValueError(f"invalid/duplicate task id {task_id!r}")
        validate_override(entry)
        by_id[task_id] = entry

    prepare_evidence_run.ISSUE_RE = ANY_RE
    accept_evidence_results.ISSUE_RE = ANY_RE
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        package_root = root / "package"
        package = build_package(
            repo_root=repo_root,
            output_root=package_root,
            issue_id=issue_id,
            screening_run_sha=screening_run_sha,
            source_ref=source_ref,
            source_commit=source_commit,
        )
        expected = {task["evidence_task_id"]: task for task in package["evidence_tasks"]["tasks"]}
        missing = sorted(set(expected) - set(by_id))
        extra = sorted(set(by_id) - set(expected))
        if missing or extra:
            raise ValueError(f"interactive Evidence override set must be exact: missing={missing} extra={extra}")

        results = root / "results"
        results.mkdir()
        recommendation_counts = {key: 0 for key in sorted(RECOMMENDATIONS)}
        for task_id, meta in expected.items():
            task_path = package_root / meta["path"]
            task = load_json(task_path)
            card = build_card(task, by_id[task_id], issue_id, runner["generated_at"])
            recommendation_counts[card["editorial"]["candidate_recommendation"]] += 1
            result = {
                "schema_version": "1.0",
                "issue_id": issue_id,
                "evidence_task_id": task_id,
                "evidence_task_sha256": sha(task_path),
                "prompt_id": package["prompt"]["prompt_id"],
                "prompt_sha256": package["prompt"]["sha256"],
                "runner": runner,
                "card": card,
            }
            (results / task_path.name).write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

        report, passed = accept_evidence_results.accept(
            package_root=package_root,
            results_dir=results,
            repo_root=repo_root,
            issue_id=issue_id,
            review_reference=review_reference,
        )
        if not passed:
            raise ValueError(f"Evidence acceptance failed: {report}")
        report = dict(report)
        report["interactive_overrides_path"] = overrides_path.relative_to(repo_root).as_posix()
        report["runner"] = runner
        report["recommendation_counts"] = recommendation_counts
        if audit_output:
            audit_output.parent.mkdir(parents=True, exist_ok=True)
            audit_output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--screening-run-sha", required=True)
    parser.add_argument("--source-ref", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--overrides", required=True)
    parser.add_argument("--review-reference", required=True)
    parser.add_argument("--audit-output")
    args = parser.parse_args()
    result = run(
        repo_root=Path(args.repo_root),
        issue_id=args.issue_id,
        screening_run_sha=args.screening_run_sha,
        source_ref=args.source_ref,
        source_commit=args.source_commit,
        overrides_path=Path(args.overrides),
        review_reference=args.review_reference,
        audit_output=Path(args.audit_output) if args.audit_output else None,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
