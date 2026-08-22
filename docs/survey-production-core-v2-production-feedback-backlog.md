# Survey Production Core v2 — Post-Merge Production Feedback Backlog

Status: `COLLECTING / IMPLEMENTATION DEFERRED UNTIL W33 + SP001 REVIEW`  
Established: 2026-08-23 JST  
Working branch: `refactor/survey-production-core-v2`

## Purpose

This document records operational improvements discovered while running the first real Core v2 production editions after merge. It is intentionally a **feedback backlog**, not an instruction to modify the currently running W33/SP001 production sessions in place.

The working rule during the first verification editions is:

```text
observe real production behavior
-> preserve execution records and generated artifacts
-> record improvement candidates here
-> do not repeatedly patch Core v2 while the verification editions are still running
-> review W33 and SP001 together
-> classify common vs Profile/edition-local issues
-> implement the resulting improvement set in one deliberate maintenance pass
```

This keeps the verification signal interpretable: we should be able to distinguish how the merged Core v2 actually behaved from how it behaved after ad-hoc repairs made mid-edition.

## Feedback item PFB-001 — Use one self-contained Grok task file in Google Drive

Status: `ACCEPTED DIRECTION / NOT YET IMPLEMENTED`

### Observation

During real W33/SP001 operation, splitting a Grok run across repository-side `grok-instruction.md`, repository-side `grok-prompt.md`, and a separate Google Drive result location creates unnecessary operator complexity.

The Human/Grok boundary becomes simpler if the complete Grok request is represented by **one self-contained file in Google Drive** and the returned result is written next to it.

The current distinction between an `instruction` file and a separate `prompt` file may not provide enough operational value to justify two files.

### Improvement direction

Prefer one run-specific Markdown file that contains everything Grok needs to execute the X Source Intake task, including:

- role / operating constraints;
- research purpose;
- research questions;
- coverage focus;
- time scope;
- evidence boundary;
- required output structure;
- exact result destination / filename policy.

The final filename can be chosen during implementation; examples include `grok-task.md` or retaining `grok-instruction.md` with the prompt content folded into it. A separate `grok-prompt.md` should **not** be required unless later evidence shows that keeping two files materially improves the workflow.

Preferred Drive layout:

```text
Grok_X_SourseIntake/
  <category>/
    <edition>/
      <run-id>/
        <grok-task-file>.md
        <result>.md
```

ChatGPT should create the run folder and write the self-contained task file there before handing control to the Human/Grok boundary.

### Provenance requirement

Google Drive is the Human/Grok operational workspace, not the authoritative replacement for repository provenance.

The later implementation should preserve the existing Core v2 guarantees:

- repository-owned manifest records run identity and logical Drive location;
- the exact self-contained Grok task bytes are hash-bound;
- repository provenance clearly identifies the exact task bytes that Grok was instructed to read;
- returned result bytes are imported into repository Raw storage and hash-bound;
- each completed result receives `DISCOVERY_RECORDED` or `NO_MATERIAL_DISCOVERY` disposition;
- Grok/X remains Discovery/community-signal input rather than final technical Evidence authority.

The implementation should avoid introducing Drive credentials or account-specific folder IDs into the public repository.

### Scope

This applies uniformly to:

- Weekly;
- Retrospective Special when X is required;
- standalone Thematic Special when X is required;
- Generative AI Foundations volumes when X is required.

### Deferred implementation

Do **not** modify the currently running W33 or SP001 flows solely to introduce this change. Preserve their actual execution records as evidence of the merged behavior.

After W33 and SP001 reach their intended review boundary, evaluate this item together with any additional production findings and implement the resulting improvement set as a batch.

## Feedback item PFB-002 — Human passes the exact Drive task-file path to Grok; do not search for a Grok connector

Status: `ACCEPTED DIRECTION / NOT YET IMPLEMENTED`

### Observation

During real W33/SP001 operation, ChatGPT attempted to look for a Grok connector/integration even though the intended operating model is simpler: Grok is invoked outside ChatGPT by the Human, using a prepared Google Drive file as the handoff object.

Connector discovery adds unnecessary work and can make Source Intake look like an integration/debugging task instead of a survey-production task.

### Improvement direction

Treat Human-mediated **Drive task-file path handoff** as the normal and deliberate Grok invocation boundary unless the Human explicitly changes that policy in the future.

