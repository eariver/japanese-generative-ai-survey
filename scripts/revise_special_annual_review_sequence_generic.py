#!/usr/bin/env python3
"""Apply evidence-closed Annual Publication Preview review repairs without year-specific counts.

This is the reusable counterpart of revise_special_annual_review_sequence.py. It preserves the
validated Annual source graph and chronology identities while parameterizing source versions,
Technical Notes cardinality and chronology cardinality from the edition being repaired.

Ordered steps implemented here:
  54       -> reader taxonomy + objective card chronology
  78-140   -> source titles + compact non-repeating References
  271      -> suppress zero-card Technical Notes wrappers
  272      -> event-level Detailed Chronology -> bibliography source mapping
  122      -> section-level TOC

Issue #139/#191 source-specific Technical Notes hardening is intentionally run before this sequence
through revise_special_annual_source_specific_notes_v5.py.
"""
from __future__ import annotations

import argparse
import copy
import json
import re
from pathlib import Path
from typing import Any

from scripts import revise_special_annual_review_sequence as base


NOTE_RE = base.NOTE_RE
RAW_ENUM_RE = base.RAW_ENUM_RE


def configure_versions(parent: str, prefix: str = "v0") -> dict[str, tuple[str, str, list[int]]]:
    m = re.fullmatch(r"v(\d+)\.(\d+)", parent)
    if not m:
        raise ValueError(f"unsupported source version: {parent}")
    major, minor = int(m.group(1)), int(m.group(2))
    def v(offset: int) -> str:
        return f"v{major}.{minor + offset}"
    return {
        "54": (v(0), v(1), [54]),
        "78-140": (v(1), v(2), [78, 140]),
        "271": (v(2), v(3), [271]),
        "272": (v(3), v(4), [272]),
        "122": (v(4), v(5), [122]),
    }


def all_rendered_notes(out: Path, manifest: dict[str, Any]) -> str:
    chunks: list[str] = []
    for article in manifest.get("articles") or []:
        rel = str(article.get("technical_notes_path") or "")
        if rel and (out / rel).is_file():
            chunks.append((out / rel).read_text(encoding="utf-8"))
    return "\n".join(chunks)


