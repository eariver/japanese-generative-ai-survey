# Survey Production Core v2 — Work Log

Status: `ACTIVE / WU-012 PRE-APPROVAL HARDENING REQUIRED`  
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

Last updated: **2026-08-22 JST — pre-approval WU-001–WU-011 audit reopened the merge gate; WU-012 required before Human approval**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Production `main`: `2086b396d2f30103d9292b722891be436cd28db5`; unchanged through this pre-approval audit.
- Validated WU-011 implementation head: `6d82b0deff7e20adfedf95d2e139fd56867e5d40`.
- WU-011 metadata/Human-review handoff head: `8beaf978793d983cc7608f4ca9c534511dd04d7a`; 5/5 green before the new audit amendment.
- Pre-approval audit plan amendment: `5cfbfabb8e097d9fe369af04c0219cb213266415`.
- Draft PR: `#310 Survey Production Core v2 implementation`; remains **draft / unmerged**. Its previous Human-approval boundary is superseded by WU-012.
- Current phase: **Phase 3 — Core v2 Candidate Implementation / pre-merge hardening**.
- **WU-010R: COMPLETE / SECOND-AUDIT GREEN.**
- **WU-011: IMPLEMENTATION COMPLETE / WORK UNIT COMPLETE / SECOND-AUDIT GREEN / 5-of-5 CROSS-REGRESSION GREEN.** WU-011 remains valid historical closure against its then-current exit condition.
- **WU-012: PLANNED / BLOCKING / NOT YET IMPLEMENTED.** It was opened by the explicit pre-approval audit requested before PR approval.
- WU-010R Repair Set: `REPAIR-WU010R-2026-08-22`; `IMPLEMENTED`, verification editions empty.
- WU-011 Repair Set: `REPAIR-WU011-2026-08-22`; `IMPLEMENTED`, verification editions empty; all five pre-Pilot CI validation rows are PASS and real Pilot verification remains PENDING.
- WU-011 machine findings AUD-019 through AUD-026: all `FIXED_GENERIC`; none may become `CLOSED` before Repair Set governance permits it.
- WU-012 pre-approval findings AUD-027 through AUD-034: **OPEN**.
- External W33/SP001 production: **NOT STARTED / NOT AUTHORIZED**. W34/SP002/SP003 are likewise not authorized.
- Confirmed absent through WU-011 closure: `sources/2026-W33/production-state.json`, `sources/SP001/production-state.json`.

## 3. Durable rollout rules

- W33 = **Weekly Profile First Production Validation**; legacy W33 state is comparison/provenance only, not a migration target.
- SP001 = **Thematic Profile First Production Validation** with genuine expansion/closure and no fabricated bounded history window.
- W34 follows W33 finding consolidation; SP002/SP003 follow SP001 finding consolidation.
- Normal Human Gates remain exactly: Architecture Review, then exact-byte Publication Preview. Candidate Selection remains internal.
- WU-012 must **not** add routine Human Gates to solve machine-validation problems.
- First external Pilots start only after WU-012 repair, a new whole-candidate audit, Human full-candidate approval, and explicit merge to `main`.
- Pilot sessions start/resume only through repository-owned Core v2 bootstrap authority; chat history is not launch authority.

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
| WU-007 | `COMPLETE / POST-AUDIT HARDENED` | factual Evidence + Edition View + Materiality + Completeness; WU-012A now hardens coverage authority |
| WU-008 | `COMPLETE / AUDITED` | Matrix + internal Selection + generic Architecture + Review Summary |
| WU-008A | `COMPLETE / AUDITED` | whole-system audit remediation + 5/5 cross-regression green |
| WU-009 | `COMPLETE / AUDITED` | generic Draft Package/Result + Profile Synthesis; WU-012B/C now harden final Profile/quality semantics |
| WU-010 | `SUPERSEDED BY WU-010R REMEDIATION` | original orchestration baseline retained; Human re-audit reopened closure |
| WU-010R | `COMPLETE / SECOND-AUDIT GREEN` | AUD-013–018 repaired; 5/5 cross-regression green; Repair Set IMPLEMENTED |
| **WU-011** | **`COMPLETE / SECOND-AUDIT GREEN`** | AUD-003/004/005 + AUD-019–026 repaired; exact publication/release/bootstrap path; 5/5 final cross-regression green |
| **WU-012** | **`PLANNED / PRE-MERGE BLOCKER`** | AUD-027–034; coverage authority, Weekly semantics, executable Profile-aware quality, Period initializer, Series layer, Pilot scope fidelity, generalization fixtures, Issue→Guard audit |

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

