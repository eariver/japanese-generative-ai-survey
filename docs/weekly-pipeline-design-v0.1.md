# Weekly Survey Pipeline Automation Design v0.1

Status: implementation baseline  
Established from: 2026-W32 manual end-to-end issue  
Authority: complements `docs/editorial-specification.md` and `docs/editorial-style-guide.md`.

## 1. Objective

The weekly automation must reproduce the **traceability and editorial gates** demonstrated by the 2026-W32 issue without turning the repository into an unattended AI-news publisher.

The target is not:

```text
cron -> LLM -> prose -> PDF -> publish
```

The target is:

```text
calendar / issue planning
    -> raw collection
    -> immutable provenance
    -> candidate normalization
    -> evidence verification
    -> cross-candidate selection
    -> issue architecture
    -> Japanese drafting
    -> claim / chronology validation
    -> reproducible TeX build
    -> rendered-page review
    -> explicit freeze
```

Core priority remains:

```text
Correctness > Traceability > Coverage > Speed
```

## 2. Automation boundary

The first automated implementation deliberately separates three classes of work.

### D — Deterministic automation

Suitable for GitHub Actions or normal scripts without editorial judgment.

Examples:

- resolve Friday 18:00 `America/New_York` cutoff;
- derive issue label from the cutoff week;
- carry forward the previous successful collection anchor;
- initialize issue state without overwriting existing artifacts;
- validate required files and state transitions;
- preserve raw-source filenames and hashes;
- detect stale hard-coded internal page references;
- run LuaLaTeX / Biber;
- fail on unresolved citations/references, missing glyphs and layout warnings;
- record build provenance and artifact digests.

### A — LLM-assisted / tool-assisted editorial work

Automation may prepare inputs and output files, but the result remains reviewable and must not silently promote itself through a human gate.

Examples:

- Grok X Trend Sensor;
- X Community Reaction Evidence Collector;
- general source discovery;
- candidate normalization;
- primary-source verification;
- paper full/targeted review;
- Evidence Card extraction;
- candidate matrix generation;
- candidate selection proposal;
- issue-architecture proposal;
- article drafting;
- citation-to-claim review;
- high-risk claim review;
- editorial prose polish.

### H — Explicit human/reviewer gate

Required where a technically valid build is not sufficient.

Initial mandatory gates:

1. **Candidate Selection Gate** — confirm that the issue is covering the right topics and that HOLD/REJECT decisions are reasonable.
2. **Freeze Gate** — inspect the final PDF and approve the frozen revision.

The system must not automatically merge or publicly release an issue merely because all deterministic jobs pass.

## 3. Canonical lifecycle

Machine lifecycle states are intentionally coarse. Fine-grained evidence status remains in candidate/evidence files.

```text
ISSUE_INITIALIZED
    -> DISCOVERY_COLLECTED
    -> CANDIDATES_NORMALIZED
    -> EVIDENCE_REVIEWED
    -> SELECTION_COMPLETE       [H gate]
    -> ARCHITECTURE_ESTABLISHED
    -> DRAFT_COMPLETE
    -> VALIDATED_DRAFT
    -> RELEASE_CANDIDATE
    -> FROZEN                   [H gate]
```

A stage may move backward when a correction is required. A `FROZEN` revision is not silently modified; substantive corrections produce a new revision.

## 4. Stage contracts

### S0 — Issue planning / initialization [D]

Inputs:

- current time;
- operational pipeline configuration;
- most recent successful `collection_anchor_at`.

Outputs:

- issue ID;
- editorial cutoff;
- collection window start/end;
- `sources/<issue>/pipeline-state.json` when explicitly initialized.

Rules:

- cutoff is always calculated using the IANA timezone `America/New_York`;
- issue ID is an edition label derived from the ISO week containing the cutoff, not a strict content interval;
- initialization is idempotent/non-destructive by default;
- if no previous collection anchor exists, unattended collection must not guess one.

### S1 — Discovery collection [A]

Inputs:

- collection window;
- editorial cutoff;
- current topic coverage policy;
- prompt version.

Collectors may include:

- Grok Trend Sensor;
- official/vendor announcement discovery;
- arXiv/OpenReview discovery;
- GitHub release/repository discovery;
- benchmark/evaluation discovery;
- later: additional social/community sources.

Outputs are **raw observations**. They are not Evidence Cards.

