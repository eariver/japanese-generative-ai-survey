#!/usr/bin/env python3
"""Make generated Special Technical Notes reader-facing without changing Evidence.

This is a derived-source presentation pass. It removes unconditional page breaks
and repository-only identifiers from the PDF-facing TeX while preserving the
complete Draft Package / Evidence provenance elsewhere in the repository.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from scripts.special_technical_note_tail_policy import (
    apply_generic_tail_policy,
    unprotected_tail_titles,
)


ROLE_LABELS = {
    "PRIMARY": "主要資料",
    "SUPPORTING": "補足資料",
}
EVENT_LABELS = {
    "OFFICIAL_PUBLICATION": "公式公開",
    "PRODUCT_RELEASE": "製品公開",
    "PRODUCT_UPDATE": "製品更新",
    "AGENT_RELEASE": "Agent公開",
    "AGENT_UPDATE": "Agent更新",
    "FRAMEWORK_RELEASE": "Framework公開",
    "FRAMEWORK_PUBLICATION": "Framework公開",
    "FRAMEWORK_UPDATE": "Framework更新",
    "MODEL_RELEASE": "モデル公開",
    "MODEL_UPDATE": "モデル更新",
    "MODEL_STUDIO_AVAILABILITY": "Model Studio提供開始",
    "OPEN_WEIGHT_RELEASE": "オープンウェイト公開",
    "PAPER_RELEASE": "論文公開",
    "PAPER_SUBMISSION": "論文投稿",
    "RESEARCH_RELEASE": "研究公開",
    "SAFETY_EVENT": "安全性事象",
    "SECURITY_ENGINEERING_NOTE": "セキュリティ技術解説",
    "API_RELEASE": "API公開",
    "API_UPDATE": "API更新",
    "API_INPUT_EXPANSION": "API入力拡張",
    "API_LIFECYCLE_FEATURE": "APIライフサイクル機能",
    "API_TOOL_RELEASE": "APIツール公開",
    "ENGINEERING_NOTE": "技術解説",
    "MODEL_BEHAVIOR_POLICY_RELEASE": "モデル行動方針公開",
    "AGENT_PRODUCT_RELEASE": "Agent製品公開",
    "PROJECT_RELEASE": "プロジェクト公開",
    "PROJECT_PRERELEASE": "プロジェクトPre-release",
    "PROJECT_UPDATE": "プロジェクト更新",
    "SYSTEM_CARD_PUBLICATION": "System Card公開",
    "RESEARCH_PREVIEW": "研究Preview",
    "REGIONAL_MODEL_RELEASE": "地域別モデル公開",
    "INTERNATIONAL_MODEL_RELEASE": "国際提供モデル公開",
    "OPEN_WEIGHT_MODEL_RELEASE": "オープンウェイトモデル公開",
    "TECHNICAL_FRAMEWORK_RELEASE": "技術Framework公開",
    "API_MODEL_RELEASE": "APIモデル公開",
    "EVALUATION_RELEASE": "評価公開",
    "MEDIA_MODEL_RELEASE": "メディアモデル公開",
    "MEDIA_MODEL_UPDATE": "メディアモデル更新",
}
TYPE_LABELS = {
    # Legacy partially translated forms can remain in historical derived
    # revisions. Keep them here so a reprocessed revision does not expose
    # mixed labels such as モデル\_RELEASE.
    "モデル_RELEASE": "モデル公開",
    "モデル_UPDATE": "モデル更新",
    "研究_RELEASE": "研究公開",
    "論文_RELEASE": "論文公開",
    "Framework_RELEASE": "Framework公開",
    "Framework_UPDATE": "Framework更新",
    "Agent_RELEASE": "Agent公開",
    "Agent_UPDATE": "Agent更新",
    "API_RELEASE": "API公開",
    "API_UPDATE": "API更新",
    "オープンウェイト_RELEASE": "オープンウェイト公開",
    "FRAMEWORK_RELEASE": "Framework公開",
    "FRAMEWORK_PUBLICATION": "Framework公開",
    "FRAMEWORK_UPDATE": "Framework更新",
    "MODEL_RELEASE": "モデル公開",
    "MODEL_UPDATE": "モデル更新",
    "AGENT_RELEASE": "Agent公開",
    "AGENT_UPDATE": "Agent更新",
    "OPEN_WEIGHT": "オープンウェイト",
    "SAFETY_EVENT": "安全性関連",
    "SECURITY_EVENT": "セキュリティ関連",
    "FRAMEWORK": "Framework",
    "RESEARCH": "研究",
    "PAPER": "論文",
    "MODEL": "モデル",
    "AGENT": "Agent",
    "API": "API",
    "OTHER": "公式情報",
    # Backward-compatible pre-reader-facing spellings.
    "MODEL UPDATE": "モデル更新",
    "OPEN WEIGHT": "オープンウェイト",
    "FRAMEWORK RELEASE": "Framework公開",
    "FRAMEWORK UPDATE": "Framework更新",
    "AGENT RELEASE": "Agent公開",
    "AGENT UPDATE": "Agent更新",
    "SAFETY EVENT": "安全性関連",
    "SECURITY EVENT": "セキュリティ関連",
    "Agent_製品公開": "Agent製品公開",
    "研究_PREVIEW": "研究Preview",
    "REGIONAL_モデル公開": "地域別モデル公開",
    "INTERNATIONAL_モデル公開": "国際提供モデル公開",
    "オープンウェイト_モデル公開": "オープンウェイトモデル公開",
    "TECHNICAL_Framework公開": "技術Framework公開",
    "API_モデル公開": "APIモデル公開",
}
TYPE_OVERRIDES = {
    "A shared playbook for trustworthy third party evaluations": "評価ガイダンス",
}

OLD_INTRO = (
    "この欄は記事本文で圧縮した一次資料上の情報を、比較・再検証しやすい形へ展開したものである。"
    "新しい外部情報は追加せず、Selection済みEvidenceのchronology、normalized claim、limitations、source URLのみを再配置する。"
)
NEW_INTRO = (
    "本欄は記事本文で圧縮した一次資料上の情報を、比較・再検証しやすい形で整理したものである。"
    "時系列、確認済みの主張、留意点、一次資料URLを掲載する。"
)
BREAK_POLICY_MARKER = "% reader-facing Technical Notes break policy"
OLD_TAIL_GUARD_MARKER = "% reader-facing Technical Notes late-card tail guard"
OLD_TAIL_GUARD = OLD_TAIL_GUARD_MARKER + "\n" + r"\Needspace{12\baselineskip}" + "\n"
TAIL_GROUP_MARKER = "% reader-facing Technical Notes coherent tail group"


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def enum_forms(value: str) -> tuple[str, ...]:
    escaped = value.replace("_", r"\_")
    return (value,) if escaped == value else (value, escaped)


CHRONOLOGY_EVENT_RE = re.compile(r"\b\d{4}-\d{2}(?:-\d{2})?\s*\(([^)]+)\)")
ALLCAPS_SPACE_RE = re.compile(r"^[A-Z][A-Z0-9]*(?:\s+[A-Z][A-Z0-9]*)+$")
MACHINE_SINGLE_TYPE_LABELS = {"PRODUCT", "OTHER"}


def _machine_taxonomy_label(value: str) -> bool:
    value = value.replace(r"\_", "_").strip()
    if not value:
        return False
    if "_" in value:
        return True
    if ALLCAPS_SPACE_RE.fullmatch(value):
        return True
    if value in MACHINE_SINGLE_TYPE_LABELS:
        return True
    return False


def reader_taxonomy_findings(text: str) -> list[str]:
    # Inspect only taxonomy fields, not URLs or free prose.
    normalized = text.replace(r"\_", "_")
    findings: set[str] = set()
    for value in CHRONOLOGY_EVENT_RE.findall(normalized):
        label = value.strip()
        if _machine_taxonomy_label(label):
            findings.add(label)
    for line in normalized.splitlines():
        stripped = line.strip()
        if stripped.startswith("種別 & "):
            value = stripped[len("種別 & "):].rsplit(r"\\", 1)[0].strip()
            if _machine_taxonomy_label(value):
                findings.add(value)
            continue
        if " & " in stripped and re.search(r"\b\d{4}-\d{2}", stripped):
            parts = [part.strip() for part in stripped.rsplit(r"\\", 1)[0].split(" & ")]
            if len(parts) >= 4:
                value = parts[-2]
                if _machine_taxonomy_label(value):
                    findings.add(value)
    return sorted(findings)


def translate_machine_labels(text: str) -> str:
    # Event types are normally emitted inside parentheses. Translate those
    # first, before broad artifact-type tokens, so MODEL\_RELEASE cannot
    # degrade into a mixed label such as モデル\_RELEASE.
    for old, new in sorted(EVENT_LABELS.items(), key=lambda item: len(item[0]), reverse=True):
        for form in enum_forms(old):
            text = text.replace(f"({form})", f"({new})")
    # Some derived/historical renderer paths can expose the same event enum
    # outside the parenthesized chronology form. Normalize any remainder
    # before replacing broad tokens such as MODEL or FRAMEWORK.
    for old, new in sorted(EVENT_LABELS.items(), key=lambda item: len(item[0]), reverse=True):
        for form in enum_forms(old):
            text = text.replace(form, new)
    for old, new in ROLE_LABELS.items():
        text = text.replace("{" + old + "}", "{" + new + "}")
        text = text.replace(f" & {old} & ", f" & {new} & ")
    # Artifact types and legacy partially translated event labels are machine
    # presentation artifacts. Replace raw and TeX-escaped forms, longest first.
    for old, new in sorted(TYPE_LABELS.items(), key=lambda item: len(item[0]), reverse=True):
        for form in enum_forms(old):
            text = text.replace(form, new)
    return text


def apply_type_overrides(text: str) -> str:
    lines = text.splitlines()
    current_title: str | None = None
    for i, line in enumerate(lines):
        for title, label in TYPE_OVERRIDES.items():
            if line.startswith(title + " & "):
                parts = line.split(" & ")
                if len(parts) >= 4:
                    parts[2] = label
                    lines[i] = " & ".join(parts)
                    line = lines[i]
        match = re.match(r"\\begin\{technicalnote\}\{(.+?)\}\{", line)
        if match:
            current_title = match.group(1)
            continue
        if line == r"\end{technicalnote}":
            current_title = None
            continue
        if current_title in TYPE_OVERRIDES and line.startswith("種別 & "):
            suffix = r" \\" if line.rstrip().endswith(r"\\") else ""
            lines[i] = f"種別 & {TYPE_OVERRIDES[current_title]}{suffix}"
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def protect_primary_source_blocks(text: str) -> str:
    """Keep a source heading with its URL list without making the whole card rigid."""
    lines = text.splitlines()
    output: list[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line == r"{\bfseries 一次資料}" and (not output or output[-1] != r"\begin{samepage}"):
            output.append(r"\begin{samepage}")
            output.append(line)
            i += 1
            while i < len(lines):
                output.append(lines[i])
                if lines[i] == r"\end{itemize}":
                    i += 1
                    if i < len(lines) and lines[i] == r"\endgroup":
                        output.append(lines[i])
                        i += 1
                    output.append(r"\end{samepage}")
                    break
                i += 1
            continue
        output.append(line)
        i += 1
    return "\n".join(output) + ("\n" if text.endswith("\n") else "")


def add_card_break_policy(text: str) -> str:
    """Discourage single-line card continuations while retaining breakable cards."""
    lines = text.splitlines()
    output: list[str] = []
    in_note = False
    policy_open = False
    for line in lines:
        if re.match(r"\\begin\{technicalnote\}\{.*?\}\{.*?\}$", line):
            in_note = True
            output.append(line)
            output.extend([
                r"\begingroup",
                BREAK_POLICY_MARKER,
                r"\widowpenalty=10000",
                r"\clubpenalty=10000",
                r"\displaywidowpenalty=10000",
            ])
            policy_open = True
            continue
        if line == r"\end{technicalnote}" and in_note:
            if policy_open:
                output.append(r"\endgroup")
            output.append(line)
            in_note = False
            policy_open = False
            continue
        output.append(line)
    return "\n".join(output) + ("\n" if text.endswith("\n") else "")


def group_late_card_tail(text: str, selected_titles: set[str] | None = None) -> str:
    """Keep the attributed-claim/limitation/source tail as one compact unit.

    The technicalnote itself stays breakable.  Only the final attributed claim,
    the limitation block, and the primary-source block are put into a minipage.
    This gives the tcolorbox a deterministic break boundary without making the
    whole card unbreakable or inserting a broad page-level Needspace guard.
    """
    text = text.replace(OLD_TAIL_GUARD, "")
    if TAIL_GROUP_MARKER in text:
        return text

    lines = text.splitlines()
    output: list[str] = []
    in_note = False
    current_title: str | None = None
    group_open = False
    groups = 0
    selected_titles = selected_titles or set()
    for line in lines:
        note_match = re.match(r"\\begin\{technicalnote\}\{(.+?)\}\{.*?\}$", line)
        if note_match:
            in_note = True
            current_title = note_match.group(1)
        if in_note and current_title in selected_titles and not group_open and re.match(r"\\item \\textbf\{(?:Vendor claim|Project claim|Author claim)\}:", line):
            # Close the technical-points list after the primary fact and reopen
            # a list for the final attributed claim inside an unbreakable tail.
            output.append(r"\end{itemize}")
            output.append(r"\begin{minipage}{\linewidth}")
            output.append(TAIL_GROUP_MARKER)
            output.append(r"\begin{itemize}[leftmargin=1.5em,itemsep=0.35em]")
            output.append(line)
            group_open = True
            groups += 1
            continue
        output.append(line)
        if group_open and line == r"\end{samepage}":
            output.append(r"\end{minipage}")
            group_open = False
        if line == r"\end{technicalnote}":
            if group_open:
                raise ValueError("Technical Notes coherent tail group did not close before card end")
            in_note = False
            current_title = None
    # Some source records legitimately have no separately attributed claim,
    # In that case there is no late-card tail to group; keep the card unchanged
    # apart from removing any obsolete Needspace marker from an older revision.
    return "\n".join(output) + ("\n" if text.endswith("\n") else "")


def transform_note(text: str, selected_titles: set[str] | None = None) -> str:
    # A Technical Notes block must follow the preceding synthesis naturally. An
    # unconditional clearpage can otherwise strand a small Claim Boundary box.
    text = re.sub(r"\A\\clearpage\s*\n", "", text, count=1)
    text = text.replace(OLD_INTRO, NEW_INTRO)
    text = text.replace(
        r"Artifact & Role & Type & Objective chronology \\",
        r"資料 & 位置づけ & 種別 & 時系列 \\",
    )
    text = text.replace("Organization & ", "組織 & ")
    text = text.replace("Artifact type & ", "種別 & ")
    text = text.replace("Chronology & ", "時系列 & ")
    text = text.replace(r"{\bfseries Primary source}", r"{\bfseries 一次資料}")
    text = text.replace(
        r"\item このrecordには独立したnormalized claimは記録されていない。",
        r"\item この資料では、個別の確認済み主張として分離された項目は記録されていない。",
    )
    # Complete Evidence IDs remain in immutable Draft Packages / source
    # provenance. Repeating them in the magazine appendix reduces readability.
    text = re.sub(
        r"^\{\\scriptsize\\color\{SurveyMuted\}Source-bound record: .*?\}\.?\}\s*$\n?",
        "",
        text,
        flags=re.MULTILINE,
    )
    text = translate_machine_labels(text)
    text = apply_type_overrides(text)
    text = protect_primary_source_blocks(text)
    if BREAK_POLICY_MARKER not in text:
        text = add_card_break_policy(text)
    text = group_late_card_tail(text, selected_titles=selected_titles)
    taxonomy_findings = reader_taxonomy_findings(text)
    if taxonomy_findings:
        raise ValueError(f"reader-facing taxonomy leak remains: {taxonomy_findings}")
    generic = apply_generic_tail_policy(text)
    text = generic.text
    unprotected = unprotected_tail_titles(text)
    if unprotected:
        raise ValueError(f"Technical Notes tail policy left unprotected card(s): {unprotected}")
    return text


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--issue-id", required=True)
    ap.add_argument("--special-slug", required=True)
    ap.add_argument("--source-version", required=True)
    args = ap.parse_args()

    root = Path(args.repo_root).resolve()
    state_path = root / "sources" / args.issue_id / "pipeline-state.json"
    state = read_json(state_path)
    source = state["provenance"]["validated_issue_source"]
    expected_manifest = root / "surveys" / "special" / args.special_slug / "revisions" / args.source_version / "source-manifest.json"
    manifest_path = root / source["path"]
    if manifest_path != expected_manifest:
        raise ValueError("state-pinned source is not the requested Special revision")
    if sha256_file(manifest_path) != source["sha256"]:
        raise ValueError("source manifest SHA mismatch before reader-facing pass")
    manifest = read_json(manifest_path)
    configured_reader = dict(manifest.get("reader_facing_technical_notes") or {})
    tail_group_titles = set(configured_reader.get("late_card_tail_group_titles") or [])
    changed: list[dict[str, str]] = []
    for article in manifest.get("articles") or []:
        rel = article.get("technical_notes_path")
        if not rel:
            continue
        path = manifest_path.parent / rel
        before = sha256_file(path)
        original = path.read_text(encoding="utf-8")
        revised = transform_note(original, selected_titles=tail_group_titles)
        if revised == original:
            raise ValueError(f"reader-facing Technical Notes pass made no change: {rel}")
        if "Selection済みEvidence" in revised or "normalized claim" in revised or "Source-bound record:" in revised:
            raise ValueError(f"pipeline-centric wording remained in Technical Notes: {rel}")
        if revised.lstrip().startswith(r"\clearpage"):
            raise ValueError(f"unconditional clearpage remained at Technical Notes boundary: {rel}")
        unprotected = unprotected_tail_titles(revised)
        if unprotected:
            raise ValueError(f"generic Technical Notes tail policy failed in {rel}: {unprotected}")
        path.write_text(revised, encoding="utf-8")
        after = sha256_file(path)
        article["technical_notes_sha256"] = after
        changed.append({"path": rel, "before_sha256": before, "after_sha256": after})

    if not changed:
        raise ValueError("source manifest contains no Technical Notes")

    # Preserve any earlier derived-language provenance written by the Japanese
    # summary pass; this presentation cleanup must not erase that binding.
    reader = dict(manifest.get("reader_facing_technical_notes") or {})
    reader.update({
        "policy": "reader-facing technical appendix; complete Evidence identifiers remain repository provenance",
        "unconditional_clearpage_at_entry": False,
        "evidence_ids_rendered_in_pdf": False,
        "pipeline_terms_removed": ["Selection済みEvidence", "normalized claim", "Source-bound record"],
        "machine_enum_policy": "reader-facing-labels-v3",
        "whole_card_unbreakable": False,
        "source_block_samepage": True,
        "paragraph_widow_orphan_penalty": 10000,
        "late_card_tail_needspace_baselines": 0,
        "late_card_tail_group_titles": sorted(tail_group_titles),
        "late_card_tail_group": "opt-in minipage from final attributed claim through limitation/source block",
        "late_card_tail_group_scope": "only exact titles selected after render QA; technicalnote remains breakable",
        "generic_boundary_source_tail_group": True,
        "generic_boundary_source_tail_scope": "all Technical Notes cards with a reader boundary and primary-source block; whole card remains breakable",
        "generic_boundary_source_tail_validation": "no unprotected boundary/limitation/source tail may remain",
        "changed_files": changed,
    })
    manifest["reader_facing_technical_notes"] = reader
    write_json(manifest_path, manifest)
    source["sha256"] = sha256_file(manifest_path)
    source["reader_facing_technical_notes"] = True
    write_json(state_path, state)

    print(json.dumps({
        "status": "READER_FACING_TECHNICAL_NOTES_APPLIED",
        "issue_id": args.issue_id,
        "source_version": args.source_version,
        "source_manifest_sha256": source["sha256"],
        "technical_notes_changed": len(changed),
        "language_policy": reader.get("language_policy"),
        "machine_enum_policy": reader.get("machine_enum_policy"),
        "source_block_samepage": reader.get("source_block_samepage"),
        "late_card_tail_group": reader.get("late_card_tail_group"),
        "generic_boundary_source_tail_group": reader.get("generic_boundary_source_tail_group"),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
