# W36 execution instruction — Human Publication Preview r2 APPROVED through canonical Freeze and Release

Status: `EXECUTION_AUTHORITY / HUMAN_PUBLICATION_PREVIEW_R2_APPROVED / COMPLETE_W36_THROUGH_RELEASE / NO_CORE_CHANGE`

Date: `2026-09-18 JST`

Repository: `eariver/japanese-generative-ai-survey`

Edition: `2026-W36`

Work branch: `weekly/2026-W36-v2-work`

## 1. Human decision authority

Human Publication Preview r2 decision:

`APPROVED`

The Human Owner explicitly approved the exact W36 Publication Preview r2 after direct review of the candidate PDF and after reviewing the final issue comments for #434, #500, #501 and #502.

Exact reviewed production authority:

`315d72805668ddf6d3f5d22085c0cad82aeee26c`

Publication Preview r2 presentation shell / dossier commit:

`d7f1ae889a70ec99692032017ee6f55eda613f87`

Exact approved Publication Candidate:

- path: `sources/2026-W36/publication/v2/publication-candidate-v2.json`
- candidate internal SHA-256: `8103f341bafa3ccc2f52c8b7d25024e7dc9b3843998c221fbcac99b0437e93b1`
- candidate file SHA-256 used by stage authority: `4a8616b7a767daa4410b979bb72439f01b96b66be4382913bfd223b4f3baccad`
- status: `READY_FOR_PUBLICATION_PREVIEW`

Exact approved PDF authority:

- path: `surveys/weekly/2026-W36/main.pdf`
- SHA-256: `07defd592672f609b2b40041f3f3afcfb4918a78e2005a1cb3a7cbd0c7d346d1`
- bytes: `359750`
- pages: `12`
- encrypted: `false`

Approved reader-surface authority:

- Reader-Surface Gate: `PASSED`
- findings: `0`
- blocking findings: `0`
- suppressed findings: `0`
- active suppressions: none

The approval covers the exact bytes above. There are no requested changes and no regeneration boundary.

This instruction authorizes completion of W36 only. It does **not** authorize content regeneration, editorial rewriting, new research, Selection changes, Architecture changes, Draft changes, or shared Core v2 repair.

## 2. Final issue-review disposition

Before this approval, Human/Sol review confirmed the final comments on the four W36 issues:

- #434 — W36 artifact PASS; subtle semantic Publication Boundary phrasing is future shared-Core quality work only.
- #500 — W36 artifact PASS; temporal-confidence propagation invariant is future shared-Core hardening only.
- #501 — W36 artifact PASS; residual stylistic roughness is non-blocking; generic language-quality review is future work only.
- #502 — W36 artifact PASS; current public Issue-comment citation is sufficient for W36. Its mutability and future preference for immutable publication-facing provenance are future hardening only.

All four issues are closed as `completed`.

These comments are **not** authorization to change the approved W36 bytes during closure. Carry-forward items belong to later bounded Core/quality maintenance.

## 3. Frozen upstream authority and Core freeze

At the Human approval point:

W36 presentation-shell branch authority:
- branch: `weekly/2026-W36-v2-work`
- HEAD: `d7f1ae889a70ec99692032017ee6f55eda613f87`
- tree: `d52b453b57b2a57899ca8e5bff350e5caa92b8ef`
- parent: `315d72805668ddf6d3f5d22085c0cad82aeee26c`

Reviewed `main`:
- HEAD: `5acbff8528890ed9fc324c0227e6c4e43067c438`
- tree: `451fd7c6c6a9fcda59daa81fe484c62291e7d018`

Pinned Production Line:
- branch: `production/survey-core-v2`
- HEAD: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
- tree: `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

The Production Line is intentionally pinned for separate Core work. **Do not move or modify it in this W36 closure.**

No changes are authorized under shared-Core paths:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`

## 4. Starting guard

The Muse invocation will provide an Exact Starting SHA/tree equal to the commit that contains this execution request.

