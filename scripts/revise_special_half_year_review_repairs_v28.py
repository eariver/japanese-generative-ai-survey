#!/usr/bin/env python3
"""Limit Half-year Technical Note enrichment and rewrites to reader-rendered files.

The selected Evidence set also contains chronology-only and other non-card roles. Earlier
fail-closed enrichment walked every selected Evidence record and the lower repair chain rewrote
every manifest Technical Notes file, even when that file was no longer included by the published
``main.tex``. That is the wrong scope: provenance must remain strict for rendered cards, while
chronology-only or retired note files should keep their Evidence/source identity without
inventing a reader claim solely to satisfy regeneration.

V28 preserves the V3 component/variant/property binding contract and changes only the reader
surface scope. It derives rendered Technical Note files from the state-pinned ``main.tex`` input
graph, applies Screening-backed signal extraction / hash-bound overrides only to cards in those
files, and guards the downstream re-enrichment hook so retired note files are copied unchanged.
This matches Publication Preview preflight's rendered-file boundary.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v13 as event
from scripts import revise_special_half_year_review_repairs_v27 as base

_INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
_ACTIVE_RENDERED_NOTE_PATHS: set[str] = set()
_ORIGINAL_REENRICH_NOTE_FILE = event._reenrich_note_file


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def _title_key(value: str) -> str:
    text = str(value or "")
    for encoded, plain in (
        (r"\&", "&"),
        (r"\_", "_"),
        (r"\%", "%"),
        (r"\#", "#"),
        (r"\{", "{"),
        (r"\}", "}"),
    ):
        text = text.replace(encoded, plain)
    return re.sub(r"\s+", " ", text).strip().lower()


def _normalize_tex_path(value: str) -> str:
    text = str(value or "").strip().replace("\\", "/")
    while text.startswith("./"):
        text = text[2:]
    if text and not Path(text).suffix:
        text += ".tex"
    return Path(text).as_posix() if text else ""


def _state_pinned_rendered_note_context(
    repo_root: Path, manifest: dict[str, Any]
) -> tuple[Path, dict[str, Any], set[str]]:
    issue_id = str(manifest.get("issue_id") or "").strip()
    if not issue_id:
        raise ValueError("source manifest missing issue_id")
    state = _load_json(repo_root / "sources" / issue_id / "pipeline-state.json")
    source = (state.get("provenance") or {}).get("validated_issue_source") or {}
    manifest_rel = str(source.get("path") or "")
    current_manifest_path = repo_root / manifest_rel
    if not manifest_rel or not current_manifest_path.is_file():
        raise ValueError("state-pinned validated source manifest missing while resolving rendered Technical Notes")
    current_manifest = _load_json(current_manifest_path)
    source_dir = current_manifest_path.parent

    main_info = current_manifest.get("main_tex")
    main_rel = "main.tex"
    if isinstance(main_info, dict):
        main_rel = _normalize_tex_path(str(main_info.get("path") or main_rel))
    main_path = source_dir / main_rel
    if not main_path.is_file():
        raise ValueError(f"state-pinned main TeX missing while resolving rendered Technical Notes: {main_rel}")
    inputs = {
        _normalize_tex_path(match.group(1))
        for match in _INPUT_RE.finditer(main_path.read_text(encoding="utf-8"))
        if _normalize_tex_path(match.group(1))
    }

    rendered_paths: set[str] = set()
    for article in current_manifest.get("articles") or []:
        if not isinstance(article, dict) or article.get("technical_notes_reader_facing") is not True:
            continue
        rel = _normalize_tex_path(str(article.get("technical_notes_path") or ""))
        if rel and rel in inputs:
            rendered_paths.add(rel)
    if not rendered_paths:
        raise ValueError("state-pinned main TeX contains no rendered reader-facing Technical Notes files")
    return source_dir, current_manifest, rendered_paths


def _rendered_technical_note_paths(repo_root: Path, manifest: dict[str, Any]) -> set[str]:
    return _state_pinned_rendered_note_context(repo_root, manifest)[2]


def _rendered_technical_note_titles(repo_root: Path, manifest: dict[str, Any]) -> set[str]:
    source_dir, _current_manifest, rendered_paths = _state_pinned_rendered_note_context(repo_root, manifest)
    titles: set[str] = set()
    for rel in sorted(rendered_paths):
        path = source_dir / rel
        if not path.is_file():
            raise ValueError(f"state-pinned rendered Technical Notes file missing: {rel}")
        for match in event.core.NOTE_RE.finditer(path.read_text(encoding="utf-8")):
            titles.add(_title_key(match.group(1)))
    if not titles:
        raise ValueError("state-pinned rendered Technical Notes files contain no cards")
    return titles


def _technical_note_rel(path: Path) -> str:
    """Recover ``technical-notes/...`` identity from copied revision paths."""
    normalized = path.as_posix()
    marker = "/technical-notes/"
    if marker in normalized:
        return "technical-notes/" + normalized.split(marker, 1)[1]
    if normalized.startswith("technical-notes/"):
        return normalized
    return path.name


def _reenrich_rendered_note_file(
    path: Path, evidence: dict[str, dict[str, Any]]
) -> tuple[int, int, int]:
    rel = _technical_note_rel(path)
    if rel not in _ACTIVE_RENDERED_NOTE_PATHS:
        # The immutable revision was copied from the current validated source. A non-rendered
        # Technical Notes file is historical/supporting material only; preserving it byte-for-byte
        # is safer than requiring or synthesizing new reader-facing technical points.
        return 0, 0, 0
    return _ORIGINAL_REENRICH_NOTE_FILE(path, evidence)


def _merge_rendered_scope(repo_root: Path, manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    index = event.impl._ORIGINAL_MERGE(repo_root, manifest)
    issue_id = str(manifest.get("issue_id") or "").strip()
    if not issue_id:
        raise ValueError("source manifest missing issue_id")
    rendered_titles = _rendered_technical_note_titles(repo_root, manifest)
    screening_by_url, queue_path = event._screening_index_with_source_type(repo_root, issue_id)
    queue_sha = event.impl._sha256(queue_path)

    for override_title, override in event.impl._ACTIVE_OVERRIDES.items():
        if _title_key(override_title) not in rendered_titles:
            continue
        expected_queue_sha = str(override.get("_expected_queue_sha256") or "").strip()
        if expected_queue_sha != queue_sha:
            raise ValueError(
                f"Technical Notes detail override Screening digest mismatch for {override_title}: "
                f"actual={queue_sha} expected={expected_queue_sha}"
            )

    seen: set[int] = set()
    enriched = 0
    skipped_nonrendered = 0
    for title, info in list(index.items()):
        identity = id(info)
        if identity in seen:
            continue
        seen.add(identity)
        canonical_title = str(info.get("canonical_title") or title)
        if _title_key(canonical_title) not in rendered_titles:
            skipped_nonrendered += 1
            continue

        records: list[dict[str, Any]] = []
        for url in info.get("urls") or []:
            record = screening_by_url.get(event.impl._normalize_url(str(url)))
            if record is not None and record not in records:
                records.append(record)
        if not records:
            raise ValueError(
                f"Rendered selected Evidence has no matching accepted Screening provenance for Technical Notes: "
                f"{canonical_title} urls={info.get('urls')}"
            )
        info["screening_records"] = records
        info["screening_queue_path"] = queue_path.relative_to(repo_root).as_posix()
        info["screening_queue_sha256"] = queue_sha

        override = event.impl._ACTIVE_OVERRIDES.get(canonical_title)
        if override is not None:
            points = event.impl._validate_override(canonical_title, override, info)
            info["technical_points"] = points
            info["technical_point_mode"] = "EDITORIAL_OVERRIDE"
            enriched += 1
            continue

        signals: list[str] = []
        events = list(info.get("events") or [])
        for record in records:
            for signal in event._safe_technical_signals(
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
        enriched += 1

    manifest.setdefault("_technical_note_enrichment_scope", {})
    if isinstance(manifest["_technical_note_enrichment_scope"], dict):
        manifest["_technical_note_enrichment_scope"].update(
            {
                "rendered_title_count": len(rendered_titles),
                "enriched_record_count": enriched,
                "skipped_nonrendered_record_count": skipped_nonrendered,
                "rendered_file_scope": "STATE_PINNED_MAIN_TEX_INPUTS_ONLY",
            }
        )
    return index


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    global _ACTIVE_RENDERED_NOTE_PATHS
    previous_merge = event._merge_event_bounded
    previous_reenrich = event._reenrich_note_file
    marker_manifest = {"issue_id": issue_id}
    _ACTIVE_RENDERED_NOTE_PATHS = _rendered_technical_note_paths(repo_root, marker_manifest)
    event._merge_event_bounded = _merge_rendered_scope
    event._reenrich_note_file = _reenrich_rendered_note_file
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        event._merge_event_bounded = previous_merge
        event._reenrich_note_file = previous_reenrich
        _ACTIVE_RENDERED_NOTE_PATHS = set()
    if isinstance(result, dict):
        result["technical_note_enrichment_scope"] = "STATE_PINNED_MAIN_TEX_RENDERED_CARDS_AND_REWRITES_ONLY_V3"
    return result


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
