#!/usr/bin/env python3
"""Run Special source expansion with reader-facing titles from approved Architecture.

Draft Packages intentionally do not duplicate Architecture package titles. This
runner joins the title by package_id at execution time without mutating any
immutable upstream artifact, then delegates all expansion/provenance work to the
canonical generator.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import expand_special_validated_source as expansion


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", default="v0.2")
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    plan_path = root / "sources" / args.issue_id / "architecture" / "issue-architecture-v0.1.json"
    plan = load_json(plan_path)
    if plan.get("status") != "APPROVED":
        raise ValueError("Issue Architecture must be APPROVED")
    titles = {
        str(package["package_id"]): str(package["title"])
        for package in plan.get("packages") or []
        if isinstance(package, dict) and package.get("package_id") and package.get("title")
    }

    original_renderer = expansion.render_technical_notes

    def render_with_architecture_title(package: dict[str, Any]) -> str:
        package_id = str(package.get("package_id") or "")
        if package_id not in titles:
            raise ValueError(f"approved Architecture title missing for package: {package_id}")
        joined = dict(package)
        joined["title"] = titles[package_id]
        return original_renderer(joined)

    expansion.render_technical_notes = render_with_architecture_title
    result = expansion.build(root, args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
