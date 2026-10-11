# W40 r8 compat validation report — evidence-supplement-card-binding-r8

Status: `PROPOSED_NOT_ACCEPTED` (Sol authorization required before any Evidence Acceptance use).
Built: 2026-10-10Z via `build_r8_package.py` (edition-local, frozen Core imports only).

## 1. Zero-drift proof (r7 → r8)

- R8 compat package SHA `30b63b119a63f3fbec9c771aa415b7d7880db8d40a1715930bc063306606818e`
  is BYTE-IDENTICAL to the r7 compat package SHA (same string).
- All 35 derived tasks byte-identical to r7 (`tasks_identical_to_r7: 35/35`); 3 projected +
  3 supplement-bound; supplement manifest r7 reused UNCHANGED (`8012cec0…`).
- Double-build identical; negatives (original-3 + BOGUS) fail closed.
- R8 rebuild under the CURRENT implementation SHA reproduces r7 bytes exactly:
  no source drift, no hidden edits. Lineage r1→r5→r6→r7→r8 recorded per task in
  `projection-ledger-r8.json` (r6→r7→r8 SHAs equal for all 35).

## 2. What r8 changes vs r7 (records/cards only, not package bytes)

- Guard reviewer record: SC-E10 v3-positive cleanup (v1/v2-only chronology).
- 35 Card candidates regenerated under r8 basis (package SHA identical, so 34 cards
  byte-identical to r7; guard card content changed).
- No Discovery/Screening/task-byte change; no supplement change.

## 3. Not authorized by this report

- NOT an Evidence Acceptance; NO `EVIDENCE_REVIEWED`; NO state transition.
- Acceptance (next step, separate frozen-Core call) requires this ledger + SC-E10
  cleanup proof + Sol authorization already recorded in r4 review.
