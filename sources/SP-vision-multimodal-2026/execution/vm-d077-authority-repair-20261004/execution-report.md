# Final execution report — TS-003 narrow authority repair to r5 PENDING

## §11 readback

- Starting HEAD & Tree: `d40163540001dff5cdcdc20864ab0542a624072b` /
  `b6b17b5475617478c5f4397b388ff7a4e4181aea` (remote HEAD/tree read-only verified).
- Final HEAD & Tree: HEAD unchanged (no commits by this run — not a Human Gate
  presentation); working tree holds replayed bytes + untracked exec dir.
- Evidence old/new result-set SHA: `4e77d1c6f8bf52ccd7b6e64a1787012c325ade49304884e7d92a44e7305deb22`
  → `bd31c88ce4a41762e8182b4939fe0b836a95796cb6e3d99cb7eee8894ad32aa9`
  (append-only; old sets retained). Views: `844e7fd86a8a991ad51886d7a836a7a2e16a4cf996ba22947dfe5cf9c3df9865`.
- VM-D077 old/new SHA: `ef583acaf64c` → `f6c02ed38c62` (claims rebound + unresolved narrowed).
- Supplement source list + hashes (`evidence-authority-supplement-vm-d077.json`,
  SHA `a72e4ccd4e12`, 10 sources, all first-party, exact bytes hash-bound):
  HF Molmo2-8B card / HF Molmo2-O-7B card / Ai2 blog / HF molmo2-data collection /
  Molmo2-Cap / AskModelAnything / VideoCapQA / SynMultiImageQA / VideoPoint README /
  VideoTrack README (snapshots/ + per-file SHA-256 in manifest). VM-D112 supplement untouched.
- Claim-3/4 source binding readback: claim-3 → 3 supplement IDs (8B/O-7B/blog);
  claim-4 → 7 supplement IDs (collection + 6 dataset surfaces); claim-1/2 → src-1
  (repo-level). Staged card canonical-validated (PARTIAL, 4 claims).
- VM-D077 PARTIAL preserved (individual third-party texts + attribution unbound).
- P09 old contradictory boundaries removed: Qwen3-VL-weights-Apache assertion (FALSE vs
  canonical VM-D074), "outside canonical Evidence" authority, old mix-unresolved/unbound
  lines (4 stale dropped incl. v4-carried LLaVA/VM-D077 shorts). VM-D076's unresolved +
  VM-D075/VM-D076 lims kept (CURRENT candidate-scoped authority, different buckets).
- Qwen3-VL canonical license state: code Apache 2.0 CONFIRMED; model-weight license
  UNRESOLVED in canonical Evidence (VM-D074 claim-3). No broadening performed.
- Molmo 2 canonical license/data state: code Apache 2.0 repo-bound; weights Apache 2.0
  within supplement scope (+ academic/non-commercial third-party caveat, separate buckets);
  dataset family availability + ODC-BY-family pattern on checked surfaces; individual
  third-party texts/attribution PARTIAL/INSPECT.
- Unchanged Evidence count: 111 basis-excluded identical (verified card-by-card).
- Selection semantic diff: NONE (112 assignments byte-identical, basis rebased only).
- Architecture semantic diff (44 lines): basis rebinding + VM-D112 re-binding (replay
  artifact of v4-base pattern) + P09 normalization (4 drops incl. stale lims, 3 ensures,
  3 canonical bucket lines). P08 LLaVA extended-lim propagated. NOTHING else.
  (`architecture-r4-to-fresh.diff`.)
- P15 39-authority map preserved (49 refs / 39 distinct; VM-D112 absent; VM-D089 present;
  map bytes untouched). No overlay implemented (no Draft this run; post-r5 handoff recorded).
- Shared Core changed: NO. Draft regenerated: NO (draft/ untouched by this run).
  Final lifecycle: `ARCHITECTURE_ESTABLISHED`. r5 PENDING (review-index r1–r4 + pub-r1;
  NO r5 record; NO worker-generated decision; fresh arch PROPOSED, null review;
  `f69daac4…` superseded only by authorized replay — wait, fresh arch SHA below).
- Fresh Architecture SHA: `2f12ddd3372be46689a5cca72d06acdaa96e38b3f1d44cd7cf091518e973883f`; summary `c9cef140d9ee25625fee13c2b55e9c84cf2447e43d01cb6fe502101d25bb07f8`; attention `734a7a4a0563f33cc1af8f0ecb6ad7799730b94f315376e993aae39cb4530603`; status PROPOSED, null review.

## Records in this dir

supplied-review-materialization.md / owner-exception-authorization.md (run-2 separate) /
owner-exception-execution.json / reentry-analysis.md (formal-path fail-closed probe) /
core-process-gap note (prior run) / p09-normalization-spec.md / session.md /
build_supplement.py + snapshots/ (10 exact-byte first-party snapshots) /
evidence-authority-supplement-vm-d077.json + union manifest (replay mechanics) /
stage_rebind.py + staged-vm-d077-rebound.json / replay_evidence.py /
replay_views_materiality.py / replay_selection.py / replay_architecture.py /
execute_exception_rewind.py / validation/ (3 stage validations + reviews) /
architecture-r4-to-fresh.diff / this report.
