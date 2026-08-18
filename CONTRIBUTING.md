# Contributing

Thanks for considering a contribution. This repository holds skills for [Lovable](https://lovable.dev) — markdown playbooks that Lovable loads when a task matches them. Contributions are welcome whether you are fixing a sentence, correcting something that turned out to be wrong in practice, or adding a whole skill.

## Before you start

**Open an issue first for a new skill.** It saves you writing something that overlaps an existing one, and the boundary between skills matters more here than in most projects — a skill that fires on the wrong request is worse than no skill.

**Small corrections need no issue.** If a playbook says something inaccurate, or a step does not work as written, open a pull request directly. Real-world corrections are the most valuable contributions this repository can get.

## The shape of a skill

Every skill in this repository follows the same structure, and new ones should too:

```
skills/<category>/<skill-name>/
├── SKILL.md          # small; always loaded when the skill fires
├── README.md         # the landing page for anyone browsing this folder
└── reference/        # loaded on demand, one file per branch
```

`SKILL.md` carries three things and nothing more:

1. **A routing table** mapping a symptom, task, or question to the one reference file that owns it.
2. **The rules that override everything**, stated once so they apply to every branch.
3. **The report format**, so output is consistent and checkable.

The depth belongs in `reference/`. If `SKILL.md` grows past roughly 5,000 characters, something in it belongs in a reference file — the point of the split is that a session loads only the branch it needs.

## Writing conventions

These are the conventions the existing skills follow. Matching them keeps the library coherent.

**Start the description with "Use when…"** and list concrete phrasings people actually type, including informal ones. The description is the only signal Lovable has when deciding whether to load the skill, so it does more work than any other line in the file.

**State the boundaries.** Every description ends by saying what the skill does *not* cover, and points at the skill that does. Overlapping skills that both fire on the same request produce contradictory instructions.

**Prefer the rule to the explanation.** "Never apply `overflow-x: hidden` to `body`" followed by one sentence on why beats three paragraphs of theory. These files are read by an agent mid-task, not studied.

**Say what not to do.** Negative rules stop specific recurring behaviour in a way positive ones do not. Most of the highest-value lines in this repository are prohibitions.

**Include the failure mode, not just the fix.** Explaining *how* something breaks is what lets someone recognise it next time in a form you did not anticipate.

**No fabricated specifics.** Do not invent limits, version numbers, API shapes, or behaviour you have not verified. If something is uncertain, say it is uncertain — a confidently wrong instruction is worse than an absent one.

**Write in English**, in prose, without emoji.

## Naming

The directory name and the `name` field must match exactly. Names are lowercase letters, digits and single hyphens, at most 64 characters, with no leading, trailing, or consecutive hyphens.

**Names cannot be changed after a skill is created in Lovable** — renaming means deleting and recreating it, which breaks every workspace that installed it. Choose carefully.

## Validate before you push

```bash
pip install pyyaml
python3 scripts/validate-skills.py
```

This checks every skill against the constraints Lovable enforces on import: frontmatter with `name` and `description`, the name matching its directory and character set, `SKILL.md` within 100,000 characters, bundled files within 1 MB each and 200 files / 10 MB per skill, and every internal `.md` link resolving.

It runs automatically on every push and pull request, and a failing run blocks the merge.

**The most common failure is a colon.** In YAML, an unquoted value cannot contain `: ` — the parser reads it as a nested key. See the README section on the colon trap.

## Pull requests

- One skill, or one coherent change, per pull request.
- Say what you changed and why. For a correction, say what happened in practice that the current text got wrong.
- If you added a skill, say how it is scoped against the existing ones.
- Update the catalogue table in the root `README.md` and the relevant category `README.md`.

## Adding a category

Categories exist when a skill needs them — there are no placeholder folders. If your skill genuinely does not fit an existing category, create the folder with its own `README.md` listing the skills inside it, and add it to the root README's repository layout.

## Licensing

Contributions are accepted under the MIT license of this repository.

One exception exists: [`art-direction`](skills/design-and-ux/art-direction/) is a derivative work under Apache License 2.0. Changes to that skill stay under Apache 2.0, and any modification of substance should be recorded in its [`NOTICE.md`](skills/design-and-ux/art-direction/NOTICE.md), which the license requires.

If you contribute material derived from someone else's work, say so in the pull request and include the attribution their license requires.
