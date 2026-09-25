# TS-002 Sol Publication Preview Review r1

Status: `REQUEST_CHANGES / BIBLIOGRAPHY_RENDER_REPAIR_AND_DEPTH_AUDIT_REQUIRED`

Date: 2026-09-26 JST

Repository: `eariver/japanese-generative-ai-survey`
Branch: `special/beyond-text-2026-work`
Reviewed remote HEAD: `0f9a5a418403ccae6558a3effa329b6be3e36aa9`
Reviewed remote tree: `f95da6eaf644a65f50230570ddd6a6ce8d818cb9`
Reviewed main HEAD: `0bbb02b3c5963403860897daec2feaf61e82589a`
Reviewed main tree: `e4ddde5ed5059d303b818f54e27204369b256bcb`
Reviewed PDF: `surveys/special/beyond-text-2026/main.pdf`, 68 pages, CI artifact SHA256 `f7dd6f999f860e41ba00ddef8bce2ef215c4b586acef2506e13835f2cd992985`.

## Decision

The 68-page count is **not itself a blocker**. The rendered manuscript is dense, two-column technical prose rather than a padded or sparse layout, and spot checks of representation, paradigms, speech, music, video, runtime, evaluation, capstones, synthesis, and references show that the approved mechanism-led structure is materially present.

However, Publication Preview r1 is not approved yet for two reasons:

1. reader-facing bibliography rendering contains malformed author output / raw macro artefacts and internal provenance boilerplate;
2. because several major mechanism packages landed materially below their nominal Architecture page allocations, a bounded semantic-depth audit is required before deciding whether expansion is necessary. Expansion must be evidence-driven, not page-count padding.

## Page-count finding

CI reports 68 pages. Direct PDF inspection shows approximately:

- front matter: 6 pages;
- substantive body: pages 7-57, 51 pages;
- references: pages 58-68, 11 pages.

The body pages are visually dense with no systematic blank-space inflation. Extracted body text is approximately 97.8k non-whitespace characters, about 1.9k non-whitespace characters per body page.

Representative major-package extracted text volumes are approximately:

- representation: 7.1k non-whitespace characters;
- paradigms: 7.0k;
- conditioning: 6.9k;
- control: 6.9k;
- editing: 7.2k;
- speech: 7.1k;
- music: 7.0k;
- video: 6.8k.

These are not empty or headline-only chapters. Spot checks show explicit bottleneck -> mechanism -> improvement -> trade-off -> succession reasoning, source-bound quantitative facts, and declared evidence limits.

### Architecture page-plan arithmetic defect

The approved Architecture note says:

`representation 8 / paradigms 10 / conditioning 5 / control 5 / editing 5 / speech 9 / music 7 / video 9 / temporal 4 / runtime 5 / evaluation 7 / convergence 4 / capstones 8 / reception 2 / front+back matter 6 (sum 84 incl. rounding)`.

Those listed allocations sum to **94**, not 84. Therefore the prior 80-page target and the listed chapter allocations were internally inconsistent as a quantitative planning instrument. This is a planning-note arithmetic defect, not a reason by itself to reopen the Human-approved Architecture. Preserve the approved Architecture historically and record this discrepancy in execution notes; do not rewrite approved Architecture merely to make arithmetic match the current PDF.

## Depth finding

The r1 manuscript is substantially better than the thin-catalog failure mode that was explicitly prohibited:

- representation is first-class and covers VAE/VQ/VQGAN/dVAE, neural codecs, semantic/acoustic hierarchy, and video tokenization;
- paradigms separates architecture, objective, and sampling/inference and covers GAN/AR/diffusion/score-SDE/LDM/DiT/flow/rectified-flow/consistency lineage;
- speech, music, and video are independent mechanism chapters rather than image appendices;
- runtime and evaluation remain independent technical chapters;
- closed systems are quarantined to capability/workflow/lifecycle context;
- X remains reception/deployment/failure evidence only.

Nevertheless, the actual chapter spans are materially shorter than the nominal package allocations, especially representation, paradigms, speech, music, and video. Before Human Publication Preview approval, perform a semantic delta audit against the 43-transition ledger and active Evidence cards. The audit must answer whether the manuscript omitted source-supported mechanism detail merely to stay compact.

Do **not** expand text just to reach 80 pages. If every transition already carries the evidence-supported bottleneck/change/improvement/trade-off/succession detail at an appropriate explanatory depth, retaining a sub-80-page manuscript is acceptable. If the audit finds supported detail collapsed into one-line mentions, generic synthesis, or citation-only coverage, expand only those locations.

## Bibliography blocker

Reader-facing references currently contain malformed author rendering. Direct PDF inspection shows examples such as visible `bibinitperiod` artefacts and initials/author strings being parsed incorrectly. The current BibTeX source uses display strings such as:

- `author = {Kingma \\& Welling}`
- `author = {van den Oord et al.}`

as normal BibLaTeX name lists, which causes reader-visible mangling.

Repair author handling deterministically. If the source record only provides a display author string rather than a proper BibLaTeX name list, preserve it as a literal author string instead of allowing name-list parsing. Do not invent full author metadata.

Also remove reader-facing generic internal provenance boilerplate from ordinary VERIFIED bibliography entries where it adds no bibliographic value, e.g. repeated text such as `Source class ... as bound in Evidence` and `Primary locator as rebound ... where applicable`. PARTIAL / NEEDS_MORE limitations may remain reader-visible where they are editorially necessary, but should be written in reader-facing language rather than pipeline jargon. Provenance audit detail remains in repository execution/Evidence artifacts.

## Layout review

Spot-rendered pages across the manuscript show clean two-column flow, readable tables/callouts, no clipping, no systematic blank pages, and no obvious margin overflow. The page-count concern is therefore a semantic-density question, not a typesetting-empty-space question.

## Required next action

Run one bounded Publication Preview r2 repair pass containing:

1. bibliography author/render cleanup;
2. reader-facing bibliography note cleanup;
3. semantic-depth delta audit against all 43 transitions and 14 packages;
4. evidence-driven targeted expansion only where the audit finds under-explained supported content;
5. revalidation and fresh PDF rendering;
6. stop again at `PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION_R2`.

Do not enter Freeze or Release.
