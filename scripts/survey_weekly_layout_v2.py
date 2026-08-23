#!/usr/bin/env python3
"""Apply deterministic post-render repairs for Core v2 WEEKLY_MAGAZINE.

The semantic renderer intentionally owns wording and Evidence binding. This helper
first re-establishes bibliography metadata from exact accepted authority, then may
change only the page/column commands immediately before the approved Weekly
closing summary. Both transformed artifact SHAs are rebound into the validated
source manifest and auditable deterministic transform results are written.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from scripts import survey_production_v2 as core
from scripts import survey_weekly_bibliography_v2 as bibliography


SUMMARY_PATTERN = re.compile(
    r"\\clearpage\n\\onecolumn\n"
    r"(?P<section>\\section\{[^\n]*\}\n"
    r"\\label\{sec:issue-summary\}\n"
    r"\\sectionkicker\{WEEKLY SYNTHESIS\})"
)
REFERENCE_MARKER = (
    "\\clearpage\n"
    "\\onecolumn\n"
    "\\printbibliography[title={References / Source Notes}]"
)


def _safe_file(root: Path, raw: str, label: str) -> Path:
    path = core.repo_local_path(root, raw, label)
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"{label} missing or unsafe: {raw}")
    return path


def _rel(root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")


def compact_closing_summary(
    root: Path,
    main_tex_path: Path,
    manifest_path: Path,
) -> dict[str, Any]:
    root = root.resolve()
    main_tex_path = main_tex_path.resolve()
    manifest_path = manifest_path.resolve()
    main_tex_path.relative_to(root)
    manifest_path.relative_to(root)
    if main_tex_path.is_symlink() or not main_tex_path.is_file():
        raise ValueError("validated source missing or unsafe")
    if manifest_path.is_symlink() or not manifest_path.is_file():
        raise ValueError("validated source manifest missing or unsafe")

    manifest = core.load_json(manifest_path)
    rendered = manifest.get("rendered_source")
    if not isinstance(rendered, dict) or set(rendered) != {"path", "sha256"}:
        raise ValueError("validated source manifest rendered_source fields invalid")
    expected_rel = _rel(root, main_tex_path)
    if rendered.get("path") != expected_rel:
        raise ValueError("validated source manifest does not bind canonical main.tex path")

    old_sha = core.sha256_file(main_tex_path)
    if rendered.get("sha256") != old_sha:
        raise ValueError("validated source manifest main.tex SHA drift before layout transform")

    text = main_tex_path.read_text(encoding="utf-8")
    matches = list(SUMMARY_PATTERN.finditer(text))
    if len(matches) != 1:
        raise ValueError(
            "Weekly closing summary layout transform requires exactly one canonical summary boundary: "
            f"found {len(matches)}"
        )
    if text.count(REFERENCE_MARKER) != 1:
        raise ValueError("Weekly references boundary is not canonical")

    match = matches[0]
    replacement = "\\newpage\n" + match.group("section")
    transformed = text[: match.start()] + replacement + text[match.end() :]
    if transformed == text:
        raise ValueError("Weekly closing summary layout transform made no change")

    summary_pos = transformed.index("\\label{sec:issue-summary}")
    references_boundary_pos = transformed.index(REFERENCE_MARKER, summary_pos)
    if "\\onecolumn" in transformed[summary_pos:references_boundary_pos]:
        raise ValueError("Weekly closing summary must remain in two-column flow until references")

    main_tex_path.write_text(transformed, encoding="utf-8")
    new_sha = core.sha256_file(main_tex_path)
    if new_sha == old_sha:
        raise ValueError("Weekly closing summary layout transform did not change source SHA")

    manifest["rendered_source"]["sha256"] = new_sha
    core.write_json(manifest_path, manifest)

    quality_root = manifest_path.parent / "quality"
    quality_root.mkdir(parents=True, exist_ok=True)
    result_path = quality_root / "weekly-closing-summary-layout.json"
    if result_path.exists():
        raise ValueError(f"refusing existing Weekly layout transform result: {result_path}")
    result = {
        "schema_version": "2.0-rc1",
        "check_id": "WEEKLY_CLOSING_SUMMARY_LAYOUT",
        "status": "PASS",
        "issue_id": manifest.get("issue_id"),
        "source_path": expected_rel,
        "source_sha256_before": old_sha,
        "source_sha256_after": new_sha,
        "manifest_path": _rel(root, manifest_path),
        "manifest_sha256_after": core.sha256_file(manifest_path),
        "transformation": "FINAL_BODY_COLUMN_TO_WEEKLY_SYNTHESIS_COLUMN",
        "finding": (
            "The approved Weekly closing summary now begins in the next two-column body column; "
            "the one-column transition remains reserved for References / Source Notes."
        ),
    }
    core.write_json(result_path, result)
    result["result_path"] = _rel(root, result_path)
    result["result_sha256"] = core.sha256_file(result_path)
    return result


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--main-tex", required=True)
    ap.add_argument("--source-manifest", required=True)
    args = ap.parse_args()

    root = Path(args.repo_root).resolve()
    main_tex = _safe_file(root, args.main_tex, "validated source")
    manifest = _safe_file(root, args.source_manifest, "validated source manifest")
    bibliography_result = bibliography.rebuild_bibliography(root, manifest)
    result = compact_closing_summary(root, main_tex, manifest)
    result["bibliography_metadata"] = {
        "result_path": bibliography_result["result_path"],
        "result_sha256": bibliography_result["result_sha256"],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
