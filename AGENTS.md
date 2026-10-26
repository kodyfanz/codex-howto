# AGENTS.md

This repository is a standalone tutorial project for Codex. Every claim, command, configuration file, and example must be valid for Codex.

## Source and product boundaries

- Treat authored Codex documentation as the source of truth. Do not use generated outputs or removed migration artifacts as curriculum sources.
- Verify product behavior against current official OpenAI documentation before documenting it.
- Prefer Codex-native concepts and paths even when the source project uses a different abstraction.
- Keep product claims scoped to the surface they apply to: Codex CLI, IDE, desktop app, cloud, or ChatGPT Work.
- Never copy credentials, local paths, analytics artifacts, or generated build output into the project.

## Curriculum structure

- Keep numbered tutorial modules in learning order.
- Each module contains a `README.md` plus copy-ready examples where useful.
- Treat placeholder-bearing files in `examples/` as reusable source templates,
  not as the completed learner output; the lesson must show the concrete
  practice content separately.
- Use `.agents/skills/` for project skills and `.codex/agents/` for project custom-agent definitions.
- Use `.codex/config.toml` and Codex hook configuration formats for project configuration examples.
- Never edit `site/` or `dist/` as curriculum sources; rebuild them from the
  authored files with the release tooling.
- Update the root index and learning roadmap whenever a module is added or its position changes.

## Documentation rules

- Write all repository content in English. Do not add translations or language-specific documentation trees unless the user changes this policy.
- Use relative links for repository content.
- Every fenced code block must declare a language.
- Keep examples safe by default and explain any command that changes external state.
- Never place real tokens, secrets, email addresses, or account identifiers in examples.
- Label experimental, deprecated, surface-specific, or account-dependent behavior explicitly.
- Prefer concise explanations followed by runnable examples and verification steps.

## Lesson authoring contract

Every hands-on lesson must be usable by a first-time learner without guessing
the missing setup. Keep the following structure, adapted to the module's
subject:

- State the learning objective and prerequisites before the exercise.
- Identify the exact starting directory and explain why it is the correct
  scope. Say what learners must avoid, such as running in this checkout, a
  nested repository, or a parent tree with an unrelated `AGENTS.md`.
- Put steps in execution order. Each step must name the surface being used and
  provide copy-ready commands or prompts with declared languages.
- Include a small demonstration or read-only inspection before the first
  change, so learners can confirm context and understand the purpose.
- Specify the requested change, its file scope, and constraints. Do not leave a
  standalone code block without explaining what to paste, where to run it, or
  why it is needed.
- Treat every code, TOML, JSON, YAML, or configuration block as an action the
  learner must be able to place correctly. Immediately before or after each
  block, state all of the following when applicable: the exact destination path
  and filename, the directory or surface where a command runs, whether the
  block is required or optional, its scope (user, project, plugin, or
  temporary), what it changes, and the observable result to expect.
- Never show a configuration snippet without identifying the configuration file
  that owns it. If a setting has both user and project scopes, show the
  recommended scope for the exercise and explain how the other scope differs.
- For an optional or advanced snippet, say explicitly that it is not part of
  the main exercise and explain when a learner should use it. If a snippet
  references a filename, command, environment variable, or placeholder, give
  the next action required to create or replace that value.
- Review lessons for orphan blocks: a reader should never have to infer what
  to copy, where to put it, whether to execute it, or how to verify it.
- Keep files in a module's example directories as reusable templates with
  placeholders when they are intended for real repositories. Put the
  placeholder-free, practice-specific version directly in the lesson so a
  learner can copy it and complete the exercise without inventing values.
- Explain the exact destination path and filename for every practice file. A
  learner may create it with an editor they know or with `nano`; the lesson
  should not require a particular editor. State that the placeholder template
  is the basic starting point for a real repository, where paths, commands, and
  rules must be replaced with verified project-specific facts.
- Include independent verification commands, expected output or observable
  results, success criteria, and the learning outcome. Learners should be able
  to tell whether the exercise worked without trusting an agent summary.
- List every required external executable or service before the first example
  that uses it, including tools such as `codex`, `rg`, `curl`, `jq`, `python3`,
  or `npx`. Give a small version or availability check and either a supported
  fallback or a clear instruction to stop/skip the dependent step when it is
  unavailable. Never make a learner discover a missing prerequisite only from
  `command not found`.
- Explain cleanup for disposable resources and identify any command that
  changes external state. Preserve a safe default and never use a real secret,
  account, or machine-specific path.

When a module teaches a repository-scoped feature, prefer an isolated practice
repository with an explicit root. Reuse the detailed sequence in Module 2 as
the consistency model: enter the tutorial checkout, create or inspect the
practice project, enter the practice project before starting Codex, perform the
smallest meaningful action, review the diff, verify the result, and clean up.
Future module revisions should keep this structure unless the feature itself
requires a different workflow; explain the exception in the lesson.

## Workflow

- Keep changes scoped to the current repository status and preserve unrelated
  user changes.
- Run focused checks while editing and the release quality gate documented in
  `scripts/README.md` before handoff.
- Do not commit or push unless the user explicitly requests it.
- Run the relevant documentation checks after each completed phase once the validation toolchain has been ported.
