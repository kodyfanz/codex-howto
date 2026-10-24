# Weekly documentation drift check

Inspect the selected repository without modifying files or external systems.

Compare user-facing documentation with code, configuration, tests, and command
help changed since the previous successful run when that baseline is available.
Report only claims that are demonstrably stale, missing, or contradictory.

For each finding, include:

- the documentation file and heading;
- the source evidence that conflicts with it;
- the user impact;
- a concise suggested correction.

If no actionable drift is found, return `No actionable documentation drift` and
list the checks performed. If required source state is unavailable, return
`Check incomplete`, explain what is missing, and do not infer a result.

Do not edit files, open pull requests, post comments, send messages, or change
connections. Stop and request human input if verification would require access
outside the configured read-only environment.
