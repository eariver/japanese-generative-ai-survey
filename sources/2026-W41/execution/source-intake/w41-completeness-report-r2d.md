# W41 completeness report r2d (record-repair, proposal for Sol review)

Status: `PROPOSED_NOT_ACCEPTED / SOL_REVIEW_REQUIRED / R2D_RECORD_REPAIR`
Proposal: `discovery/discovery-v2-proposal-r2d.jsonl` — 37 records (IDs/count preserved from r2c), schema-validated. State `ISSUE_INITIALIZED`.
Manifest: `external/x/x-source-intake-v2.json` — `discovery_ids` repaired to existing `w41-grok-x-ledger-20261011`; schema PASS + referential PASS.
Crosswalk: `execution/source-intake/w41-dailyx-92topic-crosswalk-r2d.md` — 92/92 one-to-one, counts unchanged (16/49/3/14/2/8).

## r2d repairs (no re-triage, no new candidates, no re-search)

1. Manifest↔Proposal identity: manifest `w41-grok-x-ledger-20261012` (r2b typo, no such proposal row) → existing `w41-grok-x-ledger-20261011` (r1-origin, carried r2/r2c). 37 IDs unchanged.
2. Stale proposal prose repaired (5 rows): Grok ledger AWAITING→RAW_RECEIVED title/summary; Decisions secondary-only→first-party-corroborated title/summary; Clef-omni TIME_UNRESOLVED→IN-WINDOW title (+Grok-#10-post-cutoff note); Mistral 49B-superseded→version-disagreement-preserved summary; Negative-space quiet-audio/serving→r2c-grounded lanes summary.
3. New-8 source honesty (within schema): textGrain PRIMARY kept (=blog existence confirmed, body/PDF unread); SynthID PRIMARY_OFFICIAL→x-community-signal (X-post-only basis, blog unopened); Agr/Nemotron/Nace×2/ElevenLabs SECONDARY retained (vendor-X-only, docs unverified); StepFun PRIMARY kept (=provider page + issuer X, official model page unread). All 8 reasons annotated `r2d:`.
4. Provisional clocks corrected (new-8 only): `2026-10-12T00:00:00Z` placeholders → DailyX report generation instants (10-06 report → 2026-10-05T22:00:00Z; 10-08 → 2026-10-07T22:00:00Z; 10-09 → 2026-10-08T22:00:00Z; 10-10 → 2026-10-09T22:00:00Z; each = report-date 07:00 JST, verifiable raw header). Event clocks stay in `metadata.timestamp_basis`, NOT in `observed_at`. X-post Snowflake UTC recorded per-topic in crosswalk r2d (format-only; existence/authorship unverified).

## Before/after (r2 29 → r2c 37 → r2d 37)

- r2c→r2d: 13 rows touched (fields listed in `w41-r2c-r2d-diff-r2d.md`), 24 rows byte-identical, 0 IDs added/renamed/removed, order preserved.
- New 8 (unchanged membership): textGrain (blog-exists), Agr (vendor post), Nemotron HF (distribution), SynthID portal (X-only), StepFun Step 5 (provider+issuer), Nace Drex/NDI (vendor X), ElevenLabs (vendor X).
- Rejected/held (unchanged): Cline Ling, Magnitude, MiniMax H3 demo (UNVERIFIED_HOLD/CONTEXT); XRPL (UNVERIFIED_HOLD); Saluki (PRE_WINDOW); revenue/patent/medal chatter (NOT_MATERIAL); Oct 10 business/reaction items (POST_WINDOW substance or CONTEXT).

## 92-topic disposition counts (unchanged)

- EXISTING_R2_DISCOVERY 16, CONTEXT 49, UNVERIFIED_HOLD 3, NOT_MATERIAL 14, PRE_WINDOW 2, NEW_PROPOSED_DISCOVERY 8.
- Grok-14 overlap: 9 shared IDs reconciled without double-count; 2 Grok posts post-cutoff respected as late-only (#6 +4m59s, #10 +1h11m).
- 09:00 independent runs: NOT FOUND for any date — coverage exhaustiveness NOT claimed.

## Lane coverage after r2d (unchanged from r2c, wording repaired)

- Audio: voice agents (Nova Sonic) + detection (ElevenLabs) + TTS eval context; generation releases still quiet (dated).
- Serving/local: d1 llama.cpp support, WinML llama.cpp, Magnitude unverified, v0.6.0 unobserved.
- Retrieval/embedding: EmbeddingGemma 2 + Perplexity pair (downloadable/published).
- Open weights: Kolibri + d1 downloadable; Mistral/Beam/Clef-omni announced-pending; StepFun preview via router.
- Safety/governance: textGrain, SynthID, Cyber Mission/CVP, Usage Policy, OSS Scanner.
- Japanese: no in-window model release (dated negative stands).
- X lane: raw received + reconciled; post existence/authorship unverified (Sol audit boundary preserved).

## Residual blockers for Sol (unchanged, still NOT acceptance)

1. First-party product pages still unfetched for Nano Banana, StepFun (official), Nace pair, ElevenLabs, SynthID blog.
2. Oct 9 day-only MS-Decision-1 and Tencent upload need Sol HOLD/CONTEXT confirmation.
3. 09:00-run absence limits exhaustiveness claims.
4. r2 SC-D01 rows keep r2 midnight collection dates (`2026-10-12T00:00:00Z` run-date placeholders, out of r2d scope); r2d corrected only the new-8 placeholders.
