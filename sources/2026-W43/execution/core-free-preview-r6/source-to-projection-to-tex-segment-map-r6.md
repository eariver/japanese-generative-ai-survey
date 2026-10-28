# r6 full reader-visible segment map (r3.5 reader -> r3 projection -> r3 TeX)

Validator: `full-reader-visible-segment-join-r6.py` (clean
`R6_PROSE_FIGURE_TECHNICAL_FIDELITY_CONFIRMED`, exit 0, 36 checks;
negatives `NEGATIVES_PASS`, exit 0, 38 cases).
This document is the exact segment ledger behind the verdict. Every segment
below was compared ordered 1:1 with bounded formatting transforms only.
No global bag-of-words, no count-only proxy, no sampled exemption.

## Segment inventory (verified counts)

| # | Segment class | r3.5 reader | r3 projection | r3 TeX visible | Mapping rule |
|---|---|---|---|---|---|
| S01 | Document title | 1 | 1 | cover + `sec:cover-title` | TITLE_RELABEL (single allowlist) |
| S02 | P sections / subsections / recap head | 8 / 28 / 1 | identical 37 | 37 ordered subsequence | DASH_P_SECTION (` — ` -> ` ---`); subs + recap verbatim |
| S03a | Non-recap prose paras (reader->proj) | 71 | 71 | — | ordered 1:1; 17 TOKEN_OR_PATH_TRANSLATION + 1 POST_CUTOFF_REDUNDANCY_CLEANUP |
| S03b | Non-recap prose paras (proj->TeX) | — | 71 | 72 | ordered 1:1 + exactly 1 AUTHORIZED_PARAGRAPH_SPLIT (reading-guide + 典拠 para -> 2 TeX paras) |
| S04 | Reading-note blockquotes | 8 | 8 identical | 8 SurveyRule tcolorboxes | QUOTEBOX_WRAPPING, content-identical |
| S05 | Figures (full bodies) | 3 | 3 | 3 figure envs | full-body 1:1 (2 identical, 1 token translation in 典拠 line) |
| S06 | Code blocks | 5 (bash1/py1/text1/json2) | 5 | 5 verbatims | comments token-translated; proj->TeX byte-exact; env/default sentinels pinned |
| S07a | Recap paras (reader->proj) | 5 | 5 identical | — | RECAP 5/5 |
| S07b | Recap paras (proj->TeX) | — | 5 | 5 | visible-identical modulo `**`/`\textbf` |
| S07c | Production note | absent | absent | PRESENT x1 (r3 defect) | r3-mode documents it; r6-mode requires absence (AUTHORIZED_PRINT_ONLY_DELETION) |
| S08 | Tables / ordered rows / types / ids | 20 / 80 / 78+2 | identical join | — | TOKEN_SUBS + path masking + manifest physical_text |
| S08e | Table fence notes (reader->proj) | 17 | 18 | — | 16 identical + 1 TOKEN_TRANSLATION (MemT 1.86x) + 1 AUTHORIZED_BODY_ADDITION_F-R3-03 (p8-f2 TanStack 典拠 line) |
| S09 | TeX tables / cells | — | — | 20 / 307 nonempty | caption + per-row/per-cell ordered identity (trailing generator padding stripped + asserted empty) |
| S10 | Anchored claims | 29 (strict checker) | own proj row | own TeX row + bib URL | value + variant + qualifier facets, provider/unit/comparator/provenance |
| S11 | Bibliography apparatus | — (no bib section) | — | 36 unique + intro | transplant from r2-complete block; no r1 truncation fragments |
| S12 | Citation key spans | — | 19 visible + quotes | 19/1/13/2/1/0 | 13 NATURAL + 2 FURTHER quote-bound, CURATED_REVIEW_REQUIRED |
| S13 | Routes / URLs / qualifiers | POST + 10 quals | identical | `\texttt` + 34 `\url` (0 malformed) + GH/npm separation | exact spans both artifacts |
| S14 | Table post-notes (proj->TeX) | — | 18 fence notes | 18 post-table notes | ESCAPE_ONLY (`\$`, `\%`, `\_`) |

## Reader->projection line ledger (difflib, 529 vs 530 lines)

33 opcodes: 32 single-line replaces + 1 single-line insertion.

- Replace class A (17 prose + 1 table-note + figure 典拠 + code comments +
  5 table rows + blockquote-adjacent lines): covered by `norm_src_line`
  (TOKEN_SUBS_SORTED + code-span internal-path masking + snapshot masking).
- Replace class B (1): `PROSE-r35p66`
  `POST_CUTOFF／OUT であり当週非選択` ->
  `集計期間外のため当週非選択であり`
  (redundant `であり当週非選択` cleaned; `NEVER_STORY` keeps its space).
- Replace class C (1): TITLE_RELABEL.
  `# W43 日本語本文プレビュー r3.5（非正規編集資産）` ->
  `# 週刊生成AI技術調査 2026-W43 — 印刷用原稿 r3`.
- Insertion class D (1): `TABLENOTE-p8-f2`
  `典拠: 安定核=tanstack-gh（GH 15:18:14Zのみ）／npm=tanstack-npm（15:21:49Z・別典拠・原本未取得）`
  inserted before the p8-f2 fence close (F-R3-03 authorized body addition;
  flows to the TeX post-table note at old-r3 main.tex:777).

No other insertion, deletion, or reorder exists between reader and
projection. Post-insertion tails are byte-identical (recap 5 paras included).

## Projection->TeX ledger

- Headings: 8 P-sections with the single dash rule, 28 subsections
  verbatim, recap head verbatim; matched as an ordered subsequence of the
  39 TeX section commands (cover + bib heads are print structure).
- Prose: 71 md paras -> 72 TeX logical paras; the single structural delta
  is the reading-guide para (`読み方：POST /v1/decisions …` +
  `典拠: 公式ガイド …` on adjacent md lines) rendered as two TeX paras.
  Concatenated whitespace-collapsed equality holds; every other para maps
  strictly 1:1 (bold/code/bare-URL inline forms normalized, never skipped).
- Quotes: 8 md `> 【読み方の注意】…` lines == 8 TeX note-box bodies.
- Figures: titles equal modulo `【図：…】` brackets; all body lines equal
  modulo escapes (`\_`, `\$`, `\%`).
- Code: 5/5 byte-exact proj fence body == TeX verbatim body.
- Tables/claims/bib/keys/routes: carried r5 per-cell/per-claim/per-span
  logic, all green (S08-S14).
- Bibliography apparatus (intro sentence + `{\footnotesize…}` sizing line +
  36 entries) is TeX-only print structure transplanted from the r2-complete
  block; verified for completeness, never claimed as reader-mapped prose.

## What this map does NOT claim

- No independent semantic re-audit of r3.5 source truth (r3.5
  `PASS_WITH_LIMITATIONS` stands; R32-FULL-003 FIXED not reopened).
- No visual QA (separate Phase B / independent audit business).
- No Architecture re-grading (see
  `architecture-11-partial-disposition-r6.md`).
- No provenance upgrade for the 13+2 curated keys (see
  `reference-claim-tier-curation-r6.md`).

Allowlists above are exhaustive: any unlisted delta fails the checker with
its segment ID, expected/actual bytes, and cause code.