The responsibility split should be:

```text
ChatGPT
  -> decides the Grok/X research task
  -> prepares one self-contained Grok task Markdown
  -> provisions the Google Drive run folder
  -> writes the task file into that folder
  -> tells the Human the exact Google Drive path/reference to that task file

Human
  -> gives Grok that exact Google Drive task-file path/reference
  -> does not need to copy/paste the task contents
  -> does not need to pass the run-folder path as the primary instruction

Grok
  -> opens the indicated task file
  -> follows the complete instructions in that file
  -> performs the requested X research
  -> writes the result to the location/filename specified by that task file

ChatGPT
  -> reads the returned Drive result
  -> imports exact bytes into repository Raw
  -> evaluates/dispositions the result
  -> resumes production automatically
```

ChatGPT should **not** search for, install, discover, or attempt to configure a Grok connector merely because a Grok/X run is required. The absence of such a connector is not an error, missing dependency, Exception Gate, or reason to debug the production environment.

The Human handoff should also not be described as manually passing instruction/prompt text or merely giving Grok a folder path. The intended Human action is specifically to communicate the already-prepared **Google Drive task-file path/reference**.

If a future Human instruction explicitly introduces an automated Grok integration, that may be reviewed as a separate improvement. Until then, Human-mediated Drive task-file handoff is the expected architecture.

### Relationship to stop discipline

The only expected interruption is the practical Human step after the exact Grok task file is ready in Drive.

ChatGPT should present that task-file path directly, without first spending time looking for automation/integration options and without asking for unrelated confirmation. Once the result appears at the instructed Drive location, ChatGPT resumes toward the requested Human Gate without an additional routine approval step.

### Relationship to PFB-001

PFB-001 and PFB-002 should be implemented together where practical:

```text
one self-contained Grok task file in Drive
+
Human gives Grok that exact file path/reference
+
Grok reads that file and writes the instructed result
+
ChatGPT owns everything before and after that file-path handoff
```

This removes unnecessary duplication between `instruction` and `prompt`, minimizes Human handling, and keeps the Grok boundary easy to audit.

### Deferred implementation

Do **not** alter the currently running W33/SP001 sessions solely to enforce this new policy. Their execution logs should preserve the merged Core v2 behavior.

When W33 and SP001 are reviewed together, use those records to determine the exact documentation/bootstrap/schema/tool changes needed to make the single-file Drive handoff the unambiguous default.

## Feedback item PFB-003 — Require a concluding synthesis in every Weekly and Special

Status: `ACCEPTED DIRECTION / NOT YET IMPLEMENTED`

### Observation

Human review of both the first Core-v2 Weekly and Special verification editions required the same editorial correction: add a final **総括** section.

Because this requirement applies across edition types rather than to one issue/topic, relying on Human review to request it every time is a recurring-flow defect. The production guidance and review flow should make the conclusion an expected publication component.

### Improvement direction

Every reader-facing Weekly and Special should contain a final substantive section that synthesizes the edition as a whole. The default Japanese heading should be `総括` unless an edition-specific publication guide deliberately specifies an equivalent heading.

The synthesis must do more than repeat the table of contents or individual story/section summaries. It should answer, at the appropriate scale for the edition:

- what changed or what was established across the edition;
- which developments/arguments matter most when viewed together;
- what larger technical or ecosystem direction can reasonably be inferred;
- what remains uncertain, unresolved, or worth watching next.

For Weekly, the synthesis should connect the week's otherwise separate developments into a concise overall reading of the week.

For Special, the synthesis should close the research question/period/theme by integrating the preceding chapters into a higher-level conclusion rather than merely recapping them.

The `総括` should be the last **substantive reader-facing editorial section**. Bibliography, references, colophon, appendices, or other non-editorial back matter may follow when required by the publication format.

### Flow/check requirement

Later implementation should add an explicit editorial expectation and a pre-publication check so that omission is caught before Human review. This should be owned by the narrowest appropriate layer:

- Profile/publication guidance defines the required concluding synthesis;
- ChatGPT editorial review checks that it actually synthesizes rather than mechanically repeats;
- a deterministic check may verify presence/order only where the document structure makes that reliable, but must not pretend to validate synthesis quality.

