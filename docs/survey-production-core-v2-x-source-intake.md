# Survey Production Core v2 — X Source Intake via Grok and Google Drive

Status: `CANONICAL EXTERNAL SOURCE INTAKE SUBFLOW`  
Established: 2026-08-22 JST  
Revised: 2026-08-23 JST after W33/SP001 feedback (`PFB-001`, `PFB-002`)

## 1. Purpose

X is a material discovery/community-signal surface for this survey. It is especially important for Weekly production, where release momentum, independent testing, local inference, runtime integration, community reproduction and newly discovered constraints may become material after the original announcement.

Grok is therefore treated as an **external X Source Intake sensor**, not as final technical Evidence authority.

This subflow is part of Source Intake. It does **not** add a Human editorial/publication Gate.

The two normal Human Gates remain:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

If Grok output is not yet available, production remains in ordinary Source Intake. `AWAITING_GROK` is not a Production State terminal reason or Exception Gate.

## 2. Profile policy

### Weekly

Grok/X intake is `REQUIRED_BY_PROFILE`.

Every Weekly Source Intake must include at least one completed Grok/X run before Discovery can be accepted. A quiet X week is valid: Grok may report no material signal, but the scan itself must have been performed and its result disposition recorded.

### Retrospective Period

Grok/X intake is `CHATGPT_DECIDES`.

ChatGPT decides whether X materially improves the retrospective research question. Typical reasons to use X include community adoption trajectories, reproduction, integration, local inference, operational constraints, or the difference between official release narratives and downstream technical practice.

If X is not needed, ChatGPT records `NOT_REQUIRED` with a substantive rationale. Silence is not a decision.

### Standalone Thematic

Grok/X intake is `CHATGPT_DECIDES`.

Use X when it helps answer a material thematic research question, especially ecosystem behavior, independent evaluation, adoption, competing practice or implementation experience not captured well by primary release material. Do not use X merely to inflate source count.

### Generative AI Foundations

Each volume uses a normal `THEMATIC` Production Profile, but X intake may carry `series_context = GENERATIVE_AI_FOUNDATIONS` so its Google Drive location is separated from standalone Thematic Specials.

Historical lineage, priority and attribution remain primary/historical-source questions. X is generally low-value for older historical volumes and may be more useful for contemporary implementation practice, present-day reception or frontier/end-point volumes.

## 3. Responsibility split

### ChatGPT

ChatGPT owns:

- deciding whether X is required when the Profile says `CHATGPT_DECIDES`;
- defining the X research purpose, questions, coverage focus and time scope;
- rendering one self-contained `grok-task.md` for each run;
- provisioning the Google Drive run folder;
- placing the exact task bytes in that Drive folder;
- giving the Human the exact Drive task-file path/reference;
- reading the returned Drive Markdown;
- importing its exact bytes into repository Raw storage;
- evaluating the X observations;
- mapping material observations to Discovery or explicitly recording `NO_MATERIAL_DISCOVERY`;
- performing primary-source gap-fill before technical claims become Evidence;
- resuming production automatically after result import/disposition.

### Human

The Human does not approve Grok collection as a third Gate and does not manually relay the task body.

The normal Human transport action is exactly:

> give Grok the Google Drive path/reference of the already-prepared `grok-task.md`.

The Human does **not** need to copy/paste the instruction, prompt, research questions or output specification.

### Grok

Grok:

- opens the exact Drive task-file path/reference received from the Human;
- reads that self-contained task;
- performs the requested X-native search/observation;
- writes one result Markdown to the result folder named by the task.

Grok does not write to GitHub and is not authoritative for technical facts that require primary-source verification.

### Deterministic tools / GitHub Actions

Tools own:

- manifest/schema validation;
- exact task-file hash binding;
- Profile policy enforcement;
- exact repository Raw SHA-256/byte binding after import;
- required X-run completion accounting;
- Discovery integration accounting;
- lifecycle/stage authority checks.

GitHub Actions may validate repository artifacts, but it does not need Google Drive credentials and does not invoke Grok.

## 4. No Grok connector discovery

A required X run does **not** authorize ChatGPT to search for, install, discover or configure a Grok connector.

Absence of a Grok connector is not:

- an error;
- a missing dependency;
- an Exception Gate;
- a reason to debug the production environment.

The expected architecture is **Human-mediated Drive task-file handoff** unless the Human explicitly changes that policy in the future.

## 5. Google Drive handoff contract

The configured Drive root is exactly:

`Grok_X_SourseIntake`

Persistent categories are:

```text
Grok_X_SourseIntake/
  Weekly/
  Retrospective_Special/
  Thematic_Special/
  Generative_AI_Foundations/
```

Each execution uses:

```text
Grok_X_SourseIntake/<category>/<edition-folder>/<run-id>/
  grok-task.md
  <result>.md
```

Examples:

```text
Grok_X_SourseIntake/Weekly/2026-W35/weekly-x-2026-W35/grok-task.md
Grok_X_SourseIntake/Retrospective_Special/2025-H2/community-adoption-pass-01/grok-task.md
Grok_X_SourseIntake/Thematic_Special/SP001/open-weight-ecosystem-pass-01/grok-task.md
Grok_X_SourseIntake/Generative_AI_Foundations/<volume-slug>/frontier-reception-pass-01/grok-task.md
```

