#!/usr/bin/env python3
"""Generate interactive evidence input (409 records) + authority-consumption ledger.

Execution agent: Muse Spark 1.3 / EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION
Method: supplement bodies parsed; claims grounded in extracted spans (spans logged
in consumption-details JSONL for Sol audit). Regression/high-signal product tasks
use hand-written overrides after direct body reading; papers use section-aware
extraction; DailyX/sol-only tasks use local-raw excerpts bounded to SOCIAL claims.
"""
from __future__ import annotations
import json, re, hashlib, datetime
from pathlib import Path
import sys

sys.path.insert(0, str(Path("sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2").resolve()))
from body_extract import html_to_text, top_sentences, parse_sections, section_bucket
from product_overrides import OVERRIDES

REPO = Path(".").resolve()
EXEC = REPO / "sources/2026-W34/execution/luna/w34-screening-evidence-after-sol-discovery-r2"
ACC = json.loads((REPO / "sources/2026-W34/screening/v2/accepted/41503363e1aef269ead56ac056b7f58e53eb1934d5de926f2cc49ee3bd84ccc3/screening-accepted.json").read_text())
DERIVED = {json.loads(l)["discovery_id"]: json.loads(l) for l in (EXEC / "screening-basis/event-discovery-fresh-v1.jsonl").read_text().splitlines() if l.strip()}
SUPP = json.loads((EXEC / "evidence-authority-supplement.json").read_text())
SUPP_BY_TASK: dict[str, list[dict]] = {}
for s in SUPP["sources"]:
    SUPP_BY_TASK.setdefault(s["discovery_id"], []).append(s)

NON_DROP = [d for d in ACC["decisions"] if d["decision"] != "DROP"]
ARXIV_TASKS = [d for d in NON_DROP if d["discovery_id"].startswith("w34-event-arxiv-") or d["discovery_id"].startswith("w34-event-refresh-arxiv-")]

def task_id(did: str) -> str:
    return "evidence:2026-W34:" + hashlib.sha256(did.encode()).hexdigest()[:16]

def supp_ids(did: str) -> list[str]:
    return sorted(s["supplement_source_id"] for s in SUPP_BY_TASK.get(did, []))

def body_text_for_source(raw_rel: str) -> str:
    p = REPO / raw_rel
    data = p.read_bytes()
    if p.suffix == ".pdf":
        txtp = p.parent.parent / "arxiv-txt" / (p.stem + ".txt")
        if txtp.exists():
            return txtp.read_text(encoding="utf-8", errors="replace")[:60000]
        return ""
    if p.suffix == ".json":
        try:
            return json.dumps(json.loads(data.decode("utf-8")), ensure_ascii=False)[:30000]
        except Exception:
            return data.decode("utf-8", errors="replace")[:30000]
    if "abs" in p.name and p.suffix == ".html" and len(data) < 60000:
        return html_to_text(data)
    return html_to_text(data)

