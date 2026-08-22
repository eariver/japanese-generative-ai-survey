# Survey Production Core v2 — X Source Intake via Grok and Google Drive

Status: `CANONICAL EXTERNAL SOURCE INTAKE SUBFLOW`  
Established: 2026-08-22 JST

## 1. Purpose

X is a material discovery/community-signal surface for this survey. It is especially important for Weekly production, where release momentum, independent testing, local inference, runtime integration, community reproduction and newly discovered constraints may become material after the original announcement.

Grok is therefore treated as an **external X Source Intake sensor**, not as final technical Evidence authority.

This subflow is part of Source Intake. It does **not** add a Human editorial/publication Gate.

The two normal Human Gates remain:

1. `ARCHITECTURE_REVIEW`
2. exact-byte `PUBLICATION_PREVIEW`

If Grok output is not yet available, production remains in the ordinary Source Intake stage. The edition may wait operationally for an external collection result, but this is not Human approval and not an Exception Gate by itself.

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

Use X when it helps answer a material thematic research question, especially ecosystem behavior, independent evaluation, adoption, competing practice or implementation experience not captured well by primary release material.

Do not use X merely to inflate source count.

### Generative AI Foundations

Each volume uses a normal `THEMATIC` Production Profile, but X intake may carry `series_context = GENERATIVE_AI_FOUNDATIONS` so its Google Drive location is separated from standalone Thematic Specials.

Historical lineage, priority and attribution remain primary/historical-source questions. X is generally low-value for older historical volumes and may be more useful for contemporary implementation practice, present-day reception or frontier/end-point volumes.

## 3. Responsibility split

### Human

The Human does not approve Grok collection as a third Gate.

If no automated Grok execution integration exists, the Human may act as a transport/operator by giving Grok the generated run instruction/prompt. This is an operational handoff, not editorial approval.

### ChatGPT

ChatGPT owns:

- deciding whether X is required when the Profile says `CHATGPT_DECIDES`;
- defining the X research purpose, questions, coverage focus and time scope;
- creating the run-specific Grok instruction and prompt;
- provisioning the Google Drive run folder;
- reading the returned Drive Markdown;
- importing its exact bytes into repository Raw storage;
- evaluating the X observations;
- mapping material observations to Discovery or explicitly recording `NO_MATERIAL_DISCOVERY`;
- performing primary-source gap-fill before technical claims become Evidence.

### Grok

Grok owns X-native search/observation for the run-specific task and writes one result Markdown to the instructed Google Drive run folder.

Grok does not write to GitHub and is not authoritative for technical facts that require primary-source verification.

### Deterministic tools / GitHub Actions

Tools own:

- manifest/schema validation;
- prompt/instruction hashes;
- Profile policy enforcement;
- exact repository Raw SHA-256/byte binding after import;
- required X-run completion accounting;
- Discovery integration accounting;
- lifecycle/stage authority checks.

GitHub Actions may validate these repository artifacts, but it does not need credentials to the user's Google Drive. The actual Drive read/write handoff is performed through the connected Google Drive capability available to ChatGPT/Grok or by the Human transport step.

## 4. Google Drive handoff contract

The configured Drive root is exactly:

`Grok_X_SourseIntake`

