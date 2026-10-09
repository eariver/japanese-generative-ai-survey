# Discovery observations — VM-O13 D12 computer use (BOUNDED)

Issue: `SP-vision-multimodal-2026`  |  Collector run: `vision-multimodal-discovery-r1`  |  Observed: `2026-09-30T00:38:52Z`

Status: `RAW_OBSERVATION / PRE_SCREENING / SUMMARY_CAPTURED` — abstract/page-level capture; full-body consumption is Evidence-stage work. No claim beyond the cited source is established here.

Lane framing: Mind2Web-class web-phase and SeeClick-adjacent mobile grounding are predecessor/downstream-validation CONTEXT (no standalone records): web-phase != OS-phase. Vendor computer-use deployments (Gemini 2.5 Computer Use / Claude / Operator-class) are DEPLOYMENT pointers with exact 2026 authority to bind at Evidence; no mechanism claims from product pages. Safety/audit reporting is eval-metadata only.

## VM-D090 — OSWorld (Xie et al.)
- Locator: https://arxiv.org/abs/2404.07972
- Source type: `arxiv_primary` | Published: `2024-04` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O13` | Modality: `screenshot` | Role: `anchor`
- X axes: `X02`, `X04`
- Claim notes: Real-OS multimodal-agent environment + 369-task benchmark; grounding-bottleneck thesis (best 12.24% vs human 72.36%); NeurIPS 2024. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Short-horizon scope; long-horizon thesis needs 2.0-side sources.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 absent
- repo: https://github.com/xlang-ai/OSWorld

## VM-D091 — OSWorld 2.0 (Yuan et al.)
- Locator: https://arxiv.org/abs/2606.29537
- Source type: `arxiv_primary` | Published: `2026-06` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O13`, `VM-O16` | Modality: `screenshot` | Role: `current-case`
- X axes: `X02`, `X03`, `X04`
- Claim notes: 108 long-horizon workflows; 1.6h median; ~318 vs ~30 tool calls; best 20.6% binary / 54.8% partial; token-cost curves; safety-audit metadata. State-management thesis. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: v2 Jul 2026; strictest binding in volume (model+thinking+tool+steps+release). Author-measured.
- TS-001/TS-002 overlap: TS-001 partial / TS-002 absent
- Current-case role: `EVALUATION_CASE (author-measured) + DEPLOYMENT_CASE (open env)`

## VM-D092 — SeeClick / ScreenSpot (Cheng et al.)
- Locator: https://arxiv.org/abs/2401.10935
- Source type: `arxiv_primary` | Published: `2024-01` | Access: `ARXIV_ABSTRACT_VERIFIED`
- Obligations: `VM-O13`, `VM-O16` | Modality: `screenshot` | Role: `eval-anchor`
- X axes: `X02`
- Claim notes: 600+ screenshots / 1,200+ instructions; mobile+desktop+web; text + icons/widgets; grounding-pretraining to downstream-agent gains; ACL 2024. Distinct: pure element-localization accuracy. [retrieval: ARXIV_ABSTRACT_VERIFIED; full-body consumption at Evidence stage]
- Limitation: Currency check at Evidence (v2/Pro-class successors named as check, not entries).
- TS-001/TS-002 overlap: TS-001 absent / TS-002 absent
- repo: https://github.com/njucckevin/SeeClick
