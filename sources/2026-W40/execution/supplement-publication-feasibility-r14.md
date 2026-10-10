# W40 r14 supplement-publication feasibility — corrected evidence-bound topology (F01/F05)

Status: `STUDY_ONLY_R14 / NO_RELEASE / NO_APPENDIX / NO_EXCEPTION_REQUEST`
Supersedes as working analysis (r13 study preserved immutable as prior historical
finding — no invisible replacement): `execution/supplement-publication-feasibility-r13.md`
Reviewed Core: main `afdb3df3faa20af3bb5798be429bba8dbd2100b1` (read, NOT modified).
State: `EVIDENCE_REVIEWED`. This study authorizes NOTHING; outcome may remain
`NO NORMAL SUPPLEMENT_PATH_ESTABLISHED`. No public release or exception request is made.
Addresses W40-R13-F01 (MAJOR) + F05 (MODERATE).

## 0. What r13 got wrong and what stands

- WITHDRAWN: "Release workflow enforces exactly-ONE asset" (r13 §1/§3). The workflow
  counts assets whose name equals the expected `ASSET_NAME`, not total assets (§1 below).
- WITHDRAWN as categorical: any implication that a second file "cannot" exist on a
  Release. Technically-present ≠ Core-authorized (§1, §5 tables).
- WITHDRAWN: "ad hoc PDF appendices" as the only Path-B shape; the precise bars are
  B1–B6 below with line-cited static rules.
- STANDS (re-cited, not replaced): HOLD-bar on SELECTED, SELECTED-only architecture,
  single-source/single-PDF candidate, single-identity release, TS-003
  non-transferability, Path-C bundled-goal result.

## 1. Static rule evidence (exact locations)

