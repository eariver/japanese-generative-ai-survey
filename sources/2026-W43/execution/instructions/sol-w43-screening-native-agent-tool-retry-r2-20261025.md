# Sol W43 Screening r2 — clean replay using frozen Core-native agent-first tool

Status: `EXISTING_FIRST_PARTY_COMPATIBILITY_ROUTE / BOUNDED_SCREENING_RETRY / NO_CORE_PATCH`
Date: 2026-10-25 JST
Repository: `eariver/japanese-generative-ai-survey`
Branch: `weekly/2026-W43-v2-work` **existing only**
Sol blocker adjudication: `sources/2026-W43/execution/reviews/sol-w43-screening-blocker-native-adapter-review-20261025.md`
Historical failed run and diagnostic (PRESERVE): `sources/2026-W43/execution/defects/w43-screening-prepare-state-basis-20261025.md`; remote HEAD before Sol review `3ee1ef1d73ab1d2436457299e0021bd0ae2c2f24` / root Tree `8e9a9f160a4e6cee907dba5f8d8ec51f5460d26b`.
**Exact Starting HEAD and Tree will be provided in the Sol dispatch following final instruction/index commits.** Read-only verify work HEAD & Tree plus main `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree `a134dc36a407d08ab1de416324229b3955e0325a`, frozen Core HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. Any mismatch: ZERO WRITES and STOP; no alternative branch, fallback/rebase/reset/force.

## 1. Engineering correction — native frozen mechanism exists

- The prior contract naively called `python -m scripts.survey_screening_v2 prepare` directly. After valid trusted agent-first Stage transition it fails legacy `survey_production_v2.verify_state_basis` (init SHA pin and `attestations/discovery.json` expectations) even for genuine bridge-advanced `DISCOVERY_COLLECTED` State.
- Preserve the prior `BLOCKED` result as valid evidence **about the direct legacy entrypoint**, but it does **not** establish that all frozen Core paths are unusable. Existing Issue #568 already documented the identical W42 problem plus the **first-party** `scripts/survey_agent_tool_v2.py` compatibility surface.
- Frozen helper `scripts/survey_agent_tool_v2.py` Git blob `16e6ab9050b92526004b69d7ef1852c103110703`, verified byte-identical on reviewed main, frozen Core branch, and W43. It strictly allowlists only two helpers, runs `agent.validate_agent_state`, ensures **actual current work-branch HEAD = helper implementation SHA**, scopes compatible admission to a contextmanager with finally-restoration, retains all original profile/contract/batch/source/hash checks and rejects tampered State, unaccepted archived packages, missing output or non-State basis drift. `survey_stage_validation_v2.validate_stage` uses this exact compatibility context already.
- Existing tests: `tests/test_survey_agent_tool_v2.py` covers acceptance-bound State hash exception and non-State negative drift. Use **unchanged frozen** script and tests, not a new wrapper/monkeypatch, no `pip install`, no Core patch. The direct helper remains defective and Issue #568 stays OPEN.
- Worker r1 text/session mis-typed the prior exact starting HEAD. Actual Git parent is `377bec67fd12d0c2aa2b534910f73bb7831e407c` (not `...bc aeecbe46b`). New session must record actual SHA accurately; source historical failed log remains immutable, Sol review records erratum.

## 2. Fail-closed preflight and negative verification

1. Read-only exact work/main/frozen HEAD+Tree, confirm no protected-path changes since reviewed main and verified frozen script/blob.
2. State `sources/2026-W43/production-state.json`: `DISCOVERY_COLLECTED`, next `stage:screening`, Discovery checkpoint `passed`, Human Gates `pending`. Validate through **`survey_agent_control_v2.validate_agent_state`** (not just schema); verify exact trusted checkpoint `orchestration/v2/checkpoints/ISSUE_INITIALIZED.json`, receipt and accepted Discovery.
3. Confirm accepted Discovery exact 51 records and graph `5a94b7574b9d59f05bd82e00cb464512b359a45eae00a2721b1d119abc4bd43a`; Grok X manifest `COMPLETE`, quality `PARTIAL`, raw `13425B` SHA256 `4571e0de469a7143fb1c46710c2e419a91404ff2d9538ae4d9a31a8b8f0be54a`. Never alter State/checkpoint/Acceptance.
4. Run pre-existing adapter unit tests and at least one **read-only isolated** negative tamper test against a copied/fake State or accepted package; do not weaken error behavior and do not edit canonical bytes. Record test command, stdout/stderr, exit. Do NOT claim direct legacy `validate-state` PASS: the incompatibility is still open.
5. Confirm proposed package location `sources/2026-W43/screening/v2/packages/r1` is absent or empty (failed r1 had no package). If nonempty/ambiguous, STOP rather than overwrite; no silent backup/fallback.

## 3. Exact first-party invocation surface

Use *this* frozen-Core-native entrypoint (not direct `survey_screening_v2.py`) from actual checked-out branch, with a real present-tense HEAD:

```bash
IMPL="$(git rev-parse HEAD)"
python -m scripts.survey_agent_tool_v2 \
  --repo-root . \
  --state sources/2026-W43/production-state.json \
  --helper scripts/survey_screening_v2.py -- \
  prepare \
  --state sources/2026-W43/production-state.json \
  --discovery sources/2026-W43/discovery/discovery-v2.jsonl \
  --output-dir sources/2026-W43/screening/v2/packages/r1 \
  --max-records 13 \
  --implementation-sha "$IMPL"
