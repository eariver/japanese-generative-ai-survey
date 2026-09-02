# W33 Publication Preview r2 Single-Boundary Cleanup to Next Human Gate — Luna Handoff r1

## Purpose

Execute the Owner's explicit Publication Preview r2 `REQUEST_CHANGES` decision as one bounded repair-and-rematerialization task.

There is exactly one authorized substantive publication edit:

`surveys/weekly/2026-W33/references.bib`, entry `voicedesigner`, `note` field.

Replace:

`Paper metadata; baseline and evaluation details remain unresolved in the accepted capture.`

with exactly:

`Paper metadata; baseline and evaluation details could not be confirmed from the available primary material.`

After that exact repair, rebuild and revalidate the exact publication authority and return canonically to the next pending Publication Preview Human Gate.

This is not a content rewrite, architecture revision, drafting pass, or layout redesign.

## Repository authority and start guard

- Repo: `eariver/japanese-generative-ai-survey`
- Branch: `weekly/2026-W33-v2-work`
- Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Use the Exact Starting SHA supplied by the external caller as the only permitted starting branch HEAD.

Before any GitHub write:

1. fetch the remote HEAD of `weekly/2026-W33-v2-work`;
2. require exact equality with the caller-supplied Exact Starting SHA;
3. if unequal, make no GitHub write and stop with the actual remote HEAD.

Do not create any new branch or fallback branch.

## Mandatory authority read order

Read, in this order, before any write:

1. `sources/2026-W33/execution/reviews/w33-owner-publication-preview-decision-20260901-r2.md`
2. `sources/2026-W33/execution/reviews/w33-publication-preview-r2-single-boundary-cleanup-sol-review-20260901-r1.md`
3. `sources/2026-W33/production-state.json`
4. `sources/2026-W33/publication/v2/publication-candidate-v2.json`
5. `sources/2026-W33/gates/reviews/publication-r1.json`
6. current Core contract/operator implementation required for `REQUEST_PUBLICATION_PREVIEW_REVISION` and both later `ADVANCE_STAGE` transitions
7. `surveys/weekly/2026-W33/references.bib`
8. `surveys/weekly/2026-W33/main.tex`
9. all current `surveys/weekly/2026-W33/sections/*.tex`
10. current publication validation authorities under `sources/2026-W33/publication/v2/`

The Human decision is already made. Do not reinterpret it.

Required Owner decision:

`REQUEST_CHANGES — remaining finding: 1`

Required Sol disposition:

`ACCEPT_HUMAN_REQUEST_CHANGES / SINGLE_READER_BOUNDARY_FINDING / EXACT_ONE_LINE_REPAIR_AUTHORIZED / RETURN_TO_PUBLICATION_PREVIEW`

## Starting-state verification

At the Exact Starting SHA, re-fetch rather than blindly trusting historical values.

The expected compatible state is:

- `lifecycle_state = RELEASE_CANDIDATE`
- `next_action = PUBLICATION_PREVIEW`
- `terminal_reason = HUMAN_GATE_REACHED`
- validation checkpoint = `passed`
- Publication Preview = `pending`
- Publication Preview approval provenance = `null`
- freeze = `pending`
- release = `pending`
- exception gate inactive

The expected current candidate is the r2 candidate reviewed by Owner, historically:

- candidate payload SHA-256 `d8edb38eb1c84476e24219caeae7a1fd4fac5bb3b39f1c0cee3bf9940b1e312b`
- PDF SHA-256 `13dbc6b2637e5097f82962e6e23413865e04c9a4ae5be035414d594ae19c18ce`
- page count `11`
- byte count `274435`

These are comparison values only. Re-fetch the actual current candidate and state at the Exact Starting SHA. If the candidate or state has changed unexpectedly before this task, stop rather than guessing.

## Phase 1 — materialize Human Publication Preview r2 revision

Use the canonical Core operation:

`REQUEST_PUBLICATION_PREVIEW_REVISION`

with:

- expected revision: `2`
- decision: `REQUEST_CHANGES`
- reviewed_by: `Owner`
- review reference: `sources/2026-W33/execution/reviews/w33-owner-publication-preview-decision-20260901-r2.md`
- regeneration boundary: `DRAFT_COMPLETE`
- reviewed_repository_commit_sha: the caller-supplied Exact Starting SHA

The request-only commit must be a normal non-force child of the Exact Starting SHA.

The request must describe only the single remaining boundary defect and the exact one-line replacement. It must not broaden the change request to other sections or content.

Run the canonical trusted-operator bridge and require:

- preflight PASS;
- execute PASS;
- exactly one Publication Preview revision-2 record;
- exactly one rollback to `DRAFT_COMPLETE` according to Core semantics;
- resulting `sources/2026-W33/gates/reviews/publication-r2.json` with `decision = REQUEST_CHANGES`;
- `regeneration_boundary = DRAFT_COMPLETE`;
- reviewed repository commit binding correct according to the current operator contract.

After rollback, verify:

- lifecycle = `DRAFT_COMPLETE`;
- validation = `pending`;
- Publication Preview = `pending`;
- freeze/release = `pending`;
- approval provenance = `null`;
- Architecture/Draft authority remains valid and unchanged.

If this phase fails, stop. Do not edit the bibliography before a valid rollback.

## Phase 2 — exact single-line bibliography repair

Edit only:

`surveys/weekly/2026-W33/references.bib`

and only the `voicedesigner` note field.

Required exact old text:

`note = {Paper metadata; baseline and evaluation details remain unresolved in the accepted capture.}`

Required exact new text:

`note = {Paper metadata; baseline and evaluation details could not be confirmed from the available primary material.}`

Require the old text to occur exactly once before replacement.

After replacement, require:

- old exact string occurrences = `0`;
- new exact string occurrences = `1`;
- no other substantive `references.bib` change.

The following reader source must remain byte-identical to the Exact Starting SHA:

- `surveys/weekly/2026-W33/main.tex`
- every file in `surveys/weekly/2026-W33/sections/*.tex`

Do not alter:

- section ordering;
- section content;
- 11-page design intent;
- two-column body layout;
- tables;
- theme boxes;
- claim-boundary boxes;
- Week in Review;
- Sources & limitations;
- citation set;
- bibliography keys;
- any other bibliography record.

Do not change shared Core, style files, schema, or workflow.

## Phase 3 — canonical Weekly CI rebuild

Commit the exact bibliography-only reader-source repair normally and non-force.

Use the existing canonical workflow:

`.github/workflows/build-weekly-survey.yml`

Identify the build run for the exact repair source commit.

Require:

- workflow conclusion `success`;
- LuaLaTeX build success;
- final TeX warning gate PASS;
- no undefined citation/reference;
- no publication-blocking Overfull/Underfull/missing-character failure according to the workflow contract.

Do not switch to a different build toolchain or generate an authoritative local PDF when the canonical CI workflow succeeds.

If CI fails, diagnose only whether the exact one-line bibliography change caused an escaping/syntax issue. Do not rewrite reader content or layout autonomously. If a repair beyond mechanical syntax is needed, stop and report.

## Phase 4 — exact PDF authority

Retrieve the successful workflow artifact containing:

- `main.pdf`
- `main.pdf.sha256`

Independently verify:

1. bundled checksum value;
2. independent SHA-256 of `main.pdf`;
3. equality between the two.

The new PDF SHA is expected to differ from the r2 PDF because bibliography bytes changed. Do not assume any exact new digest in advance.

Require exact PDF page count = `11`.

The Owner explicitly accepted the current 11-page structure. If the build becomes anything other than 11 pages, stop for review rather than attempting layout edits.

Pin the exact artifact PDF bytes without mutation to:

`surveys/weekly/2026-W33/main.pdf`

