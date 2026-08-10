#!/usr/bin/env python3
"""Build a post-draft issue-synthesis input from validated article drafts.

The output contains only already-validated article text plus Architecture metadata.
It is intentionally built after all ARTICLE_DRAFTING packages are complete so
cover/This Week synthesis cannot lead the technical reporting.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from scripts import validate_article_draft as draft_validator
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


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def find_draft_path(drafts_dir: Path, package_id: str) -> Path:
    candidates = [drafts_dir / f"{package_id}.draft.json", drafts_dir / f"{package_id}.json"]
    matches = [path for path in candidates if path.is_file()]
    if len(matches) > 1:
        raise ValueError(f"multiple article drafts found for {package_id}: {matches}")
    return matches[0] if matches else candidates[0]


def build(
    architecture_input_path: Path,
    architecture_plan_path: Path,
    draft_package_dir: Path,
    article_drafts_dir: Path,
    article_prompt_path: Path,
    output_path: Path,
) -> dict[str, Any]:
    architecture_report, architecture_ok = architecture_validator.validate(
        architecture_input_path, architecture_plan_path, require_approved=True
    )
    if not architecture_ok:
        raise ValueError(f"Architecture is not synthesis-ready: {architecture_report['errors']}")

    architecture_plan = load_json(architecture_plan_path)
    articles: list[dict[str, Any]] = []
    draft_records: list[dict[str, Any]] = []

    packages = [package for package in architecture_plan["packages"] if package["package_type"] in ARTICLE_TYPES]
    packages.sort(key=lambda package: package["drafting_order"])
    for package in packages:
        package_id = package["package_id"]
        draft_package_path = draft_package_dir / f"{package_id}.json"
        if not draft_package_path.is_file():
            raise ValueError(f"missing Draft Package for synthesis: {package_id}")
        draft_path = find_draft_path(article_drafts_dir, package_id)
        if not draft_path.is_file():
            raise ValueError(f"missing validated Article Draft for synthesis: {package_id}")
        report, passed = draft_validator.validate(draft_package_path, draft_path, article_prompt_path)
        if not passed:
            raise ValueError(f"Article Draft is invalid for synthesis {package_id}: {report['errors']}")
        draft = load_json(draft_path)
        articles.append(
            {
                "package_id": package_id,
                "package_type": package["package_type"],
                "drafting_order": package["drafting_order"],
                "page_target": package["page_target"],
                "late_breaking": package["late_breaking"],
                "editorial_angle": package["editorial_angle"],
                "boundaries": package.get("boundaries") or [],
                "headline": draft["headline"],
                "deck": draft["deck"],
                "blocks": [
                    {
                        "block_id": block["block_id"],
                        "block_type": block["block_type"],
                        "text": block["text"],
                        "attribution_mode": block["attribution_mode"],
                    }
                    for block in draft["blocks"]
                ],
            }
        )
        draft_records.append(
            {
                "package_id": package_id,
                "draft_package_sha256": sha256_file(draft_package_path),
                "article_draft_sha256": sha256_file(draft_path),
            }
        )

    value = {
        "schema_version": "1.0",
        "issue_id": architecture_plan["issue_id"],
        "status": "post-draft-synthesis-input-ready",
        "basis": {
            "architecture_input_sha256": sha256_file(architecture_input_path),
            "architecture_plan_sha256": sha256_file(architecture_plan_path),
            "article_prompt_sha256": sha256_file(article_prompt_path),
            "article_drafts": draft_records,
        },
        "editorial_thesis": architecture_plan["editorial_thesis"],
        "cover_anchor_candidates": architecture_plan.get("cover", {}).get("anchor_candidates") or [],
        "articles": articles,
        "constraints": {
            "language": "ja",
            "max_this_week_signals": 5,
            "no_new_external_facts": True,
            "summarize_only_validated_article_text": True,
            "late_breaking_boundary_required": True,
            "page_references_must_use_package_ids": True,
        },
    }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--architecture-input", required=True)
    parser.add_argument("--architecture-plan", required=True)
    parser.add_argument("--draft-package-dir", required=True)
    parser.add_argument("--article-drafts-dir", required=True)
    parser.add_argument("--article-prompt", default="config/prompts/editorial/article-drafting-v0.1.md")
    parser.add_argument("--output", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    value = build(
        Path(args.architecture_input), Path(args.architecture_plan),
        Path(args.draft_package_dir), Path(args.article_drafts_dir),
        Path(args.article_prompt), Path(args.output),
    )
    print(json.dumps({"issue_id": value["issue_id"], "article_count": len(value["articles"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
