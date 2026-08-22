# Survey Production Core v2 — WU-008 / Whole-System Audit

Status: `AUDIT COMPLETE / remediation gate active`  
Audit date: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft PR: `#310`  
Pre-audit WU-008 head: `a2f723eea4d22ff14d43b7da7866dc5aed764ca4`  
Production `main` at audit start: `2086b396d2f30103d9292b722891be436cd28db5`

## 1. Purpose

This audit has two layers:

1. **WU-008 completion audit** — verify Candidate Matrix, internal Selection, generic Architecture, and Architecture Review Summary against the authoritative Phase 3 contracts.
2. **Whole-system audit** — re-read the implemented v2 path from WU-005 through WU-008 as one system rather than assuming green unit/workflow tests imply cross-contract correctness.

The audit distinguishes:
- defects in already-implemented behavior;
- Pilot-blocking capabilities intentionally owned by later work units;
- future/non-Pilot capabilities that are not yet required.

A later work unit does not excuse a defect in an earlier work unit's declared contract. Conversely, an unimplemented WU-009/WU-010/WU-011 responsibility is not retroactively a WU-008 defect merely because the full Pilot is not yet production-capable.

## 2. Baseline verification

Before audit remediation, head `a2f723eea4d22ff14d43b7da7866dc5aed764ca4` passed all five cross-regression workflows:

- Survey Production Core v2 CI — SUCCESS;
- Evidence contract CI — SUCCESS;
- Screening contract CI — SUCCESS;
- repository-wide Pipeline contract tests — SUCCESS;
- Weekly pipeline spine — SUCCESS.

Draft PR #310 was mergeable and remained intentionally draft. Production `main` was unchanged.

Green CI is necessary evidence, not sufficient audit proof.

## 3. WU-008 completion assessment

### 3.1 Satisfied

WU-008 establishes:

- Candidate Matrix derived from exact accepted Evidence, Edition Evidence View, Materiality Ledger and Profile Completeness;
- deterministic Candidate identity and no silent loss of accepted Evidence tasks before Matrix;
- one explicit Selection assignment per Matrix candidate;
- Selection dispositions `SELECTED | HOLD | REJECT | INSPECT` without Human approval fields;
- Profile/Publication-owned role namespaces rather than one global Weekly role enum;
- generic Architecture packages with primary/supporting assignment, must-cover requirements, boundaries and drafting order;
- selected PRIMARY destination exactly once, selected SUPPORTING at least once, or explicit structured selected exception;
- no generic `LATE_BREAKING`, `X_COMMUNITY`, `WATCHLIST_CHRONOLOGY`, or `this_week_summary_written_last` requirement;
- Weekly and Thematic fixtures through the same Core contract without dummy fields from the other Profile;
- Architecture Review Summary with exact basis hashes, discovery/screening/evidence/materiality/selection/completeness counts, material destinations, residual limitations, page plan, and research-expansion summary;
- WU-008 schema files included in `pipeline_contract_sha256` identity;
- regression proving Architecture schema drift invalidates initialized Production State.

### 3.2 WU-008 conclusion

WU-008's **pre-Human-Gate production of a reviewable Architecture proposal** satisfies its declared exit criteria and is considered complete.

Human Gate execution and approval-state authority remain WU-010 responsibilities. AUD-001 below is therefore a Pilot blocker but not a failure of WU-008 proposal generation.

## 4. Whole-system findings

### AUD-001 — P0 before Pilot / TRACEABILITY — Architecture approval must bind immutable reviewed bytes

**Observed**

`survey_architecture_v2.py` can represent `status=APPROVED` by changing the same Architecture object to add Human Review metadata.

**Problem**

A Human reviews a proposed Architecture/Review Summary with known hashes. Rewriting the Architecture from `PROPOSED` to `APPROVED` changes the Architecture hash, so the downstream approved bytes are not literally the bytes that were reviewed.

**Required repair**

- Scope: `CORE`
- Owner: **WU-010 Human Gate/orchestration**
- Severity: `P0 before Pilot`
- Use an independent Architecture Approval Record, or equivalent immutable proposal binding, that records the exact proposed Architecture SHA and exact Architecture Review Summary SHA.
- Gate state may advance only from that exact record.
- Do not treat a self-mutated Architecture file as sole approval authority.

### AUD-002 — P0 / COVERAGE — Thematic closure counters were self-reported

**Observed**

The base WU-007 Completeness validator checked closure counters for type/internal arithmetic but did not prove that `expansion_passes`, `final_pass_new_sources`, or final-pass material-obligation counts matched Discovery provenance.

**Status: REPAIRED during this audit.**

