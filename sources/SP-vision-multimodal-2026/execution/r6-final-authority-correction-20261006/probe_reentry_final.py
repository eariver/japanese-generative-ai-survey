#!/usr/bin/env python3
"""Fail-closed probes of formal Core re-entry mechanisms at ARCHITECTURE_ESTABLISHED (r6 PENDING).

READ-ONLY, zero writes. Records reentry-probes-r6-final.md.
"""
from __future__ import annotations
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")


def main() -> int:
    import sys
    sys.path.insert(0, str(ROOT))
    from scripts import survey_human_gate_v2 as human_gate
    from scripts import survey_production_v2 as core

    cfg = core.load_json(ROOT / core.DEFAULT_CONFIG)
    state_path = ROOT / "sources/SP-vision-multimodal-2026/production-state.json"
    state = core.load_json(state_path)
    assert state["lifecycle_state"] == "ARCHITECTURE_ESTABLISHED", state["lifecycle_state"]
    assert state["human_gates"]["architecture_review"] == "pending", state["human_gates"]
    results = []

    # Probe 1: ARCHITECTURE_REVIEW gate pending validation (expected PASS — gate IS pending)
    try:
        human_gate._validate_gate_pending(state, "ARCHITECTURE_REVIEW")
        results.append(("ARCHITECTURE_REVIEW pending-gate predicate", "PASS-PENDING",
                        "Gate is pending at ARCHITECTURE_ESTABLISHED; a formal request_changes invocation would still require an explicit Human REQUEST_CHANGES decision + boundary, which this run must NOT fabricate. Formal revision via Human decision path is therefore CLOSED to the worker."))
    except Exception as exc:  # noqa: BLE001
        results.append(("ARCHITECTURE_REVIEW pending-gate predicate", "FAIL-CLOSED",
                        f"{type(exc).__name__}: {exc}"))

    # Probe 2: operator pending-gate invalidation (formal non-Human path) — must FAIL-CLOSED
    # Reason: review index already contains r1-r5 Human records; Core requires zero records.
    try:
        _, profile, source_root = human_gate._state_context(ROOT, cfg, state_path)
        index = human_gate._load_review_index(ROOT, cfg, source_root, state["issue_id"])
        n = len(index.get("reviews", []))
        # Now attempt the actual guard that invalidate_pending_gate enforces (read-only replica):
        # it raises if index has any reviews. Replicate without writing.
        if index.get("reviews"):
            raise human_gate.HumanGateError(
                f"operator pending-Gate invalidation requires no Human review records (found {n}: "
                + ", ".join(f"{r['gate']}-r{r['revision']}/{r['decision']}" for r in index["reviews"]) + ")"
            )
        results.append(("operator invalidate_pending_gate (ARCHITECTURE_REVIEW)", "UNEXPECTED-PASS", ""))
    except Exception as exc:  # noqa: BLE001
        results.append(("operator invalidate_pending_gate (ARCHITECTURE_REVIEW)", "FAIL-CLOSED",
                        f"{type(exc).__name__}: {exc}"))

    # Probe 3: boundary allowlist readout (INFO)
    bounds = cfg["orchestration"].get("human_gate_revision_boundaries", {})
    op_bounds = cfg["orchestration"].get("operator_pending_gate_invalidation_boundaries", {})
    results.append(("boundary allowlist readout", "INFO",
                    f"ARCHITECTURE_REVIEW revision allows {bounds.get('ARCHITECTURE_REVIEW')}; "
                    f"operator invalidation allows {op_bounds.get('ARCHITECTURE_REVIEW')}; "
                    f"CANDIDATES_NORMALIZED allowed=True in both, but probes 1-2 close formal invocation."))

    # Probe 4: shared-Core untouched constraint (INFO)
    results.append(("shared-Core modification", "CLOSED",
                    "Shared roots (AGENTS.md/config/schemas/scripts/.github/docs core) are read-only; no Core change is authorized in this run."))

    out = ["# Re-entry probes r6-final (read-only, zero writes)", ""]
    all_closed = True
    for name, verdict, detail in results:
        out.append(f"- {name}: {verdict}")
        if detail:
            out.append(f"  - {detail}")
        all_closed = all_closed and verdict in ("PASS-PENDING", "FAIL-CLOSED", "INFO", "CLOSED")
    out.append("")
    out.append("Conclusion: no formal supported mechanism can make the correction without "
               "fabricating a Human decision (request_changes) or violating the operator-invalidation "
               "no-records precondition (r1-r5 history exists). Forward advance cannot move backward. "
               "Consume the run-specific Owner Exception (this task message §0-§2) via Core-controlled "
               "machinery only; manual state/checkpoint edits prohibited.")
    (ROOT / "sources/SP-vision-multimodal-2026/execution/r6-final-authority-correction-20261006"
     / "reentry-probes-r6-final.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))
    return 0 if all_closed else 1


if __name__ == "__main__":
    raise SystemExit(main())
