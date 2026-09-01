# W33 Post-Issue #433 Validation + Publication Preview Rematerialization — Luna Handoff r1

## Purpose

Execute one larger, bounded deterministic unit after Sol has accepted the repaired Issue #433 reader/publication transformation.

This handoff intentionally groups the remaining machine-controlled steps through the next Human Gate:

1. `DRAFT_COMPLETE -> VALIDATED_DRAFT`;
2. replacement Publication Candidate generation from the exact repaired authority;
3. `VALIDATED_DRAFT -> RELEASE_CANDIDATE`;
4. materialization of the pending Human Publication Preview surface;
5. stop.

This is not a drafting or publication-rewrite task. Do not edit reader prose or regenerate the PDF unless the handoff explicitly requires it. The repaired source/PDF bytes are frozen.

## Repository authority

- Repo: `eariver/japanese-generative-ai-survey`
- Branch: `weekly/2026-W33-v2-work`
- Reviewed main: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Use the Exact Starting SHA supplied by the external caller as the only allowed starting remote HEAD.
- Before any GitHub write, verify the remote branch HEAD exactly equals that SHA.
- If it differs, perform no GitHub write and stop with the actual remote HEAD.

## Mandatory Sol authority

Read before doing any operator write:

`sources/2026-W33/execution/reviews/w33-publication-preview-issue433-sol-review-20260901-r2.md`

Required exact decision:

`ACCEPT / ISSUE_433_READER_TRANSFORMATION_RESOLVED / EXACT_PDF_AND_VALIDATION_AUTHORITY_VERIFIED / AUTHORIZED_FOR_VALIDATION_AND_PUBLICATION_PREVIEW_ADVANCEMENT`

Also read:

1. `sources/2026-W33/production-state.json`
2. `sources/2026-W33/gates/reviews/publication-r1.json`
3. `sources/2026-W33/execution/reviews/w33-owner-publication-preview-decision-20260901-r1.md`
4. current Core stage contracts required for `DRAFT_COMPLETE` and `VALIDATED_DRAFT`
5. the exact current validation authorities listed below
6. the stale `sources/2026-W33/publication/v2/publication-candidate-v2.json` only to verify that it is replaced, not as authority for new hashes.

## Starting state guard

Before the first write, verify current Production State is exactly compatible with:

- `lifecycle_state = DRAFT_COMPLETE`
- `next_action = stage:reader-publication-validation`
- draft checkpoint = `passed`
- validation checkpoint = `pending`
- Publication Preview = `pending`
- freeze = `pending`
- release = `pending`
- Publication Preview Human Gate = `pending`
- Publication Preview approval provenance = `null`
- exception gate inactive

The current Production State must not already be `VALIDATED_DRAFT` or `RELEASE_CANDIDATE`.

## Frozen repaired reader/publication authority

Do not modify these reader bytes or conclusions unless canonical validation fails, in which case stop and report the failure instead of repairing semantics autonomously.

### Reader source

- path: `surveys/weekly/2026-W33/main.tex`
- SHA-256: `44ef2580c072c7295d052311fca2a9a3a5bf165c7eab19a1375b1f729e8e55a0`

### Bibliography

- path: `surveys/weekly/2026-W33/references.bib`
- SHA-256: `f6f1c69e983bd9b0a63314c5da321b2061bc7b729458b51270fec11cc052ff05`

### Exact PDF

- path: `surveys/weekly/2026-W33/main.pdf`
- SHA-256: `13dbc6b2637e5097f82962e6e23413865e04c9a4ae5be035414d594ae19c18ce`
- bytes: `274435`
- pages: `11`
- Git blob SHA: `19871341f8fb3d5802f89df9405cf44a9cb2d8a3`
- source build HEAD: `7081e136758b46efecc934dcb340fafe50ca209c`
- workflow run ID: `33413283489`
- build job ID: `99557967616`
- artifact ID: `9766114667`
- artifact archive digest: `sha256:2ec504661478f5067713ede983e723b8dc4b725756bb44c561191b672e5678d3`

Do not rebuild this PDF. The exact PDF has already passed CI, independent checksum verification, repository pin verification, Luna full-page review, and independent Sol full-page review.

### Validation authorities

- Reader Manuscript Manifest:
  - `sources/2026-W33/publication/v2/reader-manuscript-v2.json`
  - SHA-256 `fe5a8c55ce147dfaff7df61dcb1346a7d7ec09cf24abea267879afbc3103c03a`
- Deterministic identifier preservation:
  - `sources/2026-W33/publication/v2/deterministic/identifier-preservation.json`
  - SHA-256 `f6d41bf97bafe764f9ae57d74e3a9c0ca7f977334b39865e87854d55dbe09305`
