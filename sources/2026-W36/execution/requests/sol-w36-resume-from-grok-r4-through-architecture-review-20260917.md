# W36 execution instruction — accepted Grok r4 through fresh Human Architecture Review

Status: `EXECUTION_AUTHORITY / W36_RESUME_FROM_ACCEPTED_GROK_R4 / GITHUB_ONLY_PAYLOAD / BOUNDED_AT_FRESH_HUMAN_ARCHITECTURE_REVIEW`

Date: `2026-09-17 JST`

Repository: `eariver/japanese-generative-ai-survey`

Branch: `weekly/2026-W36-v2-work`

## 1. Mission

Resume 2026-W36 Weekly production from the current `ISSUE_INITIALIZED / AWAITING_GROK` state, materialize the Human/Sol-reviewed Grok r4 exact bytes from the repository-local staging payload, record the X Source Intake canonically, then execute the current Core v2 Weekly pipeline through:

`DISCOVERY_COLLECTED -> CANDIDATES_NORMALIZED -> EVIDENCE_REVIEWED -> materiality/completeness -> SELECTION_COMPLETE -> ARCHITECTURE_ESTABLISHED -> fresh Human Architecture Review pending -> STOP`

Do not invent any Human decision.

This request is repository-local authority. Muse/OpenCode must not use, request, search for, authenticate to, or install Google Drive access.

## 2. Invocation starting guard

The Muse invocation MUST provide the exact current remote HEAD and tree after this request commit is pushed.

Before any repository write, read-only verify:

- remote `weekly/2026-W36-v2-work` HEAD == Exact Starting SHA supplied in the invocation;
- remote W36 tree == Exact Starting Tree supplied in the invocation;
- Exact Starting SHA parent == `8696f61697233a3021652b8128b0a673c31deb24`;
- remote `main` HEAD == `5acbff8528890ed9fc324c0227e6c4e43067c438`;
- remote `main` tree == `451fd7c6c6a9fcda59daa81fe484c62291e7d018`;
- remote `production/survey-core-v2` HEAD == `774dd39a951c9ac3818e83dfffd4c7666efb0a20`;
- remote Production Line tree == `cd46a6f7a6dcc4031e76220cea4c52c7dd1fc481`.

Also verify the repository-local staging payload exists:

`sources/2026-W36/external/x/weekly-x-2026-W36/staging/grok-x-result-r4.md.gz.b64`

Expected staging Git blob SHA:

`79a76ce8aec8090f50b6a93a4839fcb6ea3f3a7a`

Expected staging file identity including trailing LF:

- bytes: `9957`
- SHA-256: `362db8829bdbf92293a3a79284e3c6c6f35e1b13c5002b2a41cbc7309180ccbe`

If any guard differs, perform no repository/GitHub write. Report expected versus actual and STOP.

## 3. Materialize accepted Grok r4 Raw authority

The accepted Human/Sol-reviewed Grok r4 exact raw identity is:

- filename: `grok-x-result-r4.md`
- bytes: `24219`
- SHA-256: `a94f543d6714da0415b384af65b32c6e5fd792cc00f2959ca9640b5fa8bfabd2`
- observed_at: `2026-09-16T14:51:00+00:00`
- revision: `r4`
- augmentation scope: `ordinary-independent-signal`

Target repository Raw path:

`sources/2026-W36/external/x/weekly-x-2026-W36/raw/grok-x-result-r4.md`

Materialize it deterministically from the repository-local staging payload. One acceptable implementation is:

