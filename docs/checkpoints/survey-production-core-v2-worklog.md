# Survey Production Core v2 — Work Log

Status: `ACTIVE / WU-012 CHATGPT-FIRST REALIGNMENT REQUIRED`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`  
Base plan: `docs/survey-production-core-v2-improvement-plan.md`  
Current pre-approval re-audit: `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md`  
Semantic authority: `docs/survey-production-core-v2-authority.md`  
WU-011 historical exit evidence: `docs/survey-production-core-v2-wu011-second-audit-closure.md`

## 1. Ledger contract

This file is the persistent **work-status** authority for Survey Production Core v2. It owns current work-unit status, validation notes, unresolved execution issues, and the exact next action. Semantic/design policy remains owned by the authority index and its referenced contracts/audits.

Repository reality is the highest factual authority. Current `main` remains the production source of truth until a coherent v2 candidate is Human-reviewed and explicitly merged. Frozen historical releases are never rewritten by this improvement work.

## 2. Corrected production premise

The 2026-08-22 pre-approval re-audit corrected a material premise mismatch in the first WU-012 audit.

**ChatGPT is the primary research/editorial operator.** The repository exists to guide and preserve ChatGPT's reasoning work, make sessions resumable, provide efficient deterministic helpers, and prevent recurrence of known Human Review defects. The target is not an external workflow engine that makes every editorial judgment machine-provable.

Use tools for deterministic/repetitive/provenance-sensitive work. Keep open-ended Source Intake strategy, completeness judgment, selection, architecture, drafting, synthesis and editorial/visual review as explicit ChatGPT reasoning tasks with repository-backed records.

This premise is authoritative for WU-012 and supersedes the machine-first remediation language in `docs/survey-production-core-v2-improvement-plan.md` §§16–18 where they conflict.

## 3. Current snapshot

Last updated: **2026-08-22 JST — ChatGPT-first re-audit complete; WU-012 narrowed to agent-first simplification/guidance hardening**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Production `main`: `2086b396d2f30103d9292b722891be436cd28db5`; unchanged during the re-audit.
- Validated WU-011 implementation head: `6d82b0deff7e20adfedf95d2e139fd56867e5d40`.
- WU-011 metadata/Human-review handoff head: `8beaf978793d983cc7608f4ca9c534511dd04d7a`; historical 5/5 green evidence remains valid.
- First pre-approval audit amendment commit: `5cfbfabb8e097d9fe369af04c0219cb213266415`; its machine-first remediation is now superseded where conflicting.
- ChatGPT-first re-audit document commit: `909fb2a42b7688986569a51ff0f782a657c259fe`.
- Draft PR #310 remains **draft / unmerged / not ready for approval**.
- WU-010R: historical `COMPLETE / SECOND-AUDIT GREEN`.
- WU-011: historical `COMPLETE / SECOND-AUDIT GREEN / 5-of-5 CROSS-REGRESSION GREEN` against its then-current scope.
- WU-012: `PLANNED / PRE-MERGE BLOCKER`, now defined by the ChatGPT-first re-audit rather than the earlier machine-first §§16–18 plan.
- WU-010R Repair Set: `REPAIR-WU010R-2026-08-22`, `IMPLEMENTED`, Pilot verification pending.
- WU-011 Repair Set: `REPAIR-WU011-2026-08-22`, `IMPLEMENTED`, Pilot verification pending.
- External W33/SP001 production: **NOT STARTED / NOT AUTHORIZED**. W34/SP002/SP003 likewise remain unstarted.

## 4. Phase / work-unit status

| Work unit | Status | Current conclusion |
|---|---|---|
| WU-000 | `COMPLETE_WITH_AUDIT_AMENDMENT` | improvement program established |
| WU-001 / WU-001A | `COMPLETE / RETAIN` | Core/Profile/Publication/Series ownership is aligned with ChatGPT-first operation |
| WU-002 | `COMPLETE / RETAIN WITH LIGHTER MACHINE INTERPRETATION` | two Human Gates and Profile separation remain correct |
| WU-003 / WU-003B / WU-003C | `COMPLETE / STRONG` | historical invariant distillation is a core asset; make it an agent review playbook |
| WU-004 / WU-004B | `COMPLETE / RETAIN` | first-slice architecture is valid; do not demand exhaustive synthetic future-edition proof |
| WU-005 | `COMPLETE / WU-012C CORRECTION` | Profile/State useful; edition-wide implementation pin is too strict |
| WU-006 | `COMPLETE / RETAIN` | Discovery/Screening/Raw provenance are useful support tools; Source Intake judgment remains agent-owned |
| WU-007 | `COMPLETE / WU-012A/D GUIDANCE HARDENING` | Evidence/Materiality/Completeness useful; Completeness is a reasoned ChatGPT record, not externally provable truth |
| WU-008 / WU-008A | `COMPLETE / STRONG` | Matrix/internal Selection/Architecture organize agent reasoning without extra Human Gates |
| WU-009 | `COMPLETE / STRONG` | structured drafting/synthesis improves traceability; nuanced prose review remains agent-owned |
| WU-010 / WU-010R | `HISTORICALLY COMPLETE / WU-012B SIMPLIFICATION` | control-plane provenance was over-serialized for a ChatGPT-operated process |
| WU-011 | `HISTORICALLY COMPLETE / PARTLY RETAIN` | exact publication/release authority retained; local-stage control and Pilot scope authority need simplification |
| **WU-012** | **`PLANNED / PRE-MERGE BLOCKER`** | ChatGPT-first operating contract, lighter local orchestration, toolchain evolution, Issue prevention playbook, small bootstrap gaps, quality-review tiers |

## 5. WU-011 evidence retained

WU-011 remains valid historical evidence for the mechanisms it actually proved, especially:

- accepted Raw exact-byte provenance and drift rejection;
- schema/semantic validation of structured stage artifacts;
- bounded Architecture Review attention surface;
- exact Publication Candidate → Publication Preview → Visual Review → Freeze → Release Manifest → Merge Verification → Release Record PDF identity;
- durable Actions-artifact PDF authority;
- issue-only Release exact-byte reconciliation/idempotency;
- restoration/protection of unrelated current-main Weekly workflow behavior.

Validated implementation head `6d82b0deff7e20adfedf95d2e139fd56867e5d40` passed:

| Validation family | Result | Run |
|---|---|---|
| Survey Production Core v2 CI | PASS | `32563066810` |
| Screening contract CI | PASS | `32563066833` |
| Evidence contract CI | PASS | `32563066808` |
| Pipeline contract tests | PASS | `32563066856` |
| Weekly pipeline spine + committed Raw integrity | PASS | `32563066801` |

These runs do not prove the new WU-012 operator-model requirements.

## 6. Corrected pre-approval finding status

The first pre-approval audit created AUD-027 through AUD-034. Their remediation has now been re-evaluated under the ChatGPT-first premise.

| Finding | Current status | Corrected interpretation |
|---|---|---|
| AUD-027 | `OPEN` | Completeness needs explicit ChatGPT research-review guidance/rationale, not external proof of every search |
| AUD-028 | `OPEN` | Weekly Issue #9 must become a mandatory agent editorial checklist; deterministic helpers only where crisp |
| AUD-029 | `OPEN` | Quality must distinguish `DETERMINISTIC`, `AGENT_SEMANTIC`, `AGENT_VISUAL`; semantic PASS need not pretend to be a validator result |
| AUD-030 | `OPEN` | add a lightweight generic bounded-Period bootstrap/profile helper |
| AUD-031 | `DEFERRED` | full machine Series engine is premature; existing Foundations living design memo is sufficient initial Series authority |
| AUD-032 | `OPEN` | SP001 bootstrap should reference TS-001 canonical planning authority rather than duplicate/narrow its scope |
| AUD-033 | `DEFERRED` | exhaustive synthetic future-edition fixture matrix is unnecessary; use small structural tests + real Pilots |
| AUD-034 | `OPEN` | convert historical Issues into a stage/profile-aware agent/tool/Human prevention checklist |
| AUD-035 | `OPEN` | Core v2 does not explicitly model ChatGPT as operator and over-serializes every local stage |
| AUD-036 | `OPEN` | edition-wide implementation commit pin blocks controlled adoption of reviewed generic tool fixes during the same edition |

No WU-012 Repair Set exists yet. Do not mark these findings fixed until the corrected WU-012 implementation exists.

## 7. Corrected WU-012 scope

Authoritative detail: `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md`.

### WU-012A — ChatGPT-first operating contract

- state explicitly that ChatGPT is the research/editorial operator;
- scripts/workflows support deterministic/repetitive/provenance work;
- Source Intake strategy, completeness, Selection, Architecture, drafting, synthesis and semantic/visual review remain reasoned agent work;
- target + requested Human Gate remains sufficient user input.

### WU-012B — simplify local orchestration

- retain one authoritative Production State, canonical stage outputs and minimum checkpoint provenance;
- remove mandatory local Action Spec/Handoff Request/Handoff/Action Result/Validation Attestation ceremony where it adds no distinct safety property;
- retain richer request/receipt authority for external/irreversible actions where it is justified;
- preserve exactly two normal Human approval records.

### WU-012C — controlled toolchain evolution

- record implementation/tool commit per checkpoint/action;
- permit later stages to use newer reviewed `main` tooling;
- targeted revalidation/migration only when changed code affects accepted artifact contracts;
- Exception Gate only when compatibility cannot safely be determined;
- exact-byte publication/release authority remains unchanged.

### WU-012D — Issue Prevention Checklist

Map material historical defect families to one primary owner:

```text
DETERMINISTIC_TOOL_CHECK
CHATGPT_RESEARCH_REVIEW
CHATGPT_EDITORIAL_REVIEW
CHATGPT_VISUAL_REVIEW
HUMAN_ARCHITECTURE_REVIEW
HUMAN_PUBLICATION_PREVIEW
LEGACY_ONLY / NOT_APPLICABLE
```

The checklist must be short enough to be practical and explicit enough that a new session does not depend on reviewer memory.

### WU-012E — small generic bootstrap/profile gaps

- add lightweight Retrospective Period profile/bootstrap support;
- change SP001/Thematic bootstrap to reference canonical backlog/series planning authority rather than duplicating detailed scope;
- add only small structural genericity tests for arbitrary Weekly/Period/Thematic inputs;
- do not build a machine Series engine before real Foundations work demonstrates a need.

### WU-012F — quality-review tiers

- classify review items as `DETERMINISTIC`, `AGENT_SEMANTIC`, or `AGENT_VISUAL`;
- only deterministic items require executable validator evidence;
- agent semantic/visual review records bind the reviewed source/PDF revision and record concise evidence/finding;
- applicability is Profile/Publication-aware;
- no new normal Human Gate.

## 8. Current action / stop condition

**CURRENT ACTION: implement corrected WU-012A–F before asking for Human approval again.**

Do not:

- approve or merge PR #310 in its current form;
- start W33, W34, SP001, SP002 or SP003;
- implement the superseded full machine Series engine requirement from the first audit;
- implement the superseded exhaustive synthetic future-edition fixture matrix;
- convert every semantic/visual historical Issue into a deterministic validator;
- retain edition-wide implementation lock-in merely for provenance;
- add routine Human Gates beyond Architecture Review and Publication Preview.

Required sequence:

1. implement WU-012A–F in the order that minimizes control-plane churn;
2. create/update regression tests only for deterministic behavior actually retained;
3. create a separate WU-012 Repair Set after generic repairs exist;
4. run a whole-candidate re-audit against Weekly viability, Special viability, generality, Issue recurrence prevention and over-validation risk;
5. synchronize plan/authority/bootstrap/AGENTS/PR review package;
6. stop again at **Human full-candidate review of PR #310**;
7. only after explicit approval and merge may W33/SP001 production validation begin.
