# Survey Production Core v2 — ChatGPT-first pre-approval re-audit

Status: `AUTHORITATIVE PRE-APPROVAL RE-AUDIT / supersedes improvement-plan §§16–18 where conflicting`  
Established: 2026-08-22 JST  
Working branch: `refactor/survey-production-core-v2`  
Scope: WU-001 through WU-011 plus the first WU-012 audit amendment

## 1. Corrected premise

The previous pre-approval audit implicitly treated Survey Production Core v2 too much like an external workflow engine whose purpose was to make each editorial/research decision machine-provable.

That premise is incorrect for this repository.

The intended production operator is:

> **ChatGPT, using the current upper-tier reasoning model available in the product, reads repository-owned guidance/state, performs the research and editorial reasoning itself, and uses scripts/workflows as supporting tools for repetitive, deterministic, provenance-sensitive, or expensive mechanical work.**

The objective of Core v2 is therefore not to move editorial intelligence out of ChatGPT and into validators or GitHub Actions. It is to make ChatGPT's work:

- easier to start and resume from a short user request;
- less dependent on conversation history;
- consistent across Weekly and Special editions;
- explicit about research scope, Evidence, materiality and unresolved limitations;
- resistant to recurrence of defects already found through Human Review Issues;
- efficient by automating deterministic mechanics rather than editorial judgment;
- reproducible at publication/release boundaries where byte identity matters.

The canonical precedent is already visible in `AGENTS.md` and `docs/special-session-bootstrap.md`: the user supplies the target and stopping Human Gate; the agent reads current `main`, reconstructs state, performs non-Human-Gate work autonomously, and asks only when an actual Human/Exception decision is required.

## 2. Tooling boundary under the corrected premise

### 2.1 ChatGPT-owned work

ChatGPT is expected to reason about and perform:

- Source Intake strategy and search expansion;
- whether coverage is adequate for the edition's research question;
- source quality and primary-source gap filling;
- Screening decisions where semantic judgment is needed;
- Evidence interpretation and limitations;
- materiality and completeness assessment;
- Candidate Selection;
- Architecture;
- article drafting and synthesis;
- historical/technical interpretation;
- `why this week` / `why this Special` reasoning;
- semantic editorial review;
- visual/editorial assessment of the rendered publication;
- classification of new findings and whether they generalize.

These decisions should leave concise repository-backed records where they are needed for resumption, review, or future defect prevention. They do not need to be converted into deterministic algorithms merely because a structured record exists.

### 2.2 Tool-owned work

Scripts/workflows are appropriate for work where deterministic execution is superior to repeated LLM reasoning, including:

- date/cutoff/window calculation;
- bootstrap path/branch naming;
- schema/format validation;
- Raw-source hashing and immutable provenance;
- exact ID/path/URL/reference integrity;
- duplicate/missing record detection;
- deterministic bibliography/render assembly;
- TeX/PDF build/preflight;
- targeted checks such as period-label consistency where false positives can be bounded;
- exact Publication Preview/PDF/Freeze/Release byte identity;
- CI/regression checks for deterministic historical defect families;
- GitHub Release side effects and exact-byte reconciliation.

A tool may prepare structured inputs for ChatGPT or validate a ChatGPT-produced artifact. It should not attempt to replace open-ended editorial judgment with ceremonial machine state.

## 3. Re-audit of WU-001 through WU-011

