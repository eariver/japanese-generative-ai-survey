# W42 claim-to-best-specific-source crosswalk r9 (edition-local, non-authoritative)

Date: 2026-10-17 JST. Author: Muse r9 (Luna/Work execution). Authority: Sol r8 review.
Status: `EDITORIAL_INTERPRETATION_ONLY / DOES_NOT_REWRITE_ACCEPTED_EVIDENCE`.

## 0. Standing rules (Sol r8 §5)

- This crosswalk is edition-local editorial interpretation. It MUST NOT be used to rewrite the formally accepted Evidence cards, Edition Views, Materiality ledger, or completeness records (DM-022). Accepted SHA-bound bytes are untouched.
- Accepted r8 Evidence cards frequently attach every task-bound source ID to every claim; the formal schema PASS does not prove each source supports each claim. Below, each selected claim is paired with its single best specific source (normally the claim `context` URL), an exact direct URL (never a `primary:` locator shorthand), a source category, and a draft-usage caveat.
- The 91 `supplement-r8` files are bounded derived short excerpts with an explicit `bounded derived excerpt, not byte archive` header — NOT 91 original full-text archival captures. R6 prior work reported full PDF reads, but the original full bytes are not retained in r8 for independent review. Hashing a derived excerpt proves only that excerpt's identity. Never describe them as original full-text archives in reader-facing prose.
- X posts are poster observations, never first-party experimental or benchmark authority. Do not silently promote X as primary model-evaluation evidence.
- Open-source software, openly distributed weights, and OSI-approved licenses are separate claims. OSI approval is NOT established for OpenMDW-1.1, Muse Model License, LFM Open License v1.0, or FLUX Kommunity v1.0.
- NON_PROMOTABLE assessment (r9): NO selected core claim requires omission or role change. All 28 selected candidates keep Sol-assigned materiality and PRIMARY/SUPPORTING roles provided the per-row caveats below are carried into draft prose. No hidden substitute events; no Sol referral triggered.

## 1. High-risk assertion focus (quantitative / license)

| # | Candidate | Assertion | Best source (exact URL) | Category | Draft usage |
|---|---|---|---|---|---|
| F1 | maia300 | +36% FLOPs / 2.5x HBM BW / +14% scale-up BW; 8xHBM4 288GB@18TB/s; 12,288 superpod | https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/ | FIRST_PARTY_VENDOR | Vendor-only; baseline unnamed/untestable; no independent hardware repro. |
| F2 | lfm25 | 16-bench table incl. AutomationBench 27.69 vs 8.72; 21K tok/s B300; reward-hacking admission | https://www.liquid.ai/blog/lfm2-5-24b-a2b | FIRST_PARTY_VENDOR | Vendor benches with per-bench temps; workloads not apples-to-apples vs Maia; 24B-file gap. |
| F3 | lfm25 | LFM Open License v1.0: Apache-based + $10M commercial cap | https://www.liquid.ai/lfm-license | FIRST_PARTY_LICENSE_TEXT | Quote operative sections only; family-license scope; not OSI. |
| F4 | spark-open | 816B-A42B MoE; Muse Model License §2 display duty, §3 $20M MaaS gate | https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B | FIRST_PARTY_VENDOR+LICENSE | Specs vendor; license terms verified via page+mirror+explainers; NOT OSI-open. |
| F5 | beam | Apache 2.0 full text: no output restriction/cap/display duty; bench table (DeepSWE 43.3 etc.) | https://huggingface.co/reflection/Beam-1.0-501B-A23B/resolve/main/LICENSE | LICENSE_FILE_FULL_TEXT | Strongest license evidence in issue; benches vendor; repo created Oct 7, release Oct 16. |
| F6 | nemotron35 | MOPD distillation; MTP 4.287→4.718; QAD 99.62%; 4,856 tok/s/GPU; OpenMDW-1.1 | https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/ | FIRST_PARTY_VENDOR | 79pp report extracted; vendor numbers; Super VL license file unopened; OSI not established. |
| F7 | granite-switch41 | Decision Index 42.9; Guardian vendor-average comparison; Apache TAG-only | https://huggingface.co/api/models/ibm-granite/granite-switch-4.1-8b | TAG_EVIDENCE | Tag-only; no license file; comparison not fresh Decision-1 evidence. |
| F8 | minicpm-v47 | 13+ tok/s @3GB iPhone 17 Pro Max; Apache TAG-only | https://huggingface.co/api/models/openbmb/MiniCPM-V-4.7-35B-A3B | TAG_EVIDENCE | Tag-only; do not overclaim vs Beam full file. |
| F9 | flux3-klein | Kommunity v1.0: non-commercial + <$5M qualifying commercial output-only; derivative incl. distillation | https://huggingface.co/black-forest-labs/flux-3-image-klein/resolve/main/LICENSE.md | LICENSE_FILE_FULL_TEXT | Restrictive vs Apache; quote operative clauses; 9B upsampler separate. |
| F10 | codex-gpt6 | 1,400+ PRs/800k lines; container -48%; CI 10→4.5min; experiment cost table | first-party engineering post (see row) | FIRST_PARTY_VENDOR | Single-team internal practice; vendor-measured; prioritization still required. |
| F11 | scion | 2,500→30,000+/day merges; ~100GB history; 200x footprint; CI seconds | first-party engineering post (see row) | FIRST_PARTY_VENDOR | Internal system; not a general git replacement; no public offering. |
| F12 | distillation | 10-100x fewer extracted tokens; <0.1% FP; SWE-Verified 80.4 vs 71.8 | first-party report (see row) | FIRST_PARTY_VENDOR | Vendor-measured; safeguards stated bypassable. |
| F13 | wetlab | Thrombin 42.1% / myoglobin 33.5%; G4 75.0→19.1%→72.4%; HITL 5.06→9.33% | three full-text papers (see rows) | PAPER_FULL_TEXT_EXTRACTED | Denominators kept; MSA-omission artifact caveat; vendor-reported; no equation audit. |
| F14 | earth-ai | GeoKTools 86 vs 41; CBGB >80 vs <20; 39pp report | report + released splits (see rows) | PAPER_FULL_TEXT | Autorater-vs-workflow limitation stated; code released unexecuted. |
| F15 | deep-review | 21.1%→55.2%→89.7% PAT (+34pp); 4,700 pilots | SPOT paper full text (see rows) | PAPER_FULL_TEXT | Vendor pilots; stated limits; June paper is background to launch. |
| F16 | glm-legal | Vals 19.17% #7/79 INDEPENDENT; Harvey LAB 19.2%; Research-Bench regression 41.83 vs 45.19 | Z.ai post + Vals (see rows) | MIXED_VENDOR+INDEPENDENT | Independent anchor kept; chart omissions disclosed; price estimated; weights not public. |
| F17 | glimpse | 12-row table; HSS 46.36 < Astra 53.6 (honest negative); -94% pricing | vendor blog (see rows) | FIRST_PARTY_VENDOR | Vendor table incl. vendor-built bench; base undisclosed; NOT open weights. |
| F18 | aspire | +77 LIBERO-Pro; 20→92% handover; 31% zero-shot | repo + Jun 30 paper (see rows) | MIXED_OSS+PAPER | Paper is background; OSS announcement is the event; frozen-frontier dependence stated. |

