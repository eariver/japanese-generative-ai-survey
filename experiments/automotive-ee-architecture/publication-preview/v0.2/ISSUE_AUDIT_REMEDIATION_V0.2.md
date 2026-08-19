# Publication Preview v0.2 — prior Issue audit and remediation report

Status: **remediated candidate / Human Publication Preview Gate still pending**

Issue: `SP-automotive-ee-architecture-2023-2026`

This report records how the Automotive E/E Publication Preview was checked against review lessons accumulated in prior Japanese Generative AI Survey Issues, including closed Issues. It does not change production AI-survey policy. The implementation described here is confined to the experimental Automotive branch/source.

## Result summary

The v0.1 self-review findings and prior-Issue lessons were applied to produce v0.2. The revised preview keeps the approved Architecture v0.3 thesis and the required end-of-body synthesis P08, but repairs publication-facing provenance, reader language, navigation/layout, domain coverage, subject/property attribution, figures, bibliography presentation, metadata, and visual QA.

Baseline P01–P08 structured drafts remain the same validated baseline inputs. Publication-quality coverage gaps discovered after Architecture Review are recorded as a separate experiment-only supporting-source amendment rather than being falsely represented as outputs of the unchanged Article Draft validator.

## Issue-by-Issue disposition

| Issue | Applicable lesson | v0.2 disposition |
|---|---|---|
| #9 | Separate reader prose from workflow/provenance vocabulary | **PASS** — reader PDF scan has zero unintended `Evidence Task`, `Candidate Matrix`, `Draft Package`, selection-state and related internal workflow terms |
| #40 | Reader-facing technical appendix/methodology; full-page visual QA | **PASS** — front matter and source notes explain uncertainty in publication language; repository-specific provenance remains in structured bundle/audits |
| #49 | Coverage/period consistency | **PASS** — cover/front matter/metadata use 2023-08-18 through 2026-08-18 consistently; no copied month-specific retrospective wording |
| #50 | Japanese-first reader-facing claim/limitation prose | **PASS** — explanatory boundary prose is Japanese-first while preserving precise English technical terms |
| #54 | Do not publish raw internal enums | **PASS** — `VERIFIED`, `PARTIAL`, `CANDIDATE`, `HOLD`, `INSPECT_MORE`, `TIMING_UNRESOLVED` and similar internal states are absent from reader-facing PDF |
| #55 / #84 | Avoid orphan/tail-only page breaks | **PASS by visual preflight** — no blank wrapper page or page-top source/claim tail found in the revised 15-page render |
| #77 | TOC must be populated | **PASS** — real section-level TOC appears on p.2 with the final synthesis and Source Notes included |
| #79 / #106 | Special mixed layout | **PASS** — full-width heading/standfirst with local two-column narrative; full-width figures/boundaries/references where appropriate; no global page-count-driven one-column fallback |
| #78 | References retain meaningful source identity | **PASS** — bibliography entries retain title, organization/authors where available, date, URL and access date |
| #122 | TOC hierarchy must stay reader-facing and compact | **PASS** — printed TOC is main-section level only and fits naturally on p.2; subsection/internal headings are not printed |
| #123 | No hard page floor or padding | **PASS** — rendered length remains 15 pages; no padding, blank page, one-column inflation or forced spacing was added to approach the 48-page planning envelope |
| #140 | Remove repeated generic bibliography boilerplate | **PASS** — repeated per-entry generic `note` field is suppressed in the reader-facing bibliography; References contract from five pages to three without losing source identity |
| #139 | No generic source-unspecific fallback text | **PASS** — known generic fallback phrases scan to zero; supplemental paragraphs are source-specific and cited |
| #191 | Explicit subject/component/property binding | **PASS with separate semantic audit** — BMW/Volvo/Continental, AUTOSAR AP/CAPI, S-CORE, Mercedes MB.OS, VSS release evolution, middleware/platform components remain explicitly separated; no bag-of-tokens cross-entity flattening is used in the supplement |
| #172 | Never mutate URL/path/code identifiers during reader normalization | **PASS** — all reader-facing bibliography URL keys derive from exact URL bytes; URL fields contain no localization mutation; all 54 publication bibliography URLs are present as exact PDF link annotation targets |
| #110 | Avoid double bullets | **PASS** — duplicated U+2022 list marker scan returns zero |
| #166 | Broad intake does not prove domain coverage completeness | **REMEDIATED FOR PREVIEW** — official AUTOSAR Adaptive/R24/R25/CAPI material and official BMW/Mercedes/Volvo/Continental signals were added. ISO 11898-1:2024 normative text remains explicitly unresolved rather than reconstructed |
| #95 | Retrospective final synthesis before References | **PASS** — P08 remains the final technical body section and References follow it |
| #153 / #272 | Traceability without duplicate evidence-card dumps | **PASS / not directly applicable** — no duplicate Detailed Chronology appendix was introduced; source mapping stays in citations/bibliography/structured provenance |
| #271 | Suppress empty wrappers/tables | **PASS** — no empty Technical Notes or Theme wrapper is emitted |
| #128 | Do not replace thematic synthesis with page-count padding | **Principle applied** — this is a Thematic Special, not a Half-year Special; only the no-padding/cross-layer-synthesis lesson is reused |

