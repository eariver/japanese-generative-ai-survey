# Muse execution — TS-002 Issue #533 final AnyGPT terminology cleanup

Status: `EXECUTION_AUTHORITY / BOUNDED_TERMINOLOGY_FINALIZATION / PUBLICATION_PREVIEW_STOP`

Date: 2026-09-26 JST

## Mission

Resolve the sole remaining reader-facing terminology item from Issue #533 after Sol read-back:

`ゼロショット素体` in BT-D096 / AnyGPT.

All other Issue #533 terminology changes are accepted and must remain stable.

Authoritative Sol review:

`sources/SP-beyond-text-2026/execution/sol-terminology-readback-issue533-r1-20260926.md`

The exact launch HEAD/tree and reviewed main HEAD/tree are supplied externally with the execution instruction. Verify all four read-only before any write. On any mismatch, make zero writes and report expected/actual.

## Allowed scope

Reader-facing BT-D096 terminology only, plus required ledger/validation/state regeneration.

Do not rerun Discovery, Screening, Evidence, Materiality, Completeness, Selection, or Architecture.

Do not perform new technical research.

Do not alter:

- numerical values,
- comparison targets,
- citations or citation keys,
- Evidence status/boundary,
- vendor/source attribution,
- section architecture,
- transition logic,
- any previously accepted Issue #529 depth repair,
- any already accepted Issue #533 terminology replacement outside the exact BT-D096 wording.

## Source-bound decision

AnyGPT's official repository explicitly distinguishes the **base model** and **chat model**, states that the base model aligns the four modalities for intermodal conversion, and lists zero-shot TTS among base-model capabilities.

Therefore the evidence-card shorthand `zero-shot base` is to be rendered as **the AnyGPT base model evaluated in a zero-shot setting**.

### Required normalization

In the exact current BT-D096 paragraph, replace the unnatural reader-facing `ゼロショット素体` / `素体のゼロショット値` wording with natural terminology preserving this subject.

Preferred forms:

- `報告条件のベースモデルのゼロショット評価では...`
- `ベースモデルのゼロショット設定も値と一体であり...`
- `ベースモデルのゼロショット結果を調整後の姿と混同しない。`

Minor grammatical adjustment is allowed only to make those sentences natural.

The intended meaning must remain:

`AnyGPT base model + zero-shot evaluation/setting`

Do not reinterpret this as a generic baseline, unspecified base, pretraining baseline, or chat/instruction-tuned model.

## Terminology ledger

Update:

`sources/SP-beyond-text-2026/execution/terminology-issue533/terminology-decision-ledger.json`

and its Markdown view so that `ゼロショット素体` changes from:

`ESCALATE`

to:

`REPLACE`

with final count:

`2 -> 0`

and rationale bound to AnyGPT base-model terminology.

No other ledger decision may be changed unless mechanically required by this exact correction.

## Invariants

Re-run and prove:

- `\\autocite{...}` block count unchanged,
- citation-key multiset unchanged,
- number/unit token multiset unchanged,
- section/subsection order and labels unchanged,
- 139/139 citation coverage unchanged,
- Evidence status and PARTIAL/NEEDS_MORE boundaries unchanged,
- vendor and closed-system boundaries unchanged,
- `references.bib` byte-identical,
- all previously-cleaned Issue #533 high-confidence terms remain at zero,
- `ゼロショット素体` becomes zero in `main.tex` and rendered PDF.

## PDF / validation

Rebuild the exact PDF and rerun:

- deterministic manuscript validation,
- semantic/editorial validation,
- reader-surface validation,
- citation completeness,
- terminology scan,
- all-page visual regression,
- overflow/clipping/broken-glyph/blank-page scan,
- bibliography rendering regression.

Page count may change only as a layout consequence; do not optimize for page count.

## Completion report

Record:

- starting/final HEAD and tree,
- main guard,
- exact files changed,
- three BT-D096 before/after phrases if three related phrases are present,
- ledger decision/count update,
- invariant results,
- exact PDF page count and SHA-256,
- visual regression result,
- final terminology scan,
- final Core state / Human Gate.

## Stop

Normal stop:

`PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`

or the exact current-Core equivalent.

Do not fabricate Human approval.

Freeze / Release / merge / release-record remain prohibited.

Use only the existing branch. No new/fallback/repair/review branch. No force push, reset, rebase, or history rewrite. Normal commit + non-force fast-forward push only.
