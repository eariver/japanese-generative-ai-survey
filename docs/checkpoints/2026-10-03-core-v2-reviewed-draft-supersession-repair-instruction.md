# Core v2 execution instruction — reviewed Draft supersession authority before VALIDATED_DRAFT

Status: `EXECUTION_AUTHORITY / SHARED_CORE_MAINTENANCE / INVESTIGATE_FIRST / FIX_GENERIC_REVIEWED_DRAFT_SUPERSESSION_GAP / STOP_AT_SOL_CORE_REVIEW`

Date: `2026-10-03 JST`

Repository: `eariver/japanese-generative-ai-survey`

Maintenance branch:

`fix/core-v2-reviewed-draft-supersession-20261003`

## 1. Mission

Repair a confirmed Shared Core v2 design gap exposed by TS-003:

A Draft may legitimately receive several Sol-reviewed editorial/terminology revisions after the normal

`ARCHITECTURE_ESTABLISHED -> DRAFT_COMPLETE`

transition, while the historical `ARCHITECTURE_ESTABLISHED.json` Stage Checkpoint must remain immutable.

Current Core later re-validates every artifact row from that historical checkpoint against the live path. Since the canonical Draft Result and profile-synthesis paths are intentionally updated by the reviewed revision, `validate_agent_state()` and therefore

`DRAFT_COMPLETE -> VALIDATED_DRAFT`

fail closed as artifact drift.

The repair must provide a **generic, state-bound, immutable-history-preserving authority for reviewed Draft supersession**.

Do not weaken normal drift detection.

Do not rewrite historical Stage Checkpoints.

Do not special-case TS-003, THEMATIC, LONGFORM_SPECIAL, or any edition ID.

Do not generate or infer any Human decision.

Stop at a fresh Sol Core review candidate. Do not merge into `production/survey-core-v2` or `main`.

## 2. Exact startup guards

Before any write, read-only verify all of the following.

### Maintenance branch

Branch:

`fix/core-v2-reviewed-draft-supersession-20261003`

Exact Starting SHA:

`774dd39a951c9ac3818e83dfffd4c7666efb0a20`

Expected Starting Tree:

`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

### Frozen Core authority

Branch:

`production/survey-core-v2`

Expected HEAD:

`774dd39a951c9ac3818e83dfffd4c7666efb0a20`

Expected tree:

`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

### Reviewed main

Expected main HEAD:

`d6381568cc897a47d6de992189e20339350342b7`

Expected main tree:

`83ce3a216d852a1c32d0138f9c56fadefa800666`

### Read-only TS-003 reproduction fixture

Branch:

`special/vision-multimodal-2026-work`

Expected HEAD:

`4d541ee6d8f3886f7bb6ef5e7d75e1ce13811633`

Expected tree:

`70b9c28158860ef19d0e0c87612abf9413255c17`

Accepted Draft authority:

`79d2b3e291e10896ed616bd698abefc1e479ddbe`

Accepted exact publication candidate r3 PDF SHA-256:

`637877b879def1dc491b1b3d40a852cd209e22f02d57794697079a722f949795`

If any guard differs, perform zero repository/GitHub writes, report expected vs actual, and stop.

No new/fallback/repair/review branch beyond the already-created maintenance branch.

No reset, rebase, squash, cherry-pick, force push, or history rewrite.

## 3. Mandatory read order

Read before implementation:

1. this instruction;
2. `scripts/survey_stage_validation_v2.py`;
3. `scripts/survey_agent_control_v2.py`;
4. `schemas/survey-production-state.schema.json`;
5. `schemas/stage-checkpoint-v2.schema.json`;
6. `schemas/publication-surface-revalidation.schema.json`;
7. `tests/test_survey_stage_validation_v2.py`;
8. `tests/test_survey_agent_control_v2.py`;
9. `tests/test_survey_publication_revalidation_v2.py`;
10. `tests/test_survey_human_gate_revalidation_revision_v2.py`;
11. `docs/checkpoints/core-v2-post-validated-draft-publication-revalidation-20260912.md`;
12. `docs/survey-production-core-v2-historical-invariants.md`;
13. TS-003 read-only:
    - `sources/SP-vision-multimodal-2026/production-state.json`;
    - `sources/SP-vision-multimodal-2026/orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json`;
    - `sources/SP-vision-multimodal-2026/execution/sol-draft-review-r9.md`;
    - canonical Draft r9 Results and profile synthesis;
    - publication candidate r3 authority family only as downstream proof.