Repair:
- `survey_completeness_v2.py` derives expansion/final-pass counters from Discovery `research_pass` and `obligation_ids`;
- closure self-report must equal those derived values;
- Completeness obligation rows now fail closed on extra/missing fields, invalid Profile dimensions, duplicate refs, unknown Discovery/Evidence refs, and missing required text;
- dedicated negative regressions were added;
- the earlier named-obligation fixture was updated to exercise the stricter guard rather than bypass it.

### AUD-003 — P1 now / P0 before SP001 / TRACEABILITY — Discovery graph and Raw identity need stronger resolution

**Observed**

Expansion origins require non-empty `parent_refs`, but the current Discovery-set validator does not yet prove that every same-run expansion parent resolves to a valid node with a coherent earlier research pass. The Discovery contract also lacks a first-class structured discovery-method/query/reference field separate from prose `reason`, and `raw_paths` are not yet a complete accepted-Raw byte identity.

**Required before SP001**

- define same-run vs external parent-reference namespaces and reject dangling expansion edges;
- require coherent research-pass ordering for same-run expansion edges;
- retain structured discovery method/trigger data;
- bind accepted Raw byte identity structurally rather than relying only on path strings/opaque metadata;
- add dangling-edge and Raw-identity drift regressions.

Owner: WU-006 hardening + WU-011 bootstrap integration.

### AUD-004 — P1 now / P0 before Pilot / CORRECTNESS — JSON Schemas and runtime validators are not uniformly equivalent

**Observed**

Committed schemas use strict required fields, `additionalProperties: false`, types and enums, while runtime validators are hand-written and not universally equivalent. Concrete examples include Production Profile and nested Evidence fields; Completeness had the same problem before AUD-002 was repaired.

**Risk**

A schema-invalid but semantically plausible artifact could pass a narrower runtime validator, weakening the meaning of schema bytes in `pipeline_contract_sha256`.

**Required before Pilot**

Establish one fail-closed schema-conformance layer before semantic validation for model-produced/externally supplied artifacts. Add a regression showing a schema-invalid payload cannot be accepted merely because the semantic subset happens to pass.

Owner: WU-011 quality integration, with earlier repairs whenever a concrete bypass is found.

### AUD-005 — P1 before Pilot / TRACEABILITY — Review Summary needs bounded item-level exclusion/hold rationale

**Observed**

Architecture Review Summary exposes aggregate Screening/Materiality counts and detailed destinations for `MATERIAL`/`CONTEXT` Matrix candidates. Discovery rows dropped before Matrix remain authoritative in Materiality Ledger, but their item-level exclusion/duplicate/hold rationale is not surfaced concisely at Human Gate 1.

**Required before Pilot**

Add a bounded review-attention surface for `DROP`, `MAYBE`, `INSPECT`, `HOLD`, `NON_MATERIAL`, `EXCLUDED`, and `DUPLICATE`, preserving stable IDs and rationale while keeping the full Ledger authoritative. The surface must expose truncation/overflow explicitly rather than silently sampling.

Owner: WU-008 post-audit review-surface hardening / WU-011 Pilot integration.

### AUD-006 — PLANNED — Production State action/checkpoint advancement is still skeletal

`transition_state` currently establishes monotonic lifecycle mechanics and basis anti-divergence. It does not yet own the final action planner/executor, checkpoint evidence application, terminal-reason computation, or Human Gate transitions.

This is explicitly WU-010 scope and is not a current-unit defect.

### AUD-007 — PLANNED — Retrospective Period constructor is outside the first W33/SP001 slice

The config/schema declare `RETROSPECTIVE_PERIOD`, while the first executable validation slice focuses on Weekly and Thematic. Period support remains an eventual Profile requirement but is not a W33/SP001-first WU-005–008 exit condition.

### AUD-008 — PASS — W33 legacy RC remains optional and non-authoritative

No W33-specific migration compatibility was introduced into WU-008. Fresh v2 Matrix/Selection/Architecture remains canonical; the legacy W33 RC is only an optional comparison/provenance fixture.

### AUD-009 — P0 before W33 / CORRECTNESS — named completed Weekly issues must remain initializable after a newer cutoff

**Observed**

`weekly_profile()` currently resolves the latest completed cutoff and rejects a requested `issue_id` whenever it is not that latest issue.

At 2026-08-22 07:00 JST the next Weekly cutoff completed, so W34 becomes the latest issue. The planned first Pilot is still W33. Under the current initializer, a clean W33 v2 run started after that time is rejected even though W33 is a valid completed issue.

Relying on a legacy W33 `pipeline-state.json` would contradict the rule that W33 legacy reuse is optional.

**Required repair**

