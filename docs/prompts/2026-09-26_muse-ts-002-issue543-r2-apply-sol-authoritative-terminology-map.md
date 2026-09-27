# Muse execution — TS-002 Issue #543 r2 apply Sol authoritative terminology map

Status: `EXECUTION_AUTHORITY / TERMINOLOGY_APPLICATION_ONLY / NO_EDITORIAL_DISCRETION`
Date: 2026-09-26 JST

## 1. Mission

Apply the Sol-authored terminology decisions in:

`sources/SP-beyond-text-2026/execution/terminology-issue543/sol-authoritative-terminology-map-r2-20260926.md`

across the existing TS-002 reader-facing manuscript, regenerate the exact Publication Preview candidate, and stop at the Human Publication Preview gate.

This is **not** a research/editorial judgment task. Sol has already made the terminology, semantic, and source-binding decisions.

Muse MUST NOT create alternative translations, reinterpret source meaning, broaden a mapping to a different semantic context, or make a new citation decision.

## 2. Launch guard

The launch message from Sol supplies the exact remote work HEAD/tree and reviewed main HEAD/tree corresponding to the commit that contains this prompt.

At start, use remote authority (`git ls-remote origin` plus read-only fetch/object inspection), not stale local refs.

Confirm all four values exactly:

- remote work HEAD == Sol launch Expected remote HEAD
- remote work tree == Sol launch Expected remote Tree
- remote main HEAD == Sol launch Reviewed main HEAD
- remote main tree == Sol launch Expected main Tree

If any remote value differs, perform zero writes and report expected/actual values.

If only local refs are stale but remote matches, fast-forward/synchronize the existing workspace without creating a branch, then continue.

## 3. Existing Human Gate

Issue #543's Human Publication Preview `REQUEST_CHANGES` has already been recorded canonically as the current revision authority.

Do NOT create another Human decision or a new Publication Preview revision merely to execute this repair.

If the current Core state cannot legally re-enter publication-local repair under the already-recorded Issue #543 revision, stop and report the Core constraint. Do not synthesize Human authority.

Architecture approval remains approved.

## 4. Normative mapping

The following file is normative and must be treated as an immutable editorial decision surface:

`sources/SP-beyond-text-2026/execution/terminology-issue543/sol-authoritative-terminology-map-r2-20260926.md`

For each mapping:

1. locate every occurrence that matches the semantic context stated by Sol;
2. apply the specified reader-facing term/rewrite;
3. permit only minimal Japanese grammatical inflection needed to fit the surrounding sentence;
4. preserve the Sol-defined canonical English identity where the map requires it;
5. preserve the stated citation/source binding.

Do NOT replace a term when its occurrence belongs to a different semantic context than the map defines.

If uncertain whether an occurrence is covered, do not decide. Record it for Sol review.

## 5. One authorized citation-binding correction

The only pre-authorized citation-binding repair is `SOL-CIT-001` in the authoritative map:

- EnCodec-specific boundary stays on `btd007`.
- DAC **Balanced data sampling** statement binds to `btd008`.

Apply exactly that semantic split.

No other citation-key addition/removal/rebinding is authorized.

If any other apparent source-binding defect is discovered, do not fix it. Record it as `CANDIDATE_FOR_SOL_REVIEW` and leave the manuscript unchanged at that location.

## 6. No autonomous terminology repair

Muse may perform broad scanning for QA/discovery, but MUST NOT autonomously repair newly found terminology.

For every suspicious term not covered by the Sol map, create/update:

`sources/SP-beyond-text-2026/execution/terminology-issue543/muse-candidates-for-sol-review-r2.md`

Each candidate must include:

- exact term;
- complete reader-facing sentence;
- section/subsection;
- citation key / Evidence ID;
- canonical English term only if it is directly visible in an already-consumed source;
- reason the wording looks suspicious.

Do NOT include a proposed final Japanese replacement. That is a Sol editorial decision.

Finding new candidates is not itself a failure; changing them without Sol authority is a failure.

## 7. Existing terminology ledger

Update both canonical views:

`sources/SP-beyond-text-2026/execution/terminology-issue543/terminology-decision-ledger.json`

`sources/SP-beyond-text-2026/execution/terminology-issue543/terminology-decision-ledger.md`

Requirements:

- preserve the r1 decision history;
- add Sol authoritative r2 decisions with provenance `SOL_AUTHORITATIVE_R2`;
- mark prior ESCALATE entries resolved when the Sol map resolves them;
- document `SOL-CIT-001` as an explicit citation-invariant exception;
- keep JSON and Markdown semantically identical;
- do not convert new Muse-discovered candidates into REPLACE/RETAIN decisions; list those only in the candidate file pending Sol review.

## 8. Frozen content

Do not alter:

- Discovery;
- Screening;
- Evidence;
- Materiality;
- Completeness;
- Selection;
- Architecture;
- Issue #529 semantic depth;
- claim boundaries except grammar needed to apply an exact Sol mapping;
- numerical values or units;
- experimental conditions;
- vendor attribution;
- closed-system boundaries;
- section ordering;
- section/subsection architecture.

`references.bib` must remain byte-identical.

No new authority/source may be added.

## 9. Semantic invariants

Compare pre/post repair:

- section/subsection order;
- labels;
- numerical token/value semantics;
- unit semantics;
- Evidence status boundaries;
- PARTIAL / NEEDS_MORE / HOLD boundaries;
- vendor attribution;
- Issue #529 depth content;
- 139/139 bibliography coverage.

For citations:

- report the exact `\autocite{...}` sequence before/after;
- identify the only intentional delta caused by `SOL-CIT-001`;
- all other citation deltas are blockers.

## 10. Regression scans

Re-run all Issue #533 and #539 frozen-regression scans so previously removed mistranslations do not return.

Also scan all left-hand-side prohibited/residual forms enumerated in the Sol authoritative map.

The scan must include variants, not only literal exact strings.

## 11. Broad QA scan

After applying the map, perform broad reader-facing scanning twice:

1. `main.tex` source surface;
2. exact rendered PDF text surface.

Purpose: discover unrecognized suspicious translation artifacts.

This scan is discovery-only for unmapped terms. Do not modify them.

Every new item goes to `muse-candidates-for-sol-review-r2.md`.

## 12. PDF regeneration and visual QA

Regenerate the exact PDF through the canonical Special pipeline.

Required:

- deterministic manuscript validation;
- semantic/editorial validation;
- citation validation;
- terminology regression validation;
- exact PDF build;
- rendered-text scan;
- all-page visual regression;
- clipping/overflow/broken-glyph/blank-page check;
- bibliography rendering regression.

Pay special attention to:

- canonical English technical names;
- metric labels/tables;
- long component names;
- two-column line endings;
- video/speech tables;
- capstone product names;
- bibliography transition pages.

Page-count change alone is not a failure.

## 13. Repository rules

Work only on the existing branch named in the launch message.

Forbidden:

- new branch;
- fallback/repair/review branch;
- force push;
- reset;
- rebase;
- history rewrite.

Use normal commits and non-force fast-forward push only.

## 14. Stop condition

Normal completion state:

`PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`

or the exact current-Core equivalent.

Issue #543 remains OPEN for Sol final readback.

Do NOT:

- approve the Publication Preview;
- Freeze;
- Release;
- merge;
- create a release record.

## 15. Completion report

Report at minimum:

- starting/final work HEAD + tree;
- main guard;
- Core gate before/after;
- files changed;
- number of Sol mappings applied;
- previous ESCALATE resolution status;
- `SOL-CIT-001` exact citation delta;
- any `CANDIDATE_FOR_SOL_REVIEW` entries;
- Issue #533/#539 regression result;
- semantic invariants;
- 139/139 bibliography coverage;
- `references.bib` byte identity;
- exact PDF page count;
- PDF SHA-256;
- Candidate SHA-256;
- CI run/result;
- rendered-PDF broad-scan result;
- all-page visual regression result;
- final Core state and Human Gate.

Muse is an executor/validator for this pass, not the terminology editor.
