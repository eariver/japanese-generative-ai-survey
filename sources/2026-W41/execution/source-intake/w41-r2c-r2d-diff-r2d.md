# W41 r2c → r2d record-repair diff report

Status: `PROPOSED_NOT_ACCEPTED / SOL_REVIEW_REQUIRED`
Scope: 4 bounded repairs only (mission: Muse r2d Discovery記録整合性修正). No re-search, no new candidates, no re-triage, no acceptance, no downstream stages.
State: `ISSUE_INITIALIZED / stage:discovery` preserved.

## 1. Changed files

- `sources/2026-W41/external/x/x-source-intake-v2.json` (modified): `runs[0].result.discovery_ids` = `["w41-grok-x-ledger-20261012"]` → `["w41-grok-x-ledger-20261011"]`. All other bytes identical.
- `sources/2026-W41/discovery/discovery-v2-proposal-r2d.jsonl` (new): 37 rows, IDs/order preserved from r2c; 13 rows repaired, 24 rows byte-identical (see §2).
- `sources/2026-W41/execution/source-intake/w41-dailyx-92topic-crosswalk-r2d.md` (new): 92/92 one-to-one traceable rows (file/§/heading/URL/ID/Importance/Confidence/event-clock/Discovery-ID/Disposition).
- `sources/2026-W41/execution/source-intake/w41-completeness-report-r2d.md` (new): r2d status + repairs + unchanged counts/lanes/blockers.
- `sources/2026-W41/execution/SOL_DISCOVERY_COMPLETENESS_REVIEW_HANDOFF-r2d.md` (new): Sol review handoff (stop boundary).
- `sources/2026-W41/execution/sessions/muse-w41-r2d-20261012.md` (new): this session record.
- Untouched: `external/daily-x/raw/*` (7 files), `external/x/weekly-x-2026-W41/raw/*`, Core v2, `main`, W40 artifacts, reader drafts, Architecture.

## 2. Proposal row diffs (r2c → r2d, 13 touched / 24 identical)

| # | discovery_id | changed fields | r2d repair |
|---|---|---|---|
| 1 | w41-grok-x-ledger-20261011 | source.title, source.summary_text, provenance.reason | AWAITING_GROK title/summary → RAW_RECEIVED (5332B, sha, 14=12+2, unverified authorship, NanoBanana pointer, NOT accepted) |
| 2 | w41-primary-decisions-beta-20261006 | source.title, source.summary_text, provenance.reason | secondary-only → first-party changelog corroborated (Oct 6 gpt-6-luna/v1/decisions/10x + 8:53pm UTC post + $0.10/M) |
| 3 | w41-primary-clef-omni-20261009 | source.title, provenance.reason | TIME_UNRESOLVED → IN-WINDOW 18:27:34Z; Grok-#10 X post (23:11Z) is post-cutoff, NOT event clock |
| 4 | w41-primary-mistral-large4-20261006 | source.summary_text, provenance.reason | 49B-superseded → 49B/52B version-disagreement preserved (X states 49B; docs 52B; Sol audit) |
| 5 | w41-sweep-negativespace-20261011 | source.summary_text, provenance.reason | stale quiet-audio/serving → r2c-grounded lanes (NOT quiet: audio/embedding/open-weights) |
| 6 | w41-dailyx-textgrain-20261006 | source.observed_at, provenance.reason | 00:00Z → 2026-10-05T22:00:00Z (10-06 report 07:00 JST); PRIMARY kept = blog-exists, body/PDF unread |
| 7 | w41-dailyx-agr-20261006 | source.observed_at, provenance.reason | 00:00Z → 2026-10-05T22:00:00Z; SECONDARY retained (vendor-X-only) |
| 8 | w41-dailyx-nemotron-hf-20261006 | source.observed_at, provenance.reason | 00:00Z → 2026-10-05T22:00:00Z; SECONDARY retained (distribution notice, weights unopened) |
| 9 | w41-dailyx-synthid-portal-20261008 | source.source_type, source.locator, source.metadata.authority_class, source.observed_at, provenance.reason | PRIMARY_OFFICIAL → x-community-signal + x-post: locator + X_OBSERVATION (X-only basis, blog unopened); 00:00Z → 2026-10-07T22:00:00Z |
| 10 | w41-dailyx-stepfun-20261009 | source.observed_at, provenance.reason | 00:00Z → 2026-10-08T22:00:00Z; PRIMARY kept = provider page + issuer X, official model page unread |
| 11 | w41-dailyx-nace-drex-20261010 | source.observed_at, provenance.reason | 00:00Z → 2026-10-09T22:00:00Z; SECONDARY retained (X 21:19:05Z, docs unverified) |
| 12 | w41-dailyx-nace-ndi-20261010 | source.observed_at, provenance.reason | 00:00Z → 2026-10-09T22:00:00Z; SECONDARY retained (X 04:55:00Z, page unfetched) |
| 13 | w41-dailyx-elevenlabs-20261010 | source.observed_at, provenance.reason | 00:00Z → 2026-10-09T22:00:00Z; SECONDARY retained (X 21:11:51Z, specs/WG unverified) |
| — | other 24 rows | — | byte-identical (IDs, order, all fields) |

## 3. Manifest diff (1 line)

- `discovery_ids: ["w41-grok-x-ledger-20261012"]` → `["w41-grok-x-ledger-20261011"]`.
- Basis: `...20261012` never existed in any proposal (r2b typo against r1-origin `...20261011`); existing-ID priority per mission; referential PASS against r2d 37 IDs.

## 4. Crosswalk diff (r2c → r2d)

- r2c: 92 short rows (date + short title + Disposition + Reason only).
- r2d: 92 full rows adding per-topic File path, `### N.` section key, exact original heading, Primary X URL + status ID + Snowflake UTC + DailyX Posted-at + window verdict, Author, Importance/Confidence/Category, Primary source (raw), Related posts (raw), Grok-14 overlap, Event-clock verification status, Discovery ID + Disposition + preserved r2c Reason.
- Dispositions/counts preserved exactly (16/49/3/14/2/8); 2 same-event IDs made explicit (10-07 §9 → Beam row; 10-07 §10 → textGrain row). No topic added/omitted/re-triaged.

## 5. Validation

- Manifest JSON-Schema PASS (`schemas/x-source-intake-v2.schema.json`).
- Proposal 37/37 row-Schema PASS (`schemas/survey-discovery-record.schema.json`); IDs unique; issue `2026-W41` throughout.
- All `raw_paths` resolve to existing repo files.
- Manifest `discovery_ids` ⊆ proposal IDs (referential PASS).
- All `observed_at` ISO-8601 parse PASS; new-8 midnight placeholders eliminated (r2 midnight run-dates preserved out-of-scope, documented).
- Crosswalk 92/92 one-to-one vs raw `### N.` sections (positional + heading-exact check PASS); per-file counts 12/14/14/14/6/16/16 match raw headers.
- Raw originals untouched (no writes under `external/daily-x/raw/`, `external/x/*/raw/`); Core/main/W40 untouched; State `ISSUE_INITIALIZED` preserved.
