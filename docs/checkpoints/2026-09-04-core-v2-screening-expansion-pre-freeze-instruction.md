# Core v2 Screening expansion authority — pre-freeze candidate instruction

Status: **LUNA PRE-FREEZE EXECUTION AUTHORITY**

## 1. Repository / branch guard

Repository:
`eariver/japanese-generative-ai-survey`

Branch:
`fix/core-v2-screening-expansion-authority-20260904`

This task continues the existing Core maintenance branch. Do not create a new, fallback, repair, review, iteration, or replacement branch.

At task start, verify that the remote branch HEAD exactly matches the Exact Starting SHA supplied by Sol. If it does not, perform no repository/GitHub writes and stop with the actual remote HEAD.

## 2. Purpose

The Screening expansion + active Screening acceptance repair has passed Sol implementation review and targeted regressions. This task does **not** perform the final seven-point audit.

This task performs only the mandatory work immediately before candidate freeze:

1. synchronize current repository authority/worklog with the implemented repair and current seven-point audit rule;
2. run pre-freeze cross-checks against the full branch scope;
3. create/open one draft integration PR from this maintenance branch to `main` if none exists;
4. obtain exact-head diagnostic CI on the final candidate head;
5. stop with one exact immutable **FROZEN CANDIDATE SHA** for the subsequent read-only seven-point audit.

Do not run or claim the final seven-point audit in this task.

## 3. Mandatory read order

Read in this order before editing:

1. `AGENTS.md`
2. `docs/survey-production-core-v2-authority.md`
3. `docs/survey-production-core-v2-final-audit-rule.md`
4. `docs/survey-production-core-v2-session-bootstrap.md`
5. `docs/survey-production-core-v2-postintegration-amendment.md`
6. `docs/checkpoints/survey-production-core-v2-worklog.md`
7. `docs/checkpoints/2026-09-04-core-v2-screening-expansion-authority-repair-instruction.md`
8. `docs/checkpoints/2026-09-04-core-v2-screening-expansion-authority-repair-validation-r2.md`
9. `docs/checkpoints/2026-09-04-core-v2-screening-active-acceptance-sol-review.md`
10. `docs/checkpoints/2026-09-04-core-v2-screening-active-acceptance-repair-instruction.md`
11. `docs/checkpoints/2026-09-04-core-v2-screening-active-acceptance-repair-validation-r3.md`

Repository reality outranks historical status text.

## 4. Sol review disposition

Treat the current repair logic as accepted for pre-freeze preparation unless your cross-check finds a concrete defect.

The following invariants must remain unchanged:

- direct accepted Discovery remains valid;
- a derived Screening Discovery requires exact accepted-root parent closure;
- every accepted root must be accounted by at least one derived child;
- arbitrary unrelated Discovery substitution fails closed;
- derived Raw paths stay inside declared-parent Raw union;
- stable source identity is rooted in declared accepted parents;
- obligation invention is rejected;
- accepted Screening runs are immutable historical storage;
- after Screening advancement, active Screening acceptance is selected only by the passed State-bound Screening Stage Checkpoint;
- active selection is independent of accepted-directory count/order/mtime/digest order;
- downstream Evidence and Selection/Architecture use the exact effective Discovery basis and active Screening authority;
- W34 temporary corrected fixture remains 40 accepted roots -> 110 derived rows -> 40/40 accounted -> 45 KEEP / 19 MAYBE / 16 INSPECT / 30 DROP -> 80 Evidence tasks.

Do not weaken any of these to make an audit easier.

## 5. Authority synchronization required before freeze

The current candidate contains stale current-facing authority text inherited from the old pre-integration improvement branch. In particular, current repository reality already shows examples such as:

- `docs/survey-production-core-v2-authority.md` still naming `refactor/survey-production-core-v2`, PR `#310`, and a six-point audit;
- `docs/checkpoints/survey-production-core-v2-worklog.md` still naming the same historical branch/PR and six-point final audit;
- the canonical final audit rule is now seven-point;
- W34 is an active production regression edition, not `NOT STARTED`.

Synchronize current-facing authority without rewriting historical audit documents.

At minimum update:

- `docs/survey-production-core-v2-authority.md`
- `docs/checkpoints/survey-production-core-v2-worklog.md`

Also inspect:

- `docs/survey-production-core-v2-session-bootstrap.md`
- `docs/survey-production-core-v2-postintegration-amendment.md`

Only edit those latter documents if a current-facing statement is materially stale or contradicts the present seven-point / post-integration authority. Do not gratuitously rewrite historical context.

Authority synchronization must explicitly record the generic semantic additions introduced by this maintenance candidate:

1. **root Discovery authority vs effective downstream Discovery basis**;
2. a derived Screening Discovery is legal only through complete, mechanically validated accepted-root provenance closure;
3. **historical Screening acceptances vs active Screening acceptance**;
4. active Screening authority is the exact acceptance adopted by the passed Screening Stage Checkpoint, never directory cardinality/latest heuristics;
5. downstream Evidence/materiality/completeness/Selection/Architecture must follow that active/effective authority chain;
6. content-addressed historical runs remain immutable evidence;
7. production editions do not repair shared Core in place.

Do not create a parallel lifecycle, profile-specific workaround, W34-specific Core rule, or new Human Gate.

## 6. Seven-point audit wording synchronization

`docs/survey-production-core-v2-final-audit-rule.md` is canonical for the seven-point fixed-head audit.

All current-facing authority/worklog references must agree with exactly these seven acceptance points:

