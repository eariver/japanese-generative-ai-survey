#!/usr/bin/env python3
"""Canonical public release identity helpers.

Public releases are identified by issue only. Internal source revisions remain
provenance and must never be appended to public tags, titles, or PDF asset names.
Legacy already-published versioned releases remain valid historical records.
"""

from __future__ import annotations

import re


WEEKLY_RE = re.compile(r"^[0-9]{4}-W[0-9]{2}$")
SPECIAL_SLUG_RE = re.compile(r"^[0-9]{4}-(?:M[0-9]{2}|H[12]|Y)$")


def weekly_release_identity(issue_id: str) -> dict[str, str]:
    if not WEEKLY_RE.fullmatch(issue_id):
        raise ValueError(f"invalid Weekly issue id: {issue_id!r}")
    return {
        "release_identity_mode": "ISSUE_ONLY",
        "release_tag": f"weekly/{issue_id}",
        "release_title": f"Japanese Generative AI Technical Survey — {issue_id}",
        "asset_name": f"Japanese_Generative_AI_Technical_Survey_{issue_id}.pdf",
    }


def special_release_identity(special_slug: str) -> dict[str, str]:
    if not SPECIAL_SLUG_RE.fullmatch(special_slug):
        raise ValueError(f"invalid Special slug: {special_slug!r}")
    return {
        "release_identity_mode": "ISSUE_ONLY",
        "release_tag": f"special/{special_slug}",
        "release_title": f"Japanese Generative AI Technical Survey Special — {special_slug}",
        "asset_name": f"Japanese_Generative_AI_Technical_Survey_Special_{special_slug}.pdf",
    }
