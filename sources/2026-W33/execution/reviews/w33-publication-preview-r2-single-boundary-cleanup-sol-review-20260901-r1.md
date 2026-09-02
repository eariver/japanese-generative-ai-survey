# W33 Publication Preview r2 Single-Boundary Cleanup — Sol Review

- Issue: `2026-W33`
- Gate: `PUBLICATION_PREVIEW`
- Human review revision: `2`
- Controlling issue: `#433`
- Reviewed branch: `weekly/2026-W33-v2-work`
- Reviewed repository HEAD: `6361b6ea2066e6c64007587511d591dbfbcfa73b`
- Reviewed candidate payload SHA-256: `d8edb38eb1c84476e24219caeae7a1fd4fac5bb3b39f1c0cee3bf9940b1e312b`
- Reviewed PDF SHA-256: `13dbc6b2637e5097f82962e6e23413865e04c9a4ae5be035414d594ae19c18ce`
- Human decision authority: `sources/2026-W33/execution/reviews/w33-owner-publication-preview-decision-20260901-r2.md`
- Sol disposition: `ACCEPT_HUMAN_REQUEST_CHANGES / SINGLE_READER_BOUNDARY_FINDING / EXACT_ONE_LINE_REPAIR_AUTHORIZED / RETURN_TO_PUBLICATION_PREVIEW`

## Finding verification

Sol independently confirmed the sole remaining finding in the current canonical `references.bib` entry for `voicedesigner`:

`Paper metadata; baseline and evaluation details remain unresolved in the accepted capture.`

The phrase `accepted capture` is internal acquisition/Evidence-selection language. It is not needed to communicate the technical uncertainty to the reader and violates the publication-boundary intent retained from Issue #433.

The Owner's proposed replacement is semantically faithful and does not strengthen the claim:

`Paper metadata; baseline and evaluation details could not be confirmed from the available primary material.`

This keeps the unresolved baseline/evaluation boundary while expressing it entirely in reader-facing source language.

## Scope decision

This is not a drafting, architecture, evidence, or layout defect.

The Owner explicitly accepted the current:

- 11-page structure;
- two-column body layout;
- visual flow;
- substantive technical sections;
- Week in Review synthesis;
- earlier Issue #433 publication transformation repairs.

Therefore Sol authorizes exactly one substantive source edit: the specified `voicedesigner` bibliography note replacement.

No other reader prose, section source, bibliography record, heading, ordering, table, callout/boundary box, or layout edit is authorized except machine-generated hash/provenance changes required by the rebuilt exact PDF and canonical validation records.

## Canonical rollback boundary

The current lifecycle is `RELEASE_CANDIDATE` with Publication Preview pending.

Because the Human decision is `REQUEST_CHANGES` and the exact bibliography/PDF/validation/candidate bytes will change, the canonical revision must be materialized with:

- operation: `REQUEST_PUBLICATION_PREVIEW_REVISION`
- expected revision: `2`
- regeneration boundary: `DRAFT_COMPLETE`

The canonical rollback must occur before the bibliography edit and must invalidate the current validation/candidate authority according to Core semantics.

Architecture, Evidence, Selection, Draft Packages/Results, Weekly Profile Synthesis, and approved substantive reader structure are not regeneration authority for this repair and must remain unchanged.

## Required validation after the edit

After the exact one-line bibliography replacement:

1. build through the existing canonical Weekly CI workflow;
2. require the final TeX warning gate to PASS;
3. obtain the exact CI PDF artifact and independently verify its bundled checksum and SHA-256;
4. pin those exact PDF bytes to `surveys/weekly/2026-W33/main.pdf`;
5. confirm page count remains `11` unless the exact one-line bibliography change causes an unavoidable line-flow change; any page-count change must be reported and must still satisfy the hard maximum;
6. visually review all pages, with specific attention to the References pages;
7. fail-closed scan the reader-facing TeX/PDF/References for inappropriate production use of:
   - `candidate`
   - `Evidence identity`
   - `Profile Completeness`
   - `LIMITED`
   - `Screening`
   - `HOLD_OUT`
   - `DROP`
   - `materiality`
   - `SOCIAL_OBSERVATION`
   - `Core v2`
   - `accepted capture`
   - `Grok_X_SourseIntake`;
8. regenerate the current Reader Manifest, deterministic authorities, Quality Regression Bundle, Semantic/Editorial Review, and Exact-PDF Visual Review from the new source/PDF bytes;
9. require canonical `DRAFT_COMPLETE` stage validation PASS.

## Larger deterministic unit authorization

Because the content change is exact, bounded, and Human-specified, a second Sol semantic stop before the next Human Gate is not required if and only if all guards above PASS and no unauthorized source changes occur.

Luna may in the same bounded task:

1. materialize Publication Preview revision 2 and rollback to `DRAFT_COMPLETE`;
2. apply the exact one-line bibliography repair;
3. rebuild and validate the exact new reader/PDF authority;
4. advance exactly once `DRAFT_COMPLETE -> VALIDATED_DRAFT`;
5. generate and validate a replacement canonical Publication Candidate from only the new current authority;
6. advance exactly once `VALIDATED_DRAFT -> RELEASE_CANDIDATE`;
7. materialize the next pending Publication Preview Human Gate;
8. stop.

Any canonical validation failure, page/layout regression, internal-language recurrence, or unexpected source diff outside the authorized surface requires fail-closed stop before lifecycle re-advancement.

## Human authority boundary

The next Publication Preview decision remains Owner-owned.

Luna must not record `APPROVED`, `REQUEST_CHANGES`, or `REJECT` for the next preview, must not freeze/release/merge, and must not close Issue #433.
