# SP-2026-M05 HANDOFF

Status: `RELEASE_CANDIDATE`

## Gates

- Raw Sources Preserved: passed
- Candidate Inventory: passed
- Evidence Normalized: passed
- Candidate Selection: passed
- Issue Architecture: passed
- Article Draft: passed
- Claim & Chronology Validation: passed
- LaTeX Build: passed
- **Human Visual Review: pending**
- **Freeze: pending**

No Human Visual Review, Freeze, merge, publication, or release approval is inferred by this checkpoint.

## Granularity review

May was explicitly compared with the June and July Specials before Selection was advanced. The May proposal was retained rather than reduced: `FEATURE_CORE=3` plus `SECTION_CORE=12` gives 15 core Evidence items, while Supporting Evidence and Paper Watch are folded into thematic packages. This matches the June Special's editorial grain more closely than forcing May down to July's smaller Evidence count.

## Current Preview candidate

- Source version: `v0.5`
- Source manifest: `surveys/special/2026-M05/revisions/v0.5/source-manifest.json`
- Source manifest SHA-256: `e8bd3c4c217543048ff9eefc0c92af46000a7fad2a0e2a0522e71cb08c7d0163`
- Layout mode: `balanced-multicol-adaptive-spacing-with-may-chronology-width-fix`
- Build workflow run: `31517394457`
- PDF page count: `33`
- PDF SHA-256: `f215a8e7e634a19ed05a0f642df4d505018cd96f2cb8c38649639da01fe830ba`
- TeX log gate: clean (`[]`)
- Allowed page range: 32–40

## Pre-Human render QA

All 33 pages were rendered and inspected before presenting the Preview.

Resolved before Human Visual Review:
- v0.2's single-column/source-card pacing and structural chapter whitespace were replaced by balanced multicol layout.
- The frontmatter retrospective scope typo (`2026年7月`) was corrected to `2026年5月`.
- The otherwise sparse TOC tail is used by a reader-facing May chronology derived only from already-selected Evidence and only day-level confirmed Events.
- Later chapter starts use adaptive spacing rather than forced clear pages.
- Long English two-column subsection headings were shortened for display; formal artifact titles remain in Technical Notes.
- v0.3 Underfull hbox warnings were eliminated.
- v0.4 chronology-table Overfull hbox warnings were eliminated by the v0.5 width-only revision.

Final v0.5 inspection found no clipping, overlap, broken glyph, undefined citation/reference, overfull/underfull hbox, missing-character issue, isolated Claim Boundary page, or structural blank page. Frontmatter chronology and later chapter transitions remain readable; final bibliography whitespace is natural end-of-document whitespace.

The next Human Gate is **Preview / Human Visual Review**. Freeze remains a later, separate Human Gate.
