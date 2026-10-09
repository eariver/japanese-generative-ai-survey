#!/usr/bin/env python3
"""Build TS-003 Architecture r2 artifacts with canonical Core base functions.

Regeneration boundary SELECTION_COMPLETE: matrix/selection untouched (byte-identical).
Regenerates architecture-v2.json + review summary + review attention from the r2
interactive input using the same canonical builders the interactive runner uses.
"""
import shutil
from pathlib import Path

from scripts import survey_agent_control_v2 as agent_tool_ctl
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_architecture_v2 as architecture
from scripts import survey_discovery_v2 as discovery
from scripts import survey_production_v2 as core
from scripts import survey_review_attention_v2 as review_attention
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_screening_v2 as screening

REPO = Path(".")
SRC = REPO / "sources/SP-vision-multimodal-2026"
STATE = SRC / "production-state.json"
R2DIR = SRC / "execution/architecture-r2-20261001"
INPUT = R2DIR / "interactive-architecture-r2.json"


def main() -> int:
    cfg = core.load_json(REPO / core.DEFAULT_CONFIG)
    state = core.load_json(STATE)
    assert state["lifecycle_state"] == "SELECTION_COMPLETE", state["lifecycle_state"]
    profile_path = REPO / state["profile"]["path"]
    profile = core.load_json(profile_path)
    source_root = core.repo_local_path(REPO, profile["paths"]["source_root"], "paths.source_root")

    discovery_acceptance_path = source_root / "discovery/discovery-accepted-v2.json"
    accepted_discovery = discovery.validate_acceptance(REPO, discovery_acceptance_path)
    root_discovery_path = core.repo_local_path(REPO, accepted_discovery["discovery_path"], "accepted Discovery JSONL")
    ledger_path = source_root / "materiality-ledger-v2.json"
    completeness_path = source_root / "profile-completeness-v2.json"
    implementation_sha = core.repository_commit_sha(REPO)
    active = agent_tool_ctl.resolve_active_evidence_views(REPO, cfg, state)
    evidence_path, views_path = active["evidence_path"], active["views_path"]
    screening_path = screening.resolve_active_screening_acceptance(REPO, STATE, implementation_sha)["path"]
    effective = screening.resolve_effective_discovery_basis(
        REPO, screening_path.parent / "package.json", implementation_sha,
        accepted_root_path=root_discovery_path,
    )
    discovery_path = effective["path"]

    matrix_path = source_root / "candidate-matrix-v2.json"
    selection_path = source_root / "candidate-selection-v2.json"
    matrix = core.load_json(matrix_path)
    matrix_by_discovery = {row["discovery_ids"][0]: row for row in matrix["rows"]}
    interactive = core.load_json(INPUT)

    # Selection identity check: input assignments must reproduce the bound Selection bytes.
    sel = core.load_json(selection_path)
    assert len(interactive["assignments"]) == len(sel["assignments"]) == 111
    sel_by_cid = {a["candidate_id"]: a for a in sel["assignments"]}
    for row in interactive["assignments"]:
        cid = matrix_by_discovery[row["discovery_id"]]["candidate_id"]
        s = sel_by_cid[cid]
        assert (row["disposition"], row["architecture_usage"], row["rationale"],
                row["publication_role"], row["architecture_role"]) == (
                s["disposition"], s["architecture_usage"], s["rationale"],
                s["publication_role"], s["architecture_role"]), row["discovery_id"]
    print("Selection identity: 111/111 assignments match bound Selection bytes")

    candidate_id = {did: row["candidate_id"] for did, row in matrix_by_discovery.items()}
    plan_input = interactive["architecture"]
    packages = []
    for src in plan_input["packages"]:
        primary_ids = [candidate_id[x] for x in src["primary_discovery_ids"]]
        supporting_ids = [candidate_id[x] for x in src["supporting_discovery_ids"]]
        inherited = [b for cid in [*primary_ids, *supporting_ids]
                     for b in next(r for r in matrix["rows"] if r["candidate_id"] == cid)["remaining_boundaries"]]
        packages.append({
            "package_id": src["package_id"], "title": src["title"], "purpose": src["purpose"],
            "primary_candidate_ids": primary_ids, "supporting_candidate_ids": supporting_ids,
            "must_cover_requirements": list(src["must_cover_requirements"]),
            "boundaries": list(dict.fromkeys([*src["boundaries"], *inherited])),
            "drafting_order": src["drafting_order"],
            "profile_extensions": src["profile_extensions"],
            "publication_extensions": src["publication_extensions"],
        })
    proposed = {
        "schema_version": "2.0-rc1", "issue_id": state["issue_id"],
        "research_profile": profile["research_profile"],
        "publication_profile": profile["publication_profile"], "status": "PROPOSED",
        "basis": {
            "production_profile_sha256": core.sha256_file(profile_path),
            "profile_completeness_sha256": core.sha256_file(completeness_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "candidate_selection_sha256": core.sha256_file(selection_path),
        },
        "editorial_thesis": plan_input["editorial_thesis"],
        "architecture_goals": list(plan_input["architecture_goals"]),
        "page_plan": dict(plan_input["page_plan"]),
        "packages": packages, "selected_exceptions": [],
        "profile_extensions": plan_input["profile_extensions"],
        "publication_extensions": plan_input["publication_extensions"],
        "human_review": {"reviewed_by": None, "reviewed_at": None, "review_reference": None},
    }
    schema_gate.validate_instance(proposed, REPO / architecture.ARCHITECTURE_SCHEMA, label="Issue Architecture")
    errors = architecture.validate_architecture(
        REPO, proposed, profile_path, completeness_path, ledger_path,
        matrix_path, selection_path, require_approved=False)
    if errors:
        raise SystemExit("Issue Architecture invalid: " + "; ".join(errors))
    core.write_json(source_root / "architecture-v2.json", proposed)
    print("architecture-v2.json written")

    with agent_tool.current_stage_basis_override():
        review = architecture.build_architecture_review_summary(
            REPO, profile_path, discovery_path, screening_path, evidence_path, views_path,
            ledger_path, completeness_path, matrix_path, selection_path,
            source_root / "architecture-v2.json", implementation_sha)
    if review.get("readiness", {}).get("status") != "READY_FOR_ARCHITECTURE_REVIEW":
        raise SystemExit("summary BLOCKED: " + "; ".join(review.get("readiness", {}).get("errors", [])))
    schema_gate.validate_instance(review, REPO / architecture.REVIEW_SCHEMA, label="Architecture Review Summary")
    core.write_json(source_root / "architecture-review-summary-v2.json", review)
    review_attention.build_attention(REPO, screening_path, ledger_path, selection_path,
                                     source_root / "architecture-review-attention-v2.json")
    review_attention.validate_attention(REPO, source_root / "architecture-review-attention-v2.json")
    print("summary + attention written; readiness:", review["readiness"]["status"])

    shutil.copy2(INPUT, R2DIR / "interactive-architecture-r2.archived.json")
    print("done")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
