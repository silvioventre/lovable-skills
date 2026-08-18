---
name: knowledge
description: Use when the user wants to set up, write, review, or clean up the persistent instructions Lovable carries into every message — "write my project knowledge", "generate knowledge for this project", "set up coding standards for my workspace", "what should go in the knowledge file", "Lovable keeps forgetting X", "Lovable keeps using the wrong library", "I keep repeating the same instruction", "review my knowledge". Covers what belongs in workspace knowledge versus project knowledge, how to write instructions that actually change behaviour, and when a rule should be a skill instead. Not for writing skills themselves, and not for one-off instructions that belong in a single prompt.
---

# Knowledge

Knowledge is the standing instruction set carried into every message. Getting it right raises the quality of every edit; getting it wrong degrades every edit, quietly and permanently.

The trigger to write it is almost always the same complaint: *"I keep having to repeat this."* A repeated instruction is a missing knowledge entry.

## Two levels, one rule

| | Scope | Holds | Who edits |
|---|---|---|---|
| **Workspace knowledge** | Every project in the workspace | Rules that should be true everywhere — standards, conventions, preferred libraries, things to avoid | Workspace owners and admins |
| **Project knowledge** | One project | What this app is, who uses it, its schema, its architecture decisions, its vocabulary | Anyone who can edit the project |

The rule for placement: **if it would be true in your next project too, it is workspace knowledge. If it is about this app, it is project knowledge.**

Both cap at 10,000 characters. Both are included together in every message. Where they conflict, project knowledge generally wins, because it is more specific — but relying on that is worse than not conflicting. Keep shared rules in one place and project facts in the other.

One workspace knowledge per workspace; there is no way to scope different rules to subsets of projects.

## Knowledge or skill?

The decision that keeps knowledge small enough to be followed.

- **Relevant on every message** → knowledge. Coding standards, naming, brand voice, the domain vocabulary.
- **Relevant only when a specific topic comes up** → a skill. A release checklist, a review playbook, a particular kind of content.

Putting task-specific instructions into knowledge is the most common mistake here. It bloats the always-on context, dilutes the rules that do matter, and the instruction still fails to fire reliably because it is buried.

## Route the task

| The task | Playbook |
|---|---|
| Writing project knowledge for an existing app | [reference/project.md](reference/project.md) |
| Setting standards across projects | [reference/workspace.md](reference/workspace.md) |
| "Lovable keeps doing X wrong" | [reference/fixing.md](reference/fixing.md) |
| Reviewing or trimming what is already there | [reference/fixing.md](reference/fixing.md) |

## How to write it

**Be specific enough to be checkable.** "Always enable TypeScript strict mode. Never use `any` — use `unknown` and narrow it" changes behaviour. "Write clean code" does not, and it consumes characters that a real rule could have used.

**Write it like onboarding documentation.** Explain the project the way you would to a developer joining next week, including the architectural decisions you do not want revisited. A decision recorded is a decision that stops being re-litigated in every session.

**Prefer bullets and direct rules to paragraphs.** Short instructions are followed more reliably than prose.

**Say what to avoid, not only what to do.** "Do not call `fetch` directly from components" prevents a specific recurring behaviour in a way that a positive rule about service layers does not.

**Do not try to document everything.** A few clear rules and a short description of the project improve output substantially. An exhaustive specification hits the character limit and buries the rules that mattered.

## What it cannot do

**In very long conversations, standing instructions are not always followed consistently.** This is a real limit, not a reason to write more. Two consequences:

- A rule that must never be violated needs enforcement beyond knowledge — a test, a review step, a check in a skill.
- When behaviour drifts late in a long session, restating the rule in the message is a fair response; it does not mean the knowledge is wrong.

**Instruction files in the repository also apply.** A root-level `AGENTS.md` is always read regardless of conversation length, which makes it the more reliable home for rules that must survive a long session. For a technical user already keeping such a file, point them there rather than duplicating it.
