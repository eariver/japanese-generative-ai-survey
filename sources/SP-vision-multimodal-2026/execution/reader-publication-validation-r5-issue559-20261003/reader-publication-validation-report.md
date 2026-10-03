# TS-003 Issue #559 bounded reader repair — r10 validation report (r5)

Status: `RELEASE_CANDIDATE / ISSUE_559_R10_REBUILT / FRESH_SOL_REVIEW_REQUIRED`

Date: `2026-10-03 JST`

Issue: `#559 [Publication][TS-003] Publication Preview REQUEST_CHANGES — Qwen3-Omni source fidelity + terminology repair`

Branch: `special/vision-multimodal-2026-work` (existing only, no force)

## 1. Starting guard

- remote HEAD `998eb7db0fab18216841712a93e2456704a45f69` / tree `518c5954699365bf71309d505d8df4eadb9a477c` verified read-only before writes
- lifecycle `RELEASE_CANDIDATE`, `PUBLICATION_PREVIEW pending`, terminal `HUMAN_GATE_REACHED`
- canonical r1 + editorial r9 authority model preserved; r9 not reinterpreted as canonical

## 2. Authority revision

- `publication/editorial/reader-editorial-authority-r9.json` intact (SHA `7ab5751f…`)
- new `reader-editorial-authority-r10.json` SHA `14296fe82619ab158494820e74152a4e6688a119b8017ac1801f48434163b1b4`
- builders: `build_reader_editorial_authority_r10.py` (r9 + 20 explicit patches), `validate_reader_editorial_authority_r10.py` PASS
- traceability: 14 blocks + 2 decks changed, Evidence refs/order unchanged, canonical r1 provenance intact
- r10 is publication-layer only, never canonical Draft authority

## 3. Disposition A–F (primary sources read back)

- A. Qwen3-Omni 80ms (P09 p09-b5/b6): report §2.3 `https://arxiv.org/html/2509.17765` — audio frame ~80ms, temporal-ID 80ms step, video IDs dynamic from timestamps, common 80ms resolution anchored to absolute time; no `sync error <=80ms` in source. Repaired to temporal-ID granularity; `80msの時刻合わせ` -> `約80msの時間ID分解能での時刻合わせ`.
- B. Licensing (P09 p09-b6): repo `LICENSE https://github.com/QwenLM/Qwen3-Omni/blob/main/LICENSE` Apache 2.0 + report names `Qwen3-Omni-30B-A3B / Thinking / Captioner` Apache 2.0. Removed categorical `重みとコードの許諾は未確定`; states verified repo/code + named releases scope, residual beyond primary sources left specific.
- C. Video frame 枠 (P11 p11-b3/b4/b5 decks+bodies, P15 p15-b4): LongVideoBench `https://arxiv.org/html/2407.15754` 16→256 input frames. Normalized to `入力フレーム/入力フレーム数`; retained `枠` for framework/box/query-slot/coordinate senses (`枠組み`, `クエリ枠`, `共通の枠`, etc.) with reason. P09 p09-b2 `重みの許諾は未確定` retained as out-of-scope Qwen3-VL/InternVL3 context (not Qwen3-Omni).
- D. POPE (P10 p10-b2/b3/boundaries decks, P15 p15-b3/boundaries): `https://arxiv.org/abs/2305.10355` — `Polling-based Object Probing Evaluation`, polling/query object-existence probing, `more stable and flexible`. Repaired to `POPE (Polling-based Object Probing Evaluation)による問いかけ型…`, `安定かつ柔軟`, no voting; boundaries consequentially repaired.
- E. ML baseline 基線 (P07B p07b-b2/b5): `ゼロショット基線/教師あり基線` -> `ゼロショットベースライン/教師ありベースライン`; no geometric baseline occurrences.
- F. DETR (P02 p02-b4): accepted VM-D010 `https://arxiv.org/abs/2005.12872` §4 — 300-epoch baseline (AdamW, 16×V100 ~3d, batch 64) vs 500-epoch Faster R-CNN comparison (+1.5 AP). Separated to `300エポックの学習設定（…約3日の学習期間）と…500エポックの長期設定`; `日程` removed; DETR otherwise untouched.

