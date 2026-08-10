#!/usr/bin/env python3
"""Accept complete interactive Evidence Cards for a Special without paid provider API use."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import tempfile
from pathlib import Path
from typing import Any

from scripts import accept_evidence_results, prepare_evidence_run
from scripts.prepare_special_evidence_run import build_package

SPECIAL_RE = re.compile(r"^SP-[A-Za-z0-9][A-Za-z0-9._-]{2,63}$")
ANY_RE = re.compile(r"^(?:[0-9]{4}-W[0-9]{2}|SP-[A-Za-z0-9][A-Za-z0-9._-]{2,63})$")


def load_json(path: Path) -> dict[str, Any]:
    value=json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value,dict): raise ValueError(f"{path}: expected object")
    return value


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(*, repo_root: Path, issue_id: str, screening_run_sha: str, source_ref: str,
        source_commit: str, cards_path: Path, review_reference: str,
        audit_output: Path|None=None) -> dict[str, Any]:
    if not SPECIAL_RE.fullmatch(issue_id): raise ValueError("interactive Special Evidence requires SP-* issue_id")
    repo_root=repo_root.resolve(); cards_path=cards_path.resolve()
    doc=load_json(cards_path)
    if doc.get("schema_version")!="1.0" or doc.get("issue_id")!=issue_id:
        raise ValueError("interactive Evidence card file identity mismatch")
    if doc.get("screening_run_sha")!=screening_run_sha:
        raise ValueError("interactive Evidence screening_run_sha mismatch")
    runner=doc.get("runner")
    if not isinstance(runner,dict): raise ValueError("runner metadata required")
    for key in ("provider","model","invocation","generated_at"):
        if not isinstance(runner.get(key),str) or not runner[key].strip(): raise ValueError(f"runner.{key} required")
    cards=doc.get("cards")
    if not isinstance(cards,list): raise ValueError("cards must be an array")
    by_id: dict[str,dict[str,Any]]={}
    for entry in cards:
        if not isinstance(entry,dict): raise ValueError("card entries must be objects")
        task_id=entry.get("evidence_task_id"); card=entry.get("card")
        if not isinstance(task_id,str) or not task_id or task_id in by_id: raise ValueError(f"invalid/duplicate task id {task_id!r}")
        if not isinstance(card,dict): raise ValueError(f"card missing for {task_id}")
        by_id[task_id]=card

    prepare_evidence_run.ISSUE_RE=ANY_RE
    accept_evidence_results.ISSUE_RE=ANY_RE
    with tempfile.TemporaryDirectory() as tmp:
        root=Path(tmp); package_root=root/"package"
        package=build_package(repo_root=repo_root,output_root=package_root,issue_id=issue_id,
                              screening_run_sha=screening_run_sha,source_ref=source_ref,source_commit=source_commit)
        expected={t["evidence_task_id"]:t for t in package["evidence_tasks"]["tasks"]}
        missing=sorted(set(expected)-set(by_id)); extra=sorted(set(by_id)-set(expected))
        if missing or extra: raise ValueError(f"interactive Evidence set must be exact: missing={missing} extra={extra}")
        results=root/"results"; results.mkdir()
        for task_id,meta in expected.items():
            task_path=package_root/meta["path"]
            card=by_id[task_id]
            if card.get("issue_id")!=issue_id or card.get("evidence_task_id")!=task_id:
                raise ValueError(f"card identity mismatch: {task_id}")
            result={
                "schema_version":"1.0","issue_id":issue_id,"evidence_task_id":task_id,
                "evidence_task_sha256":sha(task_path),"prompt_id":package["prompt"]["prompt_id"],
                "prompt_sha256":package["prompt"]["sha256"],"runner":runner,"card":card,
            }
            (results/task_path.name).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        report,passed=accept_evidence_results.accept(package_root=package_root,results_dir=results,
                                                      repo_root=repo_root,issue_id=issue_id,
                                                      review_reference=review_reference)
        if not passed: raise ValueError(f"Evidence acceptance failed: {report}")
        report=dict(report); report["interactive_cards_path"]=cards_path.relative_to(repo_root).as_posix(); report["runner"]=runner
        if audit_output:
            audit_output.parent.mkdir(parents=True,exist_ok=True)
            audit_output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        return report


def main()->int:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo-root",default="."); p.add_argument("--issue-id",required=True)
    p.add_argument("--screening-run-sha",required=True); p.add_argument("--source-ref",required=True)
    p.add_argument("--source-commit",required=True); p.add_argument("--cards",required=True)
    p.add_argument("--review-reference",required=True); p.add_argument("--audit-output")
    a=p.parse_args()
    result=run(repo_root=Path(a.repo_root),issue_id=a.issue_id,screening_run_sha=a.screening_run_sha,
               source_ref=a.source_ref,source_commit=a.source_commit,cards_path=Path(a.cards),
               review_reference=a.review_reference,audit_output=Path(a.audit_output) if a.audit_output else None)
    print(json.dumps(result,ensure_ascii=False,indent=2)); return 0

if __name__=="__main__": raise SystemExit(main())
