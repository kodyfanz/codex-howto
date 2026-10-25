"""Shared discovery, parsing, and rendering helpers for documentation tools."""

from __future__ import annotations

import html
import posixpath
import re
from dataclasses import dataclass
from collections.abc import Callable
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit

EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "build",
    "dist",
    "node_modules",
    "site",
}

CHAPTERS: tuple[tuple[str, str], ...] = (
    ("README.md", "Introduction"),
    ("LEARNING-ROADMAP.md", "Learning roadmap"),
    ("QUICK_REFERENCE.md", "Quick reference"),
    ("GLOSSARY.md", "Glossary"),
    ("01-getting-started/README.md", "Getting started"),
    ("02-agents-md/README.md", "Project instructions"),
    ("03-skills/README.md", "Skills"),
    ("04-subagents/README.md", "Subagents"),
    ("05-mcp/README.md", "MCP"),
    ("06-hooks/README.md", "Hooks"),
    ("07-plugins/README.md", "Plugins"),
    ("08-safety-and-worktrees/README.md", "Safety and worktrees"),
    ("09-advanced-workflows/README.md", "Advanced workflows"),
    ("10-cli-and-automation/README.md", "CLI and automation"),
    ("CATALOG.md", "Feature catalog"),
    ("INDEX.md", "Index"),
    ("STYLE_GUIDE.md", "Style guide"),
    ("CONTRIBUTING.md", "Contributing"),
    ("SECURITY.md", "Security"),
    ("CODE_OF_CONDUCT.md", "Code of conduct"),
    ("resources/README.md", "Resources"),
)

LINK_RE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")
IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
FENCE_RE = re.compile(r"^\s*```([^`]*)$")
CODE_TOKEN_RE = re.compile(
    r"(?P<comment>#[^\n]*|//[^\n]*|/\*[\s\S]*?\*/|<!--[\s\S]*?-->)"
    r"|(?P<string>'(?:\\.|[^'\\])*'|\"(?:\\.|[^\"\\])*\"|`(?:\\.|[^`\\])*`)"
    r"|(?P<number>\b(?:0x[\da-fA-F]+|\d+(?:\.\d+)?)\b)"
)
KEYWORDS = {
    "bash": {"case", "do", "done", "else", "esac", "fi", "for", "function", "if", "in", "then", "while"},
    "javascript": {"async", "await", "const", "else", "export", "function", "if", "import", "let", "new", "return", "throw", "try", "var"},
    "json": {"false", "null", "true"},
    "markdown": {"blockquote", "code", "heading", "link", "list"},
    "mermaid": {"flowchart", "graph", "subgraph"},
    "python": {"and", "class", "def", "elif", "else", "for", "from", "if", "import", "in", "is", "not", "or", "return", "try", "while", "with"},
    "shell": {"case", "do", "done", "else", "esac", "fi", "for", "function", "if", "in", "then", "while"},
    "toml": {"false", "true"},
    "typescript": {"async", "await", "const", "else", "export", "function", "if", "import", "interface", "let", "new", "return", "throw", "try", "type", "var"},
    "yaml": {"false", "null", "true"},
}


@dataclass(frozen=True)
class Page:
    """A source document and its stable output location."""

    source: Path
    relative: PurePosixPath
    title: str
    output: PurePosixPath


def is_excluded(path: Path, root: Path) -> bool:
    """Return whether a path belongs to generated, cached, or reference data."""
    try:
        relative = path.resolve().relative_to(root.resolve())
    except ValueError:
        return True
    return any(part in EXCLUDED_DIRS or part.startswith(".pytest_cache") for part in relative.parts)


def markdown_files(root: Path) -> list[Path]:
    """Find authored Markdown files, excluding generated and reference trees."""
    return sorted(path for path in root.rglob("*.md") if not is_excluded(path, root))


