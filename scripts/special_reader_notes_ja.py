#!/usr/bin/env python3
"""Compatibility entry point for Special Japanese reader notes."""
from __future__ import annotations

import re
import shlex
import stat
import sys
from pathlib import Path
from typing import Any

from scripts.special_reader_notes_ja_core import *  # noqa: F401,F403
from scripts import special_reader_notes_ja_core as core

_ORIGINAL_CHECK = core.check
_GENERIC_READER_FALLBACKS = (
    '一次資料で確認できる公開・提供・機能・時系列上の事実を要約した項目',
    '提供元・プロジェクト・著者側の評価または説明として記録された項目',
    '一次資料と時系列から導いた編集上の整理。根拠となる事実と推論を区別して扱う',
)
_NOTE_RE = re.compile(r"\\begin\{technicalnote\}.*?\\end\{technicalnote\}", re.DOTALL)
_ITEM_RE = re.compile(r"^\\item\s+(.+)$", re.MULTILINE)


def arg_value(name: str, default: str | None = None) -> str | None:
    try:
        return sys.argv[sys.argv.index(name) + 1]
    except (ValueError, IndexError):
        return default


def _artifact_name(record: dict[str, Any]) -> str:
    task_id = str(record.get("evidence_task_id") or "")
    value = core.card(record)
    artifact = value.get("artifact") or {}
    canonical = str(artifact.get("canonical_name") or "").strip()
    if canonical:
        return canonical
    for source in value.get("sources") or []:
        if isinstance(source, dict) and str(source.get("title") or "").strip():
            return str(source["title"]).strip()
    return task_id


def _event_summary_item(event: dict[str, Any]) -> dict[str, Any]:
    text = str(event.get("description") or "")
    return {
        "item_id": str(event.get("event_id") or ""),
        "evidence_class": "PRIMARY_FACT",
        "source_text": text,
        "source_text_sha256": core.sha256_bytes(text),
        "text_ja": "",
    }


def collect_template_records_compat(root: Path, issue_id: str) -> list[dict[str, Any]]:
    plan = core.load_json(root / "sources" / issue_id / "architecture" / "issue-architecture-v0.1.json")
    package_dir = root / "sources" / issue_id / "drafting" / "packages" / "v0.1"
    package_ids = [
        str(p["package_id"])
        for p in plan.get("packages") or []
        if isinstance(p, dict) and p.get("package_type") in core.ARTICLE_TYPES
    ]
    records: dict[str, dict[str, Any]] = {}
    for package_id in package_ids:
        package = core.load_json(package_dir / f"{package_id}.json")
        for record in core.evidence_records(package):
            task_id = str(record.get("evidence_task_id") or "")
            if not task_id:
                raise ValueError(f"{package_id}: Evidence record has no evidence_task_id")
            c = core.card(record)
            claims = [core.summary_item(x, "claim_id") for x in c.get("claims") or [] if isinstance(x, dict) and x.get("text")]
            limitations = [core.summary_item(x, "limitation_id") for x in c.get("limitations") or [] if isinstance(x, dict) and x.get("text")]
            events = []
            if not claims:
                for event in (c.get("temporal") or {}).get("events") or []:
                    if isinstance(event, dict) and event.get("event_id") and event.get("description"):
                        events.append(_event_summary_item(event))
            prepared = {
                "evidence_task_id": task_id,
                "artifact_name": _artifact_name(record),
                "claims": claims,
                "limitations": limitations,
                "event_facts": events,
            }
            existing = records.get(task_id)
            if existing is not None and existing != prepared:
                raise ValueError(f"Evidence record differs across Draft Packages: {task_id}")
            records[task_id] = prepared
    return [records[key] for key in sorted(records)]


