# Survey Production Core v2 — Work Log

Status: `ACTIVE / canonical improvement-work checkpoint`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`  
Plan: `docs/survey-production-core-v2-improvement-plan.md`  
Semantic authority: `docs/survey-production-core-v2-authority.md`

## 1. Ledger contract

This file is the persistent **work-status** authority for Survey Production Core v2. It owns current work-unit status, validation notes, commits, unresolved execution issues, and the exact next action. Semantic/design policy is owned by the authority index and its referenced contracts/audits.

Repository reality is the highest factual authority. Current `main` remains the production source of truth until a coherent v2 candidate is reviewed and explicitly merged. Frozen historical releases are never rewritten by this improvement work.

Detailed earlier work-unit history remains recoverable from Git history; this ledger is periodically compacted so the current status and resume point remain obvious.

## 2. Current snapshot

Last updated: **2026-08-22 JST — WU-008/WU-008A closed; WU-009 started**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Production `main`: `2086b396d2f30103d9292b722891be436cd28db5` — rechecked immediately before WU-009 entry and unchanged.
- WU-008A audited remediation head: `f064dd0627864ae796b89ed8cc16ef83ad91b589`.
- Draft PR: `#310 Survey Production Core v2 implementation`; remains draft until WU-005–WU-011 form one coherent production-capable candidate.
- Current phase: **Phase 3 — Core v2 Candidate Implementation**.
- Active work unit: **WU-009 — generic Drafting + Profile Synthesis**.
- External W33/SP001 production: **NOT STARTED / NOT AUTHORIZED** until WU-011/full-candidate review and merge to `main`.

## 3. Durable rollout rules

- W33 = **Weekly Profile First Production Validation**.
- Legacy `weekly/2026-W33-work` = optional benchmark/provenance fixture only; migration/reuse is never a Pilot acceptance criterion.
- W33 remains clean-initializable even after the W34 cutoff.
- SP001 = **Thematic Profile First Production Validation** with first-class initial obligations and genuine research expansion/closure.
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
| WU-005 | `COMPLETE / AUDIT HARDENED` | Profile/State/contract+implementation identity; named completed Weekly init; path confinement |
| WU-006 | `COMPLETE / POST-AUDIT HARDENED` | Discovery/Screening v2 + self-contained accepted archive |
| WU-007 | `COMPLETE / POST-AUDIT HARDENED` | factual Evidence + Edition View + Materiality + Completeness |
| **WU-008** | **`COMPLETE / AUDITED`** | Matrix + internal Selection + generic Architecture + Review Summary |
| **WU-008A** | **`COMPLETE`** | whole-system audit remediation + 5/5 cross-regression green |
| **WU-009** | **`IN_PROGRESS`** | generic Draft Package/Result + Profile Synthesis |
| WU-010 | `PLANNED` | executable orchestration + Human Gate authority + Finding/Repair Set |
| WU-011 | `PLANNED` | P0 quality/provenance integration + full Pilot bootstrap |

## 5. WU-008 / WU-008A closure record

Whole-system audit:
`docs/survey-production-core-v2-whole-system-audit-2026-08-22.md`

Remediation closure:
`docs/survey-production-core-v2-whole-system-audit-remediation-closure.md`

### Repaired findings

- **AUD-002** — Thematic closure counters are derived from Discovery provenance; obligation rows fail closed.
- **AUD-009** — any named completed Weekly issue can be initialized deterministically after newer cutoffs; future issues fail closed.
- **AUD-010** — Production Profile has first-class `initial_obligations`; Completeness must preserve them as well as dynamically discovered obligations.
- **AUD-012** — Profile-owned repository paths are repository-confined.

### Remaining Pilot blockers

These must remain visible until their owner work units close them:

- **AUD-001 / WU-010 / P0 before Pilot** — immutable Architecture Approval Record binding exact reviewed Architecture + Review Summary bytes.
- **AUD-003 / WU-011 with WU-006 hardening / P0 before SP001** — Discovery graph resolution, structured discovery-method/trigger provenance, accepted Raw byte identity.
- **AUD-004 / WU-011 / P0 before Pilot** — common fail-closed JSON Schema conformance layer.
- **AUD-005 / before Pilot** — bounded item-level exclusion/hold/non-material/duplicate Human Review surface with explicit overflow.
- **AUD-011 / WU-010 / P0 before autonomous Pilot** — State-pinned executable implementation identity across artifact-only commits.

