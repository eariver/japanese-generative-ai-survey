#!/usr/bin/env python3
"""Rebuild WEEKLY_MAGAZINE bibliography metadata from accepted Core v2 authority.

The semantic renderer establishes citation identity and Evidence binding. This
post-render repair preserves those exact cited Discovery IDs while replacing
placeholder bibliography authors with metadata that is actually supported by
accepted Evidence: source organization/owner when deterministically knowable,
published date when present, canonical title, and canonical URL. Unknown human
paper authors are omitted rather than invented.
"""
from __future__ import annotations

from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from scripts import survey_production_v2 as core


STATUS_CODES = {"VERIFIED": "V", "PARTIAL": "P"}
MATERIALITY_CODES = {"MATERIAL": "M", "CONTEXT": "C"}
EVIDENCE_TAG_LEGEND = "V=VERIFIED, P=PARTIAL; M=MATERIAL, C=CONTEXT"


def _rel(root: Path, path: Path) -> str:
    return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")


def _safe_bound_file(root: Path, ref: dict[str, Any], label: str) -> Path:
    if not isinstance(ref, dict) or set(ref) < {"path", "sha256"}:
        raise ValueError(f"{label} authority reference invalid")
    path = core.repo_local_path(root, ref["path"], label)
    if path.is_symlink() or not path.is_file():
        raise ValueError(f"{label} missing or unsafe: {ref.get('path')}")
    if core.sha256_file(path) != ref["sha256"]:
        raise ValueError(f"{label} SHA drift")
    return path


def _normalize_date(raw: Any) -> str | None:
    if not isinstance(raw, str) or not raw.strip():
        return None
    value = raw.strip()
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except ValueError:
        pass
    try:
        return parsedate_to_datetime(value).date().isoformat()
    except (TypeError, ValueError, OverflowError):
        return None


def _source_organization(locator: str) -> str | None:
    if locator.startswith("Grok_X_SourseIntake/"):
        return "Grok/X Source Intake"
    parsed = urlparse(locator)
    host = (parsed.hostname or "").lower()
    if not host:
        return None
    if host in {"arxiv.org", "www.arxiv.org"}:
        return "arXiv"
    if host in {"github.com", "www.github.com"}:
        parts = [part for part in parsed.path.split("/") if part]
        return parts[0] if parts else "GitHub"
    if host in {"openai.com", "www.openai.com"}:
        return "OpenAI"
    return host.removeprefix("www.")


def _escape_bib(value: str) -> str:
    return value.replace("{", "\\{").replace("}", "\\}")


def _bib_key(issue_id: str, discovery_id: str) -> str:
    return "w" + issue_id.lower().replace("-", "").replace(".", "") + discovery_id.lower().replace("-", "")


def _evidence_tag(status: str, materiality: str) -> str:
    try:
        return f"{STATUS_CODES[status]}/{MATERIALITY_CODES[materiality]}"
    except KeyError as exc:
        raise ValueError(f"unsupported Weekly bibliography evidence tag: {status}/{materiality}") from exc


def _bib_text(key: str, record: dict[str, Any], urldate: str) -> str:
    title = _escape_bib(record["title"])
    organization = record.get("organization")
    published_date = record.get("published_date")
    url = record["url"]
    evidence_tag = _evidence_tag(record["status"], record["materiality"])
    lines = [
        f"@online{{{key},",
        f"  title = {{{{{title}}}}},",
    ]
    if isinstance(organization, str) and organization.strip():
        lines.append(f"  organization = {{{{{_escape_bib(organization.strip())}}}}},")
    if isinstance(published_date, str) and published_date:
        lines.append(f"  date = {{{published_date}}},")
    lines.extend(
        [
            f"  url = {{{url}}},",
            f"  urldate = {{{urldate}}},",
            f"  note = {{[{evidence_tag}]}}",
            "}",
        ]
    )
    return "\n".join(lines)


def _index_unique(rows: list[dict[str, Any]], key_name: str, label: str) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for row in rows:
        key = row.get(key_name)
        if not isinstance(key, str) or not key:
            raise ValueError(f"{label} row lacks {key_name}")
        if key in out:
            raise ValueError(f"{label} duplicates {key_name}: {key}")
        out[key] = row
    return out


