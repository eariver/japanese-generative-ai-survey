# TS-002 post-release provenance recovery (known CLI defect recurrence)

Status: `SHARED_CORE_DEFECT_RECURRENCE / EDITION_LOCAL_RECOVERY / NO_CORE_CHANGE`
Date: `2026-09-28`
Edition: `SP-beyond-text-2026`
Canonical workflow runs: `36333979769` (created Release), `36333984167` (reconciled existing Release)
Recovery branch: `release-record/SP-beyond-text-2026-36333979769`

## External release (untouched, verified)

- Public Release: `https://github.com/eariver/japanese-generative-ai-survey/releases/tag/special/beyond-text-2026`
- Tag / identity: `special/beyond-text-2026` (profile-derived public identity)
- Title: `Japanese Generative AI Technical Survey Special — beyond-text-2026`
- Asset: `Japanese_Generative_AI_Technical_Survey_Special_beyond-text-2026.pdf`
- Asset SHA-256: `4e2250677716fba5cbfe3ea0e57d9f2174e83a93a15a361d8fbae164bf45089d`
  (== Human-approved r12 PDF, 1106143 bytes, 78 pages)
- Target: main merge `4a54f07755984c1f7f56830b43fe24cfafd628a6`
- Disposition: created by canonical workflow run 36333979769; reconciled (not duplicated) by 36333984167; NOT recreated, re-uploaded, or re-run.

## Known defect recurrence (post-release CLI, TS-001 precedent fea2d8a6f / 42d78f13)

Both canonical workflow runs failed solely at:

```text
PYTHONPATH=. python scripts/survey_agent_control_v2.py --repo-root . validate-state --state "$STATE"
survey_agent_control_v2.py: error: argument command: invalid choice: 'validate-state'
```

All earlier release steps (authority resolution, PDF rehydration + exact-byte
check, merge verification build, Release create + download reconciliation,
Release Record + Checkpoint build) passed. No earlier step failed; no
publication byte required regeneration.

## Bounded recovery (TS-001 pattern, edition-local only)

On this branch, based on exact post-integration main `4a54f07755984c1f7f56830b43fe24cfafd628a6`:

1. `survey_publication_v2.build_merge_verification` (merged commit `4a54f077...`)
   -> `publication/v2/merge-verification-v2.json`
2. `survey_publication_v2.build_release_record` (existing public Release URL)
   -> `publication/v2/release-record-v2.json` (status RELEASED)
3. `scripts/survey_release_checkpoint_v2.py` (canonical helper)
   -> `publication/v2/core-stage-contract-v2.json`
   -> `orchestration/v2/checkpoints/FROZEN.json`
   -> Production State `FROZEN → RELEASED`
4. Final validation via Python API `agent.validate_agent_state` (clean, no errors)
   instead of the nonexistent `validate-state` CLI.

Changed paths: exactly these 5 files, all under `sources/SP-beyond-text-2026/`.
No shared-Core file changed. The CLI defect remains open Core, not marked fixed.

Final state: lifecycle `RELEASED`, terminal_reason `COMPLETE`, next_action null,
Architecture approved, Publication Preview approved, freeze/release passed,
exception gate inactive.
