#!/usr/bin/env python3
"""Prepare canonical TS-003 Evidence package (tasks only; no cards/views yet)."""

from __future__ import annotations

import json
from pathlib import Path

from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
SCREEN_ACC = f"{SRC}/screening/v2/accepted/71136cdd8c054b993f899fb394aee30f3cf8d23fbed61dd0a53cd29cd660de67/screening-accepted.json"
PKG_DIR = f"{SRC}/execution/screening-evidence-20260930/evidence-package"


def main() -> int:
    root = Path(".").resolve()
    with agent_tool.current_stage_basis_override():
        package_path = evidence.prepare_evidence_package(
            root,
            root / STATE_REL,
            root / DISC_REL,
            root / SCREEN_ACC,
            root / PKG_DIR,
            core.repository_commit_sha(root),
            None,
        )
    package = core.load_json(package_path)
    print("package:", package_path)
    print("tasks:", len(package["tasks"]))
    print("issue:", package.get("issue_id"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
