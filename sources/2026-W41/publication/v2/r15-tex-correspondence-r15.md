# W41 r15 → TeX correspondence (body mapping, not byte equality)

Date: 2026-10-14 JST
Primary source: `surveys/weekly/2026-W41/main.tex` (inputs 10 section files)
Method: deterministic generator from r15 proposal bytes + hand-authored synthesis/community/frontmatter/notes.
All r15 reader-facing blocks preserved; magazine structure added (kickers, wideflow, subsections, tables, notes, cites).

## Article mapping (all blocks adopted)

- P1 (16 blocks) → `sections/10-frontier-models.tex` (headline→wideflow, deck→wideflow muted, h1/h2→subsections, p1–p12→paragraphs with cites, t1→2-col table + caption, n1→technicalnote).
- P2 (17) → `sections/20-agent-infra.tex` (same pattern; h1–h4→subsections; no tables).
- P3 (22) → `sections/30-open-weights.tex` (h1–h4→subsections; t1→2-col availability table).
- P4 (7) → `sections/40-image-model.tex` (h1→subsection; p1–p5→paragraphs; n1→technicalnote).
- P5 (19) → `sections/50-provenance.tex` (h1/h2→subsections; p1–p13→paragraphs; t2→2-col table; t3→3-col table; t1→2-col table; n1→technicalnote).
- P6 (13) → `sections/60-safety-science.tex` (h1–h3→subsections; p1–p9→paragraphs; n1→technicalnote).

## Intentional naturalization (meaning preserved, recorded)

- P1/t1 free line `詳細はP2のインフラ記事で扱う。` → TeX `詳細はエージェント基盤の記事で扱う。`
  Reason: remove internal package identifier from reader surface; target article unchanged
  (Section 2). No numbers, conditions, or scope changed.

## Added magazine structure (no content loss)

- `sections/00-frontmatter.tex`: cover-stage contents, This Week boxes, reading guide (W41 dates/axes; no W40 values reused).
- `sections/85-week-in-review.tex`: FINAL_SYNTHESIS from actual 6 articles (6 enumerated changes + joint significance + next observations).
- `sections/80-community-movement.tex`: WEEKLY_COMMUNITY_MOVEMENT from Grok/X + DailyX + Evidence (14-link ledger split, negative space, announcement vs re-attention).
- `sections/99-source-notes.tex`: consulted sources, temporal/vendor/community boundaries, non-elevated items.
- `references.bib`: 20 public entries (titles/URLs/dates/access dates); all TeX cites resolve.
- `community-observation-ledger.md`: 14-row public manifest (12 ordinary + 2 late-breaking).

## Fidelity checks

- Generator fidelity: every r15 block first-40-char fragment found in TeX (6/6 packages, reported in prep log).
- Numbers/units/dates preserved: FPR/200/400, synonym triple, 8-bench values with points/%, MoE triples, Elo 1050±14, 4K-token note, timestamps, pricing splits, scale pair.
- Must-cover substance preserved (see `coverage-map-r15.json` + QA record).

(End of file)
