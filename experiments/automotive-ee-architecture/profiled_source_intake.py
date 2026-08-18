#!/usr/bin/env python3
"""Experimental domain-profile adapter for the existing Source Intake collectors.

This file intentionally lives outside scripts/ and does not modify the production AI
Source Intake implementation. It reuses scripts/source_intake.py as-is and injects
only experiment-scoped configuration/provenance and an optional verified-TLS
transport fallback. The experiment measures which context should eventually become a
shared domain-neutral collector API without changing production behavior first.
"""
from __future__ import annotations

import argparse
import json
import ssl
import subprocess
import sys
import tempfile
import urllib.error
from pathlib import Path
from typing import Any, Callable
from urllib.parse import urlparse

# Direct execution sets sys.path[0] to this experiment directory, not repository root.
# Add only the repository root so the production collector can be imported unchanged.
SCRIPT_PATH = Path(__file__).resolve()
REPOSITORY_ROOT = SCRIPT_PATH.parents[2]
if str(REPOSITORY_ROOT) not in sys.path:
    sys.path.insert(0, str(REPOSITORY_ROOT))

from scripts import source_intake as base


def repo_relative(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return path.as_posix()


def install_profiled_provenance(*, profile_path: Path, plan_path: Path, repo_root: Path) -> None:
    original: Callable[..., dict[str, Any]] = base.collector_run
    profile_ref = repo_relative(profile_path, repo_root)
    plan_ref = repo_relative(plan_path, repo_root)

    def profiled_collector_run(**kwargs: Any) -> dict[str, Any]:
        value = original(**kwargs)
        value["inputs"] = [profile_ref, plan_ref]
        value["notes"] = list(value.get("notes") or []) + [
            "EXPERIMENTAL_DOMAIN_PROFILE: production AI Source Intake code/config were not modified.",
            "Profile provenance replaces the production collector's historical weekly/config labels only; Raw acquisition behavior is unchanged unless the profile records an explicit verified-TLS transport fallback.",
        ]
        return value

    base.collector_run = profiled_collector_run


def tls_chain_failure(exc: Exception) -> bool:
    if not isinstance(exc, urllib.error.URLError):
        return False
    reason = getattr(exc, "reason", None)
    if isinstance(reason, ssl.SSLCertVerificationError):
        return True
    return "CERTIFICATE_VERIFY_FAILED" in str(exc)


def parse_last_header_block(raw: bytes) -> dict[str, str]:
    text = raw.decode("iso-8859-1", errors="replace")
    blocks = [block for block in text.replace("\r\n", "\n").split("\n\n") if block.strip().startswith("HTTP/")]
    if not blocks:
        return {}
    lines = blocks[-1].splitlines()[1:]
    result: dict[str, str] = {}
    for line in lines:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip().lower()] = value.strip()
    return result


def curl_verified_get(url: str, *, user_agent: str, timeout: int, headers: dict[str, str] | None = None) -> tuple[bytes, dict[str, Any]]:
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        body_path = root / "body.bin"
        header_path = root / "headers.txt"
        command = [
            "curl",
            "--location",
            "--silent",
            "--show-error",
            "--fail",
            "--proto",
            "=https",
            "--connect-timeout",
            str(min(timeout, 30)),
            "--max-time",
            str(timeout),
            "--user-agent",
            user_agent,
            "--dump-header",
            str(header_path),
            "--output",
            str(body_path),
            "--write-out",
            "%{url_effective}\n%{http_code}",
        ]
        for key, value in (headers or {}).items():
            command.extend(["--header", f"{key}: {value}"])
        command.append(url)
        completed = subprocess.run(command, check=False, capture_output=True, text=True)
        if completed.returncode != 0:
            raise RuntimeError(f"verified curl fallback failed rc={completed.returncode}: {completed.stderr.strip()}")
        lines = completed.stdout.splitlines()
        if len(lines) < 2:
            raise RuntimeError("verified curl fallback did not return URL/status metadata")
        final_url = lines[-2]
        try:
            status = int(lines[-1])
        except ValueError as exc:
            raise RuntimeError(f"invalid curl HTTP status: {lines[-1]!r}") from exc
        response_headers = parse_last_header_block(header_path.read_bytes()) if header_path.exists() else {}
        data = body_path.read_bytes()
        return data, {
            "requested_url": url,
            "final_url": final_url,
            "status": status,
            "content_type": response_headers.get("content-type"),
            "etag": response_headers.get("etag"),
            "last_modified": response_headers.get("last-modified"),
            "transport": "CURL_VERIFIED_TLS_FALLBACK",
        }


