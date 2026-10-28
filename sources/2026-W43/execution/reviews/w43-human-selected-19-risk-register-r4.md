# W43 human selected-19 risk register r4 (prioritized, edition-local)

Status: `HUMAN_ORIENTED_RISK_LEDGER / NATIVE_ATTENTION_UNCHANGED`
Date: 2026-10-25. Starting HEAD `db78839bd7cb858a6cc5b1620bf6c574f064339f`.
Native attention `architecture-review-attention-v2.json` is unchanged by design (68/68 unique, limit 100, overflow 0, truncated false; SHA `7c3e4deb…`): it is exception-centered (19 EXCLUDED + 2 NON_MATERIAL + 19 DROP + 4 INSPECT + 11 MAYBE + 1 HOLD + 12 REJECT) and contains ZERO items pointing at SELECTED candidates. This ledger is the separate human-readable bridge required by ISA-006. It invents no native priority attribute. Selection 19/1/12 and 8-package placements are invariant.

## How to read

- Priority: P1 = blocks reader-facing technical claims until resolved; P2 = must be bounded in prose/tables; LIMITED = standing vendor-only / unreproduced limitation carried into Draft.
- Verification tier: FIRST_PARTY_DESCRIBED (publisher states it) vs VENDOR_ONLY_BENCH (publisher measured, no independent rerun) vs UNRESOLVED_CONFLICT (publishers disagree) vs UNVERIFIED (no proof either way).
- Attention linkage: which of the 68 native items already covers adjacent background (never the selected claim itself).

## P1 — resolve before any Draft sentence claims it

| # | Candidate (suffix) | Article | Risk | Tier | Do-not-claim | Expected reader action | Attention link |
|---|---|---|---|---|---|---|---|
| 1 | DeepInfer `409f6833…` | P2 §2.2 lead | Deterministic sampling was co-described with variable-length MTP as if simultaneously enabled. | FIRST_PARTY_DESCRIBED (README read 2026-10-25) | Do NOT present `MTP_VARLEN=1` + deterministic sampling as one setup. Do NOT generalize reproducibility beyond NVIDIA + fixed `seq_seed`. | r4 Architecture separates DSpark MTP (`VARLEN=1`, nextn default 5/0-off) from deterministic sampling (`VARLEN=0` + `BATCH_INVARIANT=1` + fixed `seq_seed`, NVIDIA only) as排他的構成例 with MUST-NOT. | None of the 68 (new P1). |
| 2 | Voxtral 3 `18a859eb…` | P5 §5.1 lead | Three official Mistral pages disagree on TTS language support (announcement 35+/50+; model card 9; language matrix 35/50+; presets 18 vs 22). | UNRESOLVED_CONFLICT | Do NOT publish any single universal TTS language number. Do NOT assert "9 = presets" (presets are 18/22, not 9). Do NOT count the 11-language eval sample as support coverage. | r4 Architecture tabulates STT / realtime / TTS / cloning / presets by model + source + date with `UNRESOLVED_VENDOR_DOC_CONFLICT`; Draft must carry the conflict note. | None of the 68 (new P1). |

## P2 — bound in prose/tables (wrong bound = wrong article)

| # | Candidate | Article | Risk | Tier | Do-not-claim | Expected reader action | Attention link |
|---|---|---|---|---|---|---|---|
| 3 | Nemotron Bolt `8f140062…` | P1 §1.2/§1.5 support | "4B-class" hides 8B total vs 4B effective; license has two layers. | FIRST_PARTY_DESCRIBED (model card read 2026-10-25) | Do NOT equate 4B effective with 4B total; do NOT call OpenMDW-1.1 OSI-approved; do NOT attribute Gemma-4 terms to NVIDIA weights. | Show 8B total / 4B effective with convention in header; separate OpenMDW-1.1 (weights) from Gemma-4 Apache-2.0 (base). | None (counting is new). |
| 4 | Flint `4cea2926…` | P1 §1.2 lead | ~2.5B active uses output-head-in / input-embedding-out convention (body ≈2.2B). | FIRST_PARTY_DESCRIBED (model card read 2026-10-25) | Do NOT present 2.5B as total; do NOT compare 2.5B active directly against 4B effective. | Show 39.8B total / ~2.5B active per token with convention in header; mark non-equivalence with Nemotron. | None (counting is new). |
| 5 | FLUX 3 Max `02df2773…` | P4 §4.2/§4.3 lead | Arithmetic is correct but apparatus is unverified; vendor blog contradicts itself (26.5x/96.2% vs 12.45s/277.80s); 10.95s PR raw absent. | VENDOR_ONLY_BENCH + arithmetic recomputed here | Do NOT call 22.31x an independent measurement; do NOT cite 26.5x as fact; do NOT claim identical resolution/GPU/batch/quality/cold-warm. | Label quotients as recomputation of vendor figures; keep UNKNOWN comparability; keep fastest-headline ban. Selection rationale historic wording (`PR 10.95/277.80=…`) is preserved for invariance — Architecture §4.2 is authoritative. | None of the 68 (methodology lead). |
| 6 | Decisions API `d278dfe7…` | P8 §8.1 lead | "Output free + $0.10/$0.01" misreads as all-in flat rate; 400 misreads as account quota. | FIRST_PARTY_DESCRIBED (guide read 2026-10-25) | Do NOT present output-token $0 as zero bill (cache writes + regional + long-context extra); do NOT present 400 as total calls. | Qualify every price with cache-write-billed / regional / long-context multipliers; state "400 per request". | SELECTION INSPECT-adjacent background only (`SCREENING:w43-primary-decisions-api-20261022:INSPECT`); cost qualifier is new. |
| 7 | Review Attention itself | Process | 68/68 covers only exceptions; a reader could mistake it for selected-claim coverage. | N/A (mechanical) | Do NOT cite the 68 as evidence that selected-19 claims were re-checked. | Keep native 68 byte-identical; use THIS ledger as the selected-19 checklist. | All 68 (group counts: EXCLUDED 19, NON_MATERIAL 2, DROP 19, INSPECT 4, MAYBE 11, HOLD 1, REJECT 12). |
| 8 | P8 density | P8 plan | 3.5 pages for Decisions + TanStack + DeepSeek tempts padding or over-claim. | LIMITED | Do NOT pad to fill pages; do NOT invent lengthy procedure from thin sources. | Cost one Decisions example + stable-vs-experimental TanStack table + DeepSeek revision/availability note; shrink supplements to briefs if sources are thin. P8 3.5 is ESTIMATE. | None. |
| 9 | Japanese wording | P1–P8 | `符号生成モデル`, `hyper記憶`, undefined `声の様式`/`数表批判`, bare `最速` mislead readers. | Editorial | Do NOT use `符号生成モデル`; do NOT leave Gated DeltaNet-2 / Mixture-of-Storage / context biasing / cpWER / effective parameters undefined at first use; do NOT use unqualified `最速`. | r4 uses コード生成モデル(code generation), 日英併記 first-use definitions, and keeps `最速` only inside MUST-NOT bans. | None (language). |
| 10 | Availability/timing | P1/P3/P8 | Kimi weights Nov4 FUTURE vs API IN; Duet waitlist vs live; TanStack Oct22 release vs Oct23 blog; Metrics post-cutoff. | FIRST_PARTY_DESCRIBED where dated | Do NOT present Nov4 weights as published, Duet/1Password as live, Oct23 blog as product clock, or Metrics 23:42:03Z as W43. | Status columns distinguish announcement / waitlist-preview / GA / weights-delivered / reproduced. Metrics stays OUT; Grok binder stays NEVER_STORY. | `SELECTION:candidate:2026-W43:642c261d5e82c786:REJECT` (Metrics), `SCREENING:w43-primary-github-metrics-20261023:MAYBE`, `SCREENING:w43-r4-grok-x-ledger-20261024:MAYBE`. |

