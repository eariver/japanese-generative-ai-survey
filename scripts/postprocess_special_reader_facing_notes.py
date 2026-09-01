#!/usr/bin/env python3
"""Compatibility entry point for reader-facing Special Technical Notes."""
from __future__ import annotations

import re

from scripts.postprocess_special_reader_facing_notes_core import *  # noqa: F401,F403
from scripts import postprocess_special_reader_facing_notes_core as core

_ORIGINAL_TRANSLATE = core.translate_machine_labels
_ORIGINAL_FINDINGS = core.reader_taxonomy_findings
_SUFFIX_LABELS = (
    ("_PRERELEASE", "（Pre-release）"),
    ("_PUBLICATION", "（公開）"),
    ("_ANNOUNCEMENT", "（発表）"),
    ("_RELEASE", "（公開）"),
    ("_PREVIEW", "（Preview）"),
    ("_UPDATE", "（更新）"),
    ("_UPGRADE", "（更新）"),
    ("_LAUNCH", "（公開）"),
    ("_GA", "（一般提供）"),
    ("_AVAILABILITY", "（提供開始）"),
    ("_HARDENING", "（強化）"),
    ("_EVALUATION", "（評価）"),
    ("_INTEGRATION", "（統合）"),
    ("_UPTAKE", "（対応）"),
    ("_DEPRECATION", "（非推奨化）"),
    ("_SHUTDOWN", "（停止）"),
)

_EXACT_EVENT_LABELS = {
    "AGENT_LAUNCH": "Agent（公開）",
    "SAFETY_METHOD_PUBLICATION": "安全手法（公開）",
    "MODEL_CARD_PUBLICATION": "Model Card（公開）",
    "PRODUCT_TOOLING_RELEASE": "製品ツール（公開）",
    "CODING_AGENT_UPDATE": "Coding Agent（更新）",
    "CODING_MODEL_RELEASE": "Codingモデル（公開）",
    "VIDEO_AUDIO_MODEL_RELEASE": "映像・音声モデル（公開）",
    "RUNTIME_RELEASE": "Runtime（公開）",
    "RUNTIME_STABLE_RELEASE": "Runtime安定版（公開）",
    "LIBRARY_RELEASE": "Library（公開）",
    "GPT_OSS_INTEGRATION_RELEASE": "gpt-oss（統合）",
    "MULTIMODAL_MODEL_UPTAKE_RELEASE": "マルチモーダルモデル（対応）",
    "CROSS_LAB_SAFETY_EVALUATION": "複数組織安全性評価",
    "ATLAS_SECURITY_HARDENING": "Atlasセキュリティ（強化）",
    "OPEN_WEIGHT_SAFETY_MODEL_RELEASE": "オープンウェイト安全モデル（公開）",
    "SAFETY_RESEARCH_RELEASE": "安全性研究（公開）",
    "INTERACTIONS_API_AND_DEEP_RESEARCH_PREVIEW": "Interactions API / Deep Research（Preview）",
}

_LEGACY_H2_LABELS = {
    "SAFETY METHOD（公開）": "安全手法（公開）",
    "モデル CARD（公開）": "Model Card（公開）",
    "CODING モデル公開": "Codingモデル（公開）",
    "VIDEO AUDIO モデル公開": "映像・音声モデル（公開）",
    "RUNTIME（公開）": "Runtime（公開）",
    "RUNTIME STABLE（公開）": "Runtime安定版（公開）",
    "LIBRARY（公開）": "Library（公開）",
    "GPT OSS INTEGRATION（公開）": "gpt-oss（統合）",
    "MULTIMODAL モデル UPTAKE（公開）": "マルチモーダルモデル（対応）",
    "OPEN WEIGHT SAFETY モデル公開": "オープンウェイト安全モデル（公開）",
    "OPEN_WEIGHT SAFETY モデル公開": "オープンウェイト安全モデル（公開）",
    "SAFETY 研究（公開）": "安全性研究（公開）",
    "REGIONAL_モデル_RELEASE": "地域別モデル公開",
    "INTERNATIONAL_モデル_RELEASE": "国際提供モデル公開",
    "オープンウェイト_モデル_RELEASE": "オープンウェイトモデル公開",
    "API_モデル_RELEASE": "APIモデル公開",
    "REGIONAL_モデル公開": "地域別モデル公開",
    "INTERNATIONAL_モデル公開": "国際提供モデル公開",
    "オープンウェイト_モデル公開": "オープンウェイトモデル公開",
    "API_モデル公開": "APIモデル公開",
}

