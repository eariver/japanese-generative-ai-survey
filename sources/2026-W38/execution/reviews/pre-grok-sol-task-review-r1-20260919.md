# W38 Pre-Grok Sol Task Review — r1

Status: `PASS / DRIVE_HANDOFF_AUTHORIZED_AFTER_HARDENING`

Date: `2026-09-19 JST`

Issue: `2026-W38`

Run: `weekly-x-2026-W38`

Related generic improvement issue: #505

## Reviewed authority

Generated and Sol-hardened task:

`sources/2026-W38/external/x/weekly-x-2026-W38/grok-task.md`

SHA-256:

`20cbf5b40f834d6d6ce469eb9c80ad9dc5ecc73c65350e24928d44fa9cad3e19`

Bytes:

`26057`

Common policy:

`config/prompts/grok/x-source-intake-base-v1.md`

SHA-256:

`c514421a82ea54301c34ccd1b001988a6e209834d98d32e6205cb74ca17d2b99`

Weekly overlay:

`config/prompts/grok/x-source-intake-weekly-v1.md`

SHA-256:

`146666912b83763e4b35302e03471625660bec922f5aa1d45e7bb455721b0fdb`

Manifest:

`sources/2026-W38/external/x/x-source-intake-v2.json`

Manifest status remains:

`AWAITING_GROK`

The manifest task authority is rebound to the exact reviewed task SHA above.

## Canonical W38 window

- America/New_York: `[2026-09-11T18:00:00-04:00, 2026-09-18T18:00:00-04:00)`
- UTC: `[2026-09-11T22:00:00Z, 2026-09-18T22:00:00Z)`
- JST: `[2026-09-12T07:00:00+09:00, 2026-09-19T07:00:00+09:00)`
- end-exclusive

Drive task path:

`Grok_X_SourseIntake/Weekly/2026-W38/weekly-x-2026-W38/grok-task.md`

Expected result:

`grok-x-result.md`

## Baseline review

The generated W38 task already retained the accepted W37 hardening:

1. complete A-L lane scan;
2. open-world / unknown-unknown pass;
3. keyword snowballing and account/artifact graph expansion;
4. candidate-level direct X URL provenance;
5. source-breadth classes;
6. full deduplicated candidate pool;
7. low-yield diagnostics and mandatory expansion;
8. run-health audit;
9. downstream X provenance boundary;
10. X remains Raw Observation, never technical Evidence authority.

## Additional Sol hardening added before Drive handoff

The pre-handoff audit identified residual failure modes demonstrated by W37 r2/r3 and added explicit controls:

### A. Temporal misclassification prevention

Every retained direct status URL must carry a status-ID-derived UTC time when possible and an explicit PRE_WINDOW / ORDINARY_WINDOW / LATE_BREAKING / TIME_UNVERIFIED class.

Search filters, prose timestamps and UI-relative labels are not temporal authority.

TIME_UNVERIFIED cannot inflate ordinary breadth.

### B. Account-role discipline

`INDEPENDENT` now requires non-affiliated first-hand technical testing/reproduction/integration/measurement/original analysis.

Commentary/aggregation/unclear affiliation is conservatively `COMMUNITY`.

Only role-`INDEPENDENT` accounts count toward the independent-account diagnostic.

### C. Ledger-derived count reconciliation

A final unique-status-ID ledger is mandatory and all summary counts must be recomputed from it.

The task requires `LEDGER_COUNT_CONSISTENCY: PASS` before finalization.

This directly addresses W37 r3's derived-summary discrepancies even though its row-level ledger was correct.

### D. Ordinary-window isolation

Pre-window and Late Breaking rows cannot inflate ordinary candidate breadth or ordinary strong-candidate classification.

### E. Anti-blindspot search

A non-English anti-blindspot pass is required, including Japanese and ecosystem-appropriate terminology where material.

### F. Primary-source URL integrity

Grok must not guess official/documentation/repository/paper URLs. Unlocated sources are recorded explicitly as `PRIMARY_SOURCE_TO_LOCATE`.

### G. Strong-candidate adversarial search

Every strong candidate requires a targeted counter-signal/failure/constraint search or explicit `NO_COUNTER_SIGNAL_FOUND_AFTER_TARGETED_SEARCH`.

### H. Access-limitation fail-closed rule

If X access/search quality prevents the required audit surfaces from being completed, the result must say `INCOMPLETE_DUE_TO_ACCESS_LIMITATION` rather than claiming complete coverage.

## Prior failure modes specifically addressed

- low URL/candidate yield without mandatory expansion;
- known-vendor-only search bias;
- missing unknown-unknown discovery;
- ordinary/Late Breaking boundary mistakes;
- relying on prose/UI timestamps rather than status-ID time;
- COMMUNITY accounts counted as INDEPENDENT;
- summary/count arithmetic disagreeing with row-level URL ledger;
- Late Breaking URLs inflating ordinary breadth;
- source/account duplication inflating apparent corroboration;
- guessed primary-source URLs;
- confirmation bias around strong candidates;
- silent degradation when X access/search quality is poor.

## Verdict

- issue/run identity: PASS
- canonical window: PASS
- Drive/result identity: PASS
- common/weekly policy authority: PASS
- baseline W37 hardening: PASS
- temporal-integrity hardening: PASS
- role/affiliation hardening: PASS
- ledger/count reconciliation: PASS
- ordinary-window isolation: PASS
- anti-blindspot pass requirement: PASS
- primary-source URL integrity: PASS
- adversarial/counter-signal requirement: PASS
- access-limitation fail-closed behavior: PASS
- evidence boundary: PASS

**Sol verdict: PASS / DRIVE_HANDOFF_AUTHORIZED_AFTER_HARDENING**

This is edition-local W38 authority. Shared Core/templates were not modified.
