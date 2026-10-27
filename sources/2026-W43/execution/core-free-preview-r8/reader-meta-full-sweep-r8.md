# W43 r8 reader-meta full sweep (TeX visible-region + actual PDF text/images)

Date: 2026-10-27 JST. Subject: r8 TeX `main.tex` (97447 bytes, SHA256 `4ed553e5d779dc6696322fe6eba6e0aca8f8bdec3d73428a26b89e0dee5c686d`) + r8 PDF (487351 bytes, SHA256 `abd5b99bd051703dbdc9420c19965ed039585c0436090ae219be665c6d17dc72`, 22 A4 pages).

Method: comment-excluded visible-region scan of entire `main.tex` document body (article, table cells, source notes, bibliography, cover) + actual r8 PDF text extraction (PyMuPDF) + all 22 page PNG visual inspection at readable/full resolution.

## Authorised A/B/C closures

- A (r7 l81 / PDF p04 Flint table cell): old `（計数規約は承認済みArchitecture境界注記）` → new `（totalとactive per tokenは計数規約が異なり、直接比較できない）`. Preserves 39.8B total, 約2.5B active, experts/layers/SWA, 512K/256K/262144, Apache-2.0, row position, 307 cells. Verified on PDF p04 text + p-04.png: new wording present, old absent.
- B (r7 l440 / PDF p11 FLUX prose): whole paragraph replaced; old `承認済みArchitectureの旧ラベルはraw検証待ちの legacy として保持` + redundant neighbouring sentence removed; new single epistemic distinction: PR/blog show availability claims but FAQ-attributed text has no verified URL/version/timestamp; NOT an established inter-publisher contradiction; keyframes/live/schema/GA not derivable. Preserves modality, commercial/performance conditions, known/unknown. Verified on PDF p11 + p-11.png.
- C (r7 l985 / PDF p22 bib [recap]): old `P1-P8横断の編集合成` → new `本号の各主題を整理した派生記述`. Preserves `[派生・限定]`, `URL未取得`, `新規数値なし`, `新規の一次主張を含まない`, machine key. Verified on PDF p22 + p-22.png.

r7→r8 TeX diff is ONLY these three (B = one whole paragraph). `preview.sty` byte-identical to r7 (`0199d86d3553dbe731944999885830892203d0d2f1ff87eb96ad3d84e82b5a44`).

## Full sweep patterns

Searched visible TeX for: `承認済みArchitecture`, `承認済み`, `Architecture境界`, `raw検証待ち`, `legacy として保持`, `編集合成`, `P1-P8横断`, `印刷用原稿`, `編集プレビュー`, `未承認`, `読者確認用プレビュー`, `非正準の編集 proof`, `受理済み Core`, `p1-f1`…`p8-f3`, `§…実物`, `分離記録した文脈注記`, `P1 ---`…`P8 ---`, `APPROVED`, `GATE`, `ARCHITECTURE_ESTABLISHED`, `QA`, `REVIEW`, `INDEPENDENT_`, `MUSE_`, `SOL_`, `Grok`, `Drive`, `operator transport`, `editorial proof`, internal IDs.

Findings:
- `Architecture` count in visible body: 0. All three residual meta wordings absent.
- `承認` hits are legitimate article content (1Password approval injection, trust-model, classifier gating) — not production metadata.
- `gate` hits are legitimate technical terms (`Gated DeltaNet-2`, classifier `gating`) — not workflow gates.
- `Grok binder は 当週の対象外` is legitimate weekly scope note (selection decision), not internal workflow language.
- `実物` hit is `動かせる実物` reader prose, not `§…実物` operator tag (all `§…実物` absent).
- `REVIEW` hit is substring of `NOT A PUBLICATION PREVIEW` footer — protective mark, not meta leak.
- No `印刷用原稿`, `編集プレビュー・未承認`, `読者確認用プレビュー`, `非正準の編集 proof`, `受理済み Core`, `p*-f*`, `§…実物`, `P* ---` remain.

## Genuine evidence caution preserved (not leaks)

`未検証` (23), `未実行` (8), `原本未取得`/`原本バイト未取得`, `発行元測定` (14), `独立再現なし` (10), `未取得` (33), `発行元公表`, `未確認`, `未開封`, `未照合`, `POST_CUTOFF` variants, `404` (2), `ライセンス` (12), `Apache-2.0` (12) all present. `RAW_NOT_ARCHIVED` 0 (as r7; GH/npm clocks use `RAW_NOT_ARCHIVED`-equivalent phrasing via `原本バイト未取得` — preserved).

## Protective marks preserved

- TeX `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF` present; PDF visible `NONCANONICAL CORE-FREE UNVALIDATED PDF PROOF` ×2 (cover + end footer); `NOT A PUBLICATION PREVIEW` present; `APPROVED PUBLICATION` absent. PDF metadata Subject/Keywords = `NONCANONICAL_CORE_FREE_UNVALIDATED_PDF_PROOF` (verified via `pdfinfo`). No Human approval claimed.

## PDF text cross-check

Actual r8 PDF text (PyMuPDF): old A/B/C strings absent (0 hits); new B phrase present p11; new A/C present modulo PDF line-break spaces (verified via excerpt: Flint table p04 shows new qualification; bib p22 shows `本号の各主題を整理した派生記述`). Proof marks present.

Conclusion: No additional unambiguous reader-facing metadata outside A/B/C requiring change. Scope preserved. If independent re-audit finds further meta, Sol authorization required before enlargement (per contract §2).