```bash
python - <<'PY'
from pathlib import Path
import base64, gzip, hashlib

src = Path('sources/2026-W36/external/x/weekly-x-2026-W36/staging/grok-x-result-r4.md.gz.b64')
dst = Path('sources/2026-W36/external/x/weekly-x-2026-W36/raw/grok-x-result-r4.md')

payload = src.read_bytes()
assert len(payload) == 9957
assert hashlib.sha256(payload).hexdigest() == '362db8829bdbf92293a3a79284e3c6c6f35e1b13c5002b2a41cbc7309180ccbe'

gz = base64.b64decode(payload.strip(), validate=True)
assert len(gz) == 7467
assert hashlib.sha256(gz).hexdigest() == 'a30fc2a082babca522a6cd19d2cdb8f101fdf8a7b427ce885760cd1eeba1d408'

raw = gzip.decompress(gz)
assert len(raw) == 24219
assert hashlib.sha256(raw).hexdigest() == 'a94f543d6714da0415b384af65b32c6e5fd792cc00f2959ca9640b5fa8bfabd2'

dst.parent.mkdir(parents=True, exist_ok=True)
if dst.exists():
    existing = dst.read_bytes()
    if existing != raw:
        raise SystemExit('Raw target already exists with non-identical bytes')
else:
    dst.write_bytes(raw)
PY
```

Do not normalize whitespace, line endings, punctuation, Unicode, Markdown formatting, or URLs.

After materialization, verify again with `sha256sum` and `wc -c`.

Commit only the newly materialized Raw file as the first production write in this continuation, using a normal commit such as:

`W36: materialize accepted Grok r4 raw authority`

Then non-force push and remote read-back. If remote HEAD changed unexpectedly before this write, STOP instead.

The staging payload may remain as immutable transport provenance. Do not delete or rewrite it during this execution.

## 4. Accepted Grok r4 accounting

Recompute from the materialized Raw ledger; do not blindly copy this summary.

Expected canonical accounting:

- unique X URLs: `15`
- `ORDINARY_WINDOW`: `12`
- `BACKGROUND_ONLY`: `0`
- `LATE_BREAKING`: `3`
- ordinary official-account posts: `3`
- ordinary independent/non-official posts: `9`
- distinct ordinary independent accounts: `8`
- new ordinary independent URLs added in r4: `7`

If the Raw ledger does not reproduce these values, do not record the X intake. STOP and report the discrepancy.

The three Late Breaking URLs are:

- `https://x.com/DavidOndrej1/status/2096025503329091995`
- `https://x.com/dui_toledo/status/2096025501886214553`
- `https://x.com/neondatabase/status/2096024903027974535`

They are post-cutoff and must not contribute to ordinary-window counts.

## 5. Canonical window

W36 ordinary observation window is end-exclusive:

- America/New_York: `[2026-08-28T18:00:00-04:00, 2026-09-04T18:00:00-04:00)`
- UTC: `[2026-08-28T22:00:00Z, 2026-09-04T22:00:00Z)`
- JST: `[2026-08-29T07:00:00+09:00, 2026-09-05T07:00:00+09:00)`

Do not invent another boundary rule.

## 6. Current lifecycle authority

Before Grok materialization, W36 canonical production state is expected to remain:

- issue: `2026-W36`
- research profile: `WEEKLY`
- publication profile: `WEEKLY_MAGAZINE`
- lifecycle: `ISSUE_INITIALIZED`
- target gate: `ARCHITECTURE_REVIEW`
- next action: `stage:discovery`
- Human Architecture Review: `pending`
- Human Publication Preview: `pending`

Read the actual state. Do not hand-edit state JSON.

## 7. Record canonical X result

Inspect the current canonical `survey_x_intake_v2.py` CLI/help before invoking it.

Use current canonical tooling to record:

- run_id: `weekly-x-2026-W36`
- Raw path: `sources/2026-W36/external/x/weekly-x-2026-W36/raw/grok-x-result-r4.md`
- Raw SHA-256: `a94f543d6714da0415b384af65b32c6e5fd792cc00f2959ca9640b5fa8bfabd2`
- Raw bytes: `24219`
- source filename: `grok-x-result-r4.md`
- observed_at: `2026-09-16T14:51:00+00:00`
- result status: `SUCCESS`

Use the materialization commit time for imported-at provenance if the canonical tool derives/imports that value.

Do not contact Google Drive for reconciliation.

