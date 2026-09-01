#!/usr/bin/env python3
"""Apply ordered SP-2023-Y Annual Publication Preview review repairs.

This builder is deliberately evidence-closed.  It derives reader-facing fixes only from the
current validated Annual source, its immutable Draft Packages, the materialized accepted
Screening chronology, and preserved bibliography URLs.  It never fetches new sources or changes
accepted Article Draft claims / Selection / Architecture.

Ordered steps:
  54       -> reader taxonomy + objective card chronology
  78-140   -> source titles + compact non-repeating References
  271      -> suppress zero-card Technical Notes wrappers
  272      -> event-level Detailed Chronology -> bibliography source mapping
  122-55   -> section-level TOC + local card-tail pagination guards / relaxed chapter starts
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any

from scripts.revise_special_visual_review_repairs import source_title_map, enrich_bibliography_titles

VERSIONS = {
    "54": ("v0.5", "v0.6", [54]),
    "78-140": ("v0.6", "v0.7", [78, 140]),
    "271": ("v0.7", "v0.8", [271]),
    "272": ("v0.8", "v0.9", [272]),
    "122-55": ("v0.9", "v0.10", [122, 55]),
}
NOTE_RE = re.compile(r"\\begin\{technicalnote\}\{([^}]*)\}\{[^}]*\}.*?\\end\{technicalnote\}", re.DOTALL)
URL_RE = re.compile(r"\\url\{([^}]*)\}")
BIB_ENTRY_RE = re.compile(r"@online\{([^,]+),\n(.*?)\n\}", re.DOTALL)
BIB_URL_RE = re.compile(r"\n?\s*url\s*=\s*\{([^}]*)\},?")
BIB_NOTE_RE = re.compile(r"\n\s*note\s*=\s*\{Primary source used for chronology and technical verification\},?")
RAW_ENUM_RE = re.compile(r"\b(?:OTHER|PRODUCT|[A-Z][A-Z0-9]+_[A-Z0-9_]+)\b")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def tex_escape(value: str) -> str:
    table = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "#": r"\#", "_": r"\_", "{": r"\{", "}": r"\}"}
    return "".join(table.get(ch, ch) for ch in value)


def current_context(repo_root: Path, issue_id: str, expected_version: str) -> tuple[Path, dict[str, Any], dict[str, Any], Path]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    if state.get("lifecycle_state") != "VALIDATED_DRAFT":
        raise ValueError(f"ordered Annual repair requires VALIDATED_DRAFT, got {state.get('lifecycle_state')}")
    gates = state.get("gates") or {}
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("Annual repair requires Visual Review / Freeze pending")
    current = dict((state.get("provenance") or {}).get("validated_issue_source") or {})
    if current.get("source_version") != expected_version:
        raise ValueError(f"expected current source {expected_version}, got {current.get('source_version')}")
    manifest_path = repo_root / str(current.get("path") or "")
    if not manifest_path.is_file() or sha(manifest_path) != current.get("sha256"):
        raise ValueError("current validated source digest mismatch")
    return state_path, state, current, manifest_path


def clone_revision(repo_root: Path, special_slug: str, issue_id: str, step: str) -> tuple[Path, Path, dict[str, Any], dict[str, Any], dict[str, Any], Path]:
    expected, version, issues = VERSIONS[step]
    state_path, state, current, manifest_path = current_context(repo_root, issue_id, expected)
    current_manifest = load_json(manifest_path)
    out = repo_root / "surveys" / "special" / special_slug / "revisions" / version
    if out.exists():
        raise ValueError(f"revision already exists: {out}")
    shutil.copytree(manifest_path.parent, out)
    manifest = copy.deepcopy(current_manifest)
    manifest["source_version"] = version
    manifest["status"] = "VALIDATED_ANNUAL_ORDERED_REVIEW_REPAIR"
    manifest["basis"] = dict(manifest.get("basis") or {})
    manifest["basis"]["previous_source_manifest_path"] = current["path"]
    manifest["basis"]["previous_source_manifest_sha256"] = current["sha256"]
    repairs = list(manifest.get("ordered_review_repairs") or [])
    repairs.append({"step": step, "issue_refs": issues, "new_external_evidence": False, "article_claims_changed": False})
    manifest["ordered_review_repairs"] = repairs
    return state_path, out, state, current, manifest, manifest_path


def load_chronology(repo_root: Path, state: dict[str, Any]) -> tuple[dict[str, Any], Path]:
    info = dict((state.get("provenance") or {}).get("annual_chronology") or {})
    path = repo_root / str(info.get("path") or "")
    if not path.is_file() or sha(path) != info.get("sha256"):
        raise ValueError("annual chronology digest mismatch")
    payload = load_json(path)
    if len(payload.get("events") or []) != int(info.get("event_count") or -1):
        raise ValueError("annual chronology event count mismatch")
    return payload, path


def copy_chronology(repo_root: Path, issue_id: str, state: dict[str, Any], version: str, mutate=None) -> dict[str, Any]:
    payload, _ = load_chronology(repo_root, state)
    payload = copy.deepcopy(payload)
    before_dates = [(e.get("date"), e.get("title"), e.get("locator")) for e in payload.get("events") or []]
    before_unresolved = copy.deepcopy(payload.get("unresolved_dates") or payload.get("unresolved") or [])
    payload["source_version"] = version
    if mutate is not None:
        mutate(payload)
    after_dates = [(e.get("date"), e.get("title"), e.get("locator")) for e in payload.get("events") or []]
    if after_dates != before_dates:
        raise ValueError("ordered review repair must not alter chronology date/title/locator identity")
    if (payload.get("unresolved_dates") or payload.get("unresolved") or []) != before_unresolved:
        raise ValueError("ordered review repair must not alter unresolved chronology records")
    out = repo_root / "sources" / issue_id / "chronology" / f"annual-chronology-{version}.json"
    if out.exists():
        raise ValueError(f"chronology revision already exists: {out}")
    write_json(out, payload)
    previous = copy.deepcopy((state.get("provenance") or {}).get("annual_chronology") or {})
    state.setdefault("provenance_history", {}).setdefault("annual_chronology", []).append(previous)
    info = {
        "source_version": version,
        "path": out.relative_to(repo_root).as_posix(),
        "sha256": sha(out),
        "event_count": len(payload.get("events") or []),
        "unresolved_date_count": len(before_unresolved),
    }
    state.setdefault("provenance", {})["annual_chronology"] = info
    return payload


def refresh_manifest_hashes(out: Path, manifest: dict[str, Any]) -> None:
    main = out / "main.tex"
    front = out / str((manifest.get("frontmatter") or {}).get("path") or "sections/00-frontmatter.tex")
    refs = out / str((manifest.get("references") or {}).get("path") or "references.bib")
    manifest["main_tex"] = {"path": "main.tex", "sha256": sha(main)}
    manifest["frontmatter"] = {"path": front.relative_to(out).as_posix(), "sha256": sha(front)}
    manifest["references"] = {"path": refs.relative_to(out).as_posix(), "sha256": sha(refs)}
    for article in manifest.get("articles") or []:
        nrel = str(article.get("technical_notes_path") or "")
        if nrel and (out / nrel).is_file():
            article["technical_notes_sha256"] = sha(out / nrel)
        brel = str(article.get("layout_body_path") or "")
        if brel and (out / brel).is_file():
            article["layout_body_sha256"] = sha(out / brel)


def finalize_revision(repo_root: Path, issue_id: str, step: str, state_path: Path, out: Path, state: dict[str, Any], current: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    _, version, issues = VERSIONS[step]
    refresh_manifest_hashes(out, manifest)
    manifest_path = out / "source-manifest.json"
    write_json(manifest_path, manifest)
    manifest_sha = sha(manifest_path)
    state.setdefault("provenance_history", {}).setdefault("validated_issue_source", []).append(current)
    state["lifecycle_state"] = "VALIDATED_DRAFT"
    state["gates"]["latex_build"] = "pending"
    state["gates"]["visual_review"] = "pending"
    state["gates"]["freeze"] = "pending"
    state.setdefault("provenance", {})["validated_issue_source"] = {
        "path": manifest_path.relative_to(repo_root).as_posix(),
        "sha256": manifest_sha,
        "source_version": version,
        "layout_mode": "annual-ordered-publication-preview-repair",
    }
    state["provenance"].pop("latex_build", None)
    marker = repo_root / "sources" / issue_id / "editorial" / f"ordered-review-repair-{version}.json"
    write_json(marker, {
        "schema_version": "1.0", "issue_id": issue_id, "source_version": version,
        "step": step, "issue_refs": issues, "previous_source_version": current.get("source_version"),
        "previous_source_sha256": current.get("sha256"), "source_manifest_sha256": manifest_sha,
        "new_external_evidence": False, "article_claims_changed": False,
    })
    state["provenance"]["reader_layout_revision"] = {
        "source_version": version,
        "ordered_review_repair_path": marker.relative_to(repo_root).as_posix(),
        "ordered_review_repair_sha256": sha(marker),
        "issue_refs": issues,
    }
    write_json(state_path, state)
    return {"step": step, "source_version": version, "issue_refs": issues, "source_manifest": manifest_path.relative_to(repo_root).as_posix(), "source_manifest_sha256": manifest_sha}


def note_card_dates(text: str, locator_dates: dict[str, list[str]]) -> tuple[str, int, list[str]]:
    card_meta: dict[str, tuple[str, str]] = {}
    missing: list[str] = []
    changed = 0

    def transform(match: re.Match[str]) -> str:
        nonlocal changed
        title = match.group(1)
        block = match.group(0)
        urls = URL_RE.findall(block)
        dates = sorted({d for u in urls for d in locator_dates.get(u, [])})
        if not dates:
            missing.append(title)
            timeline = "年表対象日付なし"
        else:
            timeline = ", ".join(dates)
        type_match = re.search(r"種別\s*&\s*([^\\\n]+?)\s*\\\\", block)
        current_type = type_match.group(1).strip() if type_match else ""
        if title == "Adobe Firefly / Generative Fill":
            current_type = "製品"
        if title == "OpenAI 2023 alignment and agent-governance work":
            current_type = "安全性・ガバナンス"
        if title == "Anthropic Constitutional AI / Responsible Scaling Policy":
            current_type = "安全性・ガバナンス"
        current_type = {"PRODUCT": "製品", "OTHER": "公式情報"}.get(current_type, current_type)
        revised = re.sub(r"(種別\s*&\s*)[^\\\n]+?(\s*\\\\)", lambda m: m.group(1) + current_type + m.group(2), block, count=1)
        revised = re.sub(r"(時系列\s*&\s*)[^\\\n]+?(\s*\\\\)", lambda m: m.group(1) + timeline + m.group(2), revised, count=1)
        if revised != block:
            changed += 1
        card_meta[title] = (current_type, timeline)
        return revised

    text = NOTE_RE.sub(transform, text)
    lines = []
    for line in text.splitlines():
        parts = [x.strip() for x in line.split("&")]
        if len(parts) == 4 and parts[0] in card_meta:
            typ, timeline = card_meta[parts[0]]
            suffix = r" \\" if line.rstrip().endswith(r"\\") else ""
            line = f"{parts[0]} & {parts[1]} & {typ} & {timeline}{suffix}"
        lines.append(line)
    return "\n".join(lines) + ("\n" if text.endswith("\n") else ""), changed, missing


def step_54(repo_root: Path, out: Path, state: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    chrono, _ = load_chronology(repo_root, state)
    locator_dates: dict[str, list[str]] = {}
    for event in chrono.get("events") or []:
        locator_dates.setdefault(str(event.get("locator") or ""), []).append(str(event.get("date") or ""))
    cards = 0
    missing_all: list[str] = []
    for article in manifest.get("articles") or []:
        rel = str(article.get("technical_notes_path") or "")
        if not rel or not (out / rel).is_file():
            continue
        path = out / rel
        original = path.read_text(encoding="utf-8")
        revised, changed, missing = note_card_dates(original, locator_dates)
        cards += len(NOTE_RE.findall(revised))
        missing_all.extend(missing)
        path.write_text(revised, encoding="utf-8")
    if cards != 26:
        raise ValueError(f"#54 expected 26 Technical Notes cards, found {cards}")
    if missing_all:
        raise ValueError(f"#54 objective chronology binding missing for cards: {missing_all}")
    rendered = "\n".join((out / str(a.get("technical_notes_path"))).read_text(encoding="utf-8") for a in manifest.get("articles") or [] if a.get("technical_notes_path") and (out / str(a.get("technical_notes_path"))).is_file())
    if "時系列 & —" in rendered or " & PRODUCT & " in rendered or "安全性事象" in rendered:
        raise ValueError("#54 reader-facing taxonomy/chronology regression remains")
    manifest["derivation"] = "#54 Annual repair: Technical Notes chronology is bound by exact source URL to accepted objective chronology dates; reader taxonomy is normalized without changing provenance enums."
    manifest["issue_54"] = {"card_count": cards, "missing_objective_date_cards": 0, "multi_event_dates_sorted": True, "theme_detail_mapping_shared": True, "governance_taxonomy": "安全性・ガバナンス"}
    return manifest["issue_54"]


def chronology_title_map(payload: dict[str, Any]) -> dict[str, str]:
    return {str(e.get("locator") or ""): str(e.get("title") or "") for e in payload.get("events") or [] if e.get("locator") and e.get("title")}


def remove_reference_boilerplate(path: Path) -> int:
    text = path.read_text(encoding="utf-8")
    revised, count = BIB_NOTE_RE.subn("", text)
    path.write_text(revised, encoding="utf-8")
    return count


def compact_reference_main(main: Path) -> None:
    text = main.read_text(encoding="utf-8")
    old = r"\clearpage" + "\n" + r"\printbibliography[title={References / Source Notes}]"
    if old not in text:
        old = r"\printbibliography[title={References / Source Notes}]"
    replacement = (
        r"\Needspace{0.30\textheight}" + "\n" + r"\bigskip" + "\n"
        + r"\noindent{\small Referencesには本文・Detailed Chronologyの検証に用いた一次資料の識別情報とURLを掲載する。各entryに共通する用途説明はここに集約する。}\par" + "\n"
        + r"\smallskip" + "\n" + r"\printbibliography[title={References / Source Notes}]"
    )
    if old not in text:
        raise ValueError("#140 bibliography anchor not found")
    text = text.replace(old, replacement, 1)
    main.write_text(text, encoding="utf-8")


def step_78_140(repo_root: Path, out: Path, state: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    chrono, _ = load_chronology(repo_root, state)
    title_map = source_title_map(repo_root, manifest)
    title_map.update(chronology_title_map(chrono))
    refs = out / str((manifest.get("references") or {}).get("path") or "references.bib")
    changed, count = enrich_bibliography_titles(refs, title_map)
    boiler = remove_reference_boilerplate(refs)
    if re.search(r"title\s*=\s*\{Primary source \d+\}", refs.read_text(encoding="utf-8")):
        raise ValueError("#78 generic Primary source title remains")
    if "Primary source used for chronology and technical verification" in refs.read_text(encoding="utf-8"):
        raise ValueError("#140 repeated reference boilerplate remains")
    compact_reference_main(out / "main.tex")
    manifest["derivation"] = "#78/#140 Annual repair: bibliography titles are restored from pinned Evidence / chronology metadata and repeated per-entry purpose boilerplate is replaced by one section-level explanation."
    manifest["issue_78_140"] = {"bibliography_entry_count": count, "titles_enriched": changed, "repeated_notes_removed": boiler, "generic_title_findings": 0, "common_purpose_once": True}
    return manifest["issue_78_140"]


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
    if set(suppressed) != {"annual-chronology", "annual-synthesis"}:
        raise ValueError(f"#271 expected two empty Annual Technical Notes sections, suppressed={suppressed}")
    main.write_text(text, encoding="utf-8")
    manifest["derivation"] = "#271 Annual repair: zero-card Technical Notes wrappers are not rendered; chronology and annual synthesis narrative remain unchanged."
    manifest["issue_271"] = {"suppressed_zero_card_packages": suppressed, "empty_theme_tables_rendered": 0}
    return manifest["issue_271"]


def parse_bib_url_keys(text: str) -> dict[str, str]:
    result: dict[str, str] = {}
    for match in BIB_ENTRY_RE.finditer(text):
        key, body = match.group(1), match.group(2)
        u = BIB_URL_RE.search(body)
        if u:
            result[u.group(1).strip()] = key.strip()
    return result


def append_chronology_refs(refs: Path, chrono: dict[str, Any]) -> tuple[dict[str, str], int]:
    text = refs.read_text(encoding="utf-8")
    url_keys = parse_bib_url_keys(text)
    added = 0
    blocks: list[str] = []
    for event in chrono.get("events") or []:
        url = str(event.get("locator") or "").strip()
        if not url or url in url_keys:
            continue
        key = "chron-" + hashlib.sha256(url.encode("utf-8")).hexdigest()[:12]
        title = tex_escape(str(event.get("title") or url))
        blocks.append(f"@online{{{key},\n  title = {{{title}}},\n  url = {{{url}}},\n  urldate = {{2026-08-16}}\n}}\n")
        url_keys[url] = key
        added += 1
    if blocks:
        text = text.rstrip() + "\n\n" + "\n".join(blocks) + "\n"
        refs.write_text(text, encoding="utf-8")
    return url_keys, added


def render_chronology(payload: dict[str, Any], url_keys: dict[str, str]) -> str:
    lines = [
        "% Generated from accepted annual Screening chronology metadata with #272 source mapping. Do not hand-edit.",
        r"\noindent 日付は一次資料または論文メタデータで確認できた公開時点を採用し、後年の提供状態を遡及して補わない。各event末尾の参照番号から対応一次資料へ追跡できる。",
        r"\par\medskip",
    ]
    last_month = None
    cited = 0
    for event in payload.get("events") or []:
        date = str(event.get("date") or "")
        month = int(date[5:7])
        if month != last_month:
            lines.extend([r"\medskip", rf"\noindent\textbf{{{month}月}}\par", r"\smallskip"])
            last_month = month
        url = str(event.get("locator") or "")
        key = url_keys.get(url)
        if not key:
            raise ValueError(f"#272 bibliography key missing for chronology locator: {url}")
        event["reference_key"] = key
        title = tex_escape(str(event.get("title") or ""))
        lines.extend([rf"\noindent\textbf{{{date}}}\par", rf"{{\raggedright {title}\,\cite{{{key}}}\par}}", r"\smallskip"])
        cited += 1
    unresolved = payload.get("unresolved_dates") or payload.get("unresolved") or []
    lines.extend([
        r"\medskip",
        r"\begin{claimboundary}[日付精度の境界]",
        f"公開日の精度を一次記録から確定できなかった retained record が {len(unresolved)} 件ある。Chronology では推測日を補わず、監査記録に未解決として残す。",
        r"\end{claimboundary}",
        "",
    ])
    if cited != 75:
        raise ValueError(f"#272 expected 75 cited events, got {cited}")
    return "\n".join(lines)


def step_272(repo_root: Path, out: Path, state: dict[str, Any], manifest: dict[str, Any]) -> tuple[dict[str, Any], dict[str, str]]:
    chrono, _ = load_chronology(repo_root, state)
    chrono = copy.deepcopy(chrono)
    refs = out / str((manifest.get("references") or {}).get("path") or "references.bib")
    url_keys, added = append_chronology_refs(refs, chrono)
    body_rel = None
    for article in manifest.get("articles") or []:
        if article.get("package_id") == "annual-chronology":
            body_rel = str(article.get("layout_body_path") or "layout-bodies/annual-chronology.tex")
            break
    if not body_rel:
        raise ValueError("#272 annual chronology layout body not found")
    body = out / body_rel
    body.write_text(render_chronology(chrono, url_keys), encoding="utf-8")
    manifest["derivation"] = "#272 Annual repair: all 75 dated chronology events carry bibliography citations bound by exact preserved source locator; missing bibliography entries are added from existing accepted chronology metadata only."
    manifest["issue_272"] = {"dated_event_count": 75, "cited_event_count": 75, "chronology_only_references_added": added, "unresolved_dates_preserved": len(chrono.get("unresolved_dates") or chrono.get("unresolved") or [])}
    ref_by_locator = {str(e.get("locator") or ""): str(e.get("reference_key") or "") for e in chrono.get("events") or []}
    return manifest["issue_272"], ref_by_locator


def add_needspace_to_card(text: str, title: str) -> tuple[str, bool]:
    pattern = re.compile(r"(\\begin\{technicalnote\}\{" + re.escape(title) + r"\}\{[^}]*\}.*?)(\{\\bfseries 一次資料から整理したtechnical points\})", re.DOTALL)
    match = pattern.search(text)
    if not match:
        return text, False
    if r"\Needspace{0.35\textheight}" in match.group(0):
        return text, True
    replacement = match.group(1) + r"\Needspace{0.35\textheight}" + "\n" + match.group(2)
    return text[:match.start()] + replacement + text[match.end():], True


def relax_chapter_starts(main: Path) -> int:
    text = main.read_text(encoding="utf-8")
    token = "\\clearpage\n\\section{"
    parts = text.split(token)
    if len(parts) < 3:
        raise ValueError("#122/#55 expected multiple forced chapter starts")
    rebuilt = parts[0] + token + parts[1]
    replaced = 0
    for part in parts[2:]:
        rebuilt += "\\Needspace{0.45\\textheight}\n\\bigskip\n\\section{" + part
        replaced += 1
    main.write_text(rebuilt, encoding="utf-8")
    return replaced


def step_122_55(out: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    front = out / str((manifest.get("frontmatter") or {}).get("path") or "sections/00-frontmatter.tex")
    text = front.read_text(encoding="utf-8")
    if r"\setcounter{tocdepth}{1}" not in text:
        text = text.replace(r"\tableofcontents", r"\setcounter{tocdepth}{1}" + "\n" + r"\tableofcontents", 1)
    front.write_text(text, encoding="utf-8")
    grouped: list[str] = []
    for article in manifest.get("articles") or []:
        rel = str(article.get("technical_notes_path") or "")
        if not rel or not (out / rel).is_file():
            continue
        path = out / rel
        ntext = path.read_text(encoding="utf-8")
        for title in ("Lost in the Middle", "Qwen 2023 family"):
            revised, found = add_needspace_to_card(ntext, title)
            if found:
                ntext = revised
                grouped.append(title)
        path.write_text(ntext, encoding="utf-8")
    if set(grouped) != {"Lost in the Middle", "Qwen 2023 family"}:
        raise ValueError(f"#55 target cards not found: {grouped}")
    relaxed = relax_chapter_starts(out / "main.tex")
    manifest["layout"] = dict(manifest.get("layout") or {})
    manifest["layout"]["toc_depth"] = "section"
    manifest["layout"]["chapter_start_policy"] = "first feature new page; subsequent chapters Needspace(0.45 textheight)"
    manifest["derivation"] = "#122/#55 Annual repair: section-level TOC removes repeated Theme-at-a-glance subentries; problematic card technical tails receive local space guards and later chapter starts use Needspace rather than forced clearpages."
    manifest["issue_122_55"] = {"toc_depth": 1, "theme_at_a_glance_toc_entries_visible": 0, "guarded_card_titles": sorted(set(grouped)), "forced_chapter_clearpages_relaxed": relaxed}
    return manifest["issue_122_55"]


def build(repo_root: Path, special_slug: str, issue_id: str, step: str) -> dict[str, Any]:
    if step not in VERSIONS:
        raise ValueError(f"unsupported step: {step}")
    state_path, out, state, current, manifest, _ = clone_revision(repo_root, special_slug, issue_id, step)
    _, version, _ = VERSIONS[step]
    audit: dict[str, Any]
    chronology_ref_map: dict[str, str] | None = None
    if step == "54":
        audit = step_54(repo_root, out, state, manifest)
    elif step == "78-140":
        audit = step_78_140(repo_root, out, state, manifest)
    elif step == "271":
        audit = step_271(out, manifest)
    elif step == "272":
        audit, chronology_ref_map = step_272(repo_root, out, state, manifest)
    else:
        audit = step_122_55(out, manifest)

    def mutate_chronology(payload: dict[str, Any]) -> None:
        if chronology_ref_map is not None:
            for event in payload.get("events") or []:
                key = chronology_ref_map.get(str(event.get("locator") or ""))
                if not key:
                    raise ValueError("#272 missing reference key while copying chronology")
                event["reference_key"] = key

    copied = copy_chronology(repo_root, issue_id, state, version, mutate=mutate_chronology)
    if len(copied.get("events") or []) != 75:
        raise ValueError("Annual chronology count changed")
    result = finalize_revision(repo_root, issue_id, step, state_path, out, state, current, manifest)
    result["audit"] = audit
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--step", required=True, choices=sorted(VERSIONS))
    args = parser.parse_args()
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.step)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
