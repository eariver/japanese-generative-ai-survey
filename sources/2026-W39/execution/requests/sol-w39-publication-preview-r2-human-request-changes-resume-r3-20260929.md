# W39 Publication Preview r2 — Human REQUEST_CHANGES → canonical DRAFT_COMPLETE invalidation → fresh r3

Status: `EXECUTION_AUTHORITY / HUMAN_PUBLICATION_PREVIEW_R2_REQUEST_CHANGES / RETURN_DRAFT_COMPLETE / RESUME_PRESERVED_R3_REPAIR`

Date: `2026-09-29 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W39-v2-work`

## 1. Human decision authority

After Sol independently reviewed Publication Preview r2, identified remaining Issue #501 reader-surface defects and a typo, and explained that Core cannot canonically replace the r2-pinned publication bytes without a Human gate decision, the Human Owner explicitly directed creation of the requested-change execution.

Canonical Human decision to record against Publication Preview r2:

`REQUEST_CHANGES`

Allowed regeneration boundary:

`DRAFT_COMPLETE`

This Human decision supersedes the r2 `PENDING` status only. It does not reopen or alter the already-approved Architecture.

## 2. Exact reviewed r2 authority

Publication Preview r2 reviewed production authority:

- reviewed repository commit: `d95a811abd014ad4476d8f305b792920aa6e87fe`
- lifecycle: `RELEASE_CANDIDATE`
- next action: `PUBLICATION_PREVIEW`
- publication candidate: `sources/2026-W39/publication/v2/publication-candidate-v2.json`
- r2 candidate SHA-256: `5a9b9633bd95320ae5f7743396a202d162564427f406f1315d98df7724879f9e`
- r2 PDF: `surveys/weekly/2026-W39/main.pdf`
- r2 PDF SHA-256: `bffda20157e290d95b700c49e7d4fb5c6307e2fcbcd24f7c27cad709176089db`
- r2 PDF byte count: `328743`
- r2 page count: `12`
- r2 review shell: `sources/2026-W39/execution/reviews/publication-preview-r2.md`
- r2 dossier: `sources/2026-W39/execution/reviews/publication-preview-r2-dossier.md`

Architecture approval remains valid and immutable for this run:

- reviewed Architecture authority: `9767d68e0d83aa667eaeeee6394806c612708682`
- Architecture approval record: `sources/2026-W39/gates/architecture-approval.json`

## 3. Current starting authority and prior BLOCKED run

This request is created on top of the current W39 branch state after the legitimate Core representation BLOCKED stop.

Invocation MUST bind exact remote HEAD/tree supplied by Sol after this request commit is created.

The pre-request remote authority was:

- HEAD `f5997ed45e596f064328ed69c80832ace6a49e08`
- tree `f9caf21f37b452d6b4959d23cdc0fefdd182bcbf`

Prior BLOCKED session:

`sources/2026-W39/execution/sessions/w39-r3-residual-repair-blocked-20260928-r1.md`

The prior run correctly stopped because r2 was still Human `PENDING`; it MUST NOT be treated as a failed or unauthorized mutation.

## 4. Preserved r3 repair authority

The reader-surface repair itself is already present in current branch ancestry and MUST NOT be duplicated by cherry-picking or replaying commits blindly.

Preserved repair commit:

`01724a7dca32104a1b1c470097af0fbb99fc71c0`

Commit purpose:

`W39: r3 residual terminology repair (Sol §5 findings) + r3 occurrence ledger`

It contains the repaired reader-facing TeX and r3 terminology ledgers. The current branch HEAD descends from this commit; therefore first verify that the current reader-facing section bytes retain those repairs.

Do not cherry-pick `01724a7d...` onto the current branch.

The previous run restored only the canonical publication artifacts/PDF to r2-pinned bytes so the repository would remain valid while the Human decision was still pending. The repaired reader-facing TeX remains available for canonical regeneration after this Human decision is recorded.

## 5. Required terminology authority

The complete terminology authority for r3 remains the union of:

1. `docs/editorial/ja-technical-terminology-overtranslation-seed.md`
2. `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-additions.md`
3. `docs/editorial/ja-technical-terminology-overtranslation-seed-w39-r2-residual-additions.md`

The preserved r3 occurrence ledger records the 392-form audit and final-byte residual scan:

- `sources/2026-W39/execution/terminology/issue501-publication-r3-occurrence-ledger.json`
- `sources/2026-W39/execution/terminology/issue501-publication-r3-occurrence-summary.md`

Before regenerating publication artifacts, verify that the final reader-facing TeX at current HEAD still reflects the recorded r3 repairs. At minimum confirm the Sol residuals and typo corrected in the BLOCKED run remain corrected.

Do not substitute a fresh automatic rewrite for the reviewed occurrence decisions. If any final TeX drift is found, adjudicate it against the three-file corpus and source context before continuing.

## 6. Preflight guards

Before any write, verify read-only:

- remote `weekly/2026-W39-v2-work` HEAD == invocation Exact Starting SHA;
- remote work tree == invocation Expected Starting Tree;
- that commit contains this exact execution request;
- `f5997ed45e596f064328ed69c80832ace6a49e08` is an ancestor;
- `01724a7dca32104a1b1c470097af0fbb99fc71c0` is an ancestor;
- reviewed r2 authority `d95a811abd014ad4476d8f305b792920aa6e87fe` is an ancestor;
- remote `main` HEAD == `519aed90607f6e787bb3a7c00b651777835fd657` and tree == `3a59771e7e5622c4d3c4bebad55fec52b42151c4`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20` and tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

If any guard mismatches, perform zero repository/GitHub writes and report expected vs actual.

## 7. Canonical Human gate recording

After guards PASS, use the current reviewed Core Human Gate protocol/tooling to record Publication Preview r2 as:

- decision: `REQUEST_CHANGES`
- reviewed authority: exact r2 authority in §2
- regeneration boundary: `DRAFT_COMPLETE`
- requested changes: Issue #501 residual terminology/semantic-language repair + typo correction already documented by Sol and preserved in r3 repair artifacts
- reviewed_by: `Human Owner`
- reviewed_at: actual execution wall-clock time only

Do not hand-edit gate JSON if canonical tooling exists.

Do not fabricate a different Human decision or a different boundary.

The architecture approval must remain valid.

## 8. Canonical regeneration from DRAFT_COMPLETE

Once the Human decision has been canonically recorded and Core has legally returned/invalidation-bounded the production state to `DRAFT_COMPLETE`, regenerate the publication surface using the existing repaired reader-facing TeX at current HEAD.

Required work:

1. verify repaired TeX against the r3 occurrence ledger;
2. regenerate reader manuscript / reader-surface input and gate;
3. regenerate deterministic checks and quality regression bundle;
4. regenerate semantic-editorial and visual review artifacts with correct Worker attribution;
5. rebuild TeX/Bib/PDF through the canonical pipeline;
6. regenerate publication candidate and stage validation;
7. validate agent state and all relevant checkpoints;
8. create a fresh Human Publication Preview r3 shell and dossier.

No upstream Discovery / Screening / Evidence / Materiality / Completeness / Selection / Architecture mutation is permitted.

No Shared Core mutation is permitted.

## 9. PDF byte-binding invariant

For the newly generated r3 PDF, independently demonstrate from real files:

`SHA256(repository main.pdf)`
`== repository main.pdf.sha256`
`== SHA256(Actions artifact main.pdf)`
`== artifact main.pdf.sha256`

Also require identical PDF byte counts and page counts on the compared surfaces.

A workflow success status, matching sidecar text without hashing the PDF, or equal file size alone is insufficient.

Use the new r3 workflow run/artifact; do not reuse r2 identifiers.

## 10. Final reader-byte QA

After the exact final TeX bytes that feed the successful r3 PDF are fixed, run one final seed-external semantic readback over all reader-facing sections.

This final scan must occur after all edits, not against an intermediate candidate.

Confirm:

- no known defective corpus form remains in a defective context;
- no new forced/literal/metaphorical technical translation remains;
- no typo introduced by the repair remains;
- named products, models, benchmarks, metrics, methods and operational concepts retain technical identity;
- facts, numbers, citations, attribution, temporal boundaries and claim strength remain unchanged except for language clarification.

If a new generic terminology defect is found, add it to an explicit successor supplement before repairing it and report the addition.

## 11. Required stopping point

On success, stop at:

`RELEASE_CANDIDATE / HUMAN_GATE_REACHED / PUBLICATION_PREVIEW_R3_PENDING`

Human Publication Preview r3 decision MUST remain `PENDING`.

Do not Freeze.
Do not Release.
Do not merge to `main`.

If canonical Core tooling still cannot represent the now-explicit Human `REQUEST_CHANGES @ DRAFT_COMPLETE`, stop as a Core blocking defect without manual checkpoint/state surgery.

## 12. Git safety

- existing branch only;
- no new/fallback/repair/review branch;
- no force push;
- no reset/rebase/history rewrite;
- normal commits only;
- non-force pushes only;
- remote read-back after each write group.

## 13. Required final report

Report at minimum:

- starting HEAD/tree and all guard results;
- canonical r2 Human review record path/SHA and decision/boundary;
- proof Architecture approval remained valid;
- whether current TeX matched preserved repair commit `01724a7d...` before regeneration;
- terminology corpus/search counts and final residual scan result;
- typo result;
- regenerated reader/publication validation results;
- new PDF SHA-256, byte count, page count;
- new Actions run/artifact IDs;
- all four PDF identity hashes/sidecars and verdict;
- fresh r3 review shell/dossier paths;
- final lifecycle/terminal/next action;
- final remote HEAD/tree;
- confirmation: no Core/main/upstream authority mutation, no Freeze/Release, Human r3 decision PENDING.
