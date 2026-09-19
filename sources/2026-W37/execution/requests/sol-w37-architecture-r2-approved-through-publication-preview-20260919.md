# W37 execution instruction — Human Architecture r2 APPROVED through Publication Preview

Status: `EXECUTION_AUTHORITY / HUMAN_ARCHITECTURE_R2_APPROVED / CONTINUE_TO_PUBLICATION_PREVIEW`

Date: `2026-09-19 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W37-v2-work`

## 1. Human decision authority

The Human Owner has explicitly reviewed the W37 Architecture r2 Human Review package and decided:

`APPROVED`

Exact reviewed Architecture production authority:

- commit: `55e700a34765654cd2ced0c2a454d4fb3433dd4f`
- tree: `7f3c93216586b712375734a2c81d8dbb1cfa1efc`

Exact reviewed Architecture artifact:

`sources/2026-W37/architecture-v2.json`

SHA-256:

`81e87a64c2418c71340ee8cc1dec28267a55055d2c02d7dbb06e33623efdfcfb`

Human-facing r2 review shell:

`sources/2026-W37/execution/reviews/architecture-r2.md`

Independent Sol review:

`sources/2026-W37/execution/reviews/sol-w37-architecture-r2-independent-review-20260919.md`

Sol verdict:

`PASS / READY_FOR_HUMAN_ARCHITECTURE_REVIEW`

The Human approval accepts the existing Architecture r2 bytes and the seven-package editorial structure. It does not authorize modifications to Discovery, Screening, Evidence, Materiality, Completeness, Selection, or Architecture before drafting.

The r1 Architecture surface was invalidated while still unpresented and no Human decision was recorded for r1. Therefore do not invent a historical Human r1 `REQUEST_CHANGES`. The prior r1 `REQUEST_CHANGES` was an independent Sol review, not a Human Gate decision.

The canonical Human Gate review-index revision must be determined from repository state. Because no Human Architecture Review record currently exists, the expected first canonical Human decision revision should normally be `1`. Verify this through the current Human Gate implementation/index state; if it differs unexpectedly, STOP rather than guessing.

## 2. Mission

1. record the explicit Human Architecture approval using the canonical Human Gate protocol against the exact reviewed r2 production commit above;
2. verify the immutable approval authority and resulting lifecycle state;
3. continue W37 from the approved Architecture through:
   - Draft
   - canonical validation
   - publication rendering/candidate creation
   - lexical reader-surface validation
   - semantic reader-surface review
   - all other profile-required pre-preview checks
4. stop at a fresh:
   `PUBLICATION_PREVIEW / PENDING`

Normal endpoint is a durable Human-reviewable PDF/publication candidate with no Publication Preview Human decision recorded.

Do not Freeze or Release.

## 3. Invocation starting guard

The Muse invocation MUST supply the Exact Starting SHA/tree corresponding to the commit containing this execution request.

Before any repository/GitHub write, read-only verify:

- remote W37 HEAD == Exact Starting SHA from invocation;
- remote W37 tree == Exact Starting Tree from invocation;
- Exact Starting SHA parent == `68e09ba316cae6c377add6430a5206f162d5fbe1`;
- parent tree == `02ae12815295b62df3a44c87c4075e68eb236cbf`;
- remote `main` HEAD == `6aa385cbe287b9b20fac4ea3a61d8ffd6179ed3b`;
- remote main tree == `62cf5dfb30cc692cd19c11289fa80c837fd17b66`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- Production Line tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- Production State remains:
  - lifecycle `ARCHITECTURE_ESTABLISHED`
  - next action `ARCHITECTURE_REVIEW`
  - terminal reason `HUMAN_GATE_REACHED`
  - Architecture Review pending;
- `architecture-r2.md` still binds reviewed production commit `55e700a...`;
- Architecture SHA remains `81e87a64...`;
- independent Sol r2 review remains PASS;
- current research-stage counts remain:
  - Discovery 14
  - Screening 13 KEEP / 1 DROP
  - Evidence 11 VERIFIED / 2 PARTIAL
  - Materiality 12 MATERIAL / 1 CONTEXT / 1 EXCLUDED
  - Selection 12 SELECTED / 1 HOLD
  - Architecture 7 packages.

Any mismatch -> zero write, report expected vs actual, STOP.

No alternate/fallback/review/repair branch.

No force/reset/rebase/squash/history rewrite.

## 4. Mandatory read order

Read at minimum:

1. this execution request;
2. `sources/2026-W37/execution/reviews/architecture-r2.md`;
3. `sources/2026-W37/execution/reviews/architecture-r2-dossier.md`;
4. `sources/2026-W37/execution/reviews/sol-w37-architecture-r2-independent-review-20260919.md`;
5. `sources/2026-W37/architecture-v2.json`;
6. `sources/2026-W37/architecture-review-summary-v2.json`;
7. `sources/2026-W37/architecture-review-attention-v2.json`;
8. `sources/2026-W37/candidate-selection-v2.json`;
9. `sources/2026-W37/profile-completeness-v2.json`;
10. `sources/2026-W37/production-state.json`;
11. current `scripts/survey_human_gate_v2.py` CLI/help;
12. current Draft / publication / reader-surface / candidate / PDF pipeline contracts and CLI help;
13. W36 approved-through-Publication-Preview execution precedent where helpful.

Repository-local reviewed Core behavior is authoritative.

Do not access Google Drive.

## 5. Record Human Architecture approval canonically

Use current canonical Human Gate protocol.

Required semantics:

- gate: `ARCHITECTURE_REVIEW`
- decision: `APPROVED`
- reviewed repository commit SHA: `55e700a34765654cd2ced0c2a454d4fb3433dd4f`
- reviewed_by: `Human Owner`
- review reference must bind:
  - this execution request;
  - `architecture-r2.md`;
  - independent Sol r2 review.
- requested changes: none
- regeneration boundary: none.

Determine the canonical next review revision from the current Human review index. Expected normally: revision `1`, because r1 Architecture was never a Human-reviewed decision.

Use the actual execution timestamp produced at approval-recording time. Do not invent an earlier exact timestamp for the Human's chat message.

After recording:

- read back Human review record;
- read back review index;
- verify exact reviewed commit;
- verify approval snapshot / immutable authority created by current Core;
- verify Production State transition produced by canonical approval logic.

If the canonical protocol refuses the decision because exact bytes/state/revision do not match, STOP. Do not bypass it.

## 6. Approved W37 Architecture

Preserve this editorial thesis semantically:

`In 2026-W37 efficiency went vertical at the platform layer: OpenAI expanded its Sep 10 stack with Financial Services on Astra, a separate GPT-Live-1 voice API, and an Agents API harness; DeepSeek's Sep 10 V4.1-Flash vendor-reported results place its efficiency ahead of its Pro tier at Flash pricing while the announced Sep 14 routing remains a future operation; Cognition pushed coding efficiency (SWE-2) and harness efficiency (Fusion, verified ordinary at 17:00Z); and open weights went vertical (MiniCPM on-device, North translation, Ling multimodal) — with Anthropic's Sep 10 threat report setting the week's technical safety bound.`

Approved package order:

1. `w37-astra-vertical` — Financial Services on Astra
2. `w37-voice-frontier` — separate GPT-Live-1 voice layer
3. `w37-harness-plane` — Agents API + Fusion
4. `w37-efficient-flagship` — DeepSeek V4.1-Flash
5. `w37-frontier-coding` — SWE-2
6. `w37-open-vertical` — MiniCPM + North + Ling
7. `w37-safety-bound` — Anthropic Threat report

Do not merge or reorder packages in a way that materially changes the approved thesis without stopping for new authority.

## 7. Frozen upstream research authority

After approval is recorded, do not rerun or semantically modify:

- Grok/X intake;
- Discovery;
- Screening;
- Evidence / edition views;
- Materiality;
- Completeness;
- Selection;
- Architecture.

Expected frozen authority:

- Grok r3 direct X Raw remains exact;
- Discovery: 14;
- Screening: 13 KEEP / 1 DROP;
- Evidence: 11 VERIFIED / 2 PARTIAL;
- Materiality: 12 MATERIAL / 1 CONTEXT / 1 EXCLUDED;
- Selection: 12 SELECTED / 1 HOLD;
- Architecture: 7 packages.

If Draft exposes a genuine contradiction that invalidates approved Architecture, STOP at the smallest canonical boundary instead of silently altering upstream research.

## 8. Draft evidence boundaries

### OpenAI Financial Services / Astra

Preserve:

- Financial Services uses Astra;
- OfficeQA and other benchmark figures are OpenAI/vendor-reported;
- methodology gaps remain visible;
- pricing, entitlement limits and region boundaries unresolved where Evidence says so;
- X is momentum/community context only.

Do not generalize Financial Services facts to GPT-Live-1 or Agents API.

