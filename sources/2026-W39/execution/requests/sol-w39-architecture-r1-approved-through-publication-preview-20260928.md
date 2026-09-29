# W39 execution instruction — Human Architecture r1 APPROVED through Publication Preview

Status: `EXECUTION_AUTHORITY / HUMAN_ARCHITECTURE_R1_APPROVED / CONTINUE_TO_PUBLICATION_PREVIEW`

Date: `2026-09-28 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W39-v2-work`

## 1. Human decision authority

The Human Owner explicitly reviewed the W39 Architecture r1 Human Review package in ChatGPT and decided:

`APPROVED`

This approval accepts the existing W39 Architecture r1 bytes and seven-package editorial structure. It does not authorize modification of Discovery, Screening, Evidence, Materiality, Completeness, Selection, or Architecture before drafting.

Exact reviewed Architecture production authority:

- commit: `9767d68e0d83aa667eaeeee6394806c612708682`
- tree: `c092b329c8cc1d98a737c6a9d985d4d9e5cb7602`

Exact reviewed gate triple:

- `sources/2026-W39/architecture-v2.json`
  - sha256 `b7afb755b04c7d350f43ad99f160df7373645124f2428b37114c4f3bdba94df3`
- `sources/2026-W39/architecture-review-summary-v2.json`
  - sha256 `d244687609e5a493267f0f6083d7179caada519163719b0f8d1d20088502bb4d`
- `sources/2026-W39/architecture-review-attention-v2.json`
  - sha256 `b27c98036b61a0cd0dd093c088ad496f8fb701b48831eb218de7827cc71bc32e`

Candidate Selection authority:

- `sources/2026-W39/candidate-selection-v2.json`
- sha256 `b6c53eedd1b20c6c35772da7009560f87fefcf76d7ea09b70e755ea08b35a2a6`

Human-facing review shell:

`sources/2026-W39/execution/reviews/architecture-r1.md`

Full review dossier:

`sources/2026-W39/execution/reviews/architecture-r1-dossier.md`

Independent Sol Architecture review:

`sources/2026-W39/execution/reviews/sol-w39-architecture-20260927.md`

Sol finding:

`Blocking: 0 / READY_FOR_ARCHITECTURE_REVIEW`

A later shell-only repair commit corrected one truncated Candidate Selection SHA in `architecture-r1.md` and did not alter the reviewed Architecture bytes:

- repair commit `ddb2244c40d08b41aad96bf439702284c09f9b93`
- repair tree `a47fdf73bbfe3a25d368a53bbe242f26d57ce01b`

Do not change the reviewed production authority from `9767d68e...`; the repair commit only fixes presentation metadata.

## 2. Mission

1. Record the explicit Human Architecture approval using the current canonical Human Gate protocol against reviewed commit `9767d68e0d83aa667eaeeee6394806c612708682`.
2. Verify the immutable approval authority, review index/revision, and resulting Production State.
3. Freeze all approved upstream research and Architecture authority.
4. Draft all seven approved packages in natural technical Japanese from approved Architecture + accepted Evidence only.
5. Run all current profile-required Draft / reader-surface / citation / publication validations.
6. Build the reader-facing TeX/PDF and durable publication candidate using current reviewed Core behavior.
7. Stop at a fresh `PUBLICATION_PREVIEW / PENDING` Human Gate.

Do not Freeze or Release. Do not infer a Publication Preview decision.

## 3. Invocation starting guard

The Muse invocation MUST supply the exact remote branch SHA/tree that contains this execution request.

Before any write, read-only verify:

- remote `weekly/2026-W39-v2-work` HEAD == Exact Starting SHA supplied by invocation;
- its parent must be `ddb2244c40d08b41aad96bf439702284c09f9b93`;
- parent tree must be `a47fdf73bbfe3a25d368a53bbe242f26d57ce01b`;
- remote `main` HEAD == `519aed90607f6e787bb3a7c00b651777835fd657`;
- remote main tree == `3a59771e7e5622c4d3c4bebad55fec52b42151c4`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Production Line tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- Production State remains `ARCHITECTURE_ESTABLISHED / HUMAN_GATE_REACHED / next_action ARCHITECTURE_REVIEW`;
- Human Architecture gate is still repository-state `pending` before canonical recording;
- `architecture-r1.md` still binds reviewed authority `9767d68e...` and the corrected 64-digit Candidate Selection SHA;
- gate triple hashes above remain exact;
- research-stage counts remain:
  - Discovery 15
  - Screening 15 KEEP / 0 DROP
  - Evidence 8 VERIFIED / 7 PARTIAL
  - Materiality 12 MATERIAL / 3 CONTEXT
  - Selection 13 SELECTED / 2 HOLD
  - Architecture 7 packages.

