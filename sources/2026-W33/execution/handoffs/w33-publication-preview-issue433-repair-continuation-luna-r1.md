# W33 Publication Preview Issue #433 Repair — Luna Crash-Recovery Handoff r1

## Purpose

Resume only the unfinished tail of the Issue #433 reader/publication repair after the prior Luna/Work execution was interrupted by an unavailable local execution environment.

The canonical Publication Preview `REQUEST_CHANGES` decision, Core rollback to `DRAFT_COMPLETE`, reader-facing TeX repair, and canonical CI build have already completed on the remote branch. **Do not repeat any of them.**

This handoff exists to recover the exact successful CI PDF, pin it without mutation, complete exact-PDF visual and semantic review, regenerate the canonical `DRAFT_COMPLETE` validation authority set, validate it, record the resumed session, and stop for Sol review.

## Repository authority

- Repo: `eariver/japanese-generative-ai-survey`
- Branch: `weekly/2026-W33-v2-work`
- Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Core implementation: `02ba8323c80ac52ab407ff3199ed344907a170b2`
- Core orchestrator: `survey-production-core-v2/0.15-postintegration-transport-thematic`
- Last verified repair baseline before this handoff was added: `7081e136758b46efecc934dcb340fafe50ca209c`
- Use the **Exact Starting SHA supplied with the external invocation** as the only allowed starting remote HEAD.

Before any write, fetch the remote branch and require exact equality with the externally supplied Exact Starting SHA. If it differs, make no GitHub write, report the actual remote HEAD, and stop.

## Mandatory recovery reads

Read these before continuing:

1. `sources/2026-W33/execution/handoffs/w33-publication-preview-issue433-repair-luna-r1.md`
2. `sources/2026-W33/execution/reviews/w33-owner-publication-preview-decision-20260901-r1.md`
3. `sources/2026-W33/execution/reviews/w33-publication-preview-issue433-sol-review-20260901-r1.md`
4. GitHub Issue `#433` and its acceptance criteria
5. `sources/2026-W33/production-state.json`
6. `sources/2026-W33/gates/reviews/publication-r1.json`
7. `sources/2026-W33/gates/review-index.json`
8. the current reader source under `surveys/weekly/2026-W33/`
9. current `sources/2026-W33/publication/v2/**` only to identify stale pre-repair authorities that must be regenerated; do not treat their old hashes/review conclusions as current repair authority.

## Already-completed facts that must be verified, not repeated

At the exact starting remote state, verify all of the following. If any item is false, stop and report the mismatch rather than attempting to reconstruct history.

### Canonical Human Gate rollback

The previously completed request-only commit was:

`27c81d6c7063e44250216027398a73340a1d75fe`

It contains only:

`sources/2026-W33/execution/requests/w33-publication-preview-revision-20260901-r1.json`

The request records:

- operation `REQUEST_PUBLICATION_PREVIEW_REVISION`;
- `expected_revision = 1`;
- `reviewed_repository_commit_sha = 12a9cee3e077e78dd08bedc9eee1307bba0c5dc4`;
- `regeneration_boundary = DRAFT_COMPLETE`;
- Owner `REQUEST_CHANGES` decision.

The canonical Core execution commit was:

`064a9c0d3eb6fd049643d5891f58ac8934e8c112`

Its bridge result is PASS and the resulting Human Gate record is Publication Preview revision 1 = `REQUEST_CHANGES`.

Do **not** create another Human Gate request, another revision record, or another rollback.

### Current Production State

Require:

- `lifecycle_state = DRAFT_COMPLETE`;
- `next_action = stage:reader-publication-validation`;
- `human_gates.architecture_review = approved`;
- `human_gates.publication_preview = pending`;
- draft checkpoint = passed;
- validation checkpoint = pending with null provenance;
- publication preview checkpoint = pending;
- freeze/release = pending;
- no downstream `VALIDATED_DRAFT` or `RELEASE_CANDIDATE` history edge remains after rollback.

Do not advance the lifecycle during this handoff.

### Reader repair commits

The reader transformation repair commit is:

`d46196a36225b969adec6a5d971583ed22175188`

The subsequent TeX escaping correction is:

`7081e136758b46efecc934dcb340fafe50ca209c`

Treat the reader source at and after `7081e136...` as the current repair source. Do not rewrite it merely because the previous Luna session crashed.

If exact-PDF visual/semantic review reveals a genuine defect, make only the minimum edition-local reader-source correction necessary, then obtain a new successful canonical CI build and update all exact-PDF identities accordingly. Otherwise preserve the current source bytes and the already successful CI build below.

## Frozen semantic authority

Do not change or regenerate:

- Production Profile;
- Discovery / Screening / Evidence / Materiality / Completeness / Selection;
- Architecture / Architecture Review / Architecture approval;
- all seven Draft Packages;
- all seven Draft Results;
- Weekly Profile Synthesis Input/Result;
- shared Core, config, schemas, workflows, or survey style/template authority.

No fresh Web, X, Google Drive, raw-source, vendor, paper, or repository research is allowed.

## Exact successful CI authority

The canonical successful build already exists and should be reused rather than rebuilt when its artifact remains available and valid.

- Workflow: `Build weekly survey PDF`
- Workflow run number: `181`
- Workflow run ID: `33413283489`
- Head SHA: `7081e136758b46efecc934dcb340fafe50ca209c`
- Conclusion: `success`
- Build job ID: `99557967616`
- Final TeX publication-warning gate: PASS
- Final PDF page count: `11`
- Exact PDF SHA-256 recorded by the workflow: `13dbc6b2637e5097f82962e6e23413865e04c9a4ae5be035414d594ae19c18ce`
- Actions artifact ID: `9766114667`
- Artifact name: `japanese-generative-ai-survey-2026-W33`
- Artifact archive digest: `sha256:2ec504661478f5067713ede983e723b8dc4b725756bb44c561191b672e5678d3`

The ZIP/archive digest is **not** the PDF digest.

### Exact artifact recovery

1. Confirm run `33413283489` is still completed/success and bound to exact head SHA `7081e136...`.
2. Confirm artifact `9766114667` is still available and belongs to that run/head.
3. Download that exact Actions artifact ZIP through the authenticated GitHub artifact path/tool. Do not use an independently rebuilt PDF as a substitute while the exact artifact is available.
4. Extract `main.pdf` and `main.pdf.sha256` without modifying PDF bytes.
5. Require the bundled checksum to name the PDF SHA-256 as exactly:
   `13dbc6b2637e5097f82962e6e23413865e04c9a4ae5be035414d594ae19c18ce`.
6. Independently compute SHA-256 over extracted `main.pdf` and require the same value.
7. Require page count `11`.
8. Pin those exact bytes to `surveys/weekly/2026-W33/main.pdf` by normal non-force repository update. The repository currently may still contain the pre-repair PDF; replace it only with the exact CI artifact bytes.
9. After pinning, fetch/read back or otherwise independently hash the repository-pinned PDF and require exact SHA-256 `13dbc6...`.

If the artifact is unavailable, corrupt, or does not match the exact recorded PDF SHA, stop fail-closed. Do not invent, approximate, or silently regenerate authority. A fresh build is permitted only if the existing artifact genuinely cannot be used; if that happens, clearly record why the exact prior artifact could not be recovered, require a new canonical CI success, and bind every downstream authority to the new exact PDF hash.

## Exact-PDF all-page visual review

Render and inspect **all 11 pages** of the exact pinned PDF.

At minimum verify:

- no clipping, overlap, missing glyphs, blank/duplicated pages, broken columns, or bibliography truncation;
- headings, tables, claim-boundary boxes, page breaks, columns, and references are readable;
- the `Sources & limitations` heading renders correctly after the TeX escaping correction;
- Week in Review and References do not exhibit layout artifacts caused by the repair;
- no page exceeds the 24-page hard maximum (expected exact count is 11).

Record page-by-page review evidence in the replacement Exact-PDF Visual Review authority and the continuation session.

## Issue #433 semantic self-review

Canonical machine validation is necessary but not sufficient.

Re-read the current reader-facing source and the exact rendered PDF, especially:

- front matter;
- `Frontier Models & Access`;
- `Cyber Access & Governance`;
- Weekly Community Movement / community discussion passage;
- Week in Review;
- `Sources & limitations`;
- References.

Confirm that the repaired publication reports technical/news/community substance directly rather than explaining repository production mechanics.

Perform a fail-closed scan plus semantic review for inappropriate reader-facing production uses of:

- `candidate`;
- `HOLD`, `REJECT`, `DROP`, `HOLD_OUT`;
- `Profile Completeness` or production-state `Completeness`;
- `Evidence identity`, `Evidence Card`;
- `Issue Synthesis`;
- `materiality`;
- pipeline-stage `Discovery` / `Screening`;
- `must-cover` / package placement;
- `Core v2` / checkpoint / bridge / operator;
- raw `Grok_X_SourseIntake` path;
- production-process wording such as `承認済みArchitecture`, `technical authority`, `確認資料`, or `記事では` when it merely narrates editorial mechanics.

Ordinary external/source-language use of a token is not automatically prohibited; judge whether it functions as internal production metadata. Any retained ambiguous token must be explicitly justified in the session.