def output_path(relative: PurePosixPath, suffix: str = ".html") -> PurePosixPath:
    """Map README files to directory indexes and other Markdown to peer pages."""
    if relative == PurePosixPath("INDEX.md"):
        return PurePosixPath(f"complete-index{suffix}")
    if relative.name.lower() == "readme.md":
        return relative.parent / f"index{suffix}"
    return relative.with_suffix(suffix)


def title_from_markdown(content: str, fallback: str) -> str:
    """Read the first H1, stripping simple inline Markdown."""
    for line in content.splitlines():
        match = re.match(r"^#\s+(.+)$", line)
        if match:
            return re.sub(r"[`*_]", "", match.group(1)).strip()
    return fallback


def highlight_code(code: str, language: str) -> str:
    """Apply dependency-free syntax highlighting to common code fences."""
    normalized = language.lower().split("-")[0]
    keywords = KEYWORDS.get(normalized, set())

    def highlight_plain(value: str) -> str:
        escaped = html.escape(value)
        if not keywords:
            return escaped
        pattern = r"(?<![\w-])(" + "|".join(sorted(map(re.escape, keywords), key=len, reverse=True)) + r")(?![\w-])"
        return re.sub(pattern, r'<span class="syntax-keyword">\1</span>', escaped)

    output: list[str] = []
    cursor = 0
    for match in CODE_TOKEN_RE.finditer(code):
        output.append(highlight_plain(code[cursor:match.start()]))
        category = match.lastgroup or "string"
        output.append(f'<span class="syntax-{category}">{html.escape(match.group())}</span>')
        cursor = match.end()
    output.append(highlight_plain(code[cursor:]))
    return "".join(output)


def collect_pages(root: Path, suffix: str = ".html") -> list[Page]:
    """Collect the curated English publication in learning order."""
    pages: list[Page] = []
    missing: list[str] = []
    for relative_text, fallback in CHAPTERS:
        source = root / relative_text
        if not source.is_file():
            missing.append(relative_text)
            continue
        relative = PurePosixPath(relative_text)
        content = source.read_text(encoding="utf-8")
        pages.append(
            Page(source, relative, title_from_markdown(content, fallback), output_path(relative, suffix))
        )
    if missing:
        raise FileNotFoundError(f"Missing publication source files: {', '.join(missing)}")
    return pages


def collect_all_pages(root: Path, suffix: str = ".html") -> list[Page]:
    """Collect chapters, Markdown references, and copy-ready source listings."""
    pages = collect_pages(root, suffix)
    included = {page.source.resolve() for page in pages}
    for source in markdown_files(root):
        if source.resolve() in included:
            continue
        relative = PurePosixPath(source.relative_to(root).as_posix())
        content = source.read_text(encoding="utf-8")
        pages.append(
            Page(source, relative, title_from_markdown(content, source.stem), output_path(relative, suffix))
        )
    learning_roots = [
        path for path in root.iterdir()
        if path.is_dir() and (re.match(r"^\d{2}-", path.name) or path.name in {".agents", ".codex", ".github", "scripts"})
    ]
    support_files = [root / "LICENSE"]
    for learning_root in learning_roots:
        support_files.extend(
            path for path in learning_root.rglob("*")
            if path.is_file() and path.suffix.lower() != ".md" and "__pycache__" not in path.parts
        )
    for source in sorted({path.resolve() for path in support_files if path.is_file()}):
        if source in included:
            continue
        relative = PurePosixPath(source.relative_to(root).as_posix())
        pages.append(Page(source, relative, source.name, PurePosixPath(f"{relative}{suffix}")))
        included.add(source)
    support_source_paths = [page.source for page in pages if page.source.is_file()] + support_files
    support_directories = {
        parent
        for source in support_source_paths
        if source.is_file()
        for parent in source.parents
        if parent != root and root in parent.parents and not (parent / "README.md").is_file()
    }
    for source in sorted(support_directories):
        relative = PurePosixPath(source.relative_to(root).as_posix())
        pages.append(Page(source, relative, source.name, relative / f"index{suffix}"))
    return pages


