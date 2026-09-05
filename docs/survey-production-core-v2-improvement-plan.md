# Survey Production Core v2 — Compilation System Improvement Plan

Status: `WU-012 + AUD-046 + AUD-047 REPAIRS IMPLEMENTED / AUDIT-STABLE PRE-AUDIT CANDIDATE`  
Established: 2026-08-22 JST  
Current maintenance branch: `fix/core-v2-screening-expansion-authority-20260904`
Production source of truth: current `main` at reviewed baseline `c7a898889463b049dea4ee7337ee16ad5fbf3191`; this candidate is not merged
Current integration PR: `#483` (draft, unmerged; normal review metadata)
Operator-model authority: `docs/survey-production-core-v2-authority.md`  
Final-audit rule: `docs/survey-production-core-v2-final-audit-rule.md`

## 1. Objective

Survey Production Core v2 exists to help an upper-tier ChatGPT reasoning model compile the Japanese Generative AI Technical Survey accurately, efficiently and reproducibly across sessions.

It is **not** an external autonomous publishing engine. ChatGPT performs open-ended research/editorial reasoning; repository-owned guidance, schemas, scripts, tests and workflows support deterministic/repetitive/provenance-sensitive work.

```text
user target + requested stopping Human Gate
-> ChatGPT reads repository authority/Profile/State
-> ChatGPT researches, judges materiality/completeness, selects and drafts
-> deterministic helpers protect crisp invariants
-> exact stage artifacts + compact provenance checkpoint
-> continue autonomously
-> stop only at a real Human/Exception Gate or unavoidable manual Grok transport
```

Core priority remains:

```text
Correctness > Traceability > Coverage > Speed
```

Traceability does not justify ceremony whose cost exceeds its protection.

## 2. Acceptance priorities

Before merge, evaluate in this strict order:

1. **Weekly viability** — future Weekly issues compile reliably, including required Grok/X Source Intake and Drive return handling.
2. **Special viability** — Retrospective Period, stand-alone Thematic, SP-001–003 style work and Generative AI Foundations compile reliably, including explicit X applicability decisions.
3. **Generality** — no overfit to W33/W34/SP001–003; later Weekly and unforeseen Specials remain generic.
4. **Historical/clarified requirement recurrence prevention** — known Human Review failures and later clarified production requirements have durable prevention ownership.
5. **Control proportionality** — avoid unnecessary gates, ceremony and brittle validators once 1–4 are protected.
6. **Autonomous progression / stop discipline** — after target + requested Gate, ChatGPT does not repeatedly stop for routine internal work. Only normal Human Gates, a genuine Owner-level Exception Gate, or unavoidable manual Grok instruction/result transport may interrupt progress.
7. **Human Gate round-trip viability** — Architecture Review and exact-byte Publication Preview preserve durable reviewed-commit, approval, revision, cross-gate, and connector-safe round-trip authority.

These seven points are the canonical fixed-head final-audit contract; each is evaluated from zero on one unchanged candidate SHA.

## 3. Core/Profile architecture

```text
Survey Production Core v2
  + Research / Editorial Profile
      WEEKLY
      RETROSPECTIVE_PERIOD
      THEMATIC
  + Publication Profile
      WEEKLY_MAGAZINE
      LONGFORM_SPECIAL
  + optional living Series guidance
      Generative AI Foundations etc.
```

Core owns reusable mechanisms. Profiles own edition semantics. A living Series document may coordinate volumes without becoming another workflow engine.

### Weekly owns

- current-window/cutoff significance;
- carry-over and Late Breaking;
- Watchlist semantics;
- `why this week`;
- mandatory X/Grok intake.

### Retrospective Period owns

- bounded completed-history scope;
- chronology/period labels;
- retrospective coverage and synthesis;
- explicit X applicability decision.

### Thematic owns

- explicit research question;
- open-history/current-state scope;
- lineage/branch/competitor expansion;
- thematic completeness;
- explicit X applicability decision.

### Foundations Series

`docs/generative-ai-foundations-special-series.md` remains the living series architecture. Foundations uses normal `THEMATIC` production and the dedicated `Generative_AI_Foundations` Drive category when X is material. A machine Series engine remains deferred until real production demonstrates need.

