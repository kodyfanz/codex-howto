# Completed lesson question bank

Each question includes four options, the exact correct answer, a short
explanation, and the lesson section to review. Shuffle the options before use.

## Module 1 — Getting started with Codex

### 1.1 — Surface choice

- **Category**: Conceptual
- **Question**: Which surface is the most direct fit for terminal-first repository work and later scripting?
- **Options**: Codex CLI | IDE extension | Codex cloud only | A static documentation site
- **Correct**: Codex CLI
- **Explanation**: The CLI is designed for terminal-first repository work and provides non-interactive commands used later for scripting.
- **Review**: Choose a surface

### 1.2 — Working directory

- **Category**: Practical
- **Question**: Which command starts Codex with a specific project as its working root without first changing the shell directory?
- **Options**: `codex --cd /path/to/project` | `codex --add-dir /path/to/project` | `codex login /path/to/project` | `codex exec --output /path/to/project`
- **Correct**: `codex --cd /path/to/project`
- **Explanation**: `--cd` selects the working directory before Codex processes the task. `--add-dir` grants an additional writable directory and serves a different purpose.
- **Review**: Start in the correct directory

### 1.3 — Authentication status

- **Category**: Practical
- **Question**: Which command reports the active CLI authentication method?
- **Options**: `codex login status` | `codex /status` | `codex auth print` | `codex doctor --token`
- **Correct**: `codex login status`
- **Explanation**: `codex login status` checks the stored authentication state from the shell.
- **Review**: Sign in

### 1.4 — API keys

- **Category**: Conceptual
- **Question**: Why does the guide pipe an API key through standard input instead of putting it directly in the command?
- **Options**: To reduce exposure in shell history | To convert it into a ChatGPT subscription | To enable every cloud feature | To disable billing
- **Correct**: To reduce exposure in shell history
- **Explanation**: Secrets should not be written directly into commands, documentation, repositories, or prompts where they may be retained.
- **Review**: Sign in

### 1.5 — Prompt scope

- **Category**: Practical
- **Question**: Which first task is best bounded and reviewable?
- **Options**: Add one supported README section, avoid code changes, and run the relevant docs check | Modernize everything and use your judgment | Fix all issues in the repository without questions | Rewrite the architecture and deploy it
- **Correct**: Add one supported README section, avoid code changes, and run the relevant docs check
- **Explanation**: It states an outcome, scope boundary, evidence rule, and verification step.
- **Review**: Write a useful first task

### 1.6 — Reviewing changes

- **Category**: Practical
- **Question**: Which built-in CLI command shows the Git diff, including untracked files?
- **Options**: `/diff` | `/status` | `/review-only` | `/mention`
- **Correct**: `/diff`
- **Explanation**: `/diff` is the direct session command for reviewing current file changes.
- **Review**: Review before accepting the result

### 1.7 — Session inspection

- **Category**: Conceptual
- **Question**: What should a learner inspect with `/status`?
- **Options**: Active model, permissions, writable roots, and context usage | Only the Git branch name | Installed npm packages only | External account passwords
- **Correct**: Active model, permissions, writable roots, and context usage
- **Explanation**: `/status` helps confirm important session configuration before work proceeds.
- **Review**: Start in the correct directory

### 1.8 — Skills versus slash commands

- **Category**: Conceptual
- **Question**: Where should a reusable team workflow be authored?
- **Options**: A skill | A deprecated custom-prompt file | Shell history | Cached authentication data
- **Correct**: A skill
- **Explanation**: Built-in slash commands control the client or session, while skills are the recommended format for reusable workflows.
- **Review**: Essential slash commands

### 1.9 — Safety controls

- **Category**: Conceptual
- **Question**: Which statement correctly distinguishes sandbox and approval policy?
- **Options**: Sandbox controls execution boundaries; approval policy controls when Codex must ask | They are two names for the same setting | Approval policy controls files; sandbox selects the model | Both apply only to cloud tasks
- **Correct**: Sandbox controls execution boundaries; approval policy controls when Codex must ask
- **Explanation**: The controls interact but govern different parts of authority.
- **Review**: Permissions in the first session

### 1.10 — Exercise success

- **Category**: Practical
- **Question**: What is the strongest evidence that the first exercise succeeded?
- **Options**: Only the expected README changed and the relevant check passed | Codex produced a long explanation | No approval prompt appeared | The task used the most powerful permission mode
- **Correct**: Only the expected README changed and the relevant check passed
- **Explanation**: Observable scope and verification matter more than response length or broad authority.
- **Review**: Hands-on exercise

## Module 2 — Project instructions with AGENTS.md

### 2.1 — Purpose

- **Category**: Conceptual
- **Question**: What is the best use of a repository `AGENTS.md`?
- **Options**: Durable commands, conventions, and completion expectations | Storing API keys | Copying every design document | Recording one temporary task
- **Correct**: Durable commands, conventions, and completion expectations
- **Explanation**: `AGENTS.md` provides persistent guidance that applies across repository tasks.
- **Review**: What belongs in AGENTS.md

### 2.2 — Discovery order

