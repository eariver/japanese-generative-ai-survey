# SP-2026-M05 pre-release review repair plan

This checkpoint records the requested repair scope before producing the next Preview revision.

- Issue #50: apply the SHA-bound Japanese reader-facing Technical Notes layer to all claim and limitation narratives, including `一次情報で確認できる事実`; immutable Evidence and Draft Packages remain unchanged.
- Issue #54: keep provenance enums unchanged while rendering reader-facing artifact/event labels consistently in `Theme at a glance` and detail cards; raw enum identifiers are rejected by pre-release validation. The third-party evaluation playbook is rendered as `評価ガイダンス` rather than a safety incident.
- Issue #55: keep Technical Notes cards breakable, keep the `一次資料` heading with its URL list as a local block, and use paragraph widow/orphan penalties to avoid URL-only or one-line card tails without reintroducing Issue #40 blank-page regressions.

Repair runner: common renderer hardening from PR #56 is merged to `main`; v0.6 generation is now authorized for this work branch.

The next candidate must be an immutable revision after v0.5, pass source-language/taxonomy validation, pass the PDF log/page-budget gate, and receive a full-page render self-check before being presented for Human Visual Review. `visual_review` and `freeze` remain pending until explicit human approval.
