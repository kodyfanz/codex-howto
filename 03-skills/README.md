# Skills

Skills package repeatable workflows as focused instructions with optional
references, scripts, assets, and UI metadata. Codex can select a skill from its
description or the user can invoke it explicitly with `$skill-name`.

## Learning objectives

- Decide whether guidance belongs in a prompt, `AGENTS.md`, a skill, or a plugin.
- Explain progressive disclosure.
- Create a valid `SKILL.md` with precise trigger language.
- Add supporting resources only when they improve the workflow.
- Test explicit and implicit invocation.
- Validate a skill before sharing it.

## Choose the right mechanism

| Need                                                         | Use            |
| ------------------------------------------------------------ | -------------- |
| One task's requirements                                      | Current prompt |
| Rules that apply to every repository task                    | `AGENTS.md`    |
| A repeatable, discoverable workflow                          | Skill          |
| An installable bundle with connectors or multiple components | Plugin         |

A skill does not grant permission to perform external or destructive actions.
It describes the workflow; normal sandbox, approval, and tool permissions still
apply.

## Use a skill in Codex CLI

You do not run a skill as a shell command. Mention it in the Codex prompt, then
tell Codex what you want it to do:

1. At the prompt, type `$` and choose a skill from the suggestions. You can
   also type its full name, such as `$lesson-quiz`.
2. After the skill name, write your request in the same prompt. For example:

   ```text
   $lesson-quiz Quiz me on Module 1 as a pre-test.
   ```

3. Send the prompt. Codex applies that skill's instructions to your request.

You can also type `/skills` and select a skill from the list. If the skill is
not listed, check that it is available to this project or your Codex setup.
After adding a skill, restart Codex if it still does not appear.

The `$` mention is an explicit request to use that skill. Codex may also select
a skill automatically when your request matches its description, but naming it
is the clearest way to start when you are learning.

## Progressive disclosure

```mermaid
flowchart LR
    A[Name and description] -->|Selected| B[SKILL.md]
    B -->|Needed for this task| C[References or scripts]
```

Codex initially sees skill metadata for discovery. It loads `SKILL.md` after
selecting the skill, then reads only the supporting resources needed for the
current task.

## Skill locations

| Scope         | Location                    | Use                                   |
| ------------- | --------------------------- | ------------------------------------- |
| Repository    | `.agents/skills/<name>/`    | Shared project workflow               |
| User          | `~/.agents/skills/<name>/`  | Personal workflow across repositories |
| Administrator | `/etc/codex/skills/<name>/` | Managed machine defaults              |
| System        | Bundled with Codex          | OpenAI-provided capabilities          |

Within a repository, Codex scans `.agents/skills` from the current working
directory toward the repository root. Skills with the same `name` are not
merged.

## Minimal structure

```text
my-skill/
└── SKILL.md
```

```markdown
---
name: my-skill
description: Describe the concrete workflow and when it should apply.
---

# My skill

State the outcome, important decisions, constraints, and output requirements.
```

Names use lowercase letters, digits, and hyphens. The directory should match
the skill name.

## Write a discriminating description

The description controls discovery. Front-load the user goal and add a boundary
when a neighboring workflow could trigger incorrectly.

```yaml
description: Review a code change for concrete correctness, security, and test risks. Use for pull requests, diffs, or requested code review. Do not use for implementing the fix unless the user asks.
```

Avoid descriptions such as “helps with code.” They are too broad to route
reliably.

## Add resources intentionally

```text
my-skill/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
├── scripts/
└── assets/
```

- `references/`: policies, schemas, detailed checklists, or mode-specific
  instructions read only when relevant.
- `scripts/`: deterministic operations that would otherwise be reimplemented
  repeatedly. Run and test new scripts.
- `assets/`: files copied or adapted into output.
- `agents/openai.yaml`: optional UI metadata, invocation policy, and MCP
  dependencies.

Do not add empty directories, duplicated README files, or scripts for work the
agent can perform reliably with existing tools.

## Optional UI metadata

```yaml
interface:
  display_name: "Code Review Specialist"
  short_description: "Review code for concrete correctness risks"
  default_prompt: "Use $code-review-specialist to review this change."
```

