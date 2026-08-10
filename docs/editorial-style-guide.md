# Japanese Generative AI Technical Survey — Editorial Style Guide v0.2

Status: active editorial guidance  
Established from: 2026-W32 first full issue draft; revised from Issue #9 reader-facing review  
Authority: complements `docs/editorial-specification.md`; it does not replace evidence or chronology rules.  
Scope: applies to all published Japanese Generative AI Technical Survey editions, including Weekly and Special unless a rule explicitly says otherwise.

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

## 2. Published prose and internal editorial metadata

The publication has three information layers. Do not collapse them into one another.

1. **Published prose** — natural technical-magazine prose for the reader.
2. **Claim Boundary / Community Observation / Source Notes** — reader-visible information needed to judge claim strength, source limits, chronology or community context.
3. **Repository provenance** — complete production metadata such as Screening state, Candidate Selection, Evidence Task IDs, Draft Packages, review status, collector provenance and future-work bookkeeping.

Evidence-first transparency does **not** require exposing pipeline jargon in article prose.

Reader-facing article text must normally not contain internal production terms such as:

- `Candidate Inventory`
- `Candidate Selection`
- `Reaction Pass`
- `primary verification` as a workflow status
- `Issue Architecture`
- `Evidence Task`
- `Draft Package`
- selection/promotion status such as `昇格`
- production TODOs such as `次号で追跡する`

Translate the underlying meaning into a statement useful to the reader.

Preferred transformations:

- `Reaction Passでは～` -> `X上では～が観測された`
- `今回のEvidenceでは固定できていない` -> `公開時点で一次情報から正確な公開時刻までは確認できていない`
- `今回primary verificationしていない` -> `現時点で一次情報による確認が取れていないため、本稿では扱わない`
- `Candidate Inventoryへ残す` -> remove from article prose; preserve it in Repository provenance
- `次号で追跡する` -> when useful, `今後の追加検証を要する` or a concrete Watchlist observation point

The terms **Claim Boundary**, **Community Observation**, **Editorial Cutoff**, and other reader-facing evidence-strength concepts may remain when they help the reader understand the publication boundary.

Detailed internal terminology may remain in Source Notes or Repository provenance when clearly separated from the magazine body. A source file that intentionally contains internal metadata rather than article prose may use the explicit preflight exemption marker documented by the source-preflight tool; this exemption must not be used to hide pipeline language in ordinary articles.

## 3. Article structure

A major article should normally have the following flow:

1. **Opening proposition** — one bold sentence explaining why the topic matters in this edition.
2. **Verified event / artifact** — establish chronology and primary facts early.
3. **Technical mechanism or distinction** — explain what is technically different.
4. **Evidence boundary** — vendor/author metrics, benchmark setup, threat model or unresolved point.
5. **Community reaction**, only when useful — what people tested, questioned or built after the event.
6. **Editorial synthesis** — explain why the item matters without upgrading inference into fact.

Do not force all six elements into every short item.

For Weekly, `why this edition` normally means **why this week**. For a Special, it means **why this item is necessary to the selected historical or thematic argument**.

## 4. Headings

Headings should tell the reader the technical distinction, not merely repeat the product name.

Preferred:
- `LiveMem — contextを増やすのではなく、stateを残す`
- `Grok Build — modelではなくagent loopそのものを公開する`
- `Inference / Serving — 実装の現実とdisaggregationの条件`

Avoid generic headings such as `概要`, `詳細`, `評価` when a more informative contrast is available.

Use `sectionkicker` for classification/context, not as a second title and not as an internal editorial-status label.

## 5. Cover and front matter

The cover headline is chosen **after the main article set has been drafted**.

It should express a cross-issue pattern that is actually supported by multiple completed articles. It must not be decided first and then used to force unrelated candidates into a theme.

The cover may contain:
- one short editorial headline;
- one short deck explaining the issue-wide pattern;
- up to three anchor stories.

`This Week in AI` is also written after the body draft. It summarizes evidence-backed patterns that survived article construction.

For Special editions, use an equivalent post-draft synthesis appropriate to the edition rather than forcing weekly wording.

## 6. Event chronology vs trend chronology

Always distinguish:

- artifact/event date;
- issue-window relevance;
- community momentum date;
- post-cutoff follow-up when a cutoff applies.

Do not write a renewed trend as if it were a new release.

Preferred phrasing:
- `7月19日のPreviewがW32で再評価された`
- `7月31日の発表後、Cutoff直後にlocal workflow検証が増えた`

Avoid:
- `今週リリースされた` when the artifact was already available before the observation window.

### Weekly: why this week gate

A pre-window artifact may appear in a normal Weekly article only when the reader can be told **why it is relevant this week** in a concrete sentence.

A valid trigger may be, for example:

- a new release, weights, API or integration;
- new serving/local support;
- a material independent evaluation;
- a reproducible failure or security finding;
- a clear current-window technical-community momentum event;
- several current candidates revealing a structural trend for which an older artifact is necessary context.

If there is no defensible current-window trigger, do not frame the item as weekly newness. Move it to a `Deep Dive`, background/trend treatment, chronology, or Watchlist as appropriate.

`This Week in AI` may summarize a structural trend built from older artifacts, but must say that it is a trend visible from this week's candidate set rather than implying that every underlying artifact was released this week.

### Special: relevance gate

Special editions do not require a weekly trigger. Instead, every substantive item must have a clear role in the edition's declared coverage period or theme. Historical context should not be padded with unrelated milestones merely because they are famous.

