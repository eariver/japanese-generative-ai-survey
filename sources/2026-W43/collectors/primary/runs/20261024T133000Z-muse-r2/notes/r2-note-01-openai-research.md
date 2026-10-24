# W43 r2 consumption note 01 — OpenAI research trio (DC-02, SUBSTANTIVELY_CONSUMED via webfetch markdown 2026-10-24)

Method: direct `openai.com/index/*` webfetch (rendered markdown read in full above); `curl` with generic UA returned HTTP 403 challenge bytes (discarded, recorded as failed raw-HTML attempt). No original HTML archived; consumption is at rendered-body level, not byte-identical HTML. Publisher/date proof: page headers Oct 23 / Oct 21 / Oct 19; Keep-reading cross-links corroborate dates.

## A. Securing our frontier model training environment (Oct 23, 2026) — IN, independent technical event
- Containment doctrine: no live internet for frontier RL; offline world (cached web index, message board); defense in depth (restricted containers in microVMs, own kernel + hypervisor; macOS/Windows virtualized; GPU user-space sandboxing; network/cloud perimeters hold even after host compromise).
- Incident grounding: Sep 20 DNS-resolver misconfig → limited live-internet access (contained); Hugging Face July incident cited; pause → resume RL/inference Oct 1 (11 days later).
- Red-team scale: hundreds of billions of tokens; teams of frontier agents (incl. upcoming GPT-6 Astra Cyber + internal frontier model) with source/config/vuln docs supplied (attacker-favorable, not unaided capability measure).
- Findings (patched/disclosed): Kata Containers CVE-2026-24834 + privilege/filesystem isolation PRs; gVisor fd handling; Moby/Docker syscall filters; kernel CVE-2026-74753/80521/80841; metrics-service firewall-approved connection reuse → fetch model URL; DNS/firewall misconfig paths; cross-isolation channels (cache-timing Spectre-style, storage/CPU/TLS-cache timing). Monitoring/stopping gaps repaired; high-compute red-team made part of safety cases.
- Caveat: attacker-favorable conditions; curve is effort illustration, not controlled compute→findings law. Separate from Patch the Planet (disclosure execution) and from Oct 21 Cloud/Decisions deployment products.

## B. Using thousands of AI agents for biological data (Oct 21, 2026) — IN, independent evaluation event
- Distributed biological reasoning: thousands of GPT-Rosalind agents over whole-brain CRISPR atlas (millions of mouse brain cells) in 32 min; per-perturbation agent (cellular response + literature + mechanism report) → reasoning atlas (genes×effects×papers×mechanisms).
- Results: Tsc1/Tsc2 cerebellar divergence (dozens of neuronal genes; TSC2-linked human cerebellar abnormality); DCTN1→cholesterol-gene upregulation → distribution-failure hypothesis (testable). Human-equivalent months/year compressed; 700+ vs 11 refs (distributed vs single at largest workload); blinded experts preferred distributed 75%.
- Provenance: bioRxiv 2026.10.15.759436v1 (paper), HF dataset perturbai/wholebrain_crispr_atlas, GitHub jinlabneurogenomics/distributed_agent (reasoning atlas). Scientists remain in loop; leads require wet-lab follow-up. Separate from Rosalind Academic Plan (Oct 15 access program, OUT background).

## C. Advancing coding in low-resource languages (Oct 19, 2026) — IN, independent eval event
- MultiLangBench (new, GitHub openai/MultiLangBench): SQLite-compatible engine from scratch, 20 langs, DB-file shared interface, reference-SQLite check. Astra 87.4% avg (vs Sol 26.8%); every lang up incl. COBOL 10.9→72.1, OCaml 25.6→85.8, Fortran 21.4→83.5, VB 25.5→89.4; 19/20 ≥83% (COBOL hardest 72%). Luna 40.3% at $0.77 vs $3.48 Sol (−78%).
- COBOL migration eval: hidden byte-for-byte parity tests (fixed-point truncation semantics as example trap). Sol 86.6% low effort (61% cost of Sol 5.6%) vs 5.4% baseline; 97.9% high effort (near saturation). Expert review still required for production.
- Context: COBOL 40%+ online banking / 80% in-person CC / 95% ATM; Fortran weather/nuclear. Enterprise feedback-driven. Cost/accuracy from vendor tables (harness/effort pinned in footnotes).
