# Automotive E/E Publication Preview revision plan

Status: **ACTIVE REVISION PLAN / experiment-only**

Target: `SP-automotive-ee-architecture-2023-2026` Publication Preview v0.1

Branch: `experiment/automotive-ee-architecture-special`

This plan is intentionally recorded **before** changing the reader-facing preview. It combines the v0.1 self-review with lessons from prior Japanese Generative AI Survey review Issues, including closed Issues. The production AI survey remains authoritative; all remediation described here is confined to the Automotive experiment unless separately generalized and reviewed later.

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

### Prior AI-survey review Issues checked

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
| #140 | Repeated bibliography boilerplate should not inflate References | Remove repeated per-entry generic notes from the reader-facing bibliography while retaining provenance in machine-readable inputs |
| #139 | Generic non-source-specific fallback summaries must not reach publication | Continue to fail closed; all retained prose must be source-specific or explicit synthesis |
| #191 | Subject/component/variant/property binding must be explicit; bag-of-tokens extraction can silently misattribute properties | Re-audit P01-P08 at semantic level, especially release-series chronology and adjacent component/runtime/platform claims |
| #166 | Broad intake success is not coverage completeness; material discoveries must be tracked through to reader-facing disposition | Treat AUTOSAR and OEM/Tier1 gaps as coverage work, not merely as footnoted acquisition failures |
| #95 | Retrospective Special needs a cross-article final synthesis before References | Preserve P08 as the explicit final body section and keep it in the TOC |
| #153 / #272 | Chronology/source traceability should be compact and not duplicate full evidence cards | Do not add a duplicate evidence appendix merely to expose provenance; keep References/source mapping compact |
| #271 | Empty reader-facing wrappers/tables must be suppressed | Do not create empty Technical Notes/figure/table sections as padding |

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

- Replace ambiguous `draft_sha256` with typed hashes:
  - `submitted_body_sha256`
  - `accepted_article_draft_sha256` where applicable
  - `draft_package_sha256`
  - `article_prompt_sha256`
  - rendered TeX/Bib hashes
  - final PDF hash
- Include immutable Draft Packages (which contain the Evidence Cards), the exact Automotive drafting prompt, and validator/renderer provenance needed for revalidation, or explicitly declare repository-bound dependencies.
- Generate checksum lists using relative paths only.
- State clearly whether the bundle is self-contained or repository-bound.

### R2 — Remove internal workflow vocabulary from reader-facing PDF — HIGH

Rewrite cover/front matter/end notes so that:

- `Source Intake` -> `source collection` / `収集`
- `Screening` -> `一次選別` or omitted where unnecessary
- `Evidence Task/Card` -> `検証済み資料` / `一次資料・研究資料`
- `Candidate Matrix`, `CANDIDATE`, `HOLD`, `INSPECT_MORE` -> repository-only provenance
- `VERIFIED/PARTIAL/TIMING_UNRESOLVED` -> reader-facing descriptions of what is confirmed vs. unresolved

Preserve Claim Boundary semantics and actual unresolved gaps.

### R3 — Add reader-facing navigation and restore Special mixed-layout identity — HIGH

- Add a real TOC after the front-matter scope note.
- Restrict TOC depth to main article sections and the final synthesis.
- Use local mixed layout:
  - full-width section heading and standfirst;
  - two-column normal narrative;
  - full-width diagrams/tables or heavy claim-boundary blocks where useful;
  - full-width References.
- Avoid global `\twocolumn` / `\onecolumn` switches that introduce structural page holes.

### R4 — Domain coverage gap-fill — HIGH

Re-open research only for explicitly identified gaps:

1. **AUTOSAR current architecture/specification surface** relevant to Adaptive Platform, service/data/API boundaries, and 2023-2026 evolution.
2. **OEM/Tier1 implementation signals** for zonal/central compute, vehicle OS/platform, network/service architecture, or validation/deployment structure.

