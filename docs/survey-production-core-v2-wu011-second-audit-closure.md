# Survey Production Core v2 — WU-011 second-audit closure

Status: `IMPLEMENTATION COMPLETE / HUMAN FULL-CANDIDATE REVIEW REQUIRED`  
Audit date: 2026-08-22  
Branch: `refactor/survey-production-core-v2`  
PR: `#310` (draft; do not merge without Human review)  
Production source of truth until merge: `main`

## 1. Closure claim

WU-011 implementation scope has been re-audited as a whole candidate rather than as isolated unit changes. All merge-blocking defects found during the second audit were repaired generically and covered by regression fixtures. No W33 or SP001 Production State has been initialized.

This is **not** Pilot validation and is **not** a release approval. Findings remain `FIXED_GENERIC`; their Repair Set remains `IMPLEMENTED` until verification editions exist. The next gate is Human full-candidate review of PR #310.

## 2. WU-011 scope disposition

### 2.1 Discovery graph / provenance / Raw identity — satisfied

`scripts/survey_discovery_v2.py` now distinguishes same-run and external parent namespaces, requires same-run parents to resolve to an earlier research pass, rejects dangling/ambiguous parent edges, preserves discovery method/trigger provenance, and binds accepted Raw path, SHA-256 and byte count. Accepted Raw byte drift invalidates downstream authority.

### 2.2 Common fail-closed JSON Schema layer — satisfied

`scripts/survey_schema_v2.py` is the shared Draft 2020-12 gate. Missing `jsonschema` is fatal rather than silently skipped; schema errors are deterministic and semantic validators are reached only after structural validation.

### 2.3 Bounded Human Review attention — satisfied

`scripts/survey_review_attention_v2.py` exposes a bounded attention surface with stable item identity, rationale, basis SHA references, total/shown/overflow counts and explicit truncation. Basis drift fails closed.

### 2.4 Exact-byte Publication Preview → Visual Review → Freeze → merge verification → Release — satisfied

The quality/publication contracts carry one exact PDF authority across the chain. `REPOSITORY_FILE` and `GITHUB_ACTIONS_ARTIFACT` are both supported without requiring generated PDFs to be committed merely for liveness. Actions-backed authority binds repository, workflow run, artifact ID/name/digest, artifact member path, PDF SHA-256 and byte count.

Publication Candidate, Preview Approval, Visual Review, Freeze Record, Release Manifest, Merge Verification and Release Record remain exact-byte linked. Publication State semantic validation uses the same durable authority semantics. Release dispatch is bound to exact current-main Production State and Release Manifest SHA-256 values.

### 2.5 Long-form quality regression and post-transform revalidation — satisfied

The coupled quality bundle requires all configured checks to pass on the exact source/PDF pair, including subject/entity/property binding, identifier preservation, source-specific fail-closed notes, bibliography metadata, chronology/source mapping, empty-wrapper suppression, TOC hierarchy, technical-notes tail needspace, required synthesis survival, post-transform semantic revalidation and PDF preflight.

### 2.6 Weekly/Thematic handlers, workflows, allowlists and Pilot bootstrap — satisfied pre-Pilot

One handler/semantic-validator registry covers the complete stage plan. All executable stages require canonical Stage Handoff authority. The v2 production-control, release and assistant-control workflows are explicitly named in `config/survey-production-v2.json` and constrained to `main` dispatch authority.

W33/SP001 launch scope is repository-owned by:

- `schemas/pilot-bootstrap-v2.schema.json`;
- `config/survey-production-v2-pilots.json`;
- `scripts/survey_pilot_bootstrap_v2.py`;
- `docs/survey-production-core-v2-session-bootstrap.md`.

The planner is side-effect free and distinguishes clean initialization, safe resume and partial-initialization Exception Gate. SP001's `as_of` is fixed at first initialization and preserved on resume. Resume also verifies State-pinned implementation identity.

No Pilot has been started: both `sources/2026-W33/production-state.json` and `sources/SP001/production-state.json` were confirmed absent on the refactor branch and on `main` during this audit.

