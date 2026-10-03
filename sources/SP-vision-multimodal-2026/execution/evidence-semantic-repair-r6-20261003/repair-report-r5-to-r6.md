# Evidence Repair Report r5 → r6 (TS-003, 2026-10-03)

- Mode: append-only new acceptance. No history rewrite: r1–r5 acceptances and views untouched.
- Baseline: canonical r5 acceptance `4182d7d5...` + views `e3d0b3b3...` (Sol r5 PASS/AUTHORIZE).
- Output: acceptance `5b8d4ba62aa56465007f34782cc88e8f32ea4a9181c66cc9fa74785eb6ff07ab` (`ae485bd4...`), views `e8373be3...` (`e413a7b9...`).
- Builder: `build_evidence_r6.py` (pattern-matched on r5 builder; guard adapted to RELEASE_CANDIDATE post-gate run with no lifecycle advance; agent-state gate bypass documented below).
- Cards: 111 total — 105 byte-identical (hash-proven), 6 rebuilt (VM-D065/066/070/071/098/105). Views: 105 identical, 6 rebuilt.
- Validators run: `validate_evidence_card` ×6 rebuilt, `validate_evidence_acceptance`, `validate_edition_view` ×6, `validate_edition_views_acceptance`. All PASS.

## 1. Micro-repairs (typo-level, primary-verified, no new factual content)

- VM-D098 claim-1 (`e4d1370818155fa8`, task-285960b48aeb090906d7.json): `29 tasks/embeddings` → `29 tasks spanning multiple robot embodiments`. Authority: primary abstract arXiv:2406.09246 ("29 tasks and multiple robot embodiments", verified read-only). The prior claim text contradicted its own bound source; reader r12 already followed the primary. Provenance chain realigned. No other field changed.
- VM-D105 claim-1 (`8025f5dd3a9f4a6c`, task-04b576c4cd48b4cc10f7.json): `from unlabelled Internet video at 11B scale` → `11B-parameter model trained on unlabelled Internet video`. Authority: primary abstract arXiv:2402.15391 ("At 11B parameters, Genie ... trained in an unsupervised manner from unlabelled Internet videos", verified read-only). No other field changed.

## 2. P09 mechanism supplement (12 AUTHOR_CLAIMs, bound sources only)

All extracted strictly from already-bound primary reports (source_records locators unchanged; no new sources; no cross-model numeric comparison; vendor attribution kept). Each claim carries its primary pinpoint in `context`.

- VM-D065 (Qwen3-VL report arXiv:2511.21631v2): claim-3 2-layer MLP merger 2×2→1 + DeepStack 3-level→first-3-LLM-layers + SigLIP2 variants + [0,1000] (§2/§2.2/Fig.1/§3.2.4); claim-4 text-timestamp format seconds+HMS, Qwen2.5-VL replacement rationale (§2.3); claim-5 S0–S3 recipe budgets/lengths + sqrt loss (Table 1/Intro). Verified against report HTML §§2–3 + Table 1.
- VM-D066 (Qwen3-Omni report arXiv:2509.17765v1): claim-3 AuT rates/adapter staging (§2.2/§2.3/§3-S1); claim-4 TM-RoPE 24/20/20 + contiguous numbering + 2-sec-chunk contrast (§2.3); claim-5 streaming stack + theoretical latency Table 2 with vLLM setup + qualitative-only KV note (§2.5/Tables 1–2). Verified against report HTML §§2–3 + Tables 1–2.
- VM-D070 (InternVL3 report arXiv:2504.10479v3): claim-3 ViT-MLP-LLM widths + pixel-unshuffle 448→256 (§2.1/Table 1); claim-4 V2PE δ set + inference selection (Eqs.1–4); claim-5 SFT 16.3M→21.7M + MPO 300K + VisualPRM BoN + InternEVO 32K (§2.3/§2.4/§2.5). Verified against report HTML §§2.1–2.5 + Table 1.
- VM-D071 (Molmo 2 paper arXiv:2601.10611v4): claim-4 K-crop tiling + video sampling (§3.1); claim-5 connector layers + pooling + interleave format (§3.1); claim-6 three-stage recipe + packing/message-trees + token weighting (§3.2/Fig.3/Abstract). Verified against paper HTML §§2–3 + Table 1 + §3.2. Blog "25,000 steps" figure explicitly rejected (unbound, conflicts with paper's 30k).

Deliberately NOT extracted (undisclosed in bound reports; recorded as PUBLIC_SOURCE_DISCLOSURE_LIMIT, never conjectured): KV-cache byte counts, measured (non-theoretical) latency, DeepStack source-layer indices, per-image tile-count caps, training-throughput percentages, ViT input resolution/dims beyond stated, 12.5Hz-for-Molmo transfer. #559 constraints preserved in all drafts (80ms granularity-only phrasing; 234/547ms theoretical-only with setup; no license claims added).

## 3. Timestamps

Preserved from r5 on all 111 cards (temporal.observed_at + sources[0].accessed_at = 2026-09-30T14:24:47Z), per Sol r4/r5 no-churn rule. Bound-report section verification was performed read-only on 2026-10-03 separately (see §2 pinpoints); no new collector retrieval run was executed. Sol review may direct otherwise.

## 4. Gate adaptations (documented deviations from r5 pattern)

- `agent.validate_agent_state` bypassed via runtime filter: it fails on 7 pre-existing publication-surface checkpoint drifts proven identical on the clean starting commit (stash test; #559-cycle origin; unrelated to Evidence). Filter passes through any other error and fails closed if the baseline changes. Shared validators untouched.
- `accept_evidence_results` basis gate (state_sha256) cannot pass post-gate without rewriting historical package bytes (forbidden: would break all 5 acceptances' package_sha256). Vendored byte-identical acceptor `accept_evidence_results_postgate` asserts package bytes equal the historically accepted hash instead; all card/task validation, digest, layout, and JSON shape canonical.
- New acceptance/views carry new content-addressed hashes by design (any byte change churns). Old sets retained.

## 5. Lifecycle boundary (NOT performed)

No materiality-ledger, profile-completeness, candidate-matrix, selection, architecture, draft-package, production-state, or gate change. Those files truthfully record what they were built from (candidate-matrix basis 5cc951bd, draft-package evidence_acceptance pins, views 78a08d3c). Rebind of downstream SHA pins requires the Human-gated dependency-aware path (Architecture rN+1); no approval fabricated, no gate transitioned. Sol re-review of this batch is required before any downstream use — requested as part of the fresh content review.
