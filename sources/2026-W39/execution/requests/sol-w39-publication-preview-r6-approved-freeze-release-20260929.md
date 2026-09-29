# W39 execution instruction — Human Publication Preview r6 APPROVED through Freeze, main integration, and Release

Status: `EXECUTION_AUTHORITY / HUMAN_PUBLICATION_PREVIEW_R6_APPROVED / FREEZE_INTEGRATE_RELEASE / ISSUE551_CLOSURE / NO_CORE_CHANGE`

Date: `2026-09-29 JST`

Repository: `eariver/japanese-generative-ai-survey`

Work branch: `weekly/2026-W39-v2-work`

## 1. Human decision authority

The Human Owner explicitly reviewed W39 Publication Preview r6 after Independent Sol verification and decided:

`APPROVED`

This explicit approval authorizes the normal deterministic downstream sequence for the exact reviewed bytes: canonical Human Gate recording, Freeze, normal main integration, and public Release. It does **not** authorize any reader-visible, semantic, citation, source, bibliography, layout, or PDF-byte change after approval.

Canonical Human Gate `reviewed_at` must use the actual execution wall clock at recording time. Do not copy or synthesize an earlier stage timestamp.

Exact Human-reviewed r6 authority:

- reviewed repository commit: `98cffa3bbaf36801de1d7bcb8b2449cc0bb0b9d6`
- Publication Candidate SHA-256: `b042be85f0cf8b7f028ac8f7a96f7d2db6fc4f06acd256960a30f992d4975563`
- exact PDF:
  - path: `surveys/weekly/2026-W39/main.pdf`
  - SHA-256: `eb0e49233c8f7c04077d9abc04b2811a625597abda1c7340378b1c9f8cc3e121`
  - bytes: `335817`
  - pages: `12`
  - CI run: `36504726702`
  - artifact: `11006941649`
- Human-facing review: `sources/2026-W39/execution/reviews/publication-preview-r6.md`
- dossier: `sources/2026-W39/execution/reviews/publication-preview-r6-dossier.md`
- Independent Sol r6 review: Issue #551 comment `5881667114`, verdict `PASS / APPROVABLE`.

Issue #551 remains open at the start of this run and is to be closed only after successful Release and final read-back.

## 2. Mission

Complete W39 publication closure without changing approved bytes or Shared Core:

1. exact starting guards;
2. canonically record Human Publication Preview r6 `APPROVED` against the exact reviewed authority;
3. Freeze the exact approved Candidate/PDF bytes;
4. commit/push the FROZEN W39 authority on the existing W39 branch;
5. integrate the exact frozen W39 branch into `main` by a normal history-preserving PR merge, with no unrelated/shared-Core changes;
6. execute the canonical Core v2 Release workflow for release identity `weekly/2026-W39` from the exact FROZEN state/manifest now present on `main`;
7. verify the public Release asset is byte-identical to the approved r6 PDF;
8. if—and only if—the known post-release `validate-state` CLI defect recurs after public bytes are already correctly released, use the same bounded recovery pattern proven for W38;
9. establish final lifecycle `RELEASED / COMPLETE` on main;
10. post final release evidence to Issue #551 and close #551 as `completed`;
11. STOP.

No drafting, content repair, source admission, Evidence work, Architecture work, bibliography edit, terminology edit, PDF rebuild/substitution, or Shared Core maintenance is authorized after Human approval.

## 3. Starting guard

The Muse invocation must supply the Exact Starting SHA/tree for the commit containing this request.

Before any write, read-only verify:

