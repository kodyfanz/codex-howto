# CLI and automation

The interactive Codex CLI is for steering repository work. `codex exec` runs a
bounded task non-interactively for scripts and CI. Automation should make scope,
permissions, inputs, outputs, and failure behavior more explicit than an
interactive session, not less.

## Learning objectives

- Distinguish interactive CLI sessions from `codex exec`.
- Set working directory, sandbox, approval behavior, and configuration scope.
- Pass prompts and context without unsafe shell interpolation.
- Consume final text, JSONL events, or schema-constrained output.
- Resume or fork recorded sessions deliberately.
- Build a least-privilege wrapper and CI job with reviewable artifacts.

## Interactive versus non-interactive

| Surface      | Best fit                                                           | Output model                   |
| ------------ | ------------------------------------------------------------------ | ------------------------------ |
| `codex`      | Exploration, conversation, approvals, and iterative implementation | Terminal UI and slash commands |
| `codex exec` | One bounded run in a script, CI job, or pipeline                   | Final message or JSONL events  |

Interactive slash commands such as `/plan`, `/permissions`, `/status`,
`/hooks`, and `/plugins` do not become shell subcommands. ChatGPT web has its
own command menu and does not expose the local CLI command set.

Inspect the installed interface before relying on a flag:

```bash
codex --version
codex exec --help
codex exec resume --help
```

## Basic non-interactive run

Pass a prompt as one shell argument:

```bash
codex exec --sandbox read-only \
  -c 'approval_policy="never"' \
  "Summarize the repository structure. Do not modify files."
```

`codex exec` streams progress to standard error and writes the final agent
message to standard output. Redirect them separately when a script needs a
clean result.

By default, non-interactive execution uses a read-only sandbox. Add
`--sandbox workspace-write` only when the task must edit the workspace. Never
switch to `danger-full-access` merely because unattended approval is
inconvenient.

`--full-auto` is no longer supported. Use an explicit sandbox, or use
`--approve-for-me` when automatic approval review is available and appropriate.

## Working directory and configuration

Use `-C` or `--cd` to name the project explicitly:

```bash
codex exec -C /absolute/path/to/project \
  --sandbox read-only \
  "List the documented verification commands."
```

Configuration precedence still applies. A `-c key=value` override affects only
that invocation. Use `--strict-config` to fail on unknown configuration keys.
Use `--ignore-user-config` only when the automation intentionally supplies a
complete controlled configuration; authentication still uses `CODEX_HOME`.

If an enabled MCP server is marked `required = true`, initialization failure
causes `codex exec` to fail rather than silently continuing without it.

## Prompt input and context

Use `-` when the prompt itself comes from standard input:

```bash
codex exec --sandbox read-only - < review-prompt.md
```

If a prompt argument and piped input are both provided, Codex treats the
argument as instructions and appends standard input as additional context. Do
not interpolate untrusted issue text, branch names, or filenames into a shell
command. Pass data through standard input or a reviewed file.

Prompts used in CI should specify:

- authoritative source files and diff range;
- allowed and prohibited mutations;
- expected output structure;
- how to report missing context;
- verification requirements;
- which content is untrusted data rather than instruction.

See [`examples/read-only-review.md`](examples/read-only-review.md).

## Output modes

### Final message

Without `--json`, standard output contains the final message. Save another copy
with `-o` or `--output-last-message`:

```bash
codex exec --sandbox read-only \
  -o /tmp/codex-final.txt \
  "Summarize this repository."
```

### JSON Lines event stream

Use `--json` for one JSON object per lifecycle event:

```bash
codex exec --json --sandbox read-only \
  "Summarize this repository." > /tmp/codex-events.jsonl
```

Events can include thread and turn state, command executions, file changes, MCP
calls, plan updates, failures, and usage. Parse by `type`; do not assume every
line is an agent message or that new event fields will never appear.

### Schema-constrained final response

