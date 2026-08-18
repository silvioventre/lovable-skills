# What is worth testing

Tests cost time to write and time to maintain, and a suite nobody trusts is worse than no suite — it consumes both while protecting nothing. The question is never "should we test", it is "does this test earn its keep".

## The test that always earns it

**The bug you just fixed.** A bug that happened once can happen again, and the fix is fresh in your mind right now in a way it never will be later. This is the highest-value test in any project, and the cheapest to write.

Write it against the specific failure, not a generalisation of it.

## Earns it

- **Rules with a right and wrong answer.** Pricing, permissions, validation, calculations, state transitions. Anything where being subtly wrong is expensive and invisible.
- **Anything involving money or access.** A quiet failure here costs more than the whole suite.
- **Conditional logic with several branches.** Every branch is a case that only runs sometimes, which means only sometimes noticed.
- **The core flow the product exists for.** One browser test, end to end.
- **Sign-up and sign-in.** Broken auth means nobody can use anything else.
- **Anything that has broken twice.** A second occurrence is the code telling you it is fragile.

## Does not earn it

- **Pure presentation.** A component that renders props with no logic. The test restates the markup and breaks on every design change.
- **Wrappers and pass-throughs.** Nothing to assert that is not the framework's job.
- **Configuration and constants.** Asserting a value equals itself.
- **Behaviour that is about to change.** Testing an implementation you plan to replace next week is work thrown away twice.
- **Coverage for its own sake.** A percentage target produces tests written to raise a number, which are the worst tests in any codebase.

## The order to build coverage in

If a project has no tests and you are starting:

1. **One browser test on the core flow.** Broad, slow, catches whole classes of breakage. Highest value per test in the project.
2. **Backend tests on rules involving money, permissions, or data access.** Expensive failures, quiet symptoms.
3. **Frontend tests on the components with real branching logic** — forms, filters, permission-dependent rendering.
4. **A regression test for each bug as it is fixed**, from now on.

Step 4 is the one that compounds. Do it consistently and the suite grows to match where the project actually breaks, which no amount of upfront planning achieves.

## Signals a test is not worth keeping

- **It fails intermittently.** A flaky test trains people to ignore red, which costs more than the test protects. Fix it or delete it — leaving it is the only wrong answer.
- **It breaks on every refactor while the app still works.** Bound to implementation. Rewrite it against behaviour or drop it.
- **Nobody can say what it protects.** If its failure would not tell you anything actionable, it is not verification, it is ceremony.
- **It has never failed.** Possibly excellent, possibly asserting nothing. Break the behaviour deliberately once and find out.

## Do not test everything for every change

Most changes need one kind of verification, not all four. Match the tool to the risk:

- Changed a component's rendering → the frontend test for that component.
- Changed a backend rule → call it directly, then the edge test.
- Changed something that spans layers, or touched auth or routing → a browser test on the affected flow.
- Changed copy, styling, or spacing → look at it. Not everything needs an automated test.

Running the full suite for a text change is a habit that makes verification feel expensive, and expensive verification gets skipped when it matters.