## LIMITED — standing vendor-only / unreproduced (carried into Draft with attribution)

| # | Candidate | Article | Standing limit | Attention link |
|---|---|---|---|---|
| 11 | Kimi K3.1 Pro `98f3617d…` | P1 lead | 2.8T/104B is X-only; Nov4 weights FUTURE; API early, no local run/hash. | None of 68 (selected lead). |
| 12 | MemT-1.0 `b09782ca…` | P2 lead | 65pp equations/ablations not line-read; 1.86x/66x author-measured on different denominators; no independent run. | None of 68 (selected lead). |
| 13 | Duet `3670fe43…` | P3 lead | 6000+ catalogue ≠ live inventory; waitlist/US Pro/Max first; behaviour unreproduced. | None of 68. |
| 14 | 1Password `673368bc…` | P3 support | Coming soon at cutoff; approval-injection behaviour unreproduced. | None of 68. |
| 15 | auto-mode `ac27404f…` | P3 support | Oct22 update IN, next-week default FUTURE; classifier gating unverified. | `SCREENING:w43-primary-automode-20261021:INSPECT` (locator-level background). |
| 16 | Eleven `45140887…` | P5 support | OpenAI-protocol compat ≠ drop-in; migration guide unopened; AA unfetched. | None of 68. |
| 17 | Ming `4aa7ba12…` | P5 support | AA ranks are publisher-cited; AA originals missing; roadmap pending. | None of 68. |
| 18 | Patch Planet `5d21d93e…` | P6 lead | Rendered text only (bot-wall, no original HTML); vuln/patch scope vendor-described. | `SCREENING:w43-primary-patch-planet-20261021:INSPECT` (RSS-level background). |
| 19 | Securing `eb731206…` | P6 lead | Containment/red-team vendor-described; page clock day-only + RSS 10:00Z secondary. | None of 68. |
| 20 | Bio `6c420e98…` | P7 lead | Team-internal + blinded 75% coauthored preference; wet-lab absent; ZERO reproduction. | None of 68. |
| 21 | Low-resource `160489b7…` | P7 lead | Hidden tests vendor-held; suite public ≠ reproduced; costs vendor-measured. | None of 68. |
| 22 | TanStack `20a36d83…` | P8 support | 1.0 stable packages but harness 0.x experimental; Oct22 release vs Oct23 blog separated. | None of 68. |
| 23 | DeepSeek 1017 `d5bceca2…` | P8 support | Weight/model artifact not locally rehashed; billing transition untested; vendor harness footnotes. | None of 68. |
| 24 | HOLD KohakuMoss `b26dfd2c…` | — | Third-party trainer Oct18 IN (base Oct16 OUT distinct); no independent 5090 rerun; custom license. | `SELECTION:candidate:2026-W43:b26dfd2c2e5ac943:HOLD` (the single HOLD item). |

Counts check: 2 P1 + 8 P2/process + 14 LIMITED/held-selected (11–24 minus HOLD = 13 selected LIMITED + 1 HOLD) = 24 rows for 19 selected + 1 HOLD + process/method rows. All 19 selected candidate IDs appear at least once. No native 68 item is altered, reprioritized, or cited as selected-claim proof.
