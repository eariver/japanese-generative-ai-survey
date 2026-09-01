#!/usr/bin/env python3
"""Refine V25 entity attribution without relaxing its fail-closed policy.

V25 intentionally requires a selected-artifact alias in the same sentence as a high-risk
signal. This layer fixes detector edge cases: candidate signal vocabulary (for example
``Mamba`` or ``SSM-Transformer``), selected-artifact alias tokens, and decimal version points
must not manufacture competing subjects or false sentence boundaries. Comparison-model/version
mentions remain stronger owners of nearby numeric signals.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v25 as base
from scripts import revise_special_half_year_review_repairs_v24 as v24

_ENTITY_BINDING_CONTRACT = base._ENTITY_BINDING_CONTRACT
_SINGLE_TOKEN_RE = re.compile(r"\b([A-Z][A-Za-z0-9._+-]*)\b")
# A decimal point in a model version such as Jamba 1.5 is not a sentence boundary. Terminal
# periods still split because they are not followed by another digit.
_SENTENCE_BOUNDARY_RE = re.compile(r"[!?;\n]|\.(?!\d)")
_GENERIC_MODEL_WORDS = set(base._GENERIC_MODEL_WORDS) | {
    "community", "license", "parameters", "research", "score", "quality", "release",
    "today", "built", "effective", "novel", "improved",
}
_NON_SUBJECT_SIGNAL_KEYS = {
    base._normal(signal) for signal in v24._ENTITY_BOUND_STATIC_SIGNALS
}


def _alias_constituent_keys(aliases: list[str]) -> set[str]:
    """Return textual tokens that belong to the selected artifact identity."""
    out: set[str] = set()
    for alias in aliases:
        for token in re.findall(r"[A-Za-z][A-Za-z0-9._+-]*", alias):
            key = base._normal(token)
            if key:
                out.add(key)
    return out


def _sentence_span(text: str, pos: int) -> tuple[int, int]:
    start = 0
    for match in _SENTENCE_BOUNDARY_RE.finditer(text, 0, pos):
        start = match.end()
    end_match = _SENTENCE_BOUNDARY_RE.search(text, pos)
    end = end_match.start() if end_match else len(text)
    return start, end


def _foreign_mentions(sentence: str, aliases: list[str], rendered: str) -> list[tuple[int, int, str]]:
    """Return plausible competing subjects, excluding selected/signal vocabulary."""
    signal_key = base._normal(rendered)
    alias_tokens = _alias_constituent_keys(aliases)
    candidates: list[tuple[int, int, str]] = []
    for regex in (base._MODEL_MENTION_RE, _SINGLE_TOKEN_RE):
        for match in regex.finditer(sentence):
            mention = match.group(1).strip()
            mention_key = base._normal(mention)
            if (
                not mention_key
                or mention_key == signal_key
                or mention_key in _NON_SUBJECT_SIGNAL_KEYS
                or mention_key in alias_tokens
            ):
                continue
            tokens = mention.split()
            first = tokens[0].lower()
            has_identity_cue = any(ch.isdigit() for ch in mention) or any(ch in mention for ch in ".+-")
            if not has_identity_cue:
                if len(tokens) > 1:
                    continue
                if first in _GENERIC_MODEL_WORDS:
                    continue
            if base._mention_is_target(mention, aliases):
                continue
            item = (match.start(), match.end(), mention)
            if item not in candidates:
                candidates.append(item)
    return candidates


def _signal_is_target_bound(window: str, start: int, end: int, title: str, rendered: str) -> bool:
    aliases = base._subject_aliases(title)
    if not aliases:
        return False
    sent_start, sent_end = _sentence_span(window, start)
    sentence = window[sent_start:sent_end]
    local_start = start - sent_start
    local_end = end - sent_start
    target_spans = base._alias_spans(sentence, aliases)
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

    target_distance = min(base._distance_to_span(local_start, span) for span in target_spans)
    foreign = _foreign_mentions(sentence, aliases, rendered)
    if not foreign:
        return True

    foreign_distance = min(base._distance_to_span(local_start, (s, e)) for s, e, _ in foreign)
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
    old_signal = base._signal_is_target_bound
    base._signal_is_target_bound = _signal_is_target_bound
    try:
        return base._entity_aware_technical_signals(summary, events, title)
    finally:
        base._signal_is_target_bound = old_signal


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    old_signal = base._signal_is_target_bound
    base._signal_is_target_bound = _signal_is_target_bound
    try:
        return base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        base._signal_is_target_bound = old_signal


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
