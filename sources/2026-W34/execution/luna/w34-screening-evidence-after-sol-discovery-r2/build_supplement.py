#!/usr/bin/env python3
"""Build Evidence Authority Supplement manifest binding captured bodies to fresh tasks.

Execution agent: Muse Spark 1.3 / EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION
"""
from __future__ import annotations
import json, hashlib
from pathlib import Path

REPO = Path(".").resolve()
EXEC = REPO / "sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2"
DISC_PATH = "sources/2026-W34/screening/input/event-discovery-v2.jsonl"
ACC_PATH = "sources/2026-W34/screening/v2/accepted/41503363e1aef269ead56ac056b7f58e53eb1934d5de926f2cc49ee3bd84ccc3/screening-accepted.json"
OUT = EXEC / "evidence-authority-supplement.json"

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()

def src_id(task_id: str, locator: str) -> str:
    return "supplement-src-" + hashlib.sha256(f"{task_id}|{locator}".encode()).hexdigest()[:16]

def task_id(did: str) -> str:
    return "evidence:2026-W34:" + hashlib.sha256(did.encode()).hexdigest()[:16]

def load_prov(p: Path):
    rows = []
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
    return rows

# source_type per locator host/kind
def classify(url: str, did: str) -> tuple[str, str]:
    u = url.lower()
    if "arxiv.org/html" in u or "arxiv.org/abs" in u or "arxiv.org/pdf" in u:
        return ("arxiv_primary", "PRIMARY_PAPER")
    if "msrc.microsoft.com" in u or "cisa.gov" in u:
        return ("vulnerability_authority_api" if "msrc" in u else "government_security_authority", "PRIMARY_OFFICIAL")
    if "varonis.com" in u:
        return ("SECONDARY", "SECONDARY")
    if "github.com" in u and ("releases" in u or "qwenlm/qwen3.8" in u or "openmoss" in u or "yaxin9luo" in u or "semianalysisai" in u or "ant-research" in u):
        return ("official_project_repo", "PRIMARY_REPOSITORY")
    if "api.github.com" in u:
        return ("github_release_api_response", "PRIMARY_REPOSITORY")
    if "huggingface.co" in u:
        return ("official_project_repo", "PRIMARY_REPOSITORY")
    if "techcrunch.com" in u:
        return ("SECONDARY", "SECONDARY")
    return ("official_publisher_page", "PRIMARY_OFFICIAL")

