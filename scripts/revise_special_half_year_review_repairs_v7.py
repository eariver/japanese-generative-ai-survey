#!/usr/bin/env python3
"""Scoped entry point for Screening-backed Half-year Technical Notes enrichment.

v6 contains the enrichment implementation, but imports legacy compatibility modules that
historically communicate through module globals. Keep those globals unchanged at import
time so direct v3/v4/v5 helper tests and unrelated callers retain their original contract.
Only the actual routed Half-year build temporarily installs the v6 helpers, then restores
the previous functions in a finally block.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from scripts import revise_special_half_year_review_repairs_v6 as impl

core = impl.core

# Undo v6's compatibility-time global installation immediately. This makes importing this
# wrapper side-effect free for the rest of the process.
core.merge_evidence_index = impl._ORIGINAL_MERGE
core.source_specific_fact = impl._ORIGINAL_FACT
core.repair_note_file = impl._ORIGINAL_REPAIR_NOTE_FILE

# Re-export pure helpers used by regression tests and future compatibility layers.
_technical_signals = impl._technical_signals
_validate_override = impl._validate_override
_enrich_fact_line = impl._enrich_fact_line


def build(repo_root: Path, special_slug: str, issue_id: str, source_version: str) -> dict[str, Any]:
    previous_merge = core.merge_evidence_index
    previous_fact = core.source_specific_fact
    previous_repair = core.repair_note_file
    impl._ACTIVE_SOURCE_VERSION = source_version
    impl._ACTIVE_OVERRIDES = impl._load_overrides(repo_root, issue_id, source_version)
    core.merge_evidence_index = impl.merge_evidence_index
    core.source_specific_fact = impl.source_specific_fact
    core.repair_note_file = impl.repair_note_file
    try:
        result = impl.compat.build(repo_root, special_slug, issue_id, source_version)
        if isinstance(result, dict):
            result["technical_note_detail_overrides"] = len(impl._ACTIVE_OVERRIDES)
            result["technical_note_detail_contract"] = "SCREENING_BACKED_FAIL_CLOSED"
        return result
    finally:
        core.merge_evidence_index = previous_merge
        core.source_specific_fact = previous_fact
        core.repair_note_file = previous_repair
        impl._ACTIVE_SOURCE_VERSION = ""
        impl._ACTIVE_OVERRIDES = {}


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
