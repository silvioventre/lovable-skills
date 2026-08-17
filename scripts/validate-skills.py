#!/usr/bin/env python3
"""Validate every skill in skills/ against Lovable's SKILL.md requirements.

Checks each skill directory (any directory containing a SKILL.md) against the
constraints Lovable enforces on import, so a malformed skill fails here rather
than at Settings -> Skills -> Add.

The frontmatter is parsed with a real YAML parser, not a regex. Lovable parses
it as YAML, so anything that trips PyYAML will trip the import too — most often
an unquoted value containing ": ", which YAML reads as a nested mapping.

Run: python3 scripts/validate-skills.py
Exit: 0 all valid, 1 one or more errors.
"""

import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML is required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# Lovable's documented limits.
NAME_MAX = 64
SKILL_MD_MAX_CHARS = 100_000
BUNDLED_FILE_MAX_BYTES = 1 * 1024 * 1024
SKILL_MAX_FILES = 200
SKILL_MAX_TOTAL_BYTES = 10 * 1024 * 1024

# lowercase letters, digits and single hyphens; no leading/trailing/consecutive hyphens
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"
# The scaffold is not an importable skill: its directory name is not a legal
# skill name and its frontmatter holds placeholders. Its YAML must still parse,
# because every skill created from it inherits the syntax.
TEMPLATE = "_template"

errors: list[str] = []
warnings: list[str] = []


def err(skill: str, msg: str) -> None:
    errors.append(f"{skill}: {msg}")


def warn(skill: str, msg: str) -> None:
    warnings.append(f"{skill}: {msg}")


def split_frontmatter(text: str):
    """Return (frontmatter_text, error)."""
    if not text.startswith("---\n"):
        return None, "SKILL.md must open with a YAML frontmatter block (`---`)"
    end = text.find("\n---", 3)
    if end == -1:
        return None, "unterminated frontmatter block (no closing `---`)"
    return text[4:end], None


def explain_yaml_error(exc: Exception, fm: str) -> str:
    """Turn a YAML exception into something actionable."""
    msg = str(exc).split("\n")[0]
    mark = getattr(exc, "problem_mark", None)
    if mark is None:
        return f"invalid YAML frontmatter: {msg}"

    line, col = mark.line, mark.column
    lines = fm.split("\n")
    excerpt = lines[line][max(0, col - 45) : col + 35] if line < len(lines) else ""
    hint = ""
    if "mapping values are not allowed" in msg:
        hint = (
            "  -> an unquoted value contains ': ' (colon + space), which YAML reads "
            "as a nested key. Rephrase to drop the colon, or quote the whole value."
        )
    return (
        f"invalid YAML frontmatter at line {line + 1}, column {col + 1}: {msg}\n"
        f"      ...{excerpt}...\n{hint}".rstrip()
    )


def check_skill(skill_dir: Path, is_template: bool) -> None:
    name = skill_dir.name
    rel = skill_dir.relative_to(SKILLS_DIR.parent)
    before = len(errors)

    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")

    # --- frontmatter -------------------------------------------------------
    fm, split_error = split_frontmatter(text)
    if split_error:
        err(str(rel), split_error)
        print(f"  FAIL  {rel}")
        return

    try:
        data = yaml.safe_load(fm)
    except yaml.YAMLError as exc:
        err(str(rel), explain_yaml_error(exc, fm))
        print(f"  FAIL  {rel}")
        return

    if not isinstance(data, dict):
        err(str(rel), "frontmatter must be a YAML mapping of keys to values")
        print(f"  FAIL  {rel}")
        return

    declared = data.get("name")
    if not declared:
        err(str(rel), "frontmatter is missing `name`")
    elif not isinstance(declared, str):
        err(str(rel), f"`name` must be a string, got {type(declared).__name__}")
    elif not is_template:
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

    description = data.get("description")
    if not description:
        err(str(rel), "frontmatter is missing `description`")
    elif not isinstance(description, str):
        err(str(rel), f"`description` must be a string, got {type(description).__name__}")
    elif len(description) < 40 and not is_template:
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

    label = "template" if is_template else f"{len(files)} files, {total / 1024:.0f} KB"
    status = "ok  " if len(errors) == before else "FAIL"
    print(f"  {status}  {rel}  ({n_chars:,} chars, {label})")


def main() -> int:
    if not SKILLS_DIR.is_dir():
        print(f"No skills/ directory at {SKILLS_DIR}", file=sys.stderr)
        return 1

    skills = sorted(p.parent for p in SKILLS_DIR.rglob("SKILL.md"))
    if not skills:
        print("No skills found.", file=sys.stderr)
        return 1

    print(f"Validating {len(skills)} skill(s)\n")
    for skill in skills:
        check_skill(skill, is_template=TEMPLATE in skill.parts)

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
