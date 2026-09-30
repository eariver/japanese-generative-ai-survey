# TS-003 r2 → r3 minimal repair report (Sol r2 R2-F1/F2)

Issue: `SP-vision-multimodal-2026` | Date: `2026-09-30 UTC` | Lifecycle: `CANDIDATES_NORMALIZED` (unchanged)

r2 input: `execution/evidence-semantic-repair-r1-20260930/evidence-interactive-input-r2.json`
r3 input: `execution/evidence-semantic-repair-r2-20260930/evidence-interactive-input-r3.json`
r2 acceptance: `evidence/v2/accepted/3f6be211...` (immutable history, untouched)
r3 acceptance: `evidence/v2/accepted/c6763f1c...` (sha `1ab3efa5...`, 111 Cards)
r2 views: `evidence/v2/views/accepted/73c06689...` (untouched)
r3 views: `evidence/v2/views/accepted/fc8556a3...` (sha `fe25033b...`, 111 Views)
Same canonical task package; Discovery/Screening unchanged; 106 records byte-identical.

## Changed records: 5 of 111 (D074, D075, D077, D101, D111)

### R2-F1 — VM-D074 (Qwen3-VL repo card)
- r2 claim: weights Apache 2.0 via HF release tag (sha 0c351dd0).
- r3 claim: code Apache 2.0 via repo-root LICENSE file (bound repo, exact path); weights license unresolved in canonical Evidence (HF surface not bound; observation retained only in audit note §A).
- Why faithful: task binds only the GitHub repo root; HF release metadata is external to that binding. Repo-internal LICENSE fact stays with exact path.
- Status: VERIFIED → VERIFIED.

### R2-F1 — VM-D075 (Qwen3-Omni repo card)
- r2 claim: weights license:other via HF tag (sha 26291f79) + code unbound.
- r3 claim: README deployment surface kept (thinker-only mode, cookbooks, README-stated trending); weight/code licenses unresolved in canonical Evidence (HF-derived facts removed to audit note §A).
- Why faithful: removes the only HF-sourced assertion; no r1-style Apache implication returns.
- Status: VERIFIED → VERIFIED.

### R2-F1 — VM-D077 (molmo2 repo card)
- r2 claim: weights Apache 2.0 via HF tag + 9 datasets available via HF tags.
- r3 claim: code Apache 2.0 via repo-root LICENSE file; weights/data availability and per-dataset terms unresolved in canonical Evidence (HF surfaces not bound; observations in audit note §A); third-party mix unresolved.
- README-packaging pointers ("collections linked from the repo README", "checkpoint-to-HF conversion" TOC entry) kept as repo-internal facts.
- Why faithful: narrowest removal satisfying Sol r2 §2 option 2; PARTIAL preserved.
- Status: PARTIAL → PARTIAL.

### R2-F1-adjacent — VM-D111 (VSI-Bench, paper-bound task)
- r2 claim cited HF dataset viewer row counts/subsets; the HF dataset page is not a bound source for this task.
- r3 claim: paper-established design only (5,131 QA, 288 videos, 8 tasks, MCA+MRA, blind baselines, CoT/cognitive-map findings); viewer facts removed to audit note §A; limitation records the unbound viewer surface.
- Status: PARTIAL → PARTIAL.

### R2-F2 — VM-D101 (Ha & Schmidhuber 2018)
- Removed: claim-0 context "term-origin content consumed"; verification finding "Terminological origin ... recorded"; transition id `d14-term-origin`; inheritance note "Dream-training terminology inherited ...".
- Replacement: "dream-training formulation content"; finding restates branch-separated lineage with non-ancestry guard; transition id `d14-historical-formulation-anchor` (free-form, schema-valid); inheritance note disclaims terminology-inheritance (term history not researched).
- Limitations updated; non-ancestry guard ("Must never be narrated as Genie's technical ancestor") kept.
- Status: VERIFIED → VERIFIED.

## §A. Non-canonical supplemental observations (audit-note only, NOT canonical Evidence)

These facts were removed from canonical Cards because their surfaces are not bound task sources.
They are preserved here so Sol/later stages can admit them formally (e.g., via Evidence Authority
Supplement) if desired. Retrieval: 2026-09-30 UTC.

1. HF `Qwen/Qwen3-VL-8B-Instruct`: tag `license:apache-2.0`, sha `0c351dd01ed87e9c1b53cbc748cba10e6187ff3b`, modified 2025-10-15.
2. HF `Qwen/Qwen3-Omni-30B-A3B-Instruct`: tag `license:other`, sha `26291f793822fb6be9555850f06dfe95f2d7e695`, modified 2025-09-22.
3. HF `allenai/Molmo2-8B`: tag `license:apache-2.0`, sha `e28fa28597e5ec5e0cca2201dd8ab33d48bc4a1b`, modified 2026-01-23; datasets `allenai/Molmo2-{Cap,VideoCapQA,VideoSubtitleQA,AskModelAnything,VideoPoint,VideoTrack,MultiImageQA,SynMultiImageQA,MultiImagePoint}` listed; per-dataset terms unbound.
4. molmo2 repo-root LICENSE = Apache 2.0; Qwen3-VL repo-root LICENSE = Apache 2.0 (repo-internal files; code-scope only).
5. HF `nyu-visionx/VSI-Bench`: viewer showed full 5.13k / debiased 2.36k / pruned 2.77k rows.