- **Category**: Conceptual
- **Question**: In what order are project instruction files combined?
- **Options**: From project root toward the current working directory | Alphabetically by filename | Newest modification first | Current directory toward the filesystem root
- **Correct**: From project root toward the current working directory
- **Explanation**: Broader guidance loads first and more specific directory guidance appears later.
- **Review**: How discovery works

### 2.3 — File selection

- **Category**: Conceptual
- **Question**: When both files exist in the same directory, which one is selected first?
- **Options**: `AGENTS.override.md` | `AGENTS.md` | `README.md` | The larger file
- **Correct**: `AGENTS.override.md`
- **Explanation**: Codex checks the override name before the regular instruction file and uses at most one file per directory.
- **Review**: How discovery works

### 2.4 — Personal scope

- **Category**: Practical
- **Question**: Where should reusable personal guidance across repositories normally live?
- **Options**: `~/.codex/AGENTS.md` | `<repo>/.env` | `<repo>/README.md` | `~/.ssh/config`
- **Correct**: `~/.codex/AGENTS.md`
- **Explanation**: The Codex home instruction file supplies global personal guidance.
- **Review**: Choose the right scope

### 2.5 — Nested guidance

- **Category**: Practical
- **Question**: A payment service uses a different test command. Where should that instruction go?
- **Options**: In an instruction file inside the payment-service directory | In every source file | In the API key environment variable | Only in the current prompt forever
- **Correct**: In an instruction file inside the payment-service directory
- **Explanation**: Put specialized guidance as close as practical to the subtree it governs.
- **Review**: Add directory-specific guidance

### 2.6 — Mechanical rules

- **Category**: Conceptual
- **Question**: Where should a deterministic formatting rule usually be enforced?
- **Options**: A formatter or CI check | A longer motivational paragraph in `AGENTS.md` | Cached chat memory only | A credential file
- **Correct**: A formatter or CI check
- **Explanation**: Instruction files explain expectations; deterministic tooling should enforce mechanically checkable rules.
- **Review**: What belongs in AGENTS.md

### 2.7 — Session refresh

- **Category**: Practical
- **Question**: What should you do after changing instruction files when a running session still uses old guidance?
- **Options**: Start a new run or session | Delete the Git repository | Put the rule in a secret | Disable all verification
- **Correct**: Start a new run or session
- **Explanation**: Codex builds the instruction chain at the start of a run or interactive session.
- **Review**: Troubleshooting

### 2.8 — Size management

- **Category**: Conceptual
- **Question**: What is the best first response when combined instructions approach the size limit?
- **Options**: Remove duplication and move specialized rules into nested files | Add the entire README again | Store instructions in credentials | Convert every sentence into uppercase
- **Correct**: Remove duplication and move specialized rules into nested files
- **Explanation**: Focused nested guidance reduces unnecessary context while preserving relevant rules.
- **Review**: Troubleshooting

### 2.9 — Verification

- **Category**: Practical
- **Question**: How can you verify root and nested instruction behavior?
- **Options**: Start fresh runs from each directory and ask Codex to summarize loaded sources without editing | Assume the filename guarantees loading | Check only Git history | Rename all files to `README.md`
- **Correct**: Start fresh runs from each directory and ask Codex to summarize loaded sources without editing
- **Explanation**: Running from both scopes provides observable evidence of discovery and precedence.
- **Review**: Verify active instructions

### 2.10 — Review rules

- **Category**: Conceptual
- **Question**: What makes a useful `## Code Review Rules` entry?
- **Options**: It identifies concrete risky behavior and a safe path or exception | It says “write good code” | It duplicates every linter message | It grants permission to bypass approvals
- **Correct**: It identifies concrete risky behavior and a safe path or exception
- **Explanation**: Specific risky behavior and remediation guide Codex toward actionable review findings.
- **Review**: Review rules

## Module 3 — Skills

### 3.1 — Best mechanism
- **Category**: Conceptual
- **Question**: Which mechanism best fits a repeatable discoverable workflow?
- **Options**: Skill | Current prompt only | Credential file | Git tag
- **Correct**: Skill
- **Explanation**: Skills package repeatable workflows; one-off requirements belong in the prompt.
- **Review**: Choose the right mechanism

### 3.2 — Discovery
- **Category**: Conceptual
- **Question**: What skill content does Codex see before selecting the skill?
- **Options**: Name and description | Every reference and asset | All script source | No metadata
- **Correct**: Name and description
- **Explanation**: Progressive disclosure starts with metadata, then loads the body and needed resources.
- **Review**: Progressive disclosure

### 3.3 — Repository path
- **Category**: Practical
- **Question**: Where should a shared repository skill live?
- **Options**: `.agents/skills/<name>/SKILL.md` | `.codex/agents/<name>.toml` | `.env` | `AGENTS.override.md`
- **Correct**: `.agents/skills/<name>/SKILL.md`
- **Explanation**: `.agents/skills` is the repository authoring location for skills.
- **Review**: Skill locations

