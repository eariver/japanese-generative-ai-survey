#!/usr/bin/env python3
"""Complete canonical Evidence views/materiality/completeness from persisted acceptance.

Resume-run driver (edition-side orchestration, cf. advance_screening_r3.py precedent).
Calls ONLY reviewed-Core functions in the SAME order/arguments as
scripts/run_evidence_v2_interactive.py run(); skips recomputation of the already
persisted + validated evidence acceptance (deterministic bytes reused verbatim).

Step A (this script): revalidate persisted evidence acceptance -> build views cards
  (identical loop to runner) -> accept edition views -> validate views acceptance.
Prints the views acceptance path. Does NOT advance state.

Execution agent: Muse Spark 1.3 / EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION
"""
from __future__ import annotations

import sys
import tempfile
from pathlib import Path

REPO = Path(".").resolve()
sys.path.insert(0, str(REPO))
from scripts import survey_agent_control_v2 as agent  # noqa: E402
from scripts import survey_agent_tool_v2 as agent_tool  # noqa: E402
from scripts import survey_evidence_v2 as evidence  # noqa: E402
from scripts import survey_production_v2 as core  # noqa: E402
from scripts import run_evidence_v2_interactive as runner  # noqa: E402

EXEC_REL = "sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2"
EVIDENCE_ACCEPTANCE_REL = (
    "sources/2026-W34/evidence/v2/accepted/"
    "647cde464d92935c1ca633ade62bcbf7ebe88c458cc8b3848bae8d2fc4794831/"
    "evidence-accepted.json"
)

def main() -> int:
    repo_root = REPO
    cfg = core.load_json(repo_root / core.DEFAULT_CONFIG)
    state_path = repo_root / "sources/2026-W34/production-state.json"
    state = core.load_json(state_path)
    errors = agent.validate_agent_state(repo_root, cfg, state)
    if errors:
        raise ValueError("Production State invalid: " + "; ".join(errors))
    if state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("requires CANDIDATES_NORMALIZED")
    implementation_sha = core.repository_commit_sha(repo_root)
    print(f"implementation_sha={implementation_sha}", flush=True)

    profile_path = repo_root / state["profile"]["path"]
    profile = core.load_json(profile_path)

    # Mirror the runner: all package/acceptance basis checks run under the
    # reviewed agent-first current-stage-basis override.
    with agent_tool.current_stage_basis_override():
        result = _complete(repo_root, state_path, profile_path, profile, implementation_sha)
    print(f"VIEWS_ACCEPTANCE={result}", flush=True)
    return 0

def _complete(repo_root: Path, state_path: Path, profile_path: Path, profile: dict, implementation_sha: str) -> str:

    # 1. Revalidate persisted evidence acceptance (full Core revalidation).
    evidence_acceptance_path = repo_root / EVIDENCE_ACCEPTANCE_REL
    evidence_acceptance, package = evidence.validate_evidence_acceptance(
        repo_root, evidence_acceptance_path, implementation_sha
    )
    print(f"evidence acceptance revalidated: result_count={evidence_acceptance['result_count']}", flush=True)
    task_meta = {meta["discovery_ids"][0]: meta for meta in package["tasks"]}
    expected_ids = set(task_meta)

    # 2. Interactive input validation (same call as runner).
    input_path = repo_root / EXEC_REL / "interactive-evidence.json"
    persisted_package = core.load_json(evidence_acceptance_path.parent / "package.json")
    task_source_ids = {
        did: set(evidence.task_authority_sources(
            repo_root,
            core.load_json(evidence_acceptance_path.parent / "tasks" / Path(meta["path"]).name),
            persisted_package,
        ))
        for did, meta in sorted(task_meta.items())
    }
    interactive_doc = core.load_json(input_path)
    records_by_id, runner_meta, _ = runner.validate_interactive_input(
        interactive_doc, profile, expected_ids, task_source_ids
    )
    print(f"interactive input validated: records={len(records_by_id)}", flush=True)

    # 3. Build + accept + validate edition views (verbatim runner loop).
    evidence_by_task = {row["evidence_task_id"]: row for row in evidence_acceptance["results"]}
    with tempfile.TemporaryDirectory() as temp:
        views_dir = Path(temp) / "views"
        views_dir.mkdir()
        for did in sorted(task_meta):
            meta = task_meta[did]
            task_id = meta["evidence_task_id"]
            entry = evidence_by_task[task_id]
            view = runner._build_view(profile, task_id, entry["sha256"], records_by_id[did])
            errs = evidence.validate_edition_view(view, profile, entry["sha256"], entry["status"])
            if errs:
                raise ValueError(f"interactive Edition View {did} invalid: {'; '.join(errs)}")
            core.write_json(views_dir / evidence.view_filename(task_id), view)
        print("views cards built: 409", flush=True)
        views_root = repo_root / "sources/2026-W34/evidence/v2/views/accepted"
        with agent_tool.current_stage_basis_override():
            views_acceptance_path = evidence.accept_edition_views(
                repo_root, profile_path, evidence_acceptance_path,
                views_dir, views_root, implementation_sha,
            )
            evidence.validate_edition_views_acceptance(
                repo_root, profile_path, evidence_acceptance_path,
                views_acceptance_path, implementation_sha,
            )
    print(f"VIEWS_ACCEPTANCE={views_acceptance_path.relative_to(repo_root)}", flush=True)
    return views_acceptance_path.relative_to(repo_root).as_posix()

if __name__ == "__main__":
    raise SystemExit(main())
