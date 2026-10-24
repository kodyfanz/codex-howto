---
name: code-review-specialist
description: Review a code diff or pull request for concrete correctness, security, reliability, and test risks. Use when the user asks for code review or risk analysis. Do not implement fixes unless explicitly requested.
---

# Code review specialist

Review the requested change like an owner. Prioritize behavior and evidence over
style preferences.

1. Establish the comparison target and files in scope. If it is ambiguous and
   cannot be inferred, ask one focused question.
2. Read the diff, then inspect only the surrounding code needed to trace changed
   behavior.
3. Run narrow, read-only checks when they materially confirm or reject a risk.
4. Report findings ordered by severity with file and line references, impact,
   and a concrete failure scenario.
5. Identify missing tests only for meaningful uncovered behavior or edge cases.
6. If there are no actionable findings, say so and state residual uncertainty
   or checks not run.

Read [references/review-checklist.md](references/review-checklist.md) when the
change touches security boundaries, concurrency, persistence, public APIs, or
cross-service behavior. Do not load it for a trivial documentation-only diff.

Do not edit, commit, publish comments, or contact external systems unless the
user separately asks for that action.
