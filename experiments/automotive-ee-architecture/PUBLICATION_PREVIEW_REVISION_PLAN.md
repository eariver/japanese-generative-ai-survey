# Automotive E/E Publication Preview revision plan

Status: **EXECUTED FOR v0.2 / experiment-only / Human Gate pending**

Target: `SP-automotive-ee-architecture-2023-2026` Publication Preview v0.1 -> v0.2

Branch: `experiment/automotive-ee-architecture-special`

This plan was intentionally recorded at commit `b1e91e2e4f0fe681717033e9c5ed7a53199efbf4` **before** changing the reader-facing preview. It combines the v0.1 self-review with lessons from prior Japanese Generative AI Survey review Issues, including closed Issues. The production AI survey remains authoritative; all remediation described here is confined to the Automotive experiment unless separately generalized and reviewed later.

## 1. Inputs to this revision

### v0.1 self-review

The first Automotive E/E preview established a coherent architecture narrative, but the following defects were identified:

- preview bundle per-draft hash semantics are wrong/ambiguous;
- internal pipeline vocabulary leaks into reader-facing pages;
- AUTOSAR and OEM/Tier1 implementation coverage is too weak for a final Automotive E/E survey;
- the issue has no architecture diagrams;
- References consume a disproportionate share of the PDF;
- structural draft validation is not a substitute for semantic claim review;
- the source bundle is not fully self-contained for revalidation;
- checksum paths are environment-specific;
- PDF metadata is incomplete;
- some two-column English hyphenation is visually awkward.

### Prior AI-survey review Issues checked before implementation

The following prior review findings materially apply to this preview:

| Issue | Prior lesson | Automotive implication |
|---|---|---|
| #9 | Published prose, claim/source notes, and repository provenance are separate reader layers | Remove `Source Intake`, `Evidence Task`, `Candidate Matrix`, selection states, and production workflow terminology from normal reader-facing prose |
| #40 | Reader-facing Technical Notes must not expose production-model metadata; full-page visual QA is required | Keep provenance in repository/source bundle; show only reader-useful methodology and claim boundaries in the PDF |
| #49 | Scope/period labels must be derived from edition coverage, not copied prose | Verify cover, front matter, synthesis, and metadata consistently say 2023-08-18 through 2026-08-18 |
| #50 | Reader-facing claim/limitation prose should be natural Japanese while precise technical terms may remain English | Keep technical English terms, but ensure explanatory boundary prose is Japanese-first |
| #54 | Raw internal enums/taxonomy must not leak into publication labels | Remove `VERIFIED`, `PARTIAL`, `CANDIDATE`, `HOLD`, `INSPECT_MORE`, `TIMING_UNRESOLVED` from reader-facing prose unless translated into meaningful methodological language |
| #55 / #84 | Page breaks must not leave box/source tails or isolated fragments | Re-render every page and inspect section/claim-boundary transitions after mixed-layout changes |
| #77 | A visible TOC heading without usable entries is a publication defect | Automotive currently has no reader-facing TOC at all; add a real section-level TOC |
| #79 / #106 | Special narrative body uses mixed layout: full-width heading/standfirst + two-column narrative, full-width synthesis/reference material as needed | Replace global `\twocolumn` layout with local mixed layout; do not let page-count considerations choose layout |
| #78 | References must retain meaningful source titles/identity metadata | Current Automotive bibliography already has titles; preserve this property |
| #122 | TOC must not expose repetitive internal/subsection headings or create sparse continuation pages | Limit Automotive TOC to main sections, including final synthesis; do not list internal subheads |
| #123 | Page count is a soft editorial target, not a hard floor; never pad to reach it | Keep the preview at its natural length after quality fixes; do not inflate toward the Architecture 48-page planning envelope |
| #140 | Repeated bibliography boilerplate should not inflate References | Remove repeated generic per-entry notes from the reader-facing bibliography while retaining provenance in machine-readable inputs |
| #139 | Generic non-source-specific fallback summaries must not reach publication | Continue to fail closed; all retained prose must be source-specific or explicit synthesis |
| #191 | Subject/component/variant/property binding must be explicit; bag-of-tokens extraction can silently misattribute properties | Re-audit P01-P08 at semantic level, especially release-series chronology and adjacent component/runtime/platform claims |
| #166 | Broad intake success is not coverage completeness; material discoveries must be tracked through to reader-facing disposition | Treat AUTOSAR and OEM/Tier1 gaps as coverage work, not merely as footnoted acquisition failures |
| #95 | Retrospective Special needs a cross-article final synthesis before References | Preserve P08 as the explicit final body section and keep it in the TOC |
| #153 / #272 | Chronology/source traceability should be compact and not duplicate full evidence cards | Do not add a duplicate evidence appendix merely to expose provenance; keep References/source mapping compact |
| #271 | Empty reader-facing wrappers/tables must be suppressed | Do not create empty Technical Notes/figure/table sections as padding |

