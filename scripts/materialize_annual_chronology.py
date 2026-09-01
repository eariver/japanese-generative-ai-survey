#!/usr/bin/env python3
"""Materialize an annual reader-facing chronology from accepted Screening metadata.

Annual narrative drafting intentionally compresses events into story units and
trajectories. This recovery/expansion step restores objective event resolution
without reopening Raw sources or inventing dates: it consumes the accepted
Screening verification queue, keeps records with explicit ``published_at``
metadata, sorts them chronologically, writes a compact reader-facing TeX index,
and records the exact source locator for auditability.

The script operates only on an already-expanded source revision. It changes no
Architecture role or article prose outside the annual-chronology layout body.
"""
from __future__ import annotations

import argparse
import email.utils
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_instant(value: str) -> datetime:
    text = value.strip()
    normalized = text[:-1] + "+00:00" if text.endswith("Z") else text
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        try:
            parsed = email.utils.parsedate_to_datetime(text)
        except (TypeError, ValueError, OverflowError) as exc:
            raise ValueError(f"unsupported chronology timestamp: {value!r}") from exc
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def tex_escape(value: str) -> str:
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(char, char) for char in value)


def accepted_screening_run(source_root: Path) -> tuple[Path, dict[str, Any]]:
    runs = source_root / "screening" / "runs"
    accepted: list[tuple[Path, dict[str, Any]]] = []
    if runs.is_dir():
        for directory in runs.iterdir():
            if not directory.is_dir():
                continue
            acceptance_path = directory / "acceptance.json"
            if not acceptance_path.is_file():
                continue
            value = load_json(acceptance_path)
            if value.get("status") == "ACCEPTED":
                accepted.append((directory, value))
    if len(accepted) != 1:
        raise ValueError(f"expected exactly one accepted Screening run, found {len(accepted)}")
    return accepted[0]


