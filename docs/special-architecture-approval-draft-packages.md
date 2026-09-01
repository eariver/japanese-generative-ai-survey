# Special Issue Architecture approval → Draft Packages

A Special edition may enter article drafting only after a separate explicit human approval of the already validated `PROPOSED` Issue Architecture.

The approval workflow enforces the following boundary:

1. current Special lifecycle must be `SELECTION_COMPLETE`;
2. `candidate_selection` must already be `passed`;
3. `issue_architecture` and `article_draft` must still be `pending`;
4. the exact proposed Architecture must validate before approval;
5. approval records `approved_by`, timezone-aware `approved_at`, and the user approval reference;
6. the exact approved Architecture is revalidated with `--require-approved`;
7. lifecycle advances only to `ARCHITECTURE_ESTABLISHED` and `issue_architecture=passed`;
8. immutable Draft Packages are generated from the approved Architecture and accepted Evidence bytes;
9. `article_draft` remains pending until actual draft results are validated;
10. Visual Review, Freeze, merge, and public Release remain explicit later human gates.

For `SP-2026-M07`, the approved Architecture contains eight packages: six substantive `ARTICLE_DRAFTING` packages, one deferred post-draft frontmatter synthesis package, and one deterministic references package.