The persistent category folders are:

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
```

Examples:

```text
Grok_X_SourseIntake/Weekly/2026-W35/weekly-x-2026-W35/
Grok_X_SourseIntake/Retrospective_Special/2025-H2/community-adoption-pass-01/
Grok_X_SourseIntake/Thematic_Special/SP001/open-weight-ecosystem-pass-01/
Grok_X_SourseIntake/Generative_AI_Foundations/<volume-slug>/frontier-reception-pass-01/
```

The root folder ID/URL is intentionally not committed to the public repository. ChatGPT resolves the exact root by name through the connected Google Drive account and creates the edition/run folders at execution time.

Grok receives the exact path in the run-specific prompt. The run folder should already exist before Grok starts.

If Grok cannot find the instructed folder, it must stop rather than choosing another Drive location.

If the expected result filename already exists, Grok must not overwrite it; use a revision suffix such as `-r2` and report the actual filename.

## 5. Repository artifacts

The accepted Source Intake boundary contains:

```text
<source_root>/external/x/x-source-intake-v2.json
<source_root>/external/x/<run-id>/grok-instruction.md
<source_root>/external/x/<run-id>/grok-prompt.md
<source_root>/external/x/<run-id>/raw/<imported-result>.md   # recommended layout
```

The manifest binds:

- exact Production Profile;
- Profile X policy;
- ChatGPT's REQUIRED / NOT_REQUIRED decision and rationale;
- Drive category / edition / run folder path;
- exact instruction and prompt hashes;
- exact imported Raw bytes;
- observed/imported timestamps;
- whether material Discovery was created from that run.

The repository stores folder names/path semantics, not private Google Drive folder IDs.

## 6. Run lifecycle

For a required run:

```text
ChatGPT defines X research task
-> create Drive edition/run folder
-> render grok-instruction.md + grok-prompt.md
-> manifest = AWAITING_GROK
-> Grok searches X
-> Grok writes Markdown into exact Drive run folder
-> ChatGPT reads Drive file
-> ChatGPT imports exact Markdown bytes into repository Raw storage
-> ChatGPT evaluates the observation
-> material signal: create Discovery record(s) bound to imported Raw
   OR
   no material signal: record NO_MATERIAL_DISCOVERY + rationale
-> manifest = COMPLETE
-> deterministic X intake validation
-> Discovery acceptance / CORE_STAGE_CONTRACT
-> continue to Screening
```

`AWAITING_GROK` is not a Production State terminal reason. It is simply incomplete Source Intake work.

## 7. Weekly prompt behavior

Weekly uses the generic common X policy plus the Weekly overlay. It performs independent coverage scans across model/reasoning, agents/coding, multimodal, image, video, audio/music, open-weight/local AI, serving/systems, memory/retrieval, evaluation, safety/security and other emerging technology.

It separates:

- underlying event date;
- X momentum date;
- ordinary-window signal;
- post-cutoff `Late Breaking` signal.

A Weekly cannot skip Grok because conventional collectors happened to find many sources.

## 8. Special prompt behavior

Special runs are question-driven, not Weekly Top-10 scans.

ChatGPT creates one or more targeted Grok runs only when X is material. The prompt should say why X is useful to this specific edition and define:

- research questions;
- relevant actors/technologies/communities;
- time scope;
- coverage focus;
- evidence boundaries;
- expected downstream primary-source gap-fill.

Multiple runs are allowed when one broad X query would blur materially different research questions.

## 9. Evidence boundary

Grok/X output may support:

- Discovery;
- community reaction;
- adoption/integration signals;
- independent-test leads;
- candidate primary-source locators;
- counter-signals and unresolved questions.

It does not by itself establish publication-grade technical facts such as model specifications, benchmark values, release dates or license terms. Those claims enter Evidence only after appropriate authoritative verification.

## 10. Source Intake completion rule

Before `ISSUE_INITIALIZED -> DISCOVERY_COLLECTED` can be accepted, the exact `x-source-intake-v2.json` manifest must be present and valid.

- Weekly: decision must be `REQUIRED`; every configured Grok run must have an imported result and final disposition.
- Retrospective/Thematic/Foundations: decision may be `NOT_REQUIRED`, but the rationale must be explicit. If `REQUIRED`, every run must be completed/dispositioned.
- `DISCOVERY_RECORDED` requires the named Discovery records to bind the exact imported Grok Raw bytes.
- `NO_MATERIAL_DISCOVERY` requires an explicit rationale and no fake Discovery ID.

This prevents both failure modes:

1. X was supposed to be consulted but silently was not.
2. X was collected but its result disappeared without an explicit research disposition.