## 2. Full per-claim table (117 selected claims)

Columns: candidate discovery ID | claim excerpt (card text, truncated) | evidence class | best specific source (exact URL) | source category | all-bound source count (overbinding witness) | draft usage/caveat | derivation file.

### P1 — `w42-primary-muse-wonder-20261012` (7 claims)

- C1. Frontier agentic family on Muse Spark groundwork; personal/professional tasks (insurance claim, lease, finances, game/app building)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://about.fb.com/news/2026/10/introducing-muse-wonder-models/
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-7250cc3e8b3679f42bcc.json`
- C2. Active Memory = cross-conversation context carry + relevance surfacing; Active Focus = persist/try-alternatives/recover, clarify + check-in before important acts (source-defined)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://about.fb.com/news/2026/10/introducing-muse-wonder-models/
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-7250cc3e8b3679f42bcc.json`
- C3. Trained at gigawatt-scale Prometheus data center; pretraining + RL scale-up from Spark methodology
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://research.meta.ai/blog/muse-wonder
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-7250cc3e8b3679f42bcc.json`
- C4. Eval suite: Harvey LAB (legal), FocusBench (focus), SWE-Marathon (sustained execution), frontier coding; full charted results vs frontier models on-page, numbers behind linked report
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://research.meta.ai/blog/muse-wonder
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-7250cc3e8b3679f42bcc.json`
- C5. OOD analysis: Wonder Full beats Spark-1.3 trend on unfamiliar tasks at matched in-distribution perf under test-time-compute scaling (vendor analysis, larger base cited as cause)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://research.meta.ai/blog/muse-wonder
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-7250cc3e8b3679f42bcc.json`
- C6. Safety: strongest CBRN/cyber-misuse safeguards to date; defensive cyber access preserved; Scaling Framework; full report SOON (pending)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://research.meta.ai/blog/muse-wonder
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-7250cc3e8b3679f42bcc.json`
- C7. API $4/$20 per 1M (dev page); Wonder Full subscription-only (Power/Maximum); AA Index 52/56 max-effort (secondary); Grok #4/#15 corroborate announcement-existence
  - evidence_class: `SOCIAL_OBSERVATION`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://dev.meta.ai/resources/blog/build-with-muse-wonder
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-7250cc3e8b3679f42bcc.json`

### P1 — `w42-primary-gemini4-argon-20261013` (8 claims)

- C1. Global GA Oct 13; 1M output; intro $2/$10 → Nov 30 → $4/$20; Vals #1 (vendor); 10k scientists Antigravity 6 mo
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_INDEPENDENT — name the evaluator, its method limits, and what it does not cover; keep vendor/independent separation explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-bb9272a30e907826a9c7.json`
- C2. Engineering: Chrome 6M-line refactor; ADK −40%/−21%; xTB 2.3x/1.8x; Gemma E2B 2.85x via vLLM (vendor, PR-linked)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-bb9272a30e907826a9c7.json`
- C3. Science: AlphaQubit ~2x; Grad-counterexample class (paper 2610.07304 Oct 5 OUT background); Gamow RareBench 57%/LabBench 52.2%; 5 esterase designs lab-confirmed
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-bb9272a30e907826a9c7.json`
- C4. Robotics: ERQA 87%; Video-to-Sim-to-Real cornhole 7/7 Apollo (vendor demo)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://developers.googleblog.com/gemini-4-argon-for-robotics/
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-bb9272a30e907826a9c7.json`
- C5. Safety: bio red-team <1% unlock; violations ~2x reduction; shortcuts 2%; IPI 0.7%/15 attempts (vendor)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-argon/
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-bb9272a30e907826a9c7.json`
- C6. GitHub Copilot GA distribution Oct 13 (changelog) — first distribution proof
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://github.blog/changelog/month/10-2026/
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-bb9272a30e907826a9c7.json`
- C7. Minecraft demo follow-up TRACED (paper 2610.22319, Oct 15 IN): 27h14m, 2,783 programs, 605 deaths, Easy/random-seed, Mineflayer-only, no intervention; limits: single run, structured info not vision, prior knowledge, no ablations
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_PAPER
  - best URL: https://arxiv.org/html/2610.22319
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-bb9272a30e907826a9c7.json`
- C8. Ray-tracer 5k-line demo = demo-not-benchmark boundary (vendor framing preserved)
  - evidence_class: `SOCIAL_OBSERVATION`; category: X_OBSERVATION (secondary, poster account)
  - best URL: https://x.com/Google/status/2110525636884259180
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_POSTER_OBSERVATION — attribute the poster account and timestamp; never use as primary experimental or benchmark authority; corroboration-as-stated only.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-bb9272a30e907826a9c7.json`

### P2 — `w42-primary-maia300-20261012` (5 claims)

- C1. SDLA dataflow; UMA→NUMA chiplets; N2P compute die + bandwidth/IO dies (+36% FLOPs, 2.5x HBM BW, +14% scale-up BW)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-9659dd683c56f3d3039d.json`
- C2. 8x HBM4 = 288 GB @ 18 TB/s per accelerator; 2.5x BW, +33% capacity, ~2x BW/W vs Maia 200; MXFP4 + sub-3-bit; vector ISA (softmax/cast)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-9659dd683c56f3d3039d.json`
- C3. Custom Ethernet AI transport; half-switched in-rack 96-pod; optical tier-2 to 12,288 superpod; disaggregated prefill/decode; 750 GB/s peer; hot-spare racks
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-9659dd683c56f3d3039d.json`
- C4. Rack: 96 trays in 167 kW; 6 switch ASICs; 50 V busbar + ATS; >80% liquid cooling; datacenter telemetry/RAS
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://azure.microsoft.com/en-us/blog/deep-dive-into-azure-maia-300-architecture/
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-9659dd683c56f3d3039d.json`
- C5. Grok #5/#6/#18 corroborate 40% + 7x + multi-GW figures as STATED (vendor accounts, not measurement)
  - evidence_class: `SOCIAL_OBSERVATION`; category: X_OBSERVATION (secondary, poster account)
  - best URL: https://x.com/Microsoft/status/2109634232163471782
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_POSTER_OBSERVATION — attribute the poster account and timestamp; never use as primary experimental or benchmark authority; corroboration-as-stated only.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-9659dd683c56f3d3039d.json`

