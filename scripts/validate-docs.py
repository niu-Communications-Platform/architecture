#!/usr/bin/env python3
"""Validate robust bilingual documentation invariants."""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def error(message: str) -> None:
    ERRORS.append(message)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        error(f"Missing required file: {path.relative_to(ROOT)}")
        return ""


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    result: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"\'')
    return result


def relative_target(source: Path, target: Path) -> str:
    return Path(os.path.relpath(target, source.parent)).as_posix()


def has_markdown_link(text: str, target: str) -> bool:
    return re.search(r"\]\(" + re.escape(target) + r"(?:#[^)]+)?\)", text) is not None


def check_root_pair() -> None:
    pairs = [
        (ROOT / "README.de.md", ROOT / "README.md"),
        (ROOT / "DOCUMENTATION.de.md", ROOT / "DOCUMENTATION.md"),
    ]
    for de, en in pairs:
        de_text = read(de)
        en_text = read(en)
        if de_text and not has_markdown_link(de_text, relative_target(de, en)):
            error(f"{de.relative_to(ROOT)} must visibly link to {en.relative_to(ROOT)}")
        if en_text and not has_markdown_link(en_text, relative_target(en, de)):
            error(f"{en.relative_to(ROOT)} must visibly link to {de.relative_to(ROOT)}")


def paired_files(base: str) -> None:
    de_root = ROOT / base / "de"
    en_root = ROOT / base / "en"
    if not de_root.is_dir():
        error(f"Missing canonical directory: {de_root.relative_to(ROOT)}")
        return
    if not en_root.is_dir():
        error(f"Missing English directory: {en_root.relative_to(ROOT)}")
        return

    de_files = {p.relative_to(de_root) for p in de_root.rglob("*.md")}
    en_files = {p.relative_to(en_root) for p in en_root.rglob("*.md")}

    for rel in sorted(de_files - en_files):
        error(f"Missing English counterpart for {base}/de/{rel}")
    for rel in sorted(en_files - de_files):
        error(f"English file has no German counterpart: {base}/en/{rel}")

    for rel in sorted(de_files & en_files):
        de_file = de_root / rel
        en_file = en_root / rel
        de_text = read(de_file)
        en_text = read(en_file)
        de_to_en = relative_target(de_file, en_file)
        en_to_de = relative_target(en_file, de_file)

        if not has_markdown_link(de_text, de_to_en):
            error(f"{de_file.relative_to(ROOT)} must visibly link to its English counterpart")
        if not has_markdown_link(en_text, en_to_de):
            error(f"{en_file.relative_to(ROOT)} must visibly link to its German counterpart")

        if base == "adr" and rel.name != "README.md":
            for path, text in ((de_file, de_text), (en_file, en_text)):
                meta = frontmatter(text)
                if not meta.get("status"):
                    error(f"{path.relative_to(ROOT)} must declare an ADR status")
                if not DATE_RE.match(meta.get("date", "")):
                    error(f"{path.relative_to(ROOT)} must declare date: YYYY-MM-DD")


def check_adr_numbers() -> None:
    pattern = re.compile(r"^(\d{4})-(.+)\.md$")
    de_dir = ROOT / "adr" / "de"
    en_dir = ROOT / "adr" / "en"

    for directory, label in ((de_dir, "German"), (en_dir, "English")):
        seen: dict[str, str] = {}
        for path in directory.glob("*.md"):
            match = pattern.match(path.name)
            if not match:
                continue
            number = match.group(1)
            if number in seen:
                error(f"Duplicate ADR number {number} in {label}: {seen[number]} and {path.name}")
            seen[number] = path.name

    de_names = {p.name for p in de_dir.glob("[0-9][0-9][0-9][0-9]-*.md")}
    en_names = {p.name for p in en_dir.glob("[0-9][0-9][0-9][0-9]-*.md")}
    for name in sorted(de_names - en_names):
        error(f"ADR missing English counterpart: {name}")
    for name in sorted(en_names - de_names):
        error(f"English ADR has no German counterpart: {name}")


def main() -> int:
    check_root_pair()
    paired_files("docs")
    paired_files("adr")
    check_adr_numbers()

    if ERRORS:
        print("Documentation validation FAILED:\n")
        for item in ERRORS:
            print(f"- {item}")
        return 1

    print("Documentation validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
