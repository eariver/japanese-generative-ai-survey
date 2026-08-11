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


ROLE_LABELS = {
    "PRIMARY": "主要資料",
    "SUPPORTING": "補足資料",
}
EVENT_LABELS = {
    "MODEL_RELEASE": "モデル公開",
    "MODEL_UPDATE": "モデル更新",
    "FRAMEWORK_RELEASE": "フレームワーク公開",
    "OPEN_WEIGHT_RELEASE": "オープンウェイト公開",
    "PAPER_RELEASE": "論文公開",
    "SAFETY_EVENT": "安全性事象",
    "API_RELEASE": "API公開",
}
TYPE_LABELS = {
    "MODEL UPDATE": "モデル更新",
    "OPEN WEIGHT": "オープンウェイト",
    "FRAMEWORK RELEASE": "フレームワーク公開",
    "SAFETY EVENT": "安全性事象",
    "RESEARCH": "研究",
    "PAPER": "論文",
    "MODEL": "モデル",
    "API": "API",
}

OLD_INTRO = (
    "この欄は記事本文で圧縮した一次資料上の情報を、比較・再検証しやすい形へ展開したものである。"
    "新しい外部情報は追加せず、Selection済みEvidenceのchronology、normalized claim、limitations、source URLのみを再配置する。"
)
NEW_INTRO = (
    "本欄は記事本文で圧縮した一次資料上の情報を、比較・再検証しやすい形で整理したものである。"
    "時系列、確認済みの主張、留意点、一次資料URLを掲載する。"
)


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def translate_machine_labels(text: str) -> str:
    for old, new in EVENT_LABELS.items():
        text = text.replace(f"({old})", f"({new})")
    for old, new in ROLE_LABELS.items():
        text = text.replace("{" + old + "}", "{" + new + "}")
        text = text.replace(f" & {old} & ", f" & {new} & ")
    # Artifact types are uppercase machine labels in generated metadata/tables.
    # Longest labels are replaced first so MODEL does not partially consume
    # MODEL UPDATE.
    for old, new in sorted(TYPE_LABELS.items(), key=lambda item: len(item[0]), reverse=True):
        text = text.replace(old, new)
    return text


def transform_note(text: str) -> str:
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
    return translate_machine_labels(text)


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
    changed: list[dict[str, str]] = []
    for article in manifest.get("articles") or []:
        rel = article.get("technical_notes_path")
        if not rel:
            continue
        path = manifest_path.parent / rel
        before = sha256_file(path)
        original = path.read_text(encoding="utf-8")
        revised = transform_note(original)
        if revised == original:
            raise ValueError(f"reader-facing Technical Notes pass made no change: {rel}")
        if "Selection済みEvidence" in revised or "normalized claim" in revised or "Source-bound record:" in revised:
            raise ValueError(f"pipeline-centric wording remained in Technical Notes: {rel}")
        if revised.lstrip().startswith(r"\clearpage"):
            raise ValueError(f"unconditional clearpage remained at Technical Notes boundary: {rel}")
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
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