### 3.4 — Trigger quality
- **Category**: Conceptual
- **Question**: What makes a skill description useful?
- **Options**: A concrete user goal and meaningful boundary | A list of every possible coding task | A vague phrase such as “helps with code” | Hidden credentials
- **Correct**: A concrete user goal and meaningful boundary
- **Explanation**: Descriptions drive routing and must distinguish neighboring workflows.
- **Review**: Write a discriminating description

### 3.5 — References
- **Category**: Practical
- **Question**: When should detailed review guidance move to `references/`?
- **Options**: When it is conditional and needed only for some tasks | For every one-line instruction | To store executable secrets | Never
- **Correct**: When it is conditional and needed only for some tasks
- **Explanation**: Conditional detail belongs in references so it loads only when relevant.
- **Review**: Add resources intentionally

### 3.6 — Scripts
- **Category**: Conceptual
- **Question**: When should a skill add a script?
- **Options**: When deterministic repeated execution materially improves reliability | Whenever a shell is available | To duplicate a built-in tool | To avoid writing instructions
- **Correct**: When deterministic repeated execution materially improves reliability
- **Explanation**: Scripts should solve repeatable deterministic work and must be tested.
- **Review**: Add resources intentionally

### 3.7 — Invocation
- **Category**: Practical
- **Question**: How can a CLI user explicitly mention a skill?
- **Options**: Type `$skill-name` | Rename it to `AGENTS.md` | Put it in shell history | Use an API key as its name
- **Correct**: Type `$skill-name`
- **Explanation**: `$` mentions and `/skills` provide explicit skill invocation in Codex CLI.
- **Review**: Invoke and test

### 3.8 — Implicit policy
- **Category**: Conceptual
- **Question**: What is the default implicit invocation policy?
- **Options**: Enabled | Disabled for every skill | Enabled only for scripts | Controlled by Git
- **Correct**: Enabled
- **Explanation**: Skills are implicitly discoverable unless `allow_implicit_invocation` is deliberately set false.
- **Review**: Optional UI metadata

### 3.9 — Validation
- **Category**: Conceptual
- **Question**: What does structural validation not prove?
- **Options**: That trigger decisions and outputs are useful | That YAML can be parsed | That required frontmatter exists | That scaffold placeholders are absent
- **Correct**: That trigger decisions and outputs are useful
- **Explanation**: Representative requests are still needed after structural validation.
- **Review**: Validate

### 3.10 — Permissions
- **Category**: Conceptual
- **Question**: Does selecting a skill grant new external permissions?
- **Options**: No, normal sandbox, approvals, and tool permissions still apply | Yes, always | Only when the description is long | Only in Git repositories
- **Correct**: No, normal sandbox, approvals, and tool permissions still apply
- **Explanation**: A skill defines workflow guidance, not authority.
- **Review**: Choose the right mechanism

## Module 4 — Subagents

### 4.1 — Good candidate
- **Category**: Conceptual
- **Question**: Which task most benefits from subagents?
- **Options**: Independent security, correctness, and test reviews | Renaming one variable | One tightly sequential edit | Avoiding all review of results
- **Correct**: Independent security, correctness, and test reviews
- **Explanation**: Parallel agents help when work is genuinely independent or specialized.
- **Review**: When to use subagents

### 4.2 — Main thread
- **Category**: Conceptual
- **Question**: What should remain in the main thread?
- **Options**: Requirements, decisions, and integration | Every raw test log | All duplicated exploration | Unbounded background work
- **Correct**: Requirements, decisions, and integration
- **Explanation**: The main thread coordinates scope and consolidates focused results.
- **Review**: The orchestration model

### 4.3 — Built-in explorer
- **Category**: Practical
- **Question**: Which built-in agent is intended for read-heavy codebase exploration?
- **Options**: `explorer` | `worker` | `default` only | `publisher`
- **Correct**: `explorer`
- **Explanation**: The built-in explorer role focuses on read-heavy mapping.
- **Review**: Built-in agents

### 4.4 — Project path
- **Category**: Practical
- **Question**: Where does a project custom agent definition live?
- **Options**: `.codex/agents/<name>.toml` | `.agents/skills/<name>/SKILL.md` | `.mcp.json` | `README.md`
- **Correct**: `.codex/agents/<name>.toml`
- **Explanation**: Project custom agents are standalone TOML files under `.codex/agents`.
- **Review**: Custom-agent locations

### 4.5 — Required fields
- **Category**: Conceptual
- **Question**: Which set contains all required custom-agent fields?
- **Options**: `name`, `description`, `developer_instructions` | `model`, `token`, `owner` | `tools`, `memory`, `branch` | `url`, `command`, `args`
- **Correct**: `name`, `description`, `developer_instructions`
- **Explanation**: These three fields define identity, routing, and behavior.
- **Review**: Custom-agent locations

### 4.6 — Permissions
- **Category**: Conceptual
- **Question**: Can a custom-agent file broaden the parent sandbox?
- **Options**: No | Yes, with developer instructions | Yes, when named worker | Only through its filename
- **Correct**: No
- **Explanation**: Subagents inherit parent security boundaries and cannot expand them.
- **Review**: Inheritance and boundaries

