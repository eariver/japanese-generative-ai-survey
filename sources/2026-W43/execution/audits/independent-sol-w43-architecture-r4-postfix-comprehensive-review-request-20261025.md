# J-GAS W43 — Independent Sol architecture r4 post-fix comprehensive audit request

Status: READ_ONLY_INDEPENDENT_AUDIT_REQUEST / NO_STAGE_ADVANCE / NO_HUMAN_DECISION
Date: 2026-10-25 JST
Owner: editorial Sol. Execution: a NEW, separate independent Sol chat session.
Repository: eariver/japanese-generative-ai-survey
Exact **AUDIT TARGET** commit: ee206400c9740dd2288b894f31f79a119b7758bc
Exact audit Root Tree: 49f55eef6e8fc5beacc1645b62ba0d25e42ccb1d
Branch (existing only): weekly/2026-W43-v2-work
Reviewed main: 041a08dfef3112643cbf85b4a86a7b6f9128aed6 / a134dc36a407d08ab1de416324229b3955e0325a
Frozen Core v2: 774dd39a951c9ac3818e83dfffd4c7666efb0a20 / cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481

## Authority and restrictions

- You are an INDEPENDENT, read-only auditor, NOT the editorial Sol, worker Muse, trusted Operator, or Human Owner.
- GitHub reads only. DO NOT write commits/files/issues/comments/branches, run trusted Stage Bridge, call /survey-core-execute, change Production State/Checkpoints/Human Gates, approve Architecture, publish, or instruct Muse directly.
- Before evaluating, independently resolve all remote HEAD/Tree values and the exact audit target SHA/Tree. The branch may have moved for the addition of this request file; audit the *fixed target commit*, not an unverified latest branch.
- Blind-first: inspect actual candidate Matrix, Selection, 8 Architecture packages, all 31 must-cover clauses, review summary, all 68 Attention items, and original evidence/source references BEFORE reading the Muse closure/PASS assertions and prior audit defects. Seek NEW defects in addition to the nine known findings.
- Distinguish observed facts, source-read facts, validator outputs reproduced by you, worker-reported outputs, and NOT_EXECUTED tasks. Never call schema pass a factual correctness pass.

## Required inputs in this target commit

- sources/2026-W43/production-state.json
- sources/2026-W43/candidate-matrix-v2.json
- sources/2026-W43/candidate-selection-v2.json
- sources/2026-W43/architecture-v2.json
- sources/2026-W43/architecture-review-summary-v2.json
- sources/2026-W43/architecture-review-attention-v2.json
- sources/2026-W43/orchestration/v2/interactive/selection-architecture-{input,audit}.json
- sources/2026-W43/execution/history/selection-architecture-r3/ (7 JSON + README + SHA256SUMS)
- sources/2026-W43/execution/compat/selection-architecture-input-r4.json
- sources/2026-W43/execution/reviews/muse-w43-independent-isa-closure-architecture-r4-20261025.md
- sources/2026-W43/execution/reviews/w43-human-selected-19-risk-register-r4.md
- sources/2026-W43/execution/source-intake/w43-independent-isa-primary-source-conflict-crosswalk-r4.md
- sources/2026-W43/execution/audits/independent-sol-w43-selection-architecture-r3-comprehensive-audit-result-20261025.md
- sources/2026-W43/execution/reviews/sol-w43-selection-architecture-r3-independent-comprehensive-adjudication-20261025.md
- sources/2026-W43/execution/instructions/sol-w43-architecture-r4-comprehensive-isa-repair-20261025.md
- accepted r4 Evidence/Views, 51 Materiality records, Completeness LIMITED, supplement source IDs and immutable raw bytes when available.

## Audit plan

A. **Structural/provenance:** prove r3 Matrix and Selection are byte-identical to r4; 32 decisions = 19 SELECTED / 1 HOLD / 12 REJECT; exactly 19 nonduplicated placements in 8 packages; 31 must-cover entries; 68/68 unique attention, no truncation; 19 selected candidates each in the *separate* risk ledger; 5 residual LIMITED accurately carried. Inspect actual output hashes, r3 SHA256SUMS and input->output->summary/audit binding. Check scope of changed files vs exact starting HEAD db78839bd7cb858a6cc5b1620bf6c574f064339f and confirm all excluded state/Evidence/Core/Gate files unchanged. Run frozen Core-native validation only if legitimately executable; otherwise NOT_EXECUTED and report exact evidence used.

