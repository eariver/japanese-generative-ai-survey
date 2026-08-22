# Survey Production Core v2 — Work Log

Status: `ACTIVE / WU-011 COMPLETE / HUMAN FULL-CANDIDATE REVIEW`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`  
Plan: `docs/survey-production-core-v2-improvement-plan.md`  
Semantic authority: `docs/survey-production-core-v2-authority.md`  
WU-011 exit evidence: `docs/survey-production-core-v2-wu011-second-audit-closure.md`  
Pilot bootstrap: `docs/survey-production-core-v2-session-bootstrap.md`

## 1. Ledger contract

This file is the persistent **work-status** authority for Survey Production Core v2. It owns current work-unit status, validation notes, unresolved execution issues, and the exact next action. Semantic/design policy remains owned by the authority index and its referenced contracts/audits.

Repository reality is the highest factual authority. Current `main` remains the production source of truth until a coherent v2 candidate is Human-reviewed and explicitly merged. Frozen historical releases are never rewritten by this improvement work.

## 2. Current snapshot

Last updated: **2026-08-22 JST — WU-011 complete; stopped at Human full-candidate review boundary**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Production `main`: `2086b396d2f30103d9292b722891be436cd28db5`; unchanged through WU-011 closure.
- Validated WU-011 implementation head: `6d82b0deff7e20adfedf95d2e139fd56867e5d40`.
- Draft PR: `#310 Survey Production Core v2 implementation`; remains **draft** and must not be merged without Human full-candidate review.
- Current phase: **Phase 3 — Core v2 Candidate Implementation / Human review boundary**.
- **WU-010R: COMPLETE / SECOND-AUDIT GREEN.**
- **WU-011: COMPLETE / SECOND-AUDIT GREEN / 5-of-5 CROSS-REGRESSION GREEN.**
- WU-010R Repair Set: `REPAIR-WU010R-2026-08-22`; `IMPLEMENTED`, verification editions empty.
- WU-011 Repair Set: `REPAIR-WU011-2026-08-22`; `IMPLEMENTED`, verification editions empty; all five pre-Pilot CI validation rows are PASS and real Pilot verification remains PENDING.
- WU-011 machine findings AUD-019 through AUD-026: all `FIXED_GENERIC`; none may become `CLOSED` before Repair Set governance permits it.
- External W33/SP001 production: **NOT STARTED / NOT AUTHORIZED** before Human review + merge.
- Confirmed absent on both refactor branch and `main`: `sources/2026-W33/production-state.json`, `sources/SP001/production-state.json`.

## 3. Durable rollout rules

- W33 = **Weekly Profile First Production Validation**; legacy W33 state is comparison/provenance only, not a migration target.
- SP001 = **Thematic Profile First Production Validation** with genuine expansion/closure and no fabricated bounded history window.
- W34 follows W33 finding consolidation; SP002/SP003 follow SP001 finding consolidation.
- Normal Human Gates: Architecture Review, then exact-byte Publication Preview. Candidate Selection remains internal.
- First external Pilots start only after the full production-capable candidate is Human-reviewed and explicitly merged to `main`.
- Pilot sessions start/resume only through `docs/survey-production-core-v2-session-bootstrap.md` and `scripts/survey_pilot_bootstrap_v2.py`; chat history is not launch authority.

## 4. Phase / work-unit status

