#!/usr/bin/env python3
"""Build the English Codex How To static site with Python's standard library."""

from __future__ import annotations

import argparse
import hashlib
import html
import posixpath
import shutil
import sys
from pathlib import Path, PurePosixPath

from doc_utils import CHAPTERS, Page, collect_all_pages, relative_url, render_page
from mermaid_renderer import render_svg


def render_navigation(current: Page, pages: list[Page]) -> str:
    curated = pages[: len(CHAPTERS)]
    links: list[str] = []
    for page in curated:
        href = relative_url(current.output, page.output)
        active = ' aria-current="page"' if page.relative == current.relative else ""
        links.append(f'<a href="{html.escape(href, quote=True)}"{active}>{html.escape(page.title)}</a>')
    return "\n".join(links)


def render_pager(current: Page, pages: list[Page]) -> str:
    curated = pages[: len(CHAPTERS)]
    if current not in curated:
        return f'<a href="{relative_url(current.output, PurePosixPath("index.html"))}">Back to the guide</a>'
    index = curated.index(current)
    items: list[str] = []
    if index:
        previous = curated[index - 1]
        items.append(f'<a href="{relative_url(current.output, previous.output)}">← {html.escape(previous.title)}</a>')
    if index + 1 < len(curated):
        following = curated[index + 1]
        items.append(f'<a class="next" href="{relative_url(current.output, following.output)}">{html.escape(following.title)} →</a>')
    return "\n".join(items)


def safe_output(root: Path, output: Path) -> None:
    output = output.resolve()
    if output in {root.resolve(), root.resolve().parent, Path("/")}:
        raise ValueError("Output must be a dedicated child directory")


def build_website(root: Path, output: Path) -> Path:
    root = root.resolve()
    output = output.resolve()
    safe_output(root, output)
    pages = collect_all_pages(root)
    page_map = {page.relative: page.output for page in pages}
    template_dir = Path(__file__).parent / "website_templates"
    template = (template_dir / "page.html").read_text(encoding="utf-8")
    css_path = template_dir / "site.css"
    js_path = template_dir / "site.js"
    css_hash = hashlib.sha256(css_path.read_bytes()).hexdigest()[:12]
    js_hash = hashlib.sha256(js_path.read_bytes()).hexdigest()[:12]
    if output.exists():
        shutil.rmtree(output)
    (output / "assets").mkdir(parents=True)
    shutil.copy2(css_path, output / "assets/site.css")
    shutil.copy2(js_path, output / "assets/site.js")
    shutil.copytree(root / "resources/logos", output / "resources/logos")
    (output / "assets/mermaid").mkdir(parents=True, exist_ok=True)

    curated_count = len(CHAPTERS)
    for index, page in enumerate(pages):
        def mermaid_callback(source: str, block_index: int, *, page: Page = page) -> str:
            digest = hashlib.sha256(f"{page.relative}:{block_index}:{source}".encode("utf-8")).hexdigest()[:16]
            filename = f"{digest}.svg"
            asset = output / "assets/mermaid" / filename
            if not asset.exists():
                asset.write_text(render_svg(source, f"{page.title} diagram {block_index + 1}"), encoding="utf-8")
            return relative_url(page.output, PurePosixPath(f"assets/mermaid/{filename}"))

        body = render_page(page, page_map, mermaid_callback=mermaid_callback)
        asset_prefix = posixpath.relpath(".", str(page.output.parent))
        asset_prefix = "" if asset_prefix == "." else f"{asset_prefix}/"
        document = template
        replacements = {
            "{{TITLE}}": html.escape(page.title),
            "{{ASSET_PREFIX}}": asset_prefix,
            "{{CSS_URL}}": f"{asset_prefix}assets/site.css?v={css_hash}",
            "{{JS_URL}}": f"{asset_prefix}assets/site.js?v={js_hash}",
            "{{HOME_URL}}": relative_url(page.output, PurePosixPath("index.html")),
            "{{NAVIGATION}}": render_navigation(page, pages),
            "{{PAGE_CLASS}}": "home" if page.relative == PurePosixPath("README.md") else "",
            "{{SECTION}}": "Codex How To",
            "{{POSITION}}": f"Lesson {index + 1} of {curated_count}" if index < curated_count else "Reference",
            "{{CONTENT}}": body,
            "{{PAGER}}": render_pager(page, pages),
        }
        for marker, value in replacements.items():
            document = document.replace(marker, value)
        destination = output / str(page.output)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(document, encoding="utf-8")

    (output / ".nojekyll").write_text("", encoding="utf-8")
    print(f"Website built: {len(pages)} pages at {output}")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = (args.output or root / "site").resolve()
    try:
        build_website(root, output)
    except (OSError, ValueError) as exc:
        print(f"Website build failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