Also inspect any existing Core helper that implements active checkpoint supersession/revalidation before designing duplicate logic.

## 4. Investigate-first reproduction

Before implementing, reproduce the defect against a disposable copy/worktree of the exact TS-003 fixture.

Do not write to the TS-003 branch.

Expected shape:

- Production State lifecycle: `DRAFT_COMPLETE`;
- Architecture Review: approved;
- Publication Preview: pending;
- draft checkpoint: passed;
- validation: pending;
- historical draft checkpoint provenance:
  `sources/SP-vision-multimodal-2026/orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json`;
- Draft Packages still match the historical checkpoint;
- accepted Draft Results / synthesis are legitimate reviewed successors;
- current Core reports historical Stage Checkpoint artifact drift before normal DRAFT_COMPLETE stage semantics can pass.

Capture the exact drift roles.

Expected drift must be limited to legitimate Draft revision surface such as:

- `draft-result:<package-id>`;
- `synthesis-input`;
- `synthesis-result`.

If Draft Packages, Architecture, Selection, Evidence, approval, or other upstream authority is unexpectedly drifting, stop and report rather than broadening the repair.

Only proceed if the reproduced root cause matches this instruction.

## 5. Required invariant

The repair must preserve both of these statements simultaneously:

1. Historical Stage Checkpoints remain immutable records of the bytes accepted at the time of the transition.
2. A later explicitly reviewed Draft revision can become the active Draft authority without making arbitrary upstream mutation acceptable.

A successful implementation must **not** turn Stage Checkpoint SHA validation into “accept current bytes”.

It must instead bind a narrowly scoped supersession record to Production State, analogous in trust shape to the existing post-VALIDATED_DRAFT publication-surface revalidation mechanism.

## 6. Required authority model

Implement a generic reviewed-Draft supersession authority.

Naming may differ if a more coherent generic abstraction is found, but the semantics below are mandatory.

### 6.1 State-bound pointer

Production State must be able to carry an optional exact `{path, sha256}` pointer for the active reviewed Draft revision authority.

Suggested field:

`draft_revision_provenance`

Requirements:

- null/absent means no Draft supersession authority;
- an unreferenced record is inert;
- a referenced invalid/corrupt record fails closed;
- pointer persists through later forward lifecycle transitions unless a sanctioned rollback invalidates the Draft authority;
- it must coexist safely with `publication_revalidation_provenance`.

Update state schema and state initialization/refresh logic consistently.

### 6.2 Versioned immutable record

Use versioned immutable edition-local records, not a mutable singleton.

Suggested canonical family:

`{source_root}/draft/v2/draft-surface-revalidation-rN.json`

or an equivalent edition-local authority location that is clearly separate from canonical Draft content.

The record must bind at minimum:

- schema version;
- issue identity;
- reason class;
- reason;
- lifecycle at establishment;
- exact prior Draft Stage Checkpoint authority;
- superseded artifact rows:
  - name;
  - path;
  - prior SHA-256;
  - new SHA-256;
  - byte count;
- preserved artifact rows;
- exact review authority or review evidence reference;
- Core contract identity;
- implementation commit SHA;
- executor;
- recorded_at;
- exact establishment snapshot;
- exact `supersedes` authority for a prior revision record, or null for the first round.

Old revision records must remain byte-identical.

### 6.3 Eligible supersession surface

The mechanism must be narrow.

Allowed historical Draft checkpoint rows to supersede:

- `draft-result:<package-id>`;
- `synthesis-input`;
- `synthesis-result`.

Draft Packages are **not** eligible.

Any change to:

- `draft-package:<package-id>`;
- Architecture;
- Architecture approval;
- Selection;
- Candidate Matrix;
- Evidence;
- Edition Views;
- Materiality;
- Completeness;
- Discovery/Screening;
- Production Profile;
- contracts;

must remain ordinary drift and fail closed.

If investigation proves another artifact is mechanically derived from revised Draft Results and must be eligible, document the proof and stop for Sol before broadening unless the role is clearly equivalent to Draft-result/synthesis authority.

### 6.4 Review authority

The operation must require an exact repository-local review authority/evidence reference proving that the Draft successor was explicitly reviewed.

