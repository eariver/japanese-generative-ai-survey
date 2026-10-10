#!/usr/bin/env python3
"""W40 r8 edition-local derived Evidence package (r7 supplement + approved projection).

PROPOSED_NOT_ACCEPTED until Sol authorizes acceptance. Frozen Core imports only;
no Core modification; canonical Discovery/Screening/r1 tasks/r5/r6/r7 proposals
preserved. Expected outcome: byte-identical tasks/package to r7 (no source drift),
recorded as r7->r8 equality proof under the CURRENT implementation SHA.

Delta vs r7: none in task bytes expected (supplement r7 manifest reused unchanged;
approved projection unchanged). Lineage per task: r1 -> r5 -> r6 -> r7 -> r8 SHAs.
"""

from __future__ import annotations

import json
import tempfile
from copy import deepcopy
from pathlib import Path

from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core

ISSUE_ID = "2026-W40"
SOURCE_ROOT_REL = "sources/2026-W40"
STATE_REL = SOURCE_ROOT_REL + "/production-state.json"
DISCOVERY_REL = SOURCE_ROOT_REL + "/discovery/discovery-v2.jsonl"
SCREENING_REL = (SOURCE_ROOT_REL + "/screening/v2/accepted/"
                 "2409f568e649b25407a75d0f2baa1311de0420e77099611128b660b5cd744627/"
                 "screening-accepted.json")
SUPPLEMENT_REL = (SOURCE_ROOT_REL + "/external/evidence-supplement/"
                  "evidence-authority-supplement-r7.json")
R7_LEDGER = (SOURCE_ROOT_REL + "/execution/compat/evidence-supplement-card-binding-r7/"
             "projection-ledger-r7.json")

COMPAT_MAP = {
    "PRIMARY_RESEARCH_ABSTRACT": "PRIMARY_PAPER",
    "EVALUATOR_PUBLISHER": "PRIMARY_OFFICIAL",
}
RULE_ID_PREFIX = "W40MAP"


def build_once(repo_root: Path, output_dir: Path, implementation_sha: str) -> dict:
    if output_dir.exists() and any(output_dir.iterdir()):
        raise ValueError(f"refusing to overwrite non-empty r8 output: {output_dir}")
    with tempfile.TemporaryDirectory() as tmp:
        with agent_tool.current_stage_basis_override():
            normal_pkg_path = evidence.prepare_evidence_package(
                repo_root, repo_root / STATE_REL, repo_root / DISCOVERY_REL,
                repo_root / SCREENING_REL, Path(tmp) / "normal", implementation_sha,
                repo_root / SUPPLEMENT_REL,
            )
        package = core.load_json(normal_pkg_path)
        normal_dir = normal_pkg_path.parent
        if "authority_supplement" not in package:
            raise ValueError("r8 normal package lacks authority_supplement binding")
        r7ledger = core.load_json(repo_root / R7_LEDGER)
        r7sha = {r["discovery_id"]: r["r7_supplement_r7_bound_projected_sha256"]
                 for r in r7ledger["rows"]}
        r1pkg = core.load_json(repo_root / "sources/2026-W40/evidence/v2/packages/r1/package.json")
        r1sha = {m["discovery_ids"][0]: m["sha256"] for m in r1pkg["tasks"]}
        compat_tasks_dir = output_dir / "tasks"
        compat_tasks_dir.mkdir(parents=True, exist_ok=True)
        ledger_rows = []
        compat_meta = []
        projected_count = 0
        for meta in package["tasks"]:
            task = core.load_json(normal_dir / meta["path"])
            projected = deepcopy(task)
            recs = projected.get("source_records", [])
            if len(recs) != 1:
                raise ValueError(f"{task['evidence_task_id']}: expected exactly one source record")
            original_type = recs[0].get("source_type")
            if original_type in COMPAT_MAP:
                recs[0]["source_type"] = COMPAT_MAP[original_type]
                projected_count += 1
                rule = f"{RULE_ID_PREFIX}:{original_type}->{COMPAT_MAP[original_type]}"
            else:
                try:
                    evidence.task_authority_sources(repo_root, task, package)
                except ValueError as exc:
                    raise ValueError(
                        "COMPATIBILITY_PROJECTION_INVALID: unmapped source vocabulary "
                        f"{original_type!r} on {task['evidence_task_id']}"
                    ) from exc
                rule = f"{RULE_ID_PREFIX}:passthrough"
            check_orig = deepcopy(task)
            check_proj = deepcopy(projected)
            for rec in check_orig["source_records"]:
                rec["source_type"] = None
            for rec in check_proj["source_records"]:
                rec["source_type"] = None
            if check_orig != check_proj:
                raise ValueError(
                    "COMPATIBILITY_PROJECTION_INVALID: non-source_type drift on "
                    f"{task['evidence_task_id']}"
                )
            out_path = compat_tasks_dir / Path(meta["path"]).name
            core.write_json(out_path, projected)
            new_sha = core.sha256_file(out_path)
            did = task["discovery_ids"][0]
            ledger_rows.append({
                "discovery_id": did,
                "evidence_task_id": task["evidence_task_id"],
                "r1_canonical_task_sha256": r1sha[did],
                "r7_supplement_r7_bound_projected_sha256": r7sha[did],
                "r8_supplement_r7_bound_projected_sha256": new_sha,
                "r7_r8_task_bytes_identical": (r7sha[did] == new_sha),
                "supplement_source_ids": sorted(task.get("authority_supplement_source_ids", [])),
                "projection_rule": rule,
            })
            row_meta = dict(meta)
            row_meta["sha256"] = new_sha
            compat_meta.append(row_meta)
        compat_package = deepcopy(package)
        compat_package["tasks"] = compat_meta
        compat_path = output_dir / "package.json"
        core.write_json(compat_path, compat_package)
        with agent_tool.current_stage_basis_override():
            evidence.validate_evidence_package_basis(
                repo_root, compat_path, compat_package, implementation_sha
            )
        for meta in compat_meta:
            t = core.load_json(output_dir / meta["path"])
            evidence.task_authority_sources(repo_root, t, compat_package)
    try:
        rel_path = str(compat_path.relative_to(repo_root))
    except ValueError:
        rel_path = compat_path.as_posix()
    return {
        "compat_package_path": rel_path,
        "compat_package_sha256": core.sha256_file(compat_path),
        "task_count": len(compat_meta),
        "projected_count": projected_count,
        "passthrough_count": len(compat_meta) - projected_count,
        "supplement_bound_tasks": sum(1 for r in ledger_rows if r["supplement_source_ids"]),
        "tasks_identical_to_r7": sum(1 for r in ledger_rows if r["r7_r8_task_bytes_identical"]),
        "rows": sorted(ledger_rows, key=lambda r: r["discovery_id"]),
    }