| Work unit | Corrected assessment | Action |
|---|---|---|
| WU-001 / WU-001A | **Strong and aligned.** Core/Profile/Publication/Series ownership prevents one edition's semantics from contaminating another. | Retain. Add the explicit ChatGPT-first operator boundary to the authority set. |
| WU-002 | **Mostly aligned.** Two Human Gates, separate temporal/research profiles, and repository-owned contracts are useful guidance. Contract hashes are provenance aids, not substitutes for agent reasoning. | Retain with lighter interpretation of machine authority. |
| WU-003 / 003B / 003C | **One of the strongest parts of the program.** Historical Issues were converted into reusable knowledge. | Retain. Treat the invariant catalog as a required agent review playbook as well as a regression source. |
| WU-004 / 004B | **Aligned in research architecture.** Weekly/Thematic first slices and Profile separation are useful. | Retain; do not require synthetic proof of every future topic before real production. |
| WU-005 | **Useful state model, somewhat over-bound to one executable implementation.** Profile and lifecycle state help cross-session resume, but edition-wide implementation pinning is stricter than necessary for an agent-operated process. | Change implementation provenance to per-checkpoint/per-action records plus an explicit controlled toolchain-upgrade path. |
| WU-006 | **Aligned.** Discovery/Screening schemas and Raw provenance are useful tools around ChatGPT research. | Retain. Do not attempt to machine-prove that all possible searches were performed. |
| WU-007 | **Aligned when Completeness is treated as a reasoned editorial record.** Materiality and subject/entity binding are valuable. The earlier audit incorrectly treated self-authored Completeness as invalid merely because it is not externally proved. | Keep structured Completeness, require meaningful rationale and unresolved limitations, but let ChatGPT decide adequacy. Deterministic validation checks structure/traceability, not research truth. |
| WU-008 / 008A | **Strongly aligned.** Matrix, internal Selection, Architecture and bounded review summaries organize reasoning without adding a Human Gate. | Retain. |
| WU-009 | **Strongly aligned.** Structured drafting/Evidence references reduce hallucination and make revisions auditable. | Retain, while avoiding validators for nuanced prose that are better handled by an agent checklist. |
| WU-010 / 010R | **Directionally useful but control-plane over-engineered.** Resumability and explicit approvals are valuable; mandatory Action Spec/Handoff/Result/Validation-Attestation machinery for every local stage models ChatGPT as an external worker behind a workflow engine. | Simplify local-stage orchestration. Preserve compact State/checkpoints, Human approvals, exact critical hashes and release-side controls. |
| WU-011 | **Publication/release hardening is valuable; local-stage control wiring is heavier than necessary.** Exact-byte Candidate→Preview→Freeze→Release and Release reconciliation are appropriate. W33/SP001 bootstrap that duplicates editorial scope into a Pilot registry is too authoritative. | Retain publication/release byte authority. Simplify production-control path and make bootstrap resolve editorial scope from canonical guides/backlogs rather than duplicated Pilot literals. |

## 4. Five requested acceptance questions under the corrected premise

### 4.1 Weekly production viability — `LIKELY YES, after agent-first simplification`

The research/editorial path is adequate in principle:

- arbitrary completed Weekly IDs are derivable from the configured cutoff calendar;
- Weekly scope, carry-over, current significance and Late Breaking can be represented without W33-specific Core logic;
- Raw provenance, Evidence, subject binding, Materiality, Selection and Architecture provide useful structure for ChatGPT reasoning;
- Issue #9 lessons are already distilled into the historical invariant catalog.

The main remaining risks are operational, not missing AI capability:

1. the current local-stage control stack adds avoidable ceremony to every ChatGPT step;
2. Weekly Issue #9 concerns need to be promoted into a mandatory **agent editorial checklist**, not necessarily a semantic validator;
3. Source Intake completeness guidance should require ChatGPT to explain what it searched, what remains uncertain and why it considers the issue ready, but should not pretend that completeness is externally machine-provable.

A weak news week remains valid. No fixed source/story/page quota is needed.

### 4.2 Special production viability — `LIKELY YES for standalone Thematic; small helper gap for Period; Foundations is already viable as a guided series`

Standalone Thematic Specials are compatible with the Core design. SP-001 through SP-003 should be driven primarily by `docs/thematic-special-backlog.md` plus the generic Thematic guide, not by duplicated hard-coded scope in a Pilot registry.

Retrospective Period support needs one modest deterministic convenience: a generic bounded-period profile/bootstrap helper so ChatGPT does not rebuild month/half/year timing and paths by hand. This is a tooling-efficiency gap, not evidence that the editorial model is incomplete.

The previous audit overstated the Foundations gap. `docs/generative-ai-foundations-special-series.md` is already a substantial living Series Research Layer in the sense that matters for an agent-operated process: it defines the lineage graph, evolving volume architecture, dependencies, merge/split/resequence rules, historical-attribution rules, open questions and dated frontier snapshots. A machine-readable graph/database is not a prerequisite for beginning the series.

If repeated cross-volume Evidence lookup later becomes expensive or inconsistent, add a lightweight shared source/evidence index then. Do not implement a full Series state engine pre-emptively.

### 4.3 Generality beyond W33/W34/SP-001–003 — `YES at the architecture level; prove structurally, then learn from real editions`

The relevant test is not whether every hypothetical future edition has a synthetic end-to-end fixture. It is whether:

- generic code branches on Profile semantics rather than named edition IDs;
- a Weekly resolver accepts arbitrary valid completed issue IDs;
- Period bootstrap accepts arbitrary bounded periods;
- Thematic scope comes from a supplied research question/guide rather than TS-001-specific code;
- publication logic depends on Publication Profile, not one frozen edition;
- future ChatGPT sessions can read current policy and construct a new edition without editing Core code.

