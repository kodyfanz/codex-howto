# Assessment questions and scoring

## Mode selection

- **Quick**: eight yes/no experience checks, approximately two minutes.
- **Deep**: ten areas with a foundation and advanced check, approximately five minutes.

## Quick assessment

Ask in two rounds of four. A selected item earns one point.

### Round 1 — Foundations

1. **Completed a verified Codex task** — Used CLI, IDE, desktop app, or cloud;
   reviewed the result and ran an appropriate check.
2. **Created repository guidance** — Wrote or meaningfully edited `AGENTS.md`
   and verified that Codex loaded it.
3. **Created or installed a skill** — Used a `SKILL.md` workflow explicitly or
   observed it trigger from a matching request.
4. **Used a subagent** — Delegated a bounded task and reviewed its returned
   result.

### Round 2 — Integration and operation

5. **Configured MCP** — Connected a server or app and used one of its tools or
   resources with understood permissions.
6. **Configured a hook or plugin** — Tested a lifecycle hook or installed and
   inspected a plugin workflow.
7. **Worked with safety controls** — Deliberately selected or inspected sandbox,
   approval, rules, or worktree behavior.
8. **Used CLI automation** — Ran `codex exec`, structured output, a script, or a
   reviewed CI workflow.

### Quick scoring

- 0–2: **Foundation**
- 3–5: **Workflow builder**
- 6–8: **Advanced operator**

## Deep assessment

Ask five rounds. Each round covers two areas. Every area has two independently
scored checks: foundation and advanced. Each selected check earns one point,
for a maximum of 20.

### Round 1 — Daily use and instructions

- **Getting started, foundation**: Completed a bounded task and reviewed its
  diff or artifact.
- **Getting started, advanced**: Can choose among CLI, IDE, desktop, and cloud
  based on context, authority, and execution environment.
- **AGENTS.md, foundation**: Created project instructions with real commands and
  completion checks.
- **AGENTS.md, advanced**: Verified global, root, and nested precedence or used
  an intentional `AGENTS.override.md`.

### Round 2 — Reuse and delegation

- **Skills, foundation**: Created or installed a project skill and invoked it.
- **Skills, advanced**: Designed precise trigger metadata and used supporting
  references, scripts, assets, or invocation policy appropriately.
- **Subagents, foundation**: Delegated a focused read-heavy task and integrated
  the result.
- **Subagents, advanced**: Coordinated parallel specialists or created a custom
  `.codex/agents/*.toml` definition without overlapping write ownership.

### Round 3 — Connections and lifecycle automation

- **MCP, foundation**: Configured and used an MCP server or app connector.
- **MCP, advanced**: Deliberately configured transport, authentication, tool
  exposure, and approval behavior.
- **Hooks, foundation**: Configured and tested a hook with sample event input.
- **Hooks, advanced**: Reviewed blocking behavior, trust, failure handling, and
  project-versus-plugin scope.

### Round 4 — Distribution and safety

- **Plugins, foundation**: Installed a plugin and inspected its components and
  permissions.
- **Plugins, advanced**: Built or validated a plugin containing a skill and at
  least one additional extension type.
- **Safety, foundation**: Can explain sandbox and approval policy separately.
- **Safety, advanced**: Used command rules, managed requirements, or a worktree
  to create a deliberate boundary.

### Round 5 — Orchestration and automation

- **Advanced workflows, foundation**: Used planning or monitored a long-running
  task without losing scope.
- **Advanced workflows, advanced**: Designed a scheduled, cloud, browser-backed,
  or multi-agent workflow with a clear stopping condition.
- **CLI automation, foundation**: Used `codex exec` and handled its exit status.
- **CLI automation, advanced**: Used structured output or a least-privilege CI
  integration with reviewed credentials and permissions.

### Deep scoring

- 0–6: **Foundation**
- 7–13: **Workflow builder**
- 14–20: **Advanced operator**

For each area: 0 means learn, 1 means review, and 2 means demonstrated.

