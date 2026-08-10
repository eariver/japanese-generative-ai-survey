# Weekly Pipeline Implementation Status

Updated: 2026-08-10  
Reference issue: `2026-W32`

## Slice A — Deterministic spine

Status: **implemented**

- [x] cutoff / issue planner using `America/New_York`
- [x] collection-anchor carry-forward
- [x] per-issue pipeline state schema
- [x] `plan`, `init`, `validate` CLI
- [x] scheduled plan-only GitHub Actions workflow
- [x] static internal-page-reference guard
- [x] unit tests for DST / anchor / optional sections
- [x] reproducible PDF timestamp policy for new builds
- [x] assistant-controlled allowlisted workflow dispatch via `automation-control`

## Slice B — Source intake contracts

Status: **implemented and W32-replay validated; first live new-issue run pending**

- [x] pre-execution collector instruction schema
- [x] post-execution collector-run provenance schema
- [x] immutable Raw SHA-256 index/check
- [x] automatic Raw-integrity CI
- [x] W32 Raw provenance baseline
- [x] issue-specific Grok Trend Sensor instruction generator
- [x] arXiv API intake adapter
- [x] curated GitHub Releases intake adapter
- [x] configured official news/blog/feed snapshot adapter
- [x] OpenAI official News RSS fallback for stable automated intake
- [x] HTTP-mocked intake unit tests
- [x] append-only run-specific collector paths
- [x] W32 replay Actions artifact review
- [x] deterministic screening-index normalization
- [x] bounded screening batches
- [x] reviewed collector-artifact import workflow into the canonical weekly work branch
- [x] exact Actions run/workflow/ref/artifact/digest verification before reviewed import
- [x] real W32 resolver/branch-gate smoke (`run 31378110064` using source run `31359910803`)
- [ ] first live `source-intake` Actions artifact review for a new issue
- [ ] first successful reviewed new-issue import into its weekly work branch

Validated W32 replay (`run 31359910803`):

- 1,037 screening records total;
- 921 arXiv paper records;
- 103 curated GitHub Release records;
- 10 official feed items;
- 3 official index snapshots;
- 39 bounded screening batches.

The W32 reviewed-import smoke deliberately had no `weekly/2026-W32-work` branch. The source run and Artifact verification passed, then the workflow stopped at the branch gate before download/import, proving the resolver against real GitHub Actions metadata without modifying the frozen W32 issue.

A premature W33 live run (`31377560587`) was also rejected by the calendar guard on 2026-08-10 because the current completed editorial cutoff still maps to W32. W33 becomes the rolling issue only after Friday 2026-08-14 18:00 `America/New_York`; the pipeline must not fabricate a future issue window to bypass that boundary.

Current collector Raw layout:

```text
sources/<issue>/collectors/<collector>/runs/<observed-at>/
├─ raw/
├─ summary.json
└─ collector-run.json
```

Raw bytes are immutable after acceptance; `summary.json` is derived discovery metadata and is not a technical Evidence Card.

## GitHub Release distribution

Status: **implemented; validate and Draft smoke tests passed; public publish intentionally pending**

- [x] frozen release manifest schema
- [x] W32 release manifest
- [x] canonical tag convention `weekly/<issue>/<revision>`
- [x] `validate` mode with no tag/Release write
- [x] `draft` mode with exact PDF digest check
- [x] Draft target/anchor pinned and re-verified
- [x] `publish` requires existing verified Draft
- [x] Release PDF + `SHA256SUMS.txt` + `RELEASE_METADATA.json`
- [x] W32 exact frozen Actions-artifact source
- [x] future reproducible rebuild source mode
- [x] optional immutable-release attestation verification after publish
- [x] W32 Release workflow `validate` smoke test (`31358396989`)
- [x] W32 Draft Release creation and asset verification (`31359673413`)
- [ ] repository Immutable Releases setting decision/enablement
- [ ] first published weekly Release

Release tags are distribution/control anchors. The frozen PDF-producing source commit and PDF digest remain separately authoritative in release provenance.

## Slice C — Screening and Evidence runners

Status: **provider-agnostic automation contract implemented; interactive primary-source smoke passed**

### Screening

