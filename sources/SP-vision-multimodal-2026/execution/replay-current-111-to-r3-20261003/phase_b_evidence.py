#!/usr/bin/env python3
"""TS-003 replay Phase B: formal Evidence (111) + Edition Views.

- New 112-free task package (111 tasks) via canonical prepare_evidence_package.
- Cards: r8 card bytes carried with ONLY deterministic basis rebinding
  (basis.task_sha256 + basis.screening_acceptance_sha256 -> new package pins;
  claims/entities/sources/metrics/limitations/verification byte-identical).
  This preserves all r8 repairs (D084 V1, D010 cost/loss, D091 318-split,
  D106 SIMA scope) per Human instruction (rebinding excepted, no regression).
- Views rebuilt via canonical _build_view from the 111 authority input records.
- Canonical accept_evidence_results + accept_edition_views (content-addressed,
  append-only). NO advancement here (Phase B2 with materiality/completeness).
- Frozen Core only + documented post-gate adaptation (override + current HEAD).
"""

from __future__ import annotations

import json
import shutil
import tempfile
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_evidence_v2 as evidence
from scripts import survey_production_v2 as core
from scripts import run_evidence_v2_interactive as inter

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/replay-current-111-to-r3-20261003"
STATE_REL = f"{SRC}/production-state.json"
DISC_REL = f"{SRC}/discovery/discovery-v2.jsonl"
R8EV = "d6338dc49d65d444efc379df0adb2e63722c7d8c90164c043b9aca4721bc7b57"
R8VIEW = "11fd09a02b410c52331a4333ae14200d9d55d608f1bde38a459b40bba9196cc3"
R8_RES = f"{SRC}/evidence/v2/accepted/{R8EV}/results"
PKGDIR = f"{EDIR}/evidence-package-111"
INPUT_REL = f"{SRC}/execution/screening-evidence-20260930/evidence-interactive-input.json"

# This phase runs at CANDIDATES_NORMALIZED; screening acceptance resolved dynamically.
def _screening_acceptance(root: Path) -> Path:
    cands = sorted((root / SRC / "screening/v2/accepted").glob("*/screening-accepted.json"))
    assert cands, "no screening acceptance"
    # newest by mtime = the replay acceptance (r1 historical otherwise)
    return max(cands, key=lambda p: p.stat().st_mtime)


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
        assert scr_acc["record_count"] == 111, scr_acc["record_count"]
        assert not any(d["discovery_id"] == "VM-D112" for d in scr_acc["decisions"])
        print("screening basis:", scr_acc_path.relative_to(root))
        profile_path = root / core.load_json(root / STATE_REL)["profile"]["path"]
        profile = core.load_json(profile_path)
        source_root = core.repo_local_path(
            root, profile["paths"]["source_root"], "paths.source_root")

        package_path = evidence.prepare_evidence_package(
            root, root / STATE_REL, root / DISC_REL, scr_acc_path,
            root / PKGDIR, impl)
        package = core.load_json(package_path)
        assert len(package["tasks"]) == 111, len(package["tasks"])
        new_task_sha = {m["evidence_task_id"]: m["sha256"] for m in package["tasks"]}
        new_scr_sha = core.sha256_file(scr_acc_path)

        # Cards: r8 bytes + deterministic basis rebinding only.
        with tempfile.TemporaryDirectory() as temp:
            results_dir = Path(temp) / "evidence-results"
            results_dir.mkdir()
            for meta in package["tasks"]:
                fname = Path(meta["path"]).name
                base = core.load_json(root / R8_RES / fname)
                old_basis = dict(base["basis"])
                base["basis"]["task_sha256"] = meta["sha256"]
                base["basis"]["screening_acceptance_sha256"] = new_scr_sha
                assert base["basis"]["prompt_sha256"] == old_basis["prompt_sha256"]
                assert base["basis"]["result_contract_sha256"] == old_basis["result_contract_sha256"]
                task = core.load_json(root / PKGDIR / meta["path"])
                errs = evidence.validate_evidence_card(
                    base, task, meta["sha256"], package, repo_root=root)
                if errs:
                    raise ValueError(f"Card {meta['evidence_task_id']} invalid: {'; '.join(errs)}")
                core.write_json(results_dir / fname, base)

            source_root = core.repo_local_path(
                root, profile["paths"]["source_root"], "paths.source_root")
            evidence_root = source_root / "evidence/v2/accepted"
            evidence_acceptance_path = evidence.accept_evidence_results(
                root, package_path, results_dir, evidence_root, impl)
            evidence_acceptance, _ = evidence.validate_evidence_acceptance(
                root, evidence_acceptance_path, impl)
        assert evidence_acceptance["result_count"] == 111
        print("evidence acceptance:", evidence_acceptance_path.relative_to(root))

        # Views rebuilt canonically from the 111 authority input records.
        doc = core.load_json(root / INPUT_REL)
        records = doc["records"] if isinstance(doc, dict) else doc
        # input records keyed by discovery_id -> map to task via package metas
        task_meta = {m["discovery_ids"][0]: m for m in package["tasks"]}
        assert len(task_meta) == 111
        by_task_rows = {row["evidence_task_id"]: row for row in evidence_acceptance["results"]}
        with tempfile.TemporaryDirectory() as temp:
            views_dir = Path(temp) / "views"
            views_dir.mkdir()
            rec_by_did = {r["discovery_id"]: r for r in records}
            assert len(rec_by_did) == 111, len(rec_by_did)
            for did, meta in sorted(task_meta.items()):
                task_id = meta["evidence_task_id"]
                entry = by_task_rows[task_id]
                view = inter._build_view(profile, task_id, entry["sha256"], rec_by_did[did])
                errs = evidence.validate_edition_view(
                    view, profile, entry["sha256"], entry["status"])
                if errs:
                    raise ValueError(f"View {task_id} invalid: {'; '.join(errs)}")
                core.write_json(views_dir / evidence.view_filename(task_id), view)
            source_root = core.repo_local_path(
                root, profile["paths"]["source_root"], "paths.source_root")
            views_acceptance_path = evidence.accept_edition_views(
                root, profile_path, evidence_acceptance_path, views_dir,
                source_root / "evidence/v2/views/accepted", impl)
            evidence.validate_edition_views_acceptance(
                root, profile_path, evidence_acceptance_path, views_acceptance_path, impl)
        print("views acceptance:", views_acceptance_path.relative_to(root))

        # Regression guards (§7): r8 repairs present in carried cards.
        probes = {
            "VM-D084": ("Something-Something V1", "Something-Something V2"),
            "VM-D010": ("pair-wise matching cost", None),
            "VM-D091": ("Claude Opus 4.7", None),
            "VM-D106": ("executed in Genie-3 worlds", "SIMA-agent training use"),
        }
        task_files = {m["discovery_ids"][0]: m for m in package["tasks"]}
        for did, (good, bad) in probes.items():
            card = core.load_json(evidence_acceptance_path.parent / "results" / Path(task_files[did]["path"]).name)
            texts = [c["text"] for c in card["claims"]]
            assert any(good in t for t in texts), f"{did} repair missing: {good}"
            if bad:
                assert not any(bad in t for t in texts), f"{did} regression: {bad}"
            print(f"regression {did}: PASS")
    print("EVIDENCE 111 REPLAY COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
