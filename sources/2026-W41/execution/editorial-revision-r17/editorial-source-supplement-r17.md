# W41 r17 editorial source supplement (edition-local; NOT canonical acceptance)

Status: `EDITION_LOCAL / SOURCE_SUPPLEMENT`
Date: 2026-10-14 JST
Authority: `SOL_W41_R16_INDEPENDENT_AUDIT_ACCEPTED / BOUNDED_READER_ACCURACY_REPAIR`
Classification: SOURCE_VERIFIED / NOT_CANONICAL_ACCEPTANCE

r16 supplement (`editorial-source-supplement-r16.md`) preserved unchanged.
This file records NEW r17 verifications only. Nothing here amends Accepted
Evidence, Cards, Architecture, Canonical Draft, checkpoints, or Human decisions.

## S17-1 — Haiku prompt-length boundary + 5m/1h cache-write distinction (M-01)

- Re-verified (read-only) 2026-10-14:
  - `https://platform.claude.com/docs/en/models/haiku-5-5/overview`
    (Pricing table: `Input $0.10 / MTok for prompts up to 100,000 tokens;
    $0.50 / MTok for prompts over 100,000 tokens`; same up-to/over phrasing
    for Output, 5m cache write, 1h cache write, Cache read).
  - `https://platform.claude.com/docs/en/about-claude/pricing`
    (general pricing reference; 5m vs 1h cache-write rows distinguished).
- Boundary condition: the tier is decided by each request's prompt length
  (`prompts up to / over 100,000 tokens`). Not monthly cumulative usage, not
  output-token length, not task-total consumption. No progressive-partial
  reading (only one tier applies per request).
- 5-minute vs 1-hour cache write (must not confuse):
  - 5m cache write: $0.125 / MTok (up to 100k) ; $0.625 / MTok (over 100k).
  - 1h cache write: $0.20 / MTok (up to 100k) ; $1 / MTok (over 100k).
  - r17 proof uses 5m values only (as in r16); 1h values recorded here solely
    to prevent confusion. No 1h price appears in reader prose.
- Bill guidance kept: confirmed unit table + usage → estimate; table estimate
  ≠ individual billed amount. No guessed billing examples created.
- Authority boundary: prompt-length wording and 5m/1h distinction beyond the
  announcement table are supplement additions (Card claim-1 covers split rates
  + Sonnet halving only). Formal semantic review judges adoptability.

## S17-2 — Gemini announcement identity ruling (M-02)

1. Card URL + Claim: `evidence:2026-W41:9fdd36169d2efaf7` binds locator
   `primary:blog.google/.../gemini-at-work` (truncated) with claim-1 (Oct 8
   universal work agent: prompt box, skills/tools, cost controls, enterprise
   governance) and claim-2 (rollout specifics deferred to Cloud blog, unfetched).
2. Original-URL re-check: `https://blog.google/products/workspace/gemini-at-work-2026/`
   returns 404 on 2026-10-14 (not verifiable now).
3. New article check: `https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/gemini-at-work/`
   verified 2026-10-14 — page covers the Gemini agent as a universal agent for
   work with prompt window/box, skills and tools, cost controls, and enterprise
   governance. Claim match CONFIRMED (same four stub elements).
4. Identity ruling: DIFFERENT official material (different locator/path; original
   not retrievable to prove sameness). Treated as a separate official source
   supporting the same stub claims, NOT as the same document.
5. Bib consequence: `geminiagent` URL replaced (old 404 → new verified Cloud URL)
   with Before/After recorded in `bibliography-audit-r17.md`. P2 text unchanged
   (stub bounds kept; rollout specifics still unfetched).
6. Formal semantic review must judge whether the new source authority is
   adoptable for the stub claims.

## S17-3 — Bibliography locator checks (M-02/m-02)

- pplxdecider/pplxembed: no individual permalinks found in saved materials
  (Evidence binds category/thread URLs only). Kept with honest classification;
  no permalink invented.
- decisions/ultrafast: shared changelog listing verified as listing; no stable
  per-entry fragment found; kept as listing; no fragment invented.
- novasonic: Evidence-bound URL bot-limited on direct re-fetch (both case
  variants); search index shows live lowercase canonical with official title +
  Oct 5 date + 4-region/256K/same-pricing facts consistent with the note.
  URL kept as Evidence-bound; title fixed per audit; limitation recorded.
- Other entries: titles/dates re-verified as listed in `bibliography-audit-r17.md`.

(End of file)
