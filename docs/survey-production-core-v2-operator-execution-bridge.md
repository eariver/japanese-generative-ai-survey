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

The normal ChatGPT production runtime can:

- read and write exact repository files through the GitHub connector;
- inspect commits, trees, blobs and Actions results;
- perform open-ended research/editorial work;
- perform the Human-mediated Google Drive Grok/X handoff.

It cannot necessarily:

- mount the GitHub work branch as a local checkout; or
- invoke the repository's canonical local Core CLI over that exact branch tree.

This is an operator execution capability gap. Hand-authoring `production-state.json`, checkpoint attestations, Architecture acceptance, or other machine authorities is not an acceptable workaround.

## 2. Governing boundary

The bridge does **not** change the primary-operator model.

ChatGPT remains responsible for:

- Source Intake and research strategy;
- Evidence interpretation and materiality/completeness judgment;
- Candidate Selection;
- Architecture;
- drafting/synthesis;
- semantic/editorial review;
- exact-PDF visual review;
- deciding when an Owner-level Exception Gate is genuinely necessary.

The bridge may execute only deterministic Core mechanics already owned by repository code:

1. canonical Weekly/Thematic Profile + Production State initialization through existing Core builders;
2. deterministic stage-contract validation over already-authored artifacts;
3. compact Stage Checkpoint materialization;
4. lifecycle State advancement after exact validation.

The bridge does not invent Retrospective or series initialization semantics merely to broaden its API. If canonical Core later gains another generic Profile initializer, bridge support may be reviewed separately. Once canonical Profile/State exists, `ADVANCE_STAGE` is Profile-neutral.

Architecture approval and Publication Preview approval remain explicit Human decisions and are not bridge operations. Release remains owned by the dedicated release workflow.

## 3. Transport model

The fallback path is:

```text
ChatGPT authors/researches edition artifacts
-> ChatGPT commits those artifacts normally
-> ChatGPT commits ONE immutable operator request as a request-only commit
-> GitHub Actions checks out that exact request commit
-> bridge executes a whitelisted deterministic Core operation
-> bridge verifies its outputs
-> workflow enforces Profile-bound edition-local write scope
-> github-actions[bot] commits only generated edition-local authorities
-> no output commit retriggers the bridge
-> ChatGPT resumes from the resulting canonical State
```

The request explicitly binds `issue_id`, Profile-declared `source_root`, and `work_branch`.

Canonical request location:

```text
{source_root}/execution/requests/<request-id>.json
```

Canonical bridge-run receipt location:

```text
{source_root}/execution/bridge-runs/<request-id>/
```

`source_root` must remain repository-local under `sources/`. It is not inferred from `issue_id`; this preserves compatibility with valid Profile-specific/nested source-root layouts. The request filename stem and `request_id` must match exactly.

## 4. Why this still satisfies the GitHub Actions responsibility policy

The Actions policy admits a task when Actions provides a concrete execution advantage and the task is mechanical without editorial/research judgment.

The operator bridge satisfies both conditions:

- **concrete advantage:** it supplies the exact checked-out execution environment unavailable to the ChatGPT connector runtime;
- **mechanical scope:** it runs only allowlisted deterministic Core operations over repository-resident inputs.

This is materially different from the retired Actions-heavy authoring topology. The bridge must not:

- search the web or choose sources;
- write Evidence/Selection/Architecture prose or decisions;
- generate reader-facing prose;
- make semantic or visual PASS judgments;
- perform layout repair;
- mutate shared Core/config/schema/workflow paths during edition production;
- run arbitrary commands supplied by a request;
- accept shell snippets, Python expressions, module names or executable paths from a request.

## 5. Request operations

### `INITIALIZE_WEEKLY`

Allowed deterministic effect:

- derive the exact Weekly Profile from issue id + recorded time under current Core contract;
- require the generated Profile's `source_root` and `work_branch` to equal the request;
- create canonical `production-profile.json` and `production-state.json` under that Profile-bound source root;
- initialize the edition-local execution record tree.

### `INITIALIZE_THEMATIC`

Allowed deterministic effect:

- read one repository-local Thematic scope specification under the requested/Profile-bound source root;
- derive the exact Thematic/LONGFORM Profile using the existing canonical Core builder;
- require generated Profile identity (`issue_id`, `source_root`, `work_branch`) to equal the request;
- create canonical Profile/State;
- initialize the execution record tree.

### `ADVANCE_STAGE`

Allowed deterministic effect:

- require an exact expected current lifecycle state;
- require current Production Profile identity to equal request `issue_id`, `source_root`, and `work_branch`;
- validate the exact already-authored stage artifact set with `survey_stage_validation_v2.py` semantics;
- generate `CORE_STAGE_CONTRACT` result authority;
- wrap ChatGPT-authored research/editorial/visual review rows without changing their meaning;
- create the compact Stage Checkpoint;
- advance Production State exactly one lifecycle edge.

The request cannot supply its own deterministic `CORE_STAGE_CONTRACT` result.

## 6. Fail-closed controls

The workflow and bridge must enforce all of the following:

1. push trigger is limited to request paths under `sources/**/execution/requests/` and excludes `main`;
2. the triggering commit adds exactly one request file and changes nothing else;
3. request `work_branch` must equal the executing Git ref;
4. request `source_root` must be repository-local under `sources/`;
5. request path must equal `{source_root}/execution/requests/<request-id>.json`;
6. current/generated Production Profile must bind the same `issue_id`, `source_root`, and `work_branch`;
7. event commit SHA must be exact lowercase 40-hex;
8. operations are an enum, not arbitrary script/command execution;
9. repository paths are traversal-safe;
10. initialization refuses existing canonical Profile/State;
11. stage advancement refuses stale `expected_from_state`;
12. agent review rows cannot impersonate deterministic reviews;
13. bridge-run ids are immutable and cannot be overwritten;
14. workflow derives the write boundary from the validated bridge result rather than constructing it from `issue_id`;
15. workflow refuses generated writes outside the Profile-bound `source_root`;
16. workflow refuses mutation of immutable request authority;
17. bot output commits do not add request files and are also excluded by actor guard, so they do not chain recursively.

The trigger intentionally does not hardcode `weekly/**` or `special/**` branch naming. Exact branch authority comes from the request/Profile match, allowing valid future work-branch conventions without weakening the write boundary.

## 7. Validation consequence

The W33/SP001 clean revalidation attempts that exposed this gap remain non-PASS evidence. Adding the bridge changes shared Core implementation and the Actions surface.

Therefore:

```text
bridge maintenance implementation
-> exact-head CI/regression
-> fixed-head Core audit from zero for the changed candidate
-> Human review/integration
-> reset/rebase clean W33/SP001 validation branches from reviewed main
-> reapply only legitimate edition-local preparation/Raw evidence
-> run canonical cold-start validation through the bridge
```

No pre-bridge W33/SP001 lifecycle result may be relabeled as a successful canonical run.

## 8. Direct-local CLI remains preferred when available

The bridge is a fallback execution substrate, not a requirement that all production use Actions.

If the ChatGPT/operator runtime has an exact local checkout and can run the canonical Core CLI directly, the compact local path remains preferred. Both execution modes must produce the same canonical artifact semantics; the bridge adds transport and execution receipts, not a parallel state machine.
