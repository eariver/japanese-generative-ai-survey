# W43 Sol → Muse r1 — bounded Source Intake / Discovery execution contract

Status: `SOL_EDITORIAL_DISPATCH / INITIALIZED / BOUNDED_TO_DISCOVERY_COMPLETENESS_REVIEW`
Date: 2026-10-24 JST
Repository: `eariver/japanese-generative-ai-survey`
Edition: `2026-W43`
Canonical branch: `weekly/2026-W43-v2-work`

## 1. Authority and trust baseline

- This is an edition-local Sol editorial Worker instruction, **not** a Core v2 operator request, Human Gate approval, or permission to modify shared Core.
- Reviewed `main` (must check remote read-only): `041a08dfef3112643cbf85b4a86a7b6f9128aed6`, root tree `a134dc36a407d08ab1de416324229b3955e0325a`.
- Frozen Core line (must check remote read-only): `production/survey-core-v2` at `774dd39a951c9ac3818e83dfffd4c7666efb0a20`, root tree `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.
- Verified canonical initialization output BEFORE this dispatch file: HEAD `c77f3ec65c8ea871f2ca503942bd266e3a8bab06`, root tree `140565ae1c824029477ce14a6f992f96a18a3b40`.
- Initializer request: `sources/2026-W43/execution/requests/w43-r0-initialize-weekly-20261024.json`; trusted bridge run `40088008699` and receipt `sources/2026-W43/execution/bridge-runs/w43-r0-initialize-weekly-20261024/receipt.json` (`PASS`).
- **Execution starting HEAD and Tree are the exact post-dispatch commit/tree supplied by Sol alongside this file**. Verify the remote branch equals both values read-only before any write. This document's pre-dispatch initialization HEAD is a historical checkpoint, NOT a substitute for dispatch HEAD.
- If any expected HEAD/Tree/main/Core identity differs, report expected vs actual and stop with **ZERO WRITES**. Do not create alternate/fallback/repair/review branches, reset, rebase, force-push, rewrite history, or bypass the trusted operator bridge.

## 2. Scope and stopping boundary

Execute ONLY canonical W43 Source Intake/Discovery and supporting edition-local execution/audit records. Target state after accepted canonical discovery advancement: `DISCOVERY_COLLECTED`; do not enter Screening, Evidence, Selection, Architecture, or any Human Gate. If a required Source Intake input or trusted bridge is unavailable, preserve honest partial artifacts and stop without claiming canonical `DISCOVERY_COLLECTED`.

Stop token: `SOL_DISCOVERY_COMPLETENESS_REVIEW_READY` (or `BLOCKED` with exact reproducible reason). Sol owns the independent negative-space and coverage review before any next-stage execution.

## 3. Period and event chronology

- Immutable issue window: New York `[2026-10-16 18:00 EDT, 2026-10-23 18:00 EDT)`; UTC `[2026-10-16T22:00:00Z, 2026-10-23T22:00:00Z)`; JST `[2026-10-17 07:00, 2026-10-24 07:00)`.
- End is EXCLUSIVE. Time-window inclusion is based on the relevant EVENT's first verified appearance, not the later time the page was scraped.
- Separate original paper publication, repository first-public commit, tagged release, model-weight availability, API availability, model/system-card revision, official announcement, independent reproduction, and benchmark snapshot timestamps. Record date-only uncertainty honestly.
- Older work may enter as explicitly classified background or carry-over; never relabel earlier work as W43 news.

## 4. Research/source lanes: broad first pass, no early Selection compression

At minimum cover: (a) frontier and major AI labs / official releases; (b) open models, repositories, weights, licenses and model cards; (c) LLM architecture, MoE, inference efficiency, quantization and context management; (d) pre-training, post-training, synthetic data and datasets; (e) evaluation methodology and independent benchmarks; (f) agentic coding, tool use, runtime orchestration and enterprise developer tooling; (g) speech/audio, image, video, vision and multimodal; (h) robotics/embodied and scientific/domain use; (i) safety, security, alignment, provenance and legal/licensing constraints; (j) community and official X/Grok signals, including independent implementer reproduction; (k) operational deployment/product availability and material industry shifts.

Discover across official vendor pages/blogs, paper originals (arXiv etc.), source-control commits/releases, model repositories/cards, reproducible evaluations, changelogs and primary incident/system documents. Supplementary press/X may discover a lead but is not automatically PRIMARY technical authority. Distinguish issuer claims from third-party measurements.

## 5. Provenance, raw capture, and candidate identity

- Follow `AGENTS.md`, `docs/survey-production-core-v2-session-bootstrap.md`, `docs/survey-production-core-v2-sol-luna-review-governance.md`, `docs/survey-production-core-v2-x-source-intake.md`, `config/weekly-pipeline.json` and the canonical W43 Profile/State.
- For each material candidate, preserve source URL, canonical title, publisher, source class, event category, first-published/time-updated values and precision, retrieval timestamp/UTC, applicable commit/tag/model version, raw artifact path, bytes and SHA256, exact attribution, license/availability where applicable, and chronology uncertainty.
- Record dedup/event-family links and source-to-candidate lineage. Keep official announcement and independent validation in separate evidence slots.
- Distinguish `CAPTURED` from `SUBSTANTIVELY_CONSUMED` in an explicit audit field. Capturing a raw file, link or summary is not consumption of its technical mechanism, baselines, dataset, metrics, conditions, failure cases and limitations.
- Materialize canonical discovery data and acceptance artifacts with the existing Core contract and validators; do not synthesize machine PASS or hand-edit Production State/Checkpoints. `stage:discovery` must use the trusted `ADVANCE_STAGE` operator flow if canonical progression is requested. Keep actual request-only commit, workflow run/preflight/execute, receipt, bot output and SHA readback.

## 6. W42 carry-over and quarantined leads

Read `sources/2026-W42/candidate-selection-v2.json`, W42 evidence/selection/history, and `docs/weekly-carryover-policy.md`. W42 had 28 SELECTED, 7 HOLD, 5 INSPECT. Make an explicit carry-over/recheck table; these 12 are leads, NOT automatically selected W43 stories and NOT an assertion that all are mandatory Core carry-over records.

Recheck the unresolved W42 families with their existing source IDs: `b80ab4ccd3469c31` (timing proof), `10d76dec5907fe46` (X-only ordering claim), `800408dab7fcce56` (X-only metrics), `1b1aea9beacefbcd` (missing harness paper), `2177831df4f20832` (unverified model name), `517550f1eb0dda9d` (video method/license), `017c9bbc00134ae8` (uncorroborated security allegation), and INSPECT IDs `b2ee0e1dffa42188`, `7151fcdc6c3ee392`, `c3439ff42a96e600`, `2cd2da5b249062c9`, `7eb212557bbc5909`. Quarantine allegations and model names until real original authority supports them.

- An event already represented in the W42 Release must not become W43 content merely because follow-up discussion appeared; only genuinely new in-window claims/actions can justify a fresh event identity.
- Distinguish rechecked / unresolved / supporting-background / prior-issue correction / no-current-action, and link decisions to exact sources.

## 7. X/Grok source boundary

- Weekly X/Grok is `REQUIRED_BY_PROFILE`. Muse cannot assume direct Google Drive/Grok access. Sol handles the Drive task/result handoff and faithful edition-local import as permitted.
- Proceed with parallel public source research, but mark `X_INTAKE_PENDING` truthfully until actual source bytes and receipt are available. Do not fabricate Grok/X results, timestamp or primary evidence; do not claim full Discovery acceptance if the canonical rules require missing X material.

## 8. Deliverables and validation

Commit edition-local outputs only under approved `sources/2026-W43/` paths and any formally required W43 publication path. Include: provenance/raw-source inventory; canonical Discovery JSONL and acceptance/checkpoint when valid; candidate-family index and lane coverage matrix; W42 carry-over disposition table; explicit not-found/failed-retrieval ledger; dated release-versus-paper chronology; critical missing-topic shortlist; Sol review handoff with artifact paths/SHA256, counts by source/event/type, exact validated Core state and trusted runs; session/index updates.

Show the list of lanes checked, candidate families, first-party raw captures, substantively consumed authorities, chronological exclusions, unresolved retrievals and negative-space risks. Zero evidence of coverage must be marked as zero rather than `PASS`. No Selection/Architecture decisions at this stage.

Perform read-only gate validation first and actual machine validation before claiming a canonical Stage. Capture real stdout/return status. Use normal commits + non-force pushes with remote readback after each logical unit. At the end report: Starting HEAD/Tree; every commit and parent; Final remote HEAD/Tree; reviewed main/Core identities; actual lifecycle state and checkpoint; receipt/run IDs; raw/Discovery counts; missing lanes; stop token.

## 9. Prohibitions

No edits to `AGENTS.md`, `config/`, `schemas/`, `scripts/`, `.github/`, `tests/`, or shared Core governance. No W42 state/release/PDF/Issue #570 edits. No assumed reuse of W41/W42 runtime compatibility grants. No self-awarded Independent Review or Human Architecture/Publication approval. Do not begin Screening/Selection/Architecture until Sol has reviewed Discovery Completeness and issued a later contract.
