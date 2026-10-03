# TS-003 Technical-Depth Restoration r11 — Execution Report

- Date: 2026-10-03 JST
- Authority: `EXECUTION_AUTHORITY / READER_JSON_TECHNICAL_DEPTH_RESTORATION / STOP_BEFORE_TEX`
- Branch (existing only): `special/vision-multimodal-2026-work`
- Terminal: `TS-003 TECHNICAL_DEPTH_RESTORATION_R11_COMPLETE / READER_JSON_ONLY / FRESH_SOL_REVIEW_REQUIRED`

## 1. Starting HEAD/tree verification (read-only, pre-write)

- Expected HEAD: `42791bfa9e3fc00b81aec717c631734be023c884`
- Actual remote HEAD (`origin/special/vision-multimodal-2026-work`): `42791bfa9e3fc00b81aec717c631734be023c884` — MATCH
- Expected tree: `2e13c36f89d82164177fc49f47217f526b735e76`
- Actual remote tree: `2e13c36f89d82164177fc49f47217f526b735e76` — MATCH
- Local HEAD/tree identical, clean tree. Work authorized; no new branch created.

## 2. Files read (required inputs §4)

1. `architecture-v2.json` — all 16 packages: purpose, must_cover, boundaries, depth classes (FULL 33 / TRANSITION 53 / BRIEF 38 nodes, 124 total).
2. `publication/editorial/reader-editorial-authority-r10.json` — all 102 blocks incl. 16 `*-boundaries` CLAIM_BOUNDARY blocks (54,189 reader chars).
3. `execution/drafting-terminology-map-ja.md` — full read, binding incl. Avoid registry.
4. `execution/drafting-language-policy-ja.md` — full read.
5. `draft/v2/packages/*/draft-result.json` (P01–P15, all blocks + must_cover_coverage + boundary_dispositions) and `draft-package.json` (node mapping).
6. Evidence results `evidence/v2/accepted/*/results/*.json` — all evidence_task_ids referenced by P01–P15 draft-result/r10 resolved; claims/limitations/subjects verified per ref (111 indexed results; every cited `(task, claim-N, subject)` triple machine-verified, zero mismatches).
7. Sol Draft Reviews r1–r9 + Sol reader-publication reviews; r1/r2 principles re-confirmed (budget≠quota, repetition/padding banned, depth gaps filled with technical content, no paraphrase lengthening).

## 3. Character counts (observed only, not success metrics)

- r10 total reader chars: 54,189 (102 blocks)
- r11 total reader chars: 72,337 (146 blocks: 102 byte-identical + 44 new)
- Net technical-depth addition: +18,148 chars. No character-count target was used.

| Pkg | r10 blocks/chars | r11 blocks/chars | delta |
|-----|-----------------|-----------------|-------|
| P01 (cap) | 4 / 2,199 | 4 / 2,199 | +0 |
| P02 | 6 / 3,253 | 9 / 4,777 | +1,524 |
| P03 | 5 / 2,324 | 7 / 3,230 | +906 |
| P04 (cap) | 5 / 2,200 | 5 / 2,200 | +0 |
| P05 | 7 / 3,944 | 11 / 5,425 | +1,481 |
| P06 | 6 / 2,901 | 8 / 3,781 | +880 |
| P07A | 4 / 2,058 | 6 / 2,926 | +868 |
| P07B | 10 / 6,213 | 16 / 8,880 | +2,667 |
| P08 | 6 / 3,009 | 9 / 4,117 | +1,108 |
| P09 | 8 / 5,122 | 12 / 7,006 | +1,884 |
| P10 | 4 / 1,858 | 7 / 3,073 | +1,215 |
| P11 | 6 / 2,742 | 8 / 3,334 | +592 |
| P12 | 5 / 2,979 | 7 / 3,751 | +772 |
| P13 | 8 / 3,951 | 11 / 5,200 | +1,249 |
| P14 | 7 / 3,426 | 10 / 4,345 | +919 |
| P15 | 11 / 6,010 | 16 / 8,093 | +2,083 |

## 4. Coverage counts (technical-depth-coverage-r11.json, 124/124 Architecture nodes bound)

