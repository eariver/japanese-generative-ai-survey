#!/usr/bin/env python3
"""Compatibility wrapper enforcing bounded cross-package synthesis at Architecture.

The original v2 Architecture validator permitted packages with no direct
PRIMARY/SUPPORTING candidate placements. Drafting gives that shape one bounded
cross-package meaning when factual placements exist elsewhere: at most one such
package may exist, it must be final in drafting order, and another package must
own factual candidate placement that can be reused at Draft time.

This wrapper enforces those shared structural invariants before Architecture
Review. The previous Architecture implementation remains byte-for-byte in
``survey_architecture_v2_base.py`` and all unrelated behavior delegates to it.
Explicit ``selected_exceptions`` semantics remain owned by the frozen validator:
an exception can authorize omission of a selected candidate destination, but it
does not make an otherwise evidence-free package draftable.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

from scripts import survey_architecture_v2_base as _base

_ORIGINAL_VALIDATE_ARCHITECTURE = _base.validate_architecture


def _candidate_ids(package: dict[str, Any]) -> list[str]:
    primary = package.get("primary_candidate_ids")
    supporting = package.get("supporting_candidate_ids")
    if not isinstance(primary, list) or not isinstance(supporting, list):
        return []
    return [*primary, *supporting]


def _is_empty_placement_package(package: Any) -> bool:
    if not isinstance(package, dict):
        return False
    primary = package.get("primary_candidate_ids")
    supporting = package.get("supporting_candidate_ids")
    return (
        isinstance(primary, list)
        and isinstance(supporting, list)
        and not primary
        and not supporting
    )


def _empty_placement_contract_errors(architecture: dict[str, Any]) -> list[str]:
    """Enforce the Architecture-side half of the Draft synthesis contract."""
    packages = architecture.get("packages")
    if not isinstance(packages, list) or not packages:
        return []

    empty = [package for package in packages if _is_empty_placement_package(package)]
    if len(empty) > 1:
        return [
            "Issue Architecture permits at most one empty-placement cross-package synthesis package"
        ]
    if not empty:
        return []

    synthesis = empty[0]
    errors: list[str] = []
    order = synthesis.get("drafting_order")
    valid_orders = [
        package.get("drafting_order")
        for package in packages
        if isinstance(package, dict)
        and isinstance(package.get("drafting_order"), int)
        and not isinstance(package.get("drafting_order"), bool)
        and package.get("drafting_order") > 0
    ]
    if (
        isinstance(order, int)
        and not isinstance(order, bool)
        and order > 0
        and valid_orders
        and order != max(valid_orders)
    ):
        errors.append(
            "empty-placement cross-package synthesis package must be last in drafting order"
        )

    factual_placements = [
        candidate_id
        for package in packages
        if package is not synthesis and isinstance(package, dict)
        for candidate_id in _candidate_ids(package)
    ]
    if not factual_placements:
        errors.append(
            "empty-placement cross-package synthesis package requires prior factual candidate placements"
        )
    return errors


def validate_architecture(
    repo_root: Path,
    architecture: dict[str, Any],
    profile_path: Path,
    completeness_path: Path,
    ledger_path: Path,
    matrix_path: Path,
    selection_path: Path,
    require_approved: bool = False,
) -> list[str]:
    errors = _ORIGINAL_VALIDATE_ARCHITECTURE(
        repo_root,
        architecture,
        profile_path,
        completeness_path,
        ledger_path,
        matrix_path,
        selection_path,
        require_approved,
    )
    errors.extend(_empty_placement_contract_errors(architecture))
    return errors


# Ensure helpers defined in the frozen module (including review-summary/CLI
# paths) call the strengthened validator through their module global.
_base.validate_architecture = validate_architecture


def __getattr__(name: str) -> Any:
    return getattr(_base, name)


def main() -> int:
    return _base.main()


if __name__ == "__main__":
    raise SystemExit(main())
