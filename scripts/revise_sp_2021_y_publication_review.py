#!/usr/bin/env python3
"""Apply the ordered SP-2021-Y Publication Preview review repairs.

This is a one-shot backfill adapter. It reuses the hardened Annual/Half-year repair
layers from current main, changes no accepted Evidence/Article Draft/Architecture,
and applies the requested review sequence as immutable source revisions:

  v0.3  #139 / #191   source-specific Technical Notes
  v0.4  #54           reader taxonomy + objective chronology binding
  v0.5  #153 / #272   suppress duplicate chronology cards + event citations
  v0.6  #78 / #140    bibliography titles + compact References
  v0.7  #122 / #55    section-level TOC + generic tail/chapter pagination policy
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from scripts import revise_special_annual_source_specific_notes as annual_base
from scripts import revise_special_annual_source_specific_notes_v5 as annual_v5
from scripts import revise_special_annual_review_sequence as seq_base
from scripts import revise_special_annual_review_sequence_generic as seq_generic
from scripts import special_technical_note_tail_policy as tail_policy


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


def with_versions(mapping: dict[str, tuple[str, str, list[int]]], fn):
    previous = seq_base.VERSIONS
    seq_base.VERSIONS = mapping
    try:
        return fn()
    finally:
        seq_base.VERSIONS = previous


def run_139(repo_root: Path, special_slug: str, issue_id: str) -> dict[str, Any]:
    # The merged Annual repair originated on SP-2023-Y. Broaden only its final
    # fail-closed generic detector so the same forbidden templates are rejected
    # for any Annual year, including the generic technical-record wording used by
    # SP-2021-Y. Extraction/binding itself remains the existing #191 stack.
    previous_generic = annual_base._GENERIC_RE
    annual_base._GENERIC_RE = re.compile(
        r"一次資料で「.+?」の\d{4}年における公開・リリースの経緯を確認できる。"
        r"|一次資料で「.+?」が\d{4}年の生成AI技術記録に含まれることを確認できる。"
        r"|技術内容、性能、アクセス、安全性に関する記述は、原著者・プロジェクトの主張として扱い、独立再現済みの結果とはみなさない。"
        r"|能力や性能に関する評価は、提供元・プロジェクト側の主張として扱う。"
        r"|一次資料で確認できる範囲の事実を記録しており",
    )
    try:
        return annual_v5.build(repo_root, special_slug, issue_id, "v0.3")
    finally:
        annual_base._GENERIC_RE = previous_generic


def run_54(repo_root: Path, special_slug: str, issue_id: str) -> dict[str, Any]:
    return with_versions(
        {"54": ("v0.3", "v0.4", [54])},
        lambda: seq_generic.build_step(repo_root, special_slug, issue_id, "54"),
    )


def suppress_chronology_notes(out: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    article = next((a for a in manifest.get("articles") or [] if a.get("package_id") == "annual-chronology"), None)
    if not article:
        raise ValueError("#153 annual-chronology article not found")
    rel = str(article.get("technical_notes_path") or "")
    if not rel or not (out / rel).is_file():
        raise ValueError("#153 chronology Technical Notes file missing")
    count = int(article.get("evidence_record_count") or 0)
    if count < 1:
        raise ValueError("#153 expected duplicate chronology Technical Notes cards")
    main = out / "main.tex"
    text = main.read_text(encoding="utf-8")
    token = rf"\input{{{Path(rel).with_suffix('').as_posix()}}}"
    if text.count(token) != 1:
        raise ValueError(f"#153 expected exactly one chronology Technical Notes input, found {text.count(token)}")
    text = text.replace(token, "% #153 duplicate annual chronology Technical Notes suppressed", 1)
    main.write_text(text, encoding="utf-8")
    article["technical_notes_reader_facing"] = False
    article["technical_notes_suppressed_duplicate"] = True
    article["technical_notes_suppressed_duplicate_card_count"] = count
    manifest["issue_153"] = {
        "chronology_technical_notes_suppressed": True,
        "suppressed_duplicate_card_count": count,
        "chronology_body_preserved": True,
        "evidence_records_preserved": True,
    }
    return manifest["issue_153"]


def run_153_272(repo_root: Path, special_slug: str, issue_id: str) -> dict[str, Any]:
    mapping = {"153-272": ("v0.4", "v0.5", [153, 272])}

    def inner() -> dict[str, Any]:
        state_path, out, state, current, manifest, _ = seq_base.clone_revision(
            repo_root, special_slug, issue_id, "153-272"
        )
        audit_153 = suppress_chronology_notes(out, manifest)
        audit_272, reference_map = seq_generic.step_272(repo_root, out, state, manifest)

        def mutate(payload: dict[str, Any]) -> None:
            for event in payload.get("events") or []:
                key = reference_map.get(str(event.get("locator") or ""))
                if not key:
                    raise ValueError("#272 missing reference key while copying chronology")
                event["reference_key"] = key

        before, _ = seq_base.load_chronology(repo_root, state)
        copied = seq_base.copy_chronology(repo_root, issue_id, state, "v0.5", mutate=mutate)
        if len(copied.get("events") or []) != len(before.get("events") or []):
            raise ValueError("#272 chronology count changed")
        result = seq_base.finalize_revision(
            repo_root, issue_id, "153-272", state_path, out, state, current, manifest
        )
        result["audit"] = {"issue_153": audit_153, "issue_272": audit_272}
        return result

    return with_versions(mapping, inner)


def ensure_needspace(main: Path) -> bool:
    text = main.read_text(encoding="utf-8")
    if r"\usepackage{needspace}" in text:
        return False
    anchor = r"\usepackage{multicol}"
    if anchor not in text:
        raise ValueError("needspace dependency insertion anchor missing")
    text = text.replace(anchor, anchor + "\n" + r"\usepackage{needspace}", 1)
    main.write_text(text, encoding="utf-8")
    return True


def run_78_140(repo_root: Path, special_slug: str, issue_id: str) -> dict[str, Any]:
    mapping = {"78-140": ("v0.5", "v0.6", [78, 140])}

    def inner() -> dict[str, Any]:
        state_path, out, state, current, manifest, _ = seq_base.clone_revision(
            repo_root, special_slug, issue_id, "78-140"
        )
        audit = seq_base.step_78_140(repo_root, out, state, manifest)
        dependency_added = ensure_needspace(out / "main.tex")
        before, _ = seq_base.load_chronology(repo_root, state)
        copied = seq_base.copy_chronology(repo_root, issue_id, state, "v0.6")
        if len(copied.get("events") or []) != len(before.get("events") or []):
            raise ValueError("#78/#140 chronology count changed")
        manifest["issue_78_140"]["needspace_dependency_added"] = dependency_added
        result = seq_base.finalize_revision(
            repo_root, issue_id, "78-140", state_path, out, state, current, manifest
        )
        result["audit"] = audit
        return result

    return with_versions(mapping, inner)


def apply_tail_policy(out: Path, manifest: dict[str, Any]) -> dict[str, Any]:
    cards = protected = added = 0
    unprotected: list[str] = []
    for article in manifest.get("articles") or []:
        if article.get("technical_notes_reader_facing") is False:
            continue
        rel = str(article.get("technical_notes_path") or "")
        if not rel or not (out / rel).is_file():
            continue
        path = out / rel
        result = tail_policy.apply_generic_tail_policy(path.read_text(encoding="utf-8"))
        path.write_text(result.text, encoding="utf-8")
        cards += result.card_count
        protected += result.protected_card_count
        added += result.groups_added
        unprotected.extend(tail_policy.unprotected_tail_titles(result.text))
    if unprotected:
        raise ValueError(f"#55 unprotected Technical Notes tails remain: {unprotected}")
    if cards < 1 or protected != cards:
        raise ValueError(f"#55 expected every visible card protected, cards={cards}, protected={protected}")
    return {
        "visible_card_count": cards,
        "protected_card_count": protected,
        "generic_groups_added": added,
        "unprotected_tail_findings": 0,
        "whole_card_unbreakable": False,
    }


def run_122_55(repo_root: Path, special_slug: str, issue_id: str) -> dict[str, Any]:
    mapping = {"122-55": ("v0.6", "v0.7", [122, 55])}

    def inner() -> dict[str, Any]:
        state_path, out, state, current, manifest, _ = seq_base.clone_revision(
            repo_root, special_slug, issue_id, "122-55"
        )
        audit_122 = seq_generic.step_122(out, manifest)
        dependency_added = ensure_needspace(out / "main.tex")
        audit_55 = apply_tail_policy(out, manifest)
        relaxed = seq_base.relax_chapter_starts(out / "main.tex")
        main_text = (out / "main.tex").read_text(encoding="utf-8")
        forced_section_starts = main_text.count("\\clearpage\n\\section{")
        if forced_section_starts != 1:
            raise ValueError(f"#55 expected only the first feature to retain forced page start, got {forced_section_starts}")
        manifest.setdefault("layout", {})["toc_depth"] = "section"
        manifest["layout"]["chapter_start_policy"] = (
            "first feature new page; subsequent chapters Needspace(0.45 textheight)"
        )
        manifest["issue_122_55"] = {
            "issue_122": audit_122,
            "issue_55": audit_55,
            "needspace_dependency_added": dependency_added,
            "forced_chapter_clearpages_relaxed": relaxed,
            "forced_section_starts_remaining": forced_section_starts,
        }
        before, _ = seq_base.load_chronology(repo_root, state)
        copied = seq_base.copy_chronology(repo_root, issue_id, state, "v0.7")
        if len(copied.get("events") or []) != len(before.get("events") or []):
            raise ValueError("#122/#55 chronology count changed")
        result = seq_base.finalize_revision(
            repo_root, issue_id, "122-55", state_path, out, state, current, manifest
        )
        result["audit"] = manifest["issue_122_55"]
        return result

    return with_versions(mapping, inner)


def visible_notes(out: Path, manifest: dict[str, Any]) -> str:
    chunks: list[str] = []
    for article in manifest.get("articles") or []:
        if article.get("technical_notes_reader_facing") is False:
            continue
        rel = str(article.get("technical_notes_path") or "")
        if rel and (out / rel).is_file():
            chunks.append((out / rel).read_text(encoding="utf-8"))
    return "\n".join(chunks)


def final_verify(repo_root: Path, issue_id: str) -> dict[str, Any]:
    state = load_json(repo_root / "sources" / issue_id / "pipeline-state.json")
    if state.get("lifecycle_state") != "VALIDATED_DRAFT":
        raise ValueError("final review repair must end at VALIDATED_DRAFT")
    gates = state.get("gates") or {}
    if gates.get("latex_build") != "pending" or gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("final review repair gate state mismatch")
    if "publication_preview" in (state.get("provenance") or {}):
        raise ValueError("Publication Preview approval must remain absent")
    source = state["provenance"]["validated_issue_source"]
    if source.get("source_version") != "v0.7":
        raise ValueError(f"final source version mismatch: {source.get('source_version')}")
    manifest_path = repo_root / source["path"]
    if sha(manifest_path) != source.get("sha256"):
        raise ValueError("final source manifest digest mismatch")
    manifest = load_json(manifest_path)
    out = manifest_path.parent
    if int(manifest.get("evidence_record_count") or 0) != 38:
        raise ValueError("selected Evidence cardinality changed")

    notes = visible_notes(out, manifest)
    forbidden = [
        "が2021年の生成AI技術記録に含まれることを確認できる",
        "一次資料で確認できる範囲の事実を記録しており",
        "時系列 & —",
        " & PRODUCT & ",
    ]
    findings = [x for x in forbidden if x in notes]
    if findings:
        raise ValueError(f"reader-facing review findings remain: {findings}")

    chronology_article = next(a for a in manifest["articles"] if a["package_id"] == "annual-chronology")
    if chronology_article.get("technical_notes_reader_facing") is not False:
        raise ValueError("#153 chronology Technical Notes still reader-facing")
    main = (out / manifest["main_tex"]["path"]).read_text(encoding="utf-8")
    chronology_token = rf"\input{{{Path(chronology_article['technical_notes_path']).with_suffix('').as_posix()}}}"
    if chronology_token in main:
        raise ValueError("#153 chronology Technical Notes input remains")

    chrono_info = state["provenance"]["annual_chronology"]
    chrono = load_json(repo_root / chrono_info["path"])
    events = chrono.get("events") or []
    if len(events) != 45 or any(not e.get("reference_key") for e in events):
        raise ValueError("#272 chronology reference mapping incomplete")
    chrono_tex = (out / chronology_article["layout_body_path"]).read_text(encoding="utf-8")
    if chrono_tex.count(r"\cite{") != 45:
        raise ValueError("#272 rendered chronology citation count mismatch")

    refs = (out / manifest["references"]["path"]).read_text(encoding="utf-8")
    if re.search(r"title\s*=\s*\{Primary source \d+\}", refs):
        raise ValueError("#78 generic reference title remains")
    if "Primary source used for chronology and technical verification" in refs:
        raise ValueError("#140 repeated reference boilerplate remains")
    if main.count("Referencesには本文・Detailed Chronologyの検証に用いた一次資料") != 1:
        raise ValueError("#140 common References purpose note is not consolidated exactly once")

    front = (out / manifest["frontmatter"]["path"]).read_text(encoding="utf-8")
    if r"\setcounter{tocdepth}{1}" not in front:
        raise ValueError("#122 section-level TOC policy missing")
    if r"\usepackage{needspace}" not in main:
        raise ValueError("#55 needspace dependency missing")
    if main.count("\\clearpage\n\\section{") != 1:
        raise ValueError("#55 later forced chapter clearpages remain")
    unprotected: list[str] = []
    card_count = 0
    for article in manifest["articles"]:
        if article.get("technical_notes_reader_facing") is False:
            continue
        rel = str(article.get("technical_notes_path") or "")
        if rel and (out / rel).is_file():
            text = (out / rel).read_text(encoding="utf-8")
            card_count += len(tail_policy.NOTE_RE.findall(text))
            unprotected.extend(tail_policy.unprotected_tail_titles(text))
    if unprotected:
        raise ValueError(f"#55 unprotected tail findings remain: {unprotected}")

    audit = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "final_source_version": "v0.7",
        "requested_order": [139, 54, "153/272", "78/140", "122/55"],
        "issue_refs": [139, 54, 153, 272, 78, 140, 122, 55],
        "evidence_record_count": 38,
        "visible_technical_notes_card_count": card_count,
        "generic_fallback_findings": 0,
        "chronology_placeholder_findings": 0,
        "raw_product_findings": 0,
        "duplicate_chronology_cards_rendered": 0,
        "chronology_event_count": 45,
        "chronology_reference_mapping_count": 45,
        "generic_reference_title_findings": 0,
        "repeated_reference_boilerplate_findings": 0,
        "toc_depth": "section",
        "unprotected_technical_note_tail_findings": 0,
        "new_external_evidence": False,
        "accepted_article_claims_changed": False,
        "publication_preview_approval_recorded": False,
    }
    audit_path = repo_root / "sources" / issue_id / "editorial" / "issues-139-54-153-272-78-140-122-55-v0.7.json"
    write_json(audit_path, audit)
    return audit


def build(repo_root: Path, special_slug: str, issue_id: str) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    state0 = load_json(repo_root / "sources" / issue_id / "pipeline-state.json")
    source0 = copy.deepcopy(state0["provenance"]["validated_issue_source"])
    manifest0 = load_json(repo_root / source0["path"])
    upstream_identity = [
        (a.get("package_id"), a.get("accepted_article_tex_sha256"), a.get("draft_package_sha256"))
        for a in manifest0.get("articles") or []
    ]

    results = [
        {"stage": "139", "result": run_139(repo_root, special_slug, issue_id)},
        {"stage": "54", "result": run_54(repo_root, special_slug, issue_id)},
        {"stage": "153-272", "result": run_153_272(repo_root, special_slug, issue_id)},
        {"stage": "78-140", "result": run_78_140(repo_root, special_slug, issue_id)},
        {"stage": "122-55", "result": run_122_55(repo_root, special_slug, issue_id)},
    ]

    statef = load_json(repo_root / "sources" / issue_id / "pipeline-state.json")
    manifestf = load_json(repo_root / statef["provenance"]["validated_issue_source"]["path"])
    final_identity = [
        (a.get("package_id"), a.get("accepted_article_tex_sha256"), a.get("draft_package_sha256"))
        for a in manifestf.get("articles") or []
    ]
    if final_identity != upstream_identity:
        raise ValueError("accepted Article Draft / Draft Package identity changed during review repair")

    audit = final_verify(repo_root, issue_id)
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "initial_source_version": source0.get("source_version"),
        "final_source_version": "v0.7",
        "stages": results,
        "final_audit": audit,
    }


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", default="2021-Y")
    parser.add_argument("--issue-id", default="SP-2021-Y")
    args = parser.parse_args()
    print(json.dumps(build(Path(args.repo_root), args.special_slug, args.issue_id), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