def main() -> int:
    disc = REPO / DISC_PATH
    acc = REPO / ACC_PATH
    disc_sha = sha256_file(disc)
    acc_sha = sha256_file(acc)
    entries = []
    seen: set[tuple[str, str]] = set()

    def add(did: str, locator: str, raw_rel: str, title: str, published_at, accessed_at: str, relation: str):
        rp = REPO / raw_rel
        assert rp.is_file(), raw_rel
        tid = task_id(did)
        key = (tid, locator)
        assert key not in seen, f"dup binding {key}"
        seen.add(key)
        st, sc = classify(locator, did)
        entries.append({
            "supplement_source_id": src_id(tid, locator),
            "discovery_id": did,
            "evidence_task_id": tid,
            "locator": locator,
            "source_type": st,
            "source_class": sc,
            "title": title,
            "published_at": published_at,
            "accessed_at": accessed_at,
            "raw_path": raw_rel,
            "raw_sha256": sha256_file(rp),
            "byte_count": rp.stat().st_size,
            "relation": relation,
        })

    # 1. arxiv HTML bodies (307) + abs-note: only HTML bound
    for prov in load_prov(EXEC / "evidence-bodies/retrieval-provenance.jsonl"):
        if prov.get("outcome") != "CAPTURED" or "raw_path" not in prov:
            continue
        did = prov["discovery_id"]
        add(did, prov["locator"], prov["raw_path"],
            f"arXiv full-text HTML body for {prov['arxiv_id']}", None, prov["timestamp"],
            "primary paper body inspected for method, evaluation, results, artifacts, and limitations; abstract alone not used for substantive claims")
    # 2. arxiv PDFs (12)
    for prov in load_prov(EXEC / "evidence-bodies/arxiv-pdf-provenance.jsonl"):
        if prov.get("outcome") != "CAPTURED":
            continue
        did = prov["discovery_id"]
        add(did, prov["url"], prov["raw_path"],
            f"arXiv PDF body for {prov['arxiv_id']} (HTML conversion unavailable; text extracted via pdftotext for inspection)",
            None, prov["timestamp"],
            "primary paper PDF body; HTML full-text conversion unavailable so PDF was retrieved and text-extracted for method/evaluation/results inspection")
    # 3. official bodies
    for prov in load_prov(EXEC / "evidence-bodies/official-provenance.jsonl"):
        if prov.get("outcome") != "CAPTURED":
            continue
        did = prov["discovery_id"]
        add(did, prov["url"], prov["raw_path"],
            f"First-party/official body: {prov['url']}", None, prov["timestamp"],
            "first-party announcement/docs/changelog body inspected for capability, availability, chronology, and API/functional facts; marketing framing separated")
    # 3b. c040 shares the DeepSeek updates page raw with c022 (same bytes, fresh task binding)
    c022_updates_raw = "sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2/evidence-bodies/official/w34-event-c022__api-docs-deepseek-com-updates.html"
    add("w34-event-c040", "https://api-docs.deepseek.com/updates/",
        c022_updates_raw, "DeepSeek API updates page (shared body: Aug 13 GA + Aug 16 peak/off-peak entries)",
        None, "2026-09-08T23:00:00Z",
        "shared updates-page body documenting GA timing and pricing-switch mechanics; same bytes as c022 capture")
    # 4. shared-raw bindings: c095/c096 -> c052 release notes file
    c052_raw = "sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2/evidence-bodies/official/w34-event-c052__help-openai-com-en-articles-6825453-chatgpt-release-notes.html"
    for did, loc, rel in [
        ("w34-event-c095", "https://help.openai.com/en/articles/6825453-chatgpt-release-notes",
         "shared ChatGPT release-notes body (Aug 20 entry) covering Aug 21 product-experience updates; same bytes as c052 capture"),
        ("w34-event-c096", "https://help.openai.com/en/articles/6825453-chatgpt-release-notes",
         "shared ChatGPT release-notes body (Aug 20 Apple Messages plugin entry); same bytes as c052 capture"),
    ]:
        add(did, loc, c052_raw, "OpenAI ChatGPT release notes (shared body)", "2026-08-20T00:00:00Z",
            "2026-09-08T23:00:00Z", rel)
    # 5. Sep-8 official-fallback snapshots for Copilot tasks
    fb = "sources/2026-W34/execution/luna/w34-discovery-gapfill-after-sol-review-r1/source-intake/official-fallback/sources/2026-W34/collectors/official-pages/runs/20260908T005152Z/raw"
    for did, fn, loc in [
        ("w34-event-c099", "github-copilot-jetbrains-fallback.html", "https://docs.github.com/copilot/jetbrains"),
        ("w34-event-c100", "github-copilot-slack-fallback.html", "https://docs.github.com/copilot/slack"),
        ("w34-event-c101", "github-copilot-teams-fallback.html", "https://docs.github.com/copilot/teams"),
    ]:
        add(did, loc, f"{fb}/{fn}", f"GitHub first-party changelog snapshot for {did}",
            None, "2026-09-08T00:51:52Z",
            "pre-screening repository-owned first-party snapshot rebound to fresh task; exact bytes preserved with original run provenance")
    manifest = {
        "schema_version": "2.0-rc1",
        "supplement_id": "w34-supplement-screening-evidence-r2-muse-spark",
        "issue_id": "2026-W34",
        "basis": {
            "source_root": "sources/2026-W34",
            "discovery_path": DISC_PATH,
            "discovery_sha256": disc_sha,
            "screening_acceptance_path": ACC_PATH,
            "screening_acceptance_sha256": acc_sha,
        },
        "sources": sorted(entries, key=lambda e: (e["discovery_id"], e["locator"])),
    }
    OUT.write_text(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    from collections import Counter
    print("sources:", len(entries), Counter(e["source_class"] for e in entries))
    print("tasks bound:", len({e["discovery_id"] for e in entries}))
    print("wrote", OUT)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
