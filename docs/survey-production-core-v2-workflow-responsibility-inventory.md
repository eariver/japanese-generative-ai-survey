# Survey Production Core v2 — GitHub Actions workflow responsibility inventory

Status: `IMPLEMENTED IN REDESIGN CANDIDATE / PENDING FIXED-HEAD AUDIT`  
Established: 2026-08-23 JST  
Implemented: 2026-08-23 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft PR: `#446`  
Governing policy: `docs/survey-production-core-v2-github-actions-policy.md`

## 1. Result

The post-W33/SP001 redesign has reduced `.github/workflows/` to six mechanical workflows:

| Workflow | Responsibility | Why Actions is justified |
|---|---|---|
| `pipeline-contract-tests.yml` | full repository script/schema/unit regression | independent clean-environment regression on every relevant PR/push |
| `survey-production-v2-ci.yml` | focused Core v2 compile/contract/regression suite | independent Core contract validation and branch-protection evidence |
| `build-weekly-survey.yml` | read-only reproducible Weekly LuaLaTeX build | controlled TeX environment and independent build artifact/log |
| `build-special-pdf.yml` | read-only reproducible Special LuaLaTeX build | controlled TeX environment and independent build artifact/log |
| `survey-production-v2-export-publication-preview.yml` | exact Publication Candidate PDF transport | independently validates Candidate-bound exact bytes before Human review export |
| `survey-production-v2-release.yml` | exact-byte release/reconciliation | release credentials, immutable byte verification and idempotent reconciliation are appropriately isolated in Actions |

No remaining workflow owns Source Intake, Screening, Evidence judgment, Candidate Selection, Architecture, Drafting, Synthesis, semantic publication authoring, semantic QA, visual repair, ordinary stage adoption, or Human Gate state recording.

## 2. Canonical contract

The current `config/survey-production-v2.json` workflow authority is intentionally smaller than the workflow directory:

```text
workflow_control
  dispatch_ref = main
  publication_preview_export_workflow = survey-production-v2-export-publication-preview.yml
  release_workflow = survey-production-v2-release.yml
  handler_dispatch
    stage:release = survey-production-v2-release.yml
```

Ordinary lifecycle stages are `LOCAL_SCRIPT`. `FROZEN -> RELEASED` is the only `WORKFLOW_DISPATCH` stage.

The two build workflows and CI workflows are verification infrastructure, not lifecycle dispatch handlers.

## 3. Production work returned to ChatGPT

The redesign explicitly returns the following responsibilities to the ChatGPT production session:

- Source Intake/search strategy and source-materiality judgment;
- Grok/X applicability and task definition;
- Screening interpretation;
- Evidence interpretation and gap-fill;
- Candidate Selection;
- Architecture design;
- Drafting and Profile synthesis;
- reader-facing manuscript/source authoring;
- semantic/editorial QA;
- exact-PDF visual QA;
- semantic/layout repair after inspecting the rendered PDF;
- ordinary local stage transition/checkpoint recording after deterministic validation;
- exact Human Gate decision recording after the Human actually decides.

Repository scripts may validate or mechanically transform narrow artifacts. They do not become publication authors merely because the operation is deterministic.

## 4. Retired Core v2 mutation workflows

Commit `53f73386b86b2cb08ea1d03572787c9352f31205` removed the Core-v2 request/dispatch/mutation surface:

- `survey-production-v2-control.yml`
- `assistant-control-v2.yml`
- `survey-production-v2-work-branch-control.yml`
- `survey-production-v2-work-branch-human-gate.yml`
- `survey-production-v2-interactive-screening.yml`
- `survey-production-v2-interactive-evidence.yml`
- `survey-production-v2-interactive-selection-architecture.yml`
- `survey-production-v2-interactive-drafting-synthesis.yml`
- `survey-production-v2-interactive-semantic-publication.yml`
- `survey-production-v2-interactive-weekly-semantic-publication.yml`
- `survey-production-v2-interactive-semantic-quality.yml`