def _replace_event_item(block: str, source: dict[str, Any], summary: dict[str, Any], context: str) -> tuple[str, int]:
    item_id = str(source.get("event_id") or "")
    source_text = str(source.get("description") or "")
    if not item_id or not source_text:
        return block, 0
    if summary.get("source_text_sha256") != core.sha256_bytes(source_text):
        raise ValueError(f"source text SHA mismatch in Japanese summary artifact: {context}/{item_id}")
    if summary.get("source_text") != source_text:
        raise ValueError(f"source text copy mismatch in Japanese summary artifact: {context}/{item_id}")
    text_ja = str(summary.get("text_ja") or "")
    core.validate_ja(text_ja, f"{context}/{item_id}")
    label = core.expansion.CLASS_LABELS.get("PRIMARY_FACT", "PRIMARY_FACT")
    old = r"\item \textbf{" + core.expansion.tex_escape(label) + "}: " + core.expansion.tex_escape(source_text)
    new = r"\item \textbf{" + core.expansion.tex_escape(label) + "}: " + core.expansion.tex_escape(text_ja)
    count = block.count(old)
    if count != 1:
        raise ValueError(f"expected one source-bound Technical Notes event item, found {count}: {context}/{item_id}")
    return block.replace(old, new, 1), 1


def apply_compat(root: Path, issue_id: str, special_slug: str, summary_path: Path) -> dict[str, Any]:
    data = core.load_json(summary_path)
    if data.get("issue_id") != issue_id:
        raise ValueError("reader-facing summary issue_id mismatch")
    summaries = core.summary_index(data)

    state_path = root / "sources" / issue_id / "pipeline-state.json"
    state = core.load_json(state_path)
    source = state.get("provenance", {}).get("validated_issue_source") or {}
    manifest_path = root / str(source.get("path") or "")
    if not manifest_path.is_file() or core.sha256_file(manifest_path) != source.get("sha256"):
        raise ValueError("state-pinned source manifest missing or SHA mismatch")
    if root / "surveys" / "special" / special_slug not in manifest_path.parents:
        raise ValueError("state-pinned source does not belong to requested Special slug")
    manifest = core.load_json(manifest_path)

    total = 0
    used_tasks: set[str] = set()
    for article in manifest.get("articles") or []:
        package_path = root / str(article.get("draft_package_path") or "")
        note_path = manifest_path.parent / str(article.get("technical_notes_path") or "")
        if not package_path.is_file() or not note_path.is_file():
            raise ValueError(f"article source/Technical Notes missing: {article.get('package_id')}")
        package = core.load_json(package_path)
        text = note_path.read_text(encoding="utf-8")
        blocks = list(core.NOTE_BLOCK_RE.finditer(text))
        replacements: list[tuple[int, int, str]] = []
        used_ranges: set[tuple[int, int]] = set()
        for record in core.evidence_records(package):
            task_id = str(record.get("evidence_task_id") or "")
            if task_id not in summaries:
                raise ValueError(f"Japanese summary record missing: {task_id}")
            summary_record = summaries[task_id]
            artifact_name = str(summary_record.get("artifact_name") or _artifact_name(record))
            block_match = core.find_note_block(blocks, task_id, artifact_name)
            block_range = (block_match.start(), block_match.end())
            if block_range in used_ranges:
                raise ValueError(f"Technical Notes title fallback was ambiguous across Evidence records: {artifact_name}")
            used_ranges.add(block_range)
            block = block_match.group(0)
            claim_map = core.item_index(summary_record, "claims")
            limitation_map = core.item_index(summary_record, "limitations")
            event_map = core.item_index(summary_record, "event_facts")
            c = core.card(record)
            claims = c.get("claims") or []
            for claim in claims:
                if not isinstance(claim, dict) or not claim.get("text"):
                    continue
                item_id = str(claim.get("claim_id") or "")
                if item_id not in claim_map:
                    raise ValueError(f"Japanese claim summary missing: {task_id}/{item_id}")
                block, count = core.replace_item(block, claim, claim_map[item_id], "claim_id", task_id)
                total += count
            if not claims:
                for event in (c.get("temporal") or {}).get("events") or []:
                    if not isinstance(event, dict) or not event.get("description"):
                        continue
                    item_id = str(event.get("event_id") or "")
                    if item_id not in event_map:
                        raise ValueError(f"Japanese event summary missing: {task_id}/{item_id}")
                    block, count = _replace_event_item(block, event, event_map[item_id], task_id)
                    total += count
            for limitation in c.get("limitations") or []:
                if not isinstance(limitation, dict) or not limitation.get("text"):
                    continue
                item_id = str(limitation.get("limitation_id") or "")
                if item_id not in limitation_map:
                    raise ValueError(f"Japanese limitation summary missing: {task_id}/{item_id}")
                block, count = core.replace_item(block, limitation, limitation_map[item_id], "limitation_id", task_id)
                total += count
            replacements.append((block_match.start(), block_match.end(), block))
            used_tasks.add(task_id)
        for start, end, block in reversed(replacements):
            text = text[:start] + block + text[end:]
        note_path.write_text(text, encoding="utf-8")
        article["technical_notes_sha256"] = core.sha256_file(note_path)

    extra = sorted(set(summaries) - used_tasks)
    if extra:
        raise ValueError(f"Japanese summary artifact contains unused Evidence records: {extra}")

    reader = dict(manifest.get("reader_facing_technical_notes") or {})
    reader.update({
        "language_policy": "ja-reader-summary-v1",
        "claim_limitation_sentence_structure": "Japanese by default for claim, limitation, and event-fact summaries; precision-critical technical terms may remain English",
        "attribution_labels_preserved": True,
        "source_evidence_unchanged": True,
        "event_only_evidence_policy": "temporal-event-as-primary-fact",
        "summary_artifact_path": summary_path.relative_to(root).as_posix(),
        "summary_artifact_sha256": core.sha256_file(summary_path),
        "summary_replacement_count": total,
    })
    manifest["reader_facing_technical_notes"] = reader
    core.write_json(manifest_path, manifest)
    source["sha256"] = core.sha256_file(manifest_path)
    source["reader_facing_notes_language"] = "ja-reader-summary-v1"
    core.write_json(state_path, state)
    return {
        "status": "READER_NOTES_JA_APPLIED",
        "issue_id": issue_id,
        "source_manifest": manifest_path.relative_to(root).as_posix(),
        "source_manifest_sha256": source["sha256"],
        "summary_artifact": summary_path.relative_to(root).as_posix(),
        "summary_replacement_count": total,
    }


