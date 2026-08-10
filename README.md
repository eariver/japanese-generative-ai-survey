# japanese-generative-ai-survey

Evidence-first Japanese weekly technical survey for generative AI, built with LLMs, LaTeX, and reproducible source tracking.

## Overview

This repository is the Source of Truth for a Japanese-language weekly technical survey / magazine covering current developments in:

- Large Language Models / Reasoning Models
- AI Agents / Coding Agents / Agent Harness
- Inference / Serving
- Multimodal / Image / Video / Audio Generation
- Open Weight Models / Local AI
- Long-term Memory / Multi-Agent Systems
- Evaluation / Benchmarks
- AI Safety / Agent Security

The project does **not** aim to have an LLM write an unchecked AI-news digest.

```text
Source Collection
    -> Screening
    -> Evidence
    -> Cross-source Synthesis
    -> Japanese Drafting
    -> Claim / Citation Validation
    -> LaTeX
    -> Reproducible PDF
    -> Explicit Freeze
    -> Optional GitHub Release
```

Core priority:

```text
Correctness > Traceability > Coverage > Speed
```

## Weekly cycle

Standard editorial cutoff:

```text
Friday 18:00 America/New_York
```

Compilation is normally performed in Japan on Saturday after that cutoff. The collection window is not forced to an exact 168 hours; operationally it covers:

```text
previous successful collection time
    -> current collection time
```

See:

- [Editorial Specification](docs/editorial-specification.md)
- [Editorial Style Guide](docs/editorial-style-guide.md)
- [Weekly Pipeline Automation Design](docs/weekly-pipeline-design-v0.1.md)
- [Weekly Pipeline Operations Guide](docs/weekly-pipeline-operations.md)
- [Weekly Pipeline Implementation Status](docs/weekly-pipeline-implementation-status.md)
- [Weekly GitHub Release Process](docs/weekly-release-process.md)

## Automation model

The first full issue, `2026-W32`, was completed end-to-end and frozen as the reference implementation.

The system intentionally separates:

- **Deterministic automation** — calendar/cutoff calculation, issue state, Raw integrity, structural validation, TeX/Biber build, log gates, PDF digest and build provenance;
- **LLM/tool-assisted work** — discovery, verification, paper review, candidate selection proposal, issue architecture, drafting and claim review;
- **Human/reviewer gates** — candidate selection approval, final PDF freeze, and GitHub Release publication.

Unattended public publication remains out of scope.

## Deterministic weekly spine

Implemented in:

```text
config/weekly-pipeline.json
schemas/weekly-pipeline-state.schema.json
scripts/weekly_pipeline.py
.github/workflows/weekly-pipeline.yml
```

Per-issue machine state:

```text
sources/<issue>/pipeline-state.json
```

Typical CLI:

```bash
python scripts/weekly_pipeline.py plan
python scripts/weekly_pipeline.py init
python scripts/weekly_pipeline.py init --issue-id 2026-W33   # assertion only when W33 is the current completed issue
python scripts/weekly_pipeline.py validate --issue-id 2026-W32 --target frozen
```

`init --issue-id` never relabels another week's calendar. A future or historical issue ID is rejected; initialization follows the issue derived from the latest completed editorial cutoff.

`Weekly pipeline spine` runs a **plan-only** scheduled job every Saturday at `00:30 UTC`, safely after Friday 18:00 New York in both EDT and EST. Scheduled execution does not call an LLM, modify the repository, merge a PR, or publish an issue.

## Source intake

The baseline deterministic source-intake layer supports:

- arXiv API category/date-window collection;
- a curated GitHub Releases watchlist;
- configured official news/blog index snapshots;
- issue-specific Grok Trend Sensor Run Instruction generation.

Manual Actions entry:

```text
Actions -> Weekly pipeline spine -> Run workflow
command: source-intake
collector: all | arxiv | github | official
```

Collector outputs are review artifacts, not verified Evidence Cards.

Accepted deterministic collector runs use append-only paths:

```text
sources/<issue>/collectors/<collector>/runs/<observed-at>/
├─ raw/
├─ summary.json
└─ collector-run.json
```

Exact HTTP response bytes are kept under `raw/`. Multiple runs in the same issue therefore coexist instead of overwriting one another.

Reviewed source-intake artifacts are accepted only through the canonical weekly work branch. Before import, the control workflow verifies the exact successful `weekly-pipeline.yml` `workflow_dispatch` run on `main`, repository identity, artifact identity, expiry state and SHA-256 digest. Acceptance is append-only and refreshes the weekly Draft PR after a successful work-branch commit.

