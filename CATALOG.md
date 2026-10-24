# Codex feature catalog

Use this catalog when you know the capability you need but not the module where
it is taught. Availability can vary by client, account, workspace, and policy;
the detailed lessons will label those constraints.

## Core surfaces

| Surface         | Best fit                                               | Module                                                 |
| --------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| Codex CLI       | Terminal-first repository work and scripting           | [1](01-getting-started/README.md), [10](10-cli-and-automation/README.md) |
| IDE extension   | Editor-attached implementation and review              | [1](01-getting-started/README.md)                               |
| Desktop app     | Local project work, planning, review, and visual tools | [1](01-getting-started/README.md), [9](09-advanced-workflows/README.md)  |
| Cloud execution | Hosted tasks with configured environments              | [9](09-advanced-workflows/README.md)                            |
| ChatGPT Work    | Workspace collaboration, apps, and governed access     | [7](07-plugins/README.md), [9](09-advanced-workflows/README.md)          |

## Customization

| Capability             | Use it for                       | Primary location                                                         | Module                                                      |
| ---------------------- | -------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------------- |
| Prompt or task context | One-off requirements             | Current conversation                                                     | [1](01-getting-started/README.md)                                    |
| Project instructions   | Durable repository conventions   | `AGENTS.md`                                                              | [2](02-agents-md/README.md)                                          |
| Nested override        | Directory-specific conventions   | `AGENTS.override.md`                                                     | [2](02-agents-md/README.md)                                          |
| Skill                  | Repeatable workflow or expertise | `.agents/skills/`                                                        | [3](03-skills/README.md)                                             |
| Custom agent           | Specialized delegated role       | `.codex/agents/*.toml`                                                   | [4](04-subagents/README.md)                                          |
| Project configuration  | Trusted-repository settings      | `.codex/config.toml`                                                     | [5](05-mcp/README.md), [6](06-hooks/README.md), [8](08-safety-and-worktrees/README.md) |
| Plugin                 | Installable workflow bundle      | Root `plugin.json` or `.codex-plugin/plugin.json` compatibility manifest | [7](07-plugins/README.md)                                            |

## Integration and automation

| Capability   | Use it for                          | Avoid using it for            | Module                       |
| ------------ | ----------------------------------- | ----------------------------- | ---------------------------- |
| MCP          | External tools, data, and context   | Static repository conventions | [5](05-mcp/README.md)                 |
| Hook         | Deterministic lifecycle enforcement | Open-ended reasoning          | [6](06-hooks/README.md)               |
| Subagent     | Bounded specialist or parallel work | Tiny sequential tasks         | [4](04-subagents/README.md)           |
| Automation   | Scheduled checks and follow-ups     | Immediate one-off work        | [9](09-advanced-workflows/README.md)  |
| `codex exec` | Bounded non-interactive runs        | Long interactive discovery    | [10](10-cli-and-automation/README.md) |

## Safety controls

| Control              | Governs                               | Module                        |
| -------------------- | ------------------------------------- | ----------------------------- |
| Sandbox              | Filesystem and execution boundaries   | [8](08-safety-and-worktrees/README.md) |
| Approval policy      | When user authorization is required   | [8](08-safety-and-worktrees/README.md) |
| Rules                | Command decisions outside the sandbox | [8](08-safety-and-worktrees/README.md) |
| Managed requirements | Organization-enforced constraints     | [8](08-safety-and-worktrees/README.md) |
| Git worktree         | Isolated checkout and change set      | [8](08-safety-and-worktrees/README.md) |

## Selection guide

| Need                                                     | Start with                  |
| -------------------------------------------------------- | --------------------------- |
| “Follow this convention in every task in this repo.”     | `AGENTS.md`                 |
| “Repeat this multi-step process when relevant.”          | Skill                       |
| “Ask a specialist to investigate this independently.”    | Subagent                    |
| “Read or act on an external system.”                     | MCP server or app connector |
| “Run this deterministic check around a lifecycle event.” | Hook                        |
| “Distribute this complete workflow to others.”           | Plugin                      |
| “Run this check every weekday.”                          | Automation                  |

## Official documentation

- [Codex customization](https://learn.chatgpt.com/docs/customization/overview.md)
- [Codex configuration](https://learn.chatgpt.com/docs/config-file/config-basic.md)
- [Codex CLI](https://learn.chatgpt.com/docs/codex/cli.md)