| Work unit | Status | Exit / primary evidence |
|---|---|---|
| WU-000 | `COMPLETE_WITH_AUDIT_AMENDMENT` | improvement plan + persistent checkpoint |
| WU-001 / WU-001A | `COMPLETE / AMENDED` | component inventory + Profile-pollution audit |
| WU-002 | `COMPLETE / AMENDED` | normalized Core/Profile/Human-Gate/temporal/release contracts |
| WU-003 / WU-003B / WU-003C | `COMPLETE` | historical invariants + all-15 Special production deep audit |
| WU-004 / WU-004B | `COMPLETE / SUPERSEDED IN PART` | authoritative Phase 3 second-audit amendment |
| WU-005 | `COMPLETE / AUDIT FINDING REPAIRED` | Profile/State/contract+implementation identity; AUD-014 hardened in WU-010R |
| WU-006 | `COMPLETE / POST-AUDIT HARDENED` | Discovery/Screening v2; AUD-003 closure implemented in WU-011 |
| WU-007 | `COMPLETE / POST-AUDIT HARDENED` | factual Evidence + Edition View + Materiality + Completeness |
| WU-008 | `COMPLETE / AUDITED` | Matrix + internal Selection + generic Architecture + Review Summary |
| WU-008A | `COMPLETE / AUDITED` | whole-system audit remediation + 5/5 cross-regression green |
| WU-009 | `COMPLETE / AUDITED` | generic Draft Package/Result + Profile Synthesis |
| WU-010 | `SUPERSEDED BY WU-010R REMEDIATION` | original orchestration baseline retained; Human re-audit reopened closure |
| WU-010R | `COMPLETE / SECOND-AUDIT GREEN` | AUD-013–018 repaired; 5/5 cross-regression green; Repair Set IMPLEMENTED |
| **WU-011** | **`COMPLETE / SECOND-AUDIT GREEN / HUMAN REVIEW BOUNDARY`** | AUD-003/004/005 + AUD-019–026 repaired; exact publication/release/bootstrap path; 5/5 final cross-regression green |

## 5. WU-010R durable closure

The WU-010 Human re-audit opened AUD-013 through AUD-018. WU-010R repaired them without weakening Core/Profile separation or changing frozen production releases.

Durable outcomes include exact semantic Validation Attestations, State-pinned checkpoint/Human-Gate provenance, transitive Action Spec basis identity, independent Architecture Approval Records, action-specific retry/idempotency semantics, Repair-Set-governed Finding closure, and semantic/work-status authority separation.

WU-010R validated implementation head: `35dd8881ba83bf106ae6d934ad0212d2e0eafb47`. Closure head: `108fd86dca5fe47cd1d437e41e97c0935614ca20`.

Closure validation:

| Validation family | Result | Run |
|---|---|---|
| Survey Production Core v2 CI | `PASS` — 71 tests + contract parse + Repair Set dogfood | `32554336720` |
| Screening contract CI | `PASS` | `32554336704` |
| Evidence contract CI | `PASS` | `32554336693` |
| Pipeline contract tests | `PASS` | `32554336697` |
| Weekly pipeline spine + committed Raw integrity | `PASS` | `32554336694` |

## 6. WU-011 implemented scope

WU-011 closed the remaining pre-Pilot implementation blockers and performed a full PR second audit.

### 6.1 Original integrated-audit blockers

- **AUD-003:** same-run/external Discovery graph namespaces, earlier-pass parent resolution, structured discovery trigger/method provenance, accepted Raw path/SHA-256/byte count, fail-closed Raw drift.
- **AUD-004:** one shared Draft 2020-12 JSON Schema gate before semantic validators; missing `jsonschema` is fatal.
- **AUD-005:** bounded item-level Human Review attention with stable basis identity and explicit total/shown/overflow/truncation.

### 6.2 Exact publication and quality chain

- quality binds one exact source/PDF pair and requires the full long-form regression family including post-transform semantic revalidation;
- PDF authority supports `REPOSITORY_FILE` and durable `GITHUB_ACTIONS_ARTIFACT` identity;
- Candidate → Publication Preview → Visual Review → Freeze → Release Manifest → Merge Verification → Release Record carries the same exact PDF SHA-256/byte count;
- Production State understands artifact-backed Publication Preview authority;
- Release dispatch is bound to exact current-main Production State and Release Manifest SHA-256 inputs;
- existing issue-only Release reconciliation is allowed only after tag/title/target and exact asset-byte verification.

### 6.3 Orchestration / workflow authority

