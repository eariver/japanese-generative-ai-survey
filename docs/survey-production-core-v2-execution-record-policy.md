# Survey Production Core v2 — Edition Execution Record Policy

Status: `ACCEPTED REDESIGN DIRECTION / IMPLEMENTATION NOT STARTED`  
Established: 2026-08-23 JST  
Working branch: `refactor/survey-production-core-v2`  
Related redesign: `docs/survey-production-core-v2-redesign-plan-after-w33-sp001.md`

## 1. Purpose

Every Weekly/Special production task is normally executed in its own ChatGPT conversation. The repository therefore needs a stable, edition-local record that allows a later session or Core-maintenance review to reconstruct what actually happened without reading chat history or inferring behavior from commits alone.

W33 and SP001 showed two opposite failure modes:

- one long worklog can become stale as the lifecycle continues beyond its original stated stop;
- multiple ad-hoc checkpoint files can preserve detail but become fragmented and difficult to review as one production run.

The redesigned flow must therefore require a small, predictable execution-record tree for every edition.

Machine lifecycle/state artifacts remain authoritative for machine state. Execution records are human-readable operational provenance and must not duplicate every machine field.

## 2. Canonical location

Store edition execution records under the edition's existing source root, not in the global `docs/checkpoints/` namespace.

Target structure:

```text
sources/<issue-id>/execution/
  index.md
  sessions/
    <session-id>.md
  reviews/
    architecture-r1.md
    architecture-r2.md
    publication-r1.md
    publication-r2.md
  defects/
    <defect-id>.md
```

Examples:

```text
sources/2026-W34/execution/...
sources/SP002/execution/...
```

The exact filenames may be normalized during implementation, but the four responsibilities (`index`, `sessions`, `reviews`, `defects`) should remain distinct.

Do not create date-stamped checkpoint files directly in `docs/checkpoints/` for normal edition production after this policy is implemented.

## 3. `index.md` — one current run index per edition

`index.md` is the first file a new ChatGPT session should read after `production-state.json`.

It is a compact current-state navigation document, not a full diary.

Required fields:

- issue / edition ID;
- research profile and publication profile;
- canonical work branch;
- source-of-truth `main` commit SHA used to start the run;
- run start date/time;
- requested Human Gate / requested end state;
- current lifecycle state and current stop reason, copied only as a convenience pointer from canonical State;
- Human Gate status and links to relevant GitHub Issues/PRs;
- current accepted/rejected Publication Candidate SHA/PDF SHA when applicable;
- Grok/X applicability and latest Drive task-file path/result disposition when applicable;
- known edition-local deviations;
- known shared-Core defects encountered;
- list of session logs in chronological order;
- final disposition: `IN_PROGRESS`, `HUMAN_GATE`, `BLOCKED_CORE_DEFECT`, `TERMINATED_VALIDATION`, `COMPLETE`, or equivalent reviewed vocabulary.

### Freshness rule

The production session must update `index.md` whenever one of these changes:

- lifecycle crosses a Human Gate boundary;
- a Human Gate is rejected/approved;
- a shared-Core defect changes the ability to continue;
- a new Publication Candidate becomes the Human review target;
- the run is terminated or completed.

This avoids the stale-header problem observed in the W33 worklog.

## 4. `sessions/<session-id>.md` — actions actually performed

Create one session log per ChatGPT production conversation, or per materially separate continuation if one conversation is intentionally split into distinct execution phases.

Recommended session ID:

```text
YYYY-MM-DDTHHMM-JST-<short-purpose>.md
```

Example:

```text
2026-08-24T0830-JST-source-intake-to-architecture.md
```

A normal session log records only material production actions.

Required sections:

### Starting authority

- branch head / relevant commit SHA;
- `production-state.json` lifecycle and SHA if available;
- source-of-truth `main` SHA or integrated reviewed Core SHA;
- session objective / requested stop;
- prior session/index pointer.

### Actions actually performed

Group by meaningful stage, not by tool call.

For each stage, record:

- what research/editorial/production action was actually performed;
- significant quantitative summary where it helps interpretation (for example Discovery count, Screening decisions, Evidence status counts, selected candidates);
- material judgment and the reason for it;
- canonical artifact paths created/revised;
- commit/PR/run reference only when it materially identifies the resulting state.

### External handoff

When Grok/X is used, record only:

- exact Google Drive task-file path/reference given to the Human;
- result file path/reference returned;
- imported repository Raw path;
- result SHA/byte count or manifest identity;
- editorial disposition (`DISCOVERY_RECORDED` / `NO_MATERIAL_DISCOVERY`).

Do not duplicate the full Grok task/result contents in the session log.

### Deviations / failures

Record only failures that affected the run, for example:

- a shared-Core defect;
- a failed workflow that forced a different execution route;
- an edition-local workaround;
- authority drift or candidate invalidation;
- a deliberate restart from an earlier boundary.

