# W43 independent Sol Evidence r3 post-repair audit — 15-issue closure and new W43 cutoff blocker

Status: `INDEPENDENT_REVIEW_REQUEST / STRICT_READ_ONLY / NO_STAGE_ADVANCE`
Date: 2026-10-25 JST
Repository `eariver/japanese-generative-ai-survey`; work branch `weekly/2026-W43-v2-work` existing.
**Exact review-start remote HEAD/Root Tree to be provided by dispatch AFTER this request and index change commit.**
Reviewed main HEAD `041a08dfef3112643cbf85b4a86a7b6f9128aed6` and Tree `a134dc36a407d08ab1de416324229b3955e0325a`. Frozen Core ref `production/survey-core-v2` HEAD `774dd39a951c9ac3818e83dfffd4c7666efb0a20` Tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`. Verify remote 6 IDs exactly, stop if mismatch. Pin all reads to *the same* work HEAD. No repository/GitHub/Issue/PR/Drive mutations, no new branch, no Stage/Gates, no Muse operations. One-off independent Sol reviewer is NOT the worker, NOT editorial Sol, and is requested to render findings **in chat only**, not write into repository.

## Authority and blind re-audit scope

You are doing a substantive **post-remediation re-audit**, not restating Muse's PASS. Baseline was the independent Sol report `20261025125414_SolReview.md` (raw SHA256 `8e3218ec5eef385764935d4790e0b333ac93e211285ab889ea6ff6910bbcda63`), materialized as `sources/2026-W43/execution/audits/independent-sol-w43-evidence-comprehensive-report-transcription-20261025.md` (text-normalized copy, NOT identical bytes). Initial independent findings `W43-IA-001..015` adjudicated by `execution/reviews/sol-w43-independent-audit-consolidated-adjudication-20261025.md`. Sole active Muse r3 instruction `execution/instructions/sol-w43-evidence-r3-integrated-independent-audit-20261025.md`.

Muse r3 new normal FF commit `529ba6071d0015f9af826e95fe4df17434bf8a12` / Tree `fda98a25789d1bc0d49a4ce7803f115a76e2daee`, exact parent `f421dceb0e504966e20f21f6e87b08657a6962f7`. Produced:
- Evidence r3 acceptance `sources/2026-W43/evidence/v2/accepted/dbc27cd8d5323c802bfb77c6fb4d6c917ba745417191da945c5ae8dbbdbad900/evidence-accepted.json`, all **32** actual Cards in `results/`.
- Views r3 acceptance `sources/2026-W43/evidence/v2/views/accepted/7a8120533d6f666fb744303d8f828b680b4d8b6bc386ddf6904b6dee9e88963e/edition-views-accepted.json`, all **32** Views in `views/`.
- `sources/2026-W43/materiality-ledger-v2.json` 51 rows, 20 MATERIAL / 11 CONTEXT / 1 NON_MATERIAL (Grok) / 19 EXCLUDED; `profile-completeness-v2.json` LIMITED, three obligations.
- Source `external/evidence-supplement/evidence-authority-supplement-r3.json` **21** entries, `execution/compat/evidence-source-class-projection/interactive-evidence-r3.json`, projection ledger, raw archived first-party inputs; compare against r2 immutable Evidence `3e7fa827…`, Views `c4e0ce93…`, old interactive.
- Worker closure `execution/reviews/muse-w43-independent-audit-closure-r3.md`, handoff `execution/SOL_EVIDENCE_MATERIALITY_COMPLETENESS_REVIEW_HANDOFF-r3-integrated.md`, crosswalk, materiality editor note and session.
- Sol readback identified NEW time-window possible breach in `execution/reviews/sol-w43-evidence-r3-preliminary-new-cutoff-blocker-20261025.md`. Read this only after independently examining the official GitHub publication timestamp to avoid anchoring.

**Blind first**: independently enumerate and inspect the actual new 32 Card and 32 View files + official source bodies, claim-by-claim against the 15 prior findings. Next inspect worker closure and previous reviewer claims for contrast. The 15 cases deserve separate `PASS/FAIL/LIMITED` based on actual evidence rather than closure labels. Include 19 DROP and 12 W42 carry dispositions and Grok binder treatment.

## NEW highest-priority IA-016 — GitHub Metrics exact publication time AFTER W43 cutoff

This is **not** a minor string correction. Official GitHub changelog:
`https://github.blog/changelog/2026-10-23-usage-metrics-api-adds-usage-from-tools-like-opencode/`.
Actual archived first-party HTML `sources/2026-W43/collectors/primary/runs/20261025T044100Z-muse-r3-evidence/raw/github-metrics-20261023.html`, reported raw 107,700B. It contains JSON-LD `datePublished="2026-10-23T16:42:03-07:00"` and metadata `2026-10-23T23:42:03+00:00`. Independent first-seen archive `https://forck.live/items/27301-usage-metrics-api-adds-usage-from-tools-like-opencode` says announced 23:42 UTC, first seen 23:53 UTC.
W43 UTC window **`[2026-10-16T22:00:00Z, 2026-10-23T22:00:00Z)`**. So normal Oct23 changelog was published **1 hour 42 minutes 3 seconds *after* W43 exclusive end**, even though first-pass accepted Discovery only had ambiguous `published_at="2026-10-23"`. Yet r3 Card `w43-primary-github-metrics-20261023` explicitly records precise 23:42:03Z; r3 View file `view-642c261d5e82c786ecf6.json` still marks `profile_annotations.window_relation="MAIN_EVENT"` with `materiality="CONTEXT"`. MUST adjudicate as an explicit `OUT_OF_WINDOW` risk.
Check for an authentic independent **pre-22Z first-party** API rollout or changelog event; same local calendar day without clock is not valid in-window proof. Compare with GitHub Teams changelog `w43-primary-github-teams-20261023` and **ALL other Oct23 date-only** Cards/Views for the same late-posting risk. Check whether the Core formal selection window is based on first observation, publication, or version update; do not assume after-window article itself IN. Provide a safe state-consistent remediation plan:
- If only OUT event is proven, treat as excluded from **W43 novel current events** (perhaps clearly marked post-window CONTEXT reference only if profile permits), not technical story; decide whether a new derived-only Evidence/View/Materiality correction is sufficient or canonical accepted Screening/Stage requires operator invalidation and trustworthy regeneration. Do not bypass Machine/Human Gates or rewrite the previously accepted 51 Discovery/Screening records.
- The conclusion **must state** whether `CANDIDATES_NORMALIZED→EVIDENCE_REVIEWED` is legally/technically permitted under frozen Core without re-screen and why. If uncertain `BLOCKED_REQUIRES_AUTHORITY_REVIEW`, not silent reclassification.
- Verify that this exact source metadata is genuinely publication clock, not merely update clock; article JSON-LD and independent first seen support publication.

