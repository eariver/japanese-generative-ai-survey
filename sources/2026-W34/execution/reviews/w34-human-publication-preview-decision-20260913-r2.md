# W34 Human Publication Preview decision record — REQUEST_CHANGES r2 (Human-provided)

Date transmitted: 2026-09-13 JST via GitHub Issue #491 (created 2026-09-13T09:31:05Z; exact Human decision time not transmitted beyond issue timestamp; canonical recording instant below is execution-side, not Human instant)
Gate: `PUBLICATION_PREVIEW`
Decision: `REQUEST_CHANGES` (revision 2; second Publication Preview review for W34)
Reviewed repository commit: `c7faf207515e7429dd74abd5adaf2962725587ef`
Reviewed surface: exact current Publication Candidate `d0af4c9ca917ce3a51d58fcd213846c4d49cb8d3a9334501484ec798970de429` and PDF `1818e8669963a0d965966b6d2f4a0ef4cc8df2bdf9ed129c64fa96be7c28ed84` (12 pages, 338707 bytes)

## Requested changes (Human-provided, Issue #491 scope only)

1. Remove internal production/lifecycle wording from reader-facing claim boundaries while preserving editorial scope semantics (observed: `regional processing is NOT part of this package after Selection r2; it belongs to Package 4` in `sections/20-agent-workflows.tex` claimboundary).
2. Reconcile rendered `visited on`/`urldate` dates with canonical retrieval/capture provenance (observed: blanket `2026-08-21` vs later capture chronology, e.g. Grok Bot Aug 21 event / Aug 26 page re-date / Sep 8 capture).

No additional Human requests. No approval. Issue #491 remains open as review reference.

## Trace summary (read-only Phase A before recording)

- Defect 1: PDF -> `sections/20-agent-workflows.tex` claimboundary tail -> reader-manuscript wrapper (no prose) -> `draft/v2/packages/w34-collaborative-agent-workflows-retrieval/draft-result.json` CLAIM_BOUNDARY + `boundary_dispositions[22]` -> `draft-package.json` boundaries[22] -> `architecture-v2.json` package `w34-collaborative-agent-workflows-retrieval` boundaries[] (single occurrence; Selection r2 = c045 moved to model-economics Package 4, drafting_order 4; factually correct internally). Classification: `PUBLICATION_AUTHORING_LOCAL` — Architecture/Draft-Package internal wording correct as audit; reader-facing TeX authoring copied it verbatim instead of normalizing (precedent: HOLD-label TeX normalization without Draft change). Architecture semantics preserved.
- Defect 2: all 41 `references.bib` `urldate=2026-08-21` (weekly window_end/cutoff `2026-08-21T18:00:00-04:00`) vs active Evidence `647cde46…` `sources[].accessed_at=2026-09-08…` + `temporal.observed_at=2026-09-08T15:34:01Z` + `official-provenance.jsonl` CAPTURED `2026-09-08…`. 41/41 MISMATCH, 0 MATCH/AMBIGUOUS/NO-DATE. c066: event Aug 21 (X `2026-08-21T17:29:36Z`) / page Aug 26 re-date / capture `2026-09-08T14:52:53Z`. Canonical field: Evidence `sources[].accessed_at`. Shared generator `survey_weekly_semantic_publication_v2.py:_window/_bib_text` blanket-dates from cutoff; recorded as separate Core maintenance note, W34 repaired edition-locally at publication authoring layer to match Evidence (no Shared Core edit in this task).

## Regeneration boundary

`DRAFT_COMPLETE` — minimal valid Publication Preview boundary invalidating TeX/bib/manuscript/PDF/candidate/validation. Draft/Architecture/Evidence/Selection bytes and Architecture approval preserved. Previous r1 used same boundary for TeX-only normalization.

After correction, regenerate publication-facing artifacts and return to a fresh Publication Preview Human Gate for direct PDF review.

## Recording provenance

This file is an execution-side transcription of the Human-provided decision conveyed via Issue #491. It does not generate, modify, or reinterpret the Human decision. Reviewed-by identity for the canonical review record follows project convention (`EaRiver`).

Markers: `HUMAN_PUBLICATION_PREVIEW_REQUEST_CHANGES_R2_RECORDED`.