The generic Core must not hard-code TS-003 filenames or a specific model name.

At minimum bind exact path + SHA-256 and an explicit accepted decision class such as `PASS`.

Prefer a small structured review-binding object in the revalidation record rather than parsing prose heuristically.

Do not invent a Human gate. This is Sol/editorial review authority, not Human Publication Preview approval.

An unreviewed valid-looking Draft mutation must not be silently self-authorizing.

### 6.5 Establishment boundary

Establishment is allowed only while all of the following hold:

- lifecycle == `DRAFT_COMPLETE`;
- Architecture Review == approved;
- Publication Preview == pending;
- validation checkpoint == pending;
- freeze == pending;
- release == pending;
- exception gate inactive;
- prior draft checkpoint provenance exists and is valid.

Once validation has passed, Draft content is locked by the normal forward pipeline. Later publication-only changes use the existing publication revalidation mechanism.

No Draft supersession operation is allowed after Human Publication Preview approval, Freeze, or Release.

### 6.6 Fresh semantic/structural validation

New Draft bytes must be revalidated against the unchanged approved basis.

Re-run the existing generic Draft validators rather than just checking hashes.

At minimum prove:

- every current Draft Result is valid against its unchanged Draft Package;
- package/result pairing is complete and exact;
- approved Architecture and Architecture Approval still bind;
- Selection / Evidence basis remains unchanged;
- profile synthesis input is the exact derivation from the current reviewed Draft Results;
- profile synthesis result validates against that input/profile;
- no package is silently dropped or added.

Reuse existing drafting/synthesis validation functions where possible.

Do not add a weaker parallel validator.

### 6.7 Historical checkpoint consultation

Refactor the historical artifact-verification path so both:

- `survey_agent_control_v2.validate_agent_state`, and
- `survey_stage_validation_v2._prior_artifacts`

consult the same active-supersession helper.

For the one bound prior Draft checkpoint only:

- eligible superseded rows validate against `new_sha256` in the active record;
- every non-superseded row validates against the historical checkpoint SHA.

All other checkpoint records retain current behavior.

Do not duplicate override logic in two independent implementations.

### 6.8 Chaining

Support multiple reviewed Draft revisions before validation.

A second legitimate reviewed revision must:

- create a new versioned record;
- bind the previous record by exact `{path, sha256}`;
- leave the previous record unchanged;
- become the sole active State pointer.

Sequence discovery must ignore historical records unless State points to the active one.

A forged unreferenced higher-number record must be inert.

### 6.9 Forward lifecycle compatibility

After establishing the active reviewed Draft authority:

- `validate_agent_state` must PASS;
- normal `DRAFT_COMPLETE -> VALIDATED_DRAFT` stage validation must PASS when current reader/publication artifacts are valid;
- normal Stage Checkpoint creation and `advance-stage` must work unmodified;
- the Draft revision pointer must remain valid after advance;
- historical `ARCHITECTURE_ESTABLISHED.json` must remain byte-identical.

### 6.10 Coexistence with publication revalidation

Prove that a later legitimate `VALIDATED_DRAFT` publication-surface revalidation can coexist with the active Draft revision authority.

The two mechanisms bind different historical checkpoints/surfaces:

- Draft revision authority -> historical draft checkpoint;
- publication revalidation authority -> historical validation checkpoint.

No ordering ambiguity or global “latest SHA” override is allowed.

## 7. TS-003 acceptance fixture

Use TS-003 only as a read-only full-fidelity proof.

After generic implementation/tests are green, on a disposable copy of exact TS-003:

1. establish the reviewed Draft authority for accepted Draft r9;
2. bind the exact Sol Draft Review r9 authority;
3. verify historical `ARCHITECTURE_ESTABLISHED.json` unchanged;
4. verify `validate_agent_state` PASS;
5. run the normal DRAFT_COMPLETE reader/publication stage validation using accepted publication candidate r3;
6. verify stage validation PASS;
7. prove that normal checkpoint creation / advance to `VALIDATED_DRAFT` would succeed on the disposable fixture;
8. do not push or mutate the real TS-003 fixture branch;
9. do not create Human Publication Preview approval;
10. do not Freeze/Release.

Record the exact before/after state and hashes.

## 8. Mandatory regression tests

Add a dedicated generic regression suite. Test names may differ, but cover all of these.

