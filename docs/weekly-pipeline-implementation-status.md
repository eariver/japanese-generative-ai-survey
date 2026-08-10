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

## Slice B — Source intake contracts

Status: **implemented baseline; live weekly operational validation pending**

- [x] pre-execution collector instruction schema
- [x] post-execution collector-run provenance schema
- [x] immutable Raw SHA-256 index/check
- [x] automatic Raw-integrity CI
- [x] W32 Raw provenance baseline
- [x] issue-specific Grok Trend Sensor instruction generator
- [x] arXiv API intake adapter
- [x] curated GitHub Releases intake adapter
- [x] configured official news/blog page snapshot adapter
- [x] HTTP-mocked intake unit tests
- [x] append-only run-specific collector paths
- [ ] first live `source-intake` Actions artifact review for a new issue
- [ ] automatic import PR for reviewed collector artifacts
- [ ] duplicate/artifact/event normalization helper

Current collector Raw layout:

```text
sources/<issue>/collectors/<collector>/runs/<observed-at>/
├─ raw/
├─ summary.json
└─ collector-run.json
```

Raw bytes are immutable after acceptance; `summary.json` is derived discovery metadata and is not a technical Evidence Card.

## GitHub Release distribution

Status: **implemented; validate-mode smoke test pending**

- [x] frozen release manifest schema
- [x] W32 release manifest
- [x] canonical tag convention `weekly/<issue>/<revision>`
- [x] `validate` mode with no tag/Release write
- [x] `draft` mode with exact PDF digest check
- [x] re-runnable Draft verification without asset clobber
- [x] `publish` requires existing verified Draft
- [x] Release PDF + `SHA256SUMS.txt`
- [x] W32 exact frozen Actions-artifact source
- [x] future reproducible rebuild source mode
- [x] optional immutable-release attestation verification after publish
- [ ] W32 Release workflow `validate` smoke test
- [ ] W32 Draft Release creation/review
- [ ] repository Immutable Releases setting decision/enablement
- [ ] first published weekly Release

## Slice C — Evidence runners

Status: **not started as automation**

W32 provides manual reference artifacts, but provider/model-agnostic automated runners are not yet implemented.

Next targets:

1. candidate normalization contract;
2. screening/evidence schemas;
3. primary verification runner;
4. full/targeted paper-review runner;
5. social normalization v0.2;
6. provider/model/prompt/tool provenance.

## Slice D — Editorial runners

Status: manual/LLM-assisted reference exists from W32; automation not yet implemented.

## Slice E — Weekly PR orchestration

Status: not started.

## Slice F — Chronology + monthly/annual reuse

Status: design intent established; implementation not started.
