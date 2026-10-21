# W42 primary bundle — Anthropic Scion + ECDSA + METR (bodies consumed, 2026-10-17)

Collector run: `20261017T063300Z-muse-r1` / collector_id `primary-webfetch`
Observed at: `2026-10-17T06:40:00Z`
Capture class: `CLAIM_LEVEL_DERIVED_NOTE__NO_ORIGINAL_BYTES`.

## 1. Official: Redesigning source control at Anthropic (Scion, published Oct 13, 2026) — BODY CONSUMED
- URL: https://www.anthropic.com/engineering/redesigning-source-control
- Published Oct 13, 2026 (in-window). X post 2026-10-13 16:36 UTC in-window.
- Core facts (source-backed):
  - Merges/day: ~2,500 (May 2026) → 30,000+/day (Sep 2026); 10x+ growth.
  - Built Scion in-house VCS + migrated monorepo from git in 5 months; team of 7 (+ Antique review, search, IAM, landing).
  - Monorepo scale: main history ~100 GB; compressed working copy >25 GB; ~25M checkouts/day; naive git would be 600 PB/day.
  - Principles: always-online clients; client-server asymmetry; API-exposed queries; horizontal scalability; cheap incremental lock-free commits; sparse/virtualized checkout by design.
  - Data model: changeset = write-ahead-log entry; changed files vs first parent + content-addressed blobs; derived data (blame/path/skip lists) recursive.
  - Checkout stack: scn client → scion-daemon → scion-cache → scion-servers (Spanner/cloud storage); >99% hit rate per tier.
  - Impact (vendor): infra footprint 200x smaller vs git mirrors; CI checkout seconds not minutes; CI 25% CPU capacity win.
  - Claude role: Mythos Preview + Tag accelerated build; 20x less memory 4x faster ingestion rewrite; hermetic sims/fuzzing; superfans monitoring.
  - Scope honesty: NOT a general git replacement; only for enormous monorepos; no public offering; partner with GitHub/GitLab/OSS.
- Timestamp: IN-WINDOW (Oct 13). AUTHORITY_CONSUMED.

## 2. Official: Claude reveals ECDSA curve origins (published Oct 16, 2026) — BODY CONSUMED
- URL: https://www.anthropic.com/research/ecdsa-curve-origins
- Published Oct 16, 2026 (in-window). X posts 2026-10-16 18:41 UTC in-window.
- Core facts (source-backed):
  - Internal research Claude found P-192/224/256/384/521 seeds = `lrand48()` output seeded by Unix timestamp (not hash of phrase).
  - Method: sliding-bit scan over 34 generator/slice combos; top-bit-zero signature (4/10 seeds all-zero top bits, p=1/5810) → lrand48 (31-bit output).
  - State recovery: brute 2^17 hidden bits; truncated-LCG lattice (LLL) for prime curves (lrand48()>>23); 10 prime seeds share pattern.
  - Timestamps: May 1997–Apr 1998 (prime); binary Feb 1984 reading (halved clock → Apr 17 1998).
  - Base points: 6 curves (P-192 + 5 ANSI X9.62 examples) from FreeLIP/NTL zrandom (seeds 20000–20517, 7 discards, 26-bit limbs mod p); P-224/256/384/521 base points unexplained; B-163 unexplained.
  - Security meaning stated: no break/weakness; backdoor less plausible; no action needed.
  - Repro code on page (Python, CC0). Bounty $36,864 to ISRG.
- Timestamp: IN-WINDOW (Oct 16). AUTHORITY_CONSUMED. Independent crypto verification pending (gap).

## 3. Official: An update on independent evaluators (METR, Oct 15, 2026) — BODY CONSUMED
- URL: https://www.anthropic.com/news/an-update-on-independent-evaluators
- Published Oct 15, 2026 (in-window). X post 2026-10-15 17:27 UTC in-window.
- Core facts:
  - 6 METR staff onboarded with employee-like access (hardware/office/internal tools); publish without veto (redaction only for customer/privilege/architecture).
  - Three tiers; METR at tier 3. SecureBio reviewing chem/bio chapter; Accenture/Faculty early.
- AUTHORITY_CONSUMED for access model; METR results themselves NOT yet published (no outcome to consume).

## 4. Anthropic safety leads (locators only in this run)
- Investigating unintended model actions (Daily X 10-11 cites anthropic.com/news/investigating-unintended-model-actions): LOCATOR_ONLY, body not refetched. Do not cite details.
- Distillation defenses (anthropic.com/research/distillation-defenses, X 2026-10-12 23:58 UTC in-window): LOCATOR_ONLY.
- Simons Foundation $15M math effort (simonsfoundation.org, X 2026-10-15 21:31 UTC in-window, OpenAI co-funding $5M): LOCATOR_ONLY.
- Treatment: leads for Evidence; no body claims in Discovery.
