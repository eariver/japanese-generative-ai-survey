# Survey Production Core v2 — WU-012 Pre-approval Closure

Status: `IMPLEMENTATION COMPLETE / WHOLE-CANDIDATE AUDIT GREEN / HUMAN FULL-CANDIDATE REVIEW REQUIRED`  
Date: 2026-08-22 JST  
Branch: `refactor/survey-production-core-v2`  
PR: `#310`  
Audited semantic implementation head: `1d6e37f48cd24ce96ef7970df0e70697e546f2e3`

## 1. Purpose

This document closes the **pre-merge implementation and whole-candidate audit portion** of WU-012. It does not approve or merge PR #310, does not start W33/SP001, and does not mark the WU-012 Repair Set `VALIDATED` or `CLOSED` before real Pilot verification.

The user-requested acceptance priorities are applied in this order:

1. Weekly editions must be realistically compilable.
2. Specials must be realistically compilable, including Retrospective Period, stand-alone Thematic Specials, and the planned Generative AI Foundations series workflow.
3. The design must not be overfit to W33/W34/SP001–003.
4. Historical Human Review defects should have explicit recurrence ownership.
5. Only after 1–4 are satisfied should unnecessary gates/validation be removed or avoided.

## 2. Final operating model

The corrected Core v2 candidate is **ChatGPT-first**.

```text
short user request naming target + desired Human Gate
-> ChatGPT reads repository authority / Profile / State
-> ChatGPT performs open-ended research and editorial reasoning
-> deterministic helpers handle crisp structural/provenance/repetitive checks
-> canonical stage artifacts are produced
-> compact Stage Checkpoint binds exact stage artifacts + review basis + implementation/contract provenance
-> ChatGPT continues autonomously
-> stop only at Architecture Review, Publication Preview, or a genuine Exception Gate
```

The normal local path no longer requires the full legacy control-plane ceremony of Action Spec → Handoff Request → Handoff → Action Result → Validation Attestation. Legacy code remains in the repository as historical/compatibility material, but it is not the canonical production hot path.

The normal Human Gate count remains exactly two:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

Candidate Selection remains internal. Visual Review, Freeze, merge and Release do not become routine additional Human Gates.

## 3. Weekly viability — priority 1

**Conclusion: ready for Human approval and subsequent real W33 Pilot validation.**

The pre-approval audit originally found two material Weekly risks:

- Source Intake / Completeness could become ceremonial if an agent merely asserted readiness;
- historical Issue #9 semantics were not explicit enough in the current operating guidance.

WU-012 resolves these without imposing arbitrary source/story quotas:

- ChatGPT owns Source Intake strategy, expansion, gap-fill and substantive completeness judgment;
- readiness requires meaningful search/coverage rationale, negative-result accounting where applicable, residual uncertainty, and explicit limitations;
- deterministic validation owns traceability/structure, not the impossible claim that open-ended research has been mathematically proven complete;
- the Issue Prevention Checklist explicitly owns Weekly `why this week`, pre-window/background justification, Late Breaking single-home semantics, Watchlist state/unknown/change-condition semantics, carry-over disposition, and reader-facing/internal-metadata separation;
- Weekly-specific semantics remain Profile-owned and are not pushed into generic Core enums.

The current-main Weekly production workflow is also protected by the cross-regression suite. The final semantic candidate passed Weekly pipeline spine + committed Raw integrity on run `32568620741`.

## 4. Special viability — priority 2

**Conclusion: ready for Human approval and subsequent real SP001 / Period validation, with one deliberate Series boundary.**

### 4.1 Retrospective Period

A generic bounded-period bootstrap now supports configured monthly, half-year and annual editions plus custom bounded periods without edition-specific Core branches. Period boundaries are interpreted in the intended local temporal semantics and stored as normalized instants.

This closes the previous gap where `RETROSPECTIVE_PERIOD` existed as a declared research profile but lacked a canonical initializer.

### 4.2 Stand-alone Thematic Specials

The Thematic path remains generic. SP001 no longer treats its narrow Pilot registry copy as the editorial source of truth; bootstrap materializes scope from the canonical TS-001 planning authority. Topic-specific China-model semantics remain edition/Pilot data rather than Core code.

### 4.3 Generative AI Foundations series

A full machine-readable Series engine remains **intentionally deferred** under AUD-031.

This is not a missing pre-merge requirement. The existing living series authority already records the directed lineage model, cross-volume dependencies, merge/split/resequence policy, open research questions and frontier refresh policy. For the ChatGPT-operated process, that is sufficient to start individual volumes while maintaining outer-series reasoning.

Per-volume Production State remains independent. Shared corpus/index tooling should be added only if real Foundations production demonstrates repeated cost, drift or ambiguity that justifies it.

## 5. Generality — priority 3

**Conclusion: sufficient structural generality for merge approval; exhaustive synthetic future-edition simulation is intentionally not required.**

The candidate now supports:

- arbitrary completed Weekly identifiers through generic Weekly Profile logic;
- generic bounded Period definitions rather than month/H1/H2/year hard-coding in Core;
- arbitrary Thematic scope specs;
- planning-authority-driven SP001 materialization rather than China-specific Core behavior;
- per-checkpoint tool/contract provenance so later reviewed generic fixes can be adopted during an edition without rewriting initialization history.

