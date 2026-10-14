# W41 reader QA record r17 (architecture / reader fidelity, editorial proof stage)

Date: 2026-10-14 JST
Manifest: `sources/2026-W41/publication/v2/reader-manuscript-v2.json`
  (file SHA before r17 regen `09dd66336d8e…` / after `87bf7055be5c…`;
   content digest before `6e65d09a899d` / after `5f2286a89a69`; Git-tracked).
Primary: `surveys/weekly/2026-W41/main.tex` (comment updated to r17 provenance)
Status: `EDITORIAL_PROOF_QA` (not a semantic-review PASS, not a surface-gate PASS)

## 1. Architecture coverage 27/27 (M-01/M-02 consistent)

Manifest validator enforces exact set equality with approved
`architecture-v2.json` (4+5+7+3+5+3=27). Validated r17 manifest reports 27 rows.
No requirement dropped or invented. P1 pricing substance still maps must-cover[2]
(prompt-length condition added, numbers unchanged). Bib title/URL work caused no
body changes (P2/P3/P4/P5/P6 zero diff).

## 2. Each requirement has actual reader content (semantic, not formal-only)

- P1 (4): Section 1 paragraphs + table contain tier mapping, 44% definition,
  per-request prompt-length 4-row per-1M-token table + Sonnet halving, bench
  table with pending-reproduction note. Column headings unified
  (`Prompt ≤100k / >100k tokens`, TeX math-mode rendering of the same condition
  recorded here; proposals carry the Unicode form).
- P2–P6: carried r16 substance, verified present (fragment check 6/6).
- Details describe concrete TeX substance per requirement (coverage-map-r17).

## 3. Content–Evidence consistency (Card vs supplement separated)

- Refs/modes unchanged r16→r17 (S17 prompt-length/5m-1h/Gemini-identity facts NOT
  encoded as Card refs). TeX preserves r17 numbers/conditions.
- Gemini bib URL swap does not alter P2 claims (stub bounds kept; rollout
  specifics still unfetched). New-source adoptability left to semantic review
  (supplement S17-2 + bibliography-audit-r17).

## 4. Reader requirements (sampling limit explicit)

- `FINAL_SYNTHESIS` → Section 8 (correct; Haiku column condition fits latest body).
- `WEEKLY_COMMUNITY_MOVEMENT` → Section 7 + public ledger, as
  `FULFILLED_WITH_SAMPLING_LIMIT`: ledger-scoped 14-OFFICIAL composition,
  absence-as-finding (not proven-nonexistence), no count-based inference, next
  primary records specified. Limit stated in reader note AND here.
- Contents (7 Community / 8 Week in Review) matches TeX order.

## 5. r17 proposal ↔ TeX correspondence

- P1 (16 blocks, 4 changed) → Section 1; P2–P6 carried → Sections 2–6
  (fragment check 6/6). Synthesis/community/frontmatter/notes/bib updated as
  recorded in prep log; ledger unchanged (classification stands).

## 6. No internal metadata on reader surface

- Lexical lint on `main.tex` + 10 sections + `references.bib`: 0 BLOCKING.
- Coverage/requirement details: 0 BLOCKING. Revision numbers, Evidence/Card
  machinery, and audit-process verbs kept out of reader body/bib (boundaries
  live in supplement/audit records). Uncertainties kept.

## 7. Manifest bound to exact TeX bytes

- Manifest primary + 12 supporting files rebound to current bytes
  (SHA + byte_count) after every TeX change and revalidated. PDF built ONLY
  from these exact bytes (see pdf-qa-r17).

## Open (not claimed)

- Independent semantic review (S17 prompt-length/5m-1h adoptability, Gemini
  new-source authority, community analysis, bib bases): NOT performed, NOT passed.
- Formal surface gate: NOT passed. Independent visual review of exact r17 PDF:
  pending (page renders prepared; INDEPENDENT_VISUAL_PASS not claimed).

(End of file)
