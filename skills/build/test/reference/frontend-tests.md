# Frontend tests: UI logic in isolation

Automated tests that verify UI behaviour with explicit assertions, in a simulated browser. Fast, deterministic, and cheap enough to run constantly.

**Stack:** Vitest, React Testing Library, jsdom. Tests usually live beside the component as `.test.tsx`.

## When it is the right tool

- The expectation can be stated as a rule: *given this state, this should be visible / disabled / calculated this way.*
- You are fixing a UI regression and want it locked down so it cannot come back.
- The logic is conditional or stateful — forms, tables, filters, multi-step state, permission-dependent rendering.
- You want feedback in seconds rather than a full browser run.

If the thing you want to check requires the real app, the real backend, and a real session, this is the wrong tool — use [browser.md](browser.md).

## Test behaviour, not implementation

The rule that determines whether these tests are an asset or a liability.

**Query the way a user finds things**: by visible text, by label, by role. Not by class name, not by component internals, not by test-only selectors unless nothing else identifies the element.

**Assert what the user would observe**: what is on screen, what is disabled, what happened after the click. Not which internal state changed, not which function was called, not how many times something rendered.

The reason is practical, not ideological. A test bound to implementation breaks on every refactor while the app still works perfectly, and a suite that cries wolf gets disabled. A test bound to behaviour survives refactoring and fails only when something real broke — which is the entire point.

## What to cover in a component

Not every component. For those that earn tests (see [what-to-test.md](what-to-test.md)), cover:

- **The conditional branches.** Each state that renders something different: empty, loading, error, populated, permission-denied.
- **The rules.** Validation, calculations, formatting, sorting, filtering — anything with a right and wrong answer.
- **The edges.** Empty collections, a single item, very long strings, null and undefined where the type permits them, zero and negative numbers.
- **The interactions that matter.** Submitting a form, toggling a filter, selecting an option — and what should be true afterwards.

Skip: pure presentation with no logic, wrappers that only pass props through, and anything whose test would just restate the markup.

## Writing one that is worth keeping

**One behaviour per test.** A test asserting six things fails at the first and tells you nothing about the other five.

**Name it as the rule it protects.** "shows validation error when email is missing" — so a failure in CI reports what broke, not that `LoginForm test 3` failed.

**Make the setup obvious.** A reader should see the starting state and the action without following helpers. Shared setup that hides what a test actually does is how suites become unmaintainable.

**Watch it fail first.** Run it against the broken code, or break the behaviour temporarily. A test that has only ever been green may be asserting nothing — this happens more often than people expect, and it is undetectable afterwards.

## When a test fails

Decide which of two things happened before touching anything:

- **A real regression.** The code changed and broke the behaviour. Fix the code.
- **A wrong test.** The behaviour changed deliberately, or the test was bound to implementation and a refactor moved it. Fix the test — and if it was implementation-bound, rewrite it against behaviour rather than just updating the selector.

**Never loosen an assertion to get green.** That converts a caught regression into a hidden one, and the next person to read the suite will trust it.

## Where they fit

These prove rules hold. They do not prove the app works — a full suite can pass while sign-in is broken, because nothing in it exercises the real assembly. Pair them with a browser test on the flows that matter.
