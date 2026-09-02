# 2026-W33 Validated Draft layout-polish Sol review r2

## Authority

- Repository: `eariver/japanese-generative-ai-survey`
- Branch: `weekly/2026-W33-v2-work`
- Reviewed candidate HEAD: `0a7c16a4aad1d273390e9ebe88ffc6f3262eba02`
- Reviewed-main Core authority: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Current lifecycle during review: `DRAFT_COMPLETE`

## Independent Sol verification

The layout-polish range `2732362c41ef35f64726920ff1fb42964d40ef0b -> 0a7c16a4aad1d273390e9ebe88ffc6f3262eba02` is a normal fast-forward series. The edition-local source change is limited to `surveys/weekly/2026-W33/main.tex`: add `\usepackage{balance}` and invoke `\balance` after the final Week in Review input. No reader prose, factual claim, citation, Evidence attribution, Architecture placement, Draft Package/Result, shared Core/style/workflow, or Production State changed.

Canonical CI run `33403175661` is `success`, with head SHA exactly `b133b2da41862fce7f319c2181fe7d7b8df74d7c`. The build job and final TeX warning gate passed. Artifact `9762175041` has ZIP digest `sha256:e26779756e2a57cff92c49d2ca4bf49d35beae205702f34b0ddbcf7755d6db61`.

Sol independently downloaded that artifact and independently hashed `main.pdf`:

`4febb800d879b91ad2cd4c721fbb56c9db2d2555454595e236f71450e82868d2`

This equals the artifact digest file and repository `main.pdf.sha256`. The PDF is 270228 bytes, 11 pages, A4, unencrypted.

Sol independently rendered all 11 pages. No clipping, overlap, missing glyph, broken box border, blocking overflow, or unreadable layout was observed. The prior page-8 defect is resolved: existing Week in Review material now occupies both columns. Remaining bottom whitespace on page 8 is symmetrical/natural after the balanced final two-column section and is not a publication defect. References tail whitespace is also acceptable.

Semantic/editorial content remains accepted. Reader Manuscript, Quality Regression Bundle, semantic review, deterministic PDF preflight, identifier preservation, and citation/entity binding all bind the new reader source/PDF and remain structurally consistent.

## Sol-found provenance defect

`visual-review-v2.json` correctly binds the new source and new PDF at top level, but its human-readable `evidence_locations` retained four stale references from the pre-polish CI build:

- old PDF SHA `4f1028c221101cd21cf300a3916c9d4b7cf589b5f672a0f97f61aa6afc992243`
- old workflow run `33398104252`
- old artifact `9760255099`
- old repository PDF blob `9c0de61f6469e2f40ca81c293a541f4669f95bbc`

These must be replaced exactly with the layout-polish authorities:

- PDF SHA `4febb800d879b91ad2cd4c721fbb56c9db2d2555454595e236f71450e82868d2`
- workflow run `33403175661`
- artifact `9762175041`
- repository PDF blob `c17f1b77434351e49793b11f2ce82815ecb5693e`

No other field semantics may change except values mechanically dependent on the modified record, including `review_sha256` and any hash-binding records that must be regenerated because the visual-review bytes change.

## Decision

`CONDITIONAL_ACCEPT / EXACT_PDF_AND_LAYOUT_VERIFIED / STALE_VISUAL_PROVENANCE_REPAIR_REQUIRED / AUTHORIZED_FOR_VALIDATION_AND_PUBLICATION_CANDIDATE_ADVANCEMENT_AFTER_EXACT_REPAIR`

The four exact replacements above are mechanically pre-approved. If Luna performs only those replacements, recomputes required self/hash bindings, passes the current canonical visual-review validator and full `DRAFT_COMPLETE` stage contract, and observes no additional defect, no second Sol semantic/layout review is required before deterministic advancement.

After successful repair, Luna is authorized in the same bounded unit to:

1. advance exactly once `DRAFT_COMPLETE -> VALIDATED_DRAFT` using the repaired exact validation authority set;
2. deterministically build/validate `publication-candidate-v2.json` from the already-reviewed exact bytes;
3. advance exactly once `VALIDATED_DRAFT -> RELEASE_CANDIDATE`;
4. stop at the `PUBLICATION_PREVIEW` Human Gate with no Human decision recorded.

Luna is not authorized to approve Publication Preview, freeze, release, alter reader prose, alter the PDF/source, add research, or modify upstream semantic authority.