No new material defect requiring new Evidence/Architecture found; no broadening.

## 4. Terminology QA (seed contextual, not auto-replace)

Seed: `docs/editorial/ja-technical-terminology-overtranslation-seed.md`
- `枠`: REPLACE 6 frame senses (P11×3 + deck, P15 + deck); RETAIN framework/box/query/coordinate (`枠組み`, `クエリ枠`, `共通の枠`, `理解の枠`, synthesis `枠組み`) with surrounding-meaning reasons
- `基線`: REPLACE 2 ML senses; 0 remain
- `日程`: scheduler sense removed (DETR); 0 remain in TeX
- `投票型/投票型評価/しなやか`: removed; `投票` remains only in P10 deck? No — deck repaired; remaining `投票` is 0 in TeX except? Verified 0 `投票型`, 0 `しなやか`; boundary voting repaired
- Adjacent identity loss: none introduced (POPE canonical preserved, baseline identity preserved, frame identity preserved)

## 5. Revalidation (same-stage, lifecycle honest)

Lifecycle remains `RELEASE_CANDIDATE`, `PUBLICATION_PREVIEW pending`, `HUMAN_GATE_REACHED`; `production-state.json` and historical checkpoints untouched; no rollback, no fake transition.

- manuscript PASS (binds new TeX `bc0799c4…`)
- deterministic 4/4 PASS; preflight PASS 0 blocking/0 layout, 39pp
- identifier `111/111` (0 undef/uncited); subject/empty PASS
- bundle PASS; semantic PASS (4); editorial PASS (9, r10 wording); visual PASS (5, 39pp); gate PASS
- reader authority r10 validator PASS (Evidence bounded, 14+2 diff confined, retain decisions hold)
- candidate rebuilt via canonical `build_candidate`: `publication-candidate-v2.json` file SHA `447d229ca87b61036b932074c32d337b0a2becf728ff64e215633f732c1b1da0`, `candidate_sha256 175b75c35944b111c3da1dcd93bc634ab7a68ccfda6bac47b3654482501f1cda`, `READY_FOR_PUBLICATION_PREVIEW`

## 6. PDF regression (r4 38pp -> r10 39pp)

- r4 baseline `/tmp` SHA `78f4cc8c…` 684804B 38pp; r10 `surveys/special/vision-multimodal-2026/main.pdf` SHA `d7423583d0f9cba0413ae8a02ed92bb073fb52c0a414fcf8fd13450362cf4e38` 687179B 39pp, LuaLaTeX+Biber canonical
- TeX non-comment diff: 32 lines = 14 blocks + 2 decks repairs (Issue #559 only) + 17 r9→r10 provenance comments; bib entries identical (header only)
- extracted text differs only at repair sites + page-number/reflow shifts; citations unchanged 111/111
- pagination 38→39 due to longer Qwen3-Omni/POPE/DETR wording; TOC updated; all 39 pages rendered (150dpi/120dpi PNG success); preflight 0 overfull/underfull; no missing/overflow/overlap/broken-table/reference findings
- reader-visible differences confined to Issue #559 repairs + unavoidable reflow

## 7. Changed files

- `publication/editorial/reader-editorial-authority-r10.json` + 2 scripts (new)
- `execution/reader-publication-validation-r5-issue559-20261003/` (new: 4 adapted builders + this report)
- `surveys/.../main.tex`, `references.bib` (header), `main.pdf` (39pp)
- `publication/v2/`: manuscript, deterministic preflight, bundle, semantic, editorial, visual, gate, candidate (other deterministic byte-identical)
- No State/checkpoint/Architecture/Evidence/Selection/Draft-r1/Shared-Core/main change

Terminal: `RELEASE_CANDIDATE` / `PUBLICATION_PREVIEW pending` / `ISSUE_559_BOUNDED_REPAIR_COMPLETE` / `FRESH_SOL_REVIEW_REQUIRED` / `NO_HUMAN_PUBLICATION_PREVIEW_APPROVAL` / `NO_FREEZE` / `NO_RELEASE`