Raw collector output must be preserved unchanged once accepted into the repository.

### S2 — Candidate normalization [A + D]

Purpose:

- deduplicate multiple discoveries that refer to the same artifact/event;
- separate Artifact from Event;
- separate event chronology from trend chronology;
- create one candidate record per normalized topic;
- retain rejected or incorrect discoveries when useful for provenance.

Output:

```text
sources/<issue>/candidates/<slug>.md
sources/<issue>/candidates/index.yaml
```

No article ranking is performed at this stage.

### S3 — Evidence verification [A]

For each candidate as needed:

- find primary/authoritative sources;
- verify date/event type;
- classify technical facts vs vendor/author claims;
- extract metrics with setup boundaries;
- record limitations and unknowns;
- review full paper when headline interpretation depends on method/setup;
- normalize X reaction evidence separately.

The following evidence classes remain distinct:

```text
VERIFIED_PRIMARY
VENDOR_CLAIM
AUTHOR_REPORTED_RESULT
SOCIAL_OBSERVATION
EDITORIAL_INFERENCE
PENDING
```

Important claims must not be upgraded from social observation to technical fact.

### S4 — Candidate comparison / selection [A -> H]

Inputs:

- normalized candidate inventory;
- technical Evidence Cards;
- paper reviews;
- normalized social evidence;
- chronology state.

Comparison axes should include at least:

- W32/current-issue relevance;
- technical significance;
- source/evidence strength;
- verification depth;
- overlap with other candidates;
- amount of explanation required;
- remaining verification work.

Output roles may include:

```text
FEATURE_CORE
SECTION_CORE
PAPER_WATCH
LATE_BREAKING
CHRONOLOGY
WATCHLIST
HOLD_OUT
EXCLUDE
```

The selection proposal stops at a human/reviewer gate before downstream drafting is treated as authoritative.

### S5 — Issue architecture [A]

Only after selection is accepted:

- group related candidates into article packages;
- prevent duplicate treatment of the same underlying event;
- assign rough page budgets;
- decide where social evidence is supporting material rather than a separate story;
- preserve Late Breaking chronology.

The architecture is not a fixed category quota. Weak sections may disappear.

### S6 — Article drafting [A]

Drafts consume verified/normalized evidence, not raw collector output when a downstream evidence layer exists.

Major articles normally follow:

1. opening proposition;
2. verified event/artifact;
3. technical mechanism/distinction;
4. evidence boundary;
5. community reaction when useful;
6. editorial synthesis.

Cover and `This Week in AI` are drafted **after** the body articles.

### S7 — Editorial / claim validation [A + D]

Required reviews include:

- citation-to-claim audit;
- cross-section chronology audit;
- Main vs Post-Cutoff audit;
- vendor/author attribution audit;
- simulation/threat-model boundary review;
- high-risk claim review;
- terminology consistency;
- hard-coded internal page-reference detection.

This stage may send an article back to evidence verification.

### S8 — TeX build / PDF preflight [D]

GitHub Actions owns reproducible compilation.

Minimum gate:

- LuaLaTeX / Biber complete;
- PDF exists and is non-empty;
- no unresolved citations/references;
- no rerun requirement in final log;
- no Overfull/Underfull boxes under the current publication policy;
- no missing glyph warnings.

The PDF is a build artifact; the TeX/Bib/Evidence tree remains the repository Source of Truth.

### S9 — Visual review / freeze [H + D]

A successful TeX build is not itself a freeze decision.

Visual review checks:

- clipping/overlap;
- heading hierarchy;
- column flow;
- callout-box layout;
- blank pages;
- Cover/Contents balance;
- References overflow/wrapping;
- stale visible page references;
- unexpected regressions from the prior candidate build.

Freeze output records:

- source commit;
- Actions run/job;
- artifact ID/name;
- artifact digest;
- extracted PDF digest;
- page count/preflight result;
- visual-review result.

## 5. Repository state model

Operational machine state lives in:

```text
sources/<issue>/pipeline-state.json
```

This file is intentionally separate from `manifest.yaml`.

- `manifest.yaml` remains the rich issue/editorial manifest.
- `pipeline-state.json` is a small deterministic orchestration state that scripts can read using the Python standard library.

The state file is not allowed to replace detailed Evidence Cards or editorial records.

## 6. Collection anchor

The collection window is:

```text
previous successful collection anchor
    -> current collection
```

