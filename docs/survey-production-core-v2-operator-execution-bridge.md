# Survey Production Core v2 — Operator Execution Bridge

Status: `MAINTENANCE CANDIDATE / POST-MERGE REVALIDATION FINDING`

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

1. canonical Weekly/Thematic Profile + Production State initialization;
2. deterministic stage-contract validation over already-authored artifacts;
3. compact Stage Checkpoint materialization;
4. lifecycle State advancement after exact validation.

Architecture approval and Publication Preview approval remain explicit Human decisions and are not bridge operations.

Release remains owned by the dedicated release workflow.

## 3. Transport model

The fallback path is:

```text
ChatGPT authors/researches edition artifacts
-> ChatGPT commits those artifacts normally
-> ChatGPT commits ONE immutable operator request as a request-only commit
-> GitHub Actions checks out that exact request commit
-> bridge executes a whitelisted deterministic Core operation
-> bridge verifies its outputs
-> workflow enforces edition-local write scope
-> github-actions[bot] commits only generated edition-local authorities
-> no output commit retriggers the bridge
-> ChatGPT resumes from the resulting canonical State
```

Canonical request location:

```text
sources/<issue-id>/execution/requests/<request-id>.json
```

Canonical bridge-run receipt location:

```text
sources/<issue-id>/execution/bridge-runs/<request-id>/
```

The request filename stem and `request_id` must match exactly.

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
- create canonical `production-profile.json` and `production-state.json`;
- initialize the edition-local execution record tree.

### `INITIALIZE_THEMATIC`

Allowed deterministic effect:

- read one repository-local Thematic scope specification under the edition source root;
- derive the exact Thematic/LONGFORM Profile;
- create canonical Profile/State;
- initialize the execution record tree.

### `ADVANCE_STAGE`

Allowed deterministic effect:

- require an exact expected current lifecycle state;
- validate the exact already-authored stage artifact set with `survey_stage_validation_v2.py` semantics;
- generate `CORE_STAGE_CONTRACT` result authority;
- wrap ChatGPT-authored research/editorial/visual review rows without changing their meaning;
- create the compact Stage Checkpoint;
- advance Production State exactly one lifecycle edge.

The request cannot supply its own deterministic `CORE_STAGE_CONTRACT` result.

## 6. Fail-closed controls

The workflow and bridge must enforce all of the following:

1. push trigger is limited to edition work-branch families and request paths;
2. the triggering commit adds exactly one request file and changes nothing else;
3. request `work_branch` must equal the executing Git ref;
4. request path must be canonical for its `issue_id` and `request_id`;
5. event commit SHA must be exact lowercase 40-hex;
6. operations are an enum, not arbitrary script/command execution;
7. repository paths are traversal-safe;
8. initialization refuses existing canonical Profile/State;
9. stage advancement refuses stale `expected_from_state`;
10. agent review rows cannot impersonate deterministic reviews;
11. bridge-run ids are immutable and cannot be overwritten;
12. workflow refuses generated writes outside the edition `source_root`;
13. workflow refuses mutation of the immutable request file;
14. bot output commits do not match the request-path trigger and therefore do not chain recursively.

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
