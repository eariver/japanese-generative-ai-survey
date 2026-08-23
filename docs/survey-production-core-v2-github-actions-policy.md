# Survey Production Core v2 — GitHub Actions Responsibility Policy

Status: `CONFIRMED BY W33 + SP001 / REDESIGN INVARIANT`  
Established: 2026-08-23 JST  
Confirmed: 2026-08-23 JST  
Working branch: `refactor/survey-production-core-v2`  
Related feedback: `PFB-006` in `docs/survey-production-core-v2-production-feedback-backlog.md`

## 1. Purpose

This memo defines the responsibility rule for Survey Production Core v2 redesign after the W33/SP001 production-validation review.

The current repository has accumulated many GitHub Actions workflows that do more than CI: some generate Drafting/Synthesis artifacts, assemble publication content, perform semantic/publication mutations, revise layout/pagination/spacing, mutate stage/candidate authority, and commit generated results back to production branches.

The W33/SP001 trials confirmed that this is not merely theoretical complexity. Production work became coupled to temporary PRs, bot commits, workflow chaining, generic Core repairs, publication rebuilds and authority rebinding.

The redesign must reduce GitHub Actions to work for which running on Actions is clearly advantageous or which is genuinely mechanical and requires no editorial/research reasoning.

The governing principle is:

> **GitHub Actions is a deterministic executor / verifier, not a reasoning, editorial, or publication-authoring agent.**

A task should not be placed in Actions merely because it can be scripted or automated.

## 2. Admission rule for GitHub Actions

Before retaining or adding any production-related GitHub Actions task, ask:

1. **Is there a concrete advantage to running this task on GitHub Actions rather than having ChatGPT execute or invoke it directly?**
2. **Is the task mechanical enough that the same valid input should lead to the same expected result without research/editorial judgment?**

A task should normally run in Actions only when at least one of those conditions is strongly satisfied and the task does not transfer editorial/research judgment into CI.

Useful Actions-specific advantages include:

- reproducible, controlled build environments;
- independent CI verification of committed artifacts;
- branch-protection integration;
- isolated release credentials / permissions;
- immutable or independently generated build artifacts;
- repeatable cross-regression test execution;
- deterministic verification that should run on every relevant commit/PR;
- release/freeze checks whose independence from the authoring session is valuable.

`It is already a script`, `it can be automated`, or `we used a workflow before` are not sufficient reasons.

## 3. Appropriate Actions responsibilities

Typical work that belongs in GitHub Actions includes:

### CI and contract validation

- unit/regression tests;
- schema validation;
- format/path/invariant checks;
- deterministic stage-contract verification;
- duplicate/missing/disposition accounting where rules are crisp;
- raw/provenance integrity checks;
- SHA-256 / exact-byte verification;
- identifier-preservation checks;
- bibliography/reference integrity checks;
- machine-detectable internal-metadata leakage checks where exact patterns are known.

### Reproducible builds

- compile the already-authored TeX/publication source with a pinned toolchain;
- reproduce Weekly/Special PDFs in a controlled environment;
- detect undefined citations/references, missing glyphs, or other deterministic compiler failures;
- generate build logs and independently reproducible artifacts.

The value here is not that Actions designs the publication. The value is that the source authored and reviewed elsewhere can be rebuilt independently under a known environment.

### Freeze / release integrity

- exact-byte Publication Preview / Freeze / Release identity checks;
- release-manifest validation;
- tag/release consistency;
- controlled publication of already-approved immutable bytes;
- verification that no unreviewed byte drift occurred between approved candidate and release.

These are strong Actions use cases because independent execution and credential isolation materially improve reliability.

## 4. Work that should normally remain with ChatGPT

Tasks requiring interpretation, judgment, synthesis, prioritization, or visual/editorial taste should remain owned by ChatGPT even if helper scripts can assist.

Examples include:

- Source Intake/search strategy;
- source-quality/materiality judgment;
- Screening and Evidence interpretation;
- Candidate Selection;
- Architecture design;
- deciding what a Weekly/Special must explain;
- Drafting and Synthesis;
- prose revision and proofreading/copyediting where meaning/style is involved;
- deciding whether a draft is too shallow or repetitive;
- deciding whether selected Evidence has been adequately represented to readers;
- reader-facing Claim Boundary wording;
- Theme Synthesis / final `総括`;
- incorporation of Weekly community movement from Grok/X;
- choosing article/chapter structure;
- deciding where wide/full-width versus multi-column content is editorially appropriate;
- evaluating page balance, whitespace, scanability, hierarchy, or magazine identity;
- deciding how to repair a visually poor PDF;
- deciding whether a publication is actually good enough for Human Publication Preview.

A deterministic helper may transform or check artifacts after those decisions, but the helper must not silently become the editor.

## 5. Important distinction: mechanical execution vs encoded editorial judgment

A process can be deterministic while still containing editorial policy that should not be delegated to CI.

For example, these operations are mechanically executable:

- turn structured content into TeX;
- insert page breaks;
- switch one/two-column environments;
- compact a table of contents;
- shorten or rearrange generated blocks.