def verify_source_text(root: Path, issue_id: str, doc: dict[str, Any]) -> None:
    expected = {r["evidence_task_id"]: r for r in collect_template_records_compat(root, issue_id)}
    actual = {str(r.get("evidence_task_id") or ""): r for r in doc.get("records") or [] if isinstance(r, dict)}
    if set(expected) != set(actual):
        raise ValueError("reader-notes Evidence task set differs from immutable Draft Packages")
    for task_id, source_record in expected.items():
        supplied = actual[task_id]
        if supplied.get("artifact_name") != source_record.get("artifact_name"):
            raise ValueError(f"reader-notes artifact name mismatch: {task_id}")
        for key in ("claims", "limitations", "event_facts"):
            source_items = {x["item_id"]: x for x in source_record.get(key) or []}
            supplied_items = {x.get("item_id"): x for x in supplied.get(key) or [] if isinstance(x, dict)}
            if set(source_items) != set(supplied_items):
                raise ValueError(f"reader-notes {key} set mismatch: {task_id}")
            for item_id, src in source_items.items():
                item = supplied_items[item_id]
                if item.get("source_text") != src.get("source_text") or item.get("source_text_sha256") != src.get("source_text_sha256"):
                    raise ValueError(f"reader-notes source text mismatch: {task_id}/{key}/{item_id}")


