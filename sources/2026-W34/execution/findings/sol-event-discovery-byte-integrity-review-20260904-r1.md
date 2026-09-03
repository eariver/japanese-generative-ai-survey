# W34 Sol review — event-level Screening Discovery byte-integrity repair

Status: `SOL_REPAIR_AUTHORIZED / EDITION_LOCAL_INPUT_ONLY`

Issue: `2026-W34`  
Branch: `weekly/2026-W34-v2-work`
Reviewed branch HEAD before this decision: `e156ecbc2f3c3b297e06faa89f6d30e7c3ce73bf`

## 1. Finding

The canonical agent-first Screening wrapper retry correctly passed the current agent-first Production State validation, then failed while reading:

`sources/2026-W34/screening/input/event-discovery-v2.jsonl`

with:

```text
'utf-8' codec can't decode byte 0xaa in position 1: invalid start byte
```

The failure occurred before Screening package creation.

The committed GitHub object at the reviewed HEAD is:

- path: `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
- Git blob SHA: `20b394ea7bb0ca4cb32a90f31678d1045678255b`
- byte count: `210060`
- observed committed-byte SHA-256 from the Luna retry: `a15ddbde1bc3b35ab158d68a50313294091aa33f2d942d2e24d3d578f5344321`
- UTF-8 JSONL parse: `FAIL`

The earlier expansion session recorded a locally validated 105-record / 105-ID representation and recorded SHA-256:

`5dbdcbfd70dc1e4605560dc06fc89e940141116b0bf9bf8eefaef6f8bf9f2332`

That historical digest is useful as diagnostic evidence but **must not be treated as the required target hash** unless the exact deterministic reconstruction genuinely reproduces it. The authority is the semantic/crosswalk contract, not a stale expected byte string.

## 2. What remains valid

The following are independently preserved and are not part of the corruption:

- Production State: `DISCOVERY_COLLECTED / stage:screening`;
- accepted Discovery graph: 40 records / 40 unique IDs;
- accepted Discovery checkpoint and acceptance bytes;
- `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`;
- crosswalk cardinality: 105/105 events, missing 0, duplicate 0;
- event Discovery IDs: `w34-event-c001` through `w34-event-c105`;
- all accepted-parent references resolve to the accepted 40-record graph;
- all 36 unique Raw paths referenced by the crosswalk exist;
- DailyX 7/7 files and 76/76 topics;
- corrected Grok r2 47/47 URLs and classification 10 ordinary / 20 background / 17 late-breaking;
- carry-over remains `RECHECKED_UNRESOLVED` without promotion;
- no Screening decision/result/acceptance exists.

The crosswalk explicitly preserves, per event, the event ID/title, event-level Discovery ID, accepted parent IDs, Raw paths, source locator/type, lane, pre-Screening status, chronology qualifier, authority qualifier, expansion rationale, and next-verification intent.

## 3. Disposition

This is **not** a shared-Core defect and **not** a Discovery-semantic failure.

It is an edition-local byte-integrity/materialization defect in a non-accepted Screening input artifact.

The corrupted file may therefore be replaced in place, provided that:

1. the semantic event set remains exactly `W34-C001` through `W34-C105`;
2. the generated event Discovery IDs remain exactly `w34-event-c001` through `w34-event-c105`;
3. every generated record is derived from the existing crosswalk / Sol inventory / accepted parent graph / existing Raw only;
4. no new research, Screening judgment, Evidence judgment, or candidate pruning is performed;
5. actual current `survey_screening_v2.validate_discovery_set()` passes on the rebuilt file;
6. the canonical `survey_agent_tool_v2.py` wrapper successfully prepares the Screening package;
7. byte identity is verified **before and after Git commit**.

## 4. Reconstruction authority

Use, in order:

1. `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`
2. `sources/2026-W34/intake/working-set/sol-discovery-event-inventory-v0.2.md`
3. `sources/2026-W34/discovery/discovery-v2.jsonl` (accepted 40-record parent graph)
4. existing Raw paths already named by the crosswalk
5. current `scripts/survey_screening_v2.py` Discovery validation contract

Do not attempt to decode or salvage semantics from the corrupted bytes themselves.

## 5. Required byte-integrity protocol

Before replacing the committed file:

- generate a fresh UTF-8 JSONL candidate at a temporary local path;
- parse every line as JSON;
- run actual current `validate_discovery_set()`;
- prove 105 records / 105 unique event-level IDs;
- prove exact event-ID mapping via the crosswalk;
- compute SHA-256 and byte count of the candidate;
- retain this as `pre_commit_sha256` / `pre_commit_byte_count`.

After committing/pushing the replacement:

- read the exact committed GitHub blob / raw file back from the new remote HEAD;
- compute SHA-256 and byte count from the committed bytes;
- require equality with the pre-commit candidate;
- perform a fresh UTF-8 JSONL parse from the committed bytes;
- rerun actual current `validate_discovery_set()` against a fresh checkout or exact remote-HEAD worktree;
- only then run the canonical agent-first Screening wrapper and package validation.

If any pre/post byte mismatch occurs, stop `NEEDS_SOL_REVIEW`; do not proceed to Screening.

## 6. Scope guard

Do not modify:

- `sources/2026-W34/production-state.json`;
- accepted Discovery JSONL/acceptance/checkpoint;
- `event-discovery-crosswalk-v0.1.json`;
- existing Raw;
- shared Core;
- W33;
- any Screening decision/result/acceptance;
- any Evidence/Materiality/Completeness/Selection/Architecture artifact.

No force/reset/rewrite/rebase/new branch.

## 7. Next bounded action

Luna may perform an edition-local repair of the corrupted event-level Screening input and prove remote byte identity plus canonical wrapper package preparation. Stop at `READY_FOR_SOL_SCREENING` if and only if all checks pass.