- Scope: `WEEKLY_PROFILE` + Core profile initialization
- Severity: `P0 before W33 Pilot`
- deterministically derive a named issue's cutoff from `YYYY-Www` plus Weekly cutoff weekday/hour/timezone;
- allow any named **completed** Weekly issue to initialize without legacy state;
- reject future/not-yet-completed issues;
- preserve the same cutoff-to-cutoff editorial-window semantics;
- add regression: W33 initializes successfully after the W34 cutoff, while a genuinely future issue fails closed.

### AUD-010 — P0 before SP001 / COVERAGE — Profile-defined initial research obligations are not first-class

**Observed**

The authoritative design says Completeness is evaluated against both Profile-defined initial obligations and obligations discovered during expansion. Current Production Profile stores `scope_dimensions` but no first-class initial-obligation list. Completeness requires coverage of dimensions, so a caller can manufacture one generic satisfied row per dimension without proving that the actual initial research questions were retained.

Thematic `scope_dimensions` can also currently be empty.

**Required repair**

- Scope: `THEMATIC_PROFILE` + `CORE`
- Severity: `P0 before SP001 Pilot`
- Production Profile must carry stable initial obligation IDs, dimensions and descriptions;
- Thematic Profile must have at least one scope dimension and at least one initial obligation;
- Profile validator must reject duplicate/unknown obligation dimensions;
- Completeness must contain every Profile initial obligation, preserve its identity/dimension, and also include every dynamically discovered obligation;
- SP001 bootstrap must define topic-specific obligations as data, not code.

### AUD-011 — P1 now / P0 before autonomous Pilot / ORCHESTRATION — implementation identity must be pinned across artifact-only commits

**Observed**

Production State correctly distinguishes semantic contract identity from executable repository commit identity. The CLI defaults, however, resolve implementation identity from current `HEAD`. Production work commonly commits generated artifacts between stages; such artifact-only commits change `HEAD` even when executable code is unchanged.

**Risk**

An autonomous run can falsely report implementation drift after committing its own artifacts unless every action consistently uses the originally pinned implementation/control SHA.

**Required repair**

WU-010 planner/executor must carry the State-pinned implementation SHA through every Action Spec/result/validator invocation, or replace whole-HEAD identity with a deterministic control-code identity that cannot be altered by generated artifact commits. A stage must never silently recompute implementation authority from an artifact-only branch head.

### AUD-012 — P1 before Pilot / CORRECTNESS — Profile-owned repository paths need confinement validation

**Observed**

Thematic profile specs can currently supply `source_root`, `survey_root`, and `work_branch` strings. The semantic intent is repository-local production state/artifacts, but the Profile validator does not yet explicitly reject absolute/traversal filesystem paths.

**Required repair**

- repository paths must be normalized repository-relative paths with no `..` escape;
- issue-derived defaults remain deterministic;
- initialization and later handlers must verify confinement before write;
- add path-traversal regressions.

Owner: WU-005 hardening / WU-011 bootstrap safety.

## 5. Cross-cutting observations

### 5.1 Strong current mechanics

The strongest properties now are:
- exact basis hashes at semantic boundaries;
- complete-only accepted result sets;
- content-addressed Screening/Evidence/View archives;
- explicit Discovery→Screening→Evidence→View→Materiality traceability;
- subject/entity role binding for comparator safety;
- internal Selection separated from Human Gate approval;
- Profile-neutral Matrix/Architecture envelope;
- deterministic regressions for historical #166/#191 defect families;
- Thematic final-pass closure counters derived from recorded research provenance after AUD-002 repair.

### 5.2 WU-009 negative-design checklist

When WU-009 begins it must not reintroduce Weekly semantics through Draft Package, Draft Result, or Profile Synthesis:
- no universal `late_breaking` field;
- no universal `this_week` synthesis payload;
- Draft must ultimately bind review-authorized Architecture basis, not merely an arbitrary Architecture file;
- Evidence/Matrix boundaries must survive into drafting;
- Profile extensions remain Profile-owned.

## 6. Remediation gate before WU-009

The whole-system audit is complete, but WU-009 does **not** begin immediately because the audit found P0 defects in already-implemented foundation/completeness behavior.

Create a short audit-remediation unit and close at least:

1. AUD-009 — named completed Weekly initialization;
2. AUD-010 — first-class Profile initial obligations;
3. revalidate AUD-002 closure hardening on all cross-regression workflows;
4. record AUD-001/AUD-003/AUD-004/AUD-005/AUD-011/AUD-012 as explicit Pilot blockers owned by WU-010/WU-011 or earlier hardening;
5. recheck production `main` and PR mergeability.

After those conditions are green, WU-009 may begin. WU-010/WU-011 must still close their assigned Pilot blockers before external W33/SP001 production is authorized.

## 7. Audit principle

> Green tests prove the tested contract. They do not prove that the contract itself contains every required invariant.

Whole-system audits are therefore mandatory at coherent vertical-slice boundaries and again before Pilot authorization.
