#!/usr/bin/env python3
"""Check Markdown structure and rendering hazards in authored documentation."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from doc_utils import FENCE_RE, markdown_files


def check_file(path: Path) -> list[str]:
    errors: list[str] = []
    in_fence = False
    fence_line = 0
    table_columns: int | None = None
    lines = path.read_text(encoding="utf-8").splitlines()
    for number, line in enumerate(lines, 1):
        fence = FENCE_RE.match(line)
        if fence:
            if not in_fence and not fence.group(1).strip():
                errors.append(f"{path}:{number}: opening code fence has no language")
            in_fence = not in_fence
            fence_line = number if in_fence else 0
            table_columns = None
            continue
        if line.rstrip() != line:
            errors.append(f"{path}:{number}: trailing whitespace")
        if in_fence:
            continue
        if line.startswith("|") and line.endswith("|"):
            columns = len(re.findall(r"(?<!\\)\|", re.sub(r"`[^`]*`", "", line))) - 1
            if table_columns is None:
                table_columns = columns
            elif not re.match(r"^\|[\s:|\-]+\|$", line) and columns != table_columns:
                errors.append(f"{path}:{number}: table column count differs from header")
        else:
            table_columns = None
    if in_fence:
        errors.append(f"{path}:{fence_line}: unclosed code fence")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    files = markdown_files(root)
    errors = [error for path in files for error in check_file(path)]
    if errors:
        print("Markdown validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Markdown validation passed: {len(files)} files")
    return 0


if __name__ == "__main__":
    sys.exit(main())
