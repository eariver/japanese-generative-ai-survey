# Survey Production execution index — 2026-W33

This is the current human-readable navigation record for the edition. Machine lifecycle authority remains `sources/2026-W33/production-state.json`.

> Crash / session recovery entry point: **start from this file**. Read `production-state.json`, then the latest session record and active Sol→Luna handoff listed below. Repository state outranks chat history.

## Current authority

- Issue / edition: `2026-W33`
- Research Profile: `WEEKLY`
- Publication Profile: `WEEKLY_MAGAZINE`
- Work branch: `weekly/2026-W33-v2-work`
- Reviewed `main`: `6267de3f6876f491950139757bfdf1085fc07bdc`
- Luna worker starting SHA: `78ad4289deac13c22f67d3ec8c7c0f68a55af6eb`
- Run started: `2026-08-29T01:35:36Z`
- Requested stop: `ARCHITECTURE_REVIEW`
- Production Profile: `sources/2026-W33/production-profile.json`
- Production State: `sources/2026-W33/production-state.json`
- Current lifecycle before deterministic Discovery advancement: `ISSUE_INITIALIZED`
- Current terminal reason: `none`
- Current next machine action before advancement: `stage:discovery`
- Current semantic status: `SOL_DISCOVERY_ACCEPTED_REMOTE_MATERIALIZATION_PENDING_CORE`

## Human Gates

- Architecture Review: `pending`
- Publication Preview: `pending`
- Detailed Human review records: none recorded yet

## Sol / Luna operating split

- Sol (`Chat GPT-5.6 Sol`): semantic authority — scope, research strategy, cross-source interpretation, Screening/Evidence judgment, Materiality, Completeness closure, Selection, Architecture, editorial review, and review of Luna output.
- Luna (`Work GPT-5.6 Luna`): bounded worker — source-local collection, exact-byte recovery, schema-conforming materialization, deterministic validation, prescribed Git/operator actions, and machine-readable/reporting work under an explicit task specification.
- Deterministic Core: schema/invariant/provenance/checkpoint/lifecycle execution only; it does not make editorial judgments or Human Gate decisions.
- Human: explicit normal-Gate decisions and genuine Owner Exception decisions.

## Recovery / work records

- Core 0.15 handoff: `docs/checkpoints/2026-W33-core015-handoff-20260829.md`
- Initial Core 0.15 session: `sessions/w33-core015-20260829-r1.md`
- Sol/Luna transition session: `sessions/w33-sol-luna-transition-20260829-r2.md`
- Sol Discovery specification: `sessions/w33-sol-discovery-spec-20260829-r3.md`
- Luna Discovery worker record: `sessions/w33-luna-discovery-rebuild-20260829-r1.md`
- Latest Sol review session: `sessions/w33-sol-discovery-review-20260829-r4.md`
- Sol review detail: `reviews/w33-discovery-sol-review-20260829-r4.md`
- Luna handoff specification: `handoffs/w33-discovery-rebuild-luna-r1.md`

For both Sol and Luna, update or add an edition-local session/work record at material milestones so a crash can be recovered without chat history. Prefer concise stage-level checkpoints rather than tool-call transcripts.

## Discovery rebuild decision

- Historical semantic seed: `temp/w33-discovery-stage@a52e95c42ee09d46b3b0c89f0dfb99ed2bc988c8`, exactly 37 records.
- Exact Luna candidate from attached patch: 125,343 bytes / SHA-256 `784e20b7fb46794a34185a949b6f9e95241203ff4128aa0633fe6182f1701357` / Git blob `9de304a382c1e0ae3adcf532b05220b1879e2244`.
- Sol semantic review: `ACCEPT`.
- Canonical remote Discovery materialization: 41 records; preserves all IDs/provenance/locators/Raw bindings and concise X/carry-over/feed/gap-fill summaries; long BASE collector-expanded summaries are omitted because exact Raw is restored.
- Canonical remote Discovery SHA-256: `632ba2335e5b937e9c6401c965edba735637631c7ef66551a070d7455a82f3b0`.
- Canonical remote Discovery Git blob: `109b447ce4e6233cf18b91a7f3ad89f2c0e95b21`.
- Four Sol-frozen additions: Grok 4.6, Qwen3.8 W33 open-weight expansion, Gemini 3.7 Flash, GLM-5.3.
- Historical accepted/checkpoint/state artifacts remain non-authoritative and were not restored.

## Grok/X

- Profile applicability policy: `REQUIRED_BY_PROFILE`
- Canonical run: `weekly-x-2026-W33-postmerge-r1`
- Exact task: 9,612 bytes / SHA-256 `c86a6124bb0ff32832995883d37b7f44e08da7142af4ac39032fb7436035b356`
- Exact result: 12,171 bytes / SHA-256 `93fe6b8c2eeea4e3186868f79927108edacebc26d8ff23f1bcc38ac1080e1f06`
- X manifest state: `COMPLETE`; result `SUCCESS`; discovery disposition `DISCOVERY_RECORDED` → `x-weekly-signal-wave`.
- X remains discovery/community signal only until primary-source Evidence work.

## Next deterministic action

- Materialize/read back the candidate commit on the remote work branch.
- Build the current canonical Discovery acceptance against that exact branch tree.
- Execute the trusted Core `ADVANCE_STAGE` bridge from `ISSUE_INITIALIZED` to `DISCOVERY_COLLECTED` only after stage validation passes.
- Do not begin semantic Screening until Discovery advancement is confirmed and a new Sol/Luna boundary is recorded.

## Publication Candidate

- Current Human review target: none recorded yet
- Candidate SHA-256: none
- PDF SHA-256: none

## Deviations

- Production execution uses an edition-local Sol semantic-control plane plus Luna bounded-worker plane; shared Core is unchanged.
- Luna's local commits were not published by its environment. Sol reconstructed and reviewed the attached patch, then used the connected GitHub writer for remote materialization.
- The connected writer cannot ingest a mounted local file directly as a Git blob parameter. Sol therefore materialized a canonical Discovery representation that keeps all load-bearing identity/provenance/Raw bindings and defers long BASE collector-expanded text to exact Raw. The exact Luna candidate identity remains recorded for audit.

## Shared Core defects

- None currently recorded.

## Final disposition

`IN_PROGRESS`