- FULL (33): ADEQUATE 20 / PARTIAL 13 / DEPTH_EVIDENCE_GAP 0
- TRANSITION (53): ADEQUATE 46 / PARTIAL 7 / DEPTH_EVIDENCE_GAP 0
- BRIEF (38): ADEQUATE 37 / PARTIAL 1 (VM-D111 VSI-Bench, honest partial depth retained) / DEPTH_EVIDENCE_GAP 0
- Package-level DEPTH_EVIDENCE_GAP records (3): X01 supervision timeline (no P15 evidence; p15-b13 marked editorial inference); P15 screen-operation/HallusionBench contracts (no P15 evidence_task_id; method-principle scope kept, no numeric insertion); P09 tiling/resampling/KV/latency/fusion-distinction/multi-image internals (no P09 primary source; gaps stated explicitly in p09-b9/b10/b12 prose).
- FULL PARTIAL nodes (13): VM-D006 (training breakdown), D011 (denoising internals/DN-DETR delta), D012 (RepVL-PAN reparametrization), D051 (OWLv2 efficiency breakdown), D065/D066/D070/D071 (tiling/reduction/KV/latency/fusion distinction), D089 (training/memory internals), D095 (continuous-value serialization), D097 (action discretization), D103 (target positional conditioning), D105 (latent-action extraction).
- Dropped candidate: P11 p11-b9 (Flash-VStream) — 9/11 sentences duplicated r10 p11-b4 with zero novel propositions; not adopted. D089 stays PARTIAL on r10 p11-b4 + explicit gaps.

## 5. Repetition QA (§17)

- Initial draft: 62 exact-duplicate sentences inside new blocks vs r10. Dispositioned all 62: 36 deleted, 14 bridge/score-trim replacements, 1 block dropped (p11-b9), 2 blocks fully rewritten (p13-b11 two-stage dependence + G01; p14-b9 generative-environment record binding), 9 residual singletons re-verified as novel.
- Final: **0 exact-duplicate sentences** in new blocks vs r10 (machine-verified).
- Score-recital audit: per-number overlap computed new-vs-r10 per package. Trimmed pure recitals (p07b-b12 secondary deltas, p07b-b13 COCO/LVIS headline set → 1-shot-scope framing, p07b-b15 relative-43%, p07b-b16 OpenSeg/ODISE specifics, p02-b8 R50 42 AP, p08-b9 92.53% → scope separation). Retained single condition-bound anchors where they materialize a NEW proposition (comparative frames in p02-b7/p06-b7/p07b-b14/p10-b7/p15-b13, instrument spec in p12-b6, closed-loop illustration 85.1% in p08-b9). Rationale recorded per block above.
- Near-identical conclusion chains varied: P07B ×6 `へ接続する` closings rewritten distinctly; P09 vendor-measurement closings ×4 varied; p15-b12 vs p05-b11 numeric-comparison closings varied.

## 6. Terminology QA (§18)