Any mismatch: zero write, report expected vs actual, STOP.

No new/fallback/repair/review branch. No force/reset/rebase/squash/history rewrite.

## 4. Mandatory read order

Read at minimum:

1. this execution request;
2. `sources/2026-W39/execution/reviews/architecture-r1.md`;
3. `sources/2026-W39/execution/reviews/architecture-r1-dossier.md`;
4. `sources/2026-W39/execution/reviews/sol-w39-architecture-20260927.md`;
5. `sources/2026-W39/architecture-v2.json`;
6. `sources/2026-W39/architecture-review-summary-v2.json`;
7. `sources/2026-W39/architecture-review-attention-v2.json`;
8. `sources/2026-W39/candidate-selection-v2.json`;
9. `sources/2026-W39/profile-completeness-v2.json`;
10. `sources/2026-W39/production-state.json`;
11. current `scripts/survey_human_gate_v2.py` CLI/help;
12. current Draft / publication / reader-surface / candidate / PDF pipeline contracts and CLI help;
13. W37/W38 Weekly Architecture-APPROVED downstream precedent where useful.

Repository-local reviewed Core behavior is authoritative. Do not use remembered CLI syntax.

## 5. Record Human Architecture approval canonically

Use the current canonical Human Gate protocol.

Required semantics:

- gate: `ARCHITECTURE_REVIEW`
- decision: `APPROVED`
- reviewed repository commit SHA: `9767d68e0d83aa667eaeeee6394806c612708682`
- reviewed_by: `Human Owner`
- requested changes: none
- regeneration boundary: none
- review reference must bind this request + `architecture-r1.md` + dossier + Sol Architecture review.

Determine the next canonical review revision from repository state. Expected normally: first Human Architecture decision for W39. If current review-index state disagrees unexpectedly, STOP rather than guessing.

Use actual execution wall-clock at approval-recording time for canonical `reviewed_at`. Do not invent or backdate an exact chat-message timestamp.

After recording, read back and verify:

- `gates/architecture-approval.json`;
- immutable review snapshot under `gates/reviews/`;
- `gates/review-index.json`;
- exact reviewed commit and gate triple hashes;
- Production State Human Gate provenance/state transition.

If canonical Human Gate tooling rejects the decision, STOP. Do not bypass it with hand-edited gate JSON.

## 6. Approved Architecture is frozen

Approved package order:

1. `w39-cost-frontier` — Sol/Luna + caching + bounded X/DeepSeek serving context
2. `w39-frontier-challenger` — Opus 5.5
3. `w39-agent-operations` — Cursor harness efficiency + Rollouts/Security Reviewer
4. `w39-coding-models` — Grok 4.7
5. `w39-local-inference` — Transformers GGUF support
6. `w39-science-eval` — ART + MentalHealthBench + DolphinBench
7. `w39-memory-privacy` — secure server-side memory architecture

Preserve the approved thesis semantically: W39 is framed as a week where the frontier became cheaper and more operational, while local inference, agentic science/evaluation, and privacy architecture also moved; vendor numbers remain attributed and late-only signals remain late.

Do not merge, split, reorder, or promote HOLD candidates in a way that materially changes approved Architecture without stopping for fresh Human authority.

## 7. Frozen upstream authority and boundaries

After approval is recorded, do not rerun or semantically alter:

- Grok/X intake;
- Discovery;
- Screening;
- Evidence / views;
- Materiality;
- Completeness;
- Selection;
- Architecture.

Preserve all Architecture boundaries, including at minimum:

- GPT-6 Sol/Luna: vendor benchmarks attributed; no Astra capability-break claim; no independent billing verification; long-task claims bounded.
- Prompt caching: persistent-agent cost/latency implications remain vendor projections where applicable.
- Opus 5.5: System Card was not separately consumed; cost-parity/benchmark claims remain vendor-bound; tester quotes are not independent evidence.
- Cursor harness efficiency: reported 7% is Cursor-production-specific; do not generalize to other harnesses; coming-soon features are not shipped.
- Grok 4.7: capability standing remains limited by effort asymmetry / harness discrepancy; no community-momentum claim because retained X ledger rows are zero.
- GGUF: hardware/architecture scope limits remain explicit; no cross-platform parity or independent performance claim; llama.cpp recommendation preserved where Evidence supports it.
- ART: initial prompt and lab work human; no general autonomous-science claim; biological validity/preprint limitations preserved.
- MentalHealthBench: grader circularity/methodology boundary preserved; no score truth claim.
- DolphinBench: abstract-level consumption only; no PDF-level methodology verdict.
- Google secure server-side memory: forward-looking architecture; no GA/availability or independent security-verification claim.
- DeepSeek: supporting current-state routing/pricing context only; exact in-window cutover instant remains unestablished; no V4.1-Pro claim.
- TBC/AWS: HOLD / no package; partnership exists but performance figures remain insufficiently corroborated.
- Pixel Canary/Codex: HOLD / post-cutoff W40 precursor; do not import into ordinary W39 narrative.
- X: community signal only, never technical authority.

