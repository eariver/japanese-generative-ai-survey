#!/usr/bin/env python3
"""Create an immutable Special revision that applies Human Visual Review repairs.

This is a derived-source repair pass. It never mutates Evidence cards or accepted
Article Drafts. It may change reader-facing presentation metadata, bibliography
labels, Technical Notes break grouping, and layout source derived from already
selected Evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any

from scripts import postprocess_special_reader_facing_notes as reader_notes
from scripts.special_layout_text_normalization import (
    normalize_itemize_manual_markers,
    split_leading_standfirst,
)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def input_path(path: str) -> str:
    return Path(path).with_suffix("").as_posix()


def ensure_package(preamble: str, package: str) -> str:
    token = rf"\usepackage{{{package}}}"
    if token in preamble:
        return preamble
    anchor = r"\usepackage{jgaisurvey}"
    if anchor not in preamble:
        raise ValueError(f"cannot add {package}: jgaisurvey package anchor missing")
    return preamble.replace(anchor, anchor + "\n" + token, 1)


def evidence_records(package: dict[str, Any]) -> list[dict[str, Any]]:
    result: list[dict[str, Any]] = []
    for key in ("primary_evidence", "supporting_evidence"):
        for record in package.get(key) or []:
            if not isinstance(record, dict):
                raise ValueError(f"{package.get('package_id')}: malformed {key} record")
            result.append(record)
    return result


def source_title_map(repo_root: Path, manifest: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for article in manifest.get("articles") or []:
        package_path = repo_root / str(article.get("draft_package_path") or "")
        if not package_path.is_file():
            raise ValueError(f"Draft Package missing: {package_path}")
        expected = str(article.get("draft_package_sha256") or "")
        if expected and sha(package_path) != expected:
            raise ValueError(f"Draft Package digest mismatch: {package_path}")
        package = load_json(package_path)
        for record in evidence_records(package):
            card = record.get("card") or {}
            artifact = card.get("artifact") or {}
            title = str(artifact.get("canonical_name") or "").strip()
            if not title:
                continue
            for source in card.get("sources") or []:
                if not isinstance(source, dict):
                    continue
                url = str(source.get("url") or "").strip()
                if not url:
                    continue
                existing = result.get(url)
                if existing is not None and existing != title:
                    raise ValueError(f"source URL maps to conflicting canonical titles: {url}")
                result[url] = title
    return result


def bib_escape(value: str) -> str:
    table = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
    }
    return "".join(table.get(ch, ch) for ch in value)


ENTRY_RE = re.compile(r"@online\{.*?\n\}", re.DOTALL)
URL_RE = re.compile(r"\n\s*url\s*=\s*\{([^}]*)\},")
TITLE_RE = re.compile(r"(\n\s*title\s*=\s*\{)(.*?)(\},)", re.DOTALL)


def enrich_bibliography_titles(path: Path, title_by_url: dict[str, str]) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    changed = 0
    placeholders = 0

    def replace_entry(match: re.Match[str]) -> str:
        nonlocal changed, placeholders
        block = match.group(0)
        url_match = URL_RE.search(block)
        title_match = TITLE_RE.search(block)
        if not url_match or not title_match:
            return block
        current = title_match.group(2).strip()
        if not current.startswith("Primary source "):
            return block
        url = url_match.group(1).strip()
        title = title_by_url.get(url)
        if not title:
            placeholders += 1
            return block
        replacement = title_match.group(1) + bib_escape(title) + title_match.group(3)
        changed += 1
        return block[: title_match.start()] + replacement + block[title_match.end() :]

    revised = ENTRY_RE.sub(replace_entry, text)
    if placeholders:
        raise ValueError(f"bibliography still has {placeholders} generic Primary source title(s)")
    if "Primary source 1:" in revised:
        raise ValueError("generic bibliography title remains after Evidence-title enrichment")
    path.write_text(revised, encoding="utf-8")
    return changed, len(ENTRY_RE.findall(revised))


FALLBACK_TAIL_GROUP_MARKER = "% reader-facing Technical Notes limitation/source fallback group"


def group_limitation_source_tail(text: str, selected_titles: set[str]) -> tuple[str, int]:
    """Fallback for cards whose technical point is a verified fact, not an attributed claim.

    The existing coherent-tail grouper starts at Vendor/Project/Author claim. Some
    first-party cards instead contain only a directly verified fact. For those cards,
    keep the limitation heading/block and primary-source block together while leaving
    the whole technicalnote breakable.
    """
    grouped = 0
    for title in sorted(selected_titles):
        pattern = re.compile(
            r"(\\begin\{technicalnote\}\{" + re.escape(title) + r"\}\{[^\n]*\}\n)"
            r"(.*?)"
            r"(\\end\{technicalnote\})",
            re.DOTALL,
        )
        match = pattern.search(text)
        if match is None:
            continue
        body = match.group(2)
        if reader_notes.TAIL_GROUP_MARKER in body or FALLBACK_TAIL_GROUP_MARKER in body:
            continue
        boundary = r"{\bfseries 読む際の境界}"
        source_end = r"\end{samepage}"
        if boundary not in body or source_end not in body:
            continue
        body = body.replace(
            boundary,
            r"\begin{minipage}{\linewidth}"
            + "\n"
            + FALLBACK_TAIL_GROUP_MARKER
            + "\n"
            + boundary,
            1,
        )
        body = body.replace(source_end, source_end + "\n" + r"\end{minipage}", 1)
        replacement = match.group(1) + body + match.group(3)
        text = text[: match.start()] + replacement + text[match.end() :]
        grouped += 1
    return text, grouped


def normalize_technical_notes(
    source_dir: Path,
    manifest: dict[str, Any],
    selected_titles: set[str],
) -> tuple[int, int]:
    # Extend the shared reader-facing mapper for Special schema values first
    # encountered in M04. Provenance enums remain untouched in Draft Packages.
    reader_notes.EVENT_LABELS.update(
        {
            "MEDIA_MODEL_RELEASE": "メディアモデル公開",
            "MEDIA_MODEL_UPDATE": "メディアモデル更新",
        }
    )
    reader_notes.TYPE_LABELS.update(
        {
            "MEDIA_MODEL_RELEASE": "メディアモデル公開",
            "MEDIA_MODEL_UPDATE": "メディアモデル更新",
            "MEDIA_モデル公開": "メディアモデル公開",
            "MEDIA_モデル更新": "メディアモデル更新",
            "PRODUCT": "製品",
        }
    )

    changed = 0
    grouped = 0
    found_titles: set[str] = set()
    for article in manifest.get("articles") or []:
        rel = str(article.get("technical_notes_path") or "")
        if not rel:
            continue
        path = source_dir / rel
        if not path.is_file():
            raise ValueError(f"Technical Notes missing: {rel}")
        original = path.read_text(encoding="utf-8")
        for title in selected_titles:
            if rf"\begin{{technicalnote}}{{{title}}}" in original:
                found_titles.add(title)
        revised = reader_notes.transform_note(original, selected_titles=selected_titles)
        revised, fallback_groups = group_limitation_source_tail(revised, selected_titles)
        taxonomy_findings = reader_notes.reader_taxonomy_findings(revised)
        if taxonomy_findings:
            raise ValueError(f"{rel}: raw/partial reader taxonomy leak: {taxonomy_findings}")
        current_groups = revised.count(reader_notes.TAIL_GROUP_MARKER)
        grouped += current_groups + fallback_groups
        if revised != original:
            path.write_text(revised, encoding="utf-8")
            changed += 1
        article["technical_notes_sha256"] = sha(path)

    missing = sorted(selected_titles - found_titles)
    if missing:
        raise ValueError(f"configured late-card tail title(s) not found: {missing}")
    if grouped < len(selected_titles):
        raise ValueError(
            f"late-card tail grouping incomplete: selected={len(selected_titles)} grouped={grouped}"
        )
    return changed, grouped


def fix_frontmatter_toc(path: Path, article_count: int) -> bool:
    text = path.read_text(encoding="utf-8")
    if r"\tableofcontents" not in text:
        raise ValueError("frontmatter has no tableofcontents")
    if article_count <= 0:
        raise ValueError("cannot generate TOC for zero articles")
    before = text
    text = text.replace(r"\setcounter{tocdepth}{0}", r"\setcounter{tocdepth}{1}")
    if r"\setcounter{tocdepth}{1}" not in text:
        text = text.replace(
            r"\tableofcontents",
            r"\setcounter{tocdepth}{1}" + "\n" + r"\tableofcontents",
            1,
        )
    path.write_text(text, encoding="utf-8")
    return text != before


def split_article(
    source: Path,
    standfirst_target: Path,
    body_target: Path,
    wide_target: Path,
) -> dict[str, Any]:
    lines = source.read_text(encoding="utf-8").splitlines(keepends=True)
    section_index = next(
        (i for i, line in enumerate(lines) if line.lstrip().startswith(r"\section{")),
        None,
    )
    if section_index is None:
        raise ValueError(f"{source}: top-level section heading missing")
    section_line = lines[section_index].strip()
    label_line = ""
    remove: set[int] = {section_index}
    for index in range(section_index + 1, min(section_index + 4, len(lines))):
        stripped = lines[index].strip()
        if not stripped:
            continue
        if stripped.startswith(r"\label{"):
            label_line = stripped
            remove.add(index)
        break
    remainder = [line for i, line in enumerate(lines) if i not in remove]

    wide_index: int | None = None
    for index, line in enumerate(remainder):
        stripped = line.lstrip()
        if stripped.startswith(r"\subsection{Theme Synthesis"):
            wide_index = index
            break
        if stripped.startswith(r"\begin{claimboundary}"):
            wide_index = index
            break
    narrative_lines = remainder if wide_index is None else remainder[:wide_index]
    wide_lines = [] if wide_index is None else remainder[wide_index:]

    standfirst_lines, narrative_lines = split_leading_standfirst(narrative_lines)
    narrative_text, narrative_markers, narrative_lifted = normalize_itemize_manual_markers(
        "".join(narrative_lines)
    )
    wide_text, wide_markers, wide_lifted = normalize_itemize_manual_markers(
        "".join(wide_lines)
    )
    standfirst_text = "".join(standfirst_lines)

    if not narrative_text.strip():
        raise ValueError(f"{source}: narrative body became empty")
    standfirst_target.parent.mkdir(parents=True, exist_ok=True)
    body_target.parent.mkdir(parents=True, exist_ok=True)
    wide_target.parent.mkdir(parents=True, exist_ok=True)
    standfirst_target.write_text(standfirst_text, encoding="utf-8")
    body_target.write_text(narrative_text, encoding="utf-8")
    wide_target.write_text(wide_text, encoding="utf-8")
    return {
        "section_line": section_line,
        "label_line": label_line,
        "standfirst_sha256": sha(standfirst_target),
        "standfirst_present": bool(standfirst_text.strip()),
        "body_sha256": sha(body_target),
        "wide_sha256": sha(wide_target),
        "wide_present": bool(wide_text.strip()),
        "manual_list_markers_removed": narrative_markers + wide_markers,
        "list_wrapper_items_lifted": narrative_lifted + wide_lifted,
    }


def build_main_tex(
    current_main: Path,
    manifest: dict[str, Any],
    layout_records: dict[str, dict[str, Any]],
) -> str:
    text = current_main.read_text(encoding="utf-8")
    if r"\begin{document}" not in text:
        raise ValueError("main.tex has no begin{document}")
    preamble = text.split(r"\begin{document}", 1)[0]
    preamble = ensure_package(preamble, "multicol")
    preamble = ensure_package(preamble, "needspace")
    if r"\setlength{\columnsep}" not in preamble:
        preamble += r"\setlength{\columnsep}{6mm}" + "\n"
    if r"\setlength{\multicolsep}" not in preamble:
        preamble += r"\setlength{\multicolsep}{0.8em plus 0.2em minus 0.1em}" + "\n"

    lines = [
        preamble.rstrip(),
        "",
        r"\begin{document}",
        r"\surveycover",
        r"\clearpage",
        r"\input{sections/00-frontmatter}",
        "",
    ]
    for index, article in enumerate(manifest.get("articles") or []):
        package_id = str(article["package_id"])
        layout = layout_records[package_id]
        if index == 0:
            lines.append(r"\clearpage")
        else:
            lines.extend([r"\Needspace{0.45\textheight}", r"\bigskip"])
        lines.append(str(layout["section_line"]))
        if layout.get("label_line"):
            lines.append(str(layout["label_line"]))
        lines.append(r"\vspace{0.15em}")
        if layout.get("standfirst_present"):
            lines.extend(
                [
                    rf"\input{{{input_path(str(layout['standfirst_path']))}}}",
                    r"\vspace{0.20em}",
                ]
            )
        lines.extend(
            [
                r"\begin{multicols}{2}",
                rf"\input{{{input_path(str(layout['body_path']))}}}",
                r"\end{multicols}",
            ]
        )
        if layout.get("wide_present"):
            lines.extend(
                [
                    r"\Needspace{5\baselineskip}",
                    rf"\input{{{input_path(str(layout['wide_path']))}}}",
                ]
            )
        lines.extend(
            [
                r"\medskip",
                rf"\input{{{input_path(str(article['technical_notes_path']))}}}",
                "",
            ]
        )
    lines.extend(
        [
            r"\Needspace{0.30\textheight}",
            r"\bigskip",
            r"\printbibliography[title={References / Source Notes}]",
            r"\end{document}",
            "",
        ]
    )
    result = "\n".join(lines)
    if r"\twocolumn" in result or r"\onecolumn" in result:
        raise ValueError("Visual-review repair must use local multicols, not global column switches")
    return result


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("visual-review repair marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("visual_review_repairs") is not True:
        raise ValueError("layout marker does not request visual_review_repairs")
    constraints = marker.get("constraints") or {}
    if constraints.get("new_external_evidence_allowed") is not False:
        raise ValueError("visual-review repair must forbid new external Evidence")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("visual-review repair must remain selected-Evidence-only")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise ValueError("visual-review repair requires RELEASE_CANDIDATE")
    if gates.get("latex_build") != "passed":
        raise ValueError("visual-review repair requires a successful prior PDF build")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("visual-review repair requires Visual Review and Freeze pending")

    current = dict(state.get("provenance", {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha(current_manifest_path) != current.get("sha256"):
        raise ValueError("current validated source manifest digest mismatch")
    current_manifest = load_json(current_manifest_path)
    current_dir = current_manifest_path.parent

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(current_dir, output_dir)

    new_manifest = dict(current_manifest)
    new_manifest["source_version"] = source_version
    new_manifest["status"] = "VALIDATED_VISUAL_REVIEW_REPAIR_REVISION"
    new_manifest["derivation"] = (
        "Human Visual Review repair revision derived only from the prior validated source "
        "and already selected Evidence. Accepted Article Draft source and Evidence records "
        "remain immutable; reader-facing taxonomy, card-tail grouping, bibliography titles, "
        "TOC depth, and layout-derived article bodies are repaired."
    )
    new_manifest["basis"] = dict(current_manifest.get("basis") or {})
    new_manifest["basis"]["previous_source_manifest_path"] = current["path"]
    new_manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]

    selected_titles = set(changes.get("late_card_tail_group_titles") or [])
    notes_changed, tail_groups = normalize_technical_notes(output_dir, new_manifest, selected_titles)

    front_rel = str((new_manifest.get("frontmatter") or {}).get("path") or "sections/00-frontmatter.tex")
    front_path = output_dir / front_rel
    if not front_path.is_file():
        raise ValueError("frontmatter file missing")
    toc_changed = fix_frontmatter_toc(front_path, len(new_manifest.get("articles") or []))
    new_manifest["frontmatter"] = {"path": front_rel, "sha256": sha(front_path)}

    references_rel = str((new_manifest.get("references") or {}).get("path") or "references.bib")
    references_path = output_dir / references_rel
    title_map = source_title_map(repo_root, new_manifest)
    reference_titles_changed, reference_count = enrich_bibliography_titles(references_path, title_map)
    # Idempotent Visual Review passes may start from an already enriched bibliography.
    # enrich_bibliography_titles itself rejects unresolved generic placeholders, so a
    # zero changed-count is valid on re-entry.
    new_manifest["references"] = {"path": references_rel, "sha256": sha(references_path)}

    layout_dir = output_dir / "layout-bodies"
    layout_records: dict[str, dict[str, Any]] = {}
    standfirst_count = 0
    manual_list_markers_removed = 0
    list_wrapper_items_lifted = 0
    for index, article in enumerate(new_manifest.get("articles") or [], start=1):
        package_id = str(article["package_id"])
        source = output_dir / str(article["article_section_path"])
        expected = str(article.get("article_section_sha256") or "")
        if expected and sha(source) != expected:
            raise ValueError(f"accepted article section changed before visual repair: {package_id}")
        standfirst_rel = f"layout-bodies/{index:02d}-{package_id}-standfirst.tex"
        body_rel = f"layout-bodies/{index:02d}-{package_id}-narrative.tex"
        wide_rel = f"layout-bodies/{index:02d}-{package_id}-wide.tex"
        info = split_article(
            source,
            output_dir / standfirst_rel,
            output_dir / body_rel,
            output_dir / wide_rel,
        )
        info["standfirst_path"] = standfirst_rel
        info["body_path"] = body_rel
        info["wide_path"] = wide_rel
        layout_records[package_id] = info
        if info["standfirst_present"]:
            standfirst_count += 1
        manual_list_markers_removed += int(info["manual_list_markers_removed"])
        list_wrapper_items_lifted += int(info["list_wrapper_items_lifted"])
        article["layout_standfirst_path"] = standfirst_rel
        article["layout_standfirst_sha256"] = info["standfirst_sha256"]
        article["layout_standfirst_present"] = info["standfirst_present"]
        article["layout_body_path"] = body_rel
        article["layout_body_sha256"] = info["body_sha256"]
        article["layout_wide_path"] = wide_rel
        article["layout_wide_sha256"] = info["wide_sha256"]
        article["layout_wide_present"] = info["wide_present"]

    main_path = output_dir / "main.tex"
    main_path.write_text(build_main_tex(current_dir / "main.tex", new_manifest, layout_records), encoding="utf-8")
    new_manifest["main_tex"] = {"path": "main.tex", "sha256": sha(main_path)}
    new_manifest["layout"] = dict(current_manifest.get("layout") or {})
    new_manifest["layout"].update(
        {
            "body_mode": (
                "mixed: narrative articles two-column via local balanced multicols; full-width chapter headings "
                "and standfirsts, Theme Synthesis, Claim Boundary, Technical Notes, and References"
            ),
            "column_gap": "6mm",
            "toc_depth": "section",
            "column_switch_policy": "local multicol environments only; no global twocolumn/onecolumn switches",
            "chapter_start_policy": "first feature on new page; later chapters Needspace(0.45 textheight)",
            "references_start_policy": "Needspace(0.30 textheight), no forced clearpage",
        }
    )
    reader = dict(new_manifest.get("reader_facing_technical_notes") or {})
    reader["machine_enum_policy"] = "reader-facing-labels-v6-generic-taxonomy-guard"
    reader["late_card_tail_group_titles"] = sorted(selected_titles)
    reader["late_card_tail_group_scope"] = (
        "exact titles selected from Human Visual Review; only the coherent claim/limitation/source tail "
        "is grouped and the Technical Notes card remains breakable"
    )
    new_manifest["reader_facing_technical_notes"] = reader
    issue_refs = [int(x) for x in changes.get("issue_refs") or []]
    new_manifest["layout_revision"] = {
        "from_source_version": current_manifest.get("source_version"),
        "visual_review_repairs": True,
        "issue_refs": issue_refs,
        "reader_content_changed": True,
        "reader_content_change_scope": (
            "presentation metadata only: taxonomy labels and bibliography titles; article claims and "
            "selected Evidence are unchanged"
        ),
        "new_external_evidence": False,
        "selected_evidence_only": True,
        "toc_depth_fixed_to_section": True,
        "toc_source_changed": toc_changed,
        "balanced_local_multicols": True,
        "hard_column_mode_switches": False,
        "article_sections_changed": False,
        "derived_layout_body_count": len(layout_records),
        "standfirst_full_width": True,
        "standfirst_count": standfirst_count,
        "manual_list_markers_removed": manual_list_markers_removed,
        "list_wrapper_items_lifted": list_wrapper_items_lifted,
        "technical_notes_files_changed": notes_changed,
        "late_card_tail_group_count": tail_groups,
        "bibliography_titles_enriched": reference_titles_changed,
        "bibliography_entry_count": reference_count,
        "bibliography_traceability_fields_preserved": True,
    }

    manifest_path = output_dir / "source-manifest.json"
    write_json(manifest_path, new_manifest)
    manifest_sha = sha(manifest_path)

    history = state.setdefault("provenance_history", {})
    history.setdefault("validated_issue_source", []).append(current)
    previous_build = dict(state.get("provenance", {}).get("latex_build") or {})
    if previous_build:
        history.setdefault("latex_build", []).append(previous_build)
    state["lifecycle_state"] = "VALIDATED_DRAFT"
    state["gates"]["latex_build"] = "pending"
    state["gates"]["visual_review"] = "pending"
    state["gates"]["freeze"] = "pending"
    state["provenance"]["validated_issue_source"] = {
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": source_version,
        "layout_mode": "balanced-local-multicol-visual-review-repair",
        "layout_revision_sha256": sha(marker_path),
    }
    state["provenance"].pop("latex_build", None)
    state["provenance"]["reader_layout_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": sha(marker_path),
        "reason": str(
            marker.get("reason")
            or "Apply Human Visual Review repairs without changing selected Evidence or accepted article claims."
        ),
    }
    write_json(state_path, state)

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "source_version": source_version,
        "previous_source_version": current_manifest.get("source_version"),
        "source_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "source_manifest_sha256": manifest_sha,
        "issue_refs": issue_refs,
        "toc_depth": "section",
        "balanced_local_multicols": True,
        "technical_notes_files_changed": notes_changed,
        "late_card_tail_group_count": tail_groups,
        "bibliography_titles_enriched": reference_titles_changed,
        "bibliography_entry_count": reference_count,
        "standfirst_count": standfirst_count,
        "manual_list_markers_removed": manual_list_markers_removed,
        "list_wrapper_items_lifted": list_wrapper_items_lifted,
        "new_external_evidence": False,
        "lifecycle_state": state["lifecycle_state"],
        "latex_build_gate": state["gates"]["latex_build"],
        "visual_review_gate": state["gates"]["visual_review"],
        "freeze_gate": state["gates"]["freeze"],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