### 4.7 — Read-only wording
- **Category**: Conceptual
- **Question**: What does “do not edit files” inside agent instructions provide?
- **Options**: Behavioral guidance, not a separate sandbox | A guaranteed kernel boundary | New network permissions | A Git backup
- **Correct**: Behavioral guidance, not a separate sandbox
- **Explanation**: Enforce actual security boundaries on the parent session.
- **Review**: Inheritance and boundaries

### 4.8 — Parallel editing
- **Category**: Practical
- **Question**: How should parallel implementation agents avoid conflicts?
- **Options**: Own disjoint files or components | Edit the same files simultaneously | Skip interface agreement | Disable Git
- **Correct**: Own disjoint files or components
- **Explanation**: Disjoint ownership reduces conflicts and coordination overhead.
- **Review**: Coordinate parallel work

### 4.9 — CLI inspection
- **Category**: Practical
- **Question**: Which CLI command inspects and switches subagent threads?
- **Options**: `/subagents` | `/mcp` | `/init` | `/logout`
- **Correct**: `/subagents`
- **Explanation**: `/subagents` exposes active and completed subagent threads in the CLI.
- **Review**: Built-in agents

### 4.10 — Cost
- **Category**: Conceptual
- **Question**: Why should small sequential tasks usually stay in one agent?
- **Options**: Subagents add model work and coordination cost | Subagents cannot read files | The main agent cannot consolidate results | Git forbids delegation
- **Correct**: Subagents add model work and coordination cost
- **Explanation**: Delegation should provide meaningful parallelism or specialization.
- **Review**: When to use subagents

## Module 5 — Model Context Protocol

### 5.1 — Purpose
- **Category**: Conceptual
- **Question**: What problem does MCP solve in this curriculum?
- **Options**: Connecting Codex to external tools and context | Replacing repository instructions | Formatting Markdown only | Storing Git commits
- **Correct**: Connecting Codex to external tools and context
- **Explanation**: MCP provides capabilities and data outside the local repository.
- **Review**: Architecture and trust

### 5.2 — Stdio
- **Category**: Conceptual
- **Question**: What identifies a stdio server in `config.toml`?
- **Options**: A `command` and optional `args` | Only a remote `url` | A Markdown heading | A plugin name alone
- **Correct**: A `command` and optional `args`
- **Explanation**: Codex launches a local process for stdio transport.
- **Review**: Configure stdio in TOML

### 5.3 — HTTP
- **Category**: Conceptual
- **Question**: What is required for a streamable HTTP server configuration?
- **Options**: `url` | Local executable path | Git branch | `AGENTS.md`
- **Correct**: `url`
- **Explanation**: Streamable HTTP connects to an independently hosted URL.
- **Review**: Configure streamable HTTP in TOML

### 5.4 — Project scope
- **Category**: Practical
- **Question**: Where can a trusted project store MCP configuration?
- **Options**: `.codex/config.toml` | `.agents/skills/` | `LICENSE` | `.git/HEAD`
- **Correct**: `.codex/config.toml`
- **Explanation**: Trusted repositories can scope Codex configuration locally.
- **Review**: Configuration scope

### 5.5 — Secrets
- **Category**: Practical
- **Question**: What should a bearer-token configuration store in the file?
- **Options**: The environment variable name | The live token value | A copied browser cookie | The user's password
- **Correct**: The environment variable name
- **Explanation**: `bearer_token_env_var` keeps the credential outside version control.
- **Review**: Configure streamable HTTP in TOML

### 5.6 — CLI add
- **Category**: Practical
- **Question**: Which separator precedes a stdio server command in `codex mcp add`?
- **Options**: `--` | `#` | `@` | `:`
- **Correct**: `--`
- **Explanation**: Arguments after `--` form the stdio server command.
- **Review**: Configure with the CLI

### 5.7 — Tool exposure
- **Category**: Conceptual
- **Question**: Which field creates a tool allowlist?
- **Options**: `enabled_tools` | `disabled_tools` only | `env_vars` | `cwd`
- **Correct**: `enabled_tools`
- **Explanation**: `enabled_tools` limits the visible tools before any deny list is applied.
- **Review**: Limit tools and approvals

### 5.8 — OAuth callback
- **Category**: Practical
- **Question**: Which OAuth callback should be registered?
- **Options**: The exact callback Codex displays | A callback copied from another machine | Any localhost URL | The MCP tool name
- **Correct**: The exact callback Codex displays
- **Explanation**: Callback selection depends on server metadata and registration details.
- **Review**: OAuth

### 5.9 — Hosted web
- **Category**: Conceptual
- **Question**: Why might local MCP config work in CLI but not ChatGPT web?
- **Options**: ChatGPT web does not read local Codex config | HTTP is unsupported everywhere | Skills disable MCP | Git blocks remote tools
- **Correct**: ChatGPT web does not read local Codex config
- **Explanation**: Hosted chats use workspace-enabled plugins and connections instead.
- **Review**: Configuration scope

