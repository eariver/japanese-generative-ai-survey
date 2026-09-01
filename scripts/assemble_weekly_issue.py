#!/usr/bin/env python3
"""Assemble validated article renders into an article-only weekly LaTeX tree.

This stage is intentionally pre-frontmatter. It requires an APPROVED Architecture,
all ARTICLE_DRAFTING packages to have validated render manifests, and exact SHA
matches for Draft Package / TeX / Bib artifacts. It copies derived artifacts into
a hermetic assembly tree, merges generated bibliography entries with collision
detection, and writes main.tex in Architecture drafting order.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from scripts import merge_generated_bibliography as bibmerge
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


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def resolve_manifest_file(manifest_path: Path, raw_path: str) -> Path:
    path = Path(raw_path)
    if path.is_absolute():
        return path
    candidates = [manifest_path.parent / path, Path.cwd() / path]
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    return candidates[0].resolve()


def verify_file_record(manifest_path: Path, record: Any, label: str) -> tuple[Path | None, list[str]]:
    errors: list[str] = []
    if not isinstance(record, dict):
        return None, [f"{label} record must be an object"]
    raw_path = record.get("path")
    expected_sha = record.get("sha256")
    expected_bytes = record.get("bytes")
    if not isinstance(raw_path, str) or not raw_path:
        return None, [f"{label}.path must be non-empty"]
    path = resolve_manifest_file(manifest_path, raw_path)
    if not path.is_file():
        return path, [f"{label} file does not exist: {path}"]
    actual_sha = sha256_file(path)
    actual_bytes = path.stat().st_size
    if expected_sha != actual_sha:
        errors.append(f"{label} SHA mismatch: expected={expected_sha} actual={actual_sha}")
    if expected_bytes != actual_bytes:
        errors.append(f"{label} byte-size mismatch: expected={expected_bytes} actual={actual_bytes}")
    return path, errors


def draft_package_map(manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    values = manifest.get("package_files")
    if not isinstance(values, list):
        raise ValueError("draft package manifest package_files must be an array")
    result: dict[str, dict[str, Any]] = {}
    for entry in values:
        if not isinstance(entry, dict) or not isinstance(entry.get("package_id"), str):
            raise ValueError("invalid draft package manifest entry")
        package_id = entry["package_id"]
        if package_id in result:
            raise ValueError(f"duplicate package_id in draft package manifest: {package_id}")
        result[package_id] = entry
    return result


def render_manifest_path(render_dir: Path, package_id: str) -> Path:
    direct = render_dir / f"{package_id}.render.json"
    nested = render_dir / package_id / "render-manifest.json"
    matches = [path for path in (direct, nested) if path.is_file()]
    if len(matches) > 1:
        raise ValueError(f"multiple render manifests found for {package_id}: {matches}")
    return matches[0] if matches else direct


def build_main(template_path: Path, issue_id: str, inputs: list[str]) -> str:
    template = template_path.read_text(encoding="utf-8")
    if "@@ISSUE_ID@@" not in template or "@@SECTION_INPUTS@@" not in template:
        raise ValueError("article smoke template is missing required placeholders")
    section_inputs = "\n".join(f"\\input{{{path}}}" for path in inputs)
    return template.replace("@@ISSUE_ID@@", issue_id).replace("@@SECTION_INPUTS@@", section_inputs)


def assemble(
    architecture_input_path: Path,
    architecture_plan_path: Path,
    draft_package_manifest_path: Path,
    render_dir: Path,
    template_path: Path,
    output_dir: Path,
) -> tuple[dict[str, Any], bool]:
    architecture_report, architecture_ok = architecture_validator.validate(
        architecture_input_path, architecture_plan_path, require_approved=True
    )
    if not architecture_ok:
        raise ValueError(f"Architecture is not assembly-ready: {architecture_report['errors']}")

    architecture_plan = load_json(architecture_plan_path)
    draft_manifest = load_json(draft_package_manifest_path)
    package_map = draft_package_map(draft_manifest)
    issue_id = architecture_plan["issue_id"]
    errors: list[str] = []

    expected_articles = [
        package for package in architecture_plan["packages"]
        if package["package_type"] in ARTICLE_TYPES
    ]
    expected_articles.sort(key=lambda package: package["drafting_order"])

    if draft_manifest.get("issue_id") != issue_id:
        errors.append("draft package manifest issue_id does not match Architecture Plan")
    if draft_manifest.get("basis", {}).get("architecture_plan_sha256") != sha256_file(architecture_plan_path):
        errors.append("draft package manifest architecture_plan_sha256 mismatch")
    if draft_manifest.get("basis", {}).get("architecture_input_sha256") != sha256_file(architecture_input_path):
        errors.append("draft package manifest architecture_input_sha256 mismatch")

    output_dir.mkdir(parents=True, exist_ok=True)
    generated_sections = output_dir / "sections" / "generated"
    generated_sections.mkdir(parents=True, exist_ok=True)
    generated_bib_dir = output_dir / "generated" / "bibliography"
    generated_bib_dir.mkdir(parents=True, exist_ok=True)

    assembled: list[dict[str, Any]] = []
    bib_inputs: list[Path] = []
    section_inputs: list[str] = []

    for sequence, package in enumerate(expected_articles, start=1):
        package_id = package["package_id"]
        draft_entry = package_map.get(package_id)
        if draft_entry is None:
            errors.append(f"missing Draft Package manifest entry for article package: {package_id}")
            continue
        if draft_entry.get("execution_stage") != "ARTICLE_DRAFTING":
            errors.append(f"{package_id}: Draft Package execution_stage is not ARTICLE_DRAFTING")
        manifest_path = render_manifest_path(render_dir, package_id)
        if not manifest_path.is_file():
            errors.append(f"missing render manifest for article package: {package_id}")
            continue
        render_manifest = load_json(manifest_path)
        if render_manifest.get("passed") is not True:
            errors.append(f"{package_id}: render manifest is not passed=true")
        if render_manifest.get("issue_id") != issue_id or render_manifest.get("package_id") != package_id:
            errors.append(f"{package_id}: render manifest identity mismatch")
        if render_manifest.get("basis", {}).get("draft_package_sha256") != draft_entry.get("sha256"):
            errors.append(f"{package_id}: rendered draft_package_sha256 does not match generated Draft Package")

        tex_path, tex_errors = verify_file_record(manifest_path, render_manifest.get("tex"), f"{package_id}.tex")
        bib_path, bib_errors = verify_file_record(manifest_path, render_manifest.get("bib"), f"{package_id}.bib")
        errors.extend(tex_errors)
        errors.extend(bib_errors)
        if tex_errors or bib_errors or tex_path is None or bib_path is None:
            continue

        section_name = f"{sequence:02d}-{package_id}.tex"
        section_dest = generated_sections / section_name
        shutil.copyfile(tex_path, section_dest)
        bib_name = f"{sequence:02d}-{package_id}.bib"
        bib_dest = generated_bib_dir / bib_name
        shutil.copyfile(bib_path, bib_dest)
        bib_inputs.append(bib_dest)
        relative_input = (Path("sections") / "generated" / section_name).as_posix()
        section_inputs.append(relative_input)
        assembled.append(
            {
                "package_id": package_id,
                "drafting_order": package["drafting_order"],
                "section": {
                    "path": relative_input,
                    "sha256": sha256_file(section_dest),
                    "bytes": section_dest.stat().st_size,
                },
                "bibliography_source": {
                    "path": (Path("generated") / "bibliography" / bib_name).as_posix(),
                    "sha256": sha256_file(bib_dest),
                    "bytes": bib_dest.stat().st_size,
                },
                "render_manifest_sha256": sha256_file(manifest_path),
            }
        )

    expected_ids = [package["package_id"] for package in expected_articles]
    assembled_ids = [entry["package_id"] for entry in assembled]
    missing_articles = [package_id for package_id in expected_ids if package_id not in assembled_ids]
    if missing_articles:
        errors.append(f"article packages not assembled: {missing_articles}")

    references = output_dir / "references.bib"
    bib_manifest_path = output_dir / "generated" / "bibliography-merge.json"
    bib_manifest: dict[str, Any] | None = None
    if not errors and bib_inputs:
        bib_manifest, bib_ok = bibmerge.merge(bib_inputs, references, bib_manifest_path)
        if not bib_ok:
            errors.append(f"generated bibliography merge failed: {bib_manifest['conflicts']}")
    elif not bib_inputs:
        errors.append("no article bibliography inputs were produced")

    main_path = output_dir / "main.tex"
    if not errors:
        main_path.write_text(build_main(template_path, issue_id, section_inputs), encoding="utf-8")
    elif main_path.exists():
        main_path.unlink()

    passed = not errors
    manifest = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "ARTICLE_ONLY_ASSEMBLED" if passed else "ASSEMBLY_FAILED",
        "passed": passed,
        "basis": {
            "architecture_input_sha256": sha256_file(architecture_input_path),
            "architecture_plan_sha256": sha256_file(architecture_plan_path),
            "draft_package_manifest_sha256": sha256_file(draft_package_manifest_path),
            "template_sha256": sha256_file(template_path),
        },
        "expected_article_package_count": len(expected_articles),
        "assembled_article_package_count": len(assembled),
        "article_packages": assembled,
        "section_inputs": section_inputs,
        "bibliography": bib_manifest,
        "main": (
            {"path": "main.tex", "sha256": sha256_file(main_path), "bytes": main_path.stat().st_size}
            if passed else None
        ),
        "frontmatter_deferred": True,
        "cover_headline_deferred": True,
        "this_week_summary_deferred": True,
        "errors": errors,
        "note": "This is an article-only smoke assembly. It is not the final issue until the post-draft frontmatter/cover stage is completed and the issue-level build/visual gates pass.",
    }
    write_json(output_dir / "assembly-manifest.json", manifest)
    return manifest, passed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--architecture-input", required=True)
    parser.add_argument("--architecture-plan", required=True)
    parser.add_argument("--draft-package-manifest", required=True)
    parser.add_argument("--render-dir", required=True)
    parser.add_argument("--template", default="templates/survey/weekly-article-smoke-main.tex.in")
    parser.add_argument("--output-dir", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest, passed = assemble(
        Path(args.architecture_input),
        Path(args.architecture_plan),
        Path(args.draft_package_manifest),
        Path(args.render_dir),
        Path(args.template),
        Path(args.output_dir),
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