def step_54(repo_root: Path, out: Path, state: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    chrono, _ = base.load_chronology(repo_root, state)
    locator_dates: dict[str, list[str]] = {}
    for event in chrono.get("events") or []:
        locator = str(event.get("locator") or "").strip()
        date = str(event.get("date") or "").strip()
        if locator and date:
            locator_dates.setdefault(locator, []).append(date)

    cards = 0
    no_objective_date: list[str] = []
    changed = 0
    for article in manifest.get("articles") or []:
        rel = str(article.get("technical_notes_path") or "")
        if not rel or not (out / rel).is_file():
            continue
        path = out / rel
        original = path.read_text(encoding="utf-8")
        revised, card_changed, missing = base.note_card_dates(original, locator_dates)
        path.write_text(revised, encoding="utf-8")
        cards += len(NOTE_RE.findall(revised))
        changed += card_changed
        no_objective_date.extend(missing)

    expected = int(manifest.get("evidence_record_count") or 0)
    if cards != expected:
        raise ValueError(f"#54 expected {expected} Technical Notes cards, found {cards}")
    rendered = all_rendered_notes(out, manifest)
    if "時系列 & —" in rendered or " & PRODUCT & " in rendered:
        raise ValueError("#54 reader-facing taxonomy/chronology placeholder regression remains")
    raw = sorted(set(RAW_ENUM_RE.findall(rendered)))
    raw = [x for x in raw if x not in {"URL"}]
    if raw:
        raise ValueError(f"#54 raw reader-facing enum findings remain: {raw[:10]}")

    manifest["derivation"] = (
        "#54 Annual repair: Technical Notes chronology is bound by exact preserved source URL to "
        "accepted objective chronology dates when available; reader taxonomy is normalized without "
        "changing provenance enums. Cards without a matching material chronology event are labeled "
        "年表対象日付なし rather than assigned an invented date."
    )
    manifest["issue_54"] = {
        "card_count": cards,
        "cards_changed": changed,
        "objective_date_bound_cards": cards - len(no_objective_date),
        "cards_without_material_chronology_event": len(no_objective_date),
        "invented_dates": 0,
        "raw_product_findings": 0,
    }
    return manifest["issue_54"]


def step_271(out: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    main = out / "main.tex"
    text = main.read_text(encoding="utf-8")
    suppressed: list[str] = []
    for article in manifest.get("articles") or []:
        if int(article.get("evidence_record_count") or 0) != 0:
            continue
        rel = str(article.get("technical_notes_path") or "")
        if not rel:
            continue
        token = rf"\input{{{Path(rel).with_suffix('').as_posix()}}}"
        if token in text:
            text = text.replace(token, "% zero-card Technical Notes suppressed by #271", 1)
            suppressed.append(str(article.get("package_id") or rel))
        article["technical_notes_reader_facing"] = False
        article["technical_notes_suppressed_empty"] = True
    if not suppressed:
        raise ValueError("#271 found no rendered zero-card Technical Notes wrapper to suppress")
    text_check = text
    for package_id in suppressed:
        article = next(a for a in manifest.get("articles") or [] if str(a.get("package_id")) == package_id)
        rel = str(article.get("technical_notes_path") or "")
        token = rf"\input{{{Path(rel).with_suffix('').as_posix()}}}"
        if token in text_check:
            raise ValueError(f"#271 zero-card Technical Notes input remains: {package_id}")
    main.write_text(text, encoding="utf-8")
    manifest["derivation"] = (
        "#271 Annual repair: zero-card Technical Notes wrappers are not rendered; the associated "
        "Annual narrative/chronology body remains unchanged."
    )
    manifest["issue_271"] = {
        "suppressed_zero_card_packages": suppressed,
        "suppressed_count": len(suppressed),
        "empty_theme_tables_rendered": 0,
    }
    return manifest["issue_271"]


def render_chronology(payload: dict[str, Any], url_keys: dict[str, str]) -> str:
    lines = [
        "% Generated from accepted annual Screening chronology metadata with #272 source mapping. Do not hand-edit.",
        r"\noindent 日付は一次資料または論文メタデータで確認できた公開時点を採用し、後年の提供状態を遡及して補わない。各event末尾の参照番号から対応一次資料へ追跡できる。",
        r"\par\medskip",
    ]
    last_month: int | None = None
    cited = 0
    for event in payload.get("events") or []:
        date = str(event.get("date") or "")
        if len(date) < 7:
            raise ValueError(f"#272 invalid accepted chronology date: {date!r}")
        month = int(date[5:7])
        if month != last_month:
            lines.extend([r"\medskip", rf"\noindent\textbf{{{month}月}}\par", r"\smallskip"])
            last_month = month
        url = str(event.get("locator") or "").strip()
        key = url_keys.get(url)
        if not key:
            raise ValueError(f"#272 bibliography key missing for chronology locator: {url}")
        event["reference_key"] = key
        title = base.tex_escape(str(event.get("title") or ""))
        lines.extend([
            rf"\noindent\textbf{{{date}}}\par",
            rf"{{\raggedright {title}\,\cite{{{key}}}\par}}",
            r"\smallskip",
        ])
        cited += 1
    unresolved = payload.get("unresolved_dates") or payload.get("unresolved") or []
    lines.extend([
        r"\medskip",
        r"\begin{claimboundary}[日付精度の境界]",
        f"公開日の精度を一次記録から確定できなかった retained record が {len(unresolved)} 件ある。Chronology では推測日を補わず、監査記録に未解決として残す。",
        r"\end{claimboundary}",
        "",
    ])
    expected = len(payload.get("events") or [])
    if cited != expected:
        raise ValueError(f"#272 expected {expected} cited events, got {cited}")
    return "\n".join(lines)


def step_272(repo_root: Path, out: Path, state: dict[str, Any], manifest: dict[str, Any]) -> tuple[dict[str, Any], dict[str, str]]:
    chrono, _ = base.load_chronology(repo_root, state)
    chrono = copy.deepcopy(chrono)
    refs = out / str((manifest.get("references") or {}).get("path") or "references.bib")
    url_keys, added = base.append_chronology_refs(refs, chrono)
    body_rel = ""
    for article in manifest.get("articles") or []:
        if article.get("package_id") == "annual-chronology":
            body_rel = str(article.get("layout_body_path") or "layout-bodies/annual-chronology.tex")
            break
    if not body_rel:
        raise ValueError("#272 annual chronology layout body not found")
    (out / body_rel).write_text(render_chronology(chrono, url_keys), encoding="utf-8")
    count = len(chrono.get("events") or [])
    manifest["derivation"] = (
        f"#272 Annual repair: all {count} material chronology events carry bibliography citations "
        "bound by exact preserved source locator; missing bibliography entries are added from "
        "existing accepted chronology metadata only."
    )
    manifest["issue_272"] = {
        "dated_event_count": count,
        "cited_event_count": count,
        "chronology_only_references_added": added,
        "unresolved_dates_preserved": len(chrono.get("unresolved_dates") or chrono.get("unresolved") or []),
    }
    ref_by_locator = {str(e.get("locator") or ""): str(e.get("reference_key") or "") for e in chrono.get("events") or []}
    return manifest["issue_272"], ref_by_locator


def step_122(out: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    front = out / str((manifest.get("frontmatter") or {}).get("path") or "sections/00-frontmatter.tex")
    text = front.read_text(encoding="utf-8")
    text = re.sub(r"\\setcounter\{tocdepth\}\{\d+\}\s*", "", text)
    if r"\tableofcontents" not in text:
        raise ValueError("#122 tableofcontents anchor not found")
    text = text.replace(r"\tableofcontents", r"\setcounter{tocdepth}{1}" + "\n" + r"\tableofcontents", 1)
    front.write_text(text, encoding="utf-8")
    manifest["layout"] = dict(manifest.get("layout") or {})
    manifest["layout"]["toc_depth"] = "section"
    manifest["derivation"] = (
        "#122 Annual repair: publication TOC is section-level, so repeated Theme at a glance "
        "subentries remain navigable in the article but are omitted from the frontmatter TOC."
    )
    manifest["issue_122"] = {
        "toc_depth": 1,
        "theme_at_a_glance_toc_entries_visible": 0,
        "page_count_padding_added": False,
    }
    return manifest["issue_122"]


def build_step(repo_root: Path, special_slug: str, issue_id: str, step: str) -> dict[str, Any]:
    state_path, out, state, current, manifest, _ = base.clone_revision(repo_root, special_slug, issue_id, step)
    _expected, version, _issues = base.VERSIONS[step]
    chronology_ref_map: dict[str, str] | None = None
    if step == "54":
        audit = step_54(repo_root, out, state, manifest)
    elif step == "78-140":
        audit = base.step_78_140(repo_root, out, state, manifest)
    elif step == "271":
        audit = step_271(out, manifest)
    elif step == "272":
        audit, chronology_ref_map = step_272(repo_root, out, state, manifest)
    elif step == "122":
        audit = step_122(out, manifest)
    else:
        raise ValueError(step)

    def mutate_chronology(payload: dict[str, Any]) -> None:
        if chronology_ref_map is not None:
            for event in payload.get("events") or []:
                key = chronology_ref_map.get(str(event.get("locator") or ""))
                if not key:
                    raise ValueError("#272 missing reference key while copying chronology")
                event["reference_key"] = key

    before, _ = base.load_chronology(repo_root, state)
    before_count = len(before.get("events") or [])
    copied = base.copy_chronology(repo_root, issue_id, state, version, mutate=mutate_chronology)
    if len(copied.get("events") or []) != before_count:
        raise ValueError("Annual chronology count changed")
    result = base.finalize_revision(repo_root, issue_id, step, state_path, out, state, current, manifest)
    result["audit"] = audit
    return result


def build(repo_root: Path, special_slug: str, issue_id: str, parent_version: str) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    previous = base.VERSIONS
    base.VERSIONS = configure_versions(parent_version)
    try:
        results = [build_step(repo_root, special_slug, issue_id, step) for step in ("54", "78-140", "271", "272", "122")]
    finally:
        base.VERSIONS = previous
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "parent_source_version": parent_version,
        "steps": results,
        "final_source_version": results[-1]["source_version"],
        "new_external_evidence": False,
        "accepted_article_claims_changed": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--parent-source-version", required=True)
    args = parser.parse_args()
    print(json.dumps(build(Path(args.repo_root), args.special_slug, args.issue_id, args.parent_source_version), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