### 5.10 — Skills pairing
- **Category**: Conceptual
- **Question**: How do a skill and MCP complement each other?
- **Options**: MCP provides live capability; the skill defines the repeatable workflow | Both store the same secret | The skill replaces server authorization | MCP replaces all instructions
- **Correct**: MCP provides live capability; the skill defines the repeatable workflow
- **Explanation**: Capability and workflow guidance are separate concerns.
- **Review**: Pair MCP with skills

## Module 6 — Hooks

### 6.1 — Best mechanism
- **Category**: Conceptual
- **Question**: Which need is the best fit for a hook?
- **Options**: Run a deterministic check before a supported tool call | Explain a team's coding style | Package a reusable writing workflow | Grant repository access
- **Correct**: Run a deterministic check before a supported tool call
- **Explanation**: Hooks attach deterministic actions to lifecycle events.
- **Review**: Choose the right mechanism

### 6.2 — Project location
- **Category**: Practical
- **Question**: Where can a trusted project define JSON hooks?
- **Options**: `.codex/hooks.json` | `.agents/skills/hooks.json` | `.git/hooks.json` | `AGENTS.override.md`
- **Correct**: `.codex/hooks.json`
- **Explanation**: Project hooks live beside the active project configuration layer.
- **Review**: Where hooks live

### 6.3 — Trust after changes
- **Category**: Conceptual
- **Question**: What happens after a non-managed hook definition changes?
- **Options**: Its new hash requires review before it can run | It stays permanently trusted | It becomes a managed hook | It bypasses project trust
- **Correct**: Its new hash requires review before it can run
- **Explanation**: Hook trust is recorded against the exact current definition.
- **Review**: Where hooks live

### 6.4 — Inspection command
- **Category**: Practical
- **Question**: Which CLI command reviews hook sources and trust?
- **Options**: `/hooks` | `/mcp` | `/skills` | `/status`
- **Correct**: `/hooks`
- **Explanation**: The hook browser shows sources, changes, trust, and enabled state.
- **Review**: Where hooks live

### 6.5 — Preventive event
- **Category**: Conceptual
- **Question**: Which event can deny a supported tool call before it runs?
- **Options**: `PreToolUse` | `PostToolUse` | `SessionEnd` | `PostCompact`
- **Correct**: `PreToolUse`
- **Explanation**: A post-tool hook runs after side effects and cannot undo them.
- **Review**: Lifecycle model

### 6.6 — Command input
- **Category**: Practical
- **Question**: How does a command hook receive its event data?
- **Options**: One JSON object on standard input | Environment variables only | A Markdown file | Command-line flags only
- **Correct**: One JSON object on standard input
- **Explanation**: Handlers must parse and validate the JSON event object.
- **Review**: Input and output

### 6.7 — Exact Bash matcher
- **Category**: Practical
- **Question**: Which matcher targets the canonical Bash tool name exactly?
- **Options**: `^Bash$` | `bash*` | `shell` | `.*Write.*`
- **Correct**: `^Bash$`
- **Explanation**: Hook matchers are regular expressions; anchors express an exact match.
- **Review**: Events and matchers

### 6.8 — Concurrent handlers
- **Category**: Conceptual
- **Question**: What happens when several command handlers match one event?
- **Options**: They are launched concurrently | Only the first one runs | A deny prevents peers from starting | Codex merges their scripts
- **Correct**: They are launched concurrently
- **Explanation**: Matching command hooks must not rely on another handler running first.
- **Review**: Concurrency, timeouts, and background work

### 6.9 — Plugin data path
- **Category**: Conceptual
- **Question**: Which plugin hook variable identifies writable plugin state?
- **Options**: `PLUGIN_DATA` | `PLUGIN_ROOT` | `CODEX_HOME` | `PWD`
- **Correct**: `PLUGIN_DATA`
- **Explanation**: `PLUGIN_ROOT` identifies installed resources; `PLUGIN_DATA` is for writable state.
- **Review**: Plugin hooks

### 6.10 — Security boundary
- **Category**: Conceptual
- **Question**: Why should a hook not be the only security boundary?
- **Options**: Some tool paths can bypass hooks and hook code itself runs on the host | Hooks cannot read JSON | Hooks always run remotely | Hooks disable the sandbox
- **Correct**: Some tool paths can bypass hooks and hook code itself runs on the host
- **Explanation**: Use sandbox and managed policy for stronger enforcement.
- **Review**: Choose the right mechanism

## Module 7 — Plugins

### 7.1 — Plugin threshold
- **Category**: Conceptual
- **Question**: When is a plugin preferable to a standalone skill?
- **Options**: When related workflows and capabilities need installation and distribution together | For every private prompt | To replace repository instructions | To bypass approvals
- **Correct**: When related workflows and capabilities need installation and distribution together
- **Explanation**: A plugin adds packaging, installation, updates, and component composition.
- **Review**: Skill or plugin?

### 7.2 — Marketplace role
- **Category**: Conceptual
- **Question**: What is a marketplace?
- **Options**: A catalog that points to plugin packages | The plugin's runtime sandbox | An MCP authentication token | A skill frontmatter block
- **Correct**: A catalog that points to plugin packages
- **Explanation**: Marketplace entries describe source and install policy; the package contains capabilities.
- **Review**: Plugin architecture