_TOKEN_LABELS = {
    "CLAUDE": "Claude", "SONNET": "Sonnet", "HAIKU": "Haiku", "OPUS": "Opus",
    "GEMINI": "Gemini", "GEMINI3": "Gemini 3", "QWEN3": "Qwen3", "QWEN": "Qwen",
    "KIMI": "Kimi", "MINIMAX": "MiniMax", "HAILUO": "Hailuo", "MISTRAL": "Mistral",
    "DEVSTRAL": "Devstral", "VOXTRAL": "Voxtral", "CODESTRAL": "Codestral",
    "AUTOGLM": "AutoGLM", "GLM": "GLM", "SIMA": "SIMA", "GENIE": "Genie",
    "VEO3": "Veo 3", "IMAGEN4": "Imagen 4", "ROBOTICS": "Robotics", "ER": "ER",
    "GPT": "GPT", "OSS": "OSS", "API": "API", "AI": "AI", "MCP": "MCP",
    "OWL": "OWL", "ATLAS": "Atlas",
    "MODEL": "モデル", "PRODUCT": "製品", "AGENT": "Agent", "SAFETY": "安全性",
    "RESEARCH": "Research", "RUNTIME": "Runtime", "LIBRARY": "Library",
    "SYSTEM": "System", "CARD": "Card", "COMPUTER": "Computer", "USE": "Use",
    "BATCH": "Batch", "MODE": "Mode", "FLASH": "Flash", "LITE": "Lite",
    "IMAGE": "Image", "DEEP": "Deep", "INTERACTIONS": "Interactions", "TOOLING": "ツール",
    "ARCHITECTURE": "architecture", "SECURITY": "セキュリティ", "PHONE": "Phone",
    "MULTILINGUAL": "Multilingual", "NEXT": "Next", "MAX": "Max", "OMNI": "Omni",
    "THINKING": "Thinking", "STUDIO": "Studio", "EXP": "Exp", "TERMINUS": "Terminus",
    "CODING": "Coding", "CODER": "Coder", "PRO": "Pro", "AND": "/",
}

_MACHINE_SCHEMA_TOKENS = {
    "ANNOUNCEMENT", "EVALUATION", "HARDENING", "INTEGRATION", "METHOD", "MULTIMODAL",
    "SAFETY", "STABLE", "TOOLING", "UPTAKE", "VIDEO", "AUDIO", "CROSS", "LAB",
}