Implicit invocation is enabled by default. Set
`policy.allow_implicit_invocation: false` only for an intentionally explicit-only
skill. An MCP dependency makes a tool available; the instructions must still
explain when and how to use it.

## Create a skill

Invoke the built-in creator and describe the outcome and trigger:

```text
$skill-creator Create a project skill named release-notes that drafts release
notes from the current Git diff. It must separate user-visible changes from
internal changes and must not publish anything.
```

For manual creation, place the directory under `.agents/skills/` and create
`SKILL.md`. Codex normally detects changes automatically; restart the client if
the skill does not appear.

## Invoke and test

In the CLI or IDE extension, type `$` to mention a skill or use `/skills` to
browse available skills.

Test five request shapes:

1. A direct request that should invoke it.
2. An indirect request expressing the same goal.
3. Missing input that should cause one focused question.
4. A neighboring request that should not invoke it.
5. An edge case where the skill must stop rather than invent information.

Metadata controls whether the skill is chosen. The body controls what it does
after selection; diagnose those failures separately.

## Validate

If you have the `skill-creator` package installed, run its validator:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py \
  .agents/skills/my-skill
```

The validator checks structure, frontmatter, naming, and unfinished scaffold
placeholders. It does not prove that trigger decisions or outputs are useful.

## Copy-ready examples

- [Code review specialist](examples/code-review-specialist/SKILL.md) uses a
  focused entrypoint plus a conditional review checklist.
- [Documentation maintainer](examples/docs-maintainer/SKILL.md) shows a compact,
  instruction-only skill.
- [`$self-assessment`](../.agents/skills/self-assessment/SKILL.md) and
  [`$lesson-quiz`](../.agents/skills/lesson-quiz/SKILL.md) are active project
  skills used by this curriculum.

To try an example in another repository:

```bash
mkdir -p /path/to/project/.agents/skills
cp -R 03-skills/examples/code-review-specialist \
  /path/to/project/.agents/skills/
```

Review copied instructions before using them; tutorial examples are not a
substitute for repository-specific policy.

## Hands-on exercise: build and test a small skill

This exercise creates a disposable project skill that summarizes an existing
Git diff. Follow the steps in order. The first directory in which you run
Codex must be the practice repository, not this tutorial checkout.

### Prerequisites

- Codex CLI installed and authenticated.
- `git`, `rg`, and a POSIX shell available on the PATH.

```bash
codex --version
git --version
rg --version
```

If `rg` is unavailable, follow [Install ripgrep for lesson searches](../01-getting-started/README.md#install-ripgrep-for-lesson-searches), or replace the lesson's read-only searches with an equivalent tool such as `grep -n` before continuing.

### Step 0 — Enter the tutorial checkout

```bash
cd /path/to/codex-howto
TUTORIAL_ROOT="$PWD"
```

### Step 1 — Create an isolated practice repository

Create the practice project outside this checkout, outside another repository,
and outside a parent tree that already contains a project-level `AGENTS.md`.
This prevents unrelated instructions from affecting skill discovery.

```bash
PRACTICE_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/codex-skills-practice.XXXXXX")"
git init -q "$PRACTICE_ROOT"
mkdir -p "$PRACTICE_ROOT/.agents/skills/change-summary"
printf '%s\n' '# Skill practice project' > "$PRACTICE_ROOT/README.md"
printf 'Practice project: %s\n' "$PRACTICE_ROOT"
test "$(git -C "$PRACTICE_ROOT" rev-parse --show-toplevel)" = "$PRACTICE_ROOT"
find "$PRACTICE_ROOT" \( -name 'AGENTS.md' -o -name 'AGENTS.override.md' \) -print
```

The final command should print nothing. The directory under `.agents/skills`
is the project-local discovery path that this exercise tests.

If you already know how to create a clean practice repository, you may skip
this setup block. Assign its absolute path to `PRACTICE_ROOT`, create the same
`.agents/skills/change-summary/` directory, and verify the Git root before
continuing.

### Step 2 — Write the copy-ready skill

Create the file at the exact project-local path:

```bash
cat > "$PRACTICE_ROOT/.agents/skills/change-summary/SKILL.md" <<'EOF'
---
name: change-summary
description: Summarize an existing Git diff for a reviewer with user impact, risks, and verification evidence. Use for review summaries or branch summaries. Do not use for implementing code, editing files, or committing changes.
---

