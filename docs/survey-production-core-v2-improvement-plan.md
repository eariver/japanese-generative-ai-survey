# Survey Production Core v2 — Compilation System Improvement Plan

Status: `ACTIVE CONSOLIDATED PLAN / ChatGPT-first`  
Established: 2026-08-22 JST  
Consolidated after pre-approval re-audit: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Production source of truth until merge: current `main`  
Detailed pre-approval re-audit: `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md`

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

Replace one universal all-machine PASS list with three kinds:

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

The architecture is expected to support W35 and later Weekly issues because:

- issue/cutoff derivation is generic;
- current significance/carry-over/Late Breaking are Profile semantics, not W33 Core branches;
- research/editorial judgment remains adaptable ChatGPT work;
- deterministic provenance/identity tools are issue-agnostic.

Pre-merge work still required:

- make Issue #9 part of the mandatory Weekly agent editorial checklist;
- simplify local orchestration so routine Weekly compilation is not dominated by control-file production;
- support controlled adoption of generic tool fixes during an edition;
- retain small structural tests that arbitrary completed Weekly IDs resolve correctly.

W33 remains the first real production validation; W34 validates the first repair set on a different week.

---

## 13. Special viability

### 13.1 Retrospective Period

Add one lightweight generic bounded-Period profile/bootstrap helper supporting:

- month;
- half-year;
- year;
- explicit custom bounded period.

The helper handles deterministic dates/paths/profile construction and points ChatGPT at applicable period guidance. It does not encode the edition's stories, taxonomy or synthesis conclusions.

### 13.2 Standalone Thematic

Thematic scope comes from an explicit research question and canonical planning guide/backlog.

SP-001/TS-001, SP-002/TS-002 and SP-003/TS-003 must not require topic-specific Core branches.

The Pilot/bootstrap layer should identify the canonical planning authority rather than copy a simplified editorial scope into another registry.

### 13.3 Generative AI Foundations

Use `docs/generative-ai-foundations-special-series.md` as the living outer architecture. Each volume runs normal Thematic production while the series memo evolves from discoveries.

Do not implement a machine Series engine before actual production shows that a shared source/evidence index would reduce repeated work or drift.

---

## 14. Generality strategy

Pre-merge genericity should be demonstrated structurally, not by simulating every future edition.

Useful small tests include:

- arbitrary valid completed Weekly ID;
- arbitrary bounded Period spec;
- arbitrary Thematic question/spec;
- no production code branching on W33/SP001/TS-001 identifiers;
- Publication Profile behavior selected by profile, not named edition.

Real production remains the stronger test:

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
- **WU-005:** Profile/State — retain, but correct edition-wide implementation pinning.
- **WU-006:** Discovery/Screening — retain as tools around ChatGPT research.
- **WU-007:** Evidence/Materiality/Completeness — retain; Completeness is a structured reasoned judgment.
- **WU-008/008A:** Matrix/Selection/Architecture — retain.
- **WU-009:** structured Draft/Synthesis — retain.
- **WU-010/010R:** orchestration hardening — historical defect lessons retained; local control-plane implementation simplified in WU-012.
- **WU-011:** exact publication/release/bootstrap hardening — publication/release authority retained; local stage/Pilot scope controls simplified in WU-012.

Historical detail remains available in the worklog, authority index, audit documents and Git history.

---

## 16. WU-012 — ChatGPT-first simplification and guidance hardening

WU-012 is the current pre-merge work unit.

### WU-012A — ChatGPT-first operating contract

- make the operator/tool boundary explicit in canonical docs/bootstrap/future `AGENTS.md`;
- ensure target + stopping gate remains sufficient user input;
- classify stage work as agent reasoning, deterministic helper, Human Gate, or Exception Gate.

### WU-012B — simplify local orchestration

- retain one Production State and canonical stage outputs;
- replace mandatory local Action Spec/Handoff Request/Handoff/Result/Attestation chains with the minimum checkpoint record needed for resume/provenance;
- retain richer control records only for external/irreversible operations where they have a distinct safety purpose;
- keep exactly two Human approval records.

### WU-012C — controlled toolchain evolution

- record implementation/tool commit per checkpoint/action;
- allow later stages to use newer reviewed `main` tooling;
- require targeted revalidation/migration only when changed contracts affect accepted artifacts;
- Exception Gate only for unresolved compatibility decisions.

