# Sol Decision Record — TS-003 Paper Review Technical Fidelity Bounded Repair

- Paper Review: `REQUEST_CHANGES / HOLD`
- Sol decision: accepted (Muse does not re-derive editorial policy; repairs follow this Sol decision exactly)
- Blocking findings: PR-01 / PR-02 / PR-03
- Prior R02/R04/R05: closed (PASS / CLOSED; complete non-regression enforced)
- Accepted primary-source basis:
  - PR-01 DETR: `https://arxiv.org/pdf/2005.12872` (original paper §4, training schedule paragraph)
  - PR-02 POPE: `https://aclanthology.org/2023.emnlp-main.20/`
  - PR-03 MMBench: `https://arxiv.org/abs/2307.06281`, `https://github.com/open-compass/MMBench`
- Evidence: VM-D010 / claim-3 (PR-01), VM-D079 (PR-02), VM-D081 (PR-03)
- VM-D010 evidence wording precision issue: accepted Evidence claim-3 retains the compressed
  `300〜500エポック / 3日間` phrasing; the staged PR-01 split (300-epoch AdamW baseline ≈3 days on
  16 V100 vs 500-epoch Faster R-CNN comparison setting) is an editorial precision refinement against
  the primary source, recorded in `technical-fidelity-ledger.json`. Evidence body unchanged.
- Technical correction scope only (4 exact replacements on staged L86/L391):
  - PR-01 L86: DETR schedule conflation → 300ep base + ≈3 days + 500ep comparison split
  - PR-02 L391: `POPEは投票型…` → yes/no polling wording
  - PR-03 L391: `MMBenchは3000件超の日英設問…` → EN/ZH wording; `判定依存と英中の言語範囲…` → dependence + bilingual-range wording
- Non-blocking record-only: Issue #534 terms (`模型`, `基線`, `hardware`) counts verified unchanged, not corrected.
  Issue #559 recorded as related context; the issue is NOT closed by this repair.
- Shared Core v2 unchanged (no repair/change; `REVIEWED_CORE_CHANGE` not reused).
- Canonical authority unchanged (`surveys/special/vision-multimodal-2026/` read-only; prior staging read-only basis).
- Formal Human Gate not decided (this Paper Review is an editorial review distinct from the formal Core
  Human Gate record; Production State Publication Preview remains pending).
- Publication Candidate HOLD (no Candidate/Freeze/Release; no new branch/force-push/reset).

## Repair outputs (new staging only)

`sources/SP-vision-multimodal-2026/execution/reader-paper-fidelity-repair-20261009/`

- `apply_paper_fidelity_repair.py`, `validate_paper_fidelity_repair.py`
- `main.tex`, `references.bib`, `jgaisurvey.sty`, `main.pdf` (real TeX rebuild)
- `before-after.json`, `technical-fidelity-ledger.json`
- `citation-evidence-check.json`, `pdf-qa.json`, `text-diff.txt`
- `qa-p05-05.png`, `qa-p31-31.png` (corrected-page visuals from final PDF exact bytes)
- `session.md`, this record

## Terminal boundary

`PAPER_REVIEW_TECHNICAL_REPAIR_STAGED` / `PR_01_PR_02_PR_03_CORRECTED` /
`CANONICAL_AUTHORITY_PRESERVED` / `CORE_V2_UNCHANGED` /
`INDEPENDENT_DIFFERENTIAL_REVIEW_PENDING` / `PUBLICATION_CANDIDATE_HOLD`. STOP.

## VF-01 / VF-02 QA Evidence Closure (2026-10-10; verdict adopted as Sol)

Prior sections above are preserved unchanged as the repair history.
This section records QA evidence closure only; technical body, PDF binary,
Core v2, and all authority records are unchanged.

- Accepted verdict: `STAGED_TECHNICAL_FIDELITY_VERIFICATION_INCOMPLETE`
- PR-01 / PR-02 / PR-03: `TECHNICAL_CONTENT_ACCEPTED` (no body edit in this closure)
- VF-01 (binary-to-QA binding): CLOSED — fixed `main.pdf`
  (`b2de8449…`, 708782 bytes, 39 pages) re-verified byte-identical at start and end;
  validator now computes PDF SHA/size/pages from the real file and FAILs on mismatch;
  `qa-provenance.json` binds PDF/TeX/Bib/style/BBL SHAs to every QA artifact hash and both
  QA image hashes; `pdf-text-verification.json` stores the real 39-page extraction
  (full-text SHA `e2d09fa3…`, per-page hashes) with PR new-present/old-absent checks;
  `visual-source-manifest.json` binds each QA image to source PDF SHA + page + renderer/options.
- VF-02 (build/extraction evidence): CLOSED — existing `main.log`/`main.bbl` captured with
  generation history (23:25 JST build, LuaHBTeX 1.24.0, Biber 2.22, 124 citekeys, 0 warnings);
  isolated `REPRODUCTION_RUN` (`/tmp/opencode/repro-paper-fidelity`) from identical input SHAs
  rebuilt 39 pages / 708782 bytes / identical BBL / byte-identical extracted text and p05/p31
  renders (PDF bytes differ only by CreationDate/ModDate timestamps); recorded in
  `build-reproduction-record.json`. Rebuilt PDF was NOT written over the formal `main.pdf`;
  existing vs reproduction evidence are kept separate in that record.
- Visual QA record: mechanical preflight (computed PASS) and human observation are now separate.
  REVIEWED: p.5 (`qa-p05-05.png`) and p.31 (`qa-p31-31.png`) with per-image observation, no defects.
  All other pages: `NOT_REVIEWED` — no claim of full 39-page human review is made.
- Unverified / out of scope: human review of the remaining 37 pages; any future formal Human Gate
  decision; Publication Candidate remains HOLD.

## Closure terminal

`VF_01_VF_02_EVIDENCE_READY` / `PAPER_CONTENT_UNCHANGED` / `PDF_BINARY_UNCHANGED` /
`CORE_V2_UNCHANGED` / `INDEPENDENT_QA_CLOSURE_REVIEW_PENDING` / `PUBLICATION_CANDIDATE_HOLD`.
