# W34 Luna event-level Discovery byte-integrity repair — 2026-09-04 r1

Status: **READY_FOR_SOL_SCREENING**

Issue / edition: `2026-W34`  
Branch: `weekly/2026-W34-v2-work`  
Exact Starting SHA: `10204e45c50c644b3f31b54b07b017da450a4ce0`

## Bounded purpose

Repair only the non-accepted event-level Screening input whose committed bytes were not valid UTF-8 JSONL. The accepted 40-record Discovery graph, Production State, Discovery checkpoint, crosswalk, existing Raw, and previous diagnostic records remain immutable.

## Starting corruption

- Path: `sources/2026-W34/screening/input/event-discovery-v2.jsonl`
- Git blob: `20b394ea7bb0ca4cb32a90f31678d1045678255b`
- Bytes: `210060`
- SHA-256: `a15ddbde1bc3b35ab158d68a50313294091aa33f2d942d2e24d3d578f5344321`
- Strict UTF-8/JSONL parse: `FAIL` (`'utf-8' codec can't decode byte 0xaa in position 1: invalid start byte`)

The corrupted file was not opened for salvage. A fresh candidate was generated from the valid crosswalk, Sol inventory, accepted parent graph, existing Raw bindings, and current Discovery contract.

## Pre-commit candidate

- Records / unique Discovery IDs: `105 / 105`
- Event accounting: `W34-C001`–`W34-C105`, `105/105`, missing `0`, duplicate `0`, silently dropped `0`
- Parent validation: `PASS` against accepted 40-record graph
- Raw path validation: `PASS`, 36 unique paths
- Strict UTF-8 JSONL parse: `PASS`
- Actual `survey_screening_v2.validate_discovery_set()`: `PASS`
- Pre-commit SHA-256: `b63d053f4ea83f3f8150aeb1e3bd196a5d55903d27176fe7a350cf16ebbd5c9e`
- Pre-commit byte count: `291114`

The canonical input replacement is permitted only after these checks. The next bounded action is a fast-forward repair commit followed by exact remote-byte readback and fresh-checkout validation.

## Repair commit and remote read-back

- Repair commit: `270b4da28d6d295ecbf5292abbbe837d52890e58`
- Remote branch HEAD: `270b4da28d6d295ecbf5292abbbe837d52890e58`
- GitHub file blob: `774f6165b76245df7526083461e99b23d4d5f4bc`
- Remote SHA-256 / bytes: `b63d053f4ea83f3f8150aeb1e3bd196a5d55903d27176fe7a350cf16ebbd5c9e` / `291114`
- Pre/post SHA-256 equality: `PASS`
- Pre/post byte-count equality: `PASS`
- Remote strict UTF-8/JSONL parse: `PASS`
- Fresh remote checkout actual `survey_screening_v2.validate_discovery_set()`: `PASS`

## Agent-first package preparation

On the fresh checkout at the repair commit, `survey_agent_control_v2.validate_agent_state()` passed for `DISCOVERY_COLLECTED / stage:screening`, with Discovery checkpoint `passed` and Screening checkpoint `pending`. The canonical `scripts/survey_agent_tool_v2.py` wrapper then ran `scripts/survey_screening_v2.py prepare` with implementation SHA `270b4da28d6d295ecbf5292abbbe837d52890e58`.

The prepared package is `sources/2026-W34/screening/v2/prepared/w34-event-screening-r1/package.json`: schema `2.0-rc1`, issue `2026-W34`, profile `WEEKLY`, 105 records, and three batches (43/44/18). Its discovery basis binds the repaired file at SHA-256 `b63d053f4ea83f3f8150aeb1e3bd196a5d55903d27176fe7a350cf16ebbd5c9e`; package schema, basis, batch hashes/ID union, prompt hash, and result-contract hash all pass.

No Screening decisions, result files, acceptance, lifecycle advance, Evidence, Materiality, Completeness, Selection, Architecture, or Human Gate action was performed. Production State, accepted Discovery, Discovery checkpoint, crosswalk, existing Raw, shared Core, and W33 remain unchanged.

## Scope guard

No Screening decision/result/acceptance, lifecycle advance, Evidence, Materiality, Completeness, Selection, Architecture, shared-Core modification, W33 modification, or accepted-artifact rewrite is performed.