## Concrete v0.2 repairs

### Provenance / reproducibility

- Replaced ambiguous generic per-draft hash semantics with typed fields in `preview-manifest.json`.
- The bundled `accepted_article_draft_sha256` values now match the exact structured-draft bytes in the bundle.
- Draft Package path/SHA, prompt path/SHA, validation report path/SHA, publication source SHA, supplemental-source audit, and PDF SHA are explicit.
- `reproducibility-boundary.json` declares the bundle as **repository-bound with self-contained publication source** rather than claiming false standalone revalidation.
- `source-files-sha256.txt` uses relative paths only.
- Exact per-body submitted interactive bytes are not invented; the historical aggregate payload SHA is retained separately.

### Reader-facing editorial repair

- Removed pipeline state/selection vocabulary from cover, front matter, body boundaries, and source notes.
- Rephrased methodology as source collection, public-source verification, organization/project claim, research result, and unresolved boundary.
- Added a concise `why this Special` reading frame and one-line thesis.

### Navigation and layout

- Added section-level TOC.
- Restored the Special mixed-layout identity using local `multicols` article bodies.
- Kept P08 as an explicit full-width final synthesis before Source Notes/References.

### Domain coverage

Added nine official first-party supplemental sources to close the most serious self-review gap:

- AUTOSAR Adaptive Platform public architecture;
- AUTOSAR R24-11 and R25-11 release-event surfaces;
- AUTOSAR CAPI and 2026 CAPI contribution announcement;
- BMW Neue Klasse zonal / high-performance-compute description;
- Mercedes-Benz CLA / MB.OS production lifecycle description;
- Volvo EX90 core-compute / OTA product description;
- Continental HPC / Zone Control Unit architecture description.

These additions are recorded in `supplemental-source-audit-v0.2.json` and `architecture-coverage-amendment-v0.3a.json`. Vendor/project statements remain attributed. No access-control/TLS bypass is used. ISO 11898-1:2024 normative text remains unresolved.

### Semantic claim audit

`semantic-claim-audit-v0.2.md` checks Issue #191-type failure modes across P01–P08, with special attention to:

- OEM-specific architecture statements;
- VSS release-series wording;
- S-CORE vs. AUTOSAR CAPI ecosystem separation;
- MB.OS lifecycle evidence vs. in-vehicle topology claims;
- editorial synthesis language in P08.

### Figures

Added two deterministic editorial-synthesis figures:

1. responsibility-boundary overview: physical/zonal I/O, compute, network, service/data, lifecycle, assurance;
2. network/service responsibility view: central/HPC, zonal control, TSN/Ethernet backbone, 10BASE-T1S/CAN XL edge/sub-backbone roles.

Both are explicitly labelled as editorial concept diagrams rather than normative/OEM topology diagrams.

### References / metadata / typography

- Reader-facing References preserve meaningful titles and canonical URLs.
- Repeated generic bibliography notes are suppressed; exact provenance remains in the structured inputs.
- One uncited publication-bibliography record was removed from the PDF-facing `.bib`; the underlying source remains recoverable through repository provenance.
- PDF title, subject, keywords, and A4 metadata are populated.
- Fixed `SOURCE_DATE_EPOCH` / `FORCE_SOURCE_DATE` build metadata was added; two independent clean builds produced byte-identical PDFs.
- English hyphenation penalties/emergency stretch were adjusted without changing the page-count contract.

## Remaining explicit limitations

- ISO 11898-1:2024 normative text was not inspected; CAN XL normative details are not reconstructed.
- OEM/Tier1 sources are first-party disclosures. They strengthen production/implementation coverage but do not independently prove interoperability, safety certification, architecture uniformity, or fleet-wide performance.
- Supplemental post-Architecture facts are separately source-bound and semantically audited; they are not relabelled as having passed the unchanged baseline Article Draft validator.
- Publication Preview Human approval remains pending. No Freeze, merge, or public Release is authorized.

## Gate recommendation

**v0.2 is suitable to return to the Publication Preview Human Gate**, subject to final full-page render inspection and exact artifact hashing. It is not authorized for Freeze or production merge without explicit human approval.
