# Codex and AI glossary

Use this page as a fast lookup while reading the curriculum. Each entry links
to the lesson that demonstrates the concept and, where useful, to an official
reference that can change independently of this guide.

## AI and language-model terms

| Term | Meaning | Continue with |
|---|---|---|
| **AI** (artificial intelligence) | Software that performs tasks commonly associated with human reasoning, perception, or language. In this guide, AI refers to the model-driven capabilities used by Codex. | [Getting started](01-getting-started/README.md) |
| **LLM** (large language model) | A model trained to predict and generate language. Codex uses language models to interpret a task, inspect context, and propose or perform changes. | [Getting started](01-getting-started/README.md) |
| **Model** | The selected AI model that reasons over a task and produces responses or tool actions. Model availability and names depend on the Codex surface and account. | [Codex environments](https://learn.chatgpt.com/docs/environments/modes) |
| **Prompt** | The instructions and context supplied to the model. A good prompt states the goal, constraints, relevant paths, and how success will be checked. | [Getting started](01-getting-started/README.md) |
| **Context** | The information available to the model for a task, such as the conversation, repository files, instructions, and tool results. | [Project instructions](02-agents-md/README.md) |
| **Context window** | The model's bounded working space for input and output. Large repositories may require focused paths, summaries, or staged tasks. | [Advanced workflows](09-advanced-workflows/README.md) |
| **Token** | A unit used to represent text for model processing and usage accounting. Token boundaries do not always match words or characters. | [OpenAI documentation overview](https://learn.chatgpt.com/docs) |
| **Agent** | A model-driven workflow that can interpret a goal, use tools, and iterate toward a verified result within granted authority. | [Getting started](01-getting-started/README.md) |

## Codex surfaces and workflow components

| Term | Meaning | Continue with |
|---|---|---|
| **Codex CLI** | The terminal interface for interactive or scripted Codex work. | [CLI and automation](10-cli-and-automation/README.md) · [CLI reference](https://learn.chatgpt.com/docs/codex/cli) |
| **IDE** (integrated development environment) | An editor surface where Codex can work alongside source code, diffs, and tests. | [Getting started](01-getting-started/README.md) |
| **Desktop app** | A local Codex surface for repository work, planning, review, and connected tools. | [Getting started](01-getting-started/README.md) |
| **Cloud** | A hosted execution surface with its own environment, setup, and filesystem boundary. Do not assume local-machine behavior applies. | [Advanced workflows](09-advanced-workflows/README.md) |
| **ChatGPT Work** | A governed workspace surface for collaboration, apps, and organization-level access controls. | [Plugins](07-plugins/README.md) |
| **Task** | A user-requested unit of work with a goal, scope, authority, and verification result. | [Getting started](01-getting-started/README.md) |
| **AGENTS.md** | A Markdown instruction file that communicates repository conventions to Codex. Nested files can add more specific guidance. | [Project instructions](02-agents-md/README.md) · [AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md) |
| **Skill** | A reusable instruction package that teaches Codex a focused workflow or area of expertise. | [Skills](03-skills/README.md) · [Build skills](https://learn.chatgpt.com/docs/build-skills) |
| **Subagent** | A delegated Codex worker assigned a bounded investigation or implementation task. | [Subagents](04-subagents/README.md) · [Subagents reference](https://learn.chatgpt.com/docs/agent-configuration/subagents) |
| **MCP** (Model Context Protocol) | A protocol for connecting Codex to external tools, data, and context through an MCP server. | [MCP](05-mcp/README.md) · [MCP reference](https://learn.chatgpt.com/docs/extend/mcp) |
| **Hook** | A deterministic command triggered at a lifecycle event, such as validating input or checking a result. | [Hooks](06-hooks/README.md) · [Hooks reference](https://learn.chatgpt.com/docs/hooks) |
| **Plugin** | A distributable bundle that packages reusable Codex capabilities and supporting files. | [Plugins](07-plugins/README.md) |

## Safety, execution, and delivery terms

| Term | Meaning | Continue with |
|---|---|---|
| **Sandbox** | A boundary that limits filesystem access and command execution. It is a safety control, not a substitute for reviewing changes. | [Safety and worktrees](08-safety-and-worktrees/README.md) |
| **Approval policy** | The rule for when Codex must ask before performing an action. Approval requirements can vary by surface and workspace policy. | [Safety and worktrees](08-safety-and-worktrees/README.md) |
| **Rule** | A command or path policy that allows, denies, or requires review for an operation. | [Safety and worktrees](08-safety-and-worktrees/README.md) |
| **Worktree** | A separate Git checkout that isolates a task's files and changes from another checkout. | [Safety and worktrees](08-safety-and-worktrees/README.md) · [Worktrees reference](https://learn.chatgpt.com/docs/environments/git-worktrees) |
| **Automation** | A scheduled or event-driven workflow that runs a repeatable task with defined notifications and authority. | [Advanced workflows](09-advanced-workflows/README.md) |
| **`codex exec`** | A non-interactive CLI mode for bounded commands, scripts, and CI jobs. | [CLI and automation](10-cli-and-automation/README.md) · [Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode) |
| **CI** (continuous integration) | An automated build and test environment that checks changes before integration. | [CLI and automation](10-cli-and-automation/README.md) |
| **Verification** | A visible check that confirms whether an exercise or task achieved its stated outcome. | [Learning roadmap](LEARNING-ROADMAP.md) |

## File and format abbreviations

| Abbreviation | Expansion | Where it appears |
|---|---|---|
| **CLI** | Command-line interface | [CLI and automation](10-cli-and-automation/README.md) |
| **IDE** | Integrated development environment | [Getting started](01-getting-started/README.md) |
| **MCP** | Model Context Protocol | [MCP](05-mcp/README.md) |
| **CI** | Continuous integration | [CLI and automation](10-cli-and-automation/README.md) |
| **TOML** | Tom's Obvious Minimal Language, used for several Codex configuration files | [Subagents](04-subagents/README.md) |
| **JSON** | JavaScript Object Notation, commonly used for structured tool and hook data | [Hooks](06-hooks/README.md) |
| **YAML** | A human-readable data-serialization format used by some automation files | [CLI and automation](10-cli-and-automation/README.md) |
| **SVG** | Scalable Vector Graphics, used for diagrams and logos in the generated guide | [Asset inventory](docs/ASSET_LICENSES.md) |
| **EPUB** | Electronic publication format used for the offline guide | [Release tooling](scripts/README.md) |

## How to use this page

Start with the linked local lesson when you need a practical example. Follow
the official reference when a term is surface-specific, account-dependent, or
likely to change. If a term is missing, add it here with a concise definition,
a local lesson link, and an official reference where one exists.
