# Survey Production Core v2 — Compilation System Improvement Plan

Status: `WU-012 IMPLEMENTED / PRE-APPROVAL AUDIT GREEN / HUMAN REVIEW REQUIRED`  
Established: 2026-08-22 JST  
Consolidated after pre-approval re-audit: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Production source of truth until merge: current `main`  
Detailed pre-approval re-audit: `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md`  
WU-012 closure: `docs/survey-production-core-v2-wu012-preapproval-closure.md`

## 1. Purpose

This project improves how the Japanese Generative AI Technical Survey is compiled by ChatGPT.

The objective is **not** to build an external autonomous publishing engine. The intended operator is a current upper-tier ChatGPT reasoning model. Repository documentation, structured records, scripts and workflows exist to help that model work accurately, efficiently and consistently across sessions.

The production model is:

```text
user gives target + requested stopping Human Gate
  ↓
ChatGPT reads current repository policy/state
  ↓
ChatGPT performs research/editorial reasoning
  ↓
deterministic tools support repetitive/crisp/provenance work
  ↓
repository records enough state for another session to resume
  ↓
ChatGPT stops only at the requested Human Gate or a genuine Exception Gate
```

Core priority remains:

```text
Correctness > Traceability > Coverage > Speed
```

But precision does not mean maximizing schemas, validators, hashes or workflow transitions. A mechanism is justified only when it materially improves correctness, traceability, repeatability, resumption or production efficiency.

---

## 2. Acceptance priorities

Before Core v2 is approved, evaluate it in this order:

1. **Weekly production viability** — can ChatGPT reliably compile future Weekly issues?
2. **Special production viability** — can ChatGPT reliably compile Period/Thematic Specials, including SP-001–003 and the Foundations series?
3. **Generality** — does the system work beyond W33/W34/SP-001–003 without named-edition Core branches?
4. **Human Review Issue recurrence prevention** — have historical defects become durable guidance/tooling rather than reviewer memory?
5. **Avoid excessive gates/verification** — after 1–4 are satisfied, remove controls whose cost exceeds their protection.

When these conflict, the lower numbered requirement wins.

---

## 3. Target architecture

```text
Survey Production Core v2
  + Research / Editorial Profile
      - WEEKLY
      - RETROSPECTIVE_PERIOD
      - THEMATIC
  + Publication Profile
      - WEEKLY_MAGAZINE
      - LONGFORM_SPECIAL
  + optional living Series Research guidance
      - Generative AI Foundations etc.
```

The Core owns reusable mechanisms. Profiles own edition-specific research/editorial semantics. Publication Profiles own reader-facing assembly/layout behavior. A living Series document may coordinate multiple volumes without becoming another workflow engine or routine Human Gate.

### 3.1 Core responsibilities

Retain shared mechanisms for:

- immutable Raw provenance;
- source/discovery identity;
- Screening structure;
- Evidence structure and subject/entity binding;
- Materiality/disposition traceability;
- generic Matrix/Selection/Architecture records;
- structured Draft Package/Result;
- source/reference/identifier integrity;
- compact Production State/resume information;
- Human Gate records;
- deterministic publication/build checks;
- exact Publication Preview/Freeze/Release byte identity;
- Finding/repair history where it prevents repeated defects.

### 3.2 Profile responsibilities

`WEEKLY` owns current-week semantics, carry-over, Late Breaking, Watchlist and `why this week`.

`RETROSPECTIVE_PERIOD` owns bounded-period scope, chronology, retrospective coverage and period synthesis.

`THEMATIC` owns research-question scope, open-history/current-state policy, lineage/branch/competitor expansion and thematic completeness.

Profile semantics must not leak into generic Core fields merely because the first Pilot needs them.

### 3.3 Series guidance

`docs/generative-ai-foundations-special-series.md` is already the living outer research authority for the Foundations series. It defines the evolving lineage graph, volume architecture, dependencies, merge/split/resequence rules, historical-attribution policy, open questions and dated frontier snapshots.

A machine-readable Series state/evidence engine is **not** a precondition for starting the series. Add a lightweight shared index later only if real repeated cross-volume work demonstrates a concrete benefit.

---

## 4. Operator/tool boundary

### 4.1 ChatGPT-owned reasoning

ChatGPT owns open-ended work such as:

- Source Intake/search strategy and expansion;
- source-quality and primary-source gap-fill judgment;
- semantic Screening/Evidence interpretation;
- research completeness/materiality judgment;
- Candidate Selection;
- Architecture;
- article drafting and synthesis;
- historical significance/attribution;
- Weekly/Special editorial rationale;
- semantic review;
- visual/layout review;
- classification of new findings.

These decisions should be repository-backed and resumable, but they are not required to be externally machine-provable.

### 4.2 Deterministic tool-owned work

Use scripts/workflows where they are better than repeated reasoning:

- cutoff/window/date calculations;
- bootstrap paths/branch/profile creation;
- schema/format checks;
- Raw hashing/immutability;
- exact ID/path/URL/reference integrity;
- missing/duplicate/disposition accounting;
- targeted period-label checks;
- bibliography/render/build/preflight;
- deterministic regression checks;
- exact PDF/release authority;
- irreversible GitHub Release side effects and reconciliation.

A tool may validate a ChatGPT-created artifact. It should not replace qualitative research/editorial judgment with a ceremonial PASS field.

---

## 5. Human and Exception Gates

Normal Human Gates remain exactly:

1. **Architecture Review**
2. **Publication Preview** bound to exact PDF bytes

Candidate Selection remains internal.

Visual Review, Freeze, merge and Release are not additional routine Human Gates.

Use an Exception Gate only when a genuinely new editorial/publication/compatibility decision cannot be derived safely from repository authority. Retryable technical failures and ordinary tool upgrades are not Human Gates.

---

## 6. Cross-session resume model

The repository, not conversation history, must be sufficient for continuation.

A later session should be able to determine at minimum:

- issue/profile identity;
- work branch;
- current lifecycle/checkpoint;
- canonical stage outputs already accepted;
- applicable research/editorial guide;
- Human Gate status;
- unresolved limitations/findings;
- implementation/tool version used for each material checkpoint where relevant.

Do not require the user to repeat pipeline stages, page rules, historical Issue knowledge or release mechanics already encoded in the repository.

---

## 7. Provenance model

Preserve exact provenance where it matters, but avoid edition-wide toolchain lock-in.

### 7.1 Retain

- accepted Raw byte identity;
- stable source/Evidence IDs;
- exact source/artifact hashes where necessary;
- exact reviewed Architecture bytes;
- exact Publication Preview PDF bytes;
- exact Freeze/Release identity;
- implementation/tool commit used for a material checkpoint/action.

### 7.2 Correct

A Production State must **not** require every future stage to execute the implementation commit used at initialization.

Instead:

```text
checkpoint A -> records tool/commit A
checkpoint B -> may use newer reviewed main tool/commit B
```

If B changes the contract governing A's accepted artifact, ChatGPT performs targeted revalidation/migration before continuing. If compatibility cannot safely be decided, use an Exception Gate.

This allows the normal improvement loop:

```text
Human/agent discovers reusable pipeline defect
-> generic fix merged to main
-> current edition adopts improved tool
-> affected boundary revalidated
-> compilation continues
```

Earlier accepted artifacts keep their original provenance.

---

## 8. Local orchestration simplification

WU-010R/WU-011 introduced a robust but overly external-workflow-like chain for every local stage:

```text
Action Spec
-> Handoff Request
-> Handoff
-> Action Result
-> Validation Attestation
-> Production State transition
```

This is too much ceremony for a ChatGPT-operated repository when the same agent already creates the canonical stage artifacts.

The desired normal local path is:

```text
ChatGPT reads Profile + State + applicable guide
-> produces canonical stage artifacts
-> runs applicable deterministic checks
-> writes one compact checkpoint/result record
-> advances State
-> continues until Human/Exception Gate
```

Canonical `stage_plan` entries therefore set `handoff_required=false`. The old Handoff machinery remains available only as historical/compatibility code and may be explicitly enabled by a compatibility fixture.

Richer request/receipt authority remains appropriate for true external/asynchronous/irreversible boundaries such as durable build artifacts or public Release.

The simplification must preserve resumability, immutable accepted artifacts, Human approval identity and exact publication/release provenance.

---

## 9. Source Intake, Materiality and Completeness

Issue #166 established two durable lessons:

1. collector success or a large source count does not prove completeness;
2. material discoveries must not silently disappear downstream.

The solution is not an algorithm that proves all possible research was performed.

