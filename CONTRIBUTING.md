# Contributing to Codex How To

Contributions should make Codex easier to learn through precise explanations, tested examples, and safe workflows.

The canonical source repository is [github.com/kodyfanz/codex-howto](https://github.com/kodyfanz/codex-howto). Use it to review the project, open issues, and submit pull requests.

## Good contributions

- Complete or improve a lesson in an existing module.
- Add a small copy-ready example with verification steps.
- Correct a product claim using official OpenAI documentation.
- Improve accessibility, diagrams, navigation, or troubleshooting.
- Port or strengthen documentation validation tooling.

## Before you begin

1. Read [AGENTS.md](AGENTS.md) and the [style guide](STYLE_GUIDE.md).
2. Read the repository status in [README.md](README.md) and run the
   [release quality gate](scripts/README.md) before proposing changes.
3. Keep the numbered curriculum order intact.
4. Confirm that your change is written in English.

## Authoring workflow

1. Create a focused branch.
2. Make the smallest coherent documentation change.
3. Verify commands on the product surface named in the lesson.
4. Check links, Markdown, diagrams, and example paths.
5. Review the diff for credentials, personal paths, and unsupported claims.
6. Open a pull request describing what was verified and where.

## Product claims

- Use official OpenAI documentation as the primary source.
- Distinguish CLI, IDE, desktop app, cloud, and ChatGPT Work behavior.
- State when availability depends on account, workspace policy, operating system, or staged rollout.
- Do not infer current behavior from generated site or EPUB artifacts; verify it against official OpenAI documentation.

## Pull request checklist

- [ ] The change belongs in the selected module.
- [ ] All content is in English.
- [ ] New commands and configuration were tested.
- [ ] Internal and official links resolve.
- [ ] Examples contain no secrets or user-specific paths.
- [ ] Destructive or externally mutating commands have explicit warnings.
- [ ] Navigation documents were updated when structure changed.

## Conduct and security

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). Report security-sensitive issues according to the [Security Policy](SECURITY.md), not in a public issue.
