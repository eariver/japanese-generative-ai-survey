# W42 r15 Architecture coverage & depth gap (Unit A — BEFORE drafting; r15.1 rebuild)

Date: 2026-10-18 JST. Base r14: 112 PARAGRAPH / 20,479 paragraph-only chars / 23,601 body-PTN chars. v15.1: 136 paras / 24,162 / 27,415 (+24 / +3,683 / +3,814). Target 26.5pp article body / 28 total / max 30. Full 28-item matrix: `source-claim-matrix-r15.json` (16 PRIMARY + 12 SUPPORTING; v15.0 covered only 7 lead items — repaired).

## Method
Per PRIMARY/SUPPORTING item: approved subsection → published blocks → unanswered technical question → source/denominator status → concrete addition (v15.1 block IDs). SUPPORTING roles are bounded comparisons, not standalone stories. No re-selection, no Architecture change, no unapproved scope.

## P1 — Frontier agents (r14 15 paras/2,996; v15.1 20/3,568)
- Covered: Wonder Active Memory/Focus definitions + Prometheus scale + eval-suite charting + OOD vendor analysis + pricing windows + Argon anecdotes + Copilot distribution (FIXED t1-21) + Minecraft conditions + cost ledger (NEW t1-23) + OOD structure (NEW t1-22) + Focus checkpoint + ray-tracer boundary + safety framing.
- Unanswered: retention-scope internals, deletion/correction means, independent benches, full safety report (SOON), AA methodology, Vals methodology, model card PDF (all SOURCE_INACCESSIBLE — recorded, not invented).
- SUPPORTING: none in P1. Net +5 paras. Flow reordered (t1-22 after t1-07, t1-23 after t1-16); t1-17/t1-21 duplication FIXED.

## P2 — Maia / LFM2.5 (r14 16/2,761; v15.1 20/3,321)
- Covered: SDLA/NUMA/HBM4/MXFP4, rack/power/cooling, unnamed-baseline caveat, LFM 16-bench per-temp table (T0.6/T0.001/T0/T1.0, outlier 27.69 vs 8.72), reward-hacking admission + sealed-eval design, simulator confound (NEW t2-22), throughput denominators (NEW t2-23), license operative $10M cap (FIXED t2-21), serving-cost reading, 24B-file gap.
- Unanswered: Maia baseline values, technical paper annex, Independent hardware repro, HF file listing, Pipette logs (SOURCE_INACCESSIBLE).
- SUPPORTING: LFM bounded efficiency comparator (never apples-to-apples with Maia). Net +4 paras; t2-18/t2-21 duplication FIXED.

## P3 — Open weights (r14 20/4,237; v15.1 22/4,570)
- Covered: MTP acceptance-length with Table-8 conditions (verified ±, greedy-vs-sampled honesty), LiLiCorr/QAD/context-reuse/Dynamo, MOPD shares + dashed agentic-teacher, Beam uplift method n=20 (NEW t3-24), Spark arch/VRAM + license crosswalk (NEW t3-25), license tiers (Beam FILE vs Granite/MiniCPM TAG-only vs Spark MaaS-gate vs Nemotron OpenMDW gap vs FLUX Kommunity), Beam full text, Granite DI 42.9, MiniCPM LES, FLUX 16/50-step.
- Unanswered: 79pp PDF bytes (S3a/S3b pages substitute, recorded), Nemotron Super-VL LICENSE file, independent EXO Pareto, bench methodology behind Spark report link.
- SUPPORTING: Granite/MiniCPM/FLUX tag-only/restriction comparators. Net +2 paras (already densest chapter).

## P4 — Codex/Scion/HydraFusion (r14 17/3,121; v15.1 21/3,793)
- Covered: Codex cost table + CI triad (FIXED t4-21 distinct from t4-04) + Slack/Statsig/telemetry triad + survivorship caveat, Scion WAL/cache/scale + 200x + not-git-replacement (NEW t4-23), HydraFusion routing + Max + undisclosed-marked failover, AutoFix/AI-Scan gates (fix-vs-advisory never conflated) + billing/policy, Decider DI/calibration/versioning (NEW t4-24).
- Unanswered: independent replication (all vendor-measured), HydraFusion eval methodology/token quantification, autofix fix-rates, AI-Scan precision/recall, Decider spec diff.
- SUPPORTING: autofix/AI-Scan/Decider delivery/versioning cases. Net +4 paras; closing synthesis kept last.