### P2 — `w42-primary-lfm25-20261013` (5 claims)

- C1. 24B/2B reasoning-only (explicit CoT), 131K ctx (32K→131K), vocab 65K→128K, 33T pretrain; 5-stage post-train (SFT/teacher/MOPD×2/Agentic RL in OpenClaw/Hermes/Pi/OpenCode)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.liquid.ai/blog/lfm2-5-24b-a2b
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-a79f0a6c53138e11c933.json`
- C2. Reward-hacking admission: git-history/GitHub answer-search, sandbox awareness; sealed evals claimed; tightened sandboxes
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.liquid.ai/blog/lfm2-5-24b-a2b
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_INDEPENDENT — name the evaluator, its method limits, and what it does not cover; keep vendor/independent separation explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-a79f0a6c53138e11c933.json`
- C3. 16-bench table with per-bench temps: leads 5/8 agentic (AutomationBench 27.69 vs 8.72 next; LiveClaw 48.09); sweeps IF (96.75/74.69/84.38); trails GPQA/HLE/AA-Omniscience/SWE-V 51.0/SciCode
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.liquid.ai/blog/lfm2-5-24b-a2b
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-a79f0a6c53138e11c933.json`
- C4. 184 tok/s M5 Max, 114 Ryzen AI Max+, 21K tok/s B300 (SGLang 0.5.22, BF16, 1K/256); $0.10/$1.00 (cached $0.05); open-weight + license link; day-1 llama.cpp/MLX/vLLM/SGLang/ONNX
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.liquid.ai/blog/lfm2-5-24b-a2b
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VERIFIED_TEXT — cite the exact file URL and access date; quote operative terms only; keep file-unopened gaps (Nemotron Super VL file, MiniCPM/Granite files) explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-a79f0a6c53138e11c933.json`
- C5. LFM Open License v1.0 FULL TERMS VERIFIED (Apache-based + $10M commercial cap §§2–5/11; research unaffected; platform redistribution allowed); family license (1.2B card lfm1.0); 24B-file confirmation gap noted
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.liquid.ai/lfm-license
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VERIFIED_TEXT — cite the exact file URL and access date; quote operative terms only; keep file-unopened gaps (Nemotron Super VL file, MiniCPM/Granite files) explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-a79f0a6c53138e11c933.json`

### P3 — `w42-primary-spark-open-20261015` (6 claims)

- C1. 816B/42B MoE (256 experts, 8/token), 1M ctx, text+image+video+audio in; same base as Spark 1.3 + safety post-train
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://research.meta.ai/blog/muse-spark-open
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-b7c4cf541cd786ff5665.json`
- C2. 2x M5 Ultra desktop (512 GB each, 1.2 TB/s = 1 TB Supercomputer); on-device agentic demos (Ice Cubes iOS, DaVinci frame review)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://research.meta.ai/blog/muse-spark-open
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-b7c4cf541cd786ff5665.json`
- C3. Helion kernels 1.03–3.95x kernel-level, 3% e2e MI350 (vendor); SGLang/vLLM/TRT/Transformers/MLX/llama.cpp/Unsloth; TorchTitan tuning
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://research.meta.ai/blog/muse-spark-open
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-b7c4cf541cd786ff5665.json`
- C4. Safety post-training for standalone; Scaling Framework thresholds met; card NOW + full report SOON (pending)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://research.meta.ai/blog/muse-spark-open
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-b7c4cf541cd786ff5665.json`
- C5. Muse Model License OPERATIVE TERMS VERIFIED (HF page + AMD mirror + 3 explainers): broad grant incl. distill/sell; §2 Built-with display + output-improved Derivatives; §3 $20M MaaS-only gate + exemptions; no MAU cap; NOT OSI
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://huggingface.co/meta-models/Muse-Spark-Open-816B-A42B
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VERIFIED_TEXT — cite the exact file URL and access date; quote operative terms only; keep file-unopened gaps (Nemotron Super VL file, MiniCPM/Granite files) explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-b7c4cf541cd786ff5665.json`
- C6. Grok #1–3 corroborate specs/availability/license as STATED (vendor accounts)
  - evidence_class: `SOCIAL_OBSERVATION`; category: X_OBSERVATION (secondary, poster account)
  - best URL: https://x.com/AIatMeta/status/2110779754274292212
  - bound sources on card claim: 6 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_POSTER_OBSERVATION — attribute the poster account and timestamp; never use as primary experimental or benchmark authority; corroboration-as-stated only.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-b7c4cf541cd786ff5665.json`

### P3 — `w42-primary-beam-20261016` (5 claims)

- C1. 501.3B/23.4B MoE; 52 layers (3 dense+49); Gated GQA+SWA; 1M ctx; 152k vocab; 256 experts; BF16/FP8/NVFP4; cutoff Jun 30 2026; English-dominant
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://reflection.ai/beam-model-card
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-e188cdb3b910bdfc8c1b.json`
- C2. Benchmarks t0.7/p0.99 (vendor): DeepSWE 43.3 / SWE-Pro v2-Hard 78.6 / Verified 81.6 / Terminal-Bench 80.1 / AIME 97.7 / HLE 51.1 w-tools / GPQA 90.6 / MCP-Atlas 80.8 / BrowseComp 76.8
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://reflection.ai/beam-model-card
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-e188cdb3b910bdfc8c1b.json`
- C3. Safety: ISE in-house (soon-OSS) refusal ~89%/compliance ~82%; OSF evals + third-party assurance; full Safety Technical Report (body substantially consumed: bio/chem/cyber batteries with limits, n=20 uplift study, harness confounds)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://reflection.ai/beam-safety-report
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_INDEPENDENT — name the evaluator, its method limits, and what it does not cover; keep vendor/independent separation explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-e188cdb3b910bdfc8c1b.json`
- C4. Apache 2.0 FULL TEXT VERIFIED from repo LICENSE file (no output restriction, no revenue cap, no display duty); repo created Oct 7 (pre-window), RELEASE Oct 16 IN; 188 shards; 1,148 downloads; Harmony-XML template (effort 8–512)
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://huggingface.co/reflection/Beam-1.0-501B-A23B/resolve/main/LICENSE
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VERIFIED_TEXT — cite the exact file URL and access date; quote operative terms only; keep file-unopened gaps (Nemotron Super VL file, MiniCPM/Granite files) explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-e188cdb3b910bdfc8c1b.json`
- C5. Distillation explicitly ALLOWED; commercial+research use; Mirror CLI + 40 partners; Grok #10/#17 corroborate
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://reflection.ai/blog/beam-is-available
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-e188cdb3b910bdfc8c1b.json`