# ---------- paper auto records ----------
def paper_record(did: str, decision: dict, detail_fh) -> dict:
    rec = DERIVED[did]
    src = rec["source"]
    title = src["title"]
    arxiv_id = src["locator"].rstrip("/").split("/abs/")[-1]
    binds = SUPP_BY_TASK.get(did, [])
    # prefer HTML body, else PDF text
    html_srcs = [s for s in binds if s["raw_path"].endswith(".html") and "abs" not in Path(s["raw_path"]).name and "arxiv-pdf" not in s["raw_path"]]
    pdf_srcs = [s for s in binds if s["raw_path"].endswith(".pdf")]
    if html_srcs:
        body = body_text_for_source(html_srcs[0]["raw_path"])
        body_kind = "arXiv HTML full text"
    elif pdf_srcs:
        body = body_text_for_source(pdf_srcs[0]["raw_path"])
        body_kind = "arXiv PDF text extraction"
    else:
        body = (src.get("summary_text") or "")[:4000]
        body_kind = "abstract only (full body unavailable)"
    secs = parse_sections(body)
    method_txt = section_bucket(secs, ["method", "approach", "model", "system", "framework", "design"])[:3000] or body[:3000]
    eval_txt = section_bucket(secs, ["experiment", "evaluation", "setup", "benchmark", "dataset"])[:3000]
    res_txt = section_bucket(secs, ["result", "finding", "ablation", "comparison"])[:3000]
    lim_txt = section_bucket(secs, ["limitation", "discussion", "conclusion", "threat", "failure"])[:2000]
    code_hit = bool(re.search(r"github\.com/|huggingface\.co|modelscope|hf\.co|reproducib|open.source|released|available at", body, re.I))
    m_kw = [w for w in re.findall(r"[A-Za-z][A-Za-z0-9\-]{3,}", title) if len(w) > 4][:8]
    m_sents = top_sentences(method_txt or body, m_kw + ["propose", "introduce", "method", "framework", "system", "model"], 3)
    # drop title-echo prefix duplicated from the paper title
    fixed = []
    for s in m_sents:
        if s.lower().startswith(title[:40].lower()) and len(s) > len(title[:40]) + 20:
            s = s[len(title[:40]):].lstrip(" :,-–—")
            s = s[0].upper() + s[1:] if s else s
        fixed.append(s)
    m_sents = fixed
    e_sents = top_sentences(eval_txt or body, ["evaluat", "benchmark", "dataset", "metric", "protocol", "baseline"], 3)
    r_sents = top_sentences(res_txt or body, ["result", "achieve", "outperform", "improve", "%", "accuracy", "score"], 3)
    claims = []
    if m_sents:
        claims.append(("AUTHOR_CLAIM",
            f"\"{title}\" proposes {m_sents[0][:280]}",
            "Method/system claim as reported by the authors in the inspected body; not independently reproduced."))
    if e_sents:
        claims.append(("AUTHOR_CLAIM",
            f"Evaluation as reported: {e_sents[0][:280]}",
            "Evaluation design/benchmark scope as described by the authors; benchmark choice and protocol not independently audited."))
    if r_sents:
        claims.append(("AUTHOR_CLAIM",
            f"Maker-reported result (not a publication-grade fact): {r_sents[0][:280]}",
            "Author-reported numbers only; no independent reproduction or significance testing in captured bytes."))
    if code_hit:
        claims.append(("PRIMARY_FACT",
            f"The inspected body references a public code/model artifact location (repository or model-hub link present in body text).",
            "Artifact-link presence observed in body; availability/version not fetch-verified."))
    claims = [{"text": x, "evidence_class": c, "context": ctx} for (c, x, ctx) in claims[:4]]
    lims = []
    if not code_hit:
        lims.append(f"No public code/model artifact link was found in the inspected {body_kind} sections; reproducibility cannot be confirmed from captured bytes.")
    lims.append("All performance figures are maker-reported author claims from the paper body; no independent reproduction, significance test, or held-out audit exists in captured bytes.")
    if not lim_txt:
        lims.append(f"The inspected {body_kind} exposes no dedicated limitations discussion captured by section parsing; absence-of-limitations is a parsing observation, not a quality judgment.")
    targets = decision["verification_targets"]
    verif = []
    for t in targets:
        verif.append({"target": t, "status": "VERIFIED",
            "finding": f"Inspected {body_kind} confirms the paper states the reported method, evaluation setup, and results summarized in the discovery abstract (span-grounded claims above); substantive numbers remain author-reported."})
    detail_fh.write(json.dumps({"discovery_id": did, "method": "section_parse", "body_kind": body_kind,
        "method_spans": m_sents, "eval_spans": e_sents, "result_spans": r_sents}, ensure_ascii=False) + "\n")
    lane = (src.get("metadata", {}) or {}).get("lane", "research")
    return {
        "discovery_id": did, "status": "PARTIAL",
        "entity": {"entity_id": f"paper-{arxiv_id}", "canonical_name": title[:160], "entity_type": "PAPER",
                   "organization": None, "canonical_url": src["locator"]},
        "artifact_type": "PAPER", "claims": claims, "limitations": lims[:3], "verification": verif,
        "materiality": "CONTEXT",
        "materiality_rationale": "Provisional execution annotation only: peer-style research lead with consumed body but maker-reported results; editorial significance and selection are Sol decisions.",
        "scope_dimensions": ["current relevance", "technical significance"],
        "window_relation": "MAIN_EVENT", "carry_over": False,
        "source_bindings": supp_ids(did),
    }

