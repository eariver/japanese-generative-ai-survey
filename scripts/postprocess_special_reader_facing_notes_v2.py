#!/usr/bin/env python3
"""Reader-facing Special Technical Notes entry point with safe taxonomy localization.

Reader-facing taxonomy translation is deliberately limited so canonical URL/URI/path/code
identifiers survive byte-for-byte. Compatibility fixes that must be applied before importing
the legacy wrapper live here so translation and leak detection share the same vocabulary.
"""
from __future__ import annotations

import hashlib
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


def _opaque_prefix(text: str) -> str:
    """Return a deterministic namespace that does not already occur in *text*."""
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]
    prefix = f"@@JGOPAQUE-{digest}-"
    while prefix in text:
        prefix += "X"
    return prefix


def _protect_opaque_identifiers(text: str) -> tuple[str, list[tuple[str, str]]]:
    """Protect URL/path/code identifier spans from broad legacy token replacement.

    Each call receives its own token namespace. This makes protection composable: an
    outer compatibility wrapper may leave its placeholders in the text while an inner
    translator independently protects/restores its own spans.
    """
    replacements: list[tuple[str, str]] = []
    prefix = _opaque_prefix(text)

    def protect(match: re.Match[str]) -> str:
        token = f"{prefix}{len(replacements)}@@"
        replacements.append((token, match.group(0)))
        return token

    # Protect complete TeX identifier macros first, then any remaining raw URLs.
    rendered = _OPAQUE_MACRO_RE.sub(protect, text)
    rendered = _RAW_URL_RE.sub(protect, rendered)
    return rendered, replacements


def _restore_opaque_identifiers(text: str, replacements: list[tuple[str, str]]) -> str:
    """Restore exactly this call's placeholders and ignore namespaces owned by callers."""
    rendered = text
    for token, value in replacements:
        count = rendered.count(token)
        if count != 1:
            raise ValueError(
                f"reader-facing opaque identifier placeholder occurrence mismatch: {token} count={count}"
            )
        rendered = rendered.replace(token, value, 1)
    for token, _ in replacements:
        if token in rendered:
            raise ValueError(f"reader-facing opaque identifier placeholder remains after restoration: {token}")
    return rendered


def translate_machine_labels_preserving_identifiers(text: str) -> str:
    protected, replacements = _protect_opaque_identifiers(text)
    translated = _BASE_TRANSLATE(protected)
    return _restore_opaque_identifiers(translated, replacements)


# The legacy compatibility wrapper captures core.translate_machine_labels at import time.
# Bind the identifier-safe translator first so all later compatibility translation inherits it.
core.translate_machine_labels = translate_machine_labels_preserving_identifiers

from scripts import postprocess_special_reader_facing_notes as compat  # noqa: E402

_COMPAT_TRANSLATE = compat.translate_machine_labels_compat


def translate_machine_labels_compat(text: str) -> str:
    # Protect identifiers around the entire compatibility translation as well.
    # This remains safe even when the legacy compatibility module was imported earlier
    # in the same Python process and had already captured the historical broad translator.
    protected, replacements = _protect_opaque_identifiers(text)
    translated = _COMPAT_TRANSLATE(protected)
    return _restore_opaque_identifiers(translated, replacements)


translate_machine_labels = translate_machine_labels_compat
reader_taxonomy_findings = compat.reader_taxonomy_findings
readable_taxonomy_label = compat.readable_taxonomy_label
core.translate_machine_labels = translate_machine_labels_compat


def main() -> int:
    return compat.main()


if __name__ == "__main__":
    raise SystemExit(main())