### 2.7 Full-candidate audit / merge preparation — satisfied up to Human review

The whole PR changed-file inventory was reviewed for unrelated production regressions. A stale Weekly workflow rollback was found as AUD-026 and repaired by restoring current-main production behavior and retaining only Core v2 CI trigger/dependency additions. `pipeline-contract-tests.yml` changes are CI-only dependency/path coverage; the annual reader-note test conversion preserves assertions while removing an undeclared pytest dependency from unittest-discover cross-regression.

PR #310 remains draft. Merge and Pilot start are intentionally outside this closure.

## 3. Findings repaired during WU-011

| Finding | Defect | Generic repair status |
|---|---|---|
| AUD-019 | repository-local-only PDF liveness assumption | `FIXED_GENERIC` |
| AUD-020 | missing canonical v2 workflow/assistant-control authority | `FIXED_GENERIC` |
| AUD-021 | external Release success could split from provenance without reconciliation | `FIXED_GENERIC` |
| AUD-022 | executed code could differ from State-pinned implementation | `FIXED_GENERIC` |
| AUD-023 | Production State did not understand artifact-backed Preview authority | `FIXED_GENERIC` |
| AUD-024 | W33/SP001 bootstrap depended on chat/test-local launch knowledge | `FIXED_GENERIC` |
| AUD-025 | Human Gate Action Spec was not persisted by canonical one-stage adoption | `FIXED_GENERIC` |
| AUD-026 | candidate regressed current-main Weekly production workflow | `FIXED_GENERIC` |

These findings must not be marked `CLOSED` until the associated Repair Set is validated by real verification editions under `scripts/survey_findings_v2.py` governance.

## 4. Key second-audit invariants

1. **Two Human Gates only**: Architecture Review and Publication Preview.
2. **No hidden deterministic stage**: one canonical adoption executes at most one deterministic stage.
3. **Gate arrival is durable**: if that transition reaches Human/Exception/Complete terminal planning, the terminal Action Spec is persisted without executing another deterministic stage.
4. **Handoff is explicit**: stage requests pin explicit inputs/outputs; no "latest artifact" discovery is production authority.
5. **Runtime is pinned**: production-control and release execute State-pinned worktree code and reject workflow/implementation drift.
6. **Release is exact-byte and reconcilable**: an existing issue-only Release is reusable only after exact identity/asset verification.
7. **Legacy production behavior is protected**: Core v2 cross-regression wiring must not roll back current-main Weekly operational behavior.
8. **Pilot launch is repository-owned**: W33/SP001 scope and start/resume rules do not come from conversation history.
9. **No pre-review Pilot**: W33/SP001 must remain uninitialized until PR #310 passes Human full-candidate review and is explicitly merged to `main`.

## 5. Validation authority

The implementation candidate is required to remain green across five cross-regression families before Human review is requested:

- Survey Production Core v2 CI;
- Screening contract CI;
- Evidence contract CI;
- Pipeline contract tests;
- Weekly pipeline spine + committed Raw integrity.

Core v2 CI currently executes the full explicit v2 suite, including Pilot bootstrap, terminal Human Gate persistence, artifact-backed Publication State, exact publication-chain and finding/Repair Set governance regressions. The final exact run IDs/head are recorded in the worklog and PR body after all metadata synchronization commits settle.

## 6. Remaining gate

The implementation team's autonomous work stops after final CI synchronization. The next legitimate action is **Human full-candidate review of PR #310**.

If approved:

1. explicitly merge the coherent candidate to `main`;
2. re-enter from `docs/survey-production-core-v2-session-bootstrap.md`;
3. run side-effect-free W33/SP001 Pilot plans from current `main`;
4. initialize only the authorized Pilot work branch;
5. run each Pilot to the requested Human Gate under canonical Stage Handoff/control authority;
6. keep the WU-011 Repair Set `IMPLEMENTED` until verification-edition evidence permits `VALIDATED`/`CLOSED` governance transitions.

If Human review identifies a defect, record a new machine-readable finding and repair it before merge rather than treating review comments as an informal side channel.