### WU-012D — Issue Prevention Checklist

Create a short stage/profile-aware checklist derived from historical invariants and Issues, mapping each recurring defect to deterministic tool, ChatGPT research/editorial/visual review, Human review or legacy-only handling.

### WU-012E — small generic bootstrap/profile gaps

- add generic bounded-Period bootstrap/profile helper;
- make Thematic Pilot/bootstrap reference canonical backlog/series planning authority rather than duplicate detailed scope;
- add only small structural genericity tests;
- no pre-emptive machine Series engine.

### WU-012F — quality-review tiers

Implement `DETERMINISTIC / AGENT_SEMANTIC / AGENT_VISUAL` applicability and review records. Only deterministic items require executable validator proof.

---

## 17. WU-012 finding status

Current findings:

- AUD-027 `OPEN` — substantive ChatGPT completeness-review guidance;
- AUD-028 `OPEN` — Weekly Issue #9 agent editorial review;
- AUD-029 `OPEN` — deterministic vs agent quality tiers/applicability;
- AUD-030 `OPEN` — lightweight Period bootstrap helper;
- AUD-031 `DEFERRED` — full machine Series engine is premature;
- AUD-032 `OPEN` — SP001 bootstrap duplicates/narrows TS-001 scope;
- AUD-033 `DEFERRED` — exhaustive synthetic future-edition fixtures are unnecessary;
- AUD-034 `OPEN` — Issue Prevention Checklist missing;
- AUD-035 `OPEN` — ChatGPT operator model/local-stage over-serialization;
- AUD-036 `OPEN` — edition-wide implementation commit lock-in.

No WU-012 Repair Set exists yet.

---

## 18. WU-012 exit condition

Before PR #310 returns to Human full-candidate review:

- [ ] ChatGPT-first operator model is canonical and discoverable.
- [ ] Local-stage orchestration is materially simpler while preserving resume/provenance.
- [ ] Implementation provenance is per checkpoint/action and controlled toolchain upgrades are possible.
- [ ] Historical Issue Prevention Checklist is canonical and practical.
- [ ] Weekly Issue #9 concerns are part of the normal agent review path.
- [ ] Generic Retrospective Period bootstrap/profile helper exists.
- [ ] Thematic bootstrap references canonical planning authority rather than duplicated scope.
- [ ] Quality distinguishes deterministic, agent semantic and agent visual review.
- [ ] Only small structural genericity tests are required pre-merge.
- [ ] Immutable Raw provenance and exact Publication Preview/Freeze/Release byte authority remain intact.
- [ ] Normal Human Gate count remains exactly two.
- [ ] W33/SP001 remain unstarted.
- [ ] Whole-candidate re-audit finds no blocking contradiction against acceptance priorities 1–5.

---

## 19. Rollout after approval

After corrected WU-012 is implemented, audited and explicitly approved:

1. merge PR #310 to current `main`;
2. update canonical `AGENTS.md`/bootstrap to the merged Core v2 path;
3. run W33 as first Weekly production validation;
4. run SP001 as first Thematic production validation;
5. classify actual findings and repair only the narrowest correct layer;
6. run W34 and SP002/SP003 as second-round generalization validation;
7. stabilize/consolidate docs and retire superseded hot-path machinery only after production evidence supports it.

A future Foundations volume may begin under the same Thematic production principles, using the living Foundations series plan as outer guidance.

---

## 20. References

Primary current authorities/supporting evidence:

- `AGENTS.md`
- `docs/special-session-bootstrap.md`
- `docs/survey-production-core-v2-authority.md`
- `docs/checkpoints/survey-production-core-v2-worklog.md`
- `docs/survey-production-core-v2-agent-first-reaudit-2026-08-22.md`
- `docs/survey-production-core-v2-historical-invariants.md`
- `docs/survey-production-core-v2-historical-production-deep-audit.md`
- `docs/thematic-special-backlog.md`
- `docs/generative-ai-foundations-special-series.md`
- `docs/half-year-retrospective-specials.md`
- `docs/annual-retrospective-specials.md`
- historical Human Review Issues recorded by the invariant/deep-audit corpus.

This is a working implementation guide. Repository reality and the authority index control if later evidence requires another correction.
