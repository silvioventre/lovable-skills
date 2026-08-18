---
name: debug
description: Use when something in the project is broken, failing, or behaving unexpectedly — a build error, a red error message, a blank or white preview, a feature that stopped working, a component that disappeared, data that will not load, an edge function or permission failure, an error that keeps coming back after repeated fix attempts, or an app that runs but does the wrong thing. Also use when the user says "it's broken", "not working", "fix this error", "the screen is blank", "it worked before", "I'm stuck in a loop", or pastes a console error, stack trace, or log. Routes the symptom to the matching diagnostic playbook, finds the root cause, and fixes that rather than the symptom. Not for adding new features, and not for performance tuning unless something is actually failing.
---

# Debug

Find the root cause, then fix that. A change that makes the error message disappear without explaining why the error happened is not a fix — it relocates the bug.

## Route the symptom

Read the user's description and any pasted error, then load the one playbook that owns it. Do not load more than one to start; the playbook will tell you if the trail leads elsewhere.

| Symptom | Playbook |
|---|---|
| Build fails, red error banner, syntax or type error | [reference/build-and-preview.md](reference/build-and-preview.md) |
| Blank page, white screen, nothing renders | [reference/build-and-preview.md](reference/build-and-preview.md) |
| Preview not found, sandbox stuck spinning up | [reference/build-and-preview.md](reference/build-and-preview.md) |
| "File exceeds the 10 MB per-file commit limit" | [reference/build-and-preview.md](reference/build-and-preview.md) |
| No error, but the app does the wrong thing | [reference/behavior.md](reference/behavior.md) |
| A component or whole section vanished | [reference/behavior.md](reference/behavior.md) |
| Worked before the last change, broken now | [reference/behavior.md](reference/behavior.md) |
| State stale, UI not updating after an action | [reference/behavior.md](reference/behavior.md) |
| Data will not load, empty list, wrong rows | [reference/backend.md](reference/backend.md) |
| Edge function failing or not deploying | [reference/backend.md](reference/backend.md) |
| "Permission denied", RLS, user sees nothing or too much | [reference/backend.md](reference/backend.md) |
| Login, session, or role check misbehaving | [reference/backend.md](reference/backend.md) |
| Same error keeps returning, or a new one each fix | [reference/loops.md](reference/loops.md) |
| Two or more fix attempts with no progress | [reference/loops.md](reference/loops.md) |
| The project feels too tangled to repair | [reference/loops.md](reference/loops.md) |

If the symptom does not match a row, start at [reference/triage.md](reference/triage.md) and classify it there. If the user gave no symptom at all — "it's broken", "fix it" — do not guess: ask what they expected to happen and what happened instead, then route.

[reference/prompts.md](reference/prompts.md) holds the reusable investigation recipes: investigate-without-editing, fragile-area change, codebase audit, performance audit. Pull from it whenever a playbook calls for one.

## The rules that override everything

**Gather evidence before editing.** The exact error text, the console output, the last change that worked, and what the user expected. A fix built on a guessed cause is how one bug becomes three. [reference/triage.md](reference/triage.md) is the evidence checklist.

**Two failed attempts means stop fixing and start investigating.** Repeating a fix with small variations is the single most expensive failure mode here. After the second attempt, switch to [reference/loops.md](reference/loops.md).

**Change only what the diagnosis names.** No "while I'm here" refactors, no defensive edits to unrelated files, no reformatting. Every extra file touched is a file that can regress, and it destroys the signal about what actually caused the fix to work.

**Treat working features as locked.** Do not modify a functioning component to fix a broken neighbour without saying why it must change. If a shared component has to change, name every feature that depends on it and confirm each still works.

**Never silence a symptom.** A null check that hides a null, an empty catch, a suppressed type error, an `any` cast — each converts a visible bug into an invisible one. If the real fix is out of scope, say so plainly instead of muting the evidence.

**State the cause before the fix.** Every report says what was wrong, why it produced this symptom, and what the change does about it. If you cannot explain why the symptom happened, you have not found the cause yet.

## Report

1. **Symptom** — as observed, with the error text.
2. **Root cause** — what was actually wrong, and why it produced this symptom.
3. **Fix** — the change, and the files touched.
4. **Verification** — what you exercised to confirm it, and at what point it would have failed before.
5. **Left alone** — anything you found but did not fix, and why.

If the cause could not be isolated, say that instead of shipping a speculative fix, and give the next concrete step.
