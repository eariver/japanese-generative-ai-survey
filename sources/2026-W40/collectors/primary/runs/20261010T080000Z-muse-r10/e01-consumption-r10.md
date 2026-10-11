# E01 focused consumption log — CLM / Guard-v2 tails / FLUX weights (bounded, no reintake)

All retrieved 2026-10-10Z. `artifact_class: CLAIM_LEVEL_DERIVED_NOTE__E01_CONSUMPTION_LOG`.
Prior accepted Evidence Cards NOT patched (findings below are reviewer input; delta proposal only if Sol requires —
none meets the contradict/material bar; see verdicts).

## 1. CLM appendices + figures + code (E01)

- ar5iv full HTML curl-read to local (417,994B; 20 h2/h3 headings §§1–6 + App.A–G). Consumed (bounded, this run):
  App.D ContextBench (10,835 chars: seeded op-sequence design, READY_FOR_NEXT_OP gate, 30,768 usable budget);
  App.E configs (11,603: Codex-75%/Self-Compact-37%-every-2-turns/RLM-released/ACM-released/MEM1-reimpl baselines,
  2,048-token editing reminder, NO-trigger base harness); App.F supplementary (4,295: Qwen3.5-9B 39.9% vs 37.7%
  summary-harness, 1.4 vs 2.6 edits/task, 30.2K vs 17.6K peak context); App.G length-awareness (4,275: bucketed
  6.2K/9.8K/10.4K estimates, Sonnet-underestimates/GPT-5.4 note); App.B SCR radix-tree design + App.C FLOPs
  accounting (headings + openings verified, bodies partially read).
- Code repo README read (`facebookresearch/context-language-models`): Harbor CLI (`clm-harbor run -a clm-minimal`),
  `clm/clm_harness|clm_icl|clm_rl` + `suffix_cache_reuse` layout, CC BY-NC 4.0 license, ContextBench coming-soon,
  citation `arXiv:2609.37725`. Code internals NOT opened; no execution.
- Delta vs accepted Card: NONE contradictory (Scope/dates/metrics unchanged); ADDS appendix/method depth for P6a.
  No delta proposal needed (consumption log suffices).

## 2. ProvenanceGuard v2 remainder (E01)

- ar5iv v2 HTML curl-read to local (393,358B; 36 headings §§I–IX + App.A–C). Consumed (bounded, this run):
  V.4 (3,630: MiniCheck gap NOT significant, p≈0.13/0.26; coverage-not-accuracy as differentiator);
  V.5 (2,244: 108 allow / 173 blocked / 144 fallback table); V.6 (1,772: 50/50 probes, CI [0.93,1.00] degenerate-note);
  V.7 (1,272: Gemma-4-E4B two-judge + priority + 361 human-expert Table 21 — NOTE: this partially revises the r7
  withdrawal note, which said Gemma names appear in NO v2 passage; the name IS in v2 V.7, but the r5 claim it was
  attached to (priority-adjudication path detail) remains version-unconfirmed beyond V.7's own sentence; NO gpt-5.4
  passage found in v2 — that withdrawal STANDS);
  VI Discussion (4,814) / VII Conclusion (1,544) / VIII Limitations (4,155: single-stack generality bound, frozen-trace
  reproducibility, 361-only human review) / IX Reproducibility (2,816: MiniLM-L6-v2 + DeBERTa-v3-mnli-fever-anli +
  Gemma-4-E4B adjudication passes); App.A trace JSON schema (972) / App.B RF I/O example incl. route_score 0.224
  (1,462) / App.C conflation worked example (3,271).
- Delta vs accepted Card: NONE contradictory (metrics/scope/boundaries unchanged); ADDS adjudication-transparency
  nuance (Gemma-4-E4B IS named in V.7 — recorded here, NOT back-patched into the accepted Card per no-patch rule;
  Sol decides if a delta proposal is wanted). No delta proposal filed (non-material nuance).

## 3. FLUX 3 Image model/release/license (E01)

- r4 delegated reads stand (docs pricing + banner + Jul-23 split). New bounded check this run (search): NO open-weights
  release located for the FLUX 3 **Image SKU** specifically — BFL open-weights surface covers FLUX.1/FLUX.2 families
  (Apache-2.0 schnell vs non-commercial dev, SHA-pinned) and FLUX 3 Action (7B world-action model); Image SKU remains
  API-only with per-resolution pricing. Weights/license for the Oct 1 SKU stay UNPINNED (consistent with r4 HOLD note).
- Delta vs accepted Card: NONE (SKU/pricing/split claims unchanged). Limited check, no reintake.

## 4. Cloudflare MCP Auth spec (E01)

- Repo README fully read (bounded excerpts archived): split auth/resource servers, Service Binding validation,
  RFC 9728 metadata + 401 challenge, hash-only token storage, holder-only props encryption, handler-owns-enforcement,
  full standards list (MCP 2026-07-28 + OAuth 2.1 draft + 9 RFCs + CIMD). Per-doc pages (authorization-server
  reference, consent, discovery, storage-schema) NOT opened; no security testing.
- Delta vs accepted Card: NONE contradictory (spec surface confirmed + deepened); threat-resistance boundary STANDS.

## 5. Olmo-core 3 (E01 first priority) — see dedicated excerpt file

- Report PDF text extracted (570,369 chars; metadata: 11 authors UW/Ai2, Oct 1 14:36:19 JST creation, Code: Olmo-core,
  Date October 2026). Bounded quotes archived: FSDP→DDP+EP/PP/dist-optimizer switch; NVL8-B300 12.9B→1.2T/512GPU,
  858 TFLOP/s/GPU, DeepEP-v2 2.38T capacity test; MXFP8 +21% (65% kernel-time target); Token Gerrymandering +
  overlap-slowdown findings; full ToC §§2–20 verified. Blog-only 2.7× micro-benchmark NOT in report text (stays
  blog-level). §14 matrix cells, §§16–20 ablations, appendices, code internals NOT consumed.
- Delta vs accepted Card: NONE contradictory (infra-not-weights boundary + reporter levels intact); report-body gap
  now CLOSED at method/condition level; remaining cells/ablations/code are Selection-depth (not acceptance) gaps.

## Verdict

- No accepted Card claim contradicted; no material candidacy change; NO separate Evidence delta proposal filed
  (per §4 rule: delta only on contradiction/material alteration — none found; the Gemma-V.7 nuance is logged above
  for Sol's information and does not alter Selection).
