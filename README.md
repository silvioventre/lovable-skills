# lovable-skills

**A central library of reusable skills for [Lovable](https://lovable.dev).**

Fifteen production-ready skills that teach Lovable how to plan features, debug failures, secure an app, make it responsive, take payments, send email, and ship it — each one a focused playbook that loads only when the task calls for it.

[![Validate skills](https://github.com/silvioventre/lovable-skills/actions/workflows/validate-skills.yml/badge.svg)](https://github.com/silvioventre/lovable-skills/actions/workflows/validate-skills.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What is a Lovable skill?

A skill is a named markdown playbook with three parts: a **name**, a **description** that tells Lovable *when* to use it, and **instructions** it follows once loaded. Lovable applies a skill automatically when your request matches its description, or you invoke it explicitly with `/skill-name`.

Skills differ from [knowledge](https://docs.lovable.dev/features/knowledge) in one important way:

|  | Loaded | Use it for |
|---|---|---|
| **Knowledge** | Always, on every message | Rules that apply to everything — coding standards, brand voice, domain terms |
| **Skills** | On demand, when the request matches | Instructions that only matter for a specific kind of task |

Because skills load only when relevant, a workspace can hold many focused ones without weighing down every conversation. That is the design principle behind this library: **each skill stays small and routes to a bundle of reference files that load only when their branch is taken.**

## How these skills are built

Every skill here follows the same shape, and it is worth understanding before you use or extend them.

```
skills/<category>/<skill-name>/
├── SKILL.md          # small, always loaded when the skill fires
└── reference/        # loaded on demand, one file per branch
    ├── ...
```

`SKILL.md` carries three things and nothing more:

1. **A routing table** — symptom, task, or question mapped to the one reference file that owns it.
2. **The rules that override everything**, stated once so they apply to every branch.
3. **The report format**, so output is consistent and checkable.

The depth lives in `reference/`. A `debug` session about a blank screen loads the build-and-preview playbook and nothing else; the backend and fix-loop playbooks stay unread. This keeps the loaded context proportional to the task instead of pulling every page of doctrine into every message.

**Why routers.** Most of these skills answer a question the user cannot answer themselves — *which kind of problem is this?* Someone reporting "my app is broken" does not know whether they have a build failure, a permissions problem, or a stale deployment. The routing table makes that classification the first step, so the right playbook is loaded before any work starts.

## The catalogue

### Build

| Skill | Use it when |
|---|---|
| [`plan`](skills/build/plan/) | You want something understood before it is written — exploring an unfamiliar project, comparing approaches, breaking a vague request into buildable increments |
| [`test`](skills/build/test/) | You want to verify something works or protect it from breaking — routed to browser testing, frontend tests, or backend verification |
| [`auth`](skills/build/auth/) | You are adding or reworking sign-in — including deciding whether the app needs its own login at all |
| [`payments`](skills/build/payments/) | You are taking money — test and live environments, the subscription lifecycle, go-live, and the irreversible operations |
| [`emails`](skills/build/emails/) | The app needs to send email — sending domains, templates, and the deliverability practices that decide whether messages arrive |
| [`analyze`](skills/build/analyze/) | You want data examined or a file produced — analysis, reports, exports, charts, and building features from what was found |
| [`knowledge`](skills/build/knowledge/) | You are writing or fixing the persistent instructions Lovable carries into every message |
| [`mcp`](skills/build/mcp/) | You want your published app callable from ChatGPT, Claude, or another AI assistant |

### Design and UX

| Skill | Use it when |
|---|---|
| [`art-direction`](skills/design-and-ux/art-direction/) | You want design with a point of view — 21 commands covering visual direction, critique, and refinement |
| [`responsive`](skills/design-and-ux/responsive/) | The layout must work at every width, verified against a pass/fail gate rather than declared |

### Quality and operations

| Skill | Use it when |
|---|---|
| [`debug`](skills/troubleshooting/debug/) | Something is broken and you need the root cause, not a silenced symptom |
| [`secure`](skills/security/secure/) | You are hardening the app or asking whether it is safe to publish |
| [`ship`](skills/deployment/ship/) | You are going live — pre-flight checks, access control, and verification on the live site |
| [`deploy-external`](skills/deployment/deploy-external/) | You are considering running the frontend or backend outside Lovable Cloud |
| [`lovable-codebase-audit-cleanup`](skills/code-quality/lovable-codebase-audit-cleanup/) | The project has accumulated dead code, unused dependencies, and duplication |

## Install a skill

Skills are installed one at a time. In Lovable, go to **Settings → Skills → Add → Import from GitHub** and paste the URL of the skill's folder:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/<category>/<skill-name>
```

For example, to install `debug`:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/troubleshooting/debug
```

Lovable downloads the folder, validates it, and adds the skill to your workspace with its name, description, and reference files intact. Importing the repository root does not work — a repo containing several skills must be imported per subdirectory.

Once installed, a skill is available to **every project in that workspace**.

## Using them

You rarely need to name a skill. Each description is written to match how people actually phrase the request, so describing the problem is usually enough:

```
my pricing page has horizontal scrolling on my phone        → responsive
I paid but the premium features didn't unlock               → payments
is this safe to publish?                                    → secure
I haven't touched this app in months, explain how it works  → plan
```

To invoke one explicitly, type `/` and pick it:

```
/debug the checkout page shows a blank screen after I click pay
/secure review this before I launch on Friday
/plan I want to add comments and likes — what am I signing up for?
```

Think of the skill as the **how** and your prompt as the **what**.

### A worked example: shipping a SaaS side project

Here is how the library is meant to be used across the life of one real project — a subscription app built from scratch.

**1. Understand before building.** The idea is vague and the schema is not obvious.

```
/plan I want to build a tool where restaurant managers track inventory
across several locations. Break it into what I should build first.
```

`plan` explores what exists, asks the questions that would change the design, and returns an ordered set of increments — data model, read path, write path, states — each independently verifiable. It writes no code.

**2. Add sign-in, before anything that depends on identity.**

```
/auth add login — it's a B2B product, restaurant managers signing up themselves
```

`auth` starts from the audience rather than the technology, and would tell you here that if this were an internal tool for your own workspace, you might not need a login at all.

**3. Build the increments, verifying as you go.**

```
/test verify the whole signup and first-inventory-item flow end to end
```

`test` routes this to browser testing, because it is a multi-step user flow — and warns you that it runs as whatever user you are signed in as, so destructive actions need an explicit do-not-touch list.

**4. Something breaks.**

```
/debug the inventory list is empty for the second account I created,
but the rows are definitely in the table
```

`debug` routes this to the backend playbook, which establishes the layer before changing anything: the data exists, so this is access control, not a query bug. Empty results with no error is normal row-level-security behaviour.

**5. Take money.**

```
/payments add monthly and annual plans, unlock the multi-location feature for paid users
```

`payments` builds the entitlement logic server-side and insists on testing the whole subscription lifecycle in the test environment — cancellation, renewal, failed payment, trial — not just a successful purchase.

**6. Make it work on a phone.**

```
/responsive the whole app, it's only ever been tested on my laptop
```

`responsive` sweeps a fixed width ladder from 320px up and reports a seven-item gate, marking anything it could not verify as unverified rather than passed.

**7. Check it before anyone sees it.**

```
/secure I want to launch this weekend
```

`secure` runs the pre-publish gate. Two of its ten checks require a second account and a directly-called endpoint, because neither can be established from your own signed-in session.

**8. Go live.**

```
/ship publish it, it should be public
```

`ship` runs the pre-flight, then explains the thing that catches almost everyone: publishing deploys a snapshot, so later edits do not reach the live site until you publish again.

### How the skills relate

They are designed to hand off to each other rather than overlap:

```
plan ──▶ auth ──▶ build ──▶ test ──▶ payments ──▶ secure ──▶ ship
             │                 ▲
             └──── debug ──────┘        (when something breaks)
```

Some boundaries are deliberate and worth knowing:

- **`art-direction`'s `adapt` command vs `responsive`.** `adapt` decides *what the experience should become* on another device — a design decision. `responsive` makes the existing design actually hold at every width — execution. If the layout is right but breaks on a phone, you want `responsive`. If the layout is wrong for a phone, you want `adapt`.
- **`auth` and `payments` vs `secure`.** The first two establish *who a user is* and *what they paid for*. Neither decides what they are allowed to do — that is `secure`, enforced server-side on every request.
- **`plan` vs `debug`.** Planning around a bug you have not understood is planning around a guess. Diagnose first.
- **`test` vs `debug`.** `debug` finds the cause; `test` proves the fix and stops it regressing.

## Repository layout

```
skills/
├── _template/                  # scaffold to copy when writing a new skill
├── build/                      # plan, test, auth, payments, emails, analyze, knowledge, mcp
├── design-and-ux/              # art-direction, responsive
├── troubleshooting/            # debug
├── security/                   # secure
├── deployment/                 # ship, deploy-external
└── code-quality/               # lovable-codebase-audit-cleanup

scripts/validate-skills.py      # validates every skill against Lovable's import limits
.github/workflows/              # runs the validator on every push and pull request
```

Categories exist when a skill needs them — there are no empty folders waiting to be filled.

## Writing your own skill

1. Copy `skills/_template/SKILL.md` to `skills/<category>/<skill-name>/SKILL.md`.
2. Fill in the three required fields:
   - **`name`** — short and permanent, lowercase letters, digits and single hyphens, max 64 characters. It **cannot be changed** after the skill is created in Lovable; renaming means deleting and recreating.
   - **`description`** — start with "Use when…" and describe the trigger as concretely as you can, including what the skill does *not* cover. This is the main signal Lovable uses to decide whether to load it.
   - **Instructions** — the markdown body: steps, constraints, examples, edge cases, and the expected output format.
3. The directory name must match the `name` field exactly.
4. Put longer material in `reference/` files and link to them from `SKILL.md`, so they load only when needed.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full conventions.

## Validation

Before committing, or before importing into Lovable:

```bash
pip install pyyaml
python3 scripts/validate-skills.py
```

It checks every directory containing a `SKILL.md` against the constraints Lovable enforces on import:

- YAML frontmatter present, with `name` and `description`
- `name` matches the directory, and uses only lowercase letters, digits and single hyphens, max 64 characters
- `SKILL.md` within 100,000 characters
- each bundled file within 1 MB, and per skill at most 200 files / 10 MB total
- every internal `.md` link resolves

The frontmatter is parsed with a real YAML parser rather than a regex, because Lovable parses it as YAML — anything that breaks the parser breaks the import. This runs automatically on every push and pull request.

### The colon trap

In YAML, an unquoted value **cannot contain `: `** (colon followed by space). The parser reads it as a nested key and the import fails with `mapping values are not allowed in this context`. It is the easiest mistake to make when writing a `description`.

```yaml
# broken
description: Use when auditing a page: metadata, headings, internal links.

# fine — rephrased without the colon
description: Use when auditing a page for metadata, headings and internal links.

# fine — quoted value
description: "Use when auditing a page: metadata, headings, internal links."
```

The same applies to ` #`, which starts a comment, and to values beginning with `&`, `*`, `!`, `%` or `` ` ``. When in doubt, quote the whole value.

## Portability

These skills use the `SKILL.md` shape defined by the [Agent Skills convention](https://docs.lovable.dev/features/skills), the same format used by Anthropic's Claude and other tools that follow it. A skill downloaded from Lovable as a `.zip` can be uploaded into those tools, and vice versa.

Nothing here depends on Lovable-specific syntax. The instructions assume a Lovable project — a React and Tailwind app with a managed backend — but the playbooks themselves are ordinary markdown.

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add a skill, the writing conventions used throughout, and what the validator expects. Please also read the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

MIT — see [LICENSE](LICENSE).

One exception: [`art-direction`](skills/design-and-ux/art-direction/) is a derivative work of [Impeccable](https://github.com/pbakaus/impeccable) by Paul Bakaus, distributed under the Apache License 2.0. It carries its own `LICENSE` and a [`NOTICE.md`](skills/design-and-ux/art-direction/NOTICE.md) itemising every modification. It is not affiliated with or endorsed by the original project.

## Further reading

- [Define reusable instructions with skills](https://docs.lovable.dev/features/skills) — Lovable's own documentation
- [Knowledge](https://docs.lovable.dev/features/knowledge) — for rules that should apply to every message instead
