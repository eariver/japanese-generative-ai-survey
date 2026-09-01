#!/usr/bin/env python3
"""Validate post-draft cover/This Week synthesis against exact validated article input."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

CONCRETE_TOKEN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:/+\-]{1,}")
GENERIC_ACRONYMS = {"ai", "api", "llm", "oss", "gpu", "cpu", "pdf"}
LATE_BOUNDARY_MARKERS = ("締切後", "カットオフ後", "post-cutoff", "late breaking")


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


def concrete_tokens(text: str) -> set[str]:
    """Return conservative machine-checkable names/numbers from free text.

    This intentionally does not attempt Japanese semantic entailment. It catches
    new numeric/model-like identifiers while allowing ordinary editorial prose.
    """
    tokens: set[str] = set()
    for match in CONCRETE_TOKEN_RE.finditer(text):
        token = match.group(0)
        folded = token.casefold()
        if folded in GENERIC_ACRONYMS:
            continue
        has_digit = any(char.isdigit() for char in token)
        has_lower = any(char.islower() for char in token)
        has_upper = any(char.isupper() for char in token)
        has_separator = any(char in "._:/+-" for char in token)
        all_upper_name = token.isupper() and len(token) >= 3
        if has_digit or (has_lower and has_upper) or has_separator or all_upper_name:
            tokens.add(folded)
    return tokens


def article_text(article: dict[str, Any]) -> str:
    parts = [str(article.get("headline") or ""), str(article.get("deck") or "")]
    for block in article.get("blocks") or []:
        if isinstance(block, dict):
            parts.append(str(block.get("text") or ""))
    return "\n".join(parts)


def unsupported_concrete_tokens(text: str, articles: list[dict[str, Any]]) -> list[str]:
    allowed: set[str] = set()
    for article in articles:
        allowed.update(concrete_tokens(article_text(article)))
    return sorted(concrete_tokens(text) - allowed)


def has_late_boundary_wording(text: str) -> bool:
    folded = text.casefold()
    return any(marker.casefold() in folded for marker in LATE_BOUNDARY_MARKERS)


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

    architecture_anchors = synthesis_input.get("cover_anchor_candidates")
    if isinstance(architecture_anchors, list) and architecture_anchors:
        outside_architecture = sorted(set(anchors) - set(architecture_anchors))
        if outside_architecture:
            errors.append(
                f"cover anchors are outside Architecture cover_anchor_candidates: {outside_architecture}"
            )

    known_anchor_articles = [article_by_id[package_id] for package_id in anchors if package_id in article_by_id]
    cover_concrete = unsupported_concrete_tokens(
        f"{cover.get('headline') or ''}\n{cover.get('deck') or ''}", known_anchor_articles
    )
    if cover_concrete:
        errors.append(
            "cover introduces concrete ASCII identifiers/numbers absent from anchor article text: "
            f"{cover_concrete}"
        )

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
        if has_late and nonempty(signal.get("summary")) and not has_late_boundary_wording(signal["summary"]):
            errors.append(
                f"{prefix} references Late Breaking package but summary does not explicitly preserve post-cutoff wording"
            )

        if nonempty(signal.get("summary")):
            unsupported = unsupported_concrete_tokens(signal["summary"], known_articles)
            if unsupported:
                errors.append(
                    f"{prefix}.summary introduces concrete ASCII identifiers/numbers absent from referenced article text: {unsupported}"
                )

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
