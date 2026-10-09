#!/usr/bin/env python3
"""TS-003 Phase D (post-freeze integrity): Views (121) + Materiality + Completeness
+ advance CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED.

- Views: 121 rebuilt (view records carried for 120 + D121; D122 dropped with its task).
- Materiality: canonical derive (121 rows).
- Completeness: carried obligations; VM-O15 rationale restored to pre-D122 G02 wording
  (D122-dependent bounding claims removed); G02 residual preserved; VM-O15 LIMITATION.
- SSv2/V1 check; stage validation + checkpoint + advance. Frozen Core only.
"""
from __future__ import annotations

import json
import re
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
EDIR = f"{SRC}/execution/post-freeze-integrity-20261005"
PREV_EDIR = f"{SRC}/execution/late-cutoff-expansion-20261005"
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
        assert ev_acceptance["result_count"] == 121, ev_acceptance["result_count"]
        print("evidence basis:", ev_acc.parent.name[:12])

        # View records: 111-file + VM-D112 record + 8 late-cutoff records + D121.
        # Reuse the late-cutoff phase_d record builders by importing its constants.
        import sys as _sys
        _sys.path.insert(0, str(root / PREV_EDIR))
        import phase_d_views_materiality as _pd
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
        assert len(records) == 121 and "VM-D122" not in records
        by_task_rows = {row["evidence_task_id"]: row for row in ev_acceptance["results"]}
        assert len(by_task_rows) == 121
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

        scr_acc = max((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"),
                      key=lambda p: p.stat().st_mtime)
        ledger = evidence.build_materiality_ledger(
            root, profile_path, root / DISC_REL, scr_acc, ev_acc,
            views_acceptance_path, impl)
        ledger_path = root / f"{SRC}/materiality-ledger-v2.json"
        assert not ledger_path.exists(), "canonical ledger should have been invalidated"
        core.write_json(ledger_path, ledger)
        evidence.validate_materiality_ledger(
            ledger, root, profile_path, root / DISC_REL, scr_acc,
            ev_acc, views_acceptance_path, impl)
        assert len(ledger["rows"]) == 122, len(ledger["rows"])
        _d122 = [r for r in ledger["rows"] if r["discovery_id"] == "VM-D122"]
        assert len(_d122) == 1 and _d122[0]["downstream_disposition"] == "EXCLUDED", _d122
        print("materiality rows:", len(ledger["rows"]))

        # Completeness: HEAD obligations; VM-O15 restored to pre-D122 G02 wording
        # (D122-dependent bounding claims removed); others carried incl. late-cutoff appends.
        head_comp = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/profile-completeness-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
        triples = []
        for o in head_comp["obligations"]:
            r = o["rationale"]
            if o["obligation_id"] == "VM-O15":
                # Restore pre-D122 G02 wording: drop the Planning-Limits methodology-bound
                # clause; keep the V-JEPA 2 intra-pole admission (D121 stays).
                cut = " Planning-Limits cross-backbone range evidence admitted as methodology bound;"
                assert cut in r, r[-200:]
                r = r.replace(cut, "")
            triples.append({"obligation_id": o["obligation_id"], "status": o["status"], "rationale": r})
        assert len(triples) == 16
        o15 = next(t for t in triples if t["obligation_id"] == "VM-O15")
        assert o15["status"] == "LIMITATION" and "Planning-Limits" not in o15["rationale"], o15["rationale"]
        closure_src = head_comp.get("closure", {})
        input_value = {
            "obligations": triples,
            "residual_limitations": list(head_comp.get("residual_limitations", [])),
            "closure": {"targeted_gap_fill_completed": bool(closure_src.get("targeted_gap_fill_completed", True)),
                        "limitations": list(head_comp.get("residual_limitations", [])),
                        "status": closure_src.get("status", "LIMITED")},
        }
        discovery_records = [json.loads(l) for l in
                             open(root / DISC_REL, encoding="utf-8")]
        assert len(discovery_records) == 122
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
        print("completeness:", result["overall_status"])

        blob = ledger_path.read_text(encoding="utf-8") + comp_path.read_text(encoding="utf-8")
        assert "Something-Something V2" not in blob, "V2 entity regression"
        for m in re.finditer(r".{0,40}SSv2.{0,40}", blob):
            assert "Kinetics/SSv2/Ego4D predecessor" in m.group(0), m.group(0)
        print("SSv2 purge: clean")

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "evidence-materiality-completeness-validation-121.json"
        reviews_path = vdir / "evidence-materiality-completeness-reviews-121.json"
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
                         "passed over 121 authority (VM-D122 excluded as OUT_OF_WINDOW). "
                         "Machine validation only."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"evidence-acceptance": ev_acc,
             "edition-views-acceptance": views_acceptance_path,
             "materiality-ledger": ledger_path,
             "profile-completeness": comp_path}, reviews_path,
            ("TS-003 Evidence/Materiality/Completeness replayed over 121-record authority "
             "(VM-D122 OUT_OF_WINDOW exclusion, G02 restored). Proceed to Selection."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "EVIDENCE_REVIEWED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
    print("lifecycle:", updated["lifecycle_state"], "| next:", updated["next_action"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
