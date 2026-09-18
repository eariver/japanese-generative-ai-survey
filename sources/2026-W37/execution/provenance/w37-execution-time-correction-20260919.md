# W37 execution timestamp provenance correction ledger

Status: `EDITION_LOCAL / APPEND_ONLY_CORRECTION / ORIGINAL_BYTES_PRESERVED`

Issue: `2026-W37`

Recorded by: `Independent Sol audit`

Audit wall time:

- JST: `2026-09-19T01:52:58+09:00`
- UTC: `2026-09-18T16:52:58Z`

Generic tracking: Issue #507.

## 1. Purpose

Several W37 execution/Human-Gate metadata timestamps are future-dated or causally impossible.

This ledger does **not** rewrite historical records and does **not** invent replacement event timestamps.

Original committed bytes remain preserved.

Where exact original wall-clock event time is not recoverable from repository authority, this ledger marks the recorded timestamp invalid and uses Git commit times / already-valid Human authority only as ordering evidence or upper bounds, not as fabricated event times.

## 2. Valid wall-clock anchor

At independent audit time:

`2026-09-18T16:52:58Z`

Any W37 execution record claiming to have already occurred after this instant is future-dated and therefore cannot be a valid actual recording time.

## 3. Human Publication Preview r1 timestamp correction

Canonical Human review record:

`sources/2026-W37/gates/reviews/publication-r1.json`

Recorded value:

`reviewed_at = 2026-09-19T03:30:00Z`

Disposition:

`INVALID_AS_ACTUAL_WALL_CLOCK_TIME`

Evidence:

- this value is more than 10 hours after the independent audit wall time;
- the review record is already present in commit `ba0307502978259895a8c6668054eb1e6b585c08`;
- that commit timestamp is `2026-09-18T16:40:18Z`;
- the Human decision authority was already encoded by execution-request commit `2d94f7a837f36015a973166ae104f905d7cd23e9` at `2026-09-18T16:25:55Z`.

Therefore the exact historical Human decision second is not reconstructed here, but it necessarily occurred before the committed review record and cannot be `2026-09-19T03:30:00Z`.

The decision itself remains valid:

`PUBLICATION_PREVIEW r1 / REQUEST_CHANGES`

Only its recorded wall-clock timestamp is corrected by this ledger.

## 4. Worker language-QA timestamp correction

Artifact:

`sources/2026-W37/execution/reviews/worker-w37-draft-r2-language-qa-20260919.json`

Recorded value:

`reviewed_at = 2026-09-19T03:50:00Z`

Disposition:

`INVALID_AS_ACTUAL_WALL_CLOCK_TIME`

Evidence:

- artifact exists in commit `ba0307502978259895a8c6668054eb1e6b585c08`;
- commit timestamp: `2026-09-18T16:40:18Z`;
- recorded review time is after the commit that already contains the review.

Review content/provenance remains usable; exact historical review second is not reconstructed.

## 5. Worker semantic/editorial and visual review timestamp correction

Artifacts:

- `sources/2026-W37/publication/v2/semantic-editorial-review-v2.json`
- `sources/2026-W37/publication/v2/visual-review-v2.json`
- `sources/2026-W37/publication/v2/reader-surface-semantic-review-v2.json`

Recorded values:

`2026-09-19T04:45:00Z`

Disposition:

`INVALID_AS_ACTUAL_WALL_CLOCK_TIME`

Evidence:

- these artifacts are bound in publication-authority commit `74400d716e703c12efee97707ff0ee97d47f98a8`;
- commit timestamp: `2026-09-18T16:46:28Z`;
- recorded review times are after the commit containing the reviews.

The corrected reviewer identity `Worker/Agent (Muse Spark)` is valid; only the recorded wall-clock values are invalid.

## 6. Production State history timestamp correction

Current `sources/2026-W37/production-state.json` contains the following future-dated history values:

- `DISCOVERY_COLLECTED = 2026-09-18T23:11:00Z`
- `CANDIDATES_NORMALIZED = 2026-09-19T00:12:00Z`
- `EVIDENCE_REVIEWED = 2026-09-19T00:22:00Z`
- `SELECTION_COMPLETE = 2026-09-19T00:27:00Z`
- `ARCHITECTURE_ESTABLISHED = 2026-09-19T00:29:00Z`
- `DRAFT_COMPLETE = 2026-09-19T04:00:00Z`
- `VALIDATED_DRAFT = 2026-09-19T05:00:00Z`
- `RELEASE_CANDIDATE = 2026-09-19T05:10:00Z`

At audit time all of these are future-dated except the initial issue timestamp.

Additionally:

- canonical Human Architecture approval is recorded at `2026-09-18T15:47:01Z`;
- that approval necessarily depends on Architecture already being established;
- the State history value `ARCHITECTURE_ESTABLISHED = 2026-09-19T00:29:00Z` would place Architecture establishment **after** its Human approval.

Therefore those State history `recorded_at` values are not valid wall-clock chronology.

Do not use them for chronological analysis.

State transition identities and checkpoint/artifact bindings remain authoritative; exact wall-clock transition seconds are not reconstructed.

## 7. Valid ordering evidence

For audit ordering, the following immutable Git commit timestamps are reliable evidence that the corresponding committed bytes existed no later than those instants:

- `b6c5f9afb4db9e42f2ccb5f63b5da86771001406` — `2026-09-18T13:56:53Z`
- `822c6612e0fed447aacc0375d3de25508d90b0a3` — `2026-09-18T15:23:23Z`
- `2d94f7a837f36015a973166ae104f905d7cd23e9` — `2026-09-18T16:25:55Z`
- `ba0307502978259895a8c6668054eb1e6b585c08` — `2026-09-18T16:40:18Z`
- `74400d716e703c12efee97707ff0ee97d47f98a8` — `2026-09-18T16:46:28Z`
- `ab9f15dcadd120a0d4e72d5c9e4f537980686641` — `2026-09-18T16:47:05Z`

These commit times are **not substituted as exact event times**.

## 8. Publication-content impact

None.

This timestamp defect does not alter:

- Grok/X evidence;
- Discovery/Screening/Evidence;
- Selection/Architecture;
- Human Architecture approval decision;
- Publication Preview r1 REQUEST_CHANGES decision;
- Draft r2 wording;
- reader citations;
- PDF bytes;
- Publication Candidate bytes.

It is an execution/audit metadata defect only.

## 9. Release handling

Until generic Core hardening in Issue #507 is reviewed:

- retain this ledger in W37 release provenance;
- do not quote invalid future-dated `recorded_at/reviewed_at` values as real wall-clock event times;
- use Git history and valid Human authority to establish ordering;
- do not rewrite immutable historical records merely to cosmetically normalize timestamps.

Future Human decisions after this ledger must use actual timezone-aware wall-clock time and must be checked not to post-date the commit containing the decision record.
