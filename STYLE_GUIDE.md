# Style guide

Use these conventions to keep Codex How To consistent, testable, and easy to navigate.

## Language

- Write all repository content in English.
- Use plain language and define a product term on first use.
- Prefer active voice and direct instructions.
- Do not create translated documentation trees.

## File and directory names

- Use two-digit numbered prefixes for curriculum modules.
- Use lowercase kebab-case for ordinary files and directories.
- Use conventional uppercase names for root project documents.
- Use canonical Codex paths exactly, including `.agents`, `.codex`, and `.codex-plugin`.

## Lesson structure

Completed module READMEs should follow this order:

1. Title and one-paragraph outcome.
2. Surface and availability note.
3. Learning objectives.
4. Architecture or mental model when it adds clarity.
5. Concepts in dependency order.
6. Copy-ready examples.
7. Hands-on exercise.
8. Verification steps.
9. Security considerations.
10. Troubleshooting.
11. Related modules and official resources.

## Headings and prose

- Use one level-one heading per document.
- Do not skip heading levels.
- Keep paragraphs short and lead with the important point.
- Use **Note**, **Tip**, **Important**, and **Warning** callouts sparingly.
- Do not describe account-dependent availability as universal.

## Code blocks

- Always declare a language on fenced code blocks.
- Make examples safe by default.
- Use placeholders such as `YOUR_TOKEN` only when an environment variable example is not clearer.
- Never include real credentials, personal paths, or account identifiers.
- Explain commands that change external state.
- Include expected output or a verification command when practical.

## Product surfaces

Label instructions when behavior is specific to:

- Codex CLI
- Codex IDE extension
- Codex desktop app
- Codex cloud execution
- ChatGPT Work

Do not combine instructions from different surfaces into a single unlabeled procedure.

## Links and sources

- Use relative links for repository content.
- Link product claims to official OpenAI documentation.
- Prefer stable topic pages over release notes for durable behavior.
- Mark experimental or deprecated features directly beside the claim.
- Do not cite the local source project as authority for Codex behavior.

## Mermaid diagrams

- Use diagrams only when they make sequence, ownership, hierarchy, or branching materially clearer.
- Keep labels short and avoid embedding large code fragments.
- Declare Mermaid fences with `mermaid`.
- Validate diagrams before merging.

## Examples and templates

- State the use case, prerequisites, and authority required.
- Keep one primary concept per example.
- Provide a safe failure or rollback path where state changes.
- Verify copied examples on the documented surface.
- Avoid model names unless the lesson specifically teaches model selection.

## Commit messages

When commits are requested, use `type(scope): subject`. Prefer the module directory as the scope, for example `docs(skills): add invocation exercise`.

## Author checklist

- [ ] Content is English-only.
- [ ] Product surface and availability are explicit.
- [ ] Commands and configuration were verified.
- [ ] Code fences declare a language.
- [ ] Examples contain no secrets or personal paths.
- [ ] Internal links resolve.
- [ ] Official links support the associated claims.
- [ ] The lesson contains an observable verification step.
