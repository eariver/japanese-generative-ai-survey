# W40 Muse r4 — Sol-approved Discovery Acceptance → Screening → Evidence Review preparation

Status: `SOL_EXECUTION_AUTHORITY / DISCOVERY_COMPLETENESS_PASS / BOUNDED_AT_SOL_EVIDENCE_AUTHORITY_REVIEW`
Issue: `2026-W40` (Weekly)
Repository: `eariver/japanese-generative-ai-survey`
**Only existing work branch:** `weekly/2026-W40-v2-work`
Reviewed main: `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
Sol review authority: `sources/2026-W40/execution/reviews/sol-w40-discovery-completeness-r3-PASS-20261010.md`
Muse r3 reviewed artifact HEAD: `6c293496e940114d85a5a2100fd88dd7a044646d`; Tree: `40d6083a1b46c896c6e864899d86068c14803bff`
Muse r4 exact Starting HEAD/Tree: **given in the outer invocation after this contract's commit**. Never use the pre-contract r3 SHA as the r4 Starting SHA.

## 0. Zero-write admission guards (mandatory)

Read-only verify remote W40 branch HEAD=outer Starting SHA, its Tree=outer Starting Tree, remote main HEAD=`afdb3df3faa20af3bb5798be429bba8dbd2100b1`, reviewed Muse r3 `6c293496e940114d85a5a2100fd88dd7a044646d` is a strict ancestor of starting commit, and `production-state.json` has `lifecycle_state=ISSUE_INITIALIZED`, `next_action=stage:discovery`, Human Gates pending/pending. Any mismatch: STOP and report exact expected and actual values, **ZERO WRITES**.

No new/fallback/review/repair branch; no `git reset --hard`, rebase, rewrite, force push, cherry-pick or branch history rollback. Use normal commits, non-force fast-forward push to the existing branch. No `main`, shared Core scripts/schemas/config/workflows, W39, Special editions or Human Gate mutation. Do not falsely claim Sol/Crew approval not present in its recorded review.

## 1. Required reading order and source of truth

1. Frozen Core v2 governance `docs/survey-production-core-v2-sol-luna-review-governance.md` and bootstrap `docs/survey-production-core-v2-session-bootstrap.md`.
2. W40 `production-profile.json`, `production-state.json`, `execution/index.md`.
3. Sol r1/r2/r3 independent Discovery review records under `execution/reviews/`, especially **r3 PASS** at `sources/2026-W40/execution/reviews/sol-w40-discovery-completeness-r3-PASS-20261010.md`.
4. Muse r3 `discovery/discovery-v2.jsonl` (**37 records**) and `execution/validation/proposed-not-accepted/discovery-accepted-v2.PROPOSED_NOT_ACCEPTED.json` (proposal graph `27e9efde1ece72b11a5093ea6f7130aa1916675f95d10f369f6ac77b97b346ed`).
5. W40 `external/x/x-source-intake-v2.json`, exact Grok Raw, separate Daily X URL ledger and prior collector runs/indices.
6. Reviewed `main` Core v2 stage contract, canonical Discovery Acceptance and Screening schemas, normal Evidence task/acceptance/checkpoint contracts. W39 finalized artifacts may be used as format precedents **not borrowed as authority**.

## 2. Authorised mission and hard stop

The supervising Sol has **approved Discovery research completeness**, not an automatic Core state change. In this execution unit:

A. Materialize formal canonical 37-record `sources/2026-W40/discovery/discovery-accepted-v2.json` **only** from the exact reviewed r3 Discovery JSONL and X Manifest after independent file hash, raw path, schema, graph and source-time verification. Rerun official Core v2 `build_acceptance` / `validate_acceptance` functionality and stage validator; do not rename/copy an optimistic proposal while skipping verification.

B. Advance the current canonical state **ISSUE_INITIALIZED → DISCOVERY_COLLECTED** using normal frozen Core v2 stage validation + checkpoint + state transition; record Sol review reference and actual validator output without inventing a machine Human Gate. If Core cannot express this materialization/transition truthfully, STOP `CORE_STAGE_BLOCKED`, do not manually edit state/checkpoint or soften authority.

C. Perform canonical Screening / candidate normalization for **all 37 discovered records** (including candidate-level holds, pre-window, research sweep/non-article signals, X-only signal and editorial grouping). Apply real screening/schema contract and verify candidate traceability and no accidental drop/merge of a high-signal item. Preserve W39 HOLD boundaries and the critical new Holo4, Olmo-core 3, Open TTS Leaderboard, ProvenanceGuard and RL Environments records. Issue actual canonical Screening acceptance then advance **DISCOVERY_COLLECTED → CANDIDATES_NORMALIZED** using official Core checks and checkpoint (not manual State edit).

D. Carry out evidence research in bound task-local units for plausible material items, with **iterative retrieval and actual technical source consumption**. Prepared Evidence Cards/Tasks/Edition Views and evidence-affecting materiality/completeness *drafts* are permitted as reviewer input, but Muse must STOP for Sol independent semantic authority-consumption review **before** accepting a final `EVIDENCE_REVIEWED` stage checkpoint/state. The expected terminal canonical State after successful Screening is `CANDIDATES_NORMALIZED`.

E. Prepare one complete `SOL_EVIDENCE_AUTHORITY_REVIEW_HANDOFF.md` under W40 execution, with exact statuses for every candidate, important source body consumption, completeness materiality risks, and unselected/held candidate samples. Sol will then determine whether additional Evidence gap-fill is required before Materiality/Selection.

**Terminal:** `SOL_EVIDENCE_AUTHORITY_REVIEW_READY` when sufficient inspectable Evidence is staged, or `SOL_EVIDENCE_AUTHORITY_REVIEW_BLOCKED` if primary source/validator gaps remain. Explicit pause for Sol; no autonomous progression to Selection/Architecture or Human Architecture Gate.

## 3. Critical research and verification criteria

- Distinguish publisher exact datetime vs day-only `pub_date_day`, event date, retrieval time, X time and technical rollout; Oct 2 cutoff is 22:00Z. Do not convert day-only to arbitrary 12:00Z.
- Grok Raw must retain exact SHA `10b3d7735befa1ec435462aa5254cb45b76b3d59d6f4fca0e15fc54db0dca79f` (20,477 bytes); 4 auditable Grok status URLs remain separate from Daily X 64 IDs; user-provided PDF summaries are leads, not original technical authority.
- For every material candidate: fetch and inspect model card/repo release/paper/tech docs when available; record actual mechanism, dataset/benchmark setup, version, availability, license, attribution, claimed vs independently reproduced performance. Do not mistake an editor-derived claim note for a consumed primary source.
- Explicitly classify `AUTHORITY_NOT_FOUND`, `AUTHORITY_RETRIEVAL_FAILED`, `AUTHORITY_CAPTURED_BUT_UNCONSUMED`, `AUTHORITY_CONSUMED`. A generic `PARTIAL` cannot be used to evade readily accessible primary bodies.
- Holo4 27B noncommercial vs 35B-A3B Apache-2.0 weights; distinguish APIs vs public downloadable weights. Olmo-core 3 is MoE training infrastructure, not a trillion-parameter released model checkpoint.
- HF RL Environments shipped default per-framework snippets/tags, not per-config snippet support; no format auto-conversion/sandbox auto-launch.
- Open TTS Leaderboard WER/CER/SIM/TTFA/RTFx are objective evaluations, not naturalness or listener preference ranking.
- GPT-6.1 Sol, dots, Agents API, Decisions API, Ultrafast etc. have distinct release/availability and risk boundaries; avoid hiding material differences under one catch-all DevDay candidate.
- Ollama vs Cloudflare Clef vs Strands Decider APIs/model families; judge architecture, licenses, benchmark comparability separately.
- SynthID Bio Sep30 official vs Oct1 X momentum, FLUX 3 original July launch vs October Image-specific availability, Argon exact 1M token property.
- AstaBrief / AutoSynthData / DGX Spark 64GB `TIME_UNRESOLVED` at Oct2 cutoff; Pixel Canary and TBC/AWS rumors `HOLD`; LIFT pre-window. Do not upgrade without primary timestamp/authority; explain why exclusion is reasonable.
- Model availability, license, price, max input/output tokens, and claimed improvement percentages must be checked per artifact; vendor-only claims attributed and caveated.
- Keep ordinary/late/pre/unknown classes and individual source rights. Archive original source content where lawful and accessible, bounded excerpts otherwise; maintain SHA and source locator and honest `read vs archive` status.
- Build actual Core Evidence Acceptance only after future Sol review, unless the official Core stage genuinely requires intermediate mechanics that are fully source-backed and clearly provisional. Avoid `EVIDENCE_REVIEWED` transition before Sol gate.

## 4. Required machine evidence and independent-review dossier

For the two permitted stage transitions, retain authoritative Core validation outputs, exact SHA-indexed acceptance artifacts, request/receipt and checkpoint paths, actual exit codes and non-force write proof. Core State and stage transitions must be generated by Core, never handwritten. If a documented connector/operator bridge is used, obey its immutable request and default-branch verified execution protocol.

Deliver to Sol:

1. exact r4 Starting HEAD/Tree, reviewed main and final HEAD/Tree, ancestry/changed file allowlist/readback;
2. fresh canonical 37-item Discovery Acceptance and source graph identities, including exact Sol r3 PASS reference;
3. accepted Screening candidate inventory and CORE `CANDIDATES_NORMALIZED` checkpoint/state; per-candidate dispositions and dedup logic;
4. per important Evidence candidate: main technical claim, original primary content path/URI/SHA, whether `CAPTURED`/**consumed** vs `LOCATOR_ONLY`, methodological limitations, reuse/source provenance, status VERIFIED/PARTIAL/UNRESOLVED;
5. all authority retrieval gap-fill attempts (not single failed fetch), actual inaccessible sources and declared reason;
6. candidate-level newness/temporal status, vendor-vs-independent performance benchmarking and license/access differences;
7. materially plausible unselected evidence and the counterfactual whether fully consumed sources would justify a different issue architecture; source-rich but weakly extracted items highlighted;
8. any evidence/control contract errors as blockers, no false `VALIDATED` state;
9. comprehensive `SOL_EVIDENCE_AUTHORITY_REVIEW_HANDOFF.md` with explicit `REVIEW_PENDING`, not fabricated Sol PASS;
10. final canonical state, Human Gate status, Core unchanged and exact terminal outcome.

No new or replacement branch; W40 edition-only operations; no Human Gate action; no Selection or Architecture execution in r4. STOP at fresh Sol Evidence Authority-Consumption Review for independent adjudication.
