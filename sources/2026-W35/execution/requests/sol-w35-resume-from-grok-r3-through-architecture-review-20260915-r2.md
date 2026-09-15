# W35 execution instruction — r2 override for GitHub-only Grok Raw authority

Status: `EXECUTION_AUTHORITY / W35_RESUME_OVERRIDE / GITHUB_ONLY_RAW_AUTHORITY`

Date: `2026-09-15 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W35-v2-work`

## 1. Purpose

This request supersedes only the Starting Guard and accepted Grok Raw byte-identity fields in:

`sources/2026-W35/execution/requests/sol-w35-resume-from-grok-r3-through-architecture-review-20260915-r1.md`

All other requirements in r1 remain in force.

Muse/OpenCode still has no Google Drive authority. Do not use or request Google Drive access. All execution authority is repository-local.

## 2. Why this override exists

The Sol handoff commit `182f56a09c032bd41c9ac10b398f8e85771ab661` imported the accepted Grok r3 text into GitHub, but a text-transfer normalization removed exactly one ASCII space in a non-canonical derivative cluster-summary line:

Drive-reviewed source text:

`- Lanes: A, B, G, H, J`

GitHub repository Raw text:

`- Lanes: A, B, G, H,J`

This is the only byte-level difference identified. Applying exactly that one-character deletion to the Drive-reviewed source reproduces the GitHub checkout identity reported by Muse:

- byte count: `21589`
- SHA-256: `5d1ee181cce891f6e944679bd82262e81e3cfa98b545b5e028e00faf782fdc81`

The difference does not alter any post-level ledger row, X URL, timestamp, window classification, disposition, global accounting, or downstream verification obligation.

Do not rewrite the Raw file merely to restore cosmetic whitespace. For all repository execution from this point forward, the exact GitHub repository bytes are the accepted immutable Raw authority.

## 3. Revised starting guard

The Muse invocation will provide the Exact Starting SHA containing this r2 override.

Before any repository write, read-only verify:

- remote `weekly/2026-W35-v2-work` HEAD == Exact Starting SHA supplied in the invocation;
- Exact Starting SHA parent == `182f56a09c032bd41c9ac10b398f8e85771ab661`;
- remote `main` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote `main` tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- repository Raw path exists:
  `sources/2026-W35/external/x/weekly-x-2026-W35/raw/grok-x-result-r3.md`;
- repository Raw SHA-256 == `5d1ee181cce891f6e944679bd82262e81e3cfa98b545b5e028e00faf782fdc81`;
- repository Raw byte count == `21589`.

If any revised guard differs, perform no repository/GitHub write, report expected versus actual, and STOP.

The prior r1 guard values `43b16b9a... / 21590` are superseded and MUST NOT be used as a blocking condition.

## 4. Canonical observation authority remains unchanged

Use the repository Raw post-level ledger as canonical observation authority.

Accepted global accounting remains:

- total unique X URLs: `35`
- `ORDINARY_WINDOW`: `25`
- `BACKGROUND_ONLY`: `0`
- `LATE_BREAKING`: `10`
- ordinary official-account X URLs: `9`
- ordinary independent/non-official X URLs: `16`

The original `~40+ ordinary-window` approximation remains rejected as unreproduced.

Some cluster-level composition counts are derivative editorial summaries only. Recompute any per-cluster count from the ledger if needed.

X remains Raw Observation/community signal, not final technical Evidence.

## 5. Canonical X result recording

Continue with the r1 procedure using the repository-local Raw file.

When `scripts/survey_x_intake_v2.py record-result` records Raw authority, allow it to bind the actual repository bytes:

- Raw path: `sources/2026-W35/external/x/weekly-x-2026-W35/raw/grok-x-result-r3.md`
- actual SHA-256: `5d1ee181cce891f6e944679bd82262e81e3cfa98b545b5e028e00faf782fdc81`
- actual byte count: `21589`
- drive file name for provenance only: `grok-x-result-r3.md`
- observed at: `2026-09-15T03:06:00+09:00`
- imported at: timestamp of commit `182f56a09c032bd41c9ac10b398f8e85771ab661`, normalized by the canonical tool
- result status: `SUCCESS`
- discovery disposition: `DISCOVERY_RECORDED`

Do not attempt to contact Drive to reconcile bytes.

## 6. Resume authority

After this override guard passes, read r1 and continue all remaining r1 instructions unchanged through:

`ISSUE_INITIALIZED -> completed X Source Intake -> DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED -> SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED -> fresh Human Architecture Review pending -> STOP`

Human decisions must not be invented.

The Core-repair / Production-Line / no-main-merge policy from r1 remains fully in force.

## 7. STOP conditions

Normal stop is a fresh Human Architecture Review.

Stop earlier only for a genuine contract failure, unresolved Core defect requiring the defined repair protocol, or any revised starting-guard mismatch above.
