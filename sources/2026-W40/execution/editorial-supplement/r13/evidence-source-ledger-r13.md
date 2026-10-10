# r13 evidence-source ledger — two supplemental subjects + DGX reference (staged, NOT canonical)

Status: STAGED_R13 / NON_CANONICAL / TRACEABILITY_ONLY
Supersedes (as working ledger; r12 preserved immutable): `../r12/evidence-source-ledger-r12.md`
Canonical Evidence tasks/Discovery IDs unchanged (see `manifest-r13.md`). Re-retrieval 2026-10-10.
Addresses finding W40-R12-F06 (bounded direct capture/parse of hosted JSON-LD).

## 0. Retrieval method + byte framing (new r13 raw evidence)

- Method: direct HTTPS GET (`curl`, Chrome UA) of the two issuer-org hosted HF article
  URLs, 2026-10-10 (~19:57Z shown by transport; recorded as retrieval date 2026-10-10).
  Full article prose independently re-read via rendered fetch the same day.
- AstaBrief: **169,199 bytes** (exactly reproduces r11's 169,199) but
  SHA-256 `49e4b99ba187973057270560437726f8652327ccf1cdb3d78cde1c5bd3898e5c`
  ≠ r11 `d440b90083…e9ea9e`.
- AutoSynthData: **210,484 bytes** (exactly reproduces r11's 210,484) but
  SHA-256 `1e5af1b368ba9ca116118efdc01b76bf4f1a66cb3d94108560cbd7300ae3deaf`
  ≠ r11 `d84a35e696…b56a44`.
- Interpretation (honest, Sol r11-conformant): byte-count stability with hash drift
  PROVES dynamic page framing (request IDs, relative timestamps, vote/comment counts —
  e.g. AstaBrief upvotes rendered 28, DPO Mix page "Updated 8 days ago"). Raw-byte
  hashes are therefore framing-sensitive and NOT clocks; the embedded JSON-LD strings
  remain authoritative and are VERBATIM re-verified below.
- Raw bytes are NOT committed to the repo (r11 policy preserved — hashes recorded here
  for independent re-check against the issuer pages). Transport worked copies held only
  in local `/tmp` outside the repo.

## AstaBrief

| Field | Value (r13 re-verified) |
|---|---|
| Official article URL | https://huggingface.co/blog/allenai/astabrief |
| Canonical link | verified (`rel="canonical"` → same URI, re-parsed r13) |
| Hosting org path | `/blog/allenai/` → HF org `allenai` (page exists, `allenai (Ai2)`) |
| Author account | https://huggingface.co/Ai2Comms (page exists, `Ai2Comms (Kyle Wiggers)`) |
| JSON-LD author/creator | Person `Kyle Wiggers` → `https://huggingface.co/Ai2Comms` (re-parsed r13, matches r12) |
| JSON-LD headline | `Open-sourcing AstaBrief, the fast report-generation model in Asta` (re-parsed r13) |
| JSON-LD datePublished | `2026-10-02T15:19:50.340Z` (re-parsed r13, matches r12) |
| JSON-LD dateCreated | `2026-10-02T15:19:50.340Z` (re-parsed r13, matches r12) |
| JSON-LD dateModified | `2026-10-02T15:22:07.584Z` (re-parsed r13, matches r12) |
| JSON-LD publisher | `Hugging Face` (platform operator, NOT issuer — re-parsed r13) |
| Minimum quoted JSON-LD excerpt (new) | `"datePublished": "2026-10-02T15:19:50.340Z"` with `"dateCreated": "2026-10-02T15:19:50.340Z"`, `"dateModified": "2026-10-02T15:22:07.584Z"` |
| First-person prose | re-verified r13 from live article (`We built AstaBrief 8B…`, `we're also open-sourcing it…`) |
| Corporate counterpart | https://allenai.org/blog/astabrief (carried r12; RSS day-only, NOT hour proof) |
| Weights | `allenai/AstaBrief_8B` Apache-2.0; created 2026-02-09; lastModified 2026-10-03 (carried r12 HF-API; NOT re-queried r13) |
| SFT checkpoint | `allenai/AstaBrief_8B_SFT` Apache-2.0; created 2026-09-10 (carried r12) |
| Data (card-verified r13) | `allenai/AstaBrief_SFT_Mix` 39.5k + `allenai/AstaBrief_DPO_Mix` 6,622 rows; CC-BY-NC-4.0; density<0.25→39.5k per card prose; third-party-terms sentence per card license section |
| Access status | article + model/dataset pages publicly readable 2026-10-10 |
| Author/platform distinction | issuer = Ai2 (org path + account + prose); platform = Hugging Face (publisher field, hosting clock) |
| Explicitly unresolved | independent repro of quality/speed; repo LICENSE-file pin; rerun vs current frontier; HF-API timestamps not re-queried r13 |

## AutoSynthData

| Field | Value (r13 re-verified) |
|---|---|
| Official article URL | https://huggingface.co/blog/ServiceNow-AI/autosynthdata |
| Canonical link | verified (`rel="canonical"` → same URI, re-parsed r13) |
| Hosting org path | `/blog/ServiceNow-AI/` → HF org `ServiceNow-AI` (page exists) |
| Author accounts | esakkivel / shruthan-r / dtanow / davasam, each `Follow / ServiceNow-AI` badged (re-verified r13) |
| JSON-LD authors | same 4 persons with same account URLs (re-parsed r13, matches r12) |
| JSON-LD headline | `AutoSynthData: Generating Training Data for Enterprise Agents` (re-parsed r13) |
| JSON-LD datePublished | `2026-10-02T04:01:31.290Z` (re-parsed r13, matches r12) |
| JSON-LD dateCreated | `2026-10-02T04:01:31.290Z` (re-parsed r13, matches r12) |
| JSON-LD dateModified | `2026-10-02T04:05:48.837Z` (re-parsed r13, matches r12) |
| JSON-LD publisher | `Hugging Face` (platform operator, NOT issuer — re-parsed r13) |
| Minimum quoted JSON-LD excerpt (new) | `"datePublished": "2026-10-02T04:01:31.290Z"` with `"dateCreated": "2026-10-02T04:01:31.290Z"`, `"dateModified": "2026-10-02T04:05:48.837Z"` |
| First-person prose | re-verified r13 (`At ServiceNow CoreAI, we built AutoSynthData…`) |
| Standalone release | NONE independently identified in bounded checked sources at retrieval time (F04 wording; r12 HF-API/site-search scope carried, not re-run r13) |
| Background dataset | `ServiceNow-AI/EnterpriseOps-Gym` (created 2026-02-28, Apache-2.0, arXiv:2603.13594) — SEPARATE |
| Reported results | Hybrid +7.2pp/35%, verifier 63.01%→68.55%, 59% gap closed, 2,000 samples/~18h/epoch 5; ITSM 18.77%→27.18% (1,994 samples/66h, ran FIRST); publisher-measured, SFT-only, Gym-scoped (article prose re-verified r13) |
| Access status | article + Gym dataset publicly readable 2026-10-10 |
| Author/platform distinction | issuer = ServiceNow CoreAI (org path + badges + prose); platform = Hugging Face |
| Explicitly unresolved | code-level adapter detail; cross-env generalization; teacher registry proof; independent repro |

## DGX Spark (reference only — disposition resolved in preview-r13, no re-retrieval in r13 scope)

- Evidence task `evidence:2026-W40:4eddb6eea3df05f9` / candidate `candidate:2026-W40:071ac2e6d62319fd`;
  source `primary:blogs.nvidia.com/blog/local-ai-dgx-spark-64gb-sync/` (vendor article,
  calendar 2026-10-02; delegated page-metadata read 13:00:39Z per r6/r7 evidence record).
- NVIDIA page NOT re-fetched in r13 (out of bounded scope; r6/r7 record stands as
  `CLAIM_LEVEL_DERIVED_NOTE`). No new DGX raw evidence is claimed.
- Factual attributions retained from audited record: 64GB SKU + Sync Cluster Assistant
  announced; Oct 23 third-party availability ($4,999) FUTURE, not W40 shipping; do not
  conflate preorder with shipment.