_CANONICAL_DISPLAY_REPLACEMENTS = {
    "Claude Sonnet 4 5": "Claude Sonnet 4.5",
    "Claude Haiku 4 5": "Claude Haiku 4.5",
    "Claude Opus 4 5": "Claude Opus 4.5",
    "Batch MODE": "Batch Mode",
    "VEO3 1": "Veo 3.1",
    "VEO3": "Veo 3",
    "Gemini 2.5 Flash LITE": "Gemini 2.5 Flash-Lite",
    "IMAGEN4": "Imagen 4",
    "Gemini 2.5 IMAGE": "Gemini 2.5 Image",
    "Robotics ER 1 5": "Robotics-ER 1.5",
    "COMPUTER USE": "Computer Use",
    "Gemini 3 PRO": "Gemini 3 Pro",
    "Gemini 3 FLASH": "Gemini 3 Flash",
    "Interactions API / Deep 研究": "Interactions API / Deep Research",
    "Qwen3 CODER": "Qwen3-Coder",
    "Qwen3 NEXT": "Qwen3-Next",
    "Qwen3 MAX": "Qwen3-Max",
    "Qwen3 OMNI": "Qwen3-Omni",
    "Qwen Image MAX": "Qwen Image Max",
    "Kimi K2 THINKING": "Kimi K2 Thinking",
    "DEVSTRAL": "Devstral",
    "VOXTRAL": "Voxtral",
    "Codestral 25 08": "Codestral 25.08",
    "Le Chat Deep 研究": "Le Chat Deep Research",
    "GLM 4 5": "GLM 4.5",
    "GLM 4 6": "GLM 4.6",
    "GLM 4 7": "GLM 4.7",
    "V3.1 Terminus API": "V3.1-Terminus API",
    "V3.2 Exp API": "V3.2-Exp API",
    "Minimax M2 1": "MiniMax M2.1",
    "Minimax M2": "MiniMax M2",
    "Hailuo 2 3": "Hailuo 2.3",
    "Owl ARCHITECTURE": "OWL architecture",
    "OWL ARCHITECTURE": "OWL architecture",
    "ATLAS": "Atlas",
}

_INTENTIONAL_UPPER_ACRONYMS = {
    "AI", "API", "ASR", "CLI", "CUDA", "ER", "GA", "GLM", "GPT", "HTTP",
    "JSON", "LLM", "MCP", "OWL", "RFT", "SDK", "SIMA", "SQL", "SWE", "URL",
}

_READER_LABELS = (
    set(core.EVENT_LABELS.values())
    | set(core.TYPE_LABELS.values())
    | set(_EXACT_EVENT_LABELS.values())
    | set(_LEGACY_H2_LABELS.values())
)


def _strip_generic_event_suffix(value: str) -> str:
    value = value.strip()
    if value.endswith("（技術イベント）"):
        value = value[: -len("（技術イベント）")].rstrip()
    return value


def _canonicalize_known_names(value: str) -> str:
    rendered = value
    for old, new in sorted(_CANONICAL_DISPLAY_REPLACEMENTS.items(), key=lambda item: len(item[0]), reverse=True):
        rendered = rendered.replace(old, new)
    return rendered


def _normalize_legacy_label(value: str) -> str:
    value = _strip_generic_event_suffix(value.replace(r"\_", "_").strip())
    if value in _LEGACY_H2_LABELS:
        return _LEGACY_H2_LABELS[value]
    value = value.replace("研究Preview", "RESEARCH_PREVIEW")
    value = value.replace("研究（公開）", "RESEARCH_RELEASE")
    value = value.replace("モデル公開", "MODEL_RELEASE")
    value = value.replace("モデル更新", "MODEL_UPDATE")
    if "_" not in value and re.search(r"\b[A-Z][A-Z0-9]*\b", value):
        candidate = re.sub(r"\s+", "_", value)
        if core._machine_taxonomy_label(candidate):
            value = candidate
    return value


def _humanize_subject(value: str) -> str:
    parts = [p for p in value.split("_") if p]
    rendered = [_TOKEN_LABELS.get(p, p.title() if p.isalpha() else p) for p in parts]
    text = " ".join(rendered).replace(" / ", " / ")
    text = re.sub(r"(?<=\d) (?=\d(?:V|$|\s))", ".", text)
    text = re.sub(r"\bGPT (\d(?:\.\d)?)\b", r"GPT-\1", text)
    return _canonicalize_known_names(text.strip())


