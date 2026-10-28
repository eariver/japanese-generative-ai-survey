# W43 Sol → Muse r2 — Discovery coverage repairs and raw-authority capture

Status: `WORKER_EXECUTION_CONTRACT / LIMITED_REQUEST_CHANGES / DISCOVERY_ONLY`
Date: 2026-10-24 JST
Repo: `eariver/japanese-generative-ai-survey`
Branch: `weekly/2026-W43-v2-work`
Sol review authority: `sources/2026-W43/execution/reviews/sol-w43-discovery-completeness-review-r1-20261024.md`
Reviewed Muse input: HEAD `57afcd292d946078ae03900bd242b6f0b4f7de60` / Tree `c2e797e0beb74f2c97f57afe87b6b9b7947435db`.
Reviewed Sol review-commit checkpoint (BEFORE this contract): `3b5652a37d81ab5aa1aa5f50238299fdd531db5e`.
**Muse's actual required Exact Starting HEAD and Tree are the new post-contract remote identity supplied in the Sol message alongside this file.** Never use the pre-contract checkpoint as execution start.

## 1. Exact git guard and trust boundaries
- Read-only preflight: remote work-branch HEAD/Root Tree must match Sol-supplied Exact Starting values. `main` HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6` and Tree `a134dc36a407d08ab1de416324229b3955e0325a`; Frozen Core branch HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` and Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. Any mismatch: ZERO WRITES, report actual and stop.
- Read canonical W43 Profile/State, Sol r1 review and Muse r1 artifacts. No repair/review/fallback/new branches; only normal non-force FF commits and remote readback.
- Protected shared paths `AGENTS.md`, `config/`, `schemas/`, `scripts/`, `.github/`, `tests/`, shared Core docs unchanged. W42 Release, state, Issue #570 untouched.

## 2. Narrow mission
Rectify r1 discovery coverage deficits and chronology at **Source Intake/Discovery only**. Preserve all r1 artifacts as provenance; produce r2 proposal and authoritative original-source capture/consumption table. This execution does NOT authorize Screening, Evidence, Selection, Architecture, any Human Gate or `ADVANCE_STAGE`; State must remain `ISSUE_INITIALIZED` until a later Sol review contract allows trusted Discovery acceptance.

## 3. Blocking r1 findings: execute by IDs
1. `DC-02`: Read and preserve first-party OpenAI Oct 23 training containment/red-team/security account, Oct 21 distributed biology agents evaluation and Oct 19 low-resource coding evaluations. Exact verified URLs in Sol review. These are independent technical events from Oct 21 Google Cloud and Decisions API, not add-ons to product marketing. Inspect methodology, baselines, reproducibility and limitations.
2. `DC-03`: 1Password for Agents Oct 22 first-party press/blog, agent credential-flow/security boundaries, real partner availability, planned vs live. Avoid claiming every integration is already deployed.
3. `DC-04`: MOSS-Image official repo (first release Oct 16 may be out-of-window), Oct 18 trainer, Oct 19 technical report and Oct 20 API; verify first tagged commits/availability independently. MemT-1.0 first-party paper + repository + model cards, explain GDN-2, Mixture-of-Storage, trainable-vs-persistent memory, storage and end-to-end inference baselines; keep repository software/weights/data licenses separate.
4. `DC-05`: Kimi X post actual ID `2113680701770068067`; **13:15 EDT = 17:15Z Oct 23** versus r1 erroneous 17:15 EDT = 21:15Z. 22:00Z exclusive cutoff is **4h45m later**. Verify tweet/event via original if accessible; record proper precision or access restrictions. Separate API available vs weights planned by Nov 4.
5. `DC-06`: Correct AM-Bench 2610.24264 v1 Oct 16 21:46:19Z **OUT**; v2 Oct 20 15:40:19Z **IN as revision**, with original/substantive delta examined; OR-License 2610.24087 v1 Oct 16 18:13:25Z **OUT**. No time-undetermined claims unless precise original cannot be corroborated. Preserve date and event class.
6. `DC-07`: Capture and **substantively consume** original bodies across priority W43 families, including substantial technical docs for Claude Duet, DeepSeek V4.1/DeepInfer, Nemotron Bolt, Voxtral/Eleven, FLUX 3 Max, and new gap-fill families. Original raw bytes + SHA256/URL/UTC retrieval + publisher/first publication/date proof when technically retrievable. Source-unavailable -> `AUTHORITY_RETRIEVAL_FAILED` with exact failed attempts, never claim raw bytes.
7. `DC-08`: Investigate Ming-3.0-TTS original repo/model availability dates, independent evaluation methodology, and other high signal new evaluation/robotics/efficient training leads. ARC Prize Argon Oct 13 score is pre-window unless separate verifiable W43 event; do not redatate. Record why additional leads are rejected/parked rather than simply omitting them.
8. `DC-09`: Preserve all twelve W42 HOLD/INSPECT rechecks; do not auto-promote or repeat uncorroborated security allegation/model name as fact.

