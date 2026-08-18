# knowledge

Writing and maintaining the persistent instructions Lovable carries into every message. Getting them right raises the quality of every edit; getting them wrong degrades every edit, quietly.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/build/knowledge
```

## Use

```
/knowledge generate project knowledge for this app
/knowledge set up coding standards for my workspace
/knowledge Lovable keeps using the wrong library even though I've told it three times
```

Or just describe the situation — the description is written to match how people actually phrase it.

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | Workspace versus project, the knowledge-or-skill decision, how to write it, and what it cannot do |
| `reference/project.md` | What belongs in project knowledge, generated from the code rather than from an interview |
| `reference/workspace.md` | Shared rules across projects, and the placement test that keeps the file small |
| `reference/fixing.md` | Diagnosing knowledge that is not working — where deleting beats adding |

## Scope

Not for writing skills themselves, and not for one-off instructions that belong in a single prompt.

## License

MIT — see the [repository LICENSE](../../../LICENSE).
