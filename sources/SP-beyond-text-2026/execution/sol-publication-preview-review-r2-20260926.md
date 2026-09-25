# TS-002 Sol Publication Preview Review r2

Status: `PASS / READY_FOR_HUMAN_PUBLICATION_PREVIEW_DECISION_R2`

Date: 2026-09-26 JST

Repository: `eariver/japanese-generative-ai-survey`
Branch: `special/beyond-text-2026-work`
Reviewed remote HEAD: `4f13e6ce3772fc7471b3882114e3adb314daa980`
Reviewed remote tree: `a4f690d1c3c79b58fc2f93f46b54c96999b1db0a`
Reviewed main HEAD: `0bbb02b3c5963403860897daec2feaf61e82589a`
Reviewed main tree: `e4ddde5ed5059d303b818f54e27204369b256bcb`

## Decision

Publication Preview r2 is accepted for Human review.

This is a Sol editorial/review decision only. It is **not** the Human Publication Preview decision and does not authorize Freeze or Release.

## r2 repair readback

- The work branch is a direct fast-forward from the authorized r2 launch point `bf6f53017047ac485ad91d127846b52ed2eb5203` (`ahead_by=3`, `behind_by=0`).
- `main` remains unchanged.
- Reader manuscript body `main.tex` is byte-identical to r1 (`710f899bf0ed1feace82c22764bfbdad2cacbd96`).
- `references.bib` was regenerated and reduced from 53,481 to 34,940 bytes by removing internal provenance boilerplate and literalizing display author fields.
- r2 PDF is 65 pages. The reduction from 68 pages is attributable to bibliography compaction; body pagination is unchanged.
- CI r2 build is PASS with 0 blocking and 0 layout findings.

## Bibliography repair verification

Direct rendered-PDF inspection confirms that the r1 author-rendering defect is repaired. Representative references now render as reader-facing author strings such as:

- `Karras et al.`
- `Chen et al.`
- `Heusel et al.`
- `Panayotov et al.`
- `Black Forest Labs`

No `bibinitperiod`, `bibnamedelim`, mangled initial forms, or visible internal BibLaTeX macros were found in extracted-text scan or inspected rendered pages.

Generic internal notes such as `Source class PRIMARY_* as bound in Evidence` and generic provenance-rebind boilerplate were removed from ordinary VERIFIED entries. Reader-facing limitation notes remain for PARTIAL / NEEDS_MORE and X reception where they are semantically necessary.

The final bibliography page is sparse because the 139th X-reception entry ends the bibliography; this is not treated as a blocking layout defect.

## Semantic-depth audit

The bounded 43-transition audit reports:

- SUBSTANTIVE: 24
- COMPRESSED_BUT_SUFFICIENT: 16
- BOUNDARY_ONLY: 3
- UNDER_EXPLAINED: 0

The five anti-thinness focal packages — representation, paradigms, speech, music, and video — pass the package-level checks for mechanism explanation, source-bound quantities, trade-offs/failures, succession, modality-specific treatment, and architecture/objective/inference separation where applicable.

`T-EV-01` and `T-EV-02` were initially worker-labelled UNDER_EXPLAINED but the residual missing depth traces to already-declared Evidence access limitations (abstract/snippet/gated bodies). Because the current repair boundary does not authorize unsupported expansion, retaining their existing bounded prose as `COMPRESSED_BUT_SUFFICIENT` is accepted. This does not upgrade the underlying Evidence limitations.

Direct visual/readback sampling of representation/control, music, temporal/duplex evaluation, runtime/evaluation, capstone/synthesis, and bibliography pages did not reveal omitted section structure, clipping, near-blank body pages, or reader-facing pipeline artifacts.

## Page-count disposition

The 65-page r2 PDF is **not** rejected for being below the nominal 80-page target.

Reasons:

1. The approved planning envelope was 64–96 pages and explicitly not a hard cap.
2. r2 body prose is unchanged from r1; the 3-page reduction comes from removing bibliography boilerplate.
3. All 43 transitions are accounted for and no active-Evidence-supported transition was adjudicated UNDER_EXPLAINED.
4. The original Architecture page-allocation note itself contains a planning arithmetic inconsistency: the listed per-section allocations sum to 94 pages, not the recorded 84. That approved historical authority is intentionally preserved rather than silently rewritten.
5. Padding solely to reach 80 pages would reduce information density without adding supported technical content.

Therefore the correct review criterion is semantic completeness within declared Evidence boundaries, not mechanical page restoration.

## Remaining declared limitations

Publication Preview r2 still honestly carries the edition's existing bounded limitations:

- Completeness remains LIMITED.
- PARTIAL / NEEDS_MORE sources retain their stated authority levels.
- Vendor evaluations remain vendor-attributed claims unless independently reproduced.
- Closed-system mechanism claims remain bounded.
- LOW_SIGNAL lanes remain open rather than inflated.

None of these are newly introduced by r2 and none are concealed by the manuscript.

## Gate state

Current production state is:

- lifecycle: `RELEASE_CANDIDATE`
- architecture_review: `approved`
- publication_preview: `pending`
- next_action: `PUBLICATION_PREVIEW`
- terminal_reason: `HUMAN_GATE_REACHED`

Freeze and Release have not been entered.

## Human review surface

Human Publication Preview r2 should review:

- `surveys/special/beyond-text-2026/main.pdf`
- `surveys/special/beyond-text-2026/main.tex`
- `surveys/special/beyond-text-2026/references.bib`
- `sources/SP-beyond-text-2026/execution/publication-preview-r2-depth-audit/semantic-depth-delta-audit.md`
- `sources/SP-beyond-text-2026/execution/sessions/ts002-publication-preview-r2-20260926.md`

Requested Human decision:

- `APPROVED`
- `REQUEST_CHANGES`

No Human decision is generated by this review.
