# Muse execution prompt — TS-002 Publication Preview r2 bibliography repair + semantic-depth audit

Status: `EXECUTION_AUTHORITY / PUBLICATION_PREVIEW_R1_REQUEST_CHANGES / BOUNDED_R2`

Date: `2026-09-26 JST`

## 1. Mission

Continue `SP-beyond-text-2026` on the existing branch only.

The current Publication Preview r1 is **not rejected for being 68 pages**. Sol review found that the manuscript is dense and substantively mechanism-led, but Human Publication Preview approval must wait for:

1. reader-facing bibliography rendering repair;
2. removal/normalization of generic internal provenance boilerplate from the bibliography;
3. a bounded semantic-depth audit against the active 43-transition ledger and 14 approved Architecture packages;
4. evidence-driven targeted expansion only where that audit proves supported content was under-explained;
5. a fresh validated PDF and a fresh Publication Preview r2 stop.

Do not expand mechanically to 80 pages. Do not pad. Page count is an observation, not the acceptance criterion.

## 2. Mandatory starting guards

Repository:
`eariver/japanese-generative-ai-survey`

Branch:
`special/beyond-text-2026-work`

Exact Starting SHA:
`c48f35368f7253976bca04e69603b94b48607949`

Expected Starting Tree:
`e5a9f4d21d19126063c1de2d8d7a5883c4c04d4c`

Reviewed main SHA:
`0bbb02b3c5963403860897daec2feaf61e82589a`

Expected main Tree:
`e4ddde5ed5059d303b818f54e27204369b256bcb`

Before any write, verify read-only:

- remote work HEAD == Exact Starting SHA
- remote work tree == Expected Starting Tree
- remote main HEAD == Reviewed main SHA
- remote main tree == Expected main Tree

If any mismatch occurs, make zero writes and report expected/actual values.

No new/fallback/repair/review branch.
No force push, reset, rebase, or history rewrite.

## 3. Review authority

Read first:

`sources/SP-beyond-text-2026/execution/sol-publication-preview-review-r1-20260926.md`

Also treat as fixed authorities:

- Human-approved Architecture gate and approval records
- active sanitized Evidence result-set
- active 43-entry transition ledger
- active Architecture v2 (14 packages)
- current Publication Preview r1 manuscript/PDF

Human Architecture approval remains valid. Do not reopen or alter Architecture semantics.

## 4. Page-plan interpretation

Do not treat `80 pages` as a quota.

The approved Architecture planning note contains an arithmetic inconsistency: the listed chapter allocations plus front/back matter sum to 94, not the stated 84. Preserve the approved Architecture as historical authority; do not rewrite it simply to repair arithmetic after Human approval.

Record the discrepancy in the r2 execution report and use semantic completeness, not page-count restoration, as the decision rule.

The r1 PDF is 68 pages with approximately 6 front-matter pages, 51 substantive body pages, and 11 reference pages. The Sol spot review found the body visually dense and non-padded.

## 5. Bibliography repair — mandatory blocker

Current reader-facing bibliography author rendering is malformed in places because display-style author strings are being parsed as BibLaTeX name lists. Examples include raw `bibinitperiod` leakage and mangled initials.

Repair bibliography generation deterministically.

### 5.1 Author handling

If a record has a proper structured BibLaTeX author list already available from authoritative edition data, use it.

If edition data only carries a display string such as:

- `Kingma & Welling`
- `van den Oord et al.`
- `OpenAI`
- `Google DeepMind`

then preserve that string as a literal BibLaTeX author value so it renders as intended rather than being parsed into initials/name parts.

Do not invent missing full-author metadata and do not start broad bibliographic research merely to expand author lists.

Validation must scan rendered PDF text for at least:

- `bibinitperiod`
- `bibnamedelima`
- raw BibLaTeX macro names
- obviously mangled author-name artefacts caused by display-string parsing

and require zero occurrences.

### 5.2 Reader-facing note cleanup

Generic internal pipeline boilerplate should not be repeated in every VERIFIED bibliography entry.

Remove/normalize reader-visible boilerplate such as:

- `Source class PRIMARY_* as bound in Evidence`
- `Primary locator as rebound in 2026-09-24 provenance repair where applicable`

from ordinary VERIFIED entries unless a specific provenance caveat is genuinely necessary for the reader.

Preserve provenance in repository Evidence/execution artifacts.

PARTIAL / NEEDS_MORE limitations may remain in the publication bibliography only where they materially tell the reader what may or may not be claimed. Rewrite those notes in reader-facing language, not internal pipeline vocabulary.

Do not lose canonical URLs or dates.

## 6. Semantic-depth audit — mandatory before any expansion

Create:

`sources/SP-beyond-text-2026/execution/publication-preview-r2-depth-audit/semantic-depth-delta-audit.json`

and

`sources/SP-beyond-text-2026/execution/publication-preview-r2-depth-audit/semantic-depth-delta-audit.md`

Audit all 43 active transition-ledger entries against the actual reader-facing manuscript.

For every transition record, capture at least:

- transition_id
- destination package/chapter
- supporting discovery/evidence IDs
- manuscript section/subsection
- explicit bottleneck present? yes/no/not-supported
- representation change present? yes/no/not-applicable/not-supported
- architecture change present? yes/no/not-applicable/not-supported
- objective/process change present? yes/no/not-applicable/not-supported
- sampling/inference change present? yes/no/not-applicable/not-supported
- conditioning/control change present? yes/no/not-applicable/not-supported
- source-supported improvement present? yes/no/not-supported
- trade-off/new failure mode present? yes/no/not-supported
- successor inheritance/displacement present? yes/no/not-supported
- at least one source-specific mechanism detail present? yes/no
- at least one source-specific condition/metric/ablation detail present where Evidence supports it? yes/no/not-supported
- manuscript treatment classification: `SUBSTANTIVE`, `COMPRESSED_BUT_SUFFICIENT`, `UNDER_EXPLAINED`, `BOUNDARY_ONLY`
- repair action if UNDER_EXPLAINED

A transition is not satisfied merely because its source IDs are cited.

## 7. Priority anti-thinness packages

Perform an additional package-level audit for the five chapters whose actual page span was much smaller than the nominal planning allocation:

- `arch-representation`
- `arch-paradigms`
- `arch-speech`
- `arch-music`
- `arch-video`

For each, compare:

- approved package purpose
- primary/supporting candidates
- mapped transition entries
- source-local Evidence detail
- actual manuscript prose

Explicitly answer:

1. Does the chapter explain mechanisms, not merely name systems?
2. Does it distinguish architecture / objective / inference where relevant?
3. Does it include source-supported quantitative or experimental conditions where available?
4. Does it explain trade-offs/failure modes rather than only improvements?
5. Does it explain what the successor inherited or displaced?
6. Are any major primary sources reduced to one-line mentions despite richer VERIFIED Evidence?
7. Are important modality-specific concepts compressed because of page-count pressure?

## 8. Expansion rule

Do not add prose merely because r1 is 68 pages.

Expansion is permitted and required only for `UNDER_EXPLAINED` findings where active Evidence already supports deeper explanation.

When expanding:

- use only active Evidence / transition synthesis / approved Architecture;
- do not rerun Discovery or broad research;
- do not infer closed-system internals;
- preserve PARTIAL/NEEDS_MORE/LOW_SIGNAL boundaries;
- prefer mechanism explanation, experimental conditions, trade-offs, and historical inheritance over extra product lists;
- do not enlarge capstones or X reception merely to add pages;
- do not duplicate front-matter caveats in every chapter;
- do not add generic prose that could apply to any model.

If the audit finds no meaningful under-explanation, keep the body substantially unchanged and state that the sub-80-page result is semantically sufficient.

There is no minimum page count for r2.

## 9. Reader-facing prose QA

After any textual changes, scan for:

- internal Discovery/Evidence IDs leaked into prose
- internal terms such as `PRIMARY_PAPER`, `as bound in Evidence`, raw result-set hashes, pipeline-stage vocabulary
- stale provenance-repair future language
- TODO/FIXME placeholders
- unsupported superlatives/rankings
- vendor claims written as independent facts
- cross-condition metric comparisons

Keep current good boundaries intact.

## 10. PDF build and visual QA

Generate a fresh `main.pdf` from the final r2 source.

Run normal CI/build validators and visual inspection.

At minimum inspect rendered pages from:

- cover/front matter
- representation
- paradigms
- speech
- music
- video
- runtime/evaluation table pages
- capstones
- synthesis
- beginning/middle/end of references

Check:

- no clipping/overflow
- no broken glyphs
- no raw TeX/BibLaTeX macro text
- tables/callouts within margins
- readable bibliography author formatting
- no systematic blank pages

Record final page count, but do not grade the manuscript by page count alone.

## 11. Invariants

Preserve unless genuinely affected by reader-facing bibliography/draft repair:

- Discovery 139
- Screening decisions
- Evidence status set 126 VERIFIED / 8 PARTIAL / 5 NEEDS_MORE
- Materiality/Completeness/Selection semantics
- selected 134 / HOLD 5
- all 43 transition entries
- Human Architecture approval
- 14 Architecture packages
- closed-system non-inference boundary
- X reception-only boundary
- shared Core unchanged

No Freeze/Release/publication merge/release-record.

## 12. Required r2 execution report

Create a session report under:

`sources/SP-beyond-text-2026/execution/sessions/`

Record at least:

- starting guard values
- bibliography repair method
- number of bibliography author fields changed
- generic provenance notes removed/retained
- 43-transition audit counts by `SUBSTANTIVE / COMPRESSED_BUT_SUFFICIENT / UNDER_EXPLAINED / BOUNDARY_ONLY`
- package-level audit results for representation/paradigms/speech/music/video
- exact sections expanded, if any
- before/after manuscript character or word proxy
- before/after page count
- bibliography page count
- citation count and uncited/undefined count
- PDF visual QA results
- all validator receipts
- final remote HEAD/tree

## 13. Stop condition

Normal stop:

`PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION_R2`

or the exact current-Core equivalent.

Do not approve Publication Preview on behalf of Human Owner.
Do not enter Freeze or Release.
