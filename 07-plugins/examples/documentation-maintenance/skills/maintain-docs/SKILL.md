---
name: maintain-docs
description: Update repository documentation to match verified code, configuration, or workflow changes. Use for focused documentation maintenance. Do not invent behavior or publish changes externally.
---

# Maintain Docs

Identify the audience and the behavior that changed. Inspect source code,
configuration, tests, and existing terminology before editing documentation.

Update the smallest set of pages needed to keep navigation and examples
consistent. Preserve the repository's style, link conventions, and language.
Label surface-specific, experimental, or account-dependent behavior.

When release notes are requested, use
[the bundled template](../../assets/release-note-template.md). Omit unused
sections rather than filling them with speculation.

Verify changed commands or examples without causing external side effects. Run
the repository's documentation checks when available and summarize what was
verified. Publishing, tagging, or announcing the result requires a separate
explicit request.