### Supplemental closed-Issue scan during implementation

The broader closed-Issue scan continued while the revision was being implemented. Two additional applicable failure modes were found and added to the preflight before the candidate was declared complete:

- **#172** — reader-facing normalization must never mutate URL/path/code identifiers. Added exact bibliography-key/URL-byte and PDF-link-annotation checks.
- **#110** — source/list text must not combine with renderer markers to create double bullets. Added a duplicate U+2022 bullet scan and visual list check.

These are recorded as a plan amendment rather than retroactively pretending they were in the original pre-change list.

## 2. Revision principles

1. **Repair provenance before prose.** Typed hashes and reproducibility semantics must be unambiguous before the revised bundle is called a Publication Preview.
2. **Reader-facing language is not pipeline language.** The PDF may explain source quality and uncertainty, but not expose production state-machine vocabulary.
3. **Coverage is a domain gate.** A credible Automotive E/E survey must include adequate standards/specification and industry implementation evidence, not only papers/OSS/consortium material.
4. **No insecure retrieval shortcuts.** AUTOSAR/standards gap-fill may use legitimate alternate official routes, but TLS verification and access controls are never bypassed.
5. **No page-count padding.** 48 pages remains the Architecture planning envelope, not a rendered-page quota.
6. **The approved thesis and P08 placement remain stable.** The revision may strengthen supporting evidence and presentation, but does not replace the responsibility-boundary thesis or move References ahead of P08.
7. **No production AI pipeline changes.** Any helper, source profile, publication source, or audit added for this repair stays experiment-owned.

## 3. Ordered remediation work

### R1 — Repair preview provenance and source-bundle contract — BLOCKER

- Replace ambiguous `draft_sha256` with typed hashes such as `accepted_article_draft_sha256`, `draft_package_sha256`, prompt/source hashes, and final PDF hash.
- Keep exact review snapshots in the artifact bundle; keep repository-side dependencies explicit instead of inventing missing historical per-body bytes.
- Generate checksum lists using relative paths only.
- State clearly whether a path belongs to the review artifact or repository.

### R2 — Remove internal workflow vocabulary from reader-facing PDF — HIGH

Rewrite cover/front matter/end notes so that pipeline states and internal enums remain repository provenance while the PDF uses reader-facing source/claim/uncertainty language.

### R3 — Add reader-facing navigation and restore Special mixed-layout identity — HIGH

- Add a real TOC after the front-matter scope note.
- Restrict TOC depth to main article sections and the final synthesis.
- Use local mixed layout: full-width section heading/standfirst, two-column narrative, full-width diagrams/heavy boundaries, full-width References.
- Avoid page-count-driven global layout changes.

### R4 — Domain coverage gap-fill — HIGH

Re-open research only for:

1. AUTOSAR current architecture/specification surface relevant to Adaptive Platform, service/data/API boundaries, and 2023-2026 evolution.
2. OEM/Tier1 implementation signals for zonal/central compute, vehicle platform/lifecycle, and network/service architecture.

Use official first-party sources, preserve vendor/project attribution, keep normative-text gaps unresolved, and record any supporting-evidence amendment separately from baseline validation.

### R5 — Semantic subject/property audit — HIGH

Audit P01-P08 against #191: no comparator/adjacent-product contamination, no family-level flattening, explicit component/runtime/platform ownership, release-bound chronology, preserved attribution, and restrained P08 synthesis.

### R6 — Add explanatory architecture visuals — MEDIUM-HIGH

Add deterministic source-bounded/editorial-synthesis diagrams for responsibility boundaries and network/service responsibility. Do not use decorative or pseudo-normative topology art.

### R7 — Improve bibliography presentation without losing provenance — MEDIUM

Preserve title/organization/date/URL/access date, remove repeated generic notes from the PDF-facing bibliography, and keep exact provenance lossless in structured audit data.

### R8 — Period, metadata, typography, and visual preflight — MEDIUM/LOW

Verify period labels, PDF metadata, hyphenation, list markers, canonical URLs, clipping/overlap, blank/sparse pages, orphan boundaries, TOC, mixed columns, long URLs, and P08 -> References ordering.

## 4. Items intentionally preserved as PASS

- The responsibility-boundary thesis.
- P08 as the final body synthesis before References.
- Meaningful source titles in References.
- No rendered-page hard floor or padding.
- Unknown normative detail remains unknown.

## 5. Exit criteria for revised Publication Preview

The v0.2 candidate may return to the Human Gate only when typed provenance, reproducibility, reader-facing vocabulary, TOC/mixed layout, domain gap-fill, structural baseline validation, semantic audit, visuals, compact lossless bibliography, period/metadata checks, full-page visual QA, canonical URL integrity, list-marker integrity, P08 placement, and the production-AI boundary all pass.

Publication Preview approval itself remains a Human Gate.