- Full Avoid-registry scan over r11 bytes + contextual classification of every hit.
- PASS: 測り hits are all 測り方/測り手/continuative (no bare-metric use); 分割 hits are all train/test/rare splits (no segmentation substitution); 教師 hits are 教師信号/教師あり/教師モデル/自己教師あり or descriptive genitives (教師の役割/出所/意味 — literal, retained); 生徒 hits are 生徒モデル (prescribed form, mirrors r10 p07b-b2); 枠 hits are 枠組み/クエリ枠 (retained per #559 validation); 土台/水増し singletons are r10-carried literal uses (p15-b1/p15-b2, Sol-accepted lineage, retained + noted).
- NEW_TERMINOLOGY_RISK found and repaired in-draft: p05-b8 `再構成の変種` (map bans model/configuration-sense 変種) → `再構成のバリアント`, rebuilt. No other new Avoid forms. Zero 教員/幻覚/投票型/基線/日程 in r11.
- New-prose regression scan: no reintroduction of 網/処方/模型/足場/分割-as-segmentation/測り-as-metric/冷間始動/背骨/二塔/混合専門家/特徴量地図/範疇/遅い・固い融合.

## 7. Issue #559 regression QA

- All 9 forbidden strings absent; all 16 required repaired strings present; all 5 retain-枠 senses present; 基線/日程 absent. **PASS.**
- Guard meanings preserved in novel phrasing inside new blocks too (80ms granularity, dynamic video IDs, Apache 2.0 3-release scope, DETR 300/500 split with 学習設定/学習期間, POPE polling identity, ベースライン, フレーム).

## 8. Architecture QA (§17)

- All 16 packages keep approved purpose/must-cover/boundaries; must_cover_coverage extended by append-only r11 entries (pre-existing entries byte-identical); boundary_dispositions extended likewise.
- P01/P04 caps intact (0 new blocks). P07A/P07B metric split enforced (no cross-citation in new blocks). P12/P13/P14 bounded endpoints hold (p12-b7 explicit non-expansion closure; no kinematics/hardware; Ha→Genie non-ancestry re-confirmed in p14-b9). P15 methodology-first (condition binding + open verdict organization; no cross-family ranking; NO_CROSS_MODEL_NUMERIC_COMPARISON kept in P05).
- FULL substance spot-check: every ADEQUATE FULL node binds mechanism + predecessor delta + evidence + limitation (where sourced) in reader prose; no score-only treatment (deepest score reuse is single-anchored and condition-bound).

## 9. Changed / untouched files

Changed (new files only, all under `sources/SP-vision-multimodal-2026/publication/editorial/`):

- `reader-editorial-authority-r11.json` (SHA-256 `4107326d73d34468e63eba9d91564243ca798e194e40d834e81a4b99c03ab3bd`)
- `technical-depth-coverage-r11.json` (SHA-256 `10ed19902b7ee6bb9e28fc391a5bf6f95bd7c029c045081232c3a80e64ac58d2`)
- `build_reader_editorial_authority_r11.py` (reproducible generator: r10 bytes + new-block files only; asserts 102 pre-existing blocks byte-identical/order-preserved/decks-untouched)
- `build_technical_depth_coverage_r11.py` (coverage assembler; asserts 124/124 Architecture nodes bound, block existence, ref derivation from r11 bytes)
- `r11-new-blocks-g1.json` (P09×4 + P07B×6), `r11-new-blocks-g2.json` (P15×5 + P05×4 + P08×3), `r11-new-blocks-g3.json` (P02/P11/P13/P14/P03/P06/P07A/P10/P12; 25 admitted of 26 drafted, p11-b9 dropped with reason)
- `r11-coverage-data-a.json` / `r11-coverage-data-b.json` (hand-audited per-node dispositions)

Untouched (protected, §19): `main.tex`, `main.pdf`, `references.bib`, candidate manifests, preflight, visual review, `production-state.json`, historical checkpoints, Architecture approval/Architecture/Selection/Materiality, canonical Draft r1, r10 authority, Shared Core. Issue #559 left open (not closed). No lifecycle advancement records created.

## 10. Method notes for Sol review

- Drafting was assisted by 6 scoped research/drafting runs (package groups), each instructed to reuse only package-local evidence_task_ids verbatim. Every cited `(task, claim-N, subject)` triple was machine-verified against Evidence result bytes (zero mismatches); claim/subject inventory is reproducible via the evidence index.
- Repetition repair (dedup + rewrites + score trims + closing variation) was applied after drafting; one-shot repair logic is described in §5 above (script kept outside the repo; effects baked into the committed data files + builders).
- r11 status is `TECHNICAL_DEPTH_RESTORATION_CANDIDATE / SOL_REVIEW_REQUIRED` — never Sol-accepted/approved/canonical. All new claims are either Evidence-bound or explicitly marked `[EDITORIAL-INFERENCE grounded in: ...]` (p15-b13, p15-b16). No new Evidence admission, no Broad Discovery, no Selection/Architecture change.
- Known residual risks for Sol: (a) P06 p06-b8 `Qwen系での再利用` attribution stays report-level with G06-style non-binding note; (b) P13 p13-b9 `掛け合わせ` is descriptive (probability product), not a listed Avoid form, kept; (c) frequent `〜の話` phrasing is stylistic, not a registry hit; (d) P15 p15-b5/p15-b9 keep EMPTY evidence_refs under the verbatim-ref rule — coverage audit records the binding limitation instead of misbinding refs.
