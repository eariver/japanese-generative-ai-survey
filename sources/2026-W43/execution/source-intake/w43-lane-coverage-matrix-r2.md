# W43 lane coverage matrix r2 (2026-10-24, appends r1)

r1 (`w43-lane-coverage-matrix-r1.md`) preserved. Deltas only below.

| Lane | r1 | r2 delta | r2 status |
|---|---|---|---|
| (a) frontier | Duet/OpenAI-deploy/Muse-10M claim notes | + Duet full body, + OpenAI securing/bio/lowresource trio consumed | COVERED (substantive) |
| (b) open repos/licenses | Kimi/DeepSeek/Nemotron claim notes | + Kimi X raw + blog consumed (clock fixed), + DeepSeek docs, + Nemotron page (64K corrected), + MOSS/MemT/Ming repos+licenses pinned | COVERED (substantive) |
| (c) arch/efficiency | DeepInfer claim note | + DeepInfer README (kernels/DSpark/SWA/async/modes/HW/missing-explicit), + MemT GDN-2/MoS/34B, + StepFUN bg | COVERED (substantive) |
| (d) pretrain/posttrain/data | thin | + MemT two-stage/34B, + Kimi RL stack, + MOSS training GPUs (heterogeneous) | PARTIAL→COVERED-LEAD (datasets still thin) |
| (e) eval/benchmarks | AM/OR edge + AA via vendors | + arXiv API times (v1 OUT/v2 IN), + AA consumed as reported (Voxtral/Eleven/FLUX/Kimi/Ming), + MultiLangBench/COBOL/MemT/Nemotron tables; 0 independent repro | COVERED as leads (repro still 0) |
| (f) agentic devtooling | GitHub/TanStack claim notes | + GitHub Teams/metrics bodies, + TanStack 1.0 body, + Harness versions, + 1Password credential plane | COVERED (substantive) |
| (g) speech/video | Voxtral/Eleven/FLUX claim notes | + all three bodies + Ming repo/body; FLUX 10.95/12.45 discrepancy recorded | COVERED (substantive) |
| (h) robotics/embodied/science | trade-press only | + bio agents eval (PerturbAI/Scripps) as science anchor; robotics still trade-only | PARTIAL (robotics disclosure still missing) |
| (i) safety/security/legal | Gemini PDF unread, allegation quarantined | + OpenAI securing body (CVEs/incidents/Oct 1), + Patch Planet distinction, + licenses by artifact (Apache/MIT/PolyForm/CC-BY-NC-SA/OpenMDW/KohakuMoss) | COVERED (substantive) |
| (j) X/Grok | PENDING (no bytes) | + Kimi X HTML raw archived (timestamp proof); Grok result still pending (Sol-owned) | PARTIAL (1 X raw; Grok pending) |
| (k) deployment/industry | claim notes | + Cloud/Marketplace, Vercel/Ollama/Unsloth, MOSI API, Muse 10M, TanStack, GitHub metrics | COVERED |

Zero-coverage: NONE (every lane ≥1 lead; robotics disclosure + independent repro remain explicit gaps, marked zero not PASS).