## 8. X is Raw Observation, not technical Evidence

Never promote an X-only statement directly to a verified technical fact.

Primary verification is still required for model capability, benchmark scores, parameter counts, deal valuation/terms, exploit success rates, access tiers, architecture, pricing, license terms, hardware requirements, autonomy degree, throughput/TPS, or efficiency deltas.

Retrieval success is not semantic consumption.

## 9. Formal Discovery

After X intake is canonically recorded, perform fresh W36 formal Discovery.

The existing pre-Discovery preparation may be used as a lead source, but it is not canonical Discovery by itself.

Inspect all required Weekly lanes:

A. Foundation Models / Reasoning
B. Agents / Coding / Harness / Computer Use
C. Multimodal Foundation Models
D. Image Generation / Editing
E. Video Generation / Editing
F. Speech / Audio / Music Generation
G. Open Weight / Local AI / Quantization
H. Inference / Serving / Systems
I. Memory / Multi-Agent / Retrieval
J. Evaluation / Benchmarks
K. Safety / Security
L. Other Emerging Generative AI Technology

Do not restrict Discovery to Grok candidates. Search primary/authoritative surfaces such as official announcements, release notes, system/model cards, repositories, papers, documentation and first-party engineering posts.

Quiet lanes may legitimately remain quiet. Do not fabricate candidates to satisfy a count quota.

On successful acceptance, advance canonically to `DISCOVERY_COLLECTED`.

## 10. W35 carry-over

Read the released W35 authority fresh and derive carry-over canonically.

W35 item != automatic W36 candidate != automatic W36 Evidence != automatic W36 Selection.

Never inherit W35 Human decisions. Revalidate any prior HOLD/unresolved limitation against W36 facts. If there is no carry-over obligation, record that explicitly.

## 11. Screening and normalization

Screen fresh W36 Discovery records. For each candidate preserve window relevance, underlying event date, source quality, duplicate/cluster identity, lane, primary-source availability, materiality potential and X-only versus primary-backed status.

Advance canonically through `CANDIDATES_NORMALIZED`.

Do not copy prior-week classification blindly.

## 12. Retrieval and semantic consumption

For non-DROP candidates retrieve the necessary primary/authoritative sources and actually read the claim-relevant content.

Keep a distinction equivalent to:

- `RETRIEVED_AND_CONSUMED`
- `RETRIEVED_NOT_CONSUMED`
- `SOURCE_UNAVAILABLE`
- `SECONDARY_ONLY`
- `X_ONLY`

mapped to the current canonical schema/vocabulary.

A search snippet is not a substitute for the source body.

## 13. Evidence priorities

Freshly verify, as applicable:

### OpenAI GPT-6 Astra
- official release
- system/model card
- rollout/access
- computer-use behavior
- preparedness/security claims
- benchmark definitions

### Anthropic Fermat / Lean formalization
- Anthropic Science/official article
- public Lean repository
- process/autonomy description
- line/theorem counts
- multi-agent methodology
- verification boundary

### NVIDIA / Hugging Face
- official HF statement
- NVIDIA statement
- deal/transaction state and terms if public
- openness/independence/compute-agnostic claims

### Claude Fable / Mythos 5.1
- Anthropic official release/model docs
- exact identity and availability
- coding/agent claims

### Gemini variants
- Google/DeepMind primary authority
- exact variant naming
- release/availability/capabilities

### GLM-5.3
- Z.ai/Zhipu authority
- weights/model card
- license
- serving/local-inference facts

### Muse Spark 1.3
- Meta/first-party authority
- exact version identity
- coding/agent claims
- claimed tool-call/token efficiency deltas

X anecdotes may influence materiality, but do not independently verify these claims.

## 14. Evidence, materiality and completeness

Generate fresh W36 Evidence cards from consumed authority.

Only use `VERIFIED` where source identity, provenance, claim boundary and semantic consumption justify it. Leave primary-source gaps as `PARTIAL` or the current equivalent.

