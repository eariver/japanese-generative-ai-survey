#!/usr/bin/env python3
"""TS-003 Phase C (post-freeze integrity): Evidence (121) at CANDIDATES_NORMALIZED.

- Canonical prepare_evidence_package with union-121 supplement (22 entries carried).
- Cards: 121 carried (deterministic basis rebind; D122 has no task by DROP exclusion).
- Canonical accept (append-only). Frozen Core only.
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
EDIR = f"{SRC}/execution/post-freeze-integrity-20261005"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/evidence-package-121"
CURR = "48db41bff68320ded5d3bc34fbd12e1838b33fa44b0f32688e6752d"
CURR_RES = f"{SRC}/evidence/v2/accepted/{CURR}/results"
STABLE_RES = f"{SRC}/evidence/v2/accepted/3cd37179fe5c5a70d549dfabc9399864dea6a49ce79f1e85dcafd086ac61d412/results"
UNION = f"{EDIR}/evidence-authority-supplement-union-121.json"
DROP_TID = "evidence:SP-vision-multimodal-2026:72f7875f58def3a2"


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
        assert scr_acc["record_count"] == 122, scr_acc["record_count"]
        drops = [d["discovery_id"] for d in scr_acc["decisions"] if d["decision"] == "DROP"]
        assert drops == ["VM-D122"], drops
        print("screening basis:", scr_acc_path.parent.name[:12])

        source_root = core.repo_local_path(
            root, core.load_json(root / core.load_json(root / STATE_REL)["profile"]["path"])["paths"]["source_root"],
            "paths.source_root")
        package_path = evidence.prepare_evidence_package(
            root, root / STATE_REL, root / DISC_REL, scr_acc_path,
            root / PKGDIR, impl, root / UNION)
        package = core.load_json(package_path)
        assert len(package["tasks"]) == 121, len(package["tasks"])
        assert DROP_TID not in {m["evidence_task_id"] for m in package["tasks"]}
        PROMPT_SHA = package["prompt"]["sha256"]
        CONTRACT_SHA = package["contracts"]["card"]["sha256"]

        with tempfile.TemporaryDirectory() as temp:
            import sys as _sys
            _sys.path.insert(0, str(root / SRC / "execution/final-closure-repair-20261005"))
            import phase_c_evidence as _fc
            _fc._build_new_cards()
            staged121 = copy.deepcopy(_fc.NEW_CARDS["VM-D121"])
            tid121 = evidence.stable_task_id(ISSUE_ID, "VM-D121")
            results_dir = Path(temp) / "evidence-results"
            results_dir.mkdir()
            carried, staged_n = 0, 0
            for meta in package["tasks"]:
                fname = Path(meta["path"]).name
                task = core.load_json(root / PKGDIR / meta["path"])
                if meta["evidence_task_id"] == tid121:
                    card = copy.deepcopy(staged121)
                    card["evidence_task_id"] = meta["evidence_task_id"]
                    card["basis"] = {
                        "task_sha256": meta["sha256"],
                        "screening_acceptance_sha256": core.sha256_file(scr_acc_path),
                        "prompt_sha256": PROMPT_SHA,
                        "result_contract_sha256": CONTRACT_SHA,
                    }
                    errs = evidence.validate_evidence_card(
                        card, task, meta["sha256"], package, repo_root=root)
                    assert not errs, errs
                    core.write_json(results_dir / fname, card)
                    staged_n += 1
                    continue
                base = core.load_json(root / STABLE_RES / fname)
                base["basis"]["task_sha256"] = meta["sha256"]
                base["basis"]["screening_acceptance_sha256"] = core.sha256_file(scr_acc_path)
                assert base["basis"]["prompt_sha256"] == PROMPT_SHA, meta["evidence_task_id"]
                assert base["basis"]["result_contract_sha256"] == CONTRACT_SHA
                errs = evidence.validate_evidence_card(
                    base, task, meta["sha256"], package, repo_root=root)
                if errs:
                    raise ValueError(f"Card {meta['evidence_task_id']} invalid: {'; '.join(errs)}")
                core.write_json(results_dir / fname, base)
                carried += 1
            assert carried == 120 and staged_n == 1, (carried, staged_n)

            evidence_acceptance_path = evidence.accept_evidence_results(
                root, package_path, results_dir, source_root / "evidence/v2/accepted", impl)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, impl)
        assert evidence_acceptance["result_count"] == 121
        print("evidence acceptance:", evidence_acceptance_path.relative_to(root))
        print("carried:", carried, "| D122 excluded by DROP")
    print("EVIDENCE REPLAY COMPLETE (advance in next step)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
