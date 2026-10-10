#!/usr/bin/env python3
"""W40 r5 edition-local Evidence source-type compatibility projection (PROPOSED_NOT_ACCEPTED).

Frozen-Core compatibility adapter for the W40 recurrence of CV2-DM-016.
Imports frozen Core modules only; modifies nothing outside the edition tree
and no Core module state. Canonical Discovery/Screening bytes preserved.

Reviewed narrow mappings (Sol r5 contract §1):
  PRIMARY_RESEARCH_ABSTRACT -> PRIMARY_PAPER
    (content depth REMAINS abstract-only until full paper consumed; role = arXiv submission)
  EVALUATOR_PUBLISHER -> PRIMARY_OFFICIAL
    (ONLY for the evaluator's own original benchmark report; role = first-party
    evaluator/publisher of the benchmark, NOT model vendor, NOT independent reproduction)

Procedure (mirrors SP-efficient-llm-2026 precedent):
  1. frozen evidence.prepare_evidence_package over canonical bytes into temp dir;
  2. project ONLY source_records[*].source_type per COMPAT_MAP into derived
     compat tasks (fail closed on any other unmapped vocabulary or any other
     field difference); passthrough tasks must already resolve under frozen Core;
  3. recompute projected task SHAs; update only task SHA metadata in derived package;
  4. frozen evidence.validate_evidence_package_basis over derived package;
  5. negative tests: original 3 tasks still raise; synthetic unreviewed type raises.
Reproducibility: build twice, require identical bytes/hashes.
Output is PROPOSED_NOT_ACCEPTED until Sol authorizes the exact ledger.
"""

from __future__ import annotations

import hashlib
import json
import sys
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

COMPAT_MAP = {
    "PRIMARY_RESEARCH_ABSTRACT": "PRIMARY_PAPER",
    "EVALUATOR_PUBLISHER": "PRIMARY_OFFICIAL",
}
ROLE_NOTES = {
    "PRIMARY_RESEARCH_ABSTRACT": "arXiv-submission role; abstract-only depth until full paper consumed",
    "EVALUATOR_PUBLISHER": "first-party evaluator/publisher of its own benchmark report; not model vendor; not independent reproduction",
}
RULE_ID_PREFIX = "W40MAP"
EXPECTED_AFFECTED = {
    "w40-primary-contextlms-20260929",
    "w40-prewindow-lift-20260925",
    "w40-primary-aa-agentperf-20260929",
}


def reproduce_failure(repo_root: Path) -> list[dict]:
    """Reproduce the exact frozen-Core failure on the 3 affected canonical tasks."""
    pkg = core.load_json(repo_root / "sources/2026-W40/evidence/v2/packages/r1/package.json")
    failures = []
    for meta in pkg["tasks"]:
        task = core.load_json(repo_root / "sources/2026-W40/evidence/v2/packages/r1" / meta["path"])
        did = task["discovery_ids"][0]
        if did not in EXPECTED_AFFECTED:
            continue
        try:
            evidence.task_authority_sources(repo_root, task, pkg)
            raise AssertionError(f"expected failure did NOT occur on {did}")
        except ValueError as exc:
            failures.append({"discovery_id": did,
                             "evidence_task_id": task["evidence_task_id"],
                             "error": str(exc)})
    if {f["discovery_id"] for f in failures} != EXPECTED_AFFECTED:
        raise AssertionError("failure reproduction covered unexpected task set")
    return failures