### 7.3 — Compatibility manifest
- **Category**: Practical
- **Question**: Which file is required by the Plugin Creator compatibility scaffold?
- **Options**: `.codex-plugin/plugin.json` | `.mcp.json` | `.app.json` | `hooks/hooks.json`
- **Correct**: `.codex-plugin/plugin.json`
- **Explanation**: Other compatibility components are optional and must exist before being referenced.
- **Review**: Package layouts

### 7.4 — Portable manifest
- **Category**: Practical
- **Question**: Where does the portable Agent Plugins manifest live?
- **Options**: `plugin.json` at the plugin root | `.codex/plugin.toml` | `skills/plugin.json` | `.agents/plugins.json`
- **Correct**: `plugin.json` at the plugin root
- **Explanation**: The portable layout uses the Agent Plugins schema at the root.
- **Review**: Package layouts

### 7.5 — MCP conversion
- **Category**: Conceptual
- **Question**: Why should `.mcp.json` not simply be renamed to portable `mcp.json`?
- **Options**: The portable schema also requires transport information | Portable plugins cannot use MCP | The filename must contain a secret | Renaming disables skills
- **Correct**: The portable schema also requires transport information
- **Explanation**: Compatibility and portable MCP files have different schema requirements.
- **Review**: Package layouts

### 7.6 — Permissions
- **Category**: Conceptual
- **Question**: Does installing a plugin grant broader host or service access?
- **Options**: No, host policy and service authorization still apply | Yes, for every bundled skill | Only in CLI | Only for local marketplaces
- **Correct**: No, host policy and service authorization still apply
- **Explanation**: Packaging capabilities does not expand authority.
- **Review**: Plugin architecture

### 7.7 — Discovery after install
- **Category**: Practical
- **Question**: What should a user do after installing a plugin?
- **Options**: Start a new chat or CLI session | Delete the manifest | Embed service credentials | Disable project trust
- **Correct**: Start a new chat or CLI session
- **Explanation**: New sessions discover the installed plugin's skills and tools.
- **Review**: Supported surfaces

### 7.8 — Personal marketplace
- **Category**: Conceptual
- **Question**: Does the default personal marketplace require `codex plugin marketplace add`?
- **Options**: No, it is discovered automatically | Yes, on every launch | Only when it has one plugin | Only for skill-only plugins
- **Correct**: No, it is discovered automatically
- **Explanation**: The add command is for non-default marketplace sources.
- **Review**: Local marketplaces

### 7.9 — Plugin hook trust
- **Category**: Conceptual
- **Question**: What trust does plugin installation give bundled hooks?
- **Options**: None automatically; hook definitions require separate review | Permanent managed trust | Trust only for Bash | Trust inherited from the marketplace name
- **Correct**: None automatically; hook definitions require separate review
- **Explanation**: Plugin hooks use the normal non-managed hook trust flow.
- **Review**: Components and permissions

### 7.10 — Surface boundary
- **Category**: Conceptual
- **Question**: Which Codex surface currently lacks the plugin browser?
- **Options**: IDE extension | CLI | Codex in the ChatGPT desktop app | Plugins Directory in ChatGPT
- **Correct**: IDE extension
- **Explanation**: Plugin availability is surface-specific and should be documented explicitly.
- **Review**: Supported surfaces

## Module 8 — Safety and Worktrees

### 8.1 — Control boundary
- **Category**: Conceptual
- **Question**: What does the sandbox primarily govern?
- **Options**: Filesystem and command or network boundaries | Whether code is correct | The user's intended outcome | Git commit history
- **Correct**: Filesystem and command or network boundaries
- **Explanation**: Intent, approvals, rules, and Git solve different problems.
- **Review**: The control layers

### 8.2 — Workspace network
- **Category**: Conceptual
- **Question**: What is the default network posture of `workspace-write`?
- **Options**: Network access is off unless enabled | Unrestricted internet | GitHub only | Inherited from every browser session
- **Correct**: Network access is off unless enabled
- **Explanation**: Workspace write access does not automatically enable command network access.
- **Review**: Sandbox modes

### 8.3 — On-request approvals
- **Category**: Conceptual
- **Question**: What does `approval_policy = "on-request"` mean?
- **Options**: Work inside the sandbox and ask for boundary exceptions | Ask before every read | Never run commands | Remove the sandbox
- **Correct**: Work inside the sandbox and ask for boundary exceptions
- **Explanation**: The sandbox remains active while exceptional actions can be reviewed.
- **Review**: Approval policy and reviewer

### 8.4 — Automatic reviewer
- **Category**: Conceptual
- **Question**: What boundary does `approvals_reviewer = "auto_review"` change?
- **Options**: It changes who reviews eligible requests, not the sandbox | It enables full access | It expands writable roots | It disables rules
- **Correct**: It changes who reviews eligible requests, not the sandbox
- **Explanation**: Automatic review is a reviewer choice at an existing boundary.
- **Review**: Approval policy and reviewer

