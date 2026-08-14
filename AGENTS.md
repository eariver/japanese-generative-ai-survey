# Repository agent instructions

## Special compilation bootstrap

When a user asks to start or resume a Special edition in this repository, treat the current `main` branch as the operational source of truth and read `docs/special-session-bootstrap.md` before performing editorial work.

The user only needs to identify the target edition/period and, when relevant, the Human Gate at which to stop. Do not require the user to restate manifest paths, pipeline stages, Human Gate rules, half-year analysis requirements, taxonomy policy, Technical Notes policy, or release mechanics that are already defined in the repository.

For a request such as:

> `2025-H1 SpecialをArchitecture Reviewまで編纂してください。`

resolve the target from current repository configuration, initialize the edition if necessary, resume existing state if present, follow the current Special pipeline and applicable period guide, proceed autonomously to the requested Human Gate, and stop there for explicit human approval.

Never infer Human Gate approval from a request to begin or continue compilation. Repository state must remain sufficient for a later chat session to resume without relying on prior conversation history.

Cross-edition pipeline, validator, schema, or workflow improvements belong on `main` through the repository's normal review/CI process. Edition-specific Evidence, Architecture, drafts, provenance, and release artifacts remain scoped to that edition's work branch and canonical paths.
