#!/usr/bin/env python3
"""Run the complete offline quality and release gate."""

from __future__ import annotations

import json
import py_compile
import subprocess
import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDED = {"site", "dist", ".git", "__pycache__"}


def authored(pattern: str) -> list[Path]:
    return sorted(
        path for path in ROOT.rglob(pattern)
        if not any(part in EXCLUDED for part in path.relative_to(ROOT).parts)
    )


def run(*command: str) -> None:
    print(f"\n$ {' '.join(command)}", flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def validate_structured_files() -> None:
    for path in authored("*.json"):
        json.loads(path.read_text(encoding="utf-8"))
    for path in authored("*.toml"):
        tomllib.loads(path.read_text(encoding="utf-8"))
    for path in authored("*.py"):
        if path.parts[-2:] == ("scripts", "quality_gate.py"):
            continue
        py_compile.compile(str(path), doraise=True)
    for path in [*authored("*.yml"), *authored("*.yaml")]:
        scalar_indent: int | None = None
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if "\t" in line:
                raise ValueError(f"{path}:{number}: YAML must not contain tabs")
            stripped = line.strip()
            indent = len(line) - len(line.lstrip(" "))
            if scalar_indent is not None:
                if not stripped or indent > scalar_indent:
                    continue
                scalar_indent = None
            if stripped.endswith(("|", ">", "|-", ">-", "|+", ">+")) and ":" in stripped:
                scalar_indent = indent
                continue
            if stripped and not stripped.startswith(("#", "-", "${{")) and ":" not in stripped:
                raise ValueError(f"{path}:{number}: expected a YAML mapping or sequence")
    print(
        f"Structured files passed: {len(authored('*.json'))} JSON, "
        f"{len(authored('*.toml'))} TOML, {len(authored('*.yml')) + len(authored('*.yaml'))} YAML, "
        f"{len(authored('*.py'))} Python"
    )


def validate_extensions() -> None:
    skills = authored("SKILL.md")
    for path in skills:
        content = path.read_text(encoding="utf-8")
        if not content.startswith("---\n") or "\nname:" not in content or "\ndescription:" not in content:
            raise ValueError(f"invalid skill frontmatter: {path}")
    manifests = [path for path in authored("plugin.json") if ".codex-plugin" in path.parts]
    for path in manifests:
        manifest = json.loads(path.read_text(encoding="utf-8"))
        for key in ("name", "version", "description"):
            if not manifest.get(key):
                raise ValueError(f"{path}: missing {key}")
    print(f"Extensions passed: {len(skills)} skills, {len(manifests)} plugins")


def main() -> int:
    try:
        run(sys.executable, "scripts/check_markdown.py")
        run(sys.executable, "scripts/check_cross_references.py")
        run(sys.executable, "scripts/check_mermaid.py")
        run(sys.executable, "scripts/check_links.py")
        validate_structured_files()
        validate_extensions()
        run(sys.executable, "-m", "unittest", "discover", "-s", "scripts/tests", "-v")
        run(sys.executable, "-m", "unittest", "discover", "-s", "06-hooks/examples", "-p", "test_*.py")
        for directory in (
            "07-plugins/examples/devops-readiness/scripts",
            "07-plugins/examples/documentation-maintenance",
            "07-plugins/examples/pr-review",
        ):
            run(sys.executable, "-m", "unittest", "discover", "-s", directory, "-p", "test_*.py")
        run(sys.executable, "scripts/build_website.py")
        run(sys.executable, "scripts/build_epub.py")
        run(sys.executable, "scripts/build_release.py")
    except (OSError, ValueError, subprocess.CalledProcessError, tomllib.TOMLDecodeError) as exc:
        print(f"\nQuality gate failed: {exc}", file=sys.stderr)
        return 1
    print("\nQuality gate passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
