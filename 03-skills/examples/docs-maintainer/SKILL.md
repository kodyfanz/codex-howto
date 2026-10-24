---
name: docs-maintainer
description: Update repository documentation to match verified code, configuration, and commands. Use for README, guides, references, and documentation maintenance. Do not invent unsupported behavior or change product code unless requested.
---

# Documentation maintainer

1. Identify the audience, affected document, and source of truth in the
   repository.
2. Confirm commands, paths, options, and behavior from code or configuration.
3. Make the smallest coherent update and preserve existing voice and structure.
4. Use relative links for repository content and declare code-fence languages.
5. Run the repository's documentation checks. If none exist, verify changed
   links, headings, and examples manually.
6. Report the evidence used and any claim that remains uncertain.

Do not copy secrets, local absolute paths, generated artifacts, or unsupported
future behavior into documentation. Do not commit or publish unless asked.
