# Japanese Generative AI Technical Survey — Editorial Style Guide v0.1

Status: active editorial guidance  
Established from: 2026-W32 first full issue draft  
Authority: complements `docs/editorial-specification.md`; it does not replace evidence or chronology rules.

## 1. Editorial voice

The survey is Japanese technical prose for readers who are comfortable with AI/ML/software terminology.

- Write the sentence structure in natural Japanese.
- Keep technical English when it preserves a precise source term or avoids a misleading translation.
- Do not translate model names, API names, benchmark names, framework names or paper-defined terms merely for stylistic uniformity.
- Avoid English words when they are only decorative and the Japanese equivalent is clearer.
- Prefer one technical term consistently within an issue rather than alternating synonyms.

Examples of terms that may remain in English when technically useful:
`weights`, `serving`, `harness`, `context`, `benchmark`, `agent`, `workflow`, `tool call`, `open weight`, `Late Breaking`.

The objective is not a fixed Japanese/English ratio. The objective is that a reader can understand the argument on the first pass without losing correspondence to the source terminology.

## 2. Article structure

A major article should normally have the following flow:

1. **Opening proposition** — one bold sentence explaining why the topic matters this week.
2. **Verified event / artifact** — establish chronology and primary facts early.
3. **Technical mechanism or distinction** — explain what is technically different.
4. **Evidence boundary** — vendor/author metrics, benchmark setup, threat model or unresolved point.
5. **Community reaction**, only when useful — what people tested, questioned or built after the event.
6. **Editorial synthesis** — explain why the item matters without upgrading inference into fact.

Do not force all six elements into every short item.

## 3. Headings

Headings should tell the reader the technical distinction, not merely repeat the product name.

Preferred:
- `LiveMem — contextを増やすのではなく、stateを残す`
- `Grok Build — modelではなくagent loopそのものを公開する`
- `Inference / Serving — 実装の現実とdisaggregationの条件`

Avoid generic headings such as `概要`, `詳細`, `評価` when a more informative contrast is available.

Use `sectionkicker` for classification/context, not as a second title.

## 4. Cover and front matter

The cover headline is chosen **after the main article set has been drafted**.

It should express a cross-issue pattern that is actually supported by multiple completed articles. It must not be decided first and then used to force unrelated candidates into a theme.

The cover may contain:
- one short editorial headline;
- one short deck explaining the issue-wide pattern;
- up to three anchor stories.

`This Week in AI` is also written after the body draft. It summarizes evidence-backed patterns that survived article construction.

## 5. Event chronology vs trend chronology

Always distinguish:

- artifact/event date;
- W32/Main-window relevance;
- community momentum date;
- post-cutoff follow-up.

Do not write a renewed trend as if it were a new release.

Preferred phrasing:
- `7月19日のPreviewがW32で再評価された`
- `7月31日の発表後、Cutoff直後にlocal workflow検証が増えた`

Avoid:
- `今週リリースされた` when the artifact was already available before the observation window.

## 6. Claim classes

### Primary / technical fact
Use ordinary cited prose when a primary source or reviewed paper supports the statement.

### Vendor / author claim
Use attribution in prose and, when material to interpretation, a `claimboundary` box.

Do not turn:
`The authors report 2.06× throughput in simulation`
into:
`The system is 2.06× faster`.

### Community observation
Use `communitynote`.

An X post proves that the reaction/post existed. It does not independently prove the technical claim inside it.

### Editorial synthesis
Editorial synthesis is allowed and encouraged when it connects multiple verified facts, but it must be signaled as interpretation rather than source fact.

## 7. Benchmarks and numbers

Concrete numbers should carry enough setup context to prevent false comparison.

For benchmark values, consider:
- harness;
- reasoning effort;
- sampling settings;
- model version;
- dataset split;
- simulator vs real system;
- author/vendor vs independent evaluation.

Do not build a unified ranking table when the compared results use materially different harnesses or evaluation conditions.

## 8. Open-weight / local-AI wording

Do not use `open`, `open source`, `open weight`, and `local` as interchangeable labels.

Separately record where relevant:
- whether weights are published;
- license;
- artifact size;
- supported serving engine;
- practical hardware / memory / storage requirements;
- whether a community experiment is reproducible or merely reported.

`Weights are public` does not imply `the model is practical on a workstation`.

## 9. Safety and security wording

Security stories require a clearly bounded threat/evaluation model.

Avoid sensational compression such as:
- `the model escaped the sandbox` when the source says internet access resulted from misconfiguration;
- `TDX is broken` when the demonstrated result is specific to an observable sparse-access channel;
- `Astra is Critical` when the source says Critical capability cannot yet be ruled out.

When multiple security papers are synthesized, state explicitly if they do **not** share the same cause or threat model.

## 10. Paper coverage

Distinguish:
- paper hypothesis;
- methodology;
- author-reported result;
- independently verified fact;
- limitation/generalization boundary.

Simulation studies must remain simulations in every headline and numerical summary.

A paper with an attractive headline result should not be promoted until the full/targeted review identifies the setup that makes the result true.

## 11. X Community Watch

The purpose is to show **what the technical community did next**, not to create a popularity ranking.

Useful reaction types include:
- reproduction;
- benchmark attempt;
- local deployment;
- workflow integration;
- artifact inspection;
- failure/limitation report;
- governance or deployment concern.

Reaction volume is not a sentiment census. Main-window and post-cutoff posts remain separate.

## 12. Late Breaking

Late Breaking prevents post-cutoff information from contaminating the main chronology.

A Late Breaking item should:
- state that it is post-cutoff;
- explain why it matters to an already selected topic;
- avoid rewriting the earlier article as if the information were known at cutoff;
- receive full verification in the next issue if the topic persists.

## 13. Page budget

The page target is a planning constraint, not a quota.

Do not pad an issue with weak candidates merely to reach the target page count. A shorter evidence-dense issue is preferable to artificial balance or duplicated coverage.

Likewise, do not compress an important claim boundary solely to save a fraction of a page.

## 14. Source notes and provenance

Every published issue should preserve access from article claim back to:

`article -> citation -> candidate/evidence record -> primary/raw source`

Raw Grok output is never silently edited. Corrections and normalization belong in downstream evidence layers.

Rejected/incorrect candidates remain in the inventory when they are useful provenance for understanding detection errors or chronology corrections.

## 15. Final editorial gate

Before freezing an issue:

- citation-to-claim audit passes;
- chronology is consistent across sections;
- Main vs Post-Cutoff classification is intact;
- vendor/author metrics remain attributed;
- simulation/threat-model boundaries are visible;
- terminology is consistent;
- cover/theme is derived from the finished body;
- PDF builds without unresolved citations, missing glyphs or layout warnings;
- rendered pages receive a visual review.

The editorial goal is a survey whose prose is readable, but whose claims remain traceable when scrutinized.
