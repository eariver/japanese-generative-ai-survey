# TS-003 reader/publication validation report r2 (candidate for Sol review)

Status: `READER_PUBLICATION_CANDIDATE_R2_BUILT / EXACT_R9_PDF_READY / STAGE_DEFERRED_KNOWN_BLOCKER`

Date: `2026-10-03`

Issue: `SP-vision-multimodal-2026` — branch `special/vision-multimodal-2026-work`

## 1. Startup guards (all matched read-only)

- work HEAD `d5b1996648cd44c38e35fb2abf7c218c45c15aa4` / tree `1138e7d71920873cfd73438ae8f49b5a231d9f69`
- main `d6381568cc897a47d6de992189e20339350342b7` / `83ce3a216d852a1c32d0138f9c56fadefa800666`
- Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- map blob `cf39a5860d64b5d85a3a382911680dcadaa954a1`, status `DRAFT_R9_BINDING`
- lifecycle `DRAFT_COMPLETE`, arch approved, pub pending, draft passed, rest pending
- arch `d2f133bc…`, selection `378b818e…`

## 2. Accepted authority

- Draft r9 commit `79d2b3e291e10896ed616bd698abefc1e479ddbe` (Sol r9 PASS).
- Stale r1 candidate (`9f27aeae…` PDF) removed (preserved in git history + r1 report),
  fully regenerated from r9. Nothing of r1 reused as authority.

## 3. Changed-path inventory (r2 regeneration)

- `surveys/special/vision-multimodal-2026/`: main.tex, references.bib (byte-identical
  to r1: Evidence unchanged), jgaisurvey.sty (template copy), main.pdf + build telemetry.
- `sources/SP-vision-multimodal-2026/publication/v2/`: manuscript, semantic review,
  quality bundle + deterministic ×4, editorial review, visual review, surface gate.
- `sources/SP-vision-multimodal-2026/execution/reader-publication-validation-r2-20261003/`.
- Production State untouched (sha256 `051539069e…` before/after).

## 4. Reader fidelity (r9 authority preserved)

- 16/16 packages in drafting order, exact r9 headlines/decks/blocks/boundaries
  (TeX-escaped only); synthesis reuses validated payloads verbatim.
- 111/111 citations resolve, 0 undefined, 0 uncited; must-cover mapping exact.
- P07A/P07B distinct; P07B grouped; P09 protocol-bound; P15 synthesis-led;
  evaluator roles, boundaries, G01–G06/PARTIAL intact; no internal labels.

## 5. Terminology final scan (TeX)

Zero cumulative-map blocking forms; bare-自己教師 0; preferred forms present.
r9 headline/wording changes flow through (ボックス/オープンボキャブラリー/
バックボーン/密に融合/検出へ適応).

## 6. Bibliography binding

111 entries from accepted Evidence only (bib byte-identical to r1 since Evidence
unchanged); no invented/missing/unused citations; PARTIAL stays limited.

## 7. Gate / reviews / deterministic checks: all PASS

- reader-manuscript (fidelity + surface scans pass inside builder).
- semantic review 4/4, quality bundle 4/4 deterministic (preflight: 0 blocking,
  0 layout findings), editorial 9/9, visual 5/5, surface gate PASS.

## 8. Exact PDF

- Path: `surveys/special/vision-multimodal-2026/main.pdf`
- SHA-256: `a18caa91e4530968b99f57e88324a0d3057b58627f888c91acd9e3b341a8028d`
- Size: 684804 bytes. Pages: 38. Build: TeX Live 2026 LuaLaTeX+Biber (canonical family).
- 38 ≤ 120 max; below 112 target by Sol-accepted dedup (density justified, no padding).

## 9. Visual review (38/38 pages)

Cover/front/TOC clean; two-column narrative balanced; boundary boxes unclipped;
r9 repairs verified rendered (バックボーン, 密に融合, 検出へ適応); citations as
bracket numbers; bibliography readable; density even; no clipping/overflow/
missing glyphs/collisions/broken tables/stranded headings/blanks/punctuation artifacts.

## 10. r9 derivation proof

TeX rendered from canonical r9 results + r9 synthesis via content-preserving
renderer (r1 scripts reused verbatim except r6→r9 headline sync in review evidence);
citation keys map 1:1 to cited discovery IDs.

## 11. Stage validation: DEFERRED (known Core blocker, untouched)

`CORE_STAGE_VALIDATION_DEFERRED_KNOWN_CHECKPOINT_STALENESS` — no stage validation
run, no advance, no rollback, no checkpoint edits, no fake PASS.
Lifecycle remains `DRAFT_COMPLETE`; no Human Preview/Freeze/Release.

## 12. Terminal + push

- main/Core unchanged (verify at push). Final HEAD/tree reported after push.

`TS-003 READER_PUBLICATION_CANDIDATE_R2_COMPLETE`
`TS-003 EXACT_R9_DERIVED_PDF_READY_FOR_SOL_REVIEW`
`ALL_NON_STAGE_PUBLICATION_CHECKS_PASS`
`CORE_STAGE_VALIDATION_DEFERRED_KNOWN_CHECKPOINT_STALENESS`
`PRODUCTION_STATE_UNCHANGED_DRAFT_COMPLETE`