### 9.1 ChatGPT completeness review

For each Profile obligation, ChatGPT records enough rationale to answer:

- what was searched/investigated;
- what material sources/events/branches were found;
- what targeted gap-fill was performed;
- what remains uncertain;
- whether the obligation is satisfied, limited, not applicable, or still needs research;
- why the edition is ready/limited/incomplete.

A negative search result may be valid coverage evidence. An unsearched area must not silently appear complete.

No universal source/story/page quota is introduced.

### 9.2 Deterministic traceability

Tools continue to enforce crisp properties such as:

- every discovered/material ID receives a disposition;
- supplemental/gap-fill records join the same trace;
- subject/entity bindings remain stable;
- accepted Raw/source identities do not mutate.

---

## 10. Historical Issue recurrence prevention

The fifteen completed Specials, Weekly evolution and Human Review Issues are a durable knowledge corpus.

`docs/survey-production-core-v2-historical-invariants.md` and the deep historical audit are the source material. WU-012 converts them into a concise production-facing **Issue Prevention Checklist**.

Each material defect family receives one primary owner:

```text
DETERMINISTIC_TOOL_CHECK
CHATGPT_RESEARCH_REVIEW
CHATGPT_EDITORIAL_REVIEW
CHATGPT_VISUAL_REVIEW
HUMAN_ARCHITECTURE_REVIEW
HUMAN_PUBLICATION_PREVIEW
LEGACY_ONLY / NOT_APPLICABLE
```

Examples:

- #166 material drop → deterministic disposition accounting + ChatGPT completeness review;
- #191 subject/entity rebinding → structured Evidence + deterministic binding validation;
- #49 wrong period label → deterministic designated-field period check;
- #9 `why this week`, Late Breaking duplication, Watchlist/internal metadata → ChatGPT Weekly editorial review, with small deterministic leakage checks where reliable;
- #55 orphaned Technical Notes continuation → ChatGPT visual review rather than a global hard pagination rule;
- exact Release/PDF drift → deterministic byte-identity tooling.

Do not create a validator solely because an Issue once existed.

---

## 11. Quality review model

Use three review kinds:

```text
DETERMINISTIC
AGENT_SEMANTIC
AGENT_VISUAL
```

### 11.1 DETERMINISTIC

Requires executable check evidence and exact relevant input identity.

Examples: schema validity, IDs/URLs, bibliography refs, designated period labels, build/preflight, exact PDF bytes.

### 11.2 AGENT_SEMANTIC

ChatGPT reads the actual draft/source and records a short reasoned PASS/FINDING against an explicit checklist item.

Examples: source interpretation, why-this-week, synthesis adequacy, historical attribution, source-specificity where judgment is required.

### 11.3 AGENT_VISUAL

ChatGPT inspects rendered pages and records PASS/FINDING.

Examples: hierarchy, clipping, excessive whitespace, orphaned card tails, isolated boxes, TOC density, reader-facing flow.

Applicability is Research Profile + Publication Profile aware. A Long-form-specific concern is not required for Weekly merely because it exists in the historical Special corpus.

---

## 12. Weekly viability

The pre-approval candidate now supports later Weekly issues because:

- issue/cutoff derivation is generic;
- current significance/carry-over/Late Breaking are Profile semantics, not W33 Core branches;
- research/editorial judgment remains adaptable ChatGPT work;
- deterministic provenance/identity tools are issue-agnostic;
- Issue #9 is part of the canonical Weekly editorial review path;
- local orchestration is compact rather than control-file dominated;
- later reviewed generic tool fixes can be adopted per checkpoint;
- the current-main Weekly production spine remains protected by cross-regression.

W33 remains the first real production validation after approval/merge; it is not a design template.

---

## 13. Special viability

### 13.1 Retrospective Period

A lightweight generic bounded-Period profile/bootstrap helper supports:

- month;
- half-year;
- year;
- explicit custom bounded period.

The helper handles deterministic dates/paths/profile construction and points ChatGPT at applicable period guidance. It does not encode the edition's stories, taxonomy or synthesis conclusions.

### 13.2 Standalone Thematic

Thematic scope comes from an explicit research question and canonical planning guide/backlog.

SP-001/TS-001, SP-002/TS-002 and SP-003/TS-003 do not require topic-specific Core branches. SP001 bootstrap materializes the canonical TS-001 planning authority rather than treating a narrower Pilot registry copy as editorial truth.

