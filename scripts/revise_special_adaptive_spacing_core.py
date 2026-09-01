#!/usr/bin/env python3
"""Create an immutable layout-only Special revision with adaptive chapter spacing."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
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
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    changes = marker.get("layout_changes") or {}

    # Human Visual Review can expose several interacting reader-facing defects
    # at once. Route those through the generic immutable repair builder instead
    # of stacking issue-specific one-off transforms.
    if changes.get("visual_review_repairs") is True:
        from scripts.revise_special_visual_review_repairs import build as build_visual_review_repairs

        return build_visual_review_repairs(repo_root, special_slug, issue_id, source_version)

    # If a derived Visual Review source passed structural validation but failed
    # at the TeX compiler, recover into a new immutable revision rather than
    # mutating or overwriting the failed source version.
    if changes.get("visual_review_recovery") is True:
        from scripts.revise_special_visual_review_recovery import build as build_visual_review_recovery

        return build_visual_review_recovery(repo_root, special_slug, issue_id, source_version)

    # A mixed-layout Visual Review source can compile but still fail the strict
    # TeX log gate because long standfirsts/headings are justified in narrow
    # columns. Keep wording immutable and recover only the derived typography.
    if changes.get("visual_review_typography_recovery") is True:
        from scripts.revise_special_visual_review_typography_recovery import build as build_visual_review_typography_recovery

        return build_visual_review_typography_recovery(repo_root, special_slug, issue_id, source_version)

    # A nearly-final mixed-layout source can still miss the Special page floor
    # by one page or retain an isolated narrow-column Underfull paragraph after
    # typography recovery. Adjust only vertical page breathing and explicitly
    # selected generated paragraph alignment, without changing reader wording.
    if changes.get("visual_review_final_spacing_recovery") is True:
        from scripts.revise_special_final_spacing_recovery import build as build_final_spacing_recovery

        return build_final_spacing_recovery(repo_root, special_slug, issue_id, source_version)

    # Pre-Freeze review can identify a required cross-article retrospective
    # synthesis that is missing from an otherwise built Special preview, along
    # with reader taxonomy leakage in derived Technical Notes. Keep Evidence and
    # accepted Article Drafts immutable and derive a new source revision.
    if changes.get("retrospective_final_synthesis_repair") is True:
        from scripts.revise_special_retrospective_synthesis_repair import build as build_retrospective_synthesis_repair

        return build_retrospective_synthesis_repair(repo_root, special_slug, issue_id, source_version)

    # Issue #55: apply one generic per-card invariant instead of a Human-selected
    # title allowlist.  Boundary/limitation/source stay together; the whole card
    # remains breakable.
    if changes.get("generic_technical_note_tail_policy") is True:
        from scripts.revise_special_technical_note_tail_policy import build as build_tail_policy

        return build_tail_policy(repo_root, special_slug, issue_id, source_version)

    if changes.get("single_column_adaptive_chapter_starts") is True:
        from scripts.revise_special_single_column_adaptive_spacing import build as build_single_column

        return build_single_column(repo_root, special_slug, issue_id, source_version)

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise ValueError("adaptive spacing requires RELEASE_CANDIDATE")
    if (
        gates.get("latex_build") != "passed"
        or gates.get("visual_review") != "pending"
        or gates.get("freeze") != "pending"
    ):
        raise ValueError("adaptive spacing requires built, unapproved release candidate")
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("layout marker mismatch")
    constraints = marker.get("constraints") or {}
    if (
        constraints.get("new_external_evidence_allowed") is not False
        or constraints.get("reader_content_changed") is not False
        or constraints.get("selected_evidence_only") is not True
    ):
        raise ValueError("layout marker must be content-neutral and selected-Evidence-only")
    current = dict(state.get("provenance", {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha(current_manifest_path) != current.get("sha256"):
        raise ValueError("current source digest mismatch")
    current_manifest = load_json(current_manifest_path)
    current_dir = current_manifest_path.parent
    if not str((current_manifest.get("layout") or {}).get("body_mode", "")).startswith(
        "balanced mixed:"
    ):
        raise ValueError("adaptive spacing expects balanced mixed source")
    out = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if out.exists():
        raise ValueError(f"revision already exists: {out}")
    shutil.copytree(current_dir, out)

    main_path = out / "main.tex"
    text = main_path.read_text(encoding="utf-8")
    chapter_pattern = re.compile(r"\\clearpage\n(\\section\{)", re.M)
    matches = list(chapter_pattern.finditer(text))
    if len(matches) < 6:
        raise ValueError(f"expected chapter clearpages, found {len(matches)}")
    seen = 0

    def repl(match: re.Match[str]) -> str:
        nonlocal seen
        seen += 1
        if seen == 1:
            return match.group(0)
        return r"\Needspace{0.45\textheight}" + "\n" + r"\bigskip" + "\n" + match.group(1)

    text = chapter_pattern.sub(repl, text)
    text = text.replace(
        r"\clearpage" + "\n" + r"\input{final-synthesis/70-retrospective-synthesis}",
        r"\Needspace{0.55\textheight}"
        + "\n"
        + r"\bigskip"
        + "\n"
        + r"\input{final-synthesis/70-retrospective-synthesis}",
        1,
    )
    text = text.replace(
        r"\clearpage" + "\n" + r"\printbibliography[title={References / Source Notes}]",
        r"\bigskip" + "\n" + r"\printbibliography[title={References / Source Notes}]",
        1,
    )
    if (
        r"\clearpage" + "\n" + r"\printbibliography[title={References / Source Notes}]"
        in text
    ):
        raise ValueError("forced bibliography clearpage still present")
    main_path.write_text(text, encoding="utf-8")

    final_info = dict(current_manifest.get("final_synthesis") or {})
    final_rel = str(final_info.get("tex_path") or "")
    final_path = out / final_rel
    if not final_rel or not final_path.is_file():
        raise ValueError("final synthesis TeX missing")
    final_text = final_path.read_text(encoding="utf-8").replace(
        r"\subsection{", r"\Needspace{5\baselineskip}" + "\n" + r"\subsection{"
    )
    final_path.write_text(final_text, encoding="utf-8")

    new = dict(current_manifest)
    new["source_version"] = source_version
    new["status"] = "VALIDATED_ADAPTIVE_SPACING_REVISION"
    new["derivation"] = (
        "Layout-only revision of the prior balanced source. Reader wording, selected "
        "Evidence, accepted Article Draft sections, Theme Synthesis panels, and Technical "
        "Notes are unchanged. Forced chapter/reference page breaks are replaced with "
        "minimum-space guards."
    )
    new["basis"] = dict(current_manifest.get("basis") or {})
    new["basis"]["previous_source_manifest_path"] = current["path"]
    new["basis"]["previous_source_manifest_sha256"] = current["sha256"]
    new["main_tex"] = {"path": "main.tex", "sha256": sha(main_path)}
    new["layout"] = dict(current_manifest.get("layout") or {})
    new["layout"]["chapter_start_policy"] = (
        "first feature on new page; later chapters use Needspace(0.45 textheight)"
    )
    new["layout"]["final_synthesis_start_policy"] = "Needspace(0.55 textheight)"
    new["layout"]["references_start_policy"] = (
        "continue after final synthesis without forced clearpage"
    )
    new["layout_revision"] = {
        "from_source_version": current_manifest.get("source_version"),
        "reader_content_changed": False,
        "new_external_evidence": False,
        "adaptive_chapter_starts": True,
        "forced_bibliography_clearpage": False,
        "final_synthesis_subsection_needspace_baselines": 5,
    }
    new["final_synthesis"] = final_info
    new["final_synthesis"]["tex_sha256"] = sha(final_path)
    new["final_synthesis"]["layout_only_revision"] = True
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
        "layout_mode": "balanced-multicol-adaptive-spacing",
        "layout_revision_sha256": sha(marker_path),
    }
    state["provenance"].pop("latex_build", None)
    state["provenance"]["reader_layout_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": sha(marker_path),
        "reason": (
            "Human Visual Review requested more relaxed placement; remove avoidable blank "
            "areas at chapter and reference boundaries without changing reader content."
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
        "reader_content_changed": False,
        "new_external_evidence": False,
        "lifecycle_state": state["lifecycle_state"],
        "latex_build_gate": state["gates"]["latex_build"],
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
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
