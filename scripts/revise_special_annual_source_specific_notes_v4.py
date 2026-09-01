#!/usr/bin/env python3
"""Annual Technical Notes repair through the v17 captured incremental bridge.

The Half-year v17 compatibility layer captures v8._incremental_build at import time.  Annual v2
correctly adapts the manifest shape in-memory, but patching v8._incremental_build alone cannot reach
that captured reference.  This wrapper changes only the v17 captured delegate for the duration of
an Annual repair, pointing it at the existing Annual manifest adapter.  The adapter itself still
calls the immutable original v8 builder, so Half-year semantics and all #191/#139 fail-closed
contracts remain unchanged.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_annual_source_specific_notes_v2 as annual_v2
from scripts import revise_special_annual_source_specific_notes_v3 as base
from scripts import revise_special_half_year_review_repairs_v17 as unbuilt_bridge

_CONTRACT = "ANNUAL_V17_CAPTURED_INCREMENTAL_ADAPTER_V1"


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous = unbuilt_bridge._ORIGINAL_INCREMENTAL_BUILD
    unbuilt_bridge._ORIGINAL_INCREMENTAL_BUILD = annual_v2._annual_incremental_build
    try:
        result = base.build(repo_root, special_slug, issue_id, source_version)
    finally:
        unbuilt_bridge._ORIGINAL_INCREMENTAL_BUILD = previous
    result = dict(result)
    result["annual_v17_incremental_adapter_contract"] = _CONTRACT
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--special-slug", required=True)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--source-version", required=True)
    args = parser.parse_args()
    print(json.dumps(build(Path(args.repo_root), args.special_slug, args.issue_id, args.source_version), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