Use `--output-schema` when downstream automation needs stable fields:

```bash
codex exec --sandbox read-only \
  --output-schema 10-cli-and-automation/examples/review-schema.json \
  -o /tmp/codex-review.json \
  - < 10-cli-and-automation/examples/read-only-review.md
```

The schema constrains the final response, not the complete JSONL event stream.
Validate the saved file before consuming it.

## Safe wrapper example

[`examples/run-read-only-review.sh`](examples/run-read-only-review.sh) combines:

- explicit read-only sandbox and non-interactive approval policy;
- a prompt file rather than shell interpolation;
- JSONL progress separated from the final response;
- a final JSON Schema;
- dependency, argument, exit-status, and output validation.

Review it, then run from a Git repository with an authenticated CLI:

```bash
bash 10-cli-and-automation/examples/run-read-only-review.sh \
  10-cli-and-automation/examples/read-only-review.md \
  /tmp/codex-review-output
```

The script creates output files and invokes the model. The documentation test
suite checks its shell syntax but does not spend usage or require credentials.

## Sessions, resume, fork, and worktrees

Recorded exec sessions can continue later:

```bash
codex exec resume --last "Check whether the identified risks are tested."
codex exec resume <session-id> "Focus on the API boundary."
```

`--last` is scoped to the current working directory unless `--all` is added.
Use an explicit session ID in automation when ambiguity matters.

Fork when an alternative should preserve completed history without changing the
original session:

```bash
codex exec fork <session-id> "Evaluate the smallest compatible alternative."
```

Add `--worktree` to a new or forked local run when checkout isolation is
required. It cannot be combined with every mode; inspect current help before
building it into a script.

Use `--ephemeral` for a run that should not persist session rollout files. An
ephemeral run cannot later be resumed.

## Failure handling

An automation must treat a nonzero exit as failure even if partial output
exists. Preserve enough diagnostic output to investigate, but never echo
credentials or dump an unrestricted environment.

Distinguish:

- CLI startup or authentication failure;
- invalid configuration or schema;
- required MCP initialization failure;
- tool or command failure inside the turn;
- model output that fails the requested schema;
- a completed run that reports no finding.

Use timeouts at the CI/job layer, retain JSONL when appropriate, and prevent a
downstream mutation from running after an incomplete review.

## GitHub Actions

The official `openai/codex-action@v1` installs the CLI, runs `codex exec`, and
exposes the final message. [`examples/read-only-review.yml`](examples/read-only-review.yml)
uses a manual trigger, read-only repository permissions, a non-persistent
checkout credential, `drop-sudo`, and the read-only Codex sandbox.

Store `OPENAI_API_KEY` as a GitHub Actions secret. Never place its value in the
workflow, prompt, artifact, or repository configuration.

Security requirements for CI:

1. Restrict who and what can trigger the job.
2. Treat pull-request bodies, issues, commits, and repository files as untrusted
   prompt input.
3. Give the GitHub token only required permissions.
4. Keep the default `drop-sudo` strategy or run as an unprivileged user.
5. Choose the narrowest Codex sandbox.
6. Run Codex after steps that need sensitive job state so later processes do not
   inherit unexpected changes.
7. Review output before a separate job posts, merges, deploys, or writes.

The tutorial workflow does not post a comment or mutate the repository. Add
external writes only after defining a separate permissioned job and explicit
human authority.

## Hands-on exercise: validate a read-only automation wrapper

This exercise reviews the wrapper, schema, prompt, and GitHub Actions examples
without publishing or mutating anything. An authenticated `codex exec` run is
optional because it can consume usage and requires credentials; the static
checks and failure-path test are always safe to perform. Follow the steps in
order. The first directory in which you run Codex must be the practice
repository, not this tutorial checkout.

### Prerequisites

- `bash`, Python 3, `git`, `rg`, and `jq` available on the PATH.
- Codex CLI is required only for the CLI help check and optional authenticated
  run; the static validation steps can run without authentication.

