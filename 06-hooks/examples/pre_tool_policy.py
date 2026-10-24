#!/usr/bin/env python3
"""Illustrative PreToolUse policy for a small set of destructive commands."""

from __future__ import annotations

import json
import re
import sys
from typing import Any


BLOCKED_PATTERNS = (
    (re.compile(r"(^|[;&|]\s*)git\s+reset\s+--hard(?:\s|$)"), "git reset --hard"),
    (re.compile(r"(^|[;&|]\s*)git\s+clean\s+-[^\s]*f"), "git clean with force"),
    (re.compile(r"(^|[;&|]\s*)rm\s+-[^\s]*r[^\s]*f(?:\s|$)"), "recursive forced removal"),
)


def deny(reason: str) -> None:
    result = {
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }
    print(json.dumps(result, separators=(",", ":")))


def load_event() -> dict[str, Any] | None:
    try:
        value = json.load(sys.stdin)
    except (json.JSONDecodeError, OSError):
        deny("The command was blocked because the hook input was not valid JSON.")
        return None

    if not isinstance(value, dict):
        deny("The command was blocked because the hook input was not an object.")
        return None
    return value


def main() -> int:
    event = load_event()
    if event is None:
        return 0

    if event.get("hook_event_name") != "PreToolUse" or event.get("tool_name") != "Bash":
        return 0

    tool_input = event.get("tool_input")
    command = tool_input.get("command") if isinstance(tool_input, dict) else None
    if not isinstance(command, str) or not command.strip():
        deny("The command was blocked because tool_input.command was missing.")
        return 0

    for pattern, label in BLOCKED_PATTERNS:
        if pattern.search(command):
            deny(f"Tutorial policy blocks {label}; request explicit human review.")
            return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
