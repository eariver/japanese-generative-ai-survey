#!/usr/bin/env python3
"""Derive the normal reader-facing balanced layout before a Special's first PDF build.

Accepted Article Draft sections and Technical Notes remain unchanged. This pass creates
layout-only standfirst/body derivatives, renders chapter headings and standfirsts full-width,
and wraps only narrative bodies in local ``multicols`` environments so publication layout
validation can run before the first PDF build.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def input_path(path: str) -> str:
    return Path(path).with_suffix("").as_posix()


def split_article_layout(source: Path, standfirst_target: Path, body_target: Path) -> dict[str, str]:
    """Create layout-only derivatives without mutating the accepted article section."""
    lines = source.read_text(encoding="utf-8").splitlines(keepends=True)
    section_index = next((i for i, line in enumerate(lines) if line.lstrip().startswith(r"\section{")), None)
    if section_index is None:
        raise ValueError(f"{source}: top-level section heading not found")

    section_line = lines[section_index].strip()
    label_line = ""
    remove = {section_index}
    cursor = section_index + 1
    while cursor < len(lines):
        stripped = lines[cursor].strip()
        if not stripped:
            cursor += 1
            continue
        if stripped.startswith(r"\label{"):
            label_line = stripped
            remove.add(cursor)
            cursor += 1
        break

    standfirst_index: int | None = None
    while cursor < len(lines):
        stripped = lines[cursor].strip()
        if not stripped or stripped.startswith("%"):
            cursor += 1
            continue
        if not stripped.startswith(r"\noindent\textbf{"):
            raise ValueError(f"{source}: expected generated bold standfirst after section heading")
        standfirst_index = cursor
        break
    if standfirst_index is None:
        raise ValueError(f"{source}: standfirst not found")

    remove.add(standfirst_index)
    standfirst_target.parent.mkdir(parents=True, exist_ok=True)
    body_target.parent.mkdir(parents=True, exist_ok=True)
    standfirst_target.write_text(lines[standfirst_index], encoding="utf-8")
    body_target.write_text("".join(line for i, line in enumerate(lines) if i not in remove), encoding="utf-8")

    return {
        "section_line": section_line,
        "label_line": label_line,
        "standfirst_sha256": sha256_file(standfirst_target),
        "body_sha256": sha256_file(body_target),
    }


def build_main_tex(current_main: Path, manifest: dict[str, Any]) -> tuple[str, dict[str, dict[str, str]]]:
    text = current_main.read_text(encoding="utf-8")
    if r"\begin{document}" not in text:
        raise ValueError("generated main.tex lacks document body")
    preamble = text.split(r"\begin{document}", 1)[0]
    if r"\usepackage{multicol}" not in preamble:
        preamble = preamble.replace(r"\usepackage{jgaisurvey}", r"\usepackage{jgaisurvey}" + "\n" + r"\usepackage{multicol}")
    if r"\setlength{\columnsep}" not in preamble:
        preamble += "\\setlength{\\columnsep}{6mm}\n"
    if r"\setlength{\multicolsep}" not in preamble:
        preamble += "\\setlength{\\multicolsep}{0.8em plus 0.2em minus 0.1em}\n"

    source_dir = current_main.parent
    standfirst_dir = source_dir / "layout-standfirsts"
    body_dir = source_dir / "layout-bodies"
    records: dict[str, dict[str, str]] = {}

    lines = [
        preamble.rstrip(),
        "",
        r"\begin{document}",
        r"\surveycover",
        r"\clearpage",
        r"\input{sections/00-frontmatter}",
        "",
    ]
    for article in manifest.get("articles") or []:
        if not isinstance(article, dict):
            raise ValueError("source manifest contains non-object article")
        package_id = str(article.get("package_id") or "")
        article_rel = str(article.get("article_section_path") or "")
        notes_rel = str(article.get("technical_notes_path") or "")
        if not package_id or not article_rel or not notes_rel:
            raise ValueError("article requires package_id, article_section_path, and technical_notes_path")
        article_path = source_dir / article_rel
        if sha256_file(article_path) != article.get("article_section_sha256"):
            raise ValueError(f"accepted expanded article changed before layout derivation: {package_id}")
        notes_path = source_dir / notes_rel
        if sha256_file(notes_path) != article.get("technical_notes_sha256"):
            raise ValueError(f"Technical Notes changed before layout derivation: {package_id}")

        standfirst_rel = f"layout-standfirsts/{package_id}.tex"
        body_rel = f"layout-bodies/{package_id}.tex"
        split = split_article_layout(article_path, source_dir / standfirst_rel, source_dir / body_rel)
        records[package_id] = {
            "section_line": split["section_line"],
            "label_line": split["label_line"],
            "standfirst_path": standfirst_rel,
            "standfirst_sha256": split["standfirst_sha256"],
            "body_path": body_rel,
            "body_sha256": split["body_sha256"],
        }
        lines.extend([r"\clearpage", split["section_line"]])
        if split["label_line"]:
            lines.append(split["label_line"])
        lines.extend([
            "\\input{" + input_path(standfirst_rel) + "}",
            r"\medskip",
            r"\begin{multicols}{2}",
            "\\input{" + input_path(body_rel) + "}",
            r"\end{multicols}",
            "\\input{" + input_path(notes_rel) + "}",
            "",
        ])

    lines.extend([
        r"\clearpage",
        r"\printbibliography[title={References / Source Notes}]",
        r"\end{document}",
        "",
    ])
    return "\n".join(lines), records


def apply(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    if state.get("lifecycle_state") != "VALIDATED_DRAFT":
        raise ValueError(f"prebuild layout requires VALIDATED_DRAFT, got {state.get('lifecycle_state')}")
    gates = state.get("gates") or {}
    if gates.get("article_draft") != "passed" or gates.get("claim_and_chronology_validation") != "passed":
        raise ValueError("prebuild layout requires validated article drafts")
    if gates.get("latex_build") != "pending" or gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("prebuild layout requires build/visual/freeze gates pending")

    source = state.get("provenance", {}).get("validated_issue_source") or {}
    manifest_path = repo_root / str(source.get("path") or "")
    expected = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version / "source-manifest.json"
    if manifest_path != expected:
        raise ValueError("state-pinned source is not requested source revision")
    if not manifest_path.is_file() or sha256_file(manifest_path) != source.get("sha256"):
        raise ValueError("state-pinned source manifest missing or SHA mismatch")
    manifest = load_json(manifest_path)
    if manifest.get("status") != "VALIDATED_SOURCE_EXPANSION":
        raise ValueError("prebuild layout expects VALIDATED_SOURCE_EXPANSION")

    main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_path = manifest_path.parent / main_rel
    revised_main, layout_records = build_main_tex(main_path, manifest)
    main_path.write_text(revised_main, encoding="utf-8")

    for article in manifest.get("articles") or []:
        package_id = str(article["package_id"])
        layout = layout_records[package_id]
        article["layout_standfirst_present"] = True
        article["layout_standfirst_path"] = layout["standfirst_path"]
        article["layout_standfirst_sha256"] = layout["standfirst_sha256"]
        article["layout_body_path"] = layout["body_path"]
        article["layout_body_sha256"] = layout["body_sha256"]
        article["layout_transform"] = "accepted article section preserved; top-level section/label and generated bold standfirst are rendered full-width, remaining narrative is a layout-only local multicols derivative"

    manifest["layout"] = {
        "document_font_size": "11pt",
        "body_mode": "local two-column multicol narrative; full-width chapter headings, standfirsts, Technical Notes",
        "margin": "22mm",
        "column_gap": "6mm",
        "transition_policy": "balanced local multicols only around narrative body; no global twocolumn/onecolumn switch",
        "technical_note_policy": "full-width; one note per selected Evidence record; exact normalized claims/limitations/source URLs",
    }
    manifest["prebuild_layout"] = {
        "policy": "normal-special-balanced-local-multicol-v1",
        "article_section_changed": False,
        "technical_notes_changed": False,
        "full_width_chapter_headings": True,
        "full_width_standfirsts": True,
        "balanced_multicols": True,
        "hard_column_mode_switches": False,
        "article_count": len(layout_records),
    }
    manifest["main_tex"]["sha256"] = sha256_file(main_path)
    write_json(manifest_path, manifest)

    source["sha256"] = sha256_file(manifest_path)
    source["layout_mode"] = "balanced-local-multicol-narrative-full-width-evidence"
    source["prebuild_layout"] = True
    write_json(state_path, state)
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "source_version": source_version,
        "article_count": len(layout_records),
        "source_manifest_sha256": source["sha256"],
        "layout_mode": source["layout_mode"],
        "article_sections_changed": False,
        "technical_notes_changed": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    result = apply(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
