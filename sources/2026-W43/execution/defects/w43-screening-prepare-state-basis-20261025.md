# Shared-Core defect — screening prepare rejects trusted bridge-advanced State (W43 r1 BLOCKED)

Status: `SHARED_CORE_DEFECT / EDITION_OBSERVED / BLOCKED`
Observed: `2026-10-25` (Muse screening-r1, work branch `weekly/2026-W43-v2-work`)
Edition: `2026-W43`, State `DISCOVERY_COLLECTED` (trusted bridge run `40116386580`, `ISSUE_INITIALIZED`→`DISCOVERY_COLLECTED`)

## Observation
`survey_screening_v2.py prepare --state sources/2026-W43/production-state.json --discovery sources/2026-W43/discovery/discovery-v2.jsonl --output-dir sources/2026-W43/screening/v2/packages/r1 --max-records 13 [--implementation-sha 7a969fd94789f27edc483aae052aa041f3772acd]` fails closed, exit 2:
`Production State semantic inconsistency: checkpoint discovery authority path is not canonical; Production State history[1] implementation SHA divergence`
First attempt without override fails earlier at `verify_state_basis`: `implementation commit differs from authoritative state` (work-branch HEAD moved past init — expected).

## Reproduction boundary
- Frozen Core paths byte-identical across init commit `7a969fd9`, reviewed main `041a08df`, Frozen Core `774dd39`, work HEAD (empty `git diff` on `scripts/ config/ schemas/ .github/ tests/ AGENTS.md`). No version skew.
- State bytes intact: checkpoint file SHA `18adc602…` matches `checkpoint_provenance.discovery.sha256`; `validate_acceptance` PASS (51 records, graph `5a94b757…`); X manifest COMPLETE.
- Same local `validate-state` fails identically on W42 RELEASED state (11 checkpoint paths + history[1..10] SHA divergences) — W42 advanced exclusively via the same trusted bridge path. Proves systematic convention mismatch, not W43 data corruption.

## Root cause (shared Core, not edition)
- Trusted bridge advances via agent-first `survey_agent_control_v2.advance_with_checkpoint`: Stage Checkpoint file named after FROM state (`orchestration/v2/checkpoints/ISSUE_INITIALIZED.json`), `checkpoint_provenance` bound to that file, history row stamped with executing HEAD (request commit `e67099d5…`).
- Frozen `survey_production_v2.verify_state_basis → validate_state_semantics` (used by screening `prepare`/`accept`) instead requires direct-local convention: checkpoint file named `<checkpoint>.json` (`discovery.json`) and every history SHA equal to the single init implementation SHA.
- The bridge (running reviewed-main Core) therefore produces States its own frozen screening entry points reject. Precedent: W42 screening package r1 was prepared pre-advancement at `ISSUE_INITIALIZED` (single-history state, checks trivially green); post-advancement screening acceptances went through the bridge.

## Impact
- W43 Screening r1 cannot start via the contracted local `prepare` path: 0 of 51 decisions materialized, no Screening Acceptance claimed, no `ADVANCE_STAGE` attempted, State/checkpoints untouched. Stop token `SOL_SCREENING_REVIEW_READY_R1` NOT reached — reported `BLOCKED` instead.

## Safe edition-local workaround
- NONE that preserves fail-closed integrity. `--implementation-sha` override, manual package assembly, State/checkpoint hand-edits, or skipping validation would all be manual PASS fabrication and are refused.

## Core-maintenance pointer
- Repair belongs in shared Core (separate change, reviewed freeze/audit): reconcile `verify_state_basis`/`validate_state_semantics` with the agent-first bridge conventions (`canonical_checkpoint_path` FROM-state files; history SHAs per executing commit), or route screening `prepare` through the agent-first basis resolver. Do NOT repair production by editing `scripts/` here.

## Production disposition
- `BLOCKED`: no Screening package, results, acceptance, or stage movement produced in r1. After reviewed Core repair, rerun the contracted r1 flow cleanly from this exact State and report fresh validation (failed run is not carried forward as PASS).
