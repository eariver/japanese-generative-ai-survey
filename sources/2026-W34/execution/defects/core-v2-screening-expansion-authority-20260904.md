# W34 shared-Core defect — Screening expansion authority

Status: **BLOCKING_SHARED_CORE_DEFECT / EDITION_FROZEN_PENDING_CORE_REPAIR**

Issue: `2026-W34`  
Edition branch: `weekly/2026-W34-v2-work`  
Observed at edition HEAD: `01f488f6d7d0feb04198291fe0e21f7ad99390ac`
Reviewed main: `c7a898889463b049dea4ee7337ee16ad5fbf3191`

## Proven-good edition artifacts

The following W34 artifacts are valid and must remain immutable while Core is repaired:

- Production State: `DISCOVERY_COLLECTED / stage:screening`
- accepted Discovery authority: 40 records / 40 unique IDs
- event-level Screening Discovery expansion: 105 records / 105 unique IDs
- Sol Screening decision authority: 105 decisions
  - KEEP 45
  - MAYBE 19
  - INSPECT 16
  - DROP 25
- formal Screening acceptance: PASS
  - path: `sources/2026-W34/screening/v2/accepted/2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662/screening-accepted.json`
  - result-set SHA: `2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662`
  - 105 records / 3 batches

## Exact blocker

Current Core stage validation for `DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED` rejects the valid Screening acceptance with:

`Screening acceptance is not based on accepted Discovery authority`

The accepted Discovery authority is source-centric:

`sources/2026-W34/discovery/discovery-v2.jsonl`

with 40 records.

The accepted Screening package intentionally uses the provenance-preserving event-level expansion:

`sources/2026-W34/screening/input/event-discovery-v2.jsonl`

with 105 records.

All 105 event-level records are valid Discovery-v2 records, bind real accepted parent Discovery IDs, preserve existing Raw paths, and were validated before Screening. The expansion exists because Core Evidence is one-task-per-non-DROP Discovery ID, so source-centric 40-record Screening would collapse multiple independently screenable events.

## Root cause

Current Core has no formal downstream-authority concept for a provenance-preserving Discovery expansion created after initial Discovery acceptance.

At least two current shared-Core locations assume identity instead of validated derivation:

1. `scripts/survey_stage_validation_v2.py`
   - at lifecycle `DISCOVERY_COLLECTED`, requires Screening package `basis.discovery_path` to equal the original accepted Discovery path.

2. `scripts/survey_evidence_v2.py`
   - `validate_screening_acceptance()` requires the caller-supplied Discovery path to equal the Screening package Discovery path.
   - current stage validation later derives that caller path from the original Discovery acceptance, so a valid expansion cannot flow into Evidence.

Therefore relaxing only the Screening-stage check would be insufficient; downstream Evidence/Materiality/Completeness/Selection/Architecture basis derivation must consistently use a validated effective Screening Discovery basis while preserving the original accepted Discovery as root provenance authority.

## Required invariant for Core repair

Core may accept either:

1. the original accepted Discovery set directly; or
2. a derived Screening Discovery set whose provenance is mechanically validated against the accepted Discovery root.

A valid derived set must fail closed unless at minimum:

- every derived record is a valid Discovery-v2 record;
- every derived record uses an expansion origin requiring parent refs;
- every declared parent ref resolves to the accepted root Discovery set;
- every accepted root Discovery record remains downstream-accounted, directly or through one or more derived children;
- every derived Raw path is already present in the union of its declared accepted parents' Raw paths;
- the derived source identity is rooted in at least one declared accepted parent, rather than inventing a new source family;
- issue/profile identity is unchanged;
- package/acceptance hashes bind the exact derived bytes;
- arbitrary unrelated Discovery substitution is rejected.

The accepted root Discovery must remain immutable and independently auditable.

## Required downstream behavior

Once a Screening acceptance has a validated derived Discovery basis, that exact effective Discovery set must be used consistently for:

- Evidence task generation;
- Evidence acceptance validation;
- Edition Views;
- Materiality ledger;
- Profile Completeness;
- Candidate Matrix / Selection;
- Architecture Review summary derivation.

The original accepted Discovery remains the root provenance authority, not the task-granularity basis.

## Edition disposition

Per `AGENTS.md`, shared Core is read-only during edition production. W34 therefore stops here rather than editing `scripts/`, `schemas/`, `config/`, or workflows on the edition branch.

Do not:

- rewrite Production State;
- rewrite the Discovery checkpoint;
- replace the accepted 40-record Discovery acceptance;
- discard the valid 105-record Screening acceptance;
- collapse back to 40 source-centric Screening records merely to satisfy the current validator;
- manually advance lifecycle.

Repair Core separately from current reviewed `main`, run regression including W34 as a read-only reproducer, review/merge that repair, then resume W34 and rerun the failed formal stage validation cleanly under reviewed Core authority.