def collect_events(queue_path: Path, start: datetime, end: datetime) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    events: list[dict[str, Any]] = []
    unresolved: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for line_no, raw in enumerate(queue_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        item = json.loads(raw)
        if not isinstance(item, dict):
            raise ValueError(f"{queue_path}:{line_no}: expected object")
        record = item.get("record")
        screening = item.get("screening")
        if not isinstance(record, dict) or not isinstance(screening, dict):
            raise ValueError(f"{queue_path}:{line_no}: record/screening missing")
        if screening.get("decision") not in {"KEEP", "MAYBE", "INSPECT"}:
            continue
        title = str(record.get("title") or "").strip()
        locator = str(record.get("locator") or "").strip()
        published_at = record.get("published_at")
        base = {
            "screening_id": item.get("screening_id"),
            "title": title,
            "locator": locator,
            "source_type": record.get("source_type"),
            "duplicate_group": screening.get("duplicate_group"),
        }
        if not isinstance(published_at, str) or not published_at.strip():
            unresolved.append({**base, "reason": "published_at unavailable in accepted Screening record"})
            continue
        instant = parse_instant(published_at)
        if not (start <= instant <= end):
            raise ValueError(
                f"accepted annual chronology record outside coverage: {item.get('screening_id')} {published_at}"
            )
        key = (instant.isoformat(), locator)
        if key in seen:
            continue
        seen.add(key)
        events.append({**base, "published_at": published_at, "date": instant.date().isoformat()})
    events.sort(key=lambda item: (parse_instant(item["published_at"]), item["title"], item["screening_id"] or ""))
    unresolved.sort(key=lambda item: (item["title"], item["screening_id"] or ""))
    return events, unresolved


def render_tex(events: list[dict[str, Any]], unresolved: list[dict[str, Any]]) -> str:
    lines = [
        "% Generated from accepted annual Screening chronology metadata. Do not hand-edit.",
        "\\noindent 日付は一次資料または論文メタデータで確認できた公開時点を採用し、後年の提供状態を遡及して補わない。",
        "\\par\\medskip",
    ]
    current_month: str | None = None
    for event in events:
        month = event["date"][:7]
        if month != current_month:
            current_month = month
            month_number = int(month[5:7])
            lines.extend(["\\medskip", f"\\noindent\\textbf{{{month_number}月}}\\par", "\\smallskip"])
        lines.extend(
            [
                f"\\noindent\\textbf{{{tex_escape(event['date'])}}}\\par",
                f"{{\\raggedright {tex_escape(event['title'])}\\par}}",
                "\\smallskip",
            ]
        )
    if unresolved:
        lines.extend([
            "\\medskip",
            "\\begin{claimboundary}[日付精度の境界]",
            f"公開日の精度を一次記録から確定できなかった retained record が {len(unresolved)} 件ある。"
            "Chronology では推測日を補わず、監査記録に未解決として残す。",
            "\\end{claimboundary}",
        ])
    lines.append("")
    return "\n".join(lines)


def materialize(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    if not special_slug.endswith("-Y"):
        return {
            "schema_version": "1.0",
            "issue_id": issue_id,
            "special_slug": special_slug,
            "status": "SKIP_NOT_ANNUAL",
            "event_count": 0,
        }

    manifest_path = repo_root / "specials" / special_slug / "edition.json"
    edition = load_json(manifest_path)
    if edition.get("special_id") != issue_id or edition.get("special_slug") != special_slug:
        raise ValueError("edition identity mismatch")
    start = parse_instant(edition["coverage"]["start"])
    end = parse_instant(edition["coverage"]["end"])

    source_root = repo_root / "sources" / issue_id
    screening_dir, screening_acceptance = accepted_screening_run(source_root)
    queue_path = screening_dir / "verification-queue.jsonl"
    if not queue_path.is_file():
        raise ValueError(f"accepted Screening verification queue missing: {queue_path}")
    events, unresolved = collect_events(queue_path, start, end)
    if not events:
        raise ValueError("annual chronology has no dated retained records")

    revision_root = repo_root / "surveys" / "special" / special_slug / "revisions" / source_version
    source_manifest_path = revision_root / "source-manifest.json"
    source_manifest = load_json(source_manifest_path)
    if source_manifest.get("issue_id") != issue_id or source_manifest.get("source_version") != source_version:
        raise ValueError("expanded source manifest identity mismatch")

    rows = [row for row in source_manifest.get("articles", []) if row.get("package_id") == "annual-chronology"]
    if len(rows) != 1:
        raise ValueError(f"expected one annual-chronology article row, found {len(rows)}")
    row = rows[0]
    body_rel = row.get("layout_body_path")
    if not isinstance(body_rel, str) or not body_rel:
        raise ValueError("annual-chronology expanded article lacks layout_body_path")
    body_path = revision_root / body_rel
    body_path.write_text(render_tex(events, unresolved), encoding="utf-8")
    body_sha = sha256_file(body_path)
    row["layout_body_sha256"] = body_sha
    row["layout_transform"] = (
        "approved annual chronology package expanded from accepted Screening published_at metadata; "
        "date and title use separate reader-facing lines to preserve source titles without two-column justification warnings; "
        "source-date precision and unresolved dates remain unresolved"
    )

    audit_rel = Path("sources") / issue_id / "chronology" / f"annual-chronology-{source_version}.json"
    audit_path = repo_root / audit_rel
    audit = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "special_slug": special_slug,
        "source_version": source_version,
        "status": "MATERIALIZED",
        "coverage_start": edition["coverage"]["start"],
        "coverage_end": edition["coverage"]["end"],
        "screening_result_set_sha256": screening_acceptance.get("result_set_sha256"),
        "verification_queue_path": queue_path.relative_to(repo_root).as_posix(),
        "verification_queue_sha256": sha256_file(queue_path),
        "event_count": len(events),
        "unresolved_date_count": len(unresolved),
        "events": events,
        "unresolved_dates": unresolved,
        "reader_facing_path": body_path.relative_to(repo_root).as_posix(),
        "reader_facing_sha256": body_sha,
        "rules": [
            "Only accepted Screening records with explicit published_at metadata are materialized.",
            "No missing date is inferred or back-filled.",
            "All materialized dates must fall inside the exact annual coverage window.",
            "The source locator is preserved in this audit even though the compact reader chronology omits raw URLs.",
        ],
    }
    write_json(audit_path, audit)
    source_manifest["annual_chronology"] = {
        "status": "MATERIALIZED_FROM_ACCEPTED_SCREENING_METADATA",
        "event_count": len(events),
        "unresolved_date_count": len(unresolved),
        "audit_path": audit_rel.as_posix(),
        "audit_sha256": sha256_file(audit_path),
        "reader_facing_path": body_rel,
        "reader_facing_sha256": body_sha,
    }
    write_json(source_manifest_path, source_manifest)

    state_path = source_root / "pipeline-state.json"
    state = load_json(state_path)
    provenance = state.setdefault("provenance", {})
    validated = provenance.get("validated_issue_source")
    if not isinstance(validated, dict) or validated.get("path") != source_manifest_path.relative_to(repo_root).as_posix():
        raise ValueError("pipeline validated_issue_source does not point to expanded source manifest")
    validated["sha256"] = sha256_file(source_manifest_path)
    provenance["annual_chronology"] = {
        "source_version": source_version,
        "path": audit_rel.as_posix(),
        "sha256": sha256_file(audit_path),
        "event_count": len(events),
        "unresolved_date_count": len(unresolved),
    }
    write_json(state_path, state)
    return audit


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    parser.add_argument("--audit-output")
    args = parser.parse_args()
    audit = materialize(Path(args.repo_root), args.special_slug, args.issue_id, args.source_version)
    if args.audit_output:
        write_json(Path(args.audit_output), audit)
    print(json.dumps(audit, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
