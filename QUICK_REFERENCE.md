# Codex quick reference

This page is a navigation and decision aid. Exact commands and configuration
belong in their modules, where they can be verified and scoped to a product
surface.

## Put the instruction in the right place

| Requirement                   | Best location                              |
| ----------------------------- | ------------------------------------------ |
| One task only                 | Current prompt or thread                   |
| Every task in one repository  | Root `AGENTS.md`                           |
| One subtree only              | Nested `AGENTS.md` or `AGENTS.override.md` |
| Reusable workflow             | `.agents/skills/<name>/SKILL.md`           |
| Specialized delegated role    | `.codex/agents/<name>.toml`                |
| Trusted project settings      | `.codex/config.toml`                       |
| External tools or context     | MCP server or app connector                |
| Deterministic lifecycle check | Hook                                       |
| Installable workflow bundle   | Plugin                                     |
| Recurring check or reminder   | Automation                                 |

## Common project paths

| Purpose                             | Path                                |
| ----------------------------------- | ----------------------------------- |
| Project guidance                    | `AGENTS.md`                         |
| More specific guidance              | `<subdirectory>/AGENTS.md`          |
| Override guidance                   | `<subdirectory>/AGENTS.override.md` |
| Project skills                      | `.agents/skills/`                   |
| Project agents                      | `.codex/agents/`                    |
| Project configuration               | `.codex/config.toml`                |
| Portable plugin manifest            | `plugin.json` at the plugin root    |
| Codex compatibility plugin manifest | `.codex-plugin/plugin.json`         |

## Before you copy an example

1. Confirm the documented surface matches your client.
2. Read the required permissions and external dependencies.
3. Replace placeholders through environment variables or approved secret stores.
4. Try the example in a disposable or version-controlled project.
5. Review the diff and command output.
6. Run the listed verification step.

## Useful CLI slash commands

The available commands depend on your installed CLI version. Type `/` in the
composer to inspect the commands available in your session.

| Command | Use |
|---|---|
| `/status` | Check the active session and permission context. |
| `/permissions` | Inspect or change the current permission mode. |
| `/diff` | Review file changes. |
| `/mention` | Attach a file or directory as context. |
| `/plan` | Ask for a plan before a larger change. |
| `/compact` | Summarize a long conversation. |
| `/init` | Create an instruction-file scaffold. |
| `/skills` | Browse or invoke available skills. |
| `/new` | Start a fresh conversation in the CLI session. |
| `/quit` | Exit the interactive CLI. |

For a first task, begin with [Module 1](01-getting-started/README.md); you only need
the commands relevant to your chosen surface. See the [current official
developer-command reference](https://learn.chatgpt.com/docs/developer-commands)
for the latest command set and surface-specific details.

## Safety questions

- Which files can this task read and write?
- Can it access the network?
- Which actions require approval?
- Does it modify an external system?
- Can the result be reviewed or reversed?
- Does the workflow expose secrets in prompts, logs, or configuration?

## Module lookup

- First task and built-in commands: [Module 1](01-getting-started/README.md)
- Durable guidance: [Module 2](02-agents-md/README.md)
- Reusable workflow: [Module 3](03-skills/README.md)
- Parallel specialist work: [Module 4](04-subagents/README.md)
- External integration: [Module 5](05-mcp/README.md)
- Lifecycle automation: [Module 6](06-hooks/README.md)
- Distribution: [Module 7](07-plugins/README.md)
- Permissions and isolation: [Module 8](08-safety-and-worktrees/README.md)
- Planning and scheduled work: [Module 9](09-advanced-workflows/README.md)
- Scripts and CI: [Module 10](10-cli-and-automation/README.md)