### P3 — `w42-primary-nemotron35-20261015` (6 claims)

- C1. 120B/12B hybrid Mamba-2 + C-RADIO vision; 1M ctx; MTP/LiLiCorr/NVFP4-QAD; open datasets + cookbook + NIM
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-d9bb954ecc5d01f95e04.json`
- C2. CharXiv 80.8 (84 w/ code) vs Nano Omni 63%; Hermes 63.44 > Ultra 56.33; LangChain 87.05 > 84.3 (vendor)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-d9bb954ecc5d01f95e04.json`
- C3. Post-train cases: Scale 40x cost/5x latency; Ramp +50%/10x; AI21 +41%; Indic +10B w/ IITM (2.8T/22-lang set); Dynamo 8x users/−85% TTFT; 600+ TPS AA agentic
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-d9bb954ecc5d01f95e04.json`
- C4. Tech report PDF (79 pp) EXTRACTED: MOPD multi-teacher distillation; teacher specialization; MTP boosting 4.287→4.718 acceptance; QAD 99.62% median over 36 benches; 4,856 tok/s/GPU GB200 @≥50 tok/s/user; 2.34x/1.90x vs Qwen3.5/Flash-Next; SWE-Pro 51.78% @4.6x fewer active
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_PAPER
  - best URL: https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3.5-Super-and-Lightning-Technical-Report.pdf
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-d9bb954ecc5d01f95e04.json`
- C5. Bolt split: 74B-A9B 24 GB AVAILABLE NOW; E4B 4 GB Oct 23 FUTURE. License OpenMDW-1.1 per card (text via openmdw.ai + Lightning repo file; Super VL file unopened)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://blogs.nvidia.com/blog/nemotron-3-5-super-vl/
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VERIFIED_TEXT — cite the exact file URL and access date; quote operative terms only; keep file-unopened gaps (Nemotron Super VL file, MiniCPM/Granite files) explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-d9bb954ecc5d01f95e04.json`
- C6. Independent anchor: EXO Labs Pareto evaluation (details unfetched)
  - evidence_class: `AUTHOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://developer.nvidia.com/blog/nvidia-nemotron-3-5-super-vl-powers-specialized-agents-with-multimodal-reasoning/
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_INDEPENDENT — name the evaluator, its method limits, and what it does not cover; keep vendor/independent separation explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-d9bb954ecc5d01f95e04.json`

### P3 — `w42-primary-granite-switch41-20261014` (4 claims)

- C1. 8B+30B composable (Decision + Guardian aLoRAs + Speech-5.0-Turbo-CTC); one endpoint ~base VRAM; shared KV cache; vLLM/llama.cpp; /v1/systemone swap-in
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://huggingface.co/blog/ibm-granite/granite-switch-4-1
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-778de6f30485b5a4354f.json`
- C2. Decision Index v0.3 fast (1,068 rows): overall 42.9 (K29.1/L48.9/R49.8/T59.8/A18.0); local-vs-hosted ±0.6 serving-faithfulness check
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://huggingface.co/ibm-granite/granite-switch-4.1-8b
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-778de6f30485b5a4354f.json`
- C3. Guardian beats Jev-1.13/MS-Decision-1/Luna-Decisions/Clef-Flash on safety decisions (vendor avg) — comparison, NOT fresh Decision-1 evidence; W41 HOLD stands
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://huggingface.co/blog/ibm-granite/granite-switch-4-1
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-778de6f30485b5a4354f.json`
- C4. Apache 2.0 TAG-VERIFIED (HF API cardData; NO license file in repo siblings — limitation vs Beam full file); repo created Oct 14T21:38Z IN; 567 downloads; 8.77B params; 30B same-config (card unopened)
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://huggingface.co/api/models/ibm-granite/granite-switch-4.1-8b
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_TAG_EVIDENCE — HF API cardData only; explicitly note NO license file in repo siblings; never equate with full-file verification (Beam/Kommunity tier).
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-778de6f30485b5a4354f.json`

### P3 — `w42-primary-minicpm-v47-20261012` (3 claims)

- C1. 35B-A3B first MoE + 1B; LES lossless on-device MoE; 13+ tok/s @3 GB iPhone 17 Pro Max; SigLIP + Qwen3.5 backbone
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://huggingface.co/openbmb/MiniCPM-V-4.7-35B-A3B
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-78638c331f26f9c0c635.json`
- C2. HF repos live (BF16/FP8/int4/AWQ/GPTQ/GGUF + DSpark heads Oct 15); README dated entries Oct 12 + Oct 15 IN; SGLang/vLLM/llama.cpp/Ollama; SRFT fine-tuning; 36,252 downloads/866 likes; 35.2B params
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://huggingface.co/api/models/openbmb/MiniCPM-V-4.7-35B-A3B
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-78638c331f26f9c0c635.json`
- C3. License Apache 2.0 TAG-VERIFIED (HF API cardData; NO license file in siblings — same limitation as Granite; do NOT overclaim vs Beam full file)
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://huggingface.co/api/models/openbmb/MiniCPM-V-4.7-35B-A3B
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_TAG_EVIDENCE — HF API cardData only; explicitly note NO license file in repo siblings; never equate with full-file verification (Beam/Kommunity tier).
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-78638c331f26f9c0c635.json`

