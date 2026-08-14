#!/usr/bin/env python3
"""Enforce manifest-derived period labels in reader-facing Special source.

This is deliberately targeted. Legitimate references to adjacent months in article
chronology are allowed; only structured issue-identity fields are checked/fixed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

SCOPE_RE = re.compile(
    r"(\\begin\{claimboundary\}\[Retrospective scope\]\s*\n)(.*?)(\n\\end\{claimboundary\})",
    re.DOTALL,
)
SCOPE_PERIOD_RE = re.compile(
    r"本号は\s*(\d{4})年(\d{1,2})月\s*を、?後日確認可能になった一次情報も用いて再構成するRetrospective Specialである。"
)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_timestamp(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    parsed = datetime.fromisoformat(normalized)
    if parsed.tzinfo is None:
        raise ValueError(f"coverage timestamp must include timezone: {value}")
    return parsed


def derive_period(edition: dict[str, Any]) -> dict[str, str]:
    coverage = edition.get("coverage") or {}
    start_text = str(coverage.get("start") or "")
    end_text = str(coverage.get("end") or "")
    if not start_text or not end_text:
        raise ValueError("Special edition coverage.start/end are required")
    start = parse_timestamp(start_text)
    end = parse_timestamp(end_text)
    if (start.year, start.month) != (end.year, end.month):
        raise ValueError("period consistency guard currently requires a single calendar-month coverage")
    return {
        "year_month": f"{start.year:04d}-{start.month:02d}",
        "ja": f"{start.year}年{start.month}月",
        "start_date": start.date().isoformat(),
        "end_date": end.date().isoformat(),
    }


def resolve_source(root: Path, issue_id: str, special_slug: str) -> tuple[Path, dict[str, Any], dict[str, Any], Path, dict[str, Any]]:
    edition_path = root / "specials" / special_slug / "edition.json"
    edition = load_json(edition_path)
    if edition.get("special_id") != issue_id or edition.get("special_slug") != special_slug:
        raise ValueError("issue/slug do not match edition manifest")

    state_path = root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    source = state.get("provenance", {}).get("validated_issue_source") or {}
    manifest_path = root / str(source.get("path") or "")
    if not manifest_path.is_file():
        raise ValueError("state-pinned source manifest is missing")
    if sha256_file(manifest_path) != source.get("sha256"):
        raise ValueError("state-pinned source manifest SHA mismatch")
    manifest = load_json(manifest_path)
    return edition_path, edition, state, manifest_path, manifest


def scope_body(frontmatter: str) -> str:
    match = SCOPE_RE.search(frontmatter)
    if not match:
        raise ValueError("Retrospective scope Claim Boundary not found")
    return match.group(2)


def check_structured_periods(root: Path, issue_id: str, special_slug: str) -> dict[str, Any]:
    edition_path, edition, state, manifest_path, manifest = resolve_source(root, issue_id, special_slug)
    expected = derive_period(edition)
    source_dir = manifest_path.parent
    front_rel = str((manifest.get("frontmatter") or {}).get("path") or "sections/00-frontmatter.tex")
    front_path = source_dir / front_rel
    main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
    main_path = source_dir / main_rel
    if not front_path.is_file() or not main_path.is_file():
        raise ValueError("reader-facing frontmatter/main.tex missing")

    front = front_path.read_text(encoding="utf-8")
    body = scope_body(front)
    period_match = SCOPE_PERIOD_RE.search(body)
    if not period_match:
        raise ValueError("Retrospective scope does not contain the structured monthly period sentence")
    actual_ja = f"{period_match.group(1)}年{int(period_match.group(2))}月"
    errors: list[str] = []
    if actual_ja != expected["ja"]:
        errors.append(f"Retrospective scope period mismatch: expected {expected['ja']}, got {actual_ja}")

    main = main_path.read_text(encoding="utf-8")
    coverage_re = re.compile(
        rf"\bCoverage(?::)?\s+{re.escape(expected['start_date'])}\s+--\s+{re.escape(expected['end_date'])}\b"
    )
    expected_window = f"Coverage window: {expected['start_date']} -- {expected['end_date']}"
    if issue_id not in main:
        errors.append(f"survey setup does not contain issue id {issue_id}")
    if not coverage_re.search(main):
        errors.append(
            "survey setup coverage mismatch: expected Coverage date range "
            f"{expected['start_date']} -- {expected['end_date']}"
        )
    if expected_window not in main:
        errors.append(f"coverage-window label mismatch: missing {expected_window}")

    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "edition_manifest": edition_path.relative_to(root).as_posix(),
        "source_manifest": manifest_path.relative_to(root).as_posix(),
        "expected_period": expected,
        "retrospective_scope_period": actual_ja,
        "passed": not errors,
        "errors": errors,
    }


def apply_scope_period(root: Path, issue_id: str, special_slug: str) -> dict[str, Any]:
    edition_path, edition, state, manifest_path, manifest = resolve_source(root, issue_id, special_slug)
    expected = derive_period(edition)
    source_dir = manifest_path.parent
    front_info = dict(manifest.get("frontmatter") or {})
    front_rel = str(front_info.get("path") or "sections/00-frontmatter.tex")
    front_path = source_dir / front_rel
    if not front_path.is_file():
        raise ValueError("frontmatter file is missing")

    original = front_path.read_text(encoding="utf-8")
    match = SCOPE_RE.search(original)
    if not match:
        raise ValueError("Retrospective scope Claim Boundary not found")
    body = match.group(2)
    period_match = SCOPE_PERIOD_RE.search(body)
    if not period_match:
        raise ValueError("structured Retrospective scope period sentence not found")
    old_ja = f"{period_match.group(1)}年{int(period_match.group(2))}月"
    replacement_sentence = (
        f"本号は{expected['ja']}を後日確認可能になった一次情報も用いて再構成するRetrospective Specialである。"
    )
    new_body = SCOPE_PERIOD_RE.sub(replacement_sentence, body, count=1)
    revised = original[: match.start(2)] + new_body + original[match.end(2) :]
    changed = revised != original
    if changed:
        front_path.write_text(revised, encoding="utf-8")
        front_info["path"] = front_rel
        front_info["sha256"] = sha256_file(front_path)
        manifest["frontmatter"] = front_info
        manifest.setdefault("period_consistency", {})
        manifest["period_consistency"] = {
            "source": "specials/<slug>/edition.json coverage",
            "expected_year_month": expected["year_month"],
            "reader_period_label": expected["ja"],
            "retrospective_scope_derived_from_manifest": True,
        }
        write_json(manifest_path, manifest)
        state["provenance"]["validated_issue_source"]["sha256"] = sha256_file(manifest_path)
        state["provenance"]["validated_issue_source"]["period_consistency"] = True
        write_json(root / "sources" / issue_id / "pipeline-state.json", state)

    report = check_structured_periods(root, issue_id, special_slug)
    if not report["passed"]:
        raise ValueError(f"period consistency check failed after apply: {report['errors']}")
    report.update({"status": "PERIOD_CONSISTENCY_APPLIED", "changed": changed, "previous_scope_period": old_ja})
    return report


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("command", choices=("apply", "check"))
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--issue-id", required=True)
    ap.add_argument("--special-slug", required=True)
    args = ap.parse_args()
    root = Path(args.repo_root).resolve()
    report = apply_scope_period(root, args.issue_id, args.special_slug) if args.command == "apply" else check_structured_periods(root, args.issue_id, args.special_slug)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report.get("passed", True) else 1


if __name__ == "__main__":
    raise SystemExit(main())
