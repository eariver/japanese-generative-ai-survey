#!/usr/bin/env python3
"""Extend Half-year V3 binding to generic capability/navigation signals.

Issue #191 showed a second class of cross-subject contamination after component-specific RAG
and reranking repairs: generic capability labels from current site navigation can still be
picked up as historical model properties. OpenELM, for example, inherited ``image generation``
and a generic ``small model / cost-efficient deployment`` label from adjacent Apple research
navigation after its v0.13 Human-reviewed card had already removed those claims.

These signals are not intrinsically invalid. They are unsafe only when they are not locally
owned by the selected artifact. V34 therefore promotes the observed generic capability labels
into the existing V3 component-scoped binding set. ``speculative decoding`` is included for
the same reason: event-window filtering already rejected the later Cohere navigation occurrence,
but component binding should independently fail closed if such a label survives a future source
layout change.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v27 as binding
from scripts import revise_special_half_year_review_repairs_v33 as base

_ADDITIONAL_COMPONENT_SCOPED_SIGNALS = {
    "image generation",
    "small model / cost-efficient deployment",
    "speculative decoding",
}
_GENERIC_CAPABILITY_BINDING_CONTRACT = "GENERIC_CAPABILITY_SUBJECT_BINDING_V1"


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    old_component = set(binding._COMPONENT_SCOPED_SIGNALS)
    old_scope = set(binding._SCOPE_SENSITIVE_STATIC_SIGNALS)
    binding._COMPONENT_SCOPED_SIGNALS = old_component | _ADDITIONAL_COMPONENT_SCOPED_SIGNALS
    binding._SCOPE_SENSITIVE_STATIC_SIGNALS = old_scope | _ADDITIONAL_COMPONENT_SCOPED_SIGNALS
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        binding._COMPONENT_SCOPED_SIGNALS = old_component
        binding._SCOPE_SENSITIVE_STATIC_SIGNALS = old_scope

    if isinstance(result, dict):
        result = dict(result)
        result["generic_capability_subject_binding_contract"] = _GENERIC_CAPABILITY_BINDING_CONTRACT
    return result


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
