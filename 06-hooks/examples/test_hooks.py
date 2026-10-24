#!/usr/bin/env python3
"""Run deterministic tests for the tutorial hook handlers."""

from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


EXAMPLES = Path(__file__).resolve().parent


def run_handler(name: str, payload: object | str) -> subprocess.CompletedProcess[str]:
    stdin = payload if isinstance(payload, str) else json.dumps(payload)
    return subprocess.run(
        [sys.executable, str(EXAMPLES / name)],
        input=stdin,
        text=True,
        capture_output=True,
        check=False,
        timeout=5,
    )


class PreToolPolicyTests(unittest.TestCase):
    def test_safe_command_has_no_output(self) -> None:
        result = run_handler(
            "pre_tool_policy.py",
            {
                "hook_event_name": "PreToolUse",
                "tool_name": "Bash",
                "tool_input": {"command": "git status --short"},
            },
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")

    def test_destructive_command_is_denied(self) -> None:
        result = run_handler(
            "pre_tool_policy.py",
            {
                "hook_event_name": "PreToolUse",
                "tool_name": "Bash",
                "tool_input": {"command": "git reset --hard"},
            },
        )
        output = json.loads(result.stdout)
        decision = output["hookSpecificOutput"]
        self.assertEqual(decision["hookEventName"], "PreToolUse")
        self.assertEqual(decision["permissionDecision"], "deny")

    def test_malformed_input_is_denied_without_traceback(self) -> None:
        result = run_handler("pre_tool_policy.py", "not-json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(
            json.loads(result.stdout)["hookSpecificOutput"]["permissionDecision"],
            "deny",
        )
        self.assertEqual(result.stderr, "")


class SessionStartTests(unittest.TestCase):
    def test_security_file_adds_context(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "SECURITY.md").write_text("# Security\n", encoding="utf-8")
            result = run_handler(
                "session_start.py",
                {
                    "hook_event_name": "SessionStart",
                    "cwd": directory,
                },
            )
        output = json.loads(result.stdout)
        self.assertIn("SECURITY.md", output["hookSpecificOutput"]["additionalContext"])

    def test_missing_security_file_has_no_output(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            result = run_handler(
                "session_start.py",
                {
                    "hook_event_name": "SessionStart",
                    "cwd": directory,
                },
            )
        self.assertEqual(result.stdout, "")


if __name__ == "__main__":
    unittest.main()