def rebuild_bibliography(root: Path, manifest_path: Path) -> dict[str, Any]:
    root = root.resolve()
    manifest_path = manifest_path.resolve()
    manifest_path.relative_to(root)
    if manifest_path.is_symlink() or not manifest_path.is_file():
        raise ValueError("validated source manifest missing or unsafe")
    manifest = core.load_json(manifest_path)
    issue_id = manifest.get("issue_id")
    if not isinstance(issue_id, str) or not issue_id:
        raise ValueError("validated source manifest issue_id invalid")

    bib_ref = manifest.get("bibliography")
    if not isinstance(bib_ref, dict) or set(bib_ref) != {"path", "sha256", "cited_discovery_ids"}:
        raise ValueError("validated source manifest bibliography fields invalid")
    bib_path = core.repo_local_path(root, bib_ref["path"], "bibliography")
    if bib_path.is_symlink() or not bib_path.is_file():
        raise ValueError("bibliography missing or unsafe")
    old_sha = core.sha256_file(bib_path)
    if old_sha != bib_ref["sha256"]:
        raise ValueError("validated source manifest bibliography SHA drift before metadata transform")
    cited = bib_ref["cited_discovery_ids"]
    if not isinstance(cited, list) or not cited or not all(isinstance(x, str) and x for x in cited):
        raise ValueError("validated source manifest cited_discovery_ids invalid")
    if len(cited) != len(set(cited)):
        raise ValueError("validated source manifest cited_discovery_ids must be unique")

    profile_path = _safe_bound_file(root, manifest["production_profile"], "Production Profile")
    profile = core.load_json(profile_path)
    temporal = profile.get("research_scope", {}).get("temporal_policy", {})
    window_end = temporal.get("window_end")
    if not isinstance(window_end, str) or len(window_end) < 10:
        raise ValueError("Weekly Production Profile lacks window_end for bibliography urldate")
    urldate = window_end[:10]

    bindings = manifest.get("evidence_binding")
    if not isinstance(bindings, dict):
        raise ValueError("validated source manifest evidence_binding invalid")
    acceptance_path = _safe_bound_file(root, bindings["evidence_acceptance"], "Evidence acceptance")
    matrix_path = _safe_bound_file(root, bindings["candidate_matrix"], "Candidate Matrix")
    discovery_path = _safe_bound_file(root, bindings["discovery_acceptance"], "Discovery acceptance")
    acceptance = core.load_json(acceptance_path)
    matrix = core.load_json(matrix_path)
    discovery = core.load_json(discovery_path)

    acceptance_by_did: dict[str, dict[str, Any]] = {}
    for row in acceptance.get("results", []):
        for did in row.get("discovery_ids", []):
            if did in acceptance_by_did:
                raise ValueError(f"Evidence acceptance duplicates Discovery ID: {did}")
            acceptance_by_did[did] = row

    matrix_by_did: dict[str, dict[str, Any]] = {}
    for row in matrix.get("rows", []):
        for did in row.get("discovery_ids", []):
            if did in matrix_by_did:
                raise ValueError(f"Candidate Matrix duplicates Discovery ID: {did}")
            matrix_by_did[did] = row

    discovery_by_did = _index_unique(discovery.get("records", []), "discovery_id", "Discovery acceptance")
    records: list[tuple[str, dict[str, Any]]] = []
    date_count = 0
    organization_count = 0
    for did in cited:
        accepted = acceptance_by_did.get(did)
        candidate = matrix_by_did.get(did)
        discovery_row = discovery_by_did.get(did)
        if accepted is None or candidate is None or discovery_row is None:
            raise ValueError(f"cited Discovery ID missing bibliography authority: {did}")
        evidence_sha = candidate.get("evidence_sha256")
        if evidence_sha != accepted.get("sha256"):
            raise ValueError(f"Candidate/Evidence SHA mismatch for {did}")
        filename = accepted.get("filename")
        if not isinstance(filename, str) or not filename:
            raise ValueError(f"Evidence acceptance lacks filename for {did}")
        result_path = acceptance_path.parent / "results" / filename
        if result_path.is_symlink() or not result_path.is_file():
            raise ValueError(f"accepted Evidence Card missing for {did}")
        if core.sha256_file(result_path) != evidence_sha:
            raise ValueError(f"accepted Evidence Card SHA drift for {did}")
        card = core.load_json(result_path)
        if card.get("evidence_task_id") != accepted.get("evidence_task_id") or card.get("status") != accepted.get("status"):
            raise ValueError(f"accepted Evidence Card identity/status mismatch for {did}")

        locator = discovery_row.get("source_locator")
        title = candidate.get("title")
        if not isinstance(locator, str) or not locator or not isinstance(title, str) or not title.strip():
            raise ValueError(f"cited bibliography identity incomplete for {did}")
        sources = [row for row in card.get("sources", []) if isinstance(row, dict) and row.get("url") == locator]
        if len(sources) != 1:
            raise ValueError(f"accepted Evidence Card must bind exactly one canonical source for {did}")
        source = sources[0]
        organizations = {
            row.get("organization").strip()
            for row in card.get("entities", [])
            if isinstance(row, dict)
            and row.get("canonical_url") == locator
            and isinstance(row.get("organization"), str)
            and row.get("organization").strip()
        }
        if len(organizations) > 1:
            raise ValueError(f"accepted Evidence Card has ambiguous organization for {did}")
        organization = next(iter(organizations), None) or _source_organization(locator)
        published_date = _normalize_date(source.get("published_at"))
        if published_date:
            date_count += 1
        if organization:
            organization_count += 1
        records.append(
            (
                did,
                {
                    "title": title.strip(),
                    "organization": organization,
                    "published_date": published_date,
                    "url": locator,
                    "status": accepted["status"],
                    "materiality": candidate["materiality"],
                },
            )
        )

    header = f"% Core v2 evidence tags: {EVIDENCE_TAG_LEGEND}.\n\n"
    rebuilt = header + "\n\n".join(
        _bib_text(_bib_key(issue_id, did), record, urldate) for did, record in records
    ) + "\n"
    if "Unknown" in rebuilt:
        raise ValueError("placeholder Unknown survived bibliography metadata transform")
    bib_path.write_text(rebuilt, encoding="utf-8")
    new_sha = core.sha256_file(bib_path)
    manifest["bibliography"]["sha256"] = new_sha
    core.write_json(manifest_path, manifest)

    quality_root = manifest_path.parent / "quality"
    quality_root.mkdir(parents=True, exist_ok=True)
    result_path = quality_root / "weekly-bibliography-metadata.json"
    if result_path.exists():
        raise ValueError(f"refusing existing Weekly bibliography metadata result: {result_path}")
    result = {
        "schema_version": "2.0-rc1",
        "check_id": "WEEKLY_BIBLIOGRAPHY_METADATA_TRANSFORM",
        "status": "PASS",
        "issue_id": issue_id,
        "bibliography_path": _rel(root, bib_path),
        "bibliography_sha256_before": old_sha,
        "bibliography_sha256_after": new_sha,
        "cited_entry_count": len(records),
        "published_date_count": date_count,
        "organization_count": organization_count,
        "placeholder_author_count": 0,
        "evidence_tag_legend": EVIDENCE_TAG_LEGEND,
        "manifest_path": _rel(root, manifest_path),
        "manifest_sha256_after": core.sha256_file(manifest_path),
        "finding": (
            "Cited Weekly references were rebuilt from exact accepted Evidence/source authority. "
            "Known publication dates and deterministic source owners are retained; unsupported human authors are omitted instead of rendered as Unknown. "
            "Evidence status/materiality are encoded with a fail-closed compact tag legend; access dates remain in bibliography metadata."
        ),
    }
    core.write_json(result_path, result)
    result["result_path"] = _rel(root, result_path)
    result["result_sha256"] = core.sha256_file(result_path)
    return result


def main() -> int:
    raise SystemExit("survey_weekly_bibliography_v2.py is a library; invoke survey_weekly_layout_v2.py")


if __name__ == "__main__":
    main()
