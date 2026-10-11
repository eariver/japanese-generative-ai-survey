# r12 evidence-source ledger — two supplemental subjects (staged, NOT canonical)

Status: STAGED_R12 / NON_CANONICAL / TRACEABILITY_ONLY
Canonical Evidence tasks/Discovery IDs unchanged (see manifest). Retrieval 2026-10-10Z.

## AstaBrief

| Field | Value |
|---|---|
| Official article URL | https://huggingface.co/blog/allenai/astabrief |
| Canonical link | verified (`rel="canonical"` same URI) |
| Hosting org path | `/blog/allenai/` → HF org `allenai` (page exists, `allenai (Ai2)`) |
| Author account | https://huggingface.co/Ai2Comms (page exists, `Ai2Comms (Kyle Wiggers)`) |
| JSON-LD author/creator | Person `Kyle Wiggers` → `https://huggingface.co/Ai2Comms` |
| JSON-LD headline | `Open-sourcing AstaBrief, the fast report-generation model in Asta` |
| JSON-LD datePublished | `2026-10-02T15:19:50.340Z` |
| JSON-LD dateCreated | `2026-10-02T15:19:50.340Z` |
| JSON-LD dateModified | `2026-10-02T15:22:07.584Z` |
| JSON-LD publisher | `Hugging Face` (platform operator, NOT issuer) |
| Raw capture (r11 urllib) | 169,199 bytes; SHA-256 `d440b90083303f3d6a4b5906369f312039098996553bf6a91e369c0599e9ea9e` (framing-sensitive; JSON-LD strings authoritative) |
| First-person prose | verified (`We built AstaBrief 8B…`, `we're also open-sourcing it…`) |
| Corporate counterpart | https://allenai.org/blog/astabrief (exists; RSS day-only `2026-10-02T00:00:00-08:00`; NOT the hour proof) |
| Weights | `allenai/AstaBrief_8B` Apache-2.0; created 2026-02-09; lastModified 2026-10-03 (post-cutoff; NOT announcement) |
| SFT checkpoint | `allenai/AstaBrief_8B_SFT` Apache-2.0; created 2026-09-10 |
| Data | `allenai/AstaBrief_SFT_Mix` (39.5k, CC-BY-NC-4.0) + `allenai/AstaBrief_DPO_Mix` (6.6k); lastModified 2026-09-29 |
| Access status | article + model/dataset pages publicly readable 2026-10-10Z |
| Author/platform distinction | issuer = Ai2 (org path + account + prose); platform = Hugging Face (publisher field, hosting clock) |
| Explicitly unresolved | independent repro of quality/speed; repo LICENSE-file pin; rerun vs current frontier |

## AutoSynthData

| Field | Value |
|---|---|
| Official article URL | https://huggingface.co/blog/ServiceNow-AI/autosynthdata |
| Canonical link | verified (`rel="canonical"` same URI) |
| Hosting org path | `/blog/ServiceNow-AI/` → HF org `ServiceNow-AI` (page exists) |
| Author accounts | esakkivel / shruthan-r / dtanow / davasam, each `Follow / ServiceNow-AI` badged |
| JSON-LD authors | 4 persons (see above) |
| JSON-LD headline | `AutoSynthData: Generating Training Data for Enterprise Agents` |
| JSON-LD datePublished | `2026-10-02T04:01:31.290Z` |
| JSON-LD dateCreated | `2026-10-02T04:01:31.290Z` |
| JSON-LD dateModified | `2026-10-02T04:05:48.837Z` |
| JSON-LD publisher | `Hugging Face` (platform operator, NOT issuer) |
| Raw capture (r11 urllib) | 210,484 bytes; SHA-256 `d84a35e69695bc5b8bc531871d4c7d9a2082037eb2f89eaa32f8dd006ab56a44` (same caveat) |
| First-person prose | verified (`At ServiceNow CoreAI, we built AutoSynthData…`) |
| Standalone release | NONE found (no public model/dataset/pipeline code; HF API 401/empty; site searches negative) |
| Background dataset | `ServiceNow-AI/EnterpriseOps-Gym` (created 2026-02-28, Apache-2.0, arXiv:2603.13594) — SEPARATE |
| Reported results | Hybrid +7.2pp/35%, verifier 63.01%→68.55%, 59% gap closed; ITSM 18.77%→27.18% (1,994 samples/66h); publisher-measured, SFT-only, Gym-scoped |
| Access status | article + Gym dataset publicly readable 2026-10-10Z |
| Author/platform distinction | issuer = ServiceNow CoreAI (org path + badges + prose); platform = Hugging Face |
| Explicitly unresolved | code-level adapter detail; cross-env generalization; teacher registry proof; independent repro |
