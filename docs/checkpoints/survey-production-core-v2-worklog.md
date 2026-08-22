# Survey Production Core v2 — Work Log

Status: `ACTIVE / canonical improvement-work checkpoint`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`  
Plan: `docs/survey-production-core-v2-improvement-plan.md`  
Semantic authority: `docs/survey-production-core-v2-authority.md`

## 1. Ledger contract

This file is the persistent **work-status** authority for Survey Production Core v2. It owns current work-unit status, validation notes, unresolved execution issues, and the exact next action. Semantic/design policy remains owned by the authority index and its referenced contracts/audits.

Repository reality is the highest factual authority. Current `main` remains the production source of truth until a coherent v2 candidate is reviewed and explicitly merged. Frozen historical releases are never rewritten by this improvement work.

Detailed earlier work-unit history remains recoverable from Git history; this ledger is intentionally compacted around the current resume point.

## 2. Current snapshot

Last updated: **2026-08-22 JST — WU-010 closed after post-implementation audit; HOLD for Human re-audit**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Production `main`: `2086b396d2f30103d9292b722891be436cd28db5` — rechecked immediately before WU-010 closure and unchanged.
- WU-009 audited head: `9d58c01b50b220ea9cdfc11f6258e9b44ea676ee`.
- WU-010 audited implementation head: `b2e55a7b1316d75e44efd8df0b09a5ff8a9f8831`.
- Draft PR: `#310 Survey Production Core v2 implementation`; remains draft.
- Current phase: **Phase 3 — Core v2 Candidate Implementation**.
- Active work unit: **none — HOLD FOR HUMAN RE-AUDIT**.
- **WU-011 has NOT started.**
- External W33/SP001 production: **NOT STARTED / NOT AUTHORIZED** until WU-011/full-candidate review and merge to `main`.

## 3. Durable rollout rules

- W33 = **Weekly Profile First Production Validation**; legacy W33 state is comparison/provenance only, not a migration target.
- SP001 = **Thematic Profile First Production Validation** with genuine expansion/closure and no fabricated bounded history window.
- W34 follows W33 finding consolidation; SP002/SP003 follow SP001 finding consolidation.
- Normal Human Gates: Architecture Review, then exact-byte Publication Preview. Candidate Selection remains internal.
- First external Pilots start only after a full path through Publication Preview/Freeze/Release is merged to `main`.

## 4. Phase / work-unit status

| Work unit | Status | Exit / primary evidence |
|---|---|---|
| WU-000 | `COMPLETE_WITH_AUDIT_AMENDMENT` | improvement plan + persistent checkpoint |
| WU-001 / WU-001A | `COMPLETE / AMENDED` | component inventory + Profile-pollution audit |
| WU-002 | `COMPLETE / AMENDED` | normalized Core/Profile/Human-Gate/temporal/release contracts |
| WU-003 / WU-003B / WU-003C | `COMPLETE` | historical invariants + all-15 Special production deep audit |
| WU-004 / WU-004B | `COMPLETE / SUPERSEDED IN PART` | authoritative Phase 3 second-audit amendment |
| WU-005 | `COMPLETE / AUDIT HARDENED` | Profile/State/contract+implementation identity |
| WU-006 | `COMPLETE / POST-AUDIT HARDENED` | Discovery/Screening v2 + self-contained archive |
| WU-007 | `COMPLETE / POST-AUDIT HARDENED` | factual Evidence + Edition View + Materiality + Completeness |
| WU-008 | `COMPLETE / AUDITED` | Matrix + internal Selection + generic Architecture + Review Summary |
| WU-008A | `COMPLETE` | whole-system audit remediation + 5/5 cross-regression green |
| WU-009 | `COMPLETE / AUDITED` | generic Draft Package/Result + Profile Synthesis |
| **WU-010** | **`COMPLETE / POST-AUDIT HARDENED`** | executable orchestration + exact-byte Architecture Human Gate + Finding/Repair Set |
| **WU-011** | **`PLANNED / NOT STARTED`** | P0 quality/provenance integration + full Pilot bootstrap |

## 5. WU-009 closure anchor

WU-009 established the profile-neutral post-Architecture semantic path:
- immutable `PROPOSED` Architecture plus independent Approval Record consumption;
- generic Draft Package / Draft Result;
- exact factual Evidence and subject/identifier preservation;
- must-cover and boundary preservation;
- generic Profile Synthesis envelope;
- separate Profile/Publication extension preservation validator.

