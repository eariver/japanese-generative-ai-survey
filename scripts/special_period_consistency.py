#!/usr/bin/env python3
"""Compatibility entry point for Special period consistency."""
from __future__ import annotations

from scripts.special_period_consistency_core import *  # noqa: F401,F403


def main() -> int:
    from scripts import special_period_consistency_retrospective as retrospective
    return retrospective.main()


if __name__ == "__main__":
    raise SystemExit(main())