A small set of structural tests for arbitrary Weekly/Period/Thematic inputs is useful. Exhaustive W35+/ISO-boundary/TS-002/TS-003/unlisted-theme/Series simulation is not required before merge. Real W33/SP001 then W34/SP002/SP003 work remains the better generalization test.

### 4.4 Recurrence prevention for existing Human Review Issues — `YES if the invariant corpus becomes an explicit agent review contract`

The earlier audit incorrectly equated recurrence prevention with executable validators.

The correct defense model has three layers:

1. **Deterministic guard** — for defects with crisp machine semantics: hashes, IDs, paths, URLs, duplicate records, period labels in designated fields, missing refs, build errors, exact PDF bytes.
2. **ChatGPT editorial/research checklist** — for semantic defects such as `why this week`, misleading source interpretation, source-specificity, synthesis quality, Watchlist wording, retrospective attribution, one substantive Late Breaking home, and whether an omission is material.
3. **ChatGPT visual review checklist at Publication Preview** — for page balance, orphaned card tails, isolated boxes, TOC density, visual hierarchy and similar layout judgments.

The historical invariant catalog should be converted into a concise stage/profile-aware **Issue Prevention Checklist** that every production session is instructed to read/apply. The checklist records PASS/FINDING with short evidence. A PASS is a reasoned agent review result unless the item explicitly names a deterministic validator.

No third normal Human Gate is added.

### 4.5 Excessive gates / excessive verification — `CURRENT LOCAL CONTROL PLANE IS TOO STRICT`

The two Human Gates remain appropriate:

1. Architecture Review;
2. exact-byte Publication Preview.

However, the current v2 orchestration creates a machine-control chain around each local stage:

```text
Action Spec
-> Handoff Request
-> Handoff
-> Action Result
-> Validation Attestation
-> Production State transition
```

For an external workflow engine this is defensible. For a ChatGPT-operated repository it creates repeated serialization, hashing and dispatch work around decisions the same agent is already making and recording in the stage artifacts.

The desired local-stage model is closer to:

```text
ChatGPT reads Profile + State + applicable guide
-> performs research/editorial stage
-> writes canonical stage artifact(s)
-> runs deterministic validators that actually apply
-> records one compact checkpoint/result in Production State or a checkpoint record
-> proceeds to the next stage until a Human/Exception Gate
```

Keep richer request/receipt authority only where there is a meaningful external side effect or asynchronous execution boundary, especially build artifacts and Release.

## 5. Implementation provenance correction

The State-wide immutable `implementation.repository_commit_sha` is too strong for the intended production process.

Historical production frequently discovers a reusable pipeline defect during review, repairs the generic tool on `main`, and continues the same edition using the improved tool. That is a desirable feedback loop.

The revised rule should be:

- each checkpoint/action records the repository/tool implementation commit that produced or validated it;
- previously accepted artifacts retain their exact byte/provenance identity;
- a later stage may use a newer reviewed `main` implementation;
- when a tool/schema change materially affects an existing accepted artifact, ChatGPT must revalidate/migrate the affected boundary before continuing;
- if compatibility cannot be determined without editorial judgment, use an Exception Gate;
- publication approval/freeze/release remain exact-byte bound regardless of tool upgrades.

This provides stronger historical provenance while avoiding edition-wide toolchain lock-in.

## 6. Corrected disposition of the first WU-012 findings

The first WU-012 audit was based on the wrong machine-first premise. Its findings remain useful evidence but their remediation language must be reclassified as follows:

| Finding | Corrected disposition |
|---|---|
| AUD-027 | Retain the coverage concern, but solve it with an agent research-completeness record/checklist; do not require external proof of every search or non-empty Evidence for every legitimate negative coverage result. |
| AUD-028 | Retain. Solve primarily with a Weekly agent editorial checklist plus deterministic checks only for crisp cases. |
| AUD-029 | Reframe. The defect is not that semantic PASS is agent-authored; the defect is failure to distinguish deterministic validation from reasoned/visual agent review and the over-broad universal check set. |
| AUD-030 | Retain as a small tooling-efficiency gap: generic Period bootstrap/profile helper. |
| AUD-031 | Defer machine Series Layer implementation. Existing Foundations living design memo is sufficient authority for initial series work; add tooling only when real repeated work justifies it. |
| AUD-032 | Reframe. Do not expand duplicated SP001 registry literals; make bootstrap point to authoritative TS-001 planning scope instead. |
| AUD-033 | Reduce. Require structural genericity tests and absence of named-edition branches, not exhaustive synthetic future-edition fixtures. |
| AUD-034 | Retain but change Guard taxonomy to include ChatGPT research/editorial/visual review ownership explicitly. |