## 4. Responsibility boundary

### ChatGPT owns

- Source Intake/search strategy and expansion;
- X/Grok applicability where Profile policy permits judgment;
- Grok run-specific research instructions;
- Google Drive folder provisioning and result import;
- source quality and primary-source gap fill;
- semantic Screening/Evidence interpretation;
- completeness/materiality judgment;
- Candidate Selection and Architecture;
- drafting/synthesis;
- historical attribution/significance;
- Weekly/Special editorial semantics;
- semantic and visual review;
- ordinary repair/retry and autonomous continuation;
- classification/generalization of new findings.

### Deterministic tools own/assist

- cutoffs/windows/date/Profile bootstrap;
- schemas/formats/paths/hashes;
- X Source Intake manifest and result-binding validation;
- Raw immutability/provenance;
- IDs/URLs/source refs;
- duplicate/missing/disposition accounting;
- subject/entity/property binding;
- targeted period-label checks;
- bibliography/render/build/preflight;
- exact semantic stage validation;
- exact Production Profile-bound quality applicability;
- exact Publication Preview/PDF/Freeze/Release identity;
- Release reconciliation/idempotency.

Grok owns X-native observation only. Grok output is Discovery/community signal, not final technical Evidence authority.

## 5. Human / Exception / Grok transport boundaries

Normal production Human Gates remain exactly:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

Candidate Selection is internal. Visual Review, Freeze, merge and Release are not routine Human Gates.

Exception Gate is reserved for unresolved Owner decisions that repository authority cannot safely settle. Search refinement, ordinary QA failure, CI retry, tooling repair and weak-source replacement are not Human Gates.

When Grok cannot be invoked directly, the Human may manually pass the generated prompt/instruction or return the resulting file. That is an **operational transport stop only**. ChatGPT must not ask for unrelated approval at that boundary, and resumes automatically once the result exists in the configured Drive folder.

## 6. Cross-session resume and toolchain evolution

Repository state, not chat history, must be sufficient for continuation. A new session recovers target/Profile/work branch, Production State, accepted artifacts, current Gate, research limitations and checkpoint tool/contract provenance.

Initialization implementation identity is historical provenance, not a permanent execution lock.

Reviewed generic repair loop:

```text
reusable defect found
-> generic repair reviewed/merged on main
-> integrate repair into edition work branch
-> revalidate/migrate only affected accepted boundaries
-> next Stage Checkpoint records actual integrated head + current contract
-> continue automatically
```

Compatibility ambiguity that changes accepted meaning may require an Exception Gate; ordinary upgrades do not.

## 7. Compact orchestration

Historical WU-010R/WU-011 local ceremony is not the hot path.

Current local path:

```text
ChatGPT produces exact intended stage artifacts
-> scripts/survey_stage_validation_v2.py
-> CORE_STAGE_CONTRACT binds State/Profile/current tool/current contract/artifacts
-> applicable ChatGPT review
-> one compact Stage Checkpoint
-> State advances
-> continue immediately
```

Canonical `stage_plan[*].handoff_required=false`. Richer reconciliation remains justified at irreversible external Release boundaries, not ordinary local transitions.

## 8. Source Intake / Grok / completeness / materiality

Issue #166 established that collector success or source count does not prove completeness and material discoveries cannot disappear silently.

ChatGPT completeness review records what was searched, material branches, gap fill, meaningful negative results, residual uncertainty and READY/LIMITED reasoning. No universal source/story/page quota is introduced.

AUD-046 formalizes X/Grok:

- Weekly: `REQUIRED_BY_PROFILE`;
- Period/Thematic: explicit ChatGPT `REQUIRED` / `NOT_REQUIRED` with rationale;
- Foundations: Thematic policy plus dedicated Drive category when required;
- root: `Grok_X_SourseIntake/<category>/<edition>/<run-id>/`;
- returned Markdown imported as exact Raw bytes;
- each result must become `DISCOVERY_RECORDED` or `NO_MATERIAL_DISCOVERY`;
- technical claims require later authoritative Evidence verification.

## 9. Historical Issue prevention

Every recurring defect family gets one primary owner:

```text
DETERMINISTIC_TOOL_CHECK
CHATGPT_RESEARCH_REVIEW
CHATGPT_EDITORIAL_REVIEW
CHATGPT_VISUAL_REVIEW
HUMAN_ARCHITECTURE_REVIEW
HUMAN_PUBLICATION_PREVIEW
LEGACY_ONLY / NOT_APPLICABLE
```

Examples include #166 completeness/material drop, #191 entity rebinding, #49 period labels, #9 Weekly semantics, #55/#122/#271 layout and wrapper failures, and exact-byte release drift.

AUD-047 adds a process invariant: **two formal Human Gates are not enough if the model still pauses at every internal stage**. Stop discipline is explicitly audited.

## 10. Quality and publication

Quality uses:

```text
DETERMINISTIC
AGENT_SEMANTIC
AGENT_VISUAL
```

Applicability derives from exact Production Profile bytes. The Publication Candidate must match its bound Quality bundle and Profile.

Retrospective public identity derives from exact Profile `survey_root`, so internal `SP-2025-H2` can publish as established `special/2025-H2`.

Exact Publication Preview / Visual / Freeze / Manifest / Merge Verification / Release Record byte authority remains strict.

## 11. Generality strategy

Pre-merge genericity is structural:

- arbitrary completed Weekly ID;
- arbitrary bounded Period spec;
- arbitrary Thematic question/spec;
- no generic code branch on W33/SP001/TS-001;
- Profile-selected research/publication behavior;
- living Series guidance for evolving Foundations volumes.

AUD-033 intentionally defers exhaustive hypothetical future-edition matrices. Real W33/SP001 followed by W34/SP002/SP003 provide stronger post-merge evidence.

## 12. Repair status

`FIXED_GENERIC` includes AUD-027–030, AUD-032, AUD-034–047.

Key late repairs:

- AUD-039 exact semantic stage authority;
- AUD-040 practical current-tool adoption;
- AUD-041 fixed-head final-audit rule;
- AUD-042 exact Profile-bound Quality;
- AUD-043 Retrospective public identity;
- AUD-044 bounded Period completion guard;
- AUD-045 audit-stable status synchronization;
- AUD-046 formal Grok/X + Google Drive Source Intake;
- AUD-047 autonomous progression / stop discipline as an independent final-audit point.

Intentional `DEFERRED`:

- AUD-031 — machine Series engine;
- AUD-033 — exhaustive synthetic future-edition matrix.

`REPAIR-WU012-2026-08-22` remains `IMPLEMENTED`, not `VALIDATED/CLOSED`, until real W33/SP001 verification occurs.

## 13. Mandatory final candidate rule

The candidate tree remains a stable pre-audit snapshot:

```text
finish all repository-side changes
-> obtain five CI cross-regression families green on one exact head
-> freeze that head
-> audit all seven acceptance points from zero on the unchanged SHA
```

The five CI families are unchanged. The seven acceptance points are Weekly viability, Special viability, generality, historical/clarified recurrence prevention, control proportionality, autonomous progression/stop discipline, and Human Gate round-trip viability.

Any candidate-tree mutation invalidates the entire audit. After repair, rerun CI, freeze a new head, and rerun **all seven points from point 1**.

The final PASS is recorded outside the candidate tree in PR/Human-review metadata keyed to exact audited SHA and CI run IDs.

The prior frozen candidate `c565a3254ad303bd276edee55b2b1e6e0a1c91a7` is historical only: its audit was invalidated by a current-facing authority wording contradiction. No CI or audit result from that SHA is carried forward.

## 14. Rollout boundary

Before explicit Human approval + merge:

- PR #310 is a historical merged implementation PR; current integration review continues in draft PR #483, which remains open and unmerged;
- `main` remains production authority;
- W33/SP001 and other Core-v2 Pilots remain unstarted;
- frozen historical releases remain immutable.

After approval + merge:

1. merged `main` becomes source of truth;
2. run W33 and SP001 as first real verification editions;
3. classify concrete findings and repair the narrowest correct layer;
4. follow with W34 and SP002/SP003;
5. add deferred machinery only when production demonstrates need.
