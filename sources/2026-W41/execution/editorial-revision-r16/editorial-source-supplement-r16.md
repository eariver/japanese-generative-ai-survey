# W41 r16 editorial source supplement (edition-local; NOT canonical acceptance)

Status: `EDITION_LOCAL / SOURCE_SUPPLEMENT`
Date: 2026-10-14 JST
Authority: `SOL_W41_R15_INDEPENDENT_AUDIT_ACCEPTED / BOUNDED_PUBLICATION_REPAIR`
Classification: SOURCE_VERIFIED / NOT_CANONICAL_ACCEPTANCE

This supplement records newly verified primary-source facts used ONLY in the
unapproved r16 editorial proof. It does NOT amend Accepted Evidence, Evidence Cards,
Selection, Architecture, Canonical Draft, checkpoints, or Human decisions.
Formal semantic review must independently judge adoptability of these additions.

## S1 — Haiku 5.5 full price table (R15-M04)

- Fetched (read-only): `https://www.anthropic.com/claude-haiku-5-5` on 2026-10-14
  (page dated October 7, 2026; Pricing section, "Price per 1 million tokens").
- Verified table (Haiku 5.5, prompts up to / over 100k):
  - Cache reads: $0.01 / $0.05
  - Cache writes: $0.125 / $0.625
  - Input tokens: $0.10 / $0.50
  - Output tokens: $0.50 / $2.50
- Reference columns on same page: Haiku 4.5 ($0.10 / $1.25 / $1.00 / $5.00),
  Sonnet 5.5 ($0.10 cache reads after halving / $2.50 / $2.00 / $10.00).
- Sonnet cache-read halving confirmed on page: "$0.10 per million tokens rather
  than $0.20" (50% less).
- Authority boundary:
  1. r15 Accepted Evidence Card (`evidence:2026-W41:c880db78235eeef3` claim-1)
     supports: split ≤/>100k, cache-read $0.01/$0.05, Sonnet $0.20→$0.10.
     It does NOT contain input/output/cache-write rows or the per-1M-token unit.
  2. No saved source excerpt contains the full rows (delegated read only).
  3. The Oct 7 official page body supports the full 4-row table + unit above.
  4. Items in (3) beyond (1) are recorded HERE as supplement additions.
     They must NOT be described as pre-existing Card claims.
- Use in proof: r16 P1 (p5/t1/p9/p10/p12/n1), synthesis signals line, preview,
  TeX Section 1 + table + synthesis/community/frontmatter/notes as applicable,
  haiku55 bib note. Bill guidance kept distinct: table + usage → estimate;
  table estimate ≠ individual billed amount.
- No guessing: cache-write duration qualifier `(5分)` transcribed from mission
  audit table; page labels the row "Cache writes" ($0.125/$0.625); no other
  duration or unit inferred.

## S2 — Bibliography title/heading verifications (R15-M05)

- gpt6ui: page title/H1 `GPT-6 and Intelligent UI for everyone`, dated October 7, 2026
  (fetched 2026-10-14, `https://openai.com/index/gpt-6-for-everyone/`).
- textgrain: page title `Our approach to EU text provenance rules`, dated October 5, 2026
  (fetched 2026-10-14, `https://openai.com/index/eu-text-provenance/`).
- clefomni: changelog H1 `Clef-omni adds audio and video input, Clef-flash is now
  cheaper, and Clef is faster`, dated October 9, 2026
  (fetched 2026-10-14, changelog post URL).
- synthid: page fetch attempted 2026-10-14 (JS-heavy, body not reliably extractable);
  title adopted from audit-provided official title
  `We're making it easier to identify AI-generated content globally`
  (URL `https://blog.google/innovation-and-ai/models-and-research/google-deepmind/synth-id-ai-content/`
  already bound in Accepted Evidence Card `ef2ef9a25ec009ba`); recorded here as
  audit-provided title + Evidence-bound URL, NOT as fresh body verification.
- pplxdecider: no individual permalink found in saved materials (Evidence binds only
  category `community.perplexity.ai/c/announcements/9`); recorded as category with
  permalink unfetched (no URL invented).
- decisions/ultrafast: shared changelog listing `https://developers.openai.com/api/docs/changelog`;
  no stable per-entry fragment verified in saved materials; recorded as listing
  (no fragment invented).

(End of file)
