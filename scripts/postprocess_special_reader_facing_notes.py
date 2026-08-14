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
    ("_RELEASE", "公開"),
    ("_PREVIEW", "Preview"),
    ("_UPDATE", "更新"),
    ("_UPGRADE", "更新"),
    ("_LAUNCH", "公開"),
    ("_GA", "一般提供"),
)


def readable_taxonomy_label(value: str) -> str:
    normalized = value.replace(r"\_", "_").strip()
    if not core._machine_taxonomy_label(normalized):
        return value
    if normalized == "PRODUCT":
        return "製品"
    for suffix, label in _SUFFIX_LABELS:
        if normalized.endswith(suffix):
            base = normalized[: -len(suffix)].replace("_", " ").strip()
            return f"{base}（{label}）" if base else label
    base = normalized.replace("_", " ").strip()
    return f"{base}（技術イベント）"


def translate_remaining_taxonomy(text: str) -> str:
    def event_replace(match: re.Match[str]) -> str:
        return f"{match.group(1)}{readable_taxonomy_label(match.group(2))}{match.group(3)}"

    text = re.sub(r"(\b\d{4}-\d{2}(?:-\d{2})?\s*\()([^)]+)(\))", event_replace, text)
    lines = text.splitlines()
    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("種別 & "):
            prefix, rest = line.split("種別 & ", 1)
            value, suffix = (rest.rsplit(r"\\", 1) + [""])[:2] if r"\\" in rest else (rest, "")
            replacement = readable_taxonomy_label(value.strip())
            lines[index] = prefix + "種別 & " + replacement + (r" \\" if suffix != "" else "")
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


def main() -> int:
    core.translate_machine_labels = translate_machine_labels_compat
    return core.main()


if __name__ == "__main__":
    raise SystemExit(main())
