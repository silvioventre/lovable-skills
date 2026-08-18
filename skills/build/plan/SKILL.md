---
name: plan
description: Use when the user wants to build something new or substantial and it should be understood before it is written — "I want to add comments and likes", "how should I build this", "plan this feature", "what would this involve", "explore my project and explain how it works", "research the best way to do X", "I haven't touched this app in a while", "what am I signing up for", "break this down for me", "should I do it this way or that way". Covers exploring an unfamiliar or grown project, researching approaches before committing, scoping a vague request into a defined increment, and breaking work into buildable steps. Not for design direction, which art-direction owns, and not for diagnosing a failure, which debug owns.
---

# Plan

Understand before building. The cost of a wrong assumption is small while it is still a sentence and large once it is code that other code depends on.

This is the discipline that prevents the most expensive failure mode in AI-assisted building: a large request implemented confidently on top of a misunderstanding, discovered three features later.

## Route the request

| The request | Playbook |
|---|---|
| "Explain how this project works" | [reference/investigate.md](reference/investigate.md) |
| "I haven't touched this in a while" | [reference/investigate.md](reference/investigate.md) |
| "Where is X handled, why does Y behave that way" | [reference/investigate.md](reference/investigate.md) |
| "What's the best way to build X" | [reference/approach.md](reference/approach.md) |
| "Should I do it this way or that way" | [reference/approach.md](reference/approach.md) |
| Research before committing to a design | [reference/approach.md](reference/approach.md) |
| "Add [substantial feature]" | [reference/scope.md](reference/scope.md) |
| "What would this involve / what am I signing up for" | [reference/scope.md](reference/scope.md) |
| "Break this down" | [reference/scope.md](reference/scope.md) |

Most real requests need two of these in sequence: investigate what exists, then scope what to add. Approach sits between them when there is a genuine choice to make.

## The rule that makes this work

**Do not write code during planning.** Not a small part, not "just scaffolding". The moment code exists, the conversation shifts from *what should this be* to *how do we fix what is there*, and the plan stops being examined.

State this explicitly when you begin, and end with a plan the user approves rather than an implementation they inherit.

## Delegate the investigation

For anything with several independent questions, delegate them to subagents rather than working through them serially in the main thread.

Subagents are read-only, start with fresh context, and see only what you pass into their briefing. They investigate, they report back, they cannot change anything. Several can run at once on independent questions.

Two reasons this matters beyond speed:

- **Context stays clean.** File contents, search results, and abandoned paths do not fill the conversation, so the requirements and decisions remain legible.
- **Findings are sharper.** A bounded question investigated with fresh context returns a better answer than the same question asked halfway through a long thread.

Because a subagent sees only its briefing, the briefing is the whole job: give it the specific question, the relevant paths, and the constraints. A vague briefing returns a vague finding, and you will not know it was vague.

Split by question, not by file. "How does authentication work" and "where would comments attach to the data model" are two investigations. "Look at these twelve files" is one investigation badly described.

## Finish with something decidable

A plan the user cannot say no to is not a plan. Every output of this skill ends with:

1. **What you found** — the current state, in the terms of this project, not generically.
2. **What you propose** — the approach, and the alternatives you rejected with the reason.
3. **What it touches** — files, data, existing behaviour, anything that could regress.
4. **The increments** — the order to build in, each one independently verifiable.
5. **What is uncertain** — the assumptions you made and what would change if they are wrong.
6. **The first step**, small enough to do and check immediately.

Point 5 is the one that gets left out and the one that pays. An assumption stated is an assumption the user can correct in a sentence; an assumption buried in a plan gets discovered as a bug.

## Scope boundaries

- **Not design direction.** What it should look like, the visual world, the interaction character — that is the `art-direction` skill.
- **Not diagnosis.** If something is broken and the cause is unknown, that is the `debug` skill. Planning around a bug you have not understood plans around a guess.
- **Not implementation.** This skill ends where building begins, deliberately.
