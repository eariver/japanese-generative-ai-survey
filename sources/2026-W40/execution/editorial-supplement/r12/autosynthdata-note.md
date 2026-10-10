# SUPPLEMENTARY RESEARCH — NOT CORE-SELECTED / NOT PART OF FORMAL ARCHITECTURE

Status: `SUPPLEMENTARY_RESEARCH_READY_FOR_SOL_REVIEW / NON_CANONICAL`
Subject: ServiceNow CoreAI AutoSynthData — failure-driven synthetic curriculum for enterprise agents
Article event (Sol-verified): https://huggingface.co/blog/ServiceNow-AI/autosynthdata —
org `ServiceNow-AI`, four badged authors (Esakkiraja, Radhakrishna, Akhiyarov, Davasam),
first-person CoreAI prose, `datePublished = dateCreated = 2026-10-02T04:01:31.290Z`
(< 22:00Z cutoff).
Canonical state: Evidence PARTIAL + View/Materiality HOLD retained pending lawful
supersession (Issue #562). This note stages the technical substance for Sol review;
it is NOT an accepted Core chapter and MUST NOT be cited as one.

## 1. Problem + method shape (article-declared)

Enterprise agents fail in environment-specific ways (workflow/tool/policy blind spots).
Single failures don't make training data; AutoSynthData converts target-model failure
patterns (+ stronger teacher successes) into many NEW executable tasks exercising the
same capability differently. As the model improves, the curriculum shifts to remaining
gaps (moving frontier). Demonstrated on EnterpriseOps Gym (background, see §4).

## 2. Task abstraction + pipeline stages

- Task = (system specification, user prompt, verifier). Spec: instructions + policies +
  seeded init; must be env-compatible, no manufactured-difficulty constraints. Prompt:
  must be feasible (≥1 valid trajectory), realistic, verifiable.
- Verifier discipline: sound (accept truly successful trajectories), complete (accept
  valid alternatives, not one reference path). Lax verifiers reward wrong behavior;
  over-strict ones punish valid solutions.
- Flow: diagnose target (+ teacher) on eval tasks → capability-specification cards
  (sanitized: generator sees cards, NOT original prompts/entities/trajectories/verifiers)
  → TARGET phase (parallel core-sample generation; validate/execute/solver-eval/repair;
  vetted batch) → MULTIPLY phase (novel variants of ACCEPTED targets only; each with own
  request/state/entities/trajectory/verifier + same checks; multiplied samples cannot seed
  further — drift anchor) → SFT on accepted samples → re-evaluate → next round.
- Controller/adapter split: shared controller (generation/QC/coverage/construction) +
  env adapter (execution/state/replay/deterministic verification/solver/profiling).

## 3. Quality gates (the methodologically distinctive content)

- Solver-evaluation gate (config used): keep tasks the target solves ≤1/3 trials AND the
  stronger solver solves ≥2/3 (difficulty band).
- POSITIVE gate: reference trajectory executed in env must satisfy the candidate verifier
  (catches prompt/state/solution/criteria mismatch).
- NEGATIVE gate: mutated/wrong outcomes must FAIL verification (catches weak verifiers).
- Critic + BOUNDED repair: failures triaged (bad state/workflow/construction/trajectory/
  verifier/capability mismatch) with fixed retry limit, then discard.

## 4. Reported experiments WITH scope (publisher-measured, SFT-only, Gym-only)

- Hybrid domain (target Gemma-4-26B-A4B-it, teacher Qwen3.8-27B as named in article):
  synthetic SFT mean Pass@1 +7.2pp (35% relative); verifier success 63.01%→68.55%;
  closes 59% of target–reference gap. Generator never saw original eval tasks.
- ITSM domain (same target, teacher DeepSeek-V4.1-Flash as named): 1,994 samples / 66h
  (slower: larger teacher + pre-optimization pipeline); mean Pass@1 18.77%→27.18%.
- Limits to preserve: SFT evidence only (no RL result); single benchmark family
  (EnterpriseOps Gym Hybrid + ITSM); teacher/model names taken verbatim from article
  (no external registry proof in r12 scope); no independent reproduction.

## 5. Separation: what was NOT released

- NO standalone AutoSynthData pipeline code, weights, dataset, or service (HF API:
  no public model/dataset; site searches negative — consistent with r4
  AUTHORITY_RETRIEVAL_FAILED). Never claim open-source pipeline.
- EnterpriseOps Gym (`ServiceNow-AI/EnterpriseOps-Gym`, created 2026-02-28,
  Apache-2.0, paper Malay et al. 2026 arXiv:2603.13594) is PRE-WINDOW background
  infrastructure used for the demo, NOT the AutoSynthData release.

## 6. Unresolved / out-of-scope for this note

- No code-level adapter/controller detail beyond article prose; no cross-env
  generalization evidence; no cost/throughput analysis beyond the 66h ITSM note.
- Future canonical home (Sol decision later): P6a fourth PRIMARY subsection
  (synthetic curriculum generation), table-separated from AstaBrief mixes and
  Olmo-core infra, per r11 counterfactual Plan B.
