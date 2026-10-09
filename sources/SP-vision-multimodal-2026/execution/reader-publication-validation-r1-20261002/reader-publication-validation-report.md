# TS-003 reader/publication validation report (candidate for Sol review)

Status: `READER_PUBLICATION_CANDIDATE_BUILT / EXACT_PDF_READY / STAGE_CONTRACT_BLOCKED_BY_CORE_LIMITATION`

Date: `2026-10-02`

Issue: `SP-vision-multimodal-2026` — branch `special/vision-multimodal-2026-work`

## 1. Startup guards (all matched, read-only verified)

- work HEAD `05ff1af0f3d42efa344b5f09f360f96748e9de91` / tree `e9970f6e73736ae6da1b427388fc2c654bc2d0d5`
- main `d6381568cc897a47d6de992189e20339350342b7` / `83ce3a216d852a1c32d0138f9c56fadefa800666`
- Core `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`
- map blob `bad61f051146b0ec0c3fd25d72d816b2de41c53b`
- lifecycle `DRAFT_COMPLETE`, arch approved, pub pending, draft passed, rest pending
- arch `d2f133bc…`, selection `378b818e…`

## 2. Accepted authority

- Draft r6 commit `a345358f568e5ab7b55798c1f8469378abbd5783` / tree `572ad64a59c1274c5b035facd2fa36c0eb4ffb6b`.
- Sol Draft Review r6: PASS (reader-publication validation authorized; no Human
  Preview/Freeze/Release/new research/rewriting).
- Map `TS-003_TERMINOLOGY_MAP_CUMULATIVE_R6_BINDING` (unchanged throughout).

## 3. Changed-path inventory (this execution)

- `surveys/special/vision-multimodal-2026/main.tex` (new, 167206 bytes)
- `surveys/special/vision-multimodal-2026/references.bib` (new, 111 entries)
- `surveys/special/vision-multimodal-2026/jgaisurvey.sty` (copy of `templates/survey/jgaisurvey.sty`)
- `surveys/special/vision-multimodal-2026/main.pdf` (new, exact bytes below)
- build logs/telemetry (`main.log`, `main.bbl`, `main.bcf`, `main.run.xml`, `main-blx.bib`, aux files)
- `sources/SP-vision-multimodal-2026/publication/v2/reader-manuscript-v2.json`
- `sources/SP-vision-multimodal-2026/publication/v2/reader-surface-semantic-review-v2.json`
- `sources/SP-vision-multimodal-2026/publication/v2/quality-regression-bundle-v2.json`
- `sources/SP-vision-multimodal-2026/publication/v2/deterministic/*.json` (4 files)
- `sources/SP-vision-multimodal-2026/publication/v2/semantic-editorial-review-v2.json`
- `sources/SP-vision-multimodal-2026/publication/v2/visual-review-v2.json`
- `sources/SP-vision-multimodal-2026/publication/v2/reader-surface-gate-v2.json`
- `sources/SP-vision-multimodal-2026/execution/reader-publication-validation-r1-20261002/*`
- Production State: UNTOUCHED (sha256 identical before/after:
  `051539069e440ee8d8fb5b21e83b00a710f56bc4db3c5f8a057323832c990f44`).

## 4. Reader fidelity (content preservation)

- 16/16 packages rendered in drafting order as numbered Sections 1–16 with exact
  r6 headlines; deck + PARAGRAPH blocks byte-identical modulo TeX escaping;
  boundary blocks as concise-Japanese claimboundary boxes; synthesis Section 17
  reuses the four validated synthesis payloads verbatim.
- 111/111 cited discovery IDs resolve to Evidence-bound bib entries
  (0 undefined, 0 uncited keys); every must-cover requirement maps to an exact
  extant TeX block (manuscript validation PASS, incl. fidelity + surface scans).
- P07A/P07B distinct; P07B mechanism-grouped; P09 same-source comparisons intact
  with attribution; P15 synthesis-led; evaluator roles intact; G01–G06/PARTIAL
  intact; no internal labels; no paraphrase/addition/deletion.
- Front matter (cover/title/TOC/問いと読み方) and synthesis heading are
  structural assembly from approved Architecture/Profile authority; no new claims.

## 5. Terminology final scan (TeX + PDF text)

- Zero cumulative-map blocking forms in main.tex (all §§3.1–3.5 + §3.6 forms
  scanned, incl. 生徒-model disambiguation and encoding-符号 disambiguation).
- Bare self-supervised `自己教師`: 0. Established forms preserved
  (ニューラルネットワーク, 教師モデル, マルチモーダル, セグメンテーション,
  ポストトレーニング, ハルシネーション, デプロイ).

## 6. Bibliography / citation binding

- 111 entries from accepted Evidence source records (title/URL/date/access
  preserved; 4 repository records dateless by source, no invention).
