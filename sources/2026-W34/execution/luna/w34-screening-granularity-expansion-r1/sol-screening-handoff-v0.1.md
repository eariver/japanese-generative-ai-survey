# W34 event-level Screening handoff — 2026-09-03 r1

Status: **NEEDS_SOL_REVIEW**

## Materialized input

- Event-level Discovery: `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
- Event-level crosswalk: `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`
- Cardinality: 105 records / 105 unique event-level Discovery IDs
- Accounting: `W34-C001`–`W34-C105`, 105/105, missing 0, duplicate 0
- Every event has one or more existing Raw paths and one or more real parent IDs from the accepted 40-record graph.

## Core validation

- Actual `validate_discovery_set()`: PASS.
- Actual `prepare_package()`: BLOCKED before package generation by the existing Production State basis:
  - discovery checkpoint authority path is non-canonical under current Core;
  - `history[1].repository_commit_sha` differs from the authoritative state implementation SHA.
- Prepared package: not created; record/batch counts are therefore unavailable.

## Source boundaries preserved

- DailyX: 7/7 files and 76/76 topic rows; discovery/community signal only.
- Corrected Grok r2: 47/47 URLs; `10 ORDINARY_WINDOW / 20 BACKGROUND_ONLY / 17 LATE_BREAKING`; X Raw remains non-technical.
- Carry-over: `w34-carryover-minimax-unresolved`, `RECHECKED_UNRESOLVED`, represented without current-week promotion.
- Existing authority, chronology, first-party capture, and inherited Raw-index gaps remain explicit; no event was deleted.

## Requested Sol review

Please review the exact Core exception and state-basis mismatch recorded in `validation-v0.1.json`. No Production State, accepted Discovery artifact, shared Core, or downstream Screening artifact was changed. The event-level set should be rerun through current Core only after the state authority is repaired or superseded through the proper process.