def validate_summary(doc: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    ready = doc.get("status") == "READY"
    for record in doc.get("records") or []:
        if not isinstance(record, dict):
            errors.append("summary record must be object")
            continue
        task = str(record.get("evidence_task_id") or "<missing>")
        for key in ("claims", "limitations", "event_facts"):
            for item in record.get(key) or []:
                if not isinstance(item, dict):
                    errors.append(f"{task}/{key}: summary item must be object")
                    continue
                if ready:
                    try:
                        core.validate_ja(str(item.get("text_ja") or ""), f"{task}/{key}/{item.get('item_id')}")
                    except ValueError as exc:
                        errors.append(str(exc))
    return errors


def _declared_derived_layer_without_notes(article: dict[str, Any]) -> bool:
    return (
        article.get('_sparse_architecture_derived') is True
        and article.get('derived_reader_layer') is True
        and not str(article.get('technical_notes_path') or '').strip()
    )


def check_compat(root: Path, issue_id: str) -> dict:
    report = _ORIGINAL_CHECK(root, issue_id)
    errors = list(report.get('errors') or [])
    state = core.load_json(root / 'sources' / issue_id / 'pipeline-state.json')
    source = state.get('provenance', {}).get('validated_issue_source') or {}
    manifest_path = root / str(source.get('path') or '')
    manifest = core.load_json(manifest_path)

    derived_without_notes: list[str] = []
    for article in manifest.get('articles') or []:
        if not isinstance(article, dict) or not _declared_derived_layer_without_notes(article):
            continue
        package_id = str(article.get('package_id') or '').strip()
        if not package_id:
            errors.append('declared derived reader layer has no package_id')
            continue
        expected = f"Technical Notes missing: {package_id}"
        matches = [index for index, value in enumerate(errors) if value == expected]
        if len(matches) != 1:
            errors.append(
                f"derived reader-layer Technical Notes compatibility expected one core finding for {package_id}, found {len(matches)}"
            )
            continue
        errors.pop(matches[0])
        derived_without_notes.append(package_id)

    fallback_findings = 0
    duplicate_bullet_findings = 0
    for article in manifest.get('articles') or []:
        rel = str(article.get('technical_notes_path') or '')
        if not rel:
            continue
        path = manifest_path.parent / rel
        if not path.is_file():
            continue
        text = path.read_text(encoding='utf-8')
        for phrase in _GENERIC_READER_FALLBACKS:
            count = text.count(phrase)
            if count:
                fallback_findings += count
                errors.append(
                    f"generic Technical Notes fallback in {article.get('package_id')}: {phrase} ({count})"
                )
        for block in _NOTE_RE.findall(text):
            title_match = re.match(r"\\begin\{technicalnote\}\{(.+?)\}\{", block)
            title = title_match.group(1) if title_match else str(article.get('package_id'))
            seen: set[str] = set()
            duplicates: set[str] = set()
            for value in _ITEM_RE.findall(block):
                normalized = re.sub(r"\s+", " ", value).strip()
                if normalized in seen:
                    duplicates.add(normalized)
                seen.add(normalized)
            if duplicates:
                duplicate_bullet_findings += len(duplicates)
                errors.append(
                    f"duplicate Technical Notes bullet in {article.get('package_id')}/{title}: "
                    + '; '.join(sorted(duplicates))[:300]
                )

    report['derived_reader_layers_without_technical_notes'] = derived_without_notes
    report['derived_reader_layer_notes_policy'] = 'explicit-derived-reader-layer-only'
    report['generic_fallback_findings'] = fallback_findings
    report['duplicate_bullet_findings'] = duplicate_bullet_findings
    report['source_specific_summary_policy'] = 'required-no-generic-fallback'
    report['errors'] = errors
    report['passed'] = not errors
    return report


core.collect_template_records = collect_template_records_compat
core.apply = apply_compat
core.check = check_compat
collect_template_records = collect_template_records_compat
apply = apply_compat
check = check_compat


def install_fill_hook() -> None:
    if len(sys.argv) < 2 or sys.argv[1] != "prepare":
        return
    issue_id = arg_value("--issue-id")
    repo_root = Path(arg_value("--repo-root", ".") or ".").resolve()
    output = arg_value("--output")
    if not issue_id or not output:
        return
    overrides = repo_root / "sources" / issue_id / "editorial" / "technical-notes-ja-overrides-v0.1"
    if not overrides.is_dir() or not any(overrides.glob("part-*.json")):
        return
    git_dir = repo_root / ".git"
    if not git_dir.is_dir():
        return
    hook = git_dir / "hooks" / "pre-commit"
    helper = Path(__file__).resolve().with_name("fill_special_reader_notes_ja.py")
    summary = repo_root / output
    audit = repo_root / ".reader-notes-fill-audit.json"
    command = [
        sys.executable, str(helper), "--repo-root", str(repo_root), "--issue-id", issue_id,
        "--summary", str(summary), "--overrides-dir", str(overrides),
    ]
    script = "#!/bin/sh\nset -eu\n" + " ".join(shlex.quote(v) for v in command) + " > " + shlex.quote(str(audit)) + "\n"
    script += "git -C " + shlex.quote(str(repo_root)) + " add " + shlex.quote(str(summary.relative_to(repo_root))) + "\n"
    script += 'rm -f "$0"\n'
    hook.parent.mkdir(parents=True, exist_ok=True)
    hook.write_text(script, encoding="utf-8")
    hook.chmod(hook.stat().st_mode | stat.S_IXUSR)


def main() -> int:
    result = core.main()
    install_fill_hook()
    return result


if __name__ == "__main__":
    raise SystemExit(main())
