#!/usr/bin/env python3
"""Create a release archive from authored project content and build outputs."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path

from build_epub import build_epub
from build_website import build_website

EXCLUDED_NAMES = {
    ".DS_Store", ".git", ".pytest_cache", ".ruff_cache", ".venv", "__pycache__",
    "build", "coverage.xml", "dist", "site",
}


def source_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in EXCLUDED_NAMES for part in relative.parts):
            continue
        if path.is_file():
            files.append(path)
    return sorted(files)


def write_file(archive: zipfile.ZipFile, name: str, data: bytes) -> None:
    info = zipfile.ZipInfo(name, (2026, 1, 1, 0, 0, 0))
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, data)


def build_release(root: Path, output: Path) -> Path:
    root = root.resolve()
    output = output.resolve()
    site = root / "site"
    epub = root / "dist/codex-howto.epub"
    if not (site / "index.html").is_file():
        build_website(root, site)
    if not epub.is_file():
        build_epub(root, epub)
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w") as archive:
        for path in source_files(root):
            relative = path.relative_to(root).as_posix()
            write_file(archive, f"codex-howto/source/{relative}", path.read_bytes())
        for path in sorted(site.rglob("*")):
            if path.is_file():
                relative = path.relative_to(site).as_posix()
                write_file(archive, f"codex-howto/website/{relative}", path.read_bytes())
        write_file(archive, "codex-howto/codex-howto.epub", epub.read_bytes())
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None:
            raise ValueError("release archive contains a corrupt entry")
    print(f"Release archive built at {output}")
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    output = (args.output or root / "dist/codex-howto-release.zip").resolve()
    try:
        build_release(root, output)
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"Release build failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
