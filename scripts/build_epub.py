#!/usr/bin/env python3
"""Build a self-contained EPUB 3 edition of the English Codex How To guide."""

from __future__ import annotations

import argparse
import hashlib
import html
import posixpath
import sys
import uuid
import zipfile
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from xml.etree import ElementTree

from doc_utils import CHAPTERS, Page, collect_all_pages, render_page
from mermaid_renderer import render_svg

BOOK_CSS = """
body { color: #17211c; font-family: sans-serif; line-height: 1.55; margin: 5%; }
h1, h2, h3, h4 { color: #075c4b; line-height: 1.2; }
h1 { font-size: 2.2em; } h2 { border-top: 1px solid #c9d5cf; padding-top: .6em; }
a { color: #075c4b; } img { max-width: 100%; height: auto; }
code { font-family: monospace; color: #075c4b; background: #e8f1ed; border: 1px solid #c9d5cf; border-radius: .2em; padding: .08em .25em; }
pre { background: #12221d; color: #e6f3ed; border: 1px solid #2e6b5b; border-radius: .35em; padding: 2.2em 1em 1em; white-space: pre-wrap; }
pre::before { content: attr(data-language); display: block; margin: -1.6em -0.5em .8em; padding: .35em .5em; color: #9fe3cb; border-bottom: 1px solid #2e6b5b; font: bold .7em sans-serif; letter-spacing: .08em; text-transform: uppercase; }
pre code { background: transparent; border: 0; padding: 0; color: inherit; }
.syntax-comment { color: #91a89d; font-style: italic; }
.syntax-string { color: #f4c27a; }
.syntax-number { color: #9ed8ff; }
.syntax-keyword { color: #85d7c0; font-weight: bold; }
.syntax-heading { color: #85d7c0; font-weight: bold; font-style: normal; }
blockquote { background: #eaf3ef; border-left: .25em solid #16836d; margin-left: 0; padding: .7em 1em .7em 1.25em; }
table { border-collapse: collapse; width: 100%; font-size: .9em; }
th, td { border: 1px solid #aab8b1; padding: .4em; text-align: left; vertical-align: top; }
th { background: #d8ebe4; } .table-wrap { overflow-x: auto; }
.cover { text-align: center; padding-top: 15%; } .cover img { width: 85%; }
.mermaid-diagram { background: #eaf3ef; border: 1px solid #aab8b1; padding: 1em; }
.mermaid-diagram img { display: block; width: 100%; height: auto; }
.mermaid-diagram figcaption { color: #607068; font-size: .8em; margin-top: .5em; }
.mermaid-diagram details { margin-top: .7em; }
""".strip()


def xhtml_document(title: str, body: str, css_href: str) -> str:
    return f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en">
<head><meta charset="utf-8"/><title>{html.escape(title)}</title><link rel="stylesheet" type="text/css" href="{html.escape(css_href, quote=True)}"/></head>
<body>{body}</body>
</html>'''


def write_entry(archive: zipfile.ZipFile, name: str, data: str | bytes, *, stored: bool = False) -> None:
    info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_STORED if stored else zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, data.encode("utf-8") if isinstance(data, str) else data)


def manifest_id(index: int) -> str:
    return f"page-{index:03d}"


def build_nav(pages: list[Page]) -> str:
    items = []
    for page in pages[: len(CHAPTERS)]:
        href = f"text/{page.output}"
        items.append(f'<li><a href="{html.escape(href, quote=True)}">{html.escape(page.title)}</a></li>')
    return xhtml_document(
        "Contents",
        '<nav epub:type="toc" id="toc" xmlns:epub="http://www.idpf.org/2007/ops"><h1>Contents</h1><ol>' + "".join(items) + "</ol></nav>",
        "styles/book.css",
    )


def build_ncx(pages: list[Page], identifier: str) -> str:
    points = []
    for index, page in enumerate(pages[: len(CHAPTERS)], 1):
        points.append(
            f'<navPoint id="nav-{index}" playOrder="{index}"><navLabel><text>{html.escape(page.title)}</text></navLabel><content src="text/{html.escape(str(page.output), quote=True)}"/></navPoint>'
        )
    return f'''<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1"><head><meta name="dtb:uid" content="{identifier}"/></head><docTitle><text>Codex How To</text></docTitle><navMap>{''.join(points)}</navMap></ncx>'''