But if the script decides, as a generic production rule, how much prose survives, where every chapter breaks, what information becomes reader-facing, or how an article should be laid out, then that script is effectively making editorial decisions even though its implementation is deterministic.

Therefore the redesign must distinguish:

> **mechanically executable**

from

> **mechanically appropriate to delegate**.

`Can be scripted` does not imply `should be authored by CI`.

## 6. Target responsibility model

The desired model is:

```text
ChatGPT
  research / reasoning / editorial judgment
  architecture / drafting / synthesis
  proofreading and reader-facing composition
  publication-source authoring
  PDF-informed semantic and visual repair
          |
          v
Repository scripts
  narrow deterministic transformation/checking only
  schemas / hashes / provenance / references / preflight
          |
          v
GitHub Actions
  independent CI re-execution
  reproducible build
  deterministic PASS/FAIL verification
  freeze/release integrity
```

Actions should normally consume a candidate authored by ChatGPT and answer:

> **Does this committed candidate reproduce and satisfy the crisp machine-verifiable invariants?**

Actions should not normally answer:

> **What should the next article, paragraph, synthesis, layout, or visual revision be?**

## 7. PDF / typesetting boundary

Building a PDF in Actions is appropriate when it provides a reproducible toolchain, for example pinned LuaLaTeX/TeX Live/Python dependencies and deterministic build settings.

However, the preferred loop is:

```text
ChatGPT authors/edits publication source
-> ChatGPT reviews the resulting PDF and makes semantic/layout decisions
-> candidate source is committed
-> Actions independently rebuild the candidate
-> deterministic build/preflight checks PASS or FAIL
```

Avoid the current anti-pattern:

```text
Actions builds
-> Actions chooses a layout repair
-> Actions mutates publication source
-> another Action evaluates/mutates quality state
-> bot commits become the production authoring loop
```

Actions may detect a machine-defined defect such as an undefined citation or forbidden exact token. It should report the failure. The production operator should normally decide the editorial/layout repair.

## 8. Workflow review classification

During the consolidated post-W33/SP001 redesign, every production-related workflow must be reviewed and assigned one of:

- `KEEP_AS_CI` — Actions provides clear independent/reproducibility value and performs mechanical verification/build/release work only;
- `SHRINK_TO_CI_ONLY` — keep the independent validator/build shell, remove production mutation/authoring;
- `RETURN_TO_CHATGPT` — reasoning/editorial/publication generation or correction belongs to the ChatGPT production session;
- `LEGACY_REMOVE_CANDIDATE` — obsolete, one-off, edition-specific, or superseded production workflows should be removed from the normal Core surface.

For every workflow retained in Actions, the redesign record must state the specific benefit of Actions execution. If no meaningful benefit can be stated, direct execution by ChatGPT or a narrow repository helper is preferred.

High-priority review targets include:

- Core-v2 interactive Drafting/Synthesis;
- Selection/Architecture authoring/adoption surfaces;
- Semantic Publication;
- Semantic Quality;
- production-state/candidate mutation through write-capable workflow chains;
- accumulated `prepare-*`, `apply-*`, `revise-special-*` mutation workflows;
- execution-only PRs whose main purpose is to cause Actions to run.

## 9. Evidence from W33 / SP001

### SP001

The rejected 11-page candidate passed multiple deterministic/semantic Core checks but failed Human review for depth, layout, synthesis and reader-facing metadata leakage.

The 19-page salvage revision then required:

- generic semantic publication renderer repair on `main`;
- shared longform style repair on `main`;
- reintegration of those shared repairs into the edition branch;
- rerouting around a write-capable workflow chain that stopped after a `github-actions[bot]` authored commit;
- a separate authority-rebind operation because the new 19-page PDF initially coexisted with a candidate/quality bundle for the old 11-page bytes.

This is direct evidence that the workflow topology itself became part of the production problem.

### W33

The Weekly trial accumulated repeated execution-only rebuild/export PRs while still producing a 6-page Human-rejected candidate whose main failures were semantic/editorial, not compiler defects.

The correct response is not to add another mutation workflow. It is to return publication authorship/review to ChatGPT and keep Actions as independent build/verification infrastructure.

## 10. Relationship to publication quality

Machine checks are necessary but not sufficient.

The redesign must separate:

- deterministic QA proved by scripts/Actions;
- semantic/editorial QA performed by ChatGPT;
- exact-PDF visual QA performed by ChatGPT.

Actions must not issue a semantic-quality PASS merely because a set of schema fields or known-token checks passed.

Known internal-metadata patterns can and should be linted in CI, but the SP001 19-page re-review demonstrates that semantic production language can survive even when known-token lint reports no finding.

## 11. Implementation rule

This policy is no longer waiting for additional W33/SP001 evidence. The production review is complete and the policy is a required redesign invariant.

Implementation proceeds through `docs/survey-production-core-v2-redesign-plan-after-w33-sp001.md`.

Do not resume W33/SP001 production using the current Actions-heavy mutation path and count that as validation. After workflow reduction and publication-boundary redesign, run clean profile acceptance trials with no in-run shared-Core repair.
