# Sol R1 gap-fill ledger — Discovery expansion r2 (append-only; r1 ledger preserved)
# Edition: SP-efficient-llm-2026 | collector_run: efficient-llm-discovery-r2 | observed: 2026-09-21
# r1 ledger: sources/SP-efficient-llm-2026/raw/discovery-negative-space-2026-09-21.md (FROZEN, bound by r1 acceptance)
# r2 graph: discovery/discovery-v2-r2.jsonl (EFF-D101–EFF-D142, GAP_FILL/pass 1) + discovery-accepted-v2-r2.json
# r1 files untouched; r1 acceptance re-validated after r2 build.

## r1 gaps (G01–G10) dispositions
- G01 V4.1 paper: RESOLVED — arXiv 2609.19969 (2026-09-18) + HF-hosted PDF (EFF-D123).
- G02 DSpark mechanism: PARTIAL — report § + card + vLLM class + Dynamo recipe converge on
  semi-autoregressive in-checkpoint drafter; standalone DSpark paper still not located. Evidence must read
  report §3/appendix + config before asserting MTP-head equivalence.
- G03 DSA primary: RESOLVED — V3.2 report 2512.02556 + V3.2-Exp launch/API docs + GH tech report (EFF-D125/126).
- G04 KDA collision: PARTIAL — GLM first-party uses "sparse and linear attention" + IndexShare (published);
  "IndexPool" appears only in secondary gloss (S84); NVIDIA NIM "hybrid KDA" for GLM unresolved.
  Recommendation: use IndexShare in prose; confirm-or-drop IndexPool and NIM-KDA at Evidence.
- G05 mHC collision: OPEN — term recurs (V4-Flash, V4.1 Single-Pass mHC + Mega-mHC kernel, GLM-5.3-Flash);
  mechanism-equivalence unverified. Terminology watch retained for Architecture.
- G06 Jev independent reproduction: see G20 below.
- G07 vendor cost claims: STRUCTURED, not resolved — now dated/conditioned (V3.2-Exp 50%+ price event
  EFF-D126; Qwen 1/9 training EFF-D127; GLM 3.01x/4.44x EFF-D131; V4.1 1/4-HBM/1/8-SSD EFF-D123).
  Cost-per-completed-task still measured nowhere; independent reproduction outstanding across all capstones.
- G08 absentee sweep: Ring Attention ADDED (EFF-D108); Expert Choice ADDED (EFF-D133); BitNet b1.58 ADDED
  (EFF-D135, deployment still open); FP4 TRAINING evidence still not located (FP4 = inference/serving only);
  ThunderMLA/TileLang-kernel line noted but unexpanded (TileLang appears as DSA kernel substrate, EFF-D126).
- G09 alias map: EXTENDED — DSA now first-party defined; IndexShare added (GLM); QSA/CSA2/NSA deltas still
  unverified pairwise. Alias table lives in r1 ledger G09 + r2 raw g16 notes.
- G10 benchmark primaries: PARTIAL — SWE-Pro footnote normalized via Qwen card (EFF-D127: Claude Code harness,
  corrected tasks, re-run baselines); MLPerf/GenAI-Perf/LLMPerf/lm-harness/HELM added (EFF-D118–122);
  DeepSWE standalone methodology + BrowseComp methodology still outstanding.

## r2 gaps (G12–G20) dispositions
- G12 distributed training: ADDED 8 (EFF-D101–108). Fit-vs-arithmetic question answered per-record in raw
  (only S105 checkpointing spends arithmetic to save memory). ZeRO-Infinity folded into S104 entry (no
  separate record; Sol may request split).
- G13 KV management: ADDED 6 (EFF-D109–114). Five-way separation recorded in raw header. SnapKV located
  (assumption discharged). vLLM APC doc body + LMCache code bodies pending Evidence.
- G14 conditional depth: ADDED 3 (EFF-D115–117). MoD/MoE non-merge rule recorded. Real-LLM MoD adoption
  unverified — Sol materiality question.
- G15 harnesses: ADDED 5 (EFF-D118–122). AIPerf-as-distinct-product NOT located:
  `AIPERF_NOT_FOUND_AS_OF_2026-09-21` (GenAI-Perf covers the NVIDIA measurement lane).
- G16 capstones: ADDED 10 (EFF-D123–132). Flash-vs-Flash-Next BOUND (EFF-D127). Remaining: report full-body
  reads (V4.1/V4/GLM-5 PDFs), GLM-5.3-Flash config tensors, QSA kernel artifact, IndexPool confirm-or-drop.
- G17 MoE routing: ADDED 2 (EFF-D133/134). Bounded as instructed; aux-loss-free already covered via V3 (r1 S06).
- G18 low-bit: ADDED 3 (EFF-D135–137). MXFP4 format authority now primary (spec + paper). GGUF/imatrix
  distinction still repo-doc-level (r1 S48/S50, LOCATOR) — Evidence must read spec + quants docs.
- G19 data efficiency: ADDED 3 (EFF-D138–140) as explicit sweep. Recommendation: PURSUE only as context
  (dedup/DoReMi as training-token-reduction complements); Textbooks + tokenizer-axis PARK_WITH_REASON
  (indirect relevance; no capstone cites tokenizer as lever). Sol decides.
- G20 Jev: ADDED 2 first-party docs (EFF-D141/142: Models page + API reference).
  `INDEPENDENT_EVIDENCE_NOT_FOUND_AS_OF_2026-09-21` for peer-reviewed or vendor-independent
  benchmark/reproduction. RLCD technical description NOT FOUND beyond vendor name. Community-grade leads
  only (playground, integrations, playbooks) = deployment-interest signal, not validation.

## Retrieval failures / NOT_FOUND registry (r2)
- `AIPERF_NOT_FOUND_AS_OF_2026-09-21` (distinct NVIDIA AIPerf product).
- Standalone DSpark paper: not located (convergent secondary mechanism evidence only).
- FP4 training evidence: not located (all FP4 records are inference/serving).
- Peer-reviewed/independent Jev benchmark or reproduction: not located.
- Tokenizer-efficiency primary as 2026-capstone lever: none located (park recommended).
- IndexPool primary: not located (confirm-or-drop at Evidence).
- vLLM APC doc body, LMCache code, KDA kernel body, report PDF bodies: located-as-URL, bodies unread
  (SUMMARY/LOCATOR status honestly recorded per record).

## Provenance notes
- r2 IDs EFF-D101–EFF-D142 (no overlap with r1); all GAP_FILL/pass 1; external: parents reference r1 IDs
  where genuine relationships exist (traceability only; EXTERNAL scope, no cross-file validation debt).
- r2 acceptance (discovery-accepted-v2-r2.json, 42 records) validates standalone; composes with r1 root
  (100 records) at future Screening packaging per Core expansion rules. Lifecycle NOT advanced.
