from __future__ import annotations

import sys
import tempfile
import unittest
import zipfile
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit

SCRIPTS = Path(__file__).resolve().parents[1]
ROOT = SCRIPTS.parent
sys.path.insert(0, str(SCRIPTS))

from build_epub import build_epub, validate_epub  # noqa: E402
from build_website import build_website  # noqa: E402
from check_markdown import check_file as check_markdown_file  # noqa: E402
from doc_utils import (  # noqa: E402
    collect_all_pages,
    heading_to_anchor,
    headings,
    output_path,
    render_markdown,
)
from mermaid_renderer import render_svg  # noqa: E402


class AssetParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        for name in ("href", "src", "srcset"):
            if values.get(name):
                self.targets.append(values[name] or "")


class DocumentationUtilityTests(unittest.TestCase):
    def test_heading_anchor(self) -> None:
        self.assertEqual(heading_to_anchor("Use `AGENTS.md`: safely"), "use-agentsmd-safely")

    def test_duplicate_heading_anchors(self) -> None:
        self.assertEqual(headings("# Topic\n## Check\n## Check\n"), {"topic", "check", "check-1"})

    def test_index_output_does_not_collide_with_home(self) -> None:
        self.assertEqual(output_path(PurePosixPath("README.md")), PurePosixPath("index.html"))
        self.assertEqual(output_path(PurePosixPath("INDEX.md")), PurePosixPath("complete-index.html"))

    def test_markdown_renderer_rewrites_links_and_merges_quotes(self) -> None:
        page_map = {
            PurePosixPath("README.md"): PurePosixPath("index.html"),
            PurePosixPath("01-demo/README.md"): PurePosixPath("01-demo/index.html"),
        }
        rendered = render_markdown(
            "# Demo\n\n> one\n> two\n\n[Next](01-demo/)\n",
            PurePosixPath("README.md"),
            PurePosixPath("index.html"),
            page_map,
        )
        self.assertIn("<blockquote><p>one two</p></blockquote>", rendered)
        self.assertIn('href="01-demo/index.html"', rendered)

    def test_markdown_renderer_keeps_multiline_picture_and_hides_lint_comments(self) -> None:
        rendered = render_markdown(
            """# Demo

<!-- markdownlint-disable MD033 -->
<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="resources/logo-dark.svg"
  >
  <img alt="Demo logo" src="resources/logo.svg">
</picture>
<!-- markdownlint-enable MD033 -->
""",
            PurePosixPath("README.md"),
            PurePosixPath("index.html"),
            {PurePosixPath("README.md"): PurePosixPath("index.html")},
        )
        self.assertIn("<picture>", rendered)
        self.assertIn('<source\nmedia="(prefers-color-scheme: dark)"', rendered)
        self.assertIn('srcset="resources/logo-dark.svg"', rendered)
        self.assertIn('<img alt="Demo logo" src="resources/logo.svg">', rendered)
        self.assertNotIn("markdownlint-disable", rendered)
        self.assertNotIn("&lt;source", rendered)

    def test_mermaid_renderer_produces_svg(self) -> None:
        svg = render_svg("flowchart LR\n A[Start] --> B[Finish]")
        self.assertIn("<svg", svg)
        self.assertIn("Start", svg)
        self.assertIn("marker-end", svg)

    def test_markdown_validator_rejects_unlabeled_fence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "README.md"
            path.write_text("# Demo\n\n```\nvalue\n```\n", encoding="utf-8")
            self.assertTrue(any("no language" in error for error in check_markdown_file(path)))

    def test_generated_trees_are_excluded_from_publication(self) -> None:
        pages = collect_all_pages(ROOT)
        self.assertFalse(any(part in {"site", "dist"} for page in pages for part in page.relative.parts))
        self.assertEqual(len({page.output for page in pages}), len(pages))


class BuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temporary = tempfile.TemporaryDirectory()
        cls.output_root = Path(cls.temporary.name)
        cls.site = build_website(ROOT, cls.output_root / "site")
        cls.epub = build_epub(ROOT, cls.output_root / "codex-howto.epub")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.temporary.cleanup()

    def test_website_has_home_and_all_publication_pages(self) -> None:
        self.assertTrue((self.site / "index.html").is_file())
        self.assertTrue((self.site / "complete-index.html").is_file())
        self.assertEqual(len(list(self.site.rglob("*.html"))), len(collect_all_pages(ROOT)))

    def test_website_has_no_broken_local_assets(self) -> None:
        failures: list[tuple[Path, str]] = []
        for page in self.site.rglob("*.html"):
            parser = AssetParser()
            parser.feed(page.read_text(encoding="utf-8"))
            for raw in parser.targets:
                parts = urlsplit(raw)
                if parts.scheme or raw.startswith(("#", "//")):
                    continue
                target = (page.parent / parts.path).resolve()
                if target.is_dir():
                    target = target / "index.html"
                if not target.exists():
                    failures.append((page, raw))
        self.assertEqual(failures, [])

    def test_website_contains_no_template_or_binary_markers(self) -> None:
        for page in self.site.rglob("*.html"):
            content = page.read_bytes()
            for marker in (b"<title>{{TITLE}}", b' href="{{ASSET_PREFIX}}', b"{{NAVIGATION}}\n    </nav>"):
                self.assertNotIn(marker, content)
            self.assertNotIn(b"\x00", content)

    def test_website_contains_rendered_diagrams_and_source_fallbacks(self) -> None:
        rendered = [page for page in self.site.rglob("*.html") if b'class="mermaid-diagram"' in page.read_bytes()]
        self.assertEqual(len(rendered), 9)
        for page in rendered:
            content = page.read_text(encoding="utf-8")
            self.assertIn("<img", content)
            self.assertIn("Mermaid source", content)

    def test_epub_passes_structural_validation(self) -> None:
        validate_epub(self.epub, len(collect_all_pages(ROOT)))

    def test_epub_contains_rendered_diagram_assets(self) -> None:
        with zipfile.ZipFile(self.epub) as archive:
            diagrams = [name for name in archive.namelist() if name.startswith("OEBPS/mermaid/") and name.endswith(".svg")]
            self.assertEqual(len(diagrams), 13)
            xhtml = [archive.read(name) for name in archive.namelist() if name.endswith(".xhtml")]
            self.assertEqual(sum(b'class="mermaid-diagram"' in content for content in xhtml), 9)

    def test_epub_excludes_generated_source_paths(self) -> None:
        with zipfile.ZipFile(self.epub) as archive:
            self.assertFalse(any(name.startswith(("site/", "dist/")) for name in archive.namelist()))
            self.assertEqual(archive.namelist()[0], "mimetype")


if __name__ == "__main__":
    unittest.main()
