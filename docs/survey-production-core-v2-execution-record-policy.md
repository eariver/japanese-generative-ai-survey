# Survey Production Core v2 — Edition Execution Record Policy

Status: `IMPLEMENTED IN REDESIGN CANDIDATE / PENDING FIXED-HEAD AUDIT`  
Established: 2026-08-23 JST  
Implemented: 2026-08-23 JST  
Working branch: `refactor/survey-production-core-v2`  
Related redesign: `docs/survey-production-core-v2-redesign-plan-after-w33-sp001.md`

## 1. Purpose

Every Weekly/Special production task is normally executed in its own ChatGPT conversation. The repository therefore needs a stable, edition-local record that allows a later session or Core-maintenance review to reconstruct what actually happened without reading chat history or inferring behavior from commits alone.

W33 and SP001 showed two opposite failure modes:

- one long worklog can become stale as the lifecycle continues beyond its original stated stop;
- multiple ad-hoc checkpoint files can preserve detail but become fragmented and difficult to review as one production run.

The redesigned flow therefore requires a small, predictable execution-record tree for every edition.

Machine lifecycle/state artifacts remain authoritative for machine state. Execution records are human-readable operational provenance and must not duplicate every machine field.

## 2. Canonical location

Store edition execution records under the edition's existing source root, not in the global `docs/checkpoints/` namespace.

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

Do not create date-stamped checkpoint files directly in `docs/checkpoints/` for normal edition production after this policy is implemented.

## 3. Deterministic helper boundary

`scripts/survey_execution_record_v2.py` implements only the structural part of this policy.

It may:

- create the canonical `execution/` tree for a newly initialized edition;
- create the first `index.md` and session skeleton from exact Profile/State/commit inputs;
- validate required directories/headings, Profile identity, canonical State pointer, and session-index continuity.

It must not:

- infer or write research/editorial judgments;
- summarize a session from chat history;
- invent Human review decisions;
- decide whether a defect is shared Core;
- change Production State;
- replace ChatGPT's obligation to update the Markdown as production proceeds.

Initialization example:

```text
python scripts/survey_execution_record_v2.py init \
  --profile <source_root>/production-profile.json \
  --state <source_root>/production-state.json \
  --session-id <YYYY-MM-DDTHHMM-JST-purpose> \
  --started-at <ISO-8601> \
  --main-sha <reviewed-main-commit> \
  --branch-head <edition-branch-head> \
  --objective '<session objective>' \
  --requested-stop ARCHITECTURE_REVIEW
```

Structural validation:

```text
python scripts/survey_execution_record_v2.py validate \
  --profile <source_root>/production-profile.json \
  --state <source_root>/production-state.json
```

## 4. `index.md` — one current run index per edition

`index.md` is the first file a new ChatGPT session should read after `production-state.json`. It is a compact current-state navigation document, not a diary.

Required content includes:

- issue / edition ID;
- Research Profile and Publication Profile;
- canonical work branch;
- source-of-truth reviewed `main` commit SHA used to start the run;
- run start date/time;
- requested Human Gate / requested end state;
- current lifecycle and stop reason as convenience pointers from canonical State;
- Human Gate status and relevant Issue/PR pointers;
- current accepted/rejected Publication Candidate and PDF identity when applicable;
- Grok/X applicability, latest Drive task-file path and result disposition when applicable;
- known edition-local deviations;
- known shared-Core defects;
- session logs in chronological order;
- final disposition: `IN_PROGRESS`, `HUMAN_GATE`, `BLOCKED_CORE_DEFECT`, `TERMINATED_VALIDATION`, or `COMPLETE`.

### Freshness rule

Update `index.md` whenever:

- lifecycle crosses a Human Gate boundary;
- a Human Gate is rejected/approved;
- a shared-Core defect changes the ability to continue;
- a new Publication Candidate becomes the Human review target;
- the run is terminated or completed.

This prevents the stale-header failure observed in W33.

## 5. `sessions/<session-id>.md` — actions actually performed

Create one session log per ChatGPT production conversation, or per materially separate continuation if one conversation is intentionally split into distinct execution phases.

Recommended ID:

```text
YYYY-MM-DDTHHMM-JST-<short-purpose>.md
```

Required sections are:

### Starting authority

