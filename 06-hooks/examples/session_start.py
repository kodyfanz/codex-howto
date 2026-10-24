#!/usr/bin/env python3
"""Add a small amount of repository context at session start."""

from __future__ import annotations

import json
from pathlib import Path
import sys
from typing import Any


def main() -> int:
    try:
        event: Any = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        print(json.dumps({"systemMessage": "Session hook received invalid JSON."}))
        return 0

    if not isinstance(event, dict) or event.get("hook_event_name") != "SessionStart":
        return 0

    cwd = event.get("cwd")
    if not isinstance(cwd, str):
        return 0

    if (Path(cwd) / "SECURITY.md").is_file():
        output = {
            "hookSpecificOutput": {
                "hookEventName": "SessionStart",
                "additionalContext": (
                    "This repository contains SECURITY.md. Read it before changing "
                    "authentication, authorization, secrets, or security controls."
                ),
            }
        }
        print(json.dumps(output, separators=(",", ":")))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