- all executable stages use one settled handler/semantic-validator registry and require canonical Stage Handoff authority;
- production-control, release and assistant-control v2 workflows are explicitly named and allowlisted;
- production-control/release execute State-pinned worktree code and reject current-main workflow drift;
- generic `adopt-stage` cannot adopt `FROZEN`; release has its dedicated workflow;
- one adopted action executes at most one deterministic stage;
- when that transition reaches Human/Exception/Complete terminal planning, the terminal Action Spec is persisted without executing another deterministic stage;
- Architecture and Publication Preview approval workflows consume those exact State-bound Human Gate Action Specs.

### 6.4 Repository-owned Pilot bootstrap

Added:

- `schemas/pilot-bootstrap-v2.schema.json`;
- `config/survey-production-v2-pilots.json`;
- `scripts/survey_pilot_bootstrap_v2.py`;
- `docs/survey-production-core-v2-session-bootstrap.md`.

The planner is side-effect free and resolves W33/SP001 launch identity without chat history. It distinguishes clean initialization, safe resume and partial-initialization Exception Gate. W33 keeps its fixed completed issue window. SP001 sets `as_of` once at initialization and preserves it on resume. Resume validates Profile identity, State semantics and State-pinned executable implementation.

### 6.5 Full-candidate second-audit findings

| Finding | Repair |
|---|---|
| AUD-019 | durable Actions-artifact PDF authority |
| AUD-020 | canonical v2 workflow identities + assistant-control allowlist |
| AUD-021 | exact external Release reconciliation/idempotency |
| AUD-022 | State-pinned executable implementation/workflow identity |
| AUD-023 | State semantic support for artifact-backed Publication Preview |
| AUD-024 | W33/SP001 registry + planner/initializer + session bootstrap |
| AUD-025 | terminal Human/Exception/Complete Action Spec persistence |
| AUD-026 | restore current-main Weekly production workflow; retain only v2 cross-regression wiring |

All are `FIXED_GENERIC`. The machine Repair Set is `docs/checkpoints/survey-production-core-v2-audit-findings/WU-011-repair-set.json`, status `IMPLEMENTED`.

## 7. WU-011 final cross-regression evidence

Validated implementation head:

```text
6d82b0deff7e20adfedf95d2e139fd56867e5d40
```

All five required regression families passed on that exact head:

| Validation family | Result | GitHub Actions run |
|---|---|---|
| Survey Production Core v2 CI | `PASS` — 106 tests + contract parse, including final authority/Repair Set/Pilot-stop regression | `32563066810` |
| Screening contract CI | `PASS` | `32563066833` |
| Evidence contract CI | `PASS` | `32563066808` |
| Pipeline contract tests | `PASS` | `32563066856` |
| Weekly pipeline spine + committed Raw integrity | `PASS` | `32563066801` |

The final Core CI initially exposed two CI sparse-checkout omissions for the newly repository-owned worklog/closure/bootstrap authorities. Those were CI-harness defects only; after all four final authority documents were included, the exact head above passed the complete 106-test suite. No production semantic defect was introduced by those harness repairs.

`REPAIR-WU011-2026-08-22` records these five runs as PASS while remaining `IMPLEMENTED`, not `VALIDATED/CLOSED`, because W33/SP001 verification editions are intentionally empty.

## 8. Current action / stop condition

**STOP: Human full-candidate review of PR #310 is now the required gate.**

Autonomous WU-011 implementation, second audit, cross-regression, Repair Set evidence synchronization and merge preparation are complete.

Do not:

- start W33 or SP001;
- mark WU-011 Repair Set `VALIDATED` or `CLOSED`;
- close AUD-019 through AUD-026;
- merge PR #310 without explicit Human approval.

If Human review approves the candidate:

1. explicitly merge PR #310 to `main`;
2. re-enter from `docs/survey-production-core-v2-session-bootstrap.md`;
3. run side-effect-free W33/SP001 Pilot plans from the merged `main`;
4. initialize only the authorized Pilot work branch;
5. proceed under canonical Stage Handoff/control authority until the requested Human Gate or an Exception Gate.

If Human review identifies a defect, create a new machine-readable Finding and Repair Set update before merge rather than handling the review comment as an informal side channel.
