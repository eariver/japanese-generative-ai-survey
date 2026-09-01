# Survey Production Core v2 — Whole-System Audit Remediation Closure

Status: `CLOSED / WU-009 ENTRY AUTHORIZED`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Audit: `docs/survey-production-core-v2-whole-system-audit-2026-08-22.md`  
Audited remediation head: `f064dd0627864ae796b89ed8cc16ef83ad91b589`  
Production `main` rechecked at closure: `2086b396d2f30103d9292b722891be436cd28db5`

## 1. Closure decision

The WU-008 completion audit and the WU-005–WU-008 whole-system audit are complete. The short audit-remediation unit (WU-008A) has closed the defects that blocked entry into WU-009.

This closure does **not** authorize external W33 or SP001 production. External Pilots remain blocked until the full production-capable v2 candidate through Publication Preview / Freeze / Release has been implemented, reviewed, and merged to `main`.

## 2. Findings repaired in WU-008A

### AUD-002 — Thematic closure counters

`survey_completeness_v2.py` now derives thematic expansion/final-pass counters from Discovery provenance instead of trusting self-reported closure counters. Completeness obligation rows also fail closed on contract-shape/ref/dimension errors.

### AUD-009 — completed Weekly issue initialization

Weekly profile initialization now derives a named completed `YYYY-Www` cutoff from the configured Weekly calendar. A clean W33 v2 profile can therefore be initialized after the W34 cutoff without relying on legacy W33 state. A genuinely future/not-yet-completed issue still fails closed.

### AUD-010 — Profile-defined initial obligations

Production Profile now carries first-class `initial_obligations`. Thematic profiles require non-empty scope dimensions and initial obligations, and Completeness must preserve every Profile initial obligation in addition to obligations discovered during research expansion.

### AUD-012 — repository path confinement

Profile-owned repository paths are validated as repository-relative and traversal-safe before use.

## 3. Remaining Pilot blockers

The following findings deliberately remain open because they belong to later work units. They are mandatory before the corresponding Pilot authorization:

- **AUD-001 / WU-010 / P0 before Pilot** — immutable Architecture Approval Record binding exact reviewed Architecture and Review Summary bytes.
- **AUD-003 / WU-011 (with WU-006 hardening) / P0 before SP001** — same-run Discovery graph resolution, structured discovery method/trigger provenance, accepted Raw byte identity.
- **AUD-004 / WU-011 / P0 before Pilot** — common fail-closed JSON Schema conformance layer before semantic validation.
- **AUD-005 / WU-011 integration (earlier if convenient) / P1 before Pilot** — bounded item-level non-selected/excluded/hold review surface with explicit overflow.
- **AUD-011 / WU-010 / P0 before autonomous Pilot** — State-pinned executable implementation identity must survive artifact-only commits.

These findings may not disappear from the work log merely because WU-009 begins.

## 4. Validation at closure

All five required cross-regression workflows passed on remediation head `f064dd0627864ae796b89ed8cc16ef83ad91b589`:

| Workflow | Run | Result |
|---|---:|---|
| Survey Production Core v2 CI | `32546959222` | `SUCCESS` |
| Screening contract CI | `32546959234` | `SUCCESS` |
| Pipeline contract tests | `32546959226` | `SUCCESS` |
| Evidence contract CI | `32546959218` | `SUCCESS` |
| Weekly pipeline spine | `32546959213` | `SUCCESS` |

Weekly pipeline spine included successful committed Raw-integrity validation.

At closure:
- production `main` remained `2086b396d2f30103d9292b722891be436cd28db5`;
- Draft PR `#310` remained open, draft, and mergeable;
- no external Pilot had started.

## 5. WU-009 entry constraints

WU-009 may begin, subject to the whole-system audit negative-design checklist:

1. no universal Weekly-only `late_breaking` Draft field;
2. no universal `this_week` synthesis payload;
3. Drafting must be structurally ready to bind review-authorized Architecture bytes rather than treating an arbitrary/self-mutated Architecture file as approval authority;
4. factual Evidence refs, subject/identifier boundaries, Architecture must-cover constraints, and materiality provenance must survive into Draft Package / Draft Result validation;
5. Profile semantics remain Profile-owned;
6. Publication semantics remain Publication Profile-owned.

WU-010 must supply the actual Human Gate approval record/executor and pinned implementation identity. WU-011 must close remaining Pilot-quality/provenance blockers.

## 6. Closure principle

> WU-008A closes the defects required to continue implementation; it does not waive the remaining Pilot blockers discovered by the whole-system audit.