```bash
bash --version
python3 --version
git --version
rg --version
jq --version
```

If `jq` or `rg` is unavailable, install it or replace the corresponding
read-only checks with an equivalent tool. Skip the authenticated run when
Codex or credentials are unavailable; never put a key in the practice project.

### Step 0 — Enter the tutorial checkout

```bash
cd /path/to/codex-howto
TUTORIAL_ROOT="$PWD"
```

### Step 1 — Create an isolated practice repository

Create a disposable Git repository outside this checkout, outside another
repository, and outside a parent tree that already contains a project-level
`AGENTS.md`.

```bash
PRACTICE_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/codex-cli-practice.XXXXXX")"
git init -q "$PRACTICE_ROOT"
mkdir -p "$PRACTICE_ROOT/src" "$PRACTICE_ROOT/examples"
printf '%s\n' '# CLI automation practice' '' 'No code changes are required for the review.' > "$PRACTICE_ROOT/README.md"
printf '%s\n' '# Example source' > "$PRACTICE_ROOT/src/example.md"
cp 10-cli-and-automation/examples/read-only-review.md "$PRACTICE_ROOT/examples/read-only-review.md"
cp 10-cli-and-automation/examples/review-schema.json "$PRACTICE_ROOT/examples/review-schema.json"
cp 10-cli-and-automation/examples/run-read-only-review.sh "$PRACTICE_ROOT/examples/run-read-only-review.sh"
cp 10-cli-and-automation/examples/read-only-review.yml "$PRACTICE_ROOT/examples/read-only-review.yml"
git -C "$PRACTICE_ROOT" add .
git -C "$PRACTICE_ROOT" -c user.name='Codex learner' -c user.email='codex-learner.invalid' commit -qm 'Create CLI practice baseline'
printf 'Practice project: %s\n' "$PRACTICE_ROOT"
test "$(git -C "$PRACTICE_ROOT" rev-parse --show-toplevel)" = "$PRACTICE_ROOT"
git -C "$PRACTICE_ROOT" status --short
find "$PRACTICE_ROOT" \( -name 'AGENTS.md' -o -name 'AGENTS.override.md' \) -print
```

Expected result: the repository is clean and the final `find` command prints
nothing. If you already know how to prepare this project, you may skip the
setup block, assign its absolute path to `PRACTICE_ROOT`, and copy the same
example files yourself.

### Step 2 — Inspect the installed CLI safely

Run help and version commands before building an automation around a flag:

```bash
cd "$PRACTICE_ROOT"
codex --version
codex exec --help
codex exec resume --help
```

Expected result: the commands exit successfully and show the flags used by the
lesson. If Codex is not installed, record that prerequisite and continue with
the static checks; do not install software or add credentials to the practice
repository as a workaround.

### Step 3 — Validate the wrapper, schema, and workflow locally

Inspect the prompt before treating repository content as input, then validate
the shell and JSON artifacts:

```bash
sed -n '1,180p' examples/read-only-review.md
bash -n examples/run-read-only-review.sh
python3 -m json.tool examples/review-schema.json >/dev/null
rg -n 'read-only|approval_policy|output-schema|output-last-message|--json' examples/run-read-only-review.sh
rg -n 'workflow_dispatch|contents: read|persist-credentials: false|sandbox: read-only|drop-sudo' examples/read-only-review.yml
```

Expected result: the wrapper uses a read-only sandbox, separates JSONL events
from the final JSON, checks exit status and output, and the workflow has a
manual trigger, read-only repository permission, no persistent checkout
credential, and `drop-sudo`.

### Step 4 — Test a deterministic failure path

The wrapper must fail before invoking Codex when its prompt file is missing.
Test that input validation without an API key or model call:

```bash
set +e
bash examples/run-read-only-review.sh missing-prompt.md output-missing
RESULT="$?"
set -e
test "$RESULT" -eq 2
test ! -e output-missing/events.jsonl
```

