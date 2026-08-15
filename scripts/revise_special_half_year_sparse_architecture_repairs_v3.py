#!/usr/bin/env python3
"""Legacy reader-surface compatibility for sparse Half-year repairs.

Early validated source manifests predate the per-article ``technical_notes_reader_facing`` flag.
Their ``main.tex`` nevertheless directly renders the Technical Notes files.  V28 intentionally
requires the flag for modern manifests, so this wrapper relaxes only the legacy *absence* case:
an article is reader-facing when its Technical Notes path is directly input by the state-pinned
main TeX unless the manifest explicitly sets ``technical_notes_reader_facing`` to false.

Sparse early Half-year Evidence can also predate structured chronology on paper-only cards.  The
current repair chain must not turn that absence into a reader-facing ``時系列 —`` placeholder or
abort after a source-specific technical-point override has already been validated.  For this legacy
path only, an eventless card may use its fail-closed ``technical_points`` payload as the primary-fact
sentence; cards with chronology still use the ordinary chronology renderer, and cards without either
chronology or source-specific technical points continue to fail closed.

The first H1 renderer also emitted some generic fact bullets under the literal label ``Author claim``
instead of ``一次情報で確認できる事実``.  During re-enrichment we normalize exactly one such legacy
generic bullet to the current primary-fact label.  This is deliberately content-bound: a non-generic
Author claim is never rewritten, and ambiguous/multiple matches still fail closed.

The semantic/provenance repair itself remains v2 and therefore the current v30 fail-closed chain.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v13 as resetter
from scripts import revise_special_half_year_review_repairs_v28 as rendered
from scripts import revise_special_half_year_review_repairs_v4 as facts
from scripts import revise_special_half_year_sparse_architecture_repairs_v2 as base


_LEGACY_GENERIC_FACT_MARKERS = (
    '一次資料で「',
    '数値や能力に関する評価は、提供元・プロジェクト・著者の主張として扱う',
)


def _legacy_rendered_note_context(
    repo_root: Path, manifest: dict[str, Any]
) -> tuple[Path, dict[str, Any], set[str]]:
    issue_id = str(manifest.get("issue_id") or "").strip()
    if not issue_id:
        raise ValueError("source manifest missing issue_id")
    state = rendered._load_json(repo_root / "sources" / issue_id / "pipeline-state.json")
    source = (state.get("provenance") or {}).get("validated_issue_source") or {}
    manifest_rel = str(source.get("path") or "")
    current_manifest_path = repo_root / manifest_rel
    if not manifest_rel or not current_manifest_path.is_file():
        raise ValueError("state-pinned validated source manifest missing while resolving rendered Technical Notes")
    current_manifest = rendered._load_json(current_manifest_path)
    source_dir = current_manifest_path.parent

    main_info = current_manifest.get("main_tex")
    main_rel = "main.tex"
    if isinstance(main_info, dict):
        main_rel = rendered._normalize_tex_path(str(main_info.get("path") or main_rel))
    main_path = source_dir / main_rel
    if not main_path.is_file():
        raise ValueError(f"state-pinned main TeX missing while resolving rendered Technical Notes: {main_rel}")
    inputs = {
        rendered._normalize_tex_path(match.group(1))
        for match in rendered._INPUT_RE.finditer(main_path.read_text(encoding="utf-8"))
        if rendered._normalize_tex_path(match.group(1))
    }

    rendered_paths: set[str] = set()
    legacy_absent_flags = 0
    for article in current_manifest.get("articles") or []:
        if not isinstance(article, dict):
            continue
        if article.get("technical_notes_reader_facing") is False:
            continue
        if "technical_notes_reader_facing" not in article:
            legacy_absent_flags += 1
        rel = rendered._normalize_tex_path(str(article.get("technical_notes_path") or ""))
        if rel and rel in inputs:
            rendered_paths.add(rel)
    if not rendered_paths:
        raise ValueError("state-pinned main TeX contains no rendered Technical Notes files under legacy-compatible detection")
    if legacy_absent_flags < 1:
        # Do not silently weaken the modern contract. Sparse compatibility should only invoke this
        # path for genuinely legacy manifests missing the field.
        raise ValueError("legacy rendered-note compatibility requested but no article flags are absent")
    return source_dir, current_manifest, rendered_paths


def _eventless_source_specific_fact(title: str, info: dict[str, Any], original: Any) -> str:
    events = list(info.get("events") or [])
    if events:
        return original(title, info)

    points = [
        str(point).strip()
        for point in (info.get("technical_points") or [])
        if str(point).strip()
    ]
    if not points:
        # Preserve the ordinary fail-closed behavior when neither chronology nor a validated
        # source-specific technical point exists.
        return original(title, info)

    organization = str(info.get("organization") or "").strip()
    prefix = f"{organization}の選定済み一次資料では" if organization else "選定済み一次資料では"
    return f"{prefix}、{points[0]}"


def _legacy_reset_existing_fact_lines(path: Path, evidence: dict[str, dict[str, Any]]) -> str:
    """Reset current fact lines while accepting the H1 legacy generic ``Author claim`` label."""
    original = path.read_text(encoding="utf-8")
    changes: list[tuple[int, int, str]] = []
    for match in resetter.core.NOTE_RE.finditer(original):
        title = match.group(1)
        info = evidence.get(title)
        if info is None or info.get("suppress_reader_facing_card") is True:
            continue
        chronology = resetter.impl._ORIGINAL_FACT(str(info.get("canonical_title") or title), info)
        block = match.group(0)
        lines = block.splitlines()
        fact_indices = [
            i for i, line in enumerate(lines)
            if line.startswith(r"\item \textbf{一次情報で確認できる事実}: ")
        ]
        if len(fact_indices) > 1:
            raise ValueError(f"legacy Technical Notes contain multiple primary-fact lines: {title}")

        if fact_indices:
            target = fact_indices[0]
        else:
            generic_indices = [
                i for i, line in enumerate(lines)
                if line.startswith(r"\item \textbf{")
                and all(marker in line for marker in _LEGACY_GENERIC_FACT_MARKERS)
            ]
            if len(generic_indices) != 1:
                raise ValueError(
                    f"legacy Technical Notes fact reset requires exactly one generic replacement target: "
                    f"{title} found={len(generic_indices)}"
                )
            target = generic_indices[0]

        lines[target] = (
            r"\item \textbf{一次情報で確認できる事実}: "
            + resetter.core.tex_escape(chronology)
        )
        revised = "\n".join(lines)
        changes.append((match.start(), match.end(), revised))

    text = original
    for start, end, revised in reversed(changes):
        text = text[:start] + revised + text[end:]
    path.write_text(text, encoding="utf-8")
    return original


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    original_context = rendered._state_pinned_rendered_note_context
    original_fact = facts._ORIGINAL_FACT
    original_reset = resetter._reset_existing_fact_lines

    def compat_fact(title: str, info: dict[str, Any]) -> str:
        return _eventless_source_specific_fact(title, info, original_fact)

    rendered._state_pinned_rendered_note_context = _legacy_rendered_note_context
    facts._ORIGINAL_FACT = compat_fact
    resetter._reset_existing_fact_lines = _legacy_reset_existing_fact_lines
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        rendered._state_pinned_rendered_note_context = original_context
        facts._ORIGINAL_FACT = original_fact
        resetter._reset_existing_fact_lines = original_reset
    result = dict(result)
    result["legacy_rendered_note_detection"] = "main-tex-direct-input-unless-explicit-false-v1"
    result["legacy_eventless_fact_contract"] = "SOURCE_SPECIFIC_TECHNICAL_POINT_NO_DASH_V1"
    result["legacy_generic_fact_label_contract"] = "GENERIC_AUTHOR_CLAIM_TO_PRIMARY_FACT_V1"
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
