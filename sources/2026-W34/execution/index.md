# Survey Production execution index — 2026-W34

This is the edition-local navigation record. Machine lifecycle authority remains `sources/2026-W34/production-state.json`.

## Current authority

- Issue / edition: `2026-W34`
- Research Profile: `WEEKLY`
- Publication Profile: `WEEKLY_MAGAZINE`
- Work branch: `weekly/2026-W34-v2-work`
- Pre-integration reviewed semantic baseline: `a9f121f0d65591f52b53515712d7c0bae573b2ef`
- Current reviewed/integrated Core authority: `main@d54f9c7b3a7cef064c6701ab864daab27118cdce`
- W34 Core integration merge commit: `fb83242ddd35f8cf468941f8a76a4bafb331939f`
- Current lifecycle: `ARCHITECTURE_ESTABLISHED`
- Current next action: `ARCHITECTURE_REVIEW`
- Current terminal reason: `HUMAN_GATE_REACHED`
- Discovery checkpoint: `passed`
- Screening checkpoint: `passed`
- Evidence / Materiality / Completeness checkpoints: `passed`
- Selection checkpoint: `passed`
- Architecture checkpoint: `passed`
- Human gates: Architecture Review pending; Publication Preview pending

## Accepted Discovery and event-level Screening basis

- accepted Discovery: `sources/2026-W34/discovery/discovery-v2.jsonl`
  - 40 records / 40 unique IDs