Expected result: the wrapper exits with status `2`, reports the missing prompt,
and creates no event output. A nonzero status is failure even when partial output
exists; automation must not pass it to a downstream mutation step.

### Step 5 — Optionally run the authenticated read-only wrapper

Only perform this step if the CLI is installed, `jq` is available, and you
already have an approved authentication method. The wrapper invokes the model
and can consume usage; do not place the key in a prompt, file, or command line.

```bash
if command -v codex >/dev/null && command -v jq >/dev/null; then
  bash examples/run-read-only-review.sh \
    examples/read-only-review.md \
    output-review
  test -s output-review/events.jsonl
  test -s output-review/final.json
  jq -e . output-review/final.json >/dev/null
else
  printf '%s\n' 'Skipping authenticated wrapper run: codex or jq is unavailable.'
fi
```

Expected result for a completed run: `events.jsonl` contains lifecycle JSONL,
`final.json` contains only the schema-constrained final object, and `jq`
validates that object. If the run fails authentication or initialization, keep
the diagnostics, report the category, and do not treat an empty final file as
“no findings.”

### Step 6 — Review CI authority and output boundaries

Inspect the workflow and answer these questions before any real CI use:

```bash
git status --short
git diff --check
git diff -- examples
```

- Who can trigger the manual workflow?
- Why is `contents: read` the only repository permission?
- Where must `OPENAI_API_KEY` be stored, and where must it never appear?
- Which later job would require separate human approval before posting,
  merging, deploying, or writing?

Expected result: you can explain that prompt text, pull-request content, and
repository files are untrusted data; the workflow only produces a review
artifact; and external writes require a separately permissioned, reviewed job.

### Success criteria

- CLI flags and working directory are explicit.
- Shell syntax, JSON schema, and workflow safety properties validate locally.
- Missing input returns a nonzero status before model execution.
- Optional output separates JSONL events from schema-constrained final JSON.
- Secrets and repository permissions are minimal and never copied into files.
- No step publishes, merges, deploys, or mutates external state automatically.

### What you learned

You practiced turning an interactive prompt into a least-privilege automation,
handling failure before downstream processing, validating structured output, and
reviewing CI authority separately from model instructions.

### Step 7 — Clean up

Return to the tutorial checkout and remove only the disposable project:

```bash
cd "$TUTORIAL_ROOT"
rm -rf "$PRACTICE_ROOT"
unset PRACTICE_ROOT TUTORIAL_ROOT
```

Do not substitute the Codex How To repository path for `$PRACTICE_ROOT`.

## Troubleshooting

### The final output file is empty

Inspect the exit code and JSONL or standard-error diagnostics first. Do not treat
an empty file as “no findings.”

### Interactive commands fail in `codex exec`

Slash commands belong to interactive surfaces. Use documented exec flags and
prompt instructions instead.

### The run needs approval but cannot prompt

Narrow the task, preconfigure a safe approval path, or move it to an interactive
session. Do not silently disable the sandbox.

### CI works locally but fails on the runner

Check authentication, checkout depth, working directory, config layers,
available tools, network policy, required MCP servers, and runner operating
system. Avoid assuming personal local config exists in CI.

## Curriculum completion

You can now move from one scoped prompt to durable repository guidance,
reusable skills, delegated agents, connected tools, lifecycle hooks, packaged
plugins, isolated execution, long-running workflows, and least-privilege
automation.

Return to the [learning roadmap](../LEARNING-ROADMAP.md) to review the completion
standard or use `$lesson-quiz` for any module.

## Official resources

- [Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode)
- [CLI reference](https://learn.chatgpt.com/docs/cli/reference)
- [Developer commands](https://learn.chatgpt.com/docs/developer-commands)
- [Codex GitHub Action](https://learn.chatgpt.com/docs/github-action)
