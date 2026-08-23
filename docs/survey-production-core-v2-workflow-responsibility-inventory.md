# Survey Production Core v2 — GitHub Actions workflow responsibility inventory

Status: `IMPLEMENTATION IN PROGRESS`  
Established: 2026-08-23 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft PR: `#446`  
Governing policy: `docs/survey-production-core-v2-github-actions-policy.md`

## 1. Purpose

This inventory applies the post-W33/SP001 GitHub Actions responsibility policy to the workflows currently present in `.github/workflows`.

The classification is architectural, not a claim that every legacy file has already been deleted. During the redesign, the canonical Core hot path must follow this inventory even while historical workflows still exist in the tree.

Allowed classes:

- `KEEP_AS_CI` — Actions provides clear independent/reproducibility/credential-isolation value and performs only mechanical work.
- `SHRINK_TO_CI_ONLY` — retain the independent validation/build/export shell, remove state mutation, prose generation, semantic repair or authoring.
- `RETURN_TO_CHATGPT` — the operation is part of research/editorial/publication judgment and belongs in the ChatGPT production session.
- `LEGACY_REMOVE_CANDIDATE` — obsolete, one-off, edition-specific or superseded workflow that should disappear from the normal Core surface after reference cleanup.

## 2. Canonical v2 workflows

| Workflow | Classification | Redesign disposition | Actions-specific benefit |
|---|---|---|---|
| `survey-production-v2-ci.yml` | `KEEP_AS_CI` | Keep. CI owns compile/schema/unit/regression validation only. | Clean independent environment and PR regression evidence. |
| `survey-production-v2-release.yml` | `KEEP_AS_CI` | Keep exact-byte frozen release/reconciliation. Do not add editorial decisions. | Credential isolation, immutable release verification, idempotent reconciliation. |
| `survey-production-v2-export-publication-preview.yml` | `SHRINK_TO_CI_ONLY` | Keep export transport, but bind directly to exact Publication Candidate/PDF rather than an `interactive-*` request and standalone preflight convention. | Independent export of the exact bytes presented to Human review. |
| `survey-production-v2-control.yml` | `RETURN_TO_CHATGPT` | Remove from canonical `workflow_control`. Stage adoption and Human Gate recording are local repository-control operations owned by ChatGPT plus deterministic scripts. | No independent CI benefit justifies a write-capable workflow hop. |
| `assistant-control-v2.yml` | `LEGACY_REMOVE_CANDIDATE` | Retire once production-control dispatch is removed. Release can be invoked directly through the dedicated mechanical release surface. | Its main purpose is to relay requests into other workflows; it adds topology rather than verification. |
| `survey-production-v2-work-branch-control.yml` | `LEGACY_REMOVE_CANDIDATE` | Retire. It watches request files, validates, advances state, commits and pushes; the new production session performs this directly. | No independent advantage; it is a bot-authored state-mutation loop. |
| `survey-production-v2-work-branch-human-gate.yml` | `LEGACY_REMOVE_CANDIDATE` | Retire. Human approval is recorded directly by ChatGPT with exact gate authority after explicit Human decision. | No independent advantage; it turns approval recording into an execution-only PR/workflow. |
| `survey-production-v2-interactive-screening.yml` | `RETURN_TO_CHATGPT` | Retire from canonical path. | Screening requires source/materiality interpretation. |
| `survey-production-v2-interactive-evidence.yml` | `RETURN_TO_CHATGPT` | Retire from canonical path. | Evidence assessment is research judgment. |
| `survey-production-v2-interactive-selection-architecture.yml` | `RETURN_TO_CHATGPT` | Retire from canonical path. | Selection and Architecture are editorial/research decisions. |
| `survey-production-v2-interactive-drafting-synthesis.yml` | `RETURN_TO_CHATGPT` | Retire from canonical path. | Drafting and synthesis are authorship. |
| `survey-production-v2-interactive-semantic-publication.yml` | `RETURN_TO_CHATGPT` | Retire from canonical path. | Publication composition/revision is semantic/editorial authorship. |
| `survey-production-v2-interactive-weekly-semantic-publication.yml` | `RETURN_TO_CHATGPT` | Retire from canonical path. | Weekly publication composition remains ChatGPT-owned rather than a separate authoring engine. |
| `survey-production-v2-interactive-semantic-quality.yml` | `RETURN_TO_CHATGPT` | Retire from canonical path. Semantic/editorial and visual QA are explicit ChatGPT review records; Actions may lint only crisp invariants. | Semantic quality cannot be reduced to a workflow-authored PASS. |