### Cross-regression validation on `f064dd0627864ae796b89ed8cc16ef83ad91b589`

- Survey Production Core v2 CI `32546959222`: **SUCCESS**
- Screening contract CI `32546959234`: **SUCCESS**
- Pipeline contract tests `32546959226`: **SUCCESS**
- Evidence contract CI `32546959218`: **SUCCESS**
- Weekly pipeline spine `32546959213`: **SUCCESS**, including Raw integrity

**WU-008 and WU-008A exit criteria are satisfied.**

## 6. WU-009 active contract

Authoritative guidance:
- `docs/survey-production-core-v2-minimum-vertical-slice-audit-amendment.md` §§11–12;
- `docs/survey-production-core-v2-minimum-vertical-slice-second-audit-amendment.md`;
- `docs/survey-production-core-v2-whole-system-audit-2026-08-22.md`;
- `docs/survey-production-core-v2-whole-system-audit-remediation-closure.md`.

### Generic Draft Package

Implement a profile-neutral package carrying:
- exact upstream Architecture authorization/basis identity;
- exact factual Evidence / Matrix references required by the Architecture package;
- package title/type/ordering from Architecture;
- primary/supporting Evidence assignments;
- must-cover requirements and boundaries;
- language/citation granularity;
- raw sources forbidden;
- unknowns remain unknown;
- Profile/Publication extensions only in owned extension namespaces.

Do **not** add universal `late_breaking` or `this_week_summary_forbidden` fields.

### Draft Result

Implement structured result semantics carrying:
- headline/deck/ordered blocks;
- stable Evidence refs and attribution modes;
- must-cover/boundary disposition;
- exact Draft Package + prompt/runner identity;
- explicit limitation preservation;
- Profile/Publication-owned extensions.

Do **not** add generic `late_breaking_acknowledged`.

### Profile Synthesis

Implement a generic Synthesis Envelope with:
- issue/research/publication identity;
- exact input/prompt/runner provenance;
- `profile_payload`;
- optional Publication-owned cover/frontmatter payload where requested.

Weekly may supply current/This Week/carry-over synthesis through a Weekly payload; Thematic may supply branch/transition/parallel/competing/historical-attribution synthesis. Neither forces dummy fields into the other.

### WU-009 audit constraints

- no universal Weekly-only fields;
- no arbitrary/self-mutated Architecture file may be treated as Human approval authority;
- design the Draft basis so WU-010 can bind an independent exact-byte Architecture Approval Record without changing Draft semantics;
- Evidence refs, subject/identifier attribution, Architecture must-cover requirements and limitations survive into Draft validation;
- Profile semantics stay Profile-owned;
- Publication semantics stay Publication Profile-owned.

### WU-009 exit criteria

1. Weekly and Thematic fixtures use one Core Draft/Synthesis envelope without dummy cross-profile fields.
2. Draft Package is exact-basis-bound and derived from Architecture package assignments/constraints.
3. Draft Result cannot cite Evidence outside its Draft Package and cannot silently drop must-cover/boundary obligations.
4. factual attribution/subject boundaries remain machine-checkable through drafting.
5. Synthesis envelope is profile-neutral and exact-input-bound.
6. Profile payload validation is Profile-owned rather than one global Weekly schema.
7. WU-009 contracts participate in `pipeline_contract_sha256` and drift invalidates initialized State.
8. dedicated + cross-regression CI are green before WU-009 closes.

## 7. Resume rule

```text
read current main
-> read this worklog for status/next action
-> read docs/survey-production-core-v2-authority.md
-> read active WU authorities/audit constraints
-> verify repository reality
-> continue WU-009
-> validate dedicated + cross-regression CI
-> audit WU-009
-> update this ledger before declaring completion
```

**Current action: implement and validate WU-009 Drafting + Profile Synthesis while preserving the remaining WU-010/WU-011 Pilot blockers.**