Requirements:

- prioritize official first-party sources;
- verify exact subject/property ownership;
- classify vendor/project statements as claims rather than independent proof;
- record unresolved normative-text access boundaries;
- do not silently inject new facts into existing accepted drafts.

If new supporting Evidence materially changes an Architecture package's input set, record an experiment-only Architecture coverage amendment and revalidate before redrafting the affected section.

### R5 — Semantic subject/property audit — HIGH

Audit P01-P08 against Issue #191 failure modes:

- comparator values are not attributed to the subject;
- family-level properties are not flattened across variants with different properties;
- model/runtime/stack/API/platform responsibilities remain separate;
- release-series features are tied to the correct release/event;
- vendor/project claims remain visibly attributed;
- P08 does not strengthen the combined meaning of its source claims beyond supported editorial inference.

### R6 — Add explanatory architecture visuals — MEDIUM-HIGH

Add deterministic, source-bounded diagrams rather than decorative imagery. At minimum:

1. `責務境界の再配置` overview: physical/zonal I/O, compute, network, service/data, lifecycle, assurance.
2. Network/service responsibility view: TSN Ethernet / 10BASE-T1S / CAN XL and service/data/runtime layers, expressed as survey synthesis rather than normative topology.

Every figure must be clearly labelled as either source-supported fact or editorial synthesis.

### R7 — Improve bibliography presentation without losing provenance — MEDIUM

- Preserve source title, organization/authors where available, date, URL, and access date.
- Remove repeated generic per-entry notes from the PDF-facing bibliography.
- Keep the full source/evidence provenance in structured inputs and source bundle.
- Do not merge distinct source records in a way that makes exact evidence mapping lossy.

### R8 — Period, metadata, typography, and visual preflight — MEDIUM/LOW

- Verify all structured period labels against the edition manifest.
- Set PDF title/subject metadata.
- Reduce awkward English hyphenation without making layout brittle.
- Check bullets/list markers for duplication.
- Render every page and inspect:
  - clipping/overlap;
  - blank/sparse pages;
  - orphan Claim Boundary fragments;
  - TOC population and page references;
  - two-column balance;
  - long title/URL wrapping;
  - final P08 -> References transition.

## 4. Items intentionally preserved as PASS

- The central thesis: 2023-2026 Automotive E/E change is best understood as redistribution of responsibility boundaries, not `centralize everything`.
- P08 is the final body synthesis before References, satisfying the Architecture approval condition and the retrospective-synthesis lesson from #95.
- Reader-facing References already preserve meaningful source titles, satisfying the core failure addressed by #78.
- There is no hard rendered-page floor; the preview will not be padded toward 48 pages, consistent with #123.
- Unknown normative details remain unknown; inaccessible ISO/AUTOSAR material will not be reconstructed from memory.

## 5. Exit criteria for revised Publication Preview

A new Preview may be presented to the human gate only when all of the following are true:

- [ ] typed provenance hashes are internally consistent;
- [ ] source bundle reproducibility boundary is explicit and testable;
- [ ] reader-facing internal workflow/enums scan returns zero unintended matches;
- [ ] TOC is populated and section-level only;
- [ ] Special mixed-layout policy is restored without sparse/blank regressions;
- [ ] AUTOSAR/OEM/Tier1 coverage has been gap-filled or an explicit coverage-blocking limitation remains and is accepted as such;
- [ ] P01-P08 pass structural validation after any evidence amendments;
- [ ] P01-P08 pass a semantic subject/property/claim-strength audit;
- [ ] figures are source-bounded and non-decorative;
- [ ] bibliography is compact enough for reader use while exact provenance remains lossless;
- [ ] period consistency and PDF metadata checks pass;
- [ ] all rendered pages pass visual review;
- [ ] P08 remains the final body section immediately before References;
- [ ] production AI pipeline remains unchanged.

Publication Preview approval itself remains a Human Gate.
