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
