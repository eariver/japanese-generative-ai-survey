# Muse W43 independent ISA closure — Architecture r4 (ISA-001…009 integrated)

Status: `ISA_REPAIR_COMPLETE / SOL_W43_ARCHITECTURE_R4_INDEPENDENT_ISA_REVIEW_READY (pending Sol re-audit)`
Date: 2026-10-25. Branch `weekly/2026-W43-v2-work`. Starting HEAD `db78839bd7cb858a6cc5b1620bf6c574f064339f` / Tree `b1ee9c3e686e3f50cfabc9d679eff7e01937726e`.
Reviewed main `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / Tree `a134dc36a407d08ab1de416324229b3955e0325a`. Frozen Core v2 `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481` (remote 6-way MATCH before any write; local aligned to remote HEAD).
Independent audit: `execution/audits/independent-sol-w43-selection-architecture-r3-comprehensive-audit-result-20261025.md` (Selection PASS_WITH_LIMITATIONS, Architecture REQUEST_CHANGES, P1 x2 + P2 x7). Adjudication: `execution/reviews/sol-w43-selection-architecture-r3-independent-comprehensive-adjudication-20261025.md`. Contract: `execution/instructions/sol-w43-architecture-r4-comprehensive-isa-repair-20261025.md`.
No `ADVANCE_STAGE`, no operator comment, no Human Gate decision, no Draft/TeX/PDF/Freeze/Release. Shared Core, accepted r4 Evidence/Views/Screening/Materiality/Completeness/State/Checkpoints/Gates/main/Frozen untouched.

## 1. Disposition of all nine findings

| ID | Sev | Disposition | Canonical change | Source authority | Residual |
|---|---|---|---|---|---|
| W43-ISA-001 DeepInfer determinism | P1 MUST_FIX | FIXED_SOURCE_BOUND | P2 §2.2 rewritten: DSpark variable-length MTP (`DEEPINFER_ENABLE_MTP_VARLEN=1`, `DEEPINFER_USE_NEXTN_DECODE` default 5 / 0 disables, pinned `9bd9cf24`) vs deterministic sampling (`DEEPINFER_ENABLE_MTP_VARLEN=0` + `DEEPINFER_BATCH_INVARIANT=1` + fixed `seq_seed` in `SamplingParams`, NVIDIA only) as排他的構成例 with explicit MUST-NOT against simultaneous use; boundaries duplicated the ban. | Official README `https://github.com/deepseek-ai/DeepInfer` rendered-read 2026-10-25 (batch-invariant = `BATCH_INVARIANT=1` NVIDIA only; deterministic = `BATCH_INVARIANT=1` + `MTP_VARLEN=0` + fixed `seq_seed` NVIDIA only); pinned `environ.py` 8738B + supplement `d0805b13…/e20f1cffc…` preserved. | None blocking. Pinned-main drift after Oct21 untracked (pre-existing boundary, kept). |
| W43-ISA-002 Voxtral TTS languages | P1 MUST_FIX | DOCUMENTED_UNRESOLVED_LIMITATION (Architecture ceases to assert any unified number) | P5 §5.1 rewritten as `UNRESOLVED_VENDOR_DOC_CONFLICT` table: STT 50 / realtime 35+/45 / TTS announcement 35+/50+ vs model card 9 vs matrix 35/50+ / presets 18 (announcement) vs 22-row Docs table / cloning separate / 11-language eval sample ≠ support count. Purpose carries UNRESOLVED note. Boundaries + MUST-NOT forbid unified number and "9 = presets". | (a) `https://mistral.ai/news/voxtral-3/` — TTS 35+/50+, presets 18 (read 2026-10-25); (b) `https://docs.mistral.ai/models/voxtral-mini-tts-3-0` — "Supports 9 languages" (read 2026-10-25); (c) `https://docs.mistral.ai/studio/audio/specs-and-limits/languages` — 35 languages / 50+ dialects, 22-row preset table + cloning note (read 2026-10-25). No versioned Mistral clarification retrieved. | UNRESOLVED across first parties — explicitly reported for Human/Draft (no fake PASS). |
| W43-ISA-003 Nemotron/Flint params | P2 | FIXED_SOURCE_BOUND | P1 §1.2: `Flint 39.8B total・~2.5B active per token[出力head含み・入力embedding除外、active body約2.2B]` / `Nemotron 8B total・4B effective[計数規約非一致、等価比較禁止]` with `total/effective/active/ctx[計数方法を列見出しに明記]`; §1.5 separates OpenMDW-1.1 (weights, OSI UNVERIFIED) from Gemma-4 Apache-2.0 (base); boundaries repeat non-equivalence + license split. | Nemotron BF16 card `https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-BF16` — "Total Parameters 8B (4B effective)", Gemma-4-E4B, OpenMDW-1.1 + Gemma Apache-2.0 (read 2026-10-25); Flint card `https://huggingface.co/RecursiveSI/flint` — 39.8B total, ~2.5B active incl. output head excl. input embedding, body ≈2.2B (read 2026-10-25). | None blocking. |
| W43-ISA-004 FLUX speedup | P2 | FIXED_SOURCE_BOUND + DOCUMENTED limit | P4 §4.2: `速度の独立再計算(独立測定ではない)` with `277.80/10.95≈25.37x`, `277.80/12.45≈22.31x`, `(277.80-12.45)/277.80×100≈95.52%[t_baseline/t_candidate]`; 10.95s PR raw still missing; resolution/10s/GPU/batch/quality/cold-warm UNKNOWN; blog 26.5x/96.2% marked incompatible; fastest-headline ban kept. Purpose gains `(数表批判:ベンダー数値の検証)`. | Vendor blog `https://fal.ai/blog/introducing-flux-3-max-by-fal` — 12.45s vs 277.80s with 26.5x/96.2% (read 2026-10-25); arithmetic recomputed here (25.3699 / 22.3133 / 95.5184%). | 10.95s PR origin raw still unarchived; comparability UNKNOWN carried. Selection rationale historic wording (`PR 10.95/277.80=…`) preserved byte-identical for Selection invariance — Architecture §4.2 is authoritative. |
| W43-ISA-005 Decisions cost | P2 | FIXED_SOURCE_BOUND | P8 §8.1: `400問 per request[総呼出上限ではない]`, `cache[読取$0.01/書込別課金]`, `$0.10/M uncached入力・cache $0.01読取・出力トークン課金なし[≠総無料、地域上乗せ・長文脈乗数あり]`, `10x vendor[独立未測定]`; boundaries repeat write-billed/regional/long-context + per-request. | Guide `https://developers.openai.com/api/docs/guides/decisions` — 400/request, cache reads + `cache_write_tokens`, $0.10/M uncached, cache writes charged, output tokens not charged, regional + long-context multipliers (read 2026-10-25). | None blocking. |
| W43-ISA-006 attention bridge | P2 | FIXED (separate ledger; native unchanged) | Native `architecture-review-attention-v2.json` untouched: 68/68 unique, limit 100, overflow 0, truncated false, SHA `7c3e4deb…` byte-identical r3. New `execution/reviews/w43-human-selected-19-risk-register-r4.md` lists all selected 19 (2 P1 + 8 P2/process + 13 LIMITED + 1 HOLD row) with priority, section, tier, do-not-claim, action, and 68-item linkage. No native priority invented. | Native counts: MATERIALITY:EXCLUDED 19, NON_MATERIAL 2, SCREENING:DROP 19, INSPECT 4, MAYBE 11, SELECTION:HOLD 1, REJECT 12. | None blocking. |
| W43-ISA-007 P8 density | P2 | FIXED (estimate + content plan) | P8 `page_allocation` kept `3.5` (ESTIMATE); `editorial_note` → costed plan (Decisions example + stable-vs-experimental TanStack + DeepSeek revision note; no padding; shrink to briefs if thin). `page_plan.notes` records P8 3.5 ESTIMATE + plan. All 8 allocations unchanged (5.0+6.0+4.5+3.0+4.5+4.0+4.5+3.5=35.0 +2.0=37.0). | No new source needed; plan is editorial. | Density risk remains if Draft over-writes — plan constrains it. |
| W43-ISA-008 Japanese | P2 | FIXED | Goal[5] rewritten (コード生成, first-use 日英併記 rule, vendor superlative ban); P1 purpose `符号生成モデル→コード生成モデル(code generation)`; P2 purpose `hyper記憶→動的記憶[Gated DeltaNet-2]・外部記憶[Mixture-of-Storage]`; P2 §2.4 first-use glosses (ゲート付きデルタネット2 / 混合ストレージ記憶 / 用語辞書による認識誘導 / 連結最小置換WER); P3–P7 English glosses (credential never visible, classifier gating, frontier training containment, blinded evaluation, defense in depth); `最速` kept ONLY inside MUST-NOT bans; `声の様式`/`数表批判`/`先端モデル` defined at first use. Titles unchanged (8 IDs preserved). | Editorial (auditor word list). | None blocking. |
| W43-ISA-009 availability | P2 | FIXED | P1 §1.5 + boundaries: Kimi X `2026-10-23T17:15:24Z` IN vs Nov4 weights FUTURE, separate status columns; P3 §3.2/§3.4 + boundaries: catalogue vs live, 1Password coming soon, auto-mode FUTURE; P8 §8.2/§8.3 + boundaries: TanStack Oct22 release IN vs Oct23 blog UNRESOLVED, Metrics `23:42:03Z` POST_CUTOFF/OUT + Grok NEVER_STORY never promoted. | Cutoff `[2026-10-16T22:00:00Z, 2026-10-23T22:00:00Z)`; Metrics 23:42:03Z = +1h42m03s after (excluded); TanStack registry 15:18:14Z / release 15:21:49Z IN. | None blocking. |

