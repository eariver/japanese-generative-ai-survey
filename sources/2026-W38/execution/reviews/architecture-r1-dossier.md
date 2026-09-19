# Human Architecture Review dossier — 2026-W38 r1 (Sol-owned, Human decision pending)

Status: `ARCHITECTURE_ESTABLISHED / HUMAN_GATE_REACHED / PENDING_HUMAN_DECISION`
Date: `2026-09-19T07:00:00Z`
Revision: `r1`

## 1. Exact review identity

- Edition `2026-W38` (WEEKLY + WEEKLY_MAGAZINE), target gate `ARCHITECTURE_REVIEW`.
- Reviewed commit `ba608dc0692457ea4bb6808c39e03c25f46945da` (tree `9e68cdedcc3f57c9c111117612d9be402f61b0ab`).
- Lifecycle `ARCHITECTURE_ESTABLISHED`, terminal `HUMAN_GATE_REACHED`, next `ARCHITECTURE_REVIEW`.
- Gate triple + State + matrix/selection shas as in `architecture-r1.md`. Presented bytes are exactly the pushed commit; no Draft started.

## 2. Research coverage

- X/Grok r2 (25 URLs: 23 ordinary / 0 pre-window / 2 late-breaking; 7 ordinary INDEPENDENT, floors cleared 23>=12 / 7>=6 / 10>=8) used as sensor only, with Sol-corrected counts (15 accounts 7+3+5; C1 7 URLs; C2 `MULTI_ACCOUNT_X`).
- 10 fresh primaries retrieved and claim-consumed Sep 19: OpenAI Astra for Law (Sep 17), Google Gemini 3.8 Live (Sep 15), Anthropic LSVP (Sep 17), Anthropic Accenture (Sep 18), Anthropic R&D metrics (Sep 17), TypeSafe Jev (Sep 15), Amodei pacing essay (Sep 12), Cognition Devin Code Scans (Sep 16), Character.ai CAI-Image (Sep 16), PixAI Tsubaki.3 (Sep 16); plus 2 W37 carry-over revalidations (DeepSeek Sep-14 routing occurrence, secondary; GLM-5.5 absence, disposal).
- 13-record Discovery across all 12 lanes (A-L); Sol completeness NON_BLOCKING_WITH_INDIVIDUAL_LIMITS (vendor benches unreproduced; webfetch excerpts; date precisions; open primary captures; E-lane creator-tool-only thinness; I-lane legitimate quiet).
- W37 carry-over derived fresh: DeepSeek routing re-verified in-window (HOLD context); GLM-5.5 absence re-verified (DROP); W37 HOLD safety item stale; Sep-11 distillation detail disposed (no fresh primary, risk noted); 24+1 W37 X URLs stale.
- Edition-local repairs (pre-downstream, uncommitted, canonical redo, session-documented): strict-schema extra-field removal, Evidence source_type vocabulary normalization, missing architecture requirements backfill, stale stub removal. No committed history rewritten.

## 3. Evidence quality

- 12 Evidence: 9 VERIFIED + 3 PARTIAL (X ledger SOCIAL_OBSERVATION-only; Amodei date-precision PARTIAL; DeepSeek secondary-only PARTIAL/CONTEXT).
- Authority-consumption Sol review CLEAN: 10 AUTHORITY_CONSUMED primaries (claim-level reads with page-section context, no generic placeholders); 1 gap-fill round (Gemini docs transport-failed, recorded as RETRIEVAL_FAILED; biomolecular repo NOT_FOUND, must not be claimed).
- Completeness LIMITED with 3/3 obligations SATISFIED (carry-over / current-relevance / technical-significance).
- X never promoted; vendor/judge/partnered bounds explicit (Vals, S2S/tau-Voice/BBA/EVA, Jev evals, Devin pilots, CAI side-by-sides all stated-with-attribution).

## 4. Major candidate map

- SELECTED PRIMARY (10): astra-law, gemini-live, lsvp, accenture, rdi, jev, amodei (policy anchor), devin, cai-image, pixai.
- SELECTED SUPPORTING (1): X ledger (community signal).
- HOLD (1, NONE usage): deepseek-routing (secondary occurrence, primary gap open — context, not packaged).
- EXCLUDED/DROP (1): glm55 rumor (absence re-verified).
- Reasons per candidate in Sol materiality/selection review; all SELECTED trace to Evidence with bounds.