## 3. Reproducible PDF build workflows

| Workflow/family | Classification | Redesign disposition |
|---|---|---|
| `build-weekly-survey.yml` | `KEEP_AS_CI` | Current shape is close to desired: read-only checkout, reproducible LuaLaTeX build, compiler/log checks, SHA artifact upload. Keep as independent build verification. |
| `build-special-pdf.yml` | `SHRINK_TO_CI_ONLY` | Preserve useful pinned TeX build/log/page-count/artifact work, but remove legacy `pipeline-state.json` mutation, lifecycle transition and bot push. Adapt to canonical `survey_root/main.tex` and exact candidate/source authority. |
| other build/preflight-only workflows that only compile already-authored source | `KEEP_AS_CI` or `SHRINK_TO_CI_ONLY` | Retain only when they can consume source without editorial transformation or state mutation. |

A build workflow must fail rather than rewrite publication source when an undefined citation, missing glyph, layout compiler error or other deterministic defect is found.

## 4. Contract and regression workflow families

These remain appropriate only insofar as they are tests, not preservation requirements for obsolete production-mutation workflows.

### `KEEP_AS_CI`

- `pipeline-contract-tests.yml`
- `screening-contract.yml`
- `evidence-contract.yml`
- `special-architecture-approval-contract.yml` when it validates exact gate authority rather than a retired workflow topology
- `special-freeze-contract.yml`
- `special-issue-only-release-contract.yml`
- `weekly-issue-only-release-contract.yml`
- other schema/provenance/identifier/reference/integrity regression workflows that execute read-only checks

### `SHRINK_TO_CI_ONLY` or replace

The following contract families historically test production mutation surfaces. Their useful invariant should be moved into Core unit/regression tests; the old workflow topology itself is not a compatibility requirement:

- `special-interactive-draft-contract.yml`
- `special-interactive-evidence-contract.yml`
- `special-selection-architecture-contract.yml`
- `special-post-draft-finalization-contract.yml`
- `special-source-expansion-contract.yml`
- `special-visual-review-contract.yml` when it expects post-Human-preview visual workflow behavior

After equivalent regressions exist in `tests/test_survey_*_v2.py`, these workflow files become `LEGACY_REMOVE_CANDIDATE`.

## 5. Historical Special/Weekly production-mutation families

The following families predate or duplicate the redesigned Core hot path. They must not be used to implement new production editions.

### `RETURN_TO_CHATGPT`

These names encode research/editorial/authoring work that belongs to the production agent:

- `apply-special-interactive-drafts.yml`
- `apply-special-interactive-evidence.yml`
- `apply-special-interactive-screening.yml`
- `apply-special-selection-and-propose-architecture.yml`
- `apply-weekly-interactive-evidence.yml`
- `apply-weekly-interactive-screening.yml`
- `approve-special-architecture-and-prepare-drafts.yml` for the `prepare-drafts` portion
- `collect-special-supplemental-primary-sources.yml`
- `expand-special-validated-source.yml`
- `expand-special-validated-source-v2.yml`
- `finalize-special-validated-draft.yml` where it assembles/revises publication prose
- `import-reviewed-source-intake.yml` / `import-reviewed-special-source-intake.yml` when they interpret or rewrite imported material rather than merely verify exact bytes
- `prepare-special-evidence.yml`
- `prepare-special-reader-notes-ja.yml`
- `prepare-weekly-candidate-selection.yml`
- `prepare-weekly-evidence.yml`
- `prepare-weekly-screening.yml`
- `revise-special-interactive-evidence.yml`
- `revise-weekly-interactive-evidence.yml`

