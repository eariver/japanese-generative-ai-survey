# W34 Sol execution request — resume Drafting after reviewed Core #487 integration

Status: `EXECUTION_AUTHORITY / ARCHITECTURE_R3_HUMAN_APPROVED / REVIEWED_CORE_487_INTEGRATED / RESUME_DRAFTING_THROUGH_PUBLICATION_PREVIEW_READINESS`

Date: `2026-09-12 JST`

## 1. Mission

Resume the existing W34 production branch from the parked, Human-approved Architecture state after the shared-Core Drafting `DERIVED_EXPANSION` defect was repaired through PR #487 and the reviewed Core was integrated into W34.

This request does **not** authorize re-running Discovery, Screening, Evidence, Materiality, Completeness, Selection, or Architecture.

Normal successful path:

```text
ARCHITECTURE_ESTABLISHED / Architecture Review approved
-> Drafting + Profile Synthesis
-> DRAFT_COMPLETE
-> reader/publication validation + PDF
-> VALIDATED_DRAFT
-> Publication Boundary Validator read-only sidecar
-> Publication Candidate
-> RELEASE_CANDIDATE
-> Core v2 Authority Auditor read-only sidecar
-> SOL_PUBLICATION_PREVIEW_REVIEW_READY
-> STOP
```

Do not generate a Publication Preview Human decision.

## 2. Starting identity

The exact W34 Starting SHA/tree for the executor is supplied by the external handoff **after this request is committed**. Do not infer or substitute a different starting commit.

Reviewed main SHA required for this run:

`005e59841272464307386abfc11f5b09228f0814`

Reviewed Core repair merged by PR #487:

`Core v2: resolve effective Screening Discovery basis during Drafting`

The W34 branch already contains that reviewed main as a merge parent. Do not re-implement the repair edition-locally.

## 3. Mandatory start guards

Before any repository write, read-only verify:

- remote branch is exactly `weekly/2026-W34-v2-work`;
- remote W34 HEAD/tree equal the exact values supplied by the external handoff;
- remote `main` HEAD == `005e59841272464307386abfc11f5b09228f0814`;
- current W34 state is `ARCHITECTURE_ESTABLISHED`;
- `human_gates.architecture_review == approved`;
- `human_gates.publication_preview == pending`;
- Draft checkpoint is pending;
- no canonical Draft output from the failed pre-repair attempt exists.

If any guard fails, perform zero repository/GitHub writes and report expected vs actual.

## 4. Existing Human approval is authoritative

Human Architecture Review r3 was already canonically recorded before the Drafting defect was discovered.

Do not record Architecture approval again.

Approved Architecture review surface remains the one bound to reviewed commit:

`498e45b5648f418e346e1a171dc588494dacf716`

Human decision reference:

`sources/2026-W34/execution/reviews/w34-human-architecture-review-decision-20260911-r3.md`

Architecture approval/state/review-index bytes are immutable inputs for this resume unless the canonical Core itself identifies a genuine invalidation condition. Do not hand-edit them.

## 5. Previous defect and repair boundary

Previous Drafting start failed with:

```text
WU-009 upstream Architecture basis invalid:
Screening acceptance points at a different Discovery set
```

The defect was shared-Core behavior: Drafting re-used the root Discovery rather than resolving the accepted Screening effective Discovery for a validated `DERIVED_EXPANSION`.

The reviewed repair now resolves the effective Screening Discovery through the existing Screening authority path while preserving fail-closed package/hash/provenance validation.

Canonical repair record now present in W34 through reviewed-main integration:

`docs/checkpoints/core-v2-drafting-derived-discovery-basis-repair-20260911.md`

Do not special-case W34 and do not weaken provenance checks.

If the same mismatch reappears under the integrated reviewed Core, stop and report it as a regression. Do not bypass it.

## 6. Approved Architecture is immutable during Drafting

Canonical Architecture:

`sources/2026-W34/architecture-v2.json`

Approved editorial model:

- thesis: `agent executionのproductionization`;
- 6 substantive packages + final `WEEKLY_SYNTHESIS / WEEK_IN_REVIEW`;
- all 41 selected candidates retained according to approved Architecture;
- target pages = 20;
- max pages = 26.

Packages, in approved drafting order:

1. `w34-agent-control-plane`
2. `w34-collaborative-agent-workflows-retrieval`
3. `w34-safety-security-governance`
4. `w34-model-economics-distribution`
5. `w34-creative-multimodal-production`
6. `w34-ecosystem-infrastructure-economics`
7. `w34-week-in-review`

Do not change Discovery, Screening, Evidence, Authority Supplement, Edition Views, Materiality, Completeness, Candidate Matrix, Selection, Architecture, package order, candidate placement, page plan, or thesis.

No fresh research is authorized merely to improve prose. If accepted Evidence cannot safely support an approved claim, stop and return the exact contradiction to Sol.

## 7. Drafting requirements

Use the **current reviewed Core** canonical Drafting / Profile Synthesis path and progress to `DRAFT_COMPLETE`.

Reader-facing output is Japanese.

Required editorial guards:

- PRIMARY/SUPPORTING are evidence roles, not article-count quotas;
- preserve relevant source-specific limitations;
- vendor performance/safety/economic claims remain attributed;
- PARTIAL Evidence must not be silently written as fully verified fact;
- do not expose internal pipeline terminology, execution paths, hashes, HOLD/SELECTED labels, Sol/Muse review language, or repair history in reader-facing prose;
- preserve Grok Bot Aug 21/Aug 26 chronology boundary;
- OpenAI API regional processing remains in Model Economics & Distribution;
- final `w34-week-in-review` is cross-package synthesis and may not invent new factual claims.

The final synthesis package has no direct factual placement by design; use the reviewed Core cross-package synthesis support rather than inventing a bypass.

After `DRAFT_COMPLETE`, create a normal commit, non-force push, and fresh remote read-back before continuing.

## 8. Reader/publication validation

Proceed through canonical `DRAFT_COMPLETE -> VALIDATED_DRAFT` processing.

Expected reader/publication outputs include current-Core equivalents of:

- reader manuscript;
- `surveys/weekly/2026-W34/main.tex`;
- `surveys/weekly/2026-W34/main.pdf`;
- deterministic quality regression bundle;
- semantic editorial review;
- visual review.

Do not silently drop approved content to meet page count. If semantic, visual, deterministic quality, or PDF validation fails, stop before any sidecar or Publication Candidate and report the exact failure.

After `VALIDATED_DRAFT`, normal commit, non-force push, and fresh remote read-back are mandatory.

## 9. Read-only sidecar A — Publication Boundary Validator

Pinned tool authority:

Repository: `eariver/publication-boundary-redteam`

Exact SHA: `7b9de2105c690daaafa6698c1791d51ca84a92c0`

Use a temporary checkout outside the Survey repository and verify exact tool HEAD before execution.

This tool is a **non-authoritative read-only second opinion**.

Run against the actual validated W34 reader-facing TeX with the Weekly profile and JSON output, semantically equivalent to:

```bash
publication-boundary-scan surveys/weekly/2026-W34/main.tex --profile weekly --format json
```

Store the report under:

`sources/2026-W34/execution/luna/w34-post-architecture-drafting-sidecars/`

Record exact tool SHA, scanned source SHA-256, exit status, aggregate status, counts, and exact findings.

Handling:

- `PASS` -> continue;
- `NEEDS_REVIEW` -> stop before Publication Candidate and return to Sol;
- `FAIL` / HARD_FAIL -> stop before Publication Candidate and return to Sol.

Do not auto-edit publication text solely in response to sidecar findings.

## 10. Mandatory feedback A

After the first real W34 run of Publication Boundary Validator create:

`sources/2026-W34/execution/luna/w34-post-architecture-drafting-sidecars/feedback-publication-boundary-redteam.md`

