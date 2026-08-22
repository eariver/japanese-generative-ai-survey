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

Last updated: **2026-08-22 JST — WU-009 closed after dedicated/cross-regression audit; WU-010 started**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Production `main`: `2086b396d2f30103d9292b722891be436cd28db5` — rechecked immediately before WU-010 entry and unchanged.
- WU-009 audited head: `9d58c01b50b220ea9cdfc11f6258e9b44ea676ee`.
- Draft PR: `#310 Survey Production Core v2 implementation`; remains draft until WU-005–WU-011 form one coherent production-capable candidate.
- Current phase: **Phase 3 — Core v2 Candidate Implementation**.
- Active work unit: **WU-010 — executable orchestration + Human Gate authority + Finding/Repair Set**.
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
| WU-008 | `COMPLETE / AUDITED` | Matrix + internal Selection + generic Architecture + Review Summary |
| WU-008A | `COMPLETE` | whole-system audit remediation + 5/5 cross-regression green |
| **WU-009** | **`COMPLETE / AUDITED`** | generic Draft Package/Result + Profile Synthesis + self-contained provenance + Profile extension preservation |
| **WU-010** | **`IN_PROGRESS`** | executable orchestration + Human Gate authority + Finding/Repair Set |
| WU-011 | `PLANNED` | P0 quality/provenance integration + full Pilot bootstrap |

## 5. WU-008 / WU-008A closure record

Whole-system audit:
`docs/survey-production-core-v2-whole-system-audit-2026-08-22.md`

Remediation closure:
`docs/survey-production-core-v2-whole-system-audit-remediation-closure.md`

Repaired findings:
- **AUD-002** — Thematic closure counters derive from Discovery provenance; obligation rows fail closed.
- **AUD-009** — named completed Weekly issues initialize deterministically after newer cutoffs; future issues fail closed.
- **AUD-010** — Production Profile carries first-class initial obligations; Completeness preserves them and dynamically discovered obligations.
- **AUD-012** — Profile-owned repository paths are repository-confined.

Cross-regression validation on `f064dd0627864ae796b89ed8cc16ef83ad91b589`:
- Core v2 `32546959222`: **SUCCESS**
- Screening `32546959234`: **SUCCESS**
- Pipeline contract `32546959226`: **SUCCESS**
- Evidence `32546959218`: **SUCCESS**
- Weekly spine `32546959213`: **SUCCESS**, including Raw integrity

## 6. WU-009 completion + audit record

Implemented:
- `schemas/architecture-approval-record-v2.schema.json` as the exact-byte authorization contract consumed downstream; WU-010 owns issuing/applying it;
- `schemas/draft-v2-package.schema.json`;
- `schemas/draft-v2-result.schema.json`;
- `schemas/profile-synthesis-v2-input.schema.json`;
- `schemas/profile-synthesis-v2-result.schema.json`;
- `config/prompts/article-drafting-v2.md`;
- `config/prompts/profile-synthesis-v2.md`;
- `scripts/survey_drafting_v2.py`;
- `scripts/survey_draft_profile_v2.py`;
- `tests/test_survey_drafting_v2.py`;
- `tests/test_survey_drafting_integrity_v2.py`;
- `tests/test_survey_draft_profile_v2.py`;
- WU-009 contracts/prompts added to `pipeline_contract_sha256` identity;
- dedicated v2 CI extended through generic Drafting/Profile Synthesis and Profile/Publication extension preservation.

Key guarantees:
- generic Draft/Synthesis contracts do not require Weekly-only `late_breaking`, `this_week`, `watchlist`, or acknowledgement fields;
- Weekly and Thematic fixtures use one Core Draft/Synthesis envelope without dummy fields from the other Profile;
- Drafting requires immutable `PROPOSED` Architecture bytes plus a separate Architecture Approval Record binding the exact Architecture SHA and Architecture Review Summary SHA;
- Draft Package is deterministically derived from validated Architecture assignments and exact accepted Evidence;
- Draft Package embeds the authorized Candidate Matrix and Evidence acceptance so its provenance can be revalidated after mutable upstream work directories are unavailable;
- Synthesis revalidates Architecture → Candidate Matrix → Evidence acceptance → Evidence Card identity and rejects forged embedded Evidence even if a Draft Result is rebound to the forged package SHA;
- Draft Evidence references preserve stable `EVENT | CLAIM | METRIC | LIMITATION` identity plus `subject_id`/`subject_role` and reject subject rebinding;
- Draft Result must cover every Architecture `must_cover_requirement` exactly once and dispose every boundary exactly once;
- inference/social/claimed Evidence classes require compatible attribution modes;
- Profile Synthesis is exact-input/prompt/runner bound and Profile payload keys are taken from Profile contracts rather than a global Weekly schema;
- generic Core does not interpret Profile extension vocabulary; the adjacent Profile/Publication Draft validator requires authorized extension directives to survive Draft Result generation exactly.

### WU-009 audit findings repaired before closure

