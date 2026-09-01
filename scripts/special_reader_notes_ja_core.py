#!/usr/bin/env python3
"""Prepare, apply, and validate Japanese reader-facing Special Technical Notes.

Evidence cards remain immutable. This module creates a SHA-bound editorial layer
that maps exact normalized claim/limitation text to Japanese reader-facing
summaries, then applies only that layer to derived PDF-facing TeX.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

from scripts import expand_special_validated_source as expansion
from scripts import postprocess_special_reader_facing_notes as reader_taxonomy

ARTICLE_TYPES = {
    "LEAD", "FEATURE", "COMPARISON", "SECTION", "DEEP_DIVE", "PAPER_WATCH",
    "X_COMMUNITY", "LATE_BREAKING", "WATCHLIST_CHRONOLOGY",
}
JP_RE = re.compile(r"[ぁ-んァ-ヶ一-龠々〆ヵヶー]")
NOTE_BLOCK_RE = re.compile(r"\\begin\{technicalnote\}.*?\\end\{technicalnote\}", re.DOTALL)
RAW_EVENT_ENUMS = {
    "OFFICIAL_PUBLICATION", "PRODUCT_RELEASE", "PRODUCT_UPDATE", "AGENT_RELEASE",
    "FRAMEWORK_RELEASE", "MODEL_RELEASE", "MODEL_UPDATE", "OPEN_WEIGHT_RELEASE",
    "PAPER_RELEASE", "RESEARCH_RELEASE", "SAFETY_EVENT", "API_RELEASE", "API_UPDATE",
}
RAW_TYPE_ENUMS = {
    "OTHER", "MODEL_UPDATE", "OPEN_WEIGHT", "FRAMEWORK_RELEASE", "SAFETY_EVENT",
}
MIXED_ENUM_RE = re.compile(r"(?:モデル|研究|論文|Framework|Agent|API)(?:\\_|_)(?:RELEASE|UPDATE|PUBLICATION)")


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected JSON object")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_bytes(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def evidence_records(package: dict[str, Any]) -> list[dict[str, Any]]:
    values: list[dict[str, Any]] = []
    for key in ("primary_evidence", "supporting_evidence"):
        for record in package.get(key) or []:
            if not isinstance(record, dict):
                raise ValueError(f"{package.get('package_id')}: invalid {key} record")
            values.append(record)
    return values


def card(record: dict[str, Any]) -> dict[str, Any]:
    value = record.get("card") or {}
    if not isinstance(value, dict):
        raise ValueError("Evidence card must be an object")
    return value


def summary_item(source: dict[str, Any], id_key: str) -> dict[str, Any]:
    text = str(source.get("text") or "")
    return {
        "item_id": str(source.get(id_key) or ""),
        "evidence_class": str(source.get("evidence_class") or ""),
        "source_text": text,
        "source_text_sha256": sha256_bytes(text),
        "text_ja": "",
    }


def collect_template_records(root: Path, issue_id: str) -> list[dict[str, Any]]:
    plan = load_json(root / "sources" / issue_id / "architecture" / "issue-architecture-v0.1.json")
    package_dir = root / "sources" / issue_id / "drafting" / "packages" / "v0.1"
    package_ids = [
        str(p["package_id"])
        for p in plan.get("packages") or []
        if isinstance(p, dict) and p.get("package_type") in ARTICLE_TYPES
    ]
    records: dict[str, dict[str, Any]] = {}
    for package_id in package_ids:
        package = load_json(package_dir / f"{package_id}.json")
        for record in evidence_records(package):
            task_id = str(record.get("evidence_task_id") or "")
            if not task_id:
                raise ValueError(f"{package_id}: Evidence record has no evidence_task_id")
            c = card(record)
            artifact = c.get("artifact") or {}
            prepared = {
                "evidence_task_id": task_id,
                "artifact_name": str(artifact.get("canonical_name") or task_id),
                "claims": [summary_item(x, "claim_id") for x in c.get("claims") or [] if isinstance(x, dict) and x.get("text")],
                "limitations": [summary_item(x, "limitation_id") for x in c.get("limitations") or [] if isinstance(x, dict) and x.get("text")],
            }
            existing = records.get(task_id)
            if existing is not None and existing != prepared:
                raise ValueError(f"Evidence record differs across Draft Packages: {task_id}")
            records[task_id] = prepared
    return [records[key] for key in sorted(records)]


def prepare(root: Path, issue_id: str, output: Path) -> dict[str, Any]:
    if output.exists():
        raise ValueError(f"reader-facing summary artifact already exists: {output}")
    records = collect_template_records(root, issue_id)
    value = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "status": "DRAFT",
        "policy": {
            "reader_language": "ja",
            "technical_terms_may_remain_english": True,
            "attribution_labels_preserved": True,
            "source_evidence_mutation_forbidden": True,
            "instruction": "Fill every text_ja with natural Japanese, preserve model/API/benchmark/paper-defined terms when precision benefits, then set status to READY.",
        },
        "records": records,
    }
    write_json(output, value)
    return {
        "status": "READER_NOTES_JA_TEMPLATE_PREPARED",
        "issue_id": issue_id,
        "output": output.relative_to(root).as_posix(),
        "record_count": len(records),
        "claim_count": sum(len(r["claims"]) for r in records),
        "limitation_count": sum(len(r["limitations"]) for r in records),
    }


def validate_ja(text: str, context: str) -> None:
    if not text.strip():
        raise ValueError(f"missing Japanese reader-facing summary: {context}")
    if not JP_RE.search(text):
        raise ValueError(f"reader-facing summary must use Japanese sentence structure: {context}")


def summary_index(data: dict[str, Any]) -> dict[str, dict[str, Any]]:
    if data.get("status") != "READY":
        raise ValueError("reader-facing Technical Notes summary artifact must have status READY")
    result: dict[str, dict[str, Any]] = {}
    for record in data.get("records") or []:
        if not isinstance(record, dict):
            raise ValueError("summary record must be an object")
        task_id = str(record.get("evidence_task_id") or "")
        if not task_id or task_id in result:
            raise ValueError(f"invalid/duplicate summary evidence_task_id: {task_id}")
        result[task_id] = record
    return result


def item_index(record: dict[str, Any], key: str) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for item in record.get(key) or []:
        if not isinstance(item, dict):
            raise ValueError(f"{key}: summary item must be object")
        item_id = str(item.get("item_id") or "")
        if not item_id or item_id in result:
            raise ValueError(f"{key}: invalid/duplicate item_id {item_id}")
        result[item_id] = item
    return result


def replace_item(block: str, source: dict[str, Any], summary: dict[str, Any], id_key: str, context: str) -> tuple[str, int]:
    item_id = str(source.get(id_key) or "")
    source_text = str(source.get("text") or "")
    if not item_id or not source_text:
        return block, 0
    if summary.get("source_text_sha256") != sha256_bytes(source_text):
        raise ValueError(f"source text SHA mismatch in Japanese summary artifact: {context}/{item_id}")
    if summary.get("source_text") != source_text:
        raise ValueError(f"source text copy mismatch in Japanese summary artifact: {context}/{item_id}")
    text_ja = str(summary.get("text_ja") or "")
    validate_ja(text_ja, f"{context}/{item_id}")
    cls = str(source.get("evidence_class") or ("INFERENCE" if id_key == "limitation_id" else ""))
    label = expansion.CLASS_LABELS.get(cls, cls or "Claim")
    old = r"\item \textbf{" + expansion.tex_escape(label) + "}: " + expansion.tex_escape(source_text)
    new = r"\item \textbf{" + expansion.tex_escape(label) + "}: " + expansion.tex_escape(text_ja)
    count = block.count(old)
    if count != 1:
        raise ValueError(f"expected one source-bound Technical Notes item, found {count}: {context}/{item_id}")
    return block.replace(old, new, 1), 1


def find_note_block(blocks: list[re.Match[str]], task_id: str, artifact_name: str) -> re.Match[str]:
    """Find a card before or after repository-only Source-bound IDs are stripped."""
    marker = "Source-bound record: \\texttt{" + expansion.tex_escape(task_id) + "}"
    by_id = [m for m in blocks if marker in m.group(0)]
    if len(by_id) == 1:
        return by_id[0]
    if len(by_id) > 1:
        raise ValueError(f"multiple Technical Notes blocks contain Evidence ID: {task_id}")

    title_prefix = r"\begin{technicalnote}{" + expansion.tex_escape(artifact_name) + "}{"
    by_title = [m for m in blocks if m.group(0).startswith(title_prefix)]
    if len(by_title) != 1:
        raise ValueError(
            f"expected one Technical Notes block for {task_id}; Source-bound ID is absent and title fallback found {len(by_title)} for {artifact_name!r}"
        )
    return by_title[0]


def apply(root: Path, issue_id: str, special_slug: str, summary_path: Path) -> dict[str, Any]:
    data = load_json(summary_path)
    if data.get("issue_id") != issue_id:
        raise ValueError("reader-facing summary issue_id mismatch")
    summaries = summary_index(data)

    state_path = root / "sources" / issue_id / "pipeline-state.json"
    state = load_json(state_path)
    source = state.get("provenance", {}).get("validated_issue_source") or {}
    manifest_path = root / str(source.get("path") or "")
    if not manifest_path.is_file() or sha256_file(manifest_path) != source.get("sha256"):
        raise ValueError("state-pinned source manifest missing or SHA mismatch")
    if root / "surveys" / "special" / special_slug not in manifest_path.parents:
        raise ValueError("state-pinned source does not belong to requested Special slug")
    manifest = load_json(manifest_path)

    total = 0
    used_tasks: set[str] = set()
    for article in manifest.get("articles") or []:
        package_path = root / str(article.get("draft_package_path") or "")
        note_path = manifest_path.parent / str(article.get("technical_notes_path") or "")
        if not package_path.is_file() or not note_path.is_file():
            raise ValueError(f"article source/Technical Notes missing: {article.get('package_id')}")
        package = load_json(package_path)
        text = note_path.read_text(encoding="utf-8")
        blocks = list(NOTE_BLOCK_RE.finditer(text))
        replacements: list[tuple[int, int, str]] = []
        used_ranges: set[tuple[int, int]] = set()
        for record in evidence_records(package):
            task_id = str(record.get("evidence_task_id") or "")
            if task_id not in summaries:
                raise ValueError(f"Japanese summary record missing: {task_id}")
            summary_record = summaries[task_id]
            artifact_name = str(summary_record.get("artifact_name") or (card(record).get("artifact") or {}).get("canonical_name") or task_id)
            block_match = find_note_block(blocks, task_id, artifact_name)
            block_range = (block_match.start(), block_match.end())
            if block_range in used_ranges:
                raise ValueError(f"Technical Notes title fallback was ambiguous across Evidence records: {artifact_name}")
            used_ranges.add(block_range)
            block = block_match.group(0)
            claim_map = item_index(summary_record, "claims")
            limitation_map = item_index(summary_record, "limitations")
            c = card(record)
            for claim in c.get("claims") or []:
                if not isinstance(claim, dict) or not claim.get("text"):
                    continue
                item_id = str(claim.get("claim_id") or "")
                if item_id not in claim_map:
                    raise ValueError(f"Japanese claim summary missing: {task_id}/{item_id}")
                block, count = replace_item(block, claim, claim_map[item_id], "claim_id", task_id)
                total += count
            for limitation in c.get("limitations") or []:
                if not isinstance(limitation, dict) or not limitation.get("text"):
                    continue
                item_id = str(limitation.get("limitation_id") or "")
                if item_id not in limitation_map:
                    raise ValueError(f"Japanese limitation summary missing: {task_id}/{item_id}")
                block, count = replace_item(block, limitation, limitation_map[item_id], "limitation_id", task_id)
                total += count
            replacements.append((block_match.start(), block_match.end(), block))
            used_tasks.add(task_id)
        for start, end, block in reversed(replacements):
            text = text[:start] + block + text[end:]
        note_path.write_text(text, encoding="utf-8")
        article["technical_notes_sha256"] = sha256_file(note_path)

    extra = sorted(set(summaries) - used_tasks)
    if extra:
        raise ValueError(f"Japanese summary artifact contains unused Evidence records: {extra}")

    reader = dict(manifest.get("reader_facing_technical_notes") or {})
    reader.update({
        "language_policy": "ja-reader-summary-v1",
        "claim_limitation_sentence_structure": "Japanese by default; precision-critical technical terms may remain English",
        "attribution_labels_preserved": True,
        "source_evidence_unchanged": True,
        "summary_artifact_path": summary_path.relative_to(root).as_posix(),
        "summary_artifact_sha256": sha256_file(summary_path),
        "summary_replacement_count": total,
    })
    manifest["reader_facing_technical_notes"] = reader
    write_json(manifest_path, manifest)
    source["sha256"] = sha256_file(manifest_path)
    source["reader_facing_notes_language"] = "ja-reader-summary-v1"
    write_json(state_path, state)
    return {
        "status": "READER_NOTES_JA_APPLIED",
        "issue_id": issue_id,
        "source_manifest": manifest_path.relative_to(root).as_posix(),
        "source_manifest_sha256": source["sha256"],
        "summary_artifact": summary_path.relative_to(root).as_posix(),
        "summary_replacement_count": total,
    }


def raw_enum_findings(text: str) -> list[str]:
    return reader_taxonomy.reader_taxonomy_findings(text)


def check(root: Path, issue_id: str) -> dict[str, Any]:
    state = load_json(root / "sources" / issue_id / "pipeline-state.json")
    source = state.get("provenance", {}).get("validated_issue_source") or {}
    manifest_path = root / str(source.get("path") or "")
    if not manifest_path.is_file() or sha256_file(manifest_path) != source.get("sha256"):
        raise ValueError("state-pinned source manifest missing or SHA mismatch")
    manifest = load_json(manifest_path)
    reader = manifest.get("reader_facing_technical_notes") or {}
    errors: list[str] = []
    if reader.get("language_policy") != "ja-reader-summary-v1":
        errors.append("Technical Notes Japanese reader-summary policy is not recorded")
    summary_rel = str(reader.get("summary_artifact_path") or "")
    summary_path = root / summary_rel
    if not summary_rel or not summary_path.is_file():
        errors.append("Technical Notes Japanese summary artifact is missing")
    elif sha256_file(summary_path) != reader.get("summary_artifact_sha256"):
        errors.append("Technical Notes Japanese summary artifact SHA mismatch")

    labels = [re.escape(v) for v in expansion.CLASS_LABELS.values()]
    line_re = re.compile(r"\\item \\textbf\{(?:" + "|".join(labels) + r")\}:\s*(.+)")
    inspected = 0
    machine_enum_findings = 0
    for article in manifest.get("articles") or []:
        note_path = manifest_path.parent / str(article.get("technical_notes_path") or "")
        if not note_path.is_file():
            errors.append(f"Technical Notes missing: {article.get('package_id')}")
            continue
        text = note_path.read_text(encoding="utf-8")
        for line in text.splitlines():
            match = line_re.search(line)
            if not match:
                continue
            inspected += 1
            if not JP_RE.search(match.group(1)):
                errors.append(f"non-Japanese Technical Notes narrative: {article.get('package_id')}: {line[:120]}")
        findings = raw_enum_findings(text)
        if findings:
            machine_enum_findings += len(findings)
            errors.append(f"raw machine enum leaked in {article.get('package_id')}: {', '.join(findings)}")
    if inspected == 0:
        errors.append("no claim/limitation Technical Notes lines were inspected")
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "source_manifest": manifest_path.relative_to(root).as_posix(),
        "inspected_items": inspected,
        "machine_enum_findings": machine_enum_findings,
        "passed": not errors,
        "errors": errors,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="command", required=True)
    for name in ("prepare", "apply", "check"):
        p = sub.add_parser(name)
        p.add_argument("--repo-root", default=".")
        p.add_argument("--issue-id", required=True)
        if name == "apply":
            p.add_argument("--special-slug", required=True)
            p.add_argument("--summary", required=True)
        elif name == "prepare":
            p.add_argument("--output", required=True)
    args = ap.parse_args()
    root = Path(args.repo_root).resolve()
    if args.command == "prepare":
        report = prepare(root, args.issue_id, root / args.output)
    elif args.command == "apply":
        report = apply(root, args.issue_id, args.special_slug, root / args.summary)
    else:
        report = check(root, args.issue_id)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report.get("passed", True) else 1


if __name__ == "__main__":
    raise SystemExit(main())
