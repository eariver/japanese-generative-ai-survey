# W41 reader QA record (architecture / reader fidelity, editorial proof stage)

Date: 2026-10-14 JST
Manifest: `sources/2026-W41/publication/v2/reader-manuscript-v2.json` (validated)
Primary: `surveys/weekly/2026-W41/main.tex`
Status: `EDITORIAL_PROOF_QA` (not a semantic-review PASS, not a surface-gate PASS)

## 1. Architecture coverage 27/27

Manifest validator enforces exact set equality with approved
`architecture-v2.json` (4+5+7+3+5+3=27). Validated manifest reports 27 rows.
No requirement dropped or invented.

## 2. Each requirement has actual reader content

- P1 (4): Section 1 paragraphs + comparison table contain tier mapping, 44% definition, two-tier pricing, bench table with pending-reproduction note.
- P2 (5): Section 2 paragraphs contain beta entry, forum briefs, embed comparator, tier box, stub box with unfetched bounds.
- P3 (7): Section 3 paragraphs + availability table contain Kolibri/d1/EmbeddingGemma specs, Beam/Mistral comparison with 49B/52B unresolved, timestamp pin, Nova box, 7-row table.
- P4 (3): Section 4 paragraphs contain card spec box, narrowed blog-search sentence (no web-wide denial), Elo caveat with no ranking.
- P5 (5): Section 5 paragraphs + 3 tables contain token operating points, rollout/gating, scope table, non-equivalence note, provenance comparison table.
- P6 (3): Section 6 paragraphs contain program box, math box, simulated-eval box with respective unfetched bounds.
- Verified by generator fragment check (6/6) + manual TeX read (all sections).

## 3. Content–Evidence consistency

r15 proposals passed draft-check 6/6 + source-claim audits (evidence refs/modes unchanged r14→r15).
TeX preserves r15 numbers/conditions/scopes verbatim (except recorded P1/t1 cross-ref wording).
No new numbers, dates, prices, licenses, or efficacy claims introduced in synthesis/community/frontmatter/notes;
those sections restate article facts with cites to the same public entries.

## 4. No formal-only mapping

Coverage details describe concrete TeX substance per requirement (not blanket assertions);
synthesis derives axes from actual 6 articles (provision vs performance, total/active,
shipped vs promised, detection vs scope, vendor-measured conditions);
community section limits itself where grounds are thin (no forced articleization).

## 5. r15 JSON ↔ TeX correspondence recorded

See `r15-tex-correspondence-r15.md` (per-package section mapping + P1/t1 naturalization + added structure).

## 6. No internal metadata on reader surface

Lexical lint (Frozen Core patterns) on `main.tex`, all 10 section files, `references.bib`:
0 BLOCKING findings (verified by scan; manifest build also enforces lint).
Coverage/requirement details linted separately: 0 BLOCKING.
Manifest metadata (paths/SHAs, authored_by, ledger correction refs) lives outside TeX;
reader body contains no repo paths, Evidence IDs, revision history, or agent logs.
Public ledger filename mention follows W40 released precedent (bare filename only, no `sources/`/`surveys/` prefix).

## 7. Manifest bound to exact TeX bytes

Manifest `primary_source.sha256` binds `main.tex` exact bytes + byte_count;
`supporting_files` bind `references.bib`, `jgaisurvey.sty`, and 10 section files
with SHA + byte_count. Any TeX rebuild requires manifest rebuild (new SHA);
current manifest validates against current disk bytes.

## Required reader requirements

- `FINAL_SYNTHESIS` → Section 7 (85-week-in-review.tex) with concrete cross-article総括.
- `WEEKLY_COMMUNITY_MOVEMENT` → Section 8 (80-community-movement.tex) + public ledger (14 rows).

## Open (not claimed)

- Independent semantic review (READER_PIPELINE_INDEPENDENCE etc.): NOT performed, NOT passed.
- Reader-surface gate (formal): NOT passed (requires independent semantic authority).
- Visual review of exact PDF: pending PDF build (Phase E) + independent review.

(End of file)
