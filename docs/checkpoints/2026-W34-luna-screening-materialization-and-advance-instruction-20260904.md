# 2026-W34 Luna — Sol Screening materialization and formal Screening advancement instruction

## 1. Purpose

This is a bounded deterministic/materialization task for Weekly `2026-W34`.

Sol has completed the semantic Screening decisions for all 105 event-level Discovery records. Luna MUST NOT make, revise, reinterpret, rebalance, merge, or omit any Screening decision.

The task is to:

1. verify the exact starting branch state;
2. read the Sol Screening decision authority;
3. deterministically materialize the three Core Screening batch-result JSON files for the already-prepared package;
4. validate every result against the exact current Core contract and package basis;
5. create the formal Screening acceptance using current Core only if the complete result set validates;
6. validate that acceptance;
7. if and only if all validation passes, use the canonical agent-first/operator advancement path to advance `DISCOVERY_COLLECTED` -> `CANDIDATES_NORMALIZED`;
8. stop at `CANDIDATES_NORMALIZED / stage:evidence` without performing Evidence work.

This is not a research task and not an editorial Selection task.

## 2. Required read order

Read, in order:

1. `AGENTS.md`
2. `sources/2026-W34/production-profile.json`
3. `sources/2026-W34/production-state.json`
4. `sources/2026-W34/screening/decisions/sol-screening-decision-authority-20260904-r1.json`
5. `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
6. `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`
7. `sources/2026-W34/screening/v2/prepared/w34-event-screening-r1/package.json`
8. all three package input batches
9. `config/prompts/source-screening-v2.md`
10. `schemas/screening-v2-batch-result.schema.json`
11. `scripts/survey_screening_v2.py`
12. `scripts/survey_agent_tool_v2.py`
13. `scripts/survey_agent_control_v2.py`
14. current operator-bridge documentation required for the formal stage advance.

Do not use W33 semantic decisions as W34 authority.

## 3. Immutable basis

The prepared Screening package is:

`sources/2026-W34/screening/v2/prepared/w34-event-screening-r1/package.json`

Expected package facts:

- schema: `2.0-rc1`
- issue: `2026-W34`
- profile: `WEEKLY`
- input record count: `105`
- batch count: `3`
- batch-001: `43`
- batch-002: `44`
- batch-003: `18`
- repaired Discovery SHA-256: `b63d053f4ea83f3f8150aeb1e3bd196a5d55903d27176fe7a350cf16ebbd5c9e`
- package SHA-256 expected by Sol authority: `547305a3991a5a1e7f633ef2b0188bb4e44c916fc19a1b307778c7e01434e84a`

Before any write, recompute these from the checkout and require exact identity with the Sol authority. If they differ, stop `NEEDS_SOL_REVIEW` without writing results.

## 4. Sol Screening decisions — immutable semantic authority

Authority file:

`sources/2026-W34/screening/decisions/sol-screening-decision-authority-20260904-r1.json`

Expected total:

- KEEP: `45`
- MAYBE: `19`
- INSPECT: `16`
- DROP: `25`
- TOTAL: `105`

The decision sets in that file are final for this Screening pass.

Luna MUST NOT change a decision because of its own assessment of significance, chronology, source quality, or likely article inclusion.

## 5. Deterministic result-field construction

For each event use the exact decision from the Sol authority.

Map event IDs directly:

- `W34-C001` -> `w34-event-c001`
- ...
- `W34-C105` -> `w34-event-c105`

For the result fields follow the exact `materialization_rules` from the Sol authority:

- `decision`: exact Sol assignment.
- `reason`: exact template for that decision class, substituting the Discovery record `source.title` for `<title>`.
- `scope_tags`: derive only from `source.metadata.lane` by the specified deterministic transform.
- `duplicate_group`: exact explicit mapping in the Sol authority; otherwise `null`.
- `verification_targets`: for KEEP/MAYBE/INSPECT use exactly one target from `source.metadata.next_verification` when non-empty, else `source.summary_text`; for DROP use `[]`.
- `confidence`: exact defaults/overrides in the Sol authority.

No additional prose or semantic interpretation may be introduced.

## 6. Batch-result materialization

Create exactly:

- `sources/2026-W34/screening/v2/prepared/w34-event-screening-r1/results/batch-001.json`
- `sources/2026-W34/screening/v2/prepared/w34-event-screening-r1/results/batch-002.json`
- `sources/2026-W34/screening/v2/prepared/w34-event-screening-r1/results/batch-003.json`

Each file must conform exactly to `schemas/screening-v2-batch-result.schema.json` and repeat the exact basis hashes from the package/current package SHA.

Result membership MUST follow the actual batch input files, not an assumed numeric range.

Validation requirements:

- exactly one decision per input Discovery ID;
- no extra ID;
- no duplicate ID;
- union = all 105 event-level IDs;
- aggregate counts = 45/19/16/25 exactly;
- all required fields exact;
- basis hashes exact;
- JSON schema PASS.

## 7. Agent-first compatibility requirement

W34 Production State is agent-first and must be validated with the canonical agent-first path.

Where a Screening helper performs state-basis validation, use `scripts/survey_agent_tool_v2.py` as the compatibility wrapper rather than bypassing it with the legacy direct helper path.

Use the actual current checkout HEAD as the helper implementation SHA whenever the current Core requires one.

Do not edit Production State to satisfy a legacy verifier.

## 8. Formal Screening acceptance

After all three result files validate, invoke the current Core Screening acceptance mechanism against the prepared package and exact result directory.

Requirements:

- complete-only acceptance;
- 105 accepted decisions;
- no missing/extra/duplicate decisions;
- accepted package copy/hash exact;
- result-set content-addressed identity valid;
- acceptance validation PASS using current Core under the canonical agent-first compatibility path where required.

Do not handcraft a fake acceptance record.

## 9. Formal stage advancement

Only after formal Screening acceptance validates:

Use the canonical current operator/agent-control path to advance exactly one stage:

`DISCOVERY_COLLECTED` -> `CANDIDATES_NORMALIZED`

Expected resulting next action:

`stage:evidence`

The advancement must be an ordinary fast-forward workflow/operator action. No force, reset, rewrite, rebase, manual state mutation, or inferred Human approval.

Stop immediately after confirming the formal Screening checkpoint is `passed` and Evidence is still `pending`.

## 10. Write allowlist

You may write only:

- `sources/2026-W34/screening/v2/prepared/w34-event-screening-r1/results/**`
- the content-addressed formal Screening acceptance directory produced by current Core;
- the exact operator request/receipt/checkpoint/state paths produced by the canonical advancement mechanism;
- `sources/2026-W34/execution/luna/w34-screening-materialization-r1/**`

Do not modify:

- `sources/2026-W34/screening/decisions/sol-screening-decision-authority-20260904-r1.json`
- repaired `event-discovery-v2.jsonl`
- crosswalk
- accepted 40-record Discovery
- Discovery acceptance/checkpoint
- existing Raw
- shared Core
- W33
- any Human Gate record.

## 11. Forbidden work

Do not perform:

- new research/source intake;
- Evidence verification or acceptance;
- Materiality;
- Completeness judgment;
- Candidate Selection;
- Architecture;
- reader-facing drafting;
- Human Gate action;
- Freeze/Release.

## 12. Failure behavior

If any basis, materialization, result, acceptance, or advancement validation fails:

- do not alter Sol decisions;
- do not repair shared Core;
- do not manually patch Production State;
- preserve exact failure evidence;
- stop `NEEDS_SOL_REVIEW`.

## 13. Required completion report

Report at minimum:

- Branch
- Exact Starting SHA
- Ending SHA
- ahead / behind / commit count
- all changed paths
- Production State before / after
- Screening package SHA and Discovery basis SHA
- batch result counts and hashes
- aggregate KEEP/MAYBE/INSPECT/DROP counts
- 105/105 decision accounting, missing/extra/duplicate counts
- formal Screening acceptance path and SHA/result-set identity
- acceptance validation result
- operator/workflow run information if used
- formal Screening checkpoint result
- resulting lifecycle state / next action
- confirmation Evidence/Materiality/Selection/Architecture were not performed
- any remaining INSPECT/MAYBE verification obligations preserved for Evidence work.

Success stop state:

`CANDIDATES_NORMALIZED / stage:evidence`
