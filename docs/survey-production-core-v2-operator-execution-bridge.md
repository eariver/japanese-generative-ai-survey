# Survey Production Core v2 — Operator Execution Bridge

Status: `MAINTENANCE CANDIDATE / POST-MERGE REVALIDATION FINDING / REAUDIT PENDING`

Established: 2026-08-23 JST

Related evidence:

- `docs/checkpoints/survey-production-core-v2-postmerge-revalidation-worklog.md`
- W33 clean revalidation branch `weekly/2026-W33-v2-work`
- SP001 clean revalidation branch `special/SP001-v2-work`

Related policy:

- `docs/survey-production-core-v2-github-actions-policy.md`
- `docs/survey-production-core-v2-execution-record-policy.md`

## 1. Problem statement

The post-merge W33/SP001 clean revalidation established that the redesigned responsibility split is directionally correct but one operational assumption was incomplete.

The normal ChatGPT production runtime can read/write exact repository files through the GitHub connector, inspect commits/trees/blobs/Actions, perform open-ended research/editorial work, and perform the Human-mediated Google Drive Grok/X handoff. It cannot necessarily mount the exact GitHub work branch and invoke the repository's canonical local Core CLI over that exact tree.

This is an operator execution capability gap. Hand-authoring `production-state.json`, checkpoint attestations, Architecture acceptance, or other machine authorities is not an acceptable workaround.

## 2. Governing boundary

The bridge does **not** change the primary-operator model.

ChatGPT remains responsible for Source Intake/research strategy, Evidence interpretation, materiality/completeness, Selection, Architecture, drafting/synthesis, semantic/editorial review, exact-PDF visual review and deciding when a genuine Owner-level Exception Gate is necessary.

The bridge may execute only deterministic Core mechanics already owned by repository code:

1. canonical Weekly Profile + Production State initialization through existing Core logic;
2. canonical configured Retrospective Period Profile + Production State initialization through existing `scripts/survey_period_v2.py`;
3. canonical Thematic Profile + Production State initialization through existing Core logic;
4. deterministic stage-contract validation over already-authored artifacts;
5. compact Stage Checkpoint materialization;
6. lifecycle State advancement after exact validation.

For Retrospective Period work, **no new profile builder was added by this maintenance**. Core already contained `survey_period_v2.resolve_configured_period()` and `survey_period_v2.period_profile()`, covering generic monthly, half-year and annual configured periods. The bridge merely exposes that existing deterministic path to connector-only runtimes. Tier-specific research interpretation, coverage audit, chronology, trajectory and synthesis remain Profile/guide + ChatGPT responsibilities.

Foundations remains a living series authority layered over Thematic/LONGFORM rather than a bridge operation. Once canonical Profile/State exists, `ADVANCE_STAGE` is Profile-neutral.

Architecture approval and Publication Preview approval remain explicit Human decisions and are not bridge operations. Release remains owned by the dedicated release workflow.

## 3. Transport model

```text
ChatGPT reviews one exact main Core baseline
-> ChatGPT authors/researches edition artifacts
-> ChatGPT commits those artifacts normally
-> ChatGPT commits ONE immutable operator request as a request-only commit
-> GitHub Actions checks out that exact request commit
-> workflow proves the branch's shared Core/contract tree still matches reviewed main
-> bridge executes one whitelisted deterministic Core operation
-> bridge verifies its outputs
-> workflow enforces Profile-bound edition-local write scope
-> github-actions[bot] commits only generated edition-local authorities
-> no output commit retriggers the bridge
-> ChatGPT resumes from canonical State
```

Every request explicitly binds:

- `issue_id`;
- Profile-declared `source_root`;
- `work_branch`;
- one exact lowercase 40-hex `reviewed_main_sha`.

Initialization requests also carry `operation.execution_record.reviewed_main_sha`; the workflow requires it to equal the top-level baseline.

Canonical request location:

```text
{source_root}/execution/requests/<request-id>.json
```

Canonical bridge-run receipt location:

```text
{source_root}/execution/bridge-runs/<request-id>/
```

`source_root` must remain repository-local under `sources/`. It is not inferred by the workflow from `issue_id`. The request filename stem and `request_id` must match exactly.

`reviewed_main_sha` is per-operation provenance rather than a run-global lock. A later stage may use a newer explicitly reviewed main baseline only if the edition branch descends from it and the protected shared-Core/contract bytes match that baseline exactly.

## 4. Why this still satisfies the Actions responsibility policy

The bridge satisfies the Actions admission rule because:

- **concrete advantage:** it supplies the exact checked-out execution environment unavailable to the connector-only ChatGPT runtime;
- **mechanical scope:** it invokes only enumerated deterministic Core operations whose semantics exist independently of the workflow.

The bridge must not:

- search the web or choose sources;
- author Retrospective/Thematic editorial scope or Architecture;
- write Evidence/Selection/Architecture prose or decisions;
- generate reader-facing prose;
- make semantic or visual PASS judgments;
- perform layout repair;
- mutate shared Core/config/schema/workflow paths during edition production;
- accept shell snippets, Python expressions, module names, executable paths, workflow names or other arbitrary command surfaces.

## 5. Request operations

### `INITIALIZE_WEEKLY`

