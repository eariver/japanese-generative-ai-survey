# Survey Production session — ts002-issue543-terminology-20260926

Issue: `#543` — final broad reader-facing terminology normalization (Human Owner Publication Preview REQUEST_CHANGES)
Sol boundary: Issue #543 Sol execution-boundary comment (eariver, 2026-09-26T07:15:27Z) + Issue body (created 2026-09-26T07:12:58Z)
Branch: `special/beyond-text-2026-work` (existing only)

## Starting guards (remote authority, all PASS)

- `git ls-remote origin` + fetch: work HEAD `d8c81af83…` / tree `c09f5afd…`, main `0bbb02b3…` / tree `e4ddde5e…` — all match.
- Local was 1 commit behind (Sol #539 PASS record); fast-forward sync only.

## Human Publication Preview r7 REQUEST_CHANGES canonical record

- Next revision derived from review index (max r6 → 7).
- `gates/reviews/publication-r7.json` (reviewed d8c81af83, reviewed_at = Issue #543 creation, boundary DRAFT_COMPLETE, publication-local). Architecture approval preserved. Committed before mutation.

## Method

- Seed families audited by parallel read-only agents (sampling/score/flow/metrics/speech-eval; network/component/implementation/context-dependent) + seed-independent broad suspicious-translation scan (37 new candidates, methods M1–M5) + worker primary-source read-back for semantic-risk 量保存流れ (VITS arXiv 2106.06103 abstract confirms normalizing flows; in-repo volume-preserving wording was a misreading).
- All substitutions applied with exact-count assertions; residuals verified.

## Ledger

- `execution/terminology-issue543/terminology-decision-ledger.{json,md}` — 88 rows: ISSUE_SEED 45 / BROAD_SCAN 43; REPLACE 72 rows / RETAIN 12 / ESCALATE 4.
- ESCALATE (text unchanged): 分類得点 L158; 自然さ得点 L1090/L1108; 全帯域抽出 L158; 濾波崩壊×2; 膨張形式×1.

## Frozen regression

- #533 (17 terms) + #539 (all targets + cross-attention) remain 0. #539 RETAIN counts unchanged (母数3/案内6/資料14/枠40).

## Invariants (before → after)

- autocite 1259 identical; keys 139 identical; labels identical; PARTIAL 12; bib byte-identical.
- Sections 116, order unchanged; 8 headings reworded by terminology.
- Units: no removals; FID/IS/MOS/SNR acronym introductions are intended normalizations.
- Numerics: +128 one (百二十八→128, value-preserved).

## Next steps (same session)

1. Commit + push tex/ledger (FF only).
2. CI PDF rebuild + artifact audit.
3. build/advance validation (issue543 variants) + rendered-PDF broad scan + all-page visual QA + candidate.
4. Commit + push; stop at PUBLICATION_PREVIEW pending. No approval/Freeze/Release.
