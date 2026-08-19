# Automotive E/E experiment: post-Architecture findings

Status: **EXPERIMENTAL / Publication Preview self-review completed / production AI pipeline unchanged**

This note records findings obtained after the Automotive E/E thematic experiment passed Architecture Review and was carried through drafting, rendering, Publication Preview preparation, and a self-review of the generated reader-facing artifact.

It complements `GENERALIZATION_FINDINGS.md`, which records the Source Intake through Architecture findings. This document focuses on what became visible only after an approved architecture was turned into real article drafts and a PDF.

The repository's primary product remains the Japanese generative-AI survey. Nothing in this note authorizes weakening or replacing the existing AI-specific production behavior.

## 1. Architecture approval exposed a new semantic distinction: synthesis timing vs. synthesis placement

Architecture v0.3 was approved with one explicit editorial condition:

> Place an independent synthesis at the end of the body, immediately before References.

The existing Special finalization path already had a post-draft synthesis concept, but production code couples two separate concepts:

- **when** issue-level synthesis is generated: after article drafts stabilize;
- **where** that synthesis is rendered: front matter / `Monthly Signals`.

The Automotive issue needed the same *timing* but a different *placement*.

### Finding D1

`post-draft synthesis` is reusable editorial machinery, but its generation timing and reader-facing placement must be separate edition/profile concepts.

Do not rename or remove the current AI behavior yet. A future profile should be able to say, for example:

```text
synthesis_generation_stage = POST_DRAFT
synthesis_placement = FRONTMATTER | END_OF_BODY | BOTH | NONE
```

while the existing AI Special profile retains its current front-matter behavior by default.

## 2. An end-of-body synthesis can remain inside the shared Article Draft contract

An initial Architecture package for the synthesis had no direct Evidence inputs. That would have allowed the conclusion to become reader-visible while being effectively outside the normal article claim/evidence validator.

The safer solution was not to invent a new synthesis document format. Instead, P08 was bound to representative already-selected Evidence from the preceding architecture lanes and kept as a normal `SECTION` / `ARTICLE_DRAFTING` package.

Representative inputs cover:

- zonal / central-compute responsibility split;
- TSN / Ethernet network fabric;
- VSS / service-data contracts;
- S-CORE/open-platform maturity;
- lifecycle / CI-CD validation infrastructure;
- mixed-criticality / ASIL constraints.

The reader-visible architecture did not change; only the evidence binding was strengthened.

### Finding D2

A synthesis that makes substantive technical conclusions should preferably remain inside the same evidence-linked Article Draft contract as ordinary body sections.

Issue-level synthesis should not automatically imply a weaker provenance contract.

## 3. Shared Article Draft validation survived the Automotive domain

The following production implementation concepts were reusable without domain weakening:

- immutable Draft Package binding;
- prompt SHA binding;
- per-block stable Evidence references;
- `PRIMARY_FACT`, attributed claim, inference, limitation semantics;
- exact `must_cover` coverage declarations;
- exact boundary coverage declarations;
- requirement that all Architecture-included Evidence Tasks are materially used;
- structured block types;
- deterministic Evidence-to-bibliography resolution;
- URL-hash-derived bibliography keys.

P01-P08 were checked against the shared `scripts/validate_article_draft.py` contract after package/prompt SHA binding and passed 8/8 in the experiment review environment.

### Finding D3

The Article Draft *contract* is substantially domain-neutral. Domain specificity is concentrated in:

- the drafting prompt;
- package editorial angles;
- domain Evidence ontology and evidence selection;
- issue-level assembly.

This is a stronger result than the Architecture-only experiment could prove.

## 4. Reader-facing methodology is not the same thing as internal provenance terminology

The first rendered Automotive PDF exposed internal pipeline vocabulary in reader-facing text, including terms such as:

- Source Intake;
- Screening;
- Evidence Task / Evidence Card;
- Candidate Matrix;
- CANDIDATE / HOLD / INSPECT_MORE.

Those terms are valuable for repository auditability but are not necessarily appropriate publication language.

The existing finalization guard only blocks a small fixed set of workflow tokens. A domain that explicitly explains methodology can therefore accidentally publish implementation jargon even while technically passing the current internal-term check.

