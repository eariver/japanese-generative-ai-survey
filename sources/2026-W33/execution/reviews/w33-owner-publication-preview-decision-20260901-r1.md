# W33 Owner Publication Preview Decision — r1

- Issue: `2026-W33`
- Gate: `PUBLICATION_PREVIEW`
- Revision: `1`
- Reviewed candidate repository commit: `e372578bb8c3a0664a4145887c136ea1f335ce6d`
- Reviewed Publication Candidate: `sources/2026-W33/publication/v2/publication-candidate-v2.json`
- Reviewed exact PDF SHA-256: `4febb800d879b91ad2cd4c721fbb56c9db2d2555454595e236f71450e82868d2`
- Decision: `REQUEST_CHANGES`
- Regeneration boundary: `DRAFT_COMPLETE`
- Review reference: repository Issue `#433`
- Decision recorded: `2026-09-01` JST

## Owner direction

The Owner explicitly directed that Issue #433 be re-opened as the controlling publication-quality review concern for the current W33 Publication Candidate, that the current candidate be re-reviewed against that Issue, and that the remaining problems be corrected by Luna/Work.

This is an explicit Human `REQUEST_CHANGES` decision. Publication Preview is not approved.

## Required correction

The reader-facing publication must satisfy the publication-transformation principles and acceptance criteria in Issue #433, in particular:

1. Remove internal production/editorial/pipeline vocabulary from public reader prose and reader-facing source notes. Internal concepts such as `candidate`, `Profile Completeness`, `HOLD`, `REJECT`, Evidence identity, Issue Synthesis, placement/must-cover mechanics, internal chronology/index bookkeeping, Core workflow terminology, and similar repository-production language must not appear as publication prose.
2. Preserve reader-useful claim-strength limitations, but express them naturally in terms of what public primary material, project releases, paper authors, or community observation can and cannot establish.
3. Rewrite Weekly Community Movement so it reports the actual accepted community movement/interest visible in the bounded observation, rather than describing the policy for how community material is treated.
4. Remove raw/internal intake paths from reader-facing References. Do not invent a replacement public URL when none exists.
5. Keep the stronger technical substance already present in the current Serving, inference-systems, Agent Reliability, and Multimodal sections. Do not regress these sections into process summaries.
6. Re-review the frontier/access, cyber/governance, Week in Review, front matter, Source Notes, and any other affected reader text for Issue #433 leakage.
7. Rebuild the exact PDF through the canonical Weekly CI path and perform a new all-page visual review and semantic/editorial review against Issue #433.

## Boundary rationale

`DRAFT_COMPLETE` is the minimum correct regeneration boundary.

The approved Architecture, selected Evidence, seven Draft Packages/Results, and Weekly Profile Synthesis remain valid. The defect is in the reader/publication transformation and the validation authorities bound to that transformation. Therefore Evidence, Selection, Architecture, and Draft semantic authority must not be regenerated or changed.

`VALIDATED_DRAFT` is too late because the current validation checkpoint is bound to the rejected reader source/PDF/review bytes and must be invalidated before a replacement reader publication can be reviewed.

## Stop condition

After the replacement reader/publication validation candidate is rebuilt and fully validated from `DRAFT_COMPLETE`, stop for Sol re-review. Do not advance the replacement candidate to `VALIDATED_DRAFT`, do not recreate a Publication Candidate, and do not return to Publication Preview until Sol confirms that Issue #433 is actually resolved.
