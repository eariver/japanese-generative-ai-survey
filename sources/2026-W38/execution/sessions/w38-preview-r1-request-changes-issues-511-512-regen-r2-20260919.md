# Survey Production session — w38-preview-r1-request-changes-issues-511-512-regen-r2-20260919

Issue: `2026-W38`
Started: `2026-09-19 JST` (execution request `sol-w38-publication-preview-r1-request-changes-issues-511-512-no-core-20260919.md`)

## Starting authority

- Branch: `weekly/2026-W38-v2-work`
- Exact Starting SHA: `dd78437e519a8a5fdff43721bfb10b99683713e6` (remote HEAD/tree/parent/main/Production Line guards all PASS read-only pre-write; parent `a578063bd`, parent tree `968370d2`; main `2ab91516`/tree `279ecbd9`; Production Line `774dd39a`/tree `cd46a6f7a`; State RELEASE_CANDIDATE/PUBLICATION_PREVIEW/HUMAN_GATE_REACHED, arch approved, preview pending; r1 Candidate `43c7d33a`/PDF `767f4d98` 344241B/11p; Architecture triple SHAs unchanged)
- Local clone one commit stale (`7c9a39587` vs remote `dd78437e5`); bounded fetch + fast-forward-only sync (ancestor verified, no merge commit, local `main` untouched `3e3eebe0`), then guards re-verified.
- Execution contract: `execution/requests/sol-w38-publication-preview-r1-request-changes-issues-511-512-no-core-20260919.md`
- Human decision: `REQUEST_CHANGES` on Publication Preview r1 for Issues #511 (Jev temporal authority) and #512 (25-row ledger auditability), imported authority with explicit instruction to repair without Core v2 modification; boundary `ARCHITECTURE_ESTABLISHED`.
- Reviewed r1 authority: commit `f2306ce4`, Candidate `43c7d33a`, PDF `767f4d98` 344241B/11p.

## Actions actually performed

- Recorded Human Preview r1 `REQUEST_CHANGES` via canonical `survey_human_gate_v2.py request-publication-preview-revision` (revision 1 from index, reviewed `f2306ce4`, reviewed-by Human Owner, reviewed-at `2026-09-19T08:00:23Z` actual wall clock, boundary `ARCHITECTURE_ESTABLISHED`). Machine record: `gates/reviews/publication-r1.json` + review index. State rewound to `ARCHITECTURE_ESTABLISHED` / `stage:drafting-synthesis`; Architecture approval retained; downstream checkpoints removed by Core (recreated on re-advance).
- #511: independently re-fetched the TypeSafe first-party page twice (body renders Sep 15, front matter Sep 18 artifact — disclosed as non-overriding worker observation); implemented the contract §8 two-date model via append-only `collectors/primary/corrections/typesafe-jev-temporal-correction-20260919.md` (binds original SHA `9f9c904d`) + machine-readable `evidence/v2/corrections/typesafe-jev-temporal-correction-r1.json` (blog `2026-09-14` DAY, founder post `2026-09-15T18:17:52.151Z` bound separately). Original collector/Evidence/Architecture bytes untouched.
- #512: generated the 25-row public manifest from the canonical row ledger with independently recomputed Snowflake UTCs (25 unique, 23/2, 15 = 7+3+5, all UTCs match, no internal vocabulary): `surveys/weekly/2026-W38/community-observation-ledger.md` (SHA `fb150df7`); committed as `26284fd2e`, pushed, read back byte-identical.
- Citation-form conflict: the contract-preferred commit-pinned blob URL trips frozen gate `RSG-LEX-INTERNAL-PATHS`, and suppression plumbing is proven broken in frozen Core (W36 defect record) with Core modification prohibited. Followed the Human-accepted W36 convention: full 25-row table mirrored at `https://github.com/eariver/japanese-generative-ai-survey/issues/512#issuecomment-5740537184` (posted `08:38:53Z`), bibliography cites that stable public surface; manifest file retained as audit artifact; existing 9 X citations unchanged. Gate scans suppression-free (0/0).
- Regenerated Draft r2 from approved Architecture (7/7 packages/results + synthesis PASS; packages byte-identical except Jev result prose) with measured wall-clock input stamp; validated and advanced `ARCHITECTURE_ESTABLISHED -> DRAFT_COMPLETE` with actual wall-clock stamps.
- Updated reader TeX (Jev two-date model in section/deck/synthesis/source-notes/bib with Sep 14 note + separate founder citation; frontmatter chronology fix caught via PDF extraction re-check; source-notes manifest pointer; bib ledger-mirror entry). Lexical guard PASS 13/13.
- CI `build-weekly-survey` success on every TeX push (runs `35432085874`, `35432281280`, `35432581167`); pinned final PDF (`main.pdf`, 11 pages, 347330 bytes, SHA `3829c166`, artifact `10581840234`).
- Built manuscript (27 must-cover + 2 requirements), 3 deterministic checks (7/7, CI preflight, 20/20 citations), bundle, pre-TeX surface, Worker surface semantic PASS (5 checks), gate PASSED (0/0), Worker semantic/editorial QA (11 PASS) + visual QA (2 PASS, extraction clean) via canonical binders — all suppression-free.
- Stage validations PASS → `VALIDATED_DRAFT` → built candidate (`8aeb4dc4`) → `RELEASE_CANDIDATE` / `PUBLICATION_PREVIEW` / `HUMAN_GATE_REACHED`.
- Production commit `a55ac5b92` (State + Candidate + Candidate-bound PDF).
- Created Publication Preview r2 shell + dossier (actual wall-clock `08:44:27Z`); no Preview decision; no Freeze/Release.
- No upstream rerun. No Architecture change. No Core change. `main` untouched.

## Deviations / repairs

- One stale frontmatter Jev sentence caught by PDF-extraction re-check and fixed before final CI (extra TeX commit + rebuild; no semantic shortcut).
- One discarded drafting-input stamp (sub-minute guess replaced by measured stamp via clean regen before validation).
- Deliberate citation-form deviation (§12 blob URL → Issue-comment mirror) with full rationale in r2 dossier §4/§12; preferred-form target stays committed/pinned for audit.

## External handoff

- One GitHub Issue comment (#512 ledger mirror, public data only). No Drive use. No connector install.

## End state

- Lifecycle: `RELEASE_CANDIDATE`
- Next action: `PUBLICATION_PREVIEW` (Human decision only)
- Terminal reason: `HUMAN_GATE_REACHED`
- Issues #511/#512: left OPEN for Sol verification
- Session status: `COMPLETE_AT_GATE`