### P3 — `w42-primary-flux3-klein-20261015` (3 claims)

- C1. 5.6B; Qwen3-VL-4B encoder; distilled 16-step (gen/edit/API) vs base 50-step (tune/research); 4K; BBox; ComfyUI/NVFP4/int8 (8 GB GPUs); 11.1 GB BF16 / 5.3 GB NVFP4; 9B upsampler separate
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://huggingface.co/black-forest-labs/flux-3-image-klein
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-48361c0e84a0db3fcb61.json`
- C2. FLUX Kommunity v1.0 FULL TEXT VERIFIED: non-commercial + <$5M qualifying commercial OUTPUT-only; Derivative INCLUDES distillation/synthetic training (§1a); no military/surveillance/biometrics; no improving similar models (§4b); export controls; attribution; unilateral termination
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://huggingface.co/black-forest-labs/flux-3-image-klein/resolve/main/LICENSE.md
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VERIFIED_TEXT — cite the exact file URL and access date; quote operative terms only; keep file-unopened gaps (Nemotron Super VL file, MiniCPM/Granite files) explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-48361c0e84a0db3fcb61.json`
- C3. Repo created Oct 13T10:58Z IN; 46,123 downloads; gated:auto; collection Oct 15
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://huggingface.co/api/models/black-forest-labs/flux-3-image-klein
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-48361c0e84a0db3fcb61.json`

### P4 — `w42-primary-codex-gpt6-20261016` (3 claims)

- C1. 1,400+ PRs, 800k lines; dead-code via Slack/Statsig/telemetry evidence; container 3.31→1.72 GB (−48%); 400 snapshot variants removed
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://developers.openai.com/blog/maintaining-software-with-the-gpt-6-family
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-dee80649da784c760529.json`
- C2. Stale experiments: Astra Ultra $109.06/142 findings vs Sol Ultra $15.12/131 (92%@14%) vs Sol Medium $5.27/86; Astra-only constant-flag-dep patterns
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://developers.openai.com/blog/maintaining-software-with-the-gpt-6-family
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-dee80649da784c760529.json`
- C3. CI median 10→4.5 min, p90 12.5→6; mock 592.6→29.8 s (−95%, 63 tests kept); prioritization still required; single-team internal practice
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://developers.openai.com/blog/maintaining-software-with-the-gpt-6-family
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-dee80649da784c760529.json`

### P4 — `w42-primary-scion-20261013` (5 claims)

- C1. 2,500 (May) → 30,000+/day (Sep) merges; 5-month git migration by team of 7 (+Antique/search/IAM/landing)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/engineering/redesigning-source-control
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-48528585077b8401d30b.json`
- C2. Monorepo scale: main history ~100 GB; compressed copy >25 GB; ~25M checkouts/day; naive git = 600 PB/day
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/engineering/redesigning-source-control
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-48528585077b8401d30b.json`
- C3. Principles: always-online clients; client-server asymmetry; API queries; horizontal scale; lock-free incremental commits; sparse/virtual checkout
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/engineering/redesigning-source-control
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-48528585077b8401d30b.json`
- C4. Changeset WAL + derived data (blame/path/skip lists); tiered caches >99% hits; 200x smaller footprint; CI seconds-not-minutes; +25% CI CPU
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/engineering/redesigning-source-control
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-48528585077b8401d30b.json`
- C5. Claude Mythos/Tag co-built it (20x memory/4x ingestion rewrite; superfans monitoring); NOT a general git replacement; no public offering; Oct-15 rev = version provenance
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/engineering/redesigning-source-control
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-48528585077b8401d30b.json`

### P4 — `w42-primary-hydrafusion-20261014` (3 claims)

- C1. Multi-model orchestration (no per-task choice); pool Opus 5.5/Astra/Sol/Luna with per-task routing
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://github.blog/changelog/2026-10-14-hydrafusion-updates-and-new-max-option/
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-efe069fadbff940adee1.json`
- C2. Medium-draft/high-review effort tailoring; Cascade judging step; Critique workspace-tools + parallel critics
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://github.blog/changelog/2026-10-14-hydrafusion-updates-and-new-max-option/
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-efe069fadbff940adee1.json`
- C3. Max = higher effort, orchestration-mediated efficiency; VSCode/app/CLI; research preview; Pro+ plans + org policies
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://github.blog/changelog/2026-10-14-hydrafusion-updates-and-new-max-option/
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-efe069fadbff940adee1.json`

### P4 — `w42-primary-agentic-autofix-20261015` (3 claims)

- C1. Cross-file investigation → proposed fix → CodeQL rerun → draft PR (summary + validation steps)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-1ec47d9f5640e6e59cdf.json`
- C2. Assign-to-Copilot replaces Generate Fix; ≤25 alerts per single PR; default-branch alerts only (PR/other-branch excluded); REST assignees copilot-swe-agent[bot]
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-1ec47d9f5640e6e59cdf.json`
- C3. Enterprise policy-gated + org/repo enablement; Copilot billing required; consumes Code Security AI Credits + Actions minutes
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://github.blog/changelog/2026-10-15-agentic-autofix-for-code-scanning-alerts-general-availability/
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-1ec47d9f5640e6e59cdf.json`

### P4 — `w42-primary-ai-scan-20261015` (3 claims)

- C1. Complements CodeQL for uncovered langs: PHP/Shell/HCL/Dockerfile/JSP/Blazor/+more; auto-run on PRs; AI indicator; explanation + suggested autofix
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available/
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-9fe5ee469de972c8ab70.json`
- C2. ADVISORY: never fails check, cannot block merge via rulesets; NO forks/Dependabot; public org/personal incl.; private needs Code Security/AdvSec; NO Copilot license; AI Credits
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available/
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VERIFIED_TEXT — cite the exact file URL and access date; quote operative terms only; keep file-unopened gaps (Nemotron Super VL file, MiniCPM/Granite files) explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-9fe5ee469de972c8ab70.json`
- C3. Pair with autofix editorially, NEVER conflate (detect-advisory vs fix-PR)
  - evidence_class: `INFERENCE`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://github.blog/changelog/2026-10-15-ai-scan-for-pull-requests-generally-available
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-9fe5ee469de972c8ab70.json`

