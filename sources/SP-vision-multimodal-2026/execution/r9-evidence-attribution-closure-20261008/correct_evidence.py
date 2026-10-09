#!/usr/bin/env python3
"""TS-003 r9 attribution closure: Evidence correction (124) at CANDIDATES_NORMALIZED.

- Canonical prepare_evidence_package over unchanged Discovery (125) + Screening
  (125) + carried union-125 authority supplement.
- Determinism: 124/124 re-prepared task SHAs must equal the accepted 2b1f2463
  package task SHAs (no intake since).
- Cards: 120 carried byte-identical + 4 corrected (canonical-validated here):
  VM-D011 +1 source-local AUTHOR_CLAIM (DINO-authored predecessor lineage);
  VM-D123 claim-3 rewritten to Deformable-native only;
  VM-D124 claim-3 removed (DAB-native claims 1-2 kept);
  VM-D125 claim-3 removed (DN-native claims 1-2 kept).
- Canonical accept_evidence_results (append-only). Frozen Core only. No advance here.
"""
from __future__ import annotations

import copy
import json
import tempfile
from pathlib import Path

from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/r9-evidence-attribution-closure-20261008"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/evidence-package-124b"
SUPPLEMENT = f"{SRC}/execution/p02-detr-bridge-intake-r9-20261008/evidence-authority-supplement-union-125.json"
CURR = "2b1f2463179a276c2502af19c6964c4fba33c0c7f28ce219a53a269d247fd053"
CURR_RES = f"{SRC}/evidence/v2/accepted/{CURR}/results"

D011_TASK = "evidence:SP-vision-multimodal-2026:b10c9e111b6ab1e8"
D123_TASK = "evidence:SP-vision-multimodal-2026:a04ef197904a57c0"
D124_TASK = "evidence:SP-vision-multimodal-2026:43c5bc5adec4ac9a"
D125_TASK = "evidence:SP-vision-multimodal-2026:796e6c3c2cac7f26"
CORRECTED_TASKS = {D011_TASK, D123_TASK, D124_TASK, D125_TASK}

DINO_CLAIM3_TEXT = ("DINO design lineage as paper-stated: new DETR-like model based on DN-DETR, "
                    "DAB-DETR, and Deformable DETR; decoder queries as dynamic anchor boxes refined "
                    "step-by-step across decoder layers (DAB line); denoising training improved to "
                    "contrastive denoising (DN line); deformable attention adopted for computational "
                    "efficiency with query-selection inheritance for positional-query initialization "
                    "(Deformable line); contrastive denoising, mixed query selection, and "
                    "look-forward-twice box prediction are DINO's own improvements.")
DINO_CLAIM3_CTX = ("DINO paper abstract/§§1/3 (based-on DN/DAB/Deformable statement; dynamic anchor "
                   "boxes; contrastive denoising; mixed query selection; look-forward-twice).")

D123_CLAIM3_TEXT = ("Reference-point/query machinery native to Deformable DETR: 2D reference points "
                    "as queries, two-stage query-selection variant selecting top-K encoder features "
                    "as priors, and iterative box refinement.")
D123_CLAIM3_CTX = ("Paper §4 (reference-point formulation, two-stage variant, iterative refinement); "
                   "no later-paper lineage asserted here.")


def _fix_d011(card: dict) -> dict:
    card = copy.deepcopy(card)
    assert [c["statement_id"] for c in card["claims"]] == ["claim-1", "claim-2"], "D011 base drift"
    assert len(DINO_CLAIM3_TEXT) <= 600, len(DINO_CLAIM3_TEXT)
    card["claims"] = [*card["claims"], {
        "statement_id": "claim-3", "text": DINO_CLAIM3_TEXT,
        "subject_id": "ev-vmd011", "subject_role": "PRIMARY_SUBJECT",
        "evidence_class": "AUTHOR_CLAIM", "source_ids": ["src-1"],
        "context": DINO_CLAIM3_CTX}]
    return card


def _fix_d123(card: dict) -> dict:
    card = copy.deepcopy(card)
    assert [c["statement_id"] for c in card["claims"]] == ["claim-1", "claim-2", "claim-3"], "D123 base drift"
    assert len(D123_CLAIM3_TEXT) <= 600, len(D123_CLAIM3_TEXT)
    claims = [c for c in card["claims"] if c["statement_id"] in ("claim-1", "claim-2")]
    claims.append({"statement_id": "claim-3", "text": D123_CLAIM3_TEXT,
                   "subject_id": "ev-vmd123", "subject_role": "PRIMARY_SUBJECT",
                   "evidence_class": "AUTHOR_CLAIM", "source_ids": ["src-1"],
                   "context": D123_CLAIM3_CTX})
    card["claims"] = claims
    return card


