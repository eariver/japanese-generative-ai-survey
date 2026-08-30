# 2026-W33 Sol→Luna handoff — Selection revision r1

Status: `READY_FOR_LUNA / SELECTION_REVISION_PROPOSAL_ONLY / STOP_FOR_SOL_REVIEW`

Issue: `2026-W33`  
Canonical branch: `weekly/2026-W33-v2-work`  
Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`  
Current lifecycle at handoff creation: `EVIDENCE_REVIEWED`  
Current machine action: `stage:selection`  
Target Human Gate: `ARCHITECTURE_REVIEW`

Sol authority for this task:

`sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-revision-advance-sol-review-20260830-r1.md`

Decision:

`ACCEPT / STATE_TRANSITION_VERIFIED / REVISED_EVIDENCE_AUTHORITY_ESTABLISHED / READY_FOR_SELECTION_REVISION`

The caller must supply the exact branch HEAD containing this handoff and the Sol review above. Before any write, remote `weekly/2026-W33-v2-work` HEAD must equal that exact supplied SHA. If not, stop with `AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`; do not merge, rebase, choose a newer basis, or force-push.

## 1. Objective

Perform only the W33 Selection revision candidate/materialization phase:

1. regenerate the canonical 37-row Candidate Matrix deterministically from the revised E/M/C authority;
2. regenerate Candidate Selection against that Matrix;
3. preserve the previously accepted 28-candidate selected pool;
4. explicitly dispose the five repaired W32 carry-over candidates under their new E/M/C status;
5. validate Matrix and Selection under current Core;
6. record one Luna session;
7. commit/push the revised Matrix, revised Selection, and session;
8. stop for Sol semantic review.

Do not create a Selection Stage Checkpoint.  
Do not run `ADVANCE_STAGE`.  
Do not begin Architecture.

Successful endpoint:

`SELECTION_REVISION_CANDIDATE_READY_FOR_SOL_REVIEW`

## 2. Frozen upstream authority

### Production State

Path:

`sources/2026-W33/production-state.json`

Expected SHA-256:

`b546d8856ed60579c35627dfbe010a7c44ca0bacb526fe7a99b7cf8326a2aee7`

Required semantics:

- lifecycle: `EVIDENCE_REVIEWED`;
- next action: `stage:selection`;
- discovery/screening/evidence/materiality/completeness: passed;
- selection: pending;
- architecture: pending;
- Architecture Review: pending;
- terminal reason: null;
- Exception Gate: inactive.

Production State must remain byte-identical during this task.

### Production Profile

`sources/2026-W33/production-profile.json`

SHA-256:

`19303fcc8499a9cd7303991e69cfc0777a716db897537f50c5a9cff8dcb3f72b`

W33 temporal window:

- start: `2026-08-07T18:00:00-04:00`
- cutoff: `2026-08-14T18:00:00-04:00`

### Current revised Screening

`sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/screening-accepted.json`

- result-set: `0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a`
- acceptance SHA-256: `e6f0392004191b4668e4231c57839044e4b08ff1e32763403f2d92630b0b0a0f`

### Current Evidence acceptance

`sources/2026-W33/evidence/v2/accepted/e8c1097f497e126ac950f1d6a80b183c10bf69b2cb5c42ad370a073a9d249141/evidence-accepted.json`

- result-set: `e8c1097f497e126ac950f1d6a80b183c10bf69b2cb5c42ad370a073a9d249141`
- acceptance SHA-256: `2d3dd740adcefeec7fb32f3aba97f90e19eed8dfe4ff10a0096605c34cc98632`
- VERIFIED 24 / PARTIAL 12 / NEEDS_MORE 1 / REJECTED 0

### Current Edition View acceptance

`sources/2026-W33/evidence/v2/views/accepted/bc00ef52332d3d7f346ad5b179fd3eee6224bd5f297a46681b16d3b54af72ce8/edition-views-accepted.json`

- View set: `bc00ef52332d3d7f346ad5b179fd3eee6224bd5f297a46681b16d3b54af72ce8`
- acceptance SHA-256: `cafad25cc8e1ddeba63da0ed96c35fe986ccd6c386e451735215a00eb19fd242`
- MATERIAL 25 / CONTEXT 10 / HOLD 1 / NON_MATERIAL 1

### Current Materiality Ledger

`sources/2026-W33/materiality-ledger-v2.json`

SHA-256:

`2b771fec7405ed81a72bb60eeb686a680f3d4537969b9f20c65eda8b48df5c9f`

Rows: 41.

### Current Profile Completeness

`sources/2026-W33/profile-completeness-v2.json`

SHA-256:

`d3dfe4cc3e9b55dbbd5254f9fe61dacdfb6eda1771b9bba13deafe3279d9e08b`

Semantics:

- overall: `LIMITED`;
- `weekly:current-relevance = LIMITATION`;
- `weekly:technical-significance = LIMITATION`;
- `weekly:carry-over = SATISFIED`;
- no obligation has `NEEDS_RESEARCH`.

Do not use the historical `INCOMPLETE` Completeness as current authority.

## 3. Historical Selection is precedent only

Historical canonical files currently present at:

- `sources/2026-W33/candidate-matrix-v2.json`
- `sources/2026-W33/candidate-selection-v2.json`

are based on superseded E/M/C hashes and are not current checkpoint authority.

They may be read only to carry forward editorial assignments that the Owner already found acceptable.

Historical counts:

- SELECTED 28;
- HOLD 6;
- REJECT 3;
- INSPECT 0.

The Owner's Architecture Review finding accepted the previous 28-candidate placement strategy except for the missing mandatory weekly synthesis chapter. The revised carry-over evidence does not create a reason to expand that 28-candidate pool.

## 4. Required read order

Before writing, read at minimum:

1. `AGENTS.md` from reviewed main;
2. `docs/survey-production-core-v2-session-bootstrap.md` from reviewed main;
3. `docs/survey-production-core-v2-execution-record-policy.md` from reviewed main;
4. `config/survey-production-v2.json` from reviewed main;
5. `schemas/candidate-matrix-v2.schema.json` from reviewed main;
6. `schemas/candidate-selection-v2.schema.json` from reviewed main;
7. `scripts/survey_architecture_v2.py` and `scripts/survey_architecture_v2_base.py` from reviewed main;
8. `scripts/survey_stage_validation_v2.py` from reviewed main;
9. current Production Profile and Production State;
10. current revised Screening/Evidence/View/Ledger/Completeness authorities above;
11. historical `candidate-matrix-v2.json` and `candidate-selection-v2.json` for editorial carry-forward only;
12. `sources/2026-W33/gates/reviews/architecture-r2.json`;
13. `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-revision-sol-review-20260830-r1.md`;
14. `sources/2026-W33/execution/reviews/w33-evidence-materiality-completeness-revision-advance-sol-review-20260830-r1.md`;
15. this handoff.

If current Core or exact repository authority contradicts this handoff, stop with `CORE_OR_AUTHORITY_DRIFT_NEEDS_SOL_REVIEW`.

## 5. Regenerate Candidate Matrix deterministically

Overwrite the canonical current Matrix only at:

`sources/2026-W33/candidate-matrix-v2.json`

Use current Core derivation with exactly the revised authorities. Equivalent invocation:

```bash
python scripts/survey_architecture_v2.py \
  --repo-root . \
  --implementation-sha 6267de3f6876f491950139757bfdf1085fc07bdc \
  matrix \
  --profile sources/2026-W33/production-profile.json \
  --discovery sources/2026-W33/discovery/discovery-v2.jsonl \
  --screening sources/2026-W33/screening/v2/accepted/0723540ccade3bb9ac5fdcc1d120df8f060d2d2a5e6d2b56d26cc3c6ed41c08a/screening-accepted.json \
  --evidence sources/2026-W33/evidence/v2/accepted/e8c1097f497e126ac950f1d6a80b183c10bf69b2cb5c42ad370a073a9d249141/evidence-accepted.json \
  --views sources/2026-W33/evidence/v2/views/accepted/bc00ef52332d3d7f346ad5b179fd3eee6224bd5f297a46681b16d3b54af72ce8/edition-views-accepted.json \
  --ledger sources/2026-W33/materiality-ledger-v2.json \
  --completeness sources/2026-W33/profile-completeness-v2.json \
  --output sources/2026-W33/candidate-matrix-v2.json
