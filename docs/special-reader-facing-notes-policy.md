# Special Reader-Facing Technical Notes Policy

Status: active operational policy for future Special editions  
Origin: Issues #49, #50, #54 and #55 after SP-2026-M06 / SP-2026-M05 Preview review  
Authority: operationalizes `docs/editorial-style-guide.md` without weakening Evidence provenance.

## Purpose

Technical Notes are a reader-facing technical appendix, not a dump of normalized Evidence records. Their job is to preserve source correspondence and attribution boundaries while remaining readable as Japanese technical prose.

## Language rule

- Claim and limitation **sentence structure is Japanese by default**, including `一次情報で確認できる事実` entries.
- Model names, API names, benchmark names, framework names, paper-defined terms and precision-critical technical terminology may remain English.
- `Vendor claim`, `Project claim`, `Author claim` and similar attribution-class labels may remain as explicit claim classes.
- A full English source sentence is not acceptable as the normal reader-facing explanation merely because the underlying Evidence was normalized in English.
- If an English original is intentionally quoted, identify it as an original quotation and keep it distinct from the Japanese reader-facing summary.

## Reader-facing taxonomy rule

Repository provenance keeps the canonical artifact/event enums unchanged. The PDF-facing layer maps them to reader-facing labels.

- Raw schema identifiers such as `OTHER`, `OFFICIAL_PUBLICATION`, `PRODUCT_UPDATE`, `MODEL_RELEASE`, and TeX-escaped variants must not appear as magazine labels.
- Common event kinds are rendered as labels such as `公式公開`, `製品更新`, `モデル公開`, `Agent公開`, `Framework公開`, `API更新`, and `論文公開`.
- `OTHER` is never shown literally. It falls back to a meaningful reader-level category such as `公式情報`, with explicit artifact-specific overrides where a stronger semantic label is known.
- The same mapping is used in `Theme at a glance` and the corresponding detail card.
- Semantic overrides take precedence over an upstream coarse taxonomy when necessary for reader clarity. For example, an evaluation playbook is rendered as `評価ガイダンス`, not `安全性事象`.

The reader-facing label is presentation metadata only and does not mutate the Evidence card taxonomy.

## Provenance rule

The English normalized Evidence text remains immutable. Japanese reader-facing wording is stored in a separate SHA-bound editorial artifact:

`sources/<ISSUE>/editorial/technical-notes-ja-v0.1.json`

Each summary entry binds to:

- `evidence_task_id`;
- claim / limitation item ID;
- the exact normalized source text;
- SHA-256 of that source text;
- the Japanese reader-facing summary.

The renderer verifies the source-text SHA before replacing PDF-facing text. It never writes the Japanese summary back into the Evidence card or Draft Package. For historical working revisions where repository-only Evidence IDs were already stripped from the PDF-facing TeX, the repair path may bind a card by its exact canonical artifact title, but only if that title resolves to exactly one card in the package.

## Technical Notes break-quality rule

Technical Notes cards remain breakable. A whole-card `samepage`, aggressive chapter-level `Needspace`, or forced page break is not the default remedy because it can recreate the blank-page regressions tracked in Issue #40.

Instead:

- keep the `一次資料` heading together with its URL list as a compact local block;
- apply strong paragraph widow/orphan penalties inside the breakable card so a limitation does not leave only its last line on the next page;
- allow a large card to span pages when necessary;
- verify the actual rendered PDF so a page does not begin with only a URL or a tiny card tail.

## Workflow

1. Complete Article Draft so the selected Draft Packages are fixed.
2. Run **Prepare Special Technical Notes Japanese summaries**.
3. Fill every `text_ja` field with natural Japanese while preserving precision-critical technical terms; set artifact status to `READY`.
4. Run source expansion. The expansion workflow:
   - renders selected Evidence;
   - verifies and applies the SHA-bound Japanese summary layer;
   - removes repository-only IDs / pipeline terminology;
   - maps machine artifact/event enums to reader-facing labels;
   - applies localized Technical Notes break-quality controls;
   - verifies all claim/limitation reader-facing lines contain Japanese sentence structure;
   - rejects raw enum re-exposure;
   - verifies the issue period against the Special edition manifest.
5. PDF build repeats the language/taxonomy and period checks before compilation.
6. Human Visual Review remains responsible for actual readability and layout, including Technical Notes continuation quality.

No new Human Gate is introduced. The existing Visual Review covers the resulting reader-facing appendix.

## Period consistency

Issue identity and coverage labels are not inferred from copied prose. `Retrospective scope` is derived from `specials/<slug>/edition.json` coverage and is checked as a structured field.

Do **not** globally ban references to adjacent months. Article chronology may legitimately discuss pre-window or post-window events. Period validation therefore targets only issue-identity fields such as survey setup coverage and the `Retrospective scope` declaration.

## Post-release errata

A frozen PDF is not silently replaced for a non-critical editorial correction. Record the erratum separately and retain the original frozen PDF SHA. A corrected PDF requires an explicit post-release correction policy and distinct provenance; it is not the default response to an erratum.