### Finding D4

The repository needs a conceptual boundary between:

1. **internal provenance vocabulary** — exact pipeline/state-machine terminology;
2. **reader-facing methodology vocabulary** — stable editorial language such as `source collection`, `screening`, `primary-source verification`, `selection`, and `evidence boundary`.

A future generalization should not simply expand a blacklist indefinitely. Prefer a profile-owned reader-facing methodology vocabulary or explicit publication transform.

## 5. Domain coverage quality cannot be inferred from generic evidence completeness

The Automotive pipeline achieved complete task accounting and strong Evidence validation, yet the Publication Preview still had an editorial coverage weakness:

- AUTOSAR official primary-source coverage remained incomplete because of TLS retrieval failures;
- ISO normative text remained unavailable;
- production OEM/Tier1 E/E implementation evidence was comparatively thin;
- academic, OSS, and consortium sources were correspondingly overrepresented.

Generic checks correctly prevented fabricated replacement claims, but they could not answer the domain question:

> Is this source mix sufficient to call the result a credible 2023-2026 Automotive E/E architecture survey?

### Finding D5

Cross-domain reuse requires a **domain-specific coverage gate**, separate from deterministic task completeness.

For Automotive E/E, candidate coverage dimensions include:

- standards/specifications;
- reference/open implementations;
- peer-reviewed/research evidence;
- OEM deployment/architecture disclosures;
- Tier1/platform disclosures;
- networking;
- compute/isolation;
- service/data/runtime;
- lifecycle/validation;
- safety/security.

Missing mandatory coverage should force `RESEARCH_GAP` or equivalent rather than being silently compensated by more papers.

## 6. Retrieval failure policy should distinguish tolerable unknowns from mandatory-source gaps

The experiment correctly failed closed on TLS/access errors: no insecure TLS fallback and no bypass of restricted ISO material was used.

However, Publication Preview review showed that not every unresolved source should have the same editorial consequence.

Examples:

- unavailable detailed normative clause: may remain an explicit limitation;
- inability to retrieve the principal current AUTOSAR architecture material for an Automotive architecture survey: likely requires an alternate legitimate acquisition route or renewed research before publication.

### Finding D6

`retrieval gap` and `coverage-blocking gap` are different concepts.

A future profile should be able to mark source families as:

```text
OPTIONAL
EXPECTED
REQUIRED_FOR_PUBLICATION
```

without changing the secure transport policy.

## 7. Page budgets are editorial envelopes, not rendered-page quotas

Architecture v0.3 retained a 48-page target / 64-page maximum inherited from the planning exercise. The first real two-column PDF rendered to 15 A4 pages.

Initial reaction was that the issue was too short. Comparison with existing Special source density showed that the Automotive body was already materially denser than several existing AI Special section sets; expanding to 48 pages merely to match the planning number would have encouraged padding rather than better editorial content.

### Finding D7

Architecture `page_target` should be interpreted explicitly as one of:

- rendered-page target;
- relative editorial weight;
- planning envelope / maximum allocation.

The current field conflates these meanings. For the existing AI pipeline, retain current semantics. For thematic/retrospective profiles, make the interpretation explicit before using it as a quality gate.

## 8. Technical surveys benefit from figure requirements that are currently absent from the contract

The Automotive preview was textually coherent but contained no architecture diagrams. For a domain whose central argument is the redistribution of boundaries among physical topology, compute, network, contracts, lifecycle, and assurance, this is a significant communication weakness.

Useful figures identified by self-review:

1. the issue's five/six-layer responsibility-boundary model;
2. physically zonal vs. computationally centralized topology;
3. TSN Ethernet / 10BASE-T1S / CAN XL role separation;
4. service/data/runtime contract stack;
5. optional lifecycle/validation feedback loop.

### Finding D8

Figure need is an editorial/profile concern that should be decided at Architecture, not discovered only in Visual Review.

A future Architecture package may need fields such as:

```text
visual_required = true|false
visual_intent = "..."
visual_evidence_basis = [...]
```

without making visuals mandatory for every AI weekly article.

## 9. Bibliography expansion is a structural consequence of release-series evidence

The preview contained 46 unique bibliography sources and References consumed a large fraction of the rendered pages.

