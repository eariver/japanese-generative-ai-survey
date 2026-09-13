#!/usr/bin/env python3
"""Canonical bibliography access provenance resolution for Survey Production Core v2.

BibTeX `urldate` must represent the actual canonical retrieval/access date of the
source instance used as publication evidence, not an edition cutoff, rolling window end,
or Special retrospective as-of timestamp.
"""
from __future__ import annotations

import datetime
from pathlib import Path
from typing import Any

from scripts import survey_production_v2 as core


def parse_access_date(value: str) -> tuple[str, str]:
    """Validate *value* as an ISO-8601 timestamp or date and return (full_timestamp, YYYY-MM-DD).

    The urldate represents the calendar date of the canonical accessed_at value itself,
    preserving its explicit offset/date semantics; it is not silently shifted by UTC normalization.
    Fails closed if *value* is not a valid timestamp or date.
    """
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"access timestamp missing or empty: {value!r}")
    raw = value.strip()
    try:
        d = datetime.date.fromisoformat(raw)
        return raw, d.isoformat()
    except ValueError:
        pass

    try:
        core.parse_instant(raw)
    except ValueError as exc:
        raise ValueError(f"invalid access timestamp or date: {value!r}") from exc

    try:
        dt = datetime.datetime.fromisoformat(raw.replace("Z", "+00:00"))
        return raw, dt.date().isoformat()
    except ValueError as exc:
        raise ValueError(f"invalid access timestamp or date: {value!r}") from exc


def resolve_source_access_provenance(
    sources: list[dict[str, Any]],
    canonical_url: str,
    did: str,
    explicit_source_id: str | None = None,
) -> dict[str, Any]:
    """Resolve the canonical source access provenance for *did* and *canonical_url*.

    Multiple-source / ambiguous-source rule:
    1. Identify the source entry bound to the bibliography URL / accepted citation authority.
    2. Require an unambiguous access timestamp for that source.
    3. If multiple accepted captures legitimately support the same citation but have different
       access times, follow existing canonical binding semantics if one capture is explicitly
       authoritative (e.g. *explicit_source_id*).
    4. If no unique authoritative capture can be determined, fail closed rather than using
       min/max/latest heuristics.

    Missing-date rule:
    If the canonical cited source has no valid access timestamp, fail closed with an
    actionable error identifying the Discovery ID/source whose access provenance is missing.
    """
    if not sources or not isinstance(sources, list):
        raise ValueError(f"Discovery ID {did} has no accepted Evidence source access provenance")

    norm_url = canonical_url.strip() if isinstance(canonical_url, str) else ""
    if not norm_url:
        raise ValueError(f"Discovery ID {did} lacks canonical bibliography URL")

    url_matches = [
        s for s in sources
        if isinstance(s, dict) and (s.get("url") or "").strip() == norm_url
    ]

    selected_source: dict[str, Any]
    if len(sources) == 1:
        single = sources[0]
        if not isinstance(single, dict):
            raise ValueError(f"Discovery ID {did} source entry is invalid: {single!r}")
        single_url = (single.get("url") or "").strip()
        if single_url and single_url != norm_url:
            raise ValueError(
                f"Discovery ID {did} source URL {single_url!r} does not match canonical bibliography URL {norm_url!r}"
            )
        selected_source = single
    else:
        # Multiple source entries exist
        if len(url_matches) == 0:
            raise ValueError(
                f"Discovery ID {did} has {len(sources)} source entries but none match bibliography URL {norm_url!r}"
            )
        elif len(url_matches) == 1:
            selected_source = url_matches[0]
        else:
            # Multiple candidate captures match the bibliography URL
            timestamps: list[tuple[str, str]] = []
            for s in url_matches:
                raw_ts = s.get("accessed_at")
                if not raw_ts or not isinstance(raw_ts, str) or not raw_ts.strip():
                    raise ValueError(
                        f"Discovery ID {did} (source {s.get('source_id', 'unknown')}) has missing access timestamp"
                    )
                full_ts, norm_d = parse_access_date(raw_ts)
                timestamps.append((full_ts, norm_d))

            unique_timestamps = {ts[0] for ts in timestamps}
            if len(unique_timestamps) == 1:
                selected_source = url_matches[0]
            else:
                if explicit_source_id:
                    authoritative = [s for s in url_matches if s.get("source_id") == explicit_source_id]
                    if len(authoritative) == 1:
                        selected_source = authoritative[0]
                    else:
                        raise ValueError(
                            f"Discovery ID {did} has ambiguous captures for {norm_url!r} with different access times "
                            f"{sorted(unique_timestamps)}, and explicit_source_id {explicit_source_id!r} could not resolve uniquely"
                        )
                else:
                    raise ValueError(
                        f"Discovery ID {did} has ambiguous captures for {norm_url!r} with different access times "
                        f"{sorted(unique_timestamps)} and no unique authoritative capture"
                    )

    raw_accessed_at = selected_source.get("accessed_at")
    if not raw_accessed_at or not isinstance(raw_accessed_at, str) or not raw_accessed_at.strip():
        source_label = selected_source.get("source_id") or selected_source.get("title") or "unknown"
        raise ValueError(
            f"Discovery ID {did} (source {source_label}) has missing access timestamp in accepted Evidence"
        )

    full_timestamp, normalized_date = parse_access_date(raw_accessed_at)
    return {
        "source_id": selected_source.get("source_id"),
        "source_accessed_at": full_timestamp,
        "urldate": normalized_date,
        "source": selected_source,
    }


