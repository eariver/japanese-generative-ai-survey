# W42 r27 — Human pageplan route decision packet (PROPOSED, NOT a Gate)

Status: `HUMAN_REVIEW_REQUESTED / ROUTE_DECISION_PENDING / NO_CANONICAL_ADVANCE`. Sol will present; Human decides separately.
Basis: r1 plan (§1 of budget doc) + audited r26 physical (§2) + Core preflight proofs (compatibility doc D1–D7).
Prior decisions respected: r26 Deviation one-time acceptance (Human, 2026-10-19; process waiver ONLY, no content/Gate effect);
r1 Architecture APPROVED remains the sole binding plan; Publication Preview stays pending but NOT actionable.

## Route A — keep binding r1, add explicit Human page-count acceptance, proceed to formal Publication engineering

- **Core proof:** no frozen validator enforces advisory target 28 for WEEKLY_MAGAZINE
  (`survey_reader_fidelity_v2` soft-target doctrine + LONGFORM-only scope; architecture validator positivity-only;
  publication validators bind page_count bytes, never compare to target; r1 notes "not a hard cap"). D1–D7 dry-runs on file.
- **Canonical effect:** NONE on r1. The 21pp formal Reader/Candidate (future bounded unit, NOT r27) binds its own exact
  page_count bytes; r1 stays byte-exact. Coverage (7 pkgs × must-cover, 28 items) must be fully met — r26 diagnostic already demonstrates retainability.
- **Invalidation/data-loss risk:** minimal — preserves all research authority, r1 approval provenance, Draft, checkpoints, review index.
- **Required Human decision (explicit, edition-local, recorded as a new governance note — NOT a Gate event):**
  1. Acknowledge the measured deviation: formal issue will total ~21pp (cover1+body17+bib3), 7 under advisory target 28, within max-30 cap, with zero coverage loss and p03/p11/p13 whitespace accepted as known residual.
  2. Authorize a future bounded unit to author the formal canonical Reader manuscript + Publication Candidate under the normal
     `DRAFT_COMPLETE → validation → Publication Preview pending` stage flow (that unit performs ChatGPT semantic/editorial + visual QA, deterministic QA, exact-byte Candidate binding — none done in r27).
  3. Confirm Option B preference is now formalized by (1) — or restate it — without touching r1 bytes.
- **Earliest Core-backed next operation after Human (1)–(3):** normal stage advance to validation (handler `stage:reader-publication-validation` per config; note: no `validate:reader-publication` handler is registered in `survey_handlers_v2.py` — the future unit must resolve the intended validation entry point through the operator bridge, NOT by editing Core).

## Route B — formal Architecture r2 via lawful cross-Gate reopening

- **Core proof of current impossibility:** D2 (`request-architecture-revision` raises from DRAFT_COMPLETE),
  D3 (Publication Preview revision raises — reopen cannot start here), D5 (fabricated r2 APPROVED rejected by index semantics).
- **Lawful path (only):** complete validation + candidate under r1 → `RELEASE_CANDIDATE` with Publication Preview pending →
  Human `REQUEST_CHANGES` with pre-`ARCHITECTURE_ESTABLISHED` boundary → Core invalidates post-boundary checkpoints,
  canonical regeneration artifacts, and the ACTIVE r1 approval provenance → regress to boundary → Architecture Review r2 → new Human APPROVED.
- **Invalidation/data-loss risk:** HIGH — discards r1 approval provenance and dependent Draft/Reader derivations; forces re-review of settled research authority for a page-count-only motive. Requires the Route-A build work FIRST (a formal candidate must exist before Publication Preview is pending), then largely throws away its Gate context.
- **Required Human decisions:** (i) to build the r1 candidate knowing it will be superseded; (ii) the Publication Preview REQUEST_CHANGES with explicit boundary + requested-changes text; (iii) a full Architecture r2 review and APPROVED. Each is a separate formal Gate event with immutable snapshots.
- A faithful schema-valid r2 page-plan PROPOSAL is attached (`architecture-r2-pageplan.PROPOSED.json` + `.diff.json`:
  r1 bytes except `page_plan` → target 21 / max 23 / notes omitting per-package fractions with stated rationale).
  It is proposal text, NOT authority, and does NOT substitute for (i)–(iii).

## Route C — stop / escalate

- Applies ONLY if Human rejects both A and B, or if the missing `validate:reader-publication` handler registration
  (found during preflight) is judged to block even Route A's first step pending operator clarification.
- Action: precise blocker note to Human; no Core edits, no PROPOSED-as-approved, no Gate fabrication.

## Recommendation (Sol preflight assessment, Human decides)

**Route A, provided Human records decision (1)–(3) explicitly.** Reasons: Core-validated (the only route with passing
preflight proofs); preserves original research authority and r1 provenance; matches the independently verified
content-complete 21pp reality without padding or cutting; Route B's invalidation cost is disproportionate to a
page-count-only motive and paradoxically requires Route A's build first. Route A is recommended on evidence, NOT convenience —
D1–D7 would have forced Route C had any validator failed.

## Exact questions for Human Owner (answer each; silence decides nothing)

1. Do you ACCEPT the measured page-count deviation (formal issue ~21pp vs advisory 28, within max 30, zero coverage loss) as an explicit edition-local decision, WITHOUT altering r1 Architecture bytes? (Yes / No / Amend wording)
2. Do you AUTHORIZE a future bounded unit (separate contract) to author the formal canonical Reader manuscript and Publication Candidate under r1 and advance `DRAFT_COMPLETE → validation → Publication Preview pending`? (Yes / No / Defer)
3. Route choice: **A** (proceed under r1 + this acceptance) or **B** (build r1 candidate, then cross-Gate reopen to r2 per mechanics above) or **C** (stop/escalate with stated blocker)? If B: also confirm you understand the r1-provenance invalidation listed above.
4. The preflight found NO registered `validate:reader-publication` handler for the configured DRAFT_COMPLETE validator. Do you direct the future unit to (a) resolve via the operator bridge using existing registered handlers, or (b) halt for Core-maintenance triage first? (Core files stay read-only either way in edition work.)

## Known unknowns (explicitly NOT resolved in r27)

- Formal Reader manuscript bytes, Candidate PDF bytes/page_count, semantic-editorial + visual QA verdicts — all future-unit work.
- Whether Human wants package-level planning estimates in a future r2 note (omitted here for lack of measured basis).
- The unregistered-handler observation (§Route A, last bullet) is a routing fact, not a Core defect verdict; Core maintenance owns that triage separately.