The anchor is carried in `pipeline-state.json` as:

```json
{
  "calendar": {
    "collection_anchor_at": "..."
  }
}
```

The next issue planner scans prior state files and selects the most recent valid anchor.

It is preferable to overlap collection windows and deduplicate later than to guess a later anchor and lose events.

## 7. Scheduled GitHub Actions role

The initial scheduled workflow runs on Saturday after the Friday cutoff and is deliberately **plan-only**.

Recommended schedule:

```text
Saturday 00:30 UTC
```

This is safely after Friday 18:00 New York in both EDT and EST.

The scheduled job:

1. checks out the repository;
2. computes issue/cutoff/window metadata;
3. uploads a `weekly-pipeline-plan` artifact;
4. performs no merge, publication or LLM call.

Manual `workflow_dispatch` may run deterministic validation for a named issue.

Later phases may add PR creation and collector adapters, but unattended public release remains forbidden until policy is intentionally changed.

## 8. PR model for later automation

Recommended eventual weekly unit:

```text
branch: issue/<issue-id>
PR:     [<issue-id>] Weekly survey
```

The same PR may accumulate stage outputs, but every stage should write explicit artifacts rather than hide state in comments.

Suggested checkpoints:

1. raw/discovery imported;
2. candidate/evidence review ready;
3. selection gate ready;
4. architecture/draft ready;
5. validation/PDF ready;
6. freeze approved.

No stage should rewrite accepted raw collector output merely to simplify a later stage.

## 9. LLM execution contract

Future LLM runners should be provider/model agnostic.

Every run should record at least:

```yaml
stage:
prompt_id:
prompt_version:
prompt_hash:
model:
provider:
started_at:
completed_at:
input_artifacts:
output_artifacts:
tool_access:
```

A model name alone is insufficient provenance because prompts, source set and tool access materially change results.

LLM stages should prefer structured outputs or explicit file contracts. A malformed/partial output should fail the stage rather than be silently repaired by a different stage.

## 10. Failure semantics learned from W32

The following are **valid outcomes**, not pipeline failures:

- a coverage lane has no meaningful candidate;
- X evidence is insufficient;
- a candidate remains `PENDING`/`HOLD_OUT`;
- an announced date cannot be verified;
- a weak week produces fewer than the target number of pages;
- a Late Breaking item is deferred to the following issue.

The following are pipeline failures/blockers:

- raw provenance is lost or overwritten;
- a concrete technical claim lacks support in the verified layer;
- event chronology and trend chronology are silently conflated;
- a frozen revision is silently modified;
- deterministic publication warnings remain in the final TeX log;
- required human gates are bypassed.

## 11. Implementation slices

### Slice A — deterministic spine (implement first)

- operational config;
- calendar/issue planner;
- pipeline state schema;
- `plan`, `init`, `validate` CLI;
- scheduled plan-only Actions workflow;
- W32 frozen state as the bootstrap collection anchor.

This slice requires no external API keys.

### Slice B — source-intake contracts

- collector run metadata schema;
- immutable raw-file hashing/index;
- official/arXiv/GitHub intake adapters;
- automatic issue-specific Grok run-instruction generation;
- duplicate/event-normalization helpers.

### Slice C — evidence runners

- screening prompt;
- technical verification prompt;
- paper-review prompt;
- social normalization prompt v0.2;
- schema validation for Evidence Cards;
- provider/model/tool provenance recording.

### Slice D — editorial runners

- candidate matrix generator;
- selection proposal;
- issue architecture proposal;
- article drafting packages;
- bibliography assembly;
- citation/chronology/high-risk review.

Selection remains human-gated.

### Slice E — PR orchestration

- weekly issue branch/PR creation;
- stage status checks;
- stage artifacts attached to the PR;
- deterministic validation before merge;
- no automatic public release.

### Slice F — chronology + monthly/annual reuse

- normalize verified Artifact/Event records into the chronology store;
- generate chronology site data;
- reuse frozen weekly Evidence Cards for monthly and annual synthesis.

## 12. Current implementation decision

The repository should now implement **Slice A** before adding any new model/API integration.

Reason:

W32 proved that the difficult part is not generating prose. The difficult part is preserving the boundaries among raw discovery, verified evidence, editorial selection, chronology, drafting and final publication state.

A deterministic spine makes those boundaries enforceable before more automation increases throughput.
