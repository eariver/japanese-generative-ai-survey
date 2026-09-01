#!/usr/bin/env python3
"""Bind model-specific Half-year Technical Note signals to the selected artifact.

Event bounding prevents chronology/living-page drift, but a single first-party release page can
still contain comparison models in the same event slice. Numeric model scales and architecture
terms must therefore be attributable to the selected artifact locally, rather than merely
appearing somewhere on the selected artifact's source page.

This layer keeps the existing fail-closed extraction contract and adds a second boundary:
model-identity-sensitive signals are accepted only when the selected artifact's family anchor
appears immediately before the signal. Rejected candidates are persisted in a source-revision
audit, and the state-pinned source manifest records the contract so Publication Preview
preflight can mechanically verify it.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v23 as base
from scripts import revise_special_half_year_review_repairs_v15 as event_layer

impl = event_layer.impl

_ENTITY_BINDING_CONTRACT = "SUBJECT_ANCHORED_HIGH_RISK_SIGNALS_V1"

# These facts describe a model's scale, architecture, numerical representation, training
# recipe, or release form. They are especially likely to leak from comparison tables/paragraphs.
_ENTITY_BOUND_DYNAMIC_TEMPLATES = {
    "{0}B parameter scale",
    "{0}K context",
    "{0}M context",
    "{0}T training tokens",
}
_ENTITY_BOUND_STATIC_SIGNALS = {
    "decoder-only Transformer",
    "Mixture-of-Experts (MoE)",
    "SSM-Transformer",
    "Mamba",
    "Grouped-Query Attention (GQA)",
    "FP8",
    "INT8",
    "4-bit quantization",
    "8-bit quantization",
    "Quantization-Aware Training (QAT)",
    "SpinQuant",
    "LoRA",
    "Direct Preference Optimization (DPO)",
    "Supervised Fine-Tuning (SFT)",
    "Reinforcement Learning with Verifiable Rewards (RLVR)",
    "Mistral Research License",
    "Llama Community License",
    "open weights",
}

_GENERIC_TITLE_TOKENS = {
    "a", "an", "and", "announcing", "announcement", "api", "for", "from", "in",
    "introducing", "introduction", "model", "models", "new", "of", "on", "preview",
    "release", "research", "technical", "the", "to", "with",
}
_ORGANIZATION_PREFIXES = {
    "anthropic", "google", "meta", "microsoft", "nvidia", "openai",
}

# A deliberately short local radius is the semantic boundary. It accepts constructs such as
# "Jamba ... Mamba" or "Ministral ... 8B" while rejecting later "Llama ... 405B" comparison
# rows even though both occur in the same event-bounded source window.
_DYNAMIC_ANCHOR_RADIUS = 96
_STATIC_ANCHOR_RADIUS = 144

_AUDIT_ROWS: list[dict[str, Any]] = []


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def _write_json(path: Path, value: dict[str, Any]) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _artifact_anchor(title: str) -> str:
    """Return a conservative family token usable for local subject attribution."""
    cleaned = re.sub(r"\\[&_#%{}]", " ", str(title or ""))
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9]*(?:[-.][A-Za-z0-9]+)*", cleaned)
    candidates = [
        token
        for token in tokens
        if len(token) >= 2 and token.lower() not in _GENERIC_TITLE_TOKENS
    ]
    if not candidates:
        return ""
    if candidates[0].lower() in _ORGANIZATION_PREFIXES and len(candidates) > 1:
        return candidates[1]
    return candidates[0]


def _anchor_before(window: str, start: int, title: str, radius: int) -> bool:
    anchor = _artifact_anchor(title)
    if not anchor:
        return False
    prefix = window[max(0, start - radius) : start]
    pattern = re.compile(
        rf"(?<![A-Za-z0-9]){re.escape(anchor)}(?![A-Za-z0-9])",
        flags=re.IGNORECASE,
    )
    return any(pattern.finditer(prefix))


def _entity_aware_technical_signals(
    summary: str,
    events: list[tuple[str, str]],
    title: str = "",
) -> list[str]:
    window = event_layer._safe_event_window(summary, events, title)
    if not window:
        _AUDIT_ROWS.append(
            {
                "title": title,
                "anchor": _artifact_anchor(title),
                "accepted_entity_bound_signals": [],
                "rejected_entity_bound_signals": [],
                "window_empty": True,
            }
        )
        return []

    signals: list[str] = []
    accepted_bound: list[str] = []
    rejected_bound: list[str] = []

    dynamic_accepted = 0
    for template, pattern in impl._DYNAMIC_PATTERNS:
        for match in re.finditer(pattern, window, flags=re.IGNORECASE):
            value = next((group for group in match.groups() if group), "")
            if not value:
                continue
            rendered = template.format(value)
            if template in _ENTITY_BOUND_DYNAMIC_TEMPLATES:
                if not _anchor_before(window, match.start(), title, _DYNAMIC_ANCHOR_RADIUS):
                    if rendered not in rejected_bound:
                        rejected_bound.append(rendered)
                    continue
                if rendered not in accepted_bound:
                    accepted_bound.append(rendered)
            if rendered not in signals and dynamic_accepted < 4:
                signals.append(rendered)
                dynamic_accepted += 1

    for display, pattern in impl._SIGNAL_PATTERNS:
        if display in event_layer.event._UNSAFE_SIGNAL_NAMES:
            continue
        matches = list(re.finditer(pattern, window, flags=re.IGNORECASE | re.DOTALL))
        if not matches:
            continue
        if display in _ENTITY_BOUND_STATIC_SIGNALS:
            if not any(
                _anchor_before(window, match.start(), title, _STATIC_ANCHOR_RADIUS)
                for match in matches
            ):
                if display not in rejected_bound:
                    rejected_bound.append(display)
                continue
            if display not in accepted_bound:
                accepted_bound.append(display)
        if display not in signals:
            signals.append(display)
        if len(signals) >= 7:
            break

    _AUDIT_ROWS.append(
        {
            "title": title,
            "anchor": _artifact_anchor(title),
            "accepted_entity_bound_signals": accepted_bound,
            "rejected_entity_bound_signals": rejected_bound,
            "window_empty": False,
        }
    )
    return signals[:7]


def _aggregate_audit() -> list[dict[str, Any]]:
    grouped: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "anchor": "",
            "extraction_calls": 0,
            "accepted_entity_bound_signals": [],
            "rejected_entity_bound_signals": [],
            "empty_window_calls": 0,
        }
    )
    for row in _AUDIT_ROWS:
        title = str(row.get("title") or "")
        item = grouped[title]
        item["anchor"] = str(row.get("anchor") or item["anchor"])
        item["extraction_calls"] += 1
        if row.get("window_empty"):
            item["empty_window_calls"] += 1
        for key in ("accepted_entity_bound_signals", "rejected_entity_bound_signals"):
            for signal in row.get(key) or []:
                if signal not in item[key]:
                    item[key].append(signal)
    return [
        {"title": title, **grouped[title]}
        for title in sorted(grouped)
        if title
    ]


def _audit_coverage_population(manifest: dict[str, Any]) -> tuple[int, int, int, str]:
    """Return the unique-title audit population and its provenance.

    Entity-binding audit rows and editorial overrides are both keyed by canonical/rendered
    title. A rendered title may appear in multiple Technical Note placements, so card placement
    count is not a compatible denominator. Prefer the already-recorded rendered-title scope;
    retain the historical visible-card denominator only for older manifests that predate it.
    """
    reader = dict(manifest.get("reader_facing_technical_notes") or {})
    enrichment = dict(manifest.get("_technical_note_enrichment_scope") or {})
    visible_cards = int(reader.get("source_specific_detail_visible_card_count") or 0)
    overrides = int(reader.get("source_specific_detail_override_count") or 0)
    rendered_titles = int(enrichment.get("rendered_title_count") or 0)

    if rendered_titles > 0:
        population = rendered_titles
        basis = "UNIQUE_RENDERED_TITLE_COUNT"
        if visible_cards and visible_cards < rendered_titles:
            raise ValueError(
                "entity-binding coverage metadata is inconsistent: "
                f"visible_cards={visible_cards} unique_rendered_titles={rendered_titles}"
            )
    else:
        population = visible_cards
        basis = "VISIBLE_CARD_COUNT_LEGACY_FALLBACK"

    if overrides > population:
        raise ValueError(
            "entity-binding override count exceeds the compatible audit population: "
            f"overrides={overrides} population={population} basis={basis}"
        )
    return population, visible_cards, overrides, basis


def _record_contract(
    repo_root: Path,
    issue_id: str,
    result: dict[str, Any],
) -> dict[str, Any]:
    manifest_rel = str(result.get("source_manifest") or "")
    if not manifest_rel:
        raise ValueError("Half-year entity-binding layer requires source_manifest in build result")
    manifest_path = repo_root / manifest_rel
    if not manifest_path.is_file():
        raise ValueError(f"generated source manifest missing: {manifest_path}")

    old_sha = _sha(manifest_path)
    expected_old_sha = str(result.get("source_manifest_sha256") or "")
    if expected_old_sha and old_sha != expected_old_sha:
        raise ValueError(
            f"generated source manifest changed before entity-binding contract: actual={old_sha} expected={expected_old_sha}"
        )

    artifacts = _aggregate_audit()
    rejected_count = sum(len(item["rejected_entity_bound_signals"]) for item in artifacts)
    accepted_count = sum(len(item["accepted_entity_bound_signals"]) for item in artifacts)
    audit = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "source_version": result.get("source_version"),
        "contract": _ENTITY_BINDING_CONTRACT,
        "scope": "event-bounded Screening-backed Technical Note signal extraction",
        "policy": (
            "Model scale/architecture/training/release-form signals require a local selected-artifact "
            "identity anchor; unbound candidates are rejected before reader-facing synthesis."
        ),
        "artifact_count": len(artifacts),
        "accepted_entity_bound_signal_count": accepted_count,
        "rejected_entity_bound_signal_count": rejected_count,
        "artifacts": artifacts,
    }
    audit_path = manifest_path.parent / "technical-note-entity-binding-audit.json"
    _write_json(audit_path, audit)
    audit_sha = _sha(audit_path)

    manifest = _load_json(manifest_path)
    reader = dict(manifest.get("reader_facing_technical_notes") or {})
    population, visible_cards, overrides, coverage_basis = _audit_coverage_population(manifest)
    minimum_audited = max(0, population - overrides)
    if len(artifacts) < minimum_audited:
        raise ValueError(
            "entity-binding audit does not cover all automatically extracted visible Technical Notes: "
            f"audited={len(artifacts)} minimum={minimum_audited} population={population} "
            f"basis={coverage_basis} visible_cards={visible_cards} overrides={overrides}"
        )
    reader.update(
        {
            "entity_binding_contract": _ENTITY_BINDING_CONTRACT,
            "entity_binding_audit_path": audit_path.relative_to(manifest_path.parent).as_posix(),
            "entity_binding_audit_sha256": audit_sha,
            "entity_binding_audited_artifact_count": len(artifacts),
            "entity_binding_accepted_signal_count": accepted_count,
            "entity_binding_rejected_signal_count": rejected_count,
            "entity_binding_coverage_population_count": population,
            "entity_binding_coverage_basis": coverage_basis,
            "entity_binding_visible_card_placement_count": visible_cards,
        }
    )
    manifest["reader_facing_technical_notes"] = reader
    layout_revision = dict(manifest.get("layout_revision") or {})
    layout_revision["technical_note_entity_binding"] = _ENTITY_BINDING_CONTRACT
    manifest["layout_revision"] = layout_revision
    _write_json(manifest_path, manifest)
    new_sha = _sha(manifest_path)

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = _load_json(state_path)
    current = (state.get("provenance") or {}).get("validated_issue_source") or {}
    if str(current.get("path") or "") != manifest_rel or str(current.get("sha256") or "") != old_sha:
        raise ValueError("pipeline state no longer pins the just-generated source manifest")
    current["sha256"] = new_sha
    _write_json(state_path, state)

    result["source_manifest_sha256"] = new_sha
    result["technical_note_entity_binding_contract"] = _ENTITY_BINDING_CONTRACT
    result["technical_note_entity_binding_audit"] = audit_path.relative_to(repo_root).as_posix()
    result["technical_note_entity_binding_audit_sha256"] = audit_sha
    result["technical_note_entity_binding_rejected_signal_count"] = rejected_count
    return result


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    global _AUDIT_ROWS
    _AUDIT_ROWS = []
    previous_signals = event_layer._safe_technical_signals
    event_layer._safe_technical_signals = _entity_aware_technical_signals
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        event_layer._safe_technical_signals = previous_signals
    if not isinstance(result, dict):
        raise ValueError("Half-year repair build did not return a result object")
    return _record_contract(repo_root, issue_id, result)


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