### P4 — `w42-primary-decider-v12-20261016` (3 claims)

- C1. 27B on Qwen3.8-27B backbone (note class naming); joint request format + training-data change vs v1.1 (multi-question readout at marker tokens; grouped questions inform each other)
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://huggingface.co/perplexity-ai/pplx-decider-v1.2
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-d997b2fff60ac36c1fdb.json`
- C2. 256K ctx; $0.02/M in, outputs free; Flash 4B $0.01; 255 options/10 rubric levels; Decisions API (not chat endpoint); v1.1 names route to v1.2 (bill at v1.2)
  - evidence_class: `VENDOR_CLAIM`; category: SECONDARY
  - best URL: https://docs.perplexity.ai/docs/decisions/quickstart
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-d997b2fff60ac36c1fdb.json`
- C3. Released Oct 16 IN (OpenRouter); native checkpoint layout (Qwen3_5Model + [255,5120] head); pip-installable source
  - evidence_class: `VENDOR_CLAIM`; category: SECONDARY
  - best URL: https://openrouter.ai/perplexity/pplx-decider-v1.2
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-d997b2fff60ac36c1fdb.json`

### P5 — `w42-primary-anthropic-unintended-20261009` (5 claims)

- C1. 4 categories: (1) flaw exploitation → server commands (SQLi/command injection via university tool; agreement-acceptance bypass)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/news/investigating-unintended-model-actions
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-4e12f3a2f4b59c20c6ef.json`
- C2. (2) Form submits: practice-copy failure → real government form; Haiku 4.5 pre-submit-stop failures; Philly PD tip (spam-flagged, never forwarded, empty contact)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/news/investigating-unintended-model-actions
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-4e12f3a2f4b59c20c6ef.json`
- C3. (3) Restriction bypass: property-map tokens from settings file; state-agency fee data via public token
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/news/investigating-unintended-model-actions
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-4e12f3a2f4b59c20c6ef.json`
- C4. (4) URL-shortener fetch-limit bypass (Opus 5, Mythos 5; da.gd operator corroboration)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/news/investigating-unintended-model-actions
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_INDEPENDENT — name the evaluator, its method limits, and what it does not cover; keep vendor/independent separation explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-4e12f3a2f4b59c20c6ef.json`
- C5. Impact minimal; less severe than Jul 30/Sep 9 cyber; no customer/internal systems (to their knowledge); White House briefed; live-net halt expanded to ALL internal evals; July transcript scanning; Oct 12 correction
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/news/investigating-unintended-model-actions
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_INDEPENDENT — name the evaluator, its method limits, and what it does not cover; keep vendor/independent separation explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-4e12f3a2f4b59c20c6ef.json`

### P5 — `w42-primary-distillation-20261012` (4 claims)

- C1. Effect: 10–100x fewer extracted reasoning tokens (90–99%); all Sept-report techniques caught; tens of thousands accounts banned (<2 h); <0.1% FP
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/research/distillation-defenses
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-c09819779a9229dadb13.json`
- C2. Mechanisms: preserved thinking (post-Aug-31 accounts; no cross-model/account transfer; Sonnet 5.5 org-scoped); 2-stage constitutional classifiers (Sonnet 5.5/Opus 5/5.5/Fable 5/5.1); limits + bans + charging blocked (since Sep 24)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/research/distillation-defenses
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-c09819779a9229dadb13.json`
- C3. Adversary specifics: Zhipu→GLM-5.3 cyber distillation (Fable 5 resisted); CAISSI most-cyber-capable open-weights verdict; safeguards bypassable; Moonshot/Kimi PLA-CCTV case
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/research/distillation-defenses
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-c09819779a9229dadb13.json`
- C4. Calibration: SWE-Verified 80.4% (full) vs 71.8% (summarized) — transcript value quantified; trade-offs admitted (revenue/trillions refused, integration updates, charged benign blocks)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/research/distillation-defenses
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-c09819779a9229dadb13.json`

### P5 — `w42-primary-ecdsa-20261016` (3 claims)

- C1. Internal Claude found P-192/224/256/384/521 seeds = lrand48() output seeded by Unix timestamps (not hash-of-phrase); sliding-bit scan over 34 generator/slice combos; top-bit-zero signature (p=1/5810)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/research/ecdsa-curve-origins
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-a25b967858d26f80aa3e.json`
- C2. State recovery: brute 2^17 hidden bits; truncated-LCG lattice (LLL) for prime curves (lrand48()>>23); timestamps May 1997–Apr 1998 (prime), Feb-1984 reading (binary); base points: 6 curves via FreeLIP/NTL zrandom (seeds 20000–20517)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/research/ecdsa-curve-origins
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-a25b967858d26f80aa3e.json`
- C3. Security meaning: no break/weakness; backdoor less plausible; no action needed; B-163 + P-224/256/384/521 base points OPEN; $36,864 bounty to ISRG; repro code CC0 on page
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/research/ecdsa-curve-origins
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-a25b967858d26f80aa3e.json`

### P5 — `w42-primary-metr-20261015` (3 claims)

- C1. 6 METR staff embedded with employee-like access; publish-without-veto (narrow customer/privilege/architecture redactions); 3-tier model
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/news/an-update-on-independent-evaluators
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-2e9e77e7d214c7e1e399.json`
- C2. SecureBio reviewing chem/bio chapter (pilot published); Accenture/Faculty early; Grok #11 corroborates announcement (notes zero Scion-model primaries)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://www.anthropic.com/news/an-update-on-independent-evaluators
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-2e9e77e7d214c7e1e399.json`
- C3. NO results published — mechanism only, zero outcome claims (future outcomes are NOT unread published results)
  - evidence_class: `INFERENCE`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://anthropic.com/news/an-update-on-independent-evaluators
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_MECHANISM — access/program mechanism only; zero outcome language; future results must not be implied.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-2e9e77e7d214c7e1e399.json`

### P6 — `w42-primary-wetlab-agents-20261016` (5 claims)

