# Codex How To project task register

This file is the living task register for Codex How To. It records what the project has already delivered, what should be improved next, and where each claim or implementation can be verified.

The repository remains English-only. Keep task descriptions, acceptance criteria, and links in English so this file can be included in the website, EPUB, and release archive.

## How to maintain this file

- Mark a task `[x]` only when its acceptance criteria are verified and the linked artifact exists.
- Keep one task focused on one reviewable outcome.
- Link internal work with relative repository paths; link Codex behavior to an official OpenAI documentation page.
- Add a short note under a task when an account, product surface, feature flag, or network connection is required.
- Add new work under **Future backlog** before implementation begins. Move it to **Completed work** only after the quality gate passes.
- Do not store credentials, private URLs, or generated logs in this register.

Status: `[x]` done · `[>]` in progress · `[ ]` planned · `[-]` parked or
blocked by a policy decision.

## Project goal

Make Codex approachable for learners at different levels by providing:

1. A progressive ten-module path from first repository task to safe automation.
2. Copy-ready examples that explain scope, authority, prerequisites, and cleanup.
3. Small practical exercises with observable verification steps.
4. Surface labels for CLI, IDE, desktop, cloud, worktree, and ChatGPT Work.
5. Links to the official OpenAI documentation whenever local guidance is asummary, account-dependent, experimental, or likely to change.

## Completed work

### Foundation and curriculum

- [x] Define the English-only repository policy and Codex product boundaries.
  - Evidence: [AGENTS.md](AGENTS.md), [STYLE_GUIDE.md](STYLE_GUIDE.md), [README.md](README.md)
  - Acceptance: no translation tree is part of the current curriculum; claims identify the applicable Codex surface.
- [x] Build the ten-module learning sequence.
  - Evidence: [LEARNING-ROADMAP.md](LEARNING-ROADMAP.md), [INDEX.md](INDEX.md), [CATALOG.md](CATALOG.md)
  - Acceptance: modules remain dependency-ordered from getting started through CLI and automation.