For each, classify:

- `EDITION_LOCAL`
- `TRANSIENT_EXECUTION`
- `SHARED_CORE_DEFECT`

If `SHARED_CORE_DEFECT`, point to a file under `execution/defects/` and do not repair shared Core inside the production session under the redesigned responsibility rule.

### End state

- lifecycle / Human Gate status;
- exact candidate/PDF SHA if a review target exists;
- next action;
- whether the session ended normally, at manual Grok transport, at Human Gate, or because of a Core defect/termination.

## 5. How much to record

The record must be sufficient to answer:

1. What did ChatGPT actually do?
2. What material decisions were made and why?
3. Which exact artifacts became authoritative?
4. Where did Human/Grok interaction occur?
5. Did the production session encounter or modify shared Core?
6. Why did the session stop?

It should **not** be a transcript.

### Normal granularity

For a normal stage:

- 3–10 concise bullets are usually sufficient;
- include counts/paths/SHAs only where they identify an important boundary or make the result auditable;
- one paragraph of rationale is enough for a material editorial decision.

A normal session log should usually stay to a few pages of Markdown. Longer records are justified only for an actual failure/restart/review-revision sequence.

### Do not record routinely

Do not list:

- every connector/tool invocation;
- every poll of a GitHub Actions run;
- every successful command line;
- every file opened during research;
- repetitive PASS output already represented by one canonical validator/result artifact;
- internal chain-of-thought/reasoning traces;
- full Issue bodies or full external-source content already stored elsewhere.

Instead, record the outcome and point to the authoritative artifact/run/Issue.

## 6. `reviews/` — compact Human Gate revision history

Every Human Gate decision/revision gets one short Markdown record even if the full feedback lives in a GitHub Issue.

Record:

- gate (`ARCHITECTURE_REVIEW` / `PUBLICATION_PREVIEW`);
- revision number;
- reviewed candidate identity/SHA;
- Human decision (`APPROVED` / `REVISION_REQUIRED` / `TRIAL_TERMINATED`);
- GitHub Issue/comment link containing the detailed feedback;
- concise defect families / requested changes;
- earliest lifecycle boundary that must be regenerated;
- whether any request implies a shared-Core defect.

Do not duplicate the entire Human Issue text.

This makes it possible to see revision history locally without turning the repository into a second copy of GitHub discussions.

## 7. `defects/` — shared-Core observations from production

A Production session may observe but should not repair a shared-Core defect.

Each material shared-Core defect gets a short record containing:

- observed symptom;
- affected edition/profile;
- reproduction boundary/artifact;
- impact on correctness/quality/autonomy;
- whether a safe edition-local workaround exists;
- linked Core-maintenance Issue/backlog item;
- production disposition (`CONTINUE_WITH_SAFE_LOCAL_WORKAROUND` or `BLOCKED/TERMINATED`).

Do not put proposed generic implementation patches in the edition record. Core repair design belongs on the Core-maintenance branch/session.

## 8. Relationship to machine orchestration artifacts

Keep machine-oriented artifacts such as stage checkpoints, validation JSON, candidate manifests and exact-byte hashes under their existing canonical machine paths.

The human-readable execution tree should point to them rather than mirror them.

Target separation:

```text
sources/<issue>/production-state.json
sources/<issue>/orchestration/...     # machine lifecycle / validator artifacts
sources/<issue>/execution/...         # human-readable actions / decisions / review continuity
sources/<issue>/publication/...       # publication/candidate artifacts
```

This prevents `orchestration/` from becoming a substitute for an understandable production record and prevents `execution/` from becoming another state machine.

## 9. Session bootstrap requirement

After implementation, every new edition production conversation must begin by reading, in this order:

1. current `main` Core authority / session bootstrap;
2. `sources/<issue>/production-state.json` if the run already exists;
3. `sources/<issue>/execution/index.md` if the run already exists;
4. the latest referenced session/review/defect record needed to continue.

A new chat should not need the Human to reconstruct the prior session manually when these records exist.

## 10. Session close requirement

Before a production conversation ends for any reason other than an abrupt tool/session failure, it must:

1. update/create its session log;
2. update `execution/index.md` if current-state navigation changed;
3. ensure Human Gate/review/defect pointers are present;
4. record the exact next action/stop reason;
5. commit the record on the edition work branch.

This logging is part of the production workflow, but it is not a Human Gate and should not require routine approval.

## 11. Migration / compatibility

Existing W33 and SP001 logs remain historical evidence in `docs/checkpoints/` and should not be rewritten merely to match the new layout.

When W33/SP001 are rerun after redesign, the new attempts should use the new edition-local `sources/<issue>/execution/` structure from the beginning. Old records may be linked as prior failed-trial evidence.