def render_page(
    page: Page,
    page_map: dict[PurePosixPath, PurePosixPath],
    *,
    epub: bool = False,
    mermaid_callback: Callable[[str, int], str] | None = None,
) -> str:
    """Render Markdown, source files, or generated directory indexes."""
    if page.source.is_dir():
        links: list[str] = []
        for relative, destination in sorted(page_map.items(), key=lambda item: str(item[0])):
            if relative.parent != page.relative or relative == page.relative:
                continue
            href = relative_url(page.output, destination)
            links.append(f'<li><a href="{html.escape(href, quote=True)}">{html.escape(relative.name)}</a></li>')
        return f"<h1>{html.escape(page.title)}</h1><p>Files and subdirectories in this copy-ready example.</p><ul>{''.join(links)}</ul>"
    if page.source.suffix.lower() == ".md":
        return render_markdown(page.source.read_text(encoding="utf-8"), page.relative, page.output, page_map, epub=epub, mermaid_callback=mermaid_callback)
    content = page.source.read_text(encoding="utf-8")
    return f'<h1>{html.escape(page.title)}</h1><p>Copy-ready source file: <code>{html.escape(str(page.relative))}</code></p><pre><code>{html.escape(content)}</code></pre>'


def strip_inline_markup(text: str) -> str:
    """Remove common inline formatting for anchor generation."""
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"[`*_~]", "", text).strip()


def heading_to_anchor(heading: str) -> str:
    """Approximate GitHub's stable heading anchors for English documentation."""
    clean = strip_inline_markup(heading).lower()
    clean = re.sub(r"[^\w\- ]", "", clean, flags=re.UNICODE)
    clean = clean.replace(" ", "-")
    return re.sub(r"-+", "-", clean).strip("-")


def headings(content: str) -> set[str]:
    """Return anchors for headings outside fenced code blocks."""
    found: set[str] = set()
    counts: dict[str, int] = {}
    in_fence = False
    for line in content.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        match = HEADING_RE.match(line) if not in_fence else None
        if not match:
            continue
        base = heading_to_anchor(match.group(2))
        count = counts.get(base, 0)
        counts[base] = count + 1
        found.add(base if count == 0 else f"{base}-{count}")
    return found


def split_link_target(raw: str) -> tuple[str, str]:
    """Split a Markdown link target from its fragment and optional title."""
    raw = raw.strip()
    if raw.startswith("<") and ">" in raw:
        raw = raw[1 : raw.index(">")]
    else:
        raw = re.split(r"\s+[\"']", raw, maxsplit=1)[0]
    parts = urlsplit(raw)
    return unquote(parts.path), unquote(parts.fragment)


def relative_url(from_output: PurePosixPath, to_output: PurePosixPath) -> str:
    """Build a POSIX relative URL between generated pages."""
    return posixpath.relpath(str(to_output), str(from_output.parent))


def rewrite_target(
    raw: str,
    source: PurePosixPath,
    current_output: PurePosixPath,
    page_map: dict[PurePosixPath, PurePosixPath],
) -> str:
    """Rewrite a local Markdown target to its publication URL."""
    path_text, fragment = split_link_target(raw)
    if not path_text:
        return f"#{fragment}" if fragment else raw
    if re.match(r"^[a-z][a-z0-9+.-]*:", path_text, re.I) or path_text.startswith("//"):
        return raw
    resolved = PurePosixPath(posixpath.normpath(str(source.parent / path_text)))
    candidates = [resolved]
    if not resolved.suffix:
        candidates.append(resolved / "README.md")
    target_output = next((page_map[item] for item in candidates if item in page_map), None)
    if target_output is None:
        return raw
    rewritten = relative_url(current_output, target_output)
    return f"{rewritten}#{fragment}" if fragment else rewritten


