# SOL_SELECTION_SEMANTIC_REVIEW_HANDOFF-r10 — 2026-W40 (Muse r10, 2026-10-10Z)

Status: `SOL_SELECTION_SEMANTIC_REVIEW_READY` candidate — Sol independently reviews corrected counts, time
verdicts, deeper consumption, and the redesigned dossier before any Selection acceptance. **REVIEW_PENDING;
NO Selection acceptance/checkpoint; NO Architecture/Draft/Human action.** Canonical state stays `EVIDENCE_REVIEWED`.

## 1. Identity, ancestry, allowlist, readback, invariants

- Starting HEAD `9b8f8e8cd6a19c25f1ca4a3c79a1d2efb74a7b4c` / Tree `5f1efc5b98ab7102830994465b1fe04c5cb64bc1`
  (remote read-only match; local ff-only sync, NO reset). Reviewed main `afdb3df3faa20af3bb5798be429bba8dbd2100b1`
  (match). R9 ancestor PASS.
- Final HEAD / Tree: filled at commit (normal commit, non-force ff push, remote read-back verified).
- Changed-file allowlist (all `sources/2026-W40/`, NO Core/branch/Gate/State writes):
  - `execution/selection/selection-proposal-r10.json` (NEW; summary 20/8 fix only) + `count-report-r10.json` (NEW,
    machine recomputation) + `candidate-id-crosswalk-r10.json` (NEW, 35 mappings) + `selection-dossier-r10.md`
    (NEW, redesigned) — r9 files + matrix staging + preview preserved as history
  - `collectors/primary/runs/20261010T080000Z-muse-r10/` (time log + 2 excerpts + consumption log + run/index)
  - `execution/errata/checkpoint-material-count-r10.md` (NEW, non-mutating C01)
  - `execution/sessions/muse-w40-r10-20261010.md` (NEW) + this handoff + `execution/index.md`
- Preserved byte-identical: 37 Discovery (+acceptance), 37 Screening acceptance, 35 canonical tasks, Evidence
  acceptance (`0a62346f…`), BOTH Views acceptances (`60b622f6…`, `1effd744…`), Ledger, Completeness, Stage
  checkpoint, State, Grok Raw, Daily X 64, W39 HOLDs.
- State: `EVIDENCE_REVIEWED / stage:selection`; Selection/Architecture/Human pending.

## 2. Counts 28=20/8 + Matrix/ID/SHA crosswalk + validator output (S01/S02)

- Recomputed (no hand counts): proposal assignments AND Core preview BOTH give 35 = 28 SELECTED
  (20 PRIMARY / 8 SUPPORTING) + 1 INSPECT + 4 HOLD + 2 REJECT (`count-report-r10.json`, match=true).
  Authoritative PRIMARY/SUPPORTING membership is ONLY in `count-report-r10.json` (machine-recomputed) and
  `candidate-id-crosswalk-r10.json` (35 mappings) — no hand-typed slug list is authoritative here.
- Matrix staging (frozen-derived from accepted Evidence/Views/Ledger/Completeness, 35 rows, self-validate PASS)
  + preview `selection-preview-r10.json` (Core `validate_selection` PASS exit 0; dgx mapped INSPECT→NONE/null
  for Core-validity; status ESTABLISHED ONLY as isolated noncanonical preview, NOT Stage approval).
- Crosswalk `candidate-id-crosswalk-r10.json`: 35/35 r9-slug → Core candidate_id + evidence_task_id +
  evidence/view SHAs + materiality. No false PASS (preview path/name say review-only throughout).

## 3. Four time verifications (T01/N01) — ALL preserve HOLD/unadmitted; NO scope change

- AstaBrief: Ai2 RSS day-only + page head dateless + HF mirror 15:19:50Z (mirror ≠ original) → HOLD.
- AutoSynthData: HF JSON-LD 04:01:31Z = same platform instant Sol already ruled non-issuer-proof → HOLD.
- Web Search API: page day-only + RSS 13:00Z, but Clef control (RSS 13:00 vs actual 15:34:02Z) proves RSS times
  unreliable → unadmitted. Topic overlap noted (P8) for IF-ever-proven case.
- Pi harness: page day-only + RSS 00:00:00 → unadmitted. Overlap noted (P3/P6).
- NO `selection-scope-delta-r10.md` (contract: file only on positive proof; none obtained). No Discovery/
  Screening/Evidence/Materiality reclassification; no completeness manufacture. Full anchors in time log.

## 4. Five deeper readings (E01) — locations, deltas, NO contradictions

- Olmo-core 3: report PDF text extracted (570KB; metadata 11 authors, Oct 1 creation); FSDP→DDP+EP/PP/dist-opt,
  NVL8-B300 12.9B→1.2T/512GPU, 858 TFLOP/s/GPU, DeepEP-v2 2.38T, MXFP8 +21%, Token Gerrymandering + overlap lessons,
  full ToC §§2–20 verified. Blog-2.7× stays blog-level; §14 cells/§§16–20/code pending (Selection-depth).
- CLM: App.D–G consumed (ContextBench design, baseline configs, Qwen-size ablations, length-awareness buckets) +
  repo README (Harbor CLI, module layout, CC BY-NC 4.0, ContextBench soon); code internals unopened.
- Guard v2: V.4 (MiniCheck p≈0.13 NS), V.5 (108/173/144 table), V.6 (50/50, CI note), V.7 (Gemma-4-E4B IS named —
  partial revision of r7 withdrawal note; gpt-5.4 withdrawal STANDS), VI–IX + App.A–C consumed.
- FLUX: Image-SKU open weights NOT found (FLUX.1/2 families + Action only; SKU API-only) — SKU pins stay pending.
- MCP Auth: README fully read (split roles, RFC 9728, hash-only storage, handler-owns-enforcement, standards list);
  per-doc pages pending; threat boundary STANDS.
- Delta vs accepted Cards: NONE contradictory → NO delta proposal filed (per §4 rule). Consumption log + 2 excerpts
  archived with SHAs.

## 5. Revised package/depth + P6 alternative + duplication/counterfactual (A01/A02)

- Per dossier r10: P6→P6a (training-methods-systems: ContextLM/Olmo-core; AutoSynthData conditional) + P6b
  (evaluation-execution-infra: AgentPerf/OpenTTS/RL-Env); P2a/P2b rename-split; P5 five subsections; P7 split +
  Relay cross-cutting; P8 digest (PRIMARY=0) with DGX conditional-exclude proposal (Sol decides).
- Duplication map (DevDay spine, decision-model separation, no cross-vendor ranking, license splits, date splits)
  + strong-omission counterfactual (no 30th event; depth-only gains) + compression guard (28-item spine).
- Per-package depth/budget with mechanisms/metrics/comparisons/limits/sources/relative space; no page forcing.

## 6. Prior authority intact + erratum (C01/C02)

- Checkpoint/State/old-SHA untouched; erratum file records MATERIAL30-prose vs canonical-29 ruling (free-text
  non-authority). Completeness all-37 traceability is frozen-Core provenance mechanics; substantive scopes 31/29/2
  stand (C02, no action).

## 7. Terminal

- `SOL_SELECTION_SEMANTIC_REVIEW_READY` candidate (REVIEW_PENDING). NO scope change required (T01/N01 all
  negative → no delta file). Sol: approve dossier/packages for Architecture input, or issue targeted repair.
  CV2-DM-016 OPEN_CORE.
