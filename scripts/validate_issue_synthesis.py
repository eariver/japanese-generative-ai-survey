#!/usr/bin/env python3
"""Validate post-draft cover/This Week synthesis against exact validated article input."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def valid_datetime(value: Any) -> bool:
    if not nonempty(value):
        return False
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return False
    return parsed.tzinfo is not None


def validate(input_path: Path, result_path: Path, prompt_path: Path) -> tuple[dict[str, Any], bool]:
    synthesis_input = load_json(input_path)
    result = load_json(result_path)
    errors: list[str] = []

    if result.get("schema_version") != "1.0":
        errors.append("result.schema_version must be 1.0")
    if result.get("issue_id") != synthesis_input.get("issue_id"):
        errors.append("result.issue_id does not match synthesis input")
    if result.get("status") not in {"DRAFT", "REVISED"}:
        errors.append("result.status must be DRAFT or REVISED")

    basis = result.get("basis")
    if not isinstance(basis, dict):
        errors.append("result.basis must be an object")
        basis = {}
    if basis.get("synthesis_input_sha256") != sha256_file(input_path):
        errors.append("synthesis_input_sha256 does not match exact input bytes")
    if basis.get("prompt_id") != "issue-synthesis-v0.1":
        errors.append("prompt_id must be issue-synthesis-v0.1")
    if basis.get("prompt_sha256") != sha256_file(prompt_path):
        errors.append("prompt_sha256 does not match exact issue-synthesis prompt")

    runner = result.get("runner")
    if not isinstance(runner, dict):
        errors.append("result.runner must be an object")
    else:
        for field in ("provider", "model", "invocation"):
            if not nonempty(runner.get(field)):
                errors.append(f"runner.{field} must be non-empty")
        if not valid_datetime(runner.get("generated_at")):
            errors.append("runner.generated_at must be timezone-aware ISO-8601")

    articles = synthesis_input.get("articles")
    if not isinstance(articles, list) or not articles:
        errors.append("synthesis input articles must be non-empty")
        articles = []
    article_by_id: dict[str, dict[str, Any]] = {}
    for index, article in enumerate(articles):
        if not isinstance(article, dict) or not nonempty(article.get("package_id")):
            errors.append(f"input articles[{index}] is invalid")
            continue
        package_id = article["package_id"]
        if package_id in article_by_id:
            errors.append(f"duplicate article package_id in synthesis input: {package_id}")
        article_by_id[package_id] = article

    cover = result.get("cover")
    if not isinstance(cover, dict):
        errors.append("result.cover must be an object")
        cover = {}
    if not nonempty(cover.get("headline")) or not nonempty(cover.get("deck")):
        errors.append("cover headline and deck must be non-empty")
    anchors = cover.get("anchor_package_ids")
    if not isinstance(anchors, list) or not anchors:
        errors.append("cover.anchor_package_ids must be non-empty")
        anchors = []
    if len(anchors) > 3:
        errors.append("cover.anchor_package_ids may contain at most 3 packages")
    if len(anchors) != len(set(anchors)):
        errors.append("cover.anchor_package_ids contains duplicates")
    unknown_anchors = sorted(set(anchors) - set(article_by_id))
    if unknown_anchors:
        errors.append(f"cover references unknown article packages: {unknown_anchors}")

    signals = result.get("this_week_signals")
    max_signals = synthesis_input.get("constraints", {}).get("max_this_week_signals", 5)
    if not isinstance(signals, list) or not signals:
        errors.append("this_week_signals must be a non-empty array")
        signals = []
    if len(signals) > max_signals:
        errors.append(f"this_week_signals exceeds input maximum {max_signals}")

    signal_ids: list[str] = []
    for index, signal in enumerate(signals):
        prefix = f"this_week_signals[{index}]"
        if not isinstance(signal, dict):
            errors.append(f"{prefix} must be an object")
            continue
        signal_id = signal.get("signal_id")
        if not nonempty(signal_id):
            errors.append(f"{prefix}.signal_id must be non-empty")
        else:
            signal_ids.append(signal_id)
        if not nonempty(signal.get("title")) or not nonempty(signal.get("summary")):
            errors.append(f"{prefix} title/summary must be non-empty")
        package_ids = signal.get("package_ids")
        if not isinstance(package_ids, list) or not package_ids:
            errors.append(f"{prefix}.package_ids must be non-empty")
            package_ids = []
        if len(package_ids) != len(set(package_ids)):
            errors.append(f"{prefix}.package_ids contains duplicates")
        unknown = sorted(set(package_ids) - set(article_by_id))
        if unknown:
            errors.append(f"{prefix} references unknown article packages: {unknown}")
        known_articles = [article_by_id[package_id] for package_id in package_ids if package_id in article_by_id]
        has_late = any(article.get("late_breaking") is True for article in known_articles)
        late_flag = signal.get("late_breaking")
        if not isinstance(late_flag, bool):
            errors.append(f"{prefix}.late_breaking must be boolean")
        elif has_late and late_flag is not True:
            errors.append(f"{prefix} references Late Breaking package but late_breaking=false")
        elif not has_late and late_flag is not False:
            errors.append(f"{prefix} has late_breaking=true without any Late Breaking package")

    duplicates = sorted(key for key, count in Counter(signal_ids).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate signal_id values: {duplicates}")

    report = {
        "schema_version": "1.0",
        "passed": not errors,
        "issue_id": synthesis_input.get("issue_id"),
        "synthesis_input_sha256": sha256_file(input_path),
        "prompt_sha256": sha256_file(prompt_path),
        "article_count": len(article_by_id),
        "cover_anchor_count": len(anchors),
        "signal_count": len(signals),
        "errors": errors,
    }
    return report, not errors


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True)
    parser.add_argument("--result", required=True)
    parser.add_argument("--prompt", default="config/prompts/editorial/issue-synthesis-v0.1.md")
    parser.add_argument("--report")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    report, passed = validate(Path(args.input), Path(args.result), Path(args.prompt))
    if args.report:
        path = Path(args.report)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