def _drop_claim3(card: dict, did: str, keep: int) -> dict:
    card = copy.deepcopy(card)
    assert [c["statement_id"] for c in card["claims"]] == ["claim-1", "claim-2", "claim-3"], f"{did} base drift"
    card["claims"] = [c for c in card["claims"] if c["statement_id"] != "claim-3"]
    assert len(card["claims"]) == keep, did
    return card


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("expected canonical State at CANDIDATES_NORMALIZED")
    impl = core.repository_commit_sha(root)

    with agent_tool.current_stage_basis_override():
        scr_acc_path = max((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"),
                           key=lambda p: p.stat().st_mtime)
        scr_acc = core.load_json(scr_acc_path)
        assert scr_acc["record_count"] == 125, scr_acc["record_count"]
        print("screening basis:", scr_acc_path.parent.name[:12])

        source_root = core.repo_local_path(
            root, core.load_json(root / core.load_json(root / STATE_REL)["profile"]["path"])["paths"]["source_root"],
            "paths.source_root")
        supplement_path = root / SUPPLEMENT
        evidence.validate_evidence_authority_supplement(
            root, supplement_path, impl, expected_issue_id=ISSUE_ID,
            expected_discovery_path=root / DISC_REL,
            expected_screening_acceptance_path=scr_acc_path)
        print("supplement: carried union-125 (binding scope unchanged)")

        package_path = evidence.prepare_evidence_package(
            root, root / STATE_REL, root / DISC_REL, scr_acc_path,
            root / PKGDIR, impl, supplement_path)
        package = core.load_json(package_path)
        assert len(package["tasks"]) == 124, len(package["tasks"])

        curr_pkg = core.load_json(root / CURR_RES / "../package.json")
        curr_tasks = {m["evidence_task_id"]: m["sha256"] for m in curr_pkg["tasks"]}
        new_tasks = {m["evidence_task_id"]: m["sha256"] for m in package["tasks"]}
        assert set(curr_tasks) == set(new_tasks), "task set drift"
        drift = sorted(t for t in curr_tasks if curr_tasks[t] != new_tasks[t])
        assert drift == [], f"unexpected task SHA drift: {drift}"
        print("package determinism: 124/124 task SHAs identical (no intake since)")

        probe = core.load_json(root / CURR_RES / "task-0202917391a980c0420f.json")
        PROMPT_SHA = probe["basis"]["prompt_sha256"]
        CONTRACT_SHA = probe["basis"]["result_contract_sha256"]

        fixers = {D011_TASK: _fix_d011, D123_TASK: _fix_d123,
                  D124_TASK: lambda c: _drop_claim3(c, "VM-D124", 2),
                  D125_TASK: lambda c: _drop_claim3(c, "VM-D125", 2)}

        with tempfile.TemporaryDirectory() as temp:
            results_dir = Path(temp) / "evidence-results"
            results_dir.mkdir()
            carried, corrected = 0, []
            for meta in package["tasks"]:
                fname = Path(meta["path"]).name
                task = core.load_json(root / PKGDIR / meta["path"])
                if meta["evidence_task_id"] in fixers:
                    base = core.load_json(root / CURR_RES / fname)
                    card = fixers[meta["evidence_task_id"]](base)
                    card["evidence_task_id"] = meta["evidence_task_id"]
                    card["basis"] = {
                        "task_sha256": meta["sha256"],
                        "screening_acceptance_sha256": core.sha256_file(scr_acc_path),
                        "prompt_sha256": PROMPT_SHA,
                        "result_contract_sha256": CONTRACT_SHA,
                    }
                    errs = evidence.validate_evidence_card(
                        card, task, meta["sha256"], package, repo_root=root)
                    assert not errs, (meta["evidence_task_id"], errs)
                    corrected.append(meta["evidence_task_id"])
                else:
                    base = core.load_json(root / CURR_RES / fname)
                    base["basis"]["task_sha256"] = meta["sha256"]
                    base["basis"]["screening_acceptance_sha256"] = core.sha256_file(scr_acc_path)
                    assert base["basis"]["prompt_sha256"] == PROMPT_SHA, meta["evidence_task_id"]
                    assert base["basis"]["result_contract_sha256"] == CONTRACT_SHA
                    errs = evidence.validate_evidence_card(
                        base, task, meta["sha256"], package, repo_root=root)
                    if errs:
                        raise ValueError(f"Card {meta['evidence_task_id']} invalid: {'; '.join(errs)}")
                    card = base
                    carried += 1
                core.write_json(results_dir / fname, card)
            assert carried == 120 and len(corrected) == 4, (carried, corrected)

            evidence_acceptance_path = evidence.accept_evidence_results(
                root, package_path, results_dir, source_root / "evidence/v2/accepted", impl)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, impl)
        assert evidence_acceptance["result_count"] == 124
        statuses = {}
        for r in evidence_acceptance["results"]:
            statuses[r["status"]] = statuses.get(r["status"], 0) + 1
        print("evidence acceptance:", evidence_acceptance_path.relative_to(root))
        print("carried:", carried, "| corrected:", len(corrected), "| statuses:", statuses)
        (root / EDIR / "evidence-replay-report.json").write_text(json.dumps(
            {"acceptance": str(evidence_acceptance_path.relative_to(root)),
             "result_count": 124, "statuses": statuses,
             "carried_byte_identical": carried,
             "corrected": ["VM-D011", "VM-D123", "VM-D124", "VM-D125"]},
            ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("EVIDENCE CORRECTION COMPLETE (advance in next step)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
