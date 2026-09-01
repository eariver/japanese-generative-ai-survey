#!/usr/bin/env python3
"""Create an immutable layout-only revision adding safe spacing in final synthesis subsections."""
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
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise ValueError("final-synthesis spacing revision requires RELEASE_CANDIDATE")
    if (
        gates.get("latex_build") != "passed"
        or gates.get("visual_review") != "pending"
        or gates.get("freeze") != "pending"
    ):
        raise ValueError("final-synthesis spacing revision requires built, unapproved release candidate")

    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("layout marker mismatch")
    constraints = marker.get("constraints") or {}
    changes = marker.get("layout_changes") or {}
    if (
        constraints.get("new_external_evidence_allowed") is not False
        or constraints.get("reader_content_changed") is not False
        or constraints.get("selected_evidence_only") is not True
    ):
        raise ValueError("layout marker must be content-neutral and selected-Evidence-only")
    if changes.get("final_synthesis_subsection_spacing") is not True:
        raise ValueError("final synthesis subsection spacing marker missing")

    current = dict(state.get("provenance", {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha(current_manifest_path) != current.get("sha256"):
        raise ValueError("current source digest mismatch")
    current_manifest = load_json(current_manifest_path)
    current_dir = current_manifest_path.parent

    final_info = dict(current_manifest.get("final_synthesis") or {})
    final_rel = str(final_info.get("tex_path") or "")
    if not final_rel:
        raise ValueError("final synthesis TeX is not tracked")
    current_final_path = current_dir / final_rel
    if not current_final_path.is_file():
        raise ValueError("tracked final synthesis TeX is missing")
    prior_final_sha = str(final_info.get("tex_sha256") or "")
    if not prior_final_sha or sha(current_final_path) != prior_final_sha:
        raise ValueError("final synthesis digest mismatch")

    out = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if out.exists():
        raise ValueError(f"revision already exists: {out}")
    shutil.copytree(current_dir, out)

    final_path = out / final_rel
    text = final_path.read_text(encoding="utf-8")
    prefix = r"\par\medskip\Needspace{5\baselineskip}" + "\n"
    if prefix + r"\subsection{" in text:
        raise ValueError("final synthesis subsection guard already present")
    count = text.count(r"\subsection{")
    if count < 2:
        raise ValueError(f"expected multiple numbered final-synthesis subsections, found {count}")
    text = text.replace(r"\subsection{", prefix + r"\subsection{")
    final_path.write_text(text, encoding="utf-8")

    # Everything except the derived final-synthesis layout must remain byte-identical.
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
    refs = current_manifest.get("references") or {}
    refs_path = out / str(refs.get("path") or "")
    if refs.get("sha256") and sha(refs_path) != refs["sha256"]:
        raise ValueError("bibliography changed")

    main_path = out / "main.tex"
    new = dict(current_manifest)
    new["source_version"] = source_version
    new["status"] = "VALIDATED_FINAL_SYNTHESIS_SUBSECTION_SPACING_REVISION"
    new["derivation"] = (
        "Layout-only revision of the prior validated Retrospective Special source. "
        "Accepted synthesis wording, citations, selected Evidence, Article Drafts, Technical Notes, "
        "and bibliography data are unchanged. Numbered subsections in the final synthesis receive "
        "explicit paragraph separation and a five-baseline minimum-space guard."
    )
    new["basis"] = dict(current_manifest.get("basis") or {})
    new["basis"]["previous_source_manifest_path"] = current["path"]
    new["basis"]["previous_source_manifest_sha256"] = current["sha256"]
    new["main_tex"] = {"path": "main.tex", "sha256": sha(main_path)}
    new["layout"] = dict(current_manifest.get("layout") or {})
    new["layout"]["final_synthesis_subsection_policy"] = (
        "paragraph termination + medskip + Needspace(5 baselines) before each numbered subsection"
    )
    new_final = dict(final_info)
    new_final["tex_sha256"] = sha(final_path)
    new_final["layout_only_revision"] = True
    new_final["numbered_subsection_guard_count"] = count
    new["final_synthesis"] = new_final
    new["layout_revision"] = {
        "from_source_version": current_manifest.get("source_version"),
        "reader_content_changed": False,
        "new_external_evidence": False,
        "final_synthesis_subsection_spacing": True,
        "subsection_needspace_baselines": 5,
        "numbered_subsection_guard_count": count,
        "accepted_article_sections_changed": False,
        "technical_notes_changed": False,
        "theme_synthesis_changed": False,
        "bibliography_data_changed": False,
        "final_synthesis_wording_changed": False,
        "final_synthesis_layout_changed": True
    }
    manifest_path = out / "source-manifest.json"
    write_json(manifest_path, new)
    manifest_sha = sha(manifest_path)

    hist = state.setdefault("provenance_history", {})
    hist.setdefault("validated_issue_source", []).append(current)
    prev_build = dict(state.get("provenance", {}).get("latex_build") or {})
    if prev_build:
        hist.setdefault("latex_build", []).append(prev_build)
    state["lifecycle_state"] = "VALIDATED_DRAFT"
    state["gates"]["latex_build"] = "pending"
    state["gates"]["visual_review"] = "pending"
    state["gates"]["freeze"] = "pending"
    state["provenance"]["validated_issue_source"] = {
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": source_version,
        "layout_mode": "final-synthesis-subsection-spacing-guard",
        "layout_revision_sha256": sha(marker_path)
    }
    state["provenance"].pop("latex_build", None)
    state["provenance"]["reader_layout_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": sha(marker_path),
        "reason": (
            "Human Visual Review of M03 v0.9 found the final-synthesis subsection heading visually "
            "colliding with the preceding citation; apply a generic local spacing guard without "
            "changing accepted synthesis wording or Evidence."
        )
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
        "final_synthesis_tex_sha256": sha(final_path),
        "numbered_subsection_guard_count": count,
        "reader_content_changed": False,
        "new_external_evidence": False,
        "lifecycle_state": state["lifecycle_state"],
        "latex_build_gate": state["gates"]["latex_build"],
        "visual_review_gate": state["gates"]["visual_review"],
        "freeze_gate": state["gates"]["freeze"]
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    print(
        json.dumps(
            build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version),
            ensure_ascii=False,
            indent=2
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