- remote `weekly/2026-W39-v2-work` HEAD == invocation Exact Starting SHA;
- remote W39 tree == invocation Expected Starting Tree;
- Exact Starting SHA parent == `a0431ae0c5d3945afa4cdf5705cc238ed919bd16`;
- parent tree == `769a4050cb3c8274eeb471770f41f3312afa53f5`;
- remote `main` HEAD == `519aed90607f6e787bb3a7c00b651777835fd657`;
- remote main tree == `3a59771e7e5622c4d3c4bebad55fec52b42151c4`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Production Core tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- current W39 lifecycle == `RELEASE_CANDIDATE`;
- Architecture gate == `approved`;
- Publication Preview gate == `pending`;
- next action == `PUBLICATION_PREVIEW`;
- r1 through r5 Publication Preview decisions == `REQUEST_CHANGES` at their canonical records;
- r6 Human decision record does not yet exist;
- exact r6 Candidate/PDF identities match §1;
- Issue #551 remains open;
- Shared Core paths have not drifted from reviewed main authority.

Any mismatch -> zero approval/freeze/integration/release writes; report expected vs actual; STOP.

No reset, rebase, force push, squash, history rewrite, or cherry-pick.

## 4. Mandatory read order

Read at minimum:

1. this request;
2. `sources/2026-W39/execution/reviews/publication-preview-r6.md`;
3. `sources/2026-W39/execution/reviews/publication-preview-r6-dossier.md`;
4. all current Issue #551 comments, especially Sol r6 PASS comment `5881667114`;
5. `sources/2026-W39/gates/review-index.json` and r1-r5 publication review records;
6. current canonical Human Gate CLI/help;
7. `docs/freeze-release-policy.md`;
8. current Freeze helpers/CLI, including `scripts/survey_profiled_freeze_v2.py` and current publication freeze helper;
9. current Core stage validator/agent control for `RELEASE_CANDIDATE -> FROZEN`;
10. `.github/workflows/survey-production-v2-release.yml`;
11. W38 precedent, including commit `51d640fe30537bb15f51f94fbefb36a2a7a298a4`, main integration PR #513, and bounded post-release recovery PR #514 / commit `12cd9cd8578f62a2905a4c701a4396ce58470de5`.

Repository-local reviewed Core behavior is authoritative.

## 5. Canonically record Human Publication Preview r6 APPROVED

Use current canonical Human Gate protocol. Do not hand-edit Human gate JSON.

Required semantics:

- gate: `PUBLICATION_PREVIEW`
- revision: canonical next revision; expected `6`, but derive from review index
- decision: `APPROVED`
- reviewed repository commit: `98cffa3bbaf36801de1d7bcb8b2449cc0bb0b9d6`
- reviewed_by: `Human Owner`
- requested changes: none
- regeneration boundary: none
- review reference must bind this execution request, r6 shell/dossier, Sol r6 PASS comment, and the explicit Human approval controlling this run.

Before recording, capture actual wall clock. After recording, read back and verify:

- revision and `APPROVED` decision;
- exact reviewed commit;
- exact Candidate/PDF hashes;
- immutable approval snapshot;
- canonical Publication Preview approval authority;
- review index;
- Production State gate transition;
- timestamp is valid and not future-dated relative to its containing commit.

If canonical approval recording fails, STOP.

## 6. Approved-byte immutability

Immediately after Human approval recording, the approved publication bytes are immutable.

Before Freeze, independently re-read/recompute:

- Candidate SHA-256 == `b042be85f0cf8b7f028ac8f7a96f7d2db6fc4f06acd256960a30f992d4975563`;
- PDF SHA-256 == `eb0e49233c8f7c04077d9abc04b2811a625597abda1c7340378b1c9f8cc3e121`;
- PDF bytes == `335817`;
- PDF pages == `12`;
- source/manuscript/citation/visual authorities remain the r6 approved chain.

No rebuild is permitted to replace these bytes. A mismatch, missing artifact, changed Candidate, or provenance drift must STOP publication.

## 7. Freeze exact r6 authority

Use the current canonical Core v2 Freeze path for `RELEASE_CANDIDATE -> FROZEN`.

Required outputs include the canonical:

- `publication/v2/freeze-record-v2.json`;
- `publication/v2/release-manifest-v2.json`;
- Freeze stage validation/reviews/checkpoint;
- FROZEN Production State.

