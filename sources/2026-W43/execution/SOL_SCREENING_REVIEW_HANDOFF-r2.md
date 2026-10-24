# Sol Screening Review handoff r2 — 2026-W43 (2026-10-25)

Status: `SOL_SCREENING_REVIEW_READY_R2`
Edition `2026-W43` / WEEKLY / WEEKLY_MAGAZINE. Branch `weekly/2026-W43-v2-work`.
Starting HEAD/Tree (remote-verified read-only): `d38035814c9cd4541849b37d542c709812a876c8` / `6d18d03d8e73240d1970cc9f042e794b1df269cc`.
Reviewed main: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36a407d08ab1de416324229b3955e0325a`.
Frozen Core: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
State at work: `DISCOVERY_COLLECTED`, next `stage:screening` (unchanged; no `ADVANCE_STAGE`).
Contracts: r1 `sol-w43-screening-r1-20261025.md` (BLOCKED on legacy path) + r2 `sol-w43-screening-native-agent-tool-retry-r2-20261025.md` (native compat route). Blocker review: `sol-w43-screening-blocker-native-adapter-review-20261025.md`. r1 defect/session preserved unchanged.

## Method (frozen Core-native agent-first only)
- `survey_agent_tool_v2` allowlisted `survey_screening_v2.prepare` (4 batches 13/13/13/12, IMPL = work HEAD `d38035814…`) then `accept` (IMPL recomputed, same HEAD). Frozen blob `16e6ab90…` identical on main/frozen/W43. Protected paths unchanged vs reviewed main.
- Adapter unit tests 5/5 PASS; isolated negative tamper test fail-closed OK (tampered State copy rejected, 12 errors); canonical bytes re-verified untouched after all runs.
- Legacy direct CLI re-confirmed FAIL (exit 2, zero writes): DIRECT_LEGACY_FAIL vs AGENT_FIRST_NATIVE_PASS recorded separately; legacy incompatibility (Issue #568) untouched and still open.

## Outputs (paths + SHA256)
- Package `screening/v2/packages/r1/package.json` — `b7e9a6d4…` (51 records, batches batch-001..004, basis state `885927bd…` / discovery `f62d8459…`).
- Results `screening/v2/packages/r1/results/batch-001..004.json` (13/13/13/12; per-batch basis hashes pinned).
- Accepted `screening/v2/accepted/185257742e7a5ad7d2253312e4cc1bd731da6fd9fe484f7b978a8de85f5e93af/screening-accepted.json` — `666927d4…` (51 decisions, content-addressed dir).
- Summary `execution/source-intake/w43-screening-summary-r2.md` — `a463ed82…` (distribution, ledger, evidence targets, limitations).

## Distribution: KEEP 17 / MAYBE 11 / INSPECT 4 / DROP 19 (51/51, every ID exactly once)
- KEEP: DeepInfer, DeepSeek-1017, Duet, Eleven, FLUX-Max, Kimi, Nemotron-E4B, TanStack, Voxtral, 1Password, MemT, Ming, MOSS-trainer, OpenAI-bio, OpenAI-lowresource, OpenAI-securing, Flint.
- INSPECT (locator/RSS-only): auto-mode, Decisions-API, OpenAI-Cloud, Patch-Planet.
- MAYBE: Muse-10M, oracle-rev, GitHub deprecation/metrics/Teams, MOSS report-announce + API, AM-Bench v2, Vercel/Ollama, Claude-perf carry, Grok ledger (audit binder, NOT a technical release).
- DROP: 8 OUT/background (Qwen, Step5, Gemini-safety lead, MOSS-base, DeepInfer-repo, OR-License, AM-Bench-v1, ARC) + 11 W42 carry rechecks (quarantines/UNRESOLVED/no-new-material; W42 dispositions stand).
- Duplicates: none declared; r3 family dedup stands. Grok ledger never a Selection candidate.

## Validation (real stdout/exit, pre-commit)
- r4-equivalent schema 51/51 per batch, Core graph (via prepare/accept), raw_refs exist, Flint + ledger bind exact Grok Raw (manifest `discovery_ids` match).
- X `require_complete` PASS (COMPLETE/PARTIAL unchanged); acceptance `validate_acceptance` PASS via adapter `accept`; stage-contract precheck PASS (`DISCOVERY_COLLECTED`→`CANDIDATES_NORMALIZED`, to `/tmp`, state untouched); profile/state PASS; execution-record PASS.
- Changed-file safeguard: edition-local W43 only (screening package/results/accepted, summary, handoff, session, index); no shared/W42/Grok-Raw/Core/State/checkpoint writes.

## Still conditional
PARTIAL sensor (2 pinned posts, no repro); rendered-body consumption; 0 independent repros; AM-Bench v2 delta; weight/card/license bytes for some families; INSPECT/MAYBE rows need inspection before Evidence reliance.

## Sol decision requested
r2 screening review (distribution + dispositions + evidence targets). Trusted `ADVANCE_STAGE` (`DISCOVERY_COLLECTED`→`CANDIDATES_NORMALIZED`) only after Sol approval via immutable operator request.
