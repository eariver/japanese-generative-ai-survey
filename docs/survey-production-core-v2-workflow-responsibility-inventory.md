# Survey Production Core v2 — GitHub Actions workflow responsibility inventory

Status: `SEVEN-WORKFLOW MAINTENANCE CANDIDATE / FIXED-HEAD REAUDIT PENDING`  
Established: 2026-08-23 JST  
Bridge-maintenance update: 2026-08-23 JST  
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
| `survey-production-v2-release.yml` | exact-byte release/reconciliation | release credentials, immutable-byte verification and idempotent reconciliation are appropriately isolated in Actions |
| `survey-production-v2-operator-bridge.yml` | immutable-request execution of allowlisted deterministic Core mechanics | supplies an exact checked-out execution substrate when the ChatGPT connector runtime cannot invoke the canonical local CLI |

No workflow owns Source Intake, Screening/Evidence judgment, Candidate Selection, Architecture, Drafting, Synthesis, reader-facing authorship, semantic QA, visual QA/repair, or Human approval.

## 2. Canonical contract

`config/survey-production-v2.json` records the mechanical workflow authorities:

```text
workflow_control
  dispatch_ref = main
  operator_execution_bridge_workflow = survey-production-v2-operator-bridge.yml
  publication_preview_export_workflow = survey-production-v2-export-publication-preview.yml
  release_workflow = survey-production-v2-release.yml
  handler_dispatch
    stage:release = survey-production-v2-release.yml
```

Ordinary lifecycle stages remain `LOCAL_SCRIPT`. `FROZEN -> RELEASED` remains the only lifecycle `WORKFLOW_DISPATCH` stage.

The operator bridge is **not** a lifecycle handler. It is an optional execution substrate for the same local deterministic Core mechanics. Direct local CLI execution remains preferred when available.

## 3. Production work remains owned by ChatGPT

ChatGPT owns:

- Source Intake/search strategy and source-materiality judgment;
- Grok/X applicability and task definition;
- Screening interpretation;
- Evidence interpretation and gap-fill;
- Candidate Selection;
- Architecture design;
- Drafting and Profile synthesis;
- reader-facing manuscript/source authoring;
- semantic/editorial QA;
- exact-PDF visual QA and visual/layout repair;
- agent judgment rows supplied to a deterministic stage transition;
- exact Human Gate decision recording after the Human actually decides.

Repository scripts may validate or mechanically transform narrow artifacts. The operator bridge may only invoke the allowlisted deterministic mechanics described in `docs/survey-production-core-v2-operator-execution-bridge.md`.

## 4. Operator bridge boundary

The bridge exists because the normal connector-only ChatGPT runtime can edit the exact GitHub branch but cannot necessarily mount that branch and execute the canonical Core CLI.

Allowed bridge operations are currently:

- `INITIALIZE_WEEKLY`;
- `INITIALIZE_THEMATIC`;
- `ADVANCE_STAGE` over already-authored exact artifacts.

The request contains no arbitrary command, script, module, expression or workflow name. Profile identity must bind the exact `issue_id`, Profile-declared `source_root`, and `work_branch`. Request-only commits and generated edition-local writes are enforced fail-closed.

The bridge must not approve Architecture, approve Publication Preview, Release, research, author content, perform semantic/visual judgment, or mutate shared Core during edition production.

## 5. Retired Core v2 mutation workflows

The redesign removed the old request/dispatch/mutation and interactive authoring surface, including control, work-branch control, interactive Screening/Evidence/Selection/Architecture/Drafting/Synthesis/publication/semantic-quality workflows.

The operator bridge does not restore that topology: it has no editorial handlers, no arbitrary command surface, no workflow-chaining stage machine, and no cadence/topic authoring logic.

## 6. Retired focused/historical production topology

Obsolete focused contract workflows, legacy `apply-*` / `prepare-*` / `revise-*` flows, issue-specific pipeline workflows, annual/layout repair workflows, and old Special/Weekly publication/release mutation flows remain retired. Historical tags/releases/commits/bytes remain immutable in Git history.

## 7. Build boundary

Both retained build workflows are read-only. They may checkout authored source, compile in a controlled TeX toolchain, report deterministic findings/hashes/page counts, and upload artifacts. They must not mutate Production State, rewrite publication source, choose layout/content repairs, or commit production changes.

## 8. Publication Preview transport boundary

`survey-production-v2-export-publication-preview.yml` is transport/verification only. It resolves one exact `publication-candidate-v2.json`, requires `READY_FOR_PUBLICATION_PREVIEW`, verifies repository-resident exact PDF authority, and exports those exact bytes with audit evidence. It does not make a semantic decision.

## 9. Release boundary

`survey-production-v2-release.yml` remains the only lifecycle workflow-dispatched stage because Actions provides credential isolation, frozen-authority verification, exact-byte reconciliation and public Release integrity. It publishes already-approved bytes; it does not author or repair them.

## 10. Regression authority

`tests/test_survey_pilot_bootstrap_v2.py` requires `.github/workflows/` to equal the seven-workflow set in section 1. `tests/test_survey_core_execution_bridge_v2.py` additionally protects the bridge's request-only trigger, Profile-bound write scope, no-arbitrary-command surface, and deterministic-vs-agent responsibility split.

A new **eighth** workflow is prima facie architectural regression unless it is deliberately reviewed against the admission rule below.

## 11. Admission rule for future workflows

A workflow is not justified merely because a task can be automated. It needs a concrete Actions-specific advantage, such as:

- independent clean-environment CI;
- controlled reproducible build environment;
- credential isolation;
- exact-byte artifact/release verification;
- branch-protection integration;
- supplying an exact checked-out deterministic execution substrate that the primary operator runtime demonstrably lacks.

The operation must also remain mechanical. If it requires research interpretation, editorial judgment, semantic repair, visual taste, Human approval, or publication authorship, it belongs to ChatGPT plus narrow deterministic helpers instead.