### 8.5 — Project rules path
- **Category**: Practical
- **Question**: Where can a trusted project store command rules?
- **Options**: `.codex/rules/*.rules` | `.git/rules.toml` | `.agents/skills/rules` | `AGENTS.override.md`
- **Correct**: `.codex/rules/*.rules`
- **Explanation**: Codex scans rules beside active configuration layers.
- **Review**: Command rules

### 8.6 — Rule testing
- **Category**: Practical
- **Question**: Which command evaluates a rule without running the target command?
- **Options**: `codex execpolicy check` | `codex exec` | `git check-rule` | `/permissions`
- **Correct**: `codex execpolicy check`
- **Explanation**: The preview command returns the matching rules and strictest decision.
- **Review**: Command rules

### 8.7 — Conflicting rules
- **Category**: Conceptual
- **Question**: Which decision wins when several command rules match?
- **Options**: The most restrictive | The first file alphabetically | The shortest prefix | The user's latest prompt
- **Correct**: The most restrictive
- **Explanation**: The ordering is `forbidden`, then `prompt`, then `allow`.
- **Review**: Command rules

### 8.8 — Worktree benefit
- **Category**: Conceptual
- **Question**: What does a Git worktree isolate?
- **Options**: Checkout files and index state | Host permissions | External service identity | Every shared interface decision
- **Correct**: Checkout files and index state
- **Explanation**: Worktrees reduce local file collisions but do not expand or enforce runtime permissions.
- **Review**: Worktree model

### 8.9 — Managed worktree branch
- **Category**: Practical
- **Question**: What should you do when a detached managed worktree must become long-lived?
- **Options**: Create a branch there | Enable full access | Copy its `.git` directory | Delete the local checkout
- **Correct**: Create a branch there
- **Explanation**: Codex-managed worktrees normally start in detached `HEAD`.
- **Review**: Codex-managed worktrees

### 8.10 — Safe cleanup
- **Category**: Conceptual
- **Question**: What must happen before removing a worktree?
- **Options**: Inspect the exact path and status for work to preserve | Always use `--force` | Delete the shared Git metadata | Push every untracked file
- **Correct**: Inspect the exact path and status for work to preserve
- **Explanation**: Cleanup must not silently discard tracked or untracked work.
- **Review**: Manual Git worktree workflow

## Module 9 — Advanced Workflows

### 9.1 — Plan mode
- **Category**: Conceptual
- **Question**: When is `/plan` most useful?
- **Options**: When requirements or implementation order need review | For every one-line edit | To grant network access | To install a plugin
- **Correct**: When requirements or implementation order need review
- **Explanation**: Plan mode improves decisions before implementation but grants no new permissions.
- **Review**: Choose the planning depth

### 9.2 — Durable plan
- **Category**: Conceptual
- **Question**: Why store an execution plan in the repository?
- **Options**: To preserve decisions and progress across many turns | To replace tests | To hide scope changes | To authorize external actions
- **Correct**: To preserve decisions and progress across many turns
- **Explanation**: A durable plan is an evolving decision and verification record.
- **Review**: Choose the planning depth

### 9.3 — Integration owner
- **Category**: Conceptual
- **Question**: Which unit should retain requirements and final integration?
- **Options**: The current chat | Every subagent independently | A background terminal | A scheduled run with no prompt
- **Correct**: The current chat
- **Explanation**: Delegated work returns bounded results to the coordinating conversation.
- **Review**: Units of work

### 9.4 — Separate task
- **Category**: Conceptual
- **Question**: When should Codex create a separate user-owned task?
- **Options**: When the user explicitly asks for separate work | For every internal investigation | Whenever a command is slow | To avoid reporting progress
- **Correct**: When the user explicitly asks for separate work
- **Explanation**: Internal delegation belongs in subagents, not unsolicited visible tasks.
- **Review**: Units of work

### 9.5 — Cloud boundary
- **Category**: Conceptual
- **Question**: What does a Cloud task not receive automatically?
- **Options**: Local files, processes, browser sign-ins, and personal skills | Published repository state | Configured environment tools | Repository skills
- **Correct**: Local files, processes, browser sign-ins, and personal skills
- **Explanation**: Cloud execution uses the published environment rather than the local computer state.
- **Review**: Execution environments

### 9.6 — Republished environment
- **Category**: Conceptual
- **Question**: What happens to an existing Cloud task after its environment is republished?
- **Options**: It keeps its own working state | It is rewritten immediately | It becomes a local task | It loses all files
- **Correct**: It keeps its own working state
- **Explanation**: New tasks use the updated publication; existing tasks retain their state.
- **Review**: Execution environments

### 9.7 — Long-running monitoring
- **Category**: Conceptual
- **Question**: What is the preferred way to monitor long-running work?
- **Options**: Event-driven waiting or polling that returns on change | A tight endless loop | Repeated unchanged messages | Ignoring approval requests
- **Correct**: Event-driven waiting or polling that returns on change
- **Explanation**: Report meaningful transitions without consuming resources on unchanged state.
- **Review**: Long-running commands

