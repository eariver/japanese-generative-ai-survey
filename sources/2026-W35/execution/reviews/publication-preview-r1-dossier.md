# Human-facing Publication Preview dossier — 2026-W35 r1

Sol-owned review surface for the pending Human Publication Preview r1. Read with the exact committed Candidate-bound PDF. No Publication Preview decision is recorded in this run.

## 1. Exact review identity

- Edition `2026-W35` r1, WEEKLY + WEEKLY_MAGAZINE.
- Reviewed production commit SHA: `d1d6bdc6733b57013eb0dc6a06e97310dbfa74ac` (W35-branch commit containing exact State + Candidate + Candidate-bound PDF).
- Lifecycle `RELEASE_CANDIDATE`, next action `PUBLICATION_PREVIEW`, terminal `HUMAN_GATE_REACHED`.
- Canonical window unchanged: `[2026-08-21T18:00:00-04:00, 2026-08-28T18:00:00-04:00)` ET.
- Production Line `production/survey-core-v2 @ 774dd39a` (unchanged); reviewed `main @ 774dd39a`; no Core repairs.

## 2. Architecture approval provenance

- Architecture Review r1: `REQUEST_CHANGES` (boundary `SELECTION_COMPLETE`, reviewed `676160e3`).
- Architecture Review r2: `APPROVED` (revision 2, reviewed `7692f618488fe27bf298a7a90648a009ae9b0ffb`, recorded `2026-09-15T12:53:29Z` by Human Owner).
- Immutable records: `gates/reviews/architecture-r1.json`, `gates/reviews/architecture-r2.json`, snapshot `gates/reviews/approvals/architecture-r2.json`, canonical `gates/architecture-approval.json`.
- Approved Architecture unchanged through drafting/publication (5 packages, 17 SELECTED / 2 HOLD, corrected thesis/P1 framing).

## 3. Final package/section structure

1. Open weights go architectural → `sections/10-open-efficient-turn.tex`
2. The agent coding plane reorganizes → `sections/20-agent-coding-plane.tex`
3. Flagship claims and their bounds → `sections/30-flagship-receipts.tex`
4. Serving economics and the regional open frontier → `sections/40-infra-regional.tex`
5. Safety evidence and governance contrast → `sections/50-safety-governance.tex`
6. Week in Review synthesis (no new facts) → `sections/60-week-in-review.tex`

Frontmatter (`00`) + Sources & limitations (`99`) + `references.bib` (17 authorities) + `jgaisurvey.sty`.

## 4. Page count and layout

- PDF: `surveys/weekly/2026-W35/main.pdf`, 8 pages, 285365 bytes, unencrypted.
- SHA-256: `6115f0a774a947a269426c46003d09c9e4f962f54d5043d3778a5b815591a1b2`.
- CI `build-weekly-survey` run `34972809068` success; final-log warning gate PASS (no undefined refs, no overfull/underfull, no missing characters).
- 8 pages is within normal weekly range; per instruction, ordinary length is not a blocking factor. No severe layout failure, gross duplication, or unreadable density observed (text extraction clean, Japanese renders).

## 5. Evidence-boundary carry-through

- P1: per-model ratios only (GLM 18B/320B ~5.6%, Qwen ~6B/125B ~4.8% Qwen-specific, Hy4 ~49B/770B ~6.4%); licenses per-model UNRESOLVED; preview statuses explicit; no cluster-wide activation/license/offload claim; Qwen 4 not released; benchmarks vendor-only; X as community signal only.
- P2: AHP portable surfaces + pre-1.0 bound; Origin scope/sync + outage coincidence (not causation) + policy gap unresolved; Copilot-Teams preview + retained PR controls; Harness vendor-issued scale; grith mechanism + Linux-only gaps.
- P3: Fable 5 GDPval-AA + AnalystAgent caveat + Mythos-as-framing; GPT-5.6 Kiro + 82% vendor-claimed; density list excluded.
- P4: vLLM highlights/models/breaking/security as shipped (perf project-reported); OpenThai release/license/vendor numbers/published losses (numerics vendor-measured).
- P5: autoalign results + cheating disclosure + stated limits (no production claim); MIIT scope + ~200 + no-threshold caveat; Korea 3+7 + nonbinding + weak-force reception; contrast never equivalence.
- HOLD items (Video-IFBench, HUG-VIS) outside Architecture; background records not promoted.

