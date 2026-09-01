#!/usr/bin/env python3
"""Create an immutable final spacing recovery revision for a Special preview.

This pass is intentionally presentation-only.  It is used after a local-multicol
Special source has already undergone Visual Review repairs and typography recovery,
but the strict PDF gate still reports one or more narrow-column Underfull boxes or
the result falls just below the Special page-budget floor.  It may:

- increase only the top/bottom page margins while preserving column width; and
- render explicitly selected generated narrative paragraphs ragged-right.

Reader wording, Evidence, chronology, Technical Notes, bibliography data, accepted
Article Drafts, and all Human Gate semantics remain unchanged.
"""
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
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def wrap_ragged_paragraph(text: str, prefix: str) -> tuple[str, int]:
    """Wrap exactly one generated prose paragraph identified by a stable prefix."""
    lines = text.splitlines(keepends=True)
    hits = [i for i, line in enumerate(lines) if line.startswith(prefix)]
    if len(hits) != 1:
        raise ValueError(f"expected exactly one paragraph starting {prefix!r}, found {len(hits)}")
    index = hits[0]
    line = lines[index]
    ending = "\n" if line.endswith("\n") else ""
    body = line[:-1] if ending else line
    lines[index] = "\\begingroup\\raggedright\n" + body + "\n\\par\\endgroup" + ending
    return "".join(lines), 1


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("final spacing recovery marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("visual_review_final_spacing_recovery") is not True:
        raise ValueError("marker does not request visual_review_final_spacing_recovery")
    constraints = marker.get("constraints") or {}
    if constraints.get("new_external_evidence_allowed") is not False:
        raise ValueError("final spacing recovery must forbid new external Evidence")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("final spacing recovery must remain selected-Evidence-only")
    if constraints.get("reader_content_changed") is not False:
        raise ValueError("final spacing recovery must not change reader wording")

    vertical_margin_mm = float(changes.get("vertical_margin_mm", 27.0))
    if not 22.0 <= vertical_margin_mm <= 32.0:
        raise ValueError("vertical_margin_mm must remain within the conservative 22-32 mm range")
    ragged_specs = changes.get("ragged_paragraphs") or []
    if not isinstance(ragged_specs, list):
        raise ValueError("ragged_paragraphs must be an array")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "VALIDATED_DRAFT":
        raise ValueError("final spacing recovery requires VALIDATED_DRAFT after a failed preview gate")
    if gates.get("claim_and_chronology_validation") != "passed":
        raise ValueError("claim/chronology validation must remain passed")
    if gates.get("latex_build") != "pending":
        raise ValueError("final spacing recovery requires latex_build pending")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("Visual Review and Freeze must remain pending")

    current = dict(state.get("provenance", {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha(current_manifest_path) != current.get("sha256"):
        raise ValueError("current validated source manifest digest mismatch")
    current_manifest = load_json(current_manifest_path)
    current_layout = current_manifest.get("layout") or {}
    if "local balanced multicols" not in str(current_layout.get("body_mode") or ""):
        raise ValueError("final spacing recovery expects local balanced multicols source")
    current_layout_revision = current_manifest.get("layout_revision") or {}
    if current_layout_revision.get("visual_review_repairs") is not True:
        raise ValueError("final spacing recovery basis must preserve Visual Review repairs")
    if current_layout_revision.get("new_external_evidence") is not False:
        raise ValueError("final spacing recovery basis unexpectedly introduced external Evidence")

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(current_manifest_path.parent, output_dir)

    new_manifest = dict(current_manifest)
    articles = [dict(article) for article in current_manifest.get("articles") or []]
    new_manifest["articles"] = articles
    article_by_id = {str(article.get("package_id") or ""): article for article in articles}

    main_path = output_dir / str((new_manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_text = main_path.read_text(encoding="utf-8")
    geometry_re = re.compile(
        r"\\geometry\{(?:margin=22mm|left=22mm,right=22mm,"
        r"top=(?P<vertical>\d+(?:\.\d+)?)mm,bottom=(?P=vertical)mm),"
        r"headsep=5mm,footskip=10mm\}"
    )
    replacement = (
        r"\geometry{left=22mm,right=22mm,top=" + f"{vertical_margin_mm:g}" +
        r"mm,bottom=" + f"{vertical_margin_mm:g}" + r"mm,headsep=5mm,footskip=10mm}"
    )
    main_text, geometry_count = geometry_re.subn(lambda _m: replacement, main_text, count=1)
    if geometry_count != 1:
        raise ValueError(f"expected one Special-local geometry line, replaced {geometry_count}")
    main_path.write_text(main_text, encoding="utf-8")

    ragged_count = 0
    changed_bodies: list[str] = []
    for spec in ragged_specs:
        if not isinstance(spec, dict):
            raise ValueError("ragged paragraph specification must be an object")
        package_id = str(spec.get("package_id") or "")
        prefix = str(spec.get("prefix") or "")
        if not package_id or not prefix:
            raise ValueError("ragged paragraph specification requires package_id and prefix")
        article = article_by_id.get(package_id)
        if article is None:
            raise ValueError(f"unknown article package_id for ragged paragraph: {package_id}")
        body_rel = str(article.get("layout_body_path") or "")
        body_path = output_dir / body_rel
        expected = str(article.get("layout_body_sha256") or "")
        if not body_rel or not body_path.is_file() or (expected and sha(body_path) != expected):
            raise ValueError(f"{package_id}: layout body missing or digest mismatch")
        revised, count = wrap_ragged_paragraph(body_path.read_text(encoding="utf-8"), prefix)
        body_path.write_text(revised, encoding="utf-8")
        ragged_count += count
        changed_bodies.append(body_rel)
        article["layout_body_sha256"] = sha(body_path)
        article["layout_selective_paragraph_policy"] = "ragged-right for strict-log recovery only"

    new_manifest["source_version"] = source_version
    new_manifest["status"] = "VALIDATED_VISUAL_REVIEW_FINAL_SPACING_RECOVERY_REVISION"
    new_manifest["derivation"] = (
        "Presentation-only recovery of the prior local-multicol preview source. Top/bottom margins are "
        "slightly increased without narrowing columns, and only explicitly identified generated narrative "
        "paragraphs are rendered ragged-right to remove strict-log Underfull boxes. Reader wording, selected "
        "Evidence, chronology, Technical Notes, bibliography data, and accepted Article Draft semantics are unchanged."
    )
    new_manifest["basis"] = dict(current_manifest.get("basis") or {})
    new_manifest["basis"]["previous_source_manifest_path"] = current["path"]
    new_manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]
    new_manifest["main_tex"] = {"path": main_path.relative_to(output_dir).as_posix(), "sha256": sha(main_path)}
    new_manifest["layout"] = dict(current_layout)
    new_manifest["layout"].update(
        {
            "vertical_margin_mm": vertical_margin_mm,
            "column_width_changed": False,
            "final_spacing_recovery": True,
        }
    )
    new_manifest["layout_revision"] = dict(current_layout_revision)
    new_manifest["layout_revision"].update(
        {
            "from_source_version": current_manifest.get("source_version"),
            "visual_review_final_spacing_recovery": True,
            "reader_content_changed": False,
            "new_external_evidence": False,
            "vertical_margin_mm": vertical_margin_mm,
            "ragged_paragraph_count": ragged_count,
            "ragged_paragraph_files": changed_bodies,
            "technical_notes_changed": False,
            "references_changed": False,
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
        "layout_mode": "balanced-local-multicol-final-spacing-recovery",
        "layout_revision_sha256": sha(marker_path),
    }
    state["provenance"]["reader_layout_revision"] = {
        "source_version": source_version,
        "layout_revision_path": marker_path.relative_to(repo_root).as_posix(),
        "layout_revision_sha256": sha(marker_path),
        "reason": str(marker.get("reason") or "Recover strict log/page-budget gate without changing reader wording."),
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
        "vertical_margin_mm": vertical_margin_mm,
        "ragged_paragraph_count": ragged_count,
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