WU-011 closed its then-known pre-Pilot implementation blockers and performed a full PR second audit. The later pre-approval audit does not erase that work; it identified additional readiness requirements at a broader acceptance level.

### 6.1 Original integrated-audit blockers

- **AUD-003:** same-run/external Discovery graph namespaces, earlier-pass parent resolution, structured discovery trigger/method provenance, accepted Raw path/SHA-256/byte count, fail-closed Raw drift.
- **AUD-004:** one shared Draft 2020-12 JSON Schema gate before semantic validators; missing `jsonschema` is fatal.
- **AUD-005:** bounded item-level Human Review attention with stable basis identity and explicit total/shown/overflow/truncation.

### 6.2 Exact publication and quality chain

- quality binds one exact source/PDF pair and requires configured checks;
- PDF authority supports `REPOSITORY_FILE` and durable `GITHUB_ACTIONS_ARTIFACT` identity;
- Candidate → Publication Preview → Visual Review → Freeze → Release Manifest → Merge Verification → Release Record carries the same exact PDF SHA-256/byte count;
- Production State understands artifact-backed Publication Preview authority;
- Release dispatch is bound to exact current-main Production State and Release Manifest SHA-256 inputs;
- existing issue-only Release reconciliation is allowed only after tag/title/target and exact asset-byte verification.

WU-012C now specifically hardens the **authority and applicability of individual quality-check PASS results**; it does not invalidate WU-011's exact publication-byte chain.

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

The planner is side-effect free and resolves W33/SP001 launch identity without chat history. WU-012F must correct SP001 scope fidelity before actual initialization, and WU-012G must prove broader generic startup behavior beyond the named Pilots.

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
| Survey Production Core v2 CI | `PASS` — 106 tests + contract parse | `32563066810` |
| Screening contract CI | `PASS` | `32563066833` |
| Evidence contract CI | `PASS` | `32563066808` |
| Pipeline contract tests | `PASS` | `32563066856` |
| Weekly pipeline spine + committed Raw integrity | `PASS` | `32563066801` |

The metadata/Human-review handoff head `8beaf978793d983cc7608f4ca9c534511dd04d7a` was also 5/5 green. Those results remain historical evidence for WU-011, but they do **not** prove the newly opened WU-012 acceptance requirements.

`REPAIR-WU011-2026-08-22` remains `IMPLEMENTED`, not `VALIDATED/CLOSED`, because W33/SP001 verification editions are intentionally empty.

## 8. Pre-approval audit findings / WU-012 scope

The user-requested approval audit evaluated the candidate in priority order: Weekly viability → Special viability → generality → recurrence prevention → excessive-gate/validation risk.

New machine findings:

| Finding | Blocking gap | WU-012 owner |
|---|---|---|
| AUD-027 | mandatory completeness can self-assert `SATISFIED` without Source Intake/search support | WU-012A |
| AUD-028 | Weekly Issue #9 reader semantics not enforced through final Draft/Publication | WU-012B |
| AUD-029 | quality checks are free-text self-attested and universally over-applied | WU-012C |
| AUD-030 | first-class Retrospective Period has no canonical initializer | WU-012D |
| AUD-031 | Foundations Series Research Layer is planned but not executable | WU-012E |
| AUD-032 | SP001 registry scope is narrower than TS-001 backlog authority | WU-012F |
| AUD-033 | generalization proof remains W33/SP001-centric | WU-012G |
| AUD-034 | historical Human Review defects lack one explicit Issue→Guard ownership map | WU-012H |

The authoritative detailed repair plan is `docs/survey-production-core-v2-improvement-plan.md` §§16–18.

## 9. Current action / stop condition

**CURRENT ACTION: implement WU-012 before asking for Human approval again.**

Do not:

- approve or merge PR #310 in its current form;
- start W33, W34, SP001, SP002 or SP003;
- mark WU-012 Findings fixed/closed before implementation/regression evidence exists;
- add routine Human Gates to solve WU-012 machine-validation defects;
- retroactively modify WU-011 Repair Set to pretend these newly discovered requirements were already included.

Required sequence:

1. implement WU-012A–H in priority order, with criterion 1 (Weekly viability) taking precedence on conflicts;
2. create a separate WU-012 Repair Set after generic repairs exist;
3. run whole-system and cross-regression audit including later/unlisted Weekly/Thematic/Period/Series fixtures;
4. synchronize plan/worklog/Authority/PR evidence;
5. stop again at **Human full-candidate review of PR #310**;
6. only after explicit approval and merge may external W33/SP001 production begin.