P1 source-correctness gate: both P1s are source-bound (001 recomputed separation from live README + pinned bytes; 002 explicitly unresolved with three cited official pages and no unified number). No P1 PASS was fabricated. No `BLOCKED_ARCHITECTURE_R4_AUTHORITY` condition triggered; no Evidence authority rewrite was needed.

## 2. r3 → r4 strict field diff (canonical JSON)

- Input: `execution/compat/selection-architecture-input-r3.json` (`af39220e…`) → `selection-architecture-input-r4.json` (`67d0f39f…`). Assignments: 32/32 byte-identical (19 SELECTED / 12 REJECT / 1 HOLD; PRIMARY 12 / SUPPORTING 7 / NONE 13). Architecture section only: `runner` invocation/date; `architecture_goals[5]`; `page_plan.notes`; P1 purpose + §1.2 + §1.5 + 3 boundaries; P2 purpose + §2.2 + §2.4 + 2 boundaries; P3 §3.2 + §3.4 + 1 boundary; P4 purpose + §4.2 + 1 boundary; P5 purpose + §5.1 + §5.2 + §5.3 + 2 boundaries; P6 purpose + §6.2; P7 §7.3; P8 §8.1 + §8.2 + §8.3 + editorial_note + 3 boundaries.
- Matrix: `16a6bbfe…` → `16a6bbfe…` (IDENTICAL). Selection: `50decd86…` → `50decd86…` (IDENTICAL). 19/19 placements identical; 8 package IDs identical; 31 must-covers preserved (5+6+4+3+4+3+3+3).
- Architecture: `529ce4b3…` → `9ab37dd6…` (text edits above only). Summary: `26817906…` → `c8bb6e2e…` (architecture-SHA binding only). Attention: `7c3e4deb…` → `7c3e4deb…` (IDENTICAL, 68/68). Audit: `4acb1a5e…` → `ff2267e2…` (input SHA NEW `67d0f39f…`, arch/summary SHAs NEW, matrix/selection/attention SHAs carried).

