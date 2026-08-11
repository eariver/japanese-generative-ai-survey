# SP-2026-M07 v0.5 layout implementation

This control-code change implements the second Visual Review revision for the July 2026 Special.

The release candidate remains evidence-first. The change does not reopen Source Intake, Screening, Evidence, Candidate Selection, or the approved six-theme Architecture.

Key implementation changes:

- chapter headings are rendered full-width so long Japanese/English mixed titles cannot collide with the adjacent narrative column;
- narrative article bodies are derived from the already-accepted Article Draft TeX by removing only the top-level `section` / `label` from a layout-only copy;
- accepted article source files remain byte-identical and continue to be SHA-checked;
- narrative uses a local balanced `multicols` environment instead of global `twocolumn` / `onecolumn` switching;
- Theme Synthesis and Technical Notes remain full-width and can follow a balanced narrative on the same page when space permits;
- a `Needspace` guard keeps wide synthesis blocks from being cramped at the bottom of a page;
- a final retrospective chapter is generated from a reviewed JSON artifact that may reference only Evidence already selected by the approved July issue;
- cross-chapter relationships are explicitly framed as editorial/structural synthesis, not demonstrated causal links.

The generated v0.5 PDF must still pass the existing clean TeX-log and 32-40 page gates and must return to the human Visual Review gate before Freeze.
