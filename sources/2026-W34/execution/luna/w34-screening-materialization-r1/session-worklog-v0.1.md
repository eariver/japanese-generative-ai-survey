# W34 Luna — Screening materialization and advance

## Starting authority

- Branch: `weekly/2026-W34-v2-work`
- Exact starting SHA and verified local HEAD: `3371ba18fb8058a50585cefd0b87ed59e44b10bb`
- Remote start guard: PASS; the remote branch HEAD matched exactly before any write.
- Production State: `DISCOVERY_COLLECTED`, next action `stage:screening`.
- Sol authority: `sources/2026-W34/screening/decisions/sol-screening-decision-authority-20260904-r1.json`.

## Actions actually performed

1. Revalidated the immutable prepared package (`2.0-rc1`, `2026-W34`, `WEEKLY`, 105 records, batches 43/44/18) and all Sol basis hashes.
2. Revalidated the repaired event-level Discovery input and accepted 40-record Discovery graph without modifying either.
3. Materialized exactly one result decision for every prepared-package input record from Sol's deterministic rules. Counts are KEEP 45, MAYBE 19, INSPECT 16, DROP 25.
4. Ran the canonical agent-first wrapper for Screening acceptance using actual checkout implementation SHA `3371ba18fb8058a50585cefd0b87ed59e44b10bb`.
5. Re-ran the wrapper acceptance path and independently validated the content-addressed formal acceptance: 105 records, 3 batches, result-set SHA `2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662`.
6. Ran the current Core screening stage-contract validation with the accepted Screening artifact.

## Deterministic execution

- Result files were schema-validated and batch-validated against the immutable package basis.
- Event accounting is `W34-C001`–`W34-C105`: 105 accounted, missing 0, duplicate 0, extra 0.
- Accepted parent Discovery IDs and all event-local Raw paths validated.
- Agent-first Production State validation passed before acceptance; State bytes remained unchanged.

## Deviations / failures

The current Core stage validator failed with the exact exception:

`Screening acceptance is not based on accepted Discovery authority`

The accepted Discovery authority points to the 40-record graph at `sources/2026-W34/discovery/discovery-v2.jsonl`, while the immutable Screening package correctly binds the 105-record event-level input at `sources/2026-W34/screening/input/event-discovery-v2.jsonl`. No inferred workaround, custom checkpoint, operator advancement request, manual State edit, or shared-Core change was made.

## End state

`NEEDS_SOL_REVIEW`.

Formal Screening acceptance is valid and retained. Formal lifecycle advancement was not performed. Production State remains `DISCOVERY_COLLECTED / stage:screening`; Screening checkpoint remains pending. Evidence/Materiality/Completeness/Selection/Architecture/Human Gate/draft/Freeze/Release work was not performed.
