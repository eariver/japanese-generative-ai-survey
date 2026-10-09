# TS-003 — Post-validation editorial publication revalidation blocked by Core v2 reason-class contract

Status: `CORE_V2_DEFERRED / HUMAN_AUTHORIZED_EDITION_EXCEPTION_COMPLETED`  
Detected: 2026-10-09 JST  
Closed operationally: 2026-10-10 JST (generic Core defect remains OPEN)

## Scope and authority

- Issue: `SP-vision-multimodal-2026`
- Shared Core frozen; do **not** repair Core v2 within an edition.
- Tracking: [Core v2 issue #560](https://github.com/eariver/japanese-generative-ai-survey/issues/560); [umbrella #515](https://github.com/eariver/japanese-generative-ai-survey/issues/515); [CV2-DM-021](../../../../docs/core-v2-deferred-maintenance-summary.md).
- User decision: Human Owner approved the exact staged TS-003 PDF, then authorized an exception Freeze/Release conditional on recording this Core v2 defect; no false normal Human Gate approval.

## Reproduction

1. Existing `VALIDATED_DRAFT` checkpoint `sources/SP-vision-multimodal-2026/orchestration/v2/checkpoints/DRAFT_COMPLETE.json` bound original canonical PDF SHA-256 `0916bb5e6222a48de002773eaa1963da9decee90b73b5fc5d292fc08caff3148`; original TeX SHA-256 `edcf8ef982a63ac9dc65881aae1963a7daf64fa7fc16de67fbf97825cba090cb`.
2. Independent review/Human paper review found reader/editorial/source-fidelity defects after validation. Corrected, independent QA-closed PDF SHA-256 `b2de84493f2215e26d16e569498c5f4b6476ebc314230cbb4e01540a72742093`, 708782 bytes, 39 pages. Human Owner expressly approved those bytes.
3. Shared Core's `revalidate_publication_surface()` accepts `reason_class` from `REVALIDATION_REASON_CLASSES = {"REVIEWED_CORE_CHANGE"}`; schema `publication-surface-revalidation.schema.json` requires the same value. Editorial post-validated correction is not a Core change, and cannot be safely or truthfully represented by that reason.
4. No legitimate revalidation path for the accepted PDF remained under frozen Core. Old `publication-candidate-v2.json` identifies a different outdated PDF. Old checkpoint must not be rewritten or pretended to bind the revised PDF.
5. Therefore normal Publication Candidate → formal Human Preview → Freeze → Release could not proceed with the approved bytes.

## One-off exceptional disposition (authorized by Human Owner)

- Human approval record: `sources/SP-vision-multimodal-2026/execution/reader-paper-fidelity-repair-20261009/human-editorial-pdf-approval-20261010.md`.
- Defect [Issue #560](https://github.com/eariver/japanese-generative-ai-survey/issues/560) filed OPEN.
- Frozen exact PDF/TeX/Bib/style recorded under `sources/SP-vision-multimodal-2026/publication/exception-20261010/freeze-manifest.json`; source commit `84457925f11b5d883960f8ec07419f8b8c28a3e4`.
- PR [#561](https://github.com/eariver/japanese-generative-ai-survey/pull/561) merged to `main` at `3b0087220ee002c890437297c5a038d1f2a156f9`, with **the same approved PDF Git blob** `162ddec09b0f9e674da97282dced2aa8c447ba5a`.
- [GitHub Release `special/vision-multimodal-2026`](https://github.com/eariver/japanese-generative-ai-survey/releases/tag/special/vision-multimodal-2026) publicly published exact 708782-byte asset; GitHub sha256 and independent workflow download-verify are `b2de84493f2215e26d16e569498c5f4b6476ebc314230cbb4e01540a72742093`.
- [Workflow run 37955511006](https://github.com/eariver/japanese-generative-ai-survey/actions/runs/37955511006): `completed/success`.
- Exception-specific `release-record.json` under the same publication/exception directory is `EXCEPTION_RELEASED`. This is **not** a canonical Core v2 `RELEASED` state.
- All accepted research, Human review, reader and QA provenance remain in edition source; no shared Core code/schema/config changes; no new branch, reset or force push.
- Production State intentionally remains `VALIDATED_DRAFT`; `publication_preview` remains pending; old stage checkpoint remains immutable.

## Long-term repair

Generic solution belongs to consolidated Core v2 maintenance, not TS-003 production: allow trustworthy post-validated reader/editorial correction reason; require immutable supersession, fresh PDF/reader QA SHA binding, genuine Human decision, re-bound Candidate, and exact-byte Freeze/Release. Include Weekly and Special positive/negative/forgery/idempotency regressions.

This is a **completed edition-specific exception** with an **unfixed generic shared-Core defect**; `CORE_FIXED` is prohibited until reviewed Core maintenance and regressions establish it.