def install_profiled_transport(cfg: dict[str, Any]) -> None:
    policy = cfg.get("transport_policy") or {}
    fallback = policy.get("fallback") or {}
    if fallback.get("mode") != "CURL_VERIFIED_TLS":
        return
    if fallback.get("allow_insecure_tls") is not False:
        raise ValueError("experimental transport fallback requires allow_insecure_tls=false")
    allowed_hosts = {str(value).lower() for value in fallback.get("hosts", [])}
    original = base.http_get

    def profiled_http_get(url: str, *, user_agent: str, timeout: int, headers: dict[str, str] | None = None) -> tuple[bytes, dict[str, Any]]:
        try:
            return original(url, user_agent=user_agent, timeout=timeout, headers=headers)
        except Exception as exc:
            host = (urlparse(url).hostname or "").lower()
            if host not in allowed_hosts or not tls_chain_failure(exc):
                raise
            return curl_verified_get(url, user_agent=user_agent, timeout=timeout, headers=headers)

    base.http_get = profiled_http_get


def selected_collectors(value: str) -> list[str]:
    return ["arxiv", "github", "official"] if value == "all" else [value]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", default=".")
    parser.add_argument("--profile", required=True)
    parser.add_argument("--plan", required=True)
    parser.add_argument("--output-root", required=True)
    parser.add_argument("--collector", choices=["all", "arxiv", "github", "official"], default="all")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    profile_path = Path(args.profile)
    if not profile_path.is_absolute():
        profile_path = repo_root / profile_path
    plan_path = Path(args.plan)
    if not plan_path.is_absolute():
        plan_path = repo_root / plan_path
    output_root = Path(args.output_root)
    if not output_root.is_absolute():
        output_root = repo_root / output_root

    cfg = base.load_json(profile_path)
    plan = base.load_json(plan_path)
    if not plan.get("collection_window_start"):
        raise SystemExit("collection_window_start is unset; profiled Source Intake refuses to guess a window start")

    install_profiled_provenance(profile_path=profile_path, plan_path=plan_path, repo_root=repo_root)
    install_profiled_transport(cfg)

    runs: list[dict[str, Any]] = []
    for collector in selected_collectors(args.collector):
        if collector == "arxiv" and cfg["arxiv"].get("enabled", True):
            runs.append(base.run_arxiv(plan, cfg, output_root))
        elif collector == "github" and cfg["github_releases"].get("enabled", True):
            runs.append(base.run_github_releases(plan, cfg, output_root))
        elif collector == "official" and cfg["official_pages"].get("enabled", True):
            runs.append(base.run_official_pages(plan, cfg, output_root))

    failed = [run for run in runs if run["status"] == "failed"]
    partial = [run for run in runs if run["status"] == "partial"]
    report = {
        "schema_version": "1.0",
        "issue_id": plan["issue_id"],
        "experiment": "PROFILED_SOURCE_INTAKE",
        "profile": repo_relative(profile_path, repo_root),
        "plan": repo_relative(plan_path, repo_root),
        "collector_count": len(runs),
        "runs": [
            {
                "run_id": run["run_id"],
                "collector": run["collector"]["id"],
                "status": run["status"],
            }
            for run in runs
        ],
        "overall_status": "failed" if failed else ("partial" if partial else "success"),
        "production_files_modified": [],
    }
    base.write_json(output_root / "source-intake-report.json", report)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
