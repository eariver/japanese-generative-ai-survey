# W42 r19 validation report (read-only frozen re-verification + print QA + invariants)

Date: 2026-10-18 JST. No Core/shared-root/main change. No canonical overwrite. No stage transition. No Human Gate operation. No r18 master modification.

## Frozen validators (read-only re-verification on r18 master bytes; print changes claim no new acceptance)

- `draft-check` re-run against UNCHANGED r18 proposals (7/7 `{"passed": true}` reproduced; receipts align with r18 report). `synthesis-check` input-SHA `4cb2b01a…` PASS reproduced. These verify the frozen master, NOT new r19 content (r19 authors no proposal JSON; body text frozen).
- r18 master counts reconfirmed: 136 PARAGRAPH / 25,015 chars / 7 TABLE / 7 NOTE / 7 HEADING / 157 reader blocks; 90 keys / 19 aliases / 177 rows (authority blobs unchanged; see evidence receipt below).

## Print QA (independent of frozen checks; log-only never suffices)

- r19 TeX built from r18 Reader bytes: 150/150 non-TABLE blocks byte-present; 7/7 table captions + cell content preserved (tabularx print transform only); NO sentence inserted/deleted (only Table-7 code relocation + `\needspace` pagination control + bib display strings + stamp blocks).
- Custom scans: body internal-ID pattern 0 hits; printed-bib machine-phrase list 0 hits (TeX strings AND extracted PDF text); MD-wrapper boilerplate 0 hits; all 90 Bxx cited; B28/B57 keep-together present.
- Diagnostic: 21pp, 509,010B, SHA256 `7aced2839c0e41e344e164aa884dd33462c6625920f91110d0424269ec74ec6e` (deterministic epoch, final two byte-identical); TeX 95,034B; log 77,227B; 0 overfull/underfull/errors/missing-glyphs/undefined (pkg-info line only); HaranoAji + LM.
- Visual: ALL 21 PNGs individually opened (cover stamps ×3 lines unbroken; 7 tables in-chapter; Table 7 p17 in-flow with complete t7-07 below and completed t7-17 above — no bisection, no orphan, no cross-chapter float; 7 notes; bib p18–p20 clean alias format with significance notes only; B28 complete on p19; B57 kept together on p20; p21 stamp block contiguous + JP line, terminal stub documented). 3 split contact sheets (~2.2MB each).

## Evidence master / hash receipt (r18 authority, read-only)

- reader-preview-r18.PROPOSED.json blob `fc4fd9f2…`; P1 `b6e1c7cc…` P2 `badbbbd0…` P3 `d81023c1…` P4 `e8b7aa46…` P5 `bde64f2c…` P6 `aedfb8f4…` P7 `9e8924ea…`; bib-map `44494d98…`; ledger `d7503523…`. All unchanged (working-tree clean except new r19 paths; r18 dir diff empty at commit).

## Canonical invariants (verified at commit)

- production-state blob `63edc922…` (`DRAFT_COMPLETE`/approved/pending); checkpoints/approvals/review-index; canonical Draft/Synthesis v10.0; Evidence/Views/Materiality/Selection/Architecture; r11–r18 execution bytes; main + Frozen Core. All untouched.

## Residuals

p21 terminal stamp stub (honest, documented); B57 intra-entry ASPI/RE wrap (kept together, readable); effective area UNMEASURED (no fake metric); 83/90 HTTP UNVERIFIED carried from r17 (no new reachability claims).
