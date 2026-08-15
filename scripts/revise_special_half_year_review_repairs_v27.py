#!/usr/bin/env python3
"""Enforce component/variant/property binding for Half-year Technical Notes.

V26 binds high-risk values to a version-aware selected artifact, but two finer attribution
boundaries remain:

* a family announcement may contain variants with different licenses/properties; a bare
  ``A / B / C / Apache 2.0`` list loses variant -> property ownership;
* one announcement may describe a model plus an adjacent Stack/API/runtime component;
  deployment capabilities owned by that component must not become model attributes.

V27 therefore expands the fail-closed audit to scope-sensitive properties and rejects an
automatically rendered property when ownership is heterogeneous, exception-qualified, or
split across a closer component subject. Hash-bound editorial overrides remain the recovery
path for explicit subject-labelled statements.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v24 as v24
from scripts import revise_special_half_year_review_repairs_v25 as v25
from scripts import revise_special_half_year_review_repairs_v26 as v26

impl = v25.impl
event_layer = v25.event_layer

_ENTITY_BINDING_CONTRACT = "SUBJECT_COMPONENT_VARIANT_PROPERTY_BINDING_V3"

_LICENSE_SIGNALS = {
    "Apache 2.0",
    "Mistral Research License",
    "Llama Community License",
}
_COMPONENT_SCOPED_SIGNALS = {
    "Retrieval-Augmented Generation (RAG)",
    "function calling",
    "tool use",
    "SDK",
    "MCP client/server",
}
_SCOPE_SENSITIVE_STATIC_SIGNALS = _LICENSE_SIGNALS | _COMPONENT_SCOPED_SIGNALS | {
    "open weights",
}

# Adjacent implementation surfaces are real subjects even without a version number. V26
# deliberately ignored most two-word capitalised spans to avoid prose false positives; V27
# allows only explicit engineering-component nouns through that boundary.
_COMPONENT_OWNER_RE = re.compile(
    r"\b([A-Z][A-Za-z0-9._+-]*(?:\s+[A-Z][A-Za-z0-9._+-]*)?\s+"
    r"(?:Stack|API|APIs|SDK|CLI|Runtime|Server|Platform|Distribution|Distributions))\b"
)
_LICENSE_EXCEPTION_RE = re.compile(
    r"\b(?:except(?:\s+for)?|excluding|with\s+the\s+exception\s+of)\b",
    re.IGNORECASE,
)
_VARIANT_SCALE_RE = re.compile(r"\b\d+(?:\.\d+)?B\b", re.IGNORECASE)
_OTHER_LICENSE_RE = re.compile(
    r"\b(?:Qwen\s+Research|Qwen\s+License|Research\s+License|Community\s+License)\b",
    re.IGNORECASE,
)


def _foreign_mentions(sentence: str, aliases: list[str], rendered: str) -> list[tuple[int, int, str]]:
    found = v26._foreign_mentions(sentence, aliases, rendered)
    for match in _COMPONENT_OWNER_RE.finditer(sentence):
        mention = match.group(1).strip()
        if v25._mention_is_target(mention, aliases):
            continue
        item = (match.start(), match.end(), mention)
        if item not in found:
            found.append(item)
    return found


def _license_scope_is_safe(window: str, sentence: str, rendered: str) -> bool:
    """Permit bare family-level license rendering only when scope is homogeneous/unqualified."""
    if rendered not in _LICENSE_SIGNALS:
        return True
    # "all models except 3B/72B are Apache 2.0" is useful source prose, but rendering only
    # "Apache 2.0" destroys the exception binding. Require an explicit override instead.
    if _LICENSE_EXCEPTION_RE.search(sentence):
        return False

    scales = {m.group(0).lower() for m in _VARIANT_SCALE_RE.finditer(window)}
    heterogeneous = _OTHER_LICENSE_RE.search(window) is not None
    if len(scales) >= 2 and heterogeneous:
        return False

    # Multi-variant families need an explicit universal statement before a single license may
    # safely describe the whole family. Tables with per-row licenses therefore fail closed.
    if len(scales) >= 2:
        universal = re.search(
            rf"\b(?:all|every)\b[^.!?\n]{{0,140}}\blicen[cs]ed?\b[^.!?\n]{{0,100}}{re.escape(rendered)}",
            sentence,
            re.IGNORECASE,
        )
        if universal is None:
            return False
    return True


def _signal_is_target_bound(window: str, start: int, end: int, title: str, rendered: str) -> bool:
    aliases = v25._subject_aliases(title)
    if not aliases:
        return False
    sent_start, sent_end = v26._sentence_span(window, start)
    sentence = window[sent_start:sent_end]
    local_start = start - sent_start
    local_end = end - sent_start
    target_spans = v25._alias_spans(sentence, aliases)
    if not target_spans:
        return False

    if rendered.endswith("B parameter scale"):
        prefix = sentence[max(0, local_start - 16):local_start].lower()
        if re.search(r"(?:sub-|under\s+|below\s+|less\s+than\s+)$", prefix):
            return False

    if rendered.endswith("K context") or rendered.endswith("M context"):
        vicinity = sentence[max(0, local_start - 120):min(len(sentence), local_end + 120)].lower()
        if re.search(r"single\s+(?:gpu|node)", vicinity):
            return False

    if not _license_scope_is_safe(window, sentence, rendered):
        return False

    target_distance = min(v25._distance_to_span(local_start, span) for span in target_spans)
    foreign = _foreign_mentions(sentence, aliases, rendered)
    if not foreign:
        return True

    foreign_distance = min(v25._distance_to_span(local_start, (s, e)) for s, e, _ in foreign)
    if foreign_distance < target_distance:
        return False

    for f_start, f_end, _ in foreign:
        gap_before = local_start - f_end
        if 0 <= gap_before <= 24:
            return False
        gap_after = f_start - local_end
        if 0 <= gap_after <= 16:
            return False
    return True


def _entity_aware_technical_signals(summary: str, events: list[tuple[str, str]], title: str = "") -> list[str]:
    window = event_layer._safe_event_window(summary, events, title)
    aliases = v25._subject_aliases(title)
    anchor = aliases[0] if aliases else v24._artifact_anchor(title)
    if not window:
        v24._AUDIT_ROWS.append({
            "title": title,
            "anchor": anchor,
            "accepted_entity_bound_signals": [],
            "rejected_entity_bound_signals": [],
            "window_empty": True,
        })
        return []

    signals: list[str] = []
    accepted_bound: list[str] = []
    rejected_bound: list[str] = []
    dynamic_accepted = 0

    for template, pattern in impl._DYNAMIC_PATTERNS:
        for match in re.finditer(pattern, window, flags=re.IGNORECASE):
            value = next((group for group in match.groups() if group), "")
            if not value:
                continue
            rendered = template.format(value)
            if template in v24._ENTITY_BOUND_DYNAMIC_TEMPLATES:
                if not _signal_is_target_bound(window, match.start(), match.end(), title, rendered):
                    if rendered not in rejected_bound:
                        rejected_bound.append(rendered)
                    continue
                if rendered not in accepted_bound:
                    accepted_bound.append(rendered)
            if rendered not in signals and dynamic_accepted < 4:
                signals.append(rendered)
                dynamic_accepted += 1

    for display, pattern in impl._SIGNAL_PATTERNS:
        if display in event_layer.event._UNSAFE_SIGNAL_NAMES:
            continue
        matches = list(re.finditer(pattern, window, flags=re.IGNORECASE | re.DOTALL))
        if not matches:
            continue
        if display in v24._ENTITY_BOUND_STATIC_SIGNALS:
            bound = [_signal_is_target_bound(window, m.start(), m.end(), title, display) for m in matches]
            # V3 scope-sensitive properties are aggregate facts. A single safe occurrence cannot
            # authorize a value when another occurrence on the same selected source has different
            # component/variant ownership; explicit subject-labelled override is required.
            accepted = all(bound) if display in _SCOPE_SENSITIVE_STATIC_SIGNALS else any(bound)
            if not accepted:
                if display not in rejected_bound:
                    rejected_bound.append(display)
                continue
            if display not in accepted_bound:
                accepted_bound.append(display)
        if display not in signals:
            signals.append(display)
        if len(signals) >= 7:
            break

    v24._AUDIT_ROWS.append({
        "title": title,
        "anchor": anchor,
        "accepted_entity_bound_signals": accepted_bound,
        "rejected_entity_bound_signals": rejected_bound,
        "window_empty": False,
    })
    return signals[:7]


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    old_entity_fn = v25._entity_aware_technical_signals
    old_signal_fn = v25._signal_is_target_bound
    old_contract = v25._ENTITY_BINDING_CONTRACT
    old_static = set(v24._ENTITY_BOUND_STATIC_SIGNALS)
    v25._entity_aware_technical_signals = _entity_aware_technical_signals
    v25._signal_is_target_bound = _signal_is_target_bound
    v25._ENTITY_BINDING_CONTRACT = _ENTITY_BINDING_CONTRACT
    v24._ENTITY_BOUND_STATIC_SIGNALS = old_static | _SCOPE_SENSITIVE_STATIC_SIGNALS
    try:
        return v25.build(repo_root, special_slug, issue_id, source_version)
    finally:
        v25._entity_aware_technical_signals = old_entity_fn
        v25._signal_is_target_bound = old_signal_fn
        v25._ENTITY_BINDING_CONTRACT = old_contract
        v24._ENTITY_BOUND_STATIC_SIGNALS = old_static


if __name__ == "__main__":
    import argparse
    import json

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    result = build(Path(args.repo_root).resolve(), args.special_slug, args.issue_id, args.source_version)
    print(json.dumps(result, ensure_ascii=False, indent=2))
