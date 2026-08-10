#!/usr/bin/env python3
"""Assemble validated ARTICLE_DRAFTING render outputs into an ordered issue staging tree.

Frontmatter and References packages are intentionally deferred. This stage copies
rendered section TeX in approved drafting order, verifies all recorded hashes, and
merges renderer-generated BibLaTeX without silently resolving metadata conflicts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any

from scripts import merge_generated_bibliography as bibmerge


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def slug(value: str) -> str:
    result = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return result[:48].rstrip("-") or "package"


def resolve_recorded_path(manifest_path: Path, recorded: str) -> Path:
    raw = Path(recorded)
    if raw.is_absolute():
        if not raw.is_file():
            raise ValueError(f"rendered artifact does not exist: {raw}")
        return raw

    local = manifest_path.parent / raw
    cwd = raw
    candidates = [path for path in (local, cwd) if path.is_file()]
    unique = []
    seen: set[Path] = set()
    for candidate in candidates:
        resolved = candidate.resolve()
        if resolved not in seen:
            seen.add(resolved)
            unique.append(candidate)
    if not unique:
        raise ValueError(f"cannot resolve rendered artifact {recorded!r} from {manifest_path}")
    if len(unique) > 1:
        first_hash = sha256_file(unique[0])
        if any(sha256_file(path) != first_hash for path in unique[1:]):
            raise ValueError(f"ambiguous rendered artifact path resolves to different bytes: {recorded!r}")
    return unique[0]


def render_manifest_index(paths: list[Path]) -> tuple[dict[str, tuple[Path, dict[str, Any]]], list[str]]:
    index: dict[str, tuple[Path, dict[str, Any]]] = {}
    errors: list[str] = []
    for path in paths:
        try:
            value = load_json(path)
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            errors.append(f"{path}: invalid render manifest: {exc}")
            continue
        package_id = value.get("package_id")
        if not isinstance(package_id, str) or not package_id:
            errors.append(f"{path}: package_id missing")
            continue
        if package_id in index:
            errors.append(f"duplicate render manifest for package_id {package_id}: {index[package_id][0]} and {path}")
            continue
        index[package_id] = (path, value)
    return index, errors


def assemble(
    draft_package_manifest_path: Path,
    render_manifest_paths: list[Path],
    output_dir: Path,
) -> tuple[dict[str, Any], bool]:
    package_manifest = load_json(draft_package_manifest_path)
    errors: list[str] = []
    if package_manifest.get("schema_version") != "1.0":
        errors.append("draft package manifest schema_version must be 1.0")
    if package_manifest.get("passed") is not True:
        errors.append("draft package manifest is not passed=true")

    issue_id = package_manifest.get("issue_id")
    package_files = package_manifest.get("package_files")
    if not isinstance(package_files, list):
        raise ValueError("draft package manifest package_files must be an array")

    article_packages = sorted(
        [item for item in package_files if item.get("execution_stage") == "ARTICLE_DRAFTING"],
        key=lambda item: item["drafting_order"],
    )
    deferred = [
        {
            "package_id": item["package_id"],
            "package_type": item["package_type"],
            "execution_stage": item["execution_stage"],
            "drafting_order": item["drafting_order"],
        }
        for item in sorted(package_files, key=lambda item: item["drafting_order"])
        if item.get("execution_stage") in {"POST_DRAFT_SUMMARY", "REFERENCE_GENERATION"}
    ]

    render_index, render_errors = render_manifest_index(render_manifest_paths)
    errors.extend(render_errors)
    expected_ids = {item["package_id"] for item in article_packages}
    actual_ids = set(render_index)
    missing = sorted(expected_ids - actual_ids)
    unexpected = sorted(actual_ids - expected_ids)
    if missing:
        errors.append(f"missing render manifests for ARTICLE_DRAFTING packages: {missing}")
    if unexpected:
        errors.append(f"render manifests supplied for non-ARTICLE_DRAFTING/unknown packages: {unexpected}")

    stage_dir = output_dir
    sections_dir = stage_dir / "sections"
    sections_dir.mkdir(parents=True, exist_ok=True)
    section_records: list[dict[str, Any]] = []
    bib_inputs: list[Path] = []

    if not errors:
        for index, package_record in enumerate(article_packages, start=1):
            package_id = package_record["package_id"]
            manifest_path, render_manifest = render_index[package_id]
            if render_manifest.get("passed") is not True:
                errors.append(f"{package_id}: render manifest is not passed=true")
                continue
            if render_manifest.get("issue_id") != issue_id:
                errors.append(f"{package_id}: render manifest issue_id mismatch")
            if render_manifest.get("basis", {}).get("draft_package_sha256") != package_record.get("sha256"):
                errors.append(f"{package_id}: rendered Draft Package SHA does not match draft package manifest")

            tex_info = render_manifest.get("tex") or {}
            bib_info = render_manifest.get("bib") or {}
            try:
                tex_source = resolve_recorded_path(manifest_path, tex_info.get("path", ""))
                bib_source = resolve_recorded_path(manifest_path, bib_info.get("path", ""))
            except ValueError as exc:
                errors.append(f"{package_id}: {exc}")
                continue
            actual_tex_sha = sha256_file(tex_source)
            actual_bib_sha = sha256_file(bib_source)
            if actual_tex_sha != tex_info.get("sha256"):
                errors.append(f"{package_id}: TeX SHA does not match render manifest")
            if actual_bib_sha != bib_info.get("sha256"):
                errors.append(f"{package_id}: Bib SHA does not match render manifest")
            if errors:
                continue

            filename = f"{index * 10:02d}-{slug(package_id)}.tex"
            destination = sections_dir / filename
            shutil.copyfile(tex_source, destination)
            if sha256_file(destination) != actual_tex_sha:
                raise RuntimeError(f"copied TeX bytes changed unexpectedly for {package_id}")
            bib_inputs.append(bib_source)
            section_records.append(
                {
                    "package_id": package_id,
                    "package_type": package_record["package_type"],
                    "drafting_order": package_record["drafting_order"],
                    "source_render_manifest": manifest_path.as_posix(),
                    "section_path": destination.relative_to(stage_dir).as_posix(),
                    "section_sha256": actual_tex_sha,
                    "bib_source_sha256": actual_bib_sha,
                }
            )

    substantive_inputs: dict[str, Any] | None = None
    merged_bibliography: dict[str, Any] | None = None
    if not errors:
        inputs_path = stage_dir / "substantive-inputs.tex"
        inputs_text = "\n".join(
            rf"\input{{{Path(record['section_path']).with_suffix('').as_posix()}}}"
            for record in section_records
        ) + ("\n" if section_records else "")
        inputs_path.write_text(inputs_text, encoding="utf-8")
        substantive_inputs = {
            "path": inputs_path.relative_to(stage_dir).as_posix(),
            "sha256": sha256_file(inputs_path),
        }

        bib_output = stage_dir / "references.generated.bib"
        bib_manifest_output = stage_dir / "bibliography-merge.json"
        if bib_inputs:
            bib_manifest, bib_passed = bibmerge.merge(bib_inputs, bib_output, bib_manifest_output)
            if not bib_passed:
                errors.extend(
                    f"generated bibliography conflict: {conflict['key']}"
                    for conflict in bib_manifest.get("conflicts") or []
                )
            else:
                merged_bibliography = {
                    "path": bib_output.relative_to(stage_dir).as_posix(),
                    "sha256": bib_manifest["output"]["sha256"],
                    "entry_count": bib_manifest["entry_count"],
                    "deduplicated_keys": bib_manifest["deduplicated_keys"],
                }
        else:
            bib_output.write_text("", encoding="utf-8")
            merged_bibliography = {
                "path": bib_output.relative_to(stage_dir).as_posix(),
                "sha256": sha256_file(bib_output),
                "entry_count": 0,
                "deduplicated_keys": [],
            }

    manifest = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "substantive-assembly-ready" if not errors else "substantive-assembly-invalid",
        "passed": not errors,
        "draft_package_manifest_sha256": sha256_file(draft_package_manifest_path),
        "section_count": len(section_records),
        "sections": section_records,
        "merged_bibliography": merged_bibliography if not errors else None,
        "substantive_inputs": substantive_inputs if not errors else None,
        "deferred_packages": deferred,
        "errors": errors,
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "substantive-assembly.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return manifest, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--draft-package-manifest", required=True)
    parser.add_argument("--render-manifest", action="append", required=True, dest="render_manifests")
    parser.add_argument("--output-dir", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest, passed = assemble(
        Path(args.draft_package_manifest),
        [Path(value) for value in args.render_manifests],
        Path(args.output_dir),
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
