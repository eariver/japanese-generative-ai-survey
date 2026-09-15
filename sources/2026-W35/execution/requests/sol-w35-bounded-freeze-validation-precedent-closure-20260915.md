# W35 bounded Freeze validation precedent closure — Publication Preview APPROVED through RELEASED

Status: `EXECUTION_AUTHORITY / W35_TEMPORARY_CORE_FROZEN_CLOSURE / W34_PRECEDENT_BOUNDED_VALIDATION_CORRECTION`

Date: `2026-09-15 JST`

## 1. Mission

Complete `2026-W35` from the preserved Human-approved `RELEASE_CANDIDATE` frontier through canonical Freeze, main integration, exact-byte public Release, and terminal `RELEASED / COMPLETE`, while **keeping shared Core bytes frozen** for the separate J-GAS refactor analysis.

Shared-Core maintenance defects are intentionally deferred under GitHub Issue #497 and the W35 edition defect records:

- profile-aware Freeze incorrectly requires the legacy post-approval visual schema;
- `survey_stage_validation_v2._prior_artifacts()` treats Human Publication Preview approval provenance as a Stage Checkpoint.

This request authorizes only the same bounded Freeze/Human-Gate artifact-admission correction already used to close W34. It does **not** authorize any persistent Core edit.

## 2. Fixed starting authority

Repository: `eariver/japanese-generative-ai-survey`

Existing branch only:

`weekly/2026-W35-v2-work`

Exact Starting SHA and Tree are supplied by the Sol handoff message and must be verified read-only before any write.

Expected remote `main`:

`774dd39a951c9ac3818e83dfffd4c7666efb0a20`

Expected remote `production/survey-core-v2`:

`774dd39a951c9ac3818e83dfffd4c7666efb0a20`

Also verify the current W35 State remains:

- lifecycle `RELEASE_CANDIDATE`
- Architecture Review `approved`
- Publication Preview `approved`
- next action `stage:freeze`
- freeze `pending`
- release `pending`

and that `weekly/2026-W35` tag/Release do not already exist.

Any mismatch => zero repository/GitHub writes, report expected vs actual, STOP.

## 3. Exact approved publication authority

Do not regenerate publication content.

Approved PDF:

`surveys/weekly/2026-W35/main.pdf`

SHA-256:

`6115f0a774a947a269426c46003d09c9e4f962f54d5043d3778a5b815591a1b2`

Bytes: `285365`

Pages: `8`

Publication Candidate canonical internal candidate SHA:

`3195f74c89a3c8e163f0f29cc0123132ecedd287f84c1467d9110d40167e2e8d`

Human Publication Preview approval is already canonical and must not be re-recorded.

## 4. Shared-Core freeze constraint

Do not modify, commit, merge, cherry-pick, regenerate, or otherwise change any file under shared Core surfaces, including but not limited to:

- `scripts/`
- `schemas/`
- `config/`
- `.github/`

Do not advance `production/survey-core-v2`.

Do not open or merge a Core repair PR in this execution.

Issue #497 plus the two W35 defect records are the durable maintenance obligations.

## 5. Freeze artifact generation — required compatibility primitive

Do not invoke `scripts.survey_profiled_freeze_v2`.

Generate the exact Freeze Record and Release Manifest using the existing canonical primitive:

`scripts.survey_publication_v2.build_freeze()`

with the current W35:

- Publication Candidate
- canonical Publication Preview approval
- real current UTC `frozen_at`
- canonical output paths under `sources/2026-W35/publication/v2/`

Then run `validate_release_manifest()` normally.

The resulting release identity must be exactly:

`weekly/2026-W35`

The Freeze chain must bind exactly:

- current Publication Candidate bytes
- canonical Human Publication Preview approval bytes
- Candidate-bound pre-preview VISUAL review bytes
- approved PDF SHA above
- current validated source bytes

No legacy post-approval visual record may be invented.

## 6. Freeze stage validation — W34 precedent bounded correction

The unmodified `survey_stage_validation_v2.py` currently fails before evaluating the W35 Freeze artifacts because `_prior_artifacts()` reads `checkpoint_provenance.publication_preview` as though it were a Stage Checkpoint. This is a deferred shared-Core defect and is outside edition repair.

For this W35 closure only, use the **same semantic correction already recorded in W34 Freeze provenance**:

`survey_stage_validation_v2 with bounded Freeze/Human-Gate artifact admission correction`

The correction is permitted **only at runtime/in-memory for this validation invocation** and must not persist any Core file change.

Its exact allowed semantic effect is:

- preserve all true prior Stage Checkpoint authorities exactly;
- exclude the `publication_preview` Human approval provenance from Stage Checkpoint enumeration;
- continue to validate the Publication Preview approval through the validator's dedicated Human-Gate authority path;
- make no other behavioral change.

