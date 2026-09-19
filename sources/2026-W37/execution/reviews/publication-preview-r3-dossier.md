# Human Publication Preview dossier — 2026-W37 r3 (PENDING)

Status: `RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PENDING_HUMAN_DECISION`
Date: `2026-09-19`
Revision: `r3` (Human r1/r2 REQUEST_CHANGES preserved; r3 awaits independent Sol review and Human judgment)

This dossier was assembled by the worker from frozen approved authority and narrowly repaired Draft r3. It is not an independent Sol review and not a Human decision.

## 1. Exact review identity

- Edition `2026-W37` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`.
- Reviewed commit `8dfb83499f839907d180d9a06bd155cc12fb27d6` (State + Candidate + Candidate-bound PDF).
- Lifecycle `RELEASE_CANDIDATE`, terminal `HUMAN_GATE_REACHED`, next `PUBLICATION_PREVIEW`.
- Candidate `sources/2026-W37/publication/v2/publication-candidate-v2.json` (candidate SHA `e7f18eb2584c2c4575e15bd2be59abc5e8c9a687b238285343139c81332e53f1`, file SHA `62d4d42bf9b293ded34e2124bb4d7bcfef8ff577456fba35cd827682f10c3dab`).
- PDF `surveys/weekly/2026-W37/main.pdf` (11 pages, 309033 bytes, SHA `9e957ca2d48dd95091e0013c0f2d23f1570ad9fac89b131365259f1c8e948e56`, CI run `35375978076`, artifact `10559799086`).
- Manuscript `sources/2026-W37/publication/v2/reader-manuscript-v2.json` (manifest SHA `bde308b051872808b6db995a8c792f8c4fde9ebacd6fc0e3ab68033f8937d1eb`, file SHA `9206c4cfe627366292e013aef9ad6d2d01df4205163eeb05bcd8d40685516730`).
- Human Preview r1 `REQUEST_CHANGES` (rev 1, reviewed `8057a468`, boundary `ARCHITECTURE_ESTABLISHED`) and r2 `REQUEST_CHANGES` (rev 2, reviewed `74400d71`, boundary `ARCHITECTURE_ESTABLISHED`) both preserved.
- Architecture approval: Human r1 `APPROVED` preserved (reviewed `55e700a3`, Architecture SHA `81e87a64`).

## 2. Human Preview r2 REQUEST_CHANGES record

- Path: `sources/2026-W37/gates/reviews/publication-r2.json`, revision `2`, decision `REQUEST_CHANGES`.
- Reviewed production commit: `74400d716e703c12efee97707ff0ee97d47f98a8`.
- Boundary: `ARCHITECTURE_ESTABLISHED` (no Architecture reopen; verified `_reopens_architecture == False` preflight).
- reviewed_at: `2026-09-19T02:37:47+09:00` — actual timezone-aware wall-clock at recording time (UTC `2026-09-18T17:37:47Z`), not a synthetic round time.
- reviewed_by: `Human Owner`; references bind replacement request + r2 shell + Sol r2 review.

## 3. Architecture approval preservation

- `gates/architecture-approval.json` (SHA `1a9d27454cfd5a8dd4840be3ef7ccd59ca389145e4970281f47cc24c1f4d33d9`), snapshot and `architecture-v2.json` untouched.
- Post-revision State: lifecycle `ARCHITECTURE_ESTABLISHED`, Arch approved with byte-valid provenance, Preview pending, Draft+ pending.
- Frozen upstream unchanged: Discovery 14, Screening 13/1, Evidence 11/2, Materiality 12/1/1, Selection 12/1, Architecture 7 packages.

## 4. Draft r3 identity

- Regenerated from approved Architecture + frozen Evidence (`draft-stage-validation-r3.json` PASS → `DRAFT_COMPLETE`).
- Semantically conservative: r2→r3 diffs limited to #434 scope-language repair plus strictly necessary flow adjustments; package structure, claims, boundaries unchanged.
- r2 PDF/candidate/review SHAs not reused.

## 5. #434 before/after

- DeepSeek body: 「ベンチマーク表や図の詳細は取得の打ち切りでたどり切れておらず」→「本号ではベンチマーク表・図の詳細な検証までは行っておらず」; 「トークン単価表の値は画像に埋もれて取り切れていない」→「トークン単価表の詳細は本号の検証範囲外」; claim-boundary box likewise.
- Sources & Limitations: 「全文PDFやIOC、ベンチマーク手法の詳細、図表の値は参照の打ち切りで取り切れていない」→「本号では全文PDFやIOC、ベンチマーク手法・図表の詳細までは扱わず、その範囲を超える主張は行わない」.
- Sweep equivalents repaired in the same scope language: p1-bench/p2-eval/p3-fusion/p6-north/p7-cases 「今回たどっておらず」→検証範囲外の表現; 「取得時点」→「本号で確認した範囲」.

## 6. Process-narration sweep result

- Searched all 7 Draft r3 Results, synthesis, frontmatter, Week in Review, Sources & Limitations, TeX for: 打ち切り/取り切れ/途中で取得停止/時間都合/ツール制約/予算制約/retrieval mechanics/source-consumption narration. Result: zero remaining reader-facing occurrences (machine-checked + semantic reread).
- Genuine limitations preserved as verification scope (what was verified / not verified / edition coverage / source uncertainty / reproduction status).

## 7. #501 regression check

- Established terms intact (モデル/コード/コーディング/トークン/エージェント/エージェントハーネス/サンドボックス/サービング/エンジン/ライセンス/モデルカード/翻訳/MoE/評価用モデル/IOC). Technical-use 模型/符号/代理人/砂場/給仕/引擎/許し/札/訳し/混合専門家/検出子 reintroduction: zero (machine-checked + reread).

## 8. #506 reviewer provenance

- All new Worker artifacts (`language QA` boundary QA, reader-surface semantic, semantic/editorial, visual, session) use `Worker/Agent (Muse Spark)` exclusively. No `ChatGPT`/`Sol`/`Human`/`independent reviewer` self-identification.

## 9. #507 timestamp validation

- Human r2 record `reviewed_at`: actual wall-clock `2026-09-19T02:37:47+09:00` (UTC 17:37:47Z), timezone-aware, non-round, verified ≤ its commit time at read-back.
- Worker QA/reviews/manuscript/bundle built with actual UTC `2026-09-18T17:47:29Z` (build script `datetime.now(timezone.utc)`), verified ≤ their commit time at read-back.
- Pre-existing future-dated history/checkpoint values (e.g. `00:27Z`–`00:32Z` series from earlier runs, already covered by `execution/provenance/w37-execution-time-correction-20260919.md`) were not rewritten. Machine-transition `recorded_at` values remain Core-monotonic by necessity and are disclosed here rather than presented as wall-clock: draft advance `00:30Z`, reader-publication advance `00:31Z`, candidate advance `00:32Z` (all 2026-09-19). Historical records untouched per correction-ledger policy.

## 10. TeX/Bib identity

- `surveys/weekly/2026-W37/main.tex` + 10 sections + `references.bib` (19 records) + `jgaisurvey.sty`; lexical gate PASSED on all 12 files.

## 11. Citation/X audit

- 19/19 cited keys resolve, missing 0, unused 0. 8 direct X status URLs retained (ordinary-window, Sol-verified). X community/context only. No blob/internal-path citations.

## 12. Vendor/temporal boundary audit

- All r2 boundaries preserved (OpenAI separation; DeepSeek vendor-attributed + Sep 14 future; Fusion 17:00Z + 39% maximum; open-weights card bounds + North license/judge; threat vendor investigations + full PDF/IOC out of scope + Sep 11 detail excluded; resignation non-bearing; GLM excluded). Ordinary/pre-window/late-breaking/future-operation discipline intact.

## 13. Semantic/editorial + visual (Worker provenance)

- Semantic/editorial `277fe4be` PASSED 11 checks, reviewer `Worker/Agent (Muse Spark)`.
- Visual `1ccede46` PASSED 2 checks (11 pages), reviewer `Worker/Agent (Muse Spark)`.
- Reader-surface gate `d250d98c` PASSED (0 findings, 0 suppressions) on Worker/Agent semantic authority.

## 14. Deviation from approved Architecture

None.

## 15. Review provenance downstream

- Worker created all r3 artifacts with truthful provenance; no Sol/Human authorship claimed. Fresh Preview r3 awaits independent Sol review and Human judgment. No r3 decision recorded.
