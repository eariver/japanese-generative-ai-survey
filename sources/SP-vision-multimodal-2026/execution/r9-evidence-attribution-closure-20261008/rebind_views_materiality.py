#!/usr/bin/env python3
"""TS-003 r9 attribution closure: Views (124) + Materiality (125) + Completeness
(16 carried) + advance CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED.

- Views: 124 rebuilt from carried authority input records (111-file + VM-D112 +
  late-cutoff 8 + VM-D121 + 3 P02 bridge records); evidence SHAs rebound.
- Materiality: canonical derive (125 rows).
- Completeness: 16 obligations carried byte-identical (VM-O02 rationale already
  names the bridge; 14/2 held).
- Stage validation + checkpoint + advance. Frozen Core only.
"""
from __future__ import annotations

import json
import subprocess
import tempfile
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_completeness_v2 as completeness_mod
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import run_evidence_v2_interactive as inter
from scripts import survey_schema_v2 as schema_gate
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/r9-evidence-attribution-closure-20261008"
PREV_EDIR = f"{SRC}/execution/late-cutoff-expansion-20261005"
R9_EDIR = f"{SRC}/execution/p02-detr-bridge-intake-r9-20261008"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
INPUT_REL = f"{SRC}/execution/screening-evidence-20260930/evidence-interactive-input.json"
VALIDATION_REL = f"{EDIR}/validation"


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("expected canonical State at CANDIDATES_NORMALIZED")
    impl = core.repository_commit_sha(root)
    profile_path = root / PROFILE_REL
    profile = core.load_json(profile_path)

    with agent_tool.current_stage_basis_override():
        ev_acc = max((root / SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                     key=lambda p: p.stat().st_mtime)
        ev_acceptance = core.load_json(ev_acc)
        assert ev_acceptance["result_count"] == 124, ev_acceptance["result_count"]
        assert ev_acc.parent.name != "2b1f2463179a276c2502af19c6964c4fba33c0c7f28ce219a53a269d247fd053"
        print("evidence basis:", ev_acc.parent.name[:12])

        import importlib.util as _ilu
        _spec_a = _ilu.spec_from_file_location(
            "pd_latecutoff", str(root / PREV_EDIR / "phase_d_views_materiality.py"))
        _pd = _ilu.module_from_spec(_spec_a)
        _spec_a.loader.exec_module(_pd)
        _spec_b = _ilu.spec_from_file_location(
            "pd_bridge", str(root / R9_EDIR / "phase_d_views_materiality.py"))
        _pd9 = _ilu.module_from_spec(_spec_b)
        _spec_b.loader.exec_module(_pd9)
        doc = core.load_json(root / INPUT_REL)
        records = {r["discovery_id"]: r for r in
                   (doc["records"] if isinstance(doc, dict) else doc)}
        assert len(records) == 111 and "VM-D112" not in records
        records["VM-D112"] = dict(_pd.VM112_VIEW_RECORD)
        for did, spec in _pd.NEW_VIEW_RECORDS.items():
            mat, scopes, role, branches, transitions, note, _ = spec
            records[did] = {
                "discovery_id": did, "status": "VERIFIED", "materiality": mat,
                "materiality_rationale": note,
                "scope_dimensions": scopes, "lineage_role": role,
                "branch_ids": branches, "transition_ids": transitions,
                "inheritance_note": note, "historical_attribution_caveat": None,
            }
        records["VM-D121"] = {
            "discovery_id": "VM-D121", "status": "VERIFIED", "materiality": "MATERIAL",
            "materiality_rationale": ("Action-conditioned latent planning extending the JEPA "
                                      "predictive pole; intra-pole transition, not a new taxonomy."),
            "scope_dimensions": ["predictive_world_models"], "lineage_role": "CORE",
            "branch_ids": ["d14-jepa-action-conditioning"],
            "transition_ids": ["d14-actionfree-to-action-conditioned"],
            "inheritance_note": ("Action-free JEPA pretraining plus action-conditioned latent "
                                 "world-model post-training with MPC planning use."),
            "historical_attribution_caveat": None,
        }
        for did, spec in _pd9.NEW_VIEW_RECORDS.items():
            mat, scopes, role, branches, transitions, note, _ = spec
            records[did] = {
                "discovery_id": did, "status": "VERIFIED", "materiality": mat,
                "materiality_rationale": note,
                "scope_dimensions": scopes, "lineage_role": role,
                "branch_ids": branches, "transition_ids": transitions,
                "inheritance_note": note, "historical_attribution_caveat": None,
            }
        assert len(records) == 124 and "VM-D122" not in records
        with tempfile.TemporaryDirectory() as temp:
            views_dir = Path(temp) / "views"
            views_dir.mkdir()
            for row in ev_acceptance["results"]:
                task_id = row["evidence_task_id"]
                did = row["discovery_ids"][0]
                view = inter._build_view(profile, task_id, row["sha256"], records[did])
                errs = evidence.validate_edition_view(
                    view, profile, row["sha256"], row["status"])
                if errs:
                    raise ValueError(f"View {task_id} invalid: {'; '.join(errs)}")
                core.write_json(views_dir / evidence.view_filename(task_id), view)
            source_root = core.repo_local_path(
                root, profile["paths"]["source_root"], "paths.source_root")
            views_acceptance_path = evidence.accept_edition_views(
                root, profile_path, ev_acc, views_dir,
                source_root / "evidence/v2/views/accepted", impl)
            evidence.validate_edition_views_acceptance(
                root, profile_path, ev_acc, views_acceptance_path, impl)
        print("views acceptance:", views_acceptance_path.relative_to(root))

        curr_pkg = core.load_json(ev_acc.parent / "package.json")
        scr_acc = root / curr_pkg["basis"]["screening_acceptance_path"]
        assert scr_acc.is_file(), scr_acc
        ledger_path = root / f"{SRC}/materiality-ledger-v2.json"
        assert not ledger_path.exists(), "canonical ledger should have been invalidated"
        ledger = evidence.build_materiality_ledger(
            root, profile_path, root / DISC_REL, scr_acc, ev_acc,
            views_acceptance_path, impl)
        core.write_json(ledger_path, ledger)
        evidence.validate_materiality_ledger(
            ledger, root, profile_path, root / DISC_REL, scr_acc,
            ev_acc, views_acceptance_path, impl)
        assert len(ledger["rows"]) == 125, len(ledger["rows"])
        print("materiality rows:", len(ledger["rows"]))

        head_comp = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/profile-completeness-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
        head_obligations = head_comp["obligations"]
        assert len(head_obligations) == 16
        triples = [{"obligation_id": o["obligation_id"], "status": o["status"],
                    "rationale": o["rationale"]} for o in head_obligations]
        import collections
        assert collections.Counter(t["status"] for t in triples) == {"SATISFIED": 14, "LIMITATION": 2}
        residual = list(head_comp.get("residual_limitations", []))
        head_closure = head_comp.get("closure", {})
        closure = {"targeted_gap_fill_completed": bool(head_closure.get("targeted_gap_fill_completed", True)),
                   "limitations": list(head_closure.get("limitations", residual)),
                   "status": head_closure.get("status", "LIMITED")}
        input_value = {"obligations": triples, "residual_limitations": residual, "closure": closure}
        discovery_records = [json.loads(line) for line in open(root / DISC_REL, encoding="utf-8")]
        assert len(discovery_records) == 125
        inter._validate_completeness_input(input_value, profile)
        result = inter._build_completeness(root, profile, profile_path,
                                           discovery_records, ledger_path, ledger, input_value)
        schema_gate.validate_instance(
            result, root / "schemas/profile-completeness-result.schema.json",
            label="Profile Completeness")
        comp_path = root / f"{SRC}/profile-completeness-v2.json"
        assert not comp_path.exists(), "canonical completeness should have been invalidated"
        core.write_json(comp_path, result)
        errs = completeness_mod.validate_profile_completeness(
            result, root, profile_path, root / DISC_REL, scr_acc,
            ev_acc, views_acceptance_path, ledger_path, impl)
        assert not errs, errs[:3]
        assert collections.Counter(o["status"] for o in result["obligations"]) == {"SATISFIED": 14, "LIMITATION": 2}
        vmo02 = next(o for o in result["obligations"] if o["obligation_id"] == "VM-O02")
        assert vmo02["status"] == "SATISFIED" and len(vmo02["discovery_ids"]) == 11
        print("completeness: 14/2 held; VM-O02 SATISFIED")

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "evidence-materiality-completeness-validation-124b.json"
        reviews_path = vdir / "evidence-materiality-completeness-reviews-124b.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"evidence-acceptance": ev_acc,
             "edition-views-acceptance": views_acceptance_path,
             "materiality-ledger": ledger_path,
             "profile-completeness": comp_path},
            validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Combined Evidence/Materiality/Completeness stage-contract validation "
                         "passed over corrected 124 authority (4 cards corrected, VM-O02 held, "
                         "14/2 held). Machine validation only; Sol review + Human decision owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"evidence-acceptance": ev_acc,
             "edition-views-acceptance": views_acceptance_path,
             "materiality-ledger": ledger_path,
             "profile-completeness": comp_path}, reviews_path,
            ("TS-003 Evidence/Materiality/Completeness rebound over corrected 124-record "
             "canonical authority (attribution repair, VM-O02 held, 14/2 held). "
             "Proceed to Selection; Sol review owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "EVIDENCE_REVIEWED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
