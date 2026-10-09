#!/usr/bin/env python3
"""Edition-local P15 cross-package compatibility validator (this run only, no Core change).

Validates P15 draft-result.json evidence_refs against the UNION of:
 (a) canonical P15 draft-package.json evidence inputs, and
 (b) overlay-allowlisted evidence (p15-cross-package-synthesis-authority.json).

Rules: result schema unchanged; canonical package SHA binding maintained; normal refs via
canonical index; cross refs via overlay (accepted bytes/hash verified); FAIL map-outside
refs, unselected candidates, unknown evidence, subject mismatch, duplicates; attribution
checks identical to frozen validator.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path("/home/eariver/git/japanese-generative-ai-survey")
SRC = ROOT / "sources/SP-vision-multimodal-2026"
EXECDIR = SRC / "execution/content-revision-r4-20261004"

REF_KINDS = {"EVENT", "CLAIM", "METRIC", "LIMITATION"}
SUBJECT_ROLES = {"PRIMARY_SUBJECT", "SUPPORTING_SUBJECT", "CONTEXT_SUBJECT"}


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(65536), b""):
            h.update(c)
    return h.hexdigest()


def _card_index(cards: dict[str, dict]) -> dict[tuple[str, str, str], tuple[str, str, str | None]]:
    index = {}
    for task_id, card in cards.items():
        for row in card.get("temporal", {}).get("events", []):
            index[(task_id, "EVENT", row["event_id"])] = (row["subject_id"], row["subject_role"], None)
        for kind, rows, idk in (("CLAIM", card.get("claims", []), "statement_id"),
                                ("METRIC", card.get("metrics", []), "metric_id"),
                                ("LIMITATION", card.get("limitations", []), "statement_id")):
            for row in rows:
                index[(task_id, kind, row[idk])] = (row["subject_id"], row["subject_role"], row.get("evidence_class"))
    return index


def validate_p15_result(result: dict, package_path: Path, overlay_path: Path) -> list[str]:
    errors: list[str] = []
    package = json.loads(package_path.read_text(encoding="utf-8"))
    overlay = json.loads(overlay_path.read_text(encoding="utf-8"))
    # Canonical package binding: P15 package file must equal current canonical bytes
    # (checked by caller via sha; here verify overlay SHAs match package basis)
    basis = package.get("basis", {})
    for k in ("architecture_sha256", "candidate_matrix_sha256", "evidence_acceptance_sha256"):
        ov = overlay.get(k)
        if ov != basis.get(k):
            errors.append(f"overlay {k} does not match canonical P15 package basis")
    # Build canonical cards
    canon_cards = {i["evidence_task_id"]: i["evidence_card"] for i in package.get("evidence_inputs", [])}
    # Build overlay cards (verify accepted bytes)
    norm = json.loads((SRC / "orchestration/v2/checkpoints/CANDIDATES_NORMALIZED.json").read_text(encoding="utf-8"))
    by_name = {r["name"]: r for r in norm["artifacts"]}
    ev_acc_path = (ROOT / by_name["evidence-acceptance"]["path"]).resolve()
    ev_acc = json.loads(ev_acc_path.read_text(encoding="utf-8"))
    ev_by_task = {r["evidence_task_id"]: r for r in ev_acc["results"]}
    overlay_cards: dict[str, dict] = {}
    allow_tasks: set[str] = set()
    for e in overlay["entries"]:
        tid = e["evidence_task_id"]
        allow_tasks.add(tid)
        if tid in overlay_cards:
            continue
        meta = ev_by_task.get(tid)
        if meta is None or meta["sha256"] != e["evidence_sha256"]:
            errors.append(f"overlay acceptance mismatch: {tid}")
            continue
        p = ev_acc_path.parent / "results" / meta["filename"]
        raw = p.read_bytes()
        if hashlib.sha256(raw).hexdigest() != e["evidence_sha256"]:
            errors.append(f"overlay card bytes drift: {tid}")
            continue
        overlay_cards[tid] = json.loads(raw.decode("utf-8"))
    # Selection check: all overlay candidates must be SELECTED
    sel = json.loads((SRC / "candidate-selection-v2.json").read_text(encoding="utf-8"))
    disp = {a["candidate_id"]: a["disposition"] for a in sel["assignments"]}
    for e in overlay["entries"]:
        if disp.get(e["candidate_id"]) != "SELECTED":
            errors.append(f"overlay unselected candidate: {e['candidate_id']}")
    union_cards = dict(canon_cards)
    for k, v in overlay_cards.items():
        union_cards.setdefault(k, v)
    index = _card_index(union_cards)
    canon_tasks = set(canon_cards)
    # Check each ref
    def check_refs(refs, label):
        if not isinstance(refs, list):
            errors.append(f"{label} evidence_refs must be an array")
            return []
        classes = []
        seen = set()
        for off, ref in enumerate(refs):
            prefix = f"{label}.evidence_refs[{off}]"
            if not isinstance(ref, dict) or set(ref) != {"evidence_task_id", "kind", "evidence_id", "subject_id", "subject_role"}:
                errors.append(f"{prefix} fields invalid")
                continue
            if ref.get("kind") not in REF_KINDS or ref.get("subject_role") not in SUBJECT_ROLES:
                errors.append(f"{prefix} kind/subject_role invalid")
                continue
            key = (ref["evidence_task_id"], ref["kind"], ref["evidence_id"])
            exp = index.get(key)
            if exp is None:
                errors.append(f"{prefix} references Evidence outside union authority or unknown stable ID")
                continue
            # allowlist enforcement for cross tasks
            tid = ref["evidence_task_id"]
            if tid not in canon_tasks and tid not in allow_tasks:
                errors.append(f"{prefix} references non-allowlisted cross-package Evidence")
                continue
            if (ref["subject_id"], ref["subject_role"]) != exp[:2]:
                errors.append(f"{prefix} subject binding does not match factual Evidence")
            classes.append(exp[2] or "PRIMARY_FACT")
            full = (key[0], key[1], key[2], ref["subject_id"], ref["subject_role"])
            if full in seen:
                errors.append(f"{prefix} duplicates an Evidence reference")
            seen.add(full)
        return classes

    def check_attr(mode, refs, classes, label):
        if mode not in {"FACTUAL", "ATTRIBUTED", "INFERENCE", "MIXED", "SOCIAL", "NONE"}:
            errors.append(f"{label} attribution_mode invalid")
            return
        if mode == "NONE" and refs:
            errors.append(f"{label} attribution_mode NONE cannot carry Evidence refs")
        if mode != "NONE" and not refs:
            errors.append(f"{label} attributed/factual text requires Evidence refs")
        if "INFERENCE" in classes and mode not in {"INFERENCE", "MIXED"}:
            errors.append(f"{label} inference Evidence requires INFERENCE or MIXED attribution")
        if "SOCIAL_OBSERVATION" in classes and mode not in {"SOCIAL", "MIXED"}:
            errors.append(f"{label} social Evidence requires SOCIAL or MIXED attribution")
        if any(v in {"VENDOR_CLAIM", "PROJECT_CLAIM", "AUTHOR_CLAIM"} for v in classes) and mode not in {"ATTRIBUTED", "MIXED"}:
            errors.append(f"{label} claimed Evidence requires ATTRIBUTED or MIXED attribution")

    deck_refs = result.get("deck_evidence_refs")
    classes = check_refs(deck_refs, "deck")
    check_attr(result.get("deck_attribution_mode"), deck_refs if isinstance(deck_refs, list) else [], classes, "deck")
    for off, block in enumerate(result.get("blocks", [])):
        prefix = f"blocks[{off}]"
        refs = block.get("evidence_refs")
        c2 = check_refs(refs, prefix)
        check_attr(block.get("attribution_mode"), refs if isinstance(refs, list) else [], c2, prefix)
    return errors


if __name__ == "__main__":
    import sys
    res_path = Path(sys.argv[1])
    pkg_path = Path(sys.argv[2])
    ov_path = Path(sys.argv[3]) if len(sys.argv) > 3 else (EXECDIR / "p15-cross-package-synthesis-authority.json")
    res = json.loads(res_path.read_text(encoding="utf-8"))
    errs = validate_p15_result(res, pkg_path, ov_path)
    print(json.dumps({"errors": errs}, ensure_ascii=False, indent=2))
    raise SystemExit(1 if errs else 0)
