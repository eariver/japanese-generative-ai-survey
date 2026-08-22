# Survey Production Core v2 — Work Log

Status: `WU-012 POST-COMPLETION RE-AUDIT REPAIR IMPLEMENTED / FINAL CI + FIXED-HEAD AUDIT PENDING`  
Established: 2026-08-22 JST  
Last updated: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`  
Production source of truth until merge: current `main`  
Semantic authority: `docs/survey-production-core-v2-authority.md`  
Final-audit rule: `docs/survey-production-core-v2-final-audit-rule.md`

## 1. Ledger contract

This file is the persistent work-status authority for Survey Production Core v2. Repository reality outranks this summary. Frozen historical releases remain immutable.

The former WU-012 pre-approval closure and its final-PASS claim are historical only. The Owner required the five acceptance points to be audited **after all candidate changes are complete**. Re-auditing former synchronized head `2f3c9b10c031cf0d8e5cc114fb93e481e90fffac` from zero found AUD-039 through AUD-044, so Human full-candidate review was left and repair work resumed.

## 2. Current snapshot

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Production `main`: `2086b396d2f30103d9292b722891be436cd28db5` at the last verified production check.
- PR #310: `draft / open / unmerged`.
- WU-010R: historical `COMPLETE / SECOND-AUDIT GREEN`.
- WU-011: historical `COMPLETE / SECOND-AUDIT GREEN` with its then-current cross-regression evidence retained.
- WU-012: `POST-COMPLETION RE-AUDIT REPAIRS IMPLEMENTED / FINAL CANDIDATE NOT YET FROZEN`.
- WU-012 Repair Set: `REPAIR-WU012-2026-08-22`, status `IMPLEMENTED`; real Pilot validation intentionally pending.
- AUD-031 / AUD-033 remain intentionally `DEFERRED`.
- AUD-039 through AUD-044 are implemented as `FIXED_GENERIC` and included in the Repair Set; final candidate cross-regression/fixed-head audit is still required.
- W33, W34, SP001, SP002, SP003: `NOT STARTED / NOT AUTHORIZED BEFORE APPROVAL + MERGE`.

## 3. Corrected operating premise

**ChatGPT is the primary research/editorial operator.**

Normal edition work remains:

```text
user target + requested stopping Human Gate
-> ChatGPT reads repository authority/Profile/State
-> ChatGPT performs research/editorial reasoning
-> deterministic helpers protect crisp/repetitive/provenance invariants
-> exact semantic stage artifacts are validated
-> compact Stage Checkpoint records artifact/review/tool/contract provenance
-> continue autonomously
-> stop only at Architecture Review, Publication Preview, or genuine Exception Gate
```

Normal production Human Gates remain exactly:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

The Core-v2 five-point final audit is a change-management acceptance rule, not another edition Human Gate.

## 4. Work-unit status

| Work unit | Status | Current conclusion |
|---|---|---|
| WU-000 | `COMPLETE_WITH_AUDIT_AMENDMENT` | improvement program established |
| WU-001 / 001A | `COMPLETE` | Core/Profile/Publication/Series ownership retained |
| WU-002 | `COMPLETE` | two Human Gates + Profile separation retained |
| WU-003 / 003B / 003C | `COMPLETE` | historical invariant/deep-production corpus retained |
| WU-004 / 004B | `COMPLETE` | minimum vertical-slice evidence retained |
| WU-005 | `COMPLETE WITH WU-012 CORRECTION` | initialization provenance is not an edition-wide tool lock |
| WU-006 | `COMPLETE` | Discovery/Screening/Raw provenance retained |
| WU-007 | `COMPLETE` | Evidence/Materiality/Completeness retained with substantive ChatGPT completeness judgment |
| WU-008 / 008A | `COMPLETE` | Matrix/internal Selection/Architecture retained |
| WU-009 | `COMPLETE` | structured Draft/Synthesis retained |
| WU-010 / 010R | `HISTORICALLY COMPLETE` | defect lessons retained; local control ceremony superseded |
| WU-011 | `HISTORICALLY COMPLETE` | exact publication/release authority retained |
| **WU-012** | **`REPAIR IMPLEMENTED / FINAL CI + FIXED-HEAD AUDIT PENDING`** | ChatGPT-first hot path plus post-completion audit repairs |

## 5. WU-012 baseline implementation retained

### A — ChatGPT-first operator contract

ChatGPT owns open-ended research/editorial reasoning. Scripts own deterministic/repetitive/provenance-sensitive work. User target + requested stopping Human Gate is sufficient input.

### B — compact local orchestration

Canonical local control is Production State + exact canonical stage artifacts + compact Stage Checkpoint. `stage_plan[*].handoff_required=false`. Legacy Action/Handoff machinery remains compatibility/audit code only.

### C — controlled toolchain evolution

Initialization implementation identity is historical provenance. A reviewed generic fix may be used later in an edition only after it is actually integrated into the edition work branch. Accepted boundaries affected by the change are revalidated/migrated selectively; prior checkpoint provenance is not rewritten.

### D — Issue Prevention Checklist

Recurring Human Review defects have explicit deterministic / ChatGPT research / ChatGPT editorial / ChatGPT visual / Human / legacy ownership.

### E — generic bootstrap/profile support

Weekly, bounded Retrospective Period and Thematic Profiles remain generic. Thematic Pilot scope comes from canonical planning authority. Foundations uses its living series memo rather than a premature machine Series engine.

### F — quality tiers

Quality review remains `DETERMINISTIC / AGENT_SEMANTIC / AGENT_VISUAL`. Only deterministic checks require executable result authority.

## 6. Post-completion audit findings and repairs

The fixed old head `2f3c9b10...` audit found six blocking families. All have generic implementations and regressions in the current candidate tree:

### AUD-039 — semantic stage authority

Repair:

- added `scripts/survey_stage_validation_v2.py`;
- validates exact Discovery/Screening/Evidence/Selection/Architecture/Draft/Quality/Publication/Freeze authorities;
- Draft requires paired `draft-package:<id>` / `draft-result:<id>`;
- emits exact `CORE_STAGE_CONTRACT` result;
- `survey_agent_control_v2.py` requires and independently reconciles that result before compact checkpoint adoption;
- same-named fake files or fabricated PASS reports are insufficient.

Regression: `tests/test_survey_stage_validation_v2.py` + `tests/test_survey_agent_control_v2.py`.

### AUD-040 — actual current-tool adoption

Repair:

- generic main repair must be integrated into the edition work branch before use;
- integrated work-branch head is checkpoint execution identity;
- `scripts/survey_agent_tool_v2.py` provides a narrow allowlisted bridge for legacy Screening/Evidence helpers that still enforce historical pin semantics internally;
- current-stage validation uses agent-first State/current contract while preserving initialization and earlier checkpoint provenance.

Regression: `tests/test_survey_stage_validation_v2.py` and agent-control tool-evolution tests.

### AUD-041 — all-changes-first final audit

Repair:

- added `docs/survey-production-core-v2-final-audit-rule.md`;
- AGENTS/session bootstrap/authority reference it;
- all candidate changes/CI/docs/Finding/Repair-Set synchronization must finish before candidate freeze;
- any candidate mutation after audit starts invalidates the entire audit and all five points are rerun from point 1;
- final PASS is recorded externally in PR/Human-review metadata keyed to the exact audited SHA.

Regression: `tests/test_survey_final_audit_rule_v2.py`.

### AUD-042 — exact Production Profile-bound Quality

Repair:

- Quality Bundle requires exact `production_profile_path` and hashes it;
- research/publication applicability derives only from that Profile;
- issue-ID fallback is removed;
- Retrospective Period checks cannot silently become Thematic checks;
- Publication Candidate build/validation rejects publication-profile divergence from its coupled Quality/Profile authority.

Regressions: `tests/test_survey_quality_v2.py`, `tests/test_survey_publication_v2.py`, `tests/test_survey_profiled_freeze_v2.py`.

### AUD-043 — internal vs public Special identity

Repair:

- `scripts/survey_profiled_freeze_v2.py` derives public slug from exact Profile `paths.survey_root` basename;
- Retrospective internal `SP-2025-H2` retains public `special/2025-H2` and `2025-H2` title/asset identity;
- Release workflow rederives and fail-closes on the same Profile authority;
- SP001/Weekly public identities remain natural.

Regression: `tests/test_survey_profiled_freeze_v2.py`.

### AUD-044 — bounded Period completion guard

Repair:

- `scripts/survey_period_v2.py` requires `as_of >= end` before Retrospective Period Profile creation/initialization.

Regression: `tests/test_survey_period_v2.py`.

## 7. Finding / Repair Set status

`FIXED_GENERIC`:

- AUD-027, AUD-028, AUD-029, AUD-030
- AUD-032, AUD-034, AUD-035, AUD-036
- AUD-037, AUD-038
- AUD-039, AUD-040, AUD-041, AUD-042, AUD-043, AUD-044

Intentional `DEFERRED`:

- AUD-031 — machine Series engine; add only if real Foundations production demonstrates need.
- AUD-033 — exhaustive hypothetical future-edition matrix; use small structural tests + real Pilots.

`REPAIR-WU012-2026-08-22` remains `IMPLEMENTED`, not `VALIDATED/CLOSED`, because W33/SP001 real verification editions remain intentionally empty.

## 8. Validation evidence status

Earlier green heads and runs are historical evidence only. They do not prove the current repaired candidate.

Former synchronized review head `2f3c9b10c031cf0d8e5cc114fb93e481e90fffac` is explicitly invalid as final-review evidence because its post-completion five-point audit discovered AUD-039 through AUD-044.

Before final candidate freeze, the complete repaired/synchronized head must pass all five required cross-regression families:

1. Survey Production Core v2 CI;
2. Screening contract CI;
3. Evidence contract CI;
4. Pipeline contract tests;
5. Weekly pipeline spine + committed Raw integrity.

Current status: **PENDING on the fully synchronized repair candidate**.

## 9. Mandatory final audit after all changes

Only after code/config/schema/workflow/tests/Findings/Repair Set/authority/worklog/plan/closure/PR preparation are complete and cross-regression is green:

```text
freeze exact candidate head SHA
-> perform acceptance point 1 Weekly viability from zero
-> point 2 Special viability from zero
-> point 3 generality from zero
-> point 4 historical Issue recurrence prevention from zero
-> point 5 control proportionality from zero
-> make no candidate-tree change while auditing
```

If any point requires a repository change:

```text
current audit = INVALIDATED
-> repair/synchronize everything
-> rerun cross-regression
-> freeze new head
-> rerun all five points from point 1
```

The final audit result is not committed into the audited candidate tree. It is recorded against the exact SHA in PR/Human-review metadata.

## 10. Current action / stop condition

**CURRENT ACTION: finish synchronization and obtain five-family green CI. This is not yet the Human full-candidate review boundary.**

Do not:

- start W33/SP001 before explicit approval + merge;
- mark the Repair Set `VALIDATED/CLOSED` before real verification editions;
- add a machine Series engine or exhaustive synthetic matrix without real evidence;
- add Human Gates beyond Architecture Review and Publication Preview;
- restore legacy Handoff ceremony as the canonical local hot path;
- claim final five-point PASS from any audit that preceded later candidate changes.

After all synchronization and CI are complete, freeze one exact head and run the mandatory five-point final audit. Only an unchanged all-PASS head may be presented for Human full-candidate review.