# Change summary

Review the current Git diff without editing files or committing changes.

Return:

1. A concise user-impact summary.
2. A risk list grounded in the diff; say "None found" when appropriate.
3. A verification list containing checks that actually ran and checks that remain.

Do not invent changed files, tests, or behavior. Ask one focused question when
the repository or diff is unavailable.
EOF
```

The heredoc is a convenient way to create the exact file. If your shell or
policy does not allow it, create the same file in an editor without changing
its path or content.

### Step 3 — Enter the practice project and start Codex

The skill is project-local, so the starting directory matters.

From a terminal currently at `$PRACTICE_ROOT`, start the interactive Codex
session:

```bash
cd "$PRACTICE_ROOT"
pwd
git status --short
codex
```

Confirm that `/pwd` reports `$PRACTICE_ROOT`, then use `/skills` to check that
`change-summary` is discoverable. If it is not listed, inspect the path and
restart the Codex session before testing invocation.

### Step 4 — Test explicit invocation

After `/skills` confirms the skill is available, remain in the active Codex
prompt and enter this request:

```text
$change-summary Summarize the current branch for a reviewer. Do not edit files
or commit anything. Separate user impact, risks, and verification evidence.
```

Expected result: the skill is selected explicitly and returns the three
requested sections. Since the practice repository has no meaningful diff yet,
it should state that evidence is limited rather than inventing changes.

### Step 5 — Test matching indirect invocation

Still in the active Codex prompt, ask the same goal without naming the skill:

```text
Summarize this branch for a reviewer. Do not modify files or commit changes.
Report user impact, risks, and which verification checks actually ran.
```

Expected result: Codex may select `change-summary` implicitly because the goal
matches its description. The output must still be grounded in repository state.

### Step 6 — Test the boundary

Still in the active Codex prompt, use a neighboring request that should not
route to this skill:

```text
Implement the missing tests for the current project and commit the changes.
```

Expected result: `change-summary` is not the right workflow. Codex should ask
for missing requirements or use another workflow; it must not pretend that a
review-summary skill can implement or commit code.

### Step 7 — Verify independently

Exit Codex and run these checks from the practice project:

```bash
test -f .agents/skills/change-summary/SKILL.md
rg -n '^name: change-summary$|^description:|Do not use for implementing|^# Change summary$' .agents/skills/change-summary/SKILL.md
git status --short
```

Expected result: the file exists, the metadata and boundary language are
present, and only the intended skill file is untracked.

### Success criteria

- The skill is at `.agents/skills/change-summary/SKILL.md` with valid metadata.
- Explicit and matching indirect requests follow its output contract.
- The neighboring implementation/commit request does not use it to edit or
  commit.
- Outputs describe only evidence available in the practice repository.

### What you learned

You can distinguish a repeatable workflow from a one-off prompt or repository
rule, write a discriminating description, use progressive disclosure, and test
positive and negative routing cases.

### Step 8 — Clean up

Exit Codex with `/exit` (or close the session), then use a terminal in the
tutorial checkout. Return there before removing the disposable project:

```bash
cd "$TUTORIAL_ROOT"
test -n "$PRACTICE_ROOT" && test "$PRACTICE_ROOT" != "$TUTORIAL_ROOT"
rm -rf "$PRACTICE_ROOT"
unset PRACTICE_ROOT TUTORIAL_ROOT
```

Do not substitute the Codex How To repository path for `$PRACTICE_ROOT`.

## Troubleshooting

### The skill does not appear

- Confirm `SKILL.md` has valid `name` and `description` fields.
- Confirm it is under a scanned `.agents/skills` path.
- Check for a duplicate name and restart Codex if necessary.

### The skill triggers too often

Narrow the description around the recognizable user goal and add one meaningful
exclusion.

### The skill is selected but behaves poorly

Improve the body, inputs, decision points, or output contract. Move large
conditional details into linked references.

## Next step

Continue to [Subagents](../04-subagents/README.md) when work should run in a focused
agent thread rather than merely follow a workflow in the current one.

## Official resources

- [Build skills](https://learn.chatgpt.com/docs/build-skills.md)
- [Plugin skill format](https://developers.openai.com/plugins/build/skills.md)
