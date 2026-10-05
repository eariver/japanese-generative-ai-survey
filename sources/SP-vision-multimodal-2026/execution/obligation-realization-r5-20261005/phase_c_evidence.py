#!/usr/bin/env python3
"""TS-003 Phase C (obligation realization): Evidence (121) at CANDIDATES_NORMALIZED.

- Union supplement manifest rebuilt in this dir (same 22 entries: VM-D112 2 +
  VM-D077 10 + VM-D074 4 + VM-D075 4 + VM-D074-history 2).
- Cards: 118 carried (deterministic basis rebind; D122 has no task by DROP exclusion)
  + 3 corrected (staged D075/D090/D092, canonical-validated; basis rebound here).
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
EDIR = f"{SRC}/execution/obligation-realization-r5-20261005"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/evidence-package-121"
CURR = "caab11b84274a4f4073b77042ca46d6154fbec473de5bce9b1c2644314e9b8c7"
CURR_RES = f"{SRC}/evidence/v2/accepted/{CURR}/results"
UNION = f"{EDIR}/evidence-authority-supplement-union-121.json"
UNION_ID = "ts003-obligation-realization-supplement-union-20261005"
DROP_TID = "evidence:SP-vision-multimodal-2026:72f7875f58def3a2"
TID075 = "evidence:SP-vision-multimodal-2026:4b007409a575a02d"
TID090 = "evidence:SP-vision-multimodal-2026:85268ad1dbd5f285"
TID092 = "evidence:SP-vision-multimodal-2026:3d4f179a082773fd"
SUPPLEMENT_FILES = [
    f"{SRC}/execution/architecture-r3-intake-20261003/evidence-authority-supplement-112.json",
    f"{SRC}/execution/vm-d077-authority-repair-20261004/evidence-authority-supplement-vm-d077.json",
    f"{SRC}/execution/license-authority-repair-r5-20261004/evidence-authority-supplement-vm-d074.json",
    f"{SRC}/execution/license-authority-repair-r5-20261004/evidence-authority-supplement-vm-d075.json",
    f"{SRC}/execution/late-cutoff-expansion-20261005/evidence-authority-supplement-vm-d074-history.json",
]


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
        # Union manifest rebuilt in this dir (same entries, fresh basis validation).
        union_sources = []
        for rel in SUPPLEMENT_FILES:
            m = core.load_json(root / rel)
            union_sources.extend(m["sources"])
        assert len(union_sources) == 22, len(union_sources)
        assert len({s["supplement_source_id"] for s in union_sources}) == 22
        union_out = root / UNION
        assert not union_out.exists()
        union_out.write_text(json.dumps({
            "schema_version": "2.0-rc1",
            "supplement_id": UNION_ID,
            "issue_id": ISSUE_ID,
            "basis": {
                "source_root": SRC,
                "discovery_path": DISC_REL,
                "discovery_sha256": core.sha256_file(root / DISC_REL),
                "screening_acceptance_path": str(scr_acc_path.relative_to(root)),
                "screening_acceptance_sha256": core.sha256_file(scr_acc_path),
            },
            "sources": union_sources,
        }, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        from scripts import survey_schema_v2 as schema_gate
        schema_gate.validate_instance(
            core.load_json(union_out), root / "schemas/evidence-authority-supplement-v2.schema.json",
            label="Evidence Authority Supplement (union-121)")
        print("union manifest: 22 entries")
        package_path = evidence.prepare_evidence_package(
            root, root / STATE_REL, root / DISC_REL, scr_acc_path,
            root / PKGDIR, impl, root / UNION)
        package = core.load_json(package_path)
        assert len(package["tasks"]) == 121, len(package["tasks"])
        assert DROP_TID not in {m["evidence_task_id"] for m in package["tasks"]}
        PROMPT_SHA = package["prompt"]["sha256"]
        CONTRACT_SHA = package["contracts"]["card"]["sha256"]

        with tempfile.TemporaryDirectory() as temp:
            staged_by_task = {}
            for fn, tid in (("staged-vm-d075-card.json", TID075),
                            ("staged-vm-d090-card.json", TID090),
                            ("staged-vm-d092-card.json", TID092)):
                card = core.load_json(root / EDIR / fn)
                assert card["evidence_task_id"] == tid, fn
                staged_by_task[tid] = card
            results_dir = Path(temp) / "evidence-results"
            results_dir.mkdir()
            carried, corrected = 0, []
            for meta in package["tasks"]:
                fname = Path(meta["path"]).name
                task = core.load_json(root / PKGDIR / meta["path"])
                if meta["evidence_task_id"] in staged_by_task:
                    card = copy.deepcopy(staged_by_task[meta["evidence_task_id"]])
                    card["basis"] = {
                        "task_sha256": meta["sha256"],
                        "screening_acceptance_sha256": core.sha256_file(scr_acc_path),
                        "prompt_sha256": PROMPT_SHA,
                        "result_contract_sha256": CONTRACT_SHA,
                    }
                    errs = evidence.validate_evidence_card(
                        card, task, meta["sha256"], package, repo_root=root)
                    assert not errs, (meta["evidence_task_id"], errs)
                    core.write_json(results_dir / fname, card)
                    corrected.append(meta["evidence_task_id"])
                    continue
                base = core.load_json(root / CURR_RES / fname)
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
            assert carried == 118 and len(corrected) == 3, (carried, corrected)

            evidence_acceptance_path = evidence.accept_evidence_results(
                root, package_path, results_dir, source_root / "evidence/v2/accepted", impl)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, impl)
        assert evidence_acceptance["result_count"] == 121
        print("evidence acceptance:", evidence_acceptance_path.relative_to(root))
        print("carried:", carried, "| corrected: D075/D090/D092")
    print("EVIDENCE REPLAY COMPLETE (advance in next step)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