## 5. Negative-space / omission review

- Unselected: DeepSeek HOLD (correct — secondary-only, not a release); GLM DROP (correct — rumor-only); Bodhan/Real-SWE/BLINDSPOT/Copilot/Zed/xAI-memory secondary leads disposed at Screening scope (documented, not silent); W37 safety HOLD stale (no fresh development).
- No VERIFIED+CONTEXT/HOLD systematic defect; no cluster collapsed generically; biomolecular gap explicit, not hidden.

## 6. Editorial thesis

In 2026-W38 the frontier went vertical and verifiable: OpenAI configured Astra into Law (230M-URL index, Trusted Access); Google shipped native speech-to-speech Live; Anthropic opened biology access under verification (LSVP), published R&D pace metrics, and instantiated pacing with the Accenture embedded-evaluation deal following Amodei's essay; TypeSafe launched non-generative System One decisions (Jev); Cognition productized codebase investigation (Code Scans); image went production (CAI-Image open-lineage family, Tsubaki.3 creator GA) — with DeepSeek's Sep-14 routing held as serving context.

## 7. Architecture packages

1. w38-law-vertical (astra-law + X): Sep 17 legal-vertical config with index/bench/governance bounds.
2. w38-voice-frontier (gemini-live + X): Sep 15 live speech-to-speech with vendor-attributed benches.
3. w38-biology-access (lsvp + X): Sep 17 verified-access biology regime with grant/monitoring mechanics.
4. w38-pacing-operational (amodei + rdi + accenture): commitment -> metrics -> first deal as one governance arc.
5. w38-decision-models (jev + X): Sep 15 non-generative decisions with RLCD/speed/commercial bounds.
6. w38-agent-harness (devin): Sep 16 goal-to-PR investigations with architecture/pilot bounds.
7. w38-image-production (cai-image + pixai): open-lineage family + creator GA with explicit ranking refusal.
Order is drafting order; page allocation is a downstream drafting concern.

## 8. Page/section allocation

Downstream drafting concern (no Draft authorized). 7 packages; optional sections (e.g., Paper Watch) omitted by default; DeepSeek context note available as sidebar material only.

## 9. Counterfactual alternatives

- LSVP merged into governance arc: REJECTED (distinct access-regime mechanics).
- Image split into two packages: REJECTED (shared production thesis + bound is more honest).
- Essay standalone: REJECTED (materiality is as pacing anchor; arc shows instantiation).
- DeepSeek 8th package: REJECTED (secondary-only; HOLD is honest).
- Sparse video-model package from press releases: REJECTED (secondary-only; thinness recorded as limitation).

## 10. Known limitations and risks

- All vendor benchmarks unreproduced (carried stated-with-attribution); methodology pages for Vals/AA/Sierra unconsumed.
- Webfetch excerpts (curl blocked); Accenture hour, Jev hour, Amodei day precisions bounded as stated.
- DeepSeek primary-docs gap (secondary CONTEXT); biomolecular repo not found (must not be claimed).
- E-lane foundation-video thin; I-lane primary-quiet; pre-window context (Astra base, Flash Sep 2) excluded from ordinary claims.
- Partnership figures ($1B) are stated expectations; operational details admittedly unsettled.

## 11. Sol review finding

- Blocking: 0. Non-blocking: residual limitations above (all source-backed).
- Machine readiness READY_FOR_ARCHITECTURE_REVIEW with zero errors; Sol supervisory chain complete (completeness NON_BLOCKING, authority-consumption CLEAN, materiality/selection OWNED, architecture OWNED).
- Recommendation: architecture is sufficient for Human judgment; approval decision belongs to the Human on the exact reviewed bytes.

## 12. Human decision options

Only after the above: `APPROVED` (records against `ba608dc0692457ea4bb6808c39e03c25f46945da`, continues to Draft — not in this run) or `REQUEST_CHANGES` (explicit changes + allowed pre-Architecture boundary; Core invalidates affected downstream only and returns to that boundary). Silence is not a decision.
