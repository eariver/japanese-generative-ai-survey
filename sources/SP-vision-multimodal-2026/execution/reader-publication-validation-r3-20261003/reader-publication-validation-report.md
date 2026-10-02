# TS-003 reader/publication validation report r3 (candidate for Sol review)

Status: `PUBLICATION_CANDIDATE_R3_PROVENANCE_REBOUND / EXACT_R3_PDF_READY / STAGE_DEFERRED_KNOWN_BLOCKER`

Date: `2026-10-03`

Issue: `SP-vision-multimodal-2026` — branch `special/vision-multimodal-2026-work`

## 1. Startup guards (all matched read-only)

- work HEAD `1df8324051e4b7ccd27d2865db5cb3530fcd1feb` / tree `dd94cef277a4858bdc3edbb8a869ffd0d318826e`
- main `d6381568cc897a47d6de992189e20339350342b7` / `83ce3a216d852a1c32d0138f9c56fadefa800666`
- Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- map blob `cf39a5860d64b5d85a3a382911680dcadaa954a1`, status `DRAFT_R9_BINDING`
- lifecycle `DRAFT_COMPLETE`, arch approved, pub pending, draft passed, rest pending
- r2 PDF `a18caa91…` verified present before regeneration

## 2. Authorities

- Sol Reader/Publication Review r2 (`sol-reader-publication-review-r2.md`): REQUEST_CHANGES (F1–F3 provenance).
- Reviewed r2: commit `0ce457df8…` / tree `b08cea28…`.
- Accepted reader authority: Draft r9 @ `79d2b3e29…` (Sol r9 PASS, unchanged).
- Stale r1/r2 bytes preserved in git history; r2 workdir removed only after verification.

## 3. Provenance defects repaired (generation path, not hand-patches)

- Renderer comment: `accepted Draft r6` → `accepted Draft r9`
  (`render_reader_source.py` fixed, deterministic on regeneration).
- Review generator: hardcoded SEC list replaced by `_section_locations()` derived
  from canonical Draft Results in drafting order; `accepted r6` details → r9
  (semantic review + POST_TRANSFORM_SEMANTIC_REVALIDATION).

## 4. r2 → r3 reader-visible identity

- r2 vs r3 TeX excluding the provenance comment line: 355/355 lines identical.
- Only allowed change: non-rendering provenance comment + consequent hashes/metadata.

## 5. Stale-reference scan (current bundle + r3 exec artifacts): ZERO

- `accepted Draft r6` / `accepted r6` / `Generated deterministically from accepted Draft r6`: 0.
- `箱から集合予測、開かれた語彙へ` / `言葉を箱とマスクに結ぶ接地` / `凍結した部品をつなぐ橋`: 0.
- Historical execution records outside current bundle untouched (allowed).

## 6. Changed-path inventory

- `surveys/special/vision-multimodal-2026/`: main.tex, main.pdf + build telemetry
  (references.bib + sty byte-identical: Evidence/style unchanged).
- `sources/SP-vision-multimodal-2026/publication/v2/`: all 6 JSON + deterministic ×4.
- `sources/SP-vision-multimodal-2026/execution/reader-publication-validation-r3-20261003/`.
- Production State untouched.

## 7. Rebuilt artifact hashes

- main.tex `14c415fd…`; PDF `637877b8…`; manuscript `4653b41e…`;
  semantic review `6f8afa79…`; bundle `5d523eb8…`; editorial `f512b064…`;
  visual `b1a9ac10…`; gate `72878c40…`.
- Semantic review binds exact r3 main.tex SHA; evidence locations are current
  r9 headings (derived, not hard-coded).

## 8. Exact PDF r3

- Path: `surveys/special/vision-multimodal-2026/main.pdf`
- SHA-256: `637877b879def1dc491b1b3d40a852cd209e22f02d57794697079a722f949795`
- Size: 684804 bytes. Pages: 38. Build: TeX Live 2026 LuaLaTeX+Biber (canonical family).
- 0 blocking findings, 0 layout findings; 38 ≤ 120 max; below-target density justified.

## 9. Visual review (38/38 pages)

Cover/front/TOC/body/boundaries/references inspected: no clipping, overflow,
missing glyphs, collisions, broken boxes, bad breaks, stranded headings,
readability issues, blank anomalies, or punctuation artifacts. Density even.

## 10. Non-stage checks: ALL PASS

Manuscript/fidelity, semantic review, gate, editorial (9/9), deterministic (4/4),
preflight, visual (5/5), citation integrity (111/111, 0 undefined, 0 uncited),
terminology final scan (0 blocking forms in TeX).

## 11. State / Core blocker

- Production State byte-identical `DRAFT_COMPLETE` (never written).
- `CORE_STAGE_VALIDATION_DEFERRED_KNOWN_CHECKPOINT_STALENESS` — no stage
  validation run, no advance, no checkpoint edits, no fake PASS.
- No Human Preview/Freeze/Release. main/Core unchanged (verify at push).

`TS-003 PUBLICATION_CANDIDATE_R3_PROVENANCE_REBIND_COMPLETE`
`TS-003 CURRENT_PUBLICATION_BUNDLE_BINDS_ACCEPTED_DRAFT_R9`
`TS-003 EXACT_R3_PDF_READY_FOR_SOL_REVIEW`
`ALL_NON_STAGE_PUBLICATION_CHECKS_PASS`
`CORE_STAGE_VALIDATION_DEFERRED_KNOWN_CHECKPOINT_STALENESS`
`PRODUCTION_STATE_UNCHANGED_DRAFT_COMPLETE`