Final WU-009 audited head `9d58c01b50b220ea9cdfc11f6258e9b44ea676ee` passed Core v2, Screening, Evidence, Pipeline contract, and Weekly spine including Raw integrity.

## 6. WU-010 completion record

Authoritative guidance:
- `docs/survey-production-core-v2-minimum-vertical-slice-audit-amendment.md` §§14–16;
- `docs/survey-production-core-v2-minimum-vertical-slice-second-audit-amendment.md` §§5, 8, 10;
- `docs/survey-production-core-v2-whole-system-audit-2026-08-22.md`, especially AUD-001/AUD-006/AUD-011.

### 6.1 Implemented contracts and tooling

Added / integrated:
- `schemas/action-spec-v2.schema.json`;
- `schemas/action-result-v2.schema.json`;
- `schemas/review-finding-v2.schema.json`;
- `schemas/repair-set-v2.schema.json`;
- `scripts/survey_orchestrator_v2.py`;
- `scripts/survey_findings_v2.py`;
- `tests/test_survey_orchestrator_v2.py`;
- `tests/test_survey_findings_v2.py`;
- orchestration contract in `config/survey-production-v2.json`;
- WU-010 schemas in `pipeline_contract_sha256`;
- WU-010 modules/schemas/tests in Survey Production Core v2 CI.

### 6.2 Executable orchestration guarantees

The WU-010 orchestrator now provides:
- deterministic `plan_action()` from authoritative Production State/Profile and repository artifacts;
- `advance-to-gate()` loop that executes registered deterministic handlers and replans without reconstructing stage order from chat;
- action kinds `LOCAL_SCRIPT | WORKFLOW_DISPATCH | HUMAN_GATE | COMPLETE | EXCEPTION` selected from explicit stage contracts;
- immutable Action Spec and Action Result provenance;
- exact required-input / expected-output / State / contract / implementation basis;
- State/checkpoint advancement only after outputs validate;
- normal terminals limited to `HUMAN_GATE_REACHED`, `EXCEPTION_GATE_REQUIRED`, or `COMPLETE`;
- retryable deterministic failures remain recovery conditions and do not create Human or Exception Gates by themselves.

### 6.3 AUD-011 — State-pinned implementation identity closed

Runtime authority is the implementation SHA already pinned in Production State.

Hardening performed during WU-010 audit:
1. committed changes under `config`, `schemas`, `scripts`, or `.github/workflows` are rejected when they differ from the State-pinned implementation;
2. staged and unstaged controlled-path changes are rejected;
3. **untracked** controlled-path files are also rejected;
4. artifact-only commits may move repository `HEAD` without becoming implementation authority;
5. Action identity ignores only the observational HEAD field, allowing a pre-issued Action Spec to survive an artifact-only commit while all State/contract/implementation/artifact bases remain strict;
6. every handler invocation and Action Result carries the State-pinned implementation SHA rather than defaulting to current `HEAD`.

Regression coverage includes committed control drift, untracked control drift, artifact-only HEAD movement, and pre-issued Action Spec stability.

**AUD-011 is closed by WU-010.**

### 6.4 State / Action Result crash consistency

The initial executor could conceptually leave advanced State without a finalized successful Action Result if the process died between writes.

WU-010 now uses recoverable transaction files:
- prepared next State;
- pending successful Action Result containing before/after State SHA;
- atomic State replacement;
- Action Result finalization.

On resume, pending transactions are reconciled only when current State matches the recorded before/after identity. Divergent state fails closed.

Regression `test_interrupted_state_result_commit_is_recoverable_without_silent_divergence` simulates a crash after State replacement and proves deterministic recovery without replaying the stage or losing successful provenance.

### 6.5 AUD-001 — exact-byte Architecture Human Gate authority closed

Human Gate 1 now has a continuous exact-byte chain:

```text
Architecture stage
  -> canonical architecture-v2.json
  -> canonical architecture-review-summary-v2.json
  -> Human Gate Action Spec required_inputs with exact path + SHA-256
  -> Architecture Approval Record carrying the same two SHA-256 values
  -> Drafting consumes that Approval Record
```

The Architecture stage cannot advance unless the canonical Architecture and Review Summary outputs exist and match the Action Spec output contract. The terminal Human Gate Action Spec binds those exact files and bytes. Approval then refuses any Architecture/Review Summary bytes that differ from the reviewed Action Spec. Architecture remains immutable `PROPOSED`; approval is a separate record.

