# Security policy

Codex How To is an educational documentation project, but its scripts, configuration examples, plugins, hooks, and integrations can still create real security risk when copied into another environment.

## Supported content

Security fixes target the current default branch. Older snapshots of the guide are not maintained as separate supported releases during the build phase.

## Report privately

Do not open a public issue for a vulnerability that could expose credentials, execute unintended commands, bypass an approval boundary, or compromise users who copy an example.

Use the repository host's private vulnerability-reporting feature when it is available. Otherwise, contact the maintainers through a private channel listed in the repository profile. Do not include live secrets in the report.

## Useful report contents

- Affected file and section.
- Impact and required preconditions.
- Minimal reproduction in a disposable environment.
- Whether the issue affects CLI, IDE, desktop app, cloud, or ChatGPT Work.
- A proposed mitigation, if known.

## Security standards for examples

- Never commit real credentials or account identifiers.
- Read secrets from documented environment variables or approved secret stores.
- Use least-privilege permissions and narrowly scoped external actions.
- Explain sandbox, approval, and external-system permissions independently.
- Validate destructive targets before deletion or overwrite.
- Treat hooks, MCP servers, plugins, and downloaded scripts as executable code.
- Pin or verify third-party dependencies when reproducibility or integrity depends on them.
- Make logs safe for environments where prompts or command output may contain sensitive information.

## Non-security issues

Broken links, outdated screenshots, ordinary documentation errors, and examples that fail without creating a security impact can be reported publicly.
