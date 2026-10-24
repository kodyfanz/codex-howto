#!/usr/bin/env python3
"""Tests for the deployment-plan structure validator."""

from __future__ import annotations

import unittest

from check_deployment_plan import validate


class ValidationTests(unittest.TestCase):
    def test_complete_plan(self) -> None:
        plan = {
            "environment": "staging",
            "version": "example-version",
            "owner": "release manager",
            "rollback_trigger": "error budget threshold exceeded",
            "preflight_checks": ["tests passed"],
            "monitoring_signals": ["request error rate"],
            "rollback_steps": ["restore the previous approved version"],
        }
        self.assertEqual(validate(plan), [])

    def test_missing_fields(self) -> None:
        errors = validate({"environment": "staging"})
        self.assertTrue(any("version" in error for error in errors))
        self.assertTrue(any("rollback_steps" in error for error in errors))

    def test_non_object(self) -> None:
        self.assertEqual(validate([]), ["The plan must be a JSON object."])


if __name__ == "__main__":
    unittest.main()