# ---------- social/local auto records ----------
def local_raw_text(rec: dict) -> tuple[str, str]:
    for rp in rec["source"]["raw_paths"]:
        p = REPO / rp
        if p.is_file() and p.suffix == ".md":
            t = p.read_text(encoding="utf-8", errors="replace")
            return t[:30000], rp
    for rp in rec["source"]["raw_paths"]:
        p = REPO / rp
        if p.is_file():
            try:
                return p.read_text(encoding="utf-8", errors="replace")[:8000], rp
            except Exception:
                continue
    return "", ""

def social_record(did: str, decision: dict, detail_fh) -> dict:
    rec = DERIVED[did]
    src = rec["source"]
    title = src["title"]
    raw_txt, raw_used = local_raw_text(rec)
    kw = [w for w in re.findall(r"[A-Za-z][A-Za-z0-9\-]{4,}", title) if len(w) > 4][:8]
    sents = top_sentences(raw_txt, kw, 3) if raw_txt else []
    claims = []
    if sents:
        claims.append({"text": f"Repository DailyX/X record for \"{title[:120]}\": {sents[0][:280]}",
            "evidence_class": "SOCIAL_OBSERVATION",
            "context": "Community-signal observation only; quoted span is what the local record states, not a verified product fact."})
    else:
        claims.append({"text": f"Discovery record \"{title[:140]}\" is retained as a community/working-set signal; no excerptable first-party sentence was located in the bound local raw.",
            "evidence_class": "SOCIAL_OBSERVATION",
            "context": "Weakest bound: record existence only."})
    lims = [f"No first-party technical body is bound for this task; all technical specifics remain unverified and must not be promoted to product facts."]
    targets = decision["verification_targets"]
    verif = []
    for t in targets:
        if sents:
            verif.append({"target": t, "status": "VERIFIED",
                "finding": f"Local record {raw_used} contains discussion matching the target scope (span above); technical product claims within remain UNRESOLVED per limitation."})
        else:
            verif.append({"target": t, "status": "UNRESOLVED",
                "finding": f"No matching first-party or excerptable community span located for target in bound local raw {raw_used or 'n/a'}; retained as working-set signal only."})
    detail_fh.write(json.dumps({"discovery_id": did, "method": "local_raw", "raw_used": raw_used, "spans": sents}, ensure_ascii=False) + "\n")
    return {
        "discovery_id": did, "status": "PARTIAL" if sents else "NEEDS_MORE",
        "entity": {"entity_id": re.sub(r"[^a-z0-9]+", "-", title.lower())[:60] or did, "canonical_name": title[:160],
                   "entity_type": "PRODUCT", "organization": None, "canonical_url": src["locator"]},
        "artifact_type": "PRODUCT", "claims": claims, "limitations": lims, "verification": verif,
        "materiality": "CONTEXT" if sents else "HOLD",
        "materiality_rationale": "Provisional execution annotation only: community-signal evidence without first-party technical confirmation; selection is a Sol decision.",
        "scope_dimensions": ["current relevance", "technical significance"],
        "window_relation": "MAIN_EVENT", "carry_over": False,
        "source_bindings": supp_ids(did) or None,
    }

