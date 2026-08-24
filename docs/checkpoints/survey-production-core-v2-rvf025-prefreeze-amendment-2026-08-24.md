# Survey Production Core v2 — RVF-025 pre-freeze checkpoint amendment

Status: `PF-005 COVERAGE HARDENING ADDED / EXACT-HEAD CI REQUIRED`

Recorded: 2026-08-24 JST

This amendment supersedes only the sequencing statement in `survey-production-core-v2-rvf025-prefreeze-2026-08-24.md` that its own commit was expected to be the last candidate-tree mutation. The earlier checkpoint remains valid historical evidence for PF-001 through PF-004 and the diagnostic CI on `04043b2d71b8ce00b53ef4dce1c59e0ad7956af0`.

## PF-005 — Point-7 mandatory matrix coverage was incomplete

During pre-freeze mapping of `docs/survey-production-core-v2-final-audit-rule.md` Point 7 to concrete regressions, the implementation was found to contain the required generic behavior, but three mandatory claims were not each represented by explicit regression evidence:

1. Architecture `REQUEST_CHANGES` must round-trip from **every** configured pre-Architecture regeneration boundary, not only `SELECTION_COMPLETE`.
2. reviewed-commit durability must explicitly reject a reviewed Gate-input path whose Git tree entry is non-regular.
3. r1 `APPROVED` at each normal Human Gate should explicitly prove its immediate continuation edge: Architecture -> drafting and Publication Preview -> Freeze.

No frozen candidate existed when this gap was found, so no audit verdict was invalidated.

Repair commit before this amendment:

`9e22db5611b283a6be949b9b0e986a0b811ab940`

New regression:

`tests/test_survey_human_gate_audit_matrix_v2.py`

It adds:

- Architecture r1 `REQUEST_CHANGES` -> each of `ISSUE_INITIALIZED`, `DISCOVERY_COLLECTED`, `CANDIDATES_NORMALIZED`, `EVIDENCE_REVIEWED`, and `SELECTION_COMPLETE` -> deterministic replay -> Architecture r2 -> `APPROVED` -> drafting;
- direct Architecture r1 `APPROVED` -> drafting;
- direct Publication Preview r1 `APPROVED` -> Freeze;
- a durable reviewed commit whose Architecture Gate input is represented by a symlink-mode Git tree entry -> fail closed as non-regular.

The existing regressions continue to own stale r1 rejection, changed-byte rejection, missing/dangling reviewed commit rejection, publication-local r2, exact Candidate/PDF rebinding, connector bridge round trips, and Publication -> upstream Architecture reopen/preserved approval-history behavior.

## New pre-freeze boundary

The commit produced by this amendment is the new pre-freeze head. It is **not frozen and not accepted** until both required workflows pass on that exact SHA.

Required sequence from this amendment:

```text
exact-head Survey Production Core v2 CI PASS
+ exact-head Pipeline contract tests PASS
-> confirm PR head/base/scope unchanged
-> declare exact SHA frozen outside candidate tree
-> perform Points 1-7 from Point 1 with no inherited verdict
-> no candidate-tree mutation during audit
```

Any test failure or audit defect that requires a repository change supersedes this amendment and requires a new pre-freeze head. W33/SP001 remain paused until reviewed unchanged Core integration.
