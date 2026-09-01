#!/usr/bin/env python3
"""Create an immutable typography-only recovery revision for a Special Visual Review source.

This pass is for a derived mixed-layout source that is structurally valid but fails the
strict TeX log gate because narrow columns produce avoidable Underfull hboxes. It keeps
reader wording, Evidence, accepted Article Drafts, Technical Notes, bibliography, and
all Human Visual Review repairs unchanged. Only derived layout placement is adjusted:
article standfirsts move to full width and subsection headings become ragged-right inside
local two-column narrative bodies.
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
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def input_path(path: str) -> str:
    return Path(path).with_suffix("").as_posix()


def extract_lead_and_relax_headings(text: str) -> tuple[str, str, int]:
    """Return full-width lead, remaining narrative, and relaxed subsection count."""
    lines = text.splitlines(keepends=True)
    lead_index: int | None = None
    for index, line in enumerate(lines):
        stripped = line.strip()
        if not stripped or stripped.startswith("%"):
            continue
        if not stripped.startswith(r"\noindent\textbf{"):
            raise ValueError("narrative body does not start with expected generated standfirst")
        lead_index = index
        break
    if lead_index is None:
        raise ValueError("narrative body has no standfirst")

    lead = lines[lead_index]
    del lines[lead_index]
    if lead_index < len(lines) and not lines[lead_index].strip():
        del lines[lead_index]

    relaxed = 0
    revised: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith(r"\subsection{") and stripped.endswith("}"):
            revised.append(r"\begingroup\raggedright" + "\n")
            revised.append(line)
            revised.append(r"\par\endgroup" + "\n")
            relaxed += 1
        else:
            revised.append(line)
    if relaxed < 1:
        raise ValueError("narrative body has no subsection heading to relax")
    return lead, "".join(revised), relaxed


def add_lead_input(main_text: str, body_rel: str, lead_rel: str) -> str:
    body_input = rf"\input{{{input_path(body_rel)}}}"
    lead_input = rf"\input{{{input_path(lead_rel)}}}"
    if lead_input in main_text:
        raise ValueError(f"lead input already present: {lead_rel}")
    anchor = r"\begin{multicols}{2}" + "\n" + body_input
    replacement = lead_input + "\n" + r"\vspace{0.2em}" + "\n" + anchor
    if anchor not in main_text:
        raise ValueError(f"cannot locate narrative multicol input: {body_rel}")
    return main_text.replace(anchor, replacement, 1)


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("typography recovery marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("visual_review_typography_recovery") is not True:
        raise ValueError("marker does not request visual_review_typography_recovery")
    constraints = marker.get("constraints") or {}
    if constraints.get("new_external_evidence_allowed") is not False:
        raise ValueError("typography recovery must forbid new external Evidence")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("typography recovery must remain selected-Evidence-only")
    if constraints.get("reader_content_changed") is not False:
        raise ValueError("typography recovery must not change reader wording")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "VALIDATED_DRAFT":
        raise ValueError("typography recovery requires VALIDATED_DRAFT")
    if gates.get("claim_and_chronology_validation") != "passed":
        raise ValueError("claim/chronology validation must remain passed")
    if gates.get("latex_build") != "pending":
        raise ValueError("typography recovery requires latex_build pending")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("Visual Review and Freeze must remain pending")

    current = dict(state.get("provenance", {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha(current_manifest_path) != current.get("sha256"):
        raise ValueError("current validated source manifest digest mismatch")
    current_manifest = load_json(current_manifest_path)
    current_layout = current_manifest.get("layout") or {}
    if "local balanced multicols" not in str(current_layout.get("body_mode") or ""):
        raise ValueError("typography recovery expects local balanced multicols source")
    current_layout_revision = current_manifest.get("layout_revision") or {}
    if current_layout_revision.get("visual_review_repairs") is not True:
        raise ValueError("typography recovery basis must preserve Human Visual Review repairs")
    if current_layout_revision.get("new_external_evidence") is not False:
        raise ValueError("typography recovery basis unexpectedly introduced external Evidence")

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(current_manifest_path.parent, output_dir)

    new_manifest = dict(current_manifest)
    articles = [dict(article) for article in current_manifest.get("articles") or []]
    new_manifest["articles"] = articles
    main_path = output_dir / str((new_manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_text = main_path.read_text(encoding="utf-8")

    lead_dir = output_dir / "layout-leads"
    lead_dir.mkdir(parents=True, exist_ok=True)
    total_headings = 0
    for index, article in enumerate(articles, start=1):
        body_rel = str(article.get("layout_body_path") or "")
        if not body_rel:
            raise ValueError(f"{article.get('package_id')}: layout_body_path missing")
        body_path = output_dir / body_rel
        expected = str(article.get("layout_body_sha256") or "")
        if not body_path.is_file() or (expected and sha(body_path) != expected):
            raise ValueError(f"{article.get('package_id')}: layout body digest mismatch")
        lead, revised_body, relaxed = extract_lead_and_relax_headings(body_path.read_text(encoding="utf-8"))
        total_headings += relaxed
        body_path.write_text(revised_body, encoding="utf-8")
        lead_rel = f"layout-leads/{index:02d}-{article['package_id']}-lead.tex"
        lead_path = output_dir / lead_rel
        lead_path.write_text(lead, encoding="utf-8")
        main_text = add_lead_input(main_text, body_rel, lead_rel)
        article["layout_body_sha256"] = sha(body_path)
        article["layout_lead_path"] = lead_rel
        article["layout_lead_sha256"] = sha(lead_path)
        article["layout_subsection_heading_policy"] = "ragged-right within local two-column narrative"

    if main_text.count(r"\begin{multicols}{2}") != len(articles):
        raise ValueError("local two-column article count changed unexpectedly")
    if main_text.count("layout-leads/") != len(articles):
        raise ValueError("not every article received a full-width standfirst")
    main_path.write_text(main_text, encoding="utf-8")

    new_manifest["source_version"] = source_version
    new_manifest["status"] = "VALIDATED_VISUAL_REVIEW_TYPOGRAPHY_RECOVERY_REVISION"
    new_manifest["derivation"] = (
        "Typography-only recovery of the prior Human Visual Review repair source. The exact standfirst text "
        "is moved outside local two-column environments and subsection headings are ragged-right inside those "
        "columns to avoid narrow-column Underfull hboxes. Reader wording, Evidence, accepted Article Drafts, "
        "Technical Notes, bibliography metadata, TOC entries, and Human Visual Review repairs are unchanged."
    )
    new_manifest["basis"] = dict(current_manifest.get("basis") or {})
    new_manifest["basis"]["previous_source_manifest_path"] = current["path"]
    new_manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]
    new_manifest["main_tex"] = {"path": main_path.relative_to(output_dir).as_posix(), "sha256": sha(main_path)}
    new_manifest["layout"] = dict(current_layout)
    new_manifest["layout"].update(
        {
            "standfirst_policy": "full-width before each local two-column narrative",
            "subsection_heading_policy": "ragged-right within local two-column narrative",
        }
    )
    new_manifest["layout_revision"] = dict(current_layout_revision)
    new_manifest["layout_revision"].update(
        {
            "from_source_version": current_manifest.get("source_version"),
            "visual_review_typography_recovery": True,
            "reader_content_changed": False,
            "new_external_evidence": False,
            "article_standfirsts_moved_full_width": len(articles),
            "subsection_headings_relaxed": total_headings,
            "technical_notes_changed": False,
            "references_changed": False,
            "frontmatter_changed": False,
        }
    )

    manifest_path = output_dir / "source-manifest.json"
    write_json(manifest_path, new_manifest)
    manifest_sha = sha(manifest_path)

    history = state.setdefault("provenance_history", {})
    history.setdefault("validated_issue_source", []).append(current)
    state["provenance"]["validated_issue_source"] = {
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": source_version,
        "layout_mode": "balanced-local-multicol-visual-review-typography-recovery",
        "layout_revision_sha256": sha(marker_path),
    }
    state["provenance"]["reader_layout_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": sha(marker_path),
        "reason": str(marker.get("reason") or "Recover strict TeX log gate without changing reader wording."),
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
        "article_standfirsts_moved_full_width": len(articles),
        "subsection_headings_relaxed": total_headings,
        "reader_content_changed": False,
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
    print(json.dumps(build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
