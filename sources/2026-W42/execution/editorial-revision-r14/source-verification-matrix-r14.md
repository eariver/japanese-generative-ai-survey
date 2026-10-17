# r14 source-verification matrix (additions/edits on r13 base; no rescope)

New live readings this unit: S3a (NVIDIA Nemotron 3.5 research page, 2026-10-14, full body via webfetch 2026-10-18), S3b (Training Recipe Stage-2 RL page incl. MTP Boosting Table 8, same access). S1/S2 carried over. Accepted Evidence unchanged and remains the formal authority.

## M01/TECH-01 — Nemotron MTP acceptance length (VERIFIED, quoted with conditions)
- Exact table row (S3b, MTP Boosting section, Table 8 "Average acceptance length on the SPEED-Bench qualitative split at draft length 7"): rows SFT native 4.589/4.048; SFT+4K 5.080/4.730; Final native 4.287/3.787; Final+MTP-head 4.528/4.436; Final+25K boosting (released) 4.718/4.612 — columns greedy temp-0 / sampled temp-1.
- Derived statements: boosting +10.1% greedy, +21.8% sampled, largest per-position gains at deeper positions; cross-model sampled best 4.612 (Gemma-4 31B 4.565; Qwen3.5 4.331; Qwen3.8-Flash-Next ≤4.213); greedy Gemma 4.837 / Qwen3.5 4.799 higher (i.e. NOT Nemotron-best under greedy — must state).
- serving recipe: every config trains 5 repeated MTP heads, loss 0.3; reference runs varied; policy MTP speculative decoding OFF except reasoning teacher (one speculative token); backbone frozen, hidden-state mixing, LK distillation vs Ultra forward KL; temp-1 ≤8K on-policy rollouts; recipe does NOT include MTP boosting (report trains separately).
- MOPD shares (same page): phase1 35/25/20/15 + 5% self-anchor; phase2 30/20/20/20 + 10%; agentic teacher edge DASHED = unconfirmed lineage (MUST mark unconfirmed, not proven).
- Denominator/baseline: SPEED-Bench qualitative split, draft length 7; greedy temp-0 vs sampled temp-1.
- Negatives/limits: full 79pp report itself not retained (derived excerpt only); greedy crown belongs to others; agentic-teacher lineage unconfirmed; QAD 99.62% median over 36 benches is vendor-reported.
- r14 blocks: P3 s3-06 rewritten with Table-8 numbers + conditions; NEW P3-N1 (Table-8 row reading incl. greedy-vs-sampled cross-model honesty); NEW P3-N2 (MOPD shares + unconfirmed agentic edge + recipe-vs-report scoping).

## M02/TECH-03 — wet-lab denominators (kept fixed + one round-structure block)
- Trajectories are per-target screening rounds (thrombin 0/167→54/208→131/311 = 42.1%, strict de novo 37.1%; myoglobin 20/196→9/244→184/549 = 33.5%; G4 75.0→19.1%→72.4%); 8-clone titrations are a SEPARATE confirmation step, not the 131/311 denominator (r13 already separated; r14 adds explicit round/population reading). No longitudinal identical-denominator claim.
- FAP single-target + single-digit nM/8.6x (r8 blog excerpt, derived-note caveat kept).

## TECH-02 — Earth AI 4×2 (from S2 live read; accepted card lacks these numbers)
- Configs: standalone LLM / +basic tools / +GRA tools reactive / full GRA × Gemini 3.1 Pro + 3.8 Flash.
- Results: GeoExpertQueries 63 vs unusable baselines; GeoKTools 86 vs 41 (strongest baseline = standalone no-tool LLM); CBGB >80 vs <20; UnivEARTH 87–94 saturated.
- Contribution split: tools 3→52 (Flash, GeoExpertQueries); planning 52→63 (+10.5pp for ~3 cents: $0.199 vs $0.167); Flash <1/3 Pro cost; search 7.0→3.2/query; EE use 54% vs 38%.
- Method: 3 repeats, mean±std; human-validated tool-agnostic autorater; best-effort prefix; 100-call/30-min/1M-token-window caps; failures included in cost; dev splits 25/76 + 85/220 released with prompts/code; 3 blind experts; 4 unreconciled queries kept as informative.
- r14 blocks: P6 N1 (4-config + cost), N2 (tool-vs-plan split), N3 (golden/autorater + unreconciled kept) — replacing r13 s6-08/s6-09 merged duplicate.

## Other additions (all accepted-card-grounded)
- P1: s1-02 split (Wonder/Argon, CITE-02); N1 ray-tracer demo-not-benchmark [ARGON SOCIAL]; closing rewrite.
- P2: N1 sealed-eval design [LFM]; closing rewrite. (Serving/queue already covered; no invention beyond card.)
- P3: s3-06 Table-8 rewrite; table Nemotron row appended with acceptance-length condition.
- P4: N1 Codex survivorship/transfer caveat [CODEX]; N2 stop-conditions [AUTOFIX+AISCAN]; closing kept (grounded list).
- P5: N1 distillation durability/FP [DISTIL]; s5-16/s5-17 closings rewritten (keep four-object + independence distinction, drop formulaic tail).
- P6: DROP s6-12 (Rosalind dup; coverage via table row); N4 aptamer rounds [WETLAB]; N5 Deep Review SPOT design (26 papers/29 eq-proofs, logic-aware grader + human audit, 21.1→55.2→89.7, Banach) [DEEPREV]. (FAP/saturation/Earth splits already present.)
- P7: DROP s7-08 (dup of s7-07); N1 GLM Research-Bench regression depth [GLM]; N2 ASPIRE sim-to-real failure mode [ASPIRE]; closing kept.
- Cover deck: `専門身体` → `専門・身体分野`; 工数... (EDIT-04).
- m02: r13 already `文脈100万トークン` (S2-verified) — held, no change. m01/m03/m05: held from r13 (verified clean); closings rewritten once more where formulaic.

## Unverified / SOURCE_INACCESSIBLE
- Nemotron full 79pp PDF bytes (derived excerpts + S3a/S3b pages only); greedy/temperature details beyond Table 8 not claimed.
- Maia unnamed baseline values; independent hardware repro; METR three-tier internals beyond announcement; Vals full methodology beyond card.
- If TeX still falls short of 28pp after honest content, report `EDITORIAL_DEPTH_OR_PAGINATION_DECISION_REQUIRED`; no padding, no Architecture change.
