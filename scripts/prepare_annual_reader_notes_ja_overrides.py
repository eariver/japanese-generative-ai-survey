#!/usr/bin/env python3
"""Generate reviewed-style Japanese Technical Notes overrides for Annual Specials.

Annual Evidence cards are deliberately compact and use a small, source-bound set
of editorial sentence templates. This helper translates only those exact known
patterns. It has no free-form fallback: unknown claim/limitation wording or any
Event Fact causes a hard failure so a human/interactive reviewer must handle the
new source text explicitly.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


ISSUE_RE = re.compile(r"^SP-(?P<year>\d{4})-Y$")
# Annual backfill Evidence has used both "primary source" and
# "primary-source" in otherwise identical, reviewed claim templates. Keep the
# helper fail-closed for every other wording while accepting those two known
# orthographic variants.
PRIMARY_SOURCE = r"primary[- ]source"
TECHNICAL_RE = re.compile(
    rf"^The reviewed {PRIMARY_SOURCE} set documents (?P<name>.+) within (?P<year>\d{{4}}); "
    r"technical and evaluation results remain attributed to the originating authors\.$"
)
LIFECYCLE_RE = re.compile(
    rf"^The reviewed {PRIMARY_SOURCE} set documents the (?P<year>\d{{4}}) release/publication lifecycle of (?P<name>.+); "
    r"capability and performance claims remain attributed to the originating vendor, project, or authors\.$"
)
GENERIC_RECORD_RE = re.compile(
    rf"^The reviewed {PRIMARY_SOURCE} set documents (?P<name>.+) as part of the (?P<year>\d{{4}}) generative-AI technical record\. "
    r"Technical, performance, access, and safety assertions remain attributed to the originating authors/projects "
    r"rather than treated as independent reproduction\.$"
)
LIMITATION = (
    "Primary-source verification establishes the bounded facts recorded here; "
    "it does not convert vendor, project, or author evaluations into independent reproduction."
)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def annual_year(issue_id: str) -> str:
    match = ISSUE_RE.fullmatch(issue_id)
    if not match:
        raise ValueError(f"unsupported Annual issue_id: {issue_id!r}")
    return match.group("year")


def _check_identity(match: re.Match[str], artifact_name: str, year: str, template: str) -> None:
    if match.group("name") != artifact_name:
        raise ValueError(
            f"{template} claim artifact mismatch: template={match.group('name')!r}, record={artifact_name!r}"
        )
    if match.group("year") != year:
        raise ValueError(
            f"{template} claim year mismatch: template={match.group('year')!r}, issue={year!r}"
        )


def translate_claim(source_text: str, artifact_name: str, year: str) -> str:
    match = TECHNICAL_RE.fullmatch(source_text)
    if match:
        _check_identity(match, artifact_name, year, "technical")
        return (
            f"一次資料で「{artifact_name}」が{year}年の技術動向として記録されていることを確認できる。"
            "技術内容や評価結果は、原著者による主張として扱い、独立再現済みの結果とはみなさない。"
        )
    match = LIFECYCLE_RE.fullmatch(source_text)
    if match:
        _check_identity(match, artifact_name, year, "lifecycle")
        return (
            f"一次資料で「{artifact_name}」の{year}年における公開・リリースの経緯を確認できる。"
            "能力や性能に関する評価は、提供元・プロジェクト・著者の主張として扱う。"
        )
    match = GENERIC_RECORD_RE.fullmatch(source_text)
    if match:
        _check_identity(match, artifact_name, year, "generic-record")
        return (
            f"一次資料で「{artifact_name}」が{year}年の生成AI技術記録に含まれることを確認できる。"
            "技術内容、性能、アクセス、安全性に関する記述は、原著者・プロジェクトの主張として扱い、"
            "独立再現済みの結果とはみなさない。"
        )
    raise ValueError(f"unsupported Annual Technical Notes claim template for {artifact_name!r}: {source_text!r}")


def translate_limitation(source_text: str) -> str:
    if source_text != LIMITATION:
        raise ValueError(f"unsupported Annual Technical Notes limitation template: {source_text!r}")
    return (
        "一次資料で確認できる範囲の事実を記録しており、提供元・プロジェクト・著者による評価を"
        "独立再現済みの結果として扱わない。"
    )


def build(summary: dict[str, Any], issue_id: str) -> list[dict[str, Any]]:
    if summary.get("schema_version") != "1.0" or summary.get("issue_id") != issue_id:
        raise ValueError("summary identity mismatch")
    if summary.get("status") not in {"DRAFT", "READY"}:
        raise ValueError(f"unexpected summary status: {summary.get('status')!r}")
    year = annual_year(issue_id)
    translations: list[dict[str, Any]] = []
    records = summary.get("records")
    if not isinstance(records, list) or not records:
        raise ValueError("summary records must be non-empty")
    for record in records:
        if not isinstance(record, dict):
            raise ValueError("summary record must be object")
        task_id = record.get("evidence_task_id")
        artifact = record.get("artifact_name")
        if not isinstance(task_id, str) or not task_id or not isinstance(artifact, str) or not artifact:
            raise ValueError("record identity/artifact missing")
        event_facts = record.get("event_facts") or []
        if event_facts:
            raise ValueError(
                f"{artifact}: Annual generic translation generator refuses Event Facts; review them explicitly"
            )
        for item in record.get("claims") or []:
            source = item.get("source_text")
            source_sha = item.get("source_text_sha256")
            item_id = item.get("item_id")
            if not all(isinstance(value, str) and value for value in (source, source_sha, item_id)):
                raise ValueError(f"{artifact}: invalid claim item")
            translations.append(
                {
                    "evidence_task_id": task_id,
                    "kind": "claim",
                    "item_id": item_id,
                    "source_text_sha256": source_sha,
                    "text_ja": translate_claim(source, artifact, year),
                }
            )
        for item in record.get("limitations") or []:
            source = item.get("source_text")
            source_sha = item.get("source_text_sha256")
            item_id = item.get("item_id")
            if not all(isinstance(value, str) and value for value in (source, source_sha, item_id)):
                raise ValueError(f"{artifact}: invalid limitation item")
            translations.append(
                {
                    "evidence_task_id": task_id,
                    "kind": "limitation",
                    "item_id": item_id,
                    "source_text_sha256": source_sha,
                    "text_ja": translate_limitation(source),
                }
            )
    if not translations:
        raise ValueError("no Annual Technical Notes translations generated")
    return translations


def run(repo_root: Path, issue_id: str, summary_path: Path, overrides_dir: Path, part_size: int) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    summary_path = (repo_root / summary_path).resolve() if not summary_path.is_absolute() else summary_path.resolve()
    overrides_dir = (repo_root / overrides_dir).resolve() if not overrides_dir.is_absolute() else overrides_dir.resolve()
    summary = load_json(summary_path)
    translations = build(summary, issue_id)
    if part_size < 1:
        raise ValueError("part_size must be positive")
    overrides_dir.mkdir(parents=True, exist_ok=True)
    for existing in overrides_dir.glob("part-*.json"):
        existing.unlink()
    parts = []
    for index, start in enumerate(range(0, len(translations), part_size), start=1):
        path = overrides_dir / f"part-{index:03d}.json"
        write_json(
            path,
            {
                "schema_version": "1.0",
                "issue_id": issue_id,
                "review_mode": "ANNUAL_KNOWN_TEMPLATE_FAIL_CLOSED",
                "translations": translations[start : start + part_size],
            },
        )
        parts.append(path.name)
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "translation_count": len(translations),
        "part_count": len(parts),
        "parts": parts,
        "unknown_template_policy": "fail-closed",
        "event_fact_policy": "explicit-review-required",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--overrides-dir", required=True)
    parser.add_argument("--part-size", type=int, default=24)
    args = parser.parse_args()
    report = run(Path(args.repo_root), args.issue_id, Path(args.summary), Path(args.overrides_dir), args.part_size)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
