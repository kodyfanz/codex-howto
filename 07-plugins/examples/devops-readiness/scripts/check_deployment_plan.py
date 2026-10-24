#!/usr/bin/env python3
"""Validate the structure of a deployment-readiness plan without deploying."""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any


REQUIRED_TEXT = ("environment", "version", "owner", "rollback_trigger")
REQUIRED_LISTS = ("preflight_checks", "monitoring_signals", "rollback_steps")


def validate(value: Any) -> list[str]:
    if not isinstance(value, dict):
        return ["The plan must be a JSON object."]

    errors: list[str] = []
    for key in REQUIRED_TEXT:
        if not isinstance(value.get(key), str) or not value[key].strip():
            errors.append(f"{key} must be a non-empty string.")
    for key in REQUIRED_LISTS:
        items = value.get(key)
        if not isinstance(items, list) or not items:
            errors.append(f"{key} must be a non-empty array.")
        elif not all(isinstance(item, str) and item.strip() for item in items):
            errors.append(f"{key} entries must be non-empty strings.")
    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_deployment_plan.py PLAN.json", file=sys.stderr)
        return 2

    path = Path(sys.argv[1])
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"invalid plan: {error}", file=sys.stderr)
        return 1

    errors = validate(value)
    if errors:
        for error in errors:
            print(f"- {error}")
        return 1

    print("Deployment plan structure is complete; human evidence review is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