### 9.8 — Browser in Cloud
- **Category**: Conceptual
- **Question**: Can a Cloud task assume access to the user's local signed-in browser?
- **Options**: No | Yes, always | Only after creating a worktree | Only through `AGENTS.md`
- **Correct**: No
- **Explanation**: Browser and computer state do not transfer automatically to Cloud.
- **Review**: Browser-assisted verification

### 9.9 — Schedule shape
- **Category**: Conceptual
- **Question**: Which schedule should retain an investigation's existing conversation context?
- **Options**: A scheduled task in that chat | An independent standalone run | `codex exec --ephemeral` | A new unrelated Cloud environment
- **Correct**: A scheduled task in that chat
- **Explanation**: Standalone schedules start separate runs from their saved prompt.
- **Review**: Scheduled tasks

### 9.10 — Skill and schedule
- **Category**: Conceptual
- **Question**: How do a skill and scheduled task complement each other?
- **Options**: The skill defines the method; the task defines when and where it runs | Both grant credentials | The schedule replaces verification | The skill creates authority
- **Correct**: The skill defines the method; the task defines when and where it runs
- **Explanation**: Stabilize the workflow before automating its cadence.
- **Review**: Write a durable scheduled prompt

## Module 10 — CLI and Automation

### 10.1 — Non-interactive command
- **Category**: Practical
- **Question**: Which command runs one bounded Codex task without the interactive TUI?
- **Options**: `codex exec` | `/plan` | `codex mcp` | `codex plugin`
- **Correct**: `codex exec`
- **Explanation**: Plain `codex` starts the interactive terminal UI.
- **Review**: Interactive versus non-interactive

### 10.2 — Default sandbox
- **Category**: Conceptual
- **Question**: What sandbox does `codex exec` use by default?
- **Options**: Read-only | Workspace-write | Danger-full-access | No sandbox
- **Correct**: Read-only
- **Explanation**: Automation should opt into write access only when needed.
- **Review**: Basic non-interactive run

### 10.3 — Standard streams
- **Category**: Conceptual
- **Question**: Without `--json`, where do progress and the final message go?
- **Options**: Progress to stderr and final message to stdout | Both to stdout | Both to stderr | Final message to a Git commit
- **Correct**: Progress to stderr and final message to stdout
- **Explanation**: Separate streams make the final result easier to pipe or redirect.
- **Review**: Basic non-interactive run

### 10.4 — Piped context
- **Category**: Conceptual
- **Question**: What happens when stdin is piped while a prompt argument is also provided?
- **Options**: The prompt is instruction and stdin is appended as context | Stdin is discarded | The prompt is executed as shell syntax | The run always fails
- **Correct**: The prompt is instruction and stdin is appended as context
- **Explanation**: This supports separating trusted instructions from additional input data.
- **Review**: Prompt input and context

### 10.5 — JSONL output
- **Category**: Practical
- **Question**: Which flag emits a JSON Lines event stream?
- **Options**: `--json` | `--output-schema` | `--strict-config` | `--ephemeral`
- **Correct**: `--json`
- **Explanation**: Each line is a lifecycle event object identified by its type.
- **Review**: Output modes

### 10.6 — Output schema scope
- **Category**: Conceptual
- **Question**: What does `--output-schema` constrain?
- **Options**: The final response | Every JSONL event | Shell command arguments | The Git working tree
- **Correct**: The final response
- **Explanation**: The event stream and schema-constrained final result are separate outputs.
- **Review**: Output modes

### 10.7 — Resume selection
- **Category**: Practical
- **Question**: How does `codex exec resume --last` select a session by default?
- **Options**: Most recent session for the current working directory | Oldest global session | Latest Cloud environment | Current Git branch only
- **Correct**: Most recent session for the current working directory
- **Explanation**: Add `--all` or use an explicit ID when another directory is intended.
- **Review**: Sessions, resume, fork, and worktrees

### 10.8 — Ephemeral runs
- **Category**: Conceptual
- **Question**: What is the main consequence of `--ephemeral`?
- **Options**: The session cannot later be resumed | It enables full access | It suppresses all output | It creates a permanent worktree
- **Correct**: The session cannot later be resumed
- **Explanation**: Ephemeral runs do not persist session rollout files.
- **Review**: Sessions, resume, fork, and worktrees

### 10.9 — CI trigger
- **Category**: Conceptual
- **Question**: Why does the tutorial GitHub workflow use a manual trigger?
- **Options**: It limits who can start a credentialed example run | It grants repository writes | It bypasses prompt injection | It makes API keys public
- **Correct**: It limits who can start a credentialed example run
- **Explanation**: Trigger scope is one part of CI least privilege; untrusted content still requires care.
- **Review**: GitHub Actions

### 10.10 — Retired flag
- **Category**: Practical
- **Question**: Which former automation flag is no longer supported?
- **Options**: `--full-auto` | `--sandbox` | `--output-schema` | `--json`
- **Correct**: `--full-auto`
- **Explanation**: Use explicit sandbox settings or eligible automatic approval review instead.
- **Review**: Basic non-interactive run
