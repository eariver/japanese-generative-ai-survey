# Survey Production Core v2 — Sol/Luna Research and Architecture Review Governance

Status: `CANONICAL PRODUCTION GOVERNANCE / HUMAN-DIRECTED / 2026-09-07`
Applies to: Weekly, Retrospective Period, standalone Thematic, and guided Special series work

## 1. Purpose

This document prevents two coupled failure modes:

1. execution-agent output being treated as editorial/research authority without an independent semantic review; and
2. an Architecture Review being reduced to a short `APPROVE / REQUEST_CHANGES` request before the Human has been shown enough evidence to judge whether the research itself was sufficient.

A machine-valid pipeline state such as `READY_FOR_ARCHITECTURE_REVIEW` is necessary but never sufficient for Human Architecture Review readiness.

The operating roles are:

- **Sol supervisor/reviewer** — owns research sufficiency, semantic authority consumption, materiality, Selection judgment, Architecture responsibility, and the Human-facing Architecture Review dossier;
- **Luna/Work execution agent** — owns bounded execution, bulk retrieval, exact-byte capture, provenance, normalization, task-level evidence work, deterministic regeneration, and gap-fill work explicitly delegated by Sol;
- **Human Owner** — owns the two normal Human Gate decisions.

Model/product names may evolve, but the responsibility split is semantic: the supervising reasoning/review role must remain independent from the execution role.

## 2. Non-delegation invariant

Luna/Work is an execution engine and research assistant, not the final editorial authority.

Luna/Work may propose or mechanically materialize Evidence, Edition Views, Materiality, Selection, or Architecture artifacts, but those artifacts do not become sufficient grounds for Human Architecture approval merely because deterministic validation passes.

Sol must independently inspect the source/Evidence chain before relying on Luna/Work judgments for:

- research completeness;
- whether a captured primary source was actually consumed semantically;
- whether an unresolved claim is truly unresolved rather than merely unprocessed;
- materiality and significance;
- Selection/HOLD/INSPECT disposition;
- Architecture package choice, ordering, omission, and page allocation.

`Luna produced it` and `Core validated it` are provenance statements, not semantic approval.

## 3. Default work split

| Production activity | Luna/Work execution role | Sol supervisory role |
|---|---|---|
| Source retrieval | bulk retrieval, exact bytes, retries, provenance | search strategy, coverage obligations, missing-source judgment |
| Discovery inventory | normalize and materialize candidates | independent completeness audit and fresh negative-space sweep |
| Evidence tasks | execute task-local verification and structure records | inspect primary bodies, claim extraction, unresolved-vs-unconsumed distinction |
| Authority gap fill | run targeted searches/retrievals | decide which gaps must be pursued and when saturation is defensible |
| Materiality | provisional annotation may be generated | final semantic/materiality judgment |
| Selection | provisional disposition may be generated | final editorial selection/omission judgment |
| Architecture | provisional artifact may be generated only from explicit reviewed semantics | owns Architecture design and Human-facing rationale |
| Human Architecture Review | may prepare machine artifacts | owns the complete review dossier and recommendation |
| Drafting/publication execution | execute bounded transformations/builds | editorial, semantic, and visual review |

Unless an explicit Human instruction overrides this split, a long Luna/Work run must not silently collapse `Discovery -> Evidence -> Selection -> Architecture -> Human Gate` into one unreviewed execution chain.

## 4. Mandatory Sol review checkpoints

### 4.1 Discovery completeness review

Before Evidence results are treated as a sufficient research basis, Sol must independently evaluate Discovery coverage.

The review must include:

- source-intake surfaces actually exercised;
- major vendor/project/research/community lanes expected for the Profile;
- important first-party channels and repository/release surfaces;
- negative-space review: notable events that a reasonable independent sweep would expect but the inventory does not contain;
- duplicate/concentration effects that make a large record count misleading;
- a fresh search/sweep independent of the execution agent's candidate list when practical;
- explicit residual coverage limitations.

Candidate count alone is not a completeness argument.

### 4.2 Evidence authority-consumption review

After Evidence regeneration, Sol must distinguish four states for important candidates:

1. `AUTHORITY_NOT_FOUND` — no suitable primary authority was located;
2. `AUTHORITY_RETRIEVAL_FAILED` — a suitable locator exists but exact content could not be obtained;
3. `AUTHORITY_CAPTURED_BUT_UNCONSUMED` — primary content exists in repository/provenance but its substantive claims were not incorporated into Evidence;
4. `AUTHORITY_CONSUMED` — relevant primary content was actually read, converted into bounded claims, and limitations reflect the source rather than a generic placeholder.

`PRIMARY_OFFICIAL` binding alone does not prove `AUTHORITY_CONSUMED`.

For every substantive captured primary body that could affect materiality, Sol must inspect whether the body supports additional candidate-local claims. Generic text such as `the primary source is still required`, `locator only`, or `technical details remain unaccepted` is blocking if the required primary body is already present and readable.

### 4.3 Iterative gap-fill review

One verification attempt per candidate is not a default stopping rule.

For material or plausibly material candidates, unresolved authority must trigger targeted iterative gap fill across appropriate first-party surfaces, for example:

- announcement/article;
- documentation/changelog/release notes;
- API/model/product documentation;
- official repository/release/tag/commit;
- paper/model card/system card;
- security/advisory database;
- official cloud/provider distribution page.

Stop only when the remaining limitation is source-backed and defensible, not because the first URL failed or because one retrieval attempt was recorded.

### 4.4 Materiality and Selection review

Before Architecture is considered mature, Sol must review both positive and negative decisions:

- why each selected item is material;
- why strong/high-signal candidates are not selected;
- whether `CONTEXT`, `HOLD`, or `INSPECT` is caused by genuine Evidence limitation versus incomplete Evidence consumption;
- whether multiple candidates should be grouped into one editorial package;
- whether a sparse issue is genuinely sparse or only appears sparse because of research compression.

Extreme compression requires additional scrutiny. At minimum, if `SELECTED <= 1` while either `non-DROP >= 20` or `VERIFIED >= 10`, Sol must perform and document a dedicated **compression audit** before recommending approval.

The compression audit must test the counterfactual: *if the captured primary authorities were fully consumed, could a materially different multi-item Architecture be supported?*

## 5. Luna/Work stopping discipline

For research-heavy production, the default supervisory boundary is:

```text
Source Intake / Discovery
-> Luna/Work execution
-> Sol Discovery completeness review
-> Evidence + iterative gap fill
-> Luna/Work execution
-> SOL_EVIDENCE_REVIEW_READY
-> Sol authority-consumption + materiality review
-> additional Luna gap-fill loop when needed
-> Sol-reviewed Selection semantics
-> Architecture preparation
-> Sol Architecture review
-> Human ARCHITECTURE_REVIEW
```

Luna/Work may continue farther in one run only when Sol has already supplied the required semantic decisions or an explicit bounded instruction authorizes that continuation.

A request such as `Architecture Reviewまで編纂` authorizes autonomous production toward the Human Gate; it does **not** waive the mandatory Sol supervisory reviews in this document.

## 6. Architecture Review is a dossier, not an approval prompt

Before asking the Human for `APPROVED` or `REQUEST_CHANGES`, Sol must present a substantive Human-facing Architecture Review dossier. A short machine-status summary is not sufficient.

The dossier must contain, at minimum:

1. **Exact review identity** — edition, revision, exact reviewed repository commit, current lifecycle/Gate state.
2. **Research coverage** — Source Intake surfaces, Discovery scale, independent completeness findings, and residual coverage gaps.
3. **Evidence quality** — Evidence status counts plus authority-consumption findings; how many important primary bodies were actually consumed, not merely bound.
4. **Major candidate map** — principal themes/candidates and their disposition (`SELECTED`, `INSPECT`, `HOLD`, excluded/merged/context) with concise reasons.
5. **Negative-space / omission review** — important candidates not selected and why they are absent from the proposed issue.
6. **Editorial thesis** — what the issue is saying as a whole and why that synthesis fits the period/profile.
7. **Architecture packages** — order, role, primary/supporting candidates, claim boundaries, and rationale.
8. **Page/section allocation** — intended length and structural balance, including omitted optional sections such as Paper Watch when relevant.
9. **Counterfactual alternatives** — at least the materially plausible alternative Architecture(s) considered and why they were rejected.
10. **Known limitations and risks** — completeness limitations, chronology boundaries, publisher-only claims, unresolved authority, carry-over/late-breaking issues, and any reason the Human should hesitate.
11. **Sol review finding** — explicit blocking/non-blocking findings and recommendation.
12. **Human decision options** — only after the above has been presented, ask for `APPROVED` or `REQUEST_CHANGES`.

The Human must be able to judge both **the proposed Architecture** and **whether the research pipeline did enough work to justify that Architecture**.

## 7. Prohibited abbreviated review behavior

Do not request Architecture approval merely because:

- `architecture-review-summary` says `READY_FOR_ARCHITECTURE_REVIEW`;
- deterministic stage validation passes;
- the Architecture artifact is internally consistent;
- one selected candidate is well sourced;
- Luna/Work reports completion;
- a prior Sol pass checked only the selected candidate or only the final Architecture bytes.

Do not reduce the Human Gate to a sentence such as `APPROVE推奨です。承認しますか？` before the mandatory dossier is shown.

A later Human request for a concise recap may shorten the presentation, but the first presentation of each Architecture revision must satisfy the dossier requirement unless the Human explicitly waives it for that revision.

## 8. Review of unselected evidence is mandatory

Architecture review must inspect more than the selected set.

At minimum Sol must sample and, where risk indicates, exhaustively inspect:

- substantive primary authorities for high-signal unselected candidates;
- `VERIFIED + CONTEXT/HOLD` combinations;
- candidates whose source body is substantially richer than their Evidence claims;
- candidates whose unresolved reason contradicts available repository evidence;
- clusters where many candidates were collapsed or held for the same generic reason.

If these checks show a systematic Evidence-consumption defect, the correct outcome is `REQUEST_CHANGES` and upstream regeneration, not approval of a sparse Architecture.

## 9. Human Gate semantics remain unchanged

This governance adds mandatory internal supervisory work but does not add a third normal Human Gate.

The two normal Human Gates remain:

1. `ARCHITECTURE_REVIEW`;
2. exact-byte `PUBLICATION_PREVIEW`.

Sol review checkpoints are internal quality controls. They must not become repeated confirmation prompts to the Human.

## 10. Reusable finding handling

When a Human Architecture Review exposes a reusable failure in research depth, role separation, or review presentation:

1. repair the edition through the correct Human `REQUEST_CHANGES` path;
2. classify the failure as edition-local or shared;
3. update this governance/checklist when shared;
4. add deterministic protection only where the failure has crisp machine-testable semantics;
5. preserve the semantic review responsibility even if a deterministic warning is added.

The objective is not to maximize process ceremony. It is to ensure that execution throughput cannot silently substitute for research judgment, and that the Human Gate receives enough information to detect a bad upstream premise before approving downstream work.
