# W41 editorial-proof PDF QA r16 (technical + layout, all pages)

Date: 2026-10-14 JST
PDF: `surveys/weekly/2026-W41/main.pdf` (17 pages, 434166 bytes)
SHA-256: `d1d1ed5d4f6f8a3cc2f76ddeeccc1e41e16f6f6ae9b2b89379395da50c1545df`
(r15 PDF `cc6d5a9103…` remains in Git history; r16 is the new unapproved proof.)
Toolchain: LuaLaTeX (TeX Live 2026) + Biber 2.22
Status: `UNAPPROVED_EDITORIAL_PROOF` (independent semantic/visual audit required)

## Technical fidelity (r16 → PDF)

- Body loss: none (fragment check 6/6; 37157 extracted chars).
- 5 tables with captions verified (表1 frontier/pricing, 表2 7-item availability,
  表3 synonym triple, 表4 Astra quality 8 rows, 表5 provenance scope).
  Haiku table row now shows 4-row per-1M-token table + bill-vs-estimate note.
- Names: all model/API/bench names as in r16 (spot-checked).
- Numbers: FPR/200/400, 92/66/17, AA 49.57/49.76pt et al., MoE triples,
  Elo 1050±14, 4K-token, 44%, 10倍 (renders `10 倍` on line break, intact),
  1800億/24万年分, 90%+, 13.4pt/32%, Haiku $0.10/$0.50/$0.01/$0.125 vs
  $0.50/$2.50/$0.05/$0.625 + Sonnet $0.20→$0.10 — all match r16.
- Old unknowns gone where table confirms (`入力・出力本体の単価` absent);
  system-card/IDs unknowns retained where still true.
- FINAL_SYNTHESIS (Sec.8) + COMMUNITY_MOVEMENT (Sec.7, negative-space) present.
- References complete ([1]–[20] with fixed titles, dates, URLs, access dates;
  Biber resolved 20/20; no undefined citations; `text excluded` categorical gone).

## Visual QA (all 17 pages rendered as images + text)

- Tables: no boundary splits; Japanese/English/scripts intact.
- Characters: no tofu/garbling (fonts embedded); `%`/`$`/`_` render correctly.
- Headings: Section 7 Community + Section 8 Week in Review correctly numbered
  (TOC matches TeX order); no isolated lone headings.
- Blank pages: none fully blank. Page 14 end-of-articles whitespace (710 chars:
  complete `次に何を見るべきか` + reading box) retained from r15 layout;
  complete subsection, not a stray orphan; no unnatural fully-blank page.
- Footnotes/references: no overflow (URLs break via xurl; pp.16–17 clean).
- Cover/TOC/numbers: issue/date/cutoff/anchors, 8-line Contents (7 Community,
  8 Week in Review), kickers, page numbers 1–17 consistent.
- Log: no undefined citations/refs; Biber clean; one 0.29pt overfull (negligible).

## Fixes vs r15 (meaning-preserving except audited M-items)

- M01 bib bounded language; M02 community rewrite; M03 chapter numbers;
  M04 Haiku 4-row table + bill guidance; M05 titles/dates/URL classifications;
  M06 retrieval/audit language removal. Manifest rebuilt + revalidated per change;
  PDF rebuilt from exact bound bytes; SHA regenerated.

## Remaining visual-review condition

- INDEPENDENT_VISUAL_PASS not claimed. All-page renders available for the
  independent auditor (`w41r16-*.png` working copies, not committed).
  Formal visual review of these exact bytes is still required.

## Invariance

- No Architecture/Evidence/State/checkpoint/approval changes; no Candidate;
  no semantic/visual/gate PASS fabricated; Preview `pending`.

(End of file)