## 7. New blocking findings from the corrected premise

### A. Agent/operator model is not explicit enough in Core v2 authority

Although legacy `AGENTS.md`/Special bootstrap encode the right behavior, Core v2 authority increasingly describes handlers/workflows as if they were the production operator. The new canonical Core docs must state that ChatGPT is the reasoning/editorial operator and tools are supporting mechanisms.

### B. Local-stage orchestration is over-serialized

Mandatory Action Spec/Handoff/Result/Attestation records for each local stage add cost without proportionate safety when canonical stage artifacts and one checkpoint record already preserve the important decisions.

### C. Edition-wide implementation pinning impedes the intended improvement loop

The pipeline needs per-checkpoint implementation provenance and a controlled upgrade/revalidation path, not a requirement that every later stage execute the initialization commit's implementation roots.

These are pre-merge architecture corrections because they directly affect everyday production efficiency and the ability to apply future Issue-driven generic fixes.

## 8. Revised WU-012 — agent-first simplification and guidance hardening

WU-012 is narrowed to the following work.

### WU-012A — establish the ChatGPT-first operating contract

- make the operator/tool boundary explicit in the improvement plan, authority index, bootstrap and future `AGENTS.md`;
- define which decisions are ChatGPT reasoning, deterministic tool checks, Human Gates and Exception Gates;
- ensure a production session can start from target + requested gate without low-level user instructions.

### WU-012B — simplify local orchestration

- retain one authoritative Production State and canonical stage outputs;
- replace mandatory local Action Spec/Handoff Request/Handoff/Action Result/Validation Attestation chains with the minimum checkpoint record necessary for resumption/provenance;
- retain richer request/receipt records for external/irreversible operations where they provide real value;
- keep exactly two normal Human Gate approval records.

### WU-012C — allow controlled toolchain evolution during an edition

- move implementation provenance to checkpoint/action records;
- permit a later stage to use newer reviewed `main` tooling;
- require targeted revalidation/migration only when the changed tool affects an accepted artifact's contract;
- fail to Exception Gate only when safe compatibility cannot be determined.

### WU-012D — convert historical Issues into an agent-first prevention playbook

Create a stage/profile-aware Issue Prevention Checklist mapping each material historical invariant to one of:

```text
DETERMINISTIC_TOOL_CHECK
CHATGPT_RESEARCH_REVIEW
CHATGPT_EDITORIAL_REVIEW
CHATGPT_VISUAL_REVIEW
HUMAN_ARCHITECTURE_REVIEW
HUMAN_PUBLICATION_PREVIEW
LEGACY_ONLY / NOT_APPLICABLE
```

The checklist must tell the agent what to inspect and what evidence to record. Do not create a validator solely because an Issue once existed.

### WU-012E — small generic bootstrap/profile gaps only

- add a generic Retrospective Period bootstrap/profile helper;
- make Thematic Pilot/bootstrap entries reference canonical backlog/series planning authority instead of duplicating detailed editorial scope;
- keep only small structural genericity tests for arbitrary Weekly/Period/Thematic inputs.

Do **not** implement a machine Series engine before actual Foundations production demonstrates a need.

### WU-012F — quality review tiers

Replace the concept of one universal all-machine quality list with three explicit kinds:

```text
DETERMINISTIC
AGENT_SEMANTIC
AGENT_VISUAL
```

Only deterministic rows require executable validator evidence. Agent semantic/visual rows are explicit reasoned review records tied to the reviewed source/PDF revision. Applicability is Profile/Publication-aware.

## 9. Revised pre-merge exit condition

Before PR #310 returns to Human full-candidate review:

1. the ChatGPT-first operator model is explicit and canonical;
2. local-stage orchestration no longer requires workflow-engine ceremony that does not improve resumption/provenance;
3. the same edition can adopt a newer reviewed tool implementation through controlled checkpoint revalidation rather than being globally locked to the initialization commit;
4. historical Issue prevention is discoverable as an agent/tool/Human checklist with deterministic automation only where appropriate;
5. generic Retrospective Period bootstrap exists;
6. Thematic/Foundations scope authority is not duplicated into brittle Pilot configuration;
7. quality review distinguishes deterministic, semantic-agent and visual-agent checks;
8. the normal Human Gate count remains exactly two;
9. exact-byte publication/release authority and immutable Raw provenance remain intact;
10. W33/SP001 remain unstarted until this corrected candidate is reviewed and merged.

The goal is not to maximize the number of schemas, validators or workflow states. The goal is to let a capable ChatGPT compile editions accurately, efficiently and reproducibly while making prior Human Review lessons difficult to forget.