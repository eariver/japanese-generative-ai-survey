#!/usr/bin/env python3
"""Rebuild compat package over rebound bytes (new screening acceptance basis)."""

from __future__ import annotations

import json
import sys
import tempfile
from copy import deepcopy
from pathlib import Path

sys.path.insert(0, "sources/SP-beyond-text-2026/execution/x-import-screening-evidence-20260924/compat")
from build_compat_evidence_package import COMPAT_MAP, RULE_ID_PREFIX  # noqa: E402

from scripts import survey_agent_tool_v2 as agent_tool  # noqa: E402
from scripts import survey_evidence_v2 as evidence  # noqa: E402
from scripts import survey_production_v2 as core  # noqa: E402

ISSUE_ID = "SP-beyond-text-2026"
STATE_REL = "sources/SP-beyond-text-2026/production-state.json"
SCREENING_REL = ("sources/SP-beyond-text-2026/screening/v2/accepted/"
                 "7d608d55a3f5498e97a9e44ce63e28328aefe3c0fe1470cffafc1a8cd91280e9/"
                 "screening-accepted.json")
OUTDIR = Path("sources/SP-beyond-text-2026/execution/sanitation-r2-20260925/compat-sanitized")


def main() -> int:
    root = Path(".").resolve()
    global OUTDIR
    OUTDIR = (root / OUTDIR).resolve()
    impl = core.repository_commit_sha(root)
    state = core.load_json(root / STATE_REL)
    profile = core.load_json(root / state["profile"]["path"])
    source_root = core.repo_local_path(root, profile["paths"]["source_root"], "paths.source_root")
    accepted_discovery = core.load_json(source_root / "discovery/discovery-accepted-v2.json")
    discovery_path = core.repo_local_path(root, accepted_discovery["discovery_path"], "accepted Discovery JSONL")
    screening_path = root / SCREENING_REL
    if OUTDIR.exists() and any(OUTDIR.iterdir()):
        raise ValueError("refusing to overwrite non-empty compat output")

    with tempfile.TemporaryDirectory() as tmp:
        with agent_tool.current_stage_basis_override():
            normal_pkg = evidence.prepare_evidence_package(
                root, root / STATE_REL, discovery_path, screening_path,
                Path(tmp) / "normal", impl, None)
        package = core.load_json(normal_pkg)
        normal_dir = normal_pkg.parent
        tasks_dir = OUTDIR / "tasks"
        tasks_dir.mkdir(parents=True, exist_ok=True)
        rows, meta2, proj = [], [], 0
        for meta in package["tasks"]:
            task = core.load_json(normal_dir / meta["path"])
            projected = deepcopy(task)
            recs = projected.get("source_records", [])
            assert len(recs) == 1, meta
            orig = recs[0].get("source_type")
            if orig in COMPAT_MAP:
                recs[0]["source_type"] = COMPAT_MAP[orig]
                proj += 1
                rule = f"{RULE_ID_PREFIX}:{orig}->{COMPAT_MAP[orig]}"
            else:
                try:
                    evidence.task_authority_sources(root, task, package)
                except ValueError as exc:
                    raise ValueError(f"unmapped vocabulary {orig!r} on {task['evidence_task_id']}") from exc
                rule = f"{RULE_ID_PREFIX}:passthrough"
            co, cp = deepcopy(task), deepcopy(projected)
            for r in co["source_records"]:
                r["source_type"] = None
            for r in cp["source_records"]:
                r["source_type"] = None
            assert co == cp, f"non-source_type drift on {task['evidence_task_id']}"
            outp = tasks_dir / Path(meta["path"]).name
            core.write_json(outp, projected)
            new_sha, old_sha = core.sha256_file(outp), core.sha256_file(normal_dir / meta["path"])
            assert old_sha == meta["sha256"], "normal task hash mismatch"
            rows.append({"discovery_id": task["discovery_ids"][0],
                         "evidence_task_id": task["evidence_task_id"],
                         "original_source_type": orig,
                         "projected_source_type": recs[0]["source_type"],
                         "original_task_sha256": old_sha, "projected_task_sha256": new_sha,
                         "locator": recs[0].get("locator"), "projection_rule": rule})
            m = dict(meta)
            m["sha256"] = new_sha
            meta2.append(m)
        compat = deepcopy(package)
        compat["tasks"] = meta2
        core.write_json(OUTDIR / "package.json", compat)
        with agent_tool.current_stage_basis_override():
            evidence.validate_evidence_package_basis(root, OUTDIR / "package.json", compat, impl)
    core.write_json(OUTDIR.parent / "projection-ledger-sanitized.json",
                    {"schema_version": "1.0", "issue_id": ISSUE_ID,
                     "projection_map": COMPAT_MAP, "rule_id_prefix": RULE_ID_PREFIX,
                     "compat_package_path": str((OUTDIR / "package.json").relative_to(root)),
                     "compat_package_sha256": core.sha256_file(OUTDIR / "package.json"),
                     "task_count": len(meta2), "projected_count": proj,
                     "passthrough_count": len(meta2) - proj,
                     "rows": sorted(rows, key=lambda r: r["discovery_id"])})
    print(json.dumps({"tasks": len(meta2), "projected": proj,
                      "passthrough": len(meta2) - proj,
                      "sha": core.sha256_file(OUTDIR / "package.json")}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