- Deterministic PDF preflight:
  - `sources/2026-W33/publication/v2/deterministic/pdf-preflight.json`
  - SHA-256 `d83e33827a7756404fc323ed930a7e8b01331ecb6e019542eef15e4ae04d9c95`
- Deterministic subject/entity/property binding:
  - `sources/2026-W33/publication/v2/deterministic/subject-entity-property-binding.json`
  - SHA-256 `f535cf850b039b1e68eb3a8e15b4b6d273ee9ba6b9ecddc4ac08fead0dd0e72e`
- Quality Regression Bundle:
  - `sources/2026-W33/publication/v2/quality-regression-bundle-v2.json`
  - SHA-256 `854b9c00516e68e88329c1bf10722ebd58f94fd7d93b13d6fb6126795f0bf3d3`
- Semantic / Editorial Review:
  - `sources/2026-W33/publication/v2/semantic-editorial-review-v2.json`
  - SHA-256 `829e5464b7722050c77694eb8a21aa2ea8bed346f4c74d05cd611a13d6419e15`
- Exact-PDF Visual Review:
  - `sources/2026-W33/publication/v2/visual-review-v2.json`
  - SHA-256 `4db164a14b414094b74e4ffed630a37019d49fdaf333683da525be08361dc918`

Before writing an operator request, independently hash/read these current repository files and require exact equality.

## Stale Publication Candidate warning

The currently present:

`sources/2026-W33/publication/v2/publication-candidate-v2.json`

is intentionally stale pre-repair authority. It still references the old source/PDF/review hashes.

Do not use its old hashes as authority.

It must be replaced only after Phase 1 succeeds, using canonical Publication Candidate generation from the frozen current validation authority.

## Frozen upstream authority

Do not change:

- Production Profile;
- Discovery / Screening / Evidence / Materiality / Completeness / Selection;
- Architecture / Architecture approval;
- all seven Draft Packages;
- all seven Draft Results;
- Weekly Profile Synthesis Input/Result;
- shared Core/config/schema/workflow/style files.

No fresh Web/X/Drive/raw-source research is allowed.

# Phase 1 — Canonical DRAFT_COMPLETE validation advancement

## Objective

Advance exactly once:

`DRAFT_COMPLETE -> VALIDATED_DRAFT`

using the exact repaired authority above.

## Request

Create one immutable trusted-operator `ADVANCE_STAGE` request.

Suggested request ID:

`w33-validated-draft-advance-20260901-r2`

Suggested request path:

`sources/2026-W33/execution/requests/w33-validated-draft-advance-20260901-r2.json`

The request-only commit must be the first Luna/Work commit after the externally supplied Exact Starting SHA and must change only that new request path.

Required semantics:

- operation: `ADVANCE_STAGE`
- expected from state: `DRAFT_COMPLETE`
- intended to state: canonical Core `VALIDATED_DRAFT`
- state path: `sources/2026-W33/production-state.json`
- artifacts: use the canonical DRAFT_COMPLETE stage-contract set and current exact hashes, including at minimum:
  - publication PDF `13dbc6b2...c18ce`
  - Quality Regression Bundle `854b9c00...bf3d3`
  - Reader Manuscript `fe5a8c55...3c03a`
  - Semantic Review `829e5464...19e15`
  - validated source `44ef2580...e55a0`
  - Visual Review `4db164a1...dc918`
- do not bind any artifact to the stale pre-repair Publication Candidate.

Agent review entry must bind the Sol review above.

Suggested check ID:

`SOL_ISSUE_433_REPAIR_REVIEW`

Suggested kind:

`AGENT_EDITORIAL`

Executor:

`ChatGPT GPT-5.6 Sol`

Evidence must include the exact Sol decision string and review path.

## Core execution

Use only the canonical Survey Production Core v2 operator bridge pinned by Production State/reviewed main.

Require:

- trusted-operator transport PASS;
- preflight PASS;
- current-stage validation PASS;
- `CORE_STAGE_CONTRACT` PASS;
- `SOL_ISSUE_433_REPAIR_REVIEW` PASS;
- execution PASS;
- exactly one state transition;
- exactly one Validation checkpoint materialization.

Post-Phase-1 expected state:

- lifecycle = `VALIDATED_DRAFT`
- validation checkpoint = `passed`
- draft checkpoint remains `passed`
- downstream publication candidate/gate state must remain canonical for `VALIDATED_DRAFT`
- no Human Publication Preview decision may exist.

If any Phase 1 gate fails, stop immediately. Do not continue to Phase 2.

# Phase 2 — Replacement Publication Candidate generation

After Phase 1 succeeds, generate a replacement:

`sources/2026-W33/publication/v2/publication-candidate-v2.json`

using the canonical current Publication Candidate generator/contract.

The replacement candidate must bind only the current repaired authority.