## 3. Source-to-claim bind (exact)

- DeepInfer separation → crosswalk §1 (README rendered 2026-10-25 + pinned `environ.py`/supplements) → P2 §2.2 + boundaries + MUST-NOT.
- Voxtral conflict → crosswalk §2 (three official URLs + passages, observed 2026-10-25) → P5 §5.1 + purpose + boundaries + UNRESOLVED note. No "9 = presets" invention.
- Nemotron 8B/4B + Flint 39.8B/2.5B conventions → crosswalk §3 → P1 §1.2 + boundaries.
- FLUX 277.80/10.95/12.45 arithmetic → crosswalk §4 → P4 §4.2 + boundaries; vendor 26.5x/96.2% cited as incompatible, not fact.
- Decisions $0.10/$0.01/write-billed/regional/long-context/400-per-request → crosswalk §5 → P8 §8.1 + boundaries.
- Temporal anchors → crosswalk §6 → P1 §1.5 / P3 §3.2/§3.4 / P8 §8.2/§8.3 + boundaries.
- 68 Attention → §4 below (unchanged); 19 risks → risk register (separate ledger).

## 4. Parsed authority (frozen native outputs)

- Selection parsed 32/32: SELECTED 19, REJECT 12, HOLD 1 (KohakuMoss `b26dfd2c…`). All 19 placed 19/19 across P1 (2+1), P2 (2+0), P3 (1+2), P4 (1+0), P5 (1+2), P6 (2+0), P7 (2+0), P8 (1+2). No HOLD/REJECT placed.
- Packages 8/8: P1..P8 IDs, titles (unchanged), purposes (P1/P2/P4/P5/P6 edited), drafting orders 1..8 unchanged, page allocations unchanged.
- Must-covers 31/31: all present, each edited item listed in §2; no silent skip among ISA-003…009.
- Residual 5 LIMITED (pre-existing Evidence limits, unchanged): AA originals unfetched; Oracle/AM-Bench v1→v2 deltas unchecked; author/vendor benches unreplicated; source/weight/license gaps; app-availability ambiguity. No new source contradiction forced `SELECTION_REVIEW_REQUIRED`.
- Attention 68/68: limit 100, shown 68, overflow 0, truncated false, unique item_ids verified in scratch rebuild. Counts unchanged from r3.

