# Survey Production Core v2 — Design Authority Index

Status: `CANONICAL IMPROVEMENT-BRANCH AUTHORITY / WU-011 IMPLEMENTATION COMPLETE / WU-012 ACTIVE`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`

## 1. Purpose

The improvement branch intentionally preserves earlier design documents for auditability. Subsequent audits corrected parts of those documents, and implementation audits added cross-cutting constraints that must survive Pilot integration.

This index makes the live-tree authority unambiguous without deleting the historical reasoning that led to each correction. A continuation session working on Survey Production Core v2 must read this index before treating any other improvement document as current implementation guidance.

Current `main` remains the production source of truth until the coherent v2 candidate is Human-reviewed and explicitly merged. This index is authoritative only for work on the improvement branch until that merge.

The user-requested pre-approval WU-001–WU-011 audit on 2026-08-22 found additional readiness gaps after WU-011's valid implementation closure. Those gaps are now WU-012 and **supersede the earlier instruction to proceed directly from WU-011 to merge approval**.

## 2. Authority responsibilities

Authority is split by responsibility. Do **not** interpret the work log as a higher semantic-policy authority than the contract documents.

### 2.1 Repository reality

Actual repository files, committed artifacts, hashes, tests, workflow state, and branch state are the highest factual authority. If documentation disagrees with repository reality, correct the documentation before relying on the stale statement.

### 2.2 Work-status authority

`docs/checkpoints/survey-production-core-v2-worklog.md` is authoritative only for:

- current phase / work-unit status;
- start/stop state;
- completed commits and validation notes;
- unresolved work;
- exact next action.

It is a checkpoint ledger, not the normative semantic contract.

### 2.3 Semantic/design authority

For architecture, contracts, Pilot semantics, Profile/Core ownership, Human Gates, provenance requirements, and acceptance criteria, use this precedence:

```text
1. repository reality
2. this authority index
3. docs/survey-production-core-v2-improvement-plan.md §§16–18 (pre-approval audit/WU-012 amendment)
4. whole-system audit + explicit remediation status recorded here
5. second-audit amendments / WU-011 second-audit closure
6. first-audit amendments
7. base Phase 0/1/2/3 design documents
8. historical/current-main implementation docs used as source evidence
```

A remediation status can change a finding from open to repaired only when implementation and regression evidence exist. It does not erase unrepaired requirements from the originating audit. `FIXED_GENERIC` is not Pilot-proven `CLOSED`.

## 3. Document status map

| Document | Current authority status | Notes |
|---|---|---|
| `docs/survey-production-core-v2-improvement-plan.md` | `ACTIVE PLAN / AUTHORITATIVE WU-012 AMENDMENT IN §§16–18` | overall goal/phases remain valid; §§16–18 supersede the prior Phase-4 entry instruction until WU-012 is repaired/re-audited |
| `docs/survey-production-core-v2-component-inventory.md` | `SUPERSEDED IN PART` | process archaeology remains useful; semantic-neutrality conclusions corrected by audit amendment |
| `docs/survey-production-core-v2-component-inventory-audit-amendment.md` | `AUTHORITATIVE FOR PHASE 0 CORRECTION` | controls profile-pollution classification through Synthesis |
| `docs/survey-production-core-v2-contract-normalization.md` | `ACTIVE BASE CONTRACT / SUPERSEDED IN PART` | two-gate/temporal/release model remains; later amendments control identity/taxonomy/applicability |
| `docs/survey-production-core-v2-contract-normalization-second-audit-amendment.md` | `AUTHORITATIVE PHASE 1 AMENDMENT` | implementation identity, Finding taxonomy, Pilot entry, optional W33 reuse, Thematic closure |
| `docs/survey-production-core-v2-historical-invariants.md` | `ACTIVE INVARIANT CATALOG` | failure-driven durable invariants; WU-012H must map material recurring issues to current guards |
| `docs/survey-production-core-v2-historical-production-pattern-matrix.md` | `SUPERSEDED AS PHASE 2 EXIT EVIDENCE` | useful first-pass pattern summary; insufficient edition-depth by itself |
| `docs/survey-production-core-v2-historical-production-deep-audit.md` | `AUTHORITATIVE PHASE 2 EXIT EVIDENCE` | all 15 Specials audited at final-state production-lineage depth |
| `docs/survey-production-core-v2-minimum-vertical-slice.md` | `SUPERSEDED IN PART` | base Phase 3 reasoning retained, but not sufficient as current implementation contract |
| `docs/survey-production-core-v2-minimum-vertical-slice-audit-amendment.md` | `SUPERSEDED IN PART BY SECOND AUDIT` | first correction remains valid except where later authorities conflict |
| `docs/survey-production-core-v2-minimum-vertical-slice-second-audit-amendment.md` | `AUTHORITATIVE PHASE 3 IMPLEMENTATION AMENDMENT / FIRST-SLICE ONLY` | W33/SP001 implementation boundary remains evidence, not proof of general production readiness |
| `docs/survey-production-core-v2-whole-system-audit-2026-08-22.md` | `AUTHORITATIVE CROSS-CUTTING AUDIT` | originating integrated-audit requirements; finding status is normalized here |
| `docs/survey-production-core-v2-whole-system-audit-remediation-closure.md` | `AUTHORITATIVE HISTORICAL REMEDIATION EVIDENCE` | records WU-008A remediation and WU-009 entry |
| `docs/survey-production-core-v2-wu011-second-audit-closure.md` | `AUTHORITATIVE HISTORICAL WU-011 EXIT EVIDENCE` | WU-011 was correctly closed against its then-current scope; WU-012 is a later pre-approval audit unit |
| `docs/survey-production-core-v2-session-bootstrap.md` | `CORE V2 PILOT OPERATIONS / PRODUCTION DISABLED PENDING WU-012` | W33/SP001 start/resume procedure remains useful but must not be invoked for external initialization before WU-012 review/merge |
| `docs/survey-production-core-v2-w33-artifact-disposition.md` | `ACTIVE SUPPORTING POLICY` | optional legacy benchmark/reuse policy; not a W33 acceptance contract |
| `docs/checkpoints/survey-production-core-v2-worklog.md` | `CANONICAL WORK CHECKPOINT` | status/progress/next action only; does not override semantic contracts |
| `docs/checkpoints/survey-production-core-v2-audit-findings/` | `ACTIVE MACHINE-READABLE AUDIT EVIDENCE` | WU-010R/WU-011 Repair Sets plus OPEN WU-012 findings AUD-027–034 |

## 4. Critical corrected rules

A continuation session must not recover superseded conclusions from older documents.

Current rules are:

1. `shared file format != shared semantic Core`.
2. Weekly semantics remain behind Weekly/Profile contracts rather than polluting generic Screening, Evidence, Matrix, Drafting, or Synthesis.
3. W33 is **Weekly Profile First Production Validation**, not a Core design template.
4. The legacy W33 RC is an optional benchmark/provenance fixture; reuse is never a Pilot acceptance criterion.
5. A named completed Weekly issue remains deterministically initializable after a newer cutoff; W33 must not depend on legacy state merely because W34 is now eligible.
6. SP001 must perform true Thematic Research Expansion and closure/saturation auditing.
7. Profile-defined initial research obligations are first-class identity-bearing obligations and cannot be replaced by generic dimension-only completion rows.
8. A full production-capable v2 candidate is merged to `main` before external W33/SP001 production begins. WU-012 is now part of that pre-merge candidate.
9. Production provenance binds semantic contract identity **and** executable implementation identity **and** artifact byte identity.
10. Human Gate approval binds exact reviewed bytes. Architecture remains immutable `PROPOSED`; approval is an independent record.
11. A machine checkpoint may become `passed` only when implementation-controlled semantic validation produced an exact-byte Validation Attestation and Production State pins that attestation by path + SHA-256.
12. Production State is the sole lifecycle/gate authority and must itself be semantically reconstructable: lifecycle/history/checkpoints/gates/controller fields and their provenance must agree.
13. Action execution binds State/Profile plus transitive State-pinned checkpoint/gate authorities; changing authoritative stage input bytes invalidates the plan rather than silently changing execution basis.
14. `WORKFLOW_DISPATCH` is non-retryable by default. Retry requires explicit idempotency/reconciliation authority. `stage:release` is the explicit exception, keyed by `release_identity` with exact-byte reconciliation.
15. Pilot Finding scope and regression requirement are orthogonal fields; a Finding cannot become `CLOSED` without a closed Repair Set authority.
16. Candidate Selection is internal; normal Human Gates are Architecture Review and exact-byte Publication Preview.
17. **WU-012 must not add another routine Human Gate.** Visual/editorial residual judgment belongs in the existing Publication Preview when machine validation is inappropriate.
18. Repository-owned production paths are repository-confined; absolute/traversal escape is invalid.
19. Frozen historical releases remain unchanged.
20. Discovery same-run parent edges resolve only to an earlier research pass; external parent edges use an explicit external namespace. Accepted Raw path/SHA-256/byte count are immutable downstream authority.
21. Model/external JSON artifacts pass one shared fail-closed Draft 2020-12 schema gate before implementation semantic validation.
22. Human attention surfaces are bounded and expose total/shown/overflow/truncation rather than silently dropping review load.
23. Publication authority may use `REPOSITORY_FILE` or `GITHUB_ACTIONS_ARTIFACT`; the exact PDF SHA-256 and byte count survive Quality → Candidate → Preview → Visual Review → Freeze → Merge Verification → Release Record.
24. External Release side effects are recoverable only through explicit exact-identity reconciliation. Existing public bytes are never silently replaced or accepted by name alone.
25. Production-control and Release execute the State-pinned worktree implementation. The currently dispatched main workflow must be byte-identical to the pinned worktree workflow before action execution.
26. Canonical one-stage adoption executes at most one deterministic stage. If that transition reaches Human/Exception/Complete terminal planning, the terminal Action Spec is persisted without executing another deterministic stage.
27. W33/SP001 launch inputs come from repository-owned configuration; conversation history and test literals are not launch authority.
28. SP001 `as_of` is set exactly once at initialization and preserved on resume. Resume is valid only when Profile, State semantics and State-pinned implementation identity remain consistent.
29. Core v2 integration must not roll back unrelated current-main production behavior. Legacy workflow edits are permitted only where required for bounded cross-regression wiring and must be regression-protected.
30. **Collector success and discovered-record traceability do not prove Source Intake completeness.** A mandatory coverage obligation may not become `SATISFIED`/READY without appropriate authoritative coverage support; adequate negative searches may count without fixed source quotas.
31. **Weekly Issue #9 semantics are Weekly/Profile-owned executable requirements**, including reader-facing why-this-issue, Late Breaking one-home semantics, Watchlist presentation and published-prose/internal-metadata separation.
32. **Quality PASS is not a free-text assertion.** Applicable checks must be implementation-verifiable and exact-input bound; expected checks derive from Core + Research Profile + Publication Profile.
33. **Validation applicability is part of correctness.** Long-form/Period-only checks must not be forced on Weekly solely because they exist in the historical Special corpus.
34. A Research Profile advertised as first-class must have a canonical production initializer. `RETROSPECTIVE_PERIOD` therefore requires an explicit bounded-Period entrypoint before general Special readiness.
35. Supporting `Generative AI Foundations` means supporting its multi-volume Series semantics, not merely allowing each volume to run as an unrelated Thematic Special. Series state remains an outer non-gating authority.
36. Pilot configuration must faithfully encode the edition's planning authority. Topic-specific scope belongs in Pilot/edition configuration, not generic Thematic Core.
37. Pre-merge generalization evidence must include later/unlisted Weekly/Thematic/Period/Series fixtures rather than relying only on W33/SP001.
38. Material recurring Human Review issues require an explicit Issue→Guard primary owner. Deterministic recurrence may not rely only on reviewer memory; inherently visual/editorial judgment need not be converted into brittle global validation.

## 5. Cross-cutting finding status

### 5.1 Repaired before the WU-010 Human re-audit

- **AUD-001 / WU-010 — REPAIRED, then strengthened by WU-010R.** Architecture Review uses immutable proposed Architecture bytes plus independent Approval Record. WU-010R additionally requires semantic checkpoint attestation and State-pinned gate provenance.
- **AUD-011 / WU-010 — REPAIRED.** State-pinned implementation identity survives artifact-only commits while committed/staged/unstaged/untracked implementation-control drift fails closed.

### 5.2 WU-010R Human re-audit remediation — implementation complete

AUD-013 through AUD-018 are repaired at implementation/regression level. Machine-readable Repair Set `REPAIR-WU010R-2026-08-22` remains `IMPLEMENTED`, not `VALIDATED/CLOSED`, because W33/SP001 verification editions have not begun. Finding closure therefore remains pending Pilot verification while WU-010R itself is complete.

- **AUD-013 — `FIXED_GENERIC`.** Semantic Validation Attestation is required before checkpoint pass and Architecture approval.
- **AUD-014 — `FIXED_GENERIC`.** Production State lifecycle/history/checkpoint/gate/controller consistency and provenance validate fail-closed.
- **AUD-015 — `FIXED_GENERIC`.** Action planning consumes transitive State-pinned authorities; post-attestation drift invalidates planning.
- **AUD-016 — `FIXED_GENERIC`.** Retry is action/stage-specific and dispatch retry requires idempotency authority.
- **AUD-017 — `FIXED_GENERIC`.** This index normalizes current finding status without another amendment-chain document.
- **AUD-018 — `FIXED_GENERIC`.** Standalone Finding closure is invalid; closed Repair Set authority is required.

### 5.3 WU-011 full-candidate remediation — implementation complete, Pilot verification pending

The WU-011 second audit is recorded in `docs/survey-production-core-v2-wu011-second-audit-closure.md`. No external W33/SP001 Production State was created. The WU-011 Repair Set remains `IMPLEMENTED` with empty verification editions until real Pilots run after the eventual Human review and merge.

Original whole-system blockers are repaired:

- **AUD-003 — implemented/regression-covered.** Discovery graph resolution, structured trigger/method provenance, accepted Raw exact-byte identity and drift rejection.
- **AUD-004 — implemented/regression-covered.** Common fail-closed JSON Schema conformance before semantic acceptance.
- **AUD-005 — implemented/regression-covered.** Bounded item-level review-attention surface with explicit overflow/truncation.

Machine-readable WU-011 second-audit findings are:

- **AUD-019 — `FIXED_GENERIC`.** Durable Actions-artifact PDF authority replaces repository-local-only liveness assumption.
- **AUD-020 — `FIXED_GENERIC`.** Canonical v2 production-control/release workflow identities and assistant-control allowlist are explicit.
- **AUD-021 — `FIXED_GENERIC`.** Release uses explicit `release_identity` exact-byte reconciliation after partial external success.
- **AUD-022 — `FIXED_GENERIC`.** Executed production code/workflow identity is State-pinned.
- **AUD-023 — `FIXED_GENERIC`.** Production State validates artifact-backed Publication Preview authority.
- **AUD-024 — `FIXED_GENERIC`.** W33/SP001 registry, planner/initializer, resume rules and session bootstrap are repository-owned and fail closed.
- **AUD-025 — `FIXED_GENERIC`.** Human/Exception/Complete terminal Action Spec is durably persisted on gate arrival.
- **AUD-026 — `FIXED_GENERIC`.** Current-main Weekly production workflow was restored; only bounded v2 cross-regression wiring remains.

No implementation-level P0/P1 defect remained open **within the WU-011 audit scope at its closure**. The later approval audit intentionally tested broader production-readiness criteria and opened WU-012; it does not rewrite WU-011 history.

### 5.4 WU-012 pre-approval audit — OPEN / merge blocking

The user-requested approval audit opened these findings against candidate commit `8beaf978793d983cc7608f4ca9c534511dd04d7a`:

- **AUD-027 — `OPEN` / CORE / COVERAGE.** Mandatory completeness can self-assert SATISFIED without authoritative Source Intake/search support.
- **AUD-028 — `OPEN` / WEEKLY_PROFILE / EDITORIAL.** Issue #9 Weekly reader semantics are not enforced through final Draft/Publication.
- **AUD-029 — `OPEN` / QUALITY_CONTRACT / CORRECTNESS.** Quality PASS is self-attested and the universal check set over-applies Long-form concerns to Weekly.
- **AUD-030 — `OPEN` / PERIOD_PROFILE / ORCHESTRATION.** First-class Retrospective Period has no canonical initializer.
- **AUD-031 — `OPEN` / SERIES_LAYER / COVERAGE.** Foundations Series Research Layer is planned but not implemented.
- **AUD-032 — `OPEN` / EDITION_LOCAL / COVERAGE.** SP001 registry scope is narrower than TS-001 backlog authority.
- **AUD-033 — `OPEN` / CORE / COMPATIBILITY.** Generalization proof is too centered on W33/SP001.
- **AUD-034 — `OPEN` / QUALITY_CONTRACT / CORRECTNESS.** Historical Human Review defect families lack one explicit current Issue→Guard ownership map.

These findings have no Repair Set yet because implementation has not begun. Their authoritative repair work is WU-012A–H in `docs/survey-production-core-v2-improvement-plan.md` §§16–18.

## 6. Negative-design rules that remain active

Drafting, Synthesis and orchestration must preserve the corrected architecture:

- no generic `late_breaking` field;
- no generic `this_week` synthesis payload;
- Draft basis binds independently authorized Architecture bytes; do not depend on self-mutated `APPROVED` Architecture semantics;
- Evidence refs, attribution/subject boundaries, must-cover requirements and explicit limitations survive into Draft validation;
- Profile semantics remain Profile-owned;
- Publication semantics remain Publication Profile-owned;
- handler success is not validation authority;
- worklog status is not semantic authority;
- artifact-only HEAD movement never silently changes the State-pinned implementation authority;
- durable artifact authority does not weaken exact-byte validation;
- a Human Gate may not be synthesized from chat or inferred from silence;
- a green legacy spine does not justify modifying unrelated legacy production behavior;
- WU-012 may strengthen machine evidence but must not turn normal deterministic checkpoints into new Human Gates;
- no fixed source/story/page quota may substitute for evidence-backed completeness.

## 7. Pilot bootstrap and current gate

External W33/SP001 production remains prohibited while PR #310 is an unmerged improvement candidate. W34/SP002/SP003 are also outside authorized production until the first Pilot feedback sequence begins after merge.

The **current legitimate action is WU-012 pre-merge hardening**, not approval/merge. The previous WU-011 Human-review handoff has been reopened by the requested pre-approval audit.

After WU-012A–H are implemented, regression-covered, given a separate Repair Set, and re-audited as one candidate, the process must stop again at **Human full-candidate review of PR #310**. Only explicit approval of that repaired candidate permits merge to `main` and subsequent Pilot initialization.

A Pilot finding must be recorded in the machine-readable Finding/Repair Set loop. WU-010R/WU-011 findings remain non-closed until verification editions support their governance transition.

## 8. Avoid amendment-chain growth

These amendments/audits are temporary design-history scaffolding.

After W33/SP001 and second validation stabilize the design:

- consolidate the active Core/Profile contracts;
- mark base/amendment/audit documents as historical design evidence where appropriate;
- point bootstrap/agent docs to a small canonical contract set;
- do not create a permanent `v2/v3/...` documentation repair chain analogous to the old Special runtime repair chain.

WU-012 should update the existing plan/index/Finding governance rather than create another long chain of prose-only amendment documents unless a distinct audit artifact is genuinely needed.

## 9. Resume rule

Before starting or continuing a work unit:

```text
read current main
-> read worklog for status/next action
-> read this index for semantic authority
-> read improvement-plan §§16–18 for WU-012 requirements
-> verify repository reality
-> if WU-012 findings AUD-027–034 remain OPEN: continue WU-012, do not approve/merge/start Pilots
-> after WU-012 repair + whole-candidate audit: stop at Human full-candidate review of PR #310
-> only after explicit Human approval and merge: enter via Core v2 session bootstrap
-> for every Pilot continuation, reconstruct from Profile/State/Action Spec rather than conversation history
```
