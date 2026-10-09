#!/usr/bin/env python3
"""Edition-local bounded Draft revision regenerator for TS-003 (DRAFT_COMPLETE).

Mirrors scripts/run_drafting_synthesis_v2_interactive.py EXCEPT its
ARCHITECTURE_ESTABLISHED lifecycle precondition, which cannot hold for a
bounded revision whose lifecycle correctly remains DRAFT_COMPLETE with an
approved Architecture. Everything else is identical:

- upstream path resolution (checkpoint-bound evidence/views, screening path
  from architecture-review-attention, approval from state provenance);
- canonical drafting.derive_draft_package per package;
- identical _draft_result construction (refs/attribution/boundary block);
- identical canonical validation (validate_draft_result,
  build_synthesis_input derivation match, validate_synthesis_result).

Lifecycle gate bypass is the ONLY deviation, recorded in
execution/bounded-revision-112-20261004/. No TeX/PDF/candidate/advance.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as runtime_tool
from scripts import survey_drafting_v2 as drafting
from scripts import survey_production_v2 as core
import scripts.run_drafting_synthesis_v2_interactive as runner


def _load(path: Path):
    return core.load_json(path)


def _upstream_bounded(root: Path, state_path: Path) -> dict[str, Path]:
    state = _load(state_path)
    if state.get("human_gates", {}).get("architecture_review") != "approved":
        raise ValueError("bounded revision requires approved Architecture Review")
    cfg = _load(root / core.DEFAULT_CONFIG)
    state_errors = agent.validate_agent_state(root, cfg, state)
    # NOTE: DRAFT_COMPLETE state carries the draft checkpoint whose artifacts
    # are exactly what this script regenerates; that checkpoint is rebuilt
    # afterwards, so a pre-regeneration drift report (if any) is informational.
    if state_errors:
        print("pre-regeneration state notes (informational):", file=sys.stderr)
        for err in state_errors:
            print(" -", err, file=sys.stderr)
    profile_path = root / state["profile"]["path"]
    profile = _load(profile_path)
    source_root = root / profile["paths"]["source_root"]
    discovery_acceptance = source_root / "discovery/discovery-accepted-v2.json"
    accepted = _load(discovery_acceptance)
    raw_discovery = accepted.get("discovery_path")
    discovery_path = (root / raw_discovery).resolve()
    matrix_path = source_root / "candidate-matrix-v2.json"
    matrix = _load(matrix_path)
    # Checkpoint-bound evidence/views WITHOUT the state-validity gate (which
    # is circular mid-revision: the draft files being regenerated are
    # themselves checkpoint artifacts). Authority is still the canonical
    # CANDIDATES_NORMALIZED checkpoint record, read directly.
    norm_path = source_root / "orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json"
    norm = _load(norm_path)
    by_name = {row["name"]: row for row in norm.get("artifacts", [])}
    evidence_path = (root / by_name["evidence-acceptance"]["path"]).resolve()
    views_path = (root / by_name["edition-views-acceptance"]["path"]).resolve()
    if matrix.get("basis", {}).get("evidence_acceptance_sha256") != core.sha256_file(evidence_path):
        raise ValueError("Candidate Matrix does not bind checkpoint-bound Evidence acceptance")
    if matrix.get("basis", {}).get("edition_views_acceptance_sha256") != core.sha256_file(views_path):
        raise ValueError("Candidate Matrix does not bind checkpoint-bound Edition Views acceptance")
    approval_ref = state.get("human_gate_provenance", {}).get("architecture_review")
    approval_path = root / approval_ref["path"]
    attention = _load(source_root / "architecture-review-attention-v2.json")
    raw = attention.get("basis", {}).get("screening_acceptance_path")
    screening_path = (root / raw).resolve()
    return {
        "state": state_path,
        "profile": profile_path,
        "source_root": source_root,
        "discovery": discovery_path,
        "screening": screening_path,
        "evidence": evidence_path,
        "views": views_path,
        "ledger": source_root / "materiality-ledger-v2.json",
        "completeness": source_root / "profile-completeness-v2.json",
        "matrix": matrix_path,
        "selection": source_root / "candidate-selection-v2.json",
        "architecture": source_root / "architecture-v2.json",
        "review": source_root / "architecture-review-summary-v2.json",
        "approval": approval_path,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--state", required=True)
    ap.add_argument("--input", required=True)
    args = ap.parse_args()
    root = Path(args.repo_root).resolve()
    state_path = (root / args.state).resolve()
    input_path = (root / args.input).resolve()
    data = _load(input_path)
    up = _upstream_bounded(root, state_path)
    state = _load(state_path)
    if data.get("schema_version") != "2.0-rc1" or data.get("issue_id") != state["issue_id"]:
        raise SystemExit("interactive Drafting input identity mismatch")
    if set(data) != {"schema_version", "issue_id", "draft_version", "runner", "packages", "synthesis"}:
        raise SystemExit("interactive Drafting input envelope invalid")
    plan = _load(up["architecture"])
    specs = data["packages"]
    if {row["package_id"] for row in specs} != {row["package_id"] for row in plan["packages"]}:
        raise SystemExit("interactive Drafting must cover every Architecture package exactly once")
    spec_by_id = {row["package_id"]: row for row in specs}
    # Also accept ref_mode per block (runner default CLAIMS)
    draft_root = up["source_root"] / "draft/v2"
    pairs = []
    outputs = []
    implementation_sha = core.repository_commit_sha(root)
    # Same reviewed historical-basis semantics as the canonical agent runner
    # (run_drafting_synthesis_v2_agent.current_stage_basis_override): accepted
    # Screening/Evidence packages retain their creation-stage State SHA.
    with runtime_tool.current_stage_basis_override():
        _generate_all(root, state, data, up, plan, spec_by_id, draft_root, implementation_sha)
    print(json.dumps({"regenerated": len(spec_by_id)}, ensure_ascii=False, indent=2))
    return 0


def _generate_all(root, state, data, up, plan, spec_by_id, draft_root, implementation_sha):
    pairs = []
    outputs = []
    ordered = sorted(plan["packages"], key=lambda r: (r["drafting_order"], r["package_id"]))
    # Phase 1 (read-only vs draft outputs): derive every package while the
    # committed draft files are still intact, so the state-validity gate
    # inside derivation sees no drift. Nothing is written here.
    derived = {}
    for plan_row in ordered:
        pid = plan_row["package_id"]
        spec = spec_by_id[pid]
        if set(spec) != {"package_id", "headline", "deck", "deck_discovery_ids", "blocks"}:
            raise SystemExit(f"interactive package fields invalid: {pid}")
        derived[pid] = drafting.derive_draft_package(
            root, up["profile"], up["discovery"], up["screening"], up["evidence"],
            up["views"], up["ledger"], up["completeness"], up["matrix"], up["selection"],
            up["architecture"], up["review"], up["approval"], pid, implementation_sha,
        )
    # Phase 2 (write-only): materialize packages, then results. No state
    # validation runs here; per-result canonical validation still applies.
    for plan_row in ordered:
        pid = plan_row["package_id"]
        spec = spec_by_id[pid]
        package = derived[pid]
        package_dir = draft_root / "packages" / pid
        package_dir.mkdir(parents=True, exist_ok=True)
        package_path = package_dir / "draft-package.json"
        result_path = package_dir / "draft-result.json"
        core.write_json(package_path, package)
        result = runner._draft_result(root, package_path, package, spec, data["runner"], data["draft_version"])
        errors = drafting.validate_draft_result(result, package_path, root / drafting.DRAFT_PROMPT)
        if errors:
            raise SystemExit(f"{pid} Draft Result invalid: " + "; ".join(errors))
        core.write_json(result_path, result)
        pairs.append((package_path, result_path))
        outputs.append({"package_id": pid})
    synthesis_input = drafting.build_synthesis_input(
        root, up["profile"], up["architecture"], up["review"], up["approval"], pairs
    )
    synthesis_input_path = draft_root / "profile-synthesis-input.json"
    synthesis_result_path = draft_root / "profile-synthesis-result.json"
    core.write_json(synthesis_input_path, synthesis_input)
    syn = data["synthesis"]
    if set(syn) != {"profile_payload", "publication_payload"}:
        raise SystemExit("interactive synthesis fields invalid")
    synthesis_result = {
        "schema_version": "2.0-rc1", "issue_id": state["issue_id"],
        "research_profile": state["research_profile"], "publication_profile": state["publication_profile"],
        "synthesis_version": "v1.0", "status": "ESTABLISHED",
        "basis": {"synthesis_input_sha256": core.sha256_file(synthesis_input_path),
                  "prompt_id": "profile-synthesis-v2",
                  "prompt_sha256": core.sha256_file(root / drafting.SYNTHESIS_PROMPT)},
        "runner": data["runner"], "profile_payload": syn["profile_payload"],
        "publication_payload": syn["publication_payload"],
    }
    errors = drafting.validate_synthesis_result(
        synthesis_result, synthesis_input_path, root / drafting.SYNTHESIS_PROMPT
    )
    if errors:
        raise SystemExit("Profile Synthesis Result invalid: " + "; ".join(errors))
    core.write_json(synthesis_result_path, synthesis_result)
    archive = draft_root / "interactive-drafting-synthesis-input.json"
    core.write_json(archive, data)
    print(json.dumps({"packages": outputs, "regenerated": len(outputs)}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