```

Expected Matrix summary:

- candidate count: 37;
- materiality: MATERIAL 25 / CONTEXT 10 / HOLD 1 / NON_MATERIAL 1;
- Evidence: VERIFIED 24 / PARTIAL 12 / NEEDS_MORE 1 / REJECTED 0.

Require a fresh independent deterministic regeneration to produce byte-equivalent JSON before commit.

Do not hand-edit Matrix rows.

The candidate ID set is expected to remain the same 37 IDs because the Evidence task/result identities were intentionally preserved. If the set differs, stop for Sol review rather than guessing how to map historical assignments.

## 6. Revised Candidate Selection

Overwrite only:

`sources/2026-W33/candidate-selection-v2.json`

Use:

- schema `2.0-rc1`;
- issue `2026-W33`;
- research profile `WEEKLY`;
- publication profile `WEEKLY_MAGAZINE`;
- `selection_version = w33-selection-revision-luna-r1`;
- status `ESTABLISHED`;
- exact current Profile/Matrix/Completeness/Ledger basis hashes;
- exactly one assignment for every current Matrix candidate.

This artifact remains a Luna proposal until Sol review.

### 6.1 Exact carry-forward set

For the following 32 candidates, carry forward the historical Selection assignment semantic object exactly, except for any mechanically required current identity/basis context outside the assignment object:

- all historical 28 `SELECTED` assignments;
- all historical 3 `REJECT` assignments;
- the historical MiniMax `HOLD` assignment.

Do not change publication role, architecture role, PRIMARY/SUPPORTING usage, or rationale for these 32 records.

MiniMax candidate:

`candidate:2026-W33:986cf7db00a0202e`

must remain:

- disposition `HOLD`;
- architecture usage `NONE`;
- null publication/architecture roles.

### 6.2 Five changed carry-over assignments

Change exactly these five historical `HOLD` assignments to `REJECT`.

All five must use:

- `architecture_usage = NONE`;
- `publication_role = null`;
- `architecture_role = null`;
- empty `profile_extensions` unless current schema requires a deterministic existing value.

#### RepoWise

Candidate:

`candidate:2026-W33:348224cd5f85f112`

Disposition:

`REJECT`

Rationale semantic requirement:

> The first-party project/benchmark authority now establishes the tool and method, but no qualifying W33 event or delta is established. The current Edition View is `NON_MATERIAL`, so the carry-over is explicitly closed by non-inclusion rather than left open as HOLD.

Do not imply that project-reported benchmark metrics were independently reproduced.

#### Copilot cloud-agent

Candidate:

`candidate:2026-W33:2196b30d61a7d4d5`

Disposition:

`REJECT`

Rationale semantic requirement:

> Fresh GitHub authority closes the carry-over with an August 3 feature update, but the event is pre-window relative to W33. Retain it as resolved context in provenance, not as a selected W33 Architecture item.

#### GPT-5.6 August update

Candidate:

`candidate:2026-W33:2ca10d280e456f7f`

Disposition:

`REJECT`

Rationale semantic requirement:

> Fresh OpenAI authority closes the August 6 ChatGPT update and keeps it distinct from the original GPT-5.6 launch, but it is pre-window for W33 and should not consume a W33 Architecture placement.

Keep the Chat-only versus Work/Codex unchanged boundary intact.

#### Kimi K3 in GitHub Copilot

Candidate:

`candidate:2026-W33:dd58aff40dc7d0f9`

Disposition:

`REJECT`

Rationale semantic requirement:

> Fresh GitHub authority closes the August 6 availability/rollout carry-over, but the event is pre-window for W33. It remains resolved context and is not a separate W33 Architecture item.

#### Claude Opus 4.1 retirement

Candidate:

`candidate:2026-W33:f0414d90204e46fe`

Disposition:

`REJECT`

Rationale semantic requirement:

> Fresh Anthropic authority closes the June 5 deprecation / August 5 retirement chronology. The retirement is pre-window for W33, so the carry-over is closed without selecting it into W33 Architecture.

Preserve the distinction between Anthropic-operated and partner-operated retirement schedules.

## 7. Expected final Selection

Expected exactly:

- candidate count: 37;
- SELECTED: 28;
- HOLD: 1;
- REJECT: 8;
- INSPECT: 0;
- selected count: 28.

Every non-selected candidate must have `architecture_usage=NONE` and null publication/architecture roles.

No Matrix candidate with `NON_MATERIAL`, `HOLD`, `NEEDS_MORE`, or `REJECTED` status may be SELECTED.

The 28 selected assignments must remain exactly the previously accepted Architecture input pool. Do not add a pre-window carry-over as SUPPORTING merely because its Evidence is now VERIFIED.

## 8. Human revision constraints to preserve

This Selection task does not regenerate Architecture, but the next Architecture step must preserve the Owner's r2 requirements:

- keep the six previously accepted substantive packages unless newly accepted evidence forces a change;
- keep the 28-candidate placement strategy;
- keep target 18 pages / hard maximum 24 pages;
- keep `w33-agent-evaluation-reliability` as comparative synthesis;
- add an explicit independent `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW` chapter as a formal Architecture element.

Do not attempt to encode the weekly synthesis chapter into Candidate Selection as an artificial candidate.

## 9. Validation

Before push, require at minimum:

1. Matrix schema/current-Core validation PASS;
2. deterministic Matrix rebuild equivalence PASS;
3. Selection schema/current-Core validation PASS;
4. exact 37 Matrix IDs == exact 37 Selection IDs;
5. Matrix counts exactly 25 MATERIAL / 10 CONTEXT / 1 HOLD / 1 NON_MATERIAL;
6. Matrix Evidence counts exactly 24 VERIFIED / 12 PARTIAL / 1 NEEDS_MORE / 0 REJECTED;
7. Selection counts exactly 28 SELECTED / 1 HOLD / 8 REJECT / 0 INSPECT;
8. 28 selected candidate IDs exactly equal the historical selected ID set;
9. 32 carry-forward assignment semantic objects match historical Selection exactly;
10. exactly five assignments changed from historical HOLD to current REJECT;
11. current Profile/Completeness/Ledger/Matrix basis hashes are exact;
12. Production State SHA-256 remains `b546d8856ed60579c35627dfbe010a7c44ca0bacb526fe7a99b7cf8326a2aee7`;
13. no checkpoint, request, bridge run, Architecture, Human Gate, Draft, or source-research path changed.

If any invariant fails, stop rather than adjust counts opportunistically.

## 10. Allowed write paths

Only:

- `sources/2026-W33/candidate-matrix-v2.json`;
- `sources/2026-W33/candidate-selection-v2.json`;
- `sources/2026-W33/execution/sessions/w33-luna-selection-revision-20260830-r1.md`.

No other path may change.

## 11. Git boundary

Before writing, verify remote HEAD equals the caller-supplied Starting SHA.

Before final push/update, re-read remote HEAD and require it still equals the Starting SHA or the expected immediately prior Luna commit in this bounded sequence.

Normal fast-forward only. `force=false`.

Preferred sequence:

1. Matrix + Selection candidate commit;
2. session bookkeeping commit.

Do not create a new branch.

## 12. Required session report

Record at minimum:

- exact Starting SHA and remote equality PASS;
- candidate/final commit SHAs;
- reviewed main SHA;
- State SHA before/after;
- exact Matrix SHA-256 and summary counts;
- exact Selection SHA-256 and disposition counts;
- selected ID-set equality with historical 28;
- 32 carry-forward assignment equality result;
- five changed candidate IDs and resulting REJECT disposition;
- MiniMax HOLD confirmation;
- validation results;
- changed-path inventory;
- external-source-access count (must be zero);
- no `ADVANCE_STAGE` confirmation;
- final remote SHA.

Stop with exactly:

`SELECTION_REVISION_CANDIDATE_READY_FOR_SOL_REVIEW`