1. Weekly viability
2. Special viability
3. Generality
4. Historical/clarified recurrence prevention
5. Control proportionality
6. Autonomous progression / stop discipline
7. Human Gate round-trip viability

Do not preserve current-facing six-point wording.

Do not edit the final audit rule merely to change candidate status or record this task's PASS. Edit it only if a genuine contradiction is found.

## 7. Pre-freeze full-scope cross-check

Compare current branch against reviewed `main`.

Reviewed main baseline at Sol handoff:
`c7a898889463b049dea4ee7337ee16ad5fbf3191`

If main has moved at task start, record the actual main HEAD and determine whether the candidate can still be audited against the new base without changing repair semantics. Do not silently assume the old base.

Check all cumulative branch paths, not only the most recent commit.

Confirm:

- no W34/W33 production files are changed by the maintenance branch;
- no unrelated publication/editorial behavior is changed;
- no eighth workflow exists;
- direct/non-expanded Screening path remains backward compatible;
- strict expansion and active-acceptance tests remain present;
- all current authority text agrees with repository reality;
- candidate does not rely on chat-only facts for merge safety.

If this cross-check finds a semantic/code defect requiring implementation change, repair it now, rerun all affected tests, resynchronize authority, and do **not** carry forward earlier PASS evidence. If the required change is larger than this maintenance scope, stop `NEEDS_SOL_REVIEW`.

## 8. Local diagnostic regression before PR freeze

Run at minimum:

### A. Active authority + expansion + affected Core

- `tests.test_survey_active_screening_acceptance_v2`
- `tests.test_screening_expansion_authority_v2`
- `tests.test_survey_screening_v2`
- `tests.test_survey_screening_archive_v2`
- `tests.test_accept_screening_results`
- `tests.test_survey_agent_control_v2`
- `tests.test_survey_agent_tool_v2`
- `tests.test_survey_stage_validation_v2`
- `tests.test_survey_evidence_v2`
- `tests.test_run_evidence_v2_agent_first`
- `tests.test_run_selection_architecture_v2_interactive`

### B. Downstream contracts

- completeness/materiality
- candidate selection
- architecture
- Human Gate round-trip/direct reviewed-commit durability tests
- operator bridge trust/bootstrap tests
- canonical Thematic initialization tests

### C. Repository/schemas

- repository contract syntax
- schema/config parsing/compile checks
- workflow count exactly seven

### D. Full Python diagnostic

Run the repository's full Python test suite. Existing unrelated failures may remain diagnostic-only only if their exact names/reasons are unchanged and no changed path is implicated. Any new failure blocks freeze.

## 9. Draft integration PR and exact-head CI

There is no integration PR for this maintenance branch at Sol handoff.

After all intended code/test/doc/worklog edits are committed and pushed, create one **draft** PR:

- head: `fix/core-v2-screening-expansion-authority-20260904`
- base: `main`
- purpose: Core maintenance candidate review/CI only
- do not merge it

Use a normal integration PR title, not the reserved `Survey Core operator transport:` prefix.

The PR is not a Human Gate decision and not production transport.

The final candidate head must receive exact-head CI evidence from at least:

- `Survey Production Core v2 CI`
- `Pipeline contract tests`

These workflows are PR-triggered for relevant paths. Confirm the workflow run/head SHA equals the final candidate SHA exactly.

Also confirm any other required/triggered checks on that PR are green or explicitly understood as unrelated existing diagnostics.

If CI failure requires a repository mutation:

1. candidate is not frozen;
2. repair;
3. rerun local diagnostics;
4. resynchronize authority if needed;
5. push new head;
6. obtain fresh exact-head CI on the new head.

## 10. Candidate freeze rule

Only after all intended candidate changes are complete, authority synchronized, local diagnostics acceptable, PR scope cross-checked, and exact-head CI green:

- designate the exact branch HEAD as `FROZEN CANDIDATE SHA`;
- verify branch HEAD read-back equals it;
- verify PR head equals it;
- verify main/base SHA used for audit;
- record PR number and exact CI run IDs in the completion report.

**Do not commit a post-freeze PASS/freeze record into the candidate tree.**

The frozen SHA itself is the boundary. Final audit evidence belongs outside the candidate tree, normally PR/Human-review metadata.

After freeze, make no further candidate-tree mutations in this task.

## 11. Do not run the final audit yet

This task must stop before the fresh seven-point fixed-head audit.

Do not claim Point 1..7 PASS here.

Do not merge to main.

Do not modify W34/W33.

Do not continue W34 production using unmerged Core.

The next Sol/Luna task will run all seven acceptance points from zero on the exact frozen SHA with no tree changes.

## 12. Completion report

Return:

- Exact Starting SHA
- Ending/FROZEN CANDIDATE SHA
- start->end ahead/behind/commit count
- current main/base SHA
- cumulative candidate changed paths vs main
- authority files changed and why
- confirmation current-facing six-point/old-branch/old-PR stale text is removed where applicable
- local targeted test commands/results
- full-suite diagnostic summary
- draft PR number/URL
- exact PR head SHA
- Survey Production Core v2 CI run ID/status/head SHA
- Pipeline contract tests run ID/status/head SHA
- workflow count
- W34/W33/main write status
- confirmation no tree mutation occurred after candidate freeze
- final disposition exactly one of:
  - `FROZEN_CANDIDATE_READY_FOR_SEVEN_POINT_AUDIT`
  - `NEEDS_SOL_REVIEW`

Do not report `7/7 PASS` in this task.