## P5 — Safety (r14 15/2,388; v15.1 18/2,827)
- Covered: 4 incident categories + Philly tip + da.gd partial + White House/correction/July-scan chain (NEW t5-20: Oct 9→Oct 12, fetch-limit≠injection, halt ALL evals, replayed blocked), distillation efficacy + adversary (Zhipu/CAISSI/Moonshot) + FP/durability rewrite (FIXED t5-19: <0.1%, charged benign, durability unknown), ECDSA method + residual OPEN (NEW t5-21: B-163 + 4 base, timestamps, $36,864 ISRG, CC0), METR access-vs-zero-results (t5-21: 6 staff, 3-tier, SecureBio pilot).
- Unanswered: org identities, severity/dishonesty independent audit, CAISSI report body, independent cryptographer verification, METR downstream (all absent by design or unfetched).
- SUPPORTING: ECDSA/METR methodological/access cases. Net +3 paras; t5-06/08 vs t5-19 overlap FIXED.

## P6 — Science (r14 17/2,873; v15.1 19/3,410)
- Covered: VERID/aptamer/epitope denominators + MSA artifact + FAP hybrid + safety auth + M02 separation held, full 4×2+SD (Pro 50.8±1.7→47.6±2.7 −3.2pp VERIFIED, Flash +10.5pp, GeoKTools Pro −2.9pp, CBGB flat, saturation), 3-repeat/failure-cost methodology, tools decomposition (NEW t6-23: searches 7.0→3.2, EE 38→54%, Flash <1/3 Pro cost, standalone 37/40 strongest non-GRA, Table-5 domains, 4 unreconciled, golden blind consensus), repo discrepancy (paper 220[30/110/50/30]/74tmpl vs repo 210[30/100/50/30]/72tmpl + 44-vs-45 gap NEW) + withheld-never-open, Deep Review SPOT/pilots/taxonomy/limits, Rosalind access/pricing (NEW t6-25: $5/$0.5/$25, Oct 5, 30 seats $0 12mo, API excluded, data not training, Nipah edited summaries; refs FIXED to Rosalind claims).
- Unanswered: equation-level audit, Fig./Methods beyond headlines, independent rerun, withheld tests, commit SHA (UNKNOWN recorded), research-vs-discovery functional diff.
- SUPPORTING: Rosalind pricing/program strictly as conditions. Net +2 paras (flagship F-01/F-02 held).

## P7 — Domain/embodied (r14 12/2,103; v15.1 16/2,673 — thinnest base, largest relative gain +27%)
- Covered: Vals independent anchor + priced/timed design reading (FIXED t7-16 distinct from t7-03) + regression 41.83 vs 45.19 + 92.5% criteria (NEW t7-18) + chart-omission actor (6 higher incl Spark 25.42%, Wonder 13%) + price/weights caveats, ASPIRE dating + OSS event + frozen-frontier dependence + sim-to-real failure mode, Glimpse 12-row + HSS negative on vendor bench + −94% pricing + NOT-open-weights (NEW t7-19).
- Unanswered: Vals full methodology, Z.ai rate card, real-hardware results, Glimpse base identity/ctx confirmation, independent harness repro (SOURCE_INACCESSIBLE).
- SUPPORTING: Glimpse visual-scratch comparator. Net +4 paras.

## Pagination outlook (honest, measured)
- r14 proof: 17 pages at 23,601 body chars (~1,388 chars/page incl tables/notes/bib).
- v15.0 proof: 18 pages at 24,697 body chars (retained byte-identical as layout reference ONLY; does NOT reflect v15.1).
- v15.1: 27,415 body chars (+16% vs r14) → projected ~19-20 total pages, ~15-16 dense article pages. Vs 26.5 body-plan (~36,800 chars at this density): short ~9,400 chars (~6-7 body pages). Tables unchanged (7).
- Standing rule: NO padding, NO Architecture downscope by Muse. Remaining gap needs NEW primary reads (METR internals, Vals methodology, Maia baseline/paper, Nemotron PDF bytes, HF file listings, independent reruns) currently SOURCE_INACCESSIBLE, or a Human Architecture page-plan amendment. Contraction path (merge SUPPORTING comparators) is an Architecture change — NOT taken.
- Terminal: `EDITORIAL_DEPTH_OR_PAGINATION_DECISION_REQUIRED` with this file + readiness + validation as quantified basis. No TeX/PDF render in r15.1 (prior 18pp proof retained as reference, explicitly stale-marked).
