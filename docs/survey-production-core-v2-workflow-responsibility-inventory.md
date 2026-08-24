# Survey Production Core v2 — GitHub Actions workflow responsibility inventory

Status: `SEVEN-WORKFLOW MAINTENANCE CANDIDATE / DEFAULT-BRANCH ISSUE-COMMENT TRUST ROOT / REAUDIT PENDING`  
Established: 2026-08-23 JST  
Updated: 2026-08-24 JST  
Working branch: `maintenance/core-v2-operator-execution-bridge`  
Draft PR: `#447`

## 1. Current seven-workflow surface

| Workflow | Responsibility | Authority model |
|---|---|---|
| `pipeline-contract-tests.yml` | full repository script/schema/unit regression | CI only; read-only |
| `survey-production-v2-ci.yml` | focused Core v2 compile/contract/regression suite | independent CI |
| `build-weekly-survey.yml` | read-only Weekly LuaLaTeX build | controlled build environment |
| `build-special-pdf.yml` | read-only Special LuaLaTeX build | controlled build environment |
| `survey-production-v2-export-publication-preview.yml` | exact Publication Candidate PDF transport | exact-byte verification/transport only |
| `survey-production-v2-release.yml` | exact-byte release/reconciliation | credentials + frozen-byte verification |
| `survey-production-v2-operator-bridge.yml` | trusted default-branch operator request admission and deterministic execution | `issue_comment` authority from default branch; read-only preflight, dependent write-capable executor only after PASS |

No workflow owns Source Intake, Evidence interpretation, Selection, Architecture, Drafting/Synthesis, reader-facing authorship, semantic QA, visual repair, requested editorial repair, or the Human decision itself.

## 2. Trust-root invariant

The work branch must supply data only; it must not supply the workflow that decides whether the branch is trusted.

The execution chain is:

```text
ChatGPT pushes one request-only commit as exact current work-branch head
-> ChatGPT comments on persistent operator queue Issue #448:
     /survey-core-execute <exact-request-commit-sha>
-> survey-production-v2-operator-bridge.yml is loaded from default-branch issue_comment authority
-> read-only operator-preflight treats supplied SHA/work branch as untrusted data
-> exact work-head + request-only + reviewed-main + protected-Core checks PASS
-> only then dependent operator-execute receives contents: write
-> canonical bridge executes and pushes edition-local outputs with force-with-lease
```

There is no work-branch operator signal workflow and no `workflow_run` trust hop. `pipeline-contract-tests.yml` remains CI-only.

Trusted preflight derives protected-path authority from the request's named `reviewed_main_sha`, not from untrusted work-branch config. It also requires the supplied request SHA to equal the exact current canonical work-branch head and rechecks branch movement before execution/push.

Issue #448 is operational transport only, not a Human Gate or editorial authority. Only the exact `/survey-core-execute <40-hex>` trigger syntax is executable; the immutable request JSON remains operation authority.

## 3. Operator request surface

Allowed request kinds remain exactly eight:

1. `INITIALIZE_WEEKLY`
2. `INITIALIZE_RETROSPECTIVE`
3. `INITIALIZE_THEMATIC`
4. `ADVANCE_STAGE`
5. `RECORD_ARCHITECTURE_APPROVAL`
6. `REQUEST_ARCHITECTURE_REVISION`
7. `RECORD_PUBLICATION_PREVIEW_APPROVAL`
8. `REQUEST_PUBLICATION_PREVIEW_REVISION`

Retrospective initialization uses the existing `survey_period_v2` path. No second period builder or cadence-specific workflow is introduced.

The four Human Gate operations only record already explicit Human input. Actions/Core may not choose approval, requested changes, or regeneration boundary.

## 4. Human review / cross-gate semantics

Human-reviewed commits must be durable on the Profile-bound canonical work branch and exact-bind current reviewed State/Gate bytes.

Publication Preview `REQUEST_CHANGES` may choose an upstream boundary when feedback reveals an Evidence/Selection/Architecture defect. If the boundary is before `ARCHITECTURE_ESTABLISHED`, Core preserves old immutable approval/review history but supersedes the active canonical Architecture approval and reopens Architecture Review before publication can continue.

This is still one of the same two normal Human Gates, not a new workflow or Gate.

## 5. Why seven remains proportional

The trust repair does not add an eighth workflow. The existing operator workflow itself becomes the trusted default-branch `issue_comment` executor. `pipeline-contract-tests.yml` remains a normal CI workflow rather than accumulating production execution responsibility.

Ordinary lifecycle stages remain local Core mechanics. `FROZEN -> RELEASED` remains the only lifecycle `WORKFLOW_DISPATCH` stage.

## 6. Regression ownership

- `tests/test_survey_core_execution_bridge_v2.py`: initialization/general bridge surface, no arbitrary execution, default-branch `issue_comment` trust root, exact work-head/request-only/protected-Core admission, Thematic init→Discovery E2E.
- `tests/test_survey_core_execution_bridge_human_gate_v2.py`: explicit Human Gate request schemas, bridge round trips, trusted request-parent binding, upstream Publication→Architecture reopen.
- `tests/test_survey_human_gate_v2.py`: direct canonical round trips, durable reviewed-commit reachability, exact byte proof, immutable approval snapshots, cross-gate reopen.
- `tests/test_survey_period_v2.py`: one generic monthly/half-year/annual/custom bounded Retrospective builder.
- `tests/test_survey_pilot_bootstrap_v2.py`: exactly seven workflow filenames.

A new eighth workflow remains prima facie architectural regression unless deliberately reviewed against the Actions admission rule.

## 7. Admission rule

A workflow is justified only by concrete Actions-specific mechanical value: independent CI, reproducible build, exact-byte transport, credential isolation, release reconciliation, or a trusted exact-checkout execution substrate that the primary ChatGPT runtime lacks.

Research interpretation, editorial judgment, Human decision-making, semantic repair, and visual repair remain outside Actions.
