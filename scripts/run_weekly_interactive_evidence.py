#!/usr/bin/env python3
"""Expand a compact Weekly Evidence review into complete validated Evidence Runs.

Weekly screening can retain a large verification queue. This no-paid-provider path
keeps the review file compact while remaining evidence-safe:

- every Evidence Task is materialized exactly once;
- unreviewed paper/release tasks default to PARTIAL/HOLD, never VERIFIED;
- official index snapshots default to NEEDS_MORE/INSPECT_MORE;
- explicit reviewed overrides may promote, reject, or further qualify individual tasks;
- the exact hash-pinned Evidence package, semantic validator, and append-only
  ``accept_evidence_results`` path remain authoritative.

The compact review therefore records editorial judgment without manufacturing
primary-source verification for tasks that have not actually been reviewed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts import accept_evidence_results, prepare_evidence_run
from scripts import run_special_interactive_evidence as shared

WEEKLY_RE = re.compile(r"^[0-9]{4}-W[0-9]{2}$")
RECOMMENDATIONS = {"CANDIDATE", "HOLD", "REJECT", "INSPECT_MORE"}
CARD_STATUSES = {"VERIFIED", "PARTIAL", "REJECTED", "NEEDS_MORE"}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_verification_queue(repo_root: Path, package: dict[str, Any]) -> dict[str, dict[str, Any]]:
    queue_path = repo_root / package["screening_basis"]["verification_queue_path"]
    if not queue_path.is_file():
        raise ValueError(f"verification queue missing: {queue_path}")
    records: dict[str, dict[str, Any]] = {}
    for line_no, raw in enumerate(queue_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        value = json.loads(raw)
        sid = value.get("screening_id")
        record = value.get("record")
        if not isinstance(sid, str) or not sid or sid in records or not isinstance(record, dict):
            raise ValueError(f"invalid verification queue record at line {line_no}")
        records[sid] = record
    return records


def event_date(record: dict[str, Any]) -> str | None:
    value = record.get("published_at") or record.get("observed_at")
    return value if isinstance(value, str) and value else None


def repo_name_from_screening_id(screening_id: str) -> str | None:
    if not screening_id.startswith("github-release:"):
        return None
    body = screening_id[len("github-release:"):]
    return body.split("@", 1)[0] if "@" in body else body


def default_entry(task: dict[str, Any], queue: dict[str, dict[str, Any]], issue_id: str) -> dict[str, Any]:
    task_id = task["evidence_task_id"]
    screening_ids = task.get("screening_ids") or []
    records = []
    for sid in screening_ids:
        record = queue.get(sid)
        if record is None:
            raise ValueError(f"{task_id}: screening record absent from accepted verification queue: {sid}")
        records.append(record)
    if not records:
        raise ValueError(f"{task_id}: no screening records")

    task_type = task.get("task_type")
    source_types = set(task.get("source_types") or [])
    first = records[0]
    first_title = first.get("title") if isinstance(first.get("title"), str) and first.get("title") else screening_ids[0]
    first_date = event_date(first)

    if task_type == "INSPECT_INDEX":
        return {
            "evidence_task_id": task_id,
            "artifact": {"canonical_name": first_title, "artifact_type": "OTHER", "organization": None},
            "candidate_recommendation": "INSPECT_MORE",
            "status": "NEEDS_MORE",
            "why_now_confirmed": False,
            "why_this_special": (
                f"The official index snapshot is preserved in {issue_id}, but this task does not identify an item-level "
                "event that can support a standalone technical claim."
            ),
            "claims": [{
                "text": "The captured official index is a discovery source; the index snapshot alone is not item-level technical evidence.",
                "evidence_class": "PRIMARY_FACT",
                "source_indexes": [1],
            }],
            "limitations": [
                "No concrete item-level W33 event has been established from this index task.",
                "Do not infer a product/model release merely from the presence of the organization index in Source Intake.",
            ],
            "target_findings": {
                target: {"status": "UNRESOLVED", "finding": "Item-level source inspection is still required before this index can affect Candidate Selection."}
                for target in task.get("verification_targets") or []
            },
            "unresolved_questions": ["Which concrete item, if any, from this official index belongs in the W33 editorial window?"],
            "rationale": "Preserve the source for targeted inspection; do not promote an index page itself as a candidate.",
        }

    if source_types == {"paper"}:
        return {
            "evidence_task_id": task_id,
            "artifact": {"canonical_name": first_title, "artifact_type": "PAPER", "organization": None},
            "candidate_recommendation": "HOLD",
            "status": "PARTIAL",
            "why_now_confirmed": bool(first_date),
            "why_this_special": (
                f"The arXiv record falls inside the {issue_id} discovery window, but the default pass is abstract-level only; "
                "headline use requires paper-level method/setup review."
            ),
            "artifact_first_announced": first_date,
            "events": ([{"event_type": "PAPER_SUBMISSION", "event_date": first_date, "source_published_at": first_date, "source_indexes": [1]}]
                       if first_date else []),
            "claims": [
                {"text": f"The primary arXiv record identifies the paper titled '{first_title}'.", "evidence_class": "PRIMARY_FACT", "source_indexes": [1]},
                {"text": "Method, metric, comparison, and performance statements in the supplied abstract remain author-reported until full-paper review.", "evidence_class": "AUTHOR_CLAIM", "source_indexes": [1]},
            ],
            "limitations": [
                "This default Evidence pass verifies paper identity/chronology only and does not constitute full-paper review.",
                "Abstract-level benchmark or superiority statements must not be generalized beyond the authors' reported setup.",
            ],
            "target_findings": {
                target: {"status": "UNRESOLVED", "finding": "Identity/chronology are available from arXiv, but technical-claim and overlap review remains incomplete in the default pass."}
                for target in task.get("verification_targets") or []
            },
            "unresolved_questions": ["Does full-paper review support promotion beyond Paper Watch/HOLD after cross-candidate comparison?"],
            "rationale": "Retain as a paper-level lead while preserving the boundary between abstract screening and verified technical evidence.",
        }

    if source_types == {"github-release"}:
        repo = repo_name_from_screening_id(screening_ids[0])
        series = task_type == "VERIFY_SERIES"
        canonical_name = task.get("grouping", {}).get("duplicate_group") if series else None
        canonical_name = canonical_name or (f"{repo} {first_title}" if repo else first_title)
        events = []
        for index, record in enumerate(records, start=1):
            date = event_date(record)
            if date:
                events.append({"event_type": "SOFTWARE_RELEASE", "event_date": date, "source_published_at": date, "source_indexes": [index]})
        return {
            "evidence_task_id": task_id,
            "artifact": {"canonical_name": canonical_name, "artifact_type": "FRAMEWORK", "organization": repo},
            "candidate_recommendation": "HOLD",
            "status": "PARTIAL",
            "why_now_confirmed": bool(events),
            "why_this_special": f"The repository release record(s) fall in {issue_id}; significance and individual release-note claims still require targeted review.",
            "artifact_first_announced": events[0]["event_date"] if events else None,
            "events": events,
            "claims": [
                {"text": "The cited GitHub release page(s) establish repository release activity in the W33 window.", "evidence_class": "PRIMARY_FACT", "source_indexes": list(range(1, len(records) + 1))},
                {"text": "Technical highlights in release notes are project-maintainer claims until the relevant changes/setup are reviewed.", "evidence_class": "PROJECT_CLAIM", "source_indexes": list(range(1, len(records) + 1))},
            ],
            "limitations": ["Default pass does not independently reproduce release-note performance or hardware-support claims."],
            "target_findings": {
                target: {"status": "UNRESOLVED", "finding": "Release chronology is present, but the task's technical significance/overlap target still requires targeted release-note review."}
                for target in task.get("verification_targets") or []
            },
            "unresolved_questions": ["Which release-note changes are material enough to survive cross-candidate comparison?"],
            "grouping_accepted": series,
            "grouping_note": "Rolling releases remain grouped unless targeted review finds materially independent events." if series else "Single release retained as one verification unit.",
            "rationale": "Preserve repository chronology and defer promotion until technical significance is explicitly reviewed.",
        }

    # Official feed items are item-level sources, unlike broad official indexes.
    if "official-feed-item" in source_types:
        return {
            "evidence_task_id": task_id,
            "artifact": {"canonical_name": first_title, "artifact_type": "OTHER", "organization": None},
            "candidate_recommendation": "HOLD",
            "status": "PARTIAL",
            "why_now_confirmed": bool(first_date),
            "why_this_special": f"The first-party item is dated within {issue_id}; concrete technical claims still require article-level review.",
            "artifact_first_announced": first_date,
            "events": ([{"event_type": "OFFICIAL_PUBLICATION", "event_date": first_date, "source_published_at": first_date, "source_indexes": [1]}]
                       if first_date else []),
            "claims": [
                {"text": f"The first-party source identifies an item titled '{first_title}' in the W33 source set.", "evidence_class": "PRIMARY_FACT", "source_indexes": [1]},
                {"text": "Capability, performance, safety, or product-impact statements remain vendor claims until reviewed at the article level.", "evidence_class": "VENDOR_CLAIM", "source_indexes": [1]},
            ],
            "limitations": ["Default pass establishes item identity/chronology, not independent validation of vendor claims."],
            "target_findings": {
                target: {"status": "UNRESOLVED", "finding": "Item identity/chronology are present; technical-claim and overlap review remains incomplete in the default pass."}
                for target in task.get("verification_targets") or []
            },
            "unresolved_questions": ["Which concrete claims from the first-party item matter to W33 Candidate Selection?"],
            "rationale": "Keep as first-party evidence input pending targeted claim review.",
        }

    return {
        "evidence_task_id": task_id,
        "artifact": {"canonical_name": first_title, "artifact_type": "OTHER", "organization": None},
        "candidate_recommendation": "HOLD",
        "status": "PARTIAL",
        "why_now_confirmed": bool(first_date),
        "why_this_special": f"The source is present in the {issue_id} verification queue but requires source-specific review before promotion.",
        "artifact_first_announced": first_date,
        "events": [],
        "claims": [{"text": "The source is preserved as a W33 verification lead.", "evidence_class": "PRIMARY_FACT", "source_indexes": [1]}],
        "limitations": ["Source-specific technical verification is incomplete."],
        "target_findings": {
            target: {"status": "UNRESOLVED", "finding": "Source-specific review remains incomplete."}
            for target in task.get("verification_targets") or []
        },
        "rationale": "Hold pending source-specific review.",
    }


def merge_entry(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    result = deepcopy(base)
    for key, value in override.items():
        if key == "artifact" and isinstance(value, dict):
            artifact = dict(result.get("artifact") or {})
            artifact.update(value)
            result["artifact"] = artifact
        elif key == "target_findings" and isinstance(value, dict):
            findings = dict(result.get("target_findings") or {})
            findings.update(value)
            result["target_findings"] = findings
        else:
            result[key] = value
    return result


def validate_review(doc: dict[str, Any], issue_id: str, screening_run_sha: str) -> dict[str, dict[str, Any]]:
    if doc.get("schema_version") != "1.0" or doc.get("issue_id") != issue_id:
        raise ValueError("interactive Weekly Evidence review identity mismatch")
    if doc.get("screening_run_sha") != screening_run_sha:
        raise ValueError("interactive Weekly Evidence screening_run_sha mismatch")
    runner = doc.get("runner")
    if not isinstance(runner, dict):
        raise ValueError("runner metadata required")
    for key in ("provider", "model", "invocation", "generated_at"):
        if not isinstance(runner.get(key), str) or not runner[key].strip():
            raise ValueError(f"runner.{key} required")
    overrides = doc.get("overrides", [])
    if not isinstance(overrides, list):
        raise ValueError("overrides must be an array")
    by_id: dict[str, dict[str, Any]] = {}
    for entry in overrides:
        if not isinstance(entry, dict):
            raise ValueError("override entries must be objects")
        task_id = entry.get("evidence_task_id")
        if not isinstance(task_id, str) or not task_id or task_id in by_id:
            raise ValueError(f"invalid/duplicate evidence_task_id: {task_id!r}")
        if entry.get("candidate_recommendation") is not None and entry["candidate_recommendation"] not in RECOMMENDATIONS:
            raise ValueError(f"{task_id}: invalid candidate_recommendation")
        if entry.get("status") is not None and entry["status"] not in CARD_STATUSES:
            raise ValueError(f"{task_id}: invalid status")
        by_id[task_id] = entry
    return by_id


def run(*, repo_root: Path, issue_id: str, screening_run_sha: str, source_ref: str,
        source_commit: str, review_path: Path, review_reference: str,
        audit_output: Path | None = None) -> dict[str, Any]:
    if not WEEKLY_RE.fullmatch(issue_id):
        raise ValueError("interactive Weekly Evidence requires YYYY-Www issue_id")
    repo_root = repo_root.resolve()
    review_path = review_path.resolve()
    doc = load_json(review_path)
    overrides = validate_review(doc, issue_id, screening_run_sha)
    runner = doc["runner"]

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        package_root = root / "package"
        package = prepare_evidence_run.build_package(
            repo_root=repo_root,
            output_root=package_root,
            issue_id=issue_id,
            screening_run_sha=screening_run_sha,
            source_ref=source_ref,
            source_commit=source_commit,
        )
        queue = load_verification_queue(repo_root, package)
        expected = {task["evidence_task_id"]: task for task in package["evidence_tasks"]["tasks"]}
        extra = sorted(set(overrides) - set(expected))
        if extra:
            raise ValueError(f"review contains unknown Evidence Tasks: {extra}")

        results = root / "results"
        results.mkdir()
        recommendation_counts = {key: 0 for key in sorted(RECOMMENDATIONS)}
        status_counts = {key: 0 for key in sorted(CARD_STATUSES)}
        overridden_count = 0
        for task_id, meta in expected.items():
            task_path = package_root / meta["path"]
            task = load_json(task_path)
            entry = default_entry(task, queue, issue_id)
            if task_id in overrides:
                entry = merge_entry(entry, overrides[task_id])
                overridden_count += 1
            shared.validate_override(entry)
            card = shared.build_card(task, entry, issue_id, runner["generated_at"])
            recommendation_counts[card["editorial"]["candidate_recommendation"]] += 1
            status_counts[card["status"]] += 1
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
        report["review_path"] = review_path.relative_to(repo_root).as_posix()
        report["override_count"] = overridden_count
        report["defaulted_count"] = len(expected) - overridden_count
        report["recommendation_counts"] = recommendation_counts
        report["card_status_counts"] = status_counts
        report["runner"] = runner
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
    parser.add_argument("--review", required=True)
    parser.add_argument("--review-reference", required=True)
    parser.add_argument("--audit-output")
    args = parser.parse_args()
    result = run(
        repo_root=Path(args.repo_root),
        issue_id=args.issue_id,
        screening_run_sha=args.screening_run_sha,
        source_ref=args.source_ref,
        source_commit=args.source_commit,
        review_path=Path(args.review),
        review_reference=args.review_reference,
        audit_output=Path(args.audit_output) if args.audit_output else None,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