def build_once(repo_root: Path, output_dir: Path, implementation_sha: str) -> dict:
    state_path = repo_root / STATE_REL
    discovery_path = repo_root / DISCOVERY_REL
    screening_path = repo_root / SCREENING_REL
    if output_dir.exists() and any(output_dir.iterdir()):
        raise ValueError(f"refusing to overwrite non-empty compat output: {output_dir}")
    with tempfile.TemporaryDirectory() as tmp:
        with agent_tool.current_stage_basis_override():
            normal_pkg_path = evidence.prepare_evidence_package(
                repo_root, state_path, discovery_path, screening_path,
                Path(tmp) / "normal", implementation_sha, None,
            )
        package = core.load_json(normal_pkg_path)
        normal_dir = normal_pkg_path.parent
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
                new_type = COMPAT_MAP[original_type]
                recs[0]["source_type"] = new_type
                projected_count += 1
                rule = f"{RULE_ID_PREFIX}:{original_type}->{new_type}"
                role = ROLE_NOTES[original_type]
            else:
                try:
                    evidence.task_authority_sources(repo_root, task, package)
                except ValueError as exc:
                    raise ValueError(
                        "COMPATIBILITY_PROJECTION_INVALID: unmapped source vocabulary "
                        f"{original_type!r} on {task['evidence_task_id']}"
                    ) from exc
                new_type = original_type
                rule = f"{RULE_ID_PREFIX}:passthrough"
                role = "natively supported frozen Core class"
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
            old_sha = core.sha256_file(normal_dir / meta["path"])
            if old_sha != meta["sha256"]:
                raise ValueError("normal package task hash mismatch")
            ledger_rows.append({
                "discovery_id": task["discovery_ids"][0],
                "evidence_task_id": task["evidence_task_id"],
                "original_source_type": original_type,
                "projected_source_type": new_type,
                "original_task_sha256": old_sha,
                "projected_task_sha256": new_sha,
                "locator": recs[0].get("locator"),
                "projection_rule": rule,
                "role_note": role,
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
        # Proof: every bound task now resolves under frozen Core.
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
        "rows": sorted(ledger_rows, key=lambda r: r["discovery_id"]),
    }


def negative_unreviewed_type(repo_root: Path) -> dict:
    """Failure injection: an unreviewed source type must still fail closed."""
    pkg = core.load_json(repo_root / "sources/2026-W40/evidence/v2/packages/r1/package.json")
    meta = pkg["tasks"][0]
    task = core.load_json(repo_root / "sources/2026-W40/evidence/v2/packages/r1" / meta["path"])
    forged = deepcopy(task)
    forged["source_records"][0]["source_type"] = "BOGUS_UNREVIEWED_TYPE"
    try:
        evidence.task_authority_sources(repo_root, forged, pkg)
    except ValueError as exc:
        return {"injected_type": "BOGUS_UNREVIEWED_TYPE", "result": "FAIL_CLOSED_PASS",
                "error": str(exc)}
    raise AssertionError("negative test FAILED: unreviewed type did not fail closed")


def main() -> int:
    root = Path(".").resolve()
    impl = core.repository_commit_sha(root)
    compat_dir = root / ("sources/2026-W40/execution/compat/"
                         "evidence-source-class-projection-r5")
    out_dir = compat_dir / "compat-package"
    ledger_path = compat_dir / "projection-ledger.json"
    for path in (out_dir, ledger_path):
        if path.exists():
            raise ValueError(f"refusing to overwrite: {path}")
    failures = reproduce_failure(root)
    first = build_once(root, out_dir, impl)
    # Reproducibility: second build into temp must match byte-for-byte.
    with tempfile.TemporaryDirectory() as tmp2:
        second = build_once(root, Path(tmp2) / "compat2", impl)
    if (first["compat_package_sha256"] != second["compat_package_sha256"]
            or [(r["discovery_id"], r["projected_task_sha256"]) for r in first["rows"]]
            != [(r["discovery_id"], r["projected_task_sha256"]) for r in second["rows"]]):
        raise ValueError("reproducibility self-test FAILED: builds differ")
    negative = negative_unreviewed_type(root)
    core.write_json(ledger_path, {
        "schema_version": "2.0-rc1",
        "issue_id": ISSUE_ID,
        "status": "PROPOSED_NOT_ACCEPTED",
        "projection_map": COMPAT_MAP,
        "role_notes": ROLE_NOTES,
        "rule_id_prefix": RULE_ID_PREFIX,
        "reproduced_failures": failures,
        "negative_test": negative,
        "reproducibility": "DOUBLE_BUILD_IDENTICAL_PASS",
        **first,
    })
    print(json.dumps({"compat_package_path": first["compat_package_path"],
                        "compat_package_sha256": first["compat_package_sha256"],
                        "task_count": first["task_count"],
                        "projected_count": first["projected_count"],
                        "passthrough_count": first["passthrough_count"],
                        "negative": negative["result"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
