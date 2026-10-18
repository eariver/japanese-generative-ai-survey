# r15 new source readings (edition-local sidecar; NOT accepted Evidence)

Status: `EDITORIAL_SIDECAR / NON_ACCEPTANCE / NO_CORE_CHANGE`
Date: 2026-10-18 JST. Reader: Muse (execution). Carries over r14 S1/S2/S3a/S3b (see `../editorial-revision-r14/new-source-readings-r14.md`, NOT duplicated here). This file records only r15-delta reads. These readings do NOT rewrite accepted Evidence/Views, are not archived full-byte captures, and do not select new candidates.

## S4 — Earth AI benchmark repo README (live read, r15; F-02 evidence)
- URL: https://github.com/google-research/geospatial-reasoning-benchmarks
- Accessed: 2026-10-18 JST via webfetch text (README body obtained live; NOT an archived byte capture; repo files themselves not cloned).
- Observed release facts (verbatim scope): GeoKTools 85 dev queries (K=1:10, K=2:50, K=3:15, K=4:10; 19 templates) + 210 held-out test queries (K=1:30, K=2:100, K=3:50, K=4:30; 72 templates); tests kept private; dev JSON + 19 template specs + autorater prompts + deterministic scorer + tests/ released; GeoExpertQueries 25 dev + 76 test (=101); licenses Apache-2.0 (code) / CC-BY-4.0 (data), Google Maps + third-party data excluded with own terms.
- Version receipt: page showed "Latest commit / History / 1 Commit" at fetch time; NO commit SHA exposed by the text renderer — recorded as UNKNOWN (not fabricated). CITATION.bib + docs/PROVENANCE.md exist but snapshot dates not extracted in this read.
- Usable for: F-02 discrepancy audit (paper-220[30/110/50/30]/74tmpl vs repo-210[30/100/50/30]/72tmpl; dev 85 matches; GeoExpertQueries 101 matches in both).

## S5 — Nemotron Table 8 re-verification (live re-read, r15; TECH-01 gate)
- URL: https://docs.nvidia.com/nemotron/latest/nemotron/super35/rl/index.html (same as r14 S3b).
- Re-read: 2026-10-18 JST via webfetch text, MTP Boosting section. Table 8 values CONFIRMED identical to r14 record: draft length 7, SPEED-Bench qualitative split; SFT 4.589/4.048; SFT+4K 5.080/4.730; Final native 4.287/3.787; Final+MTP-head 4.528/4.436; Final+25K boosting 4.718/4.612; +10.1% greedy / +21.8% sampled; cross-model rows as recorded.
- This read upgrades NOTHING beyond r14 (no new numbers); it satisfies the contract's "independently open and verify" gate for r15 citation.

## S6 — Earth AI paper Table 4/5 SD + CBGB re-verification (text search over retained S2 fetch, r15)
- Source: retained webfetch text of arXiv 2610.15750v1 (S2, re-grepped 2026-10-18; no new fetch needed).
- Confirmed point estimates + SDs in running text: Pro tool-only→full GRA 50.8±1.7 → 47.6±2.7 (−3.2pp); Flash 52.2±5.4 → 62.7±2.5 (+10.5pp); GeoKTools Pro 84.5±1.4 vs 81.6±1.4 (LLM+GRA Tools level/slightly ahead); CBGB described as expert-curated external set, count 45 per accepted Evidence (no conflicting count in fetched text).
- Usable for: F-01 4×2 rewrite with error bars.

## Usage rule
r15 draft prose may cite S4/S5/S6 section content with explicit sidecar qualification where the accepted card lacks the detail; accepted Evidence remains the formal authority for Core validation (evidence_refs). No new candidate selected on this basis.