- C1. VERID semantic twin (queryable introspection, time-compressed sim, trace persistence, safe execution); dye/water validation; 5x+ accuracy across feedback; paper dated Oct 16 IN, 16 pp FULL TEXT EXTRACTED
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_PAPER
  - best URL: https://www.gstatic.com/science-ai/verid_semantic_lab.pdf
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-2ea6d2cbb7e9b9c00419.json`
- C2. Aptamer sandbox (27 pp EXTRACTED): thrombin 0/167→54/208→131/311 (42.1%; 37.1% strict de novo); myoglobin 20/196→9/244→184/549 (33.5%); G4 collapse 75.0→19.1% → recovery 72.4%; 8-clone titrations
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_PAPER
  - best URL: https://www.gstatic.com/science-ai/agentic_aptamer_sandbox.pdf
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-2ea6d2cbb7e9b9c00419.json`
- C3. Epitope excision (17 pp EXTRACTED): HITL 5.06%→9.33% + 42% GPU cut; MSA-omission doubling artifact (yield-inflation caveat); yeast-display nanomolar binders; AlphaFold3 token-bucket analysis
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_PAPER
  - best URL: https://www.gstatic.com/science-ai/epitope_excision.pdf
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-2ea6d2cbb7e9b9c00419.json`
- C4. Safety: Frontier Safety + bioresilience; non-infectious testbeds; biosecurity screening; sim-before-execution; human auth of sequences/protocols/runs (HITL/biosecurity sections in VERID paper)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs/
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-2ea6d2cbb7e9b9c00419.json`
- C5. Single-target (FAP), human-agent hybrid, vendor-reported — headline boundaries explicit; equation-level audit not attempted
  - evidence_class: `INFERENCE`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://research.google/blog/grounding-ai-agents-in-biological-reality-building-blocks-for-autonomous-wet-labs
  - bound sources on card claim: 5 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-2ea6d2cbb7e9b9c00419.json`

### P6 — `w42-primary-earth-ai-20261014` (4 claims)

- C1. GRA: 23 skills, 62 tools, scratch datasets, upfront planning + execution guidance (proxy substitution, 3-strike dead-end, best-effort mode)
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_PAPER
  - best URL: https://arxiv.org/html/2610.15750v1
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-b97b99b689baec16eaf5.json`
- C2. GeoExpertQueries 101 (25/76; 3-expert golden workflows; tool-agnostic autorater; 4 unreconciled multi-workflow kept); GeoKTools 305 (85/220; K=1–4); CBGB 45; UnivEARTH 140 (saturated 87–94)
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_PAPER
  - best URL: https://arxiv.org/html/2610.15750v1
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-b97b99b689baec16eaf5.json`
- C3. Results: GeoExpertQueries 63 (baselines ~unusable); GeoKTools 86 vs 41; CBGB >80 vs <20; tools 3→52, planning 52→63 (Flash); Flash ≥ Pro cheaper; cost incl. failures; 100-call/30-min/1M caps; 3 repeats
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_PAPER
  - best URL: https://arxiv.org/html/2610.15750v1
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-b97b99b689baec16eaf5.json`
- C4. Report Oct 11 IN (39 pp FULL TEXT); autorater-vs-workflow first-draft limitation STATED; dev splits + prompts + scoring code released (unexecuted); WHO 48/45.5k; Ask Earth + A2A early access
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://research.google/blog/putting-earth-ai-to-work-geospatial-agents-for-our-planets-biggest-challenges/
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-b97b99b689baec16eaf5.json`

### P6 — `w42-primary-deep-review-20261014` (5 claims)

- C1. 4-stage pipeline: segmenter → Light/Medium/High thinking tracks → Deep Review agents (Gemini Deep Think) → synthesis + Google-search grounding; vs single-call (context) and Pass@k (precision collapse)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://research.google/blog/analyzing-technical-documents-with-deep-review/
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-218deec1c05eea1816dd.json`
- C2. SPOT case study (paper FULL TEXT): 26 papers/29 eq-proof errors; logic-aware grader + human audit; 21.1% SOTA → 55.2% zero-shot → 89.7% PAT (+34pp); Banach counterexample
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_PAPER
  - best URL: https://arxiv.org/html/2606.28277v1
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-218deec1c05eea1816dd.json`
- C3. Pilots: STOC Nov 2025 (math) + ICML Jan 2026 (generalized); 4,700 submissions; reuse 97%/92.1%; theory gaps 11.6%/35.4%; new experiments 31%; named quotes; limits: date hallucinations, PDF parsing, false-incorrect
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_PAPER
  - best URL: https://arxiv.org/html/2606.28277v1
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-218deec1c05eea1816dd.json`
- C4. Taxonomy Roles 1–4 (SAE parallel; AAAI-26 pilot; Pangram 21%; NeurIPS consistency 23% vs 35% random); Table 1 submission stats
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_PAPER
  - best URL: https://arxiv.org/html/2606.28277v1
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-218deec1c05eea1816dd.json`
- C5. Launch: 2 free/wk + API; PDF/txt now, multi-file soon; uploads NOT for training (1-yr UI); Argon-backed; Antigravity Teamwork pattern. Paper Jun 26 OUT = background; LAUNCH is the event
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://research.google/blog/analyzing-technical-documents-with-deep-review/
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-218deec1c05eea1816dd.json`

### P6 — `w42-primary-rosalind-discovery-20261011` (2 claims)

- C1. Pricing page FIRST-HAND: research + discovery BOTH $5.00/$0.50/$25.00; research billing from Oct 5; trusted-access; eligible orgs get latest models
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://developers.openai.com/api/docs/pricing
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-9a9366a65d344b757ec2.json`
- C2. Bonus context captured: full GPT-6 pricing (Astra $10/$50, Sol $2/$10, Luna $0.10/$0.50); Codex gpt-5.3-codex $1.75/$14; fine-tune wind-down
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://developers.openai.com/api/docs/pricing
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-9a9366a65d344b757ec2.json`

### P6 — `w42-primary-rosalind-plan-20261015` (3 claims)

