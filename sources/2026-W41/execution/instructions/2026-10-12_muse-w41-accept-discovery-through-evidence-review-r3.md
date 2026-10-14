# J-GAS W41 — Muse r3 canonical Discovery Acceptance → Screening → Evidence review preparation

Status: EXECUTION_AUTHORITY / SOL_DISCOVERY_COMPLETENESS_PASS / CORE_V2_IMMUTABLE / STOP_AT_SOL_EVIDENCE_AUTHORITY_REVIEW
Date: 2026-10-12 JST
Repository: eariver/japanese-generative-ai-survey
Existing work branch only: weekly/2026-W41-v2-work

## 0. Startup exact identity / zero-write guard

The invoker supplies exact Starting HEAD and Expected Starting Tree for THIS instruction commit. In a read-only preflight require:
- remote weekly/2026-W41-v2-work HEAD and Tree exactly match invocation;
- the instruction commit parent == fbc85d144640453f787db68440b68d57f5d693b2 (Sol PASS Review commit);
- reviewed Muse r2d HEAD d02ea4402f83e527a3ab6957888d450b49f3b7ee and Tree a73c06fc0ed07d74be1561353277da7b32a8e10a are in the exact ancestry;
- remote main HEAD == 83f581ebc0dd8945ca7116f65bf6b853ca1fe6c8, Tree == 31c0adc5b57761e5073d100554279a8adc5a18f4;
- production/survey-core-v2 HEAD == 774dd39a951c9ac3818e83dfffd4c7666efb0a20, Tree == cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481;
- current canonical W41 State == ISSUE_INITIALIZED, next_action stage:discovery, Architecture and Publication Preview pending; X Manifest result status PARTIAL, intake status COMPLETE, expected raw SHA preserved.

Mismatch → ZERO WRITES and exact expected/actual report. Never create another branch or force, reset, rebase, rewrite, cherry-pick, change W40, main, shared Core, scripts, configuration, schema, CI or Human approvals. Preserve unowned worktree edits rather than discarding them; stop if a dirty worktree prevents safe operation.

## 1. Read source authority

