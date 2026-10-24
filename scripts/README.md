# Release tooling

The release toolchain uses only Python 3.10+ and its standard library. It is
English-only, works offline by default, and packages only authored project
content plus generated release outputs.

## Commands

| Command | Purpose | Output |
|---|---|---|
| `python3 scripts/check_markdown.py` | Check fences, tables, and whitespace | Console report |
| `python3 scripts/check_cross_references.py` | Check local files and anchors | Console report |
| `python3 scripts/check_mermaid.py` | Check Mermaid block structure offline | Console report |
| `python3 scripts/check_links.py` | Check internal links | Console report |
| `python3 scripts/check_links.py --external` | Probe HTTP links; requires network access | Console report |
| `python3 scripts/build_website.py` | Build the responsive static guide | `site/` |
| `python3 scripts/build_epub.py` | Build and validate EPUB 3 | `dist/codex-howto.epub` |
| `python3 scripts/build_release.py` | Package source, website, and EPUB | `dist/codex-howto-release.zip` |
| `python3 scripts/quality_gate.py` | Run all offline checks, tests, and builds | All release artifacts |

## Publication rules

- Markdown remains the source of truth.
- The curated navigation follows the learning order in `doc_utils.py`.
- Linked skills, plugin files, configurations, and scripts become readable
  source-listing pages in the website and EPUB.
- Generated outputs never include caches, coverage data, operating-system
  metadata, or nested build directories.
- Mermaid validation is structural and offline. The guide's current flowchart
  subset is rendered to local SVG with no CDN or runtime network dependency;
  every diagram also preserves its Mermaid source as an accessible fallback.

The external link check is intentionally separate from the offline quality gate
because network availability and remote rate limits are nondeterministic.
