# Survey Production Core v2 — Work Log

Status: `WU-012 + AUD-046 + AUD-047 REPAIRS IMPLEMENTED / PRE-AUDIT CANDIDATE / FINAL RESULT EXTERNAL`  
Established: 2026-08-22 JST  
Last updated: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`  
Production source of truth until merge: current `main`  
Semantic authority: `docs/survey-production-core-v2-authority.md`  
Final-audit rule: `docs/survey-production-core-v2-final-audit-rule.md`

## 1. Ledger contract

This file is the persistent **pre-audit implementation-status snapshot** for Survey Production Core v2. Repository reality outranks this summary. Frozen historical releases remain immutable.

The candidate tree intentionally stops at a stable PRE-AUDIT state. Exact-head cross-regression and the six-point final-audit verdict are recorded outside the audited candidate tree in PR/Human-review metadata. This file therefore does not need a post-audit PASS edit that would change the audited SHA.

Historical audit attempts remain evidence only:

- `2f3c9b10c031cf0d8e5cc114fb93e481e90fffac` was invalidated by AUD-039 through AUD-044;
- `68213aaca4ef6d47cf4c06dfe7ae501e3db78b6d` was invalidated by AUD-045;
- `705937af2eb45d5ba361fe748d7a622110bcb27c` completed the then-current five-point audit but was invalidated by AUD-046 when the Owner clarified formal Grok/X Source Intake + Google Drive handoff;
- AUD-047 then expanded final acceptance from five to six points so autonomous progression / stop discipline is independently re-audited.

## 2. Stable pre-audit snapshot

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Production `main`: `2086b396d2f30103d9292b722891be436cd28db5` at the last verified production check.
- PR #310: `draft / open / unmerged` until explicit Human approval.
- WU-010R: historical `COMPLETE / SECOND-AUDIT GREEN`.
- WU-011: historical `COMPLETE / SECOND-AUDIT GREEN`; its exact-byte/Raw safety evidence remains historical evidence for its then-current scope.
- WU-012: `REPAIRS IMPLEMENTED / PRE-AUDIT CANDIDATE`.
- WU-012 Repair Set: `REPAIR-WU012-2026-08-22`, status `IMPLEMENTED`; it remains not `VALIDATED/CLOSED` until real W33/SP001 verification editions exist.
- AUD-031 / AUD-033 remain intentionally `DEFERRED`.
- AUD-027–030, AUD-032, AUD-034–047 are `FIXED_GENERIC` where applicable.
- W33, W34, SP001, SP002, SP003: `NOT STARTED / NOT AUTHORIZED BEFORE APPROVAL + MERGE`.

## 3. Operating premise

**ChatGPT is the primary research/editorial operator.**

```text
user target + requested stopping Human Gate
-> ChatGPT reads repository authority/Profile/State
-> ChatGPT performs research/editorial reasoning
-> conventional/direct/Grok X Source Intake as applicable
-> deterministic helpers protect crisp/repetitive/provenance invariants
-> exact semantic stage artifacts are validated
-> compact Stage Checkpoint records artifact/review/tool/contract provenance
-> Production State advances
-> continue autonomously toward the requested Gate
```

The default is continuous progression. Source Intake, Screening, Evidence, Completeness/materiality, Selection, Architecture preparation, drafting/synthesis, deterministic QA, semantic/visual repair, generic defect repair, CI retry and ordinary Drive result import do not justify asking the user whether to continue.

A production session may pause only at:

1. `ARCHITECTURE_REVIEW`;
2. exact-byte `PUBLICATION_PREVIEW`;
3. a genuine Owner-level Exception Gate;
4. unavoidable manual Grok instruction/result transport when the external Grok execution cannot be crossed directly.

The fourth item is not editorial approval and not a third Human Gate. When the Grok result is present in the configured Drive folder, ChatGPT resumes automatically.

X/Grok is Source Intake. Weekly requires it. Retrospective Period/Thematic explicitly decide applicability with rationale. Foundations uses the Thematic Profile with a dedicated Google Drive category when X is material. Grok writes Raw Observation under `Grok_X_SourseIntake`; ChatGPT imports exact bytes, dispositions the result, and verifies authoritative sources before technical claims enter Evidence.

## 4. Work-unit status

| Work unit | Status | Current conclusion |
|---|---|---|
| WU-000 | `COMPLETE_WITH_AUDIT_AMENDMENT` | improvement program established |
| WU-001 / 001A | `COMPLETE` | Core/Profile/Publication/Series ownership retained |
| WU-002 | `COMPLETE` | two Human Gates + Profile separation retained |
| WU-003 / 003B / 003C | `COMPLETE` | historical invariant/deep-production corpus retained |
| WU-004 / 004B | `COMPLETE` | minimum vertical-slice evidence retained |
| WU-005 | `COMPLETE WITH WU-012 CORRECTION` | initialization provenance is not an edition-wide tool lock |
| WU-006 | `COMPLETE WITH AUD-046 EXTENSION` | Discovery/Screening/Raw provenance retained; X/Grok Raw is bound into Discovery Acceptance |
| WU-007 | `COMPLETE` | Evidence/Materiality/Completeness retained with substantive ChatGPT completeness judgment |
| WU-008 / 008A | `COMPLETE` | Matrix/internal Selection/Architecture retained |
| WU-009 | `COMPLETE` | structured Draft/Synthesis retained |
| WU-010 / 010R | `HISTORICALLY COMPLETE` | defect lessons retained; local control ceremony superseded |
| WU-011 | `HISTORICALLY COMPLETE` | exact publication/release authority retained |
| **WU-012** | **`REPAIRS IMPLEMENTED / PRE-AUDIT CANDIDATE`** | ChatGPT-first hot path plus all current generic repairs, including Grok/X and autonomous stop discipline |

## 5. WU-012 implementation retained

### A — ChatGPT-first operator contract

ChatGPT owns open-ended research/editorial reasoning. Scripts own deterministic/repetitive/provenance-sensitive work. User target + requested stopping Human Gate is sufficient input.

### B — compact local orchestration

Canonical local control is Production State + exact canonical stage artifacts + deterministic `CORE_STAGE_CONTRACT` validation + one compact Stage Checkpoint. `stage_plan[*].handoff_required=false`. Legacy Action/Handoff machinery remains compatibility/audit code only.

### C — controlled toolchain evolution

Initialization implementation identity is historical provenance. A reviewed generic fix may be used later only after integration into the edition work branch. Affected accepted boundaries are revalidated/migrated selectively; prior checkpoint provenance is not rewritten.

### D — Issue Prevention Checklist

Recurring Human Review defects, Grok/X boundaries and stop-discipline expectations have explicit deterministic / ChatGPT research / ChatGPT editorial / ChatGPT visual / Human / legacy ownership.

### E — generic bootstrap/profile support

Weekly, bounded Retrospective Period and Thematic Profiles remain generic. Thematic scope comes from canonical planning authority. Foundations uses its living series memo rather than a premature machine Series engine.

### F — quality tiers

Quality review remains `DETERMINISTIC / AGENT_SEMANTIC / AGENT_VISUAL`. Applicability binds the exact Production Profile. Only deterministic checks require executable result authority.

## 6. Post-completion repairs

- **AUD-039:** exact semantic stage validation through `scripts/survey_stage_validation_v2.py` + mandatory `CORE_STAGE_CONTRACT`.
- **AUD-040:** reviewed generic fixes must be integrated into the edition work branch before use.
- **AUD-041:** final-audit rule owns all-changes-first, fixed-head, restart-from-point-1 semantics and external result recording.
- **AUD-042:** Quality Bundle binds exact Production Profile; no issue-ID profile inference.
- **AUD-043:** internal Retrospective identity remains distinct from public identity derived from Profile `survey_root`.
- **AUD-044:** Retrospective Period cannot initialize before its bounded period end.
- **AUD-045:** canonical status uses audit-stable PRE-AUDIT wording and external final-result recording.
- **AUD-046:** X/Grok is a formal Source Intake subflow with Profile policy, Google Drive handoff, exact Raw import and mandatory Discovery/no-material disposition.
- **AUD-047:** final acceptance has a sixth independent point for autonomous progression / stop discipline. Formal Gate count alone is insufficient if ChatGPT still pauses repeatedly during routine internal work.

## 7. Finding / Repair Set status

`FIXED_GENERIC`:

- AUD-027, AUD-028, AUD-029, AUD-030
- AUD-032, AUD-034, AUD-035, AUD-036
- AUD-037, AUD-038
- AUD-039, AUD-040, AUD-041, AUD-042, AUD-043, AUD-044, AUD-045, AUD-046, AUD-047

Intentional `DEFERRED`:

- AUD-031 — machine Series engine; add only if real Foundations production demonstrates need.
- AUD-033 — exhaustive hypothetical future-edition matrix; use small structural tests + real Pilots.

`REPAIR-WU012-2026-08-22` remains `IMPLEMENTED`, not `VALIDATED/CLOSED`, because W33/SP001 production verification remains intentionally pending.

## 8. External final-validation handoff

The candidate tree does not claim its own final PASS. When synchronization is complete:

```text
obtain five-family green CI on one exact head
-> freeze that exact head
-> audit acceptance points 1–6 from zero on the unchanged head
-> any required candidate-tree change invalidates the whole audit
-> after repair/synchronization/CI, rerun all six from point 1
-> if unchanged all-PASS, record exact SHA + CI run IDs + six verdicts in PR/Human-review metadata
```

The six acceptance points are:

1. Weekly viability, including required Grok/X + Drive handoff;
2. Special viability, including profile-appropriate X applicability;
3. generality beyond named pilots;
4. historical/clarified requirement recurrence prevention;
5. control proportionality;
6. autonomous progression / stop discipline.

Required CI families remain five:

1. Survey Production Core v2 CI
2. Screening contract CI
3. Evidence contract CI
4. Pipeline contract tests
5. Weekly pipeline spine + committed Raw integrity

The external PR/Human-review record, not this snapshot, is authoritative for whether a frozen head completed those checks successfully.

## 9. Production boundary

Do not:

- start W33/SP001 before explicit approval + merge;
- mark the Repair Set `VALIDATED/CLOSED` before real verification editions;
- add a machine Series engine or exhaustive synthetic matrix without production evidence;
- add Human Gates beyond Architecture Review and Publication Preview;
- stop for routine internally resolvable stages or repairs;
- treat Grok/X transport as Human editorial approval;
- promote X claims directly to technical Evidence without authoritative verification;
- restore legacy Handoff ceremony as the canonical local hot path;
- reuse a verdict from an invalidated audit.

If an exact frozen head later receives five-family CI PASS and all six acceptance points PASS without candidate mutation, PR metadata may present that exact head for Human full-candidate review. The candidate tree itself remains this stable pre-audit snapshot.
