#!/usr/bin/env python3
"""Provide the safety boundary for the readiness-only plugin."""

from __future__ import annotations

import json
import sys
from typing import Any


def main() -> int:
    try:
        event: Any = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        return 0

    if isinstance(event, dict) and event.get("hook_event_name") == "SessionStart":
        output = {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": (
                    "The DevOps Readiness plugin assesses evidence only. It does not "
                    "authorize deployment, rollback, or infrastructure mutation."
                ),
            }
        }
        print(json.dumps(output, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