Then execute canonical Materiality and Completeness evaluation. Quiet lanes are not automatically a failure. Required coverage must actually have been examined, material gaps must be explicit, source-access gaps must remain visible, and X-only claims must not be promoted.

If a genuine Exception Gate is required, follow the canonical stop contract rather than forcing progression.

## 15. Selection

Perform fresh Survey Selection from W36 Evidence/Materiality/Completeness.

Important: Grok r4 `SELECTED` is an X-intake signal disposition, not the Survey Selection decision. Do not copy it mechanically.

Use current canonical `SELECTED` / `HOLD` / `DROP` semantics as appropriate.

## 16. Architecture

Build fresh W36 Architecture only after Selection is complete.

Architecture must be supported by selected Evidence and retain explicit verification boundaries and residual limitations.

Do not generalize a model-specific number, license, benchmark, cost, safety classification, openness claim or autonomy claim to an entire cluster unless the Evidence supports the cluster-wide statement.

In particular, do not repeat the W35 r1 failure mode where a property supported for only part of a cluster was written as a cluster-wide thesis.

Validate Architecture with current canonical validators.

## 17. Fresh Human Architecture Review and STOP

After Architecture generation and validation, generate the fresh Human Architecture Review surface and STOP.

Normal endpoint:

`ARCHITECTURE_ESTABLISHED / fresh Human Architecture Review pending`

Do not invent `APPROVED` or `REQUEST_CHANGES`.

Do not begin Draft, Publication Preview, Freeze or Release.

## 18. Shared-Core freeze

Do not modify:

- `.github/**`
- `config/**`
- `schemas/**`
- `scripts/**`
- `templates/**`
- `tests/**`
- `production/survey-core-v2`

Known Issue #497 and the W35 release-workflow nonexistent `survey_agent_control_v2.py validate-state` CLI defect are out of scope. Do not repair them now.

If a new shared-Core contradiction blocks Discovery through Architecture, do not invent an edition-local workaround. Preserve a safe checkpoint if possible, record the exact failing command/expected/actual/minimal reproduction, and STOP.

## 19. Commit discipline

Stay on the existing branch `weekly/2026-W36-v2-work` only.

No new fallback/repair/review branch.

At meaningful stages use normal commits, non-force push and remote read-back. Before each write, ensure the remote branch is still at the expected prior SHA.

Forbidden: force push, reset, rebase, squash, history rewrite.

## 20. Execution record

Maintain edition-local execution provenance covering at least:

- invocation Starting SHA/tree
- staging payload identity
- materialized Raw SHA/bytes
- canonical X accounting
- X intake completion
- Discovery counts
- Screening counts
- W35 carry-over result
- retrieval/semantic-consumption counts
- Evidence counts by status
- Materiality result
- Completeness result
- Selection counts
- Architecture identity/hash
- validation results
- ending HEAD/tree
- Human Architecture Review pending
- shared-Core changed paths = 0
- main unchanged
- Production Line unchanged

## 21. Final validation and report

Before normal stop, read back:

- remote W36 HEAD/tree
- production state and target gate
- machine checkpoint states
- X intake provenance
- Discovery/Screening/Evidence/Selection counts
- Architecture path/hash
- Human Architecture Review path/hash
- changed paths
- `main` still `5acbff8528890ed9fc324c0227e6c4e43067c438`
- `production/survey-core-v2` still `774dd39a951c9ac3818e83dfffd4c7666efb0a20`
- shared-Core changed paths = 0

Final report must include Starting SHA/tree, accepted r4 SHA/bytes, canonical X accounting, X intake status, Discovery total, Screening distribution, carry-over result, retrieval and semantic-consumption status, Evidence status counts, Materiality, Completeness, Selection distribution, Architecture summary/validation, Human Architecture Review path, Ending SHA/tree, main/Production Line unchanged confirmation, Core changes = 0 and exact stop reason.

Human decision must not be included or inferred.
