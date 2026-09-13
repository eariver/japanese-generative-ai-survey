# W34 Luna instruction — post-PR #483 Core sync + Screening recovery

Status: `BOUND_EXECUTION_INSTRUCTION`

Date: 2026-09-05 JST

## 1. Exact start guard

Repository:
`eariver/japanese-generative-ai-survey`

Existing branch:
`weekly/2026-W34-v2-work`

Exact Starting SHA:
`aa41ccd55ed630fa96c05efa3658bb403a779fba`

Reviewed main that must be synchronized:
`a9f121f0d65591f52b53515712d7c0bae573b2ef`

At start, read-only verify BOTH:

1. remote W34 branch HEAD == exact Starting SHA;
2. remote `main` HEAD == exact reviewed main SHA.

If either differs, perform no write and report actual SHAs.

No new branch, fallback branch, repair branch, review branch, reset, rebase, rewrite, or force update.

## 2. Mandatory W34 authority to read

Before writes, read at least:

- `AGENTS.md`
- `docs/survey-production-core-v2-session-bootstrap.md`
- `docs/survey-production-core-v2-authority.md`
- `docs/survey-production-core-v2-issue-prevention-checklist.md`
- `docs/survey-production-core-v2-final-audit-rule.md`
- `sources/2026-W34/production-profile.json`
- `sources/2026-W34/production-state.json`
- `sources/2026-W34/discovery/discovery-v2.jsonl`
- `sources/2026-W34/discovery/discovery-accepted-v2.json`
- `sources/2026-W34/orchestration/v2/checkpoints/ISSUE_INITIALIZED.json`
- `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
- `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`
- `sources/2026-W34/screening/decisions/sol-screening-decision-authority-20260904-r1.json`
- `sources/2026-W34/screening/decisions/sol-screening-coverage-supplement-20260905-r1.json`
- historical Screening acceptance `sources/2026-W34/screening/v2/accepted/2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662/screening-accepted.json`
- `sources/2026-W34/execution/defects/core-v2-screening-expansion-authority-20260904.md`
- `sources/2026-W34/execution/findings/sol-external-sidecar-qa-pilot-plan-20260905-r1.md`

The sidecar plan is future publication QA authority only. Do not run either external tool in this task.

## 3. Synchronize reviewed Core into W34

Merge reviewed `main@a9f121f0d65591f52b53515712d7c0bae573b2ef` into the existing W34 branch with a normal non-force merge.

Do not rebase W34 and do not rewrite its history.

The merge must preserve all edition-local W34 artifacts and adopt the reviewed shared-Core tree from `main`.

If a merge conflict occurs in a shared Core root, do not invent a hybrid implementation. Preserve reviewed-main Core authority unless an edition-local file is clearly outside the shared roots. If resolution is not mechanically obvious, stop `NEEDS_SOL_REVIEW` before writing a conflict guess.

After merge, verify:

- W34 branch contains `main@a9f121f0...` as ancestor;
- reviewed Core files equal main bytes;
- W34 Production State has not been manually rewritten merely because Core implementation advanced;
- `survey_agent_control_v2.validate_agent_state()` passes on the existing W34 State.

Per agent-first Core policy, later checkpoints/actions may use newer reviewed implementation provenance. Do not normalize historical State history SHAs to the new Core SHA.

## 4. Revalidate only the affected accepted boundary

Before changing Screening input, verify current historical authorities:

- Production State = `DISCOVERY_COLLECTED / stage:screening`;
- accepted root Discovery remains exactly 40 records / 40 unique root IDs;
- Discovery acceptance remains valid and unchanged;
- Discovery Stage Checkpoint remains valid and unchanged;
- existing historical 105-record Screening acceptance remains immutable and valid as historical evidence;
- existing 105 Sol semantic decisions remain unchanged.

Do not reopen or rerun formal Discovery.

## 5. Correct the derived Screening Discovery to complete root closure

The reviewed Core correctly rejects the current 105-record derived set because five accepted GitHub Releases roots are not present in its parent closure.

Create the corrected current derived Screening set with exactly 110 records:

- preserve all existing 105 event-level derived records byte-semantically except canonical JSONL rewrite/order mechanics if required;
- append exactly the five coverage passthrough children authorized by `sol-screening-coverage-supplement-20260905-r1.json`;
- do not add a sixth coverage child or any new editorial event;
- do not mutate the accepted 40-record root Discovery.

Required new children:

- `w34-coverage-comfy-org-comfyui`
- `w34-coverage-ggml-org-llama-cpp`
- `w34-coverage-nvidia-tensorrt-llm`
- `w34-coverage-sgl-project-sglang`
- `w34-coverage-vllm-project-vllm`

Each child must follow the supplement exactly:

- one exact accepted root parent;
- parent-requiring origin;
- exact copied parent source object;
- parent Raw paths only;
- exact parent obligations only;
- explicit coverage-only rationale;
- not presented as a new W34 event.

Update the current Screening input path:

`sources/2026-W34/screening/input/event-discovery-v2.jsonl`

Do not delete historical accepted package inputs. Historical acceptance remains content-addressed evidence.

Create a new provenance/crosswalk record for the corrected 110-record basis rather than rewriting the historical 105-event crosswalk's meaning. A recommended path is:

`sources/2026-W34/screening/input/event-discovery-crosswalk-v0.2.json`

It must preserve 105 event mappings and add the 5 coverage mappings explicitly as `COVERAGE_PASSTHROUGH` or equivalent non-event role.

## 6. Strict expansion validation

Run reviewed post-#483 Core expansion validation against:

- accepted root = 40;
- current derived = 110.

Required:

- root records: 40
- derived records: 110
- unique derived IDs: 110
- accounted root IDs: 40
- unaccounted root IDs: 0
- unknown parent refs: 0
- invented Raw paths: 0
- source identity substitution: 0
- invented obligations: 0
- duplicate derived IDs: 0

Any failure is `NEEDS_SOL_REVIEW`; do not weaken Core validation.

## 7. New Screening package and decisions

Prepare a NEW Screening package for the 110-record current derived basis.

Recommended run ID:
`w34-event-screening-r2`

Use the canonical agent-first wrapper:

`scripts/survey_agent_tool_v2.py`

Do not invoke a legacy helper directly around agent-first State semantics.

The helper implementation SHA must equal the actual current checkout HEAD at package-preparation time.

Do not overwrite/delete the historical r1 prepared/accepted run.

Materialize decisions mechanically from two Sol authorities:

1. the historical 105 decisions in `sol-screening-decision-authority-20260904-r1.json` — unchanged;
2. the five exact `DROP` coverage decisions in `sol-screening-coverage-supplement-20260905-r1.json`.

Expected exact totals:

- KEEP 45
- MAYBE 19
- INSPECT 16
- DROP 30
- TOTAL 110

No Luna semantic reinterpretation is allowed.

Expected non-DROP set: exactly 80.

All batch result files must validate against the exact new package hashes and result contract.

## 8. Formal Screening acceptance and active authority

Create a new immutable content-addressed Screening acceptance for r2.

Requirements:

- historical acceptance `2ab82c6...` remains present and byte-unchanged;
- new corrected acceptance coexists as a second immutable run;
- current Core acceptance validation passes;
- current expansion basis points to the corrected 110-record derived Discovery;
- no directory-order/mtime/latest heuristic is used to choose active authority.

Then use current Core stage validation/advance machinery to advance Screening.

A successful Screening Stage Checkpoint must bind the exact new `screening-acceptance` artifact. After advancement, `resolve_active_screening_acceptance()` must return the new corrected acceptance and must not return the historical 105-run acceptance.

## 9. Stage advance

Only after all Screening checks PASS, formally advance:

`DISCOVERY_COLLECTED / stage:screening`

→

`CANDIDATES_NORMALIZED / stage:evidence`

Use current agent-first Core machinery. Do not hand-edit Production State lifecycle/control fields.

After advancement verify:

- lifecycle = `CANDIDATES_NORMALIZED`;
- next_action = `stage:evidence`;
- screening checkpoint = passed;
- active Screening acceptance = corrected 110-run;
- accepted root Discovery remains immutable;
- historical 105 acceptance remains immutable;
- expected future Evidence tasks from active acceptance = 80.

Do not prepare or accept Evidence tasks in this task unless required only as a read-only dry-run assertion. The bounded stop is before real Evidence work.

## 10. External sidecar pilot handling in this task

Do not run:

- `eariver/publication-boundary-redteam`
- `eariver/survey-core-v2-authority-auditor`

They are intentionally deferred until after Human Architecture Review / publication-stage milestones.

Preserve the W34 sidecar plan and ensure no new lifecycle state, Human Gate, canonical State authority, or GitHub Actions workflow is added.

## 11. Durable execution records

Create a new execution directory, recommended:

`sources/2026-W34/execution/luna/w34-post-483-core-sync-screening-recovery-r1/`

Record at least:

- session worklog;
- validation JSON;
- Sol handoff Markdown.

Record:

- exact Starting SHA;
- reviewed main SHA;
- merge commit SHA;
- current Core implementation SHA used by package prep;
- corrected input SHA256/byte count;
- 40/110/40/0 root-closure accounting;
- old acceptance digest/path and unchanged proof;
- new package path/hash;
- new acceptance path/hash;
- decision totals 45/19/16/30;
- active resolver result;
- stage checkpoint path/hash;
- ending Production State lifecycle/next_action;
- expected Evidence tasks 80;
- external sidecar tools not executed.

## 12. Write boundary

Allowed writes are W34 edition-local artifacts plus the normal merge of reviewed main Core into the existing W34 branch.

Do not write to:

- `main`;
- W33;
- SP001/SP002/SP003;
- external tool repositories;
- shared Core beyond the exact reviewed main merge;
- historical accepted Screening run files.

## 13. Stop condition

Success:

`CANDIDATES_NORMALIZED / stage:evidence`

and report status:

`READY_FOR_SOL_EVIDENCE`

Any Core/provenance/authority inconsistency:

`NEEDS_SOL_REVIEW`

Do not continue to Evidence acceptance, Materiality, Completeness, Selection, Architecture, Drafting, or either external sidecar tool in this bounded task.