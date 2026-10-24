# Safety and worktrees

Safe Codex operation combines least-privilege runtime permissions, explicit
authority for consequential actions, reviewable Git changes, and isolated
workspaces where parallel work would otherwise collide.

## Learning objectives

- Distinguish sandbox boundaries, approvals, rules, instructions, and Git.
- Choose a permission posture appropriate to the task.
- Inspect effective settings before granting an exception.
- Test command rules without running the target command.
- Use worktrees to isolate changes and review them before integration.
- Recover or clean up work without targeting the wrong checkout.

## The control layers

```mermaid
flowchart TD
    U[User authority and task scope] --> A[Approval policy]
    A --> S[Sandbox and network boundary]
    S --> R[Command rules outside sandbox]
    R --> T[Agent tools and commands]
    T --> G[Git diff, tests, and review]
```

These layers solve different problems:

| Control                | Governs                                           | Does not guarantee               |
| ---------------------- | ------------------------------------------------- | -------------------------------- |
| User request           | Intended outcome and authorized scope             | Technical isolation              |
| Sandbox                | Filesystem and command/network boundary           | Correct intent or code           |
| Approval policy        | When a boundary crossing pauses                   | That approved work is safe       |
| Rules                  | Prefix decisions for commands outside the sandbox | Full shell or application policy |
| `AGENTS.md` and skills | Agent behavior and workflow                       | Enforcement against hostile code |
| Git and worktrees      | Review, recovery, and checkout isolation          | Runtime least privilege          |

Use multiple layers. A worktree does not make `danger-full-access` safe, and an
instruction such as “do not delete files” is not a filesystem boundary.

## Sandbox modes

| Mode                 | Practical meaning                             | Typical use                      |
| -------------------- | --------------------------------------------- | -------------------------------- |
| `read-only`          | Inspect without workspace edits               | Review, inventory, analysis      |
| `workspace-write`    | Read and write inside workspace roots         | Normal implementation            |
| `danger-full-access` | No sandbox filesystem or network restrictions | Exceptional isolated environment |

In `workspace-write`, network access is off by default unless enabled by the
effective configuration. Protected paths such as `.git` can remain read-only
even inside a writable root.

Prefer adding one required directory with `--add-dir` or a writable-root setting
over removing the sandbox. Never broaden access merely to avoid understanding a
failed command.

## Approval policy and reviewer

The common approval policies are:

- `on-request`: work inside the sandbox and request a boundary exception when
  needed.
- `never`: do not stop for an approval prompt; denied operations fail instead.

With interactive approvals, `approvals_reviewer = "user"` sends requests to the
user. `auto_review` routes eligible requests to an automatic reviewer, but it
does not change the sandbox boundary.

Full access combines `danger-full-access` with `never`. Treat it as an explicit
high-risk choice, not as a troubleshooting shortcut.

## Least-privilege configuration

[`examples/least-privilege-config.toml`](examples/least-privilege-config.toml)
shows stable sandbox settings for a trusted local project:

```toml
approval_policy = "on-request"
approvals_reviewer = "user"
sandbox_mode = "workspace-write"

[sandbox_workspace_write]
network_access = false
writable_roots = []
```

Keep personal defaults in `~/.codex/config.toml`. Put repository-specific
overrides in `.codex/config.toml`; Codex loads that layer only after the project
is trusted. Use `/status` to inspect the active mode and roots, and
`/debug-config` to identify the layer that supplied a setting.

Beta permission profiles provide finer filesystem and network policy, but they
do not compose with legacy `sandbox_mode` settings. Do not mix both models in a
single tutorial configuration.

## Command rules

Rules control which command prefixes Codex can run outside the sandbox. They are
experimental and use Starlark files under `rules/` beside an active config
layer, such as `.codex/rules/default.rules` in a trusted project.

```starlark
prefix_rule(
    pattern = ["gh", "pr", ["view", "list"]],
    decision = "prompt",
    justification = "Remote pull-request access requires review.",
    match = ["gh pr view 42", "gh pr list"],
    not_match = ["gh issue list"],
)
```

The decisions are `allow`, `prompt`, and `forbidden`. When several rules match,
the most restrictive decision wins. Make prefixes categorical and narrow; an
overly broad allow rule can authorize unexpected arguments.

Test [`examples/default.rules`](examples/default.rules) without running the
target command:

```bash
codex execpolicy check --pretty \
  --rules 08-safety-and-worktrees/examples/default.rules \
  -- gh pr view 42
```

Shell wrappers and complex syntax can change how a command is evaluated. Do not
use prefix rules as a complete shell-security language.

## Authority for external state

A technically permitted action can still be outside the user's request. Ask for
explicit authority before publishing, deploying, merging, sending messages,
changing account configuration, or deleting material data.

Before approval, check:

1. The exact target and intended effect.
2. Whether the action is recoverable.
3. Which identity and external account will be used.
4. Whether a narrower operation achieves the same goal.
5. What evidence will confirm success.

Approval for one action is not permission for a broader sequence.

## Git as a recovery layer

Before risky implementation work:

- inspect `git status --short` and the current branch;
- preserve unrelated changes;
- make small, reviewable edits;
- run relevant tests;
- inspect `git diff --check` and the final diff;
- commit or push only when explicitly requested.

Git cannot recover ignored files, untracked secrets, external service changes,
or destructive commands outside the repository. Backups and service-native
recovery still matter.

## Worktree model

A Git worktree is a second checkout that shares repository metadata and objects
with the original checkout. It isolates working files and index state so
independent chats can work without overwriting each other's local changes.

Use a worktree when:

- another task must proceed while the local checkout remains in use;
- a scheduled task may edit files in the background;
- you want a disposable change set for review;
- parallel agents own separate branches or components.

Do not use worktrees to hide overlapping ownership. Two tasks changing the same
interface still need coordination.

## Codex-managed worktrees

In the ChatGPT desktop app, select **Worktree** when starting a task. Codex
creates a managed checkout, usually in detached `HEAD`, under the configured
worktree root. Use **Create branch here** when the result should become a
long-lived branch.

Handoff moves a chat and its Git state between Local and its worktree. Ignored
files do not move automatically, so dependencies and local configuration may
need a setup script or an intentional `.worktreeinclude` policy.

Managed worktrees are lightweight and may be cleaned up. Pinned, active, and
permanent worktrees are retained; Codex saves a snapshot before deleting an
eligible managed worktree.

## Manual Git worktree workflow

Resolve all paths before creating or removing anything:

```bash
git status --short
git worktree list
git worktree add -b codex/docs-update ../codex-docs-update HEAD
```

Run Codex from the new checkout with normal least-privilege permissions:

```bash
codex -C ../codex-docs-update \
  --sandbox workspace-write \
  --ask-for-approval on-request
```

Review before integration:

```bash
git -C ../codex-docs-update status --short
git -C ../codex-docs-update diff --check
git -C ../codex-docs-update diff
```

When cleanup is requested, first confirm there is no work to preserve:

```bash
git -C ../codex-docs-update status --short
git worktree list
```

Then remove the exact verified worktree through Git:

```bash
git worktree remove ../codex-docs-update
git branch -d codex/docs-update
```

Do not add `--force` because cleanup is inconvenient. Preserve or explicitly
discard outstanding work first.

## Hands-on exercise: isolated documentation change

1. Use a disposable Git repository with at least one committed file.
2. Confirm the main checkout is clean.
3. Create a sibling worktree and a new branch as shown above.
4. Ask Codex to make one documentation-only change in that worktree.
5. Run the repository's documentation checks and inspect the diff from both
   checkouts.
6. Choose deliberately: commit and integrate the change, or remove the
   worktree after verifying no work must be retained.

### Success criteria

- The original checkout remains unchanged during work.
- Codex runs with `workspace-write`, not full access.
- The final diff contains only the intended documentation change.
- Cleanup names an exact path and happens only after status inspection.
- You can explain which risks the worktree did and did not reduce.

## Troubleshooting

### Codex cannot write a required path

Inspect `/status` and `/debug-config`. Add only the required root or move the
task into the correct project instead of choosing full access.

### A rule matches too broadly

Narrow its argument prefix, add `not_match` examples, and rerun
`codex execpolicy check` with positive and negative cases.

### Dependencies are missing in a worktree

Ignored build output and dependencies are not guaranteed to follow the
checkout. Configure a reviewed local-environment setup script or install them
inside that worktree.

### Git refuses to remove a worktree

Inspect its status and resolve tracked or untracked work. Avoid forced removal
until the user has explicitly chosen to discard the exact remaining changes.

## Next step

Continue to [Advanced workflows](../09-advanced-workflows/README.md) to coordinate
planning, long-running tasks, execution environments, and schedules.

## Official resources

- [Sandbox](https://learn.chatgpt.com/docs/sandboxing)
- [Rules](https://learn.chatgpt.com/docs/agent-configuration/rules)
- [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)
- [Permissions](https://learn.chatgpt.com/docs/permissions)
