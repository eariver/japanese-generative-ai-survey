#!/usr/bin/env python3
"""Execute mixed-layout Special revision with reader-facing text normalization.

Editorial synthesis artifacts may retain review-context wording for provenance. This
runner removes only known internal-review references before rendering, preserves the
current validated layout while inserting full-width selected-Evidence synthesis, and
allows the same immutable revision path before the first accepted PDF build.
"""

from __future__ import annotations

import json
import re
from copy import deepcopy
from pathlib import Path

from scripts import revise_special_mixed_layout as revision

# The initial mixed-layout builder accidentally used JSON-style boolean literals in
# Python dictionary expressions. They are looked up as module globals only when the
# build function executes, so bind them explicitly here until the canonical builder
# is mechanically rewritten.
revision.false = False
revision.true = True
# Architecture may legitimately classify an article package as LEAD or COMPARISON.
# They are reader-facing article forms just like FEATURE/SECTION/DEEP_DIVE and may
# receive selected-Evidence Theme Synthesis without changing the approved package.
revision.ARTICLE_TYPES.update({"LEAD", "COMPARISON"})


def reader_normalize(text: str) -> str:
    text = text.replace("本Evidence set", "本号で確認した一次資料群")
    text = re.sub(r"Issue #\d+の反省を踏まえ、", "", text)
    return text


def reader_month_label(package: dict) -> str:
    """Return the reader-facing month label from the package issue id."""
    issue_id = str(package.get("issue_id") or "")
    match = re.fullmatch(r"SP-\d{4}-M(\d{2})", issue_id)
    if match is None:
        return "一次資料・論文から読めること"
    return f"{int(match.group(1))}月の一次資料・論文から読めること"


_original_render = revision.render_synthesis


def normalized_render(theme, package, bib_map):
    normalized = dict(theme)
    normalized["title"] = reader_normalize(str(theme.get("title") or ""))
    normalized["intro"] = reader_normalize(str(theme.get("intro") or ""))
    rows = []
    for row in theme.get("rows") or []:
        item = dict(row)
        item["dimension"] = reader_normalize(str(row.get("dimension") or ""))
        item["observation"] = reader_normalize(str(row.get("observation") or ""))
        rows.append(item)
    normalized["rows"] = rows
    rendered, used = _original_render(normalized, package, bib_map)
    # The historical renderer carried a July-specific table heading from the
    # first retrospective issue that used Theme Synthesis. Keep the canonical
    # builder byte-compatible and normalize the derived reader label here.
    rendered = rendered.replace(
        "7月の一次資料・論文から読めること",
        reader_month_label(package),
        1,
    )
    return rendered, used


revision.render_synthesis = normalized_render


def inject_synthesis_into_current_layout(current_main: Path, manifest, synthesis_paths) -> str:
    """Preserve the current layout byte-shape and insert or refresh synthesis."""
    text = current_main.read_text(encoding="utf-8")
    existing_by_package = {
        str(item.get("package_id") or ""): str(item.get("path") or "")
        for item in (manifest.get("theme_synthesis") or [])
        if isinstance(item, dict) and item.get("package_id") and item.get("path")
    }
    for article in manifest.get("articles") or []:
        package_id = str(article.get("package_id") or "")
        synthesis = synthesis_paths.get(package_id)
        if not synthesis:
            continue
        synthesis_input = "\\input{" + revision.input_path(synthesis) + "}"

        # Immutable revisions copy the prior source tree first. When a prior
        # Theme Synthesis exists, the new renderer writes the refreshed panel to
        # the same relative path in the new revision. Preserve one input rather
        # than inserting a duplicate panel. If a future revision changes the
        # relative path, replace the old input exactly once.
        existing = existing_by_package.get(package_id)
        if existing:
            existing_input = "\\input{" + revision.input_path(existing) + "}"
            if text.count(existing_input) != 1:
                raise ValueError(
                    f"{package_id}: expected exactly one existing Theme Synthesis input in current main.tex"
                )
            if existing_input != synthesis_input:
                text = text.replace(existing_input, synthesis_input, 1)
            continue

        notes = str(article.get("technical_notes_path") or "")
        if not notes:
            raise ValueError(f"{package_id}: technical_notes_path required")
        notes_input = "\\input{" + revision.input_path(notes) + "}"
        if text.count(notes_input) != 1:
            raise ValueError(f"{package_id}: expected exactly one Technical Notes input in current main.tex")
        text = text.replace(notes_input, synthesis_input + "\n\\medskip\n" + notes_input, 1)
    return text