B. **P1 ISA-001, DeepInfer:** primary https://github.com/deepseek-ai/DeepInfer README plus pinned edition commit 9bd9cf24 and environ.py. Confirm variable-length DSpark MTP uses DEEPINFER_ENABLE_MTP_VARLEN=1 (NEXTN default 5, 0 off), whereas deterministic sampling requires DEEPINFER_ENABLE_MTP_VARLEN=0 AND DEEPINFER_BATCH_INVARIANT=1 AND fixed seq_seed in SamplingParams on NVIDIA. Test whether r4's P2 §2.2, purpose, boundaries and Draft MUST-NOT prevent conflation. Compare claims to pinned version; distinguish live main from W43 archival provenance.

C. **P1 ISA-002, Voxtral:** verify Mistral launch https://mistral.ai/news/voxtral-3/ TTS 35+ languages/50+ dialects, model card https://docs.mistral.ai/models/voxtral-mini-tts-3-0 9 languages, and https://docs.mistral.ai/studio/audio/specs-and-limits/languages 35/50+, 22-row preset voice table; announcement separately says 18 preset languages. Verify r4 P5 §5.1 and all references distinguish transcription vs realtime vs TTS vs cloning vs presets vs 11-language *evaluation sample*, do not invent '9=presets', and carry UNRESOLVED_VENDOR_DOC_CONFLICT with no universal count. Inspect publication/preview status and manufacturer version/date differences.

D. **P2 ISA-003..009 full sweep:**
- Nemotron 8B total/4B effective versus Flint 39.8B total/~2.5B active per token, counting conventions, OpenMDW-1.1 vs Gemma-4 license, no unsourced OSI recognition.
- FLUX: 277.80/10.95≈25.37, 277.80/12.45≈22.31 and latency reduction 95.52%; vendor 26.5x/96.2% internally inconsistent with 12.45s; independently recalculated is NOT independently measured. New lead: fal-originated press release at https://www.prnewswire.com/news-releases/fal-launches-flux-3-max-delivering-1-tier-image-to-video-quality-at-industry-leading-speeds-302913033.html cites 10.95s but is NOT yet a preserved edition raw benchmark, and may represent different conditions. Verify original timestamp, measurements, apparatus, resolution, length, quality, GPU, batch, cold/warm and attribution. Also check official https://fal.ai/flux-3-max and https://fal.ai/blog/introducing-flux-3-max-by-fal.
- Decisions: https://developers.openai.com/api/docs/guides/decisions — 400 questions PER REQUEST; uncached input $0.10/M and cache read $0.01/M, writes charged, regional and long-context multipliers, no output-token charges != free overall.
- Attention 68 exception-focused vs separately selected-19 risk coverage; P8 3.5pp ESTIMATE backed by density plan, no padding; Japanese terminology first-use accuracy; IN/OUT/FUTURE exact W43 cutoff [2026-10-16T22:00Z,2026-10-23T22:00Z), Kimi weights Nov4 FUTURE, 1Password coming soon, TanStack product Oct22 vs blog Oct23 unknown clock, GitHub Metrics 23:42:03Z OUT, Grok binder NEVER_STORY.

E. **Unforeseen defects:** investigate source-to-claim references and actual first-party bytes across ALL 19 selected and 8 packages, not only modified strings. Look for false exact arithmetic/units, source-contradicted benchmark, license, chronology, selection validity, invented citation, unsupported mechanism, mistranslation, misleading marketing superlatives, thin page allocations and new constraints leaked from r3. Sampling is acceptable only if the sample/rationale and unreviewed population are explicit. Spot-check the unreviewed long MemT paper and AA/bench limitations; do not report FULL_LINE_BY_LINE unless executed.

## Output and formal decision

Deliver a single comprehensive Japanese Markdown report: metadata (audit SHA/Tree), methods and files actually inspected, P0/P1/P2 findings with IDs + JSON pointers + precise quote/first-party URL/preserved raw provenance + recommendation + regression test + not-reviewed scope. Give ISA-001..009 each PASS/LIMITED/FAIL/NOT_VERIFIED; separately score Selection and Architecture PASS/PASS_WITH_LIMITATIONS/REQUEST_CHANGES and whether **Selection Trusted Bridge** and **Architecture Trusted Bridge** may be individually proposed. Distinguish editorial acceptance from actual Core operator receipts, and do not issue Human approval. Include actionable bounded follow-up if blocked.

Save the ORIGINAL independent review in Google Drive folder GPT-Sol_Review using YYYYMMDDHHMMSS_SolReview.md if that app is accessible; report its link and genuine raw SHA256 if actually computed. If save unavailable, return the full Markdown to the Human Owner for transfer. Do not write anything to GitHub.

Stop after the independent read-only report. Editorial Sol alone will adjudicate it and commission Muse/Operator work.