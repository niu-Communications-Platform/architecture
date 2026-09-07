#!/usr/bin/env python3
"""Validate bilingual documentation conventions for the architecture repository."""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


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


def check_root_pair() -> None:
    en = ROOT / "README.md"
    de = ROOT / "README.de.md"
    en_text = read(en)
    de_text = read(de)
    if en_text and "README.de.md" not in en_text:
        error("README.md must link to canonical README.de.md")
    if de_text and "README.md" not in de_text:
        error("README.de.md must link back to README.md")

    en_doc = ROOT / "DOCUMENTATION.md"
    de_doc = ROOT / "DOCUMENTATION.de.md"
    en_doc_text = read(en_doc)
    de_doc_text = read(de_doc)
    if en_doc_text and "DOCUMENTATION.de.md" not in en_doc_text:
        error("DOCUMENTATION.md must link to canonical DOCUMENTATION.de.md")
    if de_doc_text and "DOCUMENTATION.md" not in de_doc_text:
        error("DOCUMENTATION.de.md must link back to DOCUMENTATION.md")
    if en_doc_text and "German version is canonical" not in en_doc_text:
        error("DOCUMENTATION.md must explicitly state that the German version is canonical")


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
        error(f"English file has no canonical German counterpart: {base}/en/{rel}")

    for rel in sorted(de_files & en_files):
        de_file = de_root / rel
        en_file = en_root / rel
        de_text = read(de_file)
        en_text = read(en_file)

        if rel.name == "README.md":
            if base == "docs":
                if "../en/README.md" not in de_text:
                    error(f"{de_file.relative_to(ROOT)} must link to the English README")
                if "../de/README.md" not in en_text:
                    error(f"{en_file.relative_to(ROOT)} must link to the German README")
            continue

        de_meta = frontmatter(de_text)
        en_meta = frontmatter(en_text)

        # Descriptive docs already use structured metadata and must keep it consistent.
        if base == "docs":
            if de_meta.get("language") != "de":
                error(f"{de_file.relative_to(ROOT)} must declare language: de")
            if de_meta.get("canonical") != "true":
                error(f"{de_file.relative_to(ROOT)} must declare canonical: true")
            if en_meta.get("language") != "en":
                error(f"{en_file.relative_to(ROOT)} must declare language: en")
            if en_meta.get("canonical") != "false":
                error(f"{en_file.relative_to(ROOT)} must declare canonical: false")
            if en_meta.get("translation_status") not in {"current", "outdated", "not-translated"}:
                error(
                    f"{en_file.relative_to(ROOT)} must declare translation_status as "
                    "current, outdated, or not-translated"
                )

        # ADR metadata was introduced incrementally. Whenever it is present, enforce it.
        if base == "adr" and (de_meta or en_meta):
            if de_meta.get("language") != "de":
                error(f"{de_file.relative_to(ROOT)} must declare language: de")
            if de_meta.get("canonical") != "true":
                error(f"{de_file.relative_to(ROOT)} must declare canonical: true")
            if en_meta.get("language") != "en":
                error(f"{en_file.relative_to(ROOT)} must declare language: en")
            if en_meta.get("canonical") != "false":
                error(f"{en_file.relative_to(ROOT)} must declare canonical: false")


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
    if de_names != en_names:
        for name in sorted(de_names - en_names):
            error(f"ADR missing English counterpart: {name}")
        for name in sorted(en_names - de_names):
            error(f"English ADR has no canonical German counterpart: {name}")


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
