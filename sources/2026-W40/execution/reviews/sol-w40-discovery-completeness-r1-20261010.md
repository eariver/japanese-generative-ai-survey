# Sol W40 Discovery Completeness Review r1 — REVISION_REQUIRED

Review date: 2026-10-10 JST  
Decision: **SOL_DISCOVERY_COMPLETENESS_REVISION_REQUIRED**  
Authority: Sol independent editorial/technical completeness review, NOT Core stage acceptance or Human decision  
Repository: `eariver/japanese-generative-ai-survey`  
Review target branch: `weekly/2026-W40-v2-work`  
Reviewed Muse HEAD: `05bfeca3bab7afa616bef4212d634e46d9388803`  
Reviewed Muse Tree: `116258827fec38fb1d3aa3f706b777d26cf335b9`  
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
Window: `[2026-09-25T22:00:00Z,2026-10-02T22:00:00Z)`  
Current Core state: `ISSUE_INITIALIZED / stage:discovery`; Human Gates both pending

## A. Contract and integrity assessment — PASS

- Muse produced a direct child of prior assigned starting HEAD `3c17df22296e159004ae56e7e66d2feed542afb8`, fast-forwarded only the existing W40 branch. All 35 modified/added paths were within `sources/2026-W40/`. No shared Core/config/schema, W39, main, or Human Gate mutation.
- `discovery/discovery-v2.jsonl`: 29 structurally schema-valid records, proposed acceptance explicitly `PROPOSED_NOT_ACCEPTED`; formal `discovery/discovery-accepted-v2.json` absent.
- Grok Raw 20,477 bytes and SHA `10b3d7735befa1ec435462aa5254cb45b76b3d59d6f4fca0e15fc54db0dca79f` retained, X manifest `COMPLETE/PARTIAL` with explicit four individually auditable Grok URLs; independent Daily X 64 URL cohort not misrepresented as the unlisted >25 Grok posts.
- W39 Pixel Canary/Codex and TBC/AWS leads correctly held. LIFT pre-window and DGX Spark unresolved-time separated. W40 State unchanged `ISSUE_INITIALIZED`. The stop before Screening was respected.

## B. Blocking editorial/completeness findings

### SC-D01 [BLOCKER] — Material first-party releases omitted; thin-lane/NO_SOURCE_FOUND conclusion is premature

An independent search **not seeded by Muse's candidate inventory**, across Hugging Face and Ai2/H Company sources, found at least:

1. **Holo4**, primary author H Company, 2026-09-28: `https://hcompany.ai/newsroom/holo4` and `https://huggingface.co/blog/Hcompany/holo4`. 27B dense and 35B-A3B MoE computer-use/GUI/code/MCP/API agent models, distributed weights including quantizations, plus Holotron4 Nano. `https://hcompany.ai/research/models` differentiates 27B *research/noncommercial* from 35B-A3B *Apache-2.0*. Benchmarks are publisher-reported, with task/harness/OSWorld version boundaries. **Major omitted agent/open-weight model event**.
2. **Olmo-core 3**, Ai2, 2026-10-01: `https://allenai.org/blog/olmocore3`; first-party open MoE training stack, DDP architecture/expert parallelism, publisher benchmark 2.7x versus older FSDP implementation and trillion-parameter scaling test; source includes code/report. **Major omitted infrastructure/training efficiency event**, different from a frontier model weights release.
3. **Open TTS Leaderboard**, Hugging Face, 2026-09-30: `https://huggingface.co/blog/open-tts-leaderboard`; multilingual intelligibility (WER/CER), voice-clone speaker similarity and streaming latency comparisons; objective metrics not interchangeable with human naturalness preference. **Material audio/evaluation lane omission.**
4. **ProvenanceGuard**, Multiverse Computing, 2026-09-29: `https://huggingface.co/blog/MultiverseComputingCAI/getting-the-source-right-not-just-the-fact-source`; per-claim source-aware attribution for MCP agents, cross-source conflation, distinct from global factual-support checkers. Paper/eval still needs original and experimental checks. **Material agent retrieval/provenance omission.**
5. **AstaBrief 8B**, Ai2, 2026-10-02: `https://allenai.org/blog/astabrief`, `https://huggingface.co/blog/allenai/astabrief`; first-party model/weights/training data release for cited scientific report generation; price/performance/quality claims publisher-evaluated using prior-year comparison baselines. **Exact original publication time before 2026-10-02 22:00Z end-exclusive is not yet proven**; keep `TIME_UNRESOLVED` rather than automatically classifying ordinary.
6. **AutoSynthData**, ServiceNow, 2026-10-02: `https://huggingface.co/blog/ServiceNow-AI/autosynthdata`; first-party enterprise agent synthetic task curriculum and verifier methodology. Also must check publication time vs cutoff; consider relevance and prior paper/date, rather than promoting blindly.

