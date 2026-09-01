# W33 Owner Publication Preview Decision — r2

- Issue: `2026-W33`
- Gate: `PUBLICATION_PREVIEW`
- Revision: `2`
- Reviewed branch: `weekly/2026-W33-v2-work`
- Reviewed repository HEAD: `6361b6ea2066e6c64007587511d591dbfbcfa73b`
- Reviewed Publication Candidate: `sources/2026-W33/publication/v2/publication-candidate-v2.json`
- Reviewed candidate payload SHA-256: `d8edb38eb1c84476e24219caeae7a1fd4fac5bb3b39f1c0cee3bf9940b1e312b`
- Reviewed exact PDF SHA-256: `13dbc6b2637e5097f82962e6e23413865e04c9a4ae5be035414d594ae19c18ce`
- Reviewed PDF pages: `11`
- Reviewed PDF bytes: `274435`
- Decision: `REQUEST_CHANGES`
- Remaining findings: `1`
- Regeneration boundary: `DRAFT_COMPLETE`
- Controlling issue: `#433`
- Decision recorded: `2026-09-01` JST

## Human Review finding

The Owner reviewed Publication Preview r2 and found the edition otherwise at PASS quality.

Explicitly accepted and frozen for this revision:

- current 11-page structure;
- normal two-column body layout;
- visual layout / clipping / overlap / page flow;
- Serving & Runtime technical depth;
- Inference Systems Deep Dive;
- Agent Reliability;
- Multimodal & Media;
- independent Week in Review synthesis;
- prior Issue #433 cleanup for `candidate`, `Profile Completeness`, Evidence/Issue-Synthesis production language, and raw `Grok_X_SourseIntake` path;
- no padding toward the 18-page soft target.

The only remaining reader-facing defect is in References entry `[27]` / `voicedesigner`:

`baseline and evaluation details remain unresolved in the accepted capture.`

The phrase `accepted capture` exposes internal acquisition/Evidence-selection provenance and is not appropriate reader-facing publication language.

## Required exact correction

Replace only the following sentence fragment in `surveys/weekly/2026-W33/references.bib`:

From:

`Paper metadata; baseline and evaluation details remain unresolved in the accepted capture.`

To:

`Paper metadata; baseline and evaluation details could not be confirmed from the available primary material.`

No other substantive reader prose, section content, section ordering, layout, table, claim-boundary box, Week in Review content, or bibliography entry may be rewritten as part of this Human request.

## Regression guard

After rebuilding, the reader-facing PDF and References must be checked to ensure the following internal production vocabulary has not reappeared as production metadata:

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
- `Grok_X_SourseIntake`

Natural-language occurrences unrelated to production metadata must not be removed mechanically; the requirement is semantic publication-boundary cleanliness.

## Regeneration boundary rationale

`DRAFT_COMPLETE` is the minimum correct canonical rollback boundary because the exact bibliography bytes, compiled PDF bytes, validation authorities, validation checkpoint, Publication Candidate, and Release Candidate state are all bound to the rejected r2 publication bytes.

Architecture, Selection, Evidence, seven Draft Packages/Results, Weekly Profile Synthesis, and substantive reader structure/content remain valid and must not be regenerated.

## Required end state

After the exact one-line bibliography repair, canonical CI rebuild, exact-PDF verification, all-page review, fail-closed publication-boundary scan, validation-authority regeneration, canonical validation, replacement Publication Candidate generation, and canonical re-advancement, stop at the next Publication Preview Human Gate.

The next gate must remain `pending` with approval provenance `null`.

No Human approval is granted by this decision. Freeze, release, merge, and Issue #433 closure are forbidden before the next explicit Owner decision.
