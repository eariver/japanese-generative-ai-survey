# Survey Production execution index — SP001

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/SP001/production-state.json`.

## Current authority

- Issue / edition: `SP001`
- Research Profile: `THEMATIC`
- Publication Profile: `LONGFORM_SPECIAL`
- Work branch: `special/SP001-v2-work`
- Start-of-run reviewed `main`: `80345ab46dfa9d0fdd5657bed844197efd6e337c`
- Run started: `2026-08-24T17:24:00Z`
- Requested stop at initialization: `ARCHITECTURE_REVIEW`
- Production Profile: `sources/SP001/production-profile.json`
- Production State: `sources/SP001/production-state.json`
- Current State SHA-256: `8d83099133289450c644624da310f2492d10484794ad6089cbbd85659274e653`
- Current lifecycle: `ARCHITECTURE_ESTABLISHED`
- Current terminal reason: `none`
- Current next action: `stage:drafting-synthesis`
- Production execution status: paused for reviewed shared-Core repair before Drafting

## Human Gates

- Architecture Review: `approved` (revision r2)
- Exact reviewed repository commit: `3be63ff5a79a274b1d99f061c1ef8cf80c803d62`
- Active approval: `sources/SP001/gates/architecture-approval.json`
- Review index: `sources/SP001/gates/review-index.json`
- Immutable/current review record: `sources/SP001/gates/reviews/architecture-r2.json`
- Publication Preview: `pending`

## Publication Candidate

- Current Human review target: none yet
- Candidate SHA-256: none
- PDF SHA-256: none

## Grok/X

- Profile applicability policy: `CHATGPT_DECIDES`
- Latest Drive task-file path/reference: none recorded
- Latest result disposition: none recorded

## Deviations

- Architecture r1 received an explicit Human `REQUEST_CHANGES` to add a final synthesis/conclusion package. The allowed `SELECTION_COMPLETE` regeneration boundary was used; Discovery, Screening, Evidence, completeness, and Selection remained accepted.
- Revised six-package Architecture was Core-validated and then explicitly approved as Architecture revision r2.

## Shared Core defects

- `defects/core-v2-cross-package-synthesis-draft-input-2026-08-25.md` — Architecture permits a legitimate final package with no direct candidate destinations, while the pre-repair Draft builder rejects all zero-placement packages. SP001 is paused after Architecture approval; generic Core repair is PR #465.

## Sessions

- `sessions/postintegration-sp001-20260825-r2.md`

## Final disposition

`IN_PROGRESS / PAUSED_FOR_SHARED_CORE_REPAIR`
