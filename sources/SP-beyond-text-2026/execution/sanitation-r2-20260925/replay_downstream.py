#!/usr/bin/env python3
"""TS-002 sanitation downstream replay: ledger/completeness/matrix/selection/
architecture/review/attention + state checkpoints, back to ARCHITECTURE_ESTABLISHED.

Deterministic replay, not a new editorial pass: same decisions, same semantics,
only provenance-state wording sanitation. Prior bytes snapshotted; restored on
failure. Shared Core untouched.
"""

from __future__ import annotations

import importlib.util
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_completeness_v2 as completeness
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_screening_v2 as screening
from scripts import survey_discovery_v2 as discovery
from scripts import run_selection_architecture_v2_interactive as rsel

ISSUE_ID = "SP-beyond-text-2026"
SRC = "sources/SP-beyond-text-2026"
EXEC = f"{SRC}/execution/sanitation-r2-20260925"
SAN = Path(EXEC)


def load_mod(name, rel):
    spec = importlib.util.spec_from_file_location(name, Path(rel))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state_path = root / f"{SRC}/production-state.json"
    state0 = core.load_json(state_path)
    assert state0.get("lifecycle_state") == "ARCHITECTURE_ESTABLISHED", state0.get("lifecycle_state")
    now = datetime.now(timezone.utc)

    # ---- snapshot ----
    snap = root / EXEC / "prior-authority"
    snap.mkdir(parents=True, exist_ok=True)
    snap_files = [f"{SRC}/production-state.json",
                  f"{SRC}/materiality-ledger-v2.json",
                  f"{SRC}/profile-completeness-v2.json",
                  f"{SRC}/candidate-matrix-v2.json",
                  f"{SRC}/candidate-selection-v2.json",
                  f"{SRC}/architecture-v2.json",
                  f"{SRC}/architecture-review-summary-v2.json",
                  f"{SRC}/architecture-review-attention-v2.json",
                  f"{SRC}/orchestration/v2/interactive/selection-architecture-input.json",
                  f"{SRC}/orchestration/v2/interactive/selection-architecture-audit.json"] + [
        f"{SRC}/orchestration/v2/checkpoints/{n}.json" for n in
        ("ISSUE_INITIALIZED", "DISCOVERY_COLLECTED", "CANDIDATES_NORMALIZED",
         "EVIDENCE_REVIEWED", "SELECTION_COMPLETE")]
    for rel in snap_files:
        dst = snap / Path(rel).name
        if not dst.exists():
            shutil.copy2(root / rel, dst)
    # refresh active transition ledger from sanitized copy (snapshot originals first)
    for name in ("transition-ledger.json", "transition-ledger.md"):
        src = root / EXEC / name
        dst = root / f"{SRC}/execution/evidence-semantic-depth-r2/{name}"
        bak = snap / f"r2-{name}"
        if not bak.exists():
            shutil.copy2(dst, bak)
        shutil.copy2(src, dst)

    epid = json.loads((root / EXEC / "evidence-sanitized-build-report.json").read_text(encoding="utf-8"))
    ev_path, vw_path = root / epid["evidence_acceptance"], root / epid["views_acceptance"]
    assert ev_path.is_file() and vw_path.is_file()

    profile_path = root / state0["profile"]["path"]
    profile = core.load_json(profile_path)
    source_root = core.repo_local_path(root, profile["paths"]["source_root"], "paths.source_root")
    impl = core.repository_commit_sha(root)
    active = screening.resolve_active_screening_acceptance(root, state_path, impl)
    screening_path = Path(active["artifact_path"])
    accepted = discovery.validate_acceptance(root, source_root / "discovery/discovery-accepted-v2.json")
    discovery_path = core.repo_local_path(root, accepted["discovery_path"], "accepted Discovery JSONL")

    succeeded = False
    try:
        # ---- 0. rollback fixture to CANDIDATES_NORMALIZED (downstream rebuilt below) ----
        import copy
        state = core.load_json(state_path)
        fix = copy.deepcopy(state)
        fix["lifecycle_state"] = "CANDIDATES_NORMALIZED"
        for name in ("evidence", "materiality", "completeness", "selection", "architecture",
                     "draft", "validation", "publication_preview", "freeze", "release"):
            fix["machine_checkpoints"][name] = "pending"
            fix["checkpoint_provenance"][name] = None
        fix["history"] = [h for h in fix["history"]
                          if not (isinstance(h, dict) and h.get("from") in
                                  ("CANDIDATES_NORMALIZED", "EVIDENCE_REVIEWED", "SELECTION_COMPLETE"))]
        fix = core.refresh_state_control(fix, cfg)
        assert not agent.validate_agent_state(root, cfg, fix)
        core.write_json(state_path, fix)

        # ---- 1. ledger + completeness (unlink + canonical rebuild) ----
        ledger_path, comp_path = source_root / "materiality-ledger-v2.json", source_root / "profile-completeness-v2.json"
        ledger_path.unlink()
        comp_path.unlink()
        with agent_tool.current_stage_basis_override():
            ledger = evidence.build_materiality_ledger(
                root, profile_path, discovery_path, screening_path, ev_path, vw_path, impl)
        evidence.write_materiality_ledger(ledger_path, ledger)
        mod = load_mod("matcomp", root / f"{SRC}/execution/progress-materiality-architecture-20260925/build_materiality_completeness.py")
        discovery_records = [json.loads(l) for l in discovery_path.read_text(encoding="utf-8").splitlines() if l.strip()]
        result = rsel_main = None
        from scripts import run_evidence_v2_interactive as inter
        result = inter._build_completeness(
            root, profile, profile_path, discovery_records, ledger_path, ledger,
            {"obligations": [{"obligation_id": oid, "status": st, "rationale": ra}
                             for oid, st, ra in mod.OBLIGATIONS],
             "residual_limitations": mod.RESIDUAL,
             "closure": {"targeted_gap_fill_completed": True,
                         "limitations": mod.RESIDUAL + mod.CLOSURE_LIMITS, "status": "LIMITED"}})
        schema_gate.validate_instance(result, root / "schemas/profile-completeness-result.schema.json",
                                      label="Profile Completeness")
        with agent_tool.current_stage_basis_override():
            errs = completeness.validate_profile_completeness(
                result, root, profile_path, discovery_path, screening_path,
                ev_path, vw_path, ledger_path, impl)
        assert not errs, errs
        core.write_json(comp_path, result)

        vdir = root / EXEC / "validation"
        vdir.mkdir(parents=True, exist_ok=True)

        # evidence stage
        arts_e = {"evidence-acceptance": ev_path, "edition-views-acceptance": vw_path,
                  "materiality-ledger": ledger_path, "profile-completeness": comp_path}
        v, r = vdir / "evidence-stage-validation-sanitized.json", vdir / "evidence-stage-reviews-sanitized.json"
        for p in (v, r):
            if p.exists():
                raise ValueError(f"refusing to overwrite: {p}")
        from scripts import survey_stage_validation_v2 as sv
        sv.validate_stage(root, cfg, state_path, arts_e, v, now)
        core.write_json(r, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
            "evidence": "Evidence/Materiality/Completeness revalidation passed over sanitized Evidence (139: 126/8/5), Ledger, Completeness LIMITED. Machine validation only.",
            "result_path": str(v.relative_to(root))}]})
        cpev = root / f"{SRC}/orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json"
        cpev.unlink()
        gen = agent.build_stage_checkpoint(
            root, cfg, state_path, arts_e, r,
            "Sanitized Evidence/Materiality/Completeness replay: wording sanitation only, semantics unchanged; re-advance to EVIDENCE_REVIEWED.", now)
        upd = agent.advance_with_checkpoint(root, cfg, state_path, gen)
        assert upd.get("lifecycle_state") == "EVIDENCE_REVIEWED", upd.get("lifecycle_state")

        # ---- 2. matrix/selection/architecture/review/attention (unlink + canonical rerun) ----
        for rel in [f"{SRC}/candidate-matrix-v2.json", f"{SRC}/candidate-selection-v2.json",
                    f"{SRC}/architecture-v2.json", f"{SRC}/architecture-review-summary-v2.json",
                    f"{SRC}/architecture-review-attention-v2.json",
                    f"{SRC}/orchestration/v2/interactive/selection-architecture-input.json",
                    f"{SRC}/orchestration/v2/interactive/selection-architecture-audit.json"]:
            (root / rel).unlink()
        # selection input itself is unchanged; the runner re-archives identical bytes
        out = rsel.run(root, state_path,
                       root / f"{SRC}/execution/progress-materiality-architecture-20260925/interactive-selection-architecture.json")
        assert out["selected_count"] == 134 and out["architecture_package_count"] == 14, out
        assert out["review_readiness"] == "READY_FOR_ARCHITECTURE_REVIEW", out

        # selection stage
        arts_s = {"candidate-matrix": root / f"{SRC}/candidate-matrix-v2.json",
                  "candidate-selection": root / f"{SRC}/candidate-selection-v2.json"}
        v, r = vdir / "selection-stage-validation-sanitized.json", vdir / "selection-stage-reviews-sanitized.json"
        for p in (v, r):
            if p.exists():
                raise ValueError(f"refusing to overwrite: {p}")
        sv.validate_stage(root, cfg, state_path, arts_s, v, now)
        core.write_json(r, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
            "evidence": "Selection revalidation passed: 139 candidates, 134 SELECTED / 5 HOLD. Machine validation only.",
            "result_path": str(v.relative_to(root))}]})
        cpsel = root / f"{SRC}/orchestration/v2/checkpoints/EVIDENCE_REVIEWED.json"
        cpsel.unlink()
        gen = agent.build_stage_checkpoint(
            root, cfg, state_path, arts_s, r,
            "Sanitized Selection replay: decisions unchanged (134/5); re-advance to SELECTION_COMPLETE.", now)
        upd = agent.advance_with_checkpoint(root, cfg, state_path, gen)
        assert upd.get("lifecycle_state") == "SELECTION_COMPLETE", upd.get("lifecycle_state")

        # architecture stage
        arts_a = {"issue-architecture": root / f"{SRC}/architecture-v2.json",
                  "architecture-review-summary": root / f"{SRC}/architecture-review-summary-v2.json",
                  "architecture-review-attention": root / f"{SRC}/architecture-review-attention-v2.json"}
        v, r = vdir / "architecture-stage-validation-sanitized.json", vdir / "architecture-stage-reviews-sanitized.json"
        for p in (v, r):
            if p.exists():
                raise ValueError(f"refusing to overwrite: {p}")
        sv.validate_stage(root, cfg, state_path, arts_a, v, now)
        core.write_json(r, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Survey Production Core v2 survey_stage_validation_v2.py",
            "evidence": "Architecture revalidation passed: 14 packages, page plan 80/96, READY_FOR_ARCHITECTURE_REVIEW. Machine validation only; Human decision pending.",
            "result_path": str(v.relative_to(root))}]})
        cparch = root / f"{SRC}/orchestration/v2/checkpoints/SELECTION_COMPLETE.json"
        cparch.unlink()
        gen = agent.build_stage_checkpoint(
            root, cfg, state_path, arts_a, r,
            "Sanitized Architecture replay: design unchanged; re-advance to ARCHITECTURE_ESTABLISHED for Human R2 review.", now)
        upd = agent.advance_with_checkpoint(root, cfg, state_path, gen)
        assert upd.get("lifecycle_state") == "ARCHITECTURE_ESTABLISHED", upd.get("lifecycle_state")
        assert upd["human_gates"]["architecture_review"] == "pending", upd["human_gates"]
        assert not agent.validate_agent_state(root, cfg, upd)
        core.write_json(vdir / "checkpoint-replay-record.json", {
            "schema_version": "1.0", "issue_id": ISSUE_ID,
            "lifecycle_state": upd["lifecycle_state"], "next_action": upd["next_action"],
            "human_gates": upd["human_gates"]})
        succeeded = True
        print(json.dumps({"lifecycle": upd["lifecycle_state"], "next": upd["next_action"],
                          "gate": upd["human_gates"]["architecture_review"]}, indent=2))
        return 0
    finally:
        if not succeeded:
            for rel in snap_files:
                (root / rel).write_bytes((snap / Path(rel).name).read_bytes())
            for name in ("transition-ledger.json", "transition-ledger.md"):
                (root / f"{SRC}/execution/evidence-semantic-depth-r2/{name}").write_bytes(
                    (snap / f"r2-{name}").read_bytes())


if __name__ == "__main__":
    raise SystemExit(main())