def readable_taxonomy_label(value: str) -> str:
    original = _strip_generic_event_suffix(value.replace(r"\_", "_").strip())
    if "_" not in original:
        canonical = _canonicalize_known_names(original)
        if canonical != original:
            return canonical
    if original in _READER_LABELS:
        return original
    if original in _LEGACY_H2_LABELS:
        return _LEGACY_H2_LABELS[original]
    normalized = _normalize_legacy_label(original)
    if normalized in _READER_LABELS:
        return normalized
    if normalized in _EXACT_EVENT_LABELS:
        return _EXACT_EVENT_LABELS[normalized]
    if normalized in core.EVENT_LABELS:
        return core.EVENT_LABELS[normalized]
    if normalized in core.TYPE_LABELS:
        return core.TYPE_LABELS[normalized]
    if normalized == "PRODUCT":
        return "製品"
    if not core._machine_taxonomy_label(normalized):
        return _canonicalize_known_names(_LEGACY_H2_LABELS.get(normalized, normalized))
    for suffix, label in _SUFFIX_LABELS:
        if normalized.endswith(suffix):
            subject = _humanize_subject(normalized[: -len(suffix)])
            return f"{subject}{label}" if subject else label.strip('（）')
    return _humanize_subject(normalized) or "技術更新"


def translate_remaining_taxonomy(text: str) -> str:
    def event_replace(match: re.Match[str]) -> str:
        return f"{match.group(1)}{readable_taxonomy_label(match.group(2))}{match.group(3)}"

    text = re.sub(r"(\b\d{4}-\d{2}(?:-\d{2})?\s*\()([^)]+)(\))", event_replace, text)
    lines = text.splitlines()
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("種別 & "):
            prefix, rest = line.split("種別 & ", 1)
            value = rest.rsplit(r"\\", 1)[0] if r"\\" in rest else rest
            replacement = readable_taxonomy_label(value.strip())
            lines[index] = prefix + "種別 & " + replacement + r" \\"
            continue
        if " & " in stripped and re.search(r"\b\d{4}-\d{2}", stripped):
            trailer = r" \\" if stripped.endswith(r"\\") else ""
            body = line.rsplit(r"\\", 1)[0] if r"\\" in line else line
            parts = body.split(" & ")
            if len(parts) >= 4:
                parts[-2] = readable_taxonomy_label(parts[-2].strip())
                lines[index] = " & ".join(parts) + trailer
    return "\n".join(lines) + ("\n" if text.endswith("\n") else "")


def translate_machine_labels_compat(text: str) -> str:
    return translate_remaining_taxonomy(_ORIGINAL_TRANSLATE(translate_remaining_taxonomy(text)))


def _machine_word_findings(label: str) -> set[str]:
    findings = {token for token in re.findall(r"\b[A-Z][A-Z0-9]*\b", label) if token in _MACHINE_SCHEMA_TOKENS}
    for token in re.findall(r"\b[A-Z][A-Z0-9-]*\b", label):
        head = token.split("-", 1)[0]
        letters = "".join(ch for ch in head if ch.isalpha())
        if len(letters) < 3 or head in _INTENTIONAL_UPPER_ACRONYMS:
            continue
        findings.add(token)
    return findings


def reader_taxonomy_findings(text: str) -> list[str]:
    findings = set(_ORIGINAL_FINDINGS(text))
    normalized = text.replace(r"\_", "_")
    if "技術イベント" in normalized:
        findings.add("技術イベント")
    for value in core.CHRONOLOGY_EVENT_RE.findall(normalized):
        for token in _machine_word_findings(value):
            findings.add(f"{token} in chronology label")
    for line in normalized.splitlines():
        stripped = line.strip()
        if stripped.startswith("種別 & "):
            value = stripped[len("種別 & "):].rsplit(r"\\", 1)[0].strip()
            for token in _machine_word_findings(value):
                findings.add(f"{token} in type label")
    return sorted(findings)


core.translate_machine_labels = translate_machine_labels_compat
core.reader_taxonomy_findings = reader_taxonomy_findings


def main() -> int:
    return core.main()


if __name__ == "__main__":
    raise SystemExit(main())