## S7 — P1/P2 live re-verify (r15.1 rebuild; read-only subagent synthesis 2026-10-18)
- Wonder: `https://about.fb.com/news/2026/10/introducing-muse-wonder-models/` (Oct 12, upd Oct 13) + `https://research.meta.ai/blog/muse-wonder` (Oct 12) + `https://dev.meta.ai/resources/blog/build-with-muse-wonder` (Oct 12; API $4/$20, Cached $0.20, 1M ctx, Wonder Full subscription-only). Announcement gives definitions (Active Memory/Focus) + availability, NO numbers; OOD analysis Wonder Full vs Spark-1.3 (x=ID composite, y=OOD avg, points=reasoning efforts, TTC shift, larger-base attribution vendor analysis, no CIs/seeds/n). evals behind linked model-card report (unfetched); safety report SOON.
- Argon: `https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/` (Oct 13) + `https://github.blog/changelog/month/10-2026/` (Copilot GA Oct 13 first distribution proof) + `https://arxiv.org/html/2610.22319` (Oct 15 CC BY 4.0; 27h14m, 2783 programs/2839, 229 msgs, 605 deaths, 81 days, median 33.5s, 40% duty, Easy/random-seed/1.20.4/no cheats/no intervention, 6 restarts ~20min, $520 intro/$1040 std, 1.35B in 91% cached +16M out 24K calls, session $810/$1620, +35% submissions, -1/3 rollbacks) + robotics blog (ERQA 87%, cornhole 7/7). Minecraft single-run, structured-not-vision, no ablations. Model card PDF + Vals methodology unfetched.
- Maia: `https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/` (Oct 12; SDLA/NUMA/chiplets/MXFP4, 288GB@18TB/s, 167kW 96-tray, up to 7x rack + >2.5x perf/W vs Maia 200 unnamed baseline). Technical paper + Ignite detail unfetched; independent measurement impossible.
- LFM: `https://www.liquid.ai/blog/lfm2-5-24b-a2b` (Oct 13; 16-bench per-temp: AutomationBench 27.69 T0.6 vs 8.72, BFCLv4 65.01 T0.001, ToolSandbox 80.71 T0, LiveClaw 48.09 T1.0; reward-hacking admission) + `https://www.liquid.ai/lfm-license` (v1.0; Apache-based + $10M cap §§2-5/11). HF file listing + Pipette logs + independent rerun unfetched.
- Usable for: P1 t1-21/22/23, P2 t2-21/22/23 (sidecar-qualified; Evidence remains formal authority).

## S8 — P3 live re-verify (r15.1 rebuild; read-only subagent synthesis 2026-10-18)
- Nemotron Table 8 CONFIRMED verbatim (S3b/S5 re-verified): draft length 7, SPEED-Bench qualitative split, 4.589/4.048, 5.080/4.730, 4.287/3.787, 4.528/4.436, 4.718/4.612, +10.1% greedy/+21.8% sampled, cross-model sampled best 4.612, greedy Gemma-4 4.837/Qwen3.5 4.799 higher. No correction needed.
- Beam safety: ISE ~89% refusal/~82% compliance, OSF Limited, n=20 non-wet-lab 1918-influenza (10+10, 5hr, novice, rubric 14, uncertain/not significant/no wet-lab/single-pathogen), harness-confound. Equations unaudited.
- Spark: 62 layers hid8192 128Q/16KV GQA, BF16 ~1.5TB (~2TB VRAM)/NVFP4 ~530GB (~700GB), 2x M5 Ultra 1TB MLX, license §1/§2/§3/no MAU/NOT OSI/Exhibit A, card NOW report SOON. Methodology behind link unfetched.
- Granite DI v0.3 (1068 rows, 42.9, ±0.6), Guardian vendor-avg (NOT Decision-1 evidence), TAG-only. MiniCPM LES + 13 tok/s iPhone, TAG-only. FLUX Kommunity FULL TEXT, no bench table. Independent benches none throughout.
- Usable for: P3 t3-24/25 (sidecar-qualified; Evidence remains formal authority).

