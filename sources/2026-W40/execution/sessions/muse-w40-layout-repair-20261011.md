# Survey Production session — muse-w40-layout-repair-20261011 (Owner-authorized r3 layout-only → fresh Preview)

Issue: `2026-W40`
Executor: Muse (bounded execution, edition-local only)
Owner authorization: `execution/human-authorization/2026-10-11_owner-w40-r23-publication-preview-request-changes-r3.md` (explicit 「承認します」 to Sol's rev-3 question; no invented timestamp)
Branch: `weekly/2026-W40-v2-work` (existing only)
Started: 2026-10-11 JST

## 0. Read-only preflight (all PASS)

- Remote HEAD `fd679a3e…` / Tree `2e065554…` / main `afdb3df3…` — match. Local HEAD identical; one pre-existing unstaged ledger diff left untouched throughout (out of scope, never staged).
- State `RELEASE_CANDIDATE / PUBLICATION_PREVIEW / HUMAN_GATE_REACHED`, arch APPROVED, Preview pending/null; index ARCH-r1 APPROVED + PREVIEW-r1/r2 REQUEST_CHANGES; candidate `4be71507…` binding PDF `82f7af37…`; working-tree PDF matched.
- Boundary `DRAFT_COMPLETE` confirmed allowed in config; `needspace` package confirmed loaded in style; claimboundary is breakable (local Needspace push is the lawful control).

## 1. Formal Human Preview REQUEST_CHANGES rev 3

- Unchanged CLI, boundary `DRAFT_COMPLETE`, revision 3, Human Owner, real UTC `2026-10-11T11:55:07Z`, SHA-pinned auth ref, reviewed `fd679a3e` (Gate bytes identical).
- Record `gates/reviews/publication-r3.json`; State `DRAFT_COMPLETE` with draft still passed, validation pending; approval + r1/r2 preserved; 2 downstream checkpoints removed. Committed, pushed, readback — before layout work.

## 2. Layout-only TeX fixes (6 insertions, 0 content changes)

- LAYOUT-01: `\Needspace{12\baselineskip}` + comment before `\section{Open Reasoning}` (head/title/opening kept together).
- LAYOUT-02: `\Needspace{8\baselineskip}` + comment before the P2 claimboundary (box kept unbroken; table/content/citations untouched).
- LAYOUT-03: `\Needspace{10\baselineskip}` + comment before `\section{Enterprise Digest}` (head/title kept together).
- Diff proof: 2 files, +6/−0; content-grep empty. Draft/Synthesis/Evidence/Selection/Architecture/Core untouched.

## 3. PDF + regression (150dpi, 14/14 pages)

- CI run `38137417169` success (log gate clean), artifact `11701871676`, built from layout commit. Exact PDF: 14 pages, 466,202 bytes, `52b752bda7e3a37957ced7f815a4a2cc56bd8883c4579505e76057174e918ca6`.
- LAYOUT-01 fixed ( §2 head/title/deck together p.4); LAYOUT-02 fixed (boundary box unbroken, table above); LAYOUT-03 fixed (§9 head/title together p.9). No new orphans/splits/overlaps/gaps; tables/equations/references intact; prose/citations/numbers identical to r23.
- Surface input SHA identical to r23 (`4f78595a…`) — independent proof of prose-identical regeneration.

## 4. QA + stages + candidate → fresh Preview

- Manuscript/surface/surface-semantic/bundle/semantic/visual/gate rebuilt via unchanged builders; fresh visual review (r23 PASS not inherited).
- Official validations r4 + checkpoints: DRAFT_COMPLETE → VALIDATED_DRAFT → RELEASE_CANDIDATE (`PUBLICATION_PREVIEW / HUMAN_GATE_REACHED`, Preview pending/null).
- Candidate `fd5ee590…` (READY, 14pp). Legacy `validate-state` exit 1 (pre-existing semantics, recorded; governing agent-first PASS).
- No Preview decision, Freeze, Release, merge, or PR. No new branch/force; no Core/upstream/HOLD changes. No further rewrite cycle opened.

## End state

- Terminal: `RELEASE_CANDIDATE / PUBLICATION_PREVIEW / HUMAN_GATE_REACHED`, `FRESH_HUMAN_PUBLICATION_PREVIEW_PENDING` candidate.