## 6. Reader-surface lexical/semantic results

- Lexical scan: 10/10 TeX/Bib files PASS, zero blocking findings; structured pre-TeX surface 0 findings.
- Pre-TeX semantic review: `publication/v2/reader-surface-semantic-review-v2.json` PASS (pipeline independence + bounds + community + closure).
- Reader-surface gate: `publication/v2/reader-surface-gate-v2.json` PASS.
- Post-TeX semantic/editorial review: `publication/v2/semantic-editorial-review-v2.json` 11/11 PASS (genuinely read against exact source/PDF/Drafts).
- Visual review: `publication/v2/visual-review-v2.json` 2/2 PASS (exact-PDF QA: 8 pages, headings/tables/boundaries/bibliography present).
- Quality bundle: `publication/v2/quality-regression-bundle-v2.json` 3/3 deterministic PASS.
- Stage validations: draft, reader-publication, candidate all PASS; checkpoints `ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, `VALIDATED_DRAFT` recorded.

## 7. Known non-blocking residual limitations

- P1 anchors remain relayed-secondary bounds (Z.ai/Qwen/Tencent/IBM primaries + HF cards pending); carried explicitly in prose and source notes.
- Image/audio lanes thin (no window material candidate); paper records abstract-level; carried in source notes.
- Thai-specific claims evaluable only via vendor account; carried explicitly.
- Page allocation was a drafting concern; 8-page result retains all selected material with no content dropped.

## 8. Material deviations from approved Architecture

- None. Package order, membership, roles, thesis, must-cover requirements, and boundaries preserved. No Selection/Architecture change after r2 approval. Two minimal TeX-level normalizations only (none altered Draft authority): none required beyond initial authoring; CI passed on first build.

## 9. Exact PDF authority

- Path: `surveys/weekly/2026-W35/main.pdf`
- SHA-256: `6115f0a774a947a269426c46003d09c9e4f962f54d5043d3778a5b815591a1b2`
- Bytes: `285365`, pages: `8`, encrypted: `false`
- Candidate: `sources/2026-W35/publication/v2/publication-candidate-v2.json` (candidate SHA `3195f74c89a3c8e163f0f29cc0123132ecedd287f84c1467d9110d40167e2e8d`)
- Source: `surveys/weekly/2026-W35/main.tex` (`00d109cc…`, 1307 bytes + 8 sections + bib + style)

## 10. Human decision options (only now)

- `APPROVED` — record against the exact reviewed commit; continue to Freeze (not in this run).
- `REQUEST_CHANGES` — supply requested changes + one allowed boundary (`ARCHITECTURE_ESTABLISHED`, `DRAFT_COMPLETE`, or `VALIDATED_DRAFT` for publication-local; earlier boundary for upstream defect with cross-gate reopen).

---

## Reviewed authority

Same as §1 above; canonical machine Candidate: `sources/2026-W35/publication/v2/publication-candidate-v2.json`.

## Human decision

`PENDING` — none recorded. Valid: `APPROVED` / `REQUEST_CHANGES` only.

## Requested changes

None (no Preview review performed yet).

## Regeneration boundary

None selected (no Preview review performed yet).

## Shared-Core implication

One Core-contract observation (not a defect repair in this run): the experimental `survey_weekly_semantic_publication_v2.py` renderer currently requires `publication_extensions.closing_summary` + non-empty synthesis `publication_payload`, while the canonical architecture builder and WEEKLY_MAGAZINE contract require neither (empty allowed). Production used the canonical manual-authoring + reader-binder path (as in W33/W34), not the experimental renderer. No shared-Core edit made; recorded here for Core-maintenance awareness only.
