# TS-003 reader/publication validation report r4 (canonical-authority recovery / reader-editorial rebind)

Status: `DRAFT_COMPLETE / RECOVERED / FRESH_EXACT_PDF_READY_FOR_SOL_REVIEW`

Date: `2026-10-03 JST`

Issue: `SP-vision-multimodal-2026` — branch `special/vision-multimodal-2026-work`

## 1. Mission / authority separation

Immutable DRAFT_COMPLETE checkpoint -> checkpointed canonical Draft r1 authority
-> edition-local reader/editorial transformation (Sol-reviewed r2-r9 history +
DRAFT_R9_BINDING terminology authority) -> reader manuscript -> TeX -> PDF ->
fresh Sol exact-PDF review.

- `CANONICAL_DRAFT_AUTHORITY = checkpointed r1`
- `READER_EDITORIAL_AUTHORITY = Sol-accepted r9 refinement (publication layer only)`

Frozen Core v2 unchanged. No checkpoint rewrite, no lifecycle rollback, no
shared-Core supersession. Stop at `DRAFT_COMPLETE`; no `ADVANCE_STAGE`.

## 2. Start guards (all matched read-only before writes)

- work HEAD `4d541ee6d8f3886f7bb6ef5e7d75e1ce13811633` / tree `70b9c28158860ef19d0e0c87612abf9413255c17`
- main `d6381568cc897a47d6de992189e20339350342b7` / `83ce3a216d852a1c32d0138f9c56fadefa800666`
- Frozen Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- checkpoint blob `3c8024311d911f4e3a44e29859fc5cf481e0073e`
- checkpoint impl `1a588ff12384b4d5236d7e3860ee1cec937c14df` (execution-contract authority, not restore source)
- r1 source commit `d1053e957d92cddd9d2759ec9713db59c66263ad` / tree `d69fe46574d0d922e8a1e2c4c4a69e2719f4ddae`
- r9 commit `79d2b3e291e10896ed616bd698abefc1e479ddbe` / tree `4d96d07db9147b3c9a973a6f3bdc6b4cd09d8b53`
- pub-r3 `78b770fbabd4af29afe8a0342b747b01ae4b952b`, Sol-r3 `4d541ee6d8f3886f7bb6ef5e7d75e1ce13811633`
- terminology blob `cf39a5860d64b5d85a3a382911680dcadaa954a1`, status `DRAFT_R9_BINDING`
- lifecycle `DRAFT_COMPLETE`, arch approved, pub pending, validation/publication_preview/freeze/release pending
- Human Publication Preview approval absent; r3 PDF `637877b8…` 38pp 684804B present; r9 Draft artifacts present
- Sol findings confirmed: 16 packages r1==cur, 16 results r1!=cur, synthesis different, 34/34 cur==r9

## 3. Phase A — reader/editorial authority materialized

Root: `sources/SP-vision-multimodal-2026/publication/editorial/`

- `reader-editorial-authority-r9.json` SHA-256 `7ab5751f3a8bb9ab897d4968481a738764868d768eac6eacb3b242c9032ae9d0`
- `build_reader_editorial_authority_r9.py` (reproducible from `git show <commit>:<path>`)
- `validate_reader_editorial_authority.py` (independent re-check, never assumes)

Binds: issue identity; checkpoint path+hash; r1 source commit/tree; 16 checkpointed
Result SHAs + synthesis SHAs; r9 commit/tree; Sol r9 PASS
(`sol-draft-review-r9.md`); terminology path+blob; r1-r9 draft commits + Sol r1-r9;
pub-r3 identity; target r3 PDF SHA `637877b8…`; 16 package reader projections
(headline/deck/deck-refs/ordered blocks/block-id/type/text/Evidence-refs) +
r9 synthesis payload for renderer. Explicit `CANONICAL=r1` vs `READER=r9` labels;
forbids claiming r9 remains canonical.

