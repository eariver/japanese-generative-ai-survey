#!/usr/bin/env python3
"""Special-edition wrapper around the canonical Evidence execution package builder."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from scripts import prepare_evidence_run

ANY_SURVEY_ISSUE_RE = re.compile(r"^(?:[0-9]{4}-W[0-9]{2}|SP-[A-Za-z0-9][A-Za-z0-9._-]{2,63})$")
SPECIAL_ISSUE_RE = re.compile(r"^SP-[A-Za-z0-9][A-Za-z0-9._-]{2,63}$")


def build_package(**kwargs):
    issue_id = kwargs["issue_id"]
    if not SPECIAL_ISSUE_RE.fullmatch(issue_id):
        raise ValueError("Special Evidence package requires canonical SP-* issue_id")
    prepare_evidence_run.ISSUE_RE = ANY_SURVEY_ISSUE_RE
    return prepare_evidence_run.build_package(**kwargs)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root", default=".")
    p.add_argument("--output-root", required=True)
    p.add_argument("--issue-id", required=True)
    p.add_argument("--screening-run-sha", required=True)
    p.add_argument("--source-ref", required=True)
    p.add_argument("--source-commit", required=True)
    a = p.parse_args()
    package = build_package(
        repo_root=Path(a.repo_root), output_root=Path(a.output_root), issue_id=a.issue_id,
        screening_run_sha=a.screening_run_sha, source_ref=a.source_ref, source_commit=a.source_commit,
    )
    print(json.dumps(package, ensure_ascii=False, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
