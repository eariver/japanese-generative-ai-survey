# Repository agent instructions

## Special compilation bootstrap

When a user asks to start or resume a Special edition in this repository, treat the current `main` branch as the operational source of truth and read `docs/special-session-bootstrap.md` before performing editorial work.

The user only needs to identify the target edition/period and, when relevant, the Human Gate at which to stop. Do not require the user to restate manifest paths, pipeline stages, Human Gate rules, half-year analysis requirements, taxonomy policy, Technical Notes policy, or release mechanics that are already defined in the repository.

For a request such as:

> `2024-H2 SpecialをArchitecture Reviewまで編纂してください。`

resolve the target from current repository configuration, initialize the edition if necessary, resume existing state if present, follow the current Special pipeline and applicable period guide, proceed autonomously to the requested Human Gate, and stop there for explicit human approval.

**The start request itself authorizes deterministic initialization.** Initialization is not a Human Gate. For a configured but absent edition, do not ask for confirmation before creating the init branch, writing/validating the edition manifest and initial pipeline state, opening and merging the init PR, creating the canonical work branch, and continuing toward the requested Human Gate. If equivalent bootstrap state already exists, resume it instead of duplicating it.

Never infer Human Gate approval from a request to begin or continue compilation. The normal Human Gates are Architecture Review and Publication Preview; Candidate Selection is an internal checkpoint, and Visual Review/Freeze/merge/Release after an approved Publication Preview are deterministic state transitions under that approval. Raise an Exception Gate only when current repository policy says a genuinely new editorial/publication decision is required.

Repository state must remain sufficient for a later chat session to resume without relying on prior conversation history.

Cross-edition pipeline, validator, schema, or workflow improvements belong on `main` through the repository's normal review/CI process. Edition-specific Evidence, Architecture, drafts, provenance, and release artifacts remain scoped to that edition's work branch and canonical paths.
