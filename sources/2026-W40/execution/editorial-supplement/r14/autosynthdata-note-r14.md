# SUPPLEMENTARY RESEARCH — NOT CORE-SELECTED / NOT PART OF FORMAL ARCHITECTURE

Status: `SUPPLEMENTARY_RESEARCH_REVISED_R14 / NON_CANONICAL`
Subject: ServiceNow CoreAI AutoSynthData — failure-driven synthetic curriculum for enterprise agents
Revision of §3/examples ONLY: `../r13/autosynthdata-note-r13.md` (preserved immutable as
review evidence; all other r13 sections — abstraction, pipeline, gates inventory,
experiments, release wording, Gym separation — carry over semantically unchanged).
Article event (unchanged): https://huggingface.co/blog/ServiceNow-AI/autosynthdata —
org `ServiceNow-AI`, four badged authors, first-person CoreAI prose,
`datePublished = dateCreated = 2026-10-02T04:01:31.290Z` (< 22:00Z cutoff).
Canonical state: Evidence PARTIAL + View/Materiality HOLD retained pending lawful
supersession (Issue #562 / CV2-DM-022). This note is NOT an accepted Core chapter and
MUST NOT be cited as one. Addresses W40-R13-F06 (Sol disposition: ACCEPTED).

## Verifier semantics CORRECTED (F06): three properties, two gates, one limit theorem

r13 §3 correctly named the triad but mis-assigned what each GATE exercises: it implied
the negative gate tells us about completeness and left the positive gate's probative
scope vague. The corrected reading, bound to the article's definitions:

- **Consistency**: the verifier must agree with the user prompt, the system
  specification, and the initial/environment task state. A verifier checking the wrong
  ticket queue, wrong policy version, or wrong seeded database state fails consistency
  even if every check it runs passes.
- **Soundness** (false-positive prevention): invalid, unsuccessful, or
  policy-violating outcomes MUST NOT be accepted. A verifier that waves through a
  trajectory which skipped a mandatory approval step is unsound, however plausible the
  final state looks.
- **Completeness** (false-negative prevention): VALID alternative solutions MUST be
  accepted, independent of the exact reference trajectory. A verifier that passes only
  the byte-identical reference path and fails an equally correct reordering of two
  independent tool calls is incomplete.

Gate-to-property assignment (the F06 correction):

- **Positive gate exercises a valid reference/witness execution.** It runs the intended
  solution in the environment and checks the end state against the candidate verifier —
  i.e. it checks consistency (prompt/spec/state align for this witness), feasibility
  (the task is solvable at all), and alignment (solution and success criteria describe
  the same outcome) FOR THAT WITNESS. It cannot by itself prove universal completeness:
  one witness passing says nothing about whether OTHER valid solutions would pass.
- **Negative gate chiefly exercises soundness, NOT completeness.** It must reject
  deliberately mutated/invalid outcomes (e.g. an expected record left unmodified, a
  required field dropped, a policy constraint violated). Each rejection is evidence the
  verifier discriminates success from failure. It says NOTHING about completeness — a
  verifier can reject every mutation yet still fail a valid alternative.
- **Completeness is evidenced ONLY by valid-alternative acceptance**: distinct
  trajectories that legitimately satisfy prompt + spec + state must pass. Neither gate
  alone establishes it; the positive gate uses one witness, the negative gate uses
  invalid inputs.
- **Finite-test limit (stated plainly): a passing finite test suite does not
  mathematically prove universal soundness or completeness.** It bounds observed risk
  over tested mutations and witnesses; adversarial or untested regions remain
  unproven. Do not upgrade "all gates passed" to "verifier proven correct."

## Distinct concrete test examples (one per case)

Setup (illustrative ITSM-flavored fixture, consistent with the article's domain, NOT a
claim about Gym internals): task = "reopen incident INC-1042 and escalate to P2";
spec requires the escalation note to cite the incident's error code; policy forbids
closing the incident without customer confirmation.

1. POSITIVE (witness) — reference trajectory reopens INC-1042, sets priority P2,
   appends a note citing the incident's error code, leaves state otherwise intact.
   Executed end state satisfies the verifier → ACCEPT. Proves for this witness:
   consistent, feasible, aligned. Does NOT prove any other solution would pass.
2. NEGATIVE (mutation, must-reject) — same trajectory but the escalation note cites a
   DIFFERENT incident's error code (mutated outcome). Verifier must REJECT: the outcome
   violates the spec's citation requirement. If it accepted, the verifier would be
   unsound (weak-verifier catch) → critic/repair. Says nothing about completeness.
3. NEGATIVE (policy violation, must-reject) — trajectory closes INC-1042 without
   customer confirmation to "resolve quickly." Verifier must REJECT (policy-violating
   outcome). Acceptance here would be a soundness failure with direct training harm
   (rewarding incorrect behavior — article's lax-verifier warning).
4. ALTERNATE-VALID (completeness probe) — trajectory sets P2 BEFORE reopening (valid
   reorder of independent steps), note cites the correct error code, no policy breach.
   Verifier must ACCEPT despite differing from the reference trajectory. Rejection here
   would be a completeness failure (over-strict verifier punishing a valid solution —
   article's warning), routing to critic/repair of the verifier logic, not the solution.
5. CONSISTENCY probe — verifier evaluates against incident INC-1043's state (wrong
   seeded state) while prompt/spec say INC-1042. Reference trajectory then "fails" for
   reasons unrelated to its quality → the VERIFIER is inconsistent, and the failure
   must be attributed to verifier/state mismatch, not to the candidate solution.

## Preserved unchanged from r13 (F06-external material)

TARGET/MULTIPLY phases (no re-seeding; drift anchor); solver difficulty band
(target ≤1/3, solver ≥2/3); positive/negative gate inventory; critic categories +
fixed retry limit + re-pass requirement; batch meta-review; moving frontier (SFT
demonstrated, RL planned); experiments Hybrid (2,000 samples / ~18h / best epoch 5;
+7.2pp = 35% relative; verifier 63.01%→68.55%; 59% gap closed) and ITSM
(1,994 / 66h, ran FIRST; 18.77%→27.18%); method-only release posture with F04 bounded
wording; Gym background separation (created 2026-02-28, Apache-2.0, Malay et al. 2026
arXiv:2603.13594); SFT-only scope; teacher/model names verbatim without registry proof.

## Claim/limit audit (r14 delta)

- NEW claims in this note: gate-to-property assignment (positive→consistency/
  feasibility/alignment-for-witness; negative→soundness-not-completeness),
  finite-test limit theorem, five fixture examples. Basis: article's verifier/gate
  prose re-read 2026-10-10 (r13 retrieval) — the fixture itself is illustrative,
  labeled as such, and claims NOTHING about Gym internals.
- NO new release, license, metric, or clock claims. Source URL + noncanonical status
  identical to r13. Manifest pointers updated in `manifest-r14.md`.