If Drafting exposes a contradiction that actually invalidates approved Architecture, STOP at the smallest canonical boundary instead of silently repairing upstream authority.

## 8. Reader-facing Japanese and terminology discipline

Produce natural technical Japanese, not translated workflow prose.

Do not leak internal process vocabulary into magazine prose unless explicitly discussing methodology, including: `HOLD`, `PARTIAL`, `VERIFIED`, Screening, Selection, Materiality, candidate, blocker, internal paths, review-state terminology.

Apply the current reader-surface gate and Issue #434 intent.

Preserve exact technical terms where Japanese overtranslation would reduce clarity. Read `docs/editorial/ja-technical-terminology-overtranslation-seed.md` as a read-only editorial seed. Do not implement a new linter/auto-rewrite and do not modify Shared Core.

Avoid mechanical noun-stack calques, repetitive `〜として位置づけられる`, and qualifier dumps. Constraints should be expressed as readable source/evaluation caveats in Japanese.

## 9. X/community citations

When X/community observations are reader-facing:

- cite auditable direct public X status URLs already retained in accepted Raw where appropriate;
- do not cite internal repository Raw paths as reader-facing sources;
- keep technical facts sourced to primary/authoritative references separately;
- preserve ordinary vs late-breaking boundaries;
- do not broaden momentum beyond retained supporting accounts.

## 10. Drafting volume policy

Architecture has no fixed page target. Do not delete selected material or required caveats merely to hit a page count.

Optimize for coherent synthesis, readable density, source auditability, and balanced package depth. The user has explicitly preferred substantive coverage over an artificially short report.

Stop only for genuine quality/layout failure, not because the report is somewhat longer than previous issues.

## 11. Canonical downstream pipeline

Run every current profile-required stage needed to reach a fresh Publication Preview, including as applicable:

- canonical Human approval recording;
- Draft package construction for 7/7 approved packages;
- Draft/schema validation;
- Architecture-to-Draft coverage;
- reader-facing TeX/Bib authoring;
- citation/source binding;
- lexical reader-surface validation;
- persisted Worker semantic reader-surface review with correct Worker attribution;
- publication rendering / PDF build;
- durable PDF authority recording;
- publication candidate assembly/validation;
- lifecycle/checkpoint advancement.

Do not manufacture Sol/Human reviews. Worker-generated semantic QA must be attributed as Worker/Agent, not Sol/Human.

If current Core requires generic code/schema repair, STOP and report the defect; do not edit Shared Core.

## 12. Shared-Core freeze

No writes under `.github/**`, `config/**`, `schemas/**`, `scripts/**`, `templates/**`, or `tests/**`.

Do not modify `main` or `production/survey-core-v2`.

All production writes must remain edition-local unless current canonical tooling itself materializes expected edition-local gate/publication artifacts.

## 13. Publication Preview stop

Normal endpoint:

- approved Architecture gate durably recorded;
- Draft and all required pre-preview checks passed;
- reader-facing PDF/publication candidate exists;
- lifecycle is the canonical state immediately awaiting Human Publication Preview;
- Publication Preview decision remains `PENDING`;
- Freeze/Release not entered.

Create a fresh Human Publication Preview review shell/dossier bound to exact candidate/PDF authority if current Weekly precedent requires it, but do not generate Human or Sol decision.

Final report must include:

- starting HEAD/tree;
- ending HEAD/tree;
- canonical Architecture approval ID/revision/reviewed_at;
- approval snapshot/index paths;
- Draft package count and validation status;
- reader-facing TeX/Bib paths;
- PDF path, page count and SHA-256;
- publication candidate path/ID/SHA;
- reader-surface lexical + semantic QA results;
- lifecycle/terminal reason/next action;
- Publication Preview review path(s);
- all deviations/failures;
- shared-Core changed paths count (expected `0`).

STOP at fresh Human Publication Preview. Do not Freeze or Release.
