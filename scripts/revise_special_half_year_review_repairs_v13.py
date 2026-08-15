#!/usr/bin/env python3
"""Make Half-year Technical Notes extraction event-bounded and re-enrichable.

The first source-specific pass proved that keyword extraction over a broad living-page
window can bind unrelated page chrome, later changelog entries, or background discussion
to the selected artifact. This layer narrows the source window before the existing
fail-closed synthesis runs:

* arXiv-like pages: Abstract only;
* changelog / living README pages: the target event-date slice only;
* standalone first-party pages: start at the target date, then prefer a nearby artifact
  title occurrence and never look backward into navigation/chrome;
* concise feed summaries: unchanged fallback when no date marker is present.

It also removes generic signals that were empirically unsafe (bare ``experimental``, bare
``OCR``, generic ``distillation``, and unqualified second/fps quantities). Existing
source-specific facts can be regenerated in a later immutable revision: the old technical
clause is first reset to the accepted chronology, then rebuilt from the newly bounded
provenance.
"""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v12 as base
from scripts import revise_special_half_year_review_repairs_v11 as suppression

impl = base.impl
core = impl.core

_UNSAFE_SIGNAL_NAMES = {
    "experimental release",
    "OCR",
    "model distillation",
}
_UNSAFE_DYNAMIC_PREFIXES = ("{0}s generation", "{0} fps")

# A few event-bounded first-party phrases that become visible only after navigation and
# living-page material are excluded.
_EVENT_BOUNDED_SIGNALS: tuple[tuple[str, str], ...] = (
    ("DeepSeek-V3 served through the existing deepseek-chat API alias", r"deepseek-chat model has been upgraded to DeepSeek-V3.{0,120}API remains unchanged"),
    ("guidance-distilled FLUX.1 [dev]", r"FLUX\.1\s*\[dev\].{0,120}guidance[- ]distilled"),
    ("FlashAttention-3 Hopper/TMA/WGMMA optimization", r"FlashAttention-3.{0,500}(?:Hopper|TMA|WGMMA)"),
)

_DATE_TOKEN_RE = re.compile(
    r"(?:Date:\s*)?(?:20\d{2}[-/]\d{1,2}[-/]\d{1,2}|(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\s+\d{1,2}(?:st|nd|rd|th)?,?\s+20\d{2}|\d{1,2}\s+(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*\s+20\d{2})",
    re.IGNORECASE,
)


def _date_variants(date: str) -> tuple[str, ...]:
    dt = datetime.strptime(str(date)[:10], "%Y-%m-%d")
    day = dt.day
    suffix = "th"
    if day % 10 == 1 and day != 11:
        suffix = "st"
    elif day % 10 == 2 and day != 12:
        suffix = "nd"
    elif day % 10 == 3 and day != 13:
        suffix = "rd"
    return (
        dt.strftime("%Y-%m-%d"),
        f"{dt.year}/{dt.month}/{dt.day}",
        dt.strftime("%B %d, %Y").replace(" 0", " "),
        dt.strftime("%b %d, %Y").replace(" 0", " "),
        f"{dt.strftime('%B')} {day}{suffix}, {dt.year}",
        f"{dt.strftime('%B')} {day}th, {dt.year}",
        f"{day} {dt.strftime('%B')} {dt.year}",
    )


def _abstract_window(summary: str) -> str:
    marker = re.search(r"\bAbstract:\s*", summary, flags=re.IGNORECASE)
    if marker is None:
        return ""
    tail = summary[marker.end() :]
    end = re.search(r"\b(?:Subjects:|Comments:|Submission history|Cite as:)\b", tail, flags=re.IGNORECASE)
    if end is not None:
        tail = tail[: end.start()]
    return tail[:5000].strip()


def _is_living_changelog(summary: str) -> bool:
    lowered = summary.lower()
    explicit = any(
        marker in lowered
        for marker in (
            "project updates",
            "change log",
            "changelog",
            "news : 20",
            "release date",
        )
    )
    return explicit or len(_DATE_TOKEN_RE.findall(summary)) >= 6


def _last_event_position(summary: str, events: list[tuple[str, str]]) -> int | None:
    lower = summary.lower()
    positions: list[int] = []
    for date, _kind in events:
        try:
            variants = _date_variants(date)
        except ValueError:
            continue
        for variant in variants:
            start = 0
            needle = variant.lower()
            while True:
                pos = lower.find(needle, start)
                if pos < 0:
                    break
                positions.append(pos)
                start = pos + max(1, len(needle))
    return max(positions) if positions else None


