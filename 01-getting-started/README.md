# Getting started with Codex

Codex can work from a terminal, beside your editor, in the ChatGPT desktop app, or in a hosted cloud environment. This module helps you choose a surface, complete one small repository task, and verify the result before granting more authority.

## Learning objectives

By the end of this module, you will be able to:

- Choose a Codex surface that matches the task.
- Install and authenticate the CLI when terminal work is appropriate.
- Start Codex in the intended project directory.
- Write a task prompt with a concrete outcome and verification step.
- Inspect the session configuration and review file changes.
- Distinguish built-in slash commands from reusable skills.

## The shortest path for a first session

If you already have Codex open, skip installation and sign-in. Choose one surface, open a practice repository, start with a read-only question, then try the small documentation edit below. You do not need every Codex feature to complete this module.

If a product term is unfamiliar, use the [glossary](../GLOSSARY.md). The [learning roadmap](../LEARNING-ROADMAP.md) is optional guidance for choosing what to study next.

Before asking Codex to edit, confirm it is working in the intended project and use the permission settings provided by your environment. The sandbox limits where commands can operate; the approval policy controls when Codex asks before an action. Do not bypass a permission prompt to make the first exercise easier. Module 8 explains these controls in depth.

## Choose a surface

| Surface                 | Start here when                                          | Context to remember                                        |
| ----------------------- | -------------------------------------------------------- | ---------------------------------------------------------- |
| **Codex CLI**           | You work primarily in a terminal or need scripting later | The working directory and shell environment matter         |
| **IDE extension**       | You want editor selection and open-file context          | Confirm which workspace and files are attached             |
| **ChatGPT desktop app** | You want local projects, visual review, or longer tasks  | Choose the folder and permission mode intentionally        |
| **Codex cloud**         | The task should run in a hosted environment              | Repository access and environment setup must already exist |

Feature availability can differ by account, workspace policy, operating system, and client version. A successful sign-in does not guarantee access to every surface.

## Ask a read-only question first

Before making a change, try a prompt like this in the surface you chose:

```text
Explain in plain language what this project is for. Point me to its README,
main program file if there is one, and any documented test command. Do not edit
files or run commands. Cite supporting paths and say what you could not confirm.
```

This lets you check that Codex is looking at the right project before you ask for an edit. If you are using a CLI, confirm the working directory with `/pwd` or `/status`.

## Install the CLI

> **CLI only**: Skip this section if you are using the IDE extension, desktop
> app, or cloud environment.

The npm package installs the Codex CLI globally:

```bash
npm install --global @openai/codex
```

Verify that the executable is available:

```bash
codex --version
codex --help
```

Use your normal package-management policy in managed environments. If your organization pins a version, install the approved version rather than updating independently.

## Sign in

> **CLI only**: Sign-in steps differ across Codex surfaces. If you are using
> the IDE extension, desktop app, or cloud, follow its current sign-in flow.

For an interactive ChatGPT sign-in, run:

```bash
codex login
```

Complete the browser flow, then inspect the active authentication method:

```bash
codex login status
```

The CLI also supports API-key authentication for usage-based local workflows.
Pass the key through standard input; do not place it directly in shell history:

```bash
printenv OPENAI_API_KEY | codex login --with-api-key
```

ChatGPT sign-in and API-key sign-in can provide different feature availability, billing, workspace controls, and data-handling policies. Codex cloud requires ChatGPT sign-in.

> **Important**: Treat cached authentication data as credentials. Never copy it
> into a repository, issue, prompt, or tutorial example.

## Start in the correct directory

Move to a small repository where you can safely review changes, or use a disposable copy:

```bash
cd /path/to/your-practice-project
codex
```

If the project uses Git, run `git status --short` before asking Codex to edit.
If it does not, make a disposable copy so you can compare the result safely.

You can also set the working directory without changing your current shell:

```bash
codex --cd /path/to/your-practice-project
```

Inside the interactive CLI, use `/pwd` or `/cd` to check the working directory and `/status` to inspect the active model, permissions, writable roots, and remaining context.

## Write a useful first task

A strong task prompt states the outcome, scope, constraints, and verification.
For example:

```text
Read this repository and add a short "Local development" section to README.md.
Use only commands already documented in the repository. Do not change source
code or dependency files. After editing, show the diff and check that every
referenced command exists in the project configuration.
```

This prompt gives Codex enough room to investigate while keeping the edit small and reviewable. You do not need to prescribe every shell command.

## Review before accepting the result

In the CLI, type:

```text
/diff
```

Check that:

- Only expected files changed.
- The content matches the requested scope.
- No credentials or machine-specific paths were added.
- Commands and links are verifiable.
- Codex reports any check it could not run.

