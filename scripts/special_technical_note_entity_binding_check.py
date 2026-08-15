#!/usr/bin/env python3
"""Validate state-pinned Half-year Technical Note subject/entity binding provenance."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ENTITY_BINDING_CONTRACT = "SUBJECT_VERSION_AWARE_HIGH_RISK_SIGNALS_V2"
NOTE_RE = re.compile(r"\\begin\{technicalnote\}\{(.+?)\}\{.*?\\end\{technicalnote\}", re.DOTALL)
FACT_RE = re.compile(r"^\\item \\textbf\{一次情報で確認できる事実\}: (.+)$", re.MULTILINE)


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


def inspect_entity_binding(manifest: dict[str, Any], source_dir: Path) -> list[str]:
    """Return fail-closed pre-release findings for Half-year source-specific notes."""
    errors: list[str] = []
    if str(manifest.get("status") or "") != "VALIDATED_HALF_YEAR_SOURCE_SPECIFIC_NOTES_REVISION":
        return errors

    reader = manifest.get("reader_facing_technical_notes") or {}
    if reader.get("source_specific_detail_contract") != "SCREENING_BACKED_FAIL_CLOSED":
        errors.append("Half-year Technical Notes lost SCREENING_BACKED_FAIL_CLOSED provenance")
    if reader.get("entity_binding_contract") != ENTITY_BINDING_CONTRACT:
        errors.append(
            "Half-year Technical Notes lack the required subject/entity binding contract "
            "(version-aware V2 required): "
            f"expected={ENTITY_BINDING_CONTRACT} actual={reader.get('entity_binding_contract')}"
        )
        return errors

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
    if audited_count != len(artifacts) or int(audit.get("artifact_count") or -1) != len(artifacts):
        errors.append(
            "Technical Note entity-binding audit count mismatch: "
            f"manifest={audited_count} audit={audit.get('artifact_count')} actual={len(artifacts)}"
        )

    visible = int(reader.get("source_specific_detail_visible_card_count") or 0)
    overrides = int(reader.get("source_specific_detail_override_count") or 0)
    if len(artifacts) < max(0, visible - overrides):
        errors.append(
            "Technical Note entity-binding audit does not cover automatically extracted visible cards: "
            f"audited={len(artifacts)} visible={visible} overrides={overrides}"
        )

    cards: dict[str, list[str]] = {}
    for article in manifest.get("articles") or []:
        if not isinstance(article, dict) or article.get("technical_notes_reader_facing") is not True:
            continue
        rel = str(article.get("technical_notes_path") or "")
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
            # Suppressed/non-reader-facing Evidence can still be audited by the generator.
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
        # The audit is occurrence-aware while the reader-facing card is value-only. A value may
        # therefore appear in both lists when one occurrence is correctly bound to the selected
        # artifact and another occurrence belongs to a comparator. Any accepted occurrence is
        # sufficient authority to render that value; only rejected-only signals are forbidden.
        rejected_only = [
            str(signal)
            for signal in (item.get("rejected_entity_bound_signals") or [])
            if str(signal) and str(signal) not in accepted
        ]
        for fact in facts:
            for signal in rejected_only:
                if signal in fact:
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