Before any repository/GitHub write, verify read-only:

1. remote `weekly/2026-W36-v2-work` HEAD/tree exactly equal the invocation values;
2. that starting commit parent equals `d7f1ae889a70ec99692032017ee6f55eda613f87`;
3. the parent tree equals `d52b453b57b2a57899ca8e5bff350e5caa92b8ef`;
4. remote `main` HEAD/tree still equal the values in §3;
5. remote `production/survey-core-v2` HEAD/tree still equal the values in §3;
6. W36 canonical state is still:
   - `lifecycle_state = RELEASE_CANDIDATE`
   - `human_gates.architecture_review = approved`
   - `human_gates.publication_preview = pending`
   - `next_action = PUBLICATION_PREVIEW`
   - `terminal_reason = HUMAN_GATE_REACHED`;
7. Publication Preview r1 remains auditable as `REQUEST_CHANGES` with boundary `DRAFT_COMPLETE`;
8. Publication Preview r2 shell/dossier still reports `PENDING`;
9. no newer Human Publication Preview decision exists;
10. exact Candidate/PDF bytes match §1;
11. Reader-Surface Gate still passes with zero findings and zero suppressions;
12. Architecture r2 remains `APPROVED`;
13. no `weekly/2026-W36` Git tag or public Release exists.

Any non-idempotent mismatch: perform zero repository/GitHub writes, report expected versus actual, and STOP.

No force push, reset, rebase, squash, history rewrite, fallback branch, alternate W36 content branch, repair branch, or unreviewed content regeneration is authorized.

## 5. Mandatory read order

After the guard passes, read at minimum:

1. `sources/2026-W36/execution/reviews/publication-preview-r2.md`
2. `sources/2026-W36/execution/reviews/publication-preview-r2-dossier.md`
3. this execution request
4. `sources/2026-W36/publication/v2/publication-candidate-v2.json`
5. `sources/2026-W36/production-state.json`
6. `sources/2026-W36/gates/review-index.json`
7. `sources/2026-W36/gates/reviews/publication-r1.json`
8. `sources/2026-W36/gates/reviews/architecture-r2.json`
9. current canonical Human Gate helper
10. current canonical Freeze helpers / schemas / stage validation
11. current `.github/workflows/survey-production-v2-release.yml`
12. W35 release closure and recovery PR #499 as procedural precedent for the known post-release CLI defect only.

Current Core contracts are authoritative. Do not copy W35 hashes, timestamps, release IDs, or W35 edition paths.

## 6. Phase A — record Human Publication Preview r2 APPROVED

Record the explicit Human decision using the canonical Human Gate round-trip protocol. Do not hand-author records if the canonical helper can generate them.

Required semantics:

- gate: `PUBLICATION_PREVIEW`
- revision: `2`
- decision: `APPROVED`
- reviewed repository commit: `315d72805668ddf6d3f5d22085c0cad82aeee26c`
- reviewed artifacts: exact r2 Publication Candidate and exact Candidate-bound PDF in §1
- reviewed by: `Human Owner`
- review reference: this execution request
- requested changes: none
- regeneration boundary: none

Preserve Publication Preview r1 as immutable `REQUEST_CHANGES`.

Expected gate artifacts include the canonical r2 review record, immutable approval snapshot, canonical publication-preview approval, and review-index update according to the current helper.

After generation, independently validate all hashes and ensure approval binds to the exact PDF/Candidate in §1.

Do not reinterpret approval as permission to change publication content.

## 7. Phase B — canonical Freeze

Using only the current canonical Freeze procedure:

1. freeze the exact Human-approved W36 r2 publication bytes;
2. build/validate canonical freeze record, release manifest, stage validation and checkpoint authorities required by current Core;
3. preserve exact approved PDF/source/Candidate bytes;
4. advance only `RELEASE_CANDIDATE -> FROZEN`;
5. establish release identity `weekly/2026-W36`;
6. normal commit on `weekly/2026-W36-v2-work` and non-force push;
7. remote read-back the frozen branch HEAD/tree and all Freeze authorities.

