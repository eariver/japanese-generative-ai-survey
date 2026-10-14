# W41 Selection Proposal / Preview r6 (PROPOSED_NOT_ACCEPTED, Sol review pending)

Status: `PROPOSED_NOT_ACCEPTED / EVIDENCE_REVIEWED / STOP_BEFORE_SELECTION_ACCEPTANCE`
Date: 2026-10-12 JST
Branch: `weekly/2026-W41-v2-work` (existing only)
Basis:
- Matrix preview `execution/candidate-matrix-r6.PROPOSED.json` SHA `0d56de2b8b1b0417ce7f0cac34283a4549e6e91ca5279016aa826416e9f98d25`
  (36 candidates; Core-derived via `derive_candidate_matrix`, `validate_candidate_matrix` PASS).
- Selection preview `execution/candidate-selection-r6.PROPOSED.json` SHA `3bedcb4acbb80647539ef3a318fd6ce654e31a540d9a6e76e55d2361ab729033`
  (20 SELECTED / 13 HOLD / 2 INSPECT / 1 REJECT; `validate_selection` PASS).
- Materiality r6 `51890f06…` (20/13/3/1), Completeness r6 `f3d5a122…` (LIMITED),
  Views `cd661097…` (20/13/3), Evidence `717ea04a…` (36, immutable).
- Dossier: `execution/materiality-editorial-dossier-r6.md` (20-candidate depth).
- Exclusion: `execution/nanobanana-legacy-negative-exclusion-r6.md`
  (`LEGACY_UNVERIFIED_NEGATIVE_DO_NOT_CITE`; Selection rationales use only
  admissible `not found among pages checked 2026-10-12`; Matrix internal
  boundary hit documented, reader surfaces clean).

This is a NONCANONICAL preview. No canonical Selection Acceptance was invoked,
no `SELECTION_COMPLETE` advancement, no Architecture stage, no Human decision.
Canonical paths `sources/2026-W41/candidate-matrix-v2.json` /
`candidate-selection-v2.json` were NOT created. Sol must independently review
this preview before any canonicalization.

## 1. Reader-level issue narrative

W41 is a flagship-rollout-plus-provenance week. OpenAI shipped GPT-6 with a
tiered Intelligent UI rollout and a changelog-pinned Decisions API beta;
Anthropic answered with Haiku 5.5 pricing and a Cyber Mission program; Google
shipped an image-model card (Nano Banana 2.1) and a SynthID portal expansion
while OpenAI shipped a measured EU text-watermark (textGrain) — the issue's
only first-hand quantitative read. Around those flagships, downloadable
open-weights (Kolibri, Liquid d1, EmbeddingGemma 2) contrast with promised
weights (Beam, Mistral Large 4 end-month), and decision-model/forum announcements
(Perplexity pair, Nace Drex HOLD, MS-Decision-1 HOLD) show where the
decision-inference lane is real versus snippet-only. The honest editorial
thesis: *measured rollouts and priced APIs versus vendor-only benchmarks and
preview promises, with provenance tooling as the verifiable through-line.*

Grok X ledger contributes zero articles. It is cited only as intake provenance
(14 posts, 12 in / 2 post) in methods/acknowledgments, never as a news item.

## 2. Lead news selection

LEAD: GPT-6 + Intelligent UI rollout (A1) with Haiku 5.5 (A2) as co-lead
pricing sidebar. Rationale: only A1 has tier/date/tab rollout mechanics plus
a verified latency-figure distinction (44% is start-latency) directly affecting
JP Plus/Free users; A2 has the only split-pricing table with a halved Sonnet
cache rate. Both are vendor-stated but structurally pinned (dates/tiers/rates
VERIFIED as stated). Alternative lead (Haiku-first) rejected: Haiku benchmarks
are entirely vendor-run with system-card unfetched, while GPT-6 has rollout
mechanics + infra siblings (Decisions, Ultrafast) for a platform story.

## 3. Grouped technical mechanics (5–7 articles, not 20)

1. Frontier rollout week (LEAD): A1 PRIMARY + A2 PRIMARY + C3 Ultrafast box.
   Mechanics: tier rollout, price split, service-tier infra; latency carefully
   split (44% start vs inter-token purpose).
2. Agent platform + infra: C1 PRIMARY anchor (Decisions beta, VERIFIED
   changelog) + A5 stub contrast + C2 brief + C4 one-liner.
   Mechanics: decision endpoint vs stub announcement; forum-measured Index/Bench.
3. Open weights shipped vs promised: B1 PRIMARY anchor (Kolibri downloadable)
   + B2/B3 briefs + B4/B5 comparators + B6 speech box + A4 speech pair.
   Mechanics: MoE scale/context/license/download table; vendor-bench attribution.
4. Image spec: A3 SUPPORTING brief (exclusion-compliant).
   Mechanics: card spec block + vendor-Elo caveat + narrowed blog note.