Small structural tests cover generic Weekly/Period/Thematic behavior. AUD-033 remains deliberately `DEFERRED`: an exhaustive matrix of hypothetical W35+, every year boundary, every future Special type and Series mutation would add maintenance burden without equivalent safety. Real W33/SP001 are the next evidence source after merge.

## 6. Historical Issue recurrence prevention — priority 4

**Conclusion: recurrence ownership is explicit and no longer relies only on reviewer memory.**

Material historical defects are mapped to a primary prevention/inspection owner:

```text
DETERMINISTIC_TOOL_CHECK
CHATGPT_RESEARCH_REVIEW
CHATGPT_EDITORIAL_REVIEW
CHATGPT_VISUAL_REVIEW
HUMAN_ARCHITECTURE_REVIEW
HUMAN_PUBLICATION_PREVIEW
LEGACY_ONLY / NOT_APPLICABLE
```

The design deliberately avoids pretending that every editorial or visual defect can be encoded as a deterministic validator. Crisp recurrent failures receive deterministic checks; semantic and layout judgment remain explicit ChatGPT review responsibilities; residual reader-facing judgment remains at the already-existing Human Gates.

## 7. Over-validation / gate audit — priority 5

**Conclusion: the candidate is materially simpler than WU-010R/WU-011 while retaining the safety properties that matter.**

Removed from the canonical local hot path:

- mandatory Action Spec per local stage;
- mandatory Handoff Request / Handoff per local stage;
- mandatory Action Result / Validation Attestation ceremony where no distinct external boundary exists;
- edition-wide implementation commit lock-in;
- universal quality-check lists applied to unrelated Profiles;
- proposed extra machine Series engine before demonstrated need;
- proposed exhaustive synthetic future-edition fixture matrix.

Retained because they protect real failure modes:

- immutable Raw provenance;
- content-addressed accepted research artifacts;
- subject/entity/property binding;
- material-discovery disposition and completeness records;
- exact Architecture Review bytes;
- lifecycle-specific canonical artifact binding in compact Stage Checkpoints;
- Profile-aware deterministic / agent-semantic / agent-visual quality review;
- exact Publication Candidate / Preview / Freeze / Release byte chain;
- Release reconciliation/idempotency at the external irreversible boundary.

## 8. Whole-candidate audit finding discovered during closure

The final audit found one new Core traceability defect, `AUD-037`:

> Several compact local stages could theoretically advance with a PASS review record while binding no canonical stage artifact because those lifecycle states had no required artifact set.

This was repaired before closure. The Stage Checkpoint schema is now lifecycle-aware and requires the existing canonical logical artifacts for every transition. A regression test rejects review-only Screening advancement. The repair preserves compact orchestration while restoring exact artifact authority.

No unresolved non-deferred pre-merge finding remains from WU-012.

## 9. Final cross-regression evidence

Semantic implementation head `1d6e37f48cd24ce96ef7970df0e70697e546f2e3` passed all five required families:

| Validation family | Result | Run |
|---|---|---|
| Survey Production Core v2 CI | PASS | `32568620742` |
| Screening contract CI | PASS | `32568620692` |
| Evidence contract CI | PASS | `32568620743` |
| Pipeline contract tests | PASS | `32568620721` |
| Weekly pipeline spine + committed Raw integrity | PASS | `32568620741` |

Closure/authority metadata commits after this head must also remain CI-green before the Human review package is considered synchronized.

## 10. Finding / Repair Set disposition

WU-012 repaired findings:

- AUD-027 — `FIXED_GENERIC`
- AUD-028 — `FIXED_GENERIC`
- AUD-029 — `FIXED_GENERIC`
- AUD-030 — `FIXED_GENERIC`
- AUD-032 — `FIXED_GENERIC`
- AUD-034 — `FIXED_GENERIC`
- AUD-035 — `FIXED_GENERIC`
- AUD-036 — `FIXED_GENERIC`
- AUD-037 — `FIXED_GENERIC`

Deliberately deferred:

- AUD-031 — full machine Series engine; wait for real Foundations production evidence;
- AUD-033 — exhaustive synthetic future-edition fixture matrix; use small structural tests + real Pilots.

`REPAIR-WU012-2026-08-22` remains `IMPLEMENTED`, not `VALIDATED/CLOSED`, because verification editions are intentionally still empty. This prevents pre-merge CI from being misrepresented as real-production validation.

## 11. Production state / merge boundary

At this closure point:

- production `main` remains the source of truth and has not been changed by this branch;
- PR #310 remains draft and unmerged;
- W33, W34, SP001, SP002 and SP003 have not been started by Core v2;
- no Pilot is authorized before explicit Human approval and merge;
- frozen historical releases are untouched.

## 12. Stop condition

After closure metadata itself passes the required cross-regression checks, the next action is **Human full-candidate review of PR #310**.

Do not perform additional architectural expansion merely to make the candidate look more complete. New code before Human review is justified only if closure synchronization exposes a concrete defect.

If the Human review approves the candidate:

```text
approve PR #310
-> merge to main
-> use merged main as the new production source of truth
-> start real W33 / SP001 validation under the normal requested Human Gate
-> use resulting findings to decide whether any deferred tooling is actually necessary
```

If the Human review identifies a defect, record it through the Finding/Repair Set process and repair it before merge.