## 4. Data integrity rules
- The source of truth is primary site/repository/paper with immutable revision/tag/commit whenever possible. Every technical claim: source, date and chronology, model/setting, units/denominators, official vs independent benchmark, cost availability, license by artifact, caveats.
- Distinguish `SOURCE_LOCATED`, `RAW_CAPTURED`, `SUBSTANTIVELY_CONSUMED`, `INDEPENDENT_REPRODUCED` (only when real). Derivative note is NOT the original source. Do not double count one bundled notes file as 10 original bodies.
- Make a bounded effort for principal original sources; avoid ballooning into all possible pages. The point is substantive authority depth for the plausible primary leads, not an arbitrary candidate count.
- For a later model card/document update, do not relabel previous model/weights release date into current issue.
- Date/time first-public and date of retrospective refresh are distinct; use inclusive start, exclusive end: UTC `[2026-10-16T22:00:00Z, 2026-10-23T22:00:00Z)`.
- Do not assemble final Selection; if chronology ambiguous, mark explicitly and hold the family.

## 5. Grok/X transport and its strict status
Sol has placed the W43 **task** as native Google Doc transport at `Grok_X_SourseIntake/Weekly/2026-W43/weekly-x-2026-W43/grok-task.md`:
https://docs.google.com/document/d/1BubHtxps3Lg711pDJKfoNwe8AyeND7miT9hMQwSnsjw/edit

The unchanged source task text is also edition-local at `sources/2026-W43/external/x/weekly-x-2026-W43/grok-task.md` (source SHA256 as recorded r1). Google Doc is a transport copy, **not** byte-identical raw Markdown. Grok result not yet received; keep `x-source-intake-v2.json` `AWAITING_GROK` until Sol has verified/imported the actual result bytes. Muse has no authority to invent Grok outcomes or to treat task submission as completion. Parallel public gap-fill may proceed while X remains pending.

## 6. Deliverables and stop
- New edition-local r2 collection run with authentic primary-source captures or documented access failures; technical-consumption notes citing original content; corrected chronological log including v1/v2.
- `sources/2026-W43/discovery/discovery-v2-proposal-r2.jsonl` with old relevant identities preserved/linked, new discovery records for omissions, dedup/chronology and original capture/consume provenance.
- Updated lane coverage/negative-space report, W42 carry-over ledger, missing authority ledger, schema-validation results and explicit list of high-impact candidates not yet substantively consumed.
- Execution index/session record and Sol r2 handoff with source counts by *unique first-party original*, raw bytes SHA256 and consumption, official vs independent measurement, every changed path, normal commit chain, final HEAD/Tree, State.
- Validate r2 proposal against existing schemas. Do not synthesize discovery acceptance with X pending. No formal `ADVANCE_STAGE` request. No screening/evidence/selection/draft work.
- **STOP at `SOL_DISCOVERY_COMPLETENESS_REVIEW_READY_R2`**. If any exact SHA/Core/authority conflict or required security boundary cannot be met, `BLOCKED` with evidence and no unauthorized writes.