and the matching checksum file to:

`surveys/weekly/2026-W33/main.pdf.sha256`

Recompute the repository-pinned PDF SHA-256 and require equality with the artifact PDF SHA-256.

Record:

- workflow run ID/number;
- build job ID;
- artifact ID/name;
- artifact archive digest if available;
- exact PDF byte count;
- exact PDF SHA-256;
- Git blob SHA;
- page count.

## Phase 5 — all-page visual and reader-boundary review

Render all 11 pages of the exact pinned PDF and visually inspect them.

Require no regression in:

- clipping;
- overlap;
- missing glyph;
- broken columns;
- blank/duplicated pages;
- page flow;
- tables;
- boundary boxes;
- Week in Review;
- Sources & limitations;
- References truncation.

Specifically inspect the VoiceDesigner bibliography entry and confirm the new reader-facing note is visible and readable.

### Fail-closed production-language regression scan

Search and semantically inspect reader-facing TeX, bibliography, extracted PDF text, Week in Review, Sources & limitations, and References for inappropriate production use of:

- `candidate`
- `Evidence identity`
- `Profile Completeness`
- `LIMITED`
- `Screening`
- `HOLD_OUT`
- `DROP`
- `materiality`
- `SOCIAL_OBSERVATION`
- `Core v2`
- `accepted capture`
- `Grok_X_SourseIntake`

The required `accepted capture` occurrence count in reader-facing source/PDF is zero.

Do not mechanically delete innocent natural-language occurrences if they are not production metadata. Review semantic context.

If any previously fixed Issue #433 leakage has recurred, stop. Do not continue to validation/candidate advancement.

## Phase 6 — regenerate exact current validation authority

Regenerate the edition-local validation artifacts from the exact repaired source/bibliography/PDF bytes.

This includes at least:

- `sources/2026-W33/publication/v2/reader-manuscript-v2.json`
- `sources/2026-W33/publication/v2/deterministic/identifier-preservation.json`
- `sources/2026-W33/publication/v2/deterministic/pdf-preflight.json`
- `sources/2026-W33/publication/v2/deterministic/subject-entity-property-binding.json`
- `sources/2026-W33/publication/v2/quality-regression-bundle-v2.json`
- `sources/2026-W33/publication/v2/semantic-editorial-review-v2.json`
- `sources/2026-W33/publication/v2/visual-review-v2.json`
- any other current Core artifact required by the `DRAFT_COMPLETE` stage contract.

All hash-bound records must bind the new `references.bib` and new exact PDF authority as appropriate.

The Semantic/Editorial Review must explicitly record PASS for the Publication Boundary cleanup and confirm:

- the sole r2 finding is repaired;
- all previously accepted substantive sections remain unchanged;
- no previously fixed Issue #433 production-language regression is present;
- no fresh factual claim or new source was introduced.

The Visual Review must bind the exact new PDF and record the all-11-page inspection.

Do not reuse old hashes as current authority when underlying bytes changed.

Require:

- all canonical artifact validators PASS;
- current-stage validation PASS;
- canonical `DRAFT_COMPLETE` stage-contract validation PASS.

If any validation fails, stop before stage advancement.

## Phase 7 — advance to VALIDATED_DRAFT exactly once

Only after Phase 6 is fully PASS, create one canonical trusted-operator `ADVANCE_STAGE` request for:

`DRAFT_COMPLETE -> VALIDATED_DRAFT`

Bind the new repaired validation authority and the Sol review:

`sources/2026-W33/execution/reviews/w33-publication-preview-r2-single-boundary-cleanup-sol-review-20260901-r1.md`

Require:

- exactly one transition;
- preflight PASS;
- execute PASS;
- validation checkpoint materialized from the new exact source/PDF/review bytes;
- resulting State = `VALIDATED_DRAFT`;
- no reader source/PDF mutation during bridge execution.

If it fails, stop.