## 7. Claim classes

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

## 8. Benchmarks and numbers

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

## 9. Open-weight / local-AI wording

Do not use `open`, `open source`, `open weight`, and `local` as interchangeable labels.

Separately record where relevant:
- whether weights are published;
- license;
- artifact size;
- supported serving engine;
- practical hardware / memory / storage requirements;
- whether a community experiment is reproducible or merely reported.

`Weights are public` does not imply `the model is practical on a workstation`.

## 10. Safety and security wording

Security stories require a clearly bounded threat/evaluation model.

Avoid sensational compression such as:
- `the model escaped the sandbox` when the source says internet access resulted from misconfiguration;
- `TDX is broken` when the demonstrated result is specific to an observable sparse-access channel;
- `Astra is Critical` when the source says Critical capability cannot yet be ruled out.

When multiple security papers are synthesized, state explicitly if they do **not** share the same cause or threat model.

## 11. Paper coverage

Distinguish:
- paper hypothesis;
- methodology;
- author-reported result;
- independently verified fact;
- limitation/generalization boundary.

Simulation studies must remain simulations in every headline and numerical summary.

A paper with an attractive headline result should not be promoted until the full/targeted review identifies the setup that makes the result true.

## 12. X Community Watch

The purpose is to show **what the technical community did next**, not to create a popularity ranking and not to expose the mechanics of the Grok collection workflow.

Useful reaction types include:
- reproduction;
- benchmark attempt;
- local deployment;
- workflow integration;
- artifact inspection;
- failure/limitation report;
- governance or deployment concern.

Reaction volume is not a sentiment census. Main-window and post-cutoff posts remain separate.

Published prose should say what was observed on X and what that observation means. Terms such as `Grok Reaction Pass`, collector pass names, file status, or collection TODOs belong in Source Notes / Repository provenance.

For retrospective period Specials, X/Grok collection is normally unnecessary. For thematic Specials it is optional and should be used mainly for recent community perception or reactions to a material event, not as the backbone of historical reconstruction.

## 13. Late Breaking

Late Breaking prevents post-cutoff information from contaminating the main chronology.

A Late Breaking item should:
- state that it is post-cutoff;
- explain why it matters to an already selected topic;
- avoid rewriting the earlier article as if the information were known at cutoff;
- avoid internal TODO language about what the production pipeline will do next.

### One substantive home per event

A single post-cutoff event should have **one canonical substantive treatment** in the edition, normally the dedicated Late Breaking package/section.

If the same event is relevant to another article:

- keep the other article to a short bridge or cross-reference;
- do not repeat the same mechanism, chronology, benchmark or implications at article length;
- retain the evidence link needed to support the bridge;
- put the detailed treatment in the canonical Late Breaking location.

This rule prevents a short Weekly issue from repeating one event several times while preserving contextual connections.

## 14. Watchlist / Chronology

Watchlist is a **reader-facing observation column**, not a view into editorial queue management.

A useful Watchlist item answers:

1. **現状** — what credible signal is currently observable;
2. **未確認** — what evidence or technical condition is still missing;
3. **注視点** — what future evidence/event would materially change the assessment.

Example:

```text
Qwen Image 3.0
現状: limited preview / integration signalを確認
未確認: 独立quality test、editing consistency、open-weight/local動向
注視点: 上記Evidenceが出た場合に再評価
```

Do not write reader-facing Watchlist copy as:

- `Candidate Inventoryへ残す`;
- `次号で昇格させる`;
- `候補として保存している`;
- `記事にできなかった情報の墓場`.

The Repository may preserve exactly those internal states; the published Watchlist should instead tell the reader what to watch and why.

Chronology remains objective event history. Watchlist is prospective uncertainty/observation. Do not use either as a dumping ground for rejected candidates.

## 15. Page budget

The page target is a planning constraint, not a quota.

Do not pad an issue with weak candidates merely to reach the target page count. A shorter evidence-dense issue is preferable to artificial balance or duplicated coverage.

Likewise, do not compress an important claim boundary solely to save a fraction of a page.

## 16. Source notes and provenance

Every published issue should preserve access from article claim back to:

`article -> citation -> candidate/evidence record -> primary/raw source`

Raw Grok output is never silently edited. Corrections and normalization belong in downstream evidence layers.

Rejected/incorrect candidates remain in the inventory when they are useful provenance for understanding detection errors or chronology corrections.

Source Notes may expose more detailed verification/provenance language than ordinary articles because their function is traceability. Keep that material visibly separated from the narrative body.

## 17. Final editorial gate

Before freezing an issue:

- citation-to-claim audit passes;
- chronology is consistent across sections;
- Main vs Post-Cutoff classification is intact when applicable;
- vendor/author metrics remain attributed;
- simulation/threat-model boundaries are visible;
- terminology is consistent;
- ordinary reader-facing prose contains no unexplained internal pipeline jargon or production TODOs;
- every pre-window artifact in a normal Weekly article has a defensible reader-facing `why this week` statement;
- each Late Breaking event has one substantive home, with other occurrences reduced to cross-references;
- Watchlist entries describe current signal / missing evidence / observation point rather than queue-management state;
- cover/theme is derived from the finished body;
- PDF builds without unresolved citations, missing glyphs or layout warnings;
- rendered pages receive a visual review.

For a Special edition, replace the Weekly-specific `why this week` check with `why this Special`: each substantive item must support the declared period/theme.

The editorial goal is a survey whose prose is readable, but whose claims remain traceable when scrutinized.