```

Re-verify/record the exact current HEAD before **every** later helper invocation. If commits occur in between, recompute `IMPL="$(git rev-parse HEAD)"` at the new HEAD; no stale init `7a969fd9…` and no special override that claims an absent revision.

Use genuine prompt `config/prompts/source-screening-v2.md` and schemas `screening-v2-run-package.schema.json` / `screening-v2-batch-result.schema.json`. It should partition 51 accepted rows into bounded batches (≤13 per batch, likely 4 batches). The Core package supplies exact input identities and hashes.

Produce exactly 51 complete Screening decisions, one per ID, according to source identity, W43 window and full content. Decide `KEEP/MAYBE/DROP/INSPECT` with grounded reason, free-form scope tags, duplicate group, concrete verification targets and honest confidence. No invented model/reproduction benchmarks or generic boilerplate. High-value first-party in-window events (Flint, Kimi API, MemT, OpenAI technical/safety, agent credentials, MOSS trainer/API, DeepSeek, Nemotron 64K E4B, audio/video) get substantive independent technical assessment. Carefully distinguish W42 12 carry rechecks, original OUT versus genuinely new IN versions/events and Grok ledger as non-release audit binder. Sensor `PARTIAL` is not article Selection.

For results use the exact Core generated batch IDs / schema and basis hashes. Then execute **the same native adapter**:

```bash
IMPL="$(git rev-parse HEAD)"
python -m scripts.survey_agent_tool_v2 \
  --repo-root . \
  --state sources/2026-W43/production-state.json \
  --helper scripts/survey_screening_v2.py -- \
  accept \
  --package sources/2026-W43/screening/v2/packages/r1/package.json \
  --results-dir sources/2026-W43/screening/v2/packages/r1/results \
  --accepted-root sources/2026-W43/screening/v2/accepted \
  --implementation-sha "$IMPL"
```

Canonical result is content-addressed `sources/2026-W43/screening/v2/accepted/<result_set_sha256>/screening-accepted.json`. Validate entire result, source and acceptance path using frozen Core agent-first context (the same adapter, its internal `accept` invokes `validate_acceptance`; independent read-only evaluation via `with current_stage_basis_override()` is permitted). Do not claim legacy direct helper PASS; record `DIRECT_LEGACY_FAIL / AGENT_FIRST_NATIVE_PASS` separately. If native path fails, STOP/BLOCKED and report actual failure, no manual PASS.

## 4. Deliverables and strict stop

- All Core-generated Screening packages, complete batch inputs and output decisions, accepted content-addressed Screening result set, 51/51 count, exact package/results SHA and decision histogram.
- Explicit Source Intake/period disambiguation and out-of-window/duplicate/carry-over disposition ledger, top Evidence verification targets and original raw-depth limitations; do not exaggerate 0 independent reproductions.
- One new W43 edition-local session `execution/sessions/muse-w43-screening-native-r2-20261025.md`, one `execution/SOL_SCREENING_REVIEW_HANDOFF-r2.md`, `execution/index.md` update; append read-only logs for native adapter tests and legacy failure as appropriate. Prior blocked r1 log/defect kept intact and linked, no changing passed/disallowed stage.
- All Core schemas, acceptance/hash checks, `survey_execution_record_v2` validator and protected path checks PASS under their *proper* agent-first authority. Negative tamper checks must FAIL CLOSED as expected.
- Normal commit/non-force push on this **same existing W43 branch**, remote HEAD+Root Tree readback.

**Do not** advance `DISCOVERY_COLLECTED`, alter `production-state.json` / Stage Checkpoints, create operator request/Issue #448 comment, run Evidence/Selection/Architecture/Human Gates, edit W42 or shared/frozen Core or tests. No fallback/repair/review branch, no reset/rebase/force.

STOP `SOL_SCREENING_REVIEW_READY_R2`, return final remote HEAD/Tree and Screening acceptance path/distribution/validator results. Sol will independently review and only then authorize a trusted Stage transition.