- identifier-preservation: 111 cited == 111 defined.
- subject-entity-property-binding: 111 bindings with materiality/status/access time.

## 7. Reader-surface gate: PASS

- manuscript → semantic review → gate chain built via canonical builders;
  `validate_reader_surface_gate` PASS (part of gate construction).

## 8. Semantic / editorial review: PASS records built

- 9/9 checks (5 agent-semantic + 3 core + 1 longform), incl. below-target density
  justification (`page-plan:38/112`, `density-review:below-target-substantive`;
  short length is Sol-accepted dedup, not padding).

## 9. Deterministic quality checks: 4/4 PASS

- Build log: 0 undefined citations/references, 0 rerun warnings, 0 missing glyphs,
  0 overfull/underfull boxes. `bind_pdf_authority` REPOSITORY_FILE.

## 10. PDF build

- Method: local canonical toolchain, TeX Live 2026, LuaLaTeX + Biber + LuaLaTeX ×2
  (same engine/version family as CI `build-special-pdf.yml`).
- Path: `surveys/special/vision-multimodal-2026/main.pdf`
- SHA-256: `9f27aeaebb5297c253bb2f709b9b2084d6562c5fb06dcc218467c0863c2b7cf9`
- Bytes: 687583. Pages: 38.
- 38 < 112 target: reported, not padded, not trimmed (Sol-accepted short volume;
  density justification in LONGFORM_TECHNICAL_DEPTH). 38 ≤ 120 max holds.

## 11. Visual review: 38/38 pages inspected, no defects

- Cover/front/TOC clean; two-column narrative balanced; boundary boxes unclipped;
  citations render as bracket numbers; bibliography readable with intact URLs;
  per-page density even (no empty pages); no clipping/overflow/missing glyphs/
  collisions/broken tables/stranded headings/excess blanks.
- 5/5 visual checks PASS (TOC, needspace, page balance, exact-PDF review, mixed layout).

## 12. Layout check

- Preflight-equivalent: zero log findings; mixed-layout evidence recorded
  (wide full-width boundaries, one-column references, balanced two-column narrative;
  no architecture exception needed or claimed).

## 13. Stage-contract validation: NOT OBTAINED — Core limitation (fail-closed)

Canonical `survey_stage_validation_v2.py` (DRAFT_COMPLETE → VALIDATED_DRAFT) was
executed and refused at its global pre-check:

`Production State invalid before stage validation: Stage Checkpoint artifact
drift: draft-result:P01 … P15, synthesis-input, synthesis-result`

Root cause (verified byte-for-byte):

- The `draft` Stage Checkpoint (`orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json`,
  written at the r1 advance) binds Draft r1 bytes (e.g. P01 `e7aff8d5…`).
- Canonical Draft Results are Sol-accepted r6 (e.g. P01 `11bd8ddf…`) via the
  Sol-authorized bounded repairs r2–r6 at DRAFT_COMPLETE (each Sol-reviewed;
  r6 Sol-PASSed as editorial authority).
- `validate_agent_state` → `_validate_checkpoint_record` (survey_agent_control_v2.py:279)
  and `_prior_artifacts` (survey_stage_validation_v2.py:157) both require
  byte-identity with checkpoint-bound files, with no tolerance.
- The only Core escape hatch (superseded-artifact revalidation,
  `resolve_active_publication_revalidation`) requires VALIDATED_DRAFT
  establishment, which does not exist; the only checkpoint writer is
  `build_stage_checkpoint` (advance flow), and `advance-stage` is contract-forbidden
  (state must stay DRAFT_COMPLETE byte-identical).
- The DRAFT_COMPLETE transition semantics themselves never consult draft files
  (manuscript/source/pdf/bundle/reviews/gate only) — the blocker is purely the
  global hygiene pre-check plus prior-artifact drift enforcement.

No rollback, history rewrite, checkpoint edit, state mutation, or fabricated PASS
report was performed. Per repo policy this is recorded as a shared-Core defect
under the edition tree (this report); Core repair is separate work.

Consequence: `CORE_STAGE_CONTRACT = PASS` is NOT claimed. No `core-stage-contract`
file was written. Lifecycle remains `DRAFT_COMPLETE`; no advance executed;
no Human Publication Preview decision; no Freeze/Release.

## 14. Terminal + push

- main/Core unchanged (verify at push). Final HEAD/tree reported after push.

Honest terminal state:

`TS-003 READER_PUBLICATION_VALIDATION_CANDIDATE_COMPLETE`
`TS-003 EXACT_PDF_READY_FOR_SOL_REVIEW`
`STAGE_CONTRACT_BLOCKED_BY_CHECKPOINT_STALENESS_R1_VS_R6`
`PRODUCTION_STATE_UNCHANGED_DRAFT_COMPLETE`
`NO_HUMAN_PUBLICATION_PREVIEW_DECISION`
`NO_FREEZE`
`NO_RELEASE`
