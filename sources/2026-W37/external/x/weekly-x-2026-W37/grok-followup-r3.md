# Grok X Source Intake Follow-up — W37 r3 canonical-window correction + mandatory expansion

Status: `W37_EDITION_LOCAL / GROK_FOLLOWUP_R3 / WINDOW_RECLASSIFICATION_AND_REQUIRED_EXPANSION`

Issue: `2026-W37`

Original run:

`weekly-x-2026-W37`

Prior artifacts:

- `grok-task.md`
- `grok-x-result.md` (r1)
- `grok-followup-r2.md`
- `grok-x-result-r2.md` (r2)

Required new result filename:

`grok-x-result-r3.md`

Do **not** overwrite any prior artifact.

## 1. Why r3 is required

r2 successfully materialized 35 direct X post URLs and substantially improved provenance auditability.

However, r2 classified many posts after the W37 editorial cutoff as `ordinary`.

Canonical W37 ordinary window is:

America/New_York:

`[2026-09-04T18:00:00-04:00, 2026-09-11T18:00:00-04:00)`

UTC authority:

`[2026-09-04T22:00:00Z, 2026-09-11T22:00:00Z)`

JST reference:

`[2026-09-05T07:00:00+09:00, 2026-09-12T07:00:00+09:00)`

The end is exclusive.

Therefore:

- any post timestamp **before** `2026-09-04T22:00:00Z` is `PRE_WINDOW_CARRY_IN`;
- any post timestamp `>= 2026-09-04T22:00:00Z` and `< 2026-09-11T22:00:00Z` is `ORDINARY_WINDOW`;
- any post timestamp `>= 2026-09-11T22:00:00Z` is `LATE_BREAKING`.

Do not use calendar date alone. Compare the actual timestamp against the exact UTC boundaries.

Sol independent audit of the timestamps written in r2 found:

- total direct URLs: `35`
- expected `PRE_WINDOW_CARRY_IN`: `1`
- expected `ORDINARY_WINDOW`: `14`
- expected `LATE_BREAKING`: `20`

These expected counts are a **sanity check**, not a value to force. Re-read/reconfirm the actual post timestamps where possible. If a verified timestamp differs from the timestamp written in r2, record the discrepancy explicitly and use the verified timestamp.

## 2. Preserve r1 and r2 as immutable history

Do not edit:

- `grok-x-result.md`
- `grok-x-result-r2.md`

Create only:

`grok-x-result-r3.md`

r3 must explicitly mark:

- `R2_WINDOW_RECLASSIFIED`
- `R2_TIMESTAMP_CORRECTED`
- `NEW_R3_OBSERVATION`
- `R2_CLAIM_DOWNGRADED`
- `R2_CLAIM_RECONFIRMED`

where applicable.

## 3. Phase A — canonical reclassification of all 35 r2 URLs

Start from the **Full direct-X URL ledger** in r2.

For every one of the 35 unique direct X post URLs:

1. preserve the direct URL;
2. preserve/reconfirm account handle and role;
3. preserve/reconfirm the actual X post timestamp;
4. convert/express timestamp in UTC;
5. classify against the exact W37 UTC boundaries above;
6. assign exactly one:
   - `PRE_WINDOW_CARRY_IN`
   - `ORDINARY_WINDOW`
   - `LATE_BREAKING`;
7. record candidate ID(s);
8. record whether the timestamp/classification changed from r2.

The r3 ledger must contain all 35 r2 URLs even when they become Late Breaking or pre-window.

Do not silently discard misclassified r2 rows.

## 4. Phase B — exact ordinary-window audit before expansion

After reclassification, recompute using **ORDINARY_WINDOW rows only**:

- ordinary unique direct X URLs;
- ordinary unique accounts;
- ordinary unique independent accounts;
- ordinary unique official accounts;
- candidate-level ordinary URL count;
- candidate-level ordinary independent-account count;
- strong-candidate source-breadth classification.

Do not allow Late Breaking or pre-window posts to support an ordinary-window breadth classification.

In particular, re-evaluate C1–C4.

### Expected sanity check from Sol audit of r2 timestamps

Based on the timestamps currently written in r2:

- ordinary-window direct URLs: `14`;
- ordinary-window unique independent accounts: `4`.

Strong-candidate ordinary-window state appears approximately:

- C1 GPT-6 Astra: 3 ordinary URLs, 0 independent ordinary accounts;
- C2 DeepSeek-V4.1-Flash: 5 ordinary URLs, 2 independent ordinary accounts;
- C3 SWE-2/Fusion: 2 ordinary URLs, 1 independent ordinary account;
- C4 MiniCPM5-2B: 2 ordinary URLs, 1 independent ordinary account.

Again, independently re-evaluate from the actual timestamps. If exact verified data differs, report the difference.

## 5. Phase C — mandatory expansion decision

After Phase B, apply the W37 diagnostic triggers using only correctly classified ordinary-window evidence.

Trigger mandatory expansion if **any** condition holds:

- ordinary-window unique direct X URLs < `12`;
- ordinary-window unique independent accounts < `6`;
- full candidate pool < `8`;
- 4 or more lanes remain `NONE_FOUND`, `NONE_FOUND_CONFIRMED`, or `UNCERTAIN`;
- more than half of strong candidates are `SINGLE_SOURCE_X` or `OFFICIAL_ONLY_X` on **ordinary-window evidence only**.

