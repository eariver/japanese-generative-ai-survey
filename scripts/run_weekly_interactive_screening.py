#!/usr/bin/env python3
"""Run a complete Weekly screening pass from a compact interactive override file.

This is the no-paid-provider path for weekly issues. It regenerates the exact
screening package from the weekly work tree, expands explicit KEEP/MAYBE/INSPECT
choices plus a default DROP into one result per input record, validates every
batch, and persists the complete result set through accept_screening_results.
"""
from __future__ import annotations

import argparse
import json
import re
import tempfile
from pathlib import Path
from typing import Any

from scripts import accept_screening_results, prepare_screening_run
from scripts import run_special_interactive_screening as shared

WEEKLY_RE = re.compile(r"^[0-9]{4}-W[0-9]{2}$")


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for line_no, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        value = json.loads(raw)
        if not isinstance(value, dict):
            raise ValueError(f"{path}:{line_no}: expected JSON object")
        result.append(value)
    return result


def run(
    *,
    repo_root: Path,
    issue_id: str,
    source_ref: str,
    source_commit: str,
    overrides_path: Path,
    review_reference: str,
    audit_output: Path | None = None,
) -> dict[str, Any]:
    if not WEEKLY_RE.fullmatch(issue_id):
        raise ValueError("interactive Weekly screening requires YYYY-Www issue_id")

    repo_root = repo_root.resolve()
    overrides_path = overrides_path.resolve()
    override_doc = shared.load_json(overrides_path)
    overrides = shared.validate_overrides(override_doc, issue_id)

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        package_root = root / "package"
        package = prepare_screening_run.build_package(
            repo_root=repo_root,
            output_root=package_root,
            issue_id=issue_id,
            source_ref=source_ref,
            source_commit=source_commit,
        )

        prompt = package["prompt"]
        results_dir = root / "results"
        results_dir.mkdir()
        seen: set[str] = set()
        counts = {"KEEP": 0, "MAYBE": 0, "INSPECT": 0, "DROP": 0}
        runner = override_doc["runner"]
        default_reason = override_doc["default_drop"]["reason"]

        for batch in package["screening_input"]["batches"]:
            records = load_jsonl(package_root / batch["path"])
            decisions = []
            for record in records:
                sid = record["screening_id"]
                if sid in seen:
                    raise ValueError(f"duplicate screening_id in generated package: {sid}")
                seen.add(sid)
                decision = shared.make_decision(record, overrides.get(sid), default_reason)
                counts[decision["decision"]] += 1
                decisions.append(decision)

            result = {
                "schema_version": "1.0",
                "issue_id": issue_id,
                "batch_id": batch["batch_id"],
                "input_batch_sha256": batch["sha256"],
                "prompt_id": prompt["prompt_id"],
                "prompt_sha256": prompt["sha256"],
                "runner": runner,
                "decisions": decisions,
            }
            (results_dir / f"{batch['batch_id']}.json").write_text(
                json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )

        unknown = sorted(set(overrides) - seen)
        if unknown:
            raise ValueError(f"override screening_ids are absent from regenerated package: {unknown}")
        if len(seen) != package["screening_input"]["record_count"]:
            raise ValueError("generated screening record count mismatch")

        report, passed = accept_screening_results.accept(
            package_root=package_root,
            results_dir=results_dir,
            repo_root=repo_root,
            issue_id=issue_id,
            review_reference=review_reference,
        )
        if not passed:
            raise ValueError(f"screening acceptance failed: {report}")

        report = dict(report)
        report["decision_counts"] = counts
        report["interactive_override_path"] = overrides_path.relative_to(repo_root).as_posix()
        report["runner"] = runner
        if audit_output:
            audit_output.parent.mkdir(parents=True, exist_ok=True)
            audit_output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-ref", required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--overrides", required=True)
    parser.add_argument("--review-reference", required=True)
    parser.add_argument("--audit-output")
    args = parser.parse_args()

    result = run(
        repo_root=Path(args.repo_root),
        issue_id=args.issue_id,
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
