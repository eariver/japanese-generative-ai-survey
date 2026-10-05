#!/usr/bin/env python3
"""Build the fresh 120-task Evidence package (no cards consumed). Idempotent reuse."""
from __future__ import annotations
from pathlib import Path

from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core

import build_union

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/late-cutoff-expansion-20261005"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/evidence-package-120"


def build_package(root: Path):
    from scripts import survey_agent_tool_v2 as agent_tool
    with agent_tool.current_stage_basis_override():
        scr_acc_path = max((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"),
                           key=lambda p: p.stat().st_mtime)
        assert core.load_json(scr_acc_path)["record_count"] == 120
        union_out = build_union.build_union(root)
        state = core.load_json(root / STATE_REL)
        assert state["lifecycle_state"] == "CANDIDATES_NORMALIZED"
        impl = core.repository_commit_sha(root)
        import shutil
        shutil.rmtree(root / PKGDIR, ignore_errors=True)
        package_path = evidence.prepare_evidence_package(
            root, root / STATE_REL, root / DISC_REL, scr_acc_path,
            root / PKGDIR, impl, union_out)
        package = core.load_json(package_path)
        assert len(package["tasks"]) == 120, len(package["tasks"])
        return package_path, package


def main() -> int:
    root = Path(".").resolve()
    package_path, package = build_package(root)
    print("package:", package_path.relative_to(root), "| tasks:", len(package["tasks"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
