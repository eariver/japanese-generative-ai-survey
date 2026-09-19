# W38 Publication Preview r2 — Independent Sol review

Status: `PASS / READY_FOR_HUMAN_PUBLICATION_PREVIEW`

Edition: `2026-W38`

Independent audit wall clock anchor: `2026-09-19T18:47:21+09:00` / `2026-09-19T09:47:21Z`

Human decision: `PENDING`

## 1. Exact reviewed authority

Fresh Human Publication Preview r2 binds:

- reviewed repository commit: `a55ac5b929221bd133d8a4b819bf960d2104d6c7`
- Publication Candidate SHA-256: `8aeb4dc4f959096708186ee338e11f518dd5a2f8c31f7a7757ec9f0278bcbe3f`
- exact PDF:
  - path: `surveys/weekly/2026-W38/main.pdf`
  - SHA-256: `3829c1660b55dbe808b3dec2ee14535bbba60ec6e5268f9a91276b71fae54933`
  - bytes: `347330`
  - pages: `11`
  - CI run: `35432581167`
  - artifact: `10581840234`
- r2 preview shell:
  - `sources/2026-W38/execution/reviews/publication-preview-r2.md`
- r2 preview dossier:
  - `sources/2026-W38/execution/reviews/publication-preview-r2-dossier.md`

The r2 preview shell was generated at `2026-09-19T08:44:27Z`.
The candidate commit is `a55ac5b929221bd133d8a4b819bf960d2104d6c7`, committed at `2026-09-19T08:44:23Z`.
The shell/dossier containing commit is `5a586f40430ce2b17fac98ff415dbb655c3a9017`, committed at `2026-09-19T08:45:47Z`.

The chronology is valid: candidate -> review generation -> containing commit.

## 2. Human r1 REQUEST_CHANGES provenance

Canonical Publication Preview r1 Human decision is valid:

- gate: `PUBLICATION_PREVIEW`
- revision: `1`
- decision: `REQUEST_CHANGES`
- reviewed commit: `f2306ce407a6dc5c79e0125e3c5e8f49f04bba61`
- reviewed_at: `2026-09-19T08:00:23Z`
- regeneration boundary: `ARCHITECTURE_ESTABLISHED`
- requested changes:
  - Issue #511 TypeSafe/Jev temporal-authority correction;
  - Issue #512 full 25-row community-ledger reader auditability.

Architecture approval remains valid and unchanged.

## 3. Issue #511 independent verification

Finding: `PASS / ACCEPTANCE CRITERIA SATISFIED`

Independent Sol web re-read of the current first-party TypeSafe page confirms the visible page header:

`Company News — Sep 14, 2026`

for:

`Introducing System One Models and Jev`

The page body also states that TypeSafe is releasing the first System One Model “today” and that Jev is available “today” in early access.

The repaired edition correctly models two distinct authorities:

1. TypeSafe first-party blog displayed publication date:
   - `2026-09-14`
   - precision: day-level
2. founder/creator public launch announcement:
   - direct X status: `https://x.com/CompleteSkeptic/status/2099925682726002904`
   - Snowflake UTC independently recomputed by Sol:
     `2026-09-15T18:17:52.151Z`

These are no longer silently collapsed.

### #511 artifact verification

Append-only collector correction exists:

`sources/2026-W38/collectors/primary/corrections/typesafe-jev-temporal-correction-20260919.md`

Evidence temporal supplement exists:

`sources/2026-W38/evidence/v2/corrections/typesafe-jev-temporal-correction-r1.json`

The historical original collector bytes are preserved.

The approved Architecture bytes remain unchanged.

Reader-facing outputs now consistently state:

- TypeSafe blog: `9月14日付`
- founder launch announcement: `9月15日`

The TypeSafe bibliography entry explicitly binds the blog to Sep 14 and separately cites the Sep 15 founder launch post.

Independent PDF extraction confirms the corrected temporal model appears in the exact r2 PDF.

Both Sep 14 and Sep 15 remain within the W38 ordinary window, so event identity, materiality, selection and package identity remain unchanged.

No Architecture reopen is required.

## 4. Issue #512 independent verification

Finding: `PASS / ACCEPTANCE CRITERIA SATISFIED`

Publication-facing manifest exists:

`surveys/weekly/2026-W38/community-observation-ledger.md`

It exposes exactly 25 public direct X rows and contains only reader-safe fields:

- row number;
- account;
- role;
- direct public X status URL;
- Snowflake UTC;
- temporal class.

It does not expose candidate IDs, Screening, Selection, Evidence state, lane IDs or worker-only provenance.

Verified totals:

- total: `25`
- `ORDINARY_WINDOW`: `23`
- `LATE_BREAKING`: `2`
- pre-window: `0`
- time-unverified: `0`
- ordinary unique accounts: `15`
  - independent: `7`
  - official: `3`
  - community: `5`

The stale raw-summary arithmetic `16 / 7+3+6` is not propagated.

A stable public mirror exists at Issue #512 comment:

`https://github.com/eariver/japanese-generative-ai-survey/issues/512#issuecomment-5740537184`

The Issue comment contains all 25 rows and the same 25/23/2 + 15=7+3+5 accounting.

The bibliography cites this public mirror as `w38x-ledger-manifest`.

The existing representative direct X citations remain present.

Reader-facing Source Notes state that the full 25-row breakdown can be audited through the cited public ledger.

Community posts remain explicitly context-only and are not used to establish technical specifications, performance, price, license, availability, safety, or source-publication date.

The deviation from the originally preferred commit-pinned blob URL is acceptable for this edition because the frozen reader-surface gate rejects `surveys/` repository URLs as internal-path leakage. The Issue-comment mirror provides the required public stable reader surface without Core v2 modification.

## 5. Architecture / scope verification

No shared-Core changes are present in the repair diff.

No changes were made under:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`

Remote protected authorities remain:

- `main = 2ab91516e89b8d706bfe143ebc0e435fa5735e7a`
- `production/survey-core-v2 = 774dd39a951c9ac3818e83dfffd4c7666efb0a20`

The approved Architecture remains seven packages in the same order.

Discovery / Screening / Materiality / Completeness / Selection / Architecture were not rerun.

## 6. Reader-surface / semantic audit

Worker checks report:

- semantic/editorial: `PASSED`
- visual: `PASSED`
- reader-surface gate: `PASSED`
- findings: `0`
- suppressions: `0`

Independent Sol read-back confirms:

- no Sep-15-only TypeSafe blog model remains in reader-facing publication;
- Sep 15 is explicitly labeled as founder launch announcement;
- exact 25/23/2 community ledger claim points to a reader-auditable public surface;
- X remains context-only;
- vendor-claim qualification remains intact;
- no internal pipeline vocabulary is exposed by the new manifest.

## 7. Exact PDF independent verification

CI artifact `10581840234` was independently downloaded by Sol.

Independent SHA-256 recomputation:

`3829c1660b55dbe808b3dec2ee14535bbba60ec6e5268f9a91276b71fae54933`

This exactly matches the Publication Candidate.

Independent PDF metadata:

- pages: 11
- bytes: 347330
- page size: A4
- encrypted: no

The exact PDF was independently rendered across all 11 pages at 160 DPI.

Findings:

- no clipping;
- no text overlap;
- no garbled Japanese glyphs;
- no broken citation/reference layout;
- Jev correction renders correctly;
- Sources & Limitations renders correctly;
- reference [20] exposes the public Issue #512 ledger mirror;
- p.8 closing-page behavior remains the previously accepted non-orphan pattern.

No visual blocker found.

## 8. Timestamp provenance

New r2 review surfaces are not future-dated.

- candidate commit: `2026-09-19T08:44:23Z`
- r2 review generation: `2026-09-19T08:44:27Z`
- containing preview commit: `2026-09-19T08:45:47Z`
- independent audit current-time anchor: `2026-09-19T09:47:21Z`

Ordering is valid.

The regenerated downstream Production State times are also no longer future relative to this audit.

Historical #507 correction authorities remain preserved.

## 9. Independent Sol verdict

Issue #511:

`VERIFIED_FIXED / MAY_CLOSE`

Issue #512:

`VERIFIED_FIXED / MAY_CLOSE`

Publication Preview r2:

`PASS / READY_FOR_HUMAN_PUBLICATION_PREVIEW`

Blocking findings: **0**

Human Publication Preview r2 decision remains:

`PENDING`

No Human approval is inferred by this review.