Required invariants:

- status = `READY_FOR_PUBLICATION_PREVIEW`
- source SHA-256 = `44ef2580c072c7295d052311fca2a9a3a5bf165c7eab19a1375b1f729e8e55a0`
- PDF SHA-256 = `13dbc6b2637e5097f82962e6e23413865e04c9a4ae5be035414d594ae19c18ce`
- PDF byte count = `274435`
- PDF page count = `11`
- Reader Manuscript SHA-256 = `fe5a8c55ce147dfaff7df61dcb1346a7d7ec09cf24abea267879afbc3103c03a`
- Quality Bundle SHA-256 = `854b9c00516e68e88329c1bf10722ebd58f94fd7d93b13d6fb6126795f0bf3d3`
- Semantic Review SHA-256 = `829e5464b7722050c77694eb8a21aa2ea8bed346f4c74d05cd611a13d6419e15`
- Visual Review SHA-256 = `4db164a14b414094b74e4ffed630a37019d49fdaf333683da525be08361dc918`

No old pre-repair hash may survive in the current candidate.

Validate the replacement candidate canonically before Phase 3.

If canonical candidate generation or validation fails, stop at `VALIDATED_DRAFT` and report the failure. Do not hand-author a candidate JSON to bypass the canonical generator.

# Phase 3 — Canonical Publication Candidate advancement

After the replacement Publication Candidate validates, advance exactly once:

`VALIDATED_DRAFT -> RELEASE_CANDIDATE`

Use a second immutable trusted-operator `ADVANCE_STAGE` request.

Suggested request ID:

`w33-publication-candidate-advance-20260901-r2`

Suggested request path:

`sources/2026-W33/execution/requests/w33-publication-candidate-advance-20260901-r2.json`

Bind:

- replacement Publication Candidate path and its newly computed SHA-256;
- the same Sol Issue #433 repair acceptance review;
- canonical Core stage contract.

Require preflight and execute PASS and exactly one transition.

## Expected final Production State

Final Core-derived state must be compatible with:

- lifecycle = `RELEASE_CANDIDATE`
- next action = `PUBLICATION_PREVIEW`
- terminal reason = `HUMAN_GATE_REACHED`
- validation checkpoint = `passed`
- Publication Preview Human Gate = `pending`
- Publication Preview approval provenance = `null`
- freeze checkpoint = `pending`
- release checkpoint = `pending`
- exception gate inactive

The exact canonical field names/derived values produced by Core take precedence over prose in this handoff, but lifecycle semantics must match the above.

# Phase 4 — Human Publication Preview surface and stop

Materialize only the machine-generated/edition-local navigation needed for the Owner to review the replacement Publication Candidate at the Publication Preview gate.

Do not record an Owner decision.

Do not create a Publication Preview approval record.

Do not create revision 2 `APPROVED`, `REQUEST_CHANGES`, or `REJECT` on the Owner's behalf.

The gate must remain `pending` with approval provenance `null`.

Do not close GitHub Issue #433 in this Luna task. Sol/Owner will align issue closure with the replacement Human Publication Preview decision.

# Allowed writes

Only paths canonically needed for the two advancement operations and replacement publication candidate, plus one session record, including:

- immutable operator requests for r2 advancement;
- bridge-run outputs generated by canonical Core;
- canonical Validation checkpoint/state files generated by Core;
- replacement `sources/2026-W33/publication/v2/publication-candidate-v2.json`;
- canonical state/history/navigation outputs generated by Core for the transition to `RELEASE_CANDIDATE`;
- one new session record under `sources/2026-W33/execution/sessions/`.

Do not modify the frozen reader source, bibliography, PDF, current repaired validation authorities, Draft authority, Architecture, Evidence, Selection, Core, workflow, schema, config, or shared style.

# Session record

Create:

`sources/2026-W33/execution/sessions/w33-luna-post-issue433-validation-publication-preview-20260901-r1.md`

Record at minimum:

- Exact Starting SHA;
- ending SHA;
- both operator request commit SHAs;
- bridge/preflight/execute results for both transitions;
- Validation checkpoint path/hash;
- replacement Publication Candidate SHA-256 and all bound artifact hashes;
- final Production State lifecycle/next action/terminal reason;
- proof that exact source/PDF bytes remained unchanged;
- proof that repaired validation authorities remained unchanged;
- proof that no Human Publication Preview decision was created;
- proof that freeze/release/merge were not executed.

# Stop boundary

Successful stop is the Human Publication Preview gate.

Do not execute:

- Owner Publication Preview decision;
- `REQUEST_PUBLICATION_PREVIEW_REVISION` revision 2;
- freeze;
- release;
- merge.

Normal successful stop status:

`PUBLICATION_PREVIEW_R2_GATE_MATERIALIZED`
