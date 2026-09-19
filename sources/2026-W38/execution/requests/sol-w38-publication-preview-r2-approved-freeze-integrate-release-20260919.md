# W38 execution instruction — Human Publication Preview r2 APPROVED through Freeze, main integration, and Release

Status: `EXECUTION_AUTHORITY / HUMAN_PUBLICATION_PREVIEW_R2_APPROVED / FREEZE_INTEGRATE_RELEASE / NO_CORE_CHANGE`

Date: `2026-09-19 JST`

Repository: `eariver/japanese-generative-ai-survey`

Work branch: `weekly/2026-W38-v2-work`

## 1. Human decision authority

The Human Owner explicitly reviewed W38 Human Publication Preview r2 after Independent Sol verification and decided:

`APPROVED`

Human approval was communicated in the controlling conversation after Sol reported:

`PASS / READY_FOR_HUMAN_PUBLICATION_PREVIEW`

Independent Sol observed the conversation wall clock at:

- JST: `2026-09-19T19:39:11+09:00`
- UTC: `2026-09-19T10:39:11Z`

This establishes conversational ordering of the Human decision.

For the canonical Human Gate record itself, use the **actual execution wall clock at recording time**, not a copied/synthetic stage time.

Exact Human-reviewed r2 production authority:

- reviewed repository commit:
  `a55ac5b929221bd133d8a4b819bf960d2104d6c7`
- reviewed tree:
  `fcb8b865d71bb139fefcb6f9a021cbec9edec1be`
- Publication Candidate SHA-256:
  `8aeb4dc4f959096708186ee338e11f518dd5a2f8c31f7a7757ec9f0278bcbe3f`
- exact PDF:
  - path: `surveys/weekly/2026-W38/main.pdf`
  - SHA-256: `3829c1660b55dbe808b3dec2ee14535bbba60ec6e5268f9a91276b71fae54933`
  - bytes: `347330`
  - pages: `11`
  - CI run: `35432581167`
  - artifact: `10581840234`

Human-facing r2 review:

- `sources/2026-W38/execution/reviews/publication-preview-r2.md`
- `sources/2026-W38/execution/reviews/publication-preview-r2-dossier.md`

Independent Sol r2 review:

- `sources/2026-W38/execution/reviews/sol-w38-publication-preview-r2-independent-review-20260919.md`
- Independent Sol verdict:
  `PASS / READY_FOR_HUMAN_PUBLICATION_PREVIEW`

Issues #511 and #512 have been independently verified fixed and are closed as `completed`.

## 2. Mission

Complete W38 publication closure without modifying shared Core:

1. exact starting guards;
2. canonically record Human Publication Preview r2 `APPROVED`;
3. Freeze the exact approved Candidate/PDF bytes;
4. commit/push frozen edition authority on the existing W38 branch;
5. integrate the exact frozen W38 branch into `main` by normal PR/merge, with no unrelated changes;
6. execute the canonical Weekly release process for release identity:
   `weekly/2026-W38`;
7. verify the public Release and exact released PDF bytes;
8. if—and only if—the known Release workflow `validate-state` CLI defect recurs after the public release bytes are already successfully created, perform the same bounded post-release provenance recovery used for W37;
9. finish with canonical W38 lifecycle `RELEASED / COMPLETE`;
10. STOP.

No technical/content regeneration is authorized after Human approval.

## 3. Starting guard

The Muse invocation MUST supply Exact Starting SHA/tree for the commit containing this request.

Before any write, read-only verify:

- remote `weekly/2026-W38-v2-work` HEAD == Exact Starting SHA supplied in invocation;
- remote W38 tree == Exact Starting Tree supplied in invocation;
- Exact Starting SHA parent == `d84af96e77e955834ca106afa13ccb3418cfb89c`;
- parent tree == `0d57688d9e190efb6c48890a6334b370c0621b49`;
- remote `main` == `2ab91516e89b8d706bfe143ebc0e435fa5735e7a`;
- remote main tree == `279ecbd91ee41cb2967532cf831c43ba3a4cbea3`;
- remote `production/survey-core-v2` == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Production Line tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- current W38 lifecycle == `RELEASE_CANDIDATE`;
- Architecture gate == `approved`;
- Publication Preview gate == `pending`;
- next action == `PUBLICATION_PREVIEW`;
- r1 Publication Preview decision == `REQUEST_CHANGES`;
- r2 Human decision record does not yet exist;
- exact r2 Candidate/PDF identities match §1;
- Issues #511/#512 remain closed/completed at start;
- shared-Core diff from reviewed main remains empty.

Any mismatch -> zero production/integration/release writes; report expected vs actual; STOP.

No reset/rebase/force/squash/history rewrite.

## 4. Mandatory read order

Read at minimum:

1. this request;
2. `sources/2026-W38/execution/reviews/publication-preview-r2.md`;
3. `sources/2026-W38/execution/reviews/publication-preview-r2-dossier.md`;
4. `sources/2026-W38/execution/reviews/sol-w38-publication-preview-r2-independent-review-20260919.md`;
5. `sources/2026-W38/gates/review-index.json`;
6. `sources/2026-W38/gates/reviews/publication-r1.json`;
7. current Human Gate CLI/help;
8. current Freeze CLI/help and W37 Freeze compatibility precedent:
   - `sources/2026-W37/execution/defects/w37-freeze-core-defects-20260919.md`;
9. current release workflow and release helper/CLI;
10. W37 release provenance recovery precedent on current main.

Repository-local reviewed Core behavior is authoritative.

## 5. Canonically record Human Publication Preview r2 APPROVED

Use current canonical Human Gate protocol.

Required semantics:

- gate: `PUBLICATION_PREVIEW`
- revision: canonical next revision, expected `2` but determine from review index;
- decision: `APPROVED`
- reviewed repository commit:
  `a55ac5b929221bd133d8a4b819bf960d2104d6c7`
- reviewed_by: `Human Owner`
- requested changes: none
- regeneration boundary: none
- review reference must bind:
  - this execution request;
  - Publication Preview r2 shell/dossier;
  - Independent Sol r2 review;
  - explicit Human decision authority in §1.

Before recording, capture actual wall clock:

```bash
date --iso-8601=seconds
date -u --iso-8601=seconds
```

After recording, read back and verify:

- review revision;
- decision;
- exact reviewed commit;
- exact Candidate/PDF hashes;
- immutable approval snapshot;
- `gates/publication-preview-approval.json`;
- review index;
- Production State transition;
- `reviewed_at` is not future-dated relative to actual wall clock;
- after commit/read-back, `reviewed_at <= containing commit time`.

If canonical gate recording fails, STOP. Do not hand-edit Human gate JSON.

## 6. Freeze exact approved bytes

After canonical r2 approval, **no reader-visible or semantic bytes may change**.

Freeze only the exact approved r2 authority:

- Candidate SHA:
  `8aeb4dc4f959096708186ee338e11f518dd5a2f8c31f7a7757ec9f0278bcbe3f`
- PDF SHA:
  `3829c1660b55dbe808b3dec2ee14535bbba60ec6e5268f9a91276b71fae54933`
- bytes:
  `347330`
- pages:
  `11`

Before Freeze, recompute/read back exact Candidate/PDF bytes.

If either changes, STOP.

Release identity must be:

`weekly/2026-W38`

## 7. Known Freeze Core defects — no Core modification

The same reviewed shared-Core defects observed in W34–W37 remain in scope as known compatibility conditions.

### Defect A — profiled Freeze visual schema incompatibility

If `survey_profiled_freeze_v2.py` rejects the candidate-bound pre-preview visual review because it expects legacy `visual-review-record-v2` with top-level `pdf_path`, do not modify Core.

Use the same canonical W37-compatible path:

`survey_publication_v2.build_freeze`

to bind:

- Publication Candidate;
- Human Publication Preview approval;
- candidate-bound VISUAL review;
- exact source/PDF;
- release identity.

### Defect B — Freeze stage validator misclassifies Human approval provenance

If `survey_stage_validation_v2.py::_prior_artifacts` attempts to validate Human gate approval provenance as a Stage Checkpoint, do not modify Core.

Use only the W34/W35/W36/W37 bounded **runtime/in-memory compatibility**:

- preserve/validate all true prior checkpoints;
- exclude Human Gate approval provenance from Stage Checkpoint admission;
- validate Publication Preview approval through dedicated Human-gate authority;
- bind existing candidate-bound visual review;
- generate the normal Freeze report/reviews/checkpoint authority shape.

No shared-Core file may change.

Create an edition-local W38 defect/compatibility note if the defect reproduces.

## 8. Freeze validation

Before committing FROZEN state, verify:

- Publication Preview r2 approval immutable snapshot exists;
- exact Candidate unchanged;
- exact PDF unchanged;
- Freeze Record binds r2 approval;
- Release Manifest identity == `weekly/2026-W38`;
- exact PDF SHA/bytes/pages preserved;
- required Freeze deterministic reviews PASS;
- RELEASE_CANDIDATE -> FROZEN stage validation/checkpoint is complete;
- new timestamps use actual wall-clock where they represent real review/provenance times;
- inherited historical #507 ledgers remain preserved;
- no shared-Core paths changed.

Commit/push with normal non-force update.

Read back remote frozen HEAD/tree.

## 9. Main integration guard

Only after W38 branch is canonically FROZEN:

Read-only re-check current remote `main`.

Expected before W38 integration:

`2ab91516e89b8d706bfe143ebc0e435fa5735e7a`

If main has moved, STOP before PR merge and report actual SHA. Do not automatically merge onto a different main.

Verify the frozen W38 branch contains no shared-Core path changes relative to reviewed main.

Create a normal PR from:

`weekly/2026-W38-v2-work`

to:

`main`

The PR must describe:

- W38 exact frozen PDF SHA/bytes/pages;
- Publication Preview r2 Human APPROVED;
- Issues #511/#512 fixed/closed;
- no Core change;
- release identity `weekly/2026-W38`.

Do not squash/rebase.

Merge only if repository checks/guards allow normal merge and resulting merge contains exactly the frozen W38 authority plus expected merge-parent structure.

After merge, read back exact main merge commit/tree.

## 10. Release execution

After successful main integration, execute the repository's canonical Weekly release process for:

`weekly/2026-W38`

The public release must contain the exact frozen PDF bytes:

`3829c1660b55dbe808b3dec2ee14535bbba60ec6e5268f9a91276b71fae54933`

Do not rebuild or substitute a different PDF after Freeze.

Verify:

- release/tag identity exactly `weekly/2026-W38`;
- release asset exists;
- asset byte count == `347330`;
- release asset SHA-256 == exact frozen PDF SHA;
- release points to/integrates the frozen W38 publication authority as current workflow defines;
- no duplicate/replacement Release is created.

## 11. Known Release workflow defect — bounded recovery only

Current main retains the W37-known defect where the canonical release workflow may invoke nonexistent:

`survey_agent_control_v2.py validate-state`

after the public Release and exact PDF asset have already been successfully created.

Do not modify shared Core/workflow to fix it in this run.

If—and only if—all of the following are true:

1. canonical W38 release workflow has already created public `weekly/2026-W38`;
2. exact released PDF asset SHA/bytes match the frozen authority;
3. workflow failure occurs solely at the known nonexistent `validate-state` invocation / skipped provenance-commit step;
4. no earlier release step failed;
5. no publication bytes require regeneration;

then use the same narrow W37 recovery pattern:

- do **not** rerun/recreate/reupload the release;
- create the minimum release-provenance recovery branch needed by repository integration policy;
- base it on the exact post-W38-integration main;
- run canonical release checkpoint/helper output;
- validate final state via the available Python API / existing W37 precedent, not by inventing a new CLI command;
- write only W38 edition-local release provenance files;
- open/merge a normal recovery PR;
- no shared-Core path changes;
- no force/rebase/history rewrite.

If the failure differs materially from the W37 known defect, STOP and report it. Do not generalize recovery authority.

## 12. Final RELEASED verification

Successful final state must establish:

- Production State lifecycle == `RELEASED`;
- terminal reason == `COMPLETE`;
- next action == null;
- Architecture review == approved;
- Publication Preview == approved;
- publication_preview machine checkpoint == passed;
- freeze == passed;
- release == passed;
- release checkpoint provenance exists;
- release record/merge verification/core-stage-contract as required by current pipeline exist and validate;
- public Release `weekly/2026-W38` exists;
- public release PDF bytes exactly equal frozen r2 bytes.

## 13. #511 / #512 preservation

Do not reopen or modify Issue #511/#512 unless a release-time audit proves the r2 repair was lost.

The released PDF must retain:

### #511
- TypeSafe blog displayed date Sep 14;
- founder launch Sep 15 separately identified.

### #512
- bibliography/public Source Notes link to stable Issue #512 25-row mirror;
- exact 25/23/2 claim remains reader-auditable;
- 15 = 7+3+5 remains the edition-correct arithmetic.

## 14. Shared-Core freeze

No writes under:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`

Production Line must remain:

`774dd39a951c9ac3818e83dfffd4c7666efb0a20`

Do not merge or modify Production Line.

## 15. Timestamp provenance

For all new Human/review/provenance records:

- timezone-aware actual wall clock only;
- no future-dated synthetic stage schedule;
- Human approval `reviewed_at` <= containing commit time;
- final release provenance times must reflect actual execution ordering.

For machine state transitions, use canonical tooling. If inherited Core monotonicity constraints require non-wall-clock state values, preserve the existing correction-ledger discipline and never present those values as actual wall-clock chronology.

## 16. Commit / branch discipline

W38 production branch:

- existing branch only through Freeze;
- normal commits;
- non-force push.

Main integration:

- normal PR;
- normal merge;
- no squash/rebase.

Only exception:

A **single narrowly scoped release-provenance recovery branch** is authorized only under §11 exact known failure condition after successful public release creation.

No other new/fallback/repair/review/temp branches.

## 17. Normal stop condition

STOP only when either:

### Success

- Human Publication Preview r2 canonically APPROVED;
- exact approved Candidate/PDF frozen;
- W38 integrated to main;
- public `weekly/2026-W38` Release exists;
- exact release asset matches frozen PDF;
- W38 canonical lifecycle == `RELEASED / COMPLETE`;
- all final provenance committed/integrated;
- main read-back confirmed;
- Production Line unchanged;
- shared-Core changed paths = 0.

or:

### Guarded stop

A guard fails or an unrecognized Core/release defect appears.

Do not leave an ambiguous partial state unreported.

## 18. Final report

Report at least:

- invocation Starting SHA/tree;
- canonical Publication Preview r2 approval:
  - revision;
  - review record path/hash;
  - approval snapshot path/hash;
  - reviewed_at;
  - reviewed production commit;
- exact approved Candidate SHA;
- exact approved/frozen PDF SHA/bytes/pages;
- Freeze Record path/hash;
- Release Manifest path/hash;
- FROZEN branch HEAD/tree;
- main integration PR number;
- main merge commit/tree;
- release workflow run ID/result;
- whether known `validate-state` defect recurred;
- if recovery used:
  - recovery branch;
  - recovery PR;
  - recovery commit;
  - proof no release rerun/reupload;
- public release URL/tag;
- released PDF asset name/size/digest;
- exact-byte reconciliation result;
- final W38 Production State;
- final main HEAD/tree;
- Production Line unchanged;
- shared-Core changed paths = 0;
- #511/#512 remain closed;
- exact stop reason.