This applies to all Weekly and Special variants, including Retrospective Period, standalone Thematic, and guided series volumes.

### Deferred implementation

Do not patch W33/SP001 Core mechanics solely for this feedback item while their verification records are still being collected. Preserve the Human correction in their execution records, then implement the generic prevention rule in the consolidated maintenance pass.

## Feedback item PFB-004 — Weekly must always publish an explicit community-movement view informed by Grok/X

Status: `ACCEPTED DIRECTION / NOT YET IMPLEMENTED`

### Observation

The merged Core v2 correctly made Grok/X collection mandatory for Weekly, but real W33 production showed that **mandatory collection does not guarantee meaningful editorial use**. Grok results can be imported, dispositioned, and technically satisfy Source Intake while still being largely ignored in the reader-facing Weekly.

That defeats a primary reason for adding X/Grok to Weekly: the Weekly should capture not only official releases but also what the technical community is actually testing, adopting, reproducing, questioning, integrating, or reacting to during the week.

### Improvement direction

Every Weekly must include an explicit reader-facing **コミュニティの動き** component informed by the completed Grok/X intake for that issue.

This is not merely another source-count obligation. Weekly editorial work must inspect the Grok/X result and deliberately synthesize material community signals such as:

- independent testing/reproduction and discrepancies from vendor claims;
- adoption or rapid integration into tools/workflows;
- local/open-weight inference activity;
- implementation discoveries, limitations, regressions, or workarounds;
- notable technical debate or counter-signal;
- unusual momentum around a model, framework, benchmark, modality, or serving stack;
- community discoveries that lead to authoritative primary-source follow-up.

Where a community signal materially belongs inside a main Weekly story, it may and should also be integrated there. The dedicated community component exists to ensure that the week's community layer is never silently discarded simply because the main stories can be written from official sources alone.

### Quiet-week behavior

The component must not disappear when X is quiet.

If the required Grok/X run finds no sufficiently material community movement, the Weekly should still include the community component and state, concisely and accurately, that no major material movement was identified, together with the relevant scan scope or noteworthy low-level observations where useful.

This makes `no material community movement` an explicit editorial finding rather than an invisible absence.

### Evidence boundary

Grok/X remains Discovery/community-signal authority, not final technical Evidence authority.

Any technical fact promoted into a main claim still requires appropriate authoritative verification. However, this Evidence boundary must not be misused as a reason to suppress community observations entirely. The correct flow is:

```text
Grok/X community observation
-> editorial relevance judgment
-> primary-source/authoritative gap fill when a technical claim requires it
-> main-story integration and/or コミュニティの動き synthesis
```

### Flow/check requirement

Later implementation should strengthen Weekly production from **collection completeness** to **editorial disposition completeness**:

- Weekly cannot complete editorial review without explicitly accounting for the completed Grok/X result;
- the publication structure includes a `コミュニティの動き` component every issue;
- material Grok observations must either be reflected in the reader-facing edition or carry an explicit reason for exclusion;
- absence of material signals is represented as a reader-facing quiet-week finding rather than silently dropping the component;
- ChatGPT editorial review evaluates whether Grok/X was genuinely used rather than only technically imported.

A deterministic validator may check required structural/accounting fields, but materiality and whether the community synthesis is editorially adequate remain ChatGPT review responsibilities.

### Scope

This requirement is **Weekly-specific and mandatory every issue**.

Specials continue to use X only when their Profile/research question marks it `REQUIRED`; PFB-004 does not force a community section into every Special. When a Special does use X, its results should still receive substantive editorial disposition under the existing X Source Intake principles.

### Deferred implementation

Do not alter the running W33/SP001 Core implementation solely for this item. Use W33's actual execution record and generated artifacts as the first regression example when implementing the consolidated improvement set.

## Additional feedback items

Add later W33/SP001 findings below this section before starting the next maintenance pass. Each item should record:

- what was observed in real production;
- whether it occurred in W33, SP001, or both;
- impact on editorial quality, autonomy, operator burden, provenance, or reliability;
- whether it is edition-local, Profile-specific, or generic Core behavior;
- proposed direction without prematurely committing to a particular implementation;
- whether a safe immediate workaround existed;
- evidence pointers to the production execution record / generated artifacts when available.

Implementation should begin only after the first verification-edition feedback set is reviewed as a whole.
