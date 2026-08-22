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