## 5. Nine negatives (scratch, all fail-closed as required)

(i) Simultaneous MTP=1 + deterministic sampling: architecture contains ONLY排他的構成例 + MUST-NOT bans (3 hits all prohibitions) — simultaneous claim absent → NEGATIVE PASS.
(ii) Unconditional TTS 35+: only `統一禁止` / `書かない` prohibitions + UNRESOLVED table — unconditional single-model claim absent → PASS.
(iii) 11-language sample = capability: only `対応数ではない` / `対応言語数ではない` distinctions → PASS.
(iv) `Nemotron 4B total` / `Flint 2.5B total`: zero standalone occurrences (naive cross-boundary grep false positive documented; actual strings are `8B total・4B effective` and `39.8B total/~2.5B active`) → PASS.
(v) Totally-free pricing: only `≠総無料` qualifications + write-billed/regional/multiplier notes → PASS.
(vi) `400 total`: only `per request[総呼出上限ではない]` / `400問はper request` → PASS.
(vii) Metrics selected / Kimi-available / 1Password-live: Metrics + Grok both REJECT/NONE; `POST_CUTOFF`/`非選択`/`NEVER_STORY`/`FUTURE`(9)/`coming soon`(4) present; zero live-now claims → PASS.
(viii) Vendor-only as independently measured: 6 hits all inside MUST-NOT bans or `(独立測定ではない)` / `独立計測22xと書かない` qualifications → PASS.
(ix) 68 attention as selected-19 coverage: zero conflating strings in Architecture; separate risk register used → PASS.
(+) P4 arithmetic: 277.80/10.95=25.3699→25.37, 277.80/12.45=22.3133→22.31, (277.80-12.45)/277.80×100=95.5184%→95.52% verified; reversed `10.95/277.80`/`12.45/277.80` absent from Architecture (the single `10.95/277.80` in the tree lives in the preserved Selection rationale for FLUX, byte-identical r3 for invariance — Architecture §4.2 is authoritative). Page budget 5.0+6.0+4.5+3.0+4.5+4.0+4.5+3.5=35.0 +2.0=37.0 unchanged.
Core validators are NOT claimed to check these semantics (frozen schema checks structure/placement/basis only); the nine are edition-local negatives.

## 6. True native test transcript (scratch @db78839bd, detached, no new branch)

1. `PYTHONPATH=$SCRATCH python3 scripts/run_selection_architecture_v2_interactive.py --repo-root $SCRATCH --state sources/2026-W43/production-state.json --input selection-architecture-input-r4.json` → exit 0, `{"selected_count": 19, "architecture_package_count": 8, "review_readiness": "READY_FOR_ARCHITECTURE_REVIEW"}`.
2. Matrix SHA `16a6bbfe…` IDENTICAL r3; Selection SHA `50decd86…` IDENTICAL r3; Architecture `9ab37dd6…` NEW; Summary `c8bb6e2e…` NEW; default Attention `1dc4ebe8…` (limit 50, superseded).
3. `survey_review_attention_v2.build_attention(..., limit=100)` → 68/68 unique, overflow 0, truncated false, SHA `7c3e4deb…` IDENTICAL r3; `validate_attention` PASS.
4. Audit reconciled by recomputing exact output SHAs (no fake provenance): audit SHA `ff2267e2…`.
5. `survey_stage_validation_v2 --artifact candidate-matrix=… --artifact candidate-selection=… --output /tmp/w43-r4-stage-precheck-selection.json` (EVIDENCE_REVIEWED→SELECTION_COMPLETE) → exit 0, `status PASS`, impl `db78839bd…`, State untouched. SELECTION_COMPLETE→ARCHITECTURE_ESTABLISHED NOT run (`NOT_RUN_CURRENT_STATE` — no forged State).
6. Frozen schema/instance validators + `validate_selection` + `validate_architecture(require_approved=False)` + review-summary READY + attention validate: all PASS inside the runner (exit 0). No Stage write, no Human write.

## 7. Hash check (scratch-tested bytes reflected to branch)

New r4 machine outputs: Matrix `16a6bbfe…` (=r3), Selection `50decd86…` (=r3), Architecture `9ab37dd600d76056306f5a8419f6dbb42bf59866e559bede4f85fe49a958055a`, Summary `c8bb6e2ec9df59bebf1aafab5995e549970ee7660c8e2bd69f95a26f52d87172`, Attention `7c3e4deb…` (=r3), Input-r4 `67d0f39f…`, Audit-r4 `ff2267e2…`.
r3 history snapshots: 7 SHAs in `execution/history/selection-architecture-r3/SHA256SUMS` (matrix/selection/arch/summary/attention/input/audit + README), byte-for-byte cmp verified.