def load_evidence_sources(acceptance_path: Path) -> dict[str, dict[str, Any]]:
    """Return a mapping of did -> {'sources': list[dict], 'explicit_source_id': str | None, 'card': dict | None}."""
    resolved_path = acceptance_path.resolve()
    if not resolved_path.is_file() or resolved_path.is_symlink():
        raise ValueError(f"Evidence acceptance path missing or unsafe: {acceptance_path}")
    acceptance = core.load_json(resolved_path)

    interactive_bindings: dict[str, str | None] = {}
    interactive_sources: dict[str, list[dict[str, Any]]] = {}
    interactive_path = resolved_path.parent / "interactive-evidence.json"
    if interactive_path.is_file() and not interactive_path.is_symlink():
        try:
            interactive_data = core.load_json(interactive_path)
            for rec in interactive_data.get("records", []):
                did = rec.get("discovery_id")
                if not did:
                    continue
                bindings = rec.get("source_bindings")
                if isinstance(bindings, list) and len(bindings) == 1 and isinstance(bindings[0], str):
                    interactive_bindings[did] = bindings[0]
                if isinstance(rec.get("sources"), list):
                    interactive_sources[did] = rec["sources"]
        except Exception:
            pass

    evidence_by_did: dict[str, dict[str, Any]] = {}
    for result in acceptance.get("results", []):
        if not isinstance(result, dict):
            continue
        dids = result.get("discovery_ids", [])

        sources: list[dict[str, Any]] | None = None
        card: dict[str, Any] | None = None
        if "sources" in result and isinstance(result["sources"], list):
            sources = result["sources"]
        elif "card" in result and isinstance(result["card"], dict):
            card = result["card"]
            sources = card.get("sources")
        elif "evidence_card" in result and isinstance(result["evidence_card"], dict):
            card = result["evidence_card"]
            sources = card.get("sources")
        elif "filename" in result and isinstance(result["filename"], str):
            card_path = resolved_path.parent / "results" / result["filename"]
            if card_path.is_file() and not card_path.is_symlink():
                card = core.load_json(card_path)
                sources = card.get("sources")

        for did in dids:
            cur_sources = sources if sources is not None else interactive_sources.get(did)
            evidence_by_did[did] = {
                "sources": cur_sources,
                "card": card,
                "explicit_source_id": interactive_bindings.get(did),
            }

    for did, s_list in interactive_sources.items():
        if did not in evidence_by_did:
            evidence_by_did[did] = {
                "sources": s_list,
                "card": None,
                "explicit_source_id": interactive_bindings.get(did),
            }

    return evidence_by_did