The community passage must describe what was actually observed as bounded community discussion/attention while making clear that it is not proof of performance or technical capability. Do not add facts beyond the frozen accepted material.

## Regenerate only the current DRAFT_COMPLETE validation authority set

The files already present under `sources/2026-W33/publication/v2/` are largely pre-repair/stale after the canonical rollback. Regenerate the canonical validation authorities from the **current repaired reader source + exact pinned PDF**.

Regenerate, using current repository scripts/contracts and the same canonical semantics used for W33 before rollback:

- `sources/2026-W33/publication/v2/reader-manuscript-v2.json`;
- canonical deterministic authorities under `sources/2026-W33/publication/v2/deterministic/`;
- `sources/2026-W33/publication/v2/quality-regression-bundle-v2.json`;
- `sources/2026-W33/publication/v2/semantic-editorial-review-v2.json`;
- `sources/2026-W33/publication/v2/visual-review-v2.json`;
- any additional artifact that the current canonical `DRAFT_COMPLETE` stage contract requires **except Publication Candidate**.

Every regenerated authority must bind current exact source bytes and the exact pinned PDF SHA `13dbc6b2637e5097f82962e6e23413865e04c9a4ae5be035414d594ae19c18ce` unless a genuine defect forced a documented fresh CI build.

Do not carry forward stale pre-repair hashes or old visual/semantic conclusions merely to satisfy schema validation.

### Publication Candidate is explicitly excluded

Do **not** regenerate, modify, adopt, or use as current authority:

`sources/2026-W33/publication/v2/publication-candidate-v2.json`

It is downstream of the current stop boundary and remains stale/historical after rollback until Sol authorizes advancement. Its mere presence in the repository is not authority for this `DRAFT_COMPLETE` repair candidate.

## Canonical validation

After exact PDF pinning and regeneration of the validation authority set:

1. run the canonical current-stage validation for `DRAFT_COMPLETE`;
2. run the canonical `DRAFT_COMPLETE` stage-contract validation in read-only/check mode;
3. require all deterministic checks to PASS;
4. require the Issue #433 semantic/editorial self-review to PASS;
5. require the exact-PDF visual review to PASS;
6. confirm Production State is still exactly `DRAFT_COMPLETE` with validation/publication-preview pending.

Do **not** materialize a new `DRAFT_COMPLETE -> VALIDATED_DRAFT` checkpoint/transition in this handoff. A successful stage-contract check is preparation for Sol review, not permission to advance.

## Continuation session record

Create one new session record, preferably:

`sources/2026-W33/execution/sessions/w33-luna-publication-issue433-repair-continuation-20260901-r1.md`

Record at minimum:

- external Exact Starting SHA and ending SHA;
- original repair baseline `7081e136...`;
- confirmation that rollback/request was not repeated;
- current Production State before/after;
- exact workflow run `33413283489`, build job `99557967616`, artifact `9766114667`;
- artifact ZIP digest and exact PDF SHA independently verified;
- exact PDF page count;
- repository pin result;
- all-page visual review result;
- Issue #433 semantic leakage scan/manual re-read result;
- hashes/paths of every regenerated current validation authority;
- canonical `DRAFT_COMPLETE` validation result;
- explicit statement that Publication Candidate was not regenerated and lifecycle was not advanced;
- any environment or tooling limitation encountered.

## Write boundary

Allowed writes for this continuation are limited to:

- exact PDF pin at `surveys/weekly/2026-W33/main.pdf`;
- `sources/2026-W33/publication/v2/**` validation authorities required at `DRAFT_COMPLETE`, excluding `publication-candidate-v2.json`;
- one continuation session under `sources/2026-W33/execution/sessions/`;
- minimal reader-source correction under `surveys/weekly/2026-W33/**` only if exact visual/semantic review reveals a genuine defect; any such correction requires a fresh canonical CI build and new exact-PDF binding.

Do not write:

- Human Gate request/review/index/state unless an unexpected authority inconsistency is being reported (normally zero such writes);
- Production Profile;
- research/evidence/selection/architecture/drafting authorities;
- shared Core/config/schema/workflow/template/style paths;
- Publication Candidate;
- validation checkpoint/state transition;
- freeze/release/merge authority.

## Stop boundary

Stop at `DRAFT_COMPLETE`.

Do not execute:

- `DRAFT_COMPLETE -> VALIDATED_DRAFT`;
- replacement Publication Candidate generation;
- `VALIDATED_DRAFT -> RELEASE_CANDIDATE`;
- Publication Preview approval/revision 2;
- freeze;
- release;
- merge.

Normal successful stop status:

`ISSUE_433_READER_TRANSFORMATION_REPAIR_READY_FOR_SOL_REVIEW`
