#!/usr/bin/env python3
"""Compatibility entry point for reader-facing Special Technical Notes."""
from __future__ import annotations

import re

from scripts.postprocess_special_reader_facing_notes_core import *  # noqa: F401,F403
from scripts import postprocess_special_reader_facing_notes_core as core

_ORIGINAL_TRANSLATE = core.translate_machine_labels
_SUFFIX_LABELS = (
    ("_PRERELEASE", "Pre-release"),
    ("_PUBLICATION", "公開"),
    ("_ANNOUNCEMENT", "発表"),
    ("_RELEASE", "公開"),
    ("_PREVIEW", "Preview"),
    ("_UPDATE", "更新"),
    ("_UPGRADE", "更新"),
    ("_LAUNCH", "公開"),
    ("_GA", "一般提供"),
    ("_AVAILABILITY", "提供開始"),
    ("_HARDENING", "強化"),
    ("_EVALUATION", "評価"),
    ("_INTEGRATION", "統合"),
    ("_UPTAKE", "対応"),
    ("_DEPRECATION", "非推奨化"),
    ("_SHUTDOWN", "停止"),
)

_EXACT_EVENT_LABELS = {
    "AGENT_LAUNCH": "Agent公開",
    "SAFETY_METHOD_PUBLICATION": "安全手法公開",
    "MODEL_CARD_PUBLICATION": "Model Card公開",
    "PRODUCT_TOOLING_RELEASE": "製品ツール公開",
    "CODING_AGENT_UPDATE": "Coding Agent更新",
    "CODING_MODEL_RELEASE": "Codingモデル公開",
    "VIDEO_AUDIO_MODEL_RELEASE": "映像・音声モデル公開",
    "RUNTIME_RELEASE": "Runtime公開",
    "RUNTIME_STABLE_RELEASE": "Runtime安定版公開",
    "LIBRARY_RELEASE": "Library公開",
    "GPT_OSS_INTEGRATION_RELEASE": "gpt-oss統合",
    "MULTIMODAL_MODEL_UPTAKE_RELEASE": "マルチモーダルモデル対応",
    "CROSS_LAB_SAFETY_EVALUATION": "複数組織安全性評価",
    "ATLAS_SECURITY_HARDENING": "Atlasセキュリティ強化",
    "OPEN_WEIGHT_SAFETY_MODEL_RELEASE": "オープンウェイト安全モデル公開",
    "SAFETY_RESEARCH_RELEASE": "安全性研究公開",
    "INTERACTIONS_API_AND_DEEP_RESEARCH_PREVIEW": "Interactions API / Deep Research Preview",
}

_TOKEN_LABELS = {
    "CLAUDE": "Claude", "SONNET": "Sonnet", "HAIKU": "Haiku", "OPUS": "Opus",
    "GEMINI": "Gemini", "GEMINI3": "Gemini 3", "QWEN3": "Qwen3", "QWEN": "Qwen",
    "KIMI": "Kimi", "MINIMAX": "MiniMax", "HAILUO": "Hailuo", "MISTRAL": "Mistral",
    "DEVSTRAL": "Devstral", "VOXTRAL": "Voxtral", "CODESTRAL": "Codestral",
    "AUTOGLM": "AutoGLM", "GLM": "GLM", "SIMA": "SIMA", "GENIE": "Genie",
    "VEO3": "Veo 3", "IMAGEN4": "Imagen 4", "ROBOTICS": "Robotics", "ER": "ER",
    "GPT": "GPT", "OSS": "oss", "API": "API", "AI": "AI", "MCP": "MCP",
    "MODEL": "モデル", "PRODUCT": "製品", "AGENT": "Agent", "SAFETY": "安全性",
    "RESEARCH": "Research", "RUNTIME": "Runtime", "LIBRARY": "Library",
    "SYSTEM": "System", "CARD": "Card", "COMPUTER": "Computer", "USE": "Use",
    "BATCH": "Batch", "MODE": "Mode", "FLASH": "Flash", "LITE": "Lite",
    "IMAGE": "Image", "DEEP": "Deep", "INTERACTIONS": "Interactions", "TOOLING": "ツール",
    "ARCHITECTURE": "アーキテクチャ", "SECURITY": "セキュリティ", "PHONE": "Phone",
    "MULTILINGUAL": "Multilingual", "NEXT": "Next", "MAX": "Max", "OMNI": "Omni",
    "THINKING": "Thinking", "STUDIO": "Studio", "EXP": "Exp", "TERMINUS": "Terminus",
}


def _humanize_subject(value: str) -> str:
    parts = [p for p in value.split("_") if p]
    rendered = [_TOKEN_LABELS.get(p, p.title() if p.isalpha() else p) for p in parts]
    text = " ".join(rendered)
    text = re.sub(r"(?<=\d) (?=\d(?:V|$|\s))", ".", text)
    text = re.sub(r"\bGPT (\d(?:\.\d)?)\b", r"GPT-\1", text)
    text = re.sub(r"\bV(\d)\.(\d)\b", r"V\1.\2", text)
    text = text.replace("Veo 3.1", "Veo 3.1")
    return text.strip()


def readable_taxonomy_label(value: str) -> str:
    normalized = value.replace(r"\_", "_").strip()
    if normalized in _EXACT_EVENT_LABELS:
        return _EXACT_EVENT_LABELS[normalized]
    if normalized in core.EVENT_LABELS:
        return core.EVENT_LABELS[normalized]
    if normalized in core.TYPE_LABELS:
        return core.TYPE_LABELS[normalized]
    if normalized == "PRODUCT":
        return "製品"
    if not core._machine_taxonomy_label(normalized):
        return value
    for suffix, label in _SUFFIX_LABELS:
        if normalized.endswith(suffix):
            subject = _humanize_subject(normalized[: -len(suffix)])
            return f"{subject}{label}" if subject else label
    # Unknown schema values must not degrade to the old generic 技術イベント label.
    # Preserve a readable subject and make the uncertainty explicit without leaking enum syntax.
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
    return translate_remaining_taxonomy(_ORIGINAL_TRANSLATE(text))


_UPPERCASE_WITH_JA_SUFFIX = re.compile(r"\b[A-Z][A-Z0-9]*(?:[ _][A-Z0-9]+)+(?=（|公開|更新|発表|Preview|一般提供|提供開始|強化|評価|統合|対応|非推奨化|停止)")


def reader_taxonomy_findings(text: str) -> list[str]:
    findings = set(core.reader_taxonomy_findings(text))
    normalized = text.replace(r"\_", "_")
    if "技術イベント" in normalized:
        findings.add("技術イベント")
    for match in _UPPERCASE_WITH_JA_SUFFIX.finditer(normalized):
        findings.add(match.group(0))
    return sorted(findings)


# Patch at import time because other repair/check scripts import this compatibility
# module and call core.transform_note directly rather than invoking this module's CLI.
core.translate_machine_labels = translate_machine_labels_compat
core.reader_taxonomy_findings = reader_taxonomy_findings


def main() -> int:
    return core.main()


if __name__ == "__main__":
    raise SystemExit(main())
