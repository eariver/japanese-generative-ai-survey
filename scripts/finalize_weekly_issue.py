#!/usr/bin/env python3
"""Finalize a weekly LaTeX source tree from article-only assembly + synthesis.

This is a source-assembly stage, not a Freeze operation. It re-verifies every
assembled article section and merged bibliography, inserts package labels for
dynamic page references, renders validated post-draft frontmatter, and writes a
final main.tex. PDF build/log/visual gates remain downstream requirements.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any

from scripts import render_issue_frontmatter as frontmatter_renderer

BS = chr(92)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_file(path: Path, expected_sha: Any, expected_bytes: Any, label: str) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return [f"{label} does not exist: {path}"]
    actual_sha = sha256_file(path)
    actual_bytes = path.stat().st_size
    if expected_sha != actual_sha:
        errors.append(f"{label} SHA mismatch: expected={expected_sha} actual={actual_sha}")
    if expected_bytes != actual_bytes:
        errors.append(f"{label} byte-size mismatch: expected={expected_bytes} actual={actual_bytes}")
    return errors


def inject_package_label(source: str, package_id: str) -> str:
    label = f"{BS}label{{pkg:{package_id}}}"
    if label in source:
        raise ValueError(f"package label already exists: {package_id}")
    lines = source.splitlines()
    section_indexes = [index for index, line in enumerate(lines) if line.lstrip().startswith(f"{BS}section{{")]
    if len(section_indexes) != 1:
        raise ValueError(f"expected exactly one top-level section in rendered package {package_id}; found {len(section_indexes)}")
    index = section_indexes[0]
    lines.insert(index + 1, label)
    return "\n".join(lines) + "\n"


def build_main(template_path: Path, section_inputs: list[str]) -> str:
    template = template_path.read_text(encoding="utf-8")
    if "@@SECTION_INPUTS@@" not in template:
        raise ValueError("final weekly template is missing @@SECTION_INPUTS@@")
    inputs = "\n".join(f"{BS}input{{{path}}}" for path in section_inputs)
    return template.replace("@@SECTION_INPUTS@@", inputs)


def finalize(
    article_assembly_dir: Path,
    synthesis_input_path: Path,
    synthesis_result_path: Path,
    synthesis_prompt_path: Path,
    template_path: Path,
    output_dir: Path,
) -> tuple[dict[str, Any], bool]:
    assembly_manifest_path = article_assembly_dir / "assembly-manifest.json"
    assembly = load_json(assembly_manifest_path)
    errors: list[str] = []
    if assembly.get("passed") is not True or assembly.get("status") != "ARTICLE_ONLY_ASSEMBLED":
        errors.append("article assembly is not ARTICLE_ONLY_ASSEMBLED/passed")
    if assembly.get("frontmatter_deferred") is not True or assembly.get("cover_headline_deferred") is not True:
        errors.append("article assembly did not preserve post-draft frontmatter/cover deferral")

    output_dir.mkdir(parents=True, exist_ok=True)
    sections_dir = output_dir / "sections" / "generated"
    sections_dir.mkdir(parents=True, exist_ok=True)
    section_inputs: list[str] = []
    final_sections: list[dict[str, Any]] = []
    package_ids: set[str] = set()

    for index, item in enumerate(assembly.get("article_packages") or []):
        if not isinstance(item, dict):
            errors.append(f"article_packages[{index}] is invalid")
            continue
        package_id = item.get("package_id")
        section = item.get("section")
        if not isinstance(package_id, str) or not package_id:
            errors.append(f"article_packages[{index}].package_id is invalid")
            continue
        if package_id in package_ids:
            errors.append(f"duplicate article package_id in assembly: {package_id}")
            continue
        package_ids.add(package_id)
        if not isinstance(section, dict) or not isinstance(section.get("path"), str):
            errors.append(f"{package_id}: section record is invalid")
            continue
        source_path = article_assembly_dir / section["path"]
        file_errors = verify_file(source_path, section.get("sha256"), section.get("bytes"), f"{package_id} assembled section")
        errors.extend(file_errors)
        if file_errors:
            continue
        try:
            labeled = inject_package_label(source_path.read_text(encoding="utf-8"), package_id)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        dest_name = Path(section["path"]).name
        dest = sections_dir / dest_name
        dest.write_text(labeled, encoding="utf-8")
        relative = (Path("sections") / "generated" / dest_name).as_posix()
        section_inputs.append(relative)
        final_sections.append({
            "package_id": package_id,
            "path": relative,
            "sha256": sha256_file(dest),
            "bytes": dest.stat().st_size,
            "label": f"pkg:{package_id}",
        })

    expected_count = assembly.get("expected_article_package_count")
    if expected_count != len(final_sections):
        errors.append(f"final labeled section count {len(final_sections)} does not match expected article count {expected_count}")

    source_bib = article_assembly_dir / "references.bib"
    bib_manifest = assembly.get("bibliography")
    if not isinstance(bib_manifest, dict) or not isinstance(bib_manifest.get("output"), dict):
        errors.append("article assembly bibliography manifest is missing")
    else:
        output_record = bib_manifest["output"]
        errors.extend(verify_file(source_bib, output_record.get("sha256"), output_record.get("bytes"), "assembled references.bib"))
    if not errors and source_bib.is_file():
        shutil.copyfile(source_bib, output_dir / "references.bib")

    frontmatter_path = output_dir / "sections" / "00-frontmatter.tex"
    frontmatter_manifest_path = output_dir / "generated" / "frontmatter-render.json"
    frontmatter_manifest: dict[str, Any] | None = None
    if not errors:
        try:
            frontmatter_manifest, _ = frontmatter_renderer.render(
                synthesis_input_path,
                synthesis_result_path,
                synthesis_prompt_path,
                frontmatter_path,
                frontmatter_manifest_path,
            )
        except ValueError as exc:
            errors.append(str(exc))

    main_path = output_dir / "main.tex"
    if not errors:
        main_path.write_text(build_main(template_path, section_inputs), encoding="utf-8")
    elif main_path.exists():
        main_path.unlink()

    passed = not errors
    manifest = {
        "schema_version": "1.0",
        "issue_id": assembly.get("issue_id"),
        "status": "FINAL_SOURCE_ASSEMBLED" if passed else "FINALIZATION_FAILED",
        "passed": passed,
        "basis": {
            "article_assembly_manifest_sha256": sha256_file(assembly_manifest_path),
            "synthesis_input_sha256": sha256_file(synthesis_input_path),
            "synthesis_result_sha256": sha256_file(synthesis_result_path),
            "synthesis_prompt_sha256": sha256_file(synthesis_prompt_path),
            "template_sha256": sha256_file(template_path),
        },
        "article_section_count": len(final_sections),
        "article_sections": final_sections,
        "frontmatter": frontmatter_manifest,
        "references": (
            {"path": "references.bib", "sha256": sha256_file(output_dir / "references.bib"), "bytes": (output_dir / "references.bib").stat().st_size}
            if passed else None
        ),
        "main": (
            {"path": "main.tex", "sha256": sha256_file(main_path), "bytes": main_path.stat().st_size}
            if passed else None
        ),
        "ready_for_pdf_build": passed,
        "freeze_allowed": False,
        "remaining_gates": ["LuaLaTeX/Biber build", "final TeX log validation", "citation/claim preflight", "visual review", "Freeze decision"],
        "errors": errors,
    }
    manifest_path = output_dir / "final-source-manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifest, passed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--article-assembly-dir", required=True)
    parser.add_argument("--synthesis-input", required=True)
    parser.add_argument("--synthesis-result", required=True)
    parser.add_argument("--synthesis-prompt", default="config/prompts/editorial/issue-synthesis-v0.1.md")
    parser.add_argument("--template", default="templates/survey/weekly-final-main.tex.in")
    parser.add_argument("--output-dir", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manifest, passed = finalize(
        Path(args.article_assembly_dir), Path(args.synthesis_input),
        Path(args.synthesis_result), Path(args.synthesis_prompt),
        Path(args.template), Path(args.output_dir),
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
