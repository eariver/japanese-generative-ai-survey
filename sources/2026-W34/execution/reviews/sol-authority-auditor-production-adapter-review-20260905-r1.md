# Sol review — W34 Authority Auditor production adapter r1

Status: `PASS_FOR_W34_READ_ONLY_SIDECAR_PILOT`

Date: 2026-09-05 JST

## Reviewed candidate

- tool: `Survey Core v2 Authority Auditor`
- repository: `eariver/survey-core-v2-authority-auditor`
- baseline reviewed tool SHA: `4f88e55c66646a350ed286683f98b0cbca61f633`
- production-adapter branch: `work/w34-production-adapter-20260905`
- production-adapter candidate SHA: `c5f09d463b21c914d9c59b34597858f6182fc244`
- survey compatibility authority: `eariver/japanese-generative-ai-survey@a9f121f0d65591f52b53515712d7c0bae573b2ef`

The adapter candidate is accepted for the W34 pilot as an exact-SHA independent sidecar tool. This review does not make it Survey Production Core authority and does not merge the auditor candidate into auditor `main`.

## Review findings

### Read-only exact-byte production boundary — PASS

The adapter resolves canonical W34/W33 Production State and Publication Candidate paths from an exact survey checkout, follows Candidate- and State-bound repository-relative authority paths, reads and hashes the original upstream bytes, and passes an in-memory `Bundle` to the existing invariant engine. It does not copy/re-serialize survey artifacts into a fixture and then treat the copy as authority.

Resolved artifacts are re-read after the audit and compared against their initial SHA/byte count so checkout mutation during the read-only run is detected.

### Run A / Run B lifecycle surfaces — PASS

The adapter has explicit production phases for:

- `PRE_PUBLICATION_PREVIEW` — Authority Audit Run A;
- `POST_APPROVAL_PRE_FREEZE` — Authority Audit Run B;
- `RELEASED_COMPATIBILITY` — read-only released-edition compatibility checking.

Run A does not invent Human approval. Run B requires the actual approval surface and catches stale Candidate mutation before Freeze.

### Fail-closed path handling — PASS

Dedicated regressions cover missing Candidate, wrong issue, path escape, symlink authority, Candidate-bound digest drift, and post-approval Candidate mutation. Exact-bound production resolution does not use basename search as authority.

### Existing invariant catalog — PASS with retained limitations

Catalog remains:

- `9 FULLY_IMPLEMENTED`
- `6 PARTIAL`: `INV-04`, `INV-05`, `INV-06`, `INV-11`, `INV-12`, `INV-15`

No PARTIAL invariant is promoted to FULL or to unconditional W34 blocking authority by the adapter. The sidecar report continues to expose these limitations.

### INV-13 basename behavior — ACCEPTED bounded production specialization

The prototype's fixture-mode differing-bytes duplicate-basename rule is stricter than upstream and was already documented as advisory. The adapter preserves that rule in fixture mode. In `exact-bound` production mode it is not used because every authority read follows the exact repository-relative path bound by Candidate/State; unrelated files sharing a basename cannot override that authority. Repository-relative path safety, symlink refusal, exact digest checks, and case mismatch checks remain active.

This is accepted as a bounded production adapter specialization, not a weakening of Core authority.

### Fixture reconciliation — ACCEPTED, not a rebenchmark classification change

The candidate also reconciles stale dependent exact-byte/digest references in previously declared valid fixtures. It does not reclassify fixture metadata, replace source/PDF bytes, or change the expected corpus distribution. Validation reports the same `18 valid / 64 invalid / 12 ambiguous` metadata distribution and `18 PASS / 76 FAIL` audit outcome.

Because the baseline exact SHA remains separately preserved on auditor `main`, these fixture repairs do not rewrite the historical benchmark record. The W34 pilot pins the new adapter candidate SHA explicitly.

## Validation evidence reviewed

Candidate record reports:

- full pytest: `81 passed` (`67` pre-existing + `14` adapter tests);
- compileall: PASS;
- `git diff --check`: PASS;
- 94-fixture audit: `18 PASS / 76 FAIL`;
- base red-team: `15/15` caught;
- repair red-team: `12/12` caught;
- exact W33 checkout at survey `a9f121f0...`: resolution errors `0`, auditor PASS, production PASS;
- synthetic Run A: PASS, no approval invented;
- synthetic Run B: PASS;
- Run B Candidate mutation: FAIL as expected;
- survey checkout remained read-only/clean.

## W34 operational disposition

For W34 sidecar runs, use:

- Publication Boundary Validator: `eariver/publication-boundary-redteam@7b9de2105c690daaafa6698c1791d51ca84a92c0`
- Survey Core v2 Authority Auditor + production adapter: `eariver/survey-core-v2-authority-auditor@c5f09d463b21c914d9c59b34597858f6182fc244`

The Authority Auditor SHA above supersedes `4f88e55...` only for the W34 production-adapter pilot execution surface. `4f88e55...` remains the independent benchmark baseline/provenance parent.

Do not execute either sidecar before Human Architecture Review. Sidecar reports remain independent QA evidence and do not create Production State authority, lifecycle states, Human Gates, or an eighth workflow.