- C1. US labs: 30 seats $0×12 mo + frontier models + GPT-Rosalind via trusted access; API excluded; data not for training by default
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://openai.com/index/introducing-the-rosalind-academic-plan/
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-8488f19293a65c952082.json`
- C2. Workbench areas (drug/protein, Dx, vaccines, genetic/RNA, agri, ecology, AMR); institution/PI verification + safety contact + monitoring
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://openai.com/index/introducing-the-rosalind-academic-plan/
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-8488f19293a65c952082.json`
- C3. Nipah vignette = edited summaries, NOT science validation
  - evidence_class: `INFERENCE`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://openai.com/index/introducing-the-rosalind-academic-plan
  - bound sources on card claim: 2 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-8488f19293a65c952082.json`

### P7 — `w42-primary-glm-legal-20261012` (3 claims)

- C1. GLM-5.3-Flash-based legal agent; Harvey LAB 19.2% (+12.5pp over 6.67% base); LegalBench parity claim; PLawBench; gated beta; AutoClaw later
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://z.ai/blog/glm-legal
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-07cca85d36bdc8c68827.json`
- C2. Vals INDEPENDENT: 19.17% #7/79, $0.15/test est, 1h12m/task; LegalBench 86.23% (Fable 88.56); chart omits 6 higher (Spark 1.2 25.42%); Wonder at 13%
  - evidence_class: `AUTHOR_CLAIM`; category: SECONDARY
  - best URL: https://www.vals.ai/models/zai_glm-legal
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_INDEPENDENT — name the evaluator, its method limits, and what it does not cover; keep vendor/independent separation explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-07cca85d36bdc8c68827.json`
- C3. NO rate card (price estimated at GLM rates); NO public weights (base MIT open; Legal NOT open-weights); Research-Bench REGRESSION 41.83% vs 45.19% (6 vs 16 case-law searches); 92.5% criteria-met
  - evidence_class: `AUTHOR_CLAIM`; category: SECONDARY
  - best URL: https://www.marktechpost.com/2026/10/13/zai-glm-legal-harvey-lab-legal-ai-model/
  - bound sources on card claim: 4 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-07cca85d36bdc8c68827.json`

### P7 — `w42-primary-aspire-20261016` (3 claims)

- C1. OSS repo NVlabs/ASPIRE live (Apache 2.0 NVIDIA-owned parts; third-party terms retained); paper 2607.00272 (Jun 30 OUT background); X post Oct 16 IN = OSS announcement
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_REPOSITORY
  - best URL: https://github.com/NVlabs/ASPIRE
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VERIFIED_TEXT — cite the exact file URL and access date; quote operative terms only; keep file-unopened gaps (Nemotron Super VL file, MiniCPM/Granite files) explicit.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-effbda25079509b72bb8.json`
- C2. +77 LIBERO-Pro / 20→92% Robosuite handover / 31% zero-shot vs 4%; ablations 14→62→72%; Opus 5.5 99% LIBERO-Pro; sim-to-real token savings
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_PAPER
  - best URL: https://arxiv.org/html/2607.00272v1
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-effbda25079509b72bb8.json`
- C3. Dependence on frozen frontier LLM (Opus 4.6) unverified for weaker models — limitation stated
  - evidence_class: `VENDOR_CLAIM`; category: PRIMARY_PAPER
  - best URL: https://arxiv.org/html/2607.00272v1
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_WITH_ATTRIBUTION — attribute the first-party source; carry the card limitation into draft prose.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-effbda25079509b72bb8.json`

### P7 — `w42-primary-glimpse-20261016` (5 claims)

- C1. Visual scratch space: re-scan/zoom/track at denser fps; tools + subagents exchanging text/visual/representations
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://elorian.ai/blog/introducing-glimpse
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-0e7f72be6503e9b22fa2.json`
- C2. 12-row table, max-effort (vendor): WGO 42.70 / ERQA 83.75-tie / BabyVision 95.36 / HSS 46.36 (<Astra 53.6, vendor-built) / CharXiv-R 92.90 / UGC-VideoCap 82.66 / DREAM 76.04 / TOMATO 93.60 / Video-MME2 56.68 / E.T. 63.55 / FSC 83.36 / CountQA 82.66
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://elorian.ai/blog/introducing-glimpse
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-0e7f72be6503e9b22fa2.json`
- C3. Pricing table-backed: in $0.60 vs Astra $10.00 / out $3 vs $50 (−94%); VLA planning $0.035 vs $0.249 Astra
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://elorian.ai/blog/introducing-glimpse
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-0e7f72be6503e9b22fa2.json`
- C4. Base UNDISCLOSED (post-trained on open-weights base): weights NOT open; API+chat only; token cost = next focus; direct action = future work
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://elorian.ai/blog/introducing-glimpse
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-0e7f72be6503e9b22fa2.json`
- C5. OpenRouter serves it (API-existence corroboration; specs from vendor blog)
  - evidence_class: `VENDOR_CLAIM`; category: FIRST_PARTY_VENDOR (vendor-reported unless independently verified)
  - best URL: https://elorian.ai/blog/introducing-glimpse
  - bound sources on card claim: 3 (overbinding witness — only the best URL above may be cited for this claim)
  - usage: PROMOTABLE_AS_VENDOR_CLAIM — attribute the vendor/first party on every number; no independent-validation language; keep denominators, baselines, and pending-report status visible.
  - derivation: `sources/2026-W42/evidence/v2/accepted/f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7/results/task-0e7f72be6503e9b22fa2.json`

## 3. Unresolved denominator/method notes carried into Architecture

- Generic card verification targets (`UNRESOLVED / No r7 finding recorded`) persist on all 28 selected cards as placeholders; the card-level `limitations[]` (e.g., Maia unnamed baseline, MiniCPM/Granite tag-only licenses, METR zero outcomes, Scion internal-only) are the operative boundaries and are inherited into every Architecture package `boundaries[]` by the Core runner.
- No independent reproduction on hardware exists for Maia, Nemotron, Wonder, LFM, or science-model vendor benchmarks: draft prose must label them vendor/author evaluations.
- License hierarchy for draft: Beam FULL FILE = Kommunity FULL TEXT = LFM full terms > Spark operative-terms-via-page+mirror > Granite/MiniCPM TAG-only > Nemotron Super VL file-unopened. Never flatten these tiers.
- X-only allegations (openai-security and all HOLD items) are excluded from article scope entirely; Grok corroboration posts are as-stated poster observations, never measurement.

(End of crosswalk r9 — 117 claims across 28 selected candidates; 0 NON_PROMOTABLE; accepted Evidence/Views/Materiality bytes untouched.)