## S9 — P4/P5 live re-fetch (r15.1 rebuild; read-only subagent synthesis 2026-10-18)
- Codex: 1400+ PRs/800k lines, container 3.31->1.72GB, 400 variants, cost table $109.06/142 vs $15.12/131 vs $5.27/86, CI median 10->4.5/p90 12.5->6, mock 592.6->29.8s 63 kept, single-team boundary.
- Scion: 2500 May->30000+/day Sep, team of 7, ~100GB/~25M/600PB naive, WAL + eager/lazy + >99%/tier caches, 200x, seconds-not-minutes +25% CPU, NOT general git replacement.
- HydraFusion: pool routing, no published denominators; routing/cost/failover undisclosed (marked absent). Autofix: <=25 alerts/PR, default-branch only, REST bot, Enterprise-gated. AI Scan: advisory-only (FP containment), no forks/Dependabot.
- Decider: DI 62.30->68.09 joint (Vision 73.22->77.43), grouping +11.3/-4.8, calibration 91.3% ECE 0.014, FP8 degrade, Decisions API only, v1.1->v1.2 billing.
- Unintended: 4 categories + Philly tip + da.gd partial + minimal vs Jul30/Sep9 + White House + halt ALL evals + July scan + Oct 12 correction (fetch-limit != anti-injection). Distillation: 90-99%, tens of thousands <2h, <0.1% FP (now charged), Zhipu/CAISSI/Moonshot cases, durability unknown. ECDSA: lrand48 timestamps, 34 combos, $36,864 ISRG CC0, B-163 + 4 base OPEN. METR: 6 staff, 3-tier, SecureBio pilot, zero results.
- Usable for: P4 t4-21/23/24, P5 t5-19/20/21 (sidecar-qualified; Evidence remains formal authority).

## S10 — P6/P7 live re-open (r15.1 rebuild; read-only subagent synthesis 2026-10-18)
- Earth CORRECTIONS: Pro Full GRA is 47.6±2.7 (NOT ±2.5); Table 4 footnote averages 44 questions though text says 45 curated (unresolved 44-vs-45 gap, added to t6-21). Table 5: Crisis 35/Public Health 17/Site Selection 20/Operational 4; standalone 0.0 by construction. Standalone LLM 37.1/40.5 = strongest non-GRA baseline. Searches 7.0->3.2, EE 38%->54%, Flash $0.167->0.199 (+~3c), Pro $0.512->0.688, Flash <1/3 Pro. Golden workflows 3-expert blind + consensus, 4 unreconciled kept. Repo re-confirmed: 85 dev MATCH, test 220 vs 210 (K=2 110 vs 100), templates 18 vs 19 / 74 vs 72; withheld NEVER open; commit SHA UNKNOWN (not fabricated).
- Wet-lab/Deep Review: per-round screening vs 8-clone confirmation held; MSA-omission artifact; FAP hybrid; SPOT +34pp; pilots 4700/reuse 97/92.1%/new 31%; limits stated. Rosalind: $5/$0.5/$25 both, research billing Oct 5, 30 seats $0 12mo, API excluded, data not training, Nipah edited summaries.
- GLM-Legal: Vals 19.17% #7/79 $0.15/1h12m + LegalBench 86.23 vs 88.56 + Research-Bench REGRESSION 41.83 vs 45.19 (6 vs 16 searches) + 92.5% criteria-met + chart omits 6 higher (Spark 25.42%, Wonder 13%) disclosed. ASPIRE: OSS Oct 16 = event, paper Jun 30 = background, sim-to-real gap explicit. Glimpse: 12-row (HSS 46.36 < 53.6 vendor-bench honest negative), in $0.60 vs $10 (-94%), base undisclosed NOT open.
- Usable for: P6 t6-21/23/25, P7 t7-16/18/19 + P6 S4/S6 carryover (sidecar-qualified; Evidence remains formal authority).

## Usage rule (unchanged)
r15.1 draft prose may cite S7-S10 section content with explicit sidecar qualification where the accepted card lacks the detail; accepted Evidence remains the formal authority for Core validation. No new candidate selected on this basis.