Include exact SHA/artifact, usability, resource behavior if observed, useful findings, suspected false positives/negatives, output/context issues, operational usefulness, recommended improvements, and whether the tool should remain non-authoritative.

Do not modify the sidecar repository.

## 11. Publication Candidate

Only if canonical validation and sidecar A are acceptable (`PASS`), proceed through the canonical Publication Candidate path to `RELEASE_CANDIDATE`.

Do not create Publication Preview Human approval.

Commit, non-force push, and fresh remote read-back.

## 12. Read-only sidecar B — Core v2 Authority Auditor

Pinned tool authority:

Repository: `eariver/survey-core-v2-authority-auditor`

Exact SHA: `c5f09d463b21c914d9c59b34597858f6182fc244`

This pinned version contains the W34 read-only production adapter.

Use a temporary checkout outside the Survey repository and verify exact tool HEAD before execution. This is also a non-authoritative read-only second opinion.

Run only after a valid Publication Candidate / `RELEASE_CANDIDATE` exists. Use the pinned tool's documented `audit-production` interface against the actual Survey checkout.

Store its report in the same execution directory.

If the auditor reports a blocking authority inconsistency, stop before Publication Preview review readiness and return to Sol. Do not modify shared Core or edition authority to satisfy the sidecar automatically.

## 13. Mandatory feedback B

After the first real W34 production audit create:

`sources/2026-W34/execution/luna/w34-post-architecture-drafting-sidecars/feedback-survey-core-v2-authority-auditor.md`

Include exact SHA/artifact, adapter/CLI usability, useful findings, suspected false positives/negatives, runtime/resource behavior if observed, output/context gaps, recommended improvements, and whether the tool should remain non-authoritative.

Do not modify the auditor repository.

## 14. Resource discipline

Expected executor environment is approximately Ubuntu / 8 GB RAM.

Run heavy steps sequentially. Do not launch concurrent full Core re-validation, PDF build, or sidecar jobs that unnecessarily multiply memory usage.

The Core repair record documents that W34 upstream re-validation is computationally expensive. Slowness alone is not permission to bypass canonical validation.

## 15. Shared-Core defect discipline

If a new shared-Core defect is discovered:

- do not patch shared Core on the W34 branch;
- record an edition-local defect report;
- leave canonical stage state at the last valid checkpoint;
- stop and return to Sol.

Do not create fallback/repair/review branches from W34.

## 16. Commit / branch discipline

Use only existing branch:

`weekly/2026-W34-v2-work`

No new branch, fallback branch, repair branch, review branch, rebase, reset, force push, or history rewrite.

Before every branch update, fresh-read remote HEAD and require it to equal the executor's expected current head.

After every push, fresh remote read-back.

## 17. Terminal boundary

Normal successful terminal state for this request:

`SOL_PUBLICATION_PREVIEW_REVIEW_READY`

Expected lifecycle by then: `RELEASE_CANDIDATE` with Publication Preview Human decision still pending.

Do **not** freeze or release.

Do **not** generate Human APPROVE / REQUEST_CHANGES for Publication Preview.

Execution identity to record in handoff:

`Execution agent: Muse Spark 1.3`

`Execution mode: EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION`

Mandatory final markers:

- `ARCHITECTURE_R3_HUMAN_APPROVAL_PRESERVED`
- `REVIEWED_CORE_487_INTEGRATED`
- `DERIVED_EXPANSION_DRAFTING_BASIS_REPAIR_ACTIVE`
- `DRAFT_COMPLETE`
- `VALIDATED_DRAFT`
- `PUBLICATION_BOUNDARY_SIDECAR_EXECUTED`
- `SIDECAR_A_FEEDBACK_RECORDED`
- `RELEASE_CANDIDATE`
- `AUTHORITY_AUDITOR_SIDECAR_EXECUTED`
- `SIDECAR_B_FEEDBACK_RECORDED`
- `PUBLICATION_PREVIEW_HUMAN_DECISION_NOT_GENERATED`
- `SOL_PUBLICATION_PREVIEW_REVIEW_READY`

Then STOP.
