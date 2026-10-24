#!/usr/bin/env python3
"""Validate local Markdown links, files, directories, and heading fragments."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from doc_utils import LINK_RE, headings, markdown_files, split_link_target


def mask_fences(content: str) -> str:
    output: list[str] = []
    in_fence = False
    for line in content.splitlines():
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            output.append("")
        else:
            output.append("" if in_fence else line)
    return "\n".join(output)


def check_file(path: Path, root: Path) -> list[str]:
    errors: list[str] = []
    content = path.read_text(encoding="utf-8")
    anchor_cache: dict[Path, set[str]] = {path: headings(content)}
    for match in LINK_RE.finditer(mask_fences(content)):
        raw = match.group(2)
        normalized = raw.strip().lstrip("<")
        if re.match(r"^[a-z][a-z0-9+.-]*:", normalized, re.I) or normalized.startswith("//"):
            continue
        target_text, fragment = split_link_target(raw)
        target = path if not target_text else (path.parent / target_text).resolve()
        try:
            target.relative_to(root.resolve())
        except ValueError:
            errors.append(f"{path}: link escapes repository: {raw}")
            continue
        if target.is_dir():
            readme = target / "README.md"
            if fragment and readme.is_file():
                target = readme
            elif not fragment:
                continue
        if not target.exists():
            errors.append(f"{path}: missing link target: {raw}")
            continue
        if fragment and target.suffix.lower() == ".md":
            anchors = anchor_cache.setdefault(target, headings(target.read_text(encoding="utf-8")))
            if fragment not in anchors:
                errors.append(f"{path}: missing anchor #{fragment} in {target.relative_to(root)}")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    files = markdown_files(root)
    errors = [error for path in files for error in check_file(path, root)]
    if errors:
        print("Cross-reference validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Cross-reference validation passed: {len(files)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
