#!/usr/bin/env python3
"""Repair a built Special preview while preserving its current validated layout/content.

This path is for a Publication Preview that already has the intended mixed layout and
supplemental synthesis, but Human Visual Review finds reader-facing presentation
defects such as TOC depth, Technical Notes tail breaks, or generic bibliography
titles.  It copies the current validated source immutably, preserves accepted article
sections and existing Theme Synthesis payloads, and changes only derived presentation.
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from copy import deepcopy
from pathlib import Path
from typing import Any

from scripts.revise_special_visual_review_repairs import (
    enrich_bibliography_titles,
    ensure_package,
    fix_frontmatter_toc,
    load_json,
    normalize_technical_notes,
    sha,
    source_title_map,
    write_json,
)


def theme_synthesis_digests(source_dir: Path, manifest: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for record in manifest.get("theme_synthesis") or []:
        if not isinstance(record, dict):
            raise ValueError("malformed theme_synthesis record")
        rel = str(record.get("path") or "")
        expected = str(record.get("sha256") or "")
        if not rel or not expected:
            raise ValueError("theme_synthesis record requires path and sha256")
        path = source_dir / rel
        if not path.is_file():
            raise ValueError(f"Theme Synthesis missing: {rel}")
        actual = sha(path)
        if actual != expected:
            raise ValueError(f"Theme Synthesis digest mismatch: {rel}")
        result[rel] = actual
    return result


def accepted_article_digests(source_dir: Path, manifest: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for article in manifest.get("articles") or []:
        rel = str(article.get("article_section_path") or "")
        expected = str(article.get("article_section_sha256") or "")
        if not rel or not expected:
            raise ValueError("article section path/digest missing")
        path = source_dir / rel
        if not path.is_file() or sha(path) != expected:
            raise ValueError(f"accepted article section digest mismatch: {rel}")
        result[rel] = expected
    return result


def adapt_current_main(text: str) -> tuple[str, int, bool]:
    """Keep the current main structure, but make later structural starts adaptive."""
    if r"\begin{document}" not in text:
        raise ValueError("main.tex has no begin{document}")
    preamble, body = text.split(r"\begin{document}", 1)
    preamble = ensure_package(preamble, "needspace")
    text = preamble + r"\begin{document}" + body

    chapter_pattern = re.compile(r"\\clearpage\n(\\section\{)", re.M)
    seen = 0
    adaptive = 0

    def replace_chapter(match: re.Match[str]) -> str:
        nonlocal seen, adaptive
        seen += 1
        if seen == 1:
            return match.group(0)
        adaptive += 1
        return r"\Needspace{0.45\textheight}" + "\n" + r"\bigskip" + "\n" + match.group(1)

    text = chapter_pattern.sub(replace_chapter, text)
    if seen < 2:
        raise ValueError(f"expected at least two chapter starts, found {seen}")

    forced_refs = r"\clearpage" + "\n" + r"\printbibliography[title={References / Source Notes}]"
    refs_changed = forced_refs in text
    text = text.replace(
        forced_refs,
        r"\Needspace{0.30\textheight}"
        + "\n"
        + r"\bigskip"
        + "\n"
        + r"\printbibliography[title={References / Source Notes}]",
        1,
    )
    return text, adaptive, refs_changed


def verify_preserved_inputs(before_main: str, after_main: str, theme_paths: dict[str, str]) -> None:
    for rel in theme_paths:
        token = r"\input{" + Path(rel).with_suffix("").as_posix() + "}"
        if before_main.count(token) != 1:
            raise ValueError(f"expected exactly one Theme Synthesis input before repair: {rel}")
        if after_main.count(token) != 1:
            raise ValueError(f"Theme Synthesis input not preserved exactly once: {rel}")


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("preview repair marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("preserve_current_layout_visual_review_repairs") is not True:
        raise ValueError("layout marker does not request preserve-current-layout repairs")
    constraints = marker.get("constraints") or {}
    if constraints.get("new_external_evidence_allowed") is not False:
        raise ValueError("preview repair must forbid new external Evidence")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("preview repair must remain selected-Evidence-only")
    if constraints.get("accepted_article_claims_changed") is not False:
        raise ValueError("preview repair must preserve accepted article claims")
    if constraints.get("evidence_cards_mutated") is not False:
        raise ValueError("preview repair must not mutate Evidence cards")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise ValueError("preview repair requires RELEASE_CANDIDATE")
    if gates.get("latex_build") != "passed":
        raise ValueError("preview repair requires a successful prior PDF build")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("preview repair requires Visual Review and Freeze pending")

    current = deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha(current_manifest_path) != current.get("sha256"):
        raise ValueError("current validated source manifest digest mismatch")
    current_manifest = load_json(current_manifest_path)
    current_dir = current_manifest_path.parent

    theme_before = theme_synthesis_digests(current_dir, current_manifest)
    articles_before = accepted_article_digests(current_dir, current_manifest)
    current_main_path = current_dir / str((current_manifest.get("main_tex") or {}).get("path") or "main.tex")
    before_main = current_main_path.read_text(encoding="utf-8")

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(current_dir, output_dir)
    new_manifest = deepcopy(current_manifest)
    new_manifest["source_version"] = source_version
    new_manifest["status"] = "VALIDATED_PUBLICATION_PREVIEW_REPAIR_REVISION"
    new_manifest["derivation"] = (
        "Publication Preview repair derived only from the prior validated source and already selected Evidence. "
        "The existing mixed layout, accepted Article Draft sections, and Theme Synthesis payloads are preserved; "
        "TOC hierarchy, Technical Notes break policy, bibliography labels, and structural page starts are repaired."
    )
    new_manifest["basis"] = dict(current_manifest.get("basis") or {})
    new_manifest["basis"]["previous_source_manifest_path"] = current["path"]
    new_manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]

    # #55: re-apply the current generic per-card tail invariant to every Technical Note.
    selected_titles = set(changes.get("late_card_tail_group_titles") or [])
    notes_changed, tail_groups = normalize_technical_notes(output_dir, new_manifest, selected_titles)

    # #122: keep the printed Contents at reader-facing section level.
    front_rel = str((new_manifest.get("frontmatter") or {}).get("path") or "sections/00-frontmatter.tex")
    front_path = output_dir / front_rel
    if not front_path.is_file():
        raise ValueError("frontmatter file missing")
    toc_changed = fix_frontmatter_toc(front_path, len(new_manifest.get("articles") or []))
    new_manifest["frontmatter"] = {"path": front_rel, "sha256": sha(front_path)}

    # #78: restore reader-facing titles from immutable selected Evidence metadata.
    references_rel = str((new_manifest.get("references") or {}).get("path") or "references.bib")
    references_path = output_dir / references_rel
    title_map = source_title_map(repo_root, new_manifest)
    references_changed, reference_count = enrich_bibliography_titles(references_path, title_map)
    revised_references = references_path.read_text(encoding="utf-8")
    if re.search(r"title\s*=\s*\{Primary source \d+", revised_references):
        raise ValueError("generic Primary source bibliography title remains after preview repair")
    new_manifest["references"] = {"path": references_rel, "sha256": sha(references_path)}

    # #55/#123: keep the first feature boundary, but do not strand a Technical Notes
    # tail on its own page merely because every later chapter used a forced clearpage.
    main_path = output_dir / "main.tex"
    after_main, adaptive_chapters, references_start_changed = adapt_current_main(before_main)
    verify_preserved_inputs(before_main, after_main, theme_before)
    main_path.write_text(after_main, encoding="utf-8")
    new_manifest["main_tex"] = {"path": "main.tex", "sha256": sha(main_path)}

    # Byte-identity checks for reader content that this repair must not rewrite.
    for rel, expected in articles_before.items():
        if sha(output_dir / rel) != expected:
            raise ValueError(f"accepted article section changed during preview repair: {rel}")
    for rel, expected in theme_before.items():
        if sha(output_dir / rel) != expected:
            raise ValueError(f"Theme Synthesis payload changed during preview repair: {rel}")

    new_manifest["layout"] = dict(current_manifest.get("layout") or {})
    new_manifest["layout"].update(
        {
            "toc_depth": "section",
            "chapter_start_policy": "first feature on new page; later chapters use Needspace(0.45 textheight)",
            "references_start_policy": "Needspace(0.30 textheight), no forced clearpage",
            "page_count_policy": "32-page soft editorial target; 40-page hard ceiling; no padding solely to meet soft target",
        }
    )
    reader = dict(new_manifest.get("reader_facing_technical_notes") or {})
    reader["generic_boundary_source_tail_group"] = True
    reader["generic_boundary_source_tail_validation"] = "no unprotected boundary/limitation/source tail may remain"
    new_manifest["reader_facing_technical_notes"] = reader

    issue_refs = [int(x) for x in changes.get("issue_refs") or []]
    new_manifest["layout_revision"] = {
        "from_source_version": current_manifest.get("source_version"),
        "preserve_current_layout_visual_review_repairs": True,
        "issue_refs": issue_refs,
        "reader_content_changed": True,
        "reader_content_change_scope": "bibliography titles and presentation/navigation metadata only; accepted article claims and Evidence unchanged",
        "new_external_evidence": False,
        "selected_evidence_only": True,
        "accepted_article_sections_changed": False,
        "theme_synthesis_changed": False,
        "theme_synthesis_panel_count": len(theme_before),
        "theme_synthesis_inputs_preserved": True,
        "toc_depth_fixed_to_section": True,
        "toc_source_changed": toc_changed,
        "technical_notes_files_changed": notes_changed,
        "late_card_tail_group_count": tail_groups,
        "bibliography_titles_enriched": references_changed,
        "bibliography_entry_count": reference_count,
        "bibliography_generic_primary_source_titles_remaining": 0,
        "adaptive_later_chapter_start_count": adaptive_chapters,
        "forced_references_clearpage_removed": references_start_changed,
        "page_target_soft": 32,
        "page_target_hard_max": 40,
    }

    manifest_path = output_dir / "source-manifest.json"
    write_json(manifest_path, new_manifest)
    manifest_sha = sha(manifest_path)

    history = state.setdefault("provenance_history", {})
    history.setdefault("validated_issue_source", []).append(current)
    previous_build = deepcopy((state.get("provenance") or {}).get("latex_build") or {})
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
        "layout_mode": str((new_manifest.get("layout") or {}).get("body_mode") or current.get("layout_mode") or "mixed"),
        "layout_revision_sha256": sha(marker_path),
    }
    state["provenance"].pop("latex_build", None)
    state["provenance"]["reader_layout_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": sha(marker_path),
        "reason": str(marker.get("reason") or "Apply Publication Preview Human Visual Review repairs."),
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
        "theme_synthesis_panel_count": len(theme_before),
        "theme_synthesis_preserved": True,
        "accepted_article_sections_preserved": True,
        "toc_depth": "section",
        "technical_notes_files_changed": notes_changed,
        "late_card_tail_group_count": tail_groups,
        "bibliography_titles_enriched": references_changed,
        "bibliography_entry_count": reference_count,
        "adaptive_later_chapter_start_count": adaptive_chapters,
        "page_target_soft": 32,
        "page_target_hard_max": 40,
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
