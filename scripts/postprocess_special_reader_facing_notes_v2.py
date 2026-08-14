#!/usr/bin/env python3
"""Reader-facing Special Technical Notes entry point with safe taxonomy localization.

Reader-facing taxonomy translation is deliberately limited so canonical URL/URI/path/code
identifiers survive byte-for-byte. Compatibility fixes that must be applied before importing
the legacy wrapper live here so translation and leak detection share the same vocabulary.
"""
from __future__ import annotations

import re

from scripts import postprocess_special_reader_facing_notes_core as core

# BENCHMARK is a valid Evidence artifact type used by retrospective issues.
core.TYPE_LABELS.setdefault("BENCHMARK", "評価ベンチマーク")

# Source-semantic overrides: safety-related material is not automatically an incident/event.
core.TYPE_OVERRIDES.update(
    {
        "Automated Reasoning checks for Amazon Bedrock Guardrails": "安全性手法",
        "Deliberative alignment: reasoning enables safer language models": "Alignment研究",
        "Alignment faking in large language models": "Alignment研究",
    }
)

_BASE_TRANSLATE = core.translate_machine_labels
_OPAQUE_MACRO_RE = re.compile(r"\\(?:url|nolinkurl|path|texttt)\{[^{}]*\}|\\href\{[^{}]*\}")
_RAW_URL_RE = re.compile(r"https?://[^\s{}]+")


def _protect_opaque_identifiers(text: str) -> tuple[str, list[str]]:
    """Protect URL/path/code identifier spans from broad legacy token replacement."""
    values: list[str] = []

    def protect(match: re.Match[str]) -> str:
        token = f"@@JGOPAQUE{len(values)}@@"
        values.append(match.group(0))
        return token

    # Protect complete TeX identifier macros first, then any remaining raw URLs.
    rendered = _OPAQUE_MACRO_RE.sub(protect, text)
    rendered = _RAW_URL_RE.sub(protect, rendered)
    return rendered, values


def _restore_opaque_identifiers(text: str, values: list[str]) -> str:
    rendered = text
    for index, value in enumerate(values):
        token = f"@@JGOPAQUE{index}@@"
        if token not in rendered:
            raise ValueError(f"reader-facing opaque identifier placeholder disappeared: {token}")
        rendered = rendered.replace(token, value)
    if "@@JGOPAQUE" in rendered:
        raise ValueError("reader-facing opaque identifier placeholder remains after restoration")
    return rendered


def translate_machine_labels_preserving_identifiers(text: str) -> str:
    protected, values = _protect_opaque_identifiers(text)
    translated = _BASE_TRANSLATE(protected)
    return _restore_opaque_identifiers(translated, values)


# The legacy compatibility wrapper captures core.translate_machine_labels at import time.
# Bind the identifier-safe translator first so all later compatibility translation inherits it.
core.translate_machine_labels = translate_machine_labels_preserving_identifiers

from scripts import postprocess_special_reader_facing_notes as compat  # noqa: E402

translate_machine_labels = compat.translate_machine_labels
translate_machine_labels_compat = compat.translate_machine_labels_compat
reader_taxonomy_findings = compat.reader_taxonomy_findings
readable_taxonomy_label = compat.readable_taxonomy_label


def main() -> int:
    return compat.main()


if __name__ == "__main__":
    raise SystemExit(main())
