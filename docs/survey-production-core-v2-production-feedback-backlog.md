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

## Feedback item PFB-001 — Co-locate Grok input and output in Google Drive

Status: `ACCEPTED DIRECTION / NOT YET IMPLEMENTED`

### Observation

During real W33/SP001 operation, manual Grok transport is easier to understand when the Human/Grok working surface contains both the inputs and the returned result. The current design creates `grok-instruction.md` and `grok-prompt.md` under repository edition artifacts while Google Drive is primarily the result handoff location.

For a Human who must manually pass the generated request to Grok, this splits one Grok run across two places and makes the operational mapping less obvious than necessary.

### Improvement direction

Use each Google Drive run folder as the complete Human/Grok working surface:

```text
Grok_X_SourseIntake/
  <category>/
    <edition>/
      <run-id>/
        grok-instruction.md
        grok-prompt.md
        <result>.md
```

ChatGPT should provision the exact run folder and place the run-specific instruction and prompt there **before** asking for manual Grok transport. Grok should be instructed to read/use those files and save its final Markdown result into the same run folder.

The desired Human operation becomes:

```text
open one run folder
-> give Grok the instruction/prompt from that folder
-> Grok writes the result back to the same folder
-> ChatGPT reads the returned result and resumes automatically
```

No additional Human approval is introduced.

### Provenance requirement

Google Drive is the Human/Grok operational workspace, not the authoritative replacement for repository provenance.

The later implementation should preserve the existing Core v2 guarantees:

- repository-owned manifest records the logical Drive path and run identity;
- exact `grok-instruction.md` and `grok-prompt.md` bytes remain hash-bound;
- the Drive copies and repository-authority copies must correspond to the same intended bytes, or the design should explicitly define which copy is authoritative before the run begins;
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

The category/edition/run folder convention remains unchanged; only the operational placement of Grok input artifacts changes.

### Deferred implementation

Do **not** modify the currently running W33 or SP001 flows solely to introduce this change. Preserve their actual execution records as evidence of the merged behavior.

After W33 and SP001 reach their intended review boundary, evaluate this item together with any additional production findings and implement the resulting improvement set as a batch.

## Feedback item PFB-002 — Human owns Grok invocation; do not search for a Grok connector

Status: `ACCEPTED DIRECTION / NOT YET IMPLEMENTED`

### Observation

During real W33/SP001 operation, ChatGPT attempted to look for a Grok connector/integration even though the intended operating model is simpler: the Human will manually give Grok the prepared instruction/prompt.

Connector discovery adds unnecessary work and can make Source Intake look like an integration/debugging task instead of a survey-production task.

### Improvement direction

Treat manual Grok invocation as the normal and deliberate operating boundary unless the Human explicitly changes that policy in the future.

The responsibility split should be:

```text
ChatGPT
  -> decides the Grok/X research task
  -> prepares exact grok-instruction.md and grok-prompt.md
  -> provisions the Google Drive run folder
  -> tells the Human exactly which run folder/files are ready

Human
  -> manually gives those instructions to Grok
  -> causes Grok to write the result into the instructed Drive run folder

ChatGPT
  -> detects/reads the returned Drive result
  -> imports exact bytes into repository Raw
  -> evaluates/dispositions the result
  -> resumes production automatically
```

ChatGPT should **not** search for, install, discover, or attempt to configure a Grok connector merely because a Grok/X run is required. The absence of such a connector is not an error, missing dependency, Exception Gate, or reason to debug the production environment.

If a future Human instruction explicitly introduces an automated Grok integration, that may be reviewed as a separate improvement. Until then, manual Human transport is the expected architecture.

### Relationship to stop discipline

The only expected interruption is the practical Human transport step after the exact Grok input package is ready.

ChatGPT should present that package and Drive location directly, without first spending time looking for automation/integration options and without asking for unrelated confirmation. Once the result appears in Drive, ChatGPT resumes toward the requested Human Gate without an additional routine approval step.

### Relationship to PFB-001

PFB-001 and PFB-002 should be implemented together where practical:

```text
one Drive run folder contains Grok input + output
+
Human manually invokes Grok from that folder
+
ChatGPT owns everything before and after that manual transport boundary
```

This gives the manual Grok step a clear, stable operator interface while preserving repository-side provenance.

### Deferred implementation

Do **not** alter the currently running W33/SP001 sessions solely to enforce this new policy. Their execution logs should preserve whether connector discovery occurred under the merged Core v2 behavior.

When W33 and SP001 are reviewed together, use those records to determine the exact documentation/bootstrap/tool changes needed to make manual Human Grok transport the unambiguous default.

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
