# W42 Sol Evidence Authority Consumption Review r5 — REQUEST_CHANGES

Date: 2026-10-17 JST
Reviewed exact HEAD: `1fcfed8044f895ecf3c097faa0828560aa9c4a11`
Branch: `weekly/2026-W42-v2-work`
Main: `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`
Frozen Core: `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
Verdict: **`SOL_EVIDENCE_AUTHORITY_REQUEST_CHANGES / KEEP_DISCOVERY_AND_SCREENING_ACCEPTED`**.

## 1. Stable accepted milestones

- Core lifecycle `CANDIDATES_NORMALIZED`, Discovery and Screening checkpoints PASS; Evidence, Materiality, Completeness, Selection, Architecture pending. Both Human Gates pending.
- Real Grok raw 12,373 bytes and manifest COMPLETE (result PARTIAL / DISCOVERY_RECORDED); canonical Discovery 50 entries: **49 editorial/research candidates plus one X provenance-ledger record**, NOT 50 distinct technical news.
- Canonical Screening 50: 29 KEEP = 28 genuine candidates + one provenance binder; 16 INSPECT, 5 MAYBE, 0 DROP. Source/Screening results validated by Core. Existing accepted files and checkpoints must be preserved.
- Grok 18 posts map to seven existing model/research families, without creating 18 phantom events. No changes to Frozen Core and no unauthorized publication/Human acceptance were seen in r5 file diff.

## 2. Independent quantitative content audit

Inspected `collectors/evidence/runs/20261017T093000Z-muse-r5/evidence-task-results-r5.json` against `execution/evidence-r4/evidence-cards-r4.PROPOSED.json` and canonical Screening. The 50 task rows carry **no source-claim evidence payload** beyond status/count/brief delta; 49 r4 provisional cards contain **68 high-level claim strings in total** (median **one** claim/card, min 1, max 3). States: 23 STRONG + 13 PARTIAL + 13 THIN + one N/A_LEDGER. These are **edition-local subjective labels, not Core VERIFIED statuses**. The 50th Grok ledger has zero claims and zero Evidence targets.

The r1/r2/r4/r5 bundles include substantially more substantive technical material than was actually carried into candidate-local claim cards. Counting task rows is not equivalent to consuming their authority.

## 3. Blocking authority findings

**E42-01 — Source-body → card consumption gap (BLOCKER).** r5 bundle adds a full Muse Wonder research-blog discussion: Prometheus training, Harvey/FocusBench/SWE-Marathon, OOD/generalization, CBRN framing. Yet the only stored candidate-local Wonder card remains the r4 version with two short claims, one still saying `Research blog ... pending`, and the r5 task result only adds an `r5_upgrade` one-line label. r5 says "Wonder card upgraded" without a revised actual card. Argon Minecraft (4 agents / 27h / 2,783 programs) is only a vendor X demo and the linked full DeepMind study was not consumed. Review-ready evidence cannot rely on out-of-band summary paragraphs without traceability back to the card.

**E42-02 — Reader-critical primary licenses missing (BLOCKER for unqualified open-source/use claims).** Muse Model License, OpenMDW-1.1, FLUX Kommunity, MiniCPM licensing and LFM license full text remain unread. Beam Apache 2.0 is card-claimed, LICENSE file unread; Granite Apache header seen. Distinguish open-weight availability, OSI status, commercial restrictions, model/tool terms, weight redistribution and vendor marketing. Do not pretend full-license reads are complete; carry genuinely inaccessible texts only with explicit editorial qualification, not blanket waivers.

**E42-03 — Method/denominator/source depth inadequate (BLOCKER for benchmark reporting).** Primary research PDFs and important safety/evaluation reports unparsed: Wonder evaluation report, Nemotron methodology, Beam safety, Google Earth AI report, Deep Review PAT, autonomous wet-lab papers, Anthropic reports, and associated studies. Benchmark totals and percentages are often vendor self-reports without precise baselines, task denominators or protocol. Evidence must identify specific first-party materials read, methodological caveats, and genuinely external evaluation versus vendor assertions. No independent reproduction should be claimed.

**E42-04 — Authority-state semantic inconsistency (BLOCKER).** r4 cards label MiniCPM and FLUX `AUTHORITY_CAPTURED_BUT_UNCONSUMED` while only HF search excerpts, not complete model-card/license bodies, were captured; METR future evaluation outcome cannot be treated as unread published result. Use this state only for available captured text demonstrably not consumed. Reclassify at candidate/source level into `NOT_FOUND`, `RETRIEVAL_FAILED`, `CAPTURED_BUT_UNCONSUMED`, `CONSUMED` with evidence, and distinguish "linked but not retrieved" from truly absent.

**E42-05 — Synthetic provenance binder (WATCH; do not rewrite accepted stage casually).** `w42-grok-x-ledger-20261017` is Screening KEEP with zero candidate-local claims and explicit N/A_LEDGER. It is necessary to bind X manifest, but must not become a 29th technical story or inflate Materiality/Selection. Record a lawful non-editorial handling policy consistent with Core. Do not reinterpret one receipt as a 50th important release.

**E42-06 — Negative-space inspection (REQUIRED).** Important INSPECT/THIN candidates (Sakana/harness/Amazon papers, video/audio/Japan/local deployment, AWS and GitHub groups) cannot all be dismissed by one locator-only look-up. Pursue bounded retrieval loops, record dated negative searches and explicit defensible HOLD/CONTEXT rationale. Prevent technical magazine from being compressed to vendor announcements while original-source paragraphs remain unconsumed.

## 4. Authoritative next boundary

The valid `CANDIDATES_NORMALIZED` state and accepted Discovery/Screening **stand**. No upstream invalidation requested.

Muse should execute a **single substantial Evidence authority gap-fill and candidate-local regeneration** unit: retrieve and read actual first-party bodies/license text and material studies as available; convert technically relevant claims to source-linked candidate-local Evidence with comparison, limits, chronology and reader-facing technical detail; rebuild Core-proposed cards and views; run deterministic validation and stop at fresh `SOL_EVIDENCE_AUTHORITY_REVIEW_READY`. Do NOT accept Evidence, advance Materiality/Selection/Architecture, create a PDF or infer Human approval.

For external claims, distinguish source verified vs vendor claimed; when full primary retrieval fails, log real access method, URL, date and nonpromotable limitations. No fabricated byte archives, independent reproduction, accepted hashes, or synthetic claims. Review criterion is **substantive traceable research**, not larger counts.
