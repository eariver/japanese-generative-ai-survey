# W42 Sol independent r8 Review — Evidence stage accepted, editorial Selection scope determined

Date: 2026-10-17 JST  
Exact reviewed HEAD: `c26dc2982e45838b7695dda8f0618a9f6cec6ea1`  
Branch: `weekly/2026-W42-v2-work`  
Main: `c8d0ecc1c9566a2303ad3b4c42635d4b672650e4`  
Frozen Core v2: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` (unchanged)  
Human Architecture Review: pending; Human Publication Preview: pending.

**Verdict: `CORE_EVIDENCE_STAGE_ACCEPTED / SOL_MATERIALITY_PASS_WITH_LIMITATIONS / MUSE_SELECTION_SKETCH_REQUEST_CHANGES / SOL_SELECTION_SCOPE_DECIDED`.** The 50-record source-to-Selection machine authority is valid at current `EVIDENCE_REVIEWED`. However the r8 six-package executor sketch is not adopted. The Sol-reviewed selection mapping below is the authoritative editorial input for the next bounded Muse unit; no Human Gate is inferred.

## 1. Real stage and source-scale findings

- `production-state.json` machine checkpoints: Discovery, Screening, Evidence, Materiality, Completeness `passed`; lifecycle `EVIDENCE_REVIEWED`. Selection and Architecture `pending`. Checkpoint `CANDIDATES_NORMALIZED.json` contains actual accepted Evidence/Views/Materiality/Completeness paths and CORE_STAGE_CONTRACT PASS. Main/frozen-Core HEAD unchanged.
- Canonical Discovery 50 and Screening 50 unchanged (KEEP 29 including binder; INSPECT 16; MAYBE 5). Accepted Evidence `f2429e2792f6104ddbe520ea53f938e01ac2cc9873eb1a7713cc75b1ef4ee0e7`: 50 cards, **43 PARTIAL, 7 NEEDS_MORE, zero VERIFIED**, 152 claims (151 substantive and one binder receipt). Edition Views `4296ffd0bd9864ea764a95fa7c0eea8d7384ca4d7a0336db0fa99359148e384a`: 50. Materiality Ledger: 28 MATERIAL, 14 CONTEXT, 7 HOLD, 1 NON_MATERIAL Grok receipt; Completeness LIMITED (2 SATISFIED, 1 LIMITATION).
- Frozen native `current_stage_basis_override` and 17 mapped derived Task `source_type` projections succeeded, with original/projected SHA ledger. The State & stage transition were not manufactured by the reviewer. Generic defects #568 (DM-023), #569 (DM-016) remain OPEN_CORE. Human forbade Core modifications; none were detected in r8 remote diff.
- 91 r8 files called `supplement raw` are predominantly **short authored derived excerpts** with an explicit header `bounded derived excerpt, not byte archive`, rather than actual retained original-site/full-PDF/LICENSE bytes. For example Nemotron 79pp PDF is reduced to a ~500-byte five-line synthesis. The claim that the PDF was read comes from Muse's prior local-tool reports, **not independently reproducible through these short r8 bytes**. Hashing a derived excerpt proves only that excerpt's identity, not original-source bytes. Never claim 91 complete original-source archives. Source authority remains LIMITED.
- A sampled group of accepted cards (Wonder, Nemotron, wet-lab, Earth AI, GLM-Legal, ASPIRE, LFM) attaches nearly every task-bound source ID to **every claim**, while the real specific citation normally appears in `claims[].context`. Several verification targets are generic `UNRESOLVED / No r7 finding recorded` even when primary-body reading is claimed. These are semantic traceability weaknesses **not detected by Core schema**. **Do not modify accepted Evidence/Views/Materiality/checkpoint bytes at EVIDENCE_REVIEWED**: Core does not support arbitrary same-state supersession (DM-022). Instead create separate explicitly non-authoritative per-claim source/limitation and reader-citation clarification, never pass it off as new Core acceptance.
- No independent reproduction-on-hardware; vendor benchmarks (Nemotron, Wonder, Maia, science models) must be labeled vendor/author evaluation, not independent validation. OSI approval is not established for OpenMDW-1.1. FLUX Kommunity conditions and LFM family/file limitations must be disclosed. X-only allegations remain HOLD.

## 2. Critical defects in Muse r8 Selection sketch

1. **Maia 300 was silently excluded from all six proposed packages and its positive/negative rationale list**, despite MATERIAL in the accepted ledger and a detailed first-party architecture read. Scion and Glimpse were praised in positive rationale but lacked explicit package placement. This is a serious Selection completeness defect.
2. The P2 open-weight/rights category and P6 specialist/community category no longer explicitly overlap, but r8's six packages still mix deep systems analysis and weak topical tails; unsupported background studies must not become W42 launch stories.
3. The proposed 21+ pages (plus sidebars) cannot be taken as a hard page cap: 28 MATERIAL candidates and high-method scientific/architecture papers require space for comparison, denominator and license detail. Do not manufacture padding; use ~27–30pp planning and let source-supported treatment determine the final actual extent.
4. Sol requires **precise article-level source ownership**, not the Core card's all-URLs-per-claim references. An exact context URL/primary paper should be the source for each published number; X secondary observation cannot become primary model-evaluation authority by being in the same task.

## 3. Sol-authorized revised thesis and seven-package structure

**Editorial thesis:** W42 was not a simple model-release week. Frontier agent execution, hardware/active-compute economics, licensing constraints on open-weight deployment, software-engineering orchestration, operational safety boundaries and scientific agents advanced together. Report **which system capability is real and what remains merely a vendor claim**, keeping usable numbers/denominators and license conditions visible.

All **28** currently MATERIAL items are accounted for below, once each, with **16 PRIMARY + 12 SUPPORTING**, without adding poorly supported CONTEXT topics as fresh news. Primary/supporting assignments are **editorial decisions by Sol** for the current accepted Evidence. They are not a Human Gate decision; the frozen Core's formal Candidate Selection must still validate them.

| Package | Planned space | PRIMARY candidates | SUPPORTING candidates | What the reader should learn / boundaries |
|---|---:|---|---|---|
| P1 — Frontier agents, memory and long-horizon execution | 4.0 pp | `w42-primary-muse-wonder-20261012`, `w42-primary-gemini4-argon-20261013` | — | Wonder Active Memory/Focus vs Argon real-tool/Minecraft claims; distinguish vendor demo from verified independent agent duration |
| P2 — Hyperscaler silicon and inference efficiency | 2.5 pp | `w42-primary-maia300-20261012` | `w42-primary-lfm25-20261013` | Maia architecture HBM4/NUMA/prefill-decode and named-vs-unnamed efficiency baseline; LFM MoE latency/hardware/throughput workloads are not apples-to-apples |
| P3 — Open-weight architecture, licenses and on-device tradeoffs | 5.0 pp | `w42-primary-spark-open-20261015`, `w42-primary-beam-20261016`, `w42-primary-nemotron35-20261015` | `w42-primary-granite-switch41-20261014`, `w42-primary-minicpm-v47-20261012`, `w42-primary-flux3-klein-20261015` | Compare parameters/active parameters/context/inference feasibility plus actual Apache, Muse, OpenMDW, Kommunity and absent license file differences; no OSI assumption |
| P4 — Agent engineering, code integration and operational gates | 4.0 pp | `w42-primary-codex-gpt6-20261016`, `w42-primary-scion-20261013`, `w42-primary-hydrafusion-20261014` | `w42-primary-agentic-autofix-20261015`, `w42-primary-ai-scan-20261015`, `w42-primary-decider-v12-20261016` | Coding productivity vs maintenance/cost; source-control agent scaling, merge bottlenecks, security/review and tool-version boundaries |
| P5 — Safety, transparency and evaluation access | 3.0 pp | `w42-primary-anthropic-unintended-20261009`, `w42-primary-distillation-20261012` | `w42-primary-ecdsa-20261016`, `w42-primary-metr-20261015` | Distinguish disclosed incidents/vendor claims from independently tested misuse; ECDSA methodological detail; METR evaluator-access mechanism is NOT future outcomes |
| P6 — Scientific agent methods and real-world evidence | 4.5 pp | `w42-primary-wetlab-agents-20261016`, `w42-primary-earth-ai-20261014`, `w42-primary-deep-review-20261014` | `w42-primary-rosalind-discovery-20261011`, `w42-primary-rosalind-plan-20261015` | Lab/simulation/HITL, aptamer denominator and artifacts, Earth GRA benchmarks/evaluation design, PAT review method and life-sciences API rights/pricing |
| P7 — Domain-specialized and embodied intelligence | 3.5 pp | `w42-primary-glm-legal-20261012`, `w42-primary-aspire-20261016` | `w42-primary-glimpse-20261016` | GLM legal model's independent Vals anchor and legal-evaluation caveats; ASPIRE robotics OSS launch vs older paper; Glimpse visually grounded method with stated negative results |

Package body subtotal 26.5 pages. Editorial overview/methodology/sources about 1–2 pages; **target 27–30 pages** and permit a greater truthful length if technical needs justify it. Avoid arbitrary stuffing, a thin near-empty final page, or moving every weak lead to a formal section. Suggested drafting order P1→P2→P3→P4→P5→P6→P7; alternatives: safety-led or infrastructure-led openings. Prefer model-to-deployment causal arc over a random vendor list.

## 4. Per-candidate negative selection and omissions (22 / 50)

**14 CONTEXT** — all NONSELECTED under this decision, with reasoned disposition:
- `w42-dailyx-agenthorizon-20261010`: REJECT as W42 release (paper outside window); optionally compare methodologies only with truthful pre-window citation.
- `w42-dailyx-amazon-worldmodel-20261011`: REJECT (paper outside window, marginal new discussion).
- `w42-dailyx-sakana-mlr-20261011`: REJECT as new W42 paper, may remain future background reading.
- `w42-lead-fish-drama3-20261013`: INSPECT (audio signal, insufficient body for standalone).
- `w42-lead-oss-video-roundup-20261010`: REJECT (aggregation, weak event identity).
- `w42-lead-qwen-turbo-20261011`: REJECT (unconfirmed fresh release, don't present source-late as launch).
- `w42-primary-aws-bedrock-20261013`: REJECT (distribution roundup, not independent technical milestone).
- `w42-primary-claude-code-perf-20261016`: INSPECT (X/changelog observation; causal perf claim not independent benchmark).
- `w42-primary-lechonk-20261012`: INSPECT (vendor/press-level source, weights and methods pending).
- `w42-primary-nvidia-ocp-20261012`: INSPECT (real infrastructure/support context, not standalone headline).
- `w42-primary-nvidia-uk-20261014`: REJECT (commercial investment, not a technical change).
- `w42-primary-openai-eu-agents-20261014`: INSPECT (single-vendor sample/bias caveat).
- `w42-primary-simons-math-20261015`: REJECT (program notice, no published technical result).
- `w42-support-argon-copilot-20261013`: REJECT as independent release; Argon distribution may be cited only in P1 with official source.

**7 HOLD** — all NONSELECTED, keep open with actual gate:
- `w42-carry-ms-decision1-20261011`: HOLD until dated issuer authority (carry-over not a new launch).
- `w42-dailyx-grok-purchasing-20261010`: HOLD as X claim without corroborating contract.
- `w42-dailyx-grok-scale-20261015`: HOLD as X claim without verified infrastructure metrics.
- `w42-dailyx-harness-paper-20261011`: HOLD; actual matching paper authority NOT FOUND.
- `w42-lead-splashboard-qwen38-20261010`: HOLD, weak/unstable project.
- `w42-lead-sulphur2-20261010`: HOLD, insufficient source/method depth.
- `w42-primary-openai-security-20261013`: HOLD; X-only security allegation uncorroborated, do not repeat as fact.

**1 NON_MATERIAL**:
- `w42-grok-x-ledger-20261017`: REJECT as article; truthful provenance binder, exactly one accepted Core Evidence Task/View, never a technical release/sidebar.

No silently unassigned `MATERIAL` candidate; any Muse divergence from the exact 28 needs independent Sol reason and refreshed review **before** canonical Selection. CONTEXT can remain visible as corroborated comparative source only when it is not recast as a selected W42 release.

## 5. Next constrained execution authority

Muse may (a) generate the exact 50-row Core Candidate Matrix and 50 assigned selections using the 28 selected/5 inspect/7 hold/10 reject pattern above; (b) execute immutable Core validation and formal EVIDENCE_REVIEWED→SELECTION_COMPLETE transition; (c) create a seven-package Architecture and substantial evidence/limitation dossier **based strictly on this reviewed mapping**, including edition-local claim→single-best-primary-URL crosswalk and truthful short-excerpt provenance notes; (d) run exact schema/stage checks and stop **`SOL_ARCHITECTURE_AUDIT_READY`** for Sol independent Architecture review, with Human Architecture Gate still pending.

Stop earlier on any real validator/authority blocker. No shared Core changes, no rewriting already accepted Evidence/Views/Materiality/Completeness, no fabricated receipt, no Human approval, no Draft/TeX/PDF/Publication Preview. A Core-valid Architecture artifact is NOT automatically editorially approved. Sol must inspect package detail, major omissions, reader-facing feasibility and full mandatory Human dossier before seeking Human Gate approval.
