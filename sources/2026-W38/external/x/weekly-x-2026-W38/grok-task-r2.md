# W38 Grok/X Source Intake — r2 correction and mandatory expansion task


Status: `W38_EDITION_LOCAL / R2_CORRECTION_REQUIRED / R1_NOT_CANONICAL`


Issue: `2026-W38`


Run: `weekly-x-2026-W38`


## 1. Inputs and precedence


First read the original task in this same Drive folder:


`grok-task.md`


Then read this file completely.


The original task remains the baseline authority. This r2 file adds a bounded correction requirement after Sol rejected the first result.


Existing r1 result:


`grok-x-result.md`


Do not overwrite or delete r1.


Write the corrected result as:


`grok-x-result-r2.md`


The result remains Raw Observation/community signal, never final technical Evidence.


## 2. Why r2 is mandatory


Sol independently audited r1 and found that it does not satisfy the exact task.


The main failures are:


- Snowflake temporal verification was explicitly skipped;
- two URLs treated as ordinary are actually after the W38 cutoff;
- the required final direct-X ledger was replaced by a sample list;
- direct URLs were replaced by ellipses/prose for several claimed supports;
- run-health counts are approximate rather than ledger-derived;
- row-level roles are missing;
- `LEDGER_COUNT_CONSISTENCY: PASS` is therefore unsupported;
- the exact explicit r1 ledger is below low-yield floors and requires mandatory expansion.


Do not merely rewrite the r1 prose. Rebuild the auditable X ledger.


## 3. Canonical W38 temporal authority


UTC ordinary window:


`[2026-09-11T22:00:00Z, 2026-09-18T22:00:00Z)`


End exclusive.


For every canonical X Snowflake status ID calculate:


`timestamp_ms = (status_id >> 22) + 1288834974657`


then convert that UTC timestamp and classify:


- before start -> `PRE_WINDOW_CARRY_IN`
- >= start and < end -> `ORDINARY_WINDOW`
- >= end -> `LATE_BREAKING`
- cannot establish trustworthy time -> `TIME_UNVERIFIED`


Do not use search operators, relative UI labels, date-only prose, or result ordering as temporal authority.


## 4. Sol sanity-check values that r2 must reproduce


The seven complete unique direct status IDs present in r1 independently decode as:


| Canonical URL / ID | Snowflake UTC | Class |
|---|---|---|
| https://x.com/lrogersaz/status/2101098868368957483 | 2026-09-18T23:59:41.405Z | LATE_BREAKING |
| https://x.com/Google/status/2101042933650571469 | 2026-09-18T20:17:25.529Z | ORDINARY_WINDOW |
| https://x.com/Google/status/2101042935047307762 | 2026-09-18T20:17:25.862Z | ORDINARY_WINDOW |
| https://x.com/AnthropicAI/status/2100684274114699295 | 2026-09-17T20:32:14.432Z | ORDINARY_WINDOW |
| https://x.com/AnthropicAI/status/2100701581109072332 | 2026-09-17T21:41:00.741Z | ORDINARY_WINDOW |
| https://x.com/AnthropicAI/status/2101039819870937247 | 2026-09-18T20:05:03.146Z | ORDINARY_WINDOW |
| https://x.com/ophtaka/status/2101098410933715051 | 2026-09-18T23:57:52.344Z | LATE_BREAKING |


If your derived timestamps disagree, do not continue silently. Explain the discrepancy.


## 5. Exact pre-expansion baseline from r1


Treat the explicit r1 direct-URL set as the pre-r2 audit baseline:


- unique direct status IDs: 7
- ordinary direct URLs: 5
- late-breaking direct URLs: 2
- ordinary distinct accounts: 2
- ordinary role-INDEPENDENT accounts demonstrably present: 0
- ordinary official accounts: 2


Therefore mandatory expansion is unconditionally triggered by at least:


- ordinary URLs < 12;
- independent accounts < 6;
- strong-candidate support dominated by official-only or absent ordinary direct URLs.


Do not describe this as "partially fired".


Perform one complete mandatory expansion pass before finalizing r2.


## 6. Mandatory expansion objective


Use r1 candidates as leads, but explicitly search for missing ordinary-window direct evidence and counter-evidence.


At minimum:


### Astra / agents


Search ordinary-window independent first-hand:


- computer-use;
- closed-loop workflow;
- Agents API integration;
- failures/constraints;
- quota/cost friction;
- benchmark/reproduction.


The r1 lrogersaz URL is Late Breaking and cannot support ordinary breadth.


### Gemini Live / Gemini 3.8


Preserve the two ordinary @Google URLs, then find direct ordinary-window independent/Japanese technical status URLs if they actually exist.


Do not cite `@tetumemo ...` without exact status URLs.


If none are found after the expansion pass, classify the ordinary X support honestly as `OFFICIAL_ONLY_X`.


### Anthropic R&D / biomolecular / evaluation


The three explicit r1 ordinary URLs are official @AnthropicAI.


