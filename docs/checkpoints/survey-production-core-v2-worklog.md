# Survey Production Core v2 — Work Log

Status: `POST-INTEGRATION CORE CANDIDATE / PRE-HUMAN EVIDENCE-REGENERATION REPAIR / PRE-SOL REVIEW`
Established: 2026-08-22 JST  
Last updated: 2026-09-06 JST
Current maintenance branch: `fix/core-v2-pre-human-evidence-regeneration-20260905`
Historical implementation PRs: `#310` and post-integration repair `#452` (merged)
Current integration PR: `#484` — `Survey Production Core v2: pre-Human Evidence regeneration repair` (`draft` / `open` / `unmerged`); this branch is a normal draft integration review surface, not an operator transport, and must not be merged by this task
Production source of truth: current `main` at structural-recovery HEAD `2adcffdc8741605cd56a984e9fc509b6066172e1`; transparent structural-recovery descendant of `d8fa79ef2affacec49a47e6fc88018fb99f36899`, which is a structural-recovery descendant of pre-incident reviewed semantic/tree baseline `a9f121f0d65591f52b53515712d7c0bae573b2ef`; all three resolve to exact tree `b6c1b2cbc13165e64ac1d88d4d36b7515f7494da`, with zero changed files/content delta between the reviewed tree states. `d8fa79ef...` remains historical execution/base evidence for the completed repair runs; candidate `5b1f72c...` is semantically unchanged by this reconciliation.
Semantic authority: `docs/survey-production-core-v2-authority.md`  
Final-audit rule: `docs/survey-production-core-v2-final-audit-rule.md`

## 1. Ledger contract

This file is the persistent **pre-audit implementation-status snapshot** for Survey Production Core v2. Repository reality outranks this summary. Frozen historical releases remain immutable.

The candidate tree intentionally stops at a stable PRE-FREEZE state until the current pre-freeze task completes. Exact-head CI, the later seven-point final-audit verdict, and the final freeze result are recorded outside the audited candidate tree in PR/Human-review metadata. This file must not be edited after freeze merely to record a PASS, because that would change the audited SHA.

Historical audit attempts remain evidence only:

- `2f3c9b10c031cf0d8e5cc114fb93e481e90fffac` was invalidated by AUD-039 through AUD-044;
- `68213aaca4ef6d47cf4c06dfe7ae501e3db78b6d` was invalidated by AUD-045;
- `705937af2eb45d5ba361fe748d7a622110bcb27c` completed the then-current five-point audit but was invalidated by AUD-046 when the Owner clarified formal Grok/X Source Intake + Google Drive handoff;
- AUD-047 then made autonomous progression / stop discipline an independent acceptance dimension. The canonical final audit now has seven fixed points, with Human Gate round-trip viability as Point 7.
- `c565a3254ad303bd276edee55b2b1e6e0a1c91a7` reached the pre-audit freeze boundary, but its subsequent audit was invalidated by a current-facing authority wording contradiction. Its CI/audit evidence is historical only; the replacement candidate requires fresh synchronization, exact-head CI, and a new freeze.

## 2. Stable pre-audit snapshot

- Repository: `eariver/japanese-generative-ai-survey`
- Maintenance branch: `fix/core-v2-pre-human-evidence-regeneration-20260905`
- Production `main`: `2adcffdc8741605cd56a984e9fc509b6066172e1` at the current structural-recovery HEAD. It is a transparent structural-recovery descendant of `d8fa79ef2affacec49a47e6fc88018fb99f36899`, itself descended from pre-incident reviewed baseline `a9f121f0d65591f52b53515712d7c0bae573b2ef`; all three have exact tree `b6c1b2cbc13165e64ac1d88d4d36b7515f7494da` and zero content delta between the reviewed tree states. Current main SHA remains authoritative for repository reality; `d8fa79ef...` remains historical execution/base evidence for the completed repair runs.
- PR #310: historical implementation PR, merged.
- PR #452: historical post-integration operator/Thematic repair PR, merged; its narrow amendment remains current authority where applicable.
- WU-010R: historical `COMPLETE / SECOND-AUDIT GREEN`.
- WU-011: historical `COMPLETE / SECOND-AUDIT GREEN`; its exact-byte/Raw safety evidence remains historical evidence for its then-current scope.
- WU-012: `POST-INTEGRATION REPAIRS IMPLEMENTED / PRE-FREEZE CANDIDATE`.
- WU-012 Repair Set: `REPAIR-WU012-2026-08-22`, status `IMPLEMENTED`; it remains not `VALIDATED/CLOSED` pending explicit approval/merge of this candidate and fresh post-integration validation. Completed W33/SP001 runs are historical evidence, not pending cold starts.
- AUD-031 / AUD-033 remain intentionally `DEFERRED`.
- AUD-027–030, AUD-032, AUD-034–047 are `FIXED_GENERIC` where applicable.
- W33: released historical edition; its production artifacts remain immutable.
- SP001: released historical edition; its production artifacts remain immutable.
- W34: active production-regression edition; this maintenance branch uses only its exact read-only fixture and does not write the W34 branch.
- SP002, SP003: no canonical production-state file or canonical work branch in current `main`; outside this Core maintenance candidate's production scope.

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
| **WU-012** | **`POST-INTEGRATION REPAIRS IMPLEMENTED / PRE-FREEZE CANDIDATE`** | ChatGPT-first hot path, post-integration transport/Thematic repairs, and strict Screening expansion/active-acceptance authority |

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
- **AUD-047:** autonomous progression / stop discipline is an independent acceptance dimension. Formal Gate count alone is insufficient if ChatGPT still pauses repeatedly during routine internal work.