- accepted Discovery acceptance: `sources/2026-W34/discovery/discovery-accepted-v2.json`
- event-level Screening Discovery expansion: `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
  - 110 records / 110 unique IDs
  - W34-C001–W34-C105: 105/105, missing 0, duplicate 0
  - five Sol-authorized `COVERAGE_PASSTHROUGH` children complete accepted-root closure
- historical event-level crosswalk (retained immutable): `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.1.json`
- current corrected crosswalk: `sources/2026-W34/screening/input/event-discovery-crosswalk-v0.2.json`
- DailyX: 7/7 files, 76/76 topics
- Grok r2: 47/47 URLs; 10 ordinary / 20 background / 17 late-breaking
- carry-over: one `RECHECKED_UNRESOLVED`; no promotion

## Screening

Sol semantic authority:

`sources/2026-W34/screening/decisions/sol-screening-decision-authority-20260904-r1.json`

Coverage supplement:

`sources/2026-W34/screening/decisions/sol-screening-coverage-supplement-20260905-r1.json`

Decision counts:

- KEEP: 45
- MAYBE: 19
- INSPECT: 16
- DROP: 30
- TOTAL: 110

Prepared package:

`sources/2026-W34/screening/v2/prepared/w34-event-screening-r2/package.json`

Historical 105-record acceptance remains immutable:

`sources/2026-W34/screening/v2/accepted/2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662/screening-accepted.json`

- result-set SHA: `2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662`
- 105 records / 3 batches
- historical validation on its original 105-record basis: PASS

Corrected current Screening acceptance:

`sources/2026-W34/screening/v2/accepted/5692a79ac20f4376beee02758754a71b771ed78ff30b675d2fa8177af7f65e98/screening-accepted.json`

- result-set SHA: `5692a79ac20f4376beee02758754a71b771ed78ff30b675d2fa8177af7f65e98`
- 110 records / 3 batches
- Screening acceptance validation: PASS
- current-Core stage validation: PASS
- accepted-root accounting: 40/40, unaccounted 0
- expected future non-DROP Evidence tasks: 80

The passed Screening Stage Checkpoint at `sources/2026-W34/orchestration/v2/checkpoints/DISCOVERY_COLLECTED.json` binds the corrected acceptance by exact path and SHA. `resolve_active_screening_acceptance()` returns only this corrected run; it does not scan accepted directories or select by ordering/mtime/latest heuristics.

## Evidence, Materiality, and Completeness

The historical Evidence and Edition View acceptances remain immutable. The current active authorities were regenerated after PR #484 Core integration and are selected from the passed Stage Checkpoint provenance, not by accepted-directory ordering.

- historical accepted Evidence: `sources/2026-W34/evidence/v2/accepted/917f6b5d958d0782e9994a699899145c7fc5f11e0cc9525625385427ce721452/evidence-accepted.json`
  - retained immutable; 80/80 historical `PARTIAL`
- historical accepted Edition Views: `sources/2026-W34/evidence/v2/views/accepted/9545fae97069d7f68bde2c725eb80731561c0366bfdbc20f7ac98b1893514b4f/edition-views-accepted.json`
  - retained immutable; historical `MATERIAL 1 / CONTEXT 45 / HOLD 34`
- Evidence Authority Supplement: `sources/2026-W34/execution/luna/w34-core-repair-r1/evidence-authority-supplement.json`
  - 61 substantive exact authority bodies / 60 unique SHA-256 values / 50 task bindings
- active Evidence acceptance: `sources/2026-W34/evidence/v2/accepted/377134b62c98bf0b65a7cf8cda1ef538eac0e2afcd7aa9aeeeda0f1d09493ada/evidence-accepted.json`
  - `VERIFIED 32 / PARTIAL 27 / NEEDS_MORE 14 / REJECTED 7`
- active Edition Views acceptance: `sources/2026-W34/evidence/v2/views/accepted/bcaa69b03f5d2ae6ba6024474b13fa36cd4b2382c4d1e1ac76dc36edeab9f81e/edition-views-accepted.json`
  - `MATERIAL 1 / CONTEXT 41 / HOLD 31 / NON_MATERIAL 7`
- Materiality Ledger: `sources/2026-W34/materiality-ledger-v2.json`
  - `MATERIAL 1 / CONTEXT 41 / HOLD 31 / NON_MATERIAL 7 / DUPLICATE 4 / EXCLUDED 26`
- Profile Completeness: `sources/2026-W34/profile-completeness-v2.json`
  - overall status: `LIMITED`; current-relevance and technical-significance limitations are explicit; carry-over is explicitly disposed
- Current-Core Evidence/Views/Materiality/Completeness validation: PASS; `CANDIDATES_NORMALIZED` Stage Checkpoint binds the active Evidence/View/Materiality/Completeness set exactly

DailyX, Grok, X, and Sol working-set records remain discovery/community or authority-gap signals. They were not promoted to direct technical Evidence. The exact immutable GitHub Releases response for Transformers v5.15.1 supplies the one bounded in-window repository verification, while its release-note technical claims remain publisher claims.

## Selection and Architecture

- Candidate Matrix: `sources/2026-W34/candidate-matrix-v2.json` — 80 candidates
- Candidate Selection: `sources/2026-W34/candidate-selection-v2.json`
  - `SELECTED 1 / HOLD 64 / INSPECT 15`
  - fresh basis binds the active Evidence/View/Materiality/Completeness authorities; one exact-Raw developer-tooling candidate selected; unresolved authority-gap candidates retained without unsupported promotion
- Issue Architecture: `sources/2026-W34/architecture-v2.json` — `PROPOSED`
- Architecture Review Summary: `sources/2026-W34/architecture-review-summary-v2.json` — `READY_FOR_ARCHITECTURE_REVIEW`
- Architecture Review Attention: `sources/2026-W34/architecture-review-attention-v2.json`

The exact review surface consists of the current `production-state.json`, the three Architecture Review inputs above, and the passed stage-checkpoint chain. Human Architecture Review remains pending; no Human decision is inferred.

## Current-stage execution records

The post-PR #484 production continuation is recorded under:

`sources/2026-W34/execution/luna/w34-core-repair-r1/`

It contains the operator invalidation output, Supplement, fresh interactive inputs, Evidence/Selection/Architecture stage-contract reports, and the final state transition records. The prior `w34-evidence-through-architecture-r1` directory remains historical and is not the active authority.

Operator invalidation record:

`sources/2026-W34/execution/operator-invalidations/architecture-invalidation-0001.json`

It records `human_decision=false`, sequence `1`, the exact pre-invalidation State/Gate inputs, the `CANDIDATES_NORMALIZED` boundary, and the superseded mutable canonical paths. No Human review index row or Human decision was created.

## Recovery execution (historical)

The reviewed `main@a9f121f...` was merged normally into W34 as `b8a0ae502fd03d17bcb4f5d9e1f67a26c77ab30e`. The corrected basis and formal advance are recorded under:

`sources/2026-W34/execution/luna/w34-post-483-core-sync-screening-recovery-r1/`

The earlier recovery was bounded at `CANDIDATES_NORMALIZED`; this continuation subsequently completed Evidence, Materiality, Completeness, Selection, and Architecture and now stops at the Architecture Review Human Gate.

## External sidecar QA pilot

Edition-local pilot authority:

`sources/2026-W34/execution/findings/sol-external-sidecar-qa-pilot-plan-20260905-r1.md`

Current reviewed sidecar SHAs for W34 pilot execution:

- Publication Boundary Validator: `eariver/publication-boundary-redteam@7b9de2105c690daaafa6698c1791d51ca84a92c0`
- Survey Core v2 Authority Auditor + read-only production adapter: `eariver/survey-core-v2-authority-auditor@c5f09d463b21c914d9c59b34597858f6182fc244`

Sol review of the production adapter:

`sources/2026-W34/execution/reviews/sol-authority-auditor-production-adapter-review-20260905-r1.md`

Disposition: `PASS_FOR_W34_READ_ONLY_SIDECAR_PILOT`.

The auditor baseline `main@4f88e55c66646a350ed286683f98b0cbca61f633` remains historical benchmark provenance. The W34 adapter SHA is not Survey Core authority. Both sidecars remain execution-deferred until after Human Architecture Review and do not add lifecycle states, Human Gates, Production State authority, or workflows.

## Relevant historical and current execution records

- Discovery materialization: `sources/2026-W34/execution/sessions/w34-luna-discovery-materialization-20260903-r1.md`
- Discovery binding repair: `sources/2026-W34/execution/sessions/w34-luna-discovery-binding-repair-20260903-r1.md`
- Screening granularity expansion: `sources/2026-W34/execution/luna/w34-screening-granularity-expansion-r1/`
- event JSONL byte repair: `sources/2026-W34/execution/luna/w34-event-discovery-byte-repair-r1/`
- Screening materialization: `sources/2026-W34/execution/luna/w34-screening-materialization-r1/`
- post-#483 Core sync and Screening recovery: `sources/2026-W34/execution/luna/w34-post-483-core-sync-screening-recovery-r1/`

## Not performed in this bounded continuation

- no Production State manual edit; formal State transition used current agent-first Core machinery
- no Discovery rollback/reacceptance or accepted Discovery/checkpoint rewrite
- no historical Screening acceptance or 105 Sol decision mutation
- no Human Architecture Review decision, Drafting, Publication Candidate, Publication Preview, Freeze, or Release
- no external sidecar tool execution against W34 artifacts
- no W33/SP001/SP002/SP003 changes
- no shared Core edit
- no force/reset/rewrite/rebase

## Current disposition

`ARCHITECTURE_REVIEW_READY_FOR_HUMAN / ARCHITECTURE_ESTABLISHED / next_action:ARCHITECTURE_REVIEW`
