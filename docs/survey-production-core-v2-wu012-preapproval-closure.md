# Survey Production Core v2 — Former WU-012 Pre-approval Closure

Status: `HISTORICAL / PREVIOUS FINAL-AUDIT CLAIM INVALIDATED`  
Date originally recorded: 2026-08-22 JST  
Branch: `refactor/survey-production-core-v2`  
PR: `#310`  
Former audited semantic implementation head: `1d6e37f48cd24ce96ef7970df0e70697e546f2e3`  
Former synchronized review head later audited: `2f3c9b10c031cf0d8e5cc114fb93e481e90fffac`

## 1. Status correction

This document previously claimed that WU-012 implementation and the five-point whole-candidate audit were complete and ready for Human full-candidate review.

That claim is **not current approval evidence**.

After the Owner clarified the mandatory review discipline — **all candidate changes must finish before the five-point audit, and any later candidate mutation invalidates that audit** — head `2f3c9b10c031cf0d8e5cc114fb93e481e90fffac` was frozen and audited again from zero. That post-completion audit found six additional blocking defect families:

- `AUD-039` — compact checkpoints did not themselves preserve strong semantic stage validation;
- `AUD-040` — practical current-tool adoption after initialization remained blocked by legacy helper pinning / work-branch integration ambiguity;
- `AUD-041` — the all-changes-first fixed-head final-audit rule was not repository-owned;
- `AUD-042` — Quality applicability was not bound to the exact Production Profile and could misclassify Retrospective Period as Thematic;
- `AUD-043` — Retrospective Period internal issue identity would leak into public Special release tag/title/asset identity;
- `AUD-044` — a bounded Retrospective Period could initialize before its period end.

Therefore the former five-point PASS and former “Human Review Ready” conclusion are explicitly invalidated.

## 2. What remains historically useful

The earlier WU-012 work remains useful design and regression evidence. In particular, it established the ChatGPT-first operating premise and retained these correct principles:

- ChatGPT is the primary research/editorial operator;
- normal production has exactly two Human Gates: `ARCHITECTURE_REVIEW` and exact-byte `PUBLICATION_PREVIEW`;
- Source Intake/completeness/materiality remain substantive ChatGPT reasoning rather than ceremonial machine truth;
- Weekly, Retrospective Period and Thematic semantics remain Profile-owned;
- immutable Raw provenance, Evidence entity binding, disposition accounting and exact publication byte authority remain deterministic protections;
- local Action/Handoff ceremony is not the canonical hot path;
- a machine Series engine and exhaustive hypothetical edition matrix remain intentionally deferred absent real production need;
- W33/SP001 remain first real post-merge verification editions rather than design templates.

Historical green CI on earlier heads remains evidence that those earlier trees were internally consistent at the time. It does not prove the current repaired candidate or replace the new final audit.

## 3. Current replacement authority

Current status and process are owned by:

1. `docs/survey-production-core-v2-authority.md`;
2. `docs/survey-production-core-v2-final-audit-rule.md`;
3. `docs/checkpoints/survey-production-core-v2-worklog.md`;
4. `docs/survey-production-core-v2-session-bootstrap.md`;
5. `docs/checkpoints/survey-production-core-v2-audit-findings/WU-012-repair-set.json`;
6. `AUD-039` through `AUD-044` and their regression fixtures.

The current repairs add, among other things:

- exact deterministic `CORE_STAGE_CONTRACT` validation before compact checkpoint adoption;
- actual work-branch toolchain integration semantics plus a narrow current-tool bridge for legacy Screening/Evidence helpers;
- exact Production Profile binding for Quality applicability;
- Profile-derived public Special release identity;
- bounded-period completion guard;
- the Owner's all-changes-first fixed-head five-point audit rule.

## 4. Non-self-invalidating final closure

This file will **not** be rewritten after the new final audit merely to record a PASS, because doing so would change the audited candidate SHA and immediately invalidate the result under the new rule.

The mandatory final sequence is:

```text
complete every candidate change
-> complete five-family cross-regression
-> freeze exact candidate head SHA
-> run all five acceptance points from zero without candidate mutation
-> if any change is needed, invalidate the entire audit and repeat after all repairs
-> if all five pass, record the exact SHA + five verdicts + CI run identities in PR/Human-review metadata
```

See `docs/survey-production-core-v2-final-audit-rule.md` for the canonical rule.

## 5. Merge / production boundary

Until an unchanged candidate passes that final audit and receives explicit Human full-candidate approval:

- PR #310 remains draft and unmerged;
- current `main` remains the production source of truth;
- W33, W34, SP001, SP002 and SP003 remain unstarted by Core v2;
- the WU-012 Repair Set remains `IMPLEMENTED`, not `VALIDATED/CLOSED`;
- frozen historical releases remain untouched.