Allowed deterministic effect:

- derive the exact Weekly Profile from issue id + recorded time under current Core contract;
- require generated Profile `issue_id`, `source_root` and `work_branch` to match the request;
- create canonical `production-profile.json` / `production-state.json`;
- initialize edition-local execution records.

### `INITIALIZE_RETROSPECTIVE`

Request-specific input is only the configured `special_slug` in addition to common identity/provenance fields.

Allowed deterministic effect:

1. call `survey_period_v2.resolve_configured_period(repo_root, special_slug, recorded_at)`;
2. let the existing Core helper resolve configured period identity, calendar bounds, generic initial obligations, guide, source/survey roots and canonical work branch;
3. call `survey_period_v2.period_profile(repo_root, cfg, spec)`;
4. rely on the existing Core helper to reject an unknown configured slug or initialization before the bounded period ends;
5. require generated Profile `issue_id`, `source_root` and `work_branch` to equal the immutable request;
6. create canonical Profile/State and execution records.

No Retrospective scope file, second Profile builder, or cadence-specific bridge path is introduced. Monthly, half-year and annual coverage remain one existing `RETROSPECTIVE_PERIOD` implementation.

### `INITIALIZE_THEMATIC`

Allowed deterministic effect:

- read one repository-local Thematic scope specification under the requested source root;
- derive the exact Thematic/LONGFORM Profile using the existing canonical builder;
- require generated Profile identity to equal the request;
- create canonical Profile/State and execution records.

### `ADVANCE_STAGE`

Allowed deterministic effect:

- require exact current `expected_from_state`;
- require current Production Profile identity to equal request identity;
- validate the exact already-authored stage artifact set with canonical stage-validation semantics;
- generate `CORE_STAGE_CONTRACT` deterministic result authority;
- wrap ChatGPT-authored research/editorial/visual review rows without changing their meaning;
- create the compact Stage Checkpoint;
- advance Production State exactly one lifecycle edge.

The request cannot supply its own deterministic `CORE_STAGE_CONTRACT` PASS.

## 6. Reviewed-main Core preflight

Before installing dependencies or invoking the bridge, the workflow must:

1. validate request-level `reviewed_main_sha` shape;
2. fetch current `main` and require the reviewed SHA to be an ancestor of current main;
3. require the request commit parent to descend from the reviewed SHA;
4. for any initialization operation, require execution-record reviewed-main SHA equality;
5. protect at minimum `.github/workflows`, `config`, `schemas`, and `scripts`, plus configured `implementation_control_roots` and every pipeline/quality contract file;
6. require those protected bytes at the request parent to equal the reviewed-main baseline;
7. only then install dependencies and execute Core.

The fixed minimum roots prevent a drifted branch-side config from weakening its own comparison boundary. Legitimate edition-local Raw/research/Evidence/manuscript artifacts may differ from main.

## 7. Fail-closed controls

The workflow/bridge must enforce:

1. trigger limited to `sources/**/execution/requests/*.json` and not `main`;
2. one newly added request and request-only triggering commit;
3. exact reviewed-main provenance and shared-Core byte equivalence;
4. exact request branch/ref match;
5. source root under `sources/` and canonical request path;
6. generated/current Profile identity match;
7. configured Retrospective slug resolution through existing `survey_period_v2` only;
8. unconfigured Retrospective slug and pre-period-end initialization rejection;
9. exact lowercase event commit SHA;
10. enum operation surface only;
11. traversal-safe repository paths;
12. initialization refusal when canonical Profile/State already exists;
13. stale `expected_from_state` refusal;
14. no agent impersonation of deterministic reviews;
15. immutable/non-overwritable bridge-run ids;
16. generated writes only below validated Profile `source_root`;
17. no mutation of immutable request authority;
18. bot output commits cannot recursively chain the bridge.

The trigger intentionally does not hardcode cadence branch prefixes. Branch authority comes from request/Profile equality.

## 8. Validation consequence

The W33/SP001 clean revalidation attempts that exposed the operator gap remain non-PASS evidence. Adding the bridge changes shared Core implementation and the Actions surface.

During maintenance fixed-head preparation, a Special-viability audit correctly noticed that the bridge could not cold-start the required Retrospective validation. Deeper pre-freeze inspection found the canonical generic Period builder already existed on the reviewed base in `survey_period_v2`; the actual defect was only missing bridge exposure. A temporary duplicate Retrospective adapter/schema/test path was removed before candidate freeze.

Therefore acceptance sequence remains:

```text
finish bridge maintenance
-> exact-head CI/regression
-> complete fixed-head six-point audit from zero
-> Human full-candidate review
-> unchanged integration
-> clean Weekly + Thematic/SP001 + representative Retrospective + Foundations validation
```

No pre-bridge W33/SP001 lifecycle result may be relabeled as successful canonical validation.

## 9. Direct-local CLI remains preferred

The bridge is a fallback execution substrate. If ChatGPT/operator runtime has an exact local checkout, use canonical local helpers directly. For configured Retrospective work that helper is the already-existing `scripts/survey_period_v2.py`.

Direct local and bridge modes must produce the same canonical artifact semantics; the bridge adds transport and execution receipts, not a parallel state machine.
