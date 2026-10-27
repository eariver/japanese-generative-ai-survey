# Final handoff — `MUSE_W43_EXACT_PDF_READY_FOR_HUMAN_PUBLICATION_PREVIEW_GO` (2026-10-28)

## 1. Terminal state

- Work branch `weekly/2026-W43-v2-work`, State `RELEASE_CANDIDATE`,
  `human_gates.publication_preview = pending`, `terminal_reason = HUMAN_GATE_REACHED`,
  `exception_gate.inactive`. No Preview approval recorded; no Freeze/merge/tag/Release.
- Three trusted operator-bridge transitions, all SUCCESS with bot output commits:
  - ARCHITECTURE_ESTABLISHED → DRAFT_COMPLETE: run 40539057751, bot `ada687453`,
    checkpoint `orchestration/v2/checkpoints/ARCHITECTURE_ESTABLISHED.json`.
  - DRAFT_COMPLETE → VALIDATED_DRAFT: run 40542474497, bot `b97ae5930`,
    checkpoint `orchestration/v2/checkpoints/DRAFT_COMPLETE.json`.
  - VALIDATED_DRAFT → RELEASE_CANDIDATE: run 40542944795, bot `319549499`,
    checkpoint `orchestration/v2/checkpoints/VALIDATED_DRAFT.json`.

## 2. Immutable candidate (all bytes verified at terminal)

- PDF `surveys/weekly/2026-W43/main.pdf`: SHA256
  `b09fd1813a9095b2efa03a43f993c1b95b4e8bb304b0df33062f7895239f9165`,
  486967 bytes, 22 A4 pages. Epoch-pinned deterministic build (runs 2–3 identical).
- TeX `surveys/weekly/2026-W43/main.tex`: `3fa6ca3b…` (r8 `4ed553e5…` + 4 proof-mark lines).
- Candidate `sources/2026-W43/publication/v2/publication-candidate-v2.json`:
  `READY_FOR_PUBLICATION_PREVIEW`, `b006f6df…`.
- Authorities: manuscript `079e07ce…`, quality PASS, semantic 11/11, visual 2/2,
  surface review `0a584f2e…`, gate PASSED 0 blocking.
- General independent verdict: `GENERAL_W43_EQUIVALENCE_PASS` (P0 0 / P1 0 / P2 6 bounded),
  report `execution/audits/general-w43-r8-to-candidate-20261028.md`, binds PDF `b09fd181…`.
- Baseline r8 proof untouched: PDF `abd5b99b…` (487351B, 22p).

## 3. Refs (verify at handoff commit)

- Reviewed main: `041a08dfef3112643cbf85b4a86a7b6f9128aed6` / `a134dc36…`.
- Frozen Core v2: `774dd39a951c9ac3818e83dfffd4c7666efb0a20` / `cd46a6f7a…`.
- Final work HEAD/Tree: read back after push (below).

## 4. AFTER-GO runbook (DO NOT execute before explicit Human GO on exact PDF `b09fd181…`)

1. Human GO must name the exact Candidate (`b006f6df…`) / PDF (`b09fd181…`).
   Then `RECORD_PUBLICATION_PREVIEW_APPROVAL` via first-party operator transport
   (immutable request-only commit on this branch + Issue #448 `/survey-core-execute`),
   with durable reviewed-commit pin and actual Human text/date (never invented).
2. Under canonical identity `weekly/2026-W43`, run `RELEASE_CANDIDATE → FROZEN`
   with exact PDF freeze record / release manifest. Only narrowly scoped
   separately approved compat for a genuinely repeated frozen-validator admission
   flaw; no new Owner approval invented here.
3. Normal history-preserving PR to main; verify exact FROZEN State + PDF/Source
   Manifest/Release Manifest on main; dispatch
   `.github/workflows/survey-production-v2-release.yml` with exact
   `issue_id`, `production_state_sha256`, `release_manifest_sha256`,
   `release:2026-W43` (check actual workflow inputs first). DO NOT start pre-GO.
4. Verify published Release asset SHA == Human-approved PDF SHA; close provenance
   via first-party flow/PR. The exact-PDF GO is the one normal publication gate;
   no routine second Human Freeze/Release gate.
5. If any post-GO change alters PDF/source SHA, return to Human for a new exact-PDF GO.