- [x] Write Module 1 and Module 2 with first-task and `AGENTS.md` exercises.
  - Evidence: [01-getting-started/README.md](01-getting-started/README.md),
    [02-agents-md/README.md](02-agents-md/README.md)
  - Official references: [AGENTS.md documentation](https://learn.chatgpt.com/docs/agent-configuration/agents-md),
    [Codex environments](https://learn.chatgpt.com/docs/environments/modes)
- [x] Write Modules 3–5 for skills, subagents, and MCP.
  - Evidence: [03-skills/README.md](03-skills/README.md),
    [04-subagents/README.md](04-subagents/README.md),
    [05-mcp/README.md](05-mcp/README.md)
  - Official references: [Build skills](https://learn.chatgpt.com/docs/build-skills),
    [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents),
    [MCP](https://learn.chatgpt.com/docs/extend/mcp)
- [x] Write Modules 6–7 for hooks and plugins, including three plugin examples.
  - Evidence: [06-hooks/README.md](06-hooks/README.md),
    [07-plugins/README.md](07-plugins/README.md),
    [copy-ready example plugins](07-plugins/README.md#copy-ready-example-plugins)
  - Official references: [Hooks](https://learn.chatgpt.com/docs/hooks),
    [Build plugins](https://developers.openai.com/api/docs/guides/agents-api/tools/plugins)
- [x] Write Modules 8–10 for safety, worktrees, advanced workflows, and CLI
  automation.
  - Evidence: [08-safety-and-worktrees/README.md](08-safety-and-worktrees/README.md),
    [09-advanced-workflows/README.md](09-advanced-workflows/README.md),
    [10-cli-and-automation/README.md](10-cli-and-automation/README.md)
  - Official references: [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees),
    [Developer commands](https://learn.chatgpt.com/docs/developer-commands),
    [Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode)

### Reusable learning assets

- [x] Add the `$self-assessment` skill and a ten-module `$lesson-quiz` skill.
  - Evidence: [.agents/skills/self-assessment/SKILL.md](.agents/skills/self-assessment/SKILL.md),
    [.agents/skills/lesson-quiz/SKILL.md](.agents/skills/lesson-quiz/SKILL.md)
  - Acceptance: skill frontmatter, references, question coverage, and result
    templates validate successfully.
- [x] Add copy-ready agent, MCP, hook, plugin, rules, automation, and CI examples.
  - Evidence: [subagent example](04-subagents/examples/codebase-explorer.toml),
    [MCP example](05-mcp/examples/openai-docs-http.toml),
    [hook configuration](06-hooks/examples/hooks-config.toml),
    [least-privilege configuration](08-safety-and-worktrees/examples/least-privilege-config.toml),
    [scheduled-work example](09-advanced-workflows/examples/scheduled-doc-check.md),
    [CLI review example](10-cli-and-automation/examples/read-only-review.md)
  - Acceptance: examples contain no real credentials and include verification
    or safety notes.
- [x] Create original project branding and document asset provenance.
  - Evidence: [resources README](resources/README.md),
    [light logo](resources/logos/codex-howto-logo.svg),
    [docs/ASSET_LICENSES.md](docs/ASSET_LICENSES.md)

### Quality and release tooling

- [x] Add offline Markdown, cross-reference, link, and Mermaid validation.
  - Evidence: [scripts/check_markdown.py](scripts/check_markdown.py),
    [scripts/check_cross_references.py](scripts/check_cross_references.py),
    [scripts/check_links.py](scripts/check_links.py),
    [scripts/check_mermaid.py](scripts/check_mermaid.py)
- [x] Render supported Mermaid flowcharts to local SVG in website and EPUB
  outputs while preserving source fallback.
  - Evidence: [scripts/mermaid_renderer.py](scripts/mermaid_renderer.py),
    [release tooling](scripts/README.md)
  - Acceptance: nine diagrams render in both artifacts and the EPUB XML is
    valid.
- [x] Build and test the static website, EPUB, and release archive.
  - Evidence: [scripts/build_website.py](scripts/build_website.py),
    [scripts/build_epub.py](scripts/build_epub.py),
    [scripts/build_release.py](scripts/build_release.py),
    [scripts/README.md](scripts/README.md)
- [x] Add one offline quality gate covering documentation, structured examples,
  skills, plugins, tests, builds, and release exclusions.
  - Evidence: [scripts/quality_gate.py](scripts/quality_gate.py),
    [release-tool tests](scripts/tests/test_release_tools.py)
  - Latest verified result: 44 Markdown files, 13 Mermaid blocks, 15 release
    tests, five hook tests, and three plugin tests pass.
- [x] Clarify the Module 2 hands-on exercise with an isolated practice repo,
  ordered steps, expected observations, learning outcomes, and cleanup.
  - Evidence: [Module 2](02-agents-md/README.md)
  - Acceptance: learners can reproduce root and nested instruction discovery
    without accidentally inheriting a parent project's guidance.
- [x] Add dependency-free syntax highlighting to generated code examples.
  - Evidence: [Markdown renderer](scripts/doc_utils.py),
    [website styles](scripts/website_templates/site.css)
  - Acceptance: common strings, comments, numbers, and keywords render with
    semantic color classes in the website and EPUB without a CDN dependency.
- [x] Add a linked glossary for AI, Codex, safety, and file-format terminology.
  - Evidence: [GLOSSARY.md](GLOSSARY.md), [Complete index](INDEX.md)
  - Acceptance: key terms and abbreviations link to a local lesson and an
    official reference when the concept is surface-specific or changeable.
- [x] Make the complete learning-path diagram readable in generated outputs.
  - Evidence: [Learning roadmap](LEARNING-ROADMAP.md)
  - Acceptance: the overview groups the ten modules into four concise
    milestone nodes, and each group has a child-step flowchart that remains
    legible on website and EPUB pages.

## Future backlog

Priorities: `P0` protects correctness or learner safety, `P1` improves the
learning experience, and `P2` is useful polish or expansion.

### P0 — correctness, safety, and maintenance

- [ ] **TASK-001: Add a scheduled official-docs freshness review.**
  - Goal: detect changed URLs, renamed commands, and stale surface labels before
    learners copy them.
  - Plan: run `python3 scripts/check_links.py --external` in a network-enabled
    review environment; manually inspect every changed OpenAI source; record the
    review date here.
  - Acceptance: no unexplained broken official link; each changed claim points
    to a current official page.
  - References: [Developer commands](https://learn.chatgpt.com/docs/developer-commands),
    [Build skills](https://learn.chatgpt.com/docs/build-skills)

- [ ] **TASK-002: Add CI execution for the quality gate.**
  - Goal: prevent documentation regressions from reaching the website, EPUB, or
    release archive.
  - Plan: add a read-only workflow that runs the gate on pull requests and a
    scheduled freshness job with explicit network policy.
  - Acceptance: pull requests receive a deterministic offline result; network
    checks are isolated and never receive credentials from untrusted code.
  - Starting point: [10-cli-and-automation/examples/read-only-review.yml](10-cli-and-automation/examples/read-only-review.yml)
  - Reference: [Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode)

- [ ] **TASK-003: Add adversarial safety tests for every executable example.**
  - Goal: teach learners what an example can change, not only how to make it
    work on the happy path.
  - Plan: add fixtures for untrusted repository content, dangerous shell
    commands, unexpected hook input, missing approvals, and leaked environment
    variables.
  - Acceptance: each safety-sensitive example has a deny case, a least-privilege
    configuration, and a cleanup step.
  - References: [Hooks](https://learn.chatgpt.com/docs/hooks),
    [Developer commands](https://learn.chatgpt.com/docs/developer-commands)

- [ ] **TASK-004: Decide whether the project should become a Git repository.**
  - Goal: make worktree, review, rollback, and CI exercises reproducible.
  - Plan: document the repository decision and initial branch policy; do not
    initialize or publish a repository without explicit project-owner approval.
  - Acceptance: Module 8's worktree exercise can be followed from a clean
    checkout and its assumptions are documented.
  - Reference: [Worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)

### P1 — learner experience and practical coverage

- [ ] **TASK-005: Add a complete beginner capstone.**
  - Goal: guide a new learner from opening Codex to reviewing a safe, verified
    repository change in one short session.
  - Plan: provide a disposable fixture repository, a five-step prompt sequence,
    expected observations, a review checklist, and reset instructions.
  - Acceptance: a beginner can complete it without hidden state; every command
    has a visible success signal and a safe failure explanation.
  - Starting point: [01-getting-started/README.md](01-getting-started/README.md)

- [ ] **TASK-006: Add one lab and assessment rubric per module.**
  - Goal: make progress measurable for foundation, intermediate, and advanced
    learners.
  - Plan: add prerequisites, time estimate, task, expected output, verification,
    troubleshooting, and a small rubric to each module.
  - Acceptance: `$lesson-quiz` links to the lab and the rubric distinguishes
    “can follow steps” from “can explain authority and tradeoffs.”
  - Starting point: [.agents/skills/lesson-quiz/SKILL.md](.agents/skills/lesson-quiz/SKILL.md)

- [ ] **TASK-007: Add a surface comparison matrix.**
  - Goal: reduce confusion between Codex CLI, IDE, desktop, cloud, worktree,
    and ChatGPT Work behavior.
  - Plan: for each module, label availability, setup, authentication, filesystem
    boundary, approval model, and whether the example is experimental or
    account-dependent.
  - Acceptance: every claim has a surface label and an official reference; no
    lesson implies that one surface's behavior applies everywhere.
  - Starting point: [CATALOG.md](CATALOG.md)
  - Reference: [Codex environments](https://learn.chatgpt.com/docs/environments/modes)

- [ ] **TASK-008: Add troubleshooting paths for failed exercises.**
  - Goal: help learners recover without disabling safety controls or guessing.
  - Plan: add “symptom → likely cause → safe check → recovery” sections for
    authentication, permissions, MCP connection, hook trust, plugin paths, and
    worktrees.
  - Acceptance: each recovery path states what it changes and what it does not
    change; no step asks a learner to paste a secret.
  - Starting points: [01-getting-started/README.md](01-getting-started/README.md),
    [05-mcp/README.md](05-mcp/README.md), [06-hooks/README.md](06-hooks/README.md)

- [ ] **TASK-009: Expand the lesson quiz with scenario-based questions.**
  - Goal: test judgment about authority, surface boundaries, approvals, and
    tradeoffs rather than command memorization.
  - Plan: add one safe/unsafe decision, one debugging scenario, and one design
    question per module while keeping ten questions per quiz.
  - Acceptance: every answer cites a lesson section and at least one official
    reference; wrong answers receive targeted review links.
  - Starting point: [.agents/skills/lesson-quiz/references/question-bank.md](.agents/skills/lesson-quiz/references/question-bank.md)

### P2 — tooling and future expansion

- [ ] **TASK-010: Broaden diagram support or adopt an optional full Mermaid CLI.**
  - Goal: support sequence diagrams and other diagram types if future lessons
    need them without silently showing raw code.
  - Plan: either implement and test another bounded syntax subset or add an
    explicitly optional, pinned Mermaid CLI path; retain SVG and source
    fallbacks.
  - Acceptance: unsupported syntax fails with an actionable build error rather
    than producing a misleading diagram.
  - Current limitation: [scripts/mermaid_renderer.py](scripts/mermaid_renderer.py)
    supports flowcharts with rectangular nodes and directed arrows.

- [ ] **TASK-011: Add deterministic visual regression checks for generated pages.**
  - Goal: catch layout regressions in diagrams, tables, code blocks, and mobile
    navigation.
  - Plan: use a controlled local browser or renderer in CI, store only reviewed
    baselines, and keep screenshots out of the release unless licensed.
  - Acceptance: representative desktop and narrow viewport checks run without
    credentials or external services.
  - Related policy: [docs/ASSET_LICENSES.md](docs/ASSET_LICENSES.md)

- [ ] **TASK-012: Add an optional SDK/App Server advanced module.**
  - Goal: serve experienced learners who want to embed or orchestrate Codex
    beyond CLI workflows.
  - Plan: only add it after official documentation, stable setup instructions,
    safe authentication guidance, and a runnable local fixture are available.
  - Acceptance: the module clearly separates Codex product features from API or
    Agents SDK concepts and labels account, model, and network requirements.
  - Starting point: [10-cli-and-automation/README.md](10-cli-and-automation/README.md)
  - Reference hub: [Build with Codex](https://learn.chatgpt.com/docs/developer-commands)

## Release checklist

Before marking a future task done:

- [ ] The learner-facing documentation is concise, English-only, and linked from
  the relevant module or index.
- [ ] Every runnable example has prerequisites, safe defaults, verification, and
  cleanup guidance.
- [ ] Product claims are checked against the correct official OpenAI surface.
- [ ] Secrets, account identifiers, private paths, and generated logs are absent.
- [ ] `python3 scripts/quality_gate.py` passes.
- [ ] Website and EPUB outputs are rebuilt and inspected when the task changes
  publication content or rendering.
- [ ] This register contains the final status and links to the completed work.

## Official reference set

Use these pages as the starting point for future claims; verify the page again
when the task is started because product behavior and availability can change:

- [AGENTS.md and custom instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)
- [Model Context Protocol](https://learn.chatgpt.com/docs/extend/mcp)
- [Hooks](https://learn.chatgpt.com/docs/hooks)
- [Plugins](https://developers.openai.com/api/docs/guides/agents-api/tools/plugins)
- [Codex environments](https://learn.chatgpt.com/docs/environments/modes)
- [Git worktrees](https://learn.chatgpt.com/docs/environments/git-worktrees)
- [Developer commands](https://learn.chatgpt.com/docs/developer-commands)
- [Non-interactive mode](https://learn.chatgpt.com/docs/non-interactive-mode)
