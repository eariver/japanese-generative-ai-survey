# Human Publication Preview dossier — 2026-W37 r2 (PENDING)

Status: `RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PENDING_HUMAN_DECISION`
Date: `2026-09-19`
Revision: `r2` (Human r1 REQUEST_CHANGES preserved; r2 awaits independent Sol review and Human judgment)

This dossier was assembled by the worker from frozen approved authority and regenerated Draft r2. It is not an independent Sol review and not a Human decision.

## 1. Exact review identity

- Edition `2026-W37` (WEEKLY + WEEKLY_MAGAZINE), target gate `PUBLICATION_PREVIEW`.
- Reviewed commit `74400d716e703c12efee97707ff0ee97d47f98a8` (State + Candidate + Candidate-bound PDF).
- Lifecycle `RELEASE_CANDIDATE`, terminal `HUMAN_GATE_REACHED`, next `PUBLICATION_PREVIEW`.
- Candidate `sources/2026-W37/publication/v2/publication-candidate-v2.json` (candidate SHA `8f74d379ccf7df181b8fbe0890d4774573f6c273c046ec44f15a80a184b3ab6b`, file SHA `eea9212fa615378503bcd6138aca52e2ed703f55c779f56619450d49cd68cc0a`).
- PDF `surveys/weekly/2026-W37/main.pdf` (11 pages, 309850 bytes, SHA `c2298653e959388f359c5dadf0121e28684950343e874c2305179b4c0aa5f4fe`, CI run `35369856431`, artifact `10558181589`).
- Manuscript `sources/2026-W37/publication/v2/reader-manuscript-v2.json` (manifest SHA `0113bab9947a1c2e4f3e2ebb6d782172147af53eff6b98e18c371322f44c5f36`, file SHA `6d13eaede6703fc986d5980562c5bf15e0ae2c327fbb57b82bfec1a74038abc6`).
- Human Preview r1 `REQUEST_CHANGES` (record `gates/reviews/publication-r1.json`, rev 1, boundary `ARCHITECTURE_ESTABLISHED`, reviewed `8057a468897f67d3a11bd9287f6f56f0485877ce`) preserved.
- Architecture approval: Human r1 `APPROVED` preserved (reviewed `55e700a34765654cd2ced0c2a454d4fb3433dd4f`, Architecture SHA `81e87a64c2418c71340ee8cc1dec28267a55055d2c02d7dbb06e33623efdfcfb`).

## 2. Architecture approval preservation

- `request-publication-preview-revision` with boundary `ARCHITECTURE_ESTABLISHED` does not reopen Architecture (`_reopens_architecture == False`, verified preflight).
- Post-revision read-back: lifecycle `ARCHITECTURE_ESTABLISHED`, `architecture_review == approved` with byte-valid provenance, `publication_preview == pending`, Draft/validation/preview checkpoints pending.
- `gates/architecture-approval.json` (SHA `1a9d27454cfd5a8dd4840be3ef7ccd59ca389145e4970281f47cc24c1f4d33d9`), snapshot `gates/reviews/approvals/architecture-r1.json`, and `architecture-v2.json` untouched (no delete/regenerate/re-approve).
- Frozen upstream unchanged: Discovery 14, Screening 13/1, Evidence 11/2, Materiality 12/1/1, Selection 12/1, Architecture 7 packages.

## 3. Draft r2 identity

- Regenerated from approved Architecture + frozen Evidence via `run_drafting_synthesis_v2_agent.py` (7/7 packages + synthesis).
- Draft packages (Architecture-derived, byte-identical to r1 where Architecture unchanged); Draft Results r2 and synthesis r2 rewritten in natural technical Japanese.
- Stage validation `execution/validation/draft-stage-validation-r2.json` PASS; checkpoint `orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json`; State `DRAFT_COMPLETE`.
- r1 Draft/TeX/PDF/candidate/review SHAs not reused.

## 4. Language QA (Worker)

- Record: `sources/2026-W37/execution/reviews/worker-w37-draft-r2-language-qa-20260919.json`
- Reviewer: `Worker/Agent (Muse Spark)` (not ChatGPT/Sol/Human).
- Method: all 7 Draft Results + synthesis read as continuous Japanese prose; headings/decks and claim-boundary wording included; PASS criterion is whether a technically literate Japanese reader understands mechanism/product/metric/license/limitation without reverse-engineering English.
- Result: `PASS` (3 checks). Forbidden-word scan alone was not accepted as sufficient; semantic reread performed.

## 5. Representative r1 → r2 language repairs

- 背後の文章模型 → バックエンドのテキストモデル
- 符号模型 → コーディングモデル / 言語モデル（文脈別）
- 符号を書く力 → コーディング性能
- 表の1符号あたりの値 → トークン単価表の値
- 道具立てを束ねる → エージェント実行基盤の整備
- 雲の上の代理人 → クラウド上のエージェント
- 砂場 → サンドボックス
- 給仕 → サービング
- 引擎 → エンジン
- Apache-2.0の許し → Apache-2.0ライセンス
- MITの許し → MITライセンス
- 札の表/報告 → モデルカードの数値/報告
- 訳しに絞った → 翻訳に特化した
- 混合専門家 → MoE / Mixture-of-Experts / 混合エキスパート
- 検出子 → IOC（侵害指標）
- 金融向けの整え → 金融業務向けパッケージ
- 三つの出し分け → 3つの独立したリリース
- 効率旗艦 → 高効率モデル
- 声の層 → 音声レイヤー
- 読みの偏り付け → キーワードバイアス
- 公開試し → パブリックベータ
- 互換の経路 → 互換ルート
- 求めを振り替える → リクエストのルーティング切り替え
- 開かれた重みは縦に伸びる → オープンモデルの3方向
- 安全の物差し → 技術的安全面の文脈
- Full verification: Draft r2 + TeX r2 contain zero occurrences of the Sol-flagged forced substitutions in technical senses (machine-checked) plus human semantic reread.

