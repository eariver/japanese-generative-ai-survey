# Muse execution — TS-002 Issue #533 final residual r3

Status: `EXECUTION_AUTHORITY / ONE_TERM_PLUS_LEDGER_VIEW_SYNC / PUBLICATION_PREVIEW_STOP`

Date: 2026-09-26 JST

Authoritative Sol review:

`sources/SP-beyond-text-2026/execution/sol-terminology-readback-issue533-r2-20260926.md`

The exact launch work HEAD/tree and reviewed main HEAD/tree are supplied externally. Verify all four read-only before any write; on any mismatch make zero writes and report expected/actual.

## Mission

Complete Issue #533 by repairing exactly two residuals found in Sol read-back:

1. one remaining reader-facing `素体値` phrase in the BT-D096 / AnyGPT paragraph;
2. stale Markdown view `terminology-decision-ledger.md`, which still shows the pre-resolution ESCALATE state although canonical JSON is already correct.

Everything else from Issue #529 and Issue #533 is accepted and must remain stable.

## Allowed reader-facing change

In the exact active AnyGPT paragraph, replace:

`素体値の比較は条件固定の差として読む。`

with:

`ベースモデルのゼロショット結果の比較は条件固定の差として読む。`

or a grammatically equivalent wording preserving exactly:

`AnyGPT base model + zero-shot result + condition-bound comparison`

Do not change any neighboring number, benchmark, comparison target, citation, source-bound limitation, or claim.

After replacement, reader-facing `素体` must be 0 occurrences in `main.tex` and rendered PDF.

## Ledger Markdown synchronization

Canonical JSON ledger is already authoritative and correct for the AnyGPT item:
- decision `REPLACE`
- final term bound to AnyGPT base-model zero-shot evaluation/setting/results
- before `2`
- after `0`

Synchronize only the Markdown view:

`sources/SP-beyond-text-2026/execution/terminology-issue533/terminology-decision-ledger.md`

Required effects include:
- remove stale `ESCALATE: 1` if no other ESCALATE entries remain;
- update `ゼロショット素体` row from `2 -> 2 / ESCALATED` to `2 -> 0 / REPLACE` with the source-bound AnyGPT base-model rationale;
- update the `Additional candidates` summary so it no longer says this item is escalated.

Do not change other ledger decisions.

## Scope prohibitions

No new research.
No Discovery / Screening / Evidence / Materiality / Completeness / Selection / Architecture rerun.
No broad terminology pass.
No semantic depth changes.
No new authority.
`references.bib` must remain byte-identical.

Do not fabricate a Human approval. Use the existing Issue #533 revision authority only as permitted by the current Core. If the current Core requires a new Human decision that is not already authorized by the existing Issue #533 repair flow, stop and report rather than inventing one.

## Required invariants

Prove before/after:
- `\\autocite{...}` sequence unchanged;
- citation-key multiset unchanged;
- number/unit token multiset unchanged;
- section/subsection order, labels, kickers unchanged;
- 139/139 citation coverage unchanged;
- Evidence statuses and PARTIAL/NEEDS_MORE unchanged;
- vendor/closed-system boundaries unchanged;
- Issue #529 depth unchanged;
- previously cleaned Issue #533 terms remain zero;
- `素体` becomes zero in reader-facing `main.tex` and rendered PDF;
- canonical JSON ledger remains semantically unchanged except mechanically generated metadata only if unavoidable;
- Markdown ledger and JSON ledger agree for the AnyGPT decision/count.

## PDF and validation

Rebuild the exact PDF if manuscript changes require it and rerun the publication-local deterministic, semantic/editorial, reader-surface, citation, terminology, and visual checks required by the current production contract.

Inspect the AnyGPT page and any pagination-shifted neighboring pages. No clipping, overflow, broken glyphs, systematic blank pages, or bibliography regression.

## Completion report

Record:
- starting/final HEAD + tree;
- main guard;
- exact changed files;
- exact before/after reader phrase;
- `素体` count before/after in source and rendered PDF;
- JSON-vs-Markdown ledger agreement;
- semantic/citation/number invariants;
- PDF pages + SHA-256;
- visual result;
- final Core/Human Gate state.

## Stop

Normal stop:

`PUBLICATION_PREVIEW / AWAITING_HUMAN_PUBLICATION_PREVIEW_DECISION`

Freeze / Release / merge / release-record remain prohibited.

Existing branch only. No new/fallback/repair/review branch. No force push, reset, rebase, or history rewrite. Normal commit + non-force fast-forward push only.