def _artifact_anchor(segment: str, title: str) -> int | None:
    title = str(title or "").strip()
    if not title:
        return None
    candidates = [title]
    # Evidence canonical titles sometimes omit release-page suffixes while the page uses the
    # same leading artifact identity. Preserve a meaningful token prefix as a secondary anchor.
    if ":" in title:
        candidates.append(title.split(":", 1)[0].strip())
    if " and " in title:
        candidates.append(title.split(" and ", 1)[0].strip())
    lower = segment.lower()
    hits: list[int] = []
    for candidate in candidates:
        if len(candidate) < 5:
            continue
        pos = lower.find(candidate.lower(), 40)
        if 0 <= pos <= 1800:
            hits.append(pos)
    return min(hits) if hits else None


def _safe_event_window(summary: str, events: list[tuple[str, str]], title: str = "") -> str:
    if not summary:
        return ""

    abstract = _abstract_window(summary)
    if abstract:
        return abstract

    pos = _last_event_position(summary, events)
    if pos is None:
        # Concise RSS/feed summaries often carry the full useful fact but no literal date.
        return summary[:4000]

    segment = summary[pos:]
    if _is_living_changelog(summary):
        # Never walk backward into later releases. Keep only the local event entry; a subsequent
        # dated entry marks the next changelog unit. The hard cap protects README tables that are
        # maintained independently of the dated release note.
        next_date = _DATE_TOKEN_RE.search(segment, 24)
        if next_date is not None:
            segment = segment[: next_date.start()]
        return segment[:900].strip()

    anchor = _artifact_anchor(segment, title)
    if anchor is not None:
        segment = segment[anchor:]
    return segment[:4200].strip()


def _safe_technical_signals(summary: str, events: list[tuple[str, str]], title: str = "") -> list[str]:
    window = _safe_event_window(summary, events, title)
    if not window:
        return []

    signals: list[str] = []
    for signal in impl._dynamic_signals(window):
        if signal not in signals:
            signals.append(signal)
    for display, pattern in impl._SIGNAL_PATTERNS:
        if display in _UNSAFE_SIGNAL_NAMES:
            continue
        if re.search(pattern, window, flags=re.IGNORECASE | re.DOTALL) and display not in signals:
            signals.append(display)
        if len(signals) >= 7:
            break
    return signals[:7]


def _screening_index_with_source_type(repo_root: Path, issue_id: str) -> tuple[dict[str, dict[str, Any]], Path]:
    by_url, queue_path = impl._screening_index(repo_root, issue_id)
    # Re-read only the already hash-verified queue to attach source_type. Identity and content are
    # still inherited from the accepted queue; no new source is introduced.
    source_type_by_id: dict[str, str] = {}
    for raw in queue_path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        row = json.loads(raw)
        record = row.get("record") or {}
        screening_id = str(row.get("screening_id") or record.get("screening_id") or "")
        source_type_by_id[screening_id] = str(record.get("source_type") or "")
    for record in by_url.values():
        record["source_type"] = source_type_by_id.get(str(record.get("screening_id") or ""), "")
    return by_url, queue_path


