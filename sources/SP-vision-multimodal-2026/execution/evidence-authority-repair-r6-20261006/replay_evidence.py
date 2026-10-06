#!/usr/bin/env python3
"""TS-003 replay step 1 (exception-authorized r6): Evidence (121) at CANDIDATES_NORMALIZED.

- Canonical prepare_evidence_package over unchanged Discovery (122) + Screening (122)
  + unchanged 121 authority supplement.
- STRONG determinism check: re-prepared 121 task SHAs must equal the accepted f6ef98cb
  package task SHAs (proves no upstream drift before card swap).
- Cards: 118 carried byte-identical from f6ef98cb + 3 staged corrected cards
  (canonical-validated already; re-validated here against the fresh package basis
  with deterministic basis rebinding only).
- Canonical accept_evidence_results (append-only new content-addressed set).
- Frozen Core only. No state advance here.
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
EDIR = f"{SRC}/execution/evidence-authority-repair-r6-20261006"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
PKGDIR = f"{EDIR}/evidence-package-121"
SUPPLEMENT_REL = (f"{SRC}/execution/obligation-realization-r5-20261005/"
                  "evidence-authority-supplement-union-121.json")
CURR = "f6ef98cb6b5e6246affbde9c899e8018cac8983aa9848cc14b8ced77f54ccd24"
CURR_RES = f"{SRC}/evidence/v2/accepted/{CURR}/results"

CORRECTED_TASKS = {
    "evidence:SP-vision-multimodal-2026:4ca2413b8167abe8",
    "evidence:SP-vision-multimodal-2026:20d1ebc2759ddd61",
    "evidence:SP-vision-multimodal-2026:64c27ede08e070eb",
}


def _screening_acceptance(root: Path) -> Path:
    # Canonical screening acceptance is the one bound by the current accepted
    # Evidence package basis (deterministic; avoids glob ambiguity).
    curr_pkg = core.load_json(root / CURR_RES / "../package.json")
    rel = curr_pkg["basis"]["screening_acceptance_path"]
    p = (root / rel).resolve()
    assert p.is_file(), rel
    assert core.load_json(p)["record_count"] == 122
    return p


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
        assert scr_acc["record_count"] == 122
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
        assert len(package["tasks"]) == 121, len(package["tasks"])

        # STRONG determinism: task SHAs must equal the accepted f6ef98cb package.
        curr_pkg = core.load_json(root / CURR_RES / "../package.json")
        curr_tasks = {m["evidence_task_id"]: m["sha256"] for m in curr_pkg["tasks"]}
        new_tasks = {m["evidence_task_id"]: m["sha256"] for m in package["tasks"]}
        assert set(curr_tasks) == set(new_tasks), "task set drift"
        drift = [t for t in curr_tasks if curr_tasks[t] != new_tasks[t]]
        assert not drift, f"task SHA drift: {drift}"
        print("package determinism: 121/121 task SHAs identical")

        probe = core.load_json(root / CURR_RES / "task-0202917391a980c0420f.json")
        PROMPT_SHA = probe["basis"]["prompt_sha256"]
        CONTRACT_SHA = probe["basis"]["result_contract_sha256"]

        staged_by_task = {}
        staged_files = sorted((root / EDIR / "staged-cards").glob("staged-*.json"))
        assert len(staged_files) == 3, [str(p) for p in staged_files]
        for sfile in staged_files:
            card = core.load_json(sfile)
            staged_by_task[card["evidence_task_id"]] = card
        assert set(staged_by_task) == CORRECTED_TASKS

        with tempfile.TemporaryDirectory() as temp:
            results_dir = Path(temp) / "evidence-results"
            results_dir.mkdir()
            carried, corrected = 0, []
            carried_bytes = []
            for meta in package["tasks"]:
                fname = Path(meta["path"]).name
                task = core.load_json(root / PKGDIR / meta["path"])
                if meta["evidence_task_id"] in staged_by_task:
                    card = json.loads(json.dumps(staged_by_task[meta["evidence_task_id"]]))
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
                    carried_bytes.append(fname)
                core.write_json(results_dir / fname, card)
            assert carried == 118 and len(corrected) == 3, (carried, corrected)

            # byte-identity audit for carried cards (basis SHAs proven identical above)
            for fname in carried_bytes:
                a = (results_dir / fname).read_bytes()
                b = (root / CURR_RES / fname).read_bytes()
                assert a == b, f"carried card bytes differ: {fname}"
            print("carried byte-identity: 118/118")

            evidence_acceptance_path = evidence.accept_evidence_results(
                root, package_path, results_dir, source_root / "evidence/v2/accepted", impl)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, impl)
        assert evidence_acceptance["result_count"] == 121
        statuses = {}
        for r in evidence_acceptance["results"]:
            statuses[r["status"]] = statuses.get(r["status"], 0) + 1
        print("accepted:", evidence_acceptance_path.relative_to(root), statuses)
        assert statuses == {"VERIFIED": 116, "PARTIAL": 5}, statuses
        (root / EDIR / "evidence-replay-report.json").write_text(json.dumps(
            {"acceptance": str(evidence_acceptance_path.relative_to(root)),
             "result_count": 121, "statuses": statuses,
             "carried_byte_identical": carried, "corrected": sorted(corrected)},
            ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
