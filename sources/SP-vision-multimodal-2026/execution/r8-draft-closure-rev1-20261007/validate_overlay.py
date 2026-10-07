#!/usr/bin/env python3
"""Edition-local overlay validator for TS-003 content revision r5-rev1.

Same checks as frozen survey_drafting_v2.validate_draft_result (fields, identity,
schema/status, basis binding, runner, refs, attribution, block uniqueness,
must_cover exact-once, boundary dispositions, extensions propagation) EXCEPT the
Evidence ref index is the UNION of canonical package inputs + the consumer's
overlay cards. Additional overlay checks: overlay task allowlist, overlay
Discovery-ID allowlist per consumer, SELECTED disposition, card-bytes binding,
canonical-home preservation note (no placement change enforced structurally).

Pure edition-local compatibility; shared Core untouched.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

from scripts import survey_drafting_v2_base as base
from scripts import survey_production_v2 as core

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")


def _load_overlay_cards(overlay_path: Path, consumer: str):
    overlay = json.loads(overlay_path.read_text(encoding="utf-8"))
    entries = [e for e in overlay["entries"] if e["consumer_package"] == consumer]
    assert entries, f"no overlay entries for {consumer}"
    allow_tasks = {e["evidence_task_id"] for e in entries}
    allow_discovery = {e["discovery_id"] for e in entries}
    for e in entries:
        assert e["selection_disposition"] == "SELECTED", e["discovery_id"]
    return overlay, entries, allow_tasks, allow_discovery


def _union_index(package: dict, overlay_path: Path, consumer: str):
    overlay, entries, allow_tasks, allow_discovery = _load_overlay_cards(overlay_path, consumer)
    union_inputs = list(package["evidence_inputs"])
    have = {i["evidence_task_id"] for i in union_inputs}
    # overlay card bytes live in the evidence acceptance tree; resolve via task->file map
    # built from the package's own evidence_acceptance? P- packages embed acceptance with results.
    # Simpler: reuse card bytes through the overlay entries is impossible (file only stores meta),
    # so load cards from the canonical evidence results dir via candidate-matrix binding is overkill:
    # instead, the regen script supplies overlay cards; the validator re-derives them from the
    # acceptance path recorded in the overlay build (evidence_filename + sha re-verified below).
    return overlay, entries, allow_tasks, allow_discovery, union_inputs, have


def validate_overlay_result(result: dict, package_path: Path, overlay_path: Path,
                            consumer: str, overlay_cards: dict) -> list[str]:
    """Full frozen-equivalent validation with union index. overlay_cards: task_id -> card."""
    errors: list[str] = []
    package = core.load_json(package_path)
    overlay, entries, allow_tasks, allow_discovery = _load_overlay_cards(overlay_path, consumer)

    if set(result) != base.DRAFT_RESULT_FIELDS:
        return ["Draft Result fields must exactly match generic v2 contract"]
    for key in ("issue_id", "research_profile", "publication_profile", "package_id"):
        if result.get(key) != package.get(key):
            errors.append(f"Draft Result {key} does not match Draft Package")
    if result.get("package_id") != consumer:
        errors.append("overlay consumer mismatch")
    if result.get("schema_version") != "2.0-rc1" or result.get("status") not in {"DRAFT", "REVISED", "ESTABLISHED"}:
        errors.append("Draft Result schema/status invalid")
    expected_basis = {
        "draft_package_sha256": core.sha256_file(package_path),
        "prompt_id": "article-drafting-v2",
        "prompt_sha256": core.sha256_file(ROOT / "config/prompts/article-drafting-v2.md"),
    }
    if result.get("basis") != expected_basis:
        errors.append("Draft Result basis does not bind exact Package/prompt bytes")
    if not (isinstance(result.get("headline"), str) and result["headline"].strip()
            and isinstance(result.get("deck"), str) and result["deck"].strip()
            and isinstance(result.get("draft_version"), str) and result["draft_version"].strip()):
        errors.append("Draft Result version/headline/deck required")
    runner = result.get("runner")
    if not isinstance(runner, dict) or set(runner) != {"provider", "model", "invocation", "generated_at", "run_reference"}:
        errors.append("Draft Result runner fields invalid")
    else:
        for key in ("provider", "model", "invocation"):
            v = runner.get(key)
            if not (isinstance(v, str) and v.strip()):
                errors.append(f"Draft Result runner.{key} required")
        try:
            from datetime import datetime
            raw = runner.get("generated_at")
            norm = raw[:-1] + "+00:00" if isinstance(raw, str) and raw.endswith("Z") else raw
            dt = datetime.fromisoformat(norm)
            if dt.tzinfo is None:
                raise ValueError()
        except Exception:
            errors.append("Draft Result runner.generated_at must be timezone-aware ISO-8601")
        if runner.get("run_reference") is not None and not (isinstance(runner.get("run_reference"), str) and runner["run_reference"].strip()):
            errors.append("Draft Result runner.run_reference must be non-empty or null")

    # union index
    pseudo = {"evidence_inputs": list(package["evidence_inputs"])}
    have = {i["evidence_task_id"] for i in pseudo["evidence_inputs"]}
    for e in entries:
        tid = e["evidence_task_id"]
        if tid in have:
            continue
        card = overlay_cards.get(tid)
        if card is None:
            errors.append(f"overlay card missing for task {tid}")
            continue
        if card.get("evidence_task_id") != tid:
            errors.append(f"overlay card identity mismatch {tid}")
            continue
        raw = json.dumps(card, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        # canonical byte check uses core.json_bytes; verify via sha of canonical bytes
        if core.sha256_bytes(core.json_bytes(card)) != e["evidence_sha256"]:
            errors.append(f"overlay card bytes drift {tid}")
            continue
        pseudo["evidence_inputs"].append({"evidence_task_id": tid, "evidence_card": card})
        have.add(tid)
    if errors:
        return errors
    index = base._card_ref_index(pseudo)

    # overlay allowlist enforcement on refs
    canon_tasks = {i["evidence_task_id"] for i in package["evidence_inputs"]}
    task_of_discovery: dict[str, str] = {}
    # discovery resolution needs matrix rows (package embeds candidate_matrix)
    rows = package["candidate_matrix"]["rows"]
    for r in rows:
        for d in r.get("discovery_ids", []):
            task_of_discovery[d] = r["evidence_task_id"]
    # reverse: task -> discovery ids (matrix-level)
    disc_of_task: dict[str, set] = {}
    for r in rows:
        disc_of_task.setdefault(r["evidence_task_id"], set()).update(r.get("discovery_ids", []))

    def check_refs(refs, label):
        errs, classes = base._validate_refs(refs, index, label)
        for ref in (refs if isinstance(refs, list) else []):
            if not isinstance(ref, dict):
                continue
            tid = ref.get("evidence_task_id")
            if tid in canon_tasks:
                continue
            if tid not in allow_tasks:
                errs.append(f"{label} references Evidence outside overlay allowlist: {tid}")
                continue
            if not (disc_of_task.get(tid, set()) & allow_discovery):
                errs.append(f"{label} overlay task carries no allowlisted Discovery ID: {tid}")
        return errs, classes

    deck_refs = result.get("deck_evidence_refs")
    ref_errors, classes = check_refs(deck_refs, "deck")
    errors += ref_errors
    errors += base._validate_attribution(
        result.get("deck_attribution_mode"),
        deck_refs if isinstance(deck_refs, list) else [], classes, "deck")

    blocks = result.get("blocks")
    block_ids: list[str] = []
    if not isinstance(blocks, list) or not blocks:
        errors.append("Draft Result blocks must be a non-empty array")
        blocks = []
    for offset, block in enumerate(blocks):
        prefix = f"blocks[{offset}]"
        if not isinstance(block, dict) or set(block) != {
            "block_id", "block_type", "text", "attribution_mode", "evidence_refs"
        }:
            errors.append(f"{prefix} fields invalid")
            continue
        if not (isinstance(block.get("block_id"), str) and block["block_id"].strip()
                and isinstance(block.get("text"), str) and block["text"].strip()
                and block.get("block_type") in base.BLOCK_TYPES):
            errors.append(f"{prefix} identity/type/text invalid")
            continue
        block_ids.append(block["block_id"])
        ref_errors, classes = check_refs(block.get("evidence_refs"), prefix)
        errors += ref_errors
        errors += base._validate_attribution(
            block.get("attribution_mode"),
            block.get("evidence_refs") if isinstance(block.get("evidence_refs"), list) else [],
            classes, prefix)
    if len(block_ids) != len(set(block_ids)):
        errors.append("Draft Result block_id values must be unique")
    block_set = set(block_ids)

    must_cover = result.get("must_cover_coverage")
    expected_requirements = set(package["package"]["must_cover_requirements"])
    actual_requirements: list[str] = []
    if not isinstance(must_cover, list):
        errors.append("must_cover_coverage must be an array")
        must_cover = []
    for row in must_cover:
        if not isinstance(row, dict) or set(row) != {"requirement", "block_ids"}:
            errors.append("must_cover_coverage row fields invalid")
            continue
        actual_requirements.append(row.get("requirement"))
        ids = row.get("block_ids")
        if not isinstance(ids, list) or not ids or len(ids) != len(set(ids)) or any(v not in block_set for v in ids):
            errors.append(f"must_cover_coverage block_ids invalid for {row.get('requirement')}")
    if len(actual_requirements) != len(set(actual_requirements)) or set(actual_requirements) != expected_requirements:
        errors.append("Draft Result must cover every Architecture must-cover requirement exactly once")

    boundaries = result.get("boundary_dispositions")
    expected_boundaries = set(package["package"]["boundaries"])
    actual_boundaries: list[str] = []
    if not isinstance(boundaries, list):
        errors.append("boundary_dispositions must be an array")
        boundaries = []
    for row in boundaries:
        if not isinstance(row, dict) or set(row) != {"boundary", "handling", "block_ids", "rationale"}:
            errors.append("boundary_disposition fields invalid")
            continue
        actual_boundaries.append(row.get("boundary"))
        handling = row.get("handling")
        ids = row.get("block_ids")
        if handling not in base.BOUNDARY_HANDLING or not isinstance(ids, list) or len(ids) != len(set(ids)) or any(v not in block_set for v in ids):
            errors.append(f"boundary_disposition invalid for {row.get('boundary')}")
        if handling == "EXPLICITLY_STATED" and not ids:
            errors.append(f"explicit boundary requires at least one block: {row.get('boundary')}")
        if handling == "RESPECTED_BY_OMISSION" and ids:
            errors.append(f"omission boundary must not claim reader-facing block coverage: {row.get('boundary')}")
        v = row.get("rationale")
        if not (isinstance(v, str) and v.strip()):
            errors.append(f"boundary rationale required: {row.get('boundary')}")
    if len(actual_boundaries) != len(set(actual_boundaries)) or set(actual_boundaries) != expected_boundaries:
        errors.append("Draft Result must dispose every Architecture boundary exactly once")

    from scripts import survey_draft_profile_v2 as draft_profile
    errors += draft_profile.validate_extension_propagation(result, package)
    return errors
