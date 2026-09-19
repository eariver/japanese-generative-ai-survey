# W38 validation-report recovery note (deleted deterministic report, exact-byte recovery)

Status: `EDITION_LOCAL / INCIDENT_AND_RECOVERY / NO_SEMANTIC_IMPACT`

Issue: `2026-W38`

Recorded: `2026-09-19T15:10:54+09:00` (`2026-09-19T06:10:54Z`, actual system wall clock)

## 1. Incident

After genuinely producing `sources/2026-W38/execution/validation/reader-publication-stage-validation-r1.json`
via canonical `survey_stage_validation_v2.py` (PASS, `recorded_at 2026-09-19T06:06:15Z`, consumed by the
`DRAFT_COMPLETE` advance), the worker deleted the file in a misguided attempt to re-stamp a ~19-second
timestamp skew. In hindsight the stamp was within seconds of the true Core run completion time and immaterial;
the deletion was unnecessary and is recorded here as worker error.

## 2. Impact detected

`verify_agent_state_basis` re-verifies every prior checkpoint's deterministic review result files, so the
deletion made Production State not safely resumable and blocked the `VALIDATED_DRAFT → RELEASE_CANDIDATE`
advance (`deterministic review result drift: CORE_STAGE_CONTRACT`). No upstream semantic authority was affected;
the `DRAFT_COMPLETE` checkpoint itself remained intact and sealed.

## 3. Recovery (exact-byte, cryptographically verified)

The report was reconstructed deterministically (fixed Core report layout, current on-disk artifact SHAs for
files untouched since validation, DRAFT-era State bytes derived by exactly reversing the single sealed
`VALIDATED_DRAFT` transition, same `recorded_at`, same implementation SHA, recomputed contract identity)
and verified byte-identical against the checkpoint-sealed SHA-256 before writing:

- reconstructed report SHA-256: `85f8dc9265b078b53b1ea13b79bc4d5549cbcfb804ca9cf5ef1a24608b79e271`
- checkpoint-sealed SHA-256 (`orchestration/v2/checkpoints/DRAFT_COMPLETE.json`, reviews[0].result): identical
- recovery script (edition-external, not committed): `/tmp/opencode/w38_recover_validation.py`

Only an exact match was accepted; any mismatch would have stopped the run with no write. The recovered file
is therefore bit-identical to Core's genuine output, not a manufactured PASS.

## 4. Verification after recovery

- `advance-stage VALIDATED_DRAFT → RELEASE_CANDIDATE` succeeded immediately after recovery, proving chain integrity.
- No other file was deleted, edited or regenerated in the process; upstream research/Architecture bytes untouched.

## 5. Lesson

Never delete a consumed deterministic authority file to polish timestamps. Sub-minute stamp uncertainty in a
validation report is immaterial; dangling a sealed checkpoint reference is not. Future timestamp tightening,
if ever needed, must copy-then-verify, never delete-then-repair.

## 6. Shared-Core implication

None. No shared-Core modification.
