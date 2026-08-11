# Special Technical Notes review fixes

Common renderer hardening for pre-release findings #50, #54, and #55.

- SHA-bound Japanese reader summaries can be applied even after repository-only Evidence IDs have already been removed from a working PDF-facing revision; exact canonical card title is used only as a unique fallback binding.
- Reader-facing artifact/event taxonomy no longer exposes raw schema enums or TeX-escaped enum fragments; the evaluation playbook receives the semantic label `評価ガイダンス`.
- Technical Notes cards remain breakable. Only the source-heading/URL block is locally held together, with paragraph widow/orphan penalties inside cards to reduce tiny page-top continuations.
- Pre-release validation and the Visual QA checklist now explicitly cover Japanese narrative, raw-enum leakage, semantic type consistency, and card continuation quality.