At FROZEN, verify PDF remains exactly:

`07defd592672f609b2b40041f3f3afcfb4918a78e2005a1cb3a7cbd0c7d346d1`

and exactly 359750 bytes / 12 pages.

Any approved-content byte drift is a hard STOP.

## 8. Phase C — frozen W36 integration to main

Immediately before integration, read-only verify:

- remote `main` still equals `5acbff8528890ed9fc324c0227e6c4e43067c438` / tree `451fd7c6c6a9fcda59daa81fe484c62291e7d018`;
- `production/survey-core-v2` remains exactly pinned at `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- W36 work branch is FROZEN;
- exact frozen bytes match §1;
- no W36 tag/Release exists.

If main or Production Line moved for an unrelated reason, STOP before merge. Do not rebase or silently change the release basis.

If guards pass:

- integrate the exact frozen `weekly/2026-W36-v2-work` authority into `main`;
- use a normal PR / merge commit, not squash or rebase;
- preserve frozen W36 parent lineage;
- verify merge parents and resulting tree;
- verify merged main contains exact frozen W36 PDF/Candidate/release-manifest bytes;
- do not merge any post-freeze mutable content.

No shared-Core files may be changed by the W36 integration.

## 9. Phase D — canonical public Release

Dispatch/use the current canonical release workflow for:

- issue: `2026-W36`
- release identity/tag: `weekly/2026-W36`
- target: exact main merge commit integrating frozen W36
- frozen Production State SHA: exact current FROZEN state
- Release Manifest SHA: exact current W36 manifest
- explicit confirmation required by workflow.

The public asset must reconcile exactly to:

- PDF SHA-256 `07defd592672f609b2b40041f3f3afcfb4918a78e2005a1cb3a7cbd0c7d346d1`
- bytes `359750`

Read back and verify:

- tag/ref target;
- GitHub Release target, title, draft/prerelease state;
- exactly one intended W36 PDF asset;
- downloaded asset SHA/bytes;
- merge-verification identity;
- release-manifest identity.

If an existing `weekly/2026-W36` identity is unexpectedly found, only continue if exact idempotency checks prove target and bytes are identical. Otherwise STOP; never overwrite/delete an ambiguous release.

## 10. Known release-workflow defect — bounded no-Core recovery authority

The current reviewed `main` still contains the known W35 defect in:

`.github/workflows/survey-production-v2-release.yml`

After exact public Release creation/reconciliation and after generating Release Record / Release Stage Checkpoint, the workflow invokes the nonexistent CLI:

`python scripts/survey_agent_control_v2.py --repo-root . validate-state --state "$STATE"`

This caused W35 canonical release run `34995268862` to fail after the public Release was already correctly published/reconciled.

**Do not repair this workflow or any shared Core path during W36 closure.**

If, and only if, W36 hits the same defect with all conditions below proven:

1. workflow reached the exact-byte Release creation/reconciliation step successfully;
2. public `weekly/2026-W36` Release exists on the intended main integration merge commit;
3. downloaded public asset exactly matches the frozen manifest and §1 PDF SHA/bytes;
4. failure is specifically the same nonexistent `validate-state` invocation after Release Record / checkpoint generation;
5. no earlier release or provenance validation failed;

then perform the same bounded edition-local recovery pattern accepted in W35 PR #499.

Recovery authority:

- do not rerun or recreate the public Release;
- create one recovery branch from the exact W36 integration main commit:
  `release-record/2026-W36-recovery-<workflow-run-id>`;
- use canonical helper functions / Python API `validate_agent_state()`, not the nonexistent CLI subcommand;
- regenerate/adopt only exact W36 release provenance from the already-reconciled public Release;
- expected changed-path envelope is exactly the W36 equivalents of the five W35 #499 files:
  1. `sources/2026-W36/orchestration/v2/checkpoints/FROZEN.json`
  2. `sources/2026-W36/production-state.json`
  3. `sources/2026-W36/publication/v2/core-stage-contract-v2.json`
  4. `sources/2026-W36/publication/v2/merge-verification-v2.json`
  5. `sources/2026-W36/publication/v2/release-record-v2.json`
- if any sixth path is required, STOP and report before writing it;
- absolutely no shared-Core path change;
- one normal commit, non-force push;
- open PR to `main`;
- verify the PR changed-path envelope and exact generated content;
- merge with normal merge commit;
- verify final main read-back.

If the failure differs materially from the known W35 defect, STOP for Sol review. Do not generalize this recovery authority to another failure mode.

## 11. Phase E — terminal RELEASED audit

Whether the normal workflow completes or the exact known-defect recovery is used, terminal W36 semantics must be:

- `lifecycle_state = RELEASED`
- `terminal_reason = COMPLETE`
- `machine_checkpoints.publication_preview = passed`
- `machine_checkpoints.freeze = passed`
- `machine_checkpoints.release = passed`
- Human Architecture r2 approval retained
- Human Publication Preview r1 REQUEST_CHANGES retained
- Human Publication Preview r2 APPROVED retained
- exact public asset reconciliation PASS
- exact approved PDF authority unchanged.

Verify the final release record, merge verification, FROZEN release checkpoint and production-state hashes.

## 12. Production Line handling

`production/survey-core-v2` is **frozen for this execution**.

Do not fast-forward it to W36 main.
Do not merge main into it.
Do not synchronize it after Release.
Do not modify any Core file.

Final Production Line must remain:

`774dd39a951c9ac3818e83dfffd4c7666efb0a20`

with tree:

`cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`

Any unexpected movement is a hard STOP.

## 13. Git discipline

Normal path:

- existing W36 work branch only through Freeze;
- normal PR/merge commit for frozen W36 integration;
- non-force pushes only.

The only new branch explicitly authorized is the narrowly-scoped `release-record/2026-W36-recovery-<run-id>` branch under the exact known-defect conditions of §10.

Forbidden:

- force push;
- reset/rebase/squash/history rewrite;
- fallback content branch;
- repair/review branch for W36 content;
- changing approved source/PDF/Candidate bytes;
- Core repair;
- inventing Human decisions;
- deleting/recreating a public Release to hide a failed provenance step.

## 14. Final audit report

Before declaring W36 complete, report:

- execution-request starting SHA/tree;
- Human Publication Preview r2 approval record + immutable snapshot + review-index result;
- frozen W36 branch HEAD/tree;
- exact PDF SHA/bytes/pages at approval and Freeze;
- freeze record / release manifest / FROZEN checkpoint identities;
- frozen W36 integration PR number;
- exact main integration merge SHA and both parents;
- public tag `weekly/2026-W36` target;
- public Release ID/URL/name/target/draft/prerelease state;
- public asset name/SHA/bytes;
- canonical release workflow run ID and result;
- whether §10 recovery was needed;
- if recovery used: recovery branch, PR, one commit, exact five changed paths, recovery merge SHA;
- final canonical lifecycle/terminal reason;
- final `main` HEAD/tree;
- final frozen W36 branch HEAD/tree;
- final Production Line HEAD/tree proving it did not move;
- explicit shared-Core changed paths = 0;
- explicit confirmation of no force/rebase/squash/reset/history rewrite and no approved-content regeneration.

## 15. Stop condition

Normal success is **W36 fully RELEASED and COMPLETE**, with exact approved PDF bytes publicly reconciled and canonical provenance committed.

Do not stop merely at FROZEN if the canonical release path is healthy.

If the known post-release `validate-state` defect occurs and §10 conditions are exactly satisfied, complete the bounded provenance recovery and then finish the terminal audit.

Do not start W37 in this execution.
