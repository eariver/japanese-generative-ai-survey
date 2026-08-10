#!/usr/bin/env python3
"""Build SHA-bound per-package drafting inputs from an APPROVED Issue Architecture.

Each package contains only the Evidence Cards explicitly permitted by the approved
Architecture Plan. Sources receive deterministic citation keys so a later drafting
runner cannot silently cite material outside the package.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from scripts import validate_issue_architecture as architecture_validator


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def load_jsonl(path: Path) -> list[dict[str, Any]]:
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


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def slug(value: str) -> str:
    normalized = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return normalized[:32].rstrip("-") or "source"


def citation_key(evidence_task_id: str, source_id: str) -> str:
    prefix = hashlib.sha256(evidence_task_id.encode("utf-8")).hexdigest()[:10]
    return f"ev-{prefix}-{slug(source_id)}"


def evidence_index(evidence_reviewed: Path) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for item in load_jsonl(evidence_reviewed):
        task_id = item.get("evidence_task_id")
        if not isinstance(task_id, str) or not task_id:
            raise ValueError("evidence-reviewed item missing evidence_task_id")
        if task_id in index:
            raise ValueError(f"duplicate evidence_task_id in evidence-reviewed: {task_id}")
        index[task_id] = item
    if not index:
        raise ValueError("evidence-reviewed input is empty")
    return index


def selected_role_map(architecture_input: dict[str, Any]) -> dict[str, str]:
    roles: dict[str, str] = {}
    selected_by_role = architecture_input.get("selected_by_role")
    if not isinstance(selected_by_role, dict):
        raise ValueError("architecture input selected_by_role must be an object")
    for role, items in selected_by_role.items():
        if not isinstance(items, list):
            raise ValueError(f"architecture input role {role} must be an array")
        for item in items:
            task_id = item.get("evidence_task_id") if isinstance(item, dict) else None
            if not isinstance(task_id, str) or not task_id:
                raise ValueError(f"architecture input role {role} contains invalid item")
            if task_id in roles:
                raise ValueError(f"architecture input repeats evidence_task_id: {task_id}")
            roles[task_id] = role
    return roles


def evidence_entry(item: dict[str, Any], role: str) -> dict[str, Any]:
    return {
        "evidence_task_id": item["evidence_task_id"],
        "role": role,
        "card": item["card"],
    }


def build_source_catalog(items: list[dict[str, Any]]) -> list[dict[str, Any]]:
    catalog: list[dict[str, Any]] = []
    seen_keys: set[str] = set()
    for item in items:
        task_id = item["evidence_task_id"]
        for source in item["card"].get("sources") or []:
            source_id = source.get("source_id")
            if not isinstance(source_id, str) or not source_id:
                raise ValueError(f"Evidence Card {task_id} contains source without source_id")
            key = citation_key(task_id, source_id)
            if key in seen_keys:
                raise ValueError(f"citation key collision: {key}")
            seen_keys.add(key)
            catalog.append(
                {
                    "citation_key": key,
                    "evidence_task_id": task_id,
                    "source_id": source_id,
                    "source_class": source["source_class"],
                    "title": source["title"],
                    "url": source["url"],
                    "published_at": source.get("published_at"),
                    "role": source["role"],
                }
            )
    catalog.sort(key=lambda value: value["citation_key"])
    return catalog


def runner_mode(package_type: str) -> str:
    if package_type == "REFERENCES":
        return "DETERMINISTIC_REFERENCES"
    if package_type == "FRONTMATTER":
        return "DEFERRED_FRONTMATTER"
    return "LLM_DRAFT"


def build(
    architecture_input_path: Path,
    architecture_plan_path: Path,
    evidence_reviewed_path: Path,
    style_guide_path: Path,
    output_dir: Path,
) -> tuple[dict[str, Any], bool]:
    validation, passed = architecture_validator.validate(
        architecture_input_path,
        architecture_plan_path,
        require_approved=True,
    )
    if not passed:
        raise ValueError(f"Issue Architecture is not drafting-ready: {validation['errors']}")

    architecture_input = load_json(architecture_input_path)
    plan = load_json(architecture_plan_path)
    evidence = evidence_index(evidence_reviewed_path)
    roles = selected_role_map(architecture_input)

    issue_id = plan["issue_id"]
    issue_ids = {item.get("issue_id") for item in evidence.values()}
    if issue_ids != {issue_id}:
        raise ValueError(f"evidence-reviewed issue mismatch: {issue_ids} != {{{issue_id!r}}}")
    if not style_guide_path.is_file():
        raise ValueError(f"editorial style guide not found: {style_guide_path}")

    basis = {
        "architecture_plan_sha256": sha256_file(architecture_plan_path),
        "architecture_input_sha256": sha256_file(architecture_input_path),
        "evidence_reviewed_sha256": sha256_file(evidence_reviewed_path),
        "editorial_style_guide_sha256": sha256_file(style_guide_path),
    }

    output_dir.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    for package in sorted(plan["packages"], key=lambda value: value["drafting_order"]):
        primary_ids = package["primary_evidence_task_ids"]
        supporting_ids = package["supporting_evidence_task_ids"]
        missing = sorted(task_id for task_id in [*primary_ids, *supporting_ids] if task_id not in evidence)
        if missing:
            errors.append(f"{package['package_id']}: Evidence Runs missing from evidence-reviewed: {missing}")
            continue

        primary_items = [evidence[task_id] for task_id in primary_ids]
        supporting_items = [evidence[task_id] for task_id in supporting_ids]
        used_items = primary_items + supporting_items

        role_errors = []
        for task_id in primary_ids:
            if task_id not in roles:
                role_errors.append(f"primary task is not selected for architecture: {task_id}")
        for task_id in supporting_ids:
            if roles.get(task_id) != "SUPPORTING_EVIDENCE":
                role_errors.append(f"support task does not have SUPPORTING_EVIDENCE role: {task_id}")
        if role_errors:
            errors.extend(f"{package['package_id']}: {message}" for message in role_errors)
            continue

        value = {
            "schema_version": "1.0",
            "issue_id": issue_id,
            "package_id": package["package_id"],
            "runner_mode": runner_mode(package["package_type"]),
            "basis": basis,
            "package": {
                "title": package["title"],
                "package_type": package["package_type"],
                "page_target": package["page_target"],
                "editorial_angle": package["editorial_angle"],
                "must_cover": package["must_cover"],
                "boundaries": package["boundaries"],
                "late_breaking": package["late_breaking"],
                "drafting_order": package["drafting_order"],
            },
            "primary_evidence": [evidence_entry(item, roles[item["evidence_task_id"]]) for item in primary_items],
            "supporting_evidence": [evidence_entry(item, roles[item["evidence_task_id"]]) for item in supporting_items],
            "source_catalog": build_source_catalog(used_items),
            "article_constraints": {
                "no_new_facts_outside_evidence": True,
                "preserve_evidence_classes": True,
                "preserve_boundaries": True,
                "use_only_catalog_citations": True,
                "cover_headline_deferred": True,
                "this_week_summary_written_last": True,
            },
        }
        filename = f"{package['drafting_order']:02d}-{package['package_id']}.json"
        path = output_dir / filename
        write_json(path, value)
        records.append(
            {
                "package_id": package["package_id"],
                "package_type": package["package_type"],
                "drafting_order": package["drafting_order"],
                "runner_mode": value["runner_mode"],
                "file": filename,
                "sha256": sha256_file(path),
                "primary_evidence_count": len(primary_items),
                "supporting_evidence_count": len(supporting_items),
                "source_count": len(value["source_catalog"]),
            }
        )

    manifest = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "drafting-packages-ready" if not errors else "drafting-packages-invalid",
        "passed": not errors,
        "package_count": len(records),
        "basis": basis,
        "packages": records,
        "errors": errors,
        "rules": [
            "Each drafting package is bound to one approved Architecture Plan and exact Evidence-reviewed bytes.",
            "LLM drafting may use only Evidence Cards and citation keys included in that package.",
            "FRONTMATTER is deferred until substantive drafts stabilize; REFERENCES is deterministic/non-LLM.",
        ],
    }
    write_json(output_dir / "drafting-packages-manifest.json", manifest)
    return manifest, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--architecture-input", required=True)
    parser.add_argument("--architecture-plan", required=True)
    parser.add_argument("--evidence-reviewed", required=True)
    parser.add_argument("--style-guide", default="docs/editorial-style-guide.md")
    parser.add_argument("--output-dir", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest, passed = build(
        Path(args.architecture_input),
        Path(args.architecture_plan),
        Path(args.evidence_reviewed),
        Path(args.style_guide),
        Path(args.output_dir),
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