Then run the repository's relevant test, lint, or documentation check. If the project has no automated check for the edited file, inspect the rendered output or use a focused manual verification.

## A few useful CLI commands

These are useful early commands in the CLI:

| Command        | Purpose                                                   |
| -------------- | --------------------------------------------------------- |
| `/status`      | Inspect session configuration and context usage           |
| `/permissions` | Review or change what Codex may do without asking         |
| `/diff`        | Review tracked and untracked file changes                 |

Type `/` to see commands supported by your installed version. Find more
examples, including `/mention`, `/plan`, `/compact`, `/init`, `/skills`,
`/new`, and `/quit`, in the [quick reference](../QUICK_REFERENCE.md). Built-in slash commands control the client or session. Reusable team workflows belong in [skills](../03-skills/README.md).

To use one in the CLI, type `$` in the Codex prompt, choose a skill, then add your request after its name. For example:

```text
$lesson-quiz Quiz me on Module 1 as a pre-test.
```

Enter this in Codex's prompt, not as a terminal command. For the full steps and what to check if a skill is unavailable, see [Module 3](../03-skills/README.md).

## Hands-on exercise: one safe documentation change

### Prerequisites

- A disposable project or a version-controlled project.
- A clean or understood working tree.
- One README with a small factual omission.

> **CLI path**: The commands below use the CLI. In the IDE or desktop app, open
> the same practice project and use that surface's controls to inspect the
> workspace and review changes.

### Step 1: Record the baseline

If the practice project is a Git repository, run:

```bash
git status --short
```

Otherwise, use a fresh disposable copy and note the files you intend to change.

If the output contains existing changes, note their files and do not ask Codex to overwrite them.

### Step 2: Start Codex

```bash
codex --cd /path/to/your-practice-project
```

Run `/status` and confirm the working directory and permissions.

### Step 3: Request a bounded edit

```text
Inspect this project and add one concise "How to verify the setup" subsection
to README.md. Use only facts supported by files in this repository. Do not
change code, configuration, or dependencies. Run an appropriate documentation
check if one exists, then summarize the evidence you used.
```

### Step 4: Review the result

If you are using the CLI, run `/diff`; in another surface, open its changes view. If the practice project uses Git, inspect the working tree from a second terminal:

```bash
git status --short
git diff -- README.md
```

Without Git, open the README and confirm that only the intended section changed.

### Step 5: Verify

Run the documentation check named by the repository. If there is none, confirm that headings render correctly and every command or link in the new subsection exists.

### Success criteria

- Only `README.md` changed.
- The new text is supported by repository evidence.
- The relevant check passes, or the manual verification is documented.
- You can explain the difference between the sandbox and approval policy used.

### Optional follow-up: a small code change

If you are working in a code repository, choose a small, well-understood issue with a focused test. First ask Codex to trace the relevant behavior without editing. Then ask for the smallest fix, the focused test, and a diff review. Avoid dependency changes, external services, and broad refactors in this first code exercise. If no suitable issue is clear, skip it.

For example, adapt these requests to the project:

```text
Trace <specific behavior> through the relevant code and tests. Do not edit or
run commands yet. Tell me which focused test would verify a small correction.
```

```text
Make the smallest change needed to fix <specific observed failure>. Do not
change dependencies or unrelated behavior. Run the focused test you identified,
then summarize the result and review the diff.
```

## Troubleshooting

### `codex` is not found

Confirm that Node.js and npm are installed, reinstall the global package, and check that npm's global binary directory is on `PATH`.

### The browser login cannot return to the CLI

Remote or headless environments may not support the local callback. If enabled for your account or workspace, use device-code authentication:

```bash
codex login --device-auth
```

### Codex opened the wrong project

Use `/pwd` in the CLI or restart with `codex --cd <directory>`. Do not grant additional directory access until you have confirmed the intended project root.

### Instructions or changes look unexpected

Run `/status`, inspect the nearest `AGENTS.md` and `AGENTS.override.md` files, and review `/diff`. Start a fresh session after changing persistent instructions.

## Next step

Continue to [Project instructions with AGENTS.md](../02-agents-md/README.md) if you want stable repository conventions available in future tasks. Modules 3–10 are specialized; choose one when you need that capability rather than treating the whole sequence as a prerequisite.

## Official resources

- [Quickstart](https://learn.chatgpt.com/docs/quickstart.md)
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli.md)
- [Authentication](https://learn.chatgpt.com/docs/auth.md)
- [CLI command reference](https://learn.chatgpt.com/docs/developer-commands.md?surface=cli)
- [Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security.md)
