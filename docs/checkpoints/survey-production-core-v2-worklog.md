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

## 2. Current snapshot

Last updated: **2026-08-22 JST — WU-010R started after Human re-audit**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Production `main`: `2086b396d2f30103d9292b722891be436cd28db5` — rechecked immediately before WU-010R and unchanged.
- Pre-remediation branch head: `f6ec62603ca126acf532c7288863db3ad4fc7e6d`.
- WU-009 audited head: `9d58c01b50b220ea9cdfc11f6258e9b44ea676ee`.
- WU-010 audited implementation head: `b2e55a7b1316d75e44efd8df0b09a5ff8a9f8831`.
- Draft PR: `#310 Survey Production Core v2 implementation`; remains draft.
- Current phase: **Phase 3 — Core v2 Candidate Implementation**.
- Active work unit: **WU-010R — Human re-audit remediation**.
- **WU-011 has NOT started.**
- External W33/SP001 production: **NOT STARTED / NOT AUTHORIZED** until WU-010R, WU-011, full-candidate review and merge to `main` are complete.

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
| WU-005 | `COMPLETE / AUDIT FINDING LINKED` | Profile/State/contract+implementation identity; AUD-014 remediation owned by WU-010R |
| WU-006 | `COMPLETE / POST-AUDIT HARDENED` | Discovery/Screening v2 + self-contained archive; AUD-003 remains WU-011 |
| WU-007 | `COMPLETE / POST-AUDIT HARDENED` | factual Evidence + Edition View + Materiality + Completeness |
| WU-008 | `COMPLETE / AUDITED` | Matrix + internal Selection + generic Architecture + Review Summary |
| WU-008A | `COMPLETE` | whole-system audit remediation + 5/5 cross-regression green |
| WU-009 | `COMPLETE / AUDITED` | generic Draft Package/Result + Profile Synthesis |
| WU-010 | `REOPENED BY HUMAN RE-AUDIT` | prior orchestration implementation remains baseline, but closure was too strong |
| **WU-010R** | **`IN_PROGRESS`** | repair AUD-013 through AUD-018 and revalidate |
| **WU-011** | **`PLANNED / NOT STARTED`** | P0 quality/provenance integration + full Pilot bootstrap |

## 5. WU-010 baseline retained

The following WU-010 capabilities remain valid and are not being discarded:
- deterministic `plan_action()` / `advance_to_gate()`;
- immutable Action Spec and Action Result artifacts;
- State-pinned implementation identity across artifact-only commits;
- implementation-control drift rejection;
- recoverable State/Action Result transaction semantics;
- exact-byte Architecture + Review Summary binding in Human Gate Action Spec;
- independent Architecture Approval Record consumed by Drafting;
- machine-readable Review Finding / Repair Set contracts.

The Human re-audit found that these mechanisms need stronger fail-closed authority and provenance semantics before WU-011.

## 6. WU-010R Human re-audit findings

### AUD-013 — P0 before Pilot — semantic checkpoint / Human Gate attestation

Observed: a registered stage handler can return expected output names/paths/SHAs and cause machine checkpoints to become `passed` without the orchestrator itself proving the output satisfies the stage semantic contract. Synthetic WU-010 tests demonstrated that a schema/semantic-invalid minimal Architecture could reach Architecture Review and approval.

Required repair:
- checkpoint advancement requires an explicit validation attestation tied to exact output bytes;
- Human Gate entry/approval revalidates the exact reviewed artifacts or consumes an exact validation attestation whose validator identity and input/output SHAs are bound;
- regression must prove invalid Architecture cannot become `architecture=passed` or be approved.

### AUD-014 — P0 before autonomous Pilot — Production State self-consistency/provenance

Observed: `production-state.json` is the sole lifecycle authority, but basis verification does not prove lifecycle/history/checkpoint/gate/next-action consistency or that approved gates/checkpoints have authoritative evidence.

Required repair:
- add fail-closed State semantic validation;
- require the exact machine-checkpoint set;
- bind checkpoint validation provenance and Human Gate approval provenance in State;
- validate lifecycle/history monotonicity and current-state agreement;
- validate `next_action` / `terminal_reason` from controller semantics rather than trusting arbitrary state bytes.

### AUD-015 — P1 / P0 before autonomous provenance reliance — Action Spec stage inputs

Observed: normal Action Specs bind State/Profile but not the exact stage-specific upstream artifacts actually consumed by the handler.

Required repair:
- stage contracts declare required input artifacts;
- `plan_action()` resolves path + SHA for every stage input;
- Action identity therefore changes when a stage input changes;
- regression proves stale/input-drift Action Spec rejection.

### AUD-016 — P1 now / P0 before WORKFLOW_DISPATCH wiring — retry/idempotency

Observed: one global retry policy retries all handler exceptions, including possible future external workflow dispatches, risking duplicate dispatch after ambiguous network failure.

Required repair:
- retry policy is action/stage specific;
- `WORKFLOW_DISPATCH` defaults to non-retryable unless an idempotency/reconciliation contract is explicit;
- Action Spec records idempotency key/mode or equivalent dispatch semantics;
- regression proves workflow dispatch is not blindly retried.

### AUD-017 — P1 — semantic authority synchronization

Observed: worklog closed AUD-001/AUD-011, while the higher semantic authority index still listed them as open.

Required repair:
- update authority index directly rather than adding another amendment document;
- distinguish repaired AUD-001/AUD-011 from new AUD-013–AUD-018;
- keep AUD-003/AUD-004/AUD-005 open for WU-011.

### AUD-018 — P2 now / P1 before Pilot feedback loop — Finding/Repair closure governance

Observed: a Finding can become `CLOSED` without proving membership in a validated/closed Repair Set.

Required repair:
- standalone Finding may not close without an explicit Repair Set resolution reference, or closure is derived from the Repair Set registry;
- validator must fail closed when a closed Finding has no validated repair authority;
- regression required.

## 7. WU-010R implementation sequence

1. strengthen Production State schema/semantic validator and provenance fields;
2. add stage input and validation-attestation contracts to orchestration;
3. make checkpoint advancement depend on exact semantic validation evidence;
4. strengthen Architecture Human Gate fail-closed validation;
5. define retry/idempotency behavior by action kind/stage;
6. tighten Finding/Repair closure semantics;
7. synchronize semantic authority and PR/worklog status;
8. run focused regressions, then all five cross-regression families;
9. perform a second WU-010R audit before marking complete.

## 8. Still deliberately deferred to WU-011

These remain valid pre-Pilot blockers but are not being conflated with WU-010R:
- **AUD-003** — Discovery graph resolution, structured discovery-method/trigger provenance, accepted Raw byte identity;
- **AUD-004** — common fail-closed JSON Schema conformance layer for model/external artifacts (after State schema is strengthened by WU-010R);
- **AUD-005** — bounded item-level exclusion/hold/non-material/duplicate Human Review surface with explicit overflow;
- exact-byte Publication Preview → Visual Review → Freeze → merge verification → Release authority;
- settled W33/SP001 production handler/bootstrap wiring and assistant-control/workflow allowlists.

## 9. Current action

**WU-010R is IN_PROGRESS. Do not begin WU-011, W33, or SP001 until this work unit is repaired, tested, audited, and recorded complete.**