def _inline(
    text: str,
    source: PurePosixPath,
    current_output: PurePosixPath,
    page_map: dict[PurePosixPath, PurePosixPath],
) -> str:
    """Render the small inline-Markdown subset used by the guide."""
    tokens: list[str] = []

    def keep(value: str) -> str:
        tokens.append(value)
        return f"\x00{len(tokens) - 1}\x00"

    def code_sub(match: re.Match[str]) -> str:
        value = match.group(1) if match.group(1) is not None else match.group(2)
        return keep(f"<code>{html.escape(value)}</code>")

    text = re.sub(r"``\s?(.*?)\s?``|`([^`]+)`", code_sub, text)
    escaped = html.escape(text, quote=False)

    def image_sub(match: re.Match[str]) -> str:
        alt, raw = match.groups()
        target = rewrite_target(html.unescape(raw), source, current_output, page_map)
        return keep(f'<img src="{html.escape(target, quote=True)}" alt="{html.escape(html.unescape(alt), quote=True)}">')

    def link_sub(match: re.Match[str]) -> str:
        label, raw = match.groups()
        target = rewrite_target(html.unescape(raw), source, current_output, page_map)
        return keep(f'<a href="{html.escape(target, quote=True)}">{html.unescape(label)}</a>')

    escaped = IMAGE_RE.sub(image_sub, escaped)
    escaped = LINK_RE.sub(link_sub, escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", escaped)
    escaped = re.sub(r"~~([^~]+)~~", r"<del>\1</del>", escaped)
    for index in range(len(tokens) - 1, -1, -1):
        escaped = escaped.replace(f"\x00{index}\x00", tokens[index])
    return escaped


def render_markdown(
    content: str,
    source: PurePosixPath,
    current_output: PurePosixPath,
    page_map: dict[PurePosixPath, PurePosixPath],
    *,
    epub: bool = False,
    mermaid_callback: Callable[[str, int], str] | None = None,
) -> str:
    """Render the guide's Markdown subset without third-party dependencies."""
    lines = content.splitlines()
    output: list[str] = []
    paragraph: list[str] = []
    list_kind: str | None = None
    in_code = False
    code_language = ""
    code_lines: list[str] = []
    index = 0

    def close_list() -> None:
        nonlocal list_kind
        if list_kind:
            output.append(f"</{list_kind}>")
            list_kind = None

    def flush_paragraph() -> None:
        if paragraph:
            output.append(f"<p>{_inline(' '.join(item.strip() for item in paragraph), source, current_output, page_map)}</p>")
            paragraph.clear()

    while index < len(lines):
        line = lines[index]
        fence = FENCE_RE.match(line)
        if fence:
            flush_paragraph()
            close_list()
            if not in_code:
                in_code = True
                code_language = fence.group(1).strip().split()[0] if fence.group(1).strip() else "text"
                code_lines = []
            else:
                escaped = highlight_code("\n".join(code_lines), code_language)
                language = html.escape(code_language, quote=True)
                copy_button = "" if epub else '<button class="copy-code" type="button" aria-label="Copy code"><span class="copy-icon" aria-hidden="true"><svg viewBox="0 0 24 24" focusable="false"><path d="M9 8V5.5A1.5 1.5 0 0 1 10.5 4h8A1.5 1.5 0 0 1 20 5.5v8a1.5 1.5 0 0 1-1.5 1.5H16M5.5 8h8A1.5 1.5 0 0 1 15 9.5v9A1.5 1.5 0 0 1 13.5 20h-8A1.5 1.5 0 0 1 4 18.5v-9A1.5 1.5 0 0 1 5.5 8Z"/></svg></span><span class="sr-only">Copy code</span></button>'
                if code_language == "mermaid" and mermaid_callback is not None:
                    diagram_href = html.escape(mermaid_callback("\n".join(code_lines), index), quote=True)
                    image = f'<img src="{diagram_href}" alt="Mermaid flowchart" />' if epub else f'<img src="{diagram_href}" alt="Mermaid flowchart">'
                    output.append(f'<figure class="mermaid-diagram">{image}<figcaption>Rendered Mermaid diagram</figcaption><details><summary>Mermaid source</summary><pre class="language-mermaid" data-language="mermaid">{copy_button}<code>{escaped}</code></pre></details></figure>')
                else:
                    css_class = "mermaid" if code_language == "mermaid" else f"language-{language}"
                    output.append(f'<pre class="{css_class}" data-language="{language}">{copy_button}<code>{escaped}</code></pre>')
                in_code = False
            index += 1
            continue
        if in_code:
            code_lines.append(line)
            index += 1
            continue
        if line.strip().startswith("<!--") and line.strip().endswith("-->"):
            flush_paragraph()
            close_list()
            index += 1
            continue
        heading = HEADING_RE.match(line)
        if heading:
            flush_paragraph()
            close_list()
            level = len(heading.group(1))
            label = heading.group(2)
            output.append(f'<h{level} id="{heading_to_anchor(label)}">{_inline(label, source, current_output, page_map)}</h{level}>')
            index += 1
            continue
        if line.strip().startswith("|") and index + 1 < len(lines) and re.match(r"^\s*\|[\s:|\-]+\|\s*$", lines[index + 1]):
            flush_paragraph()
            close_list()
            rows: list[list[str]] = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                rows.append([cell.strip() for cell in re.split(r"(?<!\\)\|", lines[index].strip().strip("|"))])
                index += 1
            header, body = rows[0], rows[2:]
            output.append("<div class=\"table-wrap\"><table><thead><tr>" + "".join(f"<th>{_inline(cell, source, current_output, page_map)}</th>" for cell in header) + "</tr></thead><tbody>")
            for row in body:
                cells = [cell.replace("\\|", "|") for cell in row]
                output.append("<tr>" + "".join(f"<td>{_inline(cell, source, current_output, page_map)}</td>" for cell in cells) + "</tr>")
            output.append("</tbody></table></div>")
            continue
        item = re.match(r"^\s*[-*+]\s+(.+)$", line)
        numbered = re.match(r"^\s*\d+\.\s+(.+)$", line)
        if item or numbered:
            flush_paragraph()
            wanted = "ul" if item else "ol"
            if list_kind != wanted:
                close_list()
                output.append(f"<{wanted}>")
                list_kind = wanted
            value = (item or numbered).group(1)  # type: ignore[union-attr]
            output.append(f"<li>{_inline(value, source, current_output, page_map)}</li>")
            index += 1
            continue
        quote = re.match(r"^>\s?(.*)$", line)
        if quote:
            flush_paragraph()
            close_list()
            quote_lines: list[str] = []
            while index < len(lines):
                quoted = re.match(r"^>\s?(.*)$", lines[index])
                if not quoted:
                    break
                quote_lines.append(quoted.group(1))
                index += 1
            output.append(f"<blockquote><p>{_inline(' '.join(quote_lines), source, current_output, page_map)}</p></blockquote>")
            continue
        if re.match(r"^\s*([-*_])(?:\s*\1){2,}\s*$", line):
            flush_paragraph()
            close_list()
            output.append("<hr>")
            index += 1
            continue
        if not line.strip():
            flush_paragraph()
            close_list()
        elif line.startswith("<picture") or line.startswith("</picture") or line.lstrip().startswith(("<source", "<img")):
            flush_paragraph()
            close_list()
            if not epub:
                raw_lines = [line.strip()]
                while not raw_lines[-1].endswith(">") and index + 1 < len(lines):
                    index += 1
                    raw_lines.append(lines[index].strip())
                output.append("\n".join(raw_lines))
        else:
            paragraph.append(line)
        index += 1
    flush_paragraph()
    close_list()
    if in_code:
        raise ValueError(f"Unclosed code fence in {source}")
    rendered = "\n".join(output)
    if epub:
        def close_img(match: re.Match[str]) -> str:
            attributes = match.group(1).strip().rstrip("/").rstrip()
            return f"<img {attributes} />"

        rendered = re.sub(r"<img\s+([^>]*?)\s*/?>", close_img, rendered)
        rendered = rendered.replace("<hr>", "<hr />")
    return rendered