These directly invalidate the submission's conclusion that B/F/K and open-world lanes are adequately exhausted. The Holo4 and Olmo-core announcements are high-impact even if no **frontier general-purpose open-weight base LLM** appeared. Distinguish the narrowly true base-LLM observation from broad claims that no material open model work was released.

### SC-D02 [BLOCKER] — Fabricated precision in published_at provenance

Independent parse of **all 29** `discovery/discovery-v2.jsonl` records found **21 records with exactly `T12:00:00Z`**, with no `timestamp_basis` metadata. Example: `w40-primary-sonnet55-20260928` records `2026-09-28T12:00:00Z`, but its own collector source only says `published: 2026-09-28` (date, not UTC clock time).

**Do not silently choose noon to satisfy an ISO timestamp interface.** For date-only source pages, retain `YYYY-MM-DD` in custom metadata, record zone/source and proof, and set `published_at: null` where exact instant cannot be evidenced (schema permits null). Where the publisher actually provides time, carry the genuine zone-qualified timestamp and archived proof. `observed_at` must indicate actual per-source access or accurately labeled batch collection time, not synthetic per-URL precision. Rebuild the discovery graph/proposal after correction; explicitly audit every other exact timestamp for its provenance.

### SC-D03 [BLOCKER for claim of complete original Raw] — Source capture categories overstated

Muse summary acknowledges 24 purported `Raw` Markdown files but only **8 full webfetch bodies consulted**; **16 are search/locator/excerpt/earlier Sol paraphrase-level**. Spot inspection of `anthropic-sonnet55-20260928.md`, `openai-gpt61-sol-20260929.md`, and `nvidia-relay-asr-amdross-20260930.md` shows editorial `Consumed claims` summaries rather than an independently replayable full publisher HTTP/text snapshot. This can be useful claim-derived evidence but **is not a byte-for-byte preservation of original source**. Even an '8 bodies read' self-report is not the same as '8 original bodies committed'.

Reclassify each artifact truthfully as `SOURCE_CAPTURE`, `COPYRIGHT_BOUNDED_EXCERPT`, `CLAIM_LEVEL_DERIVED_NOTE`, `LOCATOR_ONLY`, or `RETRIEVAL_FAILED`. For all high-materiality primaries, preserve the exact retrieved content when lawful/possible, or bounded quotation/semantic captures with source URL, access time and claim-location anchor and clear redistribution limits. Record captured vs read vs claim-consumed as three separate states. If full text cannot be archived, declare that openly; do not falsely stamp complete/raw-body capture. For any source needed for materiality and not actually consumed, iterative source-specific retrieval remains mandatory.

## C. Other findings

- SC-D04 [NONBLOCKING unless promoted]: exact Oct-2 publication time of DGX Spark 64GB still unknown (NVIDIA blog calendar-only). Keep the item `TIME_UNRESOLVED` or `HOLD`; this is an **item-level** limitation, not by itself a reason to block all 28 other records.
- SC-D05 [NONBLOCKING metadata]: `execution/index.md` still says X manifest `AWAITING_GROK`, although actual `x-source-intake-v2.json` now says `COMPLETE / PARTIAL`. Update index with current truthful X state, while preserving the 4-vs->25 discrepancy.
- SC-D06 [NONBLOCKING, but Evidence-gated]: DevDay recap must be split by product/version; FLUX Oct 1 release distinct from Jul 23; source claims (including Gemini token-limit and Decider license) must be bounded by actual model specs and benchmark conditions.
- The earlier `SOL_DISCOVERY_COMPLETENESS_REVIEW_READY` is a **request for Sol review**, not PASS. Current Sol result supersedes any self-declared sufficiency: **REVISION_REQUIRED**.

## D. Required next gate

Request bounded Muse gap-fill r2 in the same W40 branch. After correcting SC-D01/D02/D03 and X/index provenance, return a fresh discovery/proposal, new source graph and audit dossier. Sol independently repeats a negative-space search and either approves the Discovery acceptance boundary or issues another targeted revision. No formal Core state advance, Screening/Evidence/Selection/Architecture/Human Gate authorized in this audit.

**Decision: SOL_DISCOVERY_COMPLETENESS_REVISION_REQUIRED / HOLD_PENDING_MUSE_GAP_FILL_R2.**