- [x] machine-collected screening record schema
- [x] bounded batch generator
- [x] provider-agnostic screening prompt v0.1
- [x] screening batch result schema
- [x] exact input/prompt SHA-256 validation
- [x] one-decision-per-input completeness validation
- [x] resumable partial-result merge
- [x] `KEEP / MAYBE / DROP / INSPECT` separation
- [x] verification queue containing only retained/inspection items
- [x] dedicated screening contract CI
- [x] interactive GPT screening smoke on real W32 replay batches
- [ ] production inference provider adapter / secret configuration
- [ ] all-batch live screening for a new issue

### Evidence tasks

- [x] deterministic Evidence Task schema and builder
- [x] one file per Evidence Task
- [x] Evidence Task SHA-256 recorded in manifest
- [x] `VERIFY_ITEM / VERIFY_SERIES / INSPECT_INDEX`
- [x] unconfirmed LLM duplicate-group hints remain explicitly unconfirmed
- [x] resumable singleton duplicate-group behavior

### Evidence Cards / Runs

- [x] structured Evidence Card schema
- [x] Evidence Run provenance wrapper
- [x] primary-source verification prompt v0.1
- [x] evidence classes: `PRIMARY_FACT`, `VENDOR_CLAIM`, `PROJECT_CLAIM`, `AUTHOR_CLAIM`, `SOCIAL_OBSERVATION`, `INFERENCE`
- [x] temporal Event/Artifact separation
- [x] stable `event_id` for event-level downstream references
- [x] metric context and limitation fields
- [x] exact Evidence Task / prompt SHA validation
- [x] source-reference integrity checks
- [x] verification-target completeness checks
- [x] unique stable Event ID validation
- [x] resumable Evidence Run merge
- [x] `CANDIDATE / HOLD / INSPECT_MORE / REJECT` queues
- [x] deterministic pre-selection Candidate Record materializer
- [x] real primary-source smoke using the llama.cpp / DeepSeek V4 support series
- [ ] production Evidence inference provider adapter
- [ ] full Evidence-run execution for a new issue

`candidate-ready` is intentionally **not** Candidate Selection. Final comparison and editorial role assignment remain behind the Selection Gate.

## Slice D — Editorial runners

Status: **deterministic comparison, Human Selection Gate, Issue Architecture, structured drafting/rendering, post-draft synthesis, final assembly, and source preflight contracts implemented; live new-issue execution pending**

### Candidate comparison + Human Selection Gate

- [x] deterministic non-ranking Candidate comparison matrix
- [x] temporal relation classification from issue collection window/cutoff
- [x] cutoff-day date-only events remain `TIMING_UNRESOLVED`
- [x] Evidence/source class counts shown as evidence depth, never importance score
- [x] comparison readiness `READY / READY_WITH_CAVEAT / HOLD / REJECT`
- [x] SHA-bound Candidate Selection decision schema
- [x] deterministic Selection template initializer
- [x] every matrix row must receive exactly one role before approval
- [x] Matrix byte changes invalidate the Selection basis
- [x] `HOLD / INSPECT_MORE / REJECT` cannot be silently promoted to positive editorial roles
- [x] `POST_CUTOFF` cannot be silently promoted into normal main-window roles
- [x] explicit `APPROVED` metadata required for the Human Selection Gate

The Selection initializer intentionally leaves ordinary `CANDIDATE` rows `UNASSIGNED`. It only pre-fills roles forced by upstream boundaries (`REJECT -> EXCLUDE`, unresolved Evidence -> `HOLD_OUT`, `POST_CUTOFF CANDIDATE -> LATE_BREAKING`). Editorial priority remains a human decision.

### Issue Architecture

- [x] approved Selection -> SHA-bound Architecture Input package
- [x] selected-only Architecture input; `HOLD_OUT / EXCLUDE` excluded from article planning
- [x] Issue Architecture schema and provider-agnostic prompt
- [x] exact Architecture Input / Matrix / Selection SHA validation
- [x] every selected non-support Evidence Task must be primary exactly once
- [x] `SUPPORTING_EVIDENCE` cannot be silently promoted to primary
- [x] Evidence caveats / remaining boundaries must propagate exactly into package boundaries
- [x] post-cutoff Evidence may be primary only in `LATE_BREAKING`
- [x] page-plan sum / maximum validation
- [x] cover headline deferred until substantive drafts stabilize
- [x] `This Week in AI` synthesis explicitly written after substantive drafts
- [x] explicit Architecture `APPROVED` metadata gate

