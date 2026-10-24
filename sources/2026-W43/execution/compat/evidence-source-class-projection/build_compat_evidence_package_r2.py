#!/usr/bin/env python3
"""Build the W43 r2 edition-local derived Evidence compatibility package.

Same frozen pattern as the r1 builder (W42 CV2DM016 precedent): prepare via
frozen Core under the native agent-first override, project ONLY
source_records[*].source_type per COMPAT_MAP into derived compat tasks,
recompute task SHAs, validate. r1 artifacts untouched; output goes to a new
compat-package-r2 directory. Supplement manifest is the r2 manifest (2 carried
paper entries + 3 first-party entries + real MemT paper entry).
"""
from __future__ import annotations

import json
import sys
import tempfile
from copy import deepcopy
from pathlib import Path

from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core

ISSUE_ID = "2026-W43"
SOURCE_ROOT_REL = "sources/2026-W43"
STATE_REL = SOURCE_ROOT_REL + "/production-state.json"
DISCOVERY_REL = SOURCE_ROOT_REL + "/discovery/discovery-v2.jsonl"
SCREENING_REL = ("sources/2026-W43/screening/v2/accepted/"
                 "75dd95db5c40b28cc2d9a665dab8a46294e010096095c2bf92aba36d5ed9817d/"
                 "screening-accepted.json")
SUPPLEMENT_REL = (SOURCE_ROOT_REL + "/external/evidence-supplement/"
                  "evidence-authority-supplement-r2.json")

COMPAT_MAP = {
    "X_VENDOR_STATEMENT": "SOCIAL",
    "X_OBSERVATION": "SOCIAL",
    "SECONDARY_CLAIM": "SECONDARY",
    "PAPER_LEAD": "SOCIAL",
    "SECONDARY_OR_COMMUNITY_LEAD": "SECONDARY",
}
RULE_ID_PREFIX = "CV2DM016-W43-MAP"


def build_once(repo_root: Path, output_dir: Path, implementation_sha: str) -> dict:
    state_path = repo_root / STATE_REL
    discovery_path = repo_root / DISCOVERY_REL
    screening_path = repo_root / SCREENING_REL
    supplement_path = repo_root / SUPPLEMENT_REL
    if output_dir.exists() and any(output_dir.iterdir()):
        raise ValueError(f"refusing to overwrite non-empty compat output: {output_dir}")

    with tempfile.TemporaryDirectory() as tmp:
        with agent_tool.current_stage_basis_override():
            normal_pkg_path = evidence.prepare_evidence_package(
                repo_root, state_path, discovery_path, screening_path,
                Path(tmp) / "normal", implementation_sha, supplement_path,
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
            else:
                try:
                    evidence.task_authority_sources(repo_root, task, package)
                except ValueError as exc:
                    raise ValueError(
                        f"COMPATIBILITY_PROJECTION_INVALID: unmapped source vocabulary "
                        f"{original_type!r} on {task['evidence_task_id']}"
                    ) from exc
                new_type = original_type
                rule = f"{RULE_ID_PREFIX}:passthrough"
            check_orig = deepcopy(task)
            check_proj = deepcopy(projected)
            for rec in check_orig["source_records"]:
                rec["source_type"] = None
            for rec in check_proj["source_records"]:
                rec["source_type"] = None
            if check_orig != check_proj:
                raise ValueError(
                    f"COMPATIBILITY_PROJECTION_INVALID: non-source_type drift on "
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


def main() -> int:
    root = Path(".").resolve()
    impl = core.repository_commit_sha(root)
    compat_dir = root / ("sources/2026-W43/execution/compat/"
                         "evidence-source-class-projection")
    out_dir = compat_dir / "compat-package-r2"
    ledger_path = compat_dir / "projection-ledger-r2.json"
    for path in (out_dir, ledger_path):
        if isinstance(path, Path) and path.exists():
            raise ValueError(f"refusing to overwrite: {path}")
    ledger = build_once(root, out_dir, impl)
    core.write_json(ledger_path, {
        "schema_version": "2.0-rc1",
        "issue_id": ISSUE_ID,
        "projection_map": COMPAT_MAP,
        "rule_id_prefix": RULE_ID_PREFIX,
        **ledger,
    })
    print(json.dumps({k: ledger[k] for k in (
        "compat_package_path", "compat_package_sha256", "task_count",
        "projected_count", "passthrough_count")}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
