# Gap recommendations

Use only the entries that match the learner's gaps. Preserve this dependency
order unless the learner explicitly wants a different topic.

| Area | Module | Focus | Exercise | Done when |
|---|---|---|---|---|
| Getting started | [01](../../../../01-getting-started/) | Surface choice, bounded prompts, `/status`, `/diff`, verification | Make one safe README edit | Only the expected file changes and the check passes |
| AGENTS.md | [02](../../../../02-agents-md/) | Discovery, scope, concise commands and completion rules | Add root and nested guidance | Root and nested runs report the correct instructions |
| Skills | [03](../../../../03-skills/) | `SKILL.md`, descriptions, progressive disclosure | Build one focused project skill | Explicit and matching implicit requests use it correctly |
| Subagents | [04](../../../../04-subagents/) | Bounded delegation and custom-agent TOML | Delegate exploration and consolidate evidence | The main thread receives a focused, verifiable result |
| MCP | [05](../../../../05-mcp/) | Transport, authentication, tool exposure, approvals | Configure one least-privilege server | A documented tool works without exposing credentials |
| Hooks | [06](../../../../06-hooks/) | Events, matchers, JSON I/O, trust | Test one hook with sample input | Expected allow/block behavior is reproducible |
| Plugins | [07](../../../../07-plugins/) | Manifest, dependencies, validation | Inspect or build one local plugin | Components and permissions are documented and validated |
| Safety and worktrees | [08](../../../../08-safety-and-worktrees/) | Sandbox, approvals, rules, Git isolation | Complete a worktree change | The diff is isolated and safely reviewed or discarded |
| Advanced workflows | [09](../../../../09-advanced-workflows/) | Planning, tasks, waiting, scheduling | Design one workflow with a stop condition | Scope, execution surface, and completion are explicit |
| CLI automation | [10](../../../../10-cli-and-automation/) | `codex exec`, output, exit status, CI | Run one bounded scripted check | The script handles success and failure safely |

Modules 1 and 2 are completed in the current phase. Modules 3–10 may still be
outlines; label them as upcoming until their status changes.

