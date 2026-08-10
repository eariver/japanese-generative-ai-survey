#!/usr/bin/env python3
"""Run deterministic source-level preflight on a finalized weekly survey tree.

This stage validates concerns visible in final source material: manifest/file
integrity, section ordering, dynamic package labels/page refs, literal page-number
regressions, exact TeX/Bib citation-key consistency, and reader-facing prose
separation from internal editorial workflow metadata. Semantic Evidence checks
remain upstream in the structured drafting validators.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from scripts.editorial_prose_guard import PROSE_LINT_EXEMPT_MARKER, reader_facing_prose_errors
from scripts.merge_generated_bibliography import parse_generated_bib

PACKAGE_LABEL_RE = re.compile(r"\\label\{pkg:([^}]+)\}")
PACKAGE_PAGEREF_RE = re.compile(r"\\pageref\{pkg:([^}]+)\}")
CITE_RE = re.compile(r"\\(?:auto|text|paren)cite(?:\[[^\]]*\]){0,2}\{([^}]+)\}")
INPUT_RE = re.compile(r"\\input\{([^}]+)\}")
LITERAL_INTERNAL_PAGE_RE = re.compile(r"(?:今号|本号)\s*[pP]\.?(?:~|\s)*\d+")
LEGACY_READER_PROSE_EXEMPT_ISSUES = {"2026-W32"}


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_record(root: Path, record: Any, label: str) -> tuple[Path | None, list[str]]:
    if not isinstance(record, dict):
        return None, [f"{label} record must be an object"]
    raw_path = record.get("path")
    if not isinstance(raw_path, str) or not raw_path:
        return None, [f"{label}.path must be non-empty"]
    path = root / raw_path
    if not path.is_file():
        return path, [f"{label} missing: {raw_path}"]
    errors: list[str] = []
    actual_sha = sha256_file(path)
    actual_bytes = path.stat().st_size
    if record.get("sha256") != actual_sha:
        errors.append(f"{label} SHA mismatch: expected={record.get('sha256')} actual={actual_sha}")
    if record.get("bytes") != actual_bytes:
        errors.append(f"{label} byte-size mismatch: expected={record.get('bytes')} actual={actual_bytes}")
    return path, errors


def cite_keys(text: str) -> set[str]:
    result: set[str] = set()
    for match in CITE_RE.finditer(text):
        for key in match.group(1).split(","):
            value = key.strip()
            if value:
                result.add(value)
    return result


def normalize_input_path(value: str) -> str:
    path = Path(value)
    if path.suffix == ".tex":
        path = path.with_suffix("")
    return path.as_posix()


def preflight(issue_dir: Path, manifest_path: Path | None = None) -> tuple[dict[str, Any], bool]:
    if manifest_path is None:
        manifest_path = issue_dir / "final-source-manifest.json"
    manifest = load_json(manifest_path)
    errors: list[str] = []

    if manifest.get("schema_version") != "1.0":
        errors.append("final source manifest schema_version must be 1.0")
    if manifest.get("passed") is not True or manifest.get("status") != "FINAL_SOURCE_ASSEMBLED":
        errors.append("final source manifest must be FINAL_SOURCE_ASSEMBLED/passed")
    if manifest.get("ready_for_pdf_build") is not True:
        errors.append("final source manifest is not ready_for_pdf_build=true")
    if manifest.get("freeze_allowed") is not False:
        errors.append("source preflight expects freeze_allowed=false before downstream PDF/visual gates")

    main_path, main_errors = verify_record(issue_dir, manifest.get("main"), "main")
    frontmatter_record = manifest.get("frontmatter")
    if not isinstance(frontmatter_record, dict) or not isinstance(frontmatter_record.get("output"), dict):
        frontmatter_path = None
        errors.append("frontmatter output record missing")
    else:
        frontmatter_output = frontmatter_record["output"]
        raw_frontmatter_path = frontmatter_output.get("path")
        if isinstance(raw_frontmatter_path, str):
            candidate = Path(raw_frontmatter_path)
            if candidate.is_absolute():
                try:
                    relative = candidate.relative_to(issue_dir)
                    frontmatter_output = dict(frontmatter_output)
                    frontmatter_output["path"] = relative.as_posix()
                except ValueError:
                    pass
        frontmatter_path, frontmatter_errors = verify_record(issue_dir, frontmatter_output, "frontmatter")
        errors.extend(frontmatter_errors)
    references_path, references_errors = verify_record(issue_dir, manifest.get("references"), "references")
    errors.extend(main_errors)
    errors.extend(references_errors)

    sections = manifest.get("article_sections")
    if not isinstance(sections, list):
        errors.append("article_sections must be an array")
        sections = []
    expected_section_count = manifest.get("article_section_count")
    if expected_section_count != len(sections):
        errors.append(
            f"article_section_count {expected_section_count} does not match article_sections length {len(sections)}"
        )

    section_paths: list[Path] = []
    package_ids: list[str] = []
    for index, section in enumerate(sections):
        if not isinstance(section, dict):
            errors.append(f"article_sections[{index}] must be an object")
            continue
        package_id = section.get("package_id")
        if not isinstance(package_id, str) or not package_id:
            errors.append(f"article_sections[{index}].package_id invalid")
            continue
        package_ids.append(package_id)
        path, section_errors = verify_record(issue_dir, section, f"section[{package_id}]")
        errors.extend(section_errors)
        if path is not None and path.is_file():
            section_paths.append(path)
            expected_label = f"pkg:{package_id}"
            if section.get("label") != expected_label:
                errors.append(f"{package_id}: manifest label must be {expected_label}")
            labels = PACKAGE_LABEL_RE.findall(path.read_text(encoding="utf-8"))
            if labels != [package_id]:
                errors.append(f"{package_id}: section must contain exactly one matching package label; found={labels}")

    if len(package_ids) != len(set(package_ids)):
        errors.append("article_sections contains duplicate package_id values")

    main_text = main_path.read_text(encoding="utf-8") if main_path and main_path.is_file() else ""
    inputs = [normalize_input_path(value) for value in INPUT_RE.findall(main_text)]
    expected_inputs = ["sections/00-frontmatter"] + [
        normalize_input_path(section.get("path", ""))
        for section in sections
        if isinstance(section, dict)
    ]
    if inputs != expected_inputs:
        errors.append(f"main.tex input order/content mismatch: expected={expected_inputs} actual={inputs}")
    if main_text.count("\\printbibliography") != 1:
        errors.append("main.tex must contain exactly one \\printbibliography")
    if main_text.count("\\addbibresource{references.bib}") != 1:
        errors.append("main.tex must contain exactly one \\addbibresource{references.bib}")

    all_tex_paths = [path for path in [frontmatter_path, *section_paths] if path is not None and path.is_file()]
    all_tex_text = "\n".join(path.read_text(encoding="utf-8") for path in all_tex_paths)
    labels = PACKAGE_LABEL_RE.findall(all_tex_text)
    label_counts = {label: labels.count(label) for label in set(labels)}
    duplicate_labels = sorted(label for label, count in label_counts.items() if count != 1)
    if duplicate_labels:
        errors.append(f"package labels must be globally unique: {duplicate_labels}")
    expected_label_set = set(package_ids)
    actual_label_set = set(labels)
    if actual_label_set != expected_label_set:
        errors.append(
            f"package label set mismatch: missing={sorted(expected_label_set - actual_label_set)} extra={sorted(actual_label_set - expected_label_set)}"
        )

    page_refs = sorted(set(PACKAGE_PAGEREF_RE.findall(all_tex_text)))
    unresolved_page_refs = sorted(set(page_refs) - expected_label_set)
    if unresolved_page_refs:
        errors.append(f"frontmatter/source uses unknown package page refs: {unresolved_page_refs}")

    literal_refs: list[str] = []
    for path in all_tex_paths:
        for match in LITERAL_INTERNAL_PAGE_RE.finditer(path.read_text(encoding="utf-8")):
            literal_refs.append(f"{path.relative_to(issue_dir).as_posix()}:{match.group(0)}")
    if literal_refs:
        errors.append(f"literal internal page references are forbidden: {literal_refs}")

    issue_id = manifest.get("issue_id")
    if issue_id not in LEGACY_READER_PROSE_EXEMPT_ISSUES:
        for path in all_tex_paths:
            errors.extend(reader_facing_prose_errors(path, issue_dir))

    citations = sorted(cite_keys(all_tex_text))
    bibliography_keys: list[str] = []
    if references_path is not None and references_path.is_file():
        try:
            bibliography_keys = sorted(parse_generated_bib(references_path))
        except ValueError as exc:
            errors.append(f"references.bib is not valid generated bibliography: {exc}")
    missing_bib = sorted(set(citations) - set(bibliography_keys))
    unused_bib = sorted(set(bibliography_keys) - set(citations))
    if missing_bib:
        errors.append(f"TeX cites keys absent from references.bib: {missing_bib}")
    if unused_bib:
        errors.append(f"references.bib contains unused generated keys: {unused_bib}")

    report = {
        "schema_version": "1.0",
        "issue_id": manifest.get("issue_id"),
        "passed": not errors,
        "final_source_manifest_sha256": sha256_file(manifest_path),
        "article_section_count": len(sections),
        "package_labels": sorted(actual_label_set),
        "page_reference_labels": page_refs,
        "citation_keys": citations,
        "bibliography_keys": bibliography_keys,
        "missing_bibliography_keys": missing_bib,
        "unused_bibliography_keys": unused_bib,
        "errors": errors,
    }
    return report, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--issue-dir", required=True)
    parser.add_argument("--manifest")
    parser.add_argument("--report")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    issue_dir = Path(args.issue_dir)
    manifest = Path(args.manifest) if args.manifest else None
    report, passed = preflight(issue_dir, manifest)
    if args.report:
        path = Path(args.report)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