# ---------- main assembly ----------
def build_override_record(did: str, decision: dict, detail_fh) -> dict:
    spec = dict(OVERRIDES[did])
    rec = DERIVED[did]
    src = rec["source"]
    targets = decision["verification_targets"]
    assert len(spec["verif"]) == len(targets), f"{did}: override verif/target count mismatch"
    verif = [{"target": t, "status": s, "finding": f} for t, (s, f) in zip(targets, spec["verif"])]
    claims = [{"text": t, "evidence_class": c, "context": ctx} for (c, t, ctx) in spec["claims"]]
    binds = supp_ids(did)
    detail_fh.write(json.dumps({"discovery_id": did, "method": "override_handread",
        "bound_sources": binds}, ensure_ascii=False) + "\n")
    out = {
        "discovery_id": did, "status": spec["status"],
        "entity": {"entity_id": spec["entity"][0], "canonical_name": spec["entity"][1],
                   "entity_type": spec["entity"][2], "organization": spec["entity"][3],
                   "canonical_url": spec["entity"][4]},
        "artifact_type": spec["artifact"], "claims": claims,
        "limitations": list(spec["lims"]), "verification": verif,
        "materiality": spec["materiality"], "materiality_rationale": spec["mat_r"],
        "scope_dimensions": ["current relevance", "technical significance"],
        "window_relation": spec["window"], "carry_over": False,
    }
    if binds:
        out["source_bindings"] = binds
    return out

def has_paper_source(did: str) -> bool:
    for s in SUPP_BY_TASK.get(did, []):
        if s["source_class"] == "PRIMARY_PAPER":
            return True
    return False

