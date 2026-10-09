#!/usr/bin/env python3
"""Fail-closed probes of formal Core re-entry mechanisms at DRAFT_COMPLETE (r8 APPROVED).

READ-ONLY, zero writes. Records reentry-probes-r9.md.
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
    assert state["lifecycle_state"] == "DRAFT_COMPLETE", state["lifecycle_state"]
    assert state["human_gates"]["architecture_review"] == "approved"
    results = []

    try:
        human_gate._validate_gate_pending(state, "ARCHITECTURE_REVIEW")
        results.append(("ARCHITECTURE_REVIEW request_changes path", "UNEXPECTED-PASS", ""))
    except Exception as exc:  # noqa: BLE001
        results.append(("ARCHITECTURE_REVIEW request_changes path", "FAIL-CLOSED",
                        f"{type(exc).__name__}: {exc} (formal revision needs an explicit Human "
                        "REQUEST_CHANGES decision + boundary, which the worker must NOT fabricate)"))
    try:
        human_gate._validate_gate_pending(state, "PUBLICATION_PREVIEW")
        results.append(("PUBLICATION_PREVIEW request_changes path", "UNEXPECTED-PASS", ""))
    except Exception as exc:  # noqa: BLE001
        results.append(("PUBLICATION_PREVIEW request_changes path", "FAIL-CLOSED",
                        f"{type(exc).__name__}: {exc}"))
    try:
        _, _, source_root = human_gate._state_context(ROOT, cfg, state_path)
        index = human_gate._load_review_index(ROOT, cfg, source_root, state["issue_id"])
        raise human_gate.HumanGateError(
            f"operator pending-Gate invalidation requires no Human review records (found "
            f"{len(index.get('reviews', []))}) and a currently-pending unpresented Gate; "
            "lifecycle is DRAFT_COMPLETE with r8 APPROVED active. No formal operator path applies.")
    except Exception as exc:  # noqa: BLE001
        results.append(("operator invalidate_pending_gate", "FAIL-CLOSED",
                        f"{type(exc).__name__}: {exc}"))
    results.append(("forward advance direction", "CLOSED",
                    "advance requires record.from_state == current lifecycle; DRAFT_COMPLETE "
                    "can only advance to reader-publication-validation, never rewind."))
    results.append(("shared-Core modification", "CLOSED",
                    "Shared roots are read-only during edition production; no Core change authorized."))

    out = ["# Re-entry probes r9 (read-only, zero writes)", ""]
    all_closed = True
    for name, verdict, detail in results:
        out.append(f"- {name}: {verdict}")
        if detail:
            out.append(f"  - {detail}")
        all_closed = all_closed and verdict in ("FAIL-CLOSED", "INFO", "CLOSED")
    out.append("")
    out.append("Conclusion: no formal supported mechanism can make the correction without "
               "the run-specific Human-bounded revision direction (§0). Consume that direction "
               "via Core-controlled machinery only (rewind + bounded replay, no gate decisions).")
    (ROOT / "sources/SP-vision-multimodal-2026/execution/p02-detr-bridge-intake-r9-20261008"
     / "reentry-probes-r9.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))
    return 0 if all_closed else 1


if __name__ == "__main__":
    raise SystemExit(main())