## Phase 8 — replacement Publication Candidate

Generate `sources/2026-W33/publication/v2/publication-candidate-v2.json` canonically from only the new current repaired authorities.

Do not reuse the r2 candidate payload SHA or old PDF/validation hashes.

Require canonical Publication Candidate validation PASS and status:

`READY_FOR_PUBLICATION_PREVIEW`

Record the new:

- Publication Candidate repository file SHA-256;
- candidate payload `candidate_sha256`;
- Reader Manifest SHA-256;
- source SHA-256;
- bibliography SHA-256 where recorded by authority;
- PDF SHA-256 and byte/page counts;
- Quality Bundle SHA-256;
- Semantic Review SHA-256/status;
- Visual Review SHA-256/status.

## Phase 9 — return to the next Publication Preview Human Gate

Only after replacement candidate validation PASS, create exactly one canonical trusted-operator `ADVANCE_STAGE` request for:

`VALIDATED_DRAFT -> RELEASE_CANDIDATE`

Require:

- exactly one transition;
- preflight PASS;
- execute PASS;
- Core receipt PASS;
- resulting lifecycle = `RELEASE_CANDIDATE`;
- `next_action = PUBLICATION_PREVIEW`;
- `terminal_reason = HUMAN_GATE_REACHED`;
- Publication Preview gate = `pending`;
- Publication Preview approval provenance = `null`;
- freeze = `pending`;
- release = `pending`;
- exception gate inactive.

This next gate is Publication Preview revision 3 for Human review purposes. Do not make the Human decision.

## Issue #433 and release boundary

Issue #433 must remain open.

Do not:

- close Issue #433;
- record Human `APPROVED` / `REQUEST_CHANGES` / `REJECT` for the new preview;
- freeze;
- release;
- merge.

## Allowed substantive source change

The only authorized substantive reader-source change from the Exact Starting SHA is the exact one-line `voicedesigner` bibliography note replacement.

Expected machine-generated changes may include:

- Human revision request/bridge artifacts;
- Production State/checkpoint changes caused by canonical rollback/advancement;
- `references.bib` one-line edit;
- exact new PDF/checksum;
- regenerated publication validation authorities;
- replacement Publication Candidate;
- operator requests/bridge outputs;
- one session record.

No other reader-facing `.tex` or bibliography content change is allowed.

## Session record

Create:

`sources/2026-W33/execution/sessions/w33-luna-publication-r2-single-boundary-cleanup-to-preview-20260901-r1.md`

Record at minimum:

- Exact Starting SHA;
- final remote HEAD;
- starting candidate payload SHA and PDF identity actually fetched;
- Publication Preview r2 revision materialization result;
- rollback result;
- exact old/new bibliography strings;
- exact changed reader-source paths;
- CI workflow run/job/artifact IDs and statuses;
- exact new PDF page count/byte count/SHA-256/Git blob;
- all-page visual review result;
- prohibited-production-language scan result;
- regenerated validation authority paths and hashes;
- semantic review status;
- visual review status;
- `DRAFT_COMPLETE` validation result;
- `DRAFT_COMPLETE -> VALIDATED_DRAFT` transition result;
- replacement candidate file/payload SHA-256;
- `VALIDATED_DRAFT -> RELEASE_CANDIDATE` transition result;
- final Production State;
- confirmation Issue #433 remains open;
- confirmation no freeze/release/merge/Human approval was performed.

## Required completion report

At successful stop, report:

- branch;
- final remote HEAD;
- new candidate payload `candidate_sha256`;
- PDF page count;
- PDF byte count;
- PDF SHA-256;
- semantic review status;
- visual review status;
- canonical validation result;
- CI result/run;
- final lifecycle/next_action/terminal_reason;
- Publication Preview pending/null provenance;
- exact changed reader-facing path list.

Normal successful stop token:

`PUBLICATION_PREVIEW_R3_GATE_MATERIALIZED`
