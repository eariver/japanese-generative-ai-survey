#!/usr/bin/env python3
"""Generate a deterministic Grok Trend Sensor run instruction from a weekly plan.

The generator never calls Grok. It creates a reviewable Markdown instruction and
pre-execution collector-instruction metadata bound to a specific prompt hash.
Completed collector provenance is recorded separately with collector-run.schema.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_iso(value: str) -> datetime:
    normalized = value[:-1] + "+00:00" if value.endswith("Z") else value
    dt = datetime.fromisoformat(normalized)
    if dt.tzinfo is None:
        raise ValueError("timestamp must contain an explicit offset")
    return dt


def generate(plan: dict[str, Any], repo_root: Path) -> tuple[str, dict[str, Any]]:
    issue_id = plan["issue_id"]
    cutoff = plan["editorial_cutoff"]
    window_start = plan.get("collection_window_start")
    if not window_start:
        raise ValueError("collection_window_start is unset; bootstrap a prior collection anchor first")

    prompt_rel = Path("config/prompts/grok/x-trend-sensor-v0.4.md")
    prompt_path = repo_root / prompt_rel
    prompt_hash = sha256_file(prompt_path)

    generated_at = parse_iso(plan["generated_at"])
    jst_date = generated_at.astimezone(ZoneInfo("Asia/Tokyo")).date().isoformat()
    output_filename = f"x-trend-sensor-{jst_date}-v0.4.md"
    instruction_id = f"{issue_id}-grok-trend-v0.4-{jst_date}"

    metadata = {
        "schema_version": "1.0",
        "issue_id": issue_id,
        "instruction_id": instruction_id,
        "stage": "trend-discovery",
        "collector": {
            "id": "grok",
            "provider": "xAI",
            "model": None,
            "prompt_id": "x-trend-sensor",
            "prompt_version": "v0.4",
            "prompt_hash": f"sha256:{prompt_hash}",
        },
        "generated_at": plan["generated_at"],
        "time": {
            "collection_window_start": window_start,
            "editorial_cutoff": cutoff,
        },
        "expected_output": {
            "filename": output_filename,
            "repository_path": f"sources/{issue_id}/grok/raw/{output_filename}",
        },
        "execution": {
            "mode": "manual-or-agent-assisted",
            "repository_write_authority": "none",
        },
        "status": "ready",
        "notes": [
            "This is pre-execution instruction metadata, not completed collector-run provenance.",
            "observed_at and output hashes belong in a collector-run record after Grok actually completes the observation.",
        ],
    }

    md = f"""# {issue_id} X Trend Sensor Run Instruction — v0.4

このRunは `{issue_id}` のX Trend Discoveryを行うためのissue-specific instructionです。

Instruction ID:

`{instruction_id}`

## 1. 使用するPrompt

以下を読み、その指示に従ってください。

`{prompt_rel}`

Authority / Context:

- `docs/editorial-specification.md`
- `docs/editorial-style-guide.md`

Prompt SHA-256:

`sha256:{prompt_hash}`

## 2. Observation Window

今回のObservation Window Start:

`{window_start}`

Editorial Cutoff:

`{cutoff}`

重要:

- Release/Event dateとX momentum dateを分離してください。
- Cutoff後、実際の観測時刻までに急浮上した重要事項は `Late Breaking` として分離してください。
- Underlying EventがWindow以前でも、今回のWindow中にtechnical-community momentumが生じた場合は候補になり得ます。
- Window開始以前の既存Rawを、今回の検索結果の代用として再利用しないでください。

## 3. Coverage

`x-trend-sensor-v0.4.md` のCoverage Scan、Media Generation Second Pass、Candidate Pool、Global Ranking、Coverage Auditを省略せず実行してください。

Laneが弱い場合は `NONE_FOUND` / `UNCERTAIN` を使用し、枠を埋めるために弱い候補を昇格させないでください。

## 4. Evidence boundary

この出力はTrend Candidate / Raw Observationです。

- Technical Factの最終Evidenceではありません。
- release date、parameter count、license、benchmark score、hardware requirement等は後段でprimary-source verificationします。
- X Post内の主張を、そのまま技術的事実へ昇格させないでください。

## 5. Output

出力ファイル名:

`{output_filename}`

想定Repository path:

`sources/{issue_id}/grok/raw/{output_filename}`

同名ファイルが既に存在する場合は上書きせず、`-r2` 等のsuffixを追加してください。

Front Matterには少なくとも以下を含めてください。

```yaml
sensor: grok
prompt_version: x-trend-sensor-v0.4
issue_id: "{issue_id}"
observation_window_start: "{window_start}"
editorial_cutoff: "{cutoff}"
status: raw
```

`observed_at` は実際にGrokが観測を完了した時刻を記録してください。Run Instruction生成時刻を代入しないでください。

## 6. Completed run provenance

このinstruction JSONは実行前metadataです。Grok実行完了後は、`schemas/collector-run.schema.json` に従う別のrun provenance recordで、実際の `observed_at`、出力path、SHA-256、bytes、実行結果を記録してください。

## 7. Final artifact

最終成果物はチャット本文へ貼らず、実際のMarkdownファイルとして提示してください。

GitHubへのPushは試みないでください。Raw fileは後段でwrite-capable toolがRepositoryへ取り込み、SHA-256 provenance indexへ追加します。
"""
    return md, metadata


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--plan", required=True)
    parser.add_argument("--markdown-output", required=True)
    parser.add_argument("--metadata-output", required=True)
    args = parser.parse_args()

    root = Path(args.repo_root).resolve()
    plan_path = Path(args.plan)
    if not plan_path.is_absolute():
        plan_path = root / plan_path
    plan = load_json(plan_path)
    md, metadata = generate(plan, root)

    md_path = Path(args.markdown_output)
    meta_path = Path(args.metadata_output)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    meta_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(md, encoding="utf-8")
    meta_path.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(md_path)
    print(meta_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
