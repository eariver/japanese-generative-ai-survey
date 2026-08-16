# Retrospective Special Backfill Bootstrap

Status: stable cross-session bootstrap contract  
Updated: 2026-08-16

## Purpose

This file provides a lightweight historical-backfill entrypoint. The canonical general startup contract is `docs/special-session-bootstrap.md`; current `main` repository state is the source of truth.

This file is intentionally not a per-edition progress ledger. It does not record a `next edition`, a `latest completed edition`, or a `latest handoff`, and it does not need to be updated when each Special is completed.

## Target selection contract

The target period is supplied explicitly by the user's task prompt and resolved against `config/special-pipeline.json`.

Examples:

- `2026-M03 Special` -> `SP-2026-M03`
- `2025-H2 Special` -> `SP-2025-H2`
- `2024-H1 Special` -> `SP-2024-H1`
- `2023-Y Special` -> `SP-2023-Y`

Do not infer the target from the most recently completed Special, gaps in history, previous chat state, or an older edition's cadence.

The exact configured coverage window is authoritative. Historical granularity and valid slugs come from `config/special-pipeline.json`; `docs/special-editions.md` explains the policy but does not override configuration.

## New-session bootstrap

When asked to start or continue a historical Special:

1. Read current `main`, `AGENTS.md`, and `docs/special-session-bootstrap.md`.
2. Resolve the requested target from `config/special-pipeline.json`.
3. Inspect `specials/<slug>/edition.json`, `sources/SP-<slug>/pipeline-state.json`, survey source, init/work branches, and relevant PRs.
4. If the edition already exists, resume from repository-recorded lifecycle/provenance.
5. If it does not exist, treat the user's start request as authorization for deterministic initialization: create/validate the init state, merge the init PR, create the work branch, and continue without asking for a separate confirmation.
6. Follow the applicable period guide; half-year editions additionally use `docs/half-year-retrospective-specials.md`, and annual editions additionally use `docs/annual-retrospective-specials.md`.
7. Proceed autonomously through non-Human-Gate stages and stop at the requested Human Gate.

## Human Gate contract

Normal Special production has only two user-interaction gates:

1. **Architecture Review** — after Candidate Selection (internal checkpoint) and Architecture Proposal;
2. **Publication Preview** — approval of the exact PDF identity.

Initialization and Candidate Selection are not Human Gates. After Publication Preview approval, Visual Review recording, Freeze, work-PR merge, exact-byte verification, and public Release are deterministic authorized transitions for the approved PDF bytes.

An Exception Gate is raised only for a genuinely new editorial/publication decision under `docs/special-human-gates.md`. Retryable collection/CI failures or other deterministic recovery do not create a Human Gate.

## Production invariants

These expectations apply regardless of historical period:

- Source Intake / Screening / Evidence provenance is retained and SHA-bound.
- Candidate Selection is an auditable internal checkpoint reviewed with Architecture.
- Architecture and story taxonomy are derived from the requested period's Evidence rather than copied from a later edition.
- Preview candidates pass current claim/chronology, period, reader-facing taxonomy, layout, TeX/log, and render-first Visual QA controls before Publication Preview.
- Technical Notes use current reader-facing taxonomy and tail policy.
- Pre-release review findings are repaired through immutable derived source revisions and re-built/re-reviewed.
- Public Release identity is issue-only: `special/<slug>`.
- Internal source revisions are provenance only and are not public Release versions.

## Progress discovery

Do not maintain a duplicated completed-edition list in this file.

Derive progress from repository state:

- edition manifests under `specials/` identify initialized editions;
- `sources/SP-<slug>/pipeline-state.json` identifies authoritative lifecycle state;
- a `FROZEN` state plus the corresponding issue-only GitHub Release identifies a completed published edition.

This keeps new sessions correct even when editions are produced out of chronological order.
