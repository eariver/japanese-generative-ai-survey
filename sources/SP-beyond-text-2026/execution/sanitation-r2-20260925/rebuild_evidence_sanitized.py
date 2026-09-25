#!/usr/bin/env python3
"""Rebuild sanitized Evidence + Views over the rebound compat package.

Same canonical builders/validators/acceptors as the rebind run; only the
interactive input differs (provenance-state wording sanitation, semantics
identical). Prior result-sets (r1, r2, rebound) preserved via guards; new SHA
yields new content-addressed dirs. No State advance here.
"""

from __future__ import annotations

import json
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_screening_v2 as screening
from scripts import run_evidence_v2_interactive as inter

ISSUE_ID = "SP-beyond-text-2026"
STATE_REL = "sources/SP-beyond-text-2026/production-state.json"
INPUT_REL = "sources/SP-beyond-text-2026/execution/sanitation-r2-20260925/evidence-interactive-input-r2-sanitized.json"
COMPAT_REL = "sources/SP-beyond-text-2026/execution/sanitation-r2-20260925/compat-sanitized/package.json"
EXEC_REL = "sources/SP-beyond-text-2026/execution/sanitation-r2-20260925"
PRIOR_SHAS = {
    "f01de6548929c74d9b9715e382027c89e5aa5c780f3865ebbf5e3e3b654985e7",
    "048cbd0942f073ed6ba134c97a5691e9ea4eb1eb0db6fa1ed842abe5faf2810e",
    "29804dcfe7d9a1e1045c1b5c93d8d708e9890445afbb0f57b061ca555a178426",
}


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / STATE_REL
    state = core.load_json(state_path)
    assert state.get("issue_id") == ISSUE_ID and state.get("lifecycle_state") == "ARCHITECTURE_ESTABLISHED", state.get("lifecycle_state")
    assert not agent.validate_agent_state(root, cfg, state)
    for sha in PRIOR_SHAS:
        p = root / f"sources/SP-beyond-text-2026/evidence/v2/accepted/{sha}/evidence-accepted.json"
        assert p.is_file(), sha
    before = {sha: core.sha256_file(root / f"sources/SP-beyond-text-2026/evidence/v2/accepted/{sha}/evidence-accepted.json")
              for sha in PRIOR_SHAS}

    profile_path = root / state["profile"]["path"]
    profile = core.load_json(profile_path)
    source_root = core.repo_local_path(root, profile["paths"]["source_root"], "paths.source_root")
    impl = core.repository_commit_sha(root)
    compat_path = root / COMPAT_REL
    package = core.load_json(compat_path)
    assert package.get("issue_id") == ISSUE_ID
    with agent_tool.current_stage_basis_override():
        evidence.validate_evidence_package_basis(root, compat_path, package, impl)
    task_meta = {m["discovery_ids"][0]: m for m in package["tasks"]}
    expected = set(task_meta)
    tsrc = {did: set(evidence.task_authority_sources(root, core.load_json(compat_path.parent / m["path"]), package))
            for did, m in task_meta.items()}
    doc = core.load_json(root / INPUT_REL)
    runner = inter._validate_runner(doc.get("runner"))
    by_id = {}
    for raw in doc["records"]:
        row = inter._validate_record(raw, profile)
        did = row["discovery_id"]
        assert did not in by_id, did
        allowed = tsrc.get(did)
        assert allowed is not None, did
        b = row.get("source_bindings")
        if b is None:
            assert len(allowed) == 1, did
        else:
            assert set(b) <= allowed, did
        by_id[did] = row
    assert set(by_id) == expected

    with tempfile.TemporaryDirectory() as temp:
        tmp = Path(temp)
        resdir = tmp / "results"
        resdir.mkdir()
        for did in sorted(task_meta):
            meta = task_meta[did]
            task = core.load_json(compat_path.parent / meta["path"])
            card = inter._build_card(root, task, meta, package, by_id[did], runner)
            errs = evidence.validate_evidence_card(card, task, meta["sha256"], package, repo_root=root)
            assert not errs, f"{did}: {errs}"
            core.write_json(resdir / Path(meta["path"]).name, card)
        with agent_tool.current_stage_basis_override():
            eap = evidence.accept_evidence_results(root, compat_path, resdir,
                                                   source_root / "evidence/v2/accepted", impl)
            evidence.validate_evidence_acceptance(root, eap, impl)
        eacc = core.load_json(eap)
        by_task = {r["evidence_task_id"]: r for r in eacc["results"]}
        vdir = tmp / "views"
        vdir.mkdir()
        for did in sorted(task_meta):
            meta = task_meta[did]
            entry = by_task[meta["evidence_task_id"]]
            view = inter._build_view(profile, meta["evidence_task_id"], entry["sha256"], by_id[did])
            errs = evidence.validate_edition_view(view, profile, entry["sha256"], entry["status"])
            assert not errs, f"{did}: {errs}"
            core.write_json(vdir / evidence.view_filename(meta["evidence_task_id"]), view)
        with agent_tool.current_stage_basis_override():
            vap = evidence.accept_edition_views(root, profile_path, eap, vdir,
                                                source_root / "evidence/v2/views/accepted", impl)
            evidence.validate_edition_views_acceptance(root, profile_path, eap, vap, impl)

    for sha in PRIOR_SHAS:
        assert core.sha256_file(root / f"sources/SP-beyond-text-2026/evidence/v2/accepted/{sha}/evidence-accepted.json") == before[sha], "history mutated"
    new_sha = core.sha256_file(eap)
    assert new_sha not in PRIOR_SHAS
    active = screening.resolve_active_screening_acceptance(root, state_path, impl)
    core.write_json(root / EXEC_REL / "evidence-sanitized-build-report.json", {
        "schema_version": "1.0", "issue_id": ISSUE_ID,
        "method": "CANONICAL_EVIDENCE_SANITIZED_THEN_STOP (no State change here)",
        "compat_package": str(compat_path.relative_to(root)),
        "prior_result_sets_preserved": sorted(PRIOR_SHAS),
        "lifecycle_state": core.load_json(state_path)["lifecycle_state"],
        "screening_acceptance": str(Path(active["artifact_path"]).relative_to(root)),
        "evidence_acceptance": str(eap.relative_to(root)),
        "evidence_sha256": new_sha,
        "views_acceptance": str(vap.relative_to(root)),
        "views_sha256": core.sha256_file(vap),
        "evidence_results": len(eacc["results"]),
        "state_advanced": False,
        "built_at": datetime.now(timezone.utc).isoformat()})
    print(json.dumps({"evidence": str(eap.relative_to(root)), "evidence_sha256": new_sha,
                      "views": str(vap.relative_to(root)), "results": len(eacc["results"])}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
