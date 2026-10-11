# W40 Muse gap-fill inventory r2 (2026-10-10Z, SC-D01/02/03)

Authority: Sol r1 `execution/reviews/sol-w40-discovery-completeness-r1-20261010.md`; contract `execution/instructions/2026-10-10_muse-w40-discovery-gapfill-r2.md`. Machine inventory: `w40-muse-gapfill-r2.json`. Supersession/capture ledger: `collectors/primary/runs/20261010T030600Z-muse-r2/r1-r2-supersession-ledger.md`.

## SC-D01: six omitted sources independently read (8 pages)

All date-day-only (no clock time evidenced); AstaBrief/AutoSynthData Oct 2 -> TIME_UNRESOLVED HOLD.

- Holo4 (Sep 28): newsroom + HF blog + models-license page. 27B dense research-noncommercial vs 35B-A3B MoE Apache-2.0; 256K ctx; API + HF BF16/FP8/NVFP4/GGUF; OSWorld 85.2%/$0.08 vs 80.8%/$0.05, OSWorld2 61.7% vs 30.9% publisher-reported; trajectories open; Holotron4 Nano sub-model. 3 excerpts + 1 note.
- Olmo-core 3 (Oct 1): Ai2 blog. Open MoE training stack (DDP/expert/pipeline/dist-opt, grouped-GEMM, MXFP8); 2.7x (52k vs 19.4k); 1.2T/58.36B-active/512GPU; report+code+demo. NOT foundation weights. 1 excerpt + 1 note.
- Open TTS Leaderboard (Sep 30): HF blog. WER/CER (Qwen3-ASR) + RTFx/TTFA (H200) + SIM (WavLM); Seed-TTS + CV3-Eval; Spaces + Listen; scripts repo. Platform, NOT new model; no human-preference proof. 1 excerpt + 1 note.
- ProvenanceGuard (Sep 29): HF team blog (paper arXiv 2606.18037 Aug 27 pre-window). Source-aware MCP verification (routing+NLI+attribution+allow/block+RARR); 281 traces/361 claims, 138/139 caught, F1 0.802; NVFlow/poster vendor-stated. Blog != independent result. 1 excerpt + 1 note.
- AstaBrief 8B (Oct 2, HOLD): Ai2 + HF blogs. Qwen3-8B, SFT47K/DPO6K, 51.1s vs 178.5s, Apache-2.0 card header (SPDX pending), 2025-era baselines. NO time -> HOLD. 1 excerpt + 1 note.
- AutoSynthData (Oct 2, HOLD): HF blog. Failure-driven curriculum (target/multiply, sample/batch gates); Hybrid +7.2pp/35%, ITSM 18.77%->27.18% publisher-reported; dataset released; Gym paper Mar 2026 background. NO time -> HOLD. 1 excerpt + 1 note.

Open-world beyond six: HF blog index enumeration (day-only corroboration), AstaBrief/AutoSynthData third-party day-level reports (no time), transformers library entries (support != premiere), low-materiality community items. Revised lanes: B THIN->MODERATE, C/I/K stronger, F THIN->MODERATE; E/G/H unchanged; full matrix in r2 sweep log.

## SC-D02: 21 noon + 4 misuses repaired, 3 exact kept

Regenerated `discovery/discovery-v2.jsonl`: 36 records (29 kept/repaired + 7 added), 33 published_at NULL with day + basis metadata, 3 exact (ContextLM arXiv 14:50:08Z, Clef JSON-LD 15:34:02Z, LIFT arXiv 11:31:02Z). Flux X-time, Grok approx, carryover/sweep batch-times demoted. Full 25-row audit table in supersession ledger.

## SC-D03: capture reclassification

- R1 24 files: ALL CLAIM_LEVEL_DERIVED_NOTE, 0 byte-identical original bodies (8 locator-grade). Preserved as history, NOT rewritten.
- R2 16 files (excl. json): 8 COPYRIGHT_BOUNDED_EXCERPT + 6 claim notes + 1 sweep log + 1 ledger. Byte-identical HTML captures 0 (webfetch rendering honestly stated). Excerpts bounded with URL/time/method/anchors/limits; notes separate.
- Grok Raw (20,477B) + DailyX 64 + W39 HOLDs + DGX HOLD preserved unchanged.

## Counts

- Raw files r2: 16 non-json (33,731B incl. ledger) + collector-run.json + raw-source-index.json.
- Discovery: 36 records, schema 36/36 PASS; proposal 36 records graph `e1ce0ec8…`, validated; X manifest COMPLETE/PARTIAL validate PASS.
- Added IDs: holo4, olmocore3, opentts, provenanceguard, astabrief-HOLD, autosynthdata-HOLD, sweep-r2. Removed/merged/split: none.
