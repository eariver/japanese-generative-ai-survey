#!/usr/bin/env python3
"""Apply Annual Publication Preview review repairs while preserving chronology narrative.

This wrapper keeps the evidence-closed generic Annual review sequence, but hardens two reader-facing
contracts exposed by SP-2020-Y review:

* #272: the accepted Q1-Q4 Annual chronology narrative is byte-preserved and a separate, compact,
  date-ordered objective event index is appended after it. Every dated event maps to a bibliography
  source by exact preserved locator; no date is invented.
* #122: the TOC remains section-level and is rendered compactly so a small tail of chapter entries
  does not create a low-density continuation page.

The other ordered repairs remain delegated unchanged: #54 reader taxonomy/date binding, #78/#140
actual source titles and reference-note consolidation, and #271 zero-card Technical Notes suppression.
No external Evidence is introduced and accepted Article Draft claims remain immutable.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from scripts import revise_special_annual_review_sequence as common
from scripts import revise_special_annual_review_sequence_generic as base

_CONTRACT = "ANNUAL_REVIEW_PRESERVE_NARRATIVE_OBJECTIVE_INDEX_COMPACT_TOC_V2"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def step_272(
    repo_root: Path,
    out: Path,
    state: dict[str, Any],
    manifest: dict[str, Any],
) -> tuple[dict[str, Any], dict[str, str]]:
    chronology, _ = common.load_chronology(repo_root, state)
    chronology = copy.deepcopy(chronology)
    refs = out / str((manifest.get("references") or {}).get("path") or "references.bib")
    url_keys, added = common.append_chronology_refs(refs, chronology)

    article = next(
        (item for item in (manifest.get("articles") or []) if item.get("package_id") == "annual-chronology"),
        None,
    )
    if not isinstance(article, dict):
        raise ValueError("#272 annual chronology article not found")
    narrative_rel = str(article.get("layout_body_path") or "")
    narrative_path = out / narrative_rel
    if not narrative_rel or not narrative_path.is_file():
        raise ValueError("#272 annual chronology narrative body missing")
    narrative_sha_before = sha(narrative_path)

    index_rel = "layout-bodies/annual-chronology-objective-index.tex"
    index_path = out / index_rel
    if index_path.exists():
        raise ValueError(f"#272 objective chronology index already exists: {index_rel}")
    index_text = base.render_chronology(chronology, url_keys)
    index_path.write_text(index_text, encoding="utf-8")

    # Append the objective index after the preserved narrative's local multicols block.  Do not
    # replace the narrative itself: #272 requires both the interpretive Q1-Q4 reading and the
    # source-mapped objective event index.
    main_path = out / "main.tex"
    main_text = main_path.read_text(encoding="utf-8")
    narrative_input = r"\input{" + Path(narrative_rel).with_suffix("").as_posix() + "}"
    anchor = narrative_input + "\n" + r"\end{multicols}"
    if main_text.count(anchor) != 1:
        raise ValueError(f"#272 expected exactly one Annual chronology narrative anchor, found {main_text.count(anchor)}")
    index_input = r"\input{" + Path(index_rel).with_suffix("").as_posix() + "}"
    replacement = (
        anchor
        + "\n"
        + r"\medskip"
        + "\n"
        + r"\subsection*{Objective event index}"
        + "\n"
        + index_input
    )
    main_text = main_text.replace(anchor, replacement, 1)
    if main_text.count(index_input) != 1:
        raise ValueError("#272 objective chronology index input was not materialized exactly once")
    main_path.write_text(main_text, encoding="utf-8")

    if sha(narrative_path) != narrative_sha_before:
        raise ValueError("#272 Annual chronology Q1-Q4 narrative changed unexpectedly")

    count = len(chronology.get("events") or [])
    article["chronology_objective_index_path"] = index_rel
    article["chronology_objective_index_sha256"] = sha(index_path)
    article["chronology_objective_index_event_count"] = count
    annual = dict(manifest.get("annual_chronology") or {})
    annual.update(
        {
            "objective_index_path": index_rel,
            "objective_index_sha256": sha(index_path),
            "objective_index_event_count": count,
            "narrative_preserved": True,
            "narrative_path": narrative_rel,
            "narrative_sha256": narrative_sha_before,
        }
    )
    manifest["annual_chronology"] = annual
    manifest["derivation"] = (
        f"#272 Annual repair: the accepted Q1-Q4 chronology narrative is byte-preserved and followed "
        f"by a separate objective index of all {count} accepted dated events. Each event carries a "
        "bibliography citation bound by exact preserved source locator; missing bibliography entries "
        "are added only from existing accepted chronology metadata."
    )
    manifest["issue_272"] = {
        "dated_event_count": count,
        "cited_event_count": count,
        "chronology_only_references_added": added,
        "unresolved_dates_preserved": len(chronology.get("unresolved_dates") or chronology.get("unresolved") or []),
        "q1_q4_narrative_preserved": True,
        "narrative_sha256": narrative_sha_before,
        "objective_index_path": index_rel,
        "objective_index_sha256": sha(index_path),
    }
    ref_by_locator = {
        str(event.get("locator") or ""): str(event.get("reference_key") or "")
        for event in chronology.get("events") or []
    }
    return manifest["issue_272"], ref_by_locator


def step_122(out: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    front_rel = str((manifest.get("frontmatter") or {}).get("path") or "sections/00-frontmatter.tex")
    front = out / front_rel
    text = front.read_text(encoding="utf-8")
    text = re.sub(r"\\setcounter\{tocdepth\}\{\d+\}\s*", "", text)
    token = r"\tableofcontents"
    if text.count(token) != 1:
        raise ValueError(f"#122 expected exactly one tableofcontents anchor, found {text.count(token)}")
    compact = (
        r"\setcounter{tocdepth}{1}"
        + "\n"
        + r"\begingroup"
        + "\n"
        + r"\footnotesize"
        + "\n"
        + r"\setlength{\parskip}{0pt}"
        + "\n"
        + token
        + "\n"
        + r"\endgroup"
    )
    text = text.replace(token, compact, 1)
    front.write_text(text, encoding="utf-8")

    manifest["layout"] = dict(manifest.get("layout") or {})
    manifest["layout"]["toc_depth"] = "section"
    manifest["layout"]["toc_render_size"] = "footnotesize"
    manifest["derivation"] = (
        "#122 Annual repair: publication TOC is section-level and rendered footnotesize with zero "
        "paragraph spacing, preventing a low-density continuation page without deleting article content."
    )
    manifest["issue_122"] = {
        "toc_depth": 1,
        "toc_render_size": "footnotesize",
        "theme_at_a_glance_toc_entries_visible": 0,
        "compact_rendering": True,
        "page_count_padding_added": False,
    }
    return manifest["issue_122"]


def build(repo_root: Path, special_slug: str, issue_id: str, parent_source_version: str) -> dict[str, Any]:
    old_272 = base.step_272
    old_122 = base.step_122
    base.step_272 = step_272
    base.step_122 = step_122
    try:
        result = base.build(repo_root, special_slug, issue_id, parent_source_version)
    finally:
        base.step_272 = old_272
        base.step_122 = old_122
    result = dict(result)
    result["annual_review_sequence_contract"] = _CONTRACT
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--parent-source-version", required=True)
    args = parser.parse_args()
    print(
        json.dumps(
            build(Path(args.repo_root), args.special_slug, args.issue_id, args.parent_source_version),
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
