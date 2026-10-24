#!/usr/bin/env python3
"""Check internal links by default and optionally probe external URLs."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

from check_cross_references import check_file
from doc_utils import LINK_RE, markdown_files


def external_urls(files: list[Path]) -> list[str]:
    urls: set[str] = set()
    for path in files:
        for match in LINK_RE.finditer(path.read_text(encoding="utf-8")):
            target = match.group(2).split()[0].strip("<>")
            if re.match(r"^https?://", target):
                urls.add(target)
    return sorted(urls)


def probe(url: str, timeout: float) -> str | None:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "codex-howto-link-checker/1.0"})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            if response.status >= 400:
                return f"{url}: HTTP {response.status}"
    except (urllib.error.URLError, TimeoutError) as exc:
        return f"{url}: {exc}"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--external", action="store_true", help="Probe HTTP(S) links; requires network access")
    parser.add_argument("--timeout", type=float, default=10.0)
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    files = markdown_files(root)
    errors = [error for path in files for error in check_file(path, root)]
    if args.external:
        for url in external_urls(files):
            error = probe(url, args.timeout)
            if error:
                errors.append(error)
    if errors:
        print("Link validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    scope = "internal and external" if args.external else "internal"
    print(f"Link validation passed ({scope}): {len(files)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