1. **Self-contained Draft provenance** — the first implementation could validate a Draft Result against a Package without independently reconstructing all embedded upstream identity. The Package now carries Matrix/Evidence acceptance and Synthesis revalidates the complete SHA chain.
2. **Forged embedded Evidence** — regression `test_synthesis_rejects_forged_embedded_evidence_even_if_result_rebinds_to_package` proves that mutating an embedded Evidence Card and rebinding the Result to the forged Package still fails.
3. **Profile/Publication extension silent drop** — a separate Profile/Publication validator now rejects dropped or invented extension directives without teaching generic Core Weekly/Thematic vocabulary.
4. **unittest duplicate discovery noise** — helper import shape was corrected so dedicated test accounting is not inflated by imported TestCase classes.

### WU-009 final validation on `9d58c01b50b220ea9cdfc11f6258e9b44ea676ee`

- Survey Production Core v2 CI `32548951871`: **SUCCESS** — compile, 50 dedicated v2 tests, JSON contract parsing.
- Evidence contract CI `32548951895`: **SUCCESS**.
- Screening contract CI `32548951878`: **SUCCESS**.
- Pipeline contract tests `32548951957`: **SUCCESS**.
- Weekly pipeline spine `32548951870`: **SUCCESS** — main test job and committed Raw integrity job both green.

**WU-009 exit criteria are satisfied.**

## 7. Remaining whole-system Pilot blockers

These remain visible until their owner work units close them:

- **AUD-001 / WU-010 / P0 before Pilot** — Human Architecture approval must be an independent immutable record binding exact reviewed Architecture + Review Summary bytes; WU-009 defines the consumed record contract, WU-010 must own issuance/state authority.
- **AUD-003 / WU-011 with WU-006 hardening / P0 before SP001** — Discovery graph resolution, structured discovery-method/trigger provenance, accepted Raw byte identity.
- **AUD-004 / WU-011 / P0 before Pilot** — common fail-closed JSON Schema conformance layer.
- **AUD-005 / before Pilot** — bounded item-level exclusion/hold/non-material/duplicate Human Review surface with explicit overflow.
- **AUD-011 / WU-010 / P0 before autonomous Pilot** — State-pinned executable implementation identity across artifact-only commits.

## 8. WU-010 active contract

Authoritative guidance:
- `docs/survey-production-core-v2-minimum-vertical-slice-audit-amendment.md` §§14–16;
- `docs/survey-production-core-v2-minimum-vertical-slice-second-audit-amendment.md` §§5, 8, 10;
- `docs/survey-production-core-v2-whole-system-audit-2026-08-22.md`, especially AUD-001/AUD-006/AUD-011.

Implement:

### Planner / Action Spec / executor
- deterministic Action Spec from authoritative Production State/Profile/artifact validity/target gate;
- action kinds `LOCAL_SCRIPT | WORKFLOW_DISPATCH | HUMAN_GATE | COMPLETE | EXCEPTION`;
- registered deterministic dispatcher rather than chat-reconstructed stage order;
- exact required-input / expected-output / state / contract / implementation basis;
- immutable Action Result provenance;
- authoritative state/checkpoint advancement only after outputs validate;
- replanning until `HUMAN_GATE_REACHED`, `EXCEPTION_GATE_REQUIRED`, or `COMPLETE`;
- recoverable technical failures remain retry/recovery conditions, not Human Gates.

### Human Gate authority — AUD-001
- Architecture Review approval is issued as a separate immutable Approval Record;
- record binds exact reviewed Architecture SHA and Review Summary SHA;
- Architecture bytes remain unchanged after review;
- Production State gate status advances only from a valid exact-byte record;
- no self-mutated `APPROVED` Architecture is sole authority.

### Implementation identity — AUD-011
- planner/executor reads the implementation SHA pinned in Production State;
- every Action Spec/Result/handler invocation carries that pinned SHA;
- artifact-only commits may change repository `HEAD` but may not silently change implementation authority;
- handlers must not default back to current `HEAD` once State exists.

### Finding / Repair Set
- normalized Finding schema uses orthogonal `scope`, `defect_kind`, `confidence`, and `requires_regression`;
- Repair Set groups Findings, actual changed layer, implementation commits, regression fixtures, compatibility impact, validation, and required Pilot verification;
- production workaround remains evidence, not automatic authorization for a Core fix.

### WU-010 exit criteria
1. planner derives deterministic next action from repository State without chat memory;
2. registered executor can execute deterministic handlers and validate/apply results;
3. State-pinned implementation SHA survives artifact-only HEAD movement;
4. exact-byte Architecture Approval Record is the Human Gate authority and Architecture bytes remain immutable;
5. target-gate/terminal behavior is deterministic and only stops at Human/Exception/Complete terminals;
6. machine-readable Finding/Repair Set contracts and validators are usable by Pilot sessions;
7. WU-010 contracts participate in pipeline identity;
8. dedicated + cross-regression CI are green before closure.

## 9. Resume rule

```text
read current main
-> read this worklog for status/next action
-> read docs/survey-production-core-v2-authority.md
-> read WU-010 authority/audit constraints
-> verify repository reality
-> implement planner/action/result/approval/finding/repair mechanics
-> validate dedicated + cross-regression CI
-> audit WU-010 including AUD-001/AUD-011
-> update this ledger before declaring completion
```

**Current action: implement WU-010 executable orchestration, exact-byte Human Gate authority, State-pinned implementation propagation, and reusable Finding/Repair Set contracts.**
