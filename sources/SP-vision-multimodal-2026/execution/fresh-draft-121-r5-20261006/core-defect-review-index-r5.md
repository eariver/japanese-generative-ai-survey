# Shared-Core defect note — Human-gate review-index validator blocks consecutive APPROVED (edition-local record, Core untouched)

Date: 2026-10-06. Edition: SP-vision-multimodal-2026. Not repaired in shared Core per production/Core boundary.

## Observed behavior

`scripts/survey_human_gate_v2.py record-architecture-approval` for r5 (after post-freeze rewind left state pending with index ending in r4 APPROVED):

- `_load_review_index` passed (index ending with active APPROVED is loadable);
- `agent.approve_architecture` updated state + wrote canonical `gates/architecture-approval.json`;
- review record `gates/reviews/architecture-r5.json` + snapshot `gates/reviews/approvals/architecture-r5.json` written;
- `_write_review_record` then failed at `_validate_review_index_semantics` on the appended index with `Human Gate review index has review after active APPROVED decision: ARCHITECTURE_REVIEW`, leaving `gates/review-index.json` un-updated.

## Analysis

The validator treats any review row after an active APPROVED as illegal, with the only clearing path being a Publication cross-gate reopen. There is no clearing path for a legitimate second Architecture APPROVED after a Core-controlled rewind that supersedes the active approval without an intervening Human REQUEST_CHANGES (exactly the post-freeze-integrity r5 situation). ARCHITECTURE REQUEST_CHANGES rows likewise do not clear the flag, so even the normal request-changes-then-re-approve loop cannot satisfy this validator for the Architecture gate.

## Edition-local handling

Completed the missing mechanical step only: appended the r5 APPROVED entry (`architecture-r5.json` SHA-256 `3ff5aba8276d15dcc19af3435351284232d6f0482fcfbdbf5ac39572ba5e0286`) to `gates/review-index.json` in the exact r1-r4 entry convention. No shared-Core file modified. Future Core loads of this index under the current validator will still flag it; that is a Core-maintenance matter, not an edition-content matter. Human review judges the committed bytes.
