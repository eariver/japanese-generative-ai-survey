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
- [ ] first live `source-intake` Actions artifact review for a new issue
- [ ] automatic import PR for reviewed collector artifacts

Validated W32 replay (`run 31359910803`):

- 1,037 screening records total;
- 921 arXiv paper records;
- 103 curated GitHub Release records;
- 10 official feed items;
- 3 official index snapshots;
- 39 bounded screening batches.

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
- [x] metric context and limitation fields
- [x] exact Evidence Task / prompt SHA validation
- [x] source-reference integrity checks
- [x] verification-target completeness checks
- [x] resumable Evidence Run merge
- [x] `CANDIDATE / HOLD / INSPECT_MORE / REJECT` queues
- [x] deterministic pre-selection Candidate Record materializer
- [x] real primary-source smoke using the llama.cpp / DeepSeek V4 support series
- [ ] production Evidence inference provider adapter
- [ ] full Evidence-run execution for a new issue

`candidate-ready` is intentionally **not** Candidate Selection. Final comparison and editorial role assignment remain behind the Selection Gate.

## Slice D — Editorial runners

Status: **pre-selection comparison + Human Selection Gate implemented; architecture/drafting runners pending**

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
- [ ] Issue Architecture generator / contract
- [ ] article-drafting package runners
- [ ] citation/claim consistency preflight reuse as a general weekly stage

Latest Selection Gate regression: `run 31365181817`, test job passed.

The Selection initializer intentionally leaves ordinary `CANDIDATE` rows `UNASSIGNED`. It only pre-fills roles forced by upstream boundaries (`REJECT -> EXCLUDE`, unresolved Evidence -> `HOLD_OUT`, `POST_CUTOFF CANDIDATE -> LATE_BREAKING`). Editorial priority remains a human decision.

## Slice E — Weekly PR orchestration

Status: not started.

Primary target: turn reviewed collection/screening/evidence artifacts into an auditable weekly PR without allowing Actions to bypass the Selection or Freeze gates.

## Slice F — Chronology + monthly/annual reuse

Status: design intent established; implementation not started.
