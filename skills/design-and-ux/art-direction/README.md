# art-direction

Design guidance for Lovable. Makes Lovable approach frontend work as an award-winning design director rather than a competent implementer: a committed visual world, a clear point of view, and a craft floor that refuses the tells of machine-made design.

A derivative of [Impeccable](https://github.com/pbakaus/impeccable) by Paul Bakaus, adapted to run inside Lovable. Not affiliated with or endorsed by the original project — see [NOTICE.md](NOTICE.md) for what changed and why.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/design-and-ux/art-direction
```

## Use

Invoke it with `/art-direction` plus what you want, or just describe the design work and let Lovable match it — the description covers the whole surface of frontend design tasks.

Twenty-one commands, grouped by intent:

| | |
|---|---|
| **Build** | `shape` · `init` · `document` · `extract` |
| **Evaluate** | `critique` · `audit` |
| **Refine** | `polish` · `bolder` · `quieter` · `distill` · `harden` · `onboard` |
| **Enhance** | `animate` · `colorize` · `typeset` · `layout` · `delight` · `overdrive` |
| **Fix** | `clarify` · `adapt` · `optimize` |

Invoked with no argument, it reads the project and recommends the two or three highest-value next moves.

Examples:

```
/art-direction bolder the pricing page
/art-direction critique the dashboard
/art-direction this landing page feels generic, give it a point of view
```

## How it works

`SKILL.md` stays small and routes to one playbook per task; the playbooks live in `reference/` and load only when their command runs. That keeps the loaded context proportional to the job instead of pulling 300KB of design doctrine into every message.

Three files carry the durable state, written into your project as ordinary files:

- `PRODUCT.md` — product truth: what this is, who it serves, the platform. Written by `init`.
- `DESIGN.md` — the committed visual world: tokens, type, materials, component character. Written by `document`, or at the finish of a new-work build.
- `docs/design/` — surface briefs, critique snapshots, and mocks.

## What this port does not have

Impeccable ships a Node toolchain that Lovable cannot run: a 59-rule anti-pattern detector, a live browser mode for picking elements and generating variants in place, a post-edit hook, and a drift-repair doctor. Those are removed here rather than left in as instructions that would fail. Where the detector ran, this port reads the source against the anti-pattern families in `reference/craft-floor.md` and inspects the rendered preview instead.

If you work in Claude Code, Cursor, or another agent with a shell, use the original — it is strictly more capable there.

## License

Apache License 2.0. Copyright 2025 Paul Bakaus; modifications copyright 2026 Silvio Ventre. See [LICENSE](LICENSE) and [NOTICE.md](NOTICE.md).