Equivalent Core v2 stages are performed by ChatGPT with narrow deterministic validators and edition-local records.

### `LEGACY_REMOVE_CANDIDATE`

Edition-specific or layout-repair workflow accumulation is not a reusable Core architecture. This includes the family:

- `revise-special-annual-final-visual-compaction.yml`
- `revise-special-annual-publication-preview.yml`
- `revise-special-annual-reference-compaction.yml`
- `revise-special-annual-reference-pagination-v2.yml` through `revise-special-annual-reference-pagination-v7.yml`
- `revise-special-annual-source-specific-notes-v2.yml`
- `revise-special-mixed-layout.yml`
- `sp-2020-y-annual-review-repair.yml`
- `sp-2025-h2-capture-preview.yml`

The underlying lessons remain in profile/invariant/checklist history; the one-off executable repair paths should not remain production entrypoints.

## 6. Historical gate/freeze/release workflows

The repository contains older Special/Weekly gate/release families such as:

- `accept-special-freeze.yml`
- `accept-special-freeze-issue-only.yml`
- `accept-special-publication-preview-issue-only.yml`
- `accept-special-visual-review.yml`
- `publish-special-frozen-release.yml`
- `publish-special-frozen-release-issue-only.yml`
- `release-weekly-survey.yml`
- `release-weekly-survey-issue-only.yml`
- `special-pipeline.yml`
- `weekly-pipeline.yml`
- `weekly-work-pr.yml`
- legacy `assistant-control.yml`

Classification: `LEGACY_REMOVE_CANDIDATE` once frozen historical release reproducibility and any still-referenced CI contracts have been preserved elsewhere.

The redesigned canonical release path is `survey-production-v2-release.yml`; Human Gate recording is repository-local ChatGPT control, not a legacy issue-only accept workflow.

## 7. Canonical workflow-control target

The Core contract should converge on a small explicit mechanical surface:

```text
workflow_control
  release_workflow = survey-production-v2-release.yml
  publication_preview_export_workflow = survey-production-v2-export-publication-preview.yml
  reproducible_build_workflows = parameterized/shared Weekly/Special build verification
```

There should be no canonical `production_control_workflow` or `assistant_control_workflow` required to progress ordinary local lifecycle stages.

`handler_dispatch` may retain only operations whose Actions execution is itself part of the contract, principally credential-isolated `stage:release`.

## 8. Required regressions before deletion

Before removing a workflow family, preserve the invariant rather than the implementation topology. At minimum add tests proving:

1. canonical Core stage plan does not dispatch Screening, Evidence, Selection, Architecture, Drafting, Synthesis, Semantic Publication or Visual Repair through Actions;
2. ordinary stage/Human Gate state recording can be performed through repository scripts without a workflow request file;
3. deterministic Quality Bundle cannot contain agent semantic/visual PASS rows;
4. Publication Candidate binds one exact reader source/PDF and pre-preview semantic/visual reviews;
5. post-approval Freeze does not require a new visual-quality decision;
6. release remains an exact-byte, credential-isolated, idempotent Actions operation;
7. reproducible build workflows never mutate reader source or lifecycle state;
8. retired workflow filenames are not referenced by current Core config/bootstrap/authority.

## 9. Deletion order

Use this order so the branch is never dependent on a deleted workflow:

```text
1. remove canonical config/bootstrap references
2. add replacement direct-control / QA regressions
3. shrink retained build/export workflows to mechanical behavior
4. delete Core-v2 interactive/write-control workflows
5. delete obsolete contract workflows after invariant migration
6. delete historical edition-specific production-mutation workflows in a separate legacy-cleanup batch
7. rerun cross-profile Core CI
```

Historical release tags and already-released publication bytes remain immutable. Removing a workflow file does not rewrite historical releases.
