# W43 Sol independent Screening r1 blocker adjudication — use existing frozen-Core agent-first adapter

Status: `SOL_BLOCKER_REVIEW / LEGACY_CORE_PATH_FAIL_CONFIRMED / NATIVE_COMPAT_EXECUTION_AUTHORIZED`
Date: 2026-10-25 JST
Repo: `eariver/japanese-generative-ai-survey`
Reviewed W43 HEAD/Root Tree: `3ee1ef1d73ab1d2436457299e0021bd0ae2c2f24` / `8e9a9f160a4e6cee907dba5f8d8ec51f5460d26b`
Actual blocked commit parent: `377bec67fd12d0c2aa2b534910f73bb7831e407c`.
Reviewed main: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`
Frozen Core: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

## Reviewed authority

- Worker W43 r1 BLOCKED record `execution/defects/w43-screening-prepare-state-basis-20261025.md` and `execution/sessions/muse-w43-screening-r1-blocked-20261025.md` are preserved unmodified. Worker created **0/51** Screening decisions, no accepted Screening, no State or Human Gate changes. Bridge run `40116386580` generated legitimate `DISCOVERY_COLLECTED` State and Discovery checkpoint.
- Git readback proved W43 blocked commit `3ee1ef1d…` descends directly from prior exact HEAD `377bec67fd12d0c2aa2b534910f73bb7831e407c`. Note: the worker's textual blocked report/session mis-transcribed that STARTING SHA as `377bec67fd12d0c2aa2b534910f73bbcaeecbe46b`; this is NOT the Git commit parent. Treat report SHA as a **transcription defect**, not evidence of a wrong actual parent. The expected Tree matches.
- Root cause checked against frozen code: `scripts/survey_screening_v2.py::prepare_package` and `validate_package_basis` call legacy `survey_production_v2.verify_state_basis`. Its `validate_state_semantics` rejects agent-first Stage checkpoint name `orchestration/v2/checkpoints/ISSUE_INITIALIZED.json` instead of legacy per-checkpoint attestation and incorrectly demands every history entry SHA equal to the init implementation SHA. Official `survey_agent_control_v2.advance_with_checkpoint` uses FROM-state checkpoint filename + real current event commit for each history row. Therefore direct helper FAIL is expected for a valid agent-first State.
- Existing repository Issue **#568** already records identical W42 Evidence failure and a human policy **Core modification prohibited/frozen**. Sol appended W43 cross-edition reproduction to that existing Issue, preserving deferred maintenance.
- **Previously missed native solution**: frozen `scripts/survey_agent_tool_v2.py` provides `run_helper` for exactly allowlisted `scripts/survey_screening_v2.py` and `scripts/survey_evidence_v2.py`, `current_stage_basis_override()` and `verify_current_stage_basis()`. Blob SHA `16e6ab9050b92526004b69d7ef1852c103110703` matches independently on `main`, `production/survey-core-v2`, W43 blocked HEAD. This calls actual `agent.validate_agent_state` first, checks real execution HEAD and validates package hash contracts, then restores original verifier in finally. Historical State-SHA drift exception applies only to archived **accepted** content-addressed packages, not to prospective Screening r1.
- Frozen stage `survey_stage_validation_v2.validate_stage` already uses `with runtime_tool.current_stage_basis_override()`. Existing `tests/test_survey_agent_tool_v2.py` exercises archived package integrity and negative non-state drift; actual W43 end-to-end wrapper invocation has **not yet been executed by Sol**.
- State, accepted 51 Discovery rows, Grok original, X registration/Raw and pinned Stage checkpoint remain intact. No Core mutation or new trusted Stage advancement requested.

## Human decision

**NONE / NOT_APPLICABLE**. Sol's BLOCKED adjudication is an internal editorial/engineering instruction. This is neither Human Architecture Review nor Publication Preview and creates no approval or Human Gate decision. Both real Human Gates remain pending.

## Requested changes

**Supersede the Screening r1 direct CLI invocation only**, not the worker's accurate failure evidence. Execute the existing first-party `python -m scripts.survey_agent_tool_v2 --repo-root . --state sources/2026-W43/production-state.json --helper scripts/survey_screening_v2.py -- prepare ...` and later `-- accept ...`. Use current actual `git rev-parse HEAD` as implementation identity, **never the init SHA**. Detailed bounded command contract in `execution/instructions/sol-w43-screening-native-agent-tool-retry-r2-20261025.md`.

- First, validate real agent-first State and all pinned Stage artifacts fail-closed. Capture the legacy direct-helper r1 FAIL as expected known incompatibility (do not report as PASS). Run regression tests for frozen adapter and negative tamper/drift checks in isolated temporary paths.
- Use genuine `DISCOVERY_COLLECTED` state, exact same 51 accepted Discovery candidates; partition 13/13/13/12 (or Core deterministic partition output), produce 51 complete Screening decisions including all X/carry/OUT cases. No research scope expansion or fake evaluation.
- Run Core `prepare` and `accept` under the **same genuine first-party adapter**, with all other schema, package/state/profile/Raw/contract/identity checks intact. Validate result hashes and archive, inspect exact output and return complete distribution to Sol.
- Preserve failed r1 ledger/defect unchanged; new adapter run logs explicitly distinguish `legacy direct: FAIL` and `native agent-first: PASS`. Do not suggest legacy validator has been repaired or Core issue closed.

## Regeneration boundary

**W43 edition-local Screening r1 clean retry ONLY**; no state rewind, no Stage Checkpoint overwrite, no `ADVANCE_STAGE`, no Evidence/Selection/Architecture, no W42 writes, no Core `scripts/config/schemas/tests/.github` edits, no Human Gate. Stop `SOL_SCREENING_REVIEW_READY_R2` for independent Sol screening review. If wrapper fails, stop `BLOCKED` with diagnostic; do not manually create package/acceptance, hand-edit State or bypass checks.

## Shared-Core implication

**Known shared-Core direct-helper mismatch (Issue #568), deferred maintenance OPEN; no code patch approved**. The native agent-first adapter is pre-existing and unchanged across all reviewed branches and is the trusted compatibility execution surface. Use it rather than requesting ad hoc repairs or a new branch.