- R1 release assets: `.github/workflows/survey-production-v2-release.yml:168-171` —
  `meta` lists release assets; `asset_count` = count of assets with
  `.name == $ASSET_NAME`; upload iff `0`, fail iff `!= 1` ("ambiguous duplicate assets
  named ${ASSET_NAME}"). There is NO guard on total asset count. A differently named
  second asset is therefore TECHNICALLY co-hostable; the workflow assigns it ZERO
  approval semantics (no SHA/byte verification lines 175-177 apply to it, no manifest
  binding line 96-98, no release-notes authority). Absence of a total-count guard is
  negative evidence only — it grants nothing.
- R2 supporting files: `schemas/reader-manuscript-v2.schema.json`
  `supporting_files.items.properties.role.enum = ["BIBLIOGRAPHY","STYLE",
  "SUPPORTING_SOURCE"]` — NO `SUPPLEMENT` role exists. `scripts/
  survey_reader_publication_v2.py:209-232` SHA/size-binds each supporting file and
  rejects duplicates; provenance of supporting TeX is build-input provenance, NOT
  publication authority for an unselected subject. A supplement PDF riding as
  `SUPPORTING_SOURCE` would be a mislabeled file, not an authorized supplement.
- R3 coverage keys vs prose: `_validate_manifest_semantics` (~236-248) rejects
  missing OR extra `(package_id, requirement)` coverage keys (exact-set equality).
  Reviewed-absence (negative evidence, stated as such): no routine in the reviewed
  module maps free-form `main.tex` sections back to coverage keys, and no quality
  `check_id` in `config/survey-production-v2.json:156-192` names prose-coverage
  scanning (deterministic checks: entity binding, identifier preservation, PDF
  preflight, etc.; semantic checks: why-this-issue, single-home, watchlist, carry-over,
  bibliography, revalidation — none is "all prose covered"). Unlabeled HOLD-derived
  prose MIGHT pass mechanical validation; catching it is a semantic-editorial/Human-Gate
  integrity requirement, not a Core syntax error. Machine gate ≠ editorial contract ≠
  Owner authority — the three must not be conflated in either direction.
- R4 architecture placement: `scripts/survey_architecture_v2_base.py:551-555` —
  `selected` built ONLY from assignments with `disposition == "SELECTED"`;
  `nonselected` excluded from packages. HOLDs cannot receive official roles,
  must-cover requirements, or normal W40 Primary subsections. (Selection bar:
  same file ~416-417, HOLD row cannot be SELECTED.)
- R5 candidate singularity: `scripts/survey_publication_v2.py::build_candidate`
  (79-160) / `validate_candidate` (160-227) — exactly ONE `source` + ONE
  repository-resident PDF + manuscript + quality bundle + SEMANTIC_EDITORIAL + VISUAL
  reviews, all SHA/byte-count cross-checked; `schemas/publication-candidate-v2.schema.json`
  has no appendix/sidecar/supplement slot (reviewed-absence).
- R6 release identity: `scripts/release_identity.py:18-26` — `ISSUE_ONLY`
  (`weekly/2026-W40`, fixed title, single `ASSET_NAME`); release workflow 93-98 binds
  manifest `release_identity` to the expected tag. A separate non-Core PDF has no entry
  point into this identity.
- R7 TS-003 boundary: one-time Human Owner exception for ALREADY-APPROVED corrected
  bytes (39pp PDF `b2de8449…`), post-`VALIDATED_DRAFT`, via Issue #560 + PR #561 +
  `EXCEPTION_FROZEN`/`EXCEPTION_RELEASED` records + run `37955511006`; normal State
  stayed `VALIDATED_DRAFT` with NO normal FROZEN/RELEASED claim
  (`docs/core-v2-deferred-maintenance-summary.md` CV2-DM-021). Standing authority for
  W40 content expansion: NONE (it never existed as such).

## 2. Path table (three explicit columns)

### Path A — independently authorized non-Core companion

| Column | Verdict + evidence |
|---|---|
| TECHNICALLY_POSSIBLE | YES. Nothing in Core prevents authoring standalone repo documents (r14 notes exist as such); GitHub can technically host extra release assets (R1 — no total-count guard). Avoid claiming "cannot physically upload": the bar is permission, not physics. |
| NORMAL_CORE_AUTHORIZED | NO. No ordinary contract covers a companion: no SUPPLEMENT role (R2), no manuscript/candidate/release binding for it (R5/R6), no review-record kinds for it. It would ship with ZERO Core guarantees. |
| EXPLICIT_HUMAN_OWNER_AUTHORITY_REQUIRED | YES — all of: (i) authorize a non-Core publication act; (ii) define its review process (which QA kinds? semantic/editorial + visual?); (iii) define labeling/hosting with confusion controls; (iv) accept canonical W40 stays 28-item; (v) accept skew vs later Core-superseded P6a sections. NONE preapproved. Reader completeness of W40 itself: NOT cured (companion is detached, unverifiable as "W40"). |

### Path B — ordinary W40 published supplement (HOLD subjects inside Core publication)

| Column | Verdict + evidence |
|---|---|
| TECHNICALLY_POSSIBLE | PARTIALLY. Bytes can be typed into `main.tex`; mechanics alone may not catch unlabeled prose (R3 negative evidence). Stated WITHOUT endorsing: possibility ≠ permissibility. |
| NORMAL_CORE_AUTHORIZED | NO — six independent bars: B1 HOLD→SELECTED bar (R4); B2 SELECTED-only packages (R4); B3 coverage exact-set + authority chain (R3 — covered prose only); B4 single-source/single-PDF candidate, no appendix slot (R5); B5 single-identity release, second PDF unbound (R6/R1); B6 no pre-Architecture promotion op at EVIDENCE_REVIEWED (CV2-DM-022 three locks, `core-reentry-feasibility-r11.md`). |
| EXPLICIT_HUMAN_OWNER_AUTHORITY_REQUIRED | A W40 content-addition exception would need its own Owner Exception Gate (new issue + exact-byte freeze-pin + EXCEPTION records + no ordinary-path claim, TS-003-shaped). NOT preapproved, NOT requested, NOT recommended (TS-003 corrected approved bytes; it never authorized content expansion — R7). Do NOT infer authority from upload capability or from one past exception. |

### Path C — no normal reader-complete option

| Column | Verdict |
|---|---|
| TECHNICALLY_POSSIBLE | Moot: the goal is a Core-authorized reader-complete W40, not arbitrary bytes somewhere. |
| NORMAL_CORE_AUTHORIZED | NO. Neither A (wrong identity, zero guarantees) nor B (B1–B6) serves it ordinarily. |
| EXPLICIT_HUMAN_OWNER_AUTHORITY_REQUIRED | The bundled goal needs either (i) Issue-#562 Core supersession → bounded re-entry → Sol re-review → ordinary chain (DESIGNED route, pending in separate task), or (ii) new Owner exception (not requested), or (iii) Path-A companion authorization (does not complete W40). |

## 3. Outcome (unchanged conclusion, corrected reasoning)

**`NO NORMAL SUPPLEMENT_PATH_ESTABLISHED`** for a reader-complete Core W40 including
the two HOLD subjects. This is a contract result, not a materiality finding (Sol r11
MATERIAL direction stands; Core HOLD ≠ merit rejection) and not a release action.
Lawful continuations: noncanonical drafting (r14 notes/corrections/prep drafts), staged
coverage/outline work, and the separate #562 Core maintenance path. No upload, no
appendix, no post-approval edit, no SHA/provenance manufacture was performed or is
authorized by this study.
