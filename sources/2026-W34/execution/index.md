# Survey Production execution index — 2026-W34

This is the edition-local navigation record. Machine lifecycle authority remains `sources/2026-W34/production-state.json`.

## Current authority

- Issue / edition: `2026-W34`
- Research Profile: `WEEKLY`
- Publication Profile: `WEEKLY_MAGAZINE`
- Work branch: `weekly/2026-W34-v2-work`
- Reviewed `main`: `c7a898889463b049dea4ee7337ee16ad5fbf3191`
- Current lifecycle: `DISCOVERY_COLLECTED`
- Current next action: `stage:screening`
- Discovery checkpoint: `passed`
- Screening checkpoint: `pending`
- Human gates: Architecture Review pending; Publication Preview pending

## Accepted Discovery and event-level Screening basis

- accepted Discovery: `sources/2026-W34/discovery/discovery-v2.jsonl`
  - 40 records / 40 unique IDs
- accepted Discovery acceptance: `sources/2026-W34/discovery/discovery-accepted-v2.json`
- event-level Screening Discovery expansion: `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
  - 105 records / 105 unique IDs
  - W34-C001–W34-C105: 105/105, missing 0, duplicate 0
- event-level crosswalk: `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`
- DailyX: 7/7 files, 76/76 topics
- Grok r2: 47/47 URLs; 10 ordinary / 20 background / 17 late-breaking
- carry-over: one `RECHECKED_UNRESOLVED`; no promotion

## Screening

Sol semantic authority:

`sources/2026-W34/screening/decisions/sol-screening-decision-authority-20260904-r1.json`

Decision counts:

- KEEP: 45
- MAYBE: 19
- INSPECT: 16
- DROP: 25
- TOTAL: 105

Prepared package:

`sources/2026-W34/screening/v2/prepared/w34-event-screening-r1/package.json`

Formal Screening acceptance is valid:

`sources/2026-W34/screening/v2/accepted/2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662/screening-accepted.json`

- result-set SHA: `2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662`
- 105 records / 3 batches
- Screening acceptance validation: PASS

## Current blocker

Formal stage validation for `DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED` fails with:

`Screening acceptance is not based on accepted Discovery authority`

The validator requires Screening to use the original accepted 40-record Discovery path exactly, while the valid Screening acceptance uses the 105-record provenance-preserving event-level expansion required for downstream event-level Evidence tasks.

This is recorded as a shared-Core defect at:

`sources/2026-W34/execution/defects/core-v2-screening-expansion-authority-20260904.md`

Per `AGENTS.md`, no shared-Core file is repaired on the edition branch. W34 remains frozen at `DISCOVERY_COLLECTED / stage:screening` pending separately reviewed Core repair.

## Relevant execution records

- Discovery materialization: `sources/2026-W34/execution/sessions/w34-luna-discovery-materialization-20260903-r1.md`
- Discovery binding repair: `sources/2026-W34/execution/sessions/w34-luna-discovery-binding-repair-20260903-r1.md`
- Screening granularity expansion: `sources/2026-W34/execution/luna/w34-screening-granularity-expansion-r1/`
- event JSONL byte repair: `sources/2026-W34/execution/luna/w34-event-discovery-byte-repair-r1/`
- Screening materialization: `sources/2026-W34/execution/luna/w34-screening-materialization-r1/`

## Forbidden while Core repair is pending

- no Production State manual edit
- no Discovery rollback/reacceptance
- no accepted Discovery/checkpoint rewrite
- no Screening decision reinterpretation
- no manual lifecycle advancement
- no Evidence/Materiality/Completeness/Selection/Architecture
- no shared-Core edits on the W34 branch
- no W33 changes
- no force/reset/rewrite/rebase

## Current disposition

`SCREENING_ACCEPTED / SHARED_CORE_EXPANSION_AUTHORITY_BLOCKER / CORE_MAINTENANCE_REQUIRED`
