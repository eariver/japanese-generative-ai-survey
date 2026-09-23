# TS-001 reissue post-release provenance recovery (CV2-DM-004 recurrence)

Status: `SHARED_CORE_DEFECT_RECURRENCE / EDITION_LOCAL_RECOVERY / NO_CORE_CHANGE`
Date: `2026-09-23`
Edition: `SP-efficient-llm-2026`
Canonical workflow run: `35863535480`
Recovery branch: `release-record/SP-efficient-llm-2026-35863535480`

## External release (untouched, verified)

- Public Release: `https://github.com/eariver/japanese-generative-ai-survey/releases/tag/special/efficient-llm-2026`
- Tag / identity: `special/efficient-llm-2026` (profile-derived public identity)
- Asset: `Japanese_Generative_AI_Technical_Survey_Special_efficient-llm-2026.pdf`
- Asset SHA-256: `8a9a721ac35b2e5baa2e20162b5a6ba4ae63945d512d985484aeae56073a23c1`
  (== Human-approved r2 PDF, 850785 bytes)
- Target: main merge `66037d67145fb01a8ea7669a4663ecd8381f4244`
- Disposition: created by the canonical workflow; NOT recreated, re-uploaded, or re-run.

## Known defect recurrence (CV2-DM-004, not repaired)

The canonical workflow failed solely at:

```text
PYTHONPATH=. python scripts/survey_agent_control_v2.py --repo-root . validate-state --state "$STATE"
survey_agent_control_v2.py: error: argument command: invalid choice: 'validate-state'
```

All earlier release steps (authority resolution, PDF rehydration + exact-byte
check, merge verification build, Release create + download reconciliation)
passed. No earlier step failed; no publication byte required regeneration.

## Bounded recovery (W35–W38 pattern, edition-local only)

On this branch, based on exact post-integration main `66037d67`:

1. `survey_publication_v2.build_merge_verification` (merged commit `66037d67...`)
   -> `publication/v2/merge-verification-v2.json` (`a0268ca9...`)
2. `survey_publication_v2.build_release_record` (existing public Release URL)
   -> `publication/v2/release-record-v2.json` (`a610d46d...`, status RELEASED)
3. `scripts/survey_release_checkpoint_v2.py` (canonical helper)
   -> `publication/v2/core-stage-contract-v2.json` (`0b364680...`)
   -> `orchestration/v2/checkpoints/FROZEN.json` (`ff12f02b...`)
   -> Production State `FROZEN → RELEASED`
4. Final validation via Python API `agent.validate_agent_state` (clean, no errors)
   instead of the nonexistent `validate-state` CLI.

Changed paths: exactly these 5 files, all under `sources/SP-efficient-llm-2026/`.
No shared-Core file changed. CV2-DM-004 remains `OPEN_CORE`, not marked fixed.

Final state: lifecycle `RELEASED`, terminal_reason `COMPLETE`, next_action null,
Architecture approved, Publication Preview approved, freeze/release passed,
exception gate inactive.
