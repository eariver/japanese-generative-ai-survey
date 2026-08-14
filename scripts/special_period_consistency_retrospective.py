#!/usr/bin/env python3
"""Manifest-derived period consistency for monthly and multi-month Specials."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from scripts import special_period_consistency as legacy

SCOPE_LABEL_RE = re.compile(
    r"本号は(?P<label>[^\n]+?)を、?後日確認可能になった一次情報も用いて再構成するRetrospective Specialである。"
)
SIGNAL_HEADING_RE = re.compile(r"\\section\*\{(?P<title>[^{}]+ Signals)\}")


def display_period_label(edition: dict[str, Any]) -> str:
    label = str(edition.get("display_label") or "").strip()
    if label.endswith(" Retrospective"):
        label = label[: -len(" Retrospective")].strip()
    if label:
        return label
    coverage = edition.get("coverage") or {}
    start = legacy.parse_timestamp(str(coverage.get("start") or ""))
    end = legacy.parse_timestamp(str(coverage.get("end") or ""))
    if (start.year, start.month) == (end.year, end.month):
        return f"{start.year}年{start.month}月"
    if start.year == end.year:
        return f"{start.year}年{start.month}月〜{end.month}月"
    return f"{start.year}年{start.month}月〜{end.year}年{end.month}月"


def signal_section_title(edition: dict[str, Any]) -> str:
    return "Retrospective Signals" if edition.get("edition_kind") == "RETROSPECTIVE_PERIOD" else "Monthly Signals"


def derive_period(edition: dict[str, Any]) -> dict[str, str]:
    coverage = edition.get("coverage") or {}
    start = legacy.parse_timestamp(str(coverage.get("start") or ""))
    end = legacy.parse_timestamp(str(coverage.get("end") or ""))
    if end < start:
        raise ValueError("coverage.end must not precede coverage.start")
    value = {
        "label": display_period_label(edition),
        "start_date": start.date().isoformat(),
        "end_date": end.date().isoformat(),
    }
    if (start.year, start.month) == (end.year, end.month):
        value["year_month"] = f"{start.year:04d}-{start.month:02d}"
    return value


def _resolve(root: Path, issue_id: str, special_slug: str):
    return legacy.resolve_source(root, issue_id, special_slug)


def check_structured_periods(root: Path, issue_id: str, special_slug: str) -> dict[str, Any]:
    edition_path, edition, _state, manifest_path, manifest = _resolve(root, issue_id, special_slug)
    expected = derive_period(edition)
    expected_signal_title = signal_section_title(edition)
    source_dir = manifest_path.parent
    front_rel = str((manifest.get("frontmatter") or {}).get("path") or "sections/00-frontmatter.tex")
    main_rel = str((manifest.get("main_tex") or {}).get("path") or "main.tex")
    front_path = source_dir / front_rel
    main_path = source_dir / main_rel
    if not front_path.is_file() or not main_path.is_file():
        raise ValueError("reader-facing frontmatter/main.tex missing")

    front_text = front_path.read_text(encoding="utf-8")
    body = legacy.scope_body(front_text)
    match = SCOPE_LABEL_RE.search(body)
    if not match:
        raise ValueError("Retrospective scope does not contain the structured period sentence")
    actual = match.group("label").strip()
    errors: list[str] = []
    if actual != expected["label"]:
        errors.append(f"Retrospective scope period mismatch: expected {expected['label']}, got {actual}")

    signal_match = SIGNAL_HEADING_RE.search(front_text)
    actual_signal_title = signal_match.group("title") if signal_match else None
    if actual_signal_title is not None and actual_signal_title != expected_signal_title:
        errors.append(
            f"reader signal heading mismatch: expected {expected_signal_title}, got {actual_signal_title}"
        )
    if signal_match and f"\\addcontentsline{{toc}}{{section}}{{{expected_signal_title}}}" not in front_text:
        errors.append(f"reader signal TOC heading mismatch: expected {expected_signal_title}")

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
        "retrospective_scope_period": actual,
        "expected_signal_heading": expected_signal_title,
        "reader_signal_heading": actual_signal_title,
        "passed": not errors,
        "errors": errors,
    }


def apply_scope_period(root: Path, issue_id: str, special_slug: str) -> dict[str, Any]:
    edition_path, edition, state, manifest_path, manifest = _resolve(root, issue_id, special_slug)
    expected = derive_period(edition)
    expected_signal_title = signal_section_title(edition)
    source_dir = manifest_path.parent
    front_info = dict(manifest.get("frontmatter") or {})
    front_rel = str(front_info.get("path") or "sections/00-frontmatter.tex")
    front_path = source_dir / front_rel
    if not front_path.is_file():
        raise ValueError("frontmatter file is missing")

    original = front_path.read_text(encoding="utf-8")
    scope_match = legacy.SCOPE_RE.search(original)
    if not scope_match:
        raise ValueError("Retrospective scope Claim Boundary not found")
    body = scope_match.group(2)
    label_match = SCOPE_LABEL_RE.search(body)
    if not label_match:
        raise ValueError("structured Retrospective scope period sentence not found")
    previous = label_match.group("label").strip()
    replacement = (
        f"本号は{expected['label']}を後日確認可能になった一次情報も用いて再構成するRetrospective Specialである。"
    )
    new_body = SCOPE_LABEL_RE.sub(replacement, body, count=1)
    revised = original[: scope_match.start(2)] + new_body + original[scope_match.end(2) :]

    signal_match = SIGNAL_HEADING_RE.search(revised)
    previous_signal_title = signal_match.group("title") if signal_match else None
    if signal_match:
        revised = SIGNAL_HEADING_RE.sub(
            rf"\\section*{{{expected_signal_title}}}", revised, count=1
        )
        for known_title in ("Monthly Signals", "Retrospective Signals"):
            revised = revised.replace(
                f"\\addcontentsline{{toc}}{{section}}{{{known_title}}}",
                f"\\addcontentsline{{toc}}{{section}}{{{expected_signal_title}}}",
            )

    changed = revised != original
    if changed:
        front_path.write_text(revised, encoding="utf-8")
        front_info["path"] = front_rel
        front_info["sha256"] = legacy.sha256_file(front_path)
        manifest["frontmatter"] = front_info
        consistency = {
            "source": "specials/<slug>/edition.json coverage/display_label",
            "reader_period_label": expected["label"],
            "retrospective_scope_derived_from_manifest": True,
            "signal_heading": expected_signal_title,
            "signal_heading_derived_from_edition_kind": True,
        }
        if "year_month" in expected:
            consistency["expected_year_month"] = expected["year_month"]
        manifest["period_consistency"] = consistency
        legacy.write_json(manifest_path, manifest)
        state["provenance"]["validated_issue_source"]["sha256"] = legacy.sha256_file(manifest_path)
        state["provenance"]["validated_issue_source"]["period_consistency"] = True
        legacy.write_json(root / "sources" / issue_id / "pipeline-state.json", state)

    report = check_structured_periods(root, issue_id, special_slug)
    if not report["passed"]:
        raise ValueError(f"period consistency check failed after apply: {report['errors']}")
    report.update(
        {
            "status": "PERIOD_CONSISTENCY_APPLIED",
            "changed": changed,
            "previous_scope_period": previous,
            "previous_signal_heading": previous_signal_title,
        }
    )
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
