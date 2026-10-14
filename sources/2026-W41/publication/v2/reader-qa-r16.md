# W41 reader QA record r16 (architecture / reader fidelity, editorial proof stage)

Date: 2026-10-14 JST
Manifest: `sources/2026-W41/publication/v2/reader-manuscript-v2.json`
  (file SHA before r16 regen `10ac07521300…` / after `09dd66336d8e…`;
   content digest before `0db5b898cd5b` / after `6e65d09a899d`; Git-tracked).
Primary: `surveys/weekly/2026-W41/main.tex` (unchanged filename, bytes as bound)
Status: `EDITORIAL_PROOF_QA` (not a semantic-review PASS, not a surface-gate PASS)

## 1. Architecture coverage 27/27 (M01–M06 consistent)

Manifest validator enforces exact set equality with approved
`architecture-v2.json` (4+5+7+3+5+3=27). Validated r16 manifest reports 27 rows.
No requirement dropped or invented. Approved Architecture wording (incl. P5
`text excluded`) untouched; reader uses bounded announcement language (M01).

## 2. Each requirement has actual reader content (semantic, not formal-only)

- P1 (4): Section 1 paragraphs + table contain tier mapping, 44% definition,
  full 4-row per-1M-token table + Sonnet halving (supplement S1), bench table
  with pending-reproduction note. Old unknowns replaced only where the table
  confirms; system-card/IDs still unknown.
- P2 (5): Section 2 paragraphs contain beta entry, forum briefs, embed
  comparator, tier box, stub box with unfetched bounds (carried, verified).
- P3 (7): Section 3 paragraphs + 7-row table contain Kolibri/d1/EmbeddingGemma
  specs, Beam/Mistral comparison with 49B/52B unresolved, timestamp pin, Nova
  box (carried, verified).
- P4 (3): Section 4 paragraphs contain card spec box, narrowed blog-search
  sentence (no web-wide denial), Elo caveat with no ranking (carried).
- P5 (5): Section 5 paragraphs + 3 tables contain token operating points,
  rollout/gating, scope table with bounded text language, non-equivalence note,
  provenance comparison table (M01/M06 applied, scope preserved).
- P6 (3): Section 6 paragraphs contain program box, math box, simulated-eval
  box with respective unfetched bounds (carried).
- Verified by r16 proposal↔TeX fragment check (6/6 packages, all blocks present).

## 3. Content–Evidence consistency (Card vs supplement separated)

- r16 proposals passed draft-check 6/6 + source-claim audits; refs/modes unchanged
  r15→r16 (supplement S1 NOT encoded as Card refs).
- TeX preserves r16 numbers/conditions/scopes; new Haiku rows/unit appear ONLY via
  supplement S1 (SOURCE_VERIFIED / NOT_CANONICAL_ACCEPTANCE); nothing presented
  as a pre-existing Card claim.
- Synthesis signals line updated for 4-row table; no new benchmarks introduced.

## 4. Reader requirements (M02/M03 semantic fulfillment)

- `FINAL_SYNTHESIS` → Section 8 (sections/85-week-in-review.tex): cross-article
  total with provision-vs-performance, total/active, shipped-vs-promised,
  detection-vs-scope, vendor-measured conditions; Haiku lines fit latest body.
  Chapter number corrected (was Section 7 in r15 records).
- `WEEKLY_COMMUNITY_MOVEMENT` → Section 7 (sections/80-community-movement.tex) +
  public ledger (14 rows): substantive negative-space analysis (official-arrival
  areas, exact 14/12/2 accounting with constraints, absence of independent
  verification as the finding, no support/evaluation inference from counts, next
  primary records specified). FULFILLED used only on this substantive basis;
  `COMMUNITY_SEMANTIC_FULFILLMENT_PENDING` not needed.
- Contents (00-frontmatter) corrected to 7 Community / 8 Week in Review,
  matching TeX order (TeX order itself unchanged).

## 5. r16 proposal ↔ TeX correspondence

- P1 (16 blocks) → Section 1; P2 (17) → Section 2; P3 (22) → Section 3;
  P4 (7) → Section 4; P5 (19) → Section 5; P6 (13) → Section 6 (all blocks
  adopted; fragment check 6/6).
- Intentional wording records: P1/t1 cross-ref naturalization (carried from r15);
  Haiku 4-row table (S1); P5 retrieval-language naturalization (M06);
  community full rewrite (M02, analysis not restatement).
- Added structure (frontmatter/synthesis/movement/notes/bib/ledger) preserved
  from r15 with M02–M06 updates noted above.

## 6. No internal metadata on reader surface (M06)

- Lexical lint (Frozen Core patterns) on `main.tex`, all 10 section files,
  `references.bib`: 0 BLOCKING.
- Coverage/requirement details: 0 BLOCKING (pre-checked).
- Removed from reader: `日次 triage` (→ analysis prose), `一次読み` (→ bounded
  measurement reading), `text excluded` categorical (→ bounded announcement
  language), process verbs in bib (→ source limitations). Uncertainties kept.
- Manifest metadata (SHAs, supplement refs, audit history) lives outside TeX;
  reader body has no repo paths, Evidence IDs, revision numbers, or agent logs.

## 7. Manifest bound to exact TeX bytes

- Manifest `primary_source` + 12 `supporting_files` bind current file bytes
  (SHA + byte_count); rebuilt after every TeX change and revalidated.
- PDF built ONLY from these exact bytes (see pdf-qa-r16). PDF-only change with
  stale manifest prohibited (not done).

## Open (not claimed)

- Independent semantic review (incl. S1 adoptability + community analysis):
  NOT performed, NOT passed. Supplement S1 left as explicit audit matter.
- Formal surface gate: NOT passed (requires independent semantic authority).
- Independent visual review of exact r16 PDF: pending (all-page renders prepared;
  INDEPENDENT_VISUAL_PASS not claimed).

(End of file)
