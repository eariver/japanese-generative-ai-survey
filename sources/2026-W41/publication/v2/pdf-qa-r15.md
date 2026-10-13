# W41 editorial-proof PDF QA (technical + layout, all pages)

Date: 2026-10-14 JST
PDF: `surveys/weekly/2026-W41/main.pdf` (17 pages, 432744 bytes)
SHA-256: `cc6d5a910373d681dadd7658fd849eaa9c70b788ff388685db970a01feaf1908`
Toolchain: LuaLaTeX (TeX Live 2026, LuaHBTeX 1.24.0) + Biber 2.22 (user TinyTeX, no Core change)
Status: `UNAPPROVED_EDITORIAL_PROOF` (independent review required; not a Candidate)

## Technical fidelity (r15 → PDF)

- Body loss: none (generator fragment check 6/6; PDF text extraction contains all
  section substance; 36235 total chars).
- 5 comparison tables displayed with captions (表1–表5 verified in extracted text):
  frontier terms, 7-item availability, synonym triple, Astra quality (8 rows, points/%),
  provenance scope. No page-boundary breakage observed (tables intact on pages 3–4, 7–8, 9–10).
- Names: GPT-6/Sol/Luna, Haiku 5.5/Sonnet 5.5, Decisions/Perplexity/Ultrafast/Gemini,
  Kolibri/d1/EmbeddingGemma 2/Beam/Mistral/Clef-omni/Nova Sonic, Nano Banana 2.1,
  textGrain/SynthID, Cyber/Math/Ironclad, GDPval/OSWorld/HLE/TB4/AA-Index/Decision Index/Bench —
  all spelled as in r15 (spot-checked in extraction + page images).
- Numbers/units/dates: FPR 1%, 200≈80%/400≈95%, 92%/66%/17%, AA 49.57/49.76pt,
  34.09%/34.86% et al., 78.1B/3.46B + 501B/23B + 1.05T/52B, Elo 1050±14 Thinking,
  4K-token note, Oct 2–9 window + per-item dates, $/token splits, 1800億/24万年分,
  90%+ expectation, 13.4pt/32%/37.0→19.2min — all match r15 (extraction verified;
  `10倍` renders with line-break space as `10 倍`, content intact).
- FINAL_SYNTHESIS included (Section 7, pages 12–14: 6 enumerated changes + joint
  significance + next observations + reading box).
- WEEKLY_COMMUNITY_MOVEMENT included (Section 8, page 12: 14-link split + negative
  space + announcement vs re-attention + context-only box).
- References complete (pages 16–17: 20 entries [1]–[20] with titles/URLs/dates/access
  dates; Biber resolved all 20 citekeys; no undefined citations in final log).

## Visual QA (all 17 pages inspected via text + page renders)

- Tables: no page-boundary splits; Japanese/English/scripts intact; captions bound.
- Characters: no tofu/garbling observed in renders (HaranoAji + LM fonts embedded);
  `%`/`$`/`_` escaped (44%, $0.01, service_tier render correctly).
- Headings: no isolated lone headings (all subsections followed by body text;
  page 4 Section 1→2 transition and page 10 tables→heading both carry text).
- Blank pages: none fully blank. Page 14 is the last two-column content page
  (heading + paragraph + reading box, 710 chars) with lower-half whitespace from
  transition to one-column Source Notes — complete subsection, not a stray orphan
  (initial 3-line orphan fixed via `\Needspace`, W40 precedent; no content change).
  No unnatural fully-blank page.
- Footnotes/references: no overflow (refs break cleanly across pages 16–17; URLs
  hyphenated via xurl; page numbers/headers consistent 1–17).
- Cover/TOC/numbers: cover (issue/date/cutoff/anchors), Contents (8 lines),
  This Week boxes, section kickers, page numbers all consistent.
- Readability first: no squeezing to cut pages (17 vs W40 14 reflects W41 content;
  `\balance` retained; overfull `\vbox 28.9pt` during output is balanced-column
  whitespace, not clipped content — verified in renders).

## Fixes applied (same run, meaning unchanged, manifest rebuilt)

1. `balance.sty` missing → installed `preprint` bundle via user tlmgr (toolchain only).
2. Tables `[h]`→`[htbp]` (float placement, no wording change).
3. `\Needspace{10\baselineskip}` before final synthesis subsection (orphan fix, W40 precedent).
4. P1/t1 cross-ref `P2のインフラ記事`→`エージェント基盤の記事` (recorded in correspondence;
   predates PDF; no internal ID on reader surface).
- After each TeX change: manifest rebuilt to exact bytes + revalidated;
  PDF rebuilt from exact manifest-bound bytes; SHA regenerated.

## Canonical / gate invariance (this Phase)

- No Architecture/Evidence/State/checkpoint/approval changes; no Candidate assembly;
  no semantic/visual review PASS fabricated; no surface-gate PASS; no Human decision.
- PDF is editorial proof only; formal Publication Preview remains `pending`.

(End of file)