This was not primarily caused by duplicate citations. VSS, vSomeIP, S-CORE and similar Evidence series intentionally preserve multiple release/event sources, which the deterministic renderer then exposes as separate bibliography entries.

### Finding D9

Series Evidence needs a publication-layer citation policy distinct from evidence-layer provenance.

The Evidence graph may need all release URLs for auditability while the reader-facing bibliography may reasonably group them under one chronology/source-series note, provided the mapping back to exact sources remains lossless in machine-readable provenance.

Do not deduplicate away evidence provenance merely to shorten References.

## 10. Passing structural validation does not equal semantic claim review

The Article Draft validator correctly checks:

- reference existence;
- Evidence class / attribution-mode compatibility;
- required task usage;
- coverage declarations;
- package/prompt binding.

It cannot fully determine whether one paragraph rhetorically overstates the combined meaning of multiple correctly referenced facts/claims/inferences.

The end-body synthesis is particularly exposed because it intentionally recombines evidence from multiple lanes.

### Finding D10

Publication readiness needs a distinct **semantic claim review** after structural Article Draft validation.

Candidate checks:

- inference language is visibly inferential;
- attributed claims are not converted into narrator voice;
- standards status is not converted into deployment proof;
- prototype/lab evidence is not converted into production validation;
- multiple Evidence refs do not create a stronger aggregate claim than any supported synthesis permits.

This should remain a human/editorial or higher-level review gate, not be pretended to be solved by the deterministic validator.

## 11. Publication source bundles need a stronger reproducibility contract

The self-review found a concrete packaging defect: `preview-manifest.json` draft hashes did not match the structured draft files included in the source bundle.

The likely cause is a semantic mismatch between hashes of:

- submitted interactive bodies;
- accepted drafts after `basis` / `runner` binding;
- rendered article inputs.

The PDF and source ZIP top-level hashes were internally consistent, but the per-article manifest semantics were ambiguous/wrong.

Additional packaging weaknesses found:

- source bundle did not include all immutable Draft Packages / Evidence Cards needed for full standalone revalidation;
- checksum listing contained environment-specific absolute `/mnt/data/...` paths;
- PDF metadata title/subject was incomplete.

### Finding D11

Publication artifacts need explicit typed hashes rather than generic `draft_sha256` fields.

Prefer names such as:

```text
submitted_body_sha256
accepted_article_draft_sha256
draft_package_sha256
rendered_tex_sha256
rendered_bib_sha256
pdf_sha256
```

A preview source bundle should either:

- be **self-contained**, including all immutable verification inputs; or
- explicitly be **repository-bound**, recording exact branch/commit/path/SHA dependencies.

Do not claim standalone reproducibility when the bundle is only partially self-contained.

## 12. Publication assembly remains one of the strongest AI/edition-specific seams

Production Special finalization contains reader-facing AI/monthly assumptions such as:

- `Monthly Signals`;
- fixed retrospective wording tied to a specific AI monthly edition;
- cover/synthesis layout assumptions.

Reusing that finalizer unchanged for Automotive would have produced incorrect publication text even though many lower-level validators were reusable.

The experiment therefore treated Automotive issue-level assembly as experiment-owned while reusing lower-level rendering semantics.

### Finding D12

The currently proven reusable core ends *before* issue-level publication assembly.

A safe future split is:

```text
shared
  article validation
  citation resolution
  article block rendering primitives
  bibliography provenance mapping
  generic PDF/build mechanics

edition/profile owned
  cover language
  front-matter methodology
  synthesis placement
  section-order assembly
  references presentation policy
  edition descriptor
  issue-level source manifest fields
```

## 13. Actions orchestration is not part of the editorial core

During Automotive drafting, push-triggered experimental GitHub Actions runs were unreliable. The underlying structured validation could still be reproduced locally against the current branch's production validator contract.

This did not justify weakening validation, but it exposed an important distinction:

- editorial correctness / deterministic validation contract;
- remote orchestration / workflow trigger reliability.

### Finding D13

CI orchestration should prove and automate the deterministic contract, not define the contract itself.

A failed or missing Actions trigger is an automation incident. It should not force editorial logic changes or make otherwise reproducible deterministic validation impossible.