Release identity must be exactly:

`weekly/2026-W39`

Freeze record and manifest must bind the r6 Human approval and exact approved PDF SHA/pages/bytes without changing publication bytes.

### Known Freeze compatibility conditions

Current frozen Core still carries the same Freeze compatibility defects observed in W34-W38. Do not modify Shared Core.

If `survey_profiled_freeze_v2.py` rejects the candidate-bound modern visual-review shape because it expects the older visual schema, use the same bounded W38-compatible canonical publication freeze helper (`survey_publication_v2.build_freeze`) to create the normal Freeze authority.

If Freeze stage validation misclassifies Human approval provenance as a Stage Checkpoint, use only the established W34-W38 runtime/in-memory compatibility: true checkpoints remain validated; Human Gate approval is validated through Human-gate authority rather than Stage Checkpoint admission; the normal Freeze report/reviews/checkpoint shape must still be produced. Record an edition-local compatibility note if reproduced.

No Shared Core file may be edited.

After Freeze, verify all exact identities, commit normally, non-force push, and read back remote frozen HEAD/tree.

## 8. Main integration

Only after W39 is canonically FROZEN, re-read remote `main`.

Expected pre-integration main:

`519aed90607f6e787bb3a7c00b651777835fd657`

If main has moved, STOP before merge and report the actual main SHA. Do not automatically merge onto a different main authority.

Verify the frozen W39 branch has no unauthorized Shared Core changes relative to reviewed main.

Create a normal PR:

- head: `weekly/2026-W39-v2-work`
- base: `main`

PR description must state at minimum:

- W39 Publication Preview r6 Human `APPROVED`;
- reviewed authority `98cffa3bbaf36801de1d7bcb8b2449cc0bb0b9d6`;
- exact frozen PDF SHA `eb0e49233c8f7c04077d9abc04b2811a625597abda1c7340378b1c9f8cc3e121` / `335817` bytes / `12` pages;
- Issue #551 repaired and Sol r6 PASS, but left open until Release closure;
- no Shared Core change;
- release identity `weekly/2026-W39`.

Do not squash or rebase. Merge only through a normal history-preserving merge after repository checks allow it. Read back resulting main merge commit/tree.

## 9. Canonical Release execution

After successful main integration, use the current canonical workflow:

`.github/workflows/survey-production-v2-release.yml`

The workflow itself requires the exact FROZEN Production State and Release Manifest on `main`.

Compute/read back from merged main and dispatch with exact values:

- `issue_id = 2026-W39`
- `production_state_sha256 = <exact merged-main FROZEN production-state SHA-256>`
- `release_manifest_sha256 = <exact merged-main release-manifest-v2.json SHA-256>`
- `confirmation = release:2026-W39`

Do not dispatch until merged-main state is exactly `FROZEN` and its agent-state validation is clean.

The workflow must publish/reconcile release identity:

`weekly/2026-W39`

and rehydrate the exact approved/frozen PDF without substitution.

Verify the public Release:

- tag == `weekly/2026-W39`;
- expected Weekly title/asset identity from current profile;
- Release is not draft/prerelease;
- release asset exists exactly once;
- released PDF SHA-256 == `eb0e49233c8f7c04077d9abc04b2811a625597abda1c7340378b1c9f8cc3e121`;
- byte count == `335817`;
- no duplicate/replacement Release is created;
- merge verification and Release Record bind the exact merged-main/frozen authority.

## 10. Known post-release workflow defect — bounded W38 recovery only

The current release workflow still invokes nonexistent:

`survey_agent_control_v2.py validate-state`

after the public Release, exact-byte asset verification, Release Record generation, and Release checkpoint helper.

If—and only if—all are true:

1. the canonical W39 Release workflow has already created/reconciled public `weekly/2026-W39`;
2. released PDF SHA/bytes exactly match the approved/frozen authority;
3. all earlier release steps passed;
4. failure occurs solely at the known nonexistent `validate-state` invocation, causing the provenance commit/PR step to be skipped;
5. no publication bytes need regeneration;

