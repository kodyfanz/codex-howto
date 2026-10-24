#!/usr/bin/env python3
"""Perform offline structural validation of Mermaid blocks."""

from __future__ import annotations

import re
import sys
from pathlib import Path

from doc_utils import markdown_files
from mermaid_renderer import render_svg

VALID_STARTS = {"flowchart", "graph"}


def blocks(content: str) -> list[str]:
    return re.findall(r"^\s*```mermaid\s*$\n(.*?)^\s*```\s*$", content, re.MULTILINE | re.DOTALL)


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    errors: list[str] = []
    count = 0
    for path in markdown_files(root):
        for number, block in enumerate(blocks(path.read_text(encoding="utf-8")), 1):
            count += 1
            first = next((line.strip().split()[0] for line in block.splitlines() if line.strip() and not line.lstrip().startswith("%%")), "")
            if first not in VALID_STARTS:
                errors.append(f"{path}: Mermaid block {number} starts with unsupported directive {first!r}")
            if block.count("[") != block.count("]") or block.count("(") != block.count(")"):
                errors.append(f"{path}: Mermaid block {number} has unbalanced brackets")
            try:
                render_svg(block)
            except ValueError as exc:
                errors.append(f"{path}: Mermaid block {number} cannot render: {exc}")
    if errors:
        print("Mermaid validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Mermaid validation passed: {count} blocks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
