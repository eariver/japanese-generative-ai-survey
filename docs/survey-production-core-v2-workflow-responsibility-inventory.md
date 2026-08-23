# Survey Production Core v2 — GitHub Actions workflow responsibility inventory

Status: `SEVEN-WORKFLOW MAINTENANCE CANDIDATE / HUMAN-GATE ROUNDTRIP SYNCHRONIZED / REAUDIT PENDING`  
Established: 2026-08-23 JST  
Human-Gate update: 2026-08-24 JST  
Working branch: `maintenance/core-v2-operator-execution-bridge`  
Draft PR: `#447`  
Governing policy: `docs/survey-production-core-v2-github-actions-policy.md`

## 1. Result

The redesigned Actions surface contains seven mechanical workflows:

| Workflow | Responsibility | Why Actions is justified |
|---|---|---|
| `pipeline-contract-tests.yml` | full repository script/schema/unit regression | independent clean-environment regression on relevant PR/push |
| `survey-production-v2-ci.yml` | focused Core v2 compile/contract/regression suite | independent Core contract validation and branch-protection evidence |
| `build-weekly-survey.yml` | read-only reproducible Weekly LuaLaTeX build | controlled TeX environment and independent build artifact/log |
| `build-special-pdf.yml` | read-only reproducible Special LuaLaTeX build | controlled TeX environment and independent build artifact/log |
| `survey-production-v2-export-publication-preview.yml` | exact Publication Candidate PDF transport | independently validates Candidate-bound exact bytes before Human review export |
| `survey-production-v2-release.yml` | exact-byte release/reconciliation | release credentials, immutable-byte verification and idempotent reconciliation are isolated in Actions |
| `survey-production-v2-operator-bridge.yml` | immutable-request execution of allowlisted deterministic Core mechanics, including recording already explicit Human Gate decisions | supplies an exact checked-out execution substrate when the ChatGPT connector runtime cannot invoke the canonical local CLI |

No workflow owns Source Intake, Screening/Evidence judgment, Candidate Selection, Architecture, Drafting, Synthesis, reader-facing authorship, semantic QA, visual QA/repair, or the Human decision itself.

## 2. Canonical contract

`config/survey-production-v2.json` records the mechanical workflow authorities. Ordinary lifecycle stages remain `LOCAL_SCRIPT`; `FROZEN -> RELEASED` remains the only lifecycle `WORKFLOW_DISPATCH` stage.

The operator bridge is **not** a lifecycle handler. It is an optional execution substrate for the same local deterministic Core mechanics. Direct local CLI execution remains preferred when available.

## 3. Production work remains owned by ChatGPT/Human

ChatGPT owns Source Intake/search strategy, Grok/X applicability, Screening/Evidence interpretation, gap-fill, Selection, Architecture, Drafting/Synthesis, reader-facing authorship, semantic/editorial QA, exact-PDF visual QA/repair, agent judgment rows, applying requested Human revisions, and deciding when a genuine Exception Gate is required.

The Human owns the actual normal Human Gate decision: `APPROVED` or routine `REQUEST_CHANGES` with feedback/regeneration boundary.

Repository scripts may validate or mechanically transform narrow artifacts. The operator bridge may record that already explicit Human decision and apply its deterministic lifecycle consequence, but may not infer or create the decision.

## 4. Operator bridge boundary

The bridge exists because the normal connector-only ChatGPT runtime can edit the exact GitHub branch but cannot necessarily mount that branch and execute the canonical Core CLI.

Allowed bridge request kinds are exactly:

1. `INITIALIZE_WEEKLY`;
2. `INITIALIZE_RETROSPECTIVE`;
3. `INITIALIZE_THEMATIC`;
4. `ADVANCE_STAGE` over already-authored exact artifacts;
5. `RECORD_ARCHITECTURE_APPROVAL`;
6. `REQUEST_ARCHITECTURE_REVISION`;
7. `RECORD_PUBLICATION_PREVIEW_APPROVAL`;
8. `REQUEST_PUBLICATION_PREVIEW_REVISION`.

The four Human Gate operations call canonical `survey_human_gate_v2` mechanics. They require pending gate/current State, contiguous expected revision and explicit Human provenance; revision requests additionally require explicit requested changes and a gate-specific enum-constrained regeneration boundary. They do not expose a generic Human-decision or rejection command.

