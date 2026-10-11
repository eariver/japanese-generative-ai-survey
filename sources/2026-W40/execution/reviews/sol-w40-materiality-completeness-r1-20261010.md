# Sol W40 Materiality and Completeness Review r1 — conditional editorial approval with two specific repairs

Status: `SOL_MATERIALITY_SEMANTIC_REVIEW_CONDITIONAL_PASS / MC01_MC02_REQUIRED_BEFORE_CORE_CHECKPOINT`  
Date: 2026-10-10 JST  
Repository: `eariver/japanese-generative-ai-survey`  
Existing branch: `weekly/2026-W40-v2-work`  
Reviewed Muse r8 HEAD: `6fc888be1920c8509ee8397479dc98b186121f9d`; Tree: `5d52f0edad1baf29423c26caf247eaf310ccb5a1`  
Reviewed main HEAD: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`  
Production State at review: `CANDIDATES_NORMALIZED`; next `stage:evidence-materiality-completeness`. Evidence/Materiality/Completeness checkpoints pending; both Human Gates pending.  
Fixed W40 UTC window: `[2026-09-25T22:00:00Z, 2026-10-02T22:00:00Z)`.

## 1. Technical execution and accepted authority — PASS

- Exact Sol r8 contract starting HEAD `98ef2db27bd11fef3ab96bef5a77af3f43aa59b0` and tree `dc126139938e7bb56b71a60fd14314a9ff1c5440`; Muse r8 finished as the immediate one-commit child, 224 W40-local paths only. Remote `main` unchanged and no Core/schema/config/Gate writes or reset/force. Stopping before Core combined Evidence/Materiality/Completeness State transition was respected.
- Official frozen `accept_evidence_results` created Evidence Acceptance `evidence/v2/accepted/0a62346f0729e768d1b67305dd96e0e99224326c862831abe79e43ced4875e07/evidence-accepted.json`, 35/35 cards (29 VERIFIED / 6 PARTIAL), package SHA `30b63b119a63f3fbec9c771aa415b7d7880db8d40a1715930bc063306606818e`; structural validation PASS.
- Official `accept_edition_views` created Views Acceptance `evidence/v2/views/accepted/60b622f659224cf1862ecdb4aa06563ee4f31ed69d2bb74f9e88c32f76e2925e/edition-views-accepted.json`; all **35** Evidence result SHA cross-references independently compared by Sol and **0 mismatches**.
- SC-E10 cleanup: r8 current reader-facing claims and Views refrain from unsupported ProvenanceGuard `v3/Aug27 current` assertions. Historical canonical source title remains immutable with explicit `execution/provenance-exceptions/LEGACY_UNVERIFIED_DO_NOT_CITE-guard-title.md`; paper v2 July26 only establishes method/results, W40 event is Sep29 team blog. The Card's inherited src-1 legacy title is not independently a current publication-time authority.
- Reviewed r8 draft Materiality Ledger covers all **37** Discovery records exactly; the frozen validators see no missing task/Screening decision or View-status drift. Completeness draft is structurally valid `LIMITED`, **3 SATISFIED obligations and 11 residual limitations**, not an unsupported unrestricted READY status. No Selection/Architecture/Human authority exists.

## 2. SC-M01 [BLOCKER FOR CANONICAL STAGE] — Evidence-source observation incorrectly classified as a technical material event

Existing r8 `w40-grok-x-ledger-20261009`:

- `Evidence.status=PARTIAL`, and the explicit reviewer rationale reads **"Required X-bound observation authority for Weekly profile; community-signal coverage, not article candidacy."**
- Nonetheless its **ACCEPTED Edition View** class is `MATERIAL`, `profile_annotations.window_relation=MAIN_EVENT`, and draft Materiality Ledger counts this as a `MATERIAL` item.
- This is **a Source Intake provenance ledger** covering four auditable X URLs and separately 64 Daily X URLs; it is not one independently new technology/event. It cannot be placed on the same Selection candidate plane as the actual technical 2026-W40 releases. It must remain citable as intake/provenance, without pretending it is a news item.

**Sol's explicit decision:** in the next edition-local **new accepted View set** change exactly this one non-event View to `materiality.status=CONTEXT`, rationale `X/Daily X provenance and coverage methodology; not independently publishable technical event; source records for actual posts are separate Discovery candidates`, `profile_annotations.window_relation=OTHER`, `why_this_issue` likewise and `carry_over=false`. Exact Evidence Card SHA must remain unchanged; its claims and X provenance remain intact. All other 34 View statuses and source bindings unchanged.

This results in **29 MATERIAL technical leads, 4 HOLD, 2 CONTEXT (LIFT + X ledger)** within the 35 non-DROP Evidence/View records, plus **2 EXCLUDED** methodological sweep logs in the 37-row Ledger. 29 MATERIAL does **not** mean 29 articles: DevDay hub, API releases and related agent capabilities overlap and must be grouped coherently at Selection, with clear per-artifact attribution.

Because Core v2 requires Materiality Ledger `downstream_disposition` equal the active View status, it is **not permissible simply to edit the Ledger's Grok row while retaining r8 accepted View hash**. Regenerate the **one changed View in a fresh immutable 35-View set**, run normal frozen View acceptance/validation and rebind the new Ledger/Completeness to the new exact View Acceptance SHA. Preserve the r8 accepted pair as historical; Evidence Acceptance and Cards do not change.

## 3. SC-M02 [BLOCKER FOR SEMANTIC COMPLETENESS] — mechanically populated ledger/obligation rationales

r8 Materiality Ledger has all substantive `MATERIAL` rows with a single generic tautology such as `Screening=KEEP; Edition View=MATERIAL`, rather than item-specific technical rationale, proof of in-window event, actual consumed authority and exclusion/aggregation alternatives. This is structurally valid but **insufficient for the mandatory Sol materiality and negative-selection review**.

r8 Completeness `weekly:current-relevance`, `weekly:technical-significance`, **and `weekly:carry-over` each reference all 37 Discovery IDs and all 35 Evidence Task IDs**. This makes the carry-over obligation falsely appear to be about every W40 newly released model rather than the two carried unresolved W39 leads. The `SATISFIED` flag alone has no semantic evidential force.

**Sol's explicit repairs:**

- Supply a defensible, source-specific reason for each of **37** Ledger rows: technical contribution and W40 date/provenance for 29 candidate events; exact HOLD basis and what would release it; pre-window context for LIFT; provenance-only X; two methodology-log EXCLUDED; cross-release dedup and editorial grouping guidance (without editing frozen accepted Screening `duplicate_group`).
- Keep the r8 Evidence/Screening classification of the **other 34** non-X views unchanged; do not manufacture performance reproduction for vendor metrics or advance time-unknown AstaBrief/AutoSynthData.
- Rewrite the three Completeness obligations to use semantically appropriate **distinct subsets**: `current-relevance` covers contemporaneous announcements and explained temporal holds; `technical-significance` covers meaningful technical candidates and justified strong-but-limited work; `carry-over` directly binds the two W39 inherited HOLDs `w40-carryover-pixelcanary-20261009` and `w40-carryover-tbc-video-20261009` only. Methodology logs and X provenance should be referenced as research-process support, not masquerade as an eligible W40 technical release.
- Keep 11 r8 disclosed source/benchmark/availability limitations unless independently resolved, do not claim fully reproducible methods or globally exhaustive web coverage. `LIMITED` is acceptable for Weekly if no material obligations are secretly left in `NEEDS_RESEARCH` and each HOLD is honestly justified. If validators or newly identified source issues require `INCOMPLETE`, **fail closed** and stop for Sol, do not force `LIMITED`.
- Add a separate editorial **Selection-input dossier** with 29 material leads and grouping/strong omission risks. Avoid auto-creating 29 thin articles or compressing major developments to two generic paragraphs.

## 4. Sol preliminary materiality judgment — semantically acceptable after exact SC-M01/M02 corrections

Sol has independently inspected the accepted Card/View basis and vendor-claim boundaries, not merely counts. The material W40 themes are technically plausible and sufficiently differentiated for **Selection consideration**, with publisher-reported metrics attributed:

- Frontier/general/agent models: Claude Sonnet 5.5, GPT-6.1 Sol, Gemini 4 Argon, Holo4 weights+GUI/agent, Japanese ELYZA 33B + MoE. **ELYZA is MATERIAL** because JA-centered training/evaluation/weights is significant to this Japanese Survey, not because it beats every frontier model. Distinct Holo4 model licenses must remain split.
- Typed decision inference: Ollama local System One support, Cloudflare Clef/Clef-flash, Strands Decider 2B. Same theme, different release types; no apples-to-apples vendor benchmark comparisons.
- Agent safety/provenance: OpenShell/Sentry, OpenAI safety-case guidance, DeepMind SynthID Bio, ProvenanceGuard (Sep29 team blog with pre-window paper), OAuth/MCP auth; separate enforcement vs evaluation vs watermark vs attribution.
- Methods/serving/evaluation and research infrastructure: Context Language Models, AA-AgentPerf-Local, Olmo-core 3 MoE training framework, HF RL Environments, Open TTS Leaderboard. Publication/report/code consumption limitations must appear in eventual manuscript.
- Visual, audio and product platform: FLUX 3 Image, VSS 3.3, Nemotron ASR adaptation, NeMo Relay, AMD Ross/World Labs, OpenAI dots and specific DevDay Agents/Decisions/Ultrafast capabilities, Cloudflare AI Search, DGX Spark 64GB (Oct2 announcement vs Oct23 future third-party shipping).

**Specific cautions**: W39 Pixel Canary/TBC remain HOLD; Oct2 AstaBrief and AutoSynthData publication clock remains TIME_UNRESOLVED, not ordinary; LIFT is PRE_WINDOW; DGX Spark is ordinary-eligible on the issuer's evidenced 13:00:39Z, but inclusion/price context remains Selection judgment; Olmo report 5MB+ retrieval limit must not be described as a consumed report; vendor benchmarks not independent reproductions. OpenAI DevDay hub contains overlapping child announcements, avoid counting it as an extra standalone technical release where duplicates.

## 5. Conditional execution release and review boundary

**Decision: `SOL_MATERIALITY_SEMANTIC_CONDITIONAL_PASS / MC01_MC02_REQUIRED`.** Authorize Muse to perform the exact one-View correction, rebuild frozen-Core acceptance for Edition Views, source-specific Ledger and honest Completeness, then **if** all authentic validators and SHA-linked Stage review requirements pass, perform official `CANDIDATES_NORMALIZED → EVIDENCE_REVIEWED` combined Evidence+Materiality+Completeness checkpoint/state transition.

This is a narrow preauthorized editorial classification and obligation-scope correction, **not** a blanket substitution of Muse's independent semantic review for Sol. Materiality categories of all other candidates and the validated Evidence Card set stay unchanged. If any semantic change besides the 1 X View or a substantive finding changes candidate merit/HOLD, STOP at Sol re-review rather than moving State.

After a valid checkpoint and transition, Muse may build a **PROPOSED_NOT_ACCEPTED Selection input/selection draft** under the Sol grouping/strong-omission constraints, but MUST stop at **`SOL_SELECTION_SEMANTIC_REVIEW_READY`**. Do NOT create canonical `SELECTION_COMPLETE`, Architecture, Human Architecture approval, Draft, or Publication artifacts in this unit.

The Sol Selection review must independently assess positive and negative candidates, editorial package count and depth, unresolved-vs-unconsumed sources, omitted high-signal candidates, duplicated DevDay/decision-model entries, and anti-compression counterfactual before Architecture.

Shared Core `CV2-DM-016` remains OPEN; no shared Core fixes at W40.
