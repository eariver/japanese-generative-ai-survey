#!/usr/bin/env python3
from pathlib import Path


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding='utf-8')
    count = text.count(old)
    if count != 1:
        raise SystemExit(f'{path}: replacement count {count} != 1 for {old[:120]!r}')
    p.write_text(text.replace(old, new), encoding='utf-8')


replace_once(
    'config/survey-production-v2.json',
    '      "schemas/stage-handoff-v2.schema.json",\n      "schemas/review-finding-v2.schema.json",',
    '      "schemas/stage-handoff-v2.schema.json",\n      "schemas/stage-handoff-request-v2.schema.json",\n      "schemas/review-finding-v2.schema.json",',
)

execute_current = '''\n\ndef execute_current(\n    repo_root: Path,\n    cfg: dict[str, Any],\n    state_path: Path,\n    orchestration_dir: Path,\n    registry: HandlerRegistry,\n    clock: Callable[[], datetime] = _now,\n) -> dict[str, Any]:\n    """Execute at most one current action and persist its exact spec/result.\n\n    Production handoffs bind the current Production State SHA, so model-assisted\n    stages are intentionally advanced one adopted handoff at a time. Terminal\n    Human/Exception/Complete actions are planned and persisted but not executed.\n    """\n    specs_dir = orchestration_dir / "specs"\n    results_dir = orchestration_dir / "results"\n    specs_dir.mkdir(parents=True, exist_ok=True)\n    results_dir.mkdir(parents=True, exist_ok=True)\n    _recover_all_pending(state_path, results_dir)\n    spec = plan_action(repo_root, cfg, state_path)\n    sequence = len(list(specs_dir.glob("*.json"))) + 1\n    safe_id = spec["action_id"].replace(":", "-")\n    spec_path = specs_dir / f"{sequence:03d}-{safe_id}.json"\n    write_action_spec(spec_path, spec)\n    if spec["action_kind"] in TERMINAL_KINDS:\n        return {\n            "terminal_reason": spec["next_terminal_reason"],\n            "action_spec_path": _relative_repo_path(repo_root, spec_path, "terminal Action Spec"),\n            "action_result_path": None,\n            "executed_actions": 0,\n            "lifecycle_state": core.load_json(state_path)["lifecycle_state"],\n        }\n    result_path = results_dir / f"{sequence:03d}-{safe_id}.json"\n    result = execute_action(repo_root, cfg, state_path, spec_path, result_path, registry, clock)\n    if result["status"] != "SUCCEEDED":\n        raise ValueError(\n            f"current deterministic action failed without creating a Human Gate: {spec['action_id']} status={result['status']}"\n        )\n    state = core.load_json(state_path)\n    return {\n        "terminal_reason": state["terminal_reason"],\n        "action_spec_path": _relative_repo_path(repo_root, spec_path, "Action Spec"),\n        "action_result_path": _relative_repo_path(repo_root, result_path, "Action Result"),\n        "executed_actions": 1,\n        "lifecycle_state": state["lifecycle_state"],\n    }\n'''
replace_once(
    'scripts/survey_orchestrator_v2.py',
    '\n\ndef advance_to_gate(repo_root: Path, cfg: dict[str, Any], state_path: Path, orchestration_dir: Path, registry: HandlerRegistry, clock: Callable[[], datetime] = _now, max_actions: int = 64) -> dict[str, Any]:',
    execute_current + '\n\ndef advance_to_gate(repo_root: Path, cfg: dict[str, Any], state_path: Path, orchestration_dir: Path, registry: HandlerRegistry, clock: Callable[[], datetime] = _now, max_actions: int = 64) -> dict[str, Any]:',
)
replace_once(
    'scripts/survey_orchestrator_v2.py',
    '    advance = sub.add_parser("advance-to-gate")\n    advance.add_argument("--state", required=True)\n    advance.add_argument("--orchestration-dir", required=True)\n    advance.add_argument("--handler-module", action="append", default=[])\n\n    approve = sub.add_parser("approve-architecture")',
    '    advance = sub.add_parser("advance-to-gate")\n    advance.add_argument("--state", required=True)\n    advance.add_argument("--orchestration-dir", required=True)\n    advance.add_argument("--handler-module", action="append", default=[])\n\n    current = sub.add_parser("execute-current")\n    current.add_argument("--state", required=True)\n    current.add_argument("--orchestration-dir", required=True)\n    current.add_argument("--handler-module", action="append", default=[])\n\n    approve = sub.add_parser("approve-architecture")',
)
replace_once(
    'scripts/survey_orchestrator_v2.py',
    '        if args.command == "advance-to-gate":\n            registry: HandlerRegistry = {}\n            for module_name in args.handler_module:\n                load_handler_module(module_name, registry)\n            result = advance_to_gate(root, cfg, _path(root, args.state), _path(root, args.orchestration_dir), registry)\n            print(json.dumps(result, ensure_ascii=False, indent=2))\n            return 0\n        if args.command == "approve-architecture":',
    '        if args.command in {"advance-to-gate", "execute-current"}:\n            registry: HandlerRegistry = {}\n            for module_name in args.handler_module:\n                load_handler_module(module_name, registry)\n            if args.command == "advance-to-gate":\n                result = advance_to_gate(root, cfg, _path(root, args.state), _path(root, args.orchestration_dir), registry)\n            else:\n                result = execute_current(root, cfg, _path(root, args.state), _path(root, args.orchestration_dir), registry)\n            print(json.dumps(result, ensure_ascii=False, indent=2))\n            return 0\n        if args.command == "approve-architecture":',
)
