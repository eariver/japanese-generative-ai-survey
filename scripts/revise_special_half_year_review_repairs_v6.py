#!/usr/bin/env python3
"""Enrich Half-year Technical Notes with source-specific details from accepted Screening provenance.

The accepted SP Evidence cards can be intentionally conservative and may preserve only
chronology plus an attribution boundary. Reader-facing Technical Notes, however, must
not collapse to title/date-only bullets. This compatibility layer joins selected Evidence
to the hash-pinned accepted Screening verification queue by canonical source URL, extracts
bounded technical signals from the preserved source summary, and fails closed when it
cannot establish at least one source-specific technical point.

Optional per-issue editorial overrides may replace the deterministic signal extraction,
but they must preserve the exact selected Evidence URL set.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

from scripts import revise_special_half_year_review_repairs_v5 as compat

core = compat.core
_ORIGINAL_MERGE = core.merge_evidence_index
_ORIGINAL_FACT = core.source_specific_fact
_ORIGINAL_REPAIR_NOTE_FILE = core.repair_note_file

_ACTIVE_SOURCE_VERSION = ""
_ACTIVE_OVERRIDES: dict[str, dict[str, Any]] = {}

FACT_LINE_RE = re.compile(
    r"^\\item \\textbf\{一次情報で確認できる事実\}: .+$",
    re.MULTILINE,
)

_GENERIC_DETAIL_MARKERS = (
    "一次資料で確認できる公開・提供・機能・時系列上の事実を要約した項目",
    "提供元・プロジェクト・著者側の評価または説明として記録された項目",
    "一次資料で確認できる範囲の事実",
)

# Strong technical concepts. English tokens are intentionally retained where they are
# canonical engineering terms; the surrounding prose is Japanese.
_SIGNAL_PATTERNS: tuple[tuple[str, str], ...] = (
    ("decoder-only Transformer", r"\bdecoder[- ]only transformer\b"),
    ("Mixture-of-Experts (MoE)", r"\bmixture[- ]of[- ]experts\b|\bMoE\b"),
    ("SSM-Transformer", r"\bSSM[- ]Transformer\b"),
    ("Mamba", r"\bMamba\b"),
    ("vision encoder", r"\bvision encoder\b"),
    ("cross-attention", r"\bcross[- ]attention\b"),
    ("Grouped-Query Attention (GQA)", r"\bGrouped[- ]Query Attention\b|\bGQA\b"),
    ("FP8", r"\bFP8\b"),
    ("INT8", r"\bINT8\b"),
    ("4-bit quantization", r"\b4[- ]bit\b.{0,40}\bquant"),
    ("8-bit quantization", r"\b8[- ]bit\b.{0,40}\bquant"),
    ("Quantization-Aware Training (QAT)", r"\bQuantization[- ]Aware Training\b|\bQAT\b"),
    ("SpinQuant", r"\bSpinQuant\b"),
    ("LoRA", r"\bLoRA\b"),
    ("Direct Preference Optimization (DPO)", r"\bDirect Preference Optimization\b|\bDPO\b"),
    ("Supervised Fine-Tuning (SFT)", r"\bSupervised Fine[- ]Tuning\b|\bSFT\b"),
    ("Reinforcement Learning with Verifiable Rewards (RLVR)", r"\bReinforcement Learning with Verifiable Rewards\b|\bRLVR\b"),
    ("function calling", r"\bfunction calling\b"),
    ("tool use", r"\btool use\b"),
    ("JSON Schema", r"\bJSON Schemas?\b"),
    ("computer use / GUI操作", r"\bcomputer use\b"),
    ("MCP client/server", r"\bMCP clients?\b|\bMCP servers?\b"),
    ("SDK", r"\bSDKs?\b"),
    ("Retrieval-Augmented Generation (RAG)", r"\bRetrieval[- ]Augmented Generation\b|\bRAG\b"),
    ("BM25", r"\bBM25\b"),
    ("reranking", r"\brerank(?:ing|er)?\b"),
    ("prompt caching", r"\bprompt caching\b"),
    ("model distillation", r"\bmodel distillation\b|\bdistillation\b"),
    ("speculative decoding", r"\bspeculative decoding\b"),
    ("KV-cache", r"\bKV[- ]Cache\b|\bKV cache\b"),
    ("low-rank projection", r"\blow[- ]rank projection\b"),
    ("full-duplex speech", r"\bfull[- ]duplex\b"),
    ("real-time audio", r"\breal[- ]time\b.{0,40}\baudio\b|\baudio\b.{0,40}\breal[- ]time\b"),
    ("text-to-video", r"\btext[- ]to[- ]video\b"),
    ("image-to-video", r"\bimage[- ]to[- ]video\b"),
    ("video editing", r"\bvideo editing\b"),
    ("audio generation", r"\baudio generation\b"),
    ("image generation", r"\bimage generation\b"),
    ("multimodal input", r"\bmultimodal inputs?\b"),
    ("multimodal output", r"\bmultimodal outputs?\b"),
    ("diffusion Transformer", r"\bdiffusion transformers?\b|\bDiT\b"),
    ("autoregressive modeling", r"\bautoregress(?:ive|ion)\b"),
    ("rectified flow", r"\brectified flow\b"),
    ("state-based unit tests", r"\bstate[- ]based unit tests?\b"),
    ("information flow control", r"\binformation flow control\b"),
    ("alignment faking", r"\balignment faking\b"),
    ("scratchpad reasoning", r"\bscratchpad\b"),
    ("verifiable rewards", r"\bverifiable rewards?\b"),
    ("process-based verifier", r"\bprocess[- ]based verifier\b"),
    ("test-time compute", r"\btest[- ]time compute\b|\binference[- ]time computation\b"),
    ("compute-optimal scaling", r"\bcompute[- ]optimal\b"),
    ("fluidity-index", r"\bfluidity[- ]index\b"),
    ("TTFT/TBT/TPOT", r"\bTTFT\b|\bTBT\b|\bTPOT\b"),
    ("content moderation classifier", r"\bmoderation\b.{0,50}\bclassifier\b|\bclassifier\b.{0,50}\bmoderation\b"),
    ("web search", r"\bweb search\b|\bsearch features?\b"),
    ("factuality evaluation", r"\bfactuality\b|\bfactual(?:ly)? correct\b"),
    ("OCR", r"\bOCR\b"),
    ("pointing", r"\bpointing\b"),
    ("PixMo", r"\bPixMo\b"),
    ("SynthID", r"\bSynthID\b"),
    ("Apache 2.0", r"\bApache 2\.0\b"),
    ("Mistral Research License", r"\bMistral Research License\b"),
    ("Llama Community License", r"\bLlama .*? Community License\b"),
    ("open weights", r"\bopen[- ]weights?\b"),
    ("public beta", r"\bpublic beta\b"),
    ("experimental release", r"\bexperimental\b"),
    ("small model / cost-efficient deployment", r"\bsmall model\b|\bcost[- ]efficient\b"),
    ("text and vision", r"\btext and vision\b|\bvision and text\b"),
    ("advanced mathematical reasoning benchmark", r"\badvanced mathematical reasoning\b"),
    ("formal / automated reasoning", r"\bautomated reasoning\b|\bformal logic\b"),
)

_DYNAMIC_PATTERNS: tuple[tuple[str, str], ...] = (
    ("{0}B parameter scale", r"\b(\d+(?:\.\d+)?)B(?:\s+parameters?)?\b"),
    ("{0}K context", r"\b(\d+(?:\.\d+)?)K\b(?=[^.!?\n]{0,45}\bcontext\b)|\bcontext(?: window| length)?[^.!?\n]{0,25}\b(\d+(?:\.\d+)?)K\b"),
    ("{0}M context", r"\b(\d+(?:\.\d+)?)M\b(?=[^.!?\n]{0,45}\bcontext\b)|\bcontext(?: window| length)?[^.!?\n]{0,25}\b(\d+(?:\.\d+)?)M\b"),
    ("{0}T training tokens", r"\b(\d+(?:\.\d+)?)T\b(?=[^.!?\n]{0,30}\btokens?\b)"),
    ("{0} APIs", r"\b(\d{1,4})\s+APIs\b"),
    ("{0} apps", r"\b(\d{1,4})\s+(?:day-to-day\s+)?apps\b"),
    ("{0} agent tasks", r"\b(\d{1,4})\s+[^.!?\n]{0,45}\bagent tasks\b"),
    ("{0} content categories", r"\b(\d{1,3})\s+categories\b"),
    ("{0}s generation", r"\b(\d+(?:\.\d+)?)\s+seconds?\b"),
    ("{0} fps", r"\b(\d+(?:\.\d+)?)\s+frames per second\b"),
)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _normalize_url(url: str) -> str:
    parts = urlsplit(url.strip())
    host = parts.netloc.lower()
    path = parts.path.rstrip("/") or "/"
    # Scheme is not part of identity for the historical arXiv collector split; everything
    # else, including path case and filename bytes, remains exact.
    return urlunsplit(("", host, path, parts.query, ""))


def _load_json(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{path}: expected JSON object")
    return data


def _accepted_screening_queue(repo_root: Path, issue_id: str) -> Path:
    evidence_root = repo_root / "sources" / issue_id / "evidence" / "runs"
    candidates: list[Path] = []
    diagnostics: list[str] = []
    for acceptance_path in sorted(evidence_root.glob("*/acceptance.json")):
        acceptance = _load_json(acceptance_path)
        if acceptance.get("status") != "ACCEPTED":
            continue
        package = acceptance.get("evidence_package") or {}
        result_set = str(package.get("screening_result_set_sha256") or "").strip()
        expected_queue_sha = str(package.get("verification_queue_sha256") or "").strip()
        if not result_set or not expected_queue_sha:
            diagnostics.append(f"{acceptance_path}: missing screening provenance")
            continue
        queue_path = (
            repo_root
            / "sources"
            / issue_id
            / "screening"
            / "runs"
            / result_set
            / "verification-queue.jsonl"
        )
        if not queue_path.is_file():
            diagnostics.append(f"{acceptance_path}: queue missing: {queue_path}")
            continue
        actual = _sha256(queue_path)
        if actual != expected_queue_sha:
            raise ValueError(
                f"Screening queue digest mismatch for {acceptance_path}: "
                f"actual={actual} expected={expected_queue_sha}"
            )
        candidates.append(queue_path)
    unique = sorted({path.resolve() for path in candidates})
    if len(unique) != 1:
        raise ValueError(
            "Half-year Technical Notes require exactly one accepted hash-pinned Screening queue; "
            f"found={len(unique)} diagnostics={diagnostics}"
        )
    return unique[0]


def _screening_index(repo_root: Path, issue_id: str) -> tuple[dict[str, dict[str, Any]], Path]:
    queue_path = _accepted_screening_queue(repo_root, issue_id)
    by_url: dict[str, dict[str, Any]] = {}
    for line_no, raw in enumerate(queue_path.read_text(encoding="utf-8").splitlines(), start=1):
        if not raw.strip():
            continue
        row = json.loads(raw)
        record = row.get("record") or {}
        locator = str(record.get("locator") or "").strip()
        title = str(record.get("title") or "").strip()
        screening = row.get("screening") or record.get("screening") or {}
        if screening.get("decision") != "KEEP":
            continue
        normalized = _normalize_url(locator) if locator else ""
        payload = {
            "screening_id": str(row.get("screening_id") or record.get("screening_id") or ""),
            "title": title,
            "locator": locator,
            "summary_text": str(record.get("summary_text") or "").strip(),
            "published_at": str(record.get("published_at") or "").strip(),
            "verification_targets": list(screening.get("verification_targets") or []),
            "reason": str(screening.get("reason") or "").strip(),
            "line_no": line_no,
        }
        if normalized:
            existing = by_url.get(normalized)
            if existing is not None and existing["screening_id"] != payload["screening_id"]:
                raise ValueError(f"ambiguous Screening locator after normalization: {locator}")
            by_url[normalized] = payload
    return by_url, queue_path


def _event_window(summary: str, events: list[tuple[str, str]]) -> str:
    if not summary:
        return ""
    lower = summary.lower()
    for date, _kind in events:
        try:
            dt = datetime.strptime(str(date)[:10], "%Y-%m-%d")
        except ValueError:
            continue
        day = dt.day
        suffix = "th"
        if day % 10 == 1 and day != 11:
            suffix = "st"
        elif day % 10 == 2 and day != 12:
            suffix = "nd"
        elif day % 10 == 3 and day != 13:
            suffix = "rd"
        variants = (
            dt.strftime("%Y-%m-%d"),
            dt.strftime("%B %d, %Y").replace(" 0", " "),
            dt.strftime("%b %d, %Y").replace(" 0", " "),
            f"{dt.strftime('%B')} {day}{suffix}, {dt.year}",
            f"{dt.strftime('%B')} {day}th, {dt.year}",
            f"{day} {dt.strftime('%B')} {dt.year}",
        )
        for variant in variants:
            pos = lower.find(variant.lower())
            if pos >= 0:
                return summary[max(0, pos - 700) : min(len(summary), pos + 3000)]
    # Papers/official articles generally begin with the relevant abstract/announcement. Limiting
    # the window also prevents later living-page updates from being back-projected.
    return summary[:8000]


def _dynamic_signals(text: str) -> list[str]:
    out: list[str] = []
    for template, pattern in _DYNAMIC_PATTERNS:
        for match in re.finditer(pattern, text, flags=re.IGNORECASE):
            value = next((group for group in match.groups() if group), "")
            if not value:
                continue
            rendered = template.format(value)
            if rendered not in out:
                out.append(rendered)
            if len(out) >= 4:
                return out
    return out


def _technical_signals(summary: str, events: list[tuple[str, str]]) -> list[str]:
    window = _event_window(summary, events)
    if not window:
        return []
    signals: list[str] = []
    # Dynamic quantities first because they make otherwise generic release cards concrete.
    for signal in _dynamic_signals(window):
        if signal not in signals:
            signals.append(signal)
    for display, pattern in _SIGNAL_PATTERNS:
        if re.search(pattern, window, flags=re.IGNORECASE | re.DOTALL) and display not in signals:
            signals.append(display)
        if len(signals) >= 7:
            break
    return signals[:7]


def _validate_override(title: str, override: dict[str, Any], info: dict[str, Any]) -> list[str]:
    expected_urls = sorted(str(url) for url in (info.get("urls") or []))
    actual_urls = sorted(str(url) for url in (override.get("source_urls") or []))
    if actual_urls != expected_urls:
        raise ValueError(
            f"Technical Notes detail override URL mismatch for {title}: "
            f"actual={actual_urls} expected={expected_urls}"
        )
    points = [str(point).strip() for point in (override.get("technical_points") or []) if str(point).strip()]
    if not points:
        raise ValueError(f"Technical Notes detail override has no technical_points: {title}")
    for point in points:
        if any(marker in point for marker in _GENERIC_DETAIL_MARKERS):
            raise ValueError(f"Technical Notes detail override is generic for {title}: {point}")
    return points


def merge_evidence_index(repo_root: Path, manifest: dict[str, Any]) -> dict[str, dict[str, Any]]:
    index = _ORIGINAL_MERGE(repo_root, manifest)
    issue_id = str(manifest.get("issue_id") or "").strip()
    if not issue_id:
        raise ValueError("source manifest missing issue_id")
    screening_by_url, queue_path = _screening_index(repo_root, issue_id)
    queue_sha = _sha256(queue_path)
    for override_title, override in _ACTIVE_OVERRIDES.items():
        expected_queue_sha = str(override.get("_expected_queue_sha256") or "").strip()
        if expected_queue_sha != queue_sha:
            raise ValueError(
                f"Technical Notes detail override Screening digest mismatch for {override_title}: "
                f"actual={queue_sha} expected={expected_queue_sha}"
            )

    seen: set[int] = set()
    for title, info in list(index.items()):
        identity = id(info)
        if identity in seen:
            continue
        seen.add(identity)
        canonical_title = str(info.get("canonical_title") or title)
        records: list[dict[str, Any]] = []
        for url in info.get("urls") or []:
            record = screening_by_url.get(_normalize_url(str(url)))
            if record is not None and record not in records:
                records.append(record)
        if not records:
            raise ValueError(
                f"Selected Evidence has no matching accepted Screening provenance for Technical Notes: "
                f"{canonical_title} urls={info.get('urls')}"
            )
        info["screening_records"] = records
        info["screening_queue_path"] = queue_path.relative_to(repo_root).as_posix()
        info["screening_queue_sha256"] = queue_sha

        override = _ACTIVE_OVERRIDES.get(canonical_title)
        if override is not None:
            points = _validate_override(canonical_title, override, info)
            info["technical_points"] = points
            info["technical_point_mode"] = "EDITORIAL_OVERRIDE"
            continue

        signals: list[str] = []
        for record in records:
            for signal in _technical_signals(str(record.get("summary_text") or ""), list(info.get("events") or [])):
                if signal not in signals:
                    signals.append(signal)
                if len(signals) >= 7:
                    break
            if len(signals) >= 7:
                break
        if not signals:
            raise ValueError(
                f"Accepted Screening provenance is too thin for reader-facing Technical Notes: {canonical_title}. "
                "Provide a hash-bound editorial technical-point override instead of emitting a fallback."
            )
        info["technical_points"] = [
            "一次資料の技術範囲として " + " / ".join(signals) + " を確認できる。"
        ]
        info["technical_point_mode"] = "SCREENING_SIGNAL_EXTRACTION"
    return index


def source_specific_fact(title: str, info: dict[str, Any]) -> str:
    canonical_title = str(info.get("canonical_title") or title)
    chronology = _ORIGINAL_FACT(canonical_title, info)
    points = [str(point).strip() for point in (info.get("technical_points") or []) if str(point).strip()]
    if not points:
        raise ValueError(f"source-specific technical points missing: {canonical_title}")
    return chronology + " " + " ".join(points)


def _enrich_fact_line(block: str, title: str, info: dict[str, Any]) -> tuple[str, int]:
    lines = block.splitlines()
    replacements = 0
    for i, line in enumerate(lines):
        if not line.startswith(r"\item \textbf{一次情報で確認できる事実}: "):
            continue
        if "一次資料の技術範囲として" in line:
            continue
        lines[i] = (
            r"\item \textbf{一次情報で確認できる事実}: "
            + core.tex_escape(source_specific_fact(title, info))
        )
        replacements += 1
    if replacements != 1:
        raise ValueError(
            f"Technical Notes must contain exactly one enrichable primary-fact bullet for {title}; "
            f"replacements={replacements}"
        )
    return "\n".join(lines), replacements


def repair_note_file(path: Path, evidence: dict[str, dict[str, Any]]) -> tuple[int, int, int]:
    # Retain all v5 protections: URL restoration, identifier-safe localization, generic-fallback
    # rejection, repeated-boundary removal, taxonomy validation, and exact URL identity.
    base_counts = _ORIGINAL_REPAIR_NOTE_FILE(path, evidence)

    original = path.read_text(encoding="utf-8")
    matches = list(core.NOTE_RE.finditer(original))
    changes: list[tuple[int, int, str]] = []
    enriched = 0
    for match in matches:
        block = match.group(0)
        title = match.group(1)
        info = evidence.get(title)
        if info is None:
            raise ValueError(f"Technical Notes title not bound to selected Evidence: {title}")
        revised, count = _enrich_fact_line(block, title, info)
        enriched += count
        if revised != block:
            changes.append((match.start(), match.end(), revised))
    text = original
    for start, end, revised in reversed(changes):
        text = text[:start] + revised + text[end:]

    if enriched != len(matches):
        raise ValueError(
            f"{path.name}: not every Technical Notes card received a source-specific technical point: "
            f"enriched={enriched} cards={len(matches)}"
        )
    for marker in _GENERIC_DETAIL_MARKERS:
        if marker in text:
            raise ValueError(f"{path.name}: generic Technical Notes detail remains: {marker}")
    if text != original:
        path.write_text(text, encoding="utf-8")
    # Keep the historical tuple contract; enriched facts replace the old fact-replacement count.
    return enriched, base_counts[1], base_counts[2]


def _load_overrides(repo_root: Path, issue_id: str, source_version: str) -> dict[str, dict[str, Any]]:
    marker_path = repo_root / "sources" / issue_id / "editorial" / f"layout-revision-{source_version}.json"
    marker = _load_json(marker_path)
    changes = marker.get("layout_changes") or {}
    rel = str(changes.get("technical_note_detail_overrides_path") or "").strip()
    if not rel:
        return {}
    path = repo_root / rel
    payload = _load_json(path)
    if str(payload.get("issue_id") or "") != issue_id:
        raise ValueError(f"Technical Notes detail override issue mismatch: {path}")
    expected_queue_sha = str(payload.get("screening_verification_queue_sha256") or "").strip()
    entries = payload.get("entries") or {}
    if not isinstance(entries, dict):
        raise ValueError(f"{path}: entries must be an object")
    # The exact queue digest is rechecked again in merge_evidence_index. Requiring it here makes the
    # synthesis artifact explicitly hash-bound to its upstream Screening provenance.
    if not expected_queue_sha:
        raise ValueError(f"{path}: screening_verification_queue_sha256 is required")
    result: dict[str, dict[str, Any]] = {}
    for title, entry in entries.items():
        if not isinstance(entry, dict):
            raise ValueError(f"{path}: override entry must be an object: {title}")
        result[str(title)] = dict(entry)
        result[str(title)]["_expected_queue_sha256"] = expected_queue_sha
    return result


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    global _ACTIVE_SOURCE_VERSION, _ACTIVE_OVERRIDES
    _ACTIVE_SOURCE_VERSION = source_version
    _ACTIVE_OVERRIDES = _load_overrides(repo_root, issue_id, source_version)
    try:
        result = compat.build(repo_root, special_slug, issue_id, source_version)
        if isinstance(result, dict):
            result["technical_note_detail_overrides"] = len(_ACTIVE_OVERRIDES)
            result["technical_note_detail_contract"] = "SCREENING_BACKED_FAIL_CLOSED"
        return result
    finally:
        _ACTIVE_SOURCE_VERSION = ""
        _ACTIVE_OVERRIDES = {}


# v3 resolves these helpers from its module globals at runtime.
core.merge_evidence_index = merge_evidence_index
core.source_specific_fact = source_specific_fact
core.repair_note_file = repair_note_file


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
