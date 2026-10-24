---
name: review-change
description: Review a local diff or pull-request patch for actionable correctness, security, compatibility, and test risks. Use when the user asks for code review. Do not implement fixes or publish review comments unless separately requested.
---

# Review Change

Inspect the actual diff and the minimum surrounding code needed to validate each
finding. Read repository instructions before applying general conventions.

Prioritize behavior-changing defects over style preferences. For every finding:

- cite the file and narrowest useful line or symbol;
- describe the concrete failure scenario;
- explain impact and confidence;
- suggest the smallest safe direction for remediation.

Check tests only where the change creates a meaningful regression risk. State
when a concern cannot be confirmed from available evidence.

Return findings ordered by severity. If no actionable finding is supported,
say so and mention any verification gap. Do not modify files, submit comments,
or change external state unless the user explicitly expands the task.
