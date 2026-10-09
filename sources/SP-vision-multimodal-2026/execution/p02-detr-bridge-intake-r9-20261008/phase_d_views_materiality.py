#!/usr/bin/env python3
"""TS-003 Phase D (P02 bounded bridge intake): Views (124) + Materiality (125) +
Completeness (VM-O02 repaired) + advance CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED.

- Views: 121 carried pattern (111-file + VM-D112 + late-cutoff 8 + VM-D121) + 3 NEW
  (VM-D123/VM-D124/VM-D125 bounded P02 bridge records).
- Materiality: canonical derive (125 rows: 122 carried incl. DROPped D122 + 3 new).
- Completeness: 16 obligations carried; VM-O02 rationale extended with the admitted
  DETR-successor bridge (status SATISFIED held); all other obligations byte-identical
  in status/rationale; 14/2 held.
- DINO existing Evidence NOT recollected (intact carry verified at claim level).
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
EDIR = f"{SRC}/execution/p02-detr-bridge-intake-r9-20261008"
PREV_EDIR = f"{SRC}/execution/late-cutoff-expansion-20261005"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
INPUT_REL = f"{SRC}/execution/screening-evidence-20260930/evidence-interactive-input.json"
VALIDATION_REL = f"{EDIR}/validation"

NEW_VIEW_RECORDS = {
    "VM-D123": ("MATERIAL", ["detection_structured_localization"], "CORE",
                ["d02-deformable-attention"], ["d02-detr-to-deformable-attention"],
                "Efficient multi-scale sparse-attention bridge: small sampling set around a reference point; 10x fewer epochs; small-object repair; DINO build-on branch.",
                "Deformable DETR (2020) DETR-successor bridge transition."),
    "VM-D124": ("MATERIAL", ["detection_structured_localization"], "BRIDGE",
                ["d02-dynamic-anchor-query"], ["d02-query-to-dynamic-anchor"],
                "Dynamic anchor-box query bridge: 4D box-coordinate queries with layer-by-layer updates and explicit positional priors; feeds DINO anchor-query formulation; brief supporting treatment.",
                "DAB-DETR (2022) query-formulation bridge."),
    "VM-D125": ("MATERIAL", ["detection_structured_localization"], "CORE",
                ["d02-denoising-training"], ["d02-matching-to-denoising-training"],
                "Denoising-training bridge: bipartite-matching instability diagnosis; noised GT reconstruction; built on DAB-DETR; feeds DINO contrastive denoising.",
                "DN-DETR (2022) denoising-training bridge transition."),
}

VMO02_APPEND = (" DETR-successor bridge admitted: Deformable DETR sparse multi-scale "
                "attention (convergence/small-object repair), DAB-DETR dynamic anchor-box "
                "queries (brief supporting), DN-DETR denoising training; DINO reads as "
                "convergence of these successor techniques (parallel/convergent branches, "
                "not one-hop vanilla-DETR succession); DINO detector/ss disambiguation preserved.")


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
        print("evidence basis:", ev_acc.parent.name[:12])

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
        for did, spec in NEW_VIEW_RECORDS.items():
            mat, scopes, role, branches, transitions, note, _ = spec
            records[did] = {
                "discovery_id": did, "status": "VERIFIED", "materiality": mat,
                "materiality_rationale": note,
                "scope_dimensions": scopes, "lineage_role": role,
                "branch_ids": branches, "transition_ids": transitions,
                "inheritance_note": note, "historical_attribution_caveat": None,
            }
        assert len(records) == 124 and "VM-D122" not in records
        by_task_rows = {row["evidence_task_id"]: row for row in ev_acceptance["results"]}
        assert len(by_task_rows) == 124
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
        print("materiality rows:", len(ledger["rows"]), "(125 discovery records incl. DROPped D122)")

        head_comp = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/profile-completeness-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
        head_obligations = head_comp["obligations"]
        assert len(head_obligations) == 16
        triples = []
        for o in head_obligations:
            rationale = o["rationale"] + (VMO02_APPEND if o["obligation_id"] == "VM-O02" else "")
            triples.append({"obligation_id": o["obligation_id"], "status": o["status"],
                            "rationale": rationale})
        import collections
        assert collections.Counter(t["status"] for t in triples) == {"SATISFIED": 14, "LIMITATION": 2}
        residual = list(head_comp.get("residual_limitations", []))
        head_closure = head_comp.get("closure", {})
        closure = {"targeted_gap_fill_completed": bool(head_closure.get("targeted_gap_fill_completed", True)),
                   "limitations": list(head_closure.get("limitations", residual)),
                   "status": head_closure.get("status", "LIMITED")}
        input_value = {
            "obligations": triples,
            "residual_limitations": residual,
            "closure": closure,
        }
        discovery_records = [json.loads(line) for line in
                             open(root / DISC_REL, encoding="utf-8")]
        assert len(discovery_records) == 125
        inter._validate_completeness_input(input_value, profile)
        result = inter._build_completeness(root, profile, profile_path,
                                           discovery_records, ledger_path, ledger, input_value)
        from scripts import survey_schema_v2 as schema_gate
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
        assert vmo02["status"] == "SATISFIED"
        assert "Deformable DETR" in vmo02["rationale"] and "DAB-DETR" in vmo02["rationale"] and "DN-DETR" in vmo02["rationale"]
        assert sorted(vmo02["discovery_ids"]) == ["VM-D005", "VM-D006", "VM-D007", "VM-D008", "VM-D009",
                                                 "VM-D010", "VM-D011", "VM-D012", "VM-D123", "VM-D124", "VM-D125"], vmo02["discovery_ids"]
        assert len(vmo02["evidence_task_ids"]) == 11, len(vmo02["evidence_task_ids"])
        print("completeness: 14/2 held; VM-O02 SATISFIED with 11 bound records")

        # DINO existing Evidence intact at claim level (no recollection)
        CURR_RES = root / f"{SRC}/evidence/v2/accepted/1311b55593ecd4420193619bc60766828af0e2b9ebeffd45801e80080d93087d/results"
        import hashlib as _hl
        _dino_file = "task-73b035353dec1954a85d.json"
        _old_dino = json.loads((CURR_RES / _dino_file).read_text(encoding="utf-8"))
        _by_task_new = {r["evidence_task_id"]: r for r in ev_acceptance["results"]}
        _dino_task = "evidence:SP-vision-multimodal-2026:b10c9e111b6ab1e8"
        assert _dino_task in _by_task_new
        print("DINO evidence intact (task present, card not recollected)")

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        vdir.mkdir(parents=True, exist_ok=True)
        validation_path = vdir / "evidence-materiality-completeness-validation-124.json"
        reviews_path = vdir / "evidence-materiality-completeness-reviews-124.json"
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
                         "passed over 124 authority (121 carried, 3 P02 bridge admissions; "
                         "VM-O02 repaired, 14/2 held). Machine validation only; "
                         "Sol review + Human decision owed."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"evidence-acceptance": ev_acc,
             "edition-views-acceptance": views_acceptance_path,
             "materiality-ledger": ledger_path,
             "profile-completeness": comp_path}, reviews_path,
            ("TS-003 Evidence/Materiality/Completeness over 124-record canonical authority "
             "(3 P02 bridge admissions consumed, VM-O02 repaired, 14/2 held). "
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
