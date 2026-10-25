# J-GAS W43 — Human Architecture Review r1 presentation (NO HUMAN DECISION)

Status: `READY_FOR_HUMAN_ARCHITECTURE_REVIEW / OWNER_DECISION_PENDING / NOT_APPROVED`
Date: 2026-10-25 JST
Repository: `eariver/japanese-generative-ai-survey`.
Existing branch: `weekly/2026-W43-v2-work`.
Canonical r6 Trusted Architecture established commit: `60a8c11c583954a88000bcbb4def53a637a9aeef`, Root Tree `fd5ddd41c777fc5456f247da79e11ab991b72ba3`.
Human review must bind exact unchanged Production State/Architecture/Summary/Attention bytes at a reachable branch commit, not a floating “latest” or an unrelated memo.
Frozen Core v2 unchanged: `production/survey-core-v2` commit `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
Reviewed main commit `041a08dfef3112643cbf85b4a86a7b6f9128aed6`, Tree `a134dc36a407d08ab1de416324229b3955e0325a`.

## Formal machine review basis

- Current `production-state.json`: `ARCHITECTURE_ESTABLISHED`, terminal `HUMAN_GATE_REACHED`; machine Selection and Architecture checkpoints PASSED, Human Architecture Review and Publication Preview both PENDING/null provenance; no Draft/TeX/PDF.
- Selection r6 separate Trusted Operator: request `sol-w43-selection-r6-readvance-20261025`, immutable request commit `0005db67e7ce0994f51ddc49a06ac4c264af2777`, generated commit `ab021b4a54a7f21f55fe9d1d2421aa8c8b6da018`, Actions `https://github.com/eariver/japanese-generative-ai-survey/actions/runs/40188308379`: preflight & execution SUCCESS, receipt PASS, contract PASS `EVIDENCE_REVIEWED→SELECTION_COMPLETE`, checkpoint passed, exact Matrix `16a6bbfe569b3215d05fbae7175b3ca04efc6c1846d28c48662245b68f854c3b`, Selection `50decd8697e1737d7adf6fe9f1ac0f4c7cc891353a7be09461b86e8b90beccea`.
- Architecture r6 separate Trusted Operator: request `sol-w43-architecture-r6-readvance-20261025`, immutable request commit `aaaf45b1315aafee2d89afb241d37b2a257dfd45`, generated commit `60a8c11c583954a88000bcbb4def53a637a9aeef`, Actions `https://github.com/eariver/japanese-generative-ai-survey/actions/runs/40188538511`: preflight & execution SUCCESS, receipt PASS, contract PASS `SELECTION_COMPLETE→ARCHITECTURE_ESTABLISHED`, checkpoint passed. Architecture `7d8f0ea5c8600acab5f19c36ed578011fe2af861ea3a445324fc2f081928c302`, Summary `38c17eccff14e96e16596fc928152d18e67810572cd5e1cd466407def9100b74`, Attention `7c3e4deb4a2cd077acac148c777aa2300f1f4dad45bbc4d0624a6b693528f12b`. Core receipt read back, not merely Muse self-report.
- Independent Sol full Architecture r5 post-Stage audit original Google Drive `https://drive.google.com/file/d/1mYjruB6L4gHdkEFh001VGXPOqwnFNgCW/view` Selection PASS_WITH_LIMITATIONS, Architecture REQUEST_CHANGES only P2 R5-N01/02/03, no newly found P0/P1 within scope; r6 correction and editorial Sol targeted readback: `sources/2026-W43/execution/reviews/sol-w43-architecture-r6-postfix-editorial-readback-20261025.md`. **No new comprehensive r6 independent audit has been run**, by bounded repair workflow; no implied full reproduction.

## Editorial thesis

W43は「フロンティア級の能力の到達と配備現実の交差点」。将来公開予定の重み/API先行と既に動く重みの比較、推論・記憶基盤、エージェント権限境界、音声・動画の評価、脆弱性開示と安全、科学評価、API/SDK配布を一冊の技術誌として構成する。話題一覧ではなく、機構・評価の計測条件・可用性・ライセンス・一次資料の不一致を中心にする。Vendor measurement and release announcement are NOT independent reproduction.

## Fixed selection, packages and page estimate

Matrix 32 unique Candidates; Selection `19 SELECTED / 1 HOLD / 12 REJECT`; 19 selected exactly once among eight packages. Matrix, Selection and all 68 Attention records are byte-content identical to archived r5. Must-cover sections 31 = 5+6+4+3+4+3+3+3; 68/68 native exception-review Attention (not selected-19 risk validation); separate 19-selected risk ledger.
 
