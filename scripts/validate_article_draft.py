#!/usr/bin/env python3
"""Validate one evidence-linked article draft against its immutable Draft Package."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any

ATTRIBUTION_MODES = {"NONE", "FACTUAL", "ATTRIBUTED", "SOCIAL", "INFERENCE", "MIXED"}
ATTRIBUTED_CLASSES = {"VENDOR_CLAIM", "PROJECT_CLAIM", "AUTHOR_CLAIM"}
NONFACT_CLASSES = ATTRIBUTED_CLASSES | {"SOCIAL_OBSERVATION", "INFERENCE"}
KINDS = {"EVENT", "CLAIM", "METRIC", "LIMITATION"}


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


def build_evidence_index(package: dict[str, Any]) -> tuple[dict[tuple[str, str, str], str], set[str], set[str], list[str]]:
    index: dict[tuple[str, str, str], str] = {}
    primary_ids: set[str] = set()
    supporting_ids: set[str] = set()
    errors: list[str] = []

    def ingest(items: Any, role: str) -> None:
        if not isinstance(items, list):
            errors.append(f"{role}_evidence must be an array")
            return
        for position, item in enumerate(items):
            if not isinstance(item, dict):
                errors.append(f"{role}_evidence[{position}] must be an object")
                continue
            task_id = item.get("evidence_task_id")
            card = item.get("card")
            if not nonempty(task_id) or not isinstance(card, dict):
                errors.append(f"{role}_evidence[{position}] lacks evidence_task_id/card")
                continue
            if card.get("evidence_task_id") not in {None, task_id}:
                errors.append(f"{role}_evidence[{position}] card/task ID mismatch")
            (primary_ids if role == "primary" else supporting_ids).add(task_id)

            for event in card.get("temporal", {}).get("events", []) or []:
                event_id = event.get("event_id") if isinstance(event, dict) else None
                if nonempty(event_id):
                    key = (task_id, "EVENT", event_id)
                    if key in index:
                        errors.append(f"duplicate Evidence reference target: {key}")
                    index[key] = "PRIMARY_FACT"
            for field, kind, id_field in (
                ("claims", "CLAIM", "claim_id"),
                ("metrics", "METRIC", "metric_id"),
                ("limitations", "LIMITATION", "limitation_id"),
            ):
                for evidence in card.get(field, []) or []:
                    evidence_id = evidence.get(id_field) if isinstance(evidence, dict) else None
                    evidence_class = evidence.get("evidence_class") if isinstance(evidence, dict) else None
                    if nonempty(evidence_id) and nonempty(evidence_class):
                        key = (task_id, kind, evidence_id)
                        if key in index:
                            errors.append(f"duplicate Evidence reference target: {key}")
                        index[key] = evidence_class

    ingest(package.get("primary_evidence"), "primary")
    ingest(package.get("supporting_evidence"), "supporting")
    overlap = sorted(primary_ids & supporting_ids)
    if overlap:
        errors.append(f"same Evidence Task appears as primary and supporting input: {overlap}")
    return index, primary_ids, supporting_ids, errors


def validate_refs(
    refs: Any,
    evidence_index: dict[tuple[str, str, str], str],
    location: str,
) -> tuple[list[str], list[str], set[str]]:
    errors: list[str] = []
    classes: list[str] = []
    task_ids: set[str] = set()
    if not isinstance(refs, list):
        return [f"{location} evidence_refs must be an array"], classes, task_ids
    tuples: list[tuple[str, str, str]] = []
    for index, ref in enumerate(refs):
        if not isinstance(ref, dict):
            errors.append(f"{location} evidence_refs[{index}] must be an object")
            continue
        task_id = ref.get("evidence_task_id")
        kind = ref.get("kind")
        evidence_id = ref.get("evidence_id")
        if not nonempty(task_id) or kind not in KINDS or not nonempty(evidence_id):
            errors.append(f"{location} evidence_refs[{index}] is malformed")
            continue
        key = (task_id, kind, evidence_id)
        tuples.append(key)
        task_ids.add(task_id)
        evidence_class = evidence_index.get(key)
        if evidence_class is None:
            errors.append(f"{location} references Evidence not present in Draft Package: {key}")
        else:
            classes.append(evidence_class)
    duplicate_refs = sorted(key for key, count in Counter(tuples).items() if count > 1)
    if duplicate_refs:
        errors.append(f"{location} contains duplicate Evidence refs: {duplicate_refs}")
    return errors, classes, task_ids


def attribution_errors(mode: Any, classes: list[str], location: str) -> list[str]:
    errors: list[str] = []
    if mode not in ATTRIBUTION_MODES:
        return [f"{location} has invalid attribution_mode {mode!r}"]
    class_set = set(classes)
    if not classes:
        if mode != "NONE":
            errors.append(f"{location} has attribution_mode={mode} but no Evidence refs")
        return errors
    if mode == "NONE":
        errors.append(f"{location} has Evidence refs but attribution_mode=NONE")
        return errors
    if mode == "FACTUAL" and class_set - {"PRIMARY_FACT"}:
        errors.append(f"{location} FACTUAL block contains non-factual Evidence classes: {sorted(class_set - {'PRIMARY_FACT'})}")
    if class_set & ATTRIBUTED_CLASSES and mode not in {"ATTRIBUTED", "MIXED"}:
        errors.append(f"{location} vendor/project/author claim requires ATTRIBUTED or MIXED mode")
    if "SOCIAL_OBSERVATION" in class_set and mode not in {"SOCIAL", "MIXED"}:
        errors.append(f"{location} social observation requires SOCIAL or MIXED mode")
    if mode == "SOCIAL" and class_set != {"SOCIAL_OBSERVATION"}:
        errors.append(f"{location} SOCIAL mode may contain only SOCIAL_OBSERVATION Evidence; use MIXED otherwise")
    if mode == "ATTRIBUTED" and ("SOCIAL_OBSERVATION" in class_set or "INFERENCE" in class_set):
        errors.append(f"{location} ATTRIBUTED mode cannot absorb social/inference Evidence; use MIXED")
    if mode == "INFERENCE" and class_set & (ATTRIBUTED_CLASSES | {"SOCIAL_OBSERVATION"}):
        errors.append(f"{location} INFERENCE mode cannot absorb attributed/social Evidence; use MIXED")
    return errors


def coverage_errors(entries: Any, required: list[str], block_ids: set[str], label: str, heading_ids: set[str]) -> list[str]:
    errors: list[str] = []
    if not isinstance(entries, list):
        return [f"{label} must be an array"]
    seen: list[str] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"{label}[{index}] must be an object")
            continue
        requirement = entry.get("requirement")
        ids = entry.get("block_ids")
        if not nonempty(requirement):
            errors.append(f"{label}[{index}].requirement must be non-empty")
            continue
        seen.append(requirement)
        if not isinstance(ids, list) or not ids:
            errors.append(f"{label}[{index}].block_ids must be non-empty")
            continue
        unknown = sorted(set(ids) - block_ids)
        if unknown:
            errors.append(f"{label}[{index}] references unknown block IDs: {unknown}")
        if set(ids) and set(ids).issubset(heading_ids):
            errors.append(f"{label}[{index}] cannot be satisfied only by HEADING blocks")
    duplicates = sorted(key for key, count in Counter(seen).items() if count > 1)
    if duplicates:
        errors.append(f"{label} repeats requirements: {duplicates}")
    required_set = set(required)
    seen_set = set(seen)
    missing = sorted(required_set - seen_set)
    extra = sorted(seen_set - required_set)
    if missing:
        errors.append(f"{label} missing package requirements: {missing}")
    if extra:
        errors.append(f"{label} contains requirements not in Draft Package: {extra}")
    return errors


def validate(package_path: Path, draft_path: Path, prompt_path: Path) -> tuple[dict[str, Any], bool]:
    package = load_json(package_path)
    draft = load_json(draft_path)
    errors: list[str] = []

    if package.get("draft_source_mode") != "EVIDENCE_PACKAGE" or package.get("execution_stage") != "ARTICLE_DRAFTING":
        errors.append("article draft validator accepts only EVIDENCE_PACKAGE / ARTICLE_DRAFTING inputs")
    if draft.get("schema_version") != "1.0":
        errors.append("draft.schema_version must be 1.0")
    if draft.get("issue_id") != package.get("issue_id"):
        errors.append("draft.issue_id does not match Draft Package")
    if draft.get("package_id") != package.get("package_id"):
        errors.append("draft.package_id does not match Draft Package")
    if draft.get("status") not in {"DRAFT", "REVISED"}:
        errors.append("draft.status must be DRAFT or REVISED")

    basis = draft.get("basis")
    if not isinstance(basis, dict):
        errors.append("draft.basis must be an object")
        basis = {}
    if basis.get("draft_package_sha256") != sha256_file(package_path):
        errors.append("draft_package_sha256 does not match exact Draft Package bytes")
    if basis.get("prompt_id") != "article-drafting-v0.1":
        errors.append("prompt_id must be article-drafting-v0.1")
    if basis.get("prompt_sha256") != sha256_file(prompt_path):
        errors.append("prompt_sha256 does not match exact article drafting prompt")

    runner = draft.get("runner")
    if not isinstance(runner, dict):
        errors.append("draft.runner must be an object")
    else:
        for field in ("provider", "model", "invocation"):
            if not nonempty(runner.get(field)):
                errors.append(f"runner.{field} must be non-empty")
        if not valid_datetime(runner.get("generated_at")):
            errors.append("runner.generated_at must be timezone-aware ISO-8601")

    if not nonempty(draft.get("headline")) or not nonempty(draft.get("deck")):
        errors.append("headline and deck must be non-empty")

    evidence_index, primary_ids, supporting_ids, evidence_errors = build_evidence_index(package)
    errors.extend(evidence_errors)
    used_tasks: set[str] = set()

    deck_errors, deck_classes, deck_tasks = validate_refs(draft.get("deck_evidence_refs"), evidence_index, "deck")
    errors.extend(deck_errors)
    used_tasks.update(deck_tasks)
    errors.extend(attribution_errors(draft.get("deck_attribution_mode"), deck_classes, "deck"))

    blocks = draft.get("blocks")
    if not isinstance(blocks, list) or not blocks:
        errors.append("draft.blocks must be a non-empty array")
        blocks = []
    block_ids: list[str] = []
    heading_ids: set[str] = set()
    late_note_count = 0
    social_ref_blocks: list[str] = []
    for index, block in enumerate(blocks):
        location = f"blocks[{index}]"
        if not isinstance(block, dict):
            errors.append(f"{location} must be an object")
            continue
        block_id = block.get("block_id")
        block_type = block.get("block_type")
        if not nonempty(block_id):
            errors.append(f"{location}.block_id must be non-empty")
            block_id = location
        else:
            block_ids.append(block_id)
        if not nonempty(block.get("text")):
            errors.append(f"{location}.text must be non-empty")
        ref_errors, classes, tasks = validate_refs(block.get("evidence_refs"), evidence_index, location)
        errors.extend(ref_errors)
        used_tasks.update(tasks)
        errors.extend(attribution_errors(block.get("attribution_mode"), classes, location))

        if block_type == "HEADING":
            heading_ids.add(block_id)
            if block.get("attribution_mode") != "NONE" or block.get("evidence_refs"):
                errors.append(f"{location} HEADING must use attribution_mode=NONE and no Evidence refs")
        if block_type == "COMMUNITY_NOTE":
            if "SOCIAL_OBSERVATION" not in set(classes):
                errors.append(f"{location} COMMUNITY_NOTE must cite SOCIAL_OBSERVATION Evidence")
        if "SOCIAL_OBSERVATION" in set(classes):
            social_ref_blocks.append(block_id)
            if block_type != "COMMUNITY_NOTE":
                errors.append(f"{location} social Evidence must be visually separated in COMMUNITY_NOTE")
        if block_type == "LATE_BREAKING_NOTE":
            late_note_count += 1

    duplicate_block_ids = sorted(key for key, count in Counter(block_ids).items() if count > 1)
    if duplicate_block_ids:
        errors.append(f"duplicate block_id values: {duplicate_block_ids}")
    block_id_set = set(block_ids)

    package_spec = package.get("package") or {}
    errors.extend(
        coverage_errors(
            draft.get("must_cover_coverage"),
            package_spec.get("must_cover") or [],
            block_id_set,
            "must_cover_coverage",
            heading_ids,
        )
    )
    errors.extend(
        coverage_errors(
            draft.get("boundary_coverage"),
            package_spec.get("boundaries") or [],
            block_id_set,
            "boundary_coverage",
            heading_ids,
        )
    )

    required_evidence_tasks = primary_ids | supporting_ids
    missing_task_usage = sorted(required_evidence_tasks - used_tasks)
    if missing_task_usage:
        errors.append(f"Draft does not use Architecture-included Evidence Tasks: {missing_task_usage}")

    late_package = package_spec.get("late_breaking") is True
    acknowledged = draft.get("late_breaking_acknowledged")
    if not isinstance(acknowledged, bool):
        errors.append("late_breaking_acknowledged must be boolean")
    if late_package and acknowledged is not True:
        errors.append("Late Breaking package requires late_breaking_acknowledged=true")
    if late_package and late_note_count == 0:
        errors.append("Late Breaking package requires at least one LATE_BREAKING_NOTE block")
    if acknowledged is False and late_note_count:
        errors.append("LATE_BREAKING_NOTE present while late_breaking_acknowledged=false")
    if acknowledged is True and late_note_count == 0:
        errors.append("late_breaking_acknowledged=true requires a LATE_BREAKING_NOTE block")

    constraints = package.get("drafting_constraints") or {}
    if constraints.get("raw_sources_forbidden") is not True or constraints.get("unknowns_remain_unknown") is not True:
        errors.append("Draft Package must preserve raw-source and unknown-value constraints")
    if constraints.get("cover_headline_finalization_forbidden") is not True:
        errors.append("Draft Package must forbid issue cover headline finalization")
    if constraints.get("this_week_summary_forbidden") is not True:
        errors.append("ARTICLE_DRAFTING package must forbid issue-level This Week summary")

    report = {
        "schema_version": "1.0",
        "passed": not errors,
        "issue_id": package.get("issue_id"),
        "package_id": package.get("package_id"),
        "draft_package_sha256": sha256_file(package_path),
        "prompt_sha256": sha256_file(prompt_path),
        "block_count": len(blocks),
        "primary_evidence_count": len(primary_ids),
        "supporting_evidence_count": len(supporting_ids),
        "used_evidence_task_count": len(used_tasks),
        "social_block_count": len(social_ref_blocks),
        "late_breaking_note_count": late_note_count,
        "missing_evidence_task_usage": missing_task_usage,
        "errors": errors,
    }
    return report, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", required=True)
    parser.add_argument("--draft", required=True)
    parser.add_argument("--prompt", default="config/prompts/editorial/article-drafting-v0.1.md")
    parser.add_argument("--report")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report, passed = validate(Path(args.package), Path(args.draft), Path(args.prompt))
    if args.report:
        path = Path(args.report)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
