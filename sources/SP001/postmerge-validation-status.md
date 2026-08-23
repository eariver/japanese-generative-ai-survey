# SP001 — Post-merge Core v2 validation status

Status: `RESEARCH + EDITORIAL ARCHITECTURE PREPARED / CANONICAL CORE EXECUTION NOT YET ESTABLISHED`

Reviewed/integrated Core start: `2cb52dc293484a5c2ddd3caf9c909f18f4699c49`

Work branch: `special/SP001-v2-work`

Historical pre-redesign branch preserved at: `archive/failed-pre-redesign-SP001-v2-work-20260823`

## Clean-run artifacts prepared

The clean branch contains newly materialized edition-local preparation only:

- `sources/SP001/research-scope-v2.json` — re-materialized from current `docs/thematic-special-backlog.md` / `TS-001`.
- `sources/SP001/intake/postmerge-primary-source-intake.md` — primary-source research map; explicitly not Core acceptance authority.
- `sources/SP001/architecture-preparation.md` — six-package editorial Architecture preparation; explicitly not `ARCHITECTURE_ESTABLISHED`.

No historical failed SP001 `production-state.json`, Candidate Matrix, Evidence acceptance, Architecture approval, or publication candidate was copied into the clean branch.

## X/Grok applicability

Decision prepared: `NOT_REQUIRED`.

Rationale: the thematic question can be closed through technical reports and first-party model repositories/model cards/API/distribution documentation. X community signal is unlikely to materially change the technical Architecture. The parallel W33 validation separately exercises the required X transport path.

This decision remains an editorial preparation until bound by the canonical Production Profile/X manifest flow.

## Research result

Primary-source research supports a six-package Architecture:

1. plural 2022–2024 foundation/model-family formation;
2. separate DeepSeek / Qwen / GLM / Kimi strategy trajectories;
3. sparsity, efficient attention and serving/runtime systems;
4. Chat → reasoning → coding → agentic transition;
5. Open Weight as licensing + distribution + runtime strategy;
6. 2026 frontier convergence and remaining boundaries.

All seven initial scope obligations have an explicit proposed destination. Supporting MiniMax/Yi/Baichuan material remains subordinate unless canonical Evidence/Materiality promotes it.

## Execution limitation observed

The current ChatGPT tool runtime can read/write GitHub through the connector and inspect Actions, but it does not expose a repository checkout shell or arbitrary workflow-dispatch action for running the integrated Core's canonical local CLI on the edition branch.

The local container cannot directly obtain the repository over GitHub network access. The redesigned six-workflow Actions surface intentionally removed research/editorial lifecycle execution from Actions. Creating a temporary workflow/test/Core mutation to gain code execution would violate the formal post-integration validation rule and would make the run invalid as cold-start evidence.

Classification: `TRANSIENT_EXECUTION / OPERATOR-RUNTIME CAPABILITY`, **not an observed shared-Core defect**.

## Evidence already available

The merged candidate's exact-head Core CI ran 171 Core-v2 tests successfully (6 legacy compatibility tests skipped), including SP001 scope materialization, Thematic closure, Screening/Evidence integrity, Candidate Matrix derivation, Architecture semantics, and normal autonomous progression to the Architecture Human Gate. This is regression evidence only and is not substituted for this real-production run.

## Next valid action

Resume from a runtime that can execute the integrated repository Core locally on `special/SP001-v2-work`, then:

1. run SP001 bootstrap/profile initialization from the current scope authority;
2. initialize canonical Production State and execution record;
3. materialize the researched primary sources as exact Discovery/Raw provenance;
4. execute Screening and factual Evidence verification;
5. close Materiality/Profile Completeness;
6. derive Candidate Matrix and author complete Candidate Selection;
7. create exact `architecture-v2.json`, review summary and attention artifacts from those bound authorities;
8. run stage validation/checkpoint and stop only when the canonical State reaches `ARCHITECTURE_REVIEW`.

The prepared research/Architecture may be used as editorial input, but must not be relabeled as canonical accepted artifacts unless the above Core chain passes without shared-Core repair.
