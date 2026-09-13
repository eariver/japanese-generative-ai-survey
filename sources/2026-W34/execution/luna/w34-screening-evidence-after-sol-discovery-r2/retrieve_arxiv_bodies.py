#!/usr/bin/env python3
"""Bulk retrieve arXiv HTML bodies for 319 paper tasks + official new bodies.

Execution agent: Muse Spark 1.3 / EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION
Stores exact bytes under execution area for Supplement binding.
"""
from __future__ import annotations
import json, time, hashlib
from pathlib import Path
import urllib.request, urllib.error

REPO = Path(".").resolve()
EXEC_REL = "sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2"
DERIVED = REPO / EXEC_REL / "screening-basis/event-discovery-fresh-v1.jsonl"
ACC_PATH = REPO / "sources/2026-W34/screening/v2/accepted/41503363e1aef269ead56ac056b7f58e53eb1934d5de926f2cc49ee3bd84ccc3/screening-accepted.json"
OUT_DIR = REPO / EXEC_REL / "evidence-bodies"
PROV_PATH = REPO / EXEC_REL / "evidence-bodies/retrieval-provenance.jsonl"

def read_jsonl(p):
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]

def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (W34-Evidence Muse-Spark-1.3; contact: research)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.status, r.read(), r.headers.get_content_type()

def main(limit=None):
    derived = {r["discovery_id"]: r for r in read_jsonl(DERIVED)}
    acc = json.loads(ACC_PATH.read_text(encoding="utf-8"))
    non_drop = [d for d in acc["decisions"] if d["decision"] != "DROP"]
    # filter arxiv tasks: derived child IDs starting with w34-event-arxiv- or w34-event-refresh-arxiv-
    arxiv_tasks = [d for d in non_drop if d["discovery_id"].startswith("w34-event-arxiv-") or d["discovery_id"].startswith("w34-event-refresh-arxiv-")]
    print(f"arxiv tasks {len(arxiv_tasks)}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "arxiv").mkdir(exist_ok=True)
    # resume: skip if already fetched
    existing = set()
    if PROV_PATH.exists():
        for line in PROV_PATH.read_text(encoding="utf-8").splitlines():
            if line.strip():
                existing.add(json.loads(line)["discovery_id"])
    print(f"already fetched {len(existing)}")
    count = 0
    for d in sorted(arxiv_tasks, key=lambda x: x["discovery_id"]):
        did = d["discovery_id"]
        if did in existing:
            continue
        if limit and count >= limit:
            break
        rec = derived[did]
        locator = rec["source"]["locator"]  # https://arxiv.org/abs/2608.xxxxx
        arxiv_id = locator.rstrip("/").split("/abs/")[-1].split("v")[0]
        # try HTML versions: v1, then without version?
        html_urls = [f"https://arxiv.org/html/{arxiv_id}v1", f"https://arxiv.org/html/{arxiv_id}"]
        # also abs URL for fallback?
        body, used_url, status = None, None, None
        err = None
        for hu in html_urls:
            try:
                s, data, ctype = fetch(hu)
                if s == 200 and len(data) > 5000 and b"<html" in data[:5000].lower():
                    body, used_url, status = data, hu, s
                    break
                else:
                    err = f"{hu} status {s} len {len(data) if data else 0}"
            except Exception as e:
                err = f"{hu} {e}"
                time.sleep(1)
                continue
        prov = {
            "discovery_id": did,
            "arxiv_id": arxiv_id,
            "locator": locator,
            "attempted_html_urls": html_urls,
            "used_url": used_url,
            "http_status": status,
            "error": err if body is None else None,
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        }
        if body is not None:
            # store exact bytes
            fname = f"{arxiv_id.replace('.', '_')}.html"
            fpath = OUT_DIR / "arxiv" / fname
            fpath.write_bytes(body)
            prov["raw_path"] = str(fpath.relative_to(REPO))
            prov["byte_count"] = len(body)
            prov["sha256"] = hashlib.sha256(body).hexdigest()
            prov["outcome"] = "CAPTURED"
        else:
            prov["outcome"] = "RETRIEVAL_FAILED"
            # fallback: try abs page?
            try:
                s, data, ctype = fetch(locator)
                if s == 200 and len(data) > 5000:
                    fname = f"{arxiv_id.replace('.', '_')}-abs.html"
                    fpath = OUT_DIR / "arxiv" / fname
                    fpath.write_bytes(data)
                    prov["fallback_abs"] = {"url": locator, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(), "path": str(fpath.relative_to(REPO))}
            except Exception as e:
                prov["fallback_error"] = str(e)
        with PROV_PATH.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(prov, ensure_ascii=False, sort_keys=True) + "\n")
        count += 1
        print(f"{count} {did} {arxiv_id} {prov['outcome']} {prov.get('byte_count',0)}")
        time.sleep(1.2)  # rate limit
    print(f"done {count} new fetches")
    return 0

if __name__ == "__main__":
    import sys
    lim = int(sys.argv[1]) if len(sys.argv) > 1 else None
    raise SystemExit(main(lim))