`INITIALIZE_RETROSPECTIVE` exposes the **existing `survey_period_v2` Core path**. The request supplies a configured `special_slug`; the bridge calls `survey_period_v2.resolve_configured_period()` and `survey_period_v2.period_profile()`, then requires generated Profile identity and paths to match the request exactly. Existing `tests/test_survey_period_v2.py` protects generic monthly/half-year/annual Retrospective semantics. The bridge adds no second period builder, new Retrospective scope schema or cadence-specific workflow logic.

Every request binds one exact reviewed `main` SHA. Before dependency installation or Core execution, the workflow verifies that the request parent descends from that reviewed baseline and that protected shared Core/contract bytes match it exactly.

The request contains no arbitrary command, script, module, expression or workflow name. The bridge must not decide Human approval, research, author content, perform semantic/visual judgment, repair layout, Release, or mutate shared Core during edition production.

## 5. Human Gate recording is not Human decision delegation

The maintenance distinction is:

```text
Human decides APPROVED / REQUEST_CHANGES + feedback/boundary
-> immutable request records that explicit input
-> bridge supplies exact checkout/CLI execution substrate
-> canonical Core validates reviewed bytes/current gate/revision
-> Core writes approval or review-revision authority and deterministic State consequence
```

Actions never generate the decision. This is the same class of mechanical responsibility as writing a validated Stage Checkpoint after ChatGPT-authored work.

## 6. Retired Core v2 mutation workflows

The redesign removed the old request/dispatch/mutation and interactive authoring surface. The operator bridge does not restore that topology: it has no editorial handlers, no arbitrary command surface, no workflow-chaining stage machine, and no cadence/topic authoring logic.

## 7. Build boundary

Both retained build workflows are read-only. They may checkout authored source, compile in a controlled TeX toolchain, report deterministic findings/hashes/page counts, and upload artifacts. They must not mutate Production State, rewrite publication source, choose layout/content repairs, or commit production changes.

## 8. Publication Preview transport boundary

`survey-production-v2-export-publication-preview.yml` is transport/verification only. It resolves one exact `publication-candidate-v2.json`, requires `READY_FOR_PUBLICATION_PREVIEW`, verifies repository-resident exact PDF authority, and exports those exact bytes with audit evidence. It does not make a semantic or Human decision.

## 9. Release boundary

`survey-production-v2-release.yml` remains the only lifecycle workflow-dispatched stage because Actions provides credential isolation, frozen-authority verification, exact-byte reconciliation and public Release integrity. It publishes already-approved bytes; it does not author or repair them.

## 10. Regression authority

`tests/test_survey_pilot_bootstrap_v2.py` requires `.github/workflows/` to equal the seven-workflow set in section 1.

`tests/test_survey_core_execution_bridge_v2.py` protects request-only trigger, reviewed-main preflight, Profile-bound write scope, no-arbitrary-command surface, initialization allowlist, deterministic-vs-agent responsibility split, direct use of the existing Retrospective builder, and init -> Discovery bridge E2E.

`tests/test_survey_core_execution_bridge_human_gate_v2.py` protects the four Human Gate request schemas and executes bridge-backed Architecture revision -> r2 approval and Publication Preview revision -> revalidation/r2 approval round trips.

`tests/test_survey_human_gate_v2.py` protects direct canonical approve/revise semantics, stale revision refusal, reviewed-byte drift refusal, regeneration-boundary limits and selective downstream invalidation.

Existing `tests/test_survey_period_v2.py` protects one generic configured-period builder across representative monthly, half-year and annual periods, custom bounded periods, pre-period-end rejection and resume semantics.

A new **eighth** workflow is prima facie architectural regression unless deliberately reviewed against the admission rule below.

## 11. Admission rule for future workflows

A workflow is not justified merely because a task can be automated. It needs a concrete Actions-specific advantage such as independent CI, controlled reproducible build, credential isolation, exact-byte verification, branch-protection integration, or supplying an exact checked-out deterministic execution substrate that the primary operator runtime demonstrably lacks.

The operation must also remain mechanical. If it requires research interpretation, editorial judgment, semantic repair, visual taste, choosing a Human decision, or publication authorship, it belongs to ChatGPT/Human plus narrow deterministic helpers instead.
