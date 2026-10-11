# SUPPLEMENTARY RESEARCH — NOT CORE-SELECTED / NOT PART OF FORMAL ARCHITECTURE

Status: `SUPPLEMENTARY_RESEARCH_REVISED_R13 / NON_CANONICAL`
Subject: ServiceNow CoreAI AutoSynthData — failure-driven synthetic curriculum for enterprise agents
Revision of: `execution/editorial-supplement/r12/autosynthdata-note.md` (preserved immutable as review evidence)
Article event (Sol-verified, r13 re-verified 2026-10-10): https://huggingface.co/blog/ServiceNow-AI/autosynthdata —
org `ServiceNow-AI`, four badged authors (Esakkiraja, Radhakrishna, Akhiyarov, Davasam),
first-person CoreAI prose, `datePublished = dateCreated = 2026-10-02T04:01:31.290Z`
(< 22:00Z cutoff; JSON-LD strings verbatim re-verified, see `evidence-source-ledger-r13.md`).
Canonical state: Evidence PARTIAL + View/Materiality HOLD retained pending lawful
supersession (Issue #562 / CV2-DM-022). This note stages the technical substance
for Sol review; it is NOT an accepted Core chapter and MUST NOT be cited as one.
Addresses independent-audit findings W40-R12-F03 (verifier semantics), F04 (release
wording), F05 (AutoSynthData part) and F06 (ledger part).

## 1. Problem + method shape (article-declared)

Enterprise agents fail in environment-specific ways (workflow/tool/policy blind spots).
Single failures don't make training data; AutoSynthData converts target-model failure
patterns (+ stronger teacher successes) into many NEW executable tasks exercising the
same capability differently. As the model improves, the curriculum shifts to remaining
gaps (moving frontier). Article: "At ServiceNow CoreAI, we built AutoSynthData to turn
those capability gaps into training data." Demonstrated on EnterpriseOps Gym
(background, see §5).

## 2. Task abstraction + pipeline stages

- Task = (system specification, user prompt, verifier). Spec: instructions + policies +
  seeded init; must be env-compatible, no manufactured-difficulty constraints. Prompt:
  must be feasible (≥1 valid trajectory), realistic, verifiable.
- Flow: diagnose target (+ teacher) on eval tasks → capability-specification cards
  (sanitized: generator sees cards, NOT original prompts/entities/trajectories/verifiers)
  → TARGET phase (parallel core-sample generation; validate/execute/solver-eval/repair;
  vetted batch) → MULTIPLY phase (novel variants of ACCEPTED targets only; each with own
  request/state/entities/trajectory/verifier + same checks; multiplied samples cannot seed
  further — drift anchor) → SFT on accepted samples → re-evaluate → next round.
- Controller/adapter split: shared controller (generation/QC/coverage/construction) +
  env adapter (execution/state/replay/deterministic verification/solver/profiling).

## 3. Verifier discipline CORRECTED (F03): consistency + soundness + completeness

r12 glossed soundness as "accept truly successful trajectories" — that inverts the
article's definition. The article names THREE verifier properties; the corrected
reading, with acceptance/rejection examples, is:

- **Consistency**: the verifier must agree with the user prompt, the system
  specification, and the task-specific environment state. *Reject example*: a verifier
  that marks success against a different ticket state / policy version than the task
  specifies fails consistency even if its checks run cleanly.
- **Soundness** (no false positives): the verifier must REJECT trajectories that fail
  to satisfy the task or violate relevant constraints. *Positive-gate accept example*:
  the reference trajectory is executed in the environment and the resulting state
  satisfies the candidate verifier — prompt, initial state, solution, and success
  criteria align, so the sample is accepted. *Positive-gate reject example*: the
  reference trajectory executes but the end state does NOT satisfy the verifier
  (prompt/state/solution/criteria mismatch) — the sample goes to critic/repair or is
  discarded, never silently accepted.
- **Completeness** (no false negatives): the verifier must ACCEPT valid solutions
  rather than encode one particular reference trajectory. *Negative-gate accept
  example (verifier strong)*: mutated/wrong outcomes (e.g. altered expected state) are
  confirmed to FAIL verification — the verifier discriminates success from failure.
  *Negative-gate reject example (verifier weak)*: a mutated outcome still PASSES —
  the verifier "awards success without requiring the intended behavior" and the sample
  is routed to critic/repair.
- Training consequence (article): "A lax verifier can reward incorrect behavior, while
  an overly restrictive verifier can penalize valid solutions." Lax = soundness failure;
  over-strict = completeness failure. Keep the two directions distinct in all downstream
  prose.

## 4. Quality gates (the methodologically distinctive content)

- Solver-evaluation gate (config used): FAVOR tasks the target solves on ≤1/3 trials
  AND the stronger solver solves on ≥2/3 (difficulty band — article: "no more than one
  of three trials" / "at least two of three trials").
- POSITIVE gate: reference trajectory executed in env must satisfy the candidate verifier
  (catches prompt/state/solution/criteria mismatch).
- NEGATIVE gate: mutated/wrong outcomes must FAIL verification (catches weak verifiers).
- Critic + BOUNDED repair: failures triaged (inconsistent state / impossible workflows /
  incorrect task construction / bad reference trajectories / weak verifier logic /
  mismatch with intended capability) with a FIXED retry limit, then discard. Repaired
  tasks must pass the relevant checks again; diagnosis guides repair of the existing
  candidate rather than regenerating from scratch.
- Batch-level meta-review (distinct from sample gates): examines accepted + rejected
  samples + generation behavior per batch (overrepresented families, missing capability
  dimensions, repeated failures, systematic critique patterns); controller rebalances
  coverage/diversity/redundancy within generation budget. Do not conflate with the
  per-sample accept/repair loop.
- Coverage/drift anchor: multiplied samples cannot seed further multiplication.

## 5. Reported experiments WITH scope (publisher-measured, SFT-only, Gym-only)

Symmetric table (F05 — settings, metrics, teachers kept in parallel columns; ITSM ran
FIRST, Hybrid second after pipeline optimization — article: "the ITSM run … preceded
pipeline optimizations that improved throughput", preserved here):

| Setting | Hybrid domain | ITSM domain |
|---|---|---|
| Target | Gemma-4-26B-A4B-it | Gemma-4-26B-A4B-it (same) |
| Teacher | Qwen3.8-27B | DeepSeek-V4.1-Flash (larger) |
| Synthetic samples | 2,000 | 1,994 |
| Generation time | ~18h | 66h (larger teacher + pre-optimization pipeline) |
| Training | SFT; best checkpoint epoch 5 | SFT |
| Mean Pass@1 | +7.2 percentage points (= 35% relative — keep pp and % distinct, never merge) | 18.77% → 27.18% |
| Verifier success | 63.01% → 68.55% | (not reported for ITSM — do not impute) |
| Gap closed | 59% of target–reference gap | (not reported for ITSM — do not impute) |

- Generator never saw original eval tasks (capability cards only) — preserved.
- Limits to preserve: SFT evidence only — RL is explicitly future ("We plan to test
  this moving, difficulty-calibrated frontier beyond SFT"); single benchmark family
  (EnterpriseOps Gym Hybrid + ITSM); teacher/model names taken verbatim from article
  (no external registry proof in r13 scope); no independent reproduction.

## 6. Separation: what was NOT released (F04 bounded wording)

- CORRECTED (F04): earlier "NO standalone AutoSynthData pipeline code, weights,
  dataset, or service" is replaced with the bounded form: **no standalone
  AutoSynthData pipeline code, weights, dataset, or service was independently
  identified in bounded checked sources at retrieval time** (r12 scope: HF API
  401/empty responses + negative site searches). A 401/empty search is not proof of
  non-existence; do not convert it into one. Corroborating (not proving) article-level
  signal: the article's own models-mentioned section lists only the teacher/target
  models (Gemma, Qwen3.8, DeepSeek-V4.1-Flash) and its datasets-mentioned section lists
  only EnterpriseOps-Gym — the article itself claims no AutoSynthData code/dataset
  release. Never claim open-source pipeline.
- EnterpriseOps Gym (`ServiceNow-AI/EnterpriseOps-Gym`, created 2026-02-28,
  Apache-2.0, paper Malay et al. 2026 arXiv:2603.13594, public released dataset linked
  from the article) is PRE-WINDOW background infrastructure used for the demo, NOT the
  AutoSynthData release.

## 7. Unresolved / out-of-scope for this note

- No code-level adapter/controller detail beyond article prose; no cross-env
  generalization evidence; no cost/throughput analysis beyond the 66h ITSM note.
- Teacher registry existence (Qwen3.8-27B, DeepSeek-V4.1-Flash, Gemma-4-26B-A4B-it
  identifiers) taken verbatim from article; not independently proved against model hubs.
- Future canonical home (Sol decision later): P6a fourth PRIMARY subsection
  (synthetic curriculum generation), table-separated from AstaBrief mixes and
  Olmo-core infra, per r11 counterfactual Plan B.
