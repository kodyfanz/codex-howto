# AGENTS.md

This repository is a standalone tutorial project for Codex. Every claim,
command, configuration file, and example must be valid for Codex.

## Source and product boundaries

- Treat authored Codex documentation as the source of truth. Do not use
  generated outputs or removed migration artifacts as curriculum sources.
- Verify product behavior against current official OpenAI documentation before
  documenting it.
- Prefer Codex-native concepts and paths even when the source project uses a
  different abstraction.
- Keep product claims scoped to the surface they apply to: Codex CLI, IDE,
  desktop app, cloud, or ChatGPT Work.
- Never copy credentials, local paths, analytics artifacts, or generated build
  output into the project.

## Curriculum structure

- Keep numbered tutorial modules in learning order.
- Each module contains a `README.md` plus copy-ready examples where useful.
- Use `.agents/skills/` for project skills and `.codex/agents/` for project
  custom-agent definitions.
- Use `.codex/config.toml` and Codex hook configuration formats for project
  configuration examples.
- Update the root index and learning roadmap whenever a module is added or its
  position changes.

## Documentation rules

- Write all repository content in English. Do not add translations or
  language-specific documentation trees unless the user changes this policy.
- Use relative links for repository content.
- Every fenced code block must declare a language.
- Keep examples safe by default and explain any command that changes external
  state.
- Never place real tokens, secrets, email addresses, or account identifiers in
  examples.
- Label experimental, deprecated, surface-specific, or account-dependent
  behavior explicitly.
- Prefer concise explanations followed by runnable examples and verification
  steps.

## Workflow

- Keep changes scoped to the current repository status and validate them with
  the release quality gate documented in `scripts/README.md`.
- Preserve unrelated user changes.
- Do not commit or push unless the user explicitly requests it.
- Run the relevant documentation checks after each completed phase once the
  validation toolchain has been ported.
