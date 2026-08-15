#!/usr/bin/env python3
"""Refine V25 entity attribution without relaxing its fail-closed policy.

V25 intentionally requires a selected-artifact alias in the same sentence as a high-risk
signal. This layer fixes one detector edge case: the candidate signal token itself (for
example ``Mamba`` or ``SSM-Transformer``) must not be counted as a competing entity, while
ordinary capitalised prose such as ``Research License`` must not outrank the selected model.
Comparison-model/version mentions remain stronger owners of nearby numeric signals.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v25 as base

_ENTITY_BINDING_CONTRACT = base._ENTITY_BINDING_CONTRACT
_SINGLE_TOKEN_RE = re.compile(r"\b([A-Z][A-Za-z0-9._+-]*)\b")
_GENERIC_MODEL_WORDS = set(base._GENERIC_MODEL_WORDS) | {
    "community", "license", "parameters", "research", "score", "quality", "release",
    "today", "built", "effective", "novel", "improved",
}


def _foreign_mentions(sentence: str, aliases: list[str], rendered: str) -> list[tuple[int, int, str]]:
    """Return plausible competing subjects, excluding the signal token itself.

    Versioned/scaled spans are strong subject cues. For unversioned names we also inspect
    individual capitalised tokens so ``Codestral Mamba`` can still make ``Mamba`` foreign to
    Mistral Large 2, while generic prose tokens are ignored.
    """
    signal_key = base._normal(rendered)
    candidates: list[tuple[int, int, str]] = []
    for regex in (base._MODEL_MENTION_RE, _SINGLE_TOKEN_RE):
        for match in regex.finditer(sentence):
            mention = match.group(1).strip()
            mention_key = base._normal(mention)
            if not mention_key or mention_key == signal_key:
                continue
            tokens = mention.split()
            first = tokens[0].lower()
            has_identity_cue = any(ch.isdigit() for ch in mention) or any(ch in mention for ch in ".+-")
            if not has_identity_cue:
                if len(tokens) > 1:
                    # Multi-word capitalised prose is too ambiguous; its constituent tokens are
                    # examined separately by _SINGLE_TOKEN_RE.
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
    sent_start, sent_end = base._sentence_span(window, start)
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
    old = base._signal_is_target_bound
    base._signal_is_target_bound = _signal_is_target_bound
    try:
        return base._entity_aware_technical_signals(summary, events, title)
    finally:
        base._signal_is_target_bound = old


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    old_signal = base._signal_is_target_bound
    old_entity = base._entity_aware_technical_signals
    base._signal_is_target_bound = _signal_is_target_bound
    base._entity_aware_technical_signals = _entity_aware_technical_signals
    try:
        # base.build captures its module-level _entity_aware_technical_signals into V24. The
        # wrapper above keeps the V26 signal predicate active for every extracted candidate.
        return base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        base._signal_is_target_bound = old_signal
        base._entity_aware_technical_signals = old_entity


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