## 6. Section/package structure (r2)

1. `10-astra-vertical` — 金融業務向けChatGPT（Astra中核）
2. `20-voice-frontier` — GPT-Live-1（独立した音声レイヤー）
3. `30-harness-plane` — Agents APIパブリックベータ＋Fusion（17:00Z通常）
4. `40-efficient-flagship` — DeepSeek V4.1-Flash（ベンダー報告、Sep 14は今後の運用）
5. `50-frontier-coding` — SWE-2（コーディング性能とコスト）
6. `55-open-vertical` — 3方向のオープンモデル（オンデバイス/翻訳/マルチモーダル）
7. `57-safety-bound` — Anthropic脅威レポート（代表的事例の留保付き）
- Frontmatter/synthesis/source-notes included. No merge/reorder against approved thesis.

## 7. X/public citation audit

- Bibliography 19 records, cited 19 keys, missing 0, unused 0 (deterministic binding PASS).
- 8 direct X status URLs retained as auditable community citations (2 Astra, 2 DeepSeek, 2 coding/harness, 2 MiniCPM); all ordinary-window per Sol r1 Snowflake verification.
- X used as community/context only; technical facts grounded in primary sources.
- No internal Raw paths or blob URLs in reader citations.

## 8. Vendor-claim boundary audit

- FinServ benchmarks vendor-reported; pricing/limits absent.
- GPT-Live-1 bench vendor-reported; language/telephone scope incomplete.
- Agents API beta scope/GA/limits absent; partner/customer claims vendor-described.
- DeepSeek ahead-of-Pro vendor-attributed, unnamed parties, no independent reproduction; Sep 14 future; in-window pricing separate.
- SWE-2 vendor tables; list-pricing cost sensitivity.
- Fusion partnered methodology; 39% maximum with per-benchmark deltas; `2026-09-11T17:00:00Z` ordinary.
- MiniCPM/North/Ling card-reported; North judge-bound CC BY-NC; Ling Sep 4/8/10 phasing.
- Threat vendor investigations; full PDF/IOC unconsumed; Sep 11 detail excluded.

## 9. Temporal-boundary audit

- Ordinary `2026-09-04T18:00 ET`–`2026-09-11T18:00 ET` (end-exclusive); Fusion 17:00Z ordinary with 5-hour margin; pre-window 1 and late-breaking 20 outside ordinary totals; Sep 14 routing future; Ling phasing without hour assertion.

## 10. Publication Boundary audit

- Lexical gate PASSED on all 12 TeX/Bib files (0 blocking, 0 suppressions).
- No HOLD/PARTIAL/VERIFIED/MATERIAL/Screening/Selection/candidate/blocker/revision-ID/internal-path leakage in reader prose.

## 11. Semantic/editorial review (Worker provenance)

- `sources/2026-W37/publication/v2/semantic-editorial-review-v2.json`: `PASSED`, 11 checks.
- Reviewer: `Worker/Agent (Muse Spark)` (Issue #506 repair; no `ChatGPT` identity).
- File SHA `180f82c7711650cdb5fbedf70dea2a6b773d0888f6a15e9f277abfa459523ad6`.

## 12. Visual review (Worker provenance)

- `sources/2026-W37/publication/v2/visual-review-v2.json`: `PASSED`, 2 checks, 11 pages.
- Reviewer: `Worker/Agent (Muse Spark)` (Issue #506 repair).
- File SHA `b9319b224f45599d21f18139a1f2205f18e5f4b68045d628ffd3db58b4314ee9`.
- Exact PDF bytes visually checked; no clipping/overlap/glyph defect; Japanese extraction clean.

## 13. Residual non-blocking limitations

- All vendor benchmarks externally unreproduced; judge/partnered methods unverified.
- Pricing/entitlement/language/telephone/rate/region gaps explicit.
- Per-token image values and per-language tables unconsumed.
- V4.1-Pro date absent; untested Fusion pairs not generalized; chip behavior vendor-described; Ling hour unresolved; threat PDF/IOC unconsumed; image/video quiet as finding.

## 14. Deviation from approved Architecture

None. Thesis, order, must-cover and boundaries preserved. No upstream rerun or Architecture change.

## 15. Review provenance downstream

- Worker created: Draft r2, language QA, TeX/Bib r2, deterministic outputs, manuscript/bundle, Worker reviews, candidate, this dossier.
- Worker did not self-author Sol/Human review. All Worker reviews labeled `Worker/Agent (Muse Spark)`.
- Fresh Preview r2 awaits independent Sol review and Human judgment. No Preview r2 decision recorded.
