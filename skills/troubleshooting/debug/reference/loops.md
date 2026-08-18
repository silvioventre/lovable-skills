# Error loops: when fixing keeps failing

The expensive failure mode. Each fix looks reasonable, the error changes shape, and the project accumulates damage faster than it accumulates repairs. The escape is procedural, not clever.

## Recognise it early

You are in a loop if any of these is true:

- Two or more attempts have not resolved it.
- The error keeps returning in slightly different form after each fix.
- Fixing one thing breaks another, repeatedly.
- You cannot say what the previous attempts actually changed.
- The next thing you plan to try is a variation of something already tried.

The moment one of these holds, **stop editing**. Another attempt from inside the loop costs more than it can return.

## Break the loop

Work in order. Do not skip to the last step because it feels faster — it is the most expensive one.

### 1. Inventory the attempts

Establish what has already been tried and what each attempt changed. If the history is unclear, ask directly: *what solutions have we tried so far for this error, and what did each one change?* Repeating a failed fix is common in loops and is pure waste.

Then check the accumulated damage. Several failed fixes leave behind edits that were never reverted — defensive checks, stubs, half-applied changes. Some of them are now themselves causing failures, and they mask the original cause.

### 2. Make the cause explainable

Ask for the error in plain terms: *explain in simple language why this error occurs.* If the explanation is vague, hand-waving, or contradicts the evidence, the cause was never found and every fix so far was a guess. That is the actual diagnosis.

Then challenge the assumption everyone has been working from. When standard fixes do not work, the initial theory of the cause is usually wrong. Look at what has not been questioned: configuration, an external dependency, a stale deployment, a timing or ordering problem, a cached value, data that differs from what everyone assumed.

### 3. Change approach, not parameters

If the cause is understood and the fix still fails, the implementation strategy is the problem. Ask for **three genuinely different approaches** to the goal — not three variants of the current one — with the trade-offs of each, and no code written yet. Investigation-only prompts are in [prompts.md](prompts.md).

The bar for "different" is that it would not hit the same failure. Another attempt at the same design does not qualify.

### 4. Isolate the broken piece

If one component or function resists everything, stop repairing it. Build a fresh minimal version with hard-coded inputs, confirm it works, then reintroduce the real pieces one at a time. The piece that breaks it is the cause — and you now have a working version to build on rather than a damaged one to patch.

Frequently faster than continuing to repair, especially for something that has been edited many times.

### 5. Roll back

When the code has become tangled by a sequence of bad fixes, reverting to the last known-good state is the cheapest move available, not an admission of failure. Everything after that point was net negative.

Then re-approach in small verified steps, and **say explicitly that a rollback happened** — otherwise the next round of reasoning is done against code that no longer exists. Note what the earlier attempt taught you so the second pass does not repeat it.

Reverting does not cleanly revert the database. If schema changes were involved, validate the schema against the code before continuing — see [backend.md](backend.md).

### 6. Start the piece over

When a project or feature is beyond untangling, rebuilding it with what you now know is often faster than repair. Keep the original as reference. Rebuild focused and in small verified increments, carrying over what worked and dropping what did not.

Reserve this for when steps 1–5 have genuinely failed, not as an escape from a hard diagnosis.

## Preventing the next loop

- **One change per step, verified before the next.** Batched changes make it impossible to tell which one caused the new failure, and that ambiguity is what loops are made of.
- **Say what not to touch** when working near fragile areas — authentication, payments, data migration. The fragile-area recipe is in [prompts.md](prompts.md).
- **Root cause before symptom, always.** A fix that silences an error without explaining it guarantees the error returns wearing a different face. If a null check was added, the question is why the value was null.
- **Record the resolution.** When a hard bug is finally solved, write down what it was and what fixed it. The next occurrence is then five minutes instead of an afternoon.

## When to stop and ask

Some failures are not yours to fix: a platform fault, an external service outage, a genuine product limitation. If the evidence points outside the project, say so with the evidence rather than continuing to edit code that is not the problem. Continuing to "fix" a working codebase against an external failure is how a small outage becomes a broken project.