## Raw provenance

Raw collector/Grok material is immutable after acceptance.

Per issue:

```text
sources/<issue>/raw-index.json
```

stores SHA-256 and byte size for every accepted file under a `raw/` path.

Commands:

```text
raw-index
raw-check
```

Normal push/PR CI also runs a `raw-integrity` job whenever Raw files or Raw indexes change.

The W32 Grok Raw baseline is already committed and protected by this mechanism.

## X / Grok sensing

Grok is used as an **X sensor**, not as factual evidence by itself.

Two passes remain distinct:

1. **Trend discovery** — what became technically important and when momentum arose;
2. **Community reaction evidence** — auditable X post URLs showing what technical users actually tested, reproduced, questioned or integrated.

Current trend prompt:

- [X Trend Sensor v0.4](config/prompts/grok/x-trend-sensor-v0.4.md)

Current reaction prompt:

- [X Community Reaction Evidence Collector v0.1](config/prompts/grok/x-community-reaction-evidence-v0.1.md)

A Trend Raw Observation is a candidate-discovery artifact. It is not sufficient by itself for release dates, parameter counts, licenses, benchmark numbers, hardware requirements or other technical facts.

## Reproducible PDF build

Current typesetting stack:

```text
LuaLaTeX + jlreq + LuaTeX-ja + HaranoAji
```

GitHub Actions builds the weekly PDF and fails on publication-blocking TeX warnings such as unresolved citations/references, Overfull/Underfull boxes and missing glyphs.

New builds also set:

```text
SOURCE_DATE_EPOCH=<source commit timestamp>
FORCE_SOURCE_DATE=1
```

and upload both `main.pdf` and `main.pdf.sha256`, providing a deterministic-byte baseline for future frozen revisions under the same source/toolchain.

## Frozen GitHub Releases

A frozen issue may be distributed through a GitHub Release without committing the PDF into the repository.

Canonical tag:

```text
weekly/<issue>/<revision>
```

Example:

```text
weekly/2026-W32/v0.2
```

Release workflow:

```text
Actions -> Release frozen weekly survey
```

Modes:

```text
validate -> draft -> human inspection -> publish
```

- `validate` performs no tag/Release write;
- `draft` creates/verifies the frozen source tag and attaches the digest-verified PDF + `SHA256SUMS.txt`;
- `publish` requires an existing Draft and re-verifies its PDF before publication.

W32 predates deterministic PDF timestamps, so its release manifest points to the exact already-validated frozen Actions artifact. Later issues can use reproducible rebuild mode.

See [Weekly GitHub Release Process](docs/weekly-release-process.md).

## Weekly magazine structure

Initial structure:

1. Cover
2. Contents / This Week in AI
3. Lead Stories
4. Model & Reasoning / Open Weight
5. Agent & Coding
6. Multimodal
7. Inference / Serving
8. Research Paper Watch
9. OSS & GitHub Watch
10. X Community Watch
11. Deep Dive
12. Watchlist / Chronology
13. References / Source Notes

The initial page budget is approximately 16 pages, with a provisional maximum of approximately 24. Weak weeks should not be padded merely to fill the target.

The frozen 2026-W32 v0.2 release candidate is 16 pages and is the first complete editorial/build reference.

## Chronology

The project maintains a conceptual distinction between:

- **Chronology:** objective artifact/event history;
- **Weekly survey:** what became technically important during a given observation period.

A model may be released on one date but become a weekly topic later because of weights, quantization, local deployment, serving support, independent evaluation or integrations.

## Current implementation direction

```text
Slice A  Deterministic spine                 implemented
Slice B  Source intake / Raw provenance      implemented; W32 replay validated, first live new issue pending
Slice C  Screening / Evidence runners        contracts implemented; production provider/live new issue pending
Slice D  Editorial / rendering runners       deterministic contracts through final source preflight implemented
Slice E  Weekly PR orchestration             in progress; work PR + reviewed intake import implemented
Slice F  Chronology + monthly/annual reuse   not started
```

The next operational milestone is the first live W33 collection after its Friday 18:00 New York cutoff, followed by reviewed import into `weekly/2026-W33-work`. In parallel, Slice E continues with auditable persistence of validated screening, Evidence and editorial stage results into the weekly Draft PR without weakening the Selection, Architecture, Visual Review or Freeze gates.

## Design principle

> AI に「文章を書かせる」システムではなく、AI に「根拠を追跡可能な Technical Survey を構築させる」システムにする。
