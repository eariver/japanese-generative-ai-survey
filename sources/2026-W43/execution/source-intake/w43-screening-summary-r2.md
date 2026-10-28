# W43 Screening r2 summary — 51/51 decisions, Core acceptance (2026-10-24)

Method: frozen `survey_agent_tool_v2` compat executor (native agent-first path) for `prepare` (4 batches 13/13/13/12) and `accept`; W42 `screening/v2` used strictly as mechanical precedent, never editorial authority. Legacy direct CLI re-confirmed FAIL (exit 2, no writes); native path PASS. No `ADVANCE_STAGE`; State `DISCOVERY_COLLECTED` untouched.

## Distribution: KEEP 17 / MAYBE 11 / INSPECT 4 / DROP 19 (total 51)

### KEEP (17) — materially relevant, proceed to Evidence verification (KEEP is NOT proof)
- Frontier/agent events: Duet 10/21 (Opus 5.5, VM browser, approval gates), Kimi API 10/23 17:15:24Z (weights Nov 4 future), OpenAI securing 10/23 (containment/CVEs/Oct-1 resume), OpenAI bio 10/21 (GPT-Rosalind, 32 min, Tsc1/Tsc2 + DCTN1 leads), OpenAI low-resource 10/19 (MultiLangBench + COBOL byte-parity).
- Open weights: DeepSeek 1017 10/17 (MIT, Harness), Nemotron E4B 10/23 (64K, OpenMDW-1.1 OSI-unproven), MemT 10/19 (GDN-2/MoS, 34B tokens, split licenses), Ming 10/19 (repo IN, month precision; 0.5B + 7.9B-A1.3B, MIT, AA ranks), Flint 10/21 (announce + HF 14:20:58Z, Apache 2.0; speed publisher-claimed).
- Speech/video: Voxtral 3 10/20, Eleven Realtime 10/20 (AA independent scores as reported), FLUX 3 Max 10/19 (10.95s PR vs 12.45s page discrepancy preserved).
- Infra/tooling: DeepInfer 10/20 (Apache 2.0, SM100/Ascend, explicit non-inclusions), 1Password 10/22 (approve/autofill, live vs coming-soon), TanStack 1.0 10/23 (stable core, experimental harness), MOSS trainer 10/18 (LyCORIS, 6GB, KohakuMoss 1.0).

### INSPECT (4) — source identity/content insufficient; more inspection before Evidence
- Anthropic auto-mode (X-only), OpenAI Decisions API (RSS-only), OpenAI-on-GCP (RSS-only distribution), Patch the Planet (RSS-only process).

### MAYBE (11) — plausibly relevant, significance unclear
- Muse 10M earnings (industry context, bias disclosure), oracle v2 revision (method caution), GitHub deprecation/metrics/Teams (metering, availability, product flow), MOSS report-announce + API (distro/availability), AM-Bench v2 (revision pending delta), Vercel/Ollama/Unsloth (distribution proof), Claude Code perf carry (supporting only), Grok X ledger (**audit/provenance binder, PARTIAL sensor — NOT a technical release, never a Selection candidate**).

### DROP (19) — out-of-window, duplicate-noise, or insufficient credible relevance (each with explicit reason)
- Background OUT (7): Qwen-Image 10/9, Step 5 weights 10/15, Gemini safety lead (unproven date), MOSS base 10/16, DeepInfer repo 10/16, OR-License v1 10/16, AM-Bench v1 10/16, ARC page 10/13 — wait, count: qwen, step5, gemini-safety, moss-base, deepinfer-repo, orlicense, ambench-v1, arc = 8 OUT/background.
- W42 carry rechecks (11): 7 HOLD + 4 INSPECT rechecks (b80ab4, 10d76de, 800408da, 1b1aea9b, 2177831d, 517550f1, 017c9bbc quarantines/UNRESOLVED; b2ee0e1d, c3439ff4, 2cd2da5b, 7eb21255 no-new-material). None promoted; W42 dispositions stand; names/allegations not propagated.
- 8 + 11 = 19. No silent drops; every ID decided exactly once.

## Duplicate groups
- None declared (`duplicate_group: null` on all 51). r3 dedup stands: Kimi single row; AM-Bench v1-OUT/v2-IN versions; MOSS 4 events and DeepInfer 2 events carry explicit family roles in metadata, not Screening duplicates.

## Evidence verification targets (selection, not exhaustive)
- Weights/license/date: Kimi weights by Nov 4 + cyber-removal scope; Nemotron HF license + report PDF + OpenMDW OSI status; Flint HF weight SHA + license file + independent tok/s repro; MemT weight/dataset terms + 34B-token training evidence; Ming exact release date + tech report + weight SHA; MOSS report PDF + API terms; DeepInfer repo tag + hardware reqs + license file.
- Benchmarks: vendor vs independent denominators/harnesses (Terminal-Bench 4.0/Science, DeepSWE, SWE-Pro/Marathon, OfficeQA Pro v2, Hallu Bench, BenchCAD, Tau2/RULER, BBA/Full-Duplex/Arena, AA suites, MultiLangBench/COBOL parity, BenchCAD); AM-Bench v2 delta; oracle-revision blast radius.
- Chronology: X post timestamps vs event dates (Kimi 17:15:24Z archived; Muse Spark pinned post = OUT weights adoption); auto-mode/Decisions/Cloud/Patch page bodies; deprecation list; metrics schema scope; Teams plan scope.
- Safety/security: containment CVEs + Sep-20 incident scope + Oct-1 resume conditions; red-team attacker-favorable caveats; 1Password per-integration live status + .com-only scope; bio follow-up experiment status; Duet permission model once accessible.
- Guardrails: no invented benchmarks/repros (0 independent repros, honestly zero); no X-only promotion (Mercury/Mammoth/Sage/Decider/Dojo/AFM remain parked); quarantine holds (model names, allegations, X-only metrics).

## Limitations (explicit, not PASS inflation)
- 19 rendered-body consumptions, 6 byte-archived raw (r2) + 2 (r4); original HTML unarchived for rendered bodies; 0 independent reproductions.
- INSPECT/MAYBE rows (15) need source inspection or significance judgment before Evidence can rely on them.
