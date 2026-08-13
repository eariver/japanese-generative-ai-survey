#!/usr/bin/env python3
"""Create an immutable layout-only Special revision with section-level TOC.

The revision changes only table-of-contents depth. Article wording, Technical Notes,
Evidence, synthesis, bibliography data, and source URLs remain byte-identical.
It can be applied either to an unreviewed RELEASE_CANDIDATE or after an over-budget
preview build that left the issue at VALIDATED_DRAFT with latex_build pending.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    lifecycle = state.get("lifecycle_state")
    if lifecycle == "RELEASE_CANDIDATE":
        if gates.get("latex_build") != "passed":
            raise ValueError("RELEASE_CANDIDATE compact-TOC revision requires latex_build passed")
    elif lifecycle == "VALIDATED_DRAFT":
        if gates.get("claim_and_chronology_validation") != "passed" or gates.get("latex_build") != "pending":
            raise ValueError("VALIDATED_DRAFT compact-TOC revision requires validated content and pending latex_build")
    else:
        raise ValueError("compact-TOC revision requires VALIDATED_DRAFT or RELEASE_CANDIDATE")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("compact-TOC revision requires unapproved Visual Review and Freeze")

    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("layout marker mismatch")
    constraints = marker.get("constraints") or {}
    changes = marker.get("layout_changes") or {}
    if constraints.get("new_external_evidence_allowed") is not False:
        raise ValueError("layout marker must forbid new external evidence")
    if constraints.get("reader_content_changed") is not False:
        raise ValueError("compact TOC must be reader-content neutral")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("layout marker must remain selected-Evidence-only")
    if changes.get("compact_toc_to_sections") is not True:
        raise ValueError("compact_toc_to_sections marker is required")

    current = dict(state.get("provenance", {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha(current_manifest_path) != current.get("sha256"):
        raise ValueError("current source digest mismatch")
    current_manifest = load_json(current_manifest_path)
    current_dir = current_manifest_path.parent
    out = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if out.exists():
        raise ValueError(f"revision already exists: {out}")
    shutil.copytree(current_dir, out)

    front_info = dict(current_manifest.get("frontmatter") or {})
    front_rel = str(front_info.get("path") or "sections/00-frontmatter.tex")
    front_path = out / front_rel
    if not front_path.is_file():
        raise ValueError("frontmatter missing")
    text = front_path.read_text(encoding="utf-8")
    if r"\setcounter{tocdepth}{0}" in text:
        raise ValueError("TOC is already section-only")
    token = r"\tableofcontents"
    if text.count(token) != 1:
        raise ValueError("expected exactly one tableofcontents in frontmatter")
    revised = text.replace(token, r"\setcounter{tocdepth}{0}" + "\n" + token, 1)
    front_path.write_text(revised, encoding="utf-8")

    for article in current_manifest.get("articles") or []:
        section = out / str(article["article_section_path"])
        notes = out / str(article["technical_notes_path"])
        if sha(section) != article["article_section_sha256"]:
            raise ValueError(f"accepted article changed: {article['package_id']}")
        if sha(notes) != article["technical_notes_sha256"]:
            raise ValueError(f"Technical Notes changed: {article['package_id']}")
    for synth in current_manifest.get("theme_synthesis") or []:
        target = out / str(synth["path"])
        if sha(target) != synth["sha256"]:
            raise ValueError(f"Theme Synthesis changed: {synth.get('package_id')}")
    final_info = dict(current_manifest.get("final_synthesis") or {})
    final_rel = str(final_info.get("tex_path") or "")
    if final_rel:
        final_path = out / final_rel
        prior_sha = str(final_info.get("tex_sha256") or "")
        if prior_sha and sha(final_path) != prior_sha:
            raise ValueError("final synthesis changed unexpectedly")

    new_manifest = dict(current_manifest)
    new_manifest["source_version"] = source_version
    new_manifest["status"] = "VALIDATED_COMPACT_TOC_REVISION"
    new_manifest["derivation"] = (
        "Layout-only revision of the prior validated source. Reader wording and Evidence are unchanged; "
        "the table of contents is limited to section-level entries to keep long-form Specials within the approved page budget."
    )
    new_manifest["basis"] = dict(current_manifest.get("basis") or {})
    new_manifest["basis"]["previous_source_manifest_path"] = current["path"]
    new_manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]
    front_info["path"] = front_rel
    front_info["sha256"] = sha(front_path)
    new_manifest["frontmatter"] = front_info
    main_path = out / str((current_manifest.get("main_tex") or {}).get("path") or "main.tex")
    new_manifest["main_tex"] = dict(current_manifest.get("main_tex") or {})
    new_manifest["main_tex"]["sha256"] = sha(main_path)
    new_manifest["layout"] = dict(current_manifest.get("layout") or {})
    new_manifest["layout"]["toc_depth"] = "section"
    new_manifest["layout_revision"] = {
        "from_source_version": current_manifest.get("source_version"),
        "reader_content_changed": False,
        "new_external_evidence": False,
        "compact_toc_to_sections": True,
        "article_sections_changed": False,
        "technical_notes_changed": False,
        "theme_synthesis_changed": False,
        "final_synthesis_changed": False,
        "bibliography_data_changed": False,
    }
    manifest_path = out / "source-manifest.json"
    write_json(manifest_path, new_manifest)
    manifest_sha = sha(manifest_path)

    history = state.setdefault("provenance_history", {})
    history.setdefault("validated_issue_source", []).append(current)
    prior_build = dict(state.get("provenance", {}).get("latex_build") or {})
    if prior_build:
        history.setdefault("latex_build", []).append(prior_build)
    state["lifecycle_state"] = "VALIDATED_DRAFT"
    state["gates"]["latex_build"] = "pending"
    state["gates"]["visual_review"] = "pending"
    state["gates"]["freeze"] = "pending"
    new_source_prov = dict(current)
    new_source_prov.update({
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": source_version,
        "layout_mode": "section-level-toc",
        "layout_revision_sha256": sha(marker_path),
    })
    state["provenance"]["validated_issue_source"] = new_source_prov
    state["provenance"].pop("latex_build", None)
    state["provenance"]["reader_layout_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": sha(marker_path),
        "reason": str(marker.get("reason") or "Compact subsection-heavy TOC without changing reader content."),
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
        "frontmatter_path": front_rel,
        "toc_depth": "section",
        "reader_content_changed": False,
        "new_external_evidence": False,
        "lifecycle_state": state["lifecycle_state"],
        "latex_build_gate": state["gates"]["latex_build"],
    }


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root", default=".")
    p.add_argument("--special-slug", required=True)
    p.add_argument("--issue-id", required=True)
    p.add_argument("--source-version", required=True)
    args = p.parse_args()
    print(json.dumps(build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