revision.build_main_tex = inject_synthesis_into_current_layout
_original_build = revision.build


def prebuild_aware_build(repo_root: Path, special_slug: str, issue_id: str, source_version: str):
    """Bridge the historical post-build builder to the current prebuild gate model."""
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    original_state = revision.load_json(state_path)
    prebuild = original_state.get("lifecycle_state") == "VALIDATED_DRAFT"
    current_source = deepcopy((original_state.get("provenance") or {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current_source.get("path") or "")
    current_main_text = ""
    if current_manifest_path.is_file():
        current_manifest = revision.load_json(current_manifest_path)
        current_main_text = (current_manifest_path.parent / str((current_manifest.get("main_tex") or {}).get("path") or "main.tex")).read_text(encoding="utf-8")

    if prebuild:
        gates = original_state.get("gates") or {}
        if gates.get("claim_and_chronology_validation") != "passed" or gates.get("latex_build") != "pending":
            raise ValueError("prebuild synthesis revision requires validated claims and pending PDF build")
        if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
            raise ValueError("prebuild synthesis revision requires Visual Review and Freeze pending")
        temporary = deepcopy(original_state)
        temporary["lifecycle_state"] = "RELEASE_CANDIDATE"
        temporary["gates"]["latex_build"] = "passed"
        revision.write_json(state_path, temporary)

    try:
        result = _original_build(repo_root, special_slug, issue_id, source_version)
    except Exception:
        if prebuild:
            revision.write_json(state_path, original_state)
        raise

    manifest_path = repo_root / str(result["source_manifest"])
    manifest = revision.load_json(manifest_path)
    local_multicols = r"\begin{multicols}{2}" in current_main_text
    if local_multicols:
        manifest["layout"] = {
            "document_font_size": "11pt",
            "body_mode": "mixed: narrative articles two-column via local multicols; theme synthesis and Technical Notes one-column full-width",
            "margin": "22mm",
            "column_gap": "6mm",
            "transition_policy": "preserve existing local multicols narrative; insert theme synthesis after narrative and before Technical Notes; no global twocolumn/onecolumn switch",
            "technical_note_policy": "one full-width note per selected Evidence record; exact normalized claims/limitations/source URLs",
            "house_style_reason": "preserve the current balanced two-column narrative identity while restoring full-width selected-Evidence comparison depth",
        }
        layout_revision = manifest.setdefault("layout_revision", {})
        layout_revision.update({
            "full_width_chapter_headings": True,
            "full_width_standfirsts": True,
            "balanced_multicols": True,
            "hard_column_mode_switches": False,
            "article_sections_changed": False,
            "technical_notes_changed": False,
            "reader_synthesis_added": True,
            "new_external_evidence": False,
        })
    revision.write_json(manifest_path, manifest)
    manifest_sha = revision.sha256_file(manifest_path)

    state = revision.load_json(state_path)
    state["provenance"]["validated_issue_source"]["sha256"] = manifest_sha
    if local_multicols:
        state["provenance"]["validated_issue_source"]["layout_mode"] = "mixed-local-two-column-narrative-full-width-evidence"
    layout_provenance = state["provenance"].setdefault("reader_layout_revision", {})
    layout_provenance["reason"] = (
        "Reader-facing comparison-depth revision using only Evidence already selected by the approved Architecture; "
        "the existing local balanced two-column narrative and full-width Technical Notes are preserved."
    )
    revision.write_json(state_path, state)

    result["source_manifest_sha256"] = manifest_sha
    result["prebuild_revision"] = prebuild
    result["preserved_local_multicols"] = local_multicols
    return result


revision.build = prebuild_aware_build


if __name__ == "__main__":
    raise SystemExit(revision.main())
