#!/usr/bin/env python3
"""TS-003 replay step 1 (exception-authorized): Evidence (112) at CANDIDATES_NORMALIZED.

- Canonical prepare_evidence_package over unchanged Discovery (112) + Screening.
- Cards: 104 carried byte-identical from current accepted set 33ec63cb + 8 staged
  corrected cards (canonical-validated already; re-validated here against the fresh
  package basis with deterministic basis rebinding only).
- Canonical accept_evidence_results (append-only new content-addressed set).
- Frozen Core only. No state advance here (phase 2 advances with views/materiality).
"""
from __future__ import annotations

import json
import tempfile
from pathlib import Path

from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/evidence-correction-r5-20261004"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/evidence-package-112"
# VM-D112 supplement sources require the exact Evidence Authority Supplement
# (unchanged r3 authority; Discovery/Screening untouched).
SUPPLEMENT_REL = f"{SRC}/execution/architecture-r3-intake-20261003/evidence-authority-supplement-112.json"
STAGED = f"{EDIR}/staged-cards"
CURR = "33ec63cbd5bbe776fb106f57fa64ca448061dfe92cbbfe3684848ddb17010b69"
CURR_RES = f"{SRC}/evidence/v2/accepted/{CURR}/results"

CORRECTED = {"VM-D062", "VM-D061", "VM-D034", "VM-D033", "VM-D024", "VM-D028", "VM-D108", "VM-D077"}


def _screening_acceptance(root: Path) -> Path:
    cands = [p for p in sorted((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"))
             if core.load_json(p)["record_count"] == 112]
    assert len(cands) == 1, [str(p) for p in cands]
    return cands[0]


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "CANDIDATES_NORMALIZED":
        raise ValueError("expected canonical State at CANDIDATES_NORMALIZED")
    impl = core.repository_commit_sha(root)

    with agent_tool.current_stage_basis_override():
        scr_acc_path = _screening_acceptance(root)
        scr_acc = core.load_json(scr_acc_path)
        assert scr_acc["record_count"] == 112
        print("screening basis:", scr_acc_path.parent.name[:12])

        source_root = core.repo_local_path(
            root, core.load_json(root / core.load_json(root / STATE_REL)["profile"]["path"])["paths"]["source_root"],
            "paths.source_root")
        supplement_path = root / SUPPLEMENT_REL
        evidence.validate_evidence_authority_supplement(
            root, supplement_path, impl, expected_issue_id=ISSUE_ID,
            expected_discovery_path=root / DISC_REL,
            expected_screening_acceptance_path=scr_acc_path)
        package_path = evidence.prepare_evidence_package(
            root, root / STATE_REL, root / DISC_REL, scr_acc_path,
            root / PKGDIR, impl, supplement_path)
        package = core.load_json(package_path)
        assert len(package["tasks"]) == 112, len(package["tasks"])
        probe = core.load_json(root / CURR_RES / "task-0202917391a980c0420f.json")
        PROMPT_SHA = probe["basis"]["prompt_sha256"]
        CONTRACT_SHA = probe["basis"]["result_contract_sha256"]

        staged_by_task = {}
        staged_files = sorted((root / EDIR / "staged-cards").glob("staged-*.json"))
        assert len(staged_files) == 8, [str(p) for p in staged_files]
        for sfile in staged_files:
            card = core.load_json(sfile)
            staged_by_task[card["evidence_task_id"]] = card

        with tempfile.TemporaryDirectory() as temp:
            results_dir = Path(temp) / "evidence-results"
            results_dir.mkdir()
            carried, corrected = 0, []
            for meta in package["tasks"]:
                fname = Path(meta["path"]).name
                task = core.load_json(root / PKGDIR / meta["path"])
                if meta["evidence_task_id"] in staged_by_task:
                    card = copy_card(staged_by_task[meta["evidence_task_id"]])
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
            assert carried == 104 and len(corrected) == 8, (carried, corrected)

            evidence_acceptance_path = evidence.accept_evidence_results(
                root, package_path, results_dir, source_root / "evidence/v2/accepted", impl)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, impl)
        assert evidence_acceptance["result_count"] == 112
        print("evidence acceptance:", evidence_acceptance_path.relative_to(root))
        print("carried:", carried, "| corrected:", len(corrected))
    print("EVIDENCE REPLAY COMPLETE (advance in next step)")
    return 0


def copy_card(card):
    import copy as _copy
    return _copy.deepcopy(card)


if __name__ == "__main__":
    raise SystemExit(main())
