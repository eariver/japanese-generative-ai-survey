# W42 carry-over table r1 (from W41 SELECTED/HOLD/INSPECT/CONTEXT + W40 obligations)

Sources: `candidate-selection-v2.json` (W41: 20 SELECTED / 13 HOLD / 2 INSPECT / 1 REJECT), `architecture-review-attention-v2.json`, W41 residual limitations. W41 Selection/Architecture are NOT W42 decisions.

## W40-carried obligations (via W41 HOLD retained)

| Obligation | W41 status | Fresh W42 trigger? | W42 disposition |
|---|---|---|---|
| Pixel Canary (stealth, no dated card) | HOLD retained (70753543) | None found in 73 Daily X topics; no new card/repo in sweeps | NO_NEW_EVIDENCE — retain watch, do not promote |
| TBC Video (figures unverified) | HOLD retained (b5cbf725) | None (OSS video roundup 1-6/Sulphur 1-12 are different models, no TBC link) | NO_NEW_EVIDENCE |
| Ai2 AstaBrief (Oct 2 confirmed, no W41 new) | HOLD retained (7ee1091c) | None in W42 intake | NO_NEW_EVIDENCE |
| ServiceNow AutoSynthData (Oct 2, no W41 new) | HOLD retained (f925ea19) | None | NO_NEW_EVIDENCE |

## W41 HOLD rechecks (high-regret + ordinary)

| W41 HOLD | Grounds | W42 trigger? | Disposition |
|---|---|---|---|
| StepFun (vendor+snippet, JS-gated, preview-vs-weights) | HOLD 2448d420 | None in W42 topics/sweeps | NO_NEW_EVIDENCE |
| MS-Decision-1 (day-only, cutoff unprovable) | HOLD 3f854055 | 2-11 digest re-mention (same UNVER, no clock/license/weights) — NOT fresh authority | RECONFIRMED HOLD — 2-11 folds into carry record, no promotion |
| Tencent (month-only News, papers pre-window) | HOLD a9e90db5 | None (no Tencent topic in W42 Daily X) | NO_NEW_EVIDENCE |
| NDI NACE 1.0 (no version/date/bench/license) | HOLD 118b542f | None (no NDI topic in W42) | NO_NEW_EVIDENCE |
| ElevenLabs WG (X-only, charter/spec missing) | HOLD 78cd776c | None (no ElevenLabs topic in W42) | NO_NEW_EVIDENCE |
| Drex NACE (docs read, X/HF/license unverified) | HOLD ee3aba30 (highest-material) | None (no Drex topic in W42) | NO_NEW_EVIDENCE |
| Agr (X-only, repo/card/evals unverified) | HOLD f0a2eae1 | None | NO_NEW_EVIDENCE |
| Nemotron HF distrib (weights/cards unopened) | HOLD c1e75d56 | SUPERSEDED by fresh W42 event: Nemotron 3.5 Super VL GA Oct 15 (6-1, official) — old distribution HOLD does NOT cover new model; new record created, old HOLD closed as OUT_OF_SCOPE for W42 (model superseded) | OUT_OF_SCOPE (superseded) + new w42-primary-nemotron35 |
| f3c852df day-only no-clock | HOLD | None | NO_NEW_EVIDENCE |

## W41 INSPECT / CONTEXT

| Item | W41 | W42 |
|---|---|---|
| ELYZA RSI (pre-window JP bg) | INSPECT/CONTEXT sidebar | No new ELYZA trigger → remain CONTEXT reference only |
| Usage Policy update (Nov 12 effective) | INSPECT/CONTEXT | No new trigger → CONTEXT only |
| Grok/X ledger | REJECT (not article) | W42 Daily X likewise intake-only, never candidate |

## W41 SELECTED successors (watch, not auto-carry)

- pplx-decider-v1.1-27b (W41 SELECTED) → v1.2 on OpenRouter (7-9) observed in-window → new successor record w42-primary-decider-v12 (version change, needs spec diff).
- Reflection Beam (W41 SELECTED supporting, Oct 5 intro) → Beam availability/weights Oct 16 (7-7) → new event record (intro was background, availability is W42 event).
- EmbeddingGemma 2 (W41 SELECTED) → GGUF chatter only (2-2) → NO new event; do not re-select.
- Mistral Large 4 (W41) vs Le Chonk (3-6): different artifacts; no carry link.
- No other W41 SELECTED has a W42 successor trigger in this intake.

## Rule compliance
- No carry promoted without fresh W42 authority. Only two version-successor/new-event records created (Nemotron 3.5, Decider v1.2, Beam availability) — each with its own in-window official trigger, not inherited materiality.
