# W37 Pre-Grok Sol Task Review — r2

Status: `PASS / DRIVE_HANDOFF_AUTHORIZED`

Date: `2026-09-18 JST`

Issue: `2026-W37`

Run: `weekly-x-2026-W37`

Related improvement issue: #505

## Reviewed authority

Generated task:

`sources/2026-W37/external/x/weekly-x-2026-W37/grok-task.md`

SHA-256:

`87bc704428d7c30ea93f633d69146f9a3f12eb24d42b6225f09842725e7c42c7`

Bytes:

`17809`

Common policy:

`config/prompts/grok/x-source-intake-base-v1.md`

SHA-256:

`c514421a82ea54301c34ccd1b001988a6e209834d98d32e6205cb74ca17d2b99`

Weekly overlay:

`config/prompts/grok/x-source-intake-weekly-v1.md`

SHA-256:

`146666912b83763e4b35302e03471625660bec922f5aa1d45e7bb455721b0fdb`

Manifest:

`sources/2026-W37/external/x/x-source-intake-v2.json`

Manifest status remains:

`AWAITING_GROK`

The manifest task authority was rebound to the reviewed task SHA above.

## Edition-specific review

Canonical ordinary window:

- America/New_York: `[2026-09-04T18:00:00-04:00, 2026-09-11T18:00:00-04:00)`
- UTC: `[2026-09-04T22:00:00Z, 2026-09-11T22:00:00Z)`
- JST reference: `[2026-09-05T07:00:00+09:00, 2026-09-12T07:00:00+09:00)`

Drive task path:

`Grok_X_SourseIntake/Weekly/2026-W37/weekly-x-2026-W37/grok-task.md`

Expected result:

`grok-x-result.md`

Stale W36 identity scan:

`0`

## Hardening added for W37

The reviewed task now requires, edition-locally:

1. complete A-L lane scan;
2. a separate open-world / unknown-unknown discovery pass;
3. vendor/model/project-agnostic searches;
4. keyword snowballing from unfamiliar entities;
5. at least one-hop account/post/artifact graph expansion where available;
6. explicit candidate discovery origin;
7. candidate-level direct X URL/account/time/source-role provenance;
8. source-breadth classification:
   - `MULTI_ACCOUNT_X`
   - `SINGLE_SOURCE_X`
   - `OFFICIAL_ONLY_X`
   - `UNVERIFIED_X_REFERENCE`
9. full deduplicated candidate pool, including useful non-selected candidates;
10. run-level breadth metrics;
11. mandatory low-yield expansion when initial discovery is thin;
12. explicit Unexpected/Open-world discoveries result;
13. preservation of X URL provenance for downstream Discovery/community-context use;
14. unchanged boundary that X cannot establish technical facts without primary-source verification.

## W37 diagnostic floors

These are **under-search triggers only**, not quotas or completeness criteria.

A mandatory expansion pass fires if any of the following holds after initial A-L + open-world scan:

- ordinary-window unique X URLs < 12;
- unique independent accounts < 6;
- full deduplicated candidate pool < 8;
- 4 or more lanes remain `NONE_FOUND / NONE_FOUND_CONFIRMED / UNCERTAIN`;
- more than half of strong candidates are single-source or official-only.

The task explicitly prohibits fabricating candidates merely to satisfy these numbers. One complete expansion pass is required; remaining low yield may then be reported honestly as a quiet week or access/search limitation.

## Review verdict

- Issue/run identity: PASS
- canonical window: PASS
- Drive/result identity: PASS
- template authority: PASS
- stale previous-week identity: PASS
- evidence boundary: PASS
- URL provenance requirement: PASS
- low-yield expansion requirement: PASS
- open-world discovery requirement: PASS
- full candidate-pool retention: PASS
- run-health audit: PASS

**Sol verdict: PASS / DRIVE_HANDOFF_AUTHORIZED**

This review is edition-local W37 authority. It does not modify shared Core templates. Issue #505 remains the proposal for reviewed generic implementation in future Weekly/X intake.