For publication, however, the authoritative acceptance path should eventually return to a repository-recorded, reproducible CI or equivalent controlled execution so provenance is not dependent on an interactive session.

## 14. Current end-to-end abstraction boundary

After Source Intake → Screening → Evidence → Selection → Architecture → Drafting → Rendering → Preview self-review, the empirically supported boundary is now:

```text
shared deterministic / reusable core
  ├─ collection transport primitives
  ├─ Raw provenance and hashing
  ├─ Screening record/batch mechanics
  ├─ Screening result structure
  ├─ Evidence Task construction
  ├─ Evidence graph/invariant validation
  ├─ source/evidence class semantics
  ├─ Candidate Matrix mechanics
  ├─ Candidate Selection safety roles
  ├─ Architecture coverage/boundary accounting
  ├─ Draft Package binding
  ├─ Article Draft structural validation
  ├─ Evidence -> citation resolution
  └─ article-level TeX/Bib rendering primitives

profile / domain / edition context
  ├─ time-window and issue semantics
  ├─ source families and mandatory coverage
  ├─ source INDEX/ITEM role
  ├─ Screening relevance/theme taxonomy
  ├─ artifact ontology
  ├─ verification prompt
  ├─ theme continuity
  ├─ page-budget semantics
  ├─ synthesis timing and placement
  ├─ reader-facing methodology vocabulary
  ├─ visual/figure requirements
  ├─ bibliography presentation policy
  ├─ cover/front-matter copy
  └─ issue-level assembly

human/editorial review layer
  ├─ domain coverage sufficiency
  ├─ semantic claim strength
  ├─ visual communication quality
  ├─ publication jargon leakage
  ├─ bibliography usability
  └─ final preview approval

not yet proven safe to generalize
  ├─ canonical production lifecycle persistence
  ├─ generic issue-level finalizer
  ├─ generic freeze/release semantics
  └─ merge/release of a non-AI product from this repository
```

## 15. Concrete self-review findings on Preview v0.1

The first reader-facing preview should **not** be treated as ready for approval without revision.

### Blocker

- Preview source-manifest per-draft hashes do not match the structured draft files included in the bundle. Manifest semantics or packaging generation must be repaired.

### High

- Internal workflow vocabulary leaks into reader-facing methodology text.
- Automotive industry coverage is too dependent on papers/OSS/consortia; AUTOSAR primary material and OEM/Tier1 production evidence need renewed attention.

### Medium-high

- No architecture figures despite a strongly relational/structural thesis.

### Medium

- References occupy a disproportionate fraction of the PDF because release-series provenance maps one-to-one into bibliography entries.
- Semantic claim review is still required after structural validation.
- Source bundle is not fully self-contained for independent revalidation.

### Low-medium / low

- absolute local paths in checksum manifest;
- incomplete PDF metadata;
- occasional awkward English hyphenation in two-column Japanese layout.

## 16. Guardrails for the next revision

1. Repair provenance/package hash semantics before changing prose.
2. Preserve all existing Evidence boundaries while revising reader-facing wording.
3. Re-open research only for identified domain coverage gaps; do not casually expand scope.
4. Prefer legitimate alternate official access routes for required-source gaps; never disable TLS verification or bypass access controls.
5. Add figures only from already-supported concepts or newly verified source material.
6. Do not shorten References by destroying machine-readable source provenance.
7. Keep P08 as the explicit end-of-body synthesis before References.
8. Do not modify the production AI profile/pipeline merely to make the Automotive issue convenient.
9. Re-run structural validation, semantic review, build, and visual review after revisions.
10. Publication Preview approval remains a human gate.

## 17. Main lesson

The experiment does **not** support the conclusion that this repository should become a generic survey framework.

It supports a narrower and safer conclusion:

> The existing AI survey has a surprisingly broad deterministic technical-survey core, but publication-quality reuse depends on extracting domain/edition profiles around coverage sufficiency, synthesis placement, reader-facing methodology, visual requirements, bibliography presentation, and issue-level assembly — while leaving the AI product authoritative by default.

The post-Architecture experiment was essential because several of the most important generalization seams were invisible until a real non-AI PDF existed and could be reviewed as a publication rather than as pipeline data.