def build_package(pages: list[Page], identifier: str, modified: str, diagram_assets: list[str]) -> str:
    manifest = [
        '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
        '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
        '<item id="css" href="styles/book.css" media-type="text/css"/>',
        '<item id="cover" href="cover.xhtml" media-type="application/xhtml+xml"/>',
        '<item id="logo-light" href="text/resources/logos/codex-howto-logo.svg" media-type="image/svg+xml" properties="cover-image"/>',
        '<item id="logo-dark" href="text/resources/logos/codex-howto-logo-dark.svg" media-type="image/svg+xml"/>',
    ]
    spine = ['<itemref idref="cover"/>']
    for index, page in enumerate(pages):
        manifest.append(f'<item id="{manifest_id(index)}" href="text/{html.escape(str(page.output), quote=True)}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="{manifest_id(index)}"/>')
    for index, href in enumerate(diagram_assets):
        manifest.append(f'<item id="diagram-{index:03d}" href="{html.escape(href, quote=True)}" media-type="image/svg+xml"/>')
    return f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="book-id" xml:lang="en">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/"><dc:identifier id="book-id">{identifier}</dc:identifier><dc:title>Codex How To</dc:title><dc:language>en</dc:language><dc:creator>Codex How To contributors</dc:creator><dc:rights>MIT License</dc:rights><meta property="dcterms:modified">{modified}</meta></metadata>
<manifest>{''.join(manifest)}</manifest><spine toc="ncx">{''.join(spine)}</spine>
</package>'''


def validate_epub(path: Path, expected_pages: int) -> None:
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        if not names or names[0] != "mimetype":
            raise ValueError("mimetype must be the first EPUB entry")
        if archive.read("mimetype") != b"application/epub+zip":
            raise ValueError("invalid EPUB mimetype")
        if archive.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            raise ValueError("EPUB mimetype must be uncompressed")
        if archive.testzip() is not None:
            raise ValueError("EPUB contains a corrupt ZIP entry")
        xhtml_names = [name for name in names if name.endswith(".xhtml")]
        if len(xhtml_names) != expected_pages + 2:
            raise ValueError("EPUB page count is incomplete")
        for name in ["META-INF/container.xml", "OEBPS/content.opf", "OEBPS/nav.xhtml", *xhtml_names]:
            ElementTree.fromstring(archive.read(name))


def build_epub(root: Path, output: Path) -> Path:
    root = root.resolve()
    output = output.resolve()
    pages = collect_all_pages(root, ".xhtml")
    page_map = {page.relative: page.output for page in pages}
    output.parent.mkdir(parents=True, exist_ok=True)
    identifier = f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, 'https://codex-howto.local/english')}"
    modified = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    diagram_assets: dict[str, bytes] = {}
    rendered_pages: list[tuple[Page, str, str]] = []
    for page in pages:
        stored_page = PurePosixPath("text") / page.output

        def mermaid_callback(source: str, block_index: int, *, page: Page = page, stored_page: PurePosixPath = stored_page) -> str:
            digest = hashlib.sha256(f"{page.relative}:{block_index}:{source}".encode("utf-8")).hexdigest()[:16]
            archive_path = f"mermaid/{digest}.svg"
            diagram_assets.setdefault(archive_path, render_svg(source, f"{page.title} diagram {block_index + 1}").encode("utf-8"))
            return posixpath.relpath(archive_path, str(stored_page.parent))

        body = render_page(page, page_map, epub=True, mermaid_callback=mermaid_callback)
        css_href = posixpath.relpath("styles/book.css", str(stored_page.parent))
        rendered_pages.append((page, body, css_href))
    container = '''<?xml version="1.0" encoding="utf-8"?>
<container xmlns="urn:oasis:names:tc:opendocument:xmlns:container" version="1.0"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>'''

    with zipfile.ZipFile(output, "w") as archive:
        write_entry(archive, "mimetype", "application/epub+zip", stored=True)
        write_entry(archive, "META-INF/container.xml", container)
        write_entry(archive, "OEBPS/styles/book.css", BOOK_CSS)
        write_entry(archive, "OEBPS/nav.xhtml", build_nav(pages))
        write_entry(archive, "OEBPS/toc.ncx", build_ncx(pages, identifier))
        write_entry(archive, "OEBPS/content.opf", build_package(pages, identifier, modified, sorted(diagram_assets)))
        cover = xhtml_document("Cover", '<section class="cover"><img src="text/resources/logos/codex-howto-logo.svg" alt="Codex How To" /></section>', "styles/book.css")
        write_entry(archive, "OEBPS/cover.xhtml", cover)
        for page, body, css_href in rendered_pages:
            stored_page = PurePosixPath("text") / page.output
            write_entry(archive, f"OEBPS/{stored_page}", xhtml_document(page.title, body, css_href))
        for archive_path, svg in sorted(diagram_assets.items()):
            write_entry(archive, f"OEBPS/{archive_path}", svg)
        for name in ("codex-howto-logo.svg", "codex-howto-logo-dark.svg"):
            write_entry(archive, f"OEBPS/text/resources/logos/{name}", (root / "resources/logos" / name).read_bytes())

    validate_epub(output, len(pages))
    print(f"EPUB built: {len(pages)} pages at {output}")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = (args.output or root / "dist/codex-howto.epub").resolve()
    try:
        build_epub(root, output)
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"EPUB build failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
