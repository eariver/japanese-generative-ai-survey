# W35 execution instruction — Human Publication Preview r1 APPROVED through canonical Freeze and Release

Status: `EXECUTION_AUTHORITY / HUMAN_PUBLICATION_PREVIEW_R1_APPROVED / COMPLETE_W35_THROUGH_RELEASE`

Date: `2026-09-15 JST`

Repository: `eariver/japanese-generative-ai-survey`

Edition: `2026-W35`

Work branch: `weekly/2026-W35-v2-work`

## 1. Human decision authority

Human Publication Preview r1 decision:

`APPROVED`

Exact reviewed production authority:

`d1d6bdc6733b57013eb0dc6a06e97310dbfa74ac`

Publication Preview presentation shell:

`2dd0ceb350024ba49a2e9c2c773a20b12c40c1a9`

Exact approved Publication Candidate:

- path: `sources/2026-W35/publication/v2/publication-candidate-v2.json`
- candidate SHA-256: `3195f74c89a3c8e163f0f29cc0123132ecedd287f84c1467d9110d40167e2e8d`
- status: `READY_FOR_PUBLICATION_PREVIEW`

Exact approved PDF authority:

- path: `surveys/weekly/2026-W35/main.pdf`
- SHA-256: `6115f0a774a947a269426c46003d09c9e4f962f54d5043d3778a5b815591a1b2`
- bytes: `285365`
- pages: `8`
- encrypted: `false`

The Human explicitly approved the exact Publication Preview r1 after direct visual review. There are no requested changes and no regeneration boundary.

This instruction authorizes completion of W35 only. It does **not** authorize content regeneration, editorial rewriting, new research, Architecture changes, Selection changes, or Core repair.

## 2. Starting guard

The Muse invocation will provide an Exact Starting SHA equal to the commit that contains this execution request.

Before any repository/GitHub write, read-only verify all of the following:

1. remote `weekly/2026-W35-v2-work` HEAD == Exact Starting SHA supplied by the invocation;
2. Exact Starting SHA parent == `2dd0ceb350024ba49a2e9c2c773a20b12c40c1a9`;
3. the parent tree == `12eea3aa567b5a1b90285b0b5be72e609d3b074b`;
4. remote `main` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
5. remote `main` tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
6. remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
7. `main` and `production/survey-core-v2` are byte/topology-equivalent at this starting authority, so there is no Production-Line-only Core content to leak into `main`;
8. `sources/2026-W35/production-state.json` reports:
   - `lifecycle_state = RELEASE_CANDIDATE`
   - `human_gates.architecture_review = approved`
   - `human_gates.publication_preview = pending`
   - `next_action = PUBLICATION_PREVIEW`
   - `terminal_reason = HUMAN_GATE_REACHED`;
9. the exact Publication Candidate and PDF bytes match §1;
10. `sources/2026-W35/execution/reviews/publication-preview-r1.md` still reports `PENDING` before this Human decision is recorded;
11. no `weekly/2026-W35` release tag / public Release already exists unless the canonical release machinery explicitly identifies an idempotent continuation from the same exact frozen bytes.

If any non-idempotent guard differs, perform **zero repository/GitHub writes**, report expected versus actual, and STOP.

No force push, reset, rebase, squash, history rewrite, fallback branch, alternate W35 branch, repair branch, or content branch is authorized.

## 3. Mandatory read order

After the guard passes, read at minimum:

1. `sources/2026-W35/execution/reviews/publication-preview-r1.md`
2. `sources/2026-W35/execution/reviews/publication-preview-r1-dossier.md`
3. this execution request
4. `sources/2026-W35/publication/v2/publication-candidate-v2.json`
5. `sources/2026-W35/production-state.json`
6. `sources/2026-W35/gates/review-index.json`
7. `sources/2026-W35/gates/reviews/architecture-r2.json`
8. current `scripts/survey_human_gate_v2.py`
9. current canonical Freeze / Release helpers, stage validation, schemas, and release workflow under the exact reviewed Core implementation
10. W34 canonical closure records as procedural precedent only, especially the `RELEASE_CANDIDATE -> FROZEN -> RELEASED` authority chain; do not copy W34 hashes or timestamps.

The current Core contract is authoritative over historical W34 implementation details if they differ.

## 4. Phase A — record Human Publication Preview r1 APPROVED

Record the explicit Human decision using the canonical Human Gate round-trip protocol. Do not hand-author an approval record if the canonical helper can generate it.

Required semantics:

- gate: `PUBLICATION_PREVIEW`
- revision: `1`
- decision: `APPROVED`
- reviewed repository commit: `d1d6bdc6733b57013eb0dc6a06e97310dbfa74ac`
- reviewed artifacts: exact current Publication Preview gate inputs, including the exact Candidate-bound PDF
- reviewed-by: `Human Owner`
- review reference: this execution request / Human approval represented by this request
- requested changes: none
- regeneration boundary: none

After recording, verify all generated immutable review/index/approval authorities and verify that Publication Preview is approved against the exact bytes in §1.

Do not reinterpret the approval as permission to alter publication content.

## 5. Phase B — canonical Freeze

Using the current canonical Freeze procedure only:

1. freeze the exact Human-approved W35 Publication Preview bytes;
2. produce/validate the canonical freeze record, release manifest, stage validation, and checkpoint authorities required by current Core;
3. preserve exact approved PDF/source/Candidate bytes;
4. advance only `RELEASE_CANDIDATE -> FROZEN`;
5. establish release identity `weekly/2026-W35` as required by the current contract;
6. create a normal commit on `weekly/2026-W35-v2-work` and non-force push;
7. remote read-back the frozen branch HEAD/tree and all freeze authorities.

