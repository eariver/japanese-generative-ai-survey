#!/usr/bin/env python3
"""TS-003 replay step 1 (exception-authorized, run blocker-repair-r5): Evidence (112).

- Union supplement manifest reused read-only from prior run (VM-D112 + VM-D077 entries).
- Cards: 111 carried (deterministic basis rebind) + 1 scoped VM-D075 (staged,
  canonical-validated; basis rebound here).
- Canonical accept_evidence_results (append-only). Frozen Core only.
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
EDIR = f"{SRC}/execution/blocker-repair-r5-20261004"
PREV_EDIR = f"{SRC}/execution/vm-d077-authority-repair-20261004"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/evidence-package-112"
UNION = f"{PREV_EDIR}/evidence-authority-supplement-union-r5.json"
CURR = "8d79dce3a71f97db855474b60aebbd66a3b497914db6fac523097813641e4ced"
CURR_RES = f"{SRC}/evidence/v2/accepted/{CURR}/results"
TID075 = "evidence:SP-vision-multimodal-2026:4b007409a575a02d"


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
        assert core.load_json(scr_acc_path)["record_count"] == 112
        print("screening basis:", scr_acc_path.parent.name[:12])

        source_root = core.repo_local_path(
            root, core.load_json(root / core.load_json(root / STATE_REL)["profile"]["path"])["paths"]["source_root"],
            "paths.source_root")
        union_out = root / UNION
        assert union_out.is_file(), "prior-run union supplement required"
        package_path = evidence.prepare_evidence_package(
            root, root / STATE_REL, root / DISC_REL, scr_acc_path,
            root / PKGDIR, impl, union_out)
        package = core.load_json(package_path)
        assert len(package["tasks"]) == 112, len(package["tasks"])
        probe = core.load_json(root / CURR_RES / "task-0202917391a980c0420f.json")
        PROMPT_SHA = probe["basis"]["prompt_sha256"]
        CONTRACT_SHA = probe["basis"]["result_contract_sha256"]

        staged = core.load_json(root / EDIR / "staged-vm-d075-scoped.json")
        assert staged["evidence_task_id"] == TID075

        with tempfile.TemporaryDirectory() as temp:
            results_dir = Path(temp) / "evidence-results"
            results_dir.mkdir()
            carried, corrected = 0, []
            for meta in package["tasks"]:
                fname = Path(meta["path"]).name
                task = core.load_json(root / PKGDIR / meta["path"])
                if meta["evidence_task_id"] == TID075:
                    import copy as _copy
                    card = _copy.deepcopy(staged)
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
            assert carried == 111 and len(corrected) == 1, (carried, corrected)

            evidence_acceptance_path = evidence.accept_evidence_results(
                root, package_path, results_dir, source_root / "evidence/v2/accepted", impl)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, impl)
        assert evidence_acceptance["result_count"] == 112
        print("evidence acceptance:", evidence_acceptance_path.relative_to(root))
        print("carried:", carried, "| corrected:", len(corrected))
    print("EVIDENCE REPLAY COMPLETE (advance in next step)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
