#!/usr/bin/env python3
"""Profile/Publication-owned Draft extension preservation for Core v2.

The generic Draft validator intentionally does not interpret Profile semantics.
This validator forms the adjacent Profile/Publication layer: extension directives
approved in Architecture and copied into the Draft Package must survive Draft
Result generation exactly. Later Profile validators may add semantic checks on
those owned values without moving Weekly/Thematic vocabulary into Core.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from scripts import survey_production_v2 as core


def validate_extension_propagation(
    result: dict[str, Any], package: dict[str, Any]
) -> list[str]:
    errors: list[str] = []
    for identity in ("issue_id", "research_profile", "publication_profile", "package_id"):
        if result.get(identity) != package.get(identity):
            errors.append(f"Draft extension validation identity mismatch: {identity}")

    for key, owner in (
        ("profile_extensions", "Research Profile"),
        ("publication_extensions", "Publication Profile"),
    ):
        package_value = package.get(key)
        result_value = result.get(key)
        if not isinstance(package_value, dict) or not isinstance(result_value, dict):
            errors.append(f"{owner} Draft extensions must be objects")
            continue
        if result_value != package_value:
            errors.append(
                f"{owner} Draft extensions must exactly preserve the authorized Draft Package directives"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", required=True)
    parser.add_argument("--result", required=True)
    args = parser.parse_args()
    try:
        package_path = Path(args.package)
        result_path = Path(args.result)
        package = core.load_json(package_path)
        result = core.load_json(result_path)
        errors = validate_extension_propagation(result, package)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(json.dumps({"passed": not errors, "errors": errors}, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