T1. valid reviewed Draft revision initially reproduces historical checkpoint drift.

T2. establishment succeeds and old Draft Stage Checkpoint bytes remain identical.

T3. Draft Package mutation is rejected.

T4. Architecture / Architecture Approval mutation is rejected.

T5. Selection/Evidence/upstream mutation is rejected.

T6. malformed or semantically invalid revised Draft Result is rejected.

T7. synthesis-input not exactly derived from revised Draft Results is rejected.

T8. synthesis-result mismatch is rejected.

T9. wrong prior checkpoint path/SHA is rejected.

T10. unreferenced forged revision record is inert.

T11. corrupted State pointer fails closed.

T12. review authority missing/invalid/non-PASS is rejected.

T13. second reviewed revision chains to the first; first record remains byte-identical.

T14. after establishment, `validate_agent_state` PASS.

T15. normal DRAFT_COMPLETE stage validation PASS with current valid publication artifacts.

T16. normal advance to VALIDATED_DRAFT PASS; pointer persists; historical checkpoint immutable.

T17. after validation/preview/freeze/release boundary, new Draft supersession is rejected.

T18. active Draft revision + later publication revalidation coexist and state validation remains PASS.

T19. WEEKLY and LONGFORM/THEMATIC-shaped fixtures prove genericity; implementation contains no edition IDs/profile-specific special casing.

T20. full existing Core contract suite and compilation remain green.

Include negative tests for path escape/symlink/duplicate superseded rows/unknown artifact name/unchanged-byte supersession.

## 9. Documentation requirements

Update the minimum necessary shared Core docs.

At minimum document:

- reviewed Draft revision authority and lifecycle boundary;
- why historical Stage Checkpoints are not rewritten;
- relationship to publication-surface revalidation;
- fail-closed scope;
- Human Gate non-involvement;
- rollback/pointer behavior;
- genericity.

Add a canonical maintenance worklog under `docs/checkpoints/` recording investigation, design, tests, disposable TS-003 proof, final candidate SHA/tree, and unresolved questions.

Do not edit historical edition artifacts.

## 10. Scope controls

Allowed:

- Shared Core scripts;
- schemas;
- generic tests;
- Core documentation/worklog.

Forbidden:

- TS-003 branch writes;
- TS-003 Draft/Publication content changes;
- main changes;
- production/survey-core-v2 changes;
- Human approval artifacts;
- workflow changes unless investigation proves strictly necessary and Sol authorizes separately;
- edition-specific conditionals;
- lowering/removing existing drift checks;
- history rewrite.

## 11. Validation

Run at minimum:

- new focused reviewed-Draft supersession suite;
- existing stage-validation tests;
- existing agent-control tests;
- existing publication-revalidation tests;
- existing Human-gate revalidation/revision tests;
- schema tests;
- full Core contract test suite;
- Python compile/static sanity used by current Core maintenance practice.

The old publication revalidation suite must remain green unchanged except where State fixture initialization requires the new nullable field.

## 12. Required output

Create a maintenance worklog such as:

`docs/checkpoints/core-v2-reviewed-draft-supersession-20261003.md`

Report:

- startup guards;
- exact reproduced TS-003 drift roles;
- root cause;
- final design;
- changed files;
- schema/state changes;
- new operation/API;
- review-authority model;
- focused test matrix;
- neighboring/full regression results;
- disposable exact TS-003 proof;
- proof historical checkpoint bytes unchanged;
- proof real TS-003 branch untouched;
- final maintenance HEAD/tree.

Use normal commits and non-force push only.

## 13. Stop boundary

Do not merge this maintenance branch.

Do not change `production/survey-core-v2`.

Do not change `main`.

Do not advance real TS-003.

Normal terminal:

`CORE_V2_REVIEWED_DRAFT_SUPERSESSION_REPAIR_CANDIDATE_COMPLETE`

`GENERIC_FAIL_CLOSED_REVISION_AUTHORITY_IMPLEMENTED`

`HISTORICAL_DRAFT_CHECKPOINT_IMMUTABLE`

`TS003_DISPOSABLE_DRAFT_R9_TO_VALIDATED_DRAFT_PROOF_PASS`

`REAL_TS003_UNCHANGED`

`AWAITING_SOL_CORE_REVIEW`

STOP there.