At the FROZEN point, verify again that the PDF SHA-256 remains exactly:

`6115f0a774a947a269426c46003d09c9e4f962f54d5043d3778a5b815591a1b2`

and remains exactly 285365 bytes / 8 pages.

Any content-byte drift is a hard STOP.

## 6. Phase C — pre-integration guard and frozen W35 integration to main

Immediately before integrating W35 to `main`, read-only verify again:

- remote `main` is still exactly `774dd39a951c9ac3818e83dfffd4c7666efb0a20` unless the only change is an explicitly recognized idempotent continuation of this same execution;
- remote `production/survey-core-v2` is still exactly `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- no Production-Line-only Core commit exists;
- the W35 work branch is FROZEN and its release bytes exactly match §1.

If `main` or Production Line moved for any unrelated reason, STOP before merge and report the new SHAs. Do not silently rebase or update the release basis.

If the guard passes, follow the established W34-style release topology under the current contract:

- open/integrate the frozen `weekly/2026-W35-v2-work` authority into `main`;
- use a **merge commit**, not squash or rebase;
- preserve the frozen W35 parent lineage;
- verify the merge commit parents and tree;
- verify that the merged `main` contains the exact frozen W35 PDF/Candidate/release manifest bytes.

Do not merge any post-freeze mutable W35 content.

## 7. Phase D — canonical public Release and exact-byte reconciliation

Use the current canonical release workflow/helper for `weekly/2026-W35`.

Required public identity:

- release/tag identity: `weekly/2026-W35`
- release target: the exact `main` merge commit that integrated the frozen W35 authority, unless the current canonical contract explicitly requires a different target; if so, STOP and report before creating the release rather than guessing
- released PDF bytes: exact SHA-256 `6115f0a774a947a269426c46003d09c9e4f962f54d5043d3778a5b815591a1b2`, 285365 bytes

After the public Release is created, independently read back:

- tag/ref target;
- GitHub Release target/identity;
- attached/downloaded PDF asset bytes;
- release manifest identity;
- merge verification authority.

The public asset must reconcile exactly to the frozen manifest and approved PDF. Filename differences permitted by the canonical workflow do not permit byte differences.

If an already-existing `weekly/2026-W35` identity is found, only continue if canonical idempotency checks prove it is the same exact intended target and bytes. Otherwise STOP without overwriting or deleting it.

## 8. Phase E — canonical RELEASED provenance

After exact public release reconciliation, use the current repaired Core `FROZEN -> RELEASED` checkpoint/release procedure.

Required terminal semantics:

- lifecycle: `RELEASED`
- terminal reason: `COMPLETE`
- release checkpoint: passed
- public release exact-byte reconciliation: passed
- release record and merge-verification authorities present and valid
- Human Architecture r2 approval provenance retained
- Human Publication Preview r1 approval provenance retained
- exact PDF authority unchanged

Follow the current canonical topology for where RELEASED provenance is committed. W34 used the post-merge main lineage; do not move the frozen W35 work branch away from its frozen authority merely to imitate a branch shape if the current Core contract does not require it.

## 9. Production Line handling

Do **not** invent a Production Line move solely to make branch SHAs equal.

After W35 release completion, inspect the repository's current documented Production Line synchronization semantics:

- if the canonical release/production policy explicitly requires advancing `production/survey-core-v2` to the newly reviewed/released `main` and it is a clean sanctioned fast-forward/merge with no exclusive Production-Line history loss, perform that exact documented step and read it back;
- if release-time Production Line synchronization is not explicitly required, leave the Production Line unchanged and report its final SHA for the next W36 initialization decision.

No force update or history rewrite of Production Line is authorized.

## 10. Core-defect rule

The Publication Preview dossier noted one non-blocking observation concerning the experimental weekly semantic renderer versus the canonical manual-authoring/reader-binder path. That observation is **not** authorization for a Core repair during W35 closure.

If the current canonical Human Gate / Freeze / Release machinery itself fails because of a genuine shared-Core defect:

- do not patch Core on the W35 branch;
- do not invent a workaround that forges provenance;
- preserve the last valid W35 authority;
- report the exact failing contract, command, artifact, and safe frontier;
- STOP for Sol ruling.

## 11. Final audit

Before declaring W35 complete, report and verify at minimum:

- starting execution-request SHA/tree;
- Publication Preview r1 approval record + immutable approval snapshot;
- frozen W35 branch HEAD/tree;
- exact frozen PDF SHA/bytes/pages;
- freeze record and release manifest SHAs;
- PR number used for frozen W35 integration, if applicable;
- exact `main` integration merge SHA and both parents;
- public tag `weekly/2026-W35` target SHA;
- public Release identity and downloaded asset SHA/bytes;
- release record / merge verification / FROZEN checkpoint authorities;
- final canonical lifecycle `RELEASED` and `terminal_reason = COMPLETE`;
- final `main` HEAD/tree;
- final `production/survey-core-v2` HEAD/tree and whether it moved under a documented rule;
- final frozen `weekly/2026-W35-v2-work` HEAD/tree;
- changed paths for each closure phase;
- confirmation that no force push, rebase, squash, reset, history rewrite, fallback branch, unreviewed content regeneration, or unauthorized Core repair occurred.

## 12. Stop condition

Normal success is **W35 fully RELEASED and COMPLETE**, with exact approved PDF bytes publicly reconciled and all canonical provenance/checkpoints valid.

Do not stop merely at FROZEN if the canonical release path is healthy.

Do not start W36 in this execution.
