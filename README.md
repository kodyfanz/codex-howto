# Learn Codex through practical repository work

<!-- markdownlint-disable MD033 -->
<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="resources/logos/codex-howto-logo-dark.svg"
  >
  <img alt="Codex How To" src="resources/logos/codex-howto-logo.svg">
</picture>
<!-- markdownlint-enable MD033 -->

If you are new to Codex, start with one small repository task in Module 1. You do not need an assessment or all ten modules to get useful work done. The later modules cover specialized capabilities to explore when your work calls for them.

> **Project status**: The authored curriculum, examples, validation tooling, website, EPUB, and release archive pass the offline quality gate. That gate checks repository content and generated outputs; it does not guarantee that Codex product behavior on linked external pages has not changed.

## Why this guide exists

Official documentation is the source of truth for product behavior. This guide adds a progressive learning path, worked examples, reusable templates, and verification steps that show how Codex capabilities fit together.

| Official OpenAI documentation | Codex How To                        |
| ----------------------------- | ----------------------------------- |
| Product reference             | Guided curriculum                   |
| Individual feature details    | End-to-end workflows                |
| Canonical configuration       | Copy-ready learning examples        |
| Broad platform coverage       | Sequenced exercises and checkpoints |

## Start here

**New to Codex?** Start with [Module 1: Getting started](01-getting-started/README.md).
You can complete its first exercise without taking an assessment.

**Already use Codex?** The optional [`$self-assessment`](.agents/skills/self-assessment/SKILL.md) skill can suggest a path when your Codex surface has loaded repository skills. Otherwise, use the [learning roadmap](LEARNING-ROADMAP.md) to choose a module.

If you want to jump to a topic, choose from the options below:

| Experience                   | Recommended entry point                | Goal                                  |
| ---------------------------- | -------------------------------------- | ------------------------------------- |
| Comfortable with basic tasks | [Project instructions](02-agents-md/README.md)  | Make repository guidance durable      |
| Building reusable workflows  | [Skills](03-skills/README.md)                   | Package repeatable expertise          |
| Coordinating complex work    | [Subagents](04-subagents/README.md)             | Delegate bounded work effectively     |
| Integrating external systems | [MCP](05-mcp/README.md)                         | Connect tools and live context safely |

See the [learning roadmap](LEARNING-ROADMAP.md) for the complete sequence and the [feature catalog](CATALOG.md) for a capability-first view. Use the [glossary](GLOSSARY.md) whenever a Codex or AI term is unfamiliar.

Modules 1–2 cover first tasks and durable repository instructions. Modules 3–10 are specialized topics; choose them as needed. Complete all ten only if you want the full curriculum.

## Curriculum

| Module | Topic                                            | Primary outcome                               |
| -----: | ------------------------------------------------ | --------------------------------------------- |
|      1 | [Getting started](01-getting-started/README.md)           | Choose a surface and complete a verified task |
|      2 | [Project instructions](02-agents-md/README.md)            | Create effective `AGENTS.md` guidance         |
|      3 | [Skills](03-skills/README.md)                             | Build a reusable project skill                |
|      4 | [Subagents](04-subagents/README.md)                       | Coordinate specialized parallel work          |
|      5 | [MCP](05-mcp/README.md)                                   | Configure an external context or tool server  |
|      6 | [Hooks](06-hooks/README.md)                               | Add deterministic lifecycle automation        |
|      7 | [Plugins](07-plugins/README.md)                           | Package and distribute a complete workflow    |
|      8 | [Safety and worktrees](08-safety-and-worktrees/README.md) | Isolate work and control permissions          |
|      9 | [Advanced workflows](09-advanced-workflows/README.md)     | Orchestrate long-running and scheduled work   |
|     10 | [CLI and automation](10-cli-and-automation/README.md)     | Use `codex exec`, scripts, and CI safely      |

## How to use the guide

1. Start at the module that matches your current experience.
2. Read the concept and surface notes before copying a configuration.
3. Complete the exercise in a disposable or version-controlled project.
4. Run the listed verification step.
5. Continue only after you can explain what authority the example gives Codex.

## Repository map

```text
codex-howto/
├── 01-getting-started/       # First task and product surfaces
├── 02-agents-md/             # Durable repository instructions
├── 03-skills/                # Reusable workflows
├── 04-subagents/             # Delegation and custom agents
├── 05-mcp/                   # External tools and context
├── 06-hooks/                 # Lifecycle automation
├── 07-plugins/               # Packaging and distribution
├── 08-safety-and-worktrees/  # Permissions and isolation
├── 09-advanced-workflows/    # Planning and long-running work
├── 10-cli-and-automation/    # Non-interactive and CI usage
├── .agents/skills/           # Optional assessment and lesson-quiz skills
├── docs/                     # Project plans and supporting documents
├── scripts/                  # Offline validation and release tooling
└── resources/                # Visual assets and reusable resources
```

The repository is standalone: authored Markdown and examples are the curriculum source, while `site/` and `dist/` are generated release artifacts.

## Documentation principles

- English is the only documentation language in the current project scope.
- Product claims are checked against official OpenAI documentation.
- Every feature is labeled by the surface where it applies.
- Examples are safe by default and contain no real credentials.
- Copy-ready examples include a way to verify the outcome.
- Deprecated compatibility paths are not presented as recommended architecture.

## Project references

- [Complete index](INDEX.md)
- [Learning roadmap](LEARNING-ROADMAP.md)
- [Feature catalog](CATALOG.md)
- [Quick reference](QUICK_REFERENCE.md)
- [Style guide](STYLE_GUIDE.md)
- [Contributing](CONTRIBUTING.md)
- [Asset and licensing inventory](docs/ASSET_LICENSES.md)
- [Release tooling](scripts/README.md)
- [Project task register](PROJECT_TASKS.md)

## Included learning skills

- `$self-assessment` — optionally identify demonstrated experience and prioritize modules.
- `$lesson-quiz` — optionally quiz yourself on a completed module. The current question bank covers modules 1 through 10.

These skills are extras for Codex surfaces that load skills from this repository. If a skill is unavailable, follow the roadmap or module exercises directly.

## Build and validate

The release toolchain requires only Python 3.10 or newer:

```bash
python3 scripts/quality_gate.py
```

It validates Markdown, internal links, cross-references, Mermaid blocks, structured examples, skills, plugins, and tests before building:

- `site/` — responsive, offline-friendly static website.
- `dist/codex-howto.epub` — validated EPUB 3 guide.
- `dist/codex-howto-release.zip` — source, website, and EPUB without generated caches or unrelated working files.

See [release tooling](scripts/README.md) and the [asset and licensing inventory](docs/ASSET_LICENSES.md) for details.

## License

This project is available under the [MIT License](LICENSE).