### 13.3 Generative AI Foundations

Use `docs/generative-ai-foundations-special-series.md` as the living outer architecture. Each volume runs normal Thematic production while the series memo evolves from discoveries.

AUD-031 intentionally defers a machine Series engine until actual production shows that a shared source/evidence index would reduce repeated work or drift.

---

## 14. Generality strategy

Pre-merge genericity is demonstrated structurally, not by simulating every future edition.

Current structural coverage includes:

- arbitrary valid completed Weekly ID;
- arbitrary bounded Period spec;
- arbitrary Thematic question/spec;
- no production code branching on W33/SP001/TS-001 identifiers;
- Publication Profile behavior selected by profile, not named edition.

AUD-033 deliberately defers an exhaustive hypothetical edition matrix. Real production remains the stronger test:

```text
W33 + SP001
-> evaluate/fix
-> W34 + SP002 + SP003
-> stabilize
```

Future unknown Specials are expected to be handled by ChatGPT's reasoning under generic Profile guidance, not pre-enumerated by test fixtures.

---

## 15. WU history summary

- **WU-001/001A:** component inventory and Core/Profile ownership — retain.
- **WU-002:** contract normalization — retain two-gate/Profile architecture; lighten machine interpretation.
- **WU-003/003B/003C:** historical invariant/deep-production audit — retain as key Issue-prevention knowledge.
- **WU-004/004B:** minimum vertical slice — retain as first-slice design evidence.
- **WU-005:** Profile/State — retained with per-checkpoint implementation provenance correction.
- **WU-006:** Discovery/Screening — retained as tools around ChatGPT research.
- **WU-007:** Evidence/Materiality/Completeness — retained; Completeness is a structured reasoned judgment.
- **WU-008/008A:** Matrix/Selection/Architecture — retained.
- **WU-009:** structured Draft/Synthesis — retained.
- **WU-010/010R:** orchestration hardening — historical defect lessons retained; local control-plane implementation simplified in WU-012.
- **WU-011:** exact publication/release/bootstrap hardening — publication/release authority retained; local stage/Pilot scope controls simplified in WU-012.
- **WU-012:** ChatGPT-first simplification/guidance hardening — implementation and pre-approval whole-candidate audit complete; Human review required.

Historical detail remains available in the worklog, authority index, audit documents and Git history.

---

## 16. WU-012 — implementation result

WU-012 is implemented. Detailed closure is `docs/survey-production-core-v2-wu012-preapproval-closure.md`.

### WU-012A — ChatGPT-first operating contract — `COMPLETE`

- operator/tool boundary is explicit in canonical authority/bootstrap/AGENTS guidance;
- target + stopping gate remains sufficient user input;
- open-ended research/editorial judgment remains ChatGPT-owned.

### WU-012B — simplify local orchestration — `COMPLETE`

- one Production State + canonical outputs + compact Stage Checkpoint is the normal local path;
- canonical `stage_plan[*].handoff_required=false` aligns config with that path;
- legacy Action/Handoff machinery is not canonical production authority;
- richer exact control remains at external/irreversible Release boundaries;
- exactly two Human approval records remain.

### WU-012C — controlled toolchain evolution — `COMPLETE`

- implementation/tool commit is recorded per checkpoint/action;
- later stages may use newer reviewed tooling;
- initialization provenance is not rewritten;
- compatibility failures remain fail-closed.

### WU-012D — Issue Prevention Checklist — `COMPLETE`

Historical recurring defects now have explicit deterministic/agent/Human ownership without converting every judgment into a validator.

### WU-012E — small generic bootstrap/profile gaps — `COMPLETE`

- generic bounded-Period bootstrap exists;
- Thematic Pilot bootstrap references canonical planning authority;
- small structural genericity tests exist;
- no premature machine Series engine was added.

### WU-012F — quality-review tiers — `COMPLETE`

`DETERMINISTIC / AGENT_SEMANTIC / AGENT_VISUAL` applicability is Profile-aware. Only deterministic items require executable validator proof.

### Whole-candidate repairs — `COMPLETE`

- AUD-037 closed the compact-checkpoint provenance loophole by requiring lifecycle-specific existing canonical artifact authorities. A review-only stage transition is rejected.
- AUD-038 removed the final config contradiction by disabling legacy Handoff requirements in the canonical stage plan and preserving old behavior only in explicit compatibility fixtures.