then use the same bounded W38 recovery pattern:

- do not recreate, rerun, replace, or re-upload the public Release;
- base the minimum recovery branch on the exact post-W39-integration main;
- preserve the already-created canonical helper outputs where valid or reproduce only the deterministic provenance outputs needed from the same release identity;
- use `survey_release_checkpoint_v2.py` plus available Python API `validate_agent_state()` as in W38 precedent;
- write only W39 edition-local release provenance files;
- open and merge a normal provenance recovery PR into main;
- no Shared Core changes;
- no force/rebase/history rewrite.

If any failure differs materially from this known defect, STOP and report it rather than generalizing the recovery authority.

## 11. Final RELEASED read-back

Final success requires current `main` to establish and validate:

- W39 lifecycle == `RELEASED`;
- terminal reason == `COMPLETE`;
- next action == null;
- Architecture Review == approved;
- Publication Preview r6 == approved;
- freeze checkpoint == passed;
- release checkpoint == passed;
- canonical Publication Preview approval, Freeze Record, Release Manifest, merge verification, Release Record, and release Stage Checkpoint all exist and validate;
- public Release `weekly/2026-W39` exists;
- public release PDF is byte-identical to approved r6 PDF;
- main contains no unauthorized Shared Core modifications;
- `production/survey-core-v2` remains exactly `774dd39a951c9ac3818e83dfffd4c7666efb0a20`.

## 12. Issue #551 closure

Only after §11 passes:

1. post a final comment to Issue #551 containing:
   - Human r6 APPROVED record/revision/reviewed commit;
   - frozen branch commit/tree;
   - main integration PR and merge commit;
   - Freeze Record and Release Manifest identities;
   - public Release URL/tag;
   - exact PDF SHA/bytes/pages;
   - release workflow run and whether bounded recovery was needed;
   - final RELEASED/COMPLETE state and validation result;
2. close Issue #551 as `completed`.

Do not close Issue #551 earlier.

Do not close Issue #501 as part of this run; it has separate broader terminology authority/history.

## 13. Forbidden operations

Forbidden throughout:

- new W39 work/fallback/repair/review branch before Freeze;
- content or reader-surface edits after approval;
- source/Evidence/Selection/Architecture changes;
- PDF regeneration as replacement for approved bytes;
- Shared Core changes under `.github/**`, `config/**`, `schemas/**`, `scripts/**`, `templates/**`, or other contract roots;
- manual Human gate JSON edits;
- manual lifecycle/state fabrication;
- force push, reset, rebase, squash, history rewrite, cherry-pick;
- duplicate Release creation or asset replacement.

The only additional branch permitted after the public Release is the canonical/minimum release-provenance branch created by the normal release workflow or the narrowly authorized W38-style recovery if the known post-release CLI defect occurs.

## 14. Required final report

Report at minimum:

1. starting W39 HEAD/tree/main/Core guard result;
2. r6 Human APPROVED canonical review record path/revision/reviewed_at/reviewed commit;
3. immutable approval snapshot / Publication Preview approval authority;
4. approved Candidate/PDF exact identity read-back;
5. Freeze Record path/SHA and Release Manifest path/SHA/release identity;
6. frozen W39 HEAD/tree and stage validation result;
7. main integration PR and merge commit/tree;
8. Release workflow run, disposition, tag, URL, asset identity;
9. independently verified released PDF SHA/bytes/pages;
10. whether the known `validate-state` defect reproduced;
11. if recovery was required: recovery branch/PR/merge and exact changed paths;
12. final W39 `RELEASED / COMPLETE` state and clean validation;
13. final main HEAD/tree and unchanged Production Core HEAD/tree;
14. Issue #551 final comment and `completed` closure;
15. confirmation that Issue #501 was not closed or altered as part of release closure.

Stop after final release closure. Do not begin W40 or any new edition in this run.