Sol audit indicates at least one trigger already fires:

`ordinary-window unique independent accounts = 4 < 6`

Also, C1/C3/C4 ordinary-window breadth must be rechecked because Late Breaking rows were previously counted toward `MULTI_ACCOUNT_X`.

Therefore, unless independently verified timestamps materially change this state, **the mandatory expansion pass is required**.

## 6. Phase D — mandatory expansion pass

The expansion objective is not to reach a quota mechanically. It is to test whether the ordinary W37 window was under-searched.

Search only for observations whose X post timestamps fall inside:

`[2026-09-04T22:00:00Z, 2026-09-11T22:00:00Z)`

Prioritize:

1. independent developers/researchers/users discussing C1 GPT-6 Astra **inside the ordinary window**;
2. independent C3 SWE-2 / Fusion / coding-agent evidence inside the window;
3. independent C4 MiniCPM5-2B evidence inside the window;
4. C2 independent DeepSeek evidence if useful;
5. weak lanes, especially D / E / I, using alternate technical vocabulary;
6. open-world terms discovered in r1/r2, but only when the supporting post is ordinary-window;
7. failed reproduction, disagreement, operational constraints, regressions, cost/latency, integrations, local inference, serving/runtime and grassroots developer use.

Expansion techniques must include:

- alternate keyword framing;
- vendor/model-name-agnostic search where useful;
- keyword snowballing;
- account graph / quote / reply / related-account expansion;
- OSS maintainer / evaluator / practitioner search.

Do not search after the cutoff merely because those posts are easy to find. Post-cutoff material belongs only in Late Breaking.

## 7. New r3 URL requirements

Every newly discovered r3 source must contain:

- direct X status URL;
- account;
- role `OFFICIAL / INDEPENDENT / COMMUNITY`;
- exact/available timestamp;
- UTC-normalized timestamp;
- candidate ID or new candidate ID;
- discovery origin;
- `ORDINARY_WINDOW / LATE_BREAKING / PRE_WINDOW_CARRY_IN`;
- why material;
- `NEW_R3_OBSERVATION`.

Do not count a source toward the ordinary diagnostic unless its timestamp is demonstrably inside the canonical ordinary window.

## 8. Recompute candidate breadth after expansion

For every C1–C10, and any new candidate, recompute:

- ordinary-window URL count;
- ordinary independent-account count;
- late-breaking URL count;
- pre-window URL count;
- source-breadth classification for **ordinary-window community evidence**.

Allowed ordinary-window classifications:

- `MULTI_ACCOUNT_X` — at least two independent/non-affiliated ordinary-window accounts;
- `SINGLE_SOURCE_X` — one usable ordinary-window independent/community account;
- `OFFICIAL_ONLY_X` — ordinary evidence is official only;
- `UNVERIFIED_X_REFERENCE` — no usable direct ordinary-window post.

Late Breaking evidence may be retained separately but must not upgrade ordinary-window classification.

## 9. Exact final audit

The final r3 audit must use exact integers, derived from the actual ledger.

Report separately:

### All retained URLs
- total unique direct X URLs;
- total accounts.

### Ordinary window
- unique direct X URLs;
- unique accounts;
- unique independent accounts;
- unique official accounts.

### Late Breaking
- unique direct X URLs;
- unique accounts.

### Pre-window carry-in
- unique direct X URLs;
- unique accounts.

### Candidate audit
- full candidate-pool count;
- candidates with zero ordinary direct URLs;
- ordinary `MULTI_ACCOUNT_X` count;
- ordinary `SINGLE_SOURCE_X` count;
- ordinary `OFFICIAL_ONLY_X` count;
- ordinary `UNVERIFIED_X_REFERENCE` count;
- strong-candidate classifications before and after expansion;
- new ordinary-window URLs found in r3;
- new ordinary independent accounts found in r3.

### Expansion audit
- which trigger(s) fired;
- exact searches/expansion methods performed;
- whether the trigger remains below floor after one complete expansion pass.

If after the required expansion ordinary independent accounts remain <6, report that honestly. Do not invent or misclassify sources.

## 10. Full output structure

The r3 result must contain:

1. **r3 scope and relation to r1/r2**
2. **Canonical W37 window authority**
3. **Reclassified r2 35-URL ledger**
4. **Corrections to r2 window classifications**
5. **Pre-expansion ordinary-window audit**
6. **Mandatory expansion trigger decision**
7. **Expansion search log**
8. **New r3 observations**
9. **Final direct-X ledger**
10. **Final candidate-level ordinary/late/pre-window classifications**
11. **Final exact run-health / breadth audit**
12. **Corrections / downgrades from r2**
13. **Remaining limitations**
14. **Primary-source candidates for downstream verification**

## 11. Evidence boundary remains unchanged

X remains:

`Raw Observation / community signal`

Do not use X alone to establish technical facts such as:

- specifications;
- benchmark truth;
- pricing;
- licensing;
- context length;
- parameter count;
- architecture;
- release availability;
- security/capability claims.

Preserve direct X provenance for downstream Discovery/community context, while downstream ChatGPT/Sol independently verifies technical claims from primary sources.

## 12. Save location

Save only as:

`Grok_X_SourseIntake/Weekly/2026-W37/weekly-x-2026-W37/grok-x-result-r3.md`

Do not overwrite any prior task/result/follow-up file.

If that filename already exists, use the next revision suffix and report the actual filename.