Do not disable schema checks, artifact SHA checks, lifecycle checks, approval checks, candidate checks, visual checks, Freeze checks, Release Manifest checks, or contract checks.

The corrected validation must genuinely execute the normal `RELEASE_CANDIDATE -> FROZEN` semantic checks against the generated W35 Freeze/Manifest and exact current upstream authorities.

Create edition-local validation provenance under a clearly named W35 execution directory, including:

1. a `CORE_STAGE_CONTRACT` PASS report matching current `schemas/stage-checkpoint-v2.schema.json` expectations;
2. a review record that explicitly names the executor as `survey_stage_validation_v2 with bounded Freeze/Human-Gate artifact admission correction`;
3. evidence text stating that this is the W34 precedent correction and referencing GitHub Issue #497 plus `sources/2026-W35/execution/defects/w35-freeze-prior-checkpoint-provenance-core-defect-20260915.md`;
4. the three Freeze checkpoint artifacts required by current schema:
   - `freeze-record`
   - `release-manifest`
   - `visual-review-record` (the existing Candidate-bound pre-preview VISUAL authority).

Do not fabricate a PASS. If the semantic Freeze validation fails after the single allowed provenance-admission correction, STOP.

## 7. Advance to FROZEN

Use the normal current controller/checkpoint mechanism to advance `RELEASE_CANDIDATE -> FROZEN`, using the validated edition-local `CORE_STAGE_CONTRACT` authority.

The resulting canonical `RELEASE_CANDIDATE.json` checkpoint must be schema-valid and bind the exact three Freeze artifacts above.

Expected state after this phase:

- lifecycle `FROZEN`
- publication_preview `passed`
- freeze `passed`
- release `pending`
- release identity `weekly/2026-W35`
- approved PDF bytes unchanged.

Commit and push normally/non-force, then remote read-back before continuing.

## 8. Main integration and Release

After a valid frozen branch exists, follow the current canonical release topology and the W34 closure precedent.

Because at the start of this execution:

`main == production/survey-core-v2 == 774dd39a...`

there is no Production-Line-only Core delta to leak.

Integrate the exact frozen W35 authority to `main` using the repository's normal reviewed merge path. Do not squash/rebase/rewrite. The frozen publication bytes must remain byte-identical after integration.

Then execute the canonical public Release identity:

`weekly/2026-W35`

Perform exact-byte reconciliation of the released asset against the frozen Release Manifest.

The released PDF must remain:

- SHA-256 `6115f0a774a947a269426c46003d09c9e4f962f54d5043d3778a5b815591a1b2`
- `285365` bytes
- `8` pages.

## 9. FROZEN -> RELEASED

Use the current canonical release checkpoint mechanism, including both deterministic authorities required by current Core:

- `CORE_STAGE_CONTRACT`
- `RELEASE_EXACT_BYTE_RECONCILIATION`

No bounded correction beyond §6 is pre-authorized. If a new Core contradiction appears in the release-stage path, STOP and report it.

Normal successful terminal state:

- lifecycle `RELEASED`
- terminal_reason `COMPLETE`
- freeze `passed`
- release `passed`
- public Release `weekly/2026-W35` exists and targets the correct integrated commit
- released asset exact-byte reconciliation PASS.

## 10. Final audit

Before reporting success, read back and report:

- final W35 work-branch HEAD/tree
- final `main` HEAD/tree
- `production/survey-core-v2` HEAD/tree, confirming it remains `774dd39a951c9ac3818e83dfffd4c7666efb0a20` and no Core bytes changed
- Freeze commit and parent
- main integration commit and parents
- Release provenance commit and parent
- tag/Release `weekly/2026-W35` target
- released asset SHA/bytes/pages
- final Production State lifecycle/checkpoints/terminal reason
- changed paths for each closure commit
- confirmation that no shared-Core file changed in the W35 compatibility closure.

## 11. Prohibitions

Do not:

- modify shared Core
- close Issue #497
- create fallback/repair/review branches
- force push
- reset/rebase/squash/history rewrite
- regenerate Draft/TeX/PDF/Candidate/Reviews
- alter Human decisions
- invent post-approval visual QA
- suppress any validation other than the exact runtime-only prior-provenance admission correction in §6
- start W36.

## 12. STOP conditions

STOP without improvisation if:

- starting guards mismatch;
- approved bytes drift;
- compatibility Freeze output fails normal Release Manifest validation;
- corrected Freeze semantic validation fails for any reason other than the known prior-provenance admission defect;
- controller rejects the resulting deterministic report/checkpoint;
- main integration changes frozen publication bytes;
- release exact-byte reconciliation fails;
- any additional shared-Core contradiction is found.
