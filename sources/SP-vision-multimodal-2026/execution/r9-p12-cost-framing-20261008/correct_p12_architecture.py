#!/usr/bin/env python3
"""TS-003 r9 final bounded correction: P12 Evidence-safe cost framing.

- Content base: HEAD-committed r9 PROPOSED architecture-v2.json + refreshed
  basis + PROPOSED status + TARGETED P12 semantic change only:
  must-cover "Screenshot-loop token costs via TS-001 vocabulary; safety audits
  as eval metadata only" REPLACED with the Evidence-safe cost-framing
  requirement; one proxy-prohibition boundary ADDED.
- Delta guard: every other package byte-identical (P02/P04/P15 explicitly
  asserted). Any semantic drift outside P12 -> STOP (no expansion).
- Fresh review-summary-v2 + attention-v2, canonical validate, advance
  SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED with gates pending. STOP THERE.
- Frozen Core only.
"""
from __future__ import annotations

import difflib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from scripts import survey_agent_control_v2 as agent
from scripts import survey_agent_tool_v2 as agent_tool
from scripts import survey_architecture_v2_base as archbase
from scripts import survey_production_v2 as core
from scripts import survey_review_attention_v2 as review_attention
from scripts import survey_stage_validation_v2 as stage_validation

ISSUE_ID = "SP-vision-multimodal-2026"
SRC = f"sources/{ISSUE_ID}"
EDIR = f"{SRC}/execution/r9-p12-cost-framing-20261008"
STATE_REL = f"{SRC}/production-state.json"
PROFILE_REL = f"{SRC}/production-profile.json"
VALIDATION_REL = f"{EDIR}/validation"

MC_OLD = ("Screenshot-loop token costs via TS-001 vocabulary; safety audits as eval metadata only")
MC_NEW = ("Long-horizon interaction and state-management burden: measured tool-call counts "
          "may be used as an interaction-horizon/state-management proxy; token, context, "
          "memory, latency, or compute costs may be asserted only where directly measured "
          "by bound Evidence. Safety audits remain evaluation metadata only.")
B_NEW_PROXY = ("Tool-call count is not itself a direct measurement of token count, "
               "context-window utilization, KV-cache/memory footprint, latency, or compute "
               "cost. It may be used only as a proxy for interaction horizon and "
               "state-management burden unless a corresponding efficiency field is directly "
               "measured by bound Evidence.")


def _package(arch: dict, package_id: str) -> dict:
    hits = [p for p in arch["packages"] if p["package_id"] == package_id]
    assert len(hits) == 1, package_id
    return hits[0]


