#!/usr/bin/env python3
"""Repair Annual Special Technical Notes with source-specific, Screening-bound details.

Issue #139 exposed a regression in SP-2023-Y: reader-facing Technical Notes had fallen back to
repeated attribution/limitation prose even though the accepted Screening queue retained concrete
method, architecture, release-scope, and availability details.  This repair intentionally reuses
all hardened Half-year extraction/binding layers instead of introducing a broader keyword scan.

The operation is an immutable pre-Publication-Preview revision.  It changes only reader-facing
Technical Notes plus revision/provenance metadata, preserves accepted Article Drafts and Evidence,
keeps the approved Architecture closed, and re-materializes the Annual chronology metadata without
changing the 75 dated events.  Automatic detail extraction is subject to the existing
SUBJECT_COMPONENT_VARIANT_PROPERTY_BINDING_V3 and hardened event windows.  Thin/ambiguous cards
fail closed and require a hash-bound editorial override tied to the exact accepted Screening queue.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import shutil
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v6 as signals
from scripts import revise_special_half_year_review_repairs_v8 as incremental
from scripts import revise_special_half_year_review_repairs_v27 as binding
from scripts import revise_special_half_year_review_repairs_v32 as event_hardening
from scripts import revise_special_half_year_review_repairs_v34 as hardened


_ANNUAL_STATUS = "VALIDATED_ANNUAL_SOURCE_SPECIFIC_NOTES_REVISION"
_ANNUAL_CONTRACT = "ANNUAL_SCREENING_BACKED_FAIL_CLOSED_V1"
_GENERIC_CAPABILITY_CONTRACT = "GENERIC_CAPABILITY_SUBJECT_BINDING_V1"

# These concepts are materially important in the 2023 annual source set but were not part of the
# later Half-year vocabulary.  They remain subject-bound because they are added to the V3 scoped
# signal set while extraction runs; the source window is the same V32 event/abstract window.
_ANNUAL_SIGNAL_PATTERNS: tuple[tuple[str, str], ...] = (
    ("PagedAttention / paged KV-cache", r"\bPagedAttention\b|\bpaged\s+attention\b"),
    ("virtual-memory-style KV-cache paging", r"\bvirtual memory\b.{0,100}\bpaging\b|\bpaging\b.{0,100}\bKV\s*cache\b"),
    ("4-bit NormalFloat (NF4)", r"\bNormalFloat\b|\bNF4\b"),
    ("double quantization", r"\bdouble quantization\b"),
    ("paged optimizers", r"\bpaged optim(?:izer|izers|isers)\b"),
    ("attention work partitioning", r"\bwork partitioning\b"),
    ("thread-block attention parallelism", r"\bthread blocks?\b.{0,90}\battention\b|\battention\b.{0,90}\bthread blocks?\b"),
    ("warp-level work distribution", r"\bwarps?\b.{0,90}\b(?:work|communication|shared memory)\b"),
    ("Tree-of-Thought search", r"\bTree of Thoughts?\b|\bToT\b"),
    ("multi-path reasoning with lookahead/backtracking", r"\b(?:look(?:ing)? ahead|lookahead)\b.{0,120}\bbacktrack(?:ing)?\b|\bbacktrack(?:ing)?\b.{0,120}\blook(?:ing)? ahead\b"),
    ("closed-form preference optimization", r"\boptimal policy in closed form\b|\bclosed form\b.{0,100}\bpreference"),
    ("preference classification loss", r"\bclassification loss\b"),
    ("adaptive/on-demand retrieval", r"\b(?:adaptive|on-demand) retrieval\b|\bretrieve on demand\b"),
    ("reflection tokens", r"\breflection tokens?\b"),
    ("selective state-space model", r"\bselective (?:state spaces?|SSMs?)\b|\bselective SSMs?\b"),
    ("input-dependent SSM parameters", r"\bSSM parameters?\b.{0,80}\bfunctions? of the input\b"),
    ("hardware-aware recurrent parallel algorithm", r"\bhardware-aware parallel algorithm\b"),
    ("single-stage audio language model", r"\bsingle[- ]stage transformer LM\b|\bsingle autoregressive language model\b"),
    ("discrete audio tokens / EnCodec", r"\bEnCodec\b|\bdiscrete audio tokens?\b"),
    ("Adversarial Diffusion Distillation (ADD)", r"\bAdversarial Diffusion Distillation\b|\bADD\b"),
    ("single-step diffusion generation", r"\bsingle[- ]step\b.{0,100}\b(?:image|generation|diffusion)\b"),
    ("sliding-window attention", r"\bsliding window attention\b|\bSWA\b"),
    ("fill-in-the-middle (FIM)", r"\bfill[- ]in[- ]the[- ]middle\b|\bFIM\b"),
    ("LLM-as-a-judge", r"\bLLM[- ]as[- ]a[- ]judge\b"),
    ("anonymous randomized pairwise battles", r"\banonymous\b.{0,80}\brandomized\b.{0,100}\bbattles?\b"),
    ("Elo-based human-preference ranking", r"\bElo\b.{0,120}\b(?:human|preference|rating)\b"),
    ("multimodal visual instruction tuning", r"\bvisual instruction tuning\b|\bmultimodal language-image instruction\b"),
    ("episodic reflective memory", r"\bepisodic memory buffer\b|\breflective text\b.{0,80}\bmemory\b"),
    ("retrieval-conditioned API selection", r"\bdocument retriever\b.{0,120}\bAPI\b|\bAPI\b.{0,120}\bdocument retriever\b"),
    ("synthetic explanation-trace distillation", r"\bexplanation traces?\b|\bstep-by-step thought processes\b"),
    ("textbook-quality synthetic/filtered data", r"\btextbook-quality\b|\bsynthetic datasets?\b.{0,100}\beducational value\b"),
)
_ANNUAL_SCOPED_SIGNALS = {display for display, _pattern in _ANNUAL_SIGNAL_PATTERNS}

_GENERIC_RE = re.compile(
    r"一次資料で「.+?」の2023年における公開・リリースの経緯を確認できる。"
    r"|能力や性能に関する評価は、提供元・プロジェクト側の主張として扱う。"
    r"|一次資料で確認できる範囲の事実を記録しており",
)


def _sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def _write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _chronology_copy(repo_root: Path, issue_id: str, source_version: str, state: dict[str, Any]) -> dict[str, Any]:
    provenance = state.setdefault("provenance", {})
    prior = copy.deepcopy(provenance.get("annual_chronology") or {})
    if not prior:
        raise ValueError("Annual source-specific repair requires materialized annual_chronology provenance")
    prior_path = repo_root / str(prior.get("path") or "")
    if not prior_path.is_file() or _sha(prior_path) != str(prior.get("sha256") or ""):
        raise ValueError("prior Annual chronology digest mismatch")
    payload = _load_json(prior_path)
    before_events = copy.deepcopy(payload.get("events") or [])
    before_unresolved = copy.deepcopy(payload.get("unresolved_dates") or payload.get("unresolved") or [])
    payload["source_version"] = source_version
    out = repo_root / "sources" / issue_id / "chronology" / f"annual-chronology-{source_version}.json"
    if out.exists():
        raise ValueError(f"Annual chronology revision already exists: {out}")
    _write_json(out, payload)
    reread = _load_json(out)
    if reread.get("events") != before_events:
        raise ValueError("Annual Technical Notes repair must not change chronology events")
    after_unresolved = reread.get("unresolved_dates") or reread.get("unresolved") or []
    if after_unresolved != before_unresolved:
        raise ValueError("Annual Technical Notes repair must not change unresolved chronology records")
    event_count = len(before_events)
    expected_event_count = int(prior.get("event_count") or event_count)
    if event_count != expected_event_count:
        raise ValueError(f"Annual chronology event count changed: {event_count} != {expected_event_count}")
    history = state.setdefault("provenance_history", {})
    history.setdefault("annual_chronology", []).append(prior)
    new = {
        "source_version": source_version,
        "path": out.relative_to(repo_root).as_posix(),
        "sha256": _sha(out),
        "event_count": event_count,
        "unresolved_date_count": int(prior.get("unresolved_date_count") or len(before_unresolved)),
    }
    provenance["annual_chronology"] = new
    return new


def _postprocess_annual(
    repo_root: Path,
    special_slug: str,
    issue_id: str,
    source_version: str,
    marker: dict[str, Any],
    result: dict[str, Any],
) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = _load_json(state_path)
    current = state.get("provenance", {}).get("validated_issue_source") or {}
    manifest_path = repo_root / str(current.get("path") or "")
    if not manifest_path.is_file():
        raise ValueError("new Annual validated source manifest missing after enrichment")
    manifest = _load_json(manifest_path)
    if manifest.get("source_version") != source_version:
        raise ValueError("Annual source version mismatch after enrichment")

    manifest["status"] = _ANNUAL_STATUS
    manifest["derivation"] = (
        "Incremental Publication Preview repair for #139 over SP-2023-Y v0.4. Selected Evidence, "
        "accepted Article Drafts, approved Architecture, narrative sections, chronology events, and bibliography remain "
        "immutable. Each reader-facing Technical Notes card receives at least one source-specific detail joined through "
        "the exact accepted hash-pinned Screening verification queue; ambiguous ownership fails closed under the #191 "
        "subject/component/variant/property binding contract."
    )
    reader = dict(manifest.get("reader_facing_technical_notes") or {})
    reader.update(
        {
            "generic_fallback_policy": "forbidden-fail-closed",
            "generic_fallback_findings": 0,
            "source_specific_detail_contract": "SCREENING_BACKED_FAIL_CLOSED",
            "annual_source_specific_detail_contract": _ANNUAL_CONTRACT,
            "subject_entity_binding_contract": binding._ENTITY_BINDING_CONTRACT,
            "event_window_contract": event_hardening._EVENT_WINDOW_CONTRACT,
            "generic_capability_subject_binding_contract": _GENERIC_CAPABILITY_CONTRACT,
        }
    )
    manifest["reader_facing_technical_notes"] = reader
    layout = dict(manifest.get("layout_revision") or {})
    layout.update(
        {
            "from_source_version": str((manifest.get("basis") or {}).get("previous_source_manifest_path") or "v0.4"),
            "annual_source_specific_notes_v1": True,
            "issue_refs": [int(x) for x in (marker.get("review_issues") or [139])],
            "reader_content_changed": True,
            "reader_content_change_scope": "reader-facing Technical Notes source-specific details only",
            "new_external_evidence": False,
            "accepted_article_sections_changed": False,
            "accepted_article_claims_changed": False,
            "evidence_cards_changed": False,
            "chronology_events_changed": False,
            "bibliography_data_changed": False,
        }
    )
    manifest["layout_revision"] = layout

    generic_findings: list[dict[str, Any]] = []
    visible_cards = 0
    for article in manifest.get("articles") or []:
        if article.get("technical_notes_reader_facing") is not True:
            continue
        rel = str(article.get("technical_notes_path") or "").strip()
        path = manifest_path.parent / rel
        text = path.read_text(encoding="utf-8")
        visible_cards += len(list(signals.core.NOTE_RE.finditer(text)))
        for match in _GENERIC_RE.finditer(text):
            generic_findings.append({"path": rel, "text": match.group(0)})
        article["technical_notes_sha256"] = _sha(path)
    if visible_cards < 1:
        raise ValueError("Annual source-specific Technical Notes repair found no visible cards")
    if generic_findings:
        raise ValueError(f"generic Annual Technical Notes fallback remains: {generic_findings[:5]}")

    reader = dict(manifest.get("reader_facing_technical_notes") or {})
    expected_enriched = int(result.get("technical_notes_source_specific_detail_enrichment_count") or 0)
    if expected_enriched != visible_cards:
        raise ValueError(f"not every Annual Technical Notes card was enriched: {expected_enriched} != {visible_cards}")
    reader["source_specific_detail_visible_card_count"] = visible_cards
    reader["source_specific_detail_enrichment_count"] = expected_enriched
    reader["source_specific_detail_url_identity_checks"] = int(result.get("technical_notes_url_identity_checks") or 0)
    reader["source_specific_detail_override_count"] = int(result.get("technical_note_detail_overrides") or 0)
    manifest["reader_facing_technical_notes"] = reader

    _write_json(manifest_path, manifest)
    manifest_sha = _sha(manifest_path)
    current["sha256"] = manifest_sha
    current["source_version"] = source_version
    current["layout_revision_sha256"] = _sha(
        repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    )
    state["provenance"]["validated_issue_source"] = current
    chronology = _chronology_copy(repo_root, issue_id, source_version, state)

    preview_transfer = repo_root / "sources" / issue_id / "preview-transfer"
    if preview_transfer.exists():
        shutil.rmtree(preview_transfer)

    state["lifecycle_state"] = "VALIDATED_DRAFT"
    state["gates"]["latex_build"] = "pending"
    state["gates"]["visual_review"] = "pending"
    state["gates"]["freeze"] = "pending"
    _write_json(state_path, state)

    result = dict(result)
    result.update(
        {
            "status": _ANNUAL_STATUS,
            "annual_source_specific_detail_contract": _ANNUAL_CONTRACT,
            "subject_entity_binding_contract": binding._ENTITY_BINDING_CONTRACT,
            "event_window_contract": event_hardening._EVENT_WINDOW_CONTRACT,
            "generic_capability_subject_binding_contract": _GENERIC_CAPABILITY_CONTRACT,
            "source_manifest_sha256": manifest_sha,
            "technical_notes_visible_card_count": visible_cards,
            "generic_fallback_findings": 0,
            "annual_chronology": chronology,
            "chronology_events_changed": False,
        }
    )
    return result


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    repo_root = repo_root.resolve()
    edition = _load_json(repo_root / "specials" / special_slug / "edition.json")
    if edition.get("special_id") != issue_id or edition.get("edition_kind") != "RETROSPECTIVE_PERIOD":
        raise ValueError("Annual source-specific notes repair requires matching RETROSPECTIVE_PERIOD edition")
    if not special_slug.endswith("-Y"):
        raise ValueError("Annual source-specific notes repair is restricted to -Y editions")

    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = _load_json(marker_path)
    changes = marker.get("layout_changes") or {}
    constraints = marker.get("constraints") or {}
    if changes.get("annual_source_specific_notes_v1") is not True:
        raise ValueError("marker does not request annual_source_specific_notes_v1")
    # The inherited incremental engine uses this compatibility flag to select the already-built
    # Technical Notes-only path.  It does not reopen the old Half-year structural transforms.
    if changes.get("half_year_review_repairs_v3") is not True:
        raise ValueError("annual marker must enable the inherited incremental note-repair compatibility path")
    required_constraints = {
        "new_external_evidence_allowed": False,
        "selected_evidence_only": True,
        "accepted_article_claims_changed": False,
        "evidence_cards_mutated": False,
    }
    for key, expected in required_constraints.items():
        if constraints.get(key) is not expected:
            raise ValueError(f"Annual Technical Notes repair constraint mismatch: {key}")

    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = _load_json(state_path)
    gates = state.get("gates") or {}
    if state.get("lifecycle_state") != "RELEASE_CANDIDATE" or gates.get("latex_build") != "passed":
        raise ValueError("Annual Technical Notes repair requires built RELEASE_CANDIDATE")
    if gates.get("visual_review") != "pending" or gates.get("freeze") != "pending":
        raise ValueError("Annual Technical Notes repair is forbidden after Visual Review or Freeze begins")
    if "publication_preview" in (state.get("provenance") or {}):
        raise ValueError("Annual Technical Notes repair is forbidden after Publication Preview approval")
    current = copy.deepcopy((state.get("provenance") or {}).get("validated_issue_source") or {})
    current_path = repo_root / str(current.get("path") or "")
    if not current_path.is_file() or _sha(current_path) != str(current.get("sha256") or ""):
        raise ValueError("current Annual validated source digest mismatch")
    current_manifest = _load_json(current_path)
    current_status = str(current_manifest.get("status") or "")

    old_statuses = set(incremental._ALREADY_STRUCTURALLY_REPAIRED)
    old_patterns = signals._SIGNAL_PATTERNS
    old_component = set(binding._COMPONENT_SCOPED_SIGNALS)
    old_scope = set(binding._SCOPE_SENSITIVE_STATIC_SIGNALS)
    incremental._ALREADY_STRUCTURALLY_REPAIRED = old_statuses | {current_status, _ANNUAL_STATUS}
    signals._SIGNAL_PATTERNS = old_patterns + tuple(
        item for item in _ANNUAL_SIGNAL_PATTERNS if item[0] not in {name for name, _ in old_patterns}
    )
    binding._COMPONENT_SCOPED_SIGNALS = old_component | _ANNUAL_SCOPED_SIGNALS
    binding._SCOPE_SENSITIVE_STATIC_SIGNALS = old_scope | _ANNUAL_SCOPED_SIGNALS
    try:
        result = hardened.build(repo_root, special_slug, issue_id, source_version)
    finally:
        incremental._ALREADY_STRUCTURALLY_REPAIRED = old_statuses
        signals._SIGNAL_PATTERNS = old_patterns
        binding._COMPONENT_SCOPED_SIGNALS = old_component
        binding._SCOPE_SENSITIVE_STATIC_SIGNALS = old_scope

    return _postprocess_annual(repo_root, special_slug, issue_id, source_version, marker, result)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    result = build(Path(args.repo_root), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