The root folder ID/URL is intentionally not committed to the public repository. ChatGPT resolves the exact root through the connected Google Drive account at execution time.

The run folder and `grok-task.md` must exist before Human handoff. Human passes the exact task-file path/reference, not merely an ambiguous category or edition folder.

If Grok cannot find the exact task file or instructed result folder, it must stop rather than choosing another location.

If the expected result filename already exists, Grok must not overwrite it; use a revision suffix such as `-r2` and report the actual filename.

## 6. Repository artifacts and provenance

The accepted Source Intake boundary contains:

```text
<source_root>/external/x/x-source-intake-v2.json
<source_root>/external/x/<run-id>/grok-task.md
<source_root>/external/x/<run-id>/raw/<imported-result>.md
```

The repository task file is the provenance authority for the exact bytes ChatGPT places in Drive. The manifest records:

- exact Production Profile;
- Profile X policy;
- ChatGPT's `REQUIRED` / `NOT_REQUIRED` decision and rationale;
- Drive category / edition / run folder path;
- exact `drive_task_path`;
- exact repository task path and SHA-256;
- expected result filename;
- exact imported Raw bytes and byte count;
- observed/imported timestamps;
- result status and Discovery disposition.

Repository provenance stores path semantics and hashes, not private Google Drive folder IDs.

A separate `grok-instruction.md` or `grok-prompt.md` is not part of the redesigned run contract. The self-contained task incorporates the generic and Profile-specific prompt policy.

## 7. Run lifecycle

For a required run:

```text
ChatGPT defines X research task
-> create Drive edition/run folder
-> render repository grok-task.md
-> place the exact task bytes at the manifest's drive_task_path
-> manifest = AWAITING_GROK
-> give Human the exact Drive task-file path/reference
-> Human gives only that path/reference to Grok
-> Grok reads grok-task.md and searches X
-> Grok writes result Markdown into the instructed Drive run folder
-> ChatGPT reads Drive result
-> ChatGPT imports exact result bytes into repository Raw storage
-> ChatGPT evaluates the observation
-> material signal: create Discovery record(s) bound to imported Raw
   OR
   no material signal: record NO_MATERIAL_DISCOVERY + rationale
-> manifest = COMPLETE
-> deterministic X intake validation
-> Discovery acceptance / CORE_STAGE_CONTRACT
-> continue to Screening automatically
```

There is no additional routine approval after Grok returns.

## 8. Weekly prompt behavior

Weekly uses the generic common X policy plus the Weekly overlay. It performs independent coverage scans across model/reasoning, agents/coding, multimodal, image, video, audio/music, open-weight/local AI, serving/systems, memory/retrieval, evaluation, safety/security and other emerging technology.

It separates:

- underlying event date;
- X momentum date;
- ordinary-window signal;
- post-cutoff `Late Breaking` signal.

A Weekly cannot skip Grok because conventional collectors happened to find many sources.

The completed Grok result also receives reader-facing editorial disposition under the Weekly Profile: a material community signal is reflected in `コミュニティの動き` or receives an internal exclusion reason; a quiet week is represented explicitly rather than silently omitted.

## 9. Special prompt behavior

Special runs are question-driven, not Weekly Top-10 scans.

ChatGPT creates one or more targeted Grok runs only when X is material. Each self-contained task states why X is useful to the edition and defines:

- research questions;
- relevant actors/technologies/communities;
- time scope;
- coverage focus;
- evidence boundaries;
- output destination;
- expected downstream primary-source gap-fill.

Multiple runs are allowed when one broad X query would blur materially different research questions.

## 10. Evidence boundary

Grok/X output may support:

- Discovery;
- community reaction;
- adoption/integration signals;
- independent-test leads;
- candidate primary-source locators;
- counter-signals and unresolved questions.

It does not by itself establish publication-grade technical facts such as model specifications, benchmark values, release dates or license terms. Those claims enter Evidence only after appropriate authoritative verification.

## 11. Source Intake completion rule

Before `ISSUE_INITIALIZED -> DISCOVERY_COLLECTED` can be accepted, the exact `x-source-intake-v2.json` manifest must be present and valid.

- Weekly: decision must be `REQUIRED`; every configured Grok run must have an imported result and final disposition.
- Retrospective/Thematic/Foundations: decision may be `NOT_REQUIRED`, but the rationale must be explicit. If `REQUIRED`, every run must be completed/dispositioned.
- each required run must bind exactly one `grok-task.md` authority and exact `drive_task_path`;
- `DISCOVERY_RECORDED` requires named Discovery records to bind the exact imported Grok Raw bytes;
- `NO_MATERIAL_DISCOVERY` requires an explicit rationale and no fake Discovery ID.

This prevents three failure modes:

1. X was supposed to be consulted but silently was not.
2. Human had to manually reconstruct or copy a Grok prompt instead of passing a prepared Drive task reference.
3. X was collected but its result disappeared without an explicit research disposition.
