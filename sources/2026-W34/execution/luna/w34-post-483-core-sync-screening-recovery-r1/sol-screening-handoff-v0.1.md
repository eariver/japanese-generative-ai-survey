# W34 Sol handoff — corrected Screening basis

Status: `READY_FOR_SOL_EVIDENCE`

The reviewed `main@a9f121f0d65591f52b53515712d7c0bae573b2ef` was normally merged into W34 as `b8a0ae502fd03d17bcb4f5d9e1f67a26c77ab30e`. The current production State is now `CANDIDATES_NORMALIZED`; the repository-configured next action is `stage:evidence-materiality-completeness`.

## Screening authority

- Accepted root Discovery: 40 records, 40 unique IDs; unchanged.
- Current derived Screening basis: `sources/2026-W34/screening/input/event-discovery-v2.jsonl`.
- Current derived basis: 110 records, 110 unique IDs, SHA-256 `9bfc0fc9b63f97cc9568dc53bb06595dd2540b92e843b55b2650abcbcc97aca2`.
- Accepted-root accounting: 40/40 accounted, 0 unaccounted.
- Event crosswalk: W34-C001–W34-C105, 105/105, missing 0, duplicate 0.
- Five coverage passthrough children were copied from their exact accepted GitHub Releases parent source objects and are not new Weekly events.

## Decisions

The 105 existing Sol decisions were reused unchanged. The five supplement decisions are exactly `DROP`:

- `w34-coverage-comfy-org-comfyui`
- `w34-coverage-ggml-org-llama-cpp`
- `w34-coverage-nvidia-tensorrt-llm`
- `w34-coverage-sgl-project-sglang`
- `w34-coverage-vllm-project-vllm`

Corrected totals are `KEEP 45 / MAYBE 19 / INSPECT 16 / DROP 30 / TOTAL 110`. The resulting expected non-DROP Evidence task count is `80`.

## Immutable and active acceptance

Historical acceptance `2ab82c6b52b26fc01cc6a82d20da08ef4b37dadaf2ff1b0e5a570f50652b3662` remains present and byte-unchanged. Corrected acceptance is:

`sources/2026-W34/screening/v2/accepted/5692a79ac20f4376beee02758754a71b771ed78ff30b675d2fa8177af7f65e98/screening-accepted.json`

It passed current-Core acceptance validation. The passed Screening Stage Checkpoint binds this exact corrected artifact, and the active resolver returns it exclusively. Historical directory contents are retained as evidence and are not used as an active-selection heuristic.

## Next bounded action

The branch is ready for Sol's independent Evidence-stage work. This session did not perform Evidence verification or acceptance, Materiality, Completeness, Selection, Architecture, Human Gate, drafting, Freeze, Release, or either external sidecar tool.

See `validation-v0.1.json` for the complete machine-validation evidence.

## Regression evidence

Targeted current-Core regressions: 25/25 PASS. Full Python test discovery: 737 tests, 0 failures, 6 skipped, PASS. No Evidence acceptance or later-stage work was run.
