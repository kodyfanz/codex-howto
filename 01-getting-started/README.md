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
`/new`, and `/quit`, in the [quick reference](../QUICK_REFERENCE.md). Built-in slash commands control the client or session.

Reusable team workflows belong in [skills](../03-skills/README.md). To use one in the CLI, type `$` in the Codex prompt, choose a skill, then add your request after its name. For example:

```text
$lesson-quiz Quiz me on Module 1 as a pre-test.
```

Enter this in Codex's prompt, not as a terminal command. For the full steps and what to check if a skill is unavailable, see [Module 3](../03-skills/README.md).

## Hands-on exercise: one safe documentation change

### Prerequisites

- Codex CLI installed and authenticated, or an IDE/desktop session ready.
- A disposable Git repository created outside this checkout and outside any
  parent directory that already contains a project-level `AGENTS.md`.
- A terminal with `git` and `rg` available for independent diff and
  verification commands.

> **CLI path**: The commands below use the CLI. In the IDE or desktop app, open
> the same practice project and use that surface's controls to inspect the
> workspace and review changes.

Check the command-line tools before continuing:

```bash
git --version
rg --version
```

If `rg` is unavailable, install it or use an equivalent read-only search such
as `grep -n` for the verification step.

### Step 0: Enter the tutorial checkout

Use the real path to this checkout. The variable makes later copy-ready
commands unambiguous.

```bash
cd /path/to/codex-howto
TUTORIAL_ROOT="$PWD"
```

### Step 1: Create an isolated practice project

Create the practice project outside this checkout, outside another repository,
and outside a directory tree that already contains a project-level
`AGENTS.md`. This keeps unrelated instructions from changing the exercise.

The Bash block below is a convenience setup, not a required Codex skill. It
creates a temporary directory, initializes it as a Git repository, writes a
minimal `README.md`, prints the path, confirms that Git recognizes the intended
root, and checks that no nested instruction file was created. Read the block
once before running it so you understand what it changes on your machine.

If you already know how to create a clean practice repository, you may skip the
setup block. Create the directory yourself, make sure it satisfies the same
constraints, and assign its absolute path to `PRACTICE_ROOT`. The later steps
use `$PRACTICE_ROOT` as a variable; replace that variable with your own path
only if you prefer not to define it.

For example, after preparing the repository yourself, verify the variable and
root like this:

```bash
PRACTICE_ROOT="/absolute/path/to/your/practice-project"
test "$(git -C "$PRACTICE_ROOT" rev-parse --show-toplevel)" = "$PRACTICE_ROOT"
find "$PRACTICE_ROOT" \( -name 'AGENTS.md' -o -name 'AGENTS.override.md' \) -print
```

The `test` command must succeed and the `find` command should print nothing.
Your repository should contain a README suitable for the small edit in Step 4.

```bash
PRACTICE_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/codex-starting-practice.XXXXXX")"
git init -q "$PRACTICE_ROOT"
printf '%s\n' \
  '# Codex starting practice' \
  '' \
  'This disposable repository is used to practice a small, reviewable edit.' \
  > "$PRACTICE_ROOT/README.md"
printf 'Practice project: %s\n' "$PRACTICE_ROOT"
test "$(git -C "$PRACTICE_ROOT" rev-parse --show-toplevel)" = "$PRACTICE_ROOT"
find "$PRACTICE_ROOT" \( -name 'AGENTS.md' -o -name 'AGENTS.override.md' \) -print
```

The final command should print nothing. The project intentionally contains one
README and no application code or dependency setup.

### Step 2: Enter the practice project and record the baseline

Enter the project before starting Codex. Codex uses the current project
directory as context.

```bash
cd "$PRACTICE_ROOT"
pwd
git status --short
```

Expected result: `pwd` prints `$PRACTICE_ROOT` and `git status` prints nothing.
If either result differs, stop and correct the directory first.

### Step 3: Start Codex and confirm context

```bash
codex
```

Inside the Codex prompt, run `/pwd` and confirm that it reports `$PRACTICE_ROOT`.
Then use this read-only demonstration prompt:

```text
Read README.md and explain what this practice project is for. Do not edit files
or run commands. Name the file you inspected and tell me what is not present in
the repository.
```

Expected result: Codex identifies `README.md`, explains its purpose, and leaves
the working tree unchanged.

### Step 4: Request a bounded edit

```text
Edit only README.md in this practice repository. Add this section after the
existing paragraph, preserving all existing text:

## How to verify the setup

- Run `git status --short` to confirm the working tree state.
- Run `git log -1 --oneline` to display the repository's latest commit.

Do not create or edit any other file. Do not add dependencies or change Git
history. After editing, run `git diff --check` and summarize the file changed,
the verification result, and any assumption you made.
```

The requested result is deliberately small: one README section with two
commands that are valid in this repository. Codex should not invent a test
framework or modify configuration to complete it.

### Step 5: Review the result

If you are using the CLI, run `/diff`; in another surface, open its changes view. If the practice project uses Git, inspect the working tree from a second terminal:

```bash
git status --short
git diff -- README.md
```

Without Git, open the README and confirm that only the intended section changed.

### Step 6: Verify

Run the checks yourself, not only from Codex's summary:

```bash
git diff --check
rg -n '^## How to verify the setup$|git status --short|git log -1 --oneline' README.md
git status --short
```

Expected result:

- `git diff --check` exits successfully.
- `rg` finds the new heading and both command examples.
- `git status --short` reports only `README.md`.

### Success criteria

- Only `README.md` changed.
- The new text matches the copy-ready request and uses repository evidence.
- The independent checks pass.
- You can explain the difference between the sandbox and approval policy used.

### What you learned

You completed the basic Codex loop: establish the correct project context, ask
a read-only question, give a bounded edit request, review the diff, and run an
independent verification command.

### Step 7: Clean up

Exit Codex, then remove only the disposable repository when you no longer need
the example:

```bash
rm -rf "$PRACTICE_ROOT"
unset PRACTICE_ROOT TUTORIAL_ROOT
```

Do not substitute the Codex How To repository path for `$PRACTICE_ROOT`.

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
