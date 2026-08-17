#!/usr/bin/env python3
"""Validate every skill in skills/ against Lovable's SKILL.md requirements.

Checks each skill directory (any directory containing a SKILL.md) against the
constraints Lovable enforces on import, so a malformed skill fails here rather
than at Settings -> Skills -> Add.

Run: python3 scripts/validate-skills.py
Exit: 0 all valid, 1 one or more errors.
"""

import re
import sys
from pathlib import Path

# Lovable's documented limits.
NAME_MAX = 64
SKILL_MD_MAX_CHARS = 100_000
BUNDLED_FILE_MAX_BYTES = 1 * 1024 * 1024
SKILL_MAX_FILES = 200
SKILL_MAX_TOTAL_BYTES = 10 * 1024 * 1024

# lowercase letters, digits and single hyphens; no leading/trailing/consecutive hyphens
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"
# The template is a scaffold to copy, not an importable skill.
EXCLUDED = {"_template"}

errors: list[str] = []
warnings: list[str] = []


def err(skill: str, msg: str) -> None:
    errors.append(f"{skill}: {msg}")


def warn(skill: str, msg: str) -> None:
    warnings.append(f"{skill}: {msg}")


def parse_frontmatter(text: str):
    """Return (dict, error) for the leading YAML frontmatter block."""
    if not text.startswith("---\n"):
        return None, "SKILL.md must open with a YAML frontmatter block (`---`)"
    end = text.find("\n---", 3)
    if end == -1:
        return None, "unterminated frontmatter block (no closing `---`)"
    body = text[4:end]
    data, key = {}, None
    for line in body.split("\n"):
        if not line.strip():
            continue
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_-]*):\s*(.*)$", line)
        if m:
            key = m.group(1)
            data[key] = m.group(2).strip()
        elif key and (line.startswith(" ") or line.startswith("\t")):
            data[key] += " " + line.strip()  # folded continuation
    return data, None


def check_skill(skill_dir: Path) -> None:
    name = skill_dir.name
    rel = skill_dir.relative_to(SKILLS_DIR.parent)
    before = len(errors)

    skill_md = skill_dir / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")

    # --- frontmatter -------------------------------------------------------
    fm, parse_error = parse_frontmatter(text)
    if parse_error:
        err(str(rel), parse_error)
        print(f"  FAIL  {rel}")
        return

    declared = fm.get("name")
    if not declared:
        err(str(rel), "frontmatter is missing `name`")
    else:
        if declared != name:
            err(str(rel), f"frontmatter name `{declared}` != directory name `{name}`")
        if len(declared) > NAME_MAX:
            err(str(rel), f"name is {len(declared)} chars, max {NAME_MAX}")
        if not NAME_RE.match(declared):
            err(
                str(rel),
                f"name `{declared}` must be lowercase letters, digits and single "
                "hyphens, with no leading, trailing or consecutive hyphens",
            )

    description = fm.get("description")
    if not description:
        err(str(rel), "frontmatter is missing `description`")
    elif len(description) < 40:
        warn(str(rel), "description is very short; it is the main trigger signal")

    # --- size limits -------------------------------------------------------
    n_chars = len(text)
    if n_chars > SKILL_MD_MAX_CHARS:
        err(str(rel), f"SKILL.md is {n_chars:,} chars, max {SKILL_MD_MAX_CHARS:,}")

    files = [p for p in skill_dir.rglob("*") if p.is_file()]
    total = sum(p.stat().st_size for p in files)
    if len(files) > SKILL_MAX_FILES:
        err(str(rel), f"{len(files)} files, max {SKILL_MAX_FILES}")
    if total > SKILL_MAX_TOTAL_BYTES:
        err(str(rel), f"total size {total / 1e6:.1f} MB, max {SKILL_MAX_TOTAL_BYTES / 1e6:.0f} MB")
    for p in files:
        if p.stat().st_size > BUNDLED_FILE_MAX_BYTES:
            err(str(rel), f"{p.relative_to(skill_dir)} is {p.stat().st_size / 1e6:.1f} MB, max 1 MB")

    # --- internal links ----------------------------------------------------
    for md in skill_dir.rglob("*.md"):
        content = md.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)#:]+\.md)\)", content):
            if target.startswith("/"):
                continue
            if not (md.parent / target).resolve().exists():
                err(str(rel), f"{md.relative_to(skill_dir)} links to missing `{target}`")

    status = "ok  " if len(errors) == before else "FAIL"
    print(f"  {status}  {rel}  ({n_chars:,} chars, {len(files)} files, {total / 1024:.0f} KB)")


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"No skills/ directory at {SKILLS_DIR}", file=sys.stderr)
        return 1

    skills = sorted(
        p.parent
        for p in SKILLS_DIR.rglob("SKILL.md")
        if not any(part in EXCLUDED for part in p.parts)
    )

    if not skills:
        print("No skills found.", file=sys.stderr)
        return 1

    print(f"Validating {len(skills)} skill(s)\n")
    for skill in skills:
        check_skill(skill)

    if warnings:
        print("\nWarnings:")
        for w in warnings:
            print(f"  ! {w}")

    if errors:
        print(f"\n{len(errors)} error(s):")
        for e in errors:
            print(f"  x {e}")
        return 1

    print(f"\nAll {len(skills)} skill(s) valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
