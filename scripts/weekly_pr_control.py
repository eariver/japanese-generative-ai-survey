#!/usr/bin/env python3
"""Prepare deterministic metadata for the auditable weekly Draft PR control workflow.

This script has no GitHub write side effects. The workflow consumes its output to
create a work branch / Draft PR while keeping merge, freeze, and release outside
this control plane.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ISSUE_RE = re.compile(r"^[0-9]{4}-W[0-9]{2}$")


def load_optional_state(repo_root: Path, issue_id: str) -> dict[str, Any] | None:
    path = repo_root / "sources" / issue_id / "pipeline-state.json"
    if not path.is_file():
        return None
    value = json.loads(path.read_text(encoding="utf-8"))
    return value if isinstance(value, dict) else None


def build(issue_id: str, repo_root: Path) -> dict[str, Any]:
    if not ISSUE_RE.fullmatch(issue_id):
        raise ValueError("issue_id must use YYYY-Www form")
    branch = f"weekly/{issue_id}-work"
    title = f"Weekly survey work — {issue_id}"
    state = load_optional_state(repo_root, issue_id)
    lifecycle_state = state.get("lifecycle_state") if state else None
    state_note = (
        f"`{lifecycle_state}`"
        if isinstance(lifecycle_state, str) and lifecycle_state
        else "not initialized on this branch"
    )
    body = f"""## Weekly survey work — {issue_id}

This is the auditable **Draft PR** for the weekly survey pipeline. It is a work surface, not an editorial approval, Freeze decision, or public Release authorization.

Current committed pipeline lifecycle state: {state_note}

### Required gates

- [ ] Reviewed collector artifacts imported append-only; Raw provenance indexed
- [ ] Screening complete and validated
- [ ] Primary Evidence verification complete for promoted items
- [ ] Candidate Selection explicitly `APPROVED`
- [ ] Issue Architecture explicitly `APPROVED`
- [ ] Structured article Draft Results validated
- [ ] Deterministic article rendering and bibliography merge complete
- [ ] Post-draft Cover / This Week synthesis validated
- [ ] Final source assembly and source-level preflight passed
- [ ] LuaLaTeX/Biber build and final TeX-log gate passed
- [ ] Visual review passed
- [ ] Freeze decision recorded

Public GitHub Release publication is a separate workflow and is never performed by this PR-control workflow.

### Automation behavior

Automation may create this branch/PR and refresh this description **only while the PR remains Draft**. Once a human marks the PR ready for review, PR-control automation must stop modifying its metadata.
"""
    return {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "branch": branch,
        "title": title,
        "body": body,
        "pipeline_state_status": lifecycle_state,
        "rules": [
            "Create the weekly work branch only when absent; never force-update it.",
            "If an existing work branch has no unique commits, it may be fast-forwarded to the current default branch before weekly work begins.",
            "Never rewrite or auto-rebase a work branch that already contains unique weekly commits.",
            "Create or edit only a Draft PR from the canonical weekly work branch to the default branch.",
            "If the existing PR is no longer Draft, fail rather than overwrite human review state.",
            "Never merge, freeze, tag, or publish a Release from this workflow.",
        ],
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--issue-id", required=True)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--output", required=True)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    value = build(args.issue_id, Path(args.repo_root))
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(value, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