def negative_tests(repo_root: Path) -> dict:
    out = {}
    pkg = core.load_json(repo_root / "sources/2026-W40/evidence/v2/packages/r1/package.json")
    for meta in pkg["tasks"]:
        task = core.load_json(repo_root / "sources/2026-W40/evidence/v2/packages/r1" / meta["path"])
        if task["discovery_ids"][0] in ("w40-primary-contextlms-20260929",
                                        "w40-prewindow-lift-20260925",
                                        "w40-primary-aa-agentperf-20260929"):
            try:
                evidence.task_authority_sources(repo_root, task, pkg)
                raise AssertionError("original failure did NOT reproduce")
            except ValueError as exc:
                out[task["discovery_ids"][0]] = str(exc)
    forged = deepcopy(task)
    forged["source_records"][0]["source_type"] = "BOGUS_UNREVIEWED_TYPE"
    try:
        evidence.task_authority_sources(repo_root, forged, pkg)
        raise AssertionError("BOGUS type did not fail closed")
    except ValueError as exc:
        out["BOGUS_UNREVIEWED_TYPE"] = "FAIL_CLOSED: " + str(exc)
    return out


def main() -> int:
    root = Path(".").resolve()
    impl = core.repository_commit_sha(root)
    compat_dir = root / ("sources/2026-W40/execution/compat/"
                         "evidence-supplement-card-binding-r8")
    out_dir = compat_dir / "compat-package"
    ledger_path = compat_dir / "projection-ledger-r8.json"
    for path in (out_dir, ledger_path):
        if path.exists():
            raise ValueError(f"refusing to overwrite: {path}")
    first = build_once(root, out_dir, impl)
    with tempfile.TemporaryDirectory() as tmp2:
        second = build_once(root, Path(tmp2) / "compat2", impl)
    if (first["compat_package_sha256"] != second["compat_package_sha256"]
            or [(r["discovery_id"], r["r8_supplement_r7_bound_projected_sha256"]) for r in first["rows"]]
            != [(r["discovery_id"], r["r8_supplement_r7_bound_projected_sha256"]) for r in second["rows"]]):
        raise ValueError("reproducibility self-test FAILED")
    negative = negative_tests(root)
    core.write_json(ledger_path, {
        "schema_version": "2.0-rc1",
        "issue_id": ISSUE_ID,
        "status": "PROPOSED_NOT_ACCEPTED",
        "projection_map": COMPAT_MAP,
        "supplement_manifest": SUPPLEMENT_REL,
        "prior_r7_ledger": "sources/2026-W40/execution/compat/evidence-supplement-card-binding-r7/projection-ledger-r7.json",
        "negative_tests": negative,
        "reproducibility": "DOUBLE_BUILD_IDENTICAL_PASS",
        **first,
    })
    print(json.dumps({
        "compat_package_path": first["compat_package_path"],
        "compat_package_sha256": first["compat_package_sha256"],
        "task_count": first["task_count"],
        "projected_count": first["projected_count"],
        "supplement_bound_tasks": first["supplement_bound_tasks"],
        "tasks_identical_to_r7": first["tasks_identical_to_r7"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