def main() -> int:
    root = Path(".").resolve()
    cfg = core.load_json(root / core.DEFAULT_CONFIG)
    state = core.load_json(root / STATE_REL)
    if state.get("issue_id") != ISSUE_ID or state.get("lifecycle_state") != "SELECTION_COMPLETE":
        raise ValueError("expected canonical State at SELECTION_COMPLETE")
    impl = core.repository_commit_sha(root)
    profile_path = root / PROFILE_REL

    with agent_tool.current_stage_basis_override():
        head_v2 = json.loads(subprocess.run(
            ["git", "show", f"HEAD:{SRC}/architecture-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8"))
        ledger_path = root / f"{SRC}/materiality-ledger-v2.json"
        comp_path = root / f"{SRC}/profile-completeness-v2.json"
        matrix_path = root / f"{SRC}/candidate-matrix-v2.json"
        sel_path = root / f"{SRC}/candidate-selection-v2.json"
        for p in (ledger_path, comp_path, matrix_path, sel_path):
            assert p.is_file(), p

        arch = json.loads(json.dumps(head_v2))
        arch["basis"] = {
            "production_profile_sha256": core.sha256_file(profile_path),
            "profile_completeness_sha256": core.sha256_file(comp_path),
            "materiality_ledger_sha256": core.sha256_file(ledger_path),
            "candidate_matrix_sha256": core.sha256_file(matrix_path),
            "candidate_selection_sha256": core.sha256_file(sel_path),
        }
        arch["status"] = "PROPOSED"
        arch["human_review"] = {"reviewed_by": None, "reviewed_at": None,
                                "review_reference": None}

        # --- P12: Evidence-safe cost framing (only semantic change) ---
        p12 = _package(arch, "P12")
        assert MC_OLD in p12["must_cover_requirements"], p12["must_cover_requirements"]
        assert B_NEW_PROXY not in p12["boundaries"]
        p12["must_cover_requirements"] = [
            MC_NEW if r == MC_OLD else r for r in p12["must_cover_requirements"]]
        p12["boundaries"] = [*p12["boundaries"], B_NEW_PROXY]

        # --- semantic checks on the new wording (all §4/§5 mandatory semantics) ---
        assert "measured tool-call counts" in MC_NEW
        assert "interaction-horizon/state-management proxy" in MC_NEW
        assert "only where directly measured" in MC_NEW
        assert "token, context" in MC_NEW and "memory" in MC_NEW
        assert "Safety audits remain evaluation metadata only" in MC_NEW
        assert "not itself a direct measurement" in B_NEW_PROXY
        assert "KV-cache/memory footprint" in B_NEW_PROXY
        assert "proxy for interaction horizon" in B_NEW_PROXY

        # --- invariants: everything else identical ---
        assert len(arch["packages"]) == 16
        for hp, np in zip(head_v2["packages"], arch["packages"]):
            assert hp["package_id"] == np["package_id"]
            assert hp["drafting_order"] == np["drafting_order"]
            assert hp["title"] == np["title"] and hp["purpose"] == np["purpose"], np["package_id"]
            assert hp["primary_candidate_ids"] == np["primary_candidate_ids"], np["package_id"]
            assert hp["supporting_candidate_ids"] == np["supporting_candidate_ids"], np["package_id"]
        assert arch["page_plan"] == head_v2["page_plan"]
        assert arch["editorial_thesis"] == head_v2["editorial_thesis"]
        assert arch["architecture_goals"] == head_v2["architecture_goals"]
        assert arch["publication_extensions"] == head_v2["publication_extensions"]
        # P12 long-horizon thesis + OSWorld distinction + condition binding preserved
        assert any("OSWorld 1.0 vs 2.0" in r for r in p12["must_cover_requirements"])
        assert any("strictest binding" in b for b in p12["boundaries"])

        # --- delta guard: only P12 differs ---
        pkgs_old = {p["package_id"]: p for p in head_v2["packages"]}
        pkgs_new = {p["package_id"]: p for p in arch["packages"]}
        for pid in pkgs_old:
            if pkgs_old[pid] != pkgs_new[pid]:
                assert pid in ("P12",), pid
        print("delta guard: only P12 cost-framing change + basis/status/review")

        arch_path = root / f"{SRC}/architecture-v2.json"
        assert not arch_path.exists(), "canonical architecture should have been invalidated"
        core.write_json(arch_path, arch)
        errs = archbase.validate_architecture(
            root, arch, profile_path, comp_path, ledger_path, matrix_path, sel_path)
        assert not errs, errs[:5]
        print("architecture v2 regenerated (PROPOSED r9, P12 corrected)")

        disc_rel = root / f"{SRC}/discovery/discovery-v2.jsonl"
        new_pkg = core.load_json(max(
            (root / SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
            key=lambda p: p.stat().st_mtime).parent / "package.json")
        scr_acc = (root / new_pkg["basis"]["screening_acceptance_path"]).resolve()
        ev_acc = max((root / SRC / "evidence/v2/accepted").glob("*/evidence-accepted.json"),
                     key=lambda p: p.stat().st_mtime)
        view_acc = max((root / SRC / "evidence/v2/views/accepted").glob("*/edition-views-accepted.json"),
                       key=lambda p: p.stat().st_mtime)
        summary = archbase.build_architecture_review_summary(
            root, profile_path, disc_rel, scr_acc, ev_acc, view_acc,
            ledger_path, comp_path, matrix_path, sel_path, arch_path, impl)
        assert summary.get("readiness", {}).get("status") == "READY_FOR_ARCHITECTURE_REVIEW", summary.get("readiness")
        sum_path = root / f"{SRC}/architecture-review-summary-v2.json"
        assert not sum_path.exists()
        core.write_json(sum_path, summary)
        attn_path = root / f"{SRC}/architecture-review-attention-v2.json"
        assert not attn_path.exists()
        review_attention.build_attention(
            root, scr_acc, ledger_path, sel_path, attn_path)
        review_attention.validate_attention(root, attn_path)
        print("review summary + attention regenerated")

        head_text = subprocess.run(
            ["git", "show", f"HEAD:{SRC}/architecture-v2.json"],
            cwd=root, check=True, capture_output=True).stdout.decode("utf-8")
        diff = "\n".join(difflib.unified_diff(
            head_text.splitlines(), arch_path.read_text(encoding="utf-8").splitlines(),
            fromfile="architecture-v2.json@r9-prev", tofile="architecture-v2.json@r9-p12-corrected", n=1))
        (root / EDIR / "architecture-r9prev-to-r9p12.diff").write_text(diff + "\n", encoding="utf-8")
        print("semantic diff lines:", len(diff.splitlines()))

        now = datetime.now(timezone.utc)
        vdir = root / VALIDATION_REL
        validation_path = vdir / "architecture-stage-validation-p12.json"
        reviews_path = vdir / "architecture-stage-reviews-p12.json"
        assert not validation_path.exists() and not reviews_path.exists()
        stage_validation.validate_stage(
            root, cfg, root / STATE_REL,
            {"issue-architecture": arch_path,
             "architecture-review-summary": sum_path,
             "architecture-review-attention": attn_path},
            validation_path, now)
        core.write_json(reviews_path, {"reviews": [{
            "check_id": "CORE_STAGE_CONTRACT", "kind": "DETERMINISTIC",
            "executor": "Muse Spark (Work execution role; deterministic tool result, not a Sol/Human decision)",
            "evidence": ("Architecture stage-contract validation passed over 124-record "
                         "canonical authority (r9 P12 Evidence-safe cost framing; all other "
                         "packages identical). Machine validation only; Sol Architecture "
                         "review + Human r9 decision owed; nothing approved here."),
            "result_path": str(validation_path.relative_to(root)),
        }]})
        generated = agent.build_stage_checkpoint(
            root, cfg, root / STATE_REL,
            {"issue-architecture": arch_path,
             "architecture-review-summary": sum_path,
             "architecture-review-attention": attn_path}, reviews_path,
            ("TS-003 Architecture r9 corrected (P12 cost framing Evidence-safe; P02/P04/P15 "
             "and all others unchanged). "
             "STOP at fresh pending Human Architecture Review r9; Sol review + Human "
             "decision owed."),
            now)
        updated = agent.advance_with_checkpoint(root, cfg, root / STATE_REL, generated)
        assert updated.get("lifecycle_state") == "ARCHITECTURE_ESTABLISHED", updated.get("lifecycle_state")
        errors = agent.validate_agent_state(root, cfg, updated)
        assert not errors, errors
        assert updated["human_gates"]["architecture_review"] == "pending", updated["human_gates"]
        assert updated["human_gate_provenance"]["architecture_review"] is None
    print("lifecycle:", updated["lifecycle_state"], "| gates:", updated["human_gates"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
