# Special Candidate Selection → Issue Architecture gate

This note records the operational boundary used by Special editions.

1. Accepted Evidence is converted into the canonical non-ranking Candidate comparison matrix.
2. Candidate Selection may become `APPROVED` only from an explicit user-reviewed assignment set bound to the exact matrix SHA-256.
3. A successful Selection advances the Special lifecycle only to `SELECTION_COMPLETE` and marks `candidate_selection=passed`.
4. The approved Selection is converted into a SHA-bound Architecture Input.
5. A proposed Issue Architecture may then be generated and validated for coverage, Evidence boundaries and page accounting.
6. The proposed Architecture remains `PROPOSED`; `issue_architecture` remains pending until a separate explicit user approval.
7. Drafting must not begin before that Architecture approval.

For expanded Specials, page target/max are read from the Special edition manifest rather than the Weekly defaults embedded in the shared Architecture Input builder.

The July 2026 retrospective is the first real execution of this path. Its reviewed Candidate Selection retains six themes in one volume, with a planned 36 pages against a 32-page target and 40-page maximum.