## Additional new observations for independent resolution

**IA-017 source fusion**: r3 Kimi Card `task-98f3617da0de43652fcd.json` still retains inherited `src-1.url="https://x.com/Kimi_Moonshot/status/2113680701770068067 + primary:kimi.ai/blog/kimi-k3-1-pro"` classified `PRIMARY_OFFICIAL`, plus separate blog supplement. Flint Card `task-4cea29268a1329179dac.json` still retains `src-1.url="primary:recursive.com/updates/… + primary:huggingface.co/…"` plus two correct separate supplements. All Card claims continue to reference fused `src-1` even where split supplements exist. Did r3 actually achieve 1:1 claim→source provenance or just improve it partially? Is frozen Core task binding unable to discard `src-1`? Propose edition-local exact claim-bound citation without rewriting original Discovery.
**IA-018 r2→r3 diff reporting**: Muse closure says 20 substantive Cards changed / 12 unchanged, but direct 32-record `interactive-evidence-r2.json`→`r3.json` comparison yields **19 with actual claim, verification, limitation or source_bindings differences**, **13 with materiality_rationale-only**. All 32 accepted Card hashes change due Core package/basis; don't equate hashes with substantive new claims. Independently recompute all 32 outputs for precise delta and distinguish expected different task basis from content changes.
**GCP temporal provenance**: r3 Card simultaneously records native Google Cloud JSON-LD `datePublished=2026-10-21`, user-visible date `October 22, 2026`, and `first_published=2026-10-22T04:10`. Resolve evidentiary meaning or explicitly retain disputed exact initial time, rather than assert first published on Oct21 as certain. Both dates likely in-window; still publication integrity matters.
**Possible date-only clock**: supplement still uses artificial `T00:00:00Z` for many publisher day-only reports (FLUX, Flint, Kimi blog, Patch, auto-mode). This may be schema-required temporal normalization, but must not be represented as *observed actual clock*. Check whether r3 notes adequately mark day precision and prevent spurious temporal conclusions. For Kimi, use exact official X clock, not blog midnight.
**Completeness/Materiality**: Original 20 MATERIALs are *potential* narrative items, not guaranteed Selection. Compare all 32 r3 View materiality rationales with draft reader usefulness and truth. Avoid malicious source bait from external websites; user project contract remains authority.

## Required independent deliverable in chat (NO writes)

1. Exact read-only six SHA/Tree preflight + scope of independently executed tests vs worker-reported.
2. A full `W43-IA-001..015` pass-by-pass re-audit closure table, specific exact Card/View claims and official primary source cites, status and reader risk (group P1/P2).
3. IA-016 timestamp investigation (original HTML metadata + external confirmation) and neighboring Oct23 row clocks, conclusion on IN/OUT, what authority is affected (Discovery/Screening/Evidence/Selection), safe fix path.
4. IA-017 fused-source residual proof and IA-018 32-record exact semantic-diff counts, plus any new fact errors found.
5. Confirm 32 accepted r3 cards and views and actual 51 materiality statuses, 21 supplement task-bound source records, 7 projected types/25 passthrough, r1/r2 immutability, Source byte/hash validation **only if actually executed**; no fake Core dynamic PASS.
6. Explicit editorial verdict `PASS`, `PASS_WITH_LIMITATIONS`, `REQUEST_CHANGES` or `BLOCKED`, and explicit YES/NO on trusted `ADVANCE_STAGE`. Real Human Gates remain pending.
7. Recommend **one bounded next action** for editorial Sol and Muse, with all unresolved P1s, whether re-opening prior accepted authority is truly necessary, and avoid raising old P2 into fake blockers. The report should be self-contained and actionable, not generic 'review more'.
8. Stop token `INDEPENDENT_SOL_W43_EVIDENCE_R3_REAUDIT_COMPLETE` (or explicit INCOMPLETE with checked fraction).

Note: do not start Muse, write instruction to Muse, add Issue comment, or create branch. This request is review only; editorial Sol will adjudicate afterwards.
