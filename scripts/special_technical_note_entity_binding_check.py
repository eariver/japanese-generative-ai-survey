#!/usr/bin/env python3
"""Validate state-pinned Half-year Technical Note subject/entity binding provenance."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ENTITY_BINDING_CONTRACT = "SUBJECT_COMPONENT_VARIANT_PROPERTY_BINDING_V3"
NOTE_RE = re.compile(r"\\begin\{technicalnote\}\{(.+?)\}\{.*?\\end\{technicalnote\}", re.DOTALL)
FACT_RE = re.compile(r"^\\item \\textbf\{一次情報で確認できる事実\}: (.+)$", re.MULTILINE)
INPUT_RE = re.compile(r"\\(?:input|include)\{([^}]+)\}")
PROXIMITY_FALLBACK_RE = re.compile(r"対象\s*event\s*近傍", re.IGNORECASE)
FLAT_MULTI_FAMILY_PARAMETER_RE = re.compile(r"\b\d+(?:\.\d+)?[BM]\s+parameter\s+scale(?:\s*/\s*\d+(?:\.\d+)?[BM]\s+parameter\s+scale)+", re.IGNORECASE)


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected object")
    return value


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


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
    return re.sub(r"\s+", " ", text).strip()


def _contains_rendered_signal(fact: str, signal: str) -> bool:
    if not signal:
        return False
    return re.search(
        rf"(?<![A-Za-z0-9]){re.escape(signal)}(?![A-Za-z0-9])",
        fact,
    ) is not None


def _normalize_tex_path(value: str) -> str:
    text = str(value or "").strip().replace("\\", "/")
    while text.startswith("./"):
        text = text[2:]
    if text and not Path(text).suffix:
        text += ".tex"
    return Path(text).as_posix() if text else ""


def _coverage_population(reader: dict[str, Any]) -> tuple[int, int, int, str]:
    """Resolve entity-audit coverage using the same units as title-keyed audit artifacts.

    Audit rows and editorial overrides are keyed by canonical/rendered title, while
    ``source_specific_detail_visible_card_count`` counts rendered card placements and can be
    larger when one title is intentionally repeated in more than one article. New manifests
    persist the compatible unique-title population explicitly. Older manifests retain the
    historical placement-count fallback.
    """
    visible = int(reader.get("source_specific_detail_visible_card_count") or 0)
    overrides = int(reader.get("source_specific_detail_override_count") or 0)
    declared_population = int(reader.get("entity_binding_coverage_population_count") or 0)
    declared_basis = str(reader.get("entity_binding_coverage_basis") or "")
    declared_visible = int(reader.get("entity_binding_visible_card_placement_count") or 0)

    if declared_population > 0:
        if declared_basis != "UNIQUE_RENDERED_TITLE_COUNT":
            raise ValueError(
                "unsupported Technical Note entity-binding coverage basis: "
                f"{declared_basis or '<missing>'}"
            )
        if declared_visible and visible and declared_visible != visible:
            raise ValueError(
                "Technical Note entity-binding visible-card placement count mismatch: "
                f"declared={declared_visible} current={visible}"
            )
        if visible and declared_population > visible:
            raise ValueError(
                "Technical Note entity-binding coverage population exceeds visible card placements: "
                f"population={declared_population} visible={visible}"
            )
        population = declared_population
        basis = declared_basis
    else:
        population = visible
        basis = "VISIBLE_CARD_COUNT_LEGACY_FALLBACK"

    if overrides > population:
        raise ValueError(
            "Technical Note entity-binding override count exceeds compatible coverage population: "
            f"overrides={overrides} population={population} basis={basis}"
        )
    return population, visible, overrides, basis


def _rendered_top_level_tex_paths(
    manifest: dict[str, Any], source_dir: Path, errors: list[str]
) -> set[str] | None:
    main_info = manifest.get("main_tex")
    if not isinstance(main_info, dict):
        return None
    main_rel = _normalize_tex_path(str(main_info.get("path") or "main.tex"))
    main_path = source_dir / main_rel
    if not main_path.is_file():
        errors.append(f"main TeX missing during entity check: {main_rel}")
        return set()
    expected = str(main_info.get("sha256") or "")
    if expected and sha(main_path) != expected:
        errors.append(f"main TeX digest mismatch during entity check: {main_rel}")
        return set()
    return {
        _normalize_tex_path(match.group(1))
        for match in INPUT_RE.finditer(main_path.read_text(encoding="utf-8"))
        if _normalize_tex_path(match.group(1))
    }


def inspect_entity_binding(manifest: dict[str, Any], source_dir: Path) -> list[str]:
    errors: list[str] = []
    reader = manifest.get("reader_facing_technical_notes") or {}
    status = str(manifest.get("status") or "")
    declared_contract = reader.get("entity_binding_contract")

    # The original source-specific-notes revision requires V3 fail-closed.
    # Later descendants may use a different status, so any descendant that
    # carries the V3 contract must still be audited regardless of status.
    if status == "VALIDATED_HALF_YEAR_SOURCE_SPECIFIC_NOTES_REVISION":
        if declared_contract != ENTITY_BINDING_CONTRACT:
            errors.append(
                "Half-year Technical Notes lack the required subject/entity binding contract "
                "(component/variant/property V3 required): "
                f"expected={ENTITY_BINDING_CONTRACT} actual={declared_contract}"
            )
            return errors
    elif declared_contract is None:
        return errors
    elif declared_contract != ENTITY_BINDING_CONTRACT:
        errors.append(
            "Half-year Technical Notes lack the required subject/entity binding contract "
            "(component/variant/property V3 required): "
            f"expected={ENTITY_BINDING_CONTRACT} actual={declared_contract}"
        )
        return errors

    if reader.get("source_specific_detail_contract") != "SCREENING_BACKED_FAIL_CLOSED":
        errors.append("Half-year Technical Notes lost SCREENING_BACKED_FAIL_CLOSED provenance")

    audit_rel = str(reader.get("entity_binding_audit_path") or "")
    expected_audit_sha = str(reader.get("entity_binding_audit_sha256") or "")
    audit_path = source_dir / audit_rel
    if not audit_rel or not audit_path.is_file():
        errors.append("Technical Note entity-binding audit is missing")
        return errors
    actual_audit_sha = sha(audit_path)
    if not expected_audit_sha or actual_audit_sha != expected_audit_sha:
        errors.append(
            "Technical Note entity-binding audit digest mismatch: "
            f"actual={actual_audit_sha} expected={expected_audit_sha}"
        )
        return errors

    audit = load_json(audit_path)
    if audit.get("contract") != ENTITY_BINDING_CONTRACT:
        errors.append("Technical Note entity-binding audit contract marker mismatch")
    artifacts = [item for item in (audit.get("artifacts") or []) if isinstance(item, dict)]
    audited_count = int(reader.get("entity_binding_audited_artifact_count") or 0)
    audit_artifact_count = int(audit["artifact_count"]) if "artifact_count" in audit else -1
    if audited_count != len(artifacts) or audit_artifact_count != len(artifacts):
        errors.append(
            "Technical Note entity-binding audit count mismatch: "
            f"manifest={audited_count} audit={audit.get('artifact_count')} actual={len(artifacts)}"
        )

    try:
        population, visible, overrides, coverage_basis = _coverage_population(reader)
    except ValueError as exc:
        errors.append(str(exc))
        population = visible = overrides = 0
        coverage_basis = "INVALID"
    if coverage_basis != "INVALID" and len(artifacts) < max(0, population - overrides):
        errors.append(
            "Technical Note entity-binding audit does not cover automatically extracted unique titles: "
            f"audited={len(artifacts)} population={population} basis={coverage_basis} "
            f"visible_placements={visible} overrides={overrides}"
        )

    rendered_paths = _rendered_top_level_tex_paths(manifest, source_dir, errors)
    if rendered_paths == set() and errors:
        return errors

    cards: dict[str, list[str]] = {}
    for article in manifest.get("articles") or []:
        if not isinstance(article, dict) or article.get("technical_notes_reader_facing") is not True:
            continue
        rel = _normalize_tex_path(str(article.get("technical_notes_path") or ""))
        if rendered_paths is not None and rel not in rendered_paths:
            continue
        path = source_dir / rel
        if not rel or not path.is_file():
            errors.append(f"reader-facing Technical Notes file missing during entity check: {rel}")
            continue
        expected = str(article.get("technical_notes_sha256") or "")
        if expected and sha(path) != expected:
            errors.append(f"Technical Notes digest mismatch during entity check: {rel}")
            continue
        for match in NOTE_RE.finditer(path.read_text(encoding="utf-8")):
            key = _title_key(match.group(1))
            card = match.group(0)
            if reader.get("annual_source_specific_detail_contract") and PROXIMITY_FALLBACK_RE.search(card):
                errors.append(f"Technical Note contains forbidden proximity fallback: {key}")
            fact_for_shape = FACT_RE.search(card)
            if reader.get("annual_source_specific_detail_contract") and "/" in key and fact_for_shape is not None and FLAT_MULTI_FAMILY_PARAMETER_RE.search(fact_for_shape.group(1)):
                errors.append(f"Technical Note flattens scope-sensitive parameter scales across a multi-family title: {key}")
            existing = cards.setdefault(key, [])
            if existing:
                current_fact = FACT_RE.search(card)
                current_text = current_fact.group(1) if current_fact is not None else None
                prior_facts = [FACT_RE.search(item) for item in existing]
                prior_texts = [item.group(1) if item is not None else None for item in prior_facts]
                if any(prior != current_text for prior in prior_texts):
                    errors.append(
                        f"conflicting reader-facing Technical Note fact for duplicate title during entity check: {key}"
                    )
            existing.append(card)

    for item in artifacts:
        title = _title_key(str(item.get("title") or ""))
        if not title:
            errors.append("entity-binding audit contains an empty title")
            continue
        card_group = cards.get(title)
        if not card_group:
            continue
        facts: list[str] = []
        for card in card_group:
            fact_match = FACT_RE.search(card)
            if fact_match is None:
                errors.append(f"Technical Note primary-fact line missing during entity check: {title}")
                continue
            fact = fact_match.group(1)
            if fact not in facts:
                facts.append(fact)

        accepted = {str(signal) for signal in (item.get("accepted_entity_bound_signals") or []) if str(signal)}
        rejected_only = [
            str(signal)
            for signal in (item.get("rejected_entity_bound_signals") or [])
            if str(signal) and str(signal) not in accepted
        ]
        for fact in facts:
            for signal in rejected_only:
                if _contains_rendered_signal(fact, signal):
                    errors.append(
                        f"Technical Note contains a source signal rejected by subject binding: {title}: {signal}"
                    )

    rejected_actual = sum(len(item.get("rejected_entity_bound_signals") or []) for item in artifacts)
    rejected_manifest = int(reader.get("entity_binding_rejected_signal_count") or 0)
    if rejected_actual != rejected_manifest:
        errors.append(
            "Technical Note entity-binding rejected-signal count mismatch: "
            f"manifest={rejected_manifest} actual={rejected_actual}"
        )
    return errors


def check(repo_root: Path, issue_id: str) -> dict[str, Any]:
    state_path = repo_root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    source = (state.get("provenance") or {}).get("validated_issue_source") or {}
    manifest_path = repo_root / str(source.get("path") or "")
    if not manifest_path.is_file() or sha(manifest_path) != str(source.get("sha256") or ""):
        raise ValueError("state-pinned source manifest missing or SHA mismatch")
    manifest = load_json(manifest_path)
    errors = inspect_entity_binding(manifest, manifest_path.parent)
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "source_manifest": manifest_path.relative_to(repo_root).as_posix(),
        "contract": ENTITY_BINDING_CONTRACT,
        "passed": not errors,
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--issue-id", required=True)
    args = parser.parse_args()
    report = check(Path(args.repo_root).resolve(), args.issue_id)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
