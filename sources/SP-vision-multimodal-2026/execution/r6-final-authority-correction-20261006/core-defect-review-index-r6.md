# Shared-Core defect note — Human-gate review-index validator blocks r6 APPROVED (edition-local record, Core untouched)

Date: 2026-10-06/07. Edition: SP-vision-multimodal-2026. Run:
`execution/r6-final-authority-correction-20261006`. Not repaired in shared Core per
production/Core boundary (shared roots read-only in edition production).

## Observed behavior

`scripts/survey_human_gate_v2.py record-architecture-approval` for r6 (state
ARCHITECTURE_ESTABLISHED pending, index ending in r5 APPROVED):

- `_load_review_index` itself raises `HumanGateError: Human Gate review index has
  review after active APPROVED decision: ARCHITECTURE_REVIEW` before writing
  anything (for r5 it passed load and only the trailing index append failed).
- Cause: the r5 index append (completed edition-locally in exact convention per
  `execution/fresh-draft-121-r5-20261006/core-defect-review-index-r5.md`) left two
  consecutive ARCHITECTURE APPROVED rows (r4, r5) with no intervening
  Publication cross-gate reopen. `_validate_review_index_semantics` treats any row
  after an active APPROVED as illegal; ARCHITECTURE REQUEST_CHANGES rows do not
  clear the flag either, so neither the normal loop nor a second post-rewind
  approval can satisfy this validator for the Architecture gate.

## Edition-local handling (exact Core-supported convention, Core untouched)

Performed the EXACT helper steps with Core functions
(`survey_agent_control_v2.approve_architecture`,
`survey_human_gate_v2._snapshot_approval`, `_review_record_payload`,
`survey_production_v2.write_json`, schema validation) in
`execution/r6-final-authority-correction-20261006/record_r6_approval.py`:

- state transition + canonical `gates/architecture-approval.json` via Core
  `approve_architecture` (no index involvement);
- snapshot `gates/reviews/approvals/architecture-r6.json` via Core `_snapshot_approval`;
- record `gates/reviews/architecture-r6.json` via Core `_review_record_payload`
  (revision 6, APPROVED, reviewed commit `31c9ebb1`, actual trio SHAs) +
  `write_json` + record-schema validation;
- review-commit reachability + exact-byte binding re-verified explicitly
  (pre-approval State bytes from the reviewed commit blob);
- index `gates/review-index.json` appended with the r6 APPROVED entry in the
  exact r1–r5 entry convention + index-schema validation (the ONLY manual step).

No shared-Core file modified. Future Core loads of this index under the current
validator will still flag the pre-existing consecutive-APPROVED shape; that is a
Core-maintenance matter, not an edition-content matter. Human review judges the
committed bytes. r1–r5 records/approvals preserved as immutable history.