### G — Screening expansion and active acceptance authority

The current maintenance candidate keeps the accepted root Discovery separate from the effective downstream Discovery basis. Derived Screening Discovery is valid only through complete mechanically validated accepted-root provenance closure; arbitrary unrelated substitution, Raw/source/obligation drift, and silent root loss remain fail-closed.

Historical content-addressed Screening acceptances remain immutable. After Screening advancement, downstream helpers resolve only the exact `screening-acceptance` artifact adopted by the passed State-bound Screening Stage Checkpoint. Directory count, mtime, digest order, and latest-file heuristics are not authority. Evidence, Materiality, Completeness, Selection, and Architecture use the same effective derived basis.

### H — Pre-Human Evidence regeneration repair (2026-09-05)

The maintenance candidate adds a supported operator-side invalidation for an exact, unpresented pending Human Gate surface. It is distinct from Human `REQUEST_CHANGES`: `human_decision=false`, no Human review index row is written, no Human revision/provenance is created, and no active Human approval may be crossed. The operation validates the exact prior State/Gate inputs and reachable work-branch commit, derives the safe regeneration boundary from Core config, supersedes affected mutable canonical singleton/checkpoint files, records their prior path/SHA authority, and derives the resumable State through the existing Core state-control machinery.

Post-Screening authority expansion is represented by an edition-local Evidence Authority Supplement. Each exact Raw body is bound to one non-DROP Discovery/Evidence task with source class, locator, chronology, retrieval provenance, byte count, and SHA-256. Evidence Cards may cite only the task's Discovery source or explicitly bound supplement source; Screening decisions/history are not rewritten.

Active Evidence and Edition View acceptance is resolved from the passed State-bound Evidence Stage Checkpoint and exact named artifacts. The View acceptance must bind the same Evidence acceptance SHA. Historical accepted runs remain immutable and may coexist.

## 7. Finding / Repair Set status

`FIXED_GENERIC`:

- AUD-027, AUD-028, AUD-029, AUD-030
- AUD-032, AUD-034, AUD-035, AUD-036
- AUD-037, AUD-038
- AUD-039, AUD-040, AUD-041, AUD-042, AUD-043, AUD-044, AUD-045, AUD-046, AUD-047

Intentional `DEFERRED`:

- AUD-031 — machine Series engine; add only if real Foundations production demonstrates need.
- AUD-033 — exhaustive hypothetical future-edition matrix; use small structural tests + real Pilots.

`REPAIR-WU012-2026-08-22` remains `IMPLEMENTED`, not `VALIDATED/CLOSED`, because this candidate still awaits explicit approval/merge and fresh post-integration validation. W33/SP001 production runs are complete historical evidence.

## 8. External final-validation handoff

The candidate tree does not claim its own final PASS. The current pre-freeze sequence is:

```text
finish all candidate changes and authority synchronization
-> obtain exact-head diagnostic CI
-> freeze that exact head
-> audit acceptance points 1–7 from zero on the unchanged head
-> any required candidate-tree change invalidates the whole audit
-> after repair/synchronization/CI, rerun all seven from point 1
-> if unchanged all-PASS, record exact SHA + CI run IDs + seven verdicts in PR/Human-review metadata
```

The seven acceptance points are:

1. Weekly viability, including required Grok/X + Drive handoff;
2. Special viability, including profile-appropriate X applicability;
3. generality beyond named pilots;
4. historical/clarified requirement recurrence prevention;
5. control proportionality;
6. autonomous progression / stop discipline;
7. Human Gate round-trip viability.

The pre-freeze task must at minimum obtain exact-head evidence for:

1. `Survey Production Core v2 CI`;
2. `Pipeline contract tests`.

The broader final audit/CI matrix remains governed by `docs/survey-production-core-v2-final-audit-rule.md`.

The external PR/Human-review record, not this snapshot, is authoritative for whether a frozen head completed those checks successfully.

## 9. Production boundary

Do not:

- use this maintenance branch to alter W33/W34/SP001 production;
- mark the Repair Set `VALIDATED/CLOSED` before real verification editions;
- add a machine Series engine or exhaustive synthetic matrix without production evidence;
- add Human Gates beyond Architecture Review and Publication Preview;
- stop for routine internally resolvable stages or repairs;
- treat Grok/X transport as Human editorial approval;
- promote X claims directly to technical Evidence without authoritative verification;
- restore legacy Handoff ceremony as the canonical local hot path;
- reuse a verdict from an invalidated audit.

If an exact frozen head later receives the required CI PASS and all seven acceptance points PASS without candidate mutation, PR metadata may present that exact head for Human full-candidate review. The candidate tree itself remains this stable pre-freeze/frozen snapshot.
