#!/usr/bin/env python3
"""TS-003 replay step 1 (section-2-authorized): Evidence (112).

- Union supplement manifest: VM-D112 (2, byte-identical carry) + VM-D077 (10, carry)
  + VM-D074 (4, new) + VM-D075 (4, new) = 20 entries.
- Cards: 110 carried (deterministic basis rebind) + 2 corrected (staged D074/D075,
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
from scripts import survey_schema_v2 as schema_gate

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/license-authority-repair-r5-20261004"
PREV1 = f"{SRC}/execution/vm-d077-authority-repair-20261004"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/evidence-package-112"
UNION = f"{EDIR}/evidence-authority-supplement-union-r5.json"
UNION_ID = "ts003-license-repair-supplement-union-20261005"
CURR = "446f359c726546411244389d66c60dd5037d9d16a671cb5842accc02a10fa2da"
CURR_RES = f"{SRC}/evidence/v2/accepted/{CURR}/results"
TID074 = "evidence:SP-vision-multimodal-2026:e543b8e20cd2e54c"
TID075 = "evidence:SP-vision-multimodal-2026:4b007409a575a02d"
SUP112 = f"{SRC}/execution/architecture-r3-intake-20261003/evidence-authority-supplement-112.json"
SUP077 = f"{PREV1}/evidence-authority-supplement-vm-d077.json"
SUP074 = f"{EDIR}/evidence-authority-supplement-vm-d074.json"
SUP075 = f"{EDIR}/evidence-authority-supplement-vm-d075.json"


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
        # Union manifest: prior entries byte-identical carry + 8 new license entries.
        union_sources = []
        for rel in (SUP112, SUP077, SUP074, SUP075):
            m = core.load_json(root / rel)
            union_sources.extend(m["sources"])
        assert len(union_sources) == 20, len(union_sources)
        assert len({s["supplement_source_id"] for s in union_sources}) == 20
        counts = {}
        for s in union_sources:
            counts[s["discovery_id"]] = counts.get(s["discovery_id"], 0) + 1
        assert counts == {"VM-D112": 2, "VM-D077": 10, "VM-D074": 4, "VM-D075": 4}, counts
        base112 = core.load_json(root / SUP112)
        union_out = root / UNION
        assert not union_out.exists()
        union_out.write_text(json.dumps({
            "schema_version": "2.0-rc1",
            "supplement_id": UNION_ID,
            "issue_id": ISSUE_ID,
            "basis": base112["basis"],
            "sources": union_sources,
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        schema_gate.validate_instance(
            core.load_json(union_out), root / "schemas/evidence-authority-supplement-v2.schema.json",
            label="Evidence Authority Supplement (union)")
        print("union manifest: 20 entries")

        package_path = evidence.prepare_evidence_package(
            root, root / STATE_REL, root / DISC_REL, scr_acc_path,
            root / PKGDIR, impl, union_out)
        package = core.load_json(package_path)
        assert len(package["tasks"]) == 112, len(package["tasks"])
        probe = core.load_json(root / CURR_RES / "task-0202917391a980c0420f.json")
        PROMPT_SHA = probe["basis"]["prompt_sha256"]
        CONTRACT_SHA = probe["basis"]["result_contract_sha256"]

        staged074 = core.load_json(root / EDIR / "staged-vm-d074-license.json")
        assert staged074["evidence_task_id"] == TID074
        staged075 = core.load_json(root / EDIR / "staged-vm-d075-license.json")
        assert staged075["evidence_task_id"] == TID075
        staged_by_task = {TID074: staged074, TID075: staged075}

        with tempfile.TemporaryDirectory() as temp:
            results_dir = Path(temp) / "evidence-results"
            results_dir.mkdir()
            carried, corrected = 0, []
            for meta in package["tasks"]:
                fname = Path(meta["path"]).name
                task = core.load_json(root / PKGDIR / meta["path"])
                if meta["evidence_task_id"] in staged_by_task:
                    import copy as _copy
                    card = _copy.deepcopy(staged_by_task[meta["evidence_task_id"]])
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
            assert carried == 110 and len(corrected) == 2, (carried, corrected)

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
