#!/usr/bin/env python3
"""Create an immutable Special revision that prevents dense Theme tables from entering the footer.

Publication Preview Theme-at-a-glance tables are intentionally compact and use ``tabularx``.
Because ``tabularx`` is an unbreakable box, a high-cardinality theme can exceed the text height
and overlap the page footer even when the ordinary TeX log gate is otherwise clean.  This
layout-only repair copies the current validated source revision and changes only the font size
inside Theme-at-a-glance tables whose data-row count crosses an explicit marker threshold.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
from copy import deepcopy
from pathlib import Path
from typing import Any


THEME_BLOCK_RE = re.compile(
    r"(?P<prefix>\\subsection\*\{Theme at a glance\}.*?\\begin\{center\}\s*)"
    r"(?P<size>\\footnotesize|\\scriptsize)"
    r"(?P<table>\s*\\begin\{tabularx\}.*?\\end\{tabularx\}\s*\\end\{center\}\s*\\normalsize)",
    re.DOTALL,
)
ROW_RE = re.compile(r"\\\\\s*$")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _theme_data_rows(table_text: str) -> int:
    if r"\midrule" not in table_text or r"\bottomrule" not in table_text:
        raise ValueError("Theme at a glance table lacks midrule/bottomrule boundaries")
    body = table_text.split(r"\midrule", 1)[1].split(r"\bottomrule", 1)[0]
    return sum(1 for line in body.splitlines() if ROW_RE.search(line.rstrip()))


def densify_theme_tables(text: str, min_rows: int) -> tuple[str, int, list[int]]:
    """Use scriptsize for Theme tables at or above ``min_rows``; return change metadata."""
    if min_rows < 1:
        raise ValueError("min_rows must be positive")
    changed = 0
    row_counts: list[int] = []

    def replace(match: re.Match[str]) -> str:
        nonlocal changed
        rows = _theme_data_rows(match.group("table"))
        row_counts.append(rows)
        size = match.group("size")
        if rows >= min_rows and size != r"\scriptsize":
            size = r"\scriptsize"
            changed += 1
        return match.group("prefix") + size + match.group("table")

    revised = THEME_BLOCK_RE.sub(replace, text)
    return revised, changed, row_counts


def _preserved_digest(source_dir: Path, info: Any, *, default_path: str = "") -> tuple[str, str] | None:
    if not isinstance(info, dict):
        return None
    rel = str(info.get("path") or default_path)
    expected = str(info.get("sha256") or "")
    if not rel or not expected:
        return None
    path = source_dir / rel
    if not path.is_file() or sha(path) != expected:
        raise ValueError(f"preserved source digest mismatch before dense-table repair: {rel}")
    return rel, expected


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = load_json(marker_path)
    if marker.get("issue_id") != issue_id or marker.get("revision") != source_version:
        raise ValueError("dense Theme-table layout marker mismatch")
    changes = marker.get("layout_changes") or {}
    if changes.get("dense_theme_table_font_guard") is not True:
        raise ValueError("layout marker does not request dense Theme-table font guard")
    min_rows = int(changes.get("theme_table_scriptsize_min_rows") or 20)
    constraints = marker.get("constraints") or {}
    if constraints.get("new_external_evidence_allowed") is not False:
        raise ValueError("dense-table repair must forbid new external Evidence")
    if constraints.get("selected_evidence_only") is not True:
        raise ValueError("dense-table repair must remain selected-Evidence-only")
    if constraints.get("accepted_article_claims_changed") is not False:
        raise ValueError("dense-table repair must preserve accepted article claims")
    if constraints.get("evidence_cards_mutated") is not False:
        raise ValueError("dense-table repair must not mutate Evidence cards")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE":
        raise ValueError("dense-table repair requires RELEASE_CANDIDATE")
    if gates.get("latex_build") != "passed":
        raise ValueError("dense-table repair requires a successful prior PDF build")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("dense-table repair requires Visual Review and Freeze pending")

    current = deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    current_manifest_path = repo_root / str(current.get("path") or "")
    if not current_manifest_path.is_file() or sha(current_manifest_path) != str(current.get("sha256") or ""):
        raise ValueError("current validated source manifest digest mismatch")
    current_manifest = load_json(current_manifest_path)
    current_dir = current_manifest_path.parent

    preserved: list[tuple[str, str]] = []
    for key, default in (("main_tex", "main.tex"), ("frontmatter", ""), ("references", ""), ("final_synthesis", "")):
        item = _preserved_digest(current_dir, current_manifest.get(key), default_path=default)
        if item:
            preserved.append(item)
    for record in current_manifest.get("theme_synthesis") or []:
        item = _preserved_digest(current_dir, record)
        if item:
            preserved.append(item)
    for article in current_manifest.get("articles") or []:
        if not isinstance(article, dict):
            raise ValueError("malformed article record")
        rel = str(article.get("article_section_path") or "")
        expected = str(article.get("article_section_sha256") or "")
        if not rel or not expected or not (current_dir / rel).is_file() or sha(current_dir / rel) != expected:
            raise ValueError(f"accepted article section digest mismatch: {rel}")
        preserved.append((rel, expected))

    output_dir = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    if output_dir.exists():
        raise ValueError(f"source revision already exists: {output_dir}")
    shutil.copytree(current_dir, output_dir)
    new_manifest = deepcopy(current_manifest)
    new_manifest["source_version"] = source_version
    new_manifest["status"] = "VALIDATED_DENSE_THEME_TABLE_LAYOUT_REVISION"
    new_manifest["derivation"] = (
        "Publication Preview layout-only repair derived from the prior validated source. "
        "Dense Theme-at-a-glance tables are reduced from footnotesize to scriptsize only when "
        "their row count reaches the marker threshold; Evidence, chronology, article claims, "
        "Technical Note facts, source URLs, and table rows remain unchanged."
    )
    new_manifest["basis"] = dict(current_manifest.get("basis") or {})
    new_manifest["basis"]["previous_source_manifest_path"] = current["path"]
    new_manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]

    changed_files = 0
    changed_tables = 0
    max_theme_rows = 0
    dense_paths: list[str] = []
    for article in new_manifest.get("articles") or []:
        if not isinstance(article, dict):
            continue
        rel = str(article.get("technical_notes_path") or "")
        if not rel:
            continue
        path = output_dir / rel
        expected = str(article.get("technical_notes_sha256") or "")
        if not path.is_file() or (expected and sha(path) != expected):
            raise ValueError(f"Technical Notes digest mismatch before dense-table repair: {rel}")
        before = path.read_text(encoding="utf-8")
        after, local_changed, row_counts = densify_theme_tables(before, min_rows)
        if row_counts:
            max_theme_rows = max(max_theme_rows, max(row_counts))
        if local_changed:
            # The only permitted byte change is the local font-size token inside the Theme table.
            if after.replace(r"\scriptsize", r"\footnotesize") != before.replace(r"\scriptsize", r"\footnotesize"):
                raise ValueError(f"dense-table repair changed non-font Technical Notes content: {rel}")
            path.write_text(after, encoding="utf-8")
            changed_files += 1
            changed_tables += local_changed
            dense_paths.append(rel)
        article["technical_notes_sha256"] = sha(path)

    if changed_tables < 1:
        raise ValueError(
            f"dense Theme-table marker requested a repair but no table reached threshold min_rows={min_rows}"
        )

    for rel, expected in preserved:
        if sha(output_dir / rel) != expected:
            raise ValueError(f"protected source changed during dense-table repair: {rel}")

    new_manifest["layout"] = dict(current_manifest.get("layout") or {})
    new_manifest["layout"]["theme_at_a_glance_dense_table_policy"] = (
        f"scriptsize for unbreakable Theme tables with >= {min_rows} data rows; row/content identity preserved"
    )
    new_manifest["layout_revision"] = {
        "from_source_version": current_manifest.get("source_version"),
        "dense_theme_table_font_guard": True,
        "theme_table_scriptsize_min_rows": min_rows,
        "dense_theme_table_count": changed_tables,
        "dense_theme_table_files": dense_paths,
        "max_theme_table_rows": max_theme_rows,
        "reader_content_changed": False,
        "new_external_evidence": False,
        "selected_evidence_only": True,
        "accepted_article_sections_changed": False,
        "technical_notes_content_changed": False,
        "technical_notes_layout_changed": True,
        "theme_synthesis_changed": False,
        "bibliography_data_changed": False,
        "main_tex_changed": False,
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
        "reason": str(marker.get("reason") or "Prevent dense Theme-at-a-glance tables from entering the footer."),
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
        "theme_table_scriptsize_min_rows": min_rows,
        "dense_theme_table_count": changed_tables,
        "dense_theme_table_files": dense_paths,
        "max_theme_table_rows": max_theme_rows,
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
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