### Structured article drafting and final assembly

Canonical contract:

```text
APPROVED Issue Architecture
  -> immutable Draft Package per package
  -> provider-agnostic structured Article Draft Result
  -> Evidence/attribution validator
  -> deterministic LaTeX renderer
  -> URL-hash-generated BibLaTeX
  -> generated bibliography merge
  -> post-draft issue synthesis
  -> final weekly source assembly
  -> deterministic source preflight
```

- [x] immutable per-package Draft Package schema/builder
- [x] separate execution stages: `ARTICLE_DRAFTING / POST_DRAFT_SUMMARY / REFERENCE_GENERATION`
- [x] Article Draft Result schema using structured blocks rather than model-authored LaTeX
- [x] stable Evidence refs: `EVENT / CLAIM / METRIC / LIMITATION` + stable Evidence ID
- [x] deck-level Evidence refs and attribution mode
- [x] `PRIMARY_FACT` factual boundary validation
- [x] vendor/project/author claims require attributed treatment
- [x] social Evidence requires `COMMUNITY_NOTE`
- [x] inference cannot silently absorb attributed/social Evidence
- [x] all Architecture-included Evidence Tasks must be materially used
- [x] exact must-cover and boundary coverage validation
- [x] Late Breaking packages require explicit acknowledgement and `LATE_BREAKING_NOTE`
- [x] exact Draft Package / prompt SHA validation
- [x] deterministic renderer maps blocks to shared survey LaTeX semantics
- [x] bibliography keys are generated from source URLs, never chosen by the drafting model
- [x] identical generated Bib entries deduplicate; conflicting metadata is a hard failure
- [x] Draft Result schema / validator alignment regression (`deck_attribution_mode`)
- [x] duplicate parallel Drafting contracts removed; stable-Event-ID path is canonical
- [x] deterministic multi-package final weekly source assembly
- [x] post-draft Cover / `This Week in AI` synthesis validation and rendering
- [x] dynamic internal page labels/references for generated sections
- [x] deterministic final issue source preflight
- [ ] production article-drafting provider adapter
- [ ] first real Draft Package -> model -> validated Article Draft smoke on a new issue
- [ ] first complete generated new-issue source tree / PDF

Latest consolidated drafting/renderer regression before final assembly: `run 31367514904`. Final assembly and preflight contracts were added afterward and are covered by the generic pipeline contract suite.

## Slice E — Weekly PR orchestration

Status: **in progress — weekly work/Draft PR control and reviewed source-intake import implemented; first live new-issue acceptance pending**.

Implemented control surface:

- [x] canonical `weekly/<issue>-work` branch convention
- [x] Draft PR creation/update control that never merges or changes a non-Draft PR
- [x] assistant allowlisted dispatch of safe weekly PR control
- [x] safe fast-forward of an empty/no-unique-work branch to current `main`
- [x] no automatic rewrite/rebase once a work branch contains unique weekly commits
- [x] reviewed source-intake run/artifact verification before acceptance
- [x] append-only collector acceptance with acceptance manifest
- [x] Raw index update/check before work-branch commit
- [x] post-import Draft PR refresh
- [x] contract tests triggered by workflow YAML changes
- [x] W32 real-metadata resolver/branch-gate smoke without modifying Frozen content
- [ ] first successful live W33 source-intake after the 2026-08-14 18:00 New York cutoff
- [ ] first reviewed W33 collector import into `weekly/2026-W33-work`
- [ ] persist validated screening results into the weekly work branch with run/prompt/model/hash provenance
- [ ] persist validated Evidence/editorial stage results without bypassing Selection/Architecture gates
- [ ] orchestrate generated TeX/Bib + final source preflight + PDF build on the weekly Draft PR
- [ ] record Visual Review and Freeze through explicit human gates only

The weekly PR is an auditable work surface. Actions may prepare or refresh it while it remains Draft, but may not infer Candidate Selection approval, Architecture approval, Visual Review approval, Freeze, merge, or public Release authorization.

## Slice F — Chronology + monthly/annual reuse

Status: **design intent established; implementation not started**.