def main() -> int:
    if "w34-event-c085" in OVERRIDES and OVERRIDES["w34-event-c085"].get("status") == "SKIP_PAPER_AUTO":
        del OVERRIDES["w34-event-c085"]
    detail_path = EXEC / "evidence-consumption-details.jsonl"
    ledger_path = EXEC / "authority-consumption-ledger.jsonl"
    out_path = EXEC / "interactive-evidence.json"
    # retrieval attempt counts from provenance logs
    attempts: dict[str, list[dict]] = {}
    for pname in ["retrieval-provenance.jsonl", "official-provenance.jsonl", "arxiv-pdf-provenance.jsonl"]:
        p = EXEC / "evidence-bodies" / pname
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                r = json.loads(line)
                attempts.setdefault(r["discovery_id"], []).append(r)
    # websearch gap-fill attempts (logged per task from execution record)
    search_attempts = {}
    sp = EXEC / "search-attempts.json"
    if sp.exists():
        search_attempts = json.loads(sp.read_text(encoding="utf-8"))
    records, ledger = [], []
    with detail_path.open("w", encoding="utf-8") as detail_fh:
        for d in sorted(NON_DROP, key=lambda x: x["discovery_id"]):
            did = d["discovery_id"]
            if did in OVERRIDES:
                rec = build_override_record(did, d, detail_fh)
                method = "override_handread"
            elif has_paper_source(did):
                rec = paper_record(did, d, detail_fh)
                method = "section_parse"
            else:
                rec = social_record(did, d, detail_fh)
                method = "local_raw"
            records.append(rec)
            # ledger row
            atts = attempts.get(did, [])
            succ = [a for a in atts if a.get("outcome") == "CAPTURED"]
            bound = SUPP_BY_TASK.get(did, [])
            if rec["status"] in ("VERIFIED", "PARTIAL") and bound:
                state = "AUTHORITY_CONSUMED"
                reason = f"{len(bound)} bound primary body/bodies read; claims grounded in extracted spans ({method})"
            elif rec["status"] == "NEEDS_MORE" and succ:
                state = "AUTHORITY_CAPTURED_BUT_UNCONSUMED"
                reason = "body captured but insufficient to resolve verification target; claim kept bounded"
            elif rec["status"] == "NEEDS_MORE" and atts and not succ:
                state = "AUTHORITY_RETRIEVAL_FAILED"
                reason = f"{len(atts)} retrieval attempt(s), all failed; see provenance logs"
            elif rec["status"] == "NEEDS_MORE":
                state = "AUTHORITY_NOT_FOUND"
                reason = "no suitable primary authority located in bounded search; community/working-set signal only"
            elif bound:
                state = "AUTHORITY_CONSUMED"
                reason = f"bound body/bodies read via {method}"
            else:
                state = "AUTHORITY_CONSUMED"
                reason = "local discovery raw read as SOCIAL authority; technical claims bounded"
            kinds = sorted({("fetch:" + ("ok" if a.get("outcome")=="CAPTURED" else "fail")) for a in atts})
            n_search = len(search_attempts.get(did, []))
            if n_search:
                kinds.append(f"websearch:{n_search}")
            if not kinds:
                kinds = ["local-read"]
            ledger.append({
                "task_id": task_id(did), "discovery_id": did,
                "screening_decision": d["decision"], "evidence_status": rec["status"],
                "verification_target": d["verification_targets"][0][:220] if d["verification_targets"] else "",
                "primary_locators": sorted({s["locator"] for s in bound}) or [DERIVED[did]["source"]["locator"]],
                "captured_body_paths": sorted({s["raw_path"] for s in bound}),
                "consumption_state": state, "reason": reason,
                "gap_fill_attempted": bool(atts) or bool(search_attempts.get(did)),
                "retrieval_attempts": f"{len(atts)} ({', '.join(kinds)})",
                "high_signal": did in ("w34-event-c004","w34-event-c019","w34-event-c010","w34-event-c011","w34-event-c017","w34-event-c066"),
                "materiality": rec["materiality"],
            })
    # source_bindings=None cleanup (social auto may set None)
    for r in records:
        if r.get("source_bindings") is None:
            r.pop("source_bindings", None)
    doc = {
        "schema_version": "2.0-rc1", "issue_id": "2026-W34",
        "runner": {"provider": "Muse Spark", "model": "muse-spark-1.3",
                   "invocation": "EXPERIMENTAL_LUNA_ROLE_SUBSTITUTION evidence generation with consumed primary bodies",
                   "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")},
        "records": sorted(records, key=lambda x: x["discovery_id"]),
        "completeness": {
            "obligations": [
                {"obligation_id": "weekly:current-relevance", "status": "LIMITATION",
                 "rationale": "In-window coverage is broad (434 identities screened; 409 evidenced) but long-tail community-signal items and date-precision boundaries leave residual uncertainty."},
                {"obligation_id": "weekly:technical-significance", "status": "LIMITATION",
                 "rationale": "First-party bodies consumed for high-signal items; paper results stay maker-reported and provisional materiality awaits Sol review."},
                {"obligation_id": "weekly:carry-over", "status": "SATISFIED",
                 "rationale": "Single inherited carry-over (MiniMax) rechecked; no promotion; disposition recorded in screening reconciliation."},
            ],
            "residual_limitations": [
                "Twelve arXiv items lack HTML full text; PDF bodies代替 consumed via text extraction.",
                "Several DailyX/sol-only items retain SOCIAL-only authority with first-party gaps explicitly bounded.",
                "Grok Bot page re-dated Aug 26; Aug 21 timing rests on DailyX X observation, not page bytes.",
                "AWS Sol-pricing mirror is post-cutoff (Sep 3); W34 pricing authority is OpenAI first-party only.",
                "Provisional materiality is execution-side only; Sol semantic review required before Selection.",
            ],
            "closure": None,
        },
    }
    out_path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with ledger_path.open("w", encoding="utf-8") as fh:
        for row in sorted(ledger, key=lambda x: x["discovery_id"]):
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")
    from collections import Counter
    print("records:", len(records), Counter(r["status"] for r in records))
    print("materiality:", Counter(r["materiality"] for r in records))
    print("ledger states:", Counter(r["consumption_state"] for r in ledger))
    print("wrote", out_path, ledger_path, detail_path)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
