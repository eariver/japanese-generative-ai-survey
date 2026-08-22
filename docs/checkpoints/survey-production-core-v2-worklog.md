# Survey Production Core v2 — Work Log

Status: `ACTIVE / canonical improvement-work checkpoint`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Draft implementation PR: `#310`  
Plan: `docs/survey-production-core-v2-improvement-plan.md`  
Semantic authority: `docs/survey-production-core-v2-authority.md`

## 1. Ledger contract

This file is the persistent **work-status** authority for Survey Production Core v2. It owns current work-unit status, validation notes, unresolved execution issues, and the exact next action. Semantic/design policy remains owned by the authority index and its referenced contracts/audits.

Repository reality is the highest factual authority. Current `main` remains the production source of truth until a coherent v2 candidate is reviewed and explicitly merged. Frozen historical releases are never rewritten by this improvement work.

## 2. Current snapshot

Last updated: **2026-08-22 JST — WU-010R completed after Human re-audit remediation and second audit**

- Repository: `eariver/japanese-generative-ai-survey`
- Improvement branch: `refactor/survey-production-core-v2`
- Production `main`: `2086b396d2f30103d9292b722891be436cd28db5` — rechecked at WU-010R closure; branch remains behind by 0 commits.
- Pre-remediation branch head: `f6ec62603ca126acf532c7288863db3ad4fc7e6d`.
- WU-010R validated implementation head: `35dd8881ba83bf106ae6d934ad0212d2e0eafb47`.
- WU-010R machine-readable Repair Set: `REPAIR-WU010R-2026-08-22`; status `IMPLEMENTED`, intentionally not `VALIDATED/CLOSED` before Pilot verification editions.
- Draft PR: `#310 Survey Production Core v2 implementation`; remains draft.
- Current phase: **Phase 3 — Core v2 Candidate Implementation**.
- **WU-010R: COMPLETE.**
- **WU-011: PLANNED / NOT STARTED.**
- External W33/SP001 production: **NOT STARTED / NOT AUTHORIZED** until WU-011, full-candidate review and merge to `main` are complete.

## 3. Durable rollout rules

- W33 = **Weekly Profile First Production Validation**; legacy W33 state is comparison/provenance only, not a migration target.
- SP001 = **Thematic Profile First Production Validation** with genuine expansion/closure and no fabricated bounded history window.
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
| WU-005 | `COMPLETE / AUDIT FINDING REPAIRED` | Profile/State/contract+implementation identity; AUD-014 hardened in WU-010R |
| WU-006 | `COMPLETE / POST-AUDIT HARDENED` | Discovery/Screening v2 + self-contained archive; AUD-003 remains WU-011 |
| WU-007 | `COMPLETE / POST-AUDIT HARDENED` | factual Evidence + Edition View + Materiality + Completeness |
| WU-008 | `COMPLETE / AUDITED` | Matrix + internal Selection + generic Architecture + Review Summary |
| WU-008A | `COMPLETE` | whole-system audit remediation + 5/5 cross-regression green |
| WU-009 | `COMPLETE / AUDITED` | generic Draft Package/Result + Profile Synthesis |
| WU-010 | `SUPERSEDED BY WU-010R REMEDIATION` | original orchestration baseline retained; Human re-audit reopened closure |
| **WU-010R** | **`COMPLETE / SECOND-AUDIT GREEN`** | AUD-013–018 repaired; 71 Core tests + 5/5 cross-regression green; Repair Set IMPLEMENTED |
| **WU-011** | **`PLANNED / NOT STARTED`** | P0 quality/provenance integration + full Pilot bootstrap |

## 5. WU-010R completed remediation

The WU-010 Human re-audit opened AUD-013 through AUD-018. WU-010R repaired them without weakening the existing Core/Profile separation or changing frozen production releases.

Implemented outcomes:

- machine checkpoints require implementation-controlled semantic validation and immutable exact-byte Validation Attestations;
- Production State pins checkpoint and Human Gate provenance and validates lifecycle/history/checkpoint/gate/controller self-consistency fail-closed;
- Action Specs consume transitive State-pinned authorities so upstream artifact drift invalidates subsequent planning;
- Architecture Review approval consumes exact attested/reviewed Architecture + Review Summary bytes;
- local retry semantics are separated from workflow dispatch; `WORKFLOW_DISPATCH` is non-retryable by default unless explicit idempotency authority exists;
- standalone Finding closure is invalid; closed Repair Set authority governs Finding closure;
- semantic authority and work-status authority are synchronized without another amendment-chain document;
- machine-readable Findings AUD-013–AUD-018 and Repair Set `REPAIR-WU010R-2026-08-22` are committed and dogfooded by Core CI.

The Repair Set remains `IMPLEMENTED`, not `VALIDATED/CLOSED`, because its verification editions are intentionally empty until W33/SP001 production validation is authorized and executed. This does not block WU-011; it prevents premature claim of Pilot-proven closure.

## 6. WU-010R validation evidence

Validated implementation head:

```text
35dd8881ba83bf106ae6d934ad0212d2e0eafb47
```

Cross-regression results at that head:

| Validation family | Result | GitHub Actions run |
|---|---|---|
| Survey Production Core v2 CI | `PASS` — 71 tests + contract parse + Repair Set dogfood | `32553928808` |
| Screening contract CI | `PASS` | `32553928806` |
| Evidence contract CI | `PASS` | `32553928811` |
| Pipeline contract tests | `PASS` | `32553928790` |
| Weekly pipeline spine + committed Raw integrity | `PASS` | `32553928809` |

Second WU-010R audit result:

- AUD-013 through AUD-018 have implementation and regression evidence;
- no new WU-010R P0/P1 defect was found;
- upstream-artifact-after-attestation tampering is covered by a dedicated negative regression;
- Finding/Repair Set governance is itself exercised against the committed WU-010R audit records;
- the remaining pre-Pilot blockers are correctly bounded to WU-011 rather than hidden under WU-010R.

## 7. Still deliberately deferred to WU-011

These remain valid pre-Pilot blockers and are now the next work-unit boundary:

- **AUD-003** — Discovery graph resolution, structured discovery-method/trigger provenance, accepted Raw byte identity;
- **AUD-004** — common fail-closed JSON Schema conformance layer for model/external artifacts;
- **AUD-005** — bounded item-level exclusion/hold/non-material/duplicate Human Review surface with explicit overflow;
- exact-byte Publication Preview → Visual Review → Freeze → merge verification → Release authority;
- settled W33/SP001 production handler/bootstrap wiring and assistant-control/workflow allowlists.

## 8. Current action

**WU-010R is COMPLETE. Stop here for this work unit. WU-011 is the next planned unit but has NOT started. Do not begin W33 or SP001 until WU-011, full-candidate review, and merge to `main` are complete.**