Record branch head, Production State path/SHA, reviewed Core/main SHA, session objective/requested stop and prior execution pointer.

### Actions actually performed

Group by meaningful stage rather than tool call. Record material work, useful counts, important judgments, canonical artifact paths, and commit/PR/run identity only when it materially identifies resulting state.

### External handoff

When Grok/X is used, record only:

- exact Google Drive `grok-task.md` path/reference given to the Human;
- returned result path/reference;
- imported repository Raw path;
- result SHA/byte count or manifest identity;
- editorial disposition (`DISCOVERY_RECORDED` / `NO_MATERIAL_DISCOVERY`).

Do not duplicate the task/result body.

### Deviations / failures

Record only run-affecting failures and classify each as:

- `EDITION_LOCAL`
- `TRANSIENT_EXECUTION`
- `SHARED_CORE_DEFECT`

A `SHARED_CORE_DEFECT` points to `execution/defects/` and is not repaired in the production session.

### End state

Record lifecycle/Human Gate status, exact candidate/PDF identity if applicable, next action and why the session ended.

## 6. Recording granularity

The record must be sufficient to answer:

1. What did ChatGPT actually do?
2. What material decisions were made and why?
3. Which exact artifacts became authoritative?
4. Where did Human/Grok interaction occur?
5. Did the production session encounter or modify shared Core?
6. Why did the session stop?

It must not be a transcript or chain-of-thought log.

A normal stage usually needs 3–10 concise bullets. Do not routinely list every connector invocation, workflow poll, successful command, file opened, repetitive PASS output, full Issue body, or full external-source content.

## 7. `reviews/` — compact Human Gate revision history

Every Human Gate decision/revision gets one short Markdown record even if detailed feedback lives in a GitHub Issue.

Required headings are:

- `Reviewed authority`
- `Human decision`
- `Requested changes`
- `Regeneration boundary`
- `Shared-Core implication`

Record gate, revision, reviewed candidate identity, Human decision, detailed feedback pointer, concise defect families, earliest regeneration boundary and whether shared Core is implicated. Do not duplicate the full Human feedback body.

## 8. `defects/` — shared-Core observations from production

A Production session may observe but must not repair a shared-Core defect.

Required headings are:

- `Observation`
- `Reproduction boundary`
- `Impact`
- `Safe edition-local workaround`
- `Core-maintenance pointer`
- `Production disposition`

Record symptom, affected edition/profile, reproducing artifact/boundary, correctness/quality/autonomy impact, safe workaround availability, maintenance pointer, and `CONTINUE_WITH_SAFE_LOCAL_WORKAROUND` or `BLOCKED/TERMINATED` disposition.

Do not put proposed generic implementation patches in the edition record.

## 9. Relationship to machine artifacts

Keep machine-oriented artifacts under existing canonical paths and point to them from execution records:

```text
sources/<issue>/production-state.json
sources/<issue>/orchestration/...     # machine lifecycle / validator artifacts
sources/<issue>/execution/...         # human-readable actions / decisions / review continuity
sources/<issue>/publication/...       # publication/candidate artifacts
```

`execution/` is not a second state machine.

## 10. Session bootstrap

Every new edition production conversation reads, in this order:

1. current reviewed `main` Core authority / session bootstrap;
2. `sources/<issue>/production-state.json` if the run exists;
3. `sources/<issue>/execution/index.md` if the run exists;
4. latest referenced session/review/defect record needed to continue.

For a new run, initialize the execution record after canonical Profile/State initialization. For an existing run, do not rerun `init`; create/update the next session record and list it in `index.md`.

## 11. Session close

Before a production conversation ends for any reason other than abrupt tool/session failure, it must:

1. update/create its session log;
2. update `execution/index.md` when current-state navigation changed;
3. ensure Human Gate/review/defect pointers are present;
4. record exact next action/stop reason;
5. run structural execution-record validation;
6. commit the record on the edition work branch.

This logging is internal production work and never requires routine approval.

## 12. Migration / compatibility

Existing W33 and SP001 logs remain historical evidence in `docs/checkpoints/` and are not rewritten merely to match the new layout.

Clean post-redesign validation runs use `sources/<issue>/execution/` from the beginning. Old W33/SP001 trial records may be linked as failed-trial evidence.