5. Provenance week: D2 PRIMARY anchor (textGrain FPR/token/edit, first-hand)
   + D1 SUPPORTING (SynthID scope/partners).
   Mechanics: FPR methodology actually read (the issue's deepest numbers) vs
   portal scope (no efficacy claim).
6. Safety + science briefs: E1 + F1 + F2.
   Mechanics: program terms, repo/Lean list, EDGAR-simulated eval — each with
   explicit non-claim boundaries.

## 4. Expected evidence citation (per article, claim-bounded)

- Art.1: A1 page (tier/date/tab/Sol-Luna/44%-start), A2 page (split rates,
  bench table), C3 changelog (tier/residency). Cite as vendor-stated; no
  wall-time or leadership claim.
- Art.2: C1 changelog entry verbatim (beta + gpt-6-luna + 10x caveat), A5 stub
  bullets + unfetched box, C2 forum (date/price/Index), C4 forum line.
- Art.3: B1 page (78B/3B, 1M, Apache-2.0, HF path, benches), B2 page (HF paths,
  Index, 8ms), B3 blog (740M/MRL/8K/Apache-2.0/HF+Kaggle, MTEB), B4 page
  (501B/23B, intent, later-month), B5 blog+docs (52B/1M/API/pricing/weights-date
  + 49B disagreement), B6 changelog (timestamp-pin + specs), A4 AWS page
  (GA/regions/256K).
- Art.4: A3 card excerpt (Gemini 3/3.6 Flash, 1M/4K+64K, 7-channel, vendor Elo)
  + admissible blog-search line only.
- Art.5: D2 blog (FPR/edit/Astra/detector-gating, first-hand) + PDF-unread box;
  D1 blog (modalities/partners/scale, text-excluded) + portal-unfetchable box.
- Art.6: E1 page (CIDP/11 partners/scanner terms/>90% expected), F1 page
  (repo/Lean/summaries/compute + non-release), F2 page (11-task/EDGAR/numbers).

## 5. Competing alternatives considered and rejected

- Haiku-first lead: rejected (§2; rollout mechanics favor GPT-6).
- Mistral-Large-4-first open-weights lead: rejected (preview, weights pending;
  Kolibri downloadable is the honest anchor).
- Drex/StepFun rescue (promote HOLDs to fill pages): rejected (JS-gating /
  shortlink gaps are real; snippet promotion would inflate).
- Grok-ledger-as-article (21st MATERIAL): rejected and corrected (provenance,
  not event; r6 CONTEXT).
- 20-articles-from-20-MATERIAL: rejected as inflation (thin items grouped per
  dossier §8).

## 6. Treatment of all 20 MATERIAL (SELECTED 20/20)

All 20 MATERIAL are SELECTED (PRIMARY 5: A1/A2/C1/B1/D2; SUPPORTING 15).
No MATERIAL is held or rejected. Thin items (A5/C4/B4) are SELECTED as
explicit comparators/one-liners inside grouped articles, not as standalone
articles — selection ≠ article count. Minimum-evidence column from the dossier
is the binding floor for Draft; anything thinner than that floor must be cut
to a sidebar, not expanded.

## 7. Why 13 HOLD / 3 CONTEXT are out (or sidebars)

HOLD 13: all HOLD (usage NONE). 12 NEEDS_MORE + Drex PARTIAL/HOLD per dossier
§7; each lacks the dated hook, retrievable body, or license/clock pin to
anchor claims. Promoting any HOLD on X-timestamp or snippet pricing alone
would be the exact inflation Sol flagged. Drex and StepFun are highest-regret
but correctly held.

CONTEXT 3:
- Grok ledger → REJECT (never publication, not even sidebar as event; methods
  provenance only).
- Usage-policy (VERIFIED CONTEXT) → INSPECT (governance sidebar candidate).
- ELYZA (pre-window JP) → INSPECT (JP background sidebar).
INSPECT here means sidebar-eligible at Architecture, not selected. If
Architecture finds no sidebar slot, both correctly fall out without affecting
the issue spine.

EXCLUDED sweep: correctly out.

## 8. Honest page/word-depth estimates (NOT pagination)

No TeX/PDF exists; exact pagination is explicitly NOT fixed. Qualitative only:
- Art.1, Art.3, Art.5 can carry deep-dive weight (tables + pins).
- Art.2 carries medium weight (one VERIFIED changelog + contrasts).
- Art.4, Art.6 are briefs by evidence boundary (spec/program/result boxes).
Honest total: a full Weekly issue (5–7 grouped articles + 0–2 sidebars), not
20 articles and not a thin issue. If Draft finds Art.2/Art.4 thinner than
floors, cut to sidebars rather than padding with HOLDs or vendor repetition.

## 9. Validation and stop

- `validate_edition_view` 36/36 PASS; `accept_edition_views` → `cd661097…` PASS;
  `validate_edition_views_acceptance` PASS.
- `build_materiality_ledger` → `51890f06…` (20/13/3/1) PASS.
- `validate_profile_completeness` PASS under agent-tool override (bare run:
  historical screening state-basis drift only, narrowly documented).
- Stage validation `evidence-stage-validation-r6.json` PASS
  (CANDIDATES_NORMALIZED→EVIDENCE_REVIEWED); checkpoint
  `orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json` built;
  `advance_with_checkpoint` → EVIDENCE_REVIEWED (evidence/materiality/
  completeness passed; gates pending).
- `derive_candidate_matrix` → `0d56de2b…` PASS; `validate_selection` → PASS
  (`3bedcb4a…`, 20/13/2/1).
- Exclusion grep: Selection assignments NO_HITS (forbidden); Matrix internal
  boundary hit documented in overlay §5 (audit, not violation).
- STOP: no Selection Acceptance, no SELECTION_COMPLETE, no Architecture,
  no Draft/PDF, no Human Gate. Terminal: `SOL_SELECTION_MATERIALITY_PREVIEW_REVIEW_READY`.

Sol: this preview plus dossier + overlay + r6 PROPOSED files are the review
inputs. Canonicalization (if approved) is a separate Sol-authorized step.

(End of file)
