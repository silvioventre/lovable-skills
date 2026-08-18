# Investigation recipes

Reusable request patterns for the situations the playbooks call for. Each one exists to constrain what happens next — most of them by preventing code from being written before the problem is understood.

## Investigate without editing

The single most useful pattern in this skill. Use it whenever the cause is not yet established, and always after a failed fix.

> Investigate this issue but do not write or change any code yet.
> Identify the root cause and explain how you confirmed it.
> If more than one cause is plausible, list each with the evidence for and against.
> Tell me what you would change and why, and wait for my go-ahead.

Why it works: it separates diagnosis from repair. Most bad fixes come from editing while the cause is still a guess, and once code has changed, the evidence about the original state is gone.

## Three approaches, no code

For when the cause is understood but the fix keeps failing, or before committing to a non-trivial implementation.

> Suggest three genuinely different ways to solve this — not three variants of the same approach.
> For each: how it works, what it costs, what could go wrong, and what it would touch.
> Recommend one and say why. Do not change anything yet.

The bar for "different" is that each would fail for different reasons. Three flavours of the same design is one approach.

## Fragile-area change

Before touching authentication, payments, data migration, permissions, or anything where a small mistake is expensive.

> This change is in a critical part of the app. Proceed with care.
> Examine all related code and dependencies before changing anything.
> Do not modify unrelated components or files.
> If anything is uncertain, stop and explain before continuing.
> State explicitly what you left untouched.
> Task: [the change]

This does not find bugs — it prevents them. The value is in setting the approach before work starts, and in the explicit account of what was deliberately not touched.

## Guardrails on a normal change

Attach to any request where collateral edits are a risk.

> Change only what is needed for this. Do not touch [specific files or areas].
> Preserve the existing naming, patterns, and structure.
> Show the change as a minimal diff, not a rewrite.
> If you spot other improvements, list them separately instead of implementing them.

Naming the off-limits files explicitly is far more reliable than "don't break anything".

## Codebase audit

For a project that has grown tangled, when no single symptom is the problem.

> Audit the codebase for structure and maintainability. This is read-only — do not change any code.
> - Files, components, or logic in the wrong place, or that would be better modularised
> - Whether separation of concerns holds: data handling vs UI vs business logic
> - Areas that are overly complex or diverging from the patterns used elsewhere
> - Duplicated components or logic that should be shared
> Give specific recommendations, ordered from most to least important.

Note the overlap: for dead code, unused dependencies, and an approval-gated cleanup, the `lovable-codebase-audit-cleanup` skill covers that ground in more depth. Use this recipe for a quick structural read, that skill for a real cleanup.

## Performance audit

When the app works but feels slow. Diagnosis only — do not let it start optimising.

> The app is functional but sluggish. Analyse it for performance problems and report back without changing code.
> - Unnecessary or duplicated data fetching, and requests that could be batched or cached
> - Components re-rendering more than they need to, or doing heavy work on every render
> - Large assets and bundles, and anything that could be split or loaded lazily
> - Anything blocking first render
> List the findings in priority order, with the cost and risk of each fix.

Then implement one finding at a time and measure. Batched optimisations cannot be attributed, and half of them usually do nothing.

## Explain the fix

After a fix lands, especially a non-obvious one.

> Explain what the actual cause was, why it produced this symptom, and why this change resolves it.
> Was this the root cause or a mitigation? If a mitigation, what remains unfixed underneath?

The last question is the one that matters. It catches the fix that silences a symptom and leaves the real defect in place, which is otherwise only discovered when it resurfaces.

## Summarise the session

At the end of a difficult debugging session.

> Summarise what the issue was, what we tried, what actually fixed it, and anything still unresolved.

Worth saving into project knowledge or a note. The next occurrence becomes minutes instead of a repeat of the whole investigation.

## What not to send

- **"Nothing works, fix it."** No symptom, no location, no expectation. Guarantees a guess.
- **"Try again."** After a failed fix, repeating the request repeats the failure. Change the approach, not the phrasing.
- **Several unrelated problems in one message.** They interleave, fixes collide, and attribution is lost. One problem per request.
- **A paraphrased error.** Send the actual text. The exact wording is frequently the whole diagnosis.
