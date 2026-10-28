# W43 Sol → Muse Screening r3 — one-character-class chronological repair of accepted decision

Status: `BOUNDED_SCREENING_CORRECTION / NATIVE_FROZEN_CORE / NO_STAGE_ADVANCE`
Date: 2026-10-25 JST
Repository: `eariver/japanese-generative-ai-survey`
Branch: `weekly/2026-W43-v2-work` (existing only)
Sol review: `sources/2026-W43/execution/reviews/sol-w43-screening-r2-chronology-review-20261025.md`
**Exact Starting HEAD/Root Tree will be provided in the Sol dispatch after this instruction and index are committed.**
Preflight read-only W43 work HEAD+Tree exact dispatch values; main HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree `a134dc36a407d08ab1de416324229b3955e0325a`; frozen Core HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. Mismatch ANY → ZERO WRITES and STOP. No branch creation/fallback/reset/rebase/force.

## 1. Original authority, preserved

- Muse Screening r2 `SOL_SCREENING_REVIEW_READY_R2`, final work SHA `757d62c59d82d0e9745e27734756ee984c79623e`, root Tree `d5bfb59280bc65b40bf7d491eb4be152cab521c8`.
- Original immutable Screening run `sources/2026-W43/screening/v2/packages/r1`, accepted path `sources/2026-W43/screening/v2/accepted/185257742e7a5ad7d2253312e4cc1bd731da6fd9fe484f7b978a8de85f5e93af/screening-accepted.json`. Do not alter ANY of these files or rename existing acceptance. Result digest `185257742e7a5ad7d2253312e4cc1bd731da6fd9fe484f7b978a8de85f5e93af`, package SHA `b7e9a6d4b138ef3c9ceb06f76537d9bf23ba26796475b9c2933e9ad36b718aa0`. 51 decisions / 51 IDs, KEEP 17, MAYBE 11, INSPECT 4, DROP 19; batches 13/13/13/12.
- Core-native adapter `scripts/survey_agent_tool_v2.py` (Git blob `16e6ab9050b92526004b69d7ef1852c103110703`, identical across main/Frozen Core/work); r2 adapter tests 5/5 PASS, negative State tamper fail-closed, native prepare/accept PASS. Legacy direct Core path remains defective, tracked OPEN Issue #568; never report direct legacy PASS.
- W43 State `DISCOVERY_COLLECTED`, next `stage:screening`; Discovery acceptance 51-record SHA `edad13b1a90fa4965fe2ef37f9ce522c110ffed7727d839e4e62fde04ec93f1b`. Frozen Profile/State/Stage Checkpoint/Grok/Accepted Discovery and Human Gates immutable.

## 2. ONE exact logical correction

- Accepted Screening record ID: `w43-primary-kimi-20261023`.
- Existing r2 `reason` text: `KEEP: announce and API live Oct 23 17:15:24Z (45min inside cutoff, X HTML archived); ...`
- Correct portion only: `KEEP: announce and API live Oct 23 17:15:24Z (4h44m36s before Oct 23 22:00Z cutoff, X HTML archived); ...`
- Basis: accepted Discovery `sources/2026-W43/discovery/discovery-v2.jsonl` has `published_at=2026-10-23T17:15:24Z`, notes `4h44m before cutoff`; Profile `cutoff=2026-10-23T18:00:00-04:00` = `2026-10-23T22:00:00Z`. Difference = 4h44m36s. Its `metadata.r3_correction` explicitly says earlier 45-minute error fixed. The r2 Screening reason reintroduced the old error despite keeping proper W43 IN and KEEP status.
- Do not change `decision=KEEP`, confidence, targets, other source IDs, vendor caveats, model/weights status, date, or any other record. This is a **reason string only** correction; no new Source Intake or research. Do not change original r2 batch/results/acceptance. Write explicit W43 edition-local Screening r3 erratum with before/after, 51-to-51 complete identity proof.

## 3. Canonical clean acceptance r3

1. Re-validate current agent-first State via frozen `survey_agent_control_v2.validate_agent_state`; X manifest and Discovery acceptance remain unchanged. Verify expected r2 Screening original exact 51 IDs and acceptance before correction.
2. Create new **`sources/2026-W43/screening/v2/packages/r2`** using frozen first-party agent tool:
```bash
IMPL="$(git rev-parse HEAD)"
python -m scripts.survey_agent_tool_v2 \
  --repo-root . \
  --state sources/2026-W43/production-state.json \
  --helper scripts/survey_screening_v2.py -- \
  prepare \
  --state sources/2026-W43/production-state.json \
  --discovery sources/2026-W43/discovery/discovery-v2.jsonl \
  --output-dir sources/2026-W43/screening/v2/packages/r2 \
  --max-records 13 \
  --implementation-sha "$IMPL"
```
3. Reproduce the previous 51 decisions by ID from r2 result set (do not hand-invent new Screening substance). Materialize schema-valid new results for `packages/r2/results/batch-001..004.json` with exact new Core package batch basis and hash contracts. The previous Kimi record is in batch-003, but look it up by discovery ID rather than assuming batch order. Modify precisely its `reason` portion shown in §2; ensure the other 50 decision objects have exact equality and Kimi all non-reason fields equality. New input/batch hashes must match Core package; no manual acceptance/hash forging.
4. Run canonical frozen Core-native `accept` from same allowlisted adapter, current actual HEAD:
```bash
IMPL="$(git rev-parse HEAD)"
python -m scripts.survey_agent_tool_v2 \
  --repo-root . \
  --state sources/2026-W43/production-state.json \
  --helper scripts/survey_screening_v2.py -- \
  accept \
  --package sources/2026-W43/screening/v2/packages/r2/package.json \
  --results-dir sources/2026-W43/screening/v2/packages/r2/results \
  --accepted-root sources/2026-W43/screening/v2/accepted \
  --implementation-sha "$IMPL"
```
5. Require **new** content-addressed `screening/v2/accepted/<NEW_SHA>/screening-accepted.json` different from old r2 digest; validate the exact package copy, 4 batch outputs, 51 decisions, unique IDs, SAME histogram, exactly one `reason` difference, raw/Discovery/X binding, accepted result hashes, native `screening.validate_acceptance`, stage validation to temporary output only, execution record validator. If new digest accidentally equals old, STOP (not corrected). No other old accepted files modified.
6. Record r3 erratum, new SHA/path, actual stdout/exit, tests and equality count, state/human gate unchanged, updated `execution/index.md`, one proper session log `execution/sessions/muse-w43-screening-chronology-r3-20261025.md` and `execution/SOL_SCREENING_REVIEW_HANDOFF-r3.md`. Previous r1 BLOCKED and r2 original accepted run preserved. Normal commit non-force push same branch; remote final SHA/Root Tree readback.
7. Do not mark direct legacy Core CLI PASS; use native agent-first validator. Do not edit `production-state.json`, Stage Checkpoints, existing trusted operator requests, Core files, W42, Human Gates, Grok/Discovery, or start Evidence/Selection/Architecture. NO `ADVANCE_STAGE` or Issue #448 comment in this run.

STOP: `SOL_SCREENING_REVIEW_READY_R3`, return final remote HEAD+Tree and new acceptance path/digest/distribution and one-row diff. Any Core failure → BLOCKED with diagnostic; no shortcut.