Read, in order:
1. `sources/2026-W41/execution/reviews/sol-w41-discovery-completeness-r2d-PASS-20261012.md` (Sol's editorial approval only);
2. W41 profile/state/index and `sources/2026-W41/discovery/discovery-v2-proposal-r2d.jsonl` (37 review-approved rows);
3. immutable 7 DailyX pre-PDF raw files, `w41-dailyx-92topic-crosswalk-r2d.md`, Grok raw + Sol temporal audit + current `external/x/x-source-intake-v2.json`;
4. prior W41 completeness reports and W40 four carry-over HOLD obligations;
5. canonical Core v2 frozen Discovery Acceptance, X schema, Stage Validation, Agent Checkpoint, Screening run/package/acceptance, and Evidence task/card/view contracts. W40 accepted Discovery and `sources/2026-W40/execution/instructions/2026-10-10_muse-w40-accept-discovery-through-evidence-review-r4.md` are FORMAT PRECEDENTS only.

## 2. Canonical Discovery acceptance

Sol's `SOL_DISCOVERY_COMPLETENESS_PASS` approves the *research-inventory completeness*, NOT Core acceptance and NOT factual authority for each claim.

A. Materialize `sources/2026-W41/discovery/discovery-v2.jsonl` as the exact validated r2d 37-record source set. Verify original proposal bytes/hash, schema and all unique IDs; do not silently modify candidate content in the name of acceptance. If a Core contract conflict is discovered, STOP and report.
B. Use frozen Core `scripts/survey_discovery_v2.py` functions `build_acceptance` and `validate_acceptance` (verify actual CLI/module signature) to create exact `sources/2026-W41/discovery/discovery-accepted-v2.json`. Verify 37 accepted records, actual immutable file SHA/byte_count, raw path binding, X manifest's `discovery_ids` and acceptance graph.
C. Use canonical Core Stage Validation/Checkpoint/State transition. Advance `ISSUE_INITIALIZED -> DISCOVERY_COLLECTED` only after all checks PASS. Core-generated State; no manual JSON State editing. Use direct local frozen CLI or trusted `ADVANCE_STAGE` Operator Bridge (request-only commit through Issue #448) if local canonical runtime is unavailable. Never invent Core outputs or skip stage validation.

## 3. Screening and Candidate Normalization

- Screen all 37 accepted Discovery records through canonical Core tools; dedup event identities with transparent per-record dispositions. Distinguish original model release vs router/API offering, X post vs underlying issuer event, first-party paper vs second-hand paraphrase, available weights vs promised weights, and original event-time vs later engagement.
- Explicitly classify W40 carry-over HOLDs (Pixel Canary, TBC Video, Ai2 AstaBrief, ServiceNow AutoSynthData), W41 cutoff-sensitive MS Decision-1/Tencent and Oct9 vendor entries. Do not promote uncertain sources on a post ID timestamp alone.
- Any weak/provisional new-8 item may remain HOLD/CONTEXT/UNRESOLVED pending Evidence; 37 discovery records do not imply 37 selected articles. Preserve defensible rejections with source-specific rationale.
- Validate and accept canonical Screening and Candidate Normalization artifacts; advance `DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED` via Core stage checks and actual checkpoint, not manual mutation.

## 4. Evidence preparation — independent Sol review boundary

For technically material candidate pool, conduct first-party source consumption and build provisional Evidence tasks/cards/Edition Views and reviewer handoff. Distinguish:
`AUTHORITY_NOT_FOUND`, `AUTHORITY_RETRIEVAL_FAILED`, `AUTHORITY_CAPTURED_BUT_UNCONSUMED`, `AUTHORITY_CONSUMED`.

Priority source checks:
- OpenAI textGrain issuer blog and technical report PDF (scheme, detection validity/robustness, rollout), Decisions API SDK/changelog, actual mathematics paper/repository;
- Google Nano Banana 2.1, SynthID portal/blog and EmbeddingGemma 2 model card/weights/benchmarks;
- StepFun Step 5 Preview issuer announcement plus OpenRouter model ID/pricing, distinguishing preview access from promised open-weight delivery;
- Nace Drex/NDI, ElevenLabs ElevenAgents detection and protocol working group; keep X-only marketing unverified if no docs;
- Liquid AI d1; AWS Nova Sonic; Aleph Alpha Kolibri, Perplexity decider/embedding models; Cloudflare Clef-omni exact issuer timestamp and weight status;
- Mistral Large 4 49B original-X vs 52B current-doc parameter accounting; Reflection Beam weight release promise; vendor vs independent benchmarks;
- evaluate screening-relevant omitted/held technical research under materiality without expanding the original historical window or creating editorial filler.

For every material claim: source URL, version/time, exact source body actually consumed, faithful bounded excerpts where appropriate, source rights, SHA, claim-level attribution, methodology, license, deployment/weight availability and vendor-versus-independent evidence. DailyX/Grok-derived summaries and URL lists must not masquerade as consumed first-party research. Limited publisher/source accessibility must be explicit.

Data-quality caveat: one Daily X report `2026-10-08_0700.md` says original investigation at 07:04 JST, although some r2d `observed_at` fields were set from nominal filename time 07:00 JST. If this affects canonical source observation provenance, correct the relevant **proposed** rows with a specifically documented source-based adjustment before acceptance, rereview exact bytes if change is substantive, and never manufacture timestamp evidence. Do not silently alter the 37-row reviewed proposal.

## 5. Hard stop

After canonical `CANDIDATES_NORMALIZED`, do not accept the final Evidence stage (`EVIDENCE_REVIEWED`) until Sol independently reviews actual original-source consumption and unresolved candidate-level risks. No Selection, Architecture, Draft, PDF, Publication, Human Gate decision or Release work in this r3 unit.

Deliver a complete `SOL_EVIDENCE_AUTHORITY_REVIEW_HANDOFF.md` with:
- exact starting/ending remote HEAD and Tree, reviewed main/Core identities, commits and changed paths;
- Core Discovery Acceptance hash, graph hash, X Manifest hash/raw SHA and all 37 record statuses;
- Screening acceptance/normalized candidate count with per-candidate group, reject and HOLD dispositions; official checkpoints and Core validation results;
- per material Evidence candidate: original technical source, true capture/consumption class, actual data/benchmark/availability restrictions, deficiencies and recommended handling;
- 92 DailyX original anchors and 14 Grok URL reconciliation unchanged;
- canonical terminal State `CANDIDATES_NORMALIZED`; Human gates still pending and Core unmodified.

Normal non-force pushes only, edition-local writes only. If validation or authority cannot be satisfied, STOP with exact machine failure and do not claim a later State. Await fresh Sol Evidence Authority-Consumption Review before any Evidence acceptance.
