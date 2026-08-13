#!/usr/bin/env python3
# Validate the reader-facing Special layout contract before PDF publication.
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inspect_layout(
    manifest: dict[str, Any],
    main_text: str,
    architecture: dict[str, Any],
) -> list[str]:
    errors: list[str] = []
    articles = [x for x in (manifest.get("articles") or []) if isinstance(x, dict)]
    if not articles:
        return ["validated Special source has no article entries"]

    override = architecture.get("layout_override") or {}
    single_column_approved = (
        architecture.get("status") == "APPROVED"
        and isinstance(override, dict)
        and override.get("narrative_body_mode") == "single-column"
        and bool(str(override.get("approval_reference") or "").strip())
    )
    if single_column_approved:
        return errors

    body_mode = str((manifest.get("layout") or {}).get("body_mode") or "")
    if "single-column" in body_mode.lower():
        errors.append(
            "Special narrative body_mode regressed to single-column without approved override"
        )
    if "two-column" not in body_mode.lower() or "multicol" not in body_mode.lower():
        errors.append(
            "Special layout manifest does not declare local two-column multicols narrative"
        )
    if r"\twocolumn" in main_text or r"\onecolumn" in main_text:
        errors.append(
            "global twocolumn/onecolumn switch is forbidden for normal Special layout"
        )

    begin_count = main_text.count(r"\begin{multicols}{2}")
    end_count = main_text.count(r"\end{multicols}")
    if begin_count != len(articles) or end_count != len(articles):
        errors.append(
            "expected one balanced two-column narrative block per article: "
            f"articles={len(articles)} begin={begin_count} end={end_count}"
        )

    front = str(
        (manifest.get("frontmatter") or {}).get("path")
        or "sections/00-frontmatter.tex"
    )
    front_input = r"\input{" + Path(front).with_suffix("").as_posix() + "}"
    first_multicol = main_text.find(r"\begin{multicols}{2}")
    if front_input not in main_text or (
        first_multicol >= 0 and main_text.find(front_input) > first_multicol
    ):
        errors.append("frontmatter must remain full-width before narrative multicols")

    depth = 0
    for line in main_text.splitlines():
        if r"\begin{multicols}{2}" in line:
            depth += 1
        if (
            "technical-notes/" in line
            and r"\input{" in line
            and depth != 0
        ):
            errors.append("Technical Notes input is nested inside narrative multicols")
        if r"\end{multicols}" in line:
            depth -= 1
        if depth < 0:
            errors.append("unbalanced multicols end marker")
            depth = 0
    if depth != 0:
        errors.append("unbalanced multicols environment")
    return errors


def check(repo_root: Path, issue_id: str) -> dict[str, Any]:
    state = load_json(repo_root / "sources" / issue_id / "pipeline-state.json")
    source = state.get("provenance", {}).get("validated_issue_source") or {}
    manifest_path = repo_root / str(source.get("path") or "")
    if not manifest_path.is_file() or sha(manifest_path) != source.get("sha256"):
        raise ValueError("state-pinned source manifest missing or SHA mismatch")
    manifest = load_json(manifest_path)

    main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_path = manifest_path.parent / main_rel
    if not main_path.is_file():
        raise ValueError("state-pinned main.tex missing")

    architecture_path = (
        repo_root
        / "sources"
        / issue_id
        / "architecture"
        / "issue-architecture-v0.1.json"
    )
    architecture = load_json(architecture_path)
    errors = inspect_layout(
        manifest,
        main_path.read_text(encoding="utf-8"),
        architecture,
    )
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "source_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "article_count": len(manifest.get("articles") or []),
        "passed": not errors,
        "errors": errors,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--issue-id", required=True)
    args = ap.parse_args()
    report = check(Path(args.repo_root).resolve(), args.issue_id)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