Validator PASS: 16/16 packages unchanged; 16/16 Evidence task-sets bounded
(P07A/P07B/P15 consolidation preserves unique sets); full ref-sets equal;
LIMITATION sets equal; package identity unchanged; CLAIM_BOUNDARY present;
must_cover unchanged; Arch order `P01..P15` intact; projections bind `79d2b3e` bytes.

## 4. Phase B — canonical Draft restored to r1

Restored only 18 files from `d1053e957…` via historical Git bytes (no manual reconstruction):

- `draft/v2/packages/*/draft-result.json` ×16 (P01..P15 incl. P07A/P07B)
- `draft/v2/profile-synthesis-input.json`, `profile-synthesis-result.json`

Verification:

- `18/18 EXACT MATCH` against `ARCHITECTURE_ESTABLISHED.json` SHA-256
- `16/16 UNCHANGED` draft-package.json (r1==checkpoint==workdir)
- `ARCHITECTURE_ESTABLISHED.json` unmodified (blob `3c80243…`)
- lifecycle still `DRAFT_COMPLETE` (State untouched to make validation pass)

## 5. Phase C — reader generation rebound to permitted layer

New bounded execution dir: `sources/SP-vision-multimodal-2026/execution/reader-publication-validation-r4-rebind-20261003/`

- `render_reader_source.py` (r4): verifies canonical r1 integrity via checkpoint SHAs,
  uses `reader-editorial-authority-r9.json` for wording, approved Architecture/Profile,
  accepted Evidence for bibliography. Never reads restored r1 prose as reader wording.
- Provenance comments corrected:
  `Generated deterministically from accepted Draft r9 bytes` ->
  `Generated deterministically from checkpointed canonical Draft r1 + edition-local Sol-accepted reader/editorial transformation (reader-editorial-authority-r9.json) + approved Architecture/Profile/Synthesis authority`
  plus per-package `% package:<id> reader-editorial-authority-r9 bound … (canonical r1 provenance verified…)`.
- No hand-edit of `main.tex`; deterministic generation from explicit source authority preserved.

## 6. Phase D — manifest/review provenance repaired

- `build_manuscript.py` (r4): reader locations derived from editorial authority +
  generated TeX sections, not r1 prose fields.
- `build_reviews.py` (r4): `_section_locations()` from editorial authority; forces
  regeneration (no stale reuse); semantic/editorial no longer claims TeX identical
  to “canonical Draft r9”. Explicitly validates: canonical=r1; reader=editorial r9;
  no new facts/sources; Evidence bounded; attribution intact; CLAIM_BOUNDARY intact;
  G01-G06/PARTIAL intact; r9 terminology intact; no pipeline leaks; Arch coverage
  complete; synthesis within selected authority.
- `build_deterministic.py` reused (TeX/PDF/Evidence only, no Draft reads).
- Regenerated current derived authority at `DRAFT_COMPLETE`:
  `main.tex`, `references.bib`, reader manuscript, semantic/editorial review,
  visual review, reader-surface semantic review, reader-surface gate,
  deterministic results, quality bundle, exact PDF.
- Historical r1-r3 execution reports untouched.

Stale-reference scan (current bundle + r4 artifacts + TeX/bib): zero
`Generated deterministically from accepted Draft r6/r9` as authority claim;
only meta `must not claim TeX identical to canonical Draft r9` guard text remains.
Old r1 headings (`箱から集合予測…` etc.) absent from current bundle (historical records untouched, allowed).

## 7. Phase E — accepted r3 reader surface preserved

Pre-rebuild r3 captured to `/tmp/opencode/ts003-recovery/main-r3.pdf` (non-repo):
SHA `637877b879def1dc491b1b3d40a852cd209e22f02d57794697079a722f949795`, 684804B, 38pp.

Post-rebuild r4:

- `main.tex` SHA-256 `da750a40a1c37e73abdd7a763c3ef6784e5d3991f97f04bac5393ed118c3a484`
- `references.bib` SHA-256 `2a3745c759a1c5b9441008c5689af4750f39ca9a413c95e9a0ad97407114b05c`
- PDF SHA-256 `78f4cc8c79c008c92a4af2a8e5f343f7a5d0c22e59f89d2fbe48c562318c214c`
- Bytes 684804, pages 38, toolchain TeX Live 2026 LuaLaTeX+Biber
- TeX non-comment diff r3 vs r4: identical (only 17 provenance comment lines changed)
- Bib non-comment diff: identical (only header comments changed)
- Citations `111/111` (0 undefined, 0 uncited)
- Extracted text `pdftotext` SHA identical `a330bcb7237fb4fe5b46a66e450f2a3082c56a1887ee7eb68fd567b33859c308` (5107 lines)
- 150dpi PNG `38/38` pages hash-identical
- Per-page PyMuPDF text identical 38/38; rects identical; xref length 1064==1064
- Normalized PDF (strip CreationDate/ModDate/ID) byte-identical; metadata-only difference
  (r3 `D:20261003015043+09'00'` vs r4 `D:20261003042922+09'00'`)
- No content-stream semantic difference; no citation difference; no pagination difference
- Exact bytes differ only via build metadata/trailer (allowed); `EXACT PDF MATCH` not
  claimed, `READER-VISIBLE EQUIVALENCE PROVEN` claimed.

No unexpected reader-visible difference; did not STOP.

## 8. Phase F — deterministic Core validation (non-advancing)

Ran canonical Frozen Core `DRAFT_COMPLETE` stage validation via
`scripts/survey_stage_validation_v2.py` with 7 current artifacts
(reader-manuscript / validated-source / publication-pdf /
quality-regression-bundle / semantic-review / visual-review / reader-surface-gate).

- Prior error `prior Stage Checkpoint artifact drift: …` disappeared.
- Result `PASS` (`from DRAFT_COMPLETE to VALIDATED_DRAFT`), recorded to
  `core-stage-validation-draft-complete.json` in this r4 dir (non-advancing evidence only).
- No `ADVANCE_STAGE`; no `DRAFT_COMPLETE -> VALIDATED_DRAFT` checkpoint created.
- Production State remains `DRAFT_COMPLETE` byte-identical; no Human Preview/Freeze/Release.

Manuscript/bundle/semantic/visual/gate validators all PASS independently.

## 9. Changed-path inventory (this recovery)

- `sources/SP-vision-multimodal-2026/draft/v2/packages/*/draft-result.json` ×16 (r1 restore)
- `sources/SP-vision-multimodal-2026/draft/v2/profile-synthesis-input.json`, `profile-synthesis-result.json`
- `sources/SP-vision-multimodal-2026/publication/editorial/` (new: authority JSON + 2 scripts)
- `sources/SP-vision-multimodal-2026/execution/reader-publication-validation-r4-rebind-20261003/` (new: 4 scripts + validation JSON + this report)
- `sources/SP-vision-multimodal-2026/publication/v2/`: `reader-manuscript-v2.json`,
  `reader-surface-semantic-review-v2.json`, `quality-regression-bundle-v2.json`,
  `semantic-editorial-review-v2.json`, `visual-review-v2.json`,
  `reader-surface-gate-v2.json`, `deterministic/pdf-preflight.json`
  (other deterministic files byte-identical, not listed as modified)
- `surveys/special/vision-multimodal-2026/main.tex`, `references.bib`, `main.pdf`
- Production State, checkpoint, Architecture approval, main/Core untouched.

## 10. Terminal

`TS-003_CANONICAL_DRAFT_R1_RECOVERED`
`TS-003_READER_EDITORIAL_R9_REBOUND`
`TS-003_R3_READER_CONTENT_PRESERVED`
`TS-003_CORE_ARTIFACT_DRIFT_CLEARED`
`TS-003_LIFECYCLE_DRAFT_COMPLETE`
`TS-003_READY_FOR_FRESH_SOL_EXACT_PDF_REVIEW`
`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`
`NO_FREEZE`
`NO_RELEASE`
