# Survey Production execution index — 2026-W33

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/2026-W33/production-state.json`.

> Crash / session recovery entry point: **start from this file**. Read `production-state.json`, then the latest session record and active Sol→Luna handoff listed below. Repository state outranks chat history.

## Current authority

- Issue / edition: `2026-W33`
- Research Profile: `WEEKLY`
- Publication Profile: `WEEKLY_MAGAZINE`
- Work branch: `weekly/2026-W33-v2-work`
- Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Last verified work-branch head before the current handoff commit: `61d156dd2512bcc37e53bcec8a6dfee8e3bf7c7b`
- Run started: `2026-08-29T01:35:36Z`
- Requested stop: `ARCHITECTURE_REVIEW`
- Production Profile: `sources/2026-W33/production-profile.json`
- Production State: `sources/2026-W33/production-state.json`
- Current lifecycle: `ISSUE_INITIALIZED`
- Current terminal reason: `none`
- Current next machine action: `stage:discovery`
- Current semantic status: `LUNA_HANDOFF_SPECIFIED`

## Human Gates

- Architecture Review: `pending`
- Publication Preview: `pending`
- Detailed review records: none recorded yet

## Sol / Luna operating split

- Sol (`Chat GPT-5.6 Sol`): semantic authority — scope, research strategy, cross-source interpretation, Screening/Evidence judgment, Materiality, Completeness closure, Selection, Architecture, editorial review, and review of Luna output.
- Luna (`Work GPT-5.6 Luna`): bounded worker — source-local collection, exact-byte recovery, schema-conforming materialization, deterministic validation, prescribed Git/operator actions, and machine-readable/reporting work under an explicit task specification.
- Deterministic Core: schema/invariant/provenance/checkpoint/lifecycle execution only; it does not make editorial judgments or Human Gate decisions.
- Human: explicit normal-Gate decisions and genuine Owner Exception decisions.
- Luna must not invent scope, add unapproved sources to close gaps, perform cross-document interpretation, decide Selection/Architecture, or infer Human Gate decisions. Ambiguity returns to Sol as `PARTIAL`, `UNRESOLVED`, `NEEDS_SOL_REVIEW`, or equivalent task-specific review status.

## Recovery / work records

- Core 0.15 handoff: `docs/checkpoints/2026-W33-core015-handoff-20260829.md`
- Initial Core 0.15 session: `sessions/w33-core015-20260829-r1.md`
- Sol/Luna transition session: `sessions/w33-sol-luna-transition-20260829-r2.md`
- Latest Sol specification session: `sessions/w33-sol-discovery-spec-20260829-r3.md`
- **Active Luna task:** `handoffs/w33-discovery-rebuild-luna-r1.md`
- Active Luna task endpoint: materialize and commit the Discovery candidate; **do not advance Production State**; return to Sol for semantic review.

For both Sol and Luna, update or add an edition-local session/work record at material milestones so a crash can be recovered without chat history. Prefer concise stage-level checkpoints rather than tool-call transcripts.

## Discovery rebuild decision

- Historical semantic seed: `temp/w33-discovery-stage@a52e95c42ee09d46b3b0c89f0dfb99ed2bc988c8`, exactly 37 records.
- Historical accepted/checkpoint/state artifacts are not current authority and must not be restored.
- Expected current candidate: 41 records = preserved 37-record seed with X provenance rebound to postmerge Raw + exactly four model-release gap-fill records.
- Four Sol-frozen additions: Grok 4.6, Qwen3.8 W33 open-weight expansion, Gemini 3.7 Flash, GLM-5.3.
- Candidate acceptance/state advancement is deferred until Sol reviews Luna's worker commit.

## Grok/X

- Profile applicability policy: `REQUIRED_BY_PROFILE`
- Canonical reconstruction run: `weekly-x-2026-W33-postmerge-r1`
- Drive task path: `Grok_X_SourseIntake/Weekly/2026-W33/weekly-x-2026-W33-postmerge-r1/grok-task.md`
- Exact task: 9612 bytes / SHA-256 `c86a6124bb0ff32832995883d37b7f44e08da7142af4ac39032fb7436035b356`
- Exact result: 12171 bytes / SHA-256 `93fe6b8c2eeea4e3186868f79927108edacebc26d8ff23f1bcc38ac1080e1f06`
- Current canonical result disposition: pending Luna materialization and Sol review before Discovery acceptance.

## Publication Candidate

- Current Human review target: none recorded yet
- Candidate SHA-256: none
- PDF SHA-256: none

## Deviations

- Production execution is organized into a Sol semantic-control plane plus Luna bounded-worker plane. This is an edition-local operating split; shared Core authority is not modified during W33 production.
- Multiple Chat/Sol connection/session interruptions occurred during preparation; repository checkpoints have been used as the recovery authority.

## Shared Core defects

- None currently recorded.

## Final disposition

`IN_PROGRESS`