### GPT-Live-1

Preserve:

- a separate full-duplex voice layer;
- it may delegate to Astra or third-party backend models;
- it is not itself an Astra package;
- benchmark/evaluation claims remain vendor-reported;
- language/telephone coverage gaps remain explicit.

### Agents API

Preserve:

- managed harness/API in public beta;
- Astra may be a configuration/example;
- this does not make Agents API an “Astra API”;
- GA/rate/region gaps remain explicit;
- partner/customer claims remain vendor-described.

### DeepSeek V4.1-Flash

Preserve:

- architecture/model claims according to first-party source;
- ahead-of-Pro comparison explicitly as DeepSeek/vendor-reported;
- unnamed third parties != independently reproduced evidence;
- Sep 14 routing is a future post-W37 operation announced by an in-window document;
- W37 in-window pricing/economics remain separate from future routing.

Do not use unqualified language equivalent to “V4.1-Flash beats V4-Pro” as independent fact.

### SWE-2

Preserve:

- vendor benchmark/cost framing;
- harness/methodology reproduction gaps;
- no independent benchmark truth claim.

### Fusion

Preserve exact temporal authority:

`2026-09-11T17:00:00Z`

which is within W37 ordinary window ending `2026-09-11T22:00:00Z`.

Preserve:

- partnered/vendor-presented evaluation;
- 39% is a table maximum, not uniform improvement;
- untested pair generalization not established.

### MiniCPM / North / Ling

Preserve model-specific boundaries.

MiniCPM:
- card-reported benchmarks;
- on-device/local relevance;
- independent reproduction absent;
- quant/chip behavior vendor-described.

North:
- judge-model evaluation bound;
- CC BY-NC research license / separate production-license implications;
- internal throughput/cost testing not independently verified.

Ling:
- multimodal model-card facts bounded;
- benchmark results card-reported;
- early publication-hour precision unresolved;
- Sep 8/10 bindings establish W37 relevance.

### Anthropic Threat report

Preserve:

- Sep 10 report as ordinary W37 event;
- notable examples are not representative of all incidents;
- investigations/cases are Anthropic/vendor-reported;
- full PDF/IOCs not consumed;
- Sep 11 late-breaking naming/detail does not enter ordinary W37 facts.

### Resignation discourse

Current disposition:

`HOLD / CONTEXT / architecture_usage NONE`

Do not promote it into thesis, package body, technical safety conclusion, or selected Architecture.

It may appear only if a current downstream contract explicitly permits non-promotional review/context notes, and it must remain secondary discourse with no technical weight.

### GLM-5.5 rumor

`DROP / EXCLUDED`

Do not surface it as a technical W37 development.

## 9. X / community provenance in reader-facing output

W37 Grok/X is community observation, not technical authority.

When community movement is reader-facing:

- use auditable public direct X status URLs already retained in the accepted Raw where citation is appropriate;
- do not substitute repository-internal Raw paths for public X references;
- do not cite internal GitHub blob URLs that expose production/internal path vocabulary;
- preserve ordinary vs Late Breaking boundary;
- do not make community momentum broader than the supporting independent-account evidence.

Technical facts must cite primary/authoritative sources separately.

This is intended to avoid recurrence of W36 Issue #502 while retaining the W37 provenance improvement from Issue #505.

## 10. Reader-facing language discipline

Known W36 reader-surface regressions must not recur.

### Internal process vocabulary

Do not leak internal workflow words into magazine prose, including context-dependent terms such as:

- HOLD
- PARTIAL
- VERIFIED
- Screening
- Selection
- Materiality
- candidate
- blocker
- unresolved authority
- internal path names

unless the publication itself is explicitly discussing methodology.

Apply the current reader-surface gate and Issue #434 intent.

### Time-window language

Do not overstate temporal relation.

Use exact date/timing where material.

Do not transform:
- pre-window context;
- post-cutoff Late Breaking;
- future announced operation

into “this week” occurrence.

Apply the lesson from Issue #500.

### Japanese prose

The finished W37 magazine must read as natural technical Japanese, not translated process notes.

Avoid:
- noun-stack English calques;
- mechanically repeated “〜として位置づけられる” phrasing;
- internal qualifier dumps inside main sentences;
- unnatural direct translations of Architecture labels.

Preserve precision while rewriting into reader-quality Japanese.

Apply Issue #501 lesson.

## 11. Review provenance downstream

Issue #506 remains binding.

Worker may create:

- Worker pre-gate analysis;
- deterministic validation outputs;
- Worker dossier.

Worker must not self-author:

- independent Sol review;
- Human review;
- Sol-owned verdict;
- Sol PASS/REQUEST_CHANGES.

The fresh Publication Preview must remain pending independent Sol review and Human judgment.

## 12. Drafting and volume policy

Use approved Architecture as the controlling structure.

Do not impose a page target by deleting selected material or required caveats.

Optimize for:

- coherent synthesis;
- readable Japanese;
- visible evidence boundaries where editorially needed;
- source auditability;
- balanced package density.

Moderate length is acceptable.

Stop only if volume causes a real quality failure such as:

- unreadable density;
- severe duplication;
- layout breakage;
- reader-surface gate failure.

## 13. Canonical downstream pipeline

Run the current reviewed Core pipeline through every required pre-Publication-Preview stage.

Use current CLI/help, not remembered command syntax.

At minimum include all profile-required:

- Draft construction;
- Draft/schema validation;
- Architecture-to-Draft coverage;
- citation/source binding;
- publication rendering;
- durable publication candidate authority;
- TeX/PDF generation;
- PDF authority recording;
- lexical reader-surface validation;
- persisted semantic reader-surface review;
- publication-candidate validation;
- state/checkpoint advancement.

Do not manufacture a semantic PASS in production code.

If semantic reader-surface review is a Worker-generated review, label it Worker/Agent appropriately, not Sol/Human.

If current Core requires a generic repair to continue, STOP and record the defect rather than modifying shared Core.

## 14. Shared-Core freeze

No writes under:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`

Do not modify:

- `main`
- `production/survey-core-v2`

Known generic issues remain out of scope:

- #497 Freeze compatibility
- release workflow nonexistent `validate-state` CLI defect
- #505 future X-intake hardening
- #506 reviewer-attribution hardening

This run stops before Freeze, so do not address Freeze/release defects.

## 15. Publication Preview deliverables

Before stopping, produce durable canonical authority for:

- final Draft;
- publication candidate;
- final rendered PDF;
- exact PDF path;
- SHA-256;
- byte count;
- page count;
- lexical reader-surface result;
- semantic reader-surface result;
- publication-profile validation;
- current Production State;
- fresh Human Publication Preview review shell/dossier.

The Human-facing dossier should make it possible for Sol/Human to review:

- Architecture approval provenance;
- actual section/package structure;
- any drafting compression;
- exact source/citation behavior;
- X/community public auditability;
- vendor-claim qualification;
- treatment of PARTIAL/HOLD/EXCLUDED inputs;
- Japanese-language quality;
- page/layout state;
- remaining non-blocking limitations;
- any deviation from approved Architecture.

Do not record Publication Preview approval.

## 16. Normal STOP condition

Successful normal endpoint:

- Architecture Human review canonically APPROVED;
- Draft generated;
- all required pre-preview validations passed;
- durable publication candidate exists;
- durable PDF exists;
- lifecycle at the current Core-defined Publication Preview gate, normally `RELEASE_CANDIDATE`;
- `PUBLICATION_PREVIEW = PENDING`;
- no Freeze;
- no Release;
- main unchanged;
- Production Line unchanged;
- shared-Core changed paths = 0;
- fresh Publication Preview dossier committed and remote-read-back verified.

Then STOP.

## 17. Commit/push discipline

Use existing W37 branch only.

Use:

- normal commits;
- non-force push;
- remote read-back;
- expected prior SHA verification before meaningful write groups.

Do not create a new branch.

Do not rewrite prior r1/r2 review provenance or Human Gate history.

## 18. Final report

Report at least:

- invocation Starting SHA/tree;
- Human Architecture approval:
  - review revision;
  - review record path/hash;
  - immutable approval authority;
  - reviewed production SHA/tree;
- ending HEAD/tree;
- frozen upstream counts;
- Draft identity;
- final section structure;
- publication candidate identity;
- PDF path/SHA/bytes/pages;
- lexical reader-surface result;
- semantic reader-surface result;
- X/community citation/public-auditability status;
- vendor-claim boundary status;
- Japanese prose quality checks;
- downstream edition-local repairs if any;
- deviations from approved Architecture if any;
- current lifecycle/next action/terminal reason;
- Publication Preview review path;
- Publication Preview Human status = PENDING;
- shared-Core changed paths = 0;
- main unchanged;
- Production Line unchanged;
- exact stop reason.

Human Publication Preview decision must remain absent.