Find direct ordinary-window independent technical reaction/evaluation if available.


If none is found, do not call this `MULTI_ACCOUNT_X`; keep it `OFFICIAL_ONLY_X` plus any community context separately.


### Jev


Provide direct ordinary-window status URLs for every claimed Japanese/English workflow signal.


The r1 @ophtaka URL is Late Breaking.


If ordinary direct support remains absent, downgrade Jev from ordinary strong candidate rather than preserving the prior conclusion.


### Other candidates / weak lanes


Continue the required open-world, Japanese, ecosystem-language, local inference, image/video, memory/RAG, safety, benchmark, and low-engagement technical searches from the original task.


One complete expansion pass is required; numeric floors are not quotas.


## 7. No placeholders in auditable provenance


Forbidden in r2 final ledger and strong-candidate representative evidence:


- `https://x.com/user/...`
- "multiple Japanese accounts"
- "additional posts"
- "see search logs" without enumerated URLs
- approximate URL/account counts
- prose-only support with no direct status URL


Each retained X observation must either have an exact canonical status URL or be explicitly marked `UNVERIFIED_X_REFERENCE` and excluded from ordinary breadth.


## 8. Required final direct-X ledger


Emit one table with one row per unique retained status ID.


Required columns:


1. canonical X URL
2. status ID
3. account
4. role: `OFFICIAL | INDEPENDENT | COMMUNITY`
5. role/affiliation note
6. candidate ID(s)
7. lane(s)
8. discovery origin(s)
9. Snowflake UTC
10. observed/displayed timestamp if available
11. temporal class
12. why retained


The same status ID may map to multiple candidates, but appears once in the run-level ledger.


## 9. Role discipline


Use:


- `OFFICIAL`: first-party project/company/model/maintainer authority;
- `INDEPENDENT`: non-affiliated actor with first-hand technical testing, reproduction, benchmark/evaluation, integration, measurement, or substantive original technical analysis;
- `COMMUNITY`: aggregation, media relaying, commentary, enthusiasm/reaction, or uncertain affiliation.


When uncertain, use `COMMUNITY`.


Only exact role-`INDEPENDENT` ordinary accounts count toward the independent-account diagnostic.


Affiliated handles do not create independent corroboration.


## 10. Candidate-level exact recount


For every plausible candidate report exact:


- ordinary URLs;
- ordinary accounts;
- ordinary INDEPENDENT accounts;
- ordinary OFFICIAL accounts;
- ordinary COMMUNITY accounts;
- pre-window URLs;
- late-breaking URLs;
- TIME_UNVERIFIED URLs;
- final ordinary source-breadth classification.


Strong ordinary candidates must be justified from ordinary rows only.


Late Breaking may be retained separately but cannot rescue ordinary breadth.


## 11. Run-level exact recount


Recompute from the final ledger:


- total unique status IDs;
- PRE_WINDOW count;
- ORDINARY count;
- LATE_BREAKING count;
- TIME_UNVERIFIED count;
- ordinary unique accounts;
- ordinary INDEPENDENT accounts;
- ordinary OFFICIAL accounts;
- ordinary COMMUNITY accounts;
- full candidate-pool count;
- strong candidate count;
- non-selected count;
- source-breadth class counts;
- open-world / graph / snowball candidate counts;
- lane-by-lane final state.


No `~`, `>`, `majority`, `12+`, `6+`, or similar approximate summary values are allowed where an exact ledger-derived count can be computed.


## 12. Reconciliation gate


Before final output verify:


- total unique status IDs = PRE + ORDINARY + LATE + TIME_UNVERIFIED;
- ordinary account counts reconcile by role;
- every candidate count matches the final ledger;
- source-breadth classifications match role-aware ordinary rows;
- low-yield trigger inputs use the final ledger;
- no duplicate status ID inflates run-level counts.


Only then emit:


`LEDGER_COUNT_CONSISTENCY: PASS`


If reconciliation fails, correct the summary before saving r2.


## 13. Search-quality fail-closed rule


If X access prevents the complete direct ledger, Snowflake classification, role-aware recount, and required audit surfaces from being produced, set the result status clearly to:


`INCOMPLETE_DUE_TO_ACCESS_LIMITATION`


Do not declare PASS-like ledger consistency from a sample.


## 14. Timestamp provenance


Set front-matter `observed_at` to the actual r2 observation completion time with timezone offset.


Do not copy r1's `2026-09-19T04:00:00+09:00`.


## 15. Output preservation


Keep useful r1 leads, counter-signals and negative lane findings where they survive the r2 audit.


Do not fabricate additional candidates or URLs merely to clear diagnostic floors.


The objective is an auditable, temporally correct Raw Observation artifact, not a larger-looking report.


Save only:


`Grok_X_SourseIntake/Weekly/2026-W38/weekly-x-2026-W38/grok-x-result-r2.md`


Do not overwrite `grok-x-result.md`.