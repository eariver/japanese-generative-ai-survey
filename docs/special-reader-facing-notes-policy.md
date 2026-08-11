# Special Reader-Facing Technical Notes Policy

Status: active operational policy for future Special editions  
Origin: Issues #49 and #50 after SP-2026-M06  
Authority: operationalizes `docs/editorial-style-guide.md` without weakening Evidence provenance.

## Purpose

Technical Notes are a reader-facing technical appendix, not a dump of normalized Evidence records. Their job is to preserve source correspondence and attribution boundaries while remaining readable as Japanese technical prose.

## Language rule

- Claim and limitation **sentence structure is Japanese by default**.
- Model names, API names, benchmark names, framework names, paper-defined terms and precision-critical technical terminology may remain English.
- `Vendor claim`, `Project claim`, `Author claim` and similar attribution-class labels may remain as explicit claim classes.
- A full English source sentence is not acceptable as the normal reader-facing explanation merely because the underlying Evidence was normalized in English.
- If an English original is intentionally quoted, identify it as an original quotation and keep it distinct from the Japanese reader-facing summary.

## Provenance rule

The English normalized Evidence text remains immutable. Japanese reader-facing wording is stored in a separate SHA-bound editorial artifact:

`sources/<ISSUE>/editorial/technical-notes-ja-v0.1.json`

Each summary entry binds to:

- `evidence_task_id`;
- claim / limitation item ID;
- the exact normalized source text;
- SHA-256 of that source text;
- the Japanese reader-facing summary.

The renderer verifies the source-text SHA before replacing PDF-facing text. It never writes the Japanese summary back into the Evidence card or Draft Package.

## Workflow

1. Complete Article Draft so the selected Draft Packages are fixed.
2. Run **Prepare Special Technical Notes Japanese summaries**.
3. Fill every `text_ja` field with natural Japanese while preserving precision-critical technical terms; set artifact status to `READY`.
4. Run source expansion. The expansion workflow:
   - renders selected Evidence;
   - verifies and applies the SHA-bound Japanese summary layer;
   - removes repository-only IDs / pipeline terminology;
   - verifies all claim/limitation reader-facing lines contain Japanese sentence structure;
   - verifies the issue period against the Special edition manifest.
5. PDF build repeats the language and period checks before compilation.
6. Human Visual Review remains responsible for actual readability and layout.

No new Human Gate is introduced. The existing Visual Review covers the resulting reader-facing appendix.

## Period consistency

Issue identity and coverage labels are not inferred from copied prose. `Retrospective scope` is derived from `specials/<slug>/edition.json` coverage and is checked as a structured field.

Do **not** globally ban references to adjacent months. Article chronology may legitimately discuss pre-window or post-window events. Period validation therefore targets only issue-identity fields such as survey setup coverage and the `Retrospective scope` declaration.

## Post-release errata

A frozen PDF is not silently replaced for a non-critical editorial correction. Record the erratum separately and retain the original frozen PDF SHA. A corrected PDF requires an explicit post-release correction policy and distinct provenance; it is not the default response to an erratum.
