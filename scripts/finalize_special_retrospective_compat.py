#!/usr/bin/env python3
"""Retrospective Special compatibility wrapper for finalization."""
from __future__ import annotations

import tempfile
from copy import deepcopy
from pathlib import Path

from scripts import finalize_special_validated_draft as core

_ORIGINAL = core.validate_and_collect_articles


def validate_and_collect_articles_compat(
    architecture_input_path: Path,
    architecture_plan_path: Path,
    package_dir: Path,
    article_run_dir: Path,
    article_prompt_path: Path,
):
    plan = core.load_json(architecture_plan_path)
    article_ids = [
        package["package_id"]
        for package in plan.get("packages") or []
        if package.get("package_type") in core.ARTICLE_TYPES
    ]
    declared = list((plan.get("cover") or {}).get("anchor_candidates") or [])
    matched = [value for value in declared if value in article_ids]
    unknown = [value for value in declared if value not in article_ids]

    # Existing monthly plans use package IDs and keep the strict legacy path.
    # A fully semantic label set is treated as editorial hints; post-draft
    # synthesis may then choose from the exact article package set.
    if declared and unknown and not matched:
        patched = deepcopy(plan)
        patched.setdefault("cover", {})["anchor_candidates"] = article_ids
        with tempfile.TemporaryDirectory() as tmp:
            patched_path = Path(tmp) / "issue-architecture-compat.json"
            core.write_json(patched_path, patched)
            return _ORIGINAL(
                architecture_input_path,
                patched_path,
                package_dir,
                article_run_dir,
                article_prompt_path,
            )

    return _ORIGINAL(
        architecture_input_path,
        architecture_plan_path,
        package_dir,
        article_run_dir,
        article_prompt_path,
    )


def main() -> int:
    core.validate_and_collect_articles = validate_and_collect_articles_compat
    return core.main()


if __name__ == "__main__":
    raise SystemExit(main())
