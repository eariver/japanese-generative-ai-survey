#!/usr/bin/env python3
"""Validate one article Draft Run against its exact SHA-bound drafting package.

The validator checks package/prompt provenance, primary-Evidence coverage, claim
ledger references and evidence classes, citation-key integrity, architecture
boundary coverage, and Late Breaking treatment before prose can enter LaTeX.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

EVIDENCE_CLASSES = {
    "PRIMARY_FACT",
    "VENDOR_CLAIM",
    "PROJECT_CLAIM",
    "AUTHOR_CLAIM",
    "SOCIAL_OBSERVATION",
    "INFERENCE",
}
ASSERTION_MODE = {
    "PRIMARY_FACT": "FACT",
    "VENDOR_CLAIM": "ATTRIBUTED_CLAIM",
    "PROJECT_CLAIM": "ATTRIBUTED_CLAIM",
    "AUTHOR_CLAIM": "ATTRIBUTED_CLAIM",
    "SOCIAL_OBSERVATION": "ATTRIBUTED_CLAIM",
    "INFERENCE": "INFERENCE",
}
CITE_RE = re.compile(r"\\(?:auto|text|paren)cite(?:\[[^\]]*\]){0,2}\{([^}]+)\}")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def valid_datetime(value: Any) -> bool:
    if not nonempty(value):
        return False
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def body_citation_keys(latex: str | None) -> set[str]:
    if not latex:
        return set()
    keys: set[str] = set()
    for match in CITE_RE.finditer(latex):
        for key in match.group(1).split(","):
            normalized = key.strip()
            if normalized:
                keys.add(normalized)
    return keys


def evidence_maps(package: dict[str, Any]) -> tuple[dict[str, dict[str, Any]], set[str], set[str]]:
    cards: dict[str, dict[str, Any]] = {}
    primary_ids: set[str] = set()
    supporting_ids: set[str] = set()
    for field, target in (("primary_evidence", primary_ids), ("supporting_evidence", supporting_ids)):
        values = package.get(field)
        if not isinstance(values, list):
            raise ValueError(f"drafting package {field} must be an array")
        for entry in values:
            if not isinstance(entry, dict):
                raise ValueError(f"drafting package {field} contains non-object entry")
            task_id = entry.get("evidence_task_id")
            card = entry.get("card")
            if not nonempty(task_id) or not isinstance(card, dict):
                raise ValueError(f"drafting package {field} contains invalid entry")
            if task_id in cards:
                raise ValueError(f"drafting package repeats evidence_task_id: {task_id}")
            cards[task_id] = card
            target.add(task_id)
    return cards, primary_ids, supporting_ids


def source_catalog_maps(package: dict[str, Any], cards: dict[str, dict[str, Any]]) -> tuple[dict[str, dict[str, Any]], dict[tuple[str, str], str]]:
    by_key: dict[str, dict[str, Any]] = {}
    by_source: dict[tuple[str, str], str] = {}
    catalog = package.get("source_catalog")
    if not isinstance(catalog, list):
        raise ValueError("drafting package source_catalog must be an array")
    for item in catalog:
        if not isinstance(item, dict):
            raise ValueError("source_catalog contains non-object item")
        key = item.get("citation_key")
        task_id = item.get("evidence_task_id")
        source_id = item.get("source_id")
        if not nonempty(key) or not nonempty(task_id) or not nonempty(source_id):
            raise ValueError("source_catalog contains invalid key/task/source")
        if key in by_key:
            raise ValueError(f"duplicate citation_key in source_catalog: {key}")
        if (task_id, source_id) in by_source:
            raise ValueError(f"duplicate task/source in source_catalog: {task_id}#{source_id}")
        card = cards.get(task_id)
        if card is None:
            raise ValueError(f"source_catalog references package-external Evidence Task: {task_id}")
        card_source = next((source for source in card.get("sources") or [] if source.get("source_id") == source_id), None)
        if card_source is None:
            raise ValueError(f"source_catalog references unknown Evidence source: {task_id}#{source_id}")
        by_key[key] = item
        by_source[(task_id, source_id)] = key
    return by_key, by_source


def id_map(values: Any, field: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    if not isinstance(values, list):
        return result
    for value in values:
        if isinstance(value, dict) and nonempty(value.get(field)):
            result[value[field]] = value
    return result


def validate(package_path: Path, run_path: Path, prompt_path: Path) -> tuple[dict[str, Any], bool]:
    package = load_json(package_path)
    run = load_json(run_path)
    errors: list[str] = []

    if package.get("runner_mode") != "LLM_DRAFT":
        errors.append(f"draft validator accepts only runner_mode=LLM_DRAFT, got {package.get('runner_mode')!r}")
    if run.get("schema_version") != "1.0":
        errors.append("run.schema_version must be 1.0")
    if run.get("issue_id") != package.get("issue_id"):
        errors.append("run.issue_id does not match drafting package")
    if run.get("package_id") != package.get("package_id"):
        errors.append("run.package_id does not match drafting package")
    if run.get("drafting_package_sha256") != sha256_file(package_path):
        errors.append("run.drafting_package_sha256 does not match exact package bytes")
    if run.get("prompt_id") != "article-drafting-v0.1":
        errors.append("run.prompt_id must be article-drafting-v0.1")
    if run.get("prompt_sha256") != sha256_file(prompt_path):
        errors.append("run.prompt_sha256 does not match exact prompt bytes")

    runner = run.get("runner")
    if not isinstance(runner, dict):
        errors.append("run.runner must be an object")
    else:
        for field in ("provider", "model", "invocation"):
            if not nonempty(runner.get(field)):
                errors.append(f"run.runner.{field} must be non-empty")
        if not valid_datetime(runner.get("generated_at")):
            errors.append("run.runner.generated_at must be timezone-aware ISO-8601")

    cards, primary_ids, supporting_ids = evidence_maps(package)
    allowed_ids = set(cards)
    catalog_by_key, citation_by_source = source_catalog_maps(package, cards)

    draft = run.get("draft")
    if not isinstance(draft, dict):
        errors.append("run.draft must be an object")
        draft = {}
    status = draft.get("status")
    if status not in {"DRAFTED", "NEEDS_EVIDENCE", "BLOCKED"}:
        errors.append("draft.status must be DRAFTED, NEEDS_EVIDENCE, or BLOCKED")

    used_ids = draft.get("evidence_task_ids_used")
    if not isinstance(used_ids, list):
        errors.append("draft.evidence_task_ids_used must be an array")
        used_ids = []
    if len(used_ids) != len(set(used_ids)):
        errors.append("draft.evidence_task_ids_used contains duplicates")
    external_used = sorted(set(used_ids) - allowed_ids)
    if external_used:
        errors.append(f"draft uses Evidence Tasks outside package: {external_used}")
    if status == "DRAFTED":
        missing_primary = sorted(primary_ids - set(used_ids))
        if missing_primary:
            errors.append(f"DRAFTED package omits primary Evidence Tasks: {missing_primary}")
        if not nonempty(draft.get("title")):
            errors.append("DRAFTED package requires non-empty title")
        if not nonempty(draft.get("latex_body")):
            errors.append("DRAFTED package requires non-empty latex_body")

    ledger = draft.get("claim_ledger")
    if not isinstance(ledger, list):
        errors.append("draft.claim_ledger must be an array")
        ledger = []
    claim_ids_seen: set[str] = set()
    ledger_citations: set[str] = set()
    ledger_tasks: set[str] = set()

    for index, claim in enumerate(ledger):
        prefix = f"claim_ledger[{index}]"
        if not isinstance(claim, dict):
            errors.append(f"{prefix} must be an object")
            continue
        draft_claim_id = claim.get("draft_claim_id")
        if not nonempty(draft_claim_id):
            errors.append(f"{prefix}.draft_claim_id must be non-empty")
        elif draft_claim_id in claim_ids_seen:
            errors.append(f"duplicate draft_claim_id: {draft_claim_id}")
        else:
            claim_ids_seen.add(draft_claim_id)

        evidence_class = claim.get("evidence_class")
        if evidence_class not in EVIDENCE_CLASSES:
            errors.append(f"{prefix}.evidence_class is invalid: {evidence_class!r}")
        elif claim.get("assertion_mode") != ASSERTION_MODE[evidence_class]:
            errors.append(
                f"{prefix}.assertion_mode must be {ASSERTION_MODE[evidence_class]} for {evidence_class}"
            )

        refs = claim.get("evidence_refs")
        if not isinstance(refs, list) or not refs:
            errors.append(f"{prefix}.evidence_refs must be a non-empty array")
            refs = []
        structured_classes: list[str] = []
        expected_citations: set[str] = set()
        for ref_index, ref in enumerate(refs):
            ref_prefix = f"{prefix}.evidence_refs[{ref_index}]"
            if not isinstance(ref, dict):
                errors.append(f"{ref_prefix} must be an object")
                continue
            task_id = ref.get("evidence_task_id")
            if task_id not in allowed_ids:
                errors.append(f"{ref_prefix} references package-external Evidence Task: {task_id!r}")
                continue
            ledger_tasks.add(task_id)
            card = cards[task_id]
            claims = id_map(card.get("claims"), "claim_id")
            metrics = id_map(card.get("metrics"), "metric_id")
            limitations = id_map(card.get("limitations"), "limitation_id")
            events = card.get("temporal", {}).get("events") or []
            sources = {source.get("source_id"): source for source in card.get("sources") or [] if nonempty(source.get("source_id"))}

            underlying_source_ids: set[str] = set()
            for field, mapping in (("claim_ids", claims), ("metric_ids", metrics), ("limitation_ids", limitations)):
                values = ref.get(field)
                if not isinstance(values, list):
                    errors.append(f"{ref_prefix}.{field} must be an array")
                    values = []
                for value in values:
                    item = mapping.get(value)
                    if item is None:
                        errors.append(f"{ref_prefix}.{field} references unknown ID: {value!r}")
                        continue
                    underlying_source_ids.update(item.get("source_ids") or [])
                    if field != "limitation_ids" and item.get("evidence_class"):
                        structured_classes.append(item["evidence_class"])

            event_indices = ref.get("event_indices")
            if not isinstance(event_indices, list):
                errors.append(f"{ref_prefix}.event_indices must be an array")
                event_indices = []
            for event_index in event_indices:
                if not isinstance(event_index, int) or isinstance(event_index, bool) or not (0 <= event_index < len(events)):
                    errors.append(f"{ref_prefix}.event_indices contains invalid index: {event_index!r}")
                    continue
                event = events[event_index]
                underlying_source_ids.update(event.get("source_ids") or [])
                structured_classes.append("PRIMARY_FACT")

            ref_source_ids = ref.get("source_ids")
            if not isinstance(ref_source_ids, list):
                errors.append(f"{ref_prefix}.source_ids must be an array")
                ref_source_ids = []
            unknown_sources = sorted(set(ref_source_ids) - set(sources))
            if unknown_sources:
                errors.append(f"{ref_prefix}.source_ids references unknown source IDs: {unknown_sources}")
            missing_underlying = sorted(underlying_source_ids - set(ref_source_ids))
            if missing_underlying:
                errors.append(
                    f"{ref_prefix}.source_ids must include sources used by referenced Evidence items: {missing_underlying}"
                )
            for source_id in ref_source_ids:
                key = citation_by_source.get((task_id, source_id))
                if key is None:
                    errors.append(f"{ref_prefix} source has no citation key in package catalog: {task_id}#{source_id}")
                else:
                    expected_citations.add(key)

        if evidence_class != "INFERENCE":
            if not structured_classes:
                errors.append(f"{prefix}: non-INFERENCE claim must reference claim/metric/event Evidence")
            mismatched = sorted({value for value in structured_classes if value != evidence_class})
            if mismatched:
                errors.append(
                    f"{prefix}: draft evidence_class {evidence_class} does not match referenced Evidence classes {mismatched}"
                )
        elif not refs:
            errors.append(f"{prefix}: INFERENCE requires supporting Evidence refs")

        citation_keys = claim.get("citation_keys")
        if not isinstance(citation_keys, list) or not citation_keys:
            errors.append(f"{prefix}.citation_keys must be a non-empty array")
            citation_keys = []
        if len(citation_keys) != len(set(citation_keys)):
            errors.append(f"{prefix}.citation_keys contains duplicates")
        unknown_keys = sorted(set(citation_keys) - set(catalog_by_key))
        if unknown_keys:
            errors.append(f"{prefix}.citation_keys contains package-external keys: {unknown_keys}")
        if set(citation_keys) != expected_citations:
            errors.append(
                f"{prefix}.citation_keys must exactly match Evidence ref source_ids; expected={sorted(expected_citations)} actual={sorted(set(citation_keys))}"
            )
        ledger_citations.update(citation_keys)

    if status == "DRAFTED":
        missing_ledger_tasks = sorted(primary_ids - ledger_tasks)
        if missing_ledger_tasks:
            errors.append(f"claim ledger does not materially reference primary Evidence Tasks: {missing_ledger_tasks}")

    latex_body = draft.get("latex_body")
    body_keys = body_citation_keys(latex_body if isinstance(latex_body, str) else None)
    unknown_body_keys = sorted(body_keys - set(catalog_by_key))
    if unknown_body_keys:
        errors.append(f"latex_body cites package-external keys: {unknown_body_keys}")
    if status == "DRAFTED":
        missing_from_body = sorted(ledger_citations - body_keys)
        unledgered_body = sorted(body_keys - ledger_citations)
        if missing_from_body:
            errors.append(f"claim-ledger citation keys missing from latex_body: {missing_from_body}")
        if unledgered_body:
            errors.append(f"latex_body citations are not represented in claim ledger: {unledgered_body}")

    package_spec = package.get("package") or {}
    must_cover = package_spec.get("must_cover") or []
    must_coverage = draft.get("must_cover_coverage")
    if not isinstance(must_coverage, list):
        errors.append("draft.must_cover_coverage must be an array")
        must_coverage = []
    must_keys = [value.get("requirement") for value in must_coverage if isinstance(value, dict)]
    if len(must_keys) != len(set(must_keys)):
        errors.append("must_cover_coverage contains duplicate requirements")
    if set(must_keys) != set(must_cover):
        errors.append("must_cover_coverage must cover package.must_cover exactly")
    for item in must_coverage:
        if not isinstance(item, dict):
            continue
        if item.get("status") not in {"COVERED", "BLOCKED"}:
            errors.append(f"invalid must_cover coverage status: {item.get('status')!r}")
        if item.get("status") == "BLOCKED" and not nonempty(item.get("note")):
            errors.append(f"BLOCKED must-cover item requires note: {item.get('requirement')!r}")
        if status == "DRAFTED" and item.get("status") == "BLOCKED":
            errors.append(f"DRAFTED package cannot leave must-cover item BLOCKED: {item.get('requirement')!r}")

    boundaries = package_spec.get("boundaries") or []
    boundary_coverage = draft.get("boundary_coverage")
    if not isinstance(boundary_coverage, list):
        errors.append("draft.boundary_coverage must be an array")
        boundary_coverage = []
    boundary_keys = [value.get("boundary") for value in boundary_coverage if isinstance(value, dict)]
    if len(boundary_keys) != len(set(boundary_keys)):
        errors.append("boundary_coverage contains duplicate boundaries")
    if set(boundary_keys) != set(boundaries):
        errors.append("boundary_coverage must cover package.boundaries exactly")
    for item in boundary_coverage:
        if not isinstance(item, dict):
            continue
        coverage_status = item.get("status")
        if coverage_status not in {"PRESERVED", "NOT_APPLICABLE", "BLOCKED"}:
            errors.append(f"invalid boundary coverage status: {coverage_status!r}")
        if coverage_status in {"NOT_APPLICABLE", "BLOCKED"} and not nonempty(item.get("note")):
            errors.append(f"{coverage_status} boundary requires note: {item.get('boundary')!r}")
        if status == "DRAFTED" and coverage_status == "BLOCKED":
            errors.append(f"DRAFTED package cannot leave boundary BLOCKED: {item.get('boundary')!r}")

    if status == "DRAFTED" and package_spec.get("late_breaking") is True:
        if not isinstance(latex_body, str) or "latebreaking" not in latex_body:
            errors.append("Late Breaking DRAFTED package must use latebreaking LaTeX treatment")

    open_questions = draft.get("open_questions")
    if not isinstance(open_questions, list) or any(not nonempty(value) for value in open_questions):
        errors.append("draft.open_questions must be an array of non-empty strings")
    if status in {"NEEDS_EVIDENCE", "BLOCKED"} and not open_questions:
        errors.append(f"{status} draft requires at least one open_question")

    report = {
        "schema_version": "1.0",
        "passed": not errors,
        "issue_id": package.get("issue_id"),
        "package_id": package.get("package_id"),
        "draft_status": status,
        "primary_evidence_count": len(primary_ids),
        "supporting_evidence_count": len(supporting_ids),
        "claim_ledger_count": len(ledger),
        "catalog_citation_count": len(catalog_by_key),
        "body_citation_count": len(body_keys),
        "errors": errors,
    }
    return report, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", required=True)
    parser.add_argument("--run", required=True)
    parser.add_argument("--prompt", default="config/prompts/editorial/article-drafting-v0.1.md")
    parser.add_argument("--report")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report, passed = validate(Path(args.package), Path(args.run), Path(args.prompt))
    if args.report:
        path = Path(args.report)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
