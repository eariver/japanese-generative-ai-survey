# Human-facing Publication Preview dossier — 2026-W36 r2

Sol-owned review surface for the pending Human Publication Preview r2. Read with the exact committed Candidate-bound PDF. No Publication Preview r2 decision is recorded in this run.

## 1. Exact review identity

- Edition `2026-W36` r2, WEEKLY + WEEKLY_MAGAZINE.
- Reviewed production commit SHA: `315d72805668ddf6d3f5d22085c0cad82aeee26c` (W36-branch commit containing exact State + Candidate + Candidate-bound PDF).
- Lifecycle `RELEASE_CANDIDATE`, next action `PUBLICATION_PREVIEW`, terminal `HUMAN_GATE_REACHED`.
- Canonical window unchanged: `[2026-08-28T18:00:00-04:00, 2026-09-04T18:00:00-04:00)` ET.
- Production Line `production/survey-core-v2 @ 774dd39a` (unchanged); reviewed `main @ 5acbff85`; no Core repairs.
- Execution contract: `execution/requests/sol-w36-resume-r2-with-issue-comment-citation-no-core-change-20260917.md` (NO_CORE_CHANGE, boundary `DRAFT_COMPLETE`, STOP at r2 PENDING).

## 2. Architecture approval provenance

- Architecture Review r1: `REQUEST_CHANGES` (boundary `SELECTION_COMPLETE`, reviewed `0295bd08`).
- Architecture Review r2: `APPROVED` (revision 2, reviewed `3e1e0fc3b802bf388e56486c638acba35b7bc2ae`, recorded `2026-09-17T00:09:00Z` by Human Owner).
- Immutable records: `gates/reviews/architecture-r1.json`, `gates/reviews/architecture-r2.json`, snapshot `gates/reviews/approvals/architecture-r2.json`, canonical `gates/architecture-approval.json`.
- Approved Architecture unchanged through drafting/publication (6 packages, 18 SELECTED / 1 HOLD).
- Publication Preview r1: `REQUEST_CHANGES` (revision 1, reviewed `c4ab0455`, boundary `DRAFT_COMPLETE`); preserved auditable in `gates/reviews/publication-r1.json` and `gates/review-index.json`. No r2 decision exists yet.

## 3. What changed since the blocked r2 state (and what did not)