---

## 17. WU-012 finding status

Repaired generically:

- AUD-027 `FIXED_GENERIC` — substantive ChatGPT completeness-review guidance;
- AUD-028 `FIXED_GENERIC` — Weekly Issue #9 agent editorial review;
- AUD-029 `FIXED_GENERIC` — deterministic vs agent quality tiers/applicability;
- AUD-030 `FIXED_GENERIC` — lightweight Period bootstrap helper;
- AUD-032 `FIXED_GENERIC` — SP001 planning-authority materialization;
- AUD-034 `FIXED_GENERIC` — Issue Prevention Checklist;
- AUD-035 `FIXED_GENERIC` — ChatGPT-first operator model / compact local orchestration;
- AUD-036 `FIXED_GENERIC` — per-checkpoint toolchain provenance;
- AUD-037 `FIXED_GENERIC` — lifecycle-specific canonical artifact binding;
- AUD-038 `FIXED_GENERIC` — canonical stage-plan Handoff contradiction removed.

Deliberately deferred:

- AUD-031 `DEFERRED` — full machine Series engine is premature;
- AUD-033 `DEFERRED` — exhaustive synthetic future-edition fixture matrix is unnecessary before real Pilot evidence.

Repair Set: `REPAIR-WU012-2026-08-22` is `IMPLEMENTED`. It is intentionally not `VALIDATED/CLOSED` before W33/SP001 production verification.

---

## 18. WU-012 exit condition

Before PR #310 returns to Human full-candidate review:

- [x] ChatGPT-first operator model is canonical and discoverable.
- [x] Local-stage orchestration is materially simpler while preserving resume/provenance.
- [x] Canonical stage configuration no longer requires legacy Handoffs.
- [x] Implementation provenance is per checkpoint/action and controlled toolchain upgrades are possible.
- [x] Historical Issue Prevention Checklist is canonical and practical.
- [x] Weekly Issue #9 concerns are part of the normal agent review path.
- [x] Generic Retrospective Period bootstrap/profile helper exists.
- [x] Thematic bootstrap references canonical planning authority rather than duplicated scope.
- [x] Quality distinguishes deterministic, agent semantic and agent visual review.
- [x] Only small structural genericity tests are required pre-merge.
- [x] Immutable Raw provenance and exact Publication Preview/Freeze/Release byte authority remain intact.
- [x] Normal Human Gate count remains exactly two.
- [x] W33/SP001 remain unstarted.
- [x] Whole-candidate re-audit finds no blocking non-deferred contradiction against acceptance priorities 1–5.
- [x] Semantic implementation head `1d6e37f48cd24ce96ef7970df0e70697e546f2e3` passed all five required cross-regression families.

The exit condition is satisfied once the final synchronized config/docs/test head itself is 5/5 CI-green.

---

## 19. Rollout after approval

After explicit Human approval:

1. merge PR #310 to current `main`;
2. treat merged `main` as the new production source of truth;
3. run W33 as first Weekly production validation;
4. run SP001 as first Thematic production validation;
5. classify actual findings and repair only the narrowest correct layer;
6. run W34 and SP002/SP003 as second-round generalization validation;
7. stabilize/consolidate docs and retire superseded legacy hot-path machinery only after production evidence supports it.

A future Foundations volume may begin under the same Thematic production principles, using the living Foundations series plan as outer guidance.

---

## 20. References

Primary current authorities/supporting evidence:

- `AGENTS.md`
- `docs/special-session-bootstrap.md`
- `docs/survey-production-core-v2-authority.md`
- `docs/checkpoints/survey-production-core-v2-worklog.md`
- `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md`
- `docs/survey-production-core-v2-wu012-preapproval-closure.md`
- `docs/survey-production-core-v2-issue-prevention-checklist.md`
- `docs/survey-production-core-v2-historical-invariants.md`
- `docs/survey-production-core-v2-historical-production-deep-audit.md`
- `docs/thematic-special-backlog.md`
- `docs/generative-ai-foundations-special-series.md`
- `docs/half-year-retrospective-specials.md`
- `docs/annual-retrospective-specials.md`
- historical Human Review Issues recorded by the invariant/deep-audit corpus.

Repository reality and the authority index control if later evidence requires another correction.
