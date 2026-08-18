---
name: test
description: Use when the user wants to verify that something works, prove a fix, or protect behaviour from breaking later — "test this", "write tests for the login form", "verify the checkout flow works", "does this actually work", "check it end to end", "make sure this doesn't break again", "add test coverage", "call that function with a bad input". Routes the request to the right verification tool for the kind of behaviour being checked — browser testing for real user flows, frontend tests for UI logic, direct calls and edge tests for backend rules. Not for diagnosing a failure whose cause is unknown, which the debug skill covers first.
---

# Test

Pick the tool that matches the kind of behaviour being verified. Using the wrong one is how verification becomes slow, flaky, and eventually ignored.

## Route by what you are verifying

| What you want to check | Tool | Playbook |
|---|---|---|
| A real user flow, end to end | Browser testing | [reference/browser.md](reference/browser.md) |
| Something visibly broken to users | Browser testing | [reference/browser.md](reference/browser.md) |
| UI logic — conditional rendering, forms, filters, tables | Frontend tests | [reference/frontend-tests.md](reference/frontend-tests.md) |
| A UI regression you want to prevent returning | Frontend tests | [reference/frontend-tests.md](reference/frontend-tests.md) |
| A backend rule with a specific input | Direct edge call | [reference/backend-tests.md](reference/backend-tests.md) |
| Business rules or permissions over time | Edge tests | [reference/backend-tests.md](reference/backend-tests.md) |
| What is worth testing at all | — | [reference/what-to-test.md](reference/what-to-test.md) |

The short version of the heuristic: **if the issue is visible to users, use browser testing; if a rule should stay true over time, write a test; if it is backend logic, call the function directly first.**

## Two kinds of verification

Everything here is one of two things, and confusing them produces bad tests.

- **Checking a complete flow.** Does sign-up actually work, start to finish, the way a person would do it? Slow, broad, catches integration failures nothing else catches.
- **Checking one rule in isolation.** Given this input, does this component or function produce that output? Fast, narrow, precise about what broke.

You need both, for different things. A suite of only flow tests is slow and vague about failures; a suite of only isolated tests passes completely while the app is unusable.

## The rules

**Reproduce before you fix, confirm after.** The sequence that makes verification worth its cost:

1. Reproduce the failure with a specific input, and observe it.
2. Apply the fix.
3. Run the same input again and confirm the behaviour changed.
4. Add a test so it cannot regress silently.

Step 1 is the one that gets skipped. A fix applied to a failure you never actually observed is a guess, and step 3 cannot tell you anything if you never established what step 1 looked like.

**A test that has never failed has proven nothing.** Write it so you have seen it go red for the right reason — against the broken code, or by temporarily breaking the thing it covers. A test that passes against both working and broken code is worse than no test, because it is trusted.

**Verification runs when asked.** These tools are not automatic. If a change deserves verification, run it or say plainly that it was not verified. Never report work as tested because tests exist in the project.

**Never change a test to make it pass.** A failing test is either a real regression or a wrong test, and those need opposite responses. Decide which before touching it. Loosening an assertion to get green converts a caught bug into a hidden one.

## What gets observed

When these tools run, the following is available and is usually enough to diagnose a failure without extra instrumentation: browser console logs, network requests, test failures and build errors, and request and response data from direct backend calls.

Read that output before adding logging of your own. The evidence is frequently already there.

## Report

1. **What was verified**, and with which tool.
2. **The result** — passing, failing, with the actual output for failures.
3. **What was not verified**, explicitly. An untested path is a known gap, not a silent one.
4. **What was added**, if tests were written, and what would make each one fail.
