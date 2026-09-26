# Survey Production session — ts002-issue539-terminology-20260926

Issue: `#539` — second-pass reader-facing terminology normalization (Human Owner Publication Preview REQUEST_CHANGES)
Sol boundary: Issue #539 Sol execution-boundary comment (eariver, 2026-09-26T05:53:23Z) + Issue #539 body (created 2026-09-26T05:49:42Z)
Branch: `special/beyond-text-2026-work` (existing only)

## Starting guards (remote authority, all PASS)

First attempt stopped zero-writes on stale local refs. Re-verified against remote (`git ls-remote origin` + fetch):
- Remote work HEAD `f166c4c44a3f1acb3c8730f4ef3ce10f84ae12fc` == Expected remote HEAD.
- Remote work tree `b1ab6a8cab0a5dcc643bfa04f91c31520b27cdda` == Expected remote Tree.
- Remote main `0bbb02b3c5963403860897daec2feaf61e82589a` / `e4ddde5ed5059d303b818f54e27204369b256bcb` == reviewed main.
- Local HEAD was exactly one commit behind remote (parent 3c72bec1b); synced by fast-forward merge only (no reset/rebase/force/new branch).

## Main guard

- Canonical `survey_human_gate_v2.py request-publication-preview-revision`; Architecture approval preserved; no Freeze/Release/merge.

## Human Publication Preview r6 REQUEST_CHANGES canonical record

- Next revision derived from review index (max publication r5 → 6; `--expected-revision 6` as assertion, not hard-code).
- `gates/reviews/publication-r6.json` (reviewed commit f166c4c44, reviewed_at = Issue #539 creation 2026-09-26T05:49:42Z, boundary DRAFT_COMPLETE, publication-local).
- Lifecycle RELEASE_CANDIDATE → DRAFT_COMPLETE. Architecture approval untouched (approved). Committed as 5f7a5fec before any repair mutation.

## Changed files (this session, pre-PDF)

- `surveys/special/beyond-text-2026/main.tex` (terminology-only; see ledger; references.bib byte-identical a639eca3…)
- `sources/SP-beyond-text-2026/execution/terminology-issue539/terminology-decision-ledger.{json,md}` (new, 68 rows, MD generated from JSON)
- `sources/SP-beyond-text-2026/gates/reviews/publication-r6.json` + review-index + production-state (committed 5f7a5fec)

## Terminology ledger

- Canonical JSON (68 rows: REPLACE 63 / RETAIN 5 / ESCALATE 0) + synced MD view.
- Every substitution applied with exact-count assertion; residuals verified zero (high-confidence) or retain-count.
- 票-anaphora coherence: 模型票→モデルカード with 票内/票外/standalone 票→カード系.
- Section titles legitimately updated ×2 (資料効率化/資料側→データ効率化/データ側); order/count unchanged.

## High-confidence before/after (main.tex)

- 模型 142→0; 模型票 4→0; 票(card-anaphora) 11→0; U網 14→0 (U-Net 3→17); 波形網 5→0 (WaveNet 9); 得点網 2→0; 枠間 6→0 (フレーム間 6); 民生画像処理装置 5→0 (民生GPU 5); 文章符号器 4→0 (テキストエンコーダ 4); 交叉注意 21→0 + 交差注意 5→0 (クロスアテンション 26).
- 母数 11→3 (RETAIN 大域的母数2+大域母数1); 案内 27→6 (RETAIN 一般語6); 資料 86→14 (RETAIN 典拠14); 枠 82→40 (RETAIN 枠組み18+枠内19+枠外1+条件枠1+話者の枠1).

## Frozen #533 regression: PASS (all 17 terms 0)

## Semantic invariants (before → after)

- autocite blocks 1259→1259 identical; citation-key multiset identical (139 unique); unit multiset identical; labels identical; vendors identical; PARTIAL 12 unchanged; NEEDS_MORE 0.
- Sections 116, order unchanged; 2 headings reworded by terminology.
- Numeric tokens: −$24$×3 / +24×3 / +1×5, fully explained by sanctioned GPU rewording (24GB/9分/5秒720P24 numerals preserved; 単一→1基 device-count rendering).

## Next steps (same session)

1. Commit + push tex/ledger (fast-forward only).
2. Dispatch CI `Build Special survey PDF` on pushed SHA; download exact artifact.
3. pdf-build-audit-issue539 + build_validation_issue539 + advance_validation_issue539 + all-page visual QA + advance_candidate_issue539.
4. Commit + push; stop at PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION. No approval, no Freeze/Release.