Regression `test_reviewed_architecture_cannot_be_replaced_before_approval` proves a post-review byte substitution is rejected.

**AUD-001 is closed by WU-010 for Architecture Review.**

### 6.6 Review Finding / Repair Set handoff

Machine-readable Pilot feedback no longer needs ad hoc repair script semantics.

`Review Finding v2` separates:
- scope/layer;
- defect kind;
- confidence;
- whether a regression is required;
- observed/expected/actual behavior;
- workaround;
- provenance;
- improvement action / regression fixture / status.

`Repair Set v2` groups exact Findings with:
- affected components and actual layers changed;
- disposition;
- implementation commits;
- regression fixtures;
- compatibility impact;
- validation results;
- verification editions;
- lifecycle status.

Semantic validators require implemented/validated repairs to account for required regression fixtures and require validated/closed Repair Sets to have all-PASS validation plus verification editions.

Principle retained:
> A production workaround is evidence about a defect, not automatic authorization to promote that workaround into Core.

### 6.7 WU-010 post-implementation audit repairs

The following issues were found by audit after the first green implementation and repaired before closure:

1. **Untracked implementation files** — added fail-closed detection under implementation control roots.
2. **Schema-only WORKFLOW_DISPATCH** — stage `action_kind` is now contract-driven rather than hard-coded to `LOCAL_SCRIPT`.
3. **Artifact-only HEAD false staleness** — Action identity/spec comparison now treats observed HEAD as observational while keeping all authoritative bases strict.
4. **State/Result split-brain on crash** — introduced recoverable transaction semantics with exact before/after State SHA.
5. **Human review substitution gap** — Human Gate Action Spec now binds the exact Architecture + Review Summary bytes before approval; Approval Record must preserve those SHA values.

No additional WU-010-owned P0 defect remained after this audit.

### 6.8 WU-010 audited validation head

Audited implementation head:
`b2e55a7b1316d75e44efd8df0b09a5ff8a9f8831`

All five cross-regression families passed on that exact head:
- Survey Production Core v2 CI `32550363804`: **SUCCESS** — compile, **63 tests**, all v2 JSON contract parsing;
- Screening contract CI `32550363753`: **SUCCESS**;
- Evidence contract CI `32550363867`: **SUCCESS**;
- Pipeline contract tests `32550363865`: **SUCCESS**;
- Weekly pipeline spine `32550363887`: **SUCCESS** — main test job and committed Raw integrity job both green.

WU-010 changed only Core-v2 implementation/config/schema/tests/worklog/CI paths relative to the WU-009 audited head; no frozen edition or production artifact was modified.

**WU-010 exit criteria are satisfied.**

## 7. Explicitly deferred / still blocking Pilot production

The following are **not WU-010 defects** and remain deliberately open for WU-011 / pre-Pilot integration:

- **AUD-003 / WU-011 / P0 before SP001** — Discovery graph resolution, structured discovery-method/trigger provenance, accepted Raw byte identity.
- **AUD-004 / WU-011 / P0 before Pilot** — common fail-closed JSON Schema conformance layer.
- **AUD-005 / WU-011 or pre-Pilot P0** — bounded item-level exclusion/hold/non-material/duplicate Human Review surface with explicit overflow.
- **Publication Preview exact-byte authority / WU-011** — bind exact publication candidate PDF bytes through Publication Preview, Visual Review, Freeze, merge verification, and Release.
- **Pilot handler/bootstrap wiring / WU-011** — connect settled canonical stage handlers/workflow dispatches and assistant-control allowlists for W33/SP001. WU-010 provides the registry/dispatcher contract but intentionally does not start Pilot-specific bootstrap work.
- exact frozen historical replay remains a legacy provenance/compatibility concern, not a Core v2 migration requirement.

## 8. Re-audit hold

Per Human instruction, stop after WU-010 before beginning WU-011.

Resume sequence after Human re-audit:

```text
re-read current main
-> re-read this worklog and semantic authority
-> audit WU-010 implementation/contracts/CI evidence
-> record any audit findings as Review Finding / Repair Set where appropriate
-> repair/revalidate WU-010 if required
-> only after explicit continuation, start WU-011
```

**Current action: STOP. Perform Human re-audit of WU-010. Do not begin WU-011, W33, or SP001.**
