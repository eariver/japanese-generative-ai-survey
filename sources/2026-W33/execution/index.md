# Survey Production execution index — 2026-W33

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/2026-W33/production-state.json`.

> Crash / session recovery entry point: **start from this file**. Read `production-state.json`, then the latest session record and active Sol→Luna handoff listed below. Repository state outranks chat history.

## Current authority

- Issue / edition: `2026-W33`
- Research Profile: `WEEKLY`
- Publication Profile: `WEEKLY_MAGAZINE`
- Work branch: `weekly/2026-W33-v2-work`
- Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Last verified pre-transition work-branch head: `22966dfa7af176243396ba564e2555d14e1b5fdf`
- Run started: `2026-08-29T01:35:36Z`
- Requested stop: `ARCHITECTURE_REVIEW`
- Production Profile: `sources/2026-W33/production-profile.json`
- Production State: `sources/2026-W33/production-state.json`
- Current lifecycle: `ISSUE_INITIALIZED`
- Current terminal reason: `none`
- Current next action: `stage:discovery`

## Human Gates

- Architecture Review: `pending`
- Publication Preview: `pending`
- Detailed review records: none recorded yet

## Sol / Luna operating split

- Sol (`Chat GPT-5.6 Sol`): semantic authority — scope, research strategy, cross-source interpretation, Screening/Evidence judgment, Materiality, Completeness closure, Selection, Architecture, editorial review, and review of Luna output.
- Luna (`Work GPT-5.6 Luna`): bounded worker — source-local collection, exact-byte recovery, schema-conforming materialization, deterministic validation, prescribed Git/operator actions, and machine-readable/reporting work under an explicit task specification.
- Deterministic Core: schema/invariant/provenance/checkpoint/lifecycle execution only; it does not make editorial judgments or Human Gate decisions.
- Human: explicit normal-Gate decisions and genuine Owner Exception decisions.
- Luna must not invent scope, add unapproved sources to close gaps, perform cross-document interpretation, decide Selection/Architecture, or infer Human Gate decisions. Ambiguity returns to Sol as `PARTIAL`, `UNRESOLVED`, or equivalent task-specific review status.

## Recovery / work records

- Core 0.15 handoff: `docs/checkpoints/2026-W33-core015-handoff-20260829.md`
- Initial Core 0.15 session: `sessions/w33-core015-20260829-r1.md`
- Sol/Luna transition session: `sessions/w33-sol-luna-transition-20260829-r2.md`
- Active Luna task: pending Sol specification; when created it will be linked here under `handoffs/`.

For both Sol and Luna, update or add an edition-local session/work record at material milestones so a crash can be recovered without chat history. Prefer concise stage-level checkpoints rather than tool-call transcripts.

## Publication Candidate

- Current Human review target: none recorded yet
- Candidate SHA-256: none
- PDF SHA-256: none

## Grok/X

- Profile applicability policy: `REQUIRED_BY_PROFILE`
- Historical/recovered W33 X material has been audited by Sol, but no Core 0.15 canonical X intake is currently accepted on this reset branch.
- Sol audit identified the later `weekly-x-2026-W33-postmerge-r1` run as the intended canonical reconstruction input, subject to exact-byte/current-schema materialization before Discovery acceptance.
- Current canonical result disposition: pending Core 0.15 Discovery rebuild.

## Deviations

- Production execution is being reorganized into a Sol semantic-control plane plus Luna bounded-worker plane. This is an edition-local operating split; shared Core authority is not modified during W33 production.

## Shared Core defects

- None currently recorded.

## Final disposition

`IN_PROGRESS`