This removes execution-only PR/request-file hops from the canonical production path.

## 5. Retired obsolete focused contract workflows

Commit `1bd3c45b975a0ffea7bd09352624bd18cf4b488f` removed six contract workflows that either duplicated the full unit suite or encoded obsolete production-mutation topology:

- `special-interactive-draft-contract.yml`
- `special-interactive-evidence-contract.yml`
- `special-selection-architecture-contract.yml`
- `special-post-draft-finalization-contract.yml`
- `special-source-expansion-contract.yml`
- `special-visual-review-contract.yml`

The useful invariants are now owned by ordinary unit/Core regression tests rather than by preserving those workflow files.

## 6. Retired historical production topology

Commit `46818916547d91602fdbf42a293509fa1def49fd` removes the remaining historical Actions production topology, including:

- legacy `apply-*`, `prepare-*`, `revise-*`, import/expansion/finalization and supplemental-source workflows;
- legacy `assistant-control.yml`;
- old Special visual/freeze/publication-preview acceptance workflows;
- old Special/Weekly issue-only and versioned release workflows;
- old `special-pipeline.yml`, `weekly-pipeline.yml`, and `weekly-work-pr.yml`;
- edition-specific annual/layout repair workflows;
- focused Screening/Evidence/Architecture/Freeze/issue-only-release contract workflows that added no invariant beyond the full unit/Core suites or explicitly asserted obsolete workflow topology.

Historical tags, releases, commits and released bytes remain immutable and recoverable from Git history. Deleting a workflow entrypoint does not rewrite history.

## 7. Build boundary

Both retained build workflows are read-only.

They may:

- checkout already-authored source;
- compile with a controlled TeX toolchain;
- report deterministic compiler/log findings;
- compute SHA/page-count/byte evidence;
- upload build artifacts.

They must not:

- mutate `production-state.json` or legacy `pipeline-state.json`;
- write editorial page-budget decisions into lifecycle state;
- rewrite publication source;
- choose layout repairs;
- commit or push generated production changes.

Page budgets remain editorial authority. A build may report page count but does not make content decisions to satisfy a target.

## 8. Publication Preview transport boundary

`s​​urvey-production-v2-export-publication-preview.yml` is transport/verification only.

It resolves one exact `publication-candidate-v2.json`, validates `READY_FOR_PUBLICATION_PREVIEW`, requires repository-resident exact PDF bytes, verifies Candidate path/hash/byte-count authority, and exports those bytes with an audit sidecar.

There is no `interactive-preview-export.json` production request artifact and no new semantic/preflight decision in the export workflow.

## 9. Release boundary

`s​​urvey-production-v2-release.yml` remains because Actions materially improves this operation:

- isolated release credentials;
- exact frozen authority verification;
- exact PDF rehydration/verification;
- idempotent existing-release reconciliation;
- public GitHub Release creation/download verification;
- post-release provenance record creation.

The workflow publishes already-approved immutable bytes. It does not author or repair the publication.

## 10. Regression authority

`tests/test_survey_pilot_bootstrap_v2.py` now requires the workflow directory to contain exactly the six workflows listed in section 1. This makes workflow reduction a tested Core property rather than a documentation preference.

`pipeline-contract-tests.yml` continues to run the complete `tests/test_*.py` suite and validate JSON contracts. `survey-production-v2-ci.yml` independently compiles all `scripts/survey_*_v2.py` modules, runs all `tests/test_survey_*_v2.py` tests, and parses Core JSON contracts. Core CI is enabled for both the redesign branch and `main`.

## 11. Admission rule for future workflows

A new workflow must not be added merely because a task can be automated.

Before adding one, document a concrete Actions-specific advantage such as:

- independent clean-environment CI;
- controlled reproducible build environment;
- credential isolation;
- exact-byte artifact/release verification;
- branch-protection integration.

If the operation requires research interpretation, editorial judgment, semantic repair, visual taste, or ordinary repository-local state mutation, it belongs to ChatGPT plus narrow deterministic helpers instead.