| Package | Planned subject and included candidates (PRIMARY / SUPPORTING) | Must cover | Estimated pages |
|---|---|---:|---:|
| P1 | 公開予定の重みと現行モデル — Moonshot Kimi K3.1 Pro、Recursive Flint / NVIDIA Nemotron 3.5 Bolt E4B | 5 | 5.0 |
| P2 | 推論・記憶機構 — DeepSeek DeepInfer、MemTensor MemT-1.0 / なし | 6 | 6.0 |
| P3 | エージェントの権限境界 — Anthropic Claude Duet / 1Password for Agents、Anthropic auto-mode default | 4 | 4.5 |
| P4 | FLUX 3 Max速度と計数の批判 — fal FLUX 3 Max / なし | 3 | 3.0 |
| P5 | 音声TTS/STT/Realtime — Mistral Voxtral 3 / InclusionAI Ming-3.0-tts、ElevenLabs Eleven Realtime v1 | 4 | 4.5 |
| P6 | 協調開示と訓練隔離 — OpenAI Patch the Planet、OpenAI frontier training containment and red-teaming / なし | 3 | 4.0 |
| P7 | 生物・低資源言語の評価 — OpenAI distributed biological reasoning、OpenAI low-resource language coding evaluations / なし | 3 | 4.5 |
| P8 | 判断API、開発ツール、配布 — OpenAI Decisions API / TanStack AI 1.0、DeepSeek V4.1-Flash-1017 | 3 | 3.5 |
| **Total** | 12 PRIMARY + 7 SUPPORTING = 19 unique selected | **31** | **35.0** |

Front matter, methods, references and index another estimated 2.0pp ⇒ **37.0pp expected**, **38pp editorial target**, **44pp cap**. Estimates only; no unjustified filler. Allow changes to actual PDF pagination during drafting, still require adequate technical depth, especially P2/P5/P7/P8.

## Three independently identified P2 repair closures

- R5-N01 P4 §4.2: multiplier `T_baseline/T_candidate` 277.80/10.95≈25.37× (Oct19 fal PR) and 277.80/12.45≈22.31× (fal blog/product), separately reduction fraction `(T_baseline−T_candidate)/T_baseline×100≈95.52%` on old baseline 277.80s, not candidate 12.45s; vendor source tensions kept, no independent performance experiment.
- R5-N02 P8 §8.2: GitHub Release `published_at=2026-10-22T15:18:14Z`, npm registry `time["1.0.0"]=2026-10-22T15:21:49.491Z`. Qualified exact API keys and observed time; blog Oct23 day-only, not a product clock.
- R5-N03 P6 §6.1: `CVE ゼロ` removed; current statement is “当該発行者ページの確認範囲でCVE識別子を特定できず、CVE付与の有無は未検証”, not “no CVE exists”.

## Standing unresolved and partial evidence — MUST carry into drafting

1. Evidence acceptance currently includes 32 PARTIAL cards and Completeness LIMITED; residual limitations 5, including nine date-only midnight placeholders not true clocks, selected candidate/source contradictions, postcutoff Metrics W44 OUT. Do not promote OUT/FUTURE to W43 news.
2. Kimi weight release Nov 4 FUTURE; open weights ≠ OSI-open-source; Flint vs Nemotron total/active/effective parameter conventions differ, weights license and base license are not interchangeable; original weight blobs unverified.
3. DeepInfer DSpark variable MTP and deterministic sampling are mutually exclusive configuration recipes, no fake joint benchmark; MemT 65-page paper equations/ablations not exhaustively independently reproduced, published 1.86×/66× are author-reported differing denominators.
4. FLUX speed first-party fal PR (10.95 seconds) vs blog/product (12.45), arithmetic contradiction with 26.5x/96.2%; Elo blog +47 vs product/PR +50 with original Artificial Analysis historical snapshot unavailable; keyframes availability PR/FAQ UNRESOLVED, no dated API live/GA proof. Source-page rendered only for some claims.
5. Voxtral language support, evaluation population, 18 vs 22 preset and model card 9 vs 35+ vendor claims UNRESOLVED, never collapse into one "supported-language" count.
6. Agent features coming soon versus live catalog, auth boundaries and safety claims vendor-only; Decisions API 400 questions PER REQUEST, cache writes charged; no statement that all billing is free; TanStack stable core vs experimental harness.
7. OpenAI Patch page rendered-only; CVE numbering neither directly verified nor disproved. Bio blinded preferences lack independently run wet-lab and OpenAI low-resource public SQLite suite vs private hidden migration test are different samples. All vendor benchmarks and timing are not independent reproduction.
8. Target draft must be substantive, with first-party attribution, exact snapshot timing, denominators, apparatus, license, status labels; prevent dense kanji translation and misplaced general claims. The 35pp body plan is an estimate not a commitment or drafting authorization.

## Human Owner decision requested (not recorded by this file)

Owner reviews above exact W43 r6 architecture and residual limitations. Choose exactly:
- `APPROVED` — explicitly approve **2026-W43 Architecture r6** with fixed, provenance-bound canonical architecture as reviewed. Sol will then create a separate immutable Human Gate record through approved, trusted `RECORD_ARCHITECTURE_APPROVAL` bridge; read back actual approval receipt and only then dispatch Muse Draft.
- `REQUEST_CHANGES` — specify Architecture changes, with the proper upstream regeneration boundary and exact reviewed commit; Sol will record authentic Human revision and execute canonical revisions.

**Until explicit Human response, both Human Gates PENDING; NO Human decision or approval is fabricated.** No Draft, TeX, PDF, Freeze or Release merely because this review packet exists.
