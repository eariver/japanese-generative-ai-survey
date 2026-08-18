#!/usr/bin/env python3
"""Build and validate the full-Evidence Automotive E/E Architecture proposal.

The input is the shared Architecture Input produced in the Selection dry-run. This
adapter changes only experiment artifacts: it applies the Automotive edition page
budget, groups the selected Evidence according to architecture-profile.json, propagates
all Evidence boundaries, and validates the resulting PROPOSED plan with the unchanged
production Issue Architecture validator.

The legacy `this_week_summary_written_last` field is retained solely because the
production validator currently requires it. An explicit semantics overlay records that
this retrospective edition uses an executive synthesis, not a weekly summary.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any

SCRIPT = Path(__file__).resolve()
REPO_DEFAULT = SCRIPT.parents[2]
if str(REPO_DEFAULT) not in sys.path:
    sys.path.insert(0, str(REPO_DEFAULT))

from scripts import validate_issue_architecture


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def selected_map(architecture_input: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for items in (architecture_input.get("selected_by_role") or {}).values():
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            task_id = item.get("evidence_task_id")
            if isinstance(task_id, str) and task_id:
                if task_id in result:
                    raise ValueError(f"duplicate selected Evidence Task: {task_id}")
                result[task_id] = item
    return result


def union_boundaries(selected: dict[str, dict[str, Any]], ids: list[str]) -> list[str]:
    result: list[str] = []
    seen: set[str] = set()
    for task_id in ids:
        item = selected.get(task_id)
        if item is None:
            raise ValueError(f"Architecture profile references non-selected Evidence Task: {task_id}")
        for boundary in item.get("remaining_boundaries") or []:
            if isinstance(boundary, str):
                normalized = " ".join(boundary.split())
                if normalized and normalized not in seen:
                    seen.add(normalized)
                    result.append(normalized)
    return result


def render_markdown(plan: dict[str, Any], report: dict[str, Any], semantics: dict[str, Any]) -> str:
    lines = [
        "# Automotive E/E Architecture Review — experiment v0.2",
        "",
        f"- Status: **{plan['status']}**",
        f"- Planned pages: **{plan['page_budget']['planned']} / target {plan['page_budget']['target']} / max {plan['page_budget']['max']}**",
        f"- Packages: **{len(plan['packages'])}**",
        f"- Primary coverage: **{report['primary_covered_count']} / {report['primary_required_count']}**",
        "- Production lifecycle advanced: **no**",
        "- Human gate: **Architecture Review**",
        "",
        "## Editorial thesis",
        "",
        plan["editorial_thesis"],
        "",
        "## Package plan",
        "",
        "| Order | ID | Type | Pages | Title | Primary | Support |",
        "|---:|---|---|---:|---|---:|---:|",
    ]
    for package in sorted(plan["packages"], key=lambda item: item["drafting_order"]):
        title = str(package["title"]).replace("|", "\\|")
        lines.append(
            f"| {package['drafting_order']} | {package['package_id']} | {package['package_type']} | "
            f"{package['page_target']} | {title} | {len(package['primary_evidence_task_ids'])} | "
            f"{len(package['supporting_evidence_task_ids'])} |"
        )
    lines.extend([
        "",
        "## Architecture goals",
        "",
    ])
    for goal in plan["architecture_goals"]:
        lines.append(f"- {goal}")
    lines.extend([
        "",
        "## Compatibility seam discovered",
        "",
        f"- {semantics['legacy_field_note']}",
        f"- {semantics['page_budget_note']}",
        f"- {semantics['theme_note']}",
        "",
        "This proposal is not approved for drafting until the Architecture human gate is explicitly accepted.",
        "",
    ])
    return "\n".join(lines)


def build(*, shared_input_path: Path, profile_path: Path, output_root: Path) -> dict[str, Any]:
    shared_input_path = shared_input_path.resolve()
    profile_path = profile_path.resolve()
    output_root = output_root.resolve()
    shared_input = load_json(shared_input_path)
    profile = load_json(profile_path)
    issue_id = profile.get("issue_id")
    if shared_input.get("issue_id") != issue_id:
        raise ValueError("Architecture profile/input issue mismatch")

    architecture_input = json.loads(json.dumps(shared_input, ensure_ascii=False))
    budget = profile.get("page_budget") or {}
    if budget.get("target") != 48 or budget.get("max") != 64:
        raise ValueError("Automotive architecture profile must preserve the edition 48/64 page budget")
    architecture_input.setdefault("editorial_constraints", {})["page_target"] = budget["target"]
    architecture_input["editorial_constraints"]["page_max"] = budget["max"]
    # Keep this legacy field because the unchanged production validator requires it.
    architecture_input["editorial_constraints"]["this_week_summary_written_last"] = True
    profiled_input_path = output_root / "architecture-input-profiled-v0.2.json"
    write_json(profiled_input_path, architecture_input)

    selected = selected_map(architecture_input)
    packages_spec = profile.get("packages")
    if not isinstance(packages_spec, list) or not packages_spec:
        raise ValueError("architecture profile packages must be non-empty")
    packages: list[dict[str, Any]] = []
    for order, spec in enumerate(packages_spec, start=1):
        if not isinstance(spec, dict):
            raise ValueError("architecture package specs must be objects")
        primaries = spec.get("primary_evidence_task_ids") or []
        supports = spec.get("supporting_evidence_task_ids") or []
        if not isinstance(primaries, list) or not isinstance(supports, list):
            raise ValueError("package primary/support IDs must be arrays")
        packages.append({
            "package_id": spec["package_id"],
            "title": spec["title"],
            "package_type": spec["package_type"],
            "primary_evidence_task_ids": primaries,
            "supporting_evidence_task_ids": supports,
            "page_target": spec["page_target"],
            "editorial_angle": spec["editorial_angle"],
            "must_cover": spec.get("must_cover") or [],
            "boundaries": union_boundaries(selected, [*primaries, *supports]),
            "late_breaking": False,
            "drafting_order": order,
        })

    planned = sum(float(package["page_target"]) for package in packages)
    if planned != float(budget.get("planned")):
        raise ValueError(f"profile package pages {planned:g} do not match declared planned budget {budget.get('planned')}")

    plan = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "architecture_version": profile.get("architecture_version", "v0.2"),
        "status": "PROPOSED",
        "basis": {
            "architecture_input_sha256": sha256_file(profiled_input_path),
            "selection_sha256": architecture_input["basis"]["selection_sha256"],
            "matrix_sha256": architecture_input["basis"]["matrix_sha256"],
        },
        "approval": {"approved_by": None, "approved_at": None, "approval_reference": None},
        "editorial_thesis": profile["editorial_thesis"],
        "architecture_goals": profile["architecture_goals"],
        "page_budget": {
            "target": budget["target"],
            "max": budget["max"],
            "planned": planned,
        },
        "cover": {
            "headline_deferred": True,
            "headline": None,
            "anchor_candidates": profile.get("cover_anchor_candidates") or [],
        },
        "packages": packages,
        # Legacy compatibility field required by production validator. The semantics
        # overlay below explicitly renames its meaning for a retrospective edition.
        "this_week_summary_written_last": True,
    }
    plan_path = output_root / "issue-architecture-proposal-v0.2.json"
    write_json(plan_path, plan)
    validation, passed = validate_issue_architecture.validate(profiled_input_path, plan_path, require_approved=False)
    if not passed:
        raise ValueError(f"shared Issue Architecture validator rejected proposal: {validation['errors']}")

    semantics = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "basis": {
            "architecture_profile_sha256": sha256_file(profile_path),
            "architecture_input_sha256": sha256_file(profiled_input_path),
            "architecture_plan_sha256": sha256_file(plan_path),
        },
        "legacy_field_note": "`this_week_summary_written_last=true` is retained only as a production-validator compatibility field; for this retrospective it means the Executive Synthesis is finalized after package drafts stabilize.",
        "page_budget_note": "The shared Architecture Input default 16/24 page budget is overridden in the experiment artifact to the edition manifest's 48/64 pages.",
        "theme_note": "Automotive A–F thematic grouping remains profile/overlay context; it is not injected into the shared Selection or Architecture Input schemas.",
        "production_validator_modified": False,
        "production_lifecycle_advanced": False,
    }
    semantics_path = output_root / "architecture-semantics-overlay-v0.2.json"
    write_json(semantics_path, semantics)

    review_path = output_root / "ARCHITECTURE_REVIEW.md"
    review_path.write_text(render_markdown(plan, validation, semantics), encoding="utf-8")

    package_type_counts = Counter(package["package_type"] for package in packages)
    manifest = {
        "schema_version": "1.0",
        "experiment": "PROFILED_AUTOMOTIVE_EE_ARCHITECTURE_PROPOSAL",
        "issue_id": issue_id,
        "architecture_version": plan["architecture_version"],
        "status": plan["status"],
        "profiled_architecture_input": {
            "path": "architecture-input-profiled-v0.2.json",
            "sha256": sha256_file(profiled_input_path),
            "selected_item_count": architecture_input.get("selected_item_count"),
            "excluded_item_count": architecture_input.get("excluded_item_count"),
        },
        "plan": {
            "path": "issue-architecture-proposal-v0.2.json",
            "sha256": sha256_file(plan_path),
            "package_count": len(packages),
            "package_type_counts": dict(sorted(package_type_counts.items())),
            "page_target": budget["target"],
            "page_max": budget["max"],
            "planned_pages": planned,
            "primary_required_count": validation.get("primary_required_count"),
            "primary_covered_count": validation.get("primary_covered_count"),
            "missing_primary_items": validation.get("missing_primary_items"),
            "duplicate_primary_items": validation.get("duplicate_primary_items"),
            "shared_validator_passed": passed,
        },
        "review_markdown": {"path": "ARCHITECTURE_REVIEW.md", "sha256": sha256_file(review_path)},
        "semantics_overlay": {"path": "architecture-semantics-overlay-v0.2.json", "sha256": sha256_file(semantics_path)},
        "shared_validator": "scripts/validate_issue_architecture.py",
        "shared_validator_modified": False,
        "production_lifecycle_advanced": False,
        "architecture_human_gate_reached": True,
        "architecture_human_gate_approved": False,
        "finding": "The complete Automotive Evidence set can be organized into a 48-page Architecture Proposal and validated by the shared Issue Architecture validator unchanged. The remaining domain coupling is edition context: page budget, theme taxonomy and weekly-named summary semantics."
    }
    write_json(output_root / "architecture-probe-manifest.json", manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--shared-input", required=True)
    parser.add_argument("--profile", required=True)
    parser.add_argument("--output-root", required=True)
    args = parser.parse_args()
    manifest = build(
        shared_input_path=Path(args.shared_input),
        profile_path=Path(args.profile),
        output_root=Path(args.output_root),
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
