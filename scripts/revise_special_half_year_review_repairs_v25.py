#!/usr/bin/env python3
"""Strengthen Half-year Technical Note subject/entity binding with version-aware attribution.

V24 established a local family-anchor boundary, but an announcement can mention the selected
family and a comparator in the same sentence. V25 therefore binds high-risk signals to a
version-aware selected-artifact alias and rejects a candidate when a closer foreign model
mention owns the value. It is intentionally conservative: losing an automatically extracted
signal is preferable to publishing a confidently misattributed specification; accepted
Screening-backed overrides remain the fail-closed recovery path.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v24 as base
from scripts import revise_special_half_year_review_repairs_v15 as event_layer

impl = event_layer.impl

_ENTITY_BINDING_CONTRACT = "SUBJECT_VERSION_AWARE_HIGH_RISK_SIGNALS_V2"

_GENERIC_MODEL_WORDS = {
    "a", "an", "and", "architecture", "available", "context", "effective", "family",
    "for", "from", "in", "large", "long", "model", "models", "new", "of", "on",
    "open", "preview", "release", "small", "the", "to", "with",
    "transformer", "using", "window",
}

# Capitalised/product-like spans used only as a competing-subject detector. A mention without a
# version/scale is considered foreign only when it sits very close to the candidate signal; this
# catches "Codestral 22B" / "Codestral Mamba" while avoiding ordinary prose headings.
_MODEL_MENTION_RE = re.compile(
    r"\b([A-Z][A-Za-z0-9._+-]*(?:\s+[A-Z][A-Za-z0-9._+-]*)?(?:\s+\d+(?:\.\d+)?(?:[A-Za-z]+)?)?)\b"
)
_SENTENCE_BOUNDARY_RE = re.compile(r"[.!?;\n]")


def _normal(value: str) -> str:
    return re.sub(r"\s+", " ", str(value or "").replace("/", " ")).strip().lower()


def _subject_aliases(title: str) -> list[str]:
    """Derive version-aware aliases from a selected artifact title.

    Examples:
      Jamba 1.5 Mini and Large -> Jamba 1.5 Mini / Jamba 1.5 Large / Jamba 1.5
      Ministral 3B and 8B     -> Ministral 3B / Ministral 8B
      Llama 3.2               -> Llama 3.2
      Mistral Large 2         -> Mistral Large 2
    """
    text = re.sub(r"\\([&_#%{}])", r"\1", str(title or ""))
    text = re.sub(r"\s+", " ", text).strip()
    aliases: list[str] = []

    scale_pair = re.match(r"^(.+?)\s+(\d+(?:\.\d+)?B)\s+(?:and|/)\s+(\d+(?:\.\d+)?B)\b", text, re.I)
    if scale_pair:
        base_name, first, second = scale_pair.groups()
        aliases.extend([f"{base_name} {first}", f"{base_name} {second}"])
    variant_pair = re.match(r"^(.+?\d+(?:\.\d+)?)\s+([A-Za-z][A-Za-z0-9-]*)\s+and\s+([A-Za-z][A-Za-z0-9-]*)\b", text)
    if variant_pair:
        stem, first, second = variant_pair.groups()
        aliases.extend([f"{stem} {first}", f"{stem} {second}", stem])

    # Keep the identity-bearing prefix through the first version token. For names such as
    # "Mistral Large 2", include the capitalised descriptor before the version as well.
    version = re.match(r"^([A-Za-z][A-Za-z0-9._+-]*(?:\s+[A-Z][A-Za-z0-9._+-]*)?\s+\d+(?:\.\d+)?)(?:\s|$)", text)
    if version:
        aliases.append(version.group(1))

    # Titles like "Llama 3.3 70B Instruct" should also bind the release-scale identity.
    scaled = re.match(r"^([A-Za-z][A-Za-z0-9._+-]*\s+\d+(?:\.\d+)?\s+\d+(?:\.\d+)?B)\b", text, re.I)
    if scaled:
        aliases.append(scaled.group(1))

    if not aliases:
        # For non-versioned artifacts retain V24's conservative family anchor.
        anchor = base._artifact_anchor(text)
        if anchor:
            aliases.append(anchor)

    out: list[str] = []
    for alias in aliases:
        alias = re.sub(r"\s+", " ", alias).strip()
        if alias and _normal(alias) not in {_normal(item) for item in out}:
            out.append(alias)
    # Prefer the most specific alias for distance comparisons.
    return sorted(out, key=len, reverse=True)


def _sentence_span(text: str, pos: int) -> tuple[int, int]:
    start = 0
    for match in _SENTENCE_BOUNDARY_RE.finditer(text, 0, pos):
        start = match.end()
    end_match = _SENTENCE_BOUNDARY_RE.search(text, pos)
    end = end_match.start() if end_match else len(text)
    return start, end


def _alias_spans(sentence: str, aliases: list[str]) -> list[tuple[int, int]]:
    spans: list[tuple[int, int]] = []
    for alias in aliases:
        pattern = re.compile(rf"(?<![A-Za-z0-9]){re.escape(alias)}(?![A-Za-z0-9])", re.I)
        spans.extend((m.start(), m.end()) for m in pattern.finditer(sentence))
    return spans


def _mention_is_target(mention: str, aliases: list[str]) -> bool:
    m = _normal(mention)
    if not m:
        return False
    for alias in aliases:
        a = _normal(alias)
        if m == a or m.startswith(a + " ") or a.startswith(m + " "):
            return True
    return False


def _foreign_mentions(sentence: str, aliases: list[str]) -> list[tuple[int, int, str]]:
    found: list[tuple[int, int, str]] = []
    for match in _MODEL_MENTION_RE.finditer(sentence):
        mention = match.group(1).strip()
        tokens = mention.split()
        if not tokens:
            continue
        first = tokens[0].lower()
        has_identity_cue = any(ch.isdigit() for ch in mention) or any(ch in mention for ch in ".+-")
        # A lone capitalised token can still be a model/product (Codestral, Mamba), but common
        # prose words are excluded unless the span contains an identity cue.
        if not has_identity_cue and first in _GENERIC_MODEL_WORDS:
            continue
        if _mention_is_target(mention, aliases):
            continue
        found.append((match.start(), match.end(), mention))
    return found


def _distance_to_span(pos: int, span: tuple[int, int]) -> int:
    start, end = span
    if start <= pos <= end:
        return 0
    if pos < start:
        return start - pos
    return pos - end


def _signal_is_target_bound(window: str, start: int, end: int, title: str, rendered: str) -> bool:
    aliases = _subject_aliases(title)
    if not aliases:
        return False
    sent_start, sent_end = _sentence_span(window, start)
    sentence = window[sent_start:sent_end]
    local_start = start - sent_start
    local_end = end - sent_start
    target_spans = _alias_spans(sentence, aliases)
    if not target_spans:
        return False

    # Category expressions such as "sub-10B" are not a model's parameter specification.
    if rendered.endswith("B parameter scale"):
        prefix = sentence[max(0, local_start - 16):local_start].lower()
        if re.search(r"(?:sub-|under\s+|below\s+|less\s+than\s+)$", prefix):
            return False

    # A deployment-capacity statement (e.g. 140K on one GPU) is not the advertised model
    # context-window specification. The same page may separately contain the real 256K window.
    if rendered.endswith("K context") or rendered.endswith("M context"):
        vicinity = sentence[max(0, local_start - 120):min(len(sentence), local_end + 120)].lower()
        if re.search(r"single\s+(?:gpu|node)", vicinity):
            return False

    target_distance = min(_distance_to_span(local_start, span) for span in target_spans)
    foreign = _foreign_mentions(sentence, aliases)
    if not foreign:
        return True

    # A comparator/product mention that is closer to the value than the selected subject owns
    # the value for extraction purposes. This also catches list continuations such as
    # "Llama 3.1 70B and 405B" where the second scale omits the repeated model name.
    foreign_distance = min(_distance_to_span(local_start, (s, e)) for s, e, _ in foreign)
    if foreign_distance < target_distance:
        return False

    # Direct attachment is stronger than a distant target mention even on equal boundaries.
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
    aliases = _subject_aliases(title)
    anchor = aliases[0] if aliases else base._artifact_anchor(title)
    if not window:
        base._AUDIT_ROWS.append({
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
            if template in base._ENTITY_BOUND_DYNAMIC_TEMPLATES:
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
        if display in base._ENTITY_BOUND_STATIC_SIGNALS:
            if not any(_signal_is_target_bound(window, m.start(), m.end(), title, display) for m in matches):
                if display not in rejected_bound:
                    rejected_bound.append(display)
                continue
            if display not in accepted_bound:
                accepted_bound.append(display)
        if display not in signals:
            signals.append(display)
        if len(signals) >= 7:
            break

    base._AUDIT_ROWS.append({
        "title": title,
        "anchor": anchor,
        "accepted_entity_bound_signals": accepted_bound,
        "rejected_entity_bound_signals": rejected_bound,
        "window_empty": False,
    })
    return signals[:7]


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    old_fn = base._entity_aware_technical_signals
    old_contract = base._ENTITY_BINDING_CONTRACT
    base._entity_aware_technical_signals = _entity_aware_technical_signals
    base._ENTITY_BINDING_CONTRACT = _ENTITY_BINDING_CONTRACT
    try:
        return base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        base._entity_aware_technical_signals = old_fn
        base._ENTITY_BINDING_CONTRACT = old_contract


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