- Changed (only reader-facing citation target): `surveys/weekly/2026-W36/references.bib` `w36community` URL from `https://github.com/eariver/japanese-generative-ai-survey/blob/188f5acc0cfd97885e3b110b565a57d31e13ff3c/surveys/weekly/2026-W36/community-observation.md` to `https://github.com/eariver/japanese-generative-ai-survey/issues/502#issuecomment-5716020666` (accepted 15 X URLs + context-only boundary, no internal paths). New bib SHA `fe650393214d61ccf19cce6838541795be1dfb4b2d43be423538bc0d1a4de03d` (8980 bytes).
- Removed from active publication input: `sources/2026-W36/publication/v2/reader-surface-suppressions-v2.json` (prior blob-permalink workaround; history preserved in git). Regenerated gate passes with zero suppressions.
- Preserved as audit artifact: `surveys/weekly/2026-W36/community-observation.md` (unchanged bytes).
- Preserved r1 repairs (#434/#500/#501/#502): no reader-facing HOLD/PARTIAL/revision-ID/promotion language; GLM-5.3 medium-confidence boundary with no same-week assertion; natural precise technical Japanese; NVIDIA/Hugging Face agreed/announced not closed; community observation context-only, never technical authority.
- Frozen upstream untouched: Discovery 19, Screening 19 KEEP, Evidence 13 VERIFIED / 6 PARTIAL, Materiality 18 MATERIAL / 1 CONTEXT, Selection 18 SELECTED / 1 HOLD; Architecture, approvals, Draft Packages/Results byte-identical.

## 4. Final package/section structure

1. Astra goes Critical, monitored → `sections/10-astra-critical-cyber.tex`
2. Fermat, checked by machine → `sections/20-fermat-proof.tex`
3. Open weights go full-lifecycle → `sections/30-open-efficient.tex`
4. Frontier coding, bounded → `sections/40-frontier-coding.tex`
5. The agent harness plane advances → `sections/50-agent-harness.tex`
6. Platforms, space, and pixels → `sections/55-ecosystem-spatial-media.tex`
7. Week in Review synthesis (no new facts) → `sections/60-week-in-review.tex`

Frontmatter (`00`) + Sources & limitations (`99`) + `references.bib` (18 authorities) + `jgaisurvey.sty`.

## 5. Page count and layout

- PDF: `surveys/weekly/2026-W36/main.pdf`, 12 pages, 359750 bytes, unencrypted.
- SHA-256: `07defd592672f609b2b40041f3f3afcfb4918a78e2005a1cb3a7cbd0c7d346d1`.
- CI `build-weekly-survey` run `35294636439` success (artifact `10527815569`, digest `sha256:a92a79d1817a81cd979a28590952f7240077b11a2e010e8f8fad771331325218`, source build head `52bb2f6c9`); final-log warning gate PASS.
- Text extraction: 25563 chars, all sections present, Issue #502 comment URL present, no blob permalink, no HOLD/PARTIAL tokens, Japanese renders.

## 6. Reader-surface lexical/semantic results (suppression-free)

- Lexical scan: 11/11 TeX/Bib files PASS, zero blocking findings, zero suppressions.
- Pre-TeX semantic review: `publication/v2/reader-surface-semantic-review-v2.json` PASS (review SHA `8ab12b3facbf0075afd8dcfd57c173b68a6fb848f3e1fa3ed5ccab8599135f26`, pipeline independence + evidence-bound fidelity + community semantics + synthesis closure + transaction-status fidelity).
- Reader-surface gate: `publication/v2/reader-surface-gate-v2.json` PASSED (gate SHA `d0bdb619df1aa619dff7228edaa9f97c385647976170d475d60d5d539687b526`, 0 total / 0 blocking / 0 suppressed).
- Manuscript: `publication/v2/reader-manuscript-v2.json` (manifest SHA `199d450cc6bf266b45e7d8f1f30e954b2bba07842e063f4d156d145affd95292`, 20/20 coverage, validated via canonical `validate_manuscript_manifest`).
- Post-TeX semantic/editorial review: `publication/v2/semantic-editorial-review-v2.json` 11/11 PASS on exact new bytes.
- Visual review: `publication/v2/visual-review-v2.json` 2/2 PASS on exact PDF bytes.
- Quality bundle: `publication/v2/quality-regression-bundle-v2.json` (bundle SHA `702cd3b4ed63d81bb2d6a212310af0adb133e62adf894573c320220bd4f0788a`, 3/3 deterministic PASS).
- Stage validations: `execution/validation/reader-publication-stage-validation-r2.json` (DRAFT_COMPLETE→VALIDATED_DRAFT) and `execution/validation/publication-candidate-stage-validation-r2.json` (VALIDATED_DRAFT→RELEASE_CANDIDATE) both PASS; checkpoints `DRAFT_COMPLETE.json`, `VALIDATED_DRAFT.json` recorded.

## 7. Known non-blocking residual limitations

- Vendor figures publisher-only throughout; carried explicitly in prose and source notes.
- System-card pages, Fermat reruns, closing/regulatory outcomes, full license texts, and methodology pages not consumed; carried as explicit boundaries.
- FUSE abstract-only; GLM UTC-hour unresolved (medium-confidence boundary); H3 leaderboard date-bound.
- 12-page result retains all selected material with no content dropped.

## 8. Material deviations from approved Architecture

- None. Package order, membership, roles, thesis, must-cover requirements, and boundaries preserved. No Selection/Architecture change after r2 approval. Single edition-local bibliography URL swap plus downstream rebinding only; no Draft authority altered; no Core change.

## 9. Exact PDF/candidate authority

- Path: `surveys/weekly/2026-W36/main.pdf`
- SHA-256: `07defd592672f609b2b40041f3f3afcfb4918a78e2005a1cb3a7cbd0c7d346d1`
- Bytes: `359750`, pages: `12`, encrypted: `false`
- Candidate: `sources/2026-W36/publication/v2/publication-candidate-v2.json` (candidate SHA `8103f341bafa3ccc2f52c8b7d25024e7dc9b3843998c221fbcac99b0437e93b1`)
- Source: `surveys/weekly/2026-W36/main.tex` (`e6d98ccde634f0077ce547c7089f8da420ecbc9fe0d367bb1d29b4b103c898d3`, 1266 bytes + 9 sections + bib + style)

## 10. Human decision options (only now)

- `APPROVED` — record against the exact reviewed commit; continue to Freeze (not in this run).
- `REQUEST_CHANGES` — supply requested changes + one allowed boundary (`ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, or `VALIDATED_DRAFT` for publication-local; earlier boundary for upstream defect with cross-gate reopen).

---

## Reviewed authority

Same as §1 above; canonical machine Candidate: `sources/2026-W36/publication/v2/publication-candidate-v2.json`.

## Human decision

`PENDING` — none recorded. Valid: `APPROVED` / `REQUEST_CHANGES` only.

## Requested changes

None (no Preview r2 review performed yet).

## Regeneration boundary

None selected (no Preview r2 review performed yet).

## Shared-Core implication

None. No Core v2 change in this run; `main` and Production Line untouched and unmerged by design.
