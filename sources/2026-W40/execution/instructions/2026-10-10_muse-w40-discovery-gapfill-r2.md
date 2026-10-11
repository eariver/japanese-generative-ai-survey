# W40 — Muse bounded Discovery Gap-fill r2

Status: `SOL_BOUND_EXECUTION_REQUEST / CORRECT_SC_D01_SC_D02_SC_D03 / STOP_AT_SOL_DISCOVERY_REVIEW`
Review authority: `sources/2026-W40/execution/reviews/sol-w40-discovery-completeness-r1-20261010.md`
Repository: `eariver/japanese-generative-ai-survey`
Existing branch only: `weekly/2026-W40-v2-work`
Reviewed main HEAD: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Starting HEAD/Tree: **the exact outer invocation values representing the commit that added this file** (not the preceding Muse commit).
Pre-review Muse baseline HEAD: `05bfeca3bab7afa616bef4212d634e46d9388803` ; Tree `116258827fec38fb1d3aa3f706b777d26cf335b9`.

## Zero-write admission guard

Before ANY write verify read-only remote work HEAD=outer Starting SHA, its Tree=outer Starting Tree, remote main HEAD=`afdb3df3faa20af3bb5798be429bba8dbd2100b1`, baseline Muse commit is ancestor, current `production-state.json` is `ISSUE_INITIALIZED`, next `stage:discovery`, both Human Gates pending. Mismatch => STOP, report expected/actual. No fallback/review/new branch, no force/rewrite/rebase/reset/merge, no Core/config/schema/CI/main/other-edition write.

## Mission

Address Sol Discovery audit r1 blockers **SC-D01/SC-D02/SC-D03** without weakening prior technical review, erasing provenance, fabricating time, or inflating article volume. The existing Muse 29 records and acceptance proposal are **staging input**, not frozen acceptance. Preserve earlier r1 work as auditable history where possible, append replacement snapshots and a clear supersession ledger. Since no canonical Discovery acceptance or stage checkpoint exists, regenerate only W40 draft/pre-accepted surfaces. Terminal at fresh Sol Discovery Completeness Review; never perform Screening.

### R2-A: substantive independent omitted-source verification

Independently access and inspect the six first-party announcements cited in `sources/2026-W40/execution/reviews/sol-w40-discovery-completeness-r1-20261010.md`:

- H Company Holo4 (Sep 28), incl 27B dense, 35B-A3B MoE, quantized model weights, materially **different licenses** (27B noncommercial vs 35B Apache-2.0); distinguish API availability, open weights, benchmark suite/version, reproduced vs self-reported results.
- Ai2 Olmo-core 3 (Oct 1): DDP/expert/pipeline/distributed optimizer details, technical report and code, 2.7x benchmark conditions, MoE training infrastructure rather than a new pretrained foundation model.
- Hugging Face Open TTS Leaderboard (Sep 30): WER/CER/TTFA/RTFx/speaker SIM methods, evaluated sets, absent human preference; distinguish an evaluation platform release from a new speech model.
- Multiverse Computing ProvenanceGuard (Sep 29): attribution to exact MCP source, cross-source conflation; original paper and protocol if available. Do not cite a team blog as independent result.
- Ai2 AstaBrief 8B (Oct 2): original timestamp/timezone relative to W40 22:00Z cutoff; published model version, training data, relevance and 2025-era comparison baselines; if exact time unproven classify `TIME_UNRESOLVED` and retain as material lead/HOLD.
- ServiceNow AutoSynthData (Oct 2): published paper/tool/demo dates vs Oct 2 blog and cutoff; environment verifier/task generation mechanism; record `TIME_UNRESOLVED` if needed.

Perform a new open-world search beyond these six, including Hugging Face original lab/team blogs and model repository Releases for the week; inspect any additional credible strong sources. Reevaluate the entire A–L coverage; a concentrated web query list is not evidence of no events. Keep negative results with exact searched surfaces and reproducible source links. Do not mechanically force all six into article Selection — this is a **discovery** review.

### R2-B: origin and provenance integrity

- Audit all 29 existing Discovery records (plus newly discovered records) for `source.published_at`, `source.observed_at`, event and first-party publication time, timezone, date precision and source evidence.
- **21 entries using unsupported `T12:00:00Z` must be repaired.** If only the day is known, set schema-allowed `published_at: null` and record day + `DATETIME_NOT_PROVEN` + local timezone ambiguity under metadata; never substitute arbitrary clock time. For verified exact original instants, preserve source/UTC offset and corroborating evidence. Do not treat current web updated timestamps or download time as 2026 original issue time.
- For material sources, archive actual obtained body bytes *when legally/practically possible* and capture SHA/bytes/URI. Else original-URL anchored, bounded permissible excerpts and an explicit access/redistribution record. Store **derivative claim cards separately** from captured original source bytes. Distinguish `CAPTURED`, `READ`, `CLAIM_CONSUMED`, and `LOCATOR_ONLY`. Do not describe 24 editorial note files as 24 preserved original bodies.
- Preserve exact 20,477-byte Grok Raw unchanged and the Daily X 64 URL ledger; their source and provenance remain separate. X manifest `COMPLETE/PARTIAL` must preserve its real limitations. Fix stale `execution/index.md` 'AWAITING_GROK' text.
- Preserve W39 Pixel Canary and TBC/5x claims on HOLD unless original dated technical verification is found. For DGX Spark 64GB, resolve if possible else HOLD; never use the blog's calendar-only date to invent time before cutoff.

### R2-C: regenerate and preflight

Regenerate the W40 draft `discovery/discovery-v2.jsonl` and isolated `PROPOSED_NOT_ACCEPTED` acceptance with accurate exact source RAW refs/SHA/source graph. Explicitly track r1->r2 added/removed/merged/split IDs and reasons. Update collector run/raw indexes with actual file classes; strict schema validation and authoritative Core v2 deterministic preflight only. No invented human/Sol PASS, no canonical `discovery-accepted-v2.json`, no `DISCOVERY_COLLECTED`, no Screening/Evidence or downstream state.

Provide a fresh `SOL_DISCOVERY_COMPLETENESS_REVIEW_HANDOFF-r2.md` with:
1. starting and final HEAD/Tree, branch ancestry, diff path allowlist, reviewed main and nonforce push/readback;
2. each SC-D01/02/03 resolution with source and file evidence; 21 artificial-noon audit result;
3. new candidate inventory, version/date/license and materiality *leads* vs HOLD; original-newness vs recurrence;
4. A–L search/negative-space matrix and sources traversed, including weak audio/open-model training agents;
5. captured original bodies vs derivative excerpts vs locator-only exact counts and bytes/hashes; exact URLs and reproduction of fetch methods;
6. recomputed 29+ Discovery IDs/raw graph/acceptance proposal and validator records;
7. updated X manifest/index coherence, original Grok 4 versus separate Daily X 64 accounting;
8. terminal `SOL_DISCOVERY_COMPLETENESS_REVIEW_READY` only if supportable, otherwise `SOL_DISCOVERY_COMPLETENESS_REVIEW_BLOCKED`.

Stop here, returning all remaining unresolved high-signal sources and reasoned limitations to Sol. Do NOT extend into Screening, Evidence, Selection, Architecture or Human decisions. All writes only inside `sources/2026-W40/` on existing branch, normal commits, non-force push. If Core defect is discovered, **do not patch** Core; log a deferred maintenance issue with clear evidence for Sol.

## Last-stop state invariant

`production-state.json.lifecycle_state == ISSUE_INITIALIZED`, `next_action == stage:discovery`, Human Gates pending/pending. Sol decides the completeness approval.
