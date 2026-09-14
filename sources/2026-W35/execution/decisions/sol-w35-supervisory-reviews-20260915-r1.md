# Sol supervisory reviews — W35 resume-from-Grok-r3 run (r1)

Status: `SOL_SUPERVISORY_REVIEW / PRE_GATE / ARCHITECTURE_REVIEW_PENDING`
Date: `2026-09-15 JST`
Reviewer role: Sol (independent of Luna/Work execution; this run's execution and review were performed under explicit Sol ownership of research sufficiency, authority consumption, materiality, selection, and architecture).
State reviewed: `ARCHITECTURE_ESTABLISHED` (machine checkpoints discovery/screening/evidence/materiality/completeness/selection/architecture all passed).

## 1. Discovery completeness review

Surfaces exercised: Sol-reviewed Grok/X r3 ledger (35 URLs) + 19 first-party/secondary retrievals stored as edition-local Raws + pre-Discovery web breadth sweep.
Lanes covered by accepted Discovery: A (foundation), B (agents/coding), C (multimodal), E (video, thin), F (speech/audio via HUG-VIS voice-cloning only), G (open/local), H (serving), J (evaluation), K (safety/security), L (other/governance).
Negative-space sweep (independent of the ledger): tracker-dated but uncorroborated in-window items exist without retrievable primaries — Gemini 3.5 Transcribe (08-26, speech), Apodex 1.1 (08-24), Ling 3.0 Flash Fin (08-28). No first-party source was located in this run's sweep; promoting tracker rows without retrieval would violate evidence-first discipline.
Duplicate/concentration: the three open-weight releases dominate X momentum (expected concentration, not hidden); agent-tooling and governance lanes are independently sourced outside X.
Residual coverage limitations (explicit): image-generation lane has no material in-window candidate (Grok CANDIDATE_NOT_SELECTED corroborated by sweep); speech/audio model lane likewise; memory/multi-agent has no distinct cluster (UNCERTAIN); MiniMax first-party recheck not re-executed (no new dated event surfaced).
Finding: NON-BLOCKING. No silent concentration; gaps are declared, not hidden. A quiet-lane call is defensible after this sweep.

## 2. Evidence authority-consumption review

Classification of the 19 task authorities:
- AUTHORITY_CONSUMED (8 VERIFIED cards): Grok r3 ledger (read in full, 234 lines); Anthropic alignment page (full); OpenAI Kiro page (full); grith launch post (full); Harness release body (exact lines recovered); OpenThai launch post (full); vLLM v0.28.0 notes (substantive sections); 2 arXiv abstracts (abstract-level, explicitly bounded).
- CAPTURED_BUT_UNCONSUMED: none. Every bound Raw was read in full during this run; PARTIAL status throughout reflects missing vendor primaries, never unread bytes.
- AUTHORITY_RETRIEVAL_FAILED: z.ai blog + HF cards (empty/failed fetch; secondary + X rows used instead, PARTIAL); GitHub release API (not attempted; release page used).
- AUTHORITY_NOT_FOUND: image-lane primary; speech-lane model primary; MiniMax recheck primary.
The W34 failure mode (retrieval count ≈ understood) is not repeated: 11 PARTIAL cards separate consumed-relayed claims from unverified primaries with exact verification targets.
Additionally corrected pre-commit: initial Discovery used a custom source_type vocabulary outside the closed Evidence authority map; classified as ISSUE_LOCAL_CONTENT_PROBLEM (existing canonical classes covered all cases), repaired edition-locally by rebasing to PRIMARY_OFFICIAL/PRIMARY_PAPER/SECONDARY/SOCIAL and regenerating all downstream bytes. No generic Core defect; no repair branch; Production Line untouched.
Finding: NO BLOCKING DEFECT.

## 3. Materiality and Selection review (with unselected-evidence inspection)

Positive: all 17 SELECTED carry MATERIAL status with VERIFIED/PARTIAL evidence and PRIMARY/SUPPORTING usage + WEEKLY: roles.
Negative: 1 DROP (Muse Code, pre-window background — chronology verified against byline, not snippet date); 2 HOLD (abstract-only CONTEXT papers — inspected, correctly unarchitected); X-carried Nvidia-HF rumor and video fragments correctly kept out of candidacy (unconfirmed/fragmentary). Post-window NVIDIA-HF confirmation (Sept 10) is out of scope and correctly excluded.
Compression check: SELECTED=17 (trigger SELECTED<=1 not met); no compression audit required. The issue is not sparsely architected to hide weak research: 5 packages over 17 candidates with genuine HOLD/DROP negatives.
Grouping check: three open MoEs grouped in P1 (shared efficiency-architecture thesis, distinct licenses/specs preserved); agent-plane items grouped in P2 (distinct protocol/forge/context/review/security roles preserved); governance contrast grouped in P5 with non-equivalence bound.
Finding: NO BLOCKING DEFECT. One non-blocking note: P1 leans on three PARTIAL secondaries — acceptable only because must-cover requirements inherit the verification bounds into drafting.

## 4. Sol Architecture review

Thesis fits the window: open-weight efficiency turned architectural + agent-plane reorganization + bounded flagship/governance. Package order P1->P5 follows evidential weight (strongest convergence first). No W34 structure copied (verified: W34 packages were collaboration/agent-control/safety/model-economics/creative/retrieval themed; W35's five are window-specific).
Alternative considered and rejected: flagship-first ordering (Fable-led). Rejected because flagship claims are the least-verified (PARTIAL, primaries missing) while the open-weight cluster has the deepest corroboration; leading with the weakest-verified claim would mislead.
Page/section allocation: deferred to drafting (noted in page_plan); no optional-section omission decided yet.
Known risks for the Human: (a) P1's three anchors are PARTIAL — drafting must preserve bounds; (b) thin image/audio lanes are real gaps, not oversight; (c) all vendor figures stay publisher-only.
Sol findings: 0 blocking, 3 non-blocking (coverage residuals; P1 PARTIAL weight; page allocation pending).
Recommendation: present for Human Architecture Review; do not auto-advance.

## 5. Human Gate discipline

No Human decision recorded or inferred. Dossier accompanies the pending Gate; short READY status is not the review surface.