def _merge_event_bounded(repo_root: Path, manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    index = impl._ORIGINAL_MERGE(repo_root, manifest)
    issue_id = str(manifest.get("issue_id") or "").strip()
    if not issue_id:
        raise ValueError("source manifest missing issue_id")
    screening_by_url, queue_path = _screening_index_with_source_type(repo_root, issue_id)
    queue_sha = impl._sha256(queue_path)
    for override_title, override in impl._ACTIVE_OVERRIDES.items():
        expected_queue_sha = str(override.get("_expected_queue_sha256") or "").strip()
        if expected_queue_sha != queue_sha:
            raise ValueError(
                f"Technical Notes detail override Screening digest mismatch for {override_title}: "
                f"actual={queue_sha} expected={expected_queue_sha}"
            )

    seen: set[int] = set()
    for title, info in list(index.items()):
        identity = id(info)
        if identity in seen:
            continue
        seen.add(identity)
        canonical_title = str(info.get("canonical_title") or title)
        records: list[dict[str, Any]] = []
        for url in info.get("urls") or []:
            record = screening_by_url.get(impl._normalize_url(str(url)))
            if record is not None and record not in records:
                records.append(record)
        if not records:
            raise ValueError(
                f"Selected Evidence has no matching accepted Screening provenance for Technical Notes: "
                f"{canonical_title} urls={info.get('urls')}"
            )
        info["screening_records"] = records
        info["screening_queue_path"] = queue_path.relative_to(repo_root).as_posix()
        info["screening_queue_sha256"] = queue_sha

        override = impl._ACTIVE_OVERRIDES.get(canonical_title)
        if override is not None:
            points = impl._validate_override(canonical_title, override, info)
            info["technical_points"] = points
            info["technical_point_mode"] = "EDITORIAL_OVERRIDE"
            continue

        signals: list[str] = []
        events = list(info.get("events") or [])
        for record in records:
            for signal in _safe_technical_signals(
                str(record.get("summary_text") or ""),
                events,
                canonical_title,
            ):
                if signal not in signals:
                    signals.append(signal)
                if len(signals) >= 7:
                    break
            if len(signals) >= 7:
                break
        if not signals:
            raise ValueError(
                f"Event-bounded accepted Screening provenance is too thin for reader-facing Technical Notes: "
                f"{canonical_title}. Provide a hash-bound editorial technical-point override instead of widening the source window."
            )
        info["technical_points"] = [
            "対象event近傍の一次資料から " + " / ".join(signals) + " を確認できる。"
        ]
        info["technical_point_mode"] = "EVENT_BOUNDED_SCREENING_SIGNAL_EXTRACTION"
    return index


def _reset_existing_fact_lines(path: Path, evidence: dict[str, dict[str, Any]]) -> str:
    original = path.read_text(encoding="utf-8")
    changes: list[tuple[int, int, str]] = []
    for match in core.NOTE_RE.finditer(original):
        title = match.group(1)
        info = evidence.get(title)
        if info is None or info.get("suppress_reader_facing_card") is True:
            continue
        chronology = impl._ORIGINAL_FACT(str(info.get("canonical_title") or title), info)
        block = match.group(0)
        lines = block.splitlines()
        found = 0
        for i, line in enumerate(lines):
            if line.startswith(r"\item \textbf{一次情報で確認できる事実}: "):
                lines[i] = r"\item \textbf{一次情報で確認できる事実}: " + core.tex_escape(chronology)
                found += 1
        if found != 1:
            raise ValueError(f"Technical Notes fact reset expected exactly one fact line: {title} found={found}")
        revised = "\n".join(lines)
        changes.append((match.start(), match.end(), revised))
    text = original
    for start, end, revised in reversed(changes):
        text = text[:start] + revised + text[end:]
    path.write_text(text, encoding="utf-8")
    return original


_ORIGINAL_SUPPRESSION_REPAIR = suppression.repair_note_file


def _reenrich_note_file(path: Path, evidence: dict[str, dict[str, Any]]) -> tuple[int, int, int]:
    original = _reset_existing_fact_lines(path, evidence)
    try:
        return _ORIGINAL_SUPPRESSION_REPAIR(path, evidence)
    except Exception:
        path.write_text(original, encoding="utf-8")
        raise


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous_patterns = impl._SIGNAL_PATTERNS
    previous_dynamic = impl._DYNAMIC_PATTERNS
    previous_suppression_repair = suppression.repair_note_file
    previous_merge = impl.merge_evidence_index

    safe_patterns = tuple((name, pattern) for name, pattern in previous_patterns if name not in _UNSAFE_SIGNAL_NAMES)
    safe_dynamic = tuple(item for item in previous_dynamic if item[0] not in _UNSAFE_DYNAMIC_PREFIXES)
    impl._SIGNAL_PATTERNS = _EVENT_BOUNDED_SIGNALS + safe_patterns
    impl._DYNAMIC_PATTERNS = safe_dynamic
    suppression.repair_note_file = _reenrich_note_file
    impl.merge_evidence_index = _merge_event_bounded
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
        if isinstance(result, dict):
            result["technical_note_semantic_binding"] = "EVENT_BOUNDED_V1"
            result["unsafe_signal_classes_removed"] = sorted(_UNSAFE_SIGNAL_NAMES)
            result["unqualified_duration_signals_removed"] = True
        return result
    finally:
        impl._SIGNAL_PATTERNS = previous_patterns
        impl._DYNAMIC_PATTERNS = previous_dynamic
        suppression.repair_note_file = previous_suppression_repair
        impl.merge_evidence_index = previous_merge


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
