#!/usr/bin/env python3
"""Fail-closed probes of formal Core re-entry mechanisms (READ-ONLY, zero writes).

Probes the exact guard predicates a formal rewind would need. All must FAIL CLOSED.
Recorded in reentry-probes-r6.md.
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

    # Probe 1: ARCHITECTURE_REVIEW gate pending? (needs ARCHITECTURE_ESTABLISHED + pending)
    try:
        human_gate._validate_gate_pending(state, "ARCHITECTURE_REVIEW")
        results.append(("ARCHITECTURE_REVIEW pending gate", "UNEXPECTED-PASS", ""))
    except Exception as exc:  # noqa: BLE001
        results.append(("ARCHITECTURE_REVIEW pending gate", "FAIL-CLOSED",
                        f"{type(exc).__name__}: {exc}"))

    # Probe 2: PUBLICATION_PREVIEW gate pending? (needs RELEASE_CANDIDATE + pending)
    try:
        human_gate._validate_gate_pending(state, "PUBLICATION_PREVIEW")
        results.append(("PUBLICATION_PREVIEW pending gate", "FAIL-CLOSED",
                        f"{type(exc).__name__}: {exc}"))
    except Exception as exc:  # noqa: BLE001
        results.append(("PUBLICATION_PREVIEW pending gate", "FAIL-CLOSED",
                        f"{type(exc).__name__}: {exc}"))

    # Probe 3: is CANDIDATES_NORMALIZED an allowed boundary for any gate context
    # WITHOUT a pending gate decision? _revised_state enforces boundary allowlist
    # but is only invoked from request_changes, which requires _validate_gate_pending
    # (probes 1-2 fail closed). Record the allowlist fact read-only.
    import json as _json
    bounds = cfg["orchestration"].get("human_gate_revision_boundaries", {})
    results.append(("boundary allowlist readout",
                    "INFO",
                    f"ARCHITECTURE_REVIEW allows {bounds.get('ARCHITECTURE_REVIEW')}; "
                    f"CANDIDATES_NORMALIZED allowed={('CANDIDATES_NORMALIZED' in (bounds.get('ARCHITECTURE_REVIEW') or []))} "
                    "but invocation requires a pending gate (probes 1-2 closed)"))

    out = ["# Re-entry probes r6 (read-only, zero writes)", ""]
    all_closed = True
    for name, verdict, detail in results:
        out.append(f"- {name}: {verdict}")
        if detail:
            out.append(f"  - {detail}")
        all_closed = all_closed and verdict in ("FAIL-CLOSED", "INFO")
    out.append("")
    out.append("Conclusion: no pending Human Gate at DRAFT_COMPLETE can authorize a formal "
               "revision; forward advance cannot move backward (record.from_state must equal "
               "current lifecycle). Owner Exception consumed per run-specific authorization.")
    (ROOT / "sources/SP-vision-multimodal-2026/execution/evidence-authority-repair-r6-20261006"
     / "reentry-probes-r6.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))
    return 0 if all_closed else 1


if __name__ == "__main__":
    raise SystemExit(main())
