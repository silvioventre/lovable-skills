# Choosing an approach

For when there is a genuine decision to make and the wrong answer is expensive to reverse. Not every task needs this — most have one obvious way, and deliberating over them is its own kind of waste.

## Is there actually a choice?

Run this filter first. An approach comparison is warranted when at least one holds:

- The decision is **hard to reverse** — a data model, an auth strategy, a dependency that will spread.
- The options have **genuinely different consequences**, not just different syntax.
- It **touches something fragile**: payments, permissions, migrations, anything users depend on.
- The user asked, which means they have a doubt worth resolving.

If none holds, pick the approach that matches what the project already does and move on. Consistency with the existing codebase beats a marginally better pattern introduced alone.

## Investigate before comparing

Options compared in the abstract produce a generically correct answer that may not fit this project at all.

Establish first: what the codebase already does for similar problems, what is already installed that could serve, what constraints exist (data model, auth, plan limits), and what the user has already ruled out.

Where external knowledge would help — how a pattern is normally built, what the common failure modes are — delegate that research alongside the codebase inspection rather than after it. They are independent questions and can run at once.

## Make the options genuinely different

Two or three, and they must fail for different reasons. Three variants of the same design is one option described three ways, and it produces a decision that was never really made.

For each, state:

- **How it works**, in one or two sentences.
- **What it costs** — effort, new dependencies, complexity added permanently.
- **What it constrains later.** The most important line and the one usually missing. Every approach closes doors; say which.
- **How it fails.** Not whether, but how — and whether the failure is loud or quiet. A quiet failure mode is a much bigger cost than a slightly higher build effort.
- **Whether it fits this project**, given what you found.

Then **recommend one and say why.** A comparison without a recommendation pushes the decision back to someone with less context than you now have. Recommending is not deciding — the user still chooses.

## Bias toward the reversible

When options are close, prefer the one that is easier to undo. A reversible choice made quickly beats an irreversible choice deliberated at length, because the information that would settle it usually arrives only after building.

Corollary: it is worth spending real time on the decisions that are actually hard to reverse — the data model, how identity works, what the app fundamentally is — and very little on the ones that are not.

## Adding a dependency

A recurring version of this decision, and one people get wrong in both directions.

A package is worth it when it solves a genuinely hard problem — drag and drop, rich text, date handling, charting — that would take real effort and be worse hand-rolled.

A package is not worth it for something a small amount of project code would do, because you inherit its bugs, its update cadence, its bundle size, and its eventual abandonment permanently.

Before adopting one, check that it is actually maintained: recent releases, issues being answered, real usage. An unmaintained package for a solved problem is a future migration you have scheduled without noticing.

## Then scope it

An approach is not a plan. Once chosen, break it into increments — [scope.md](scope.md) — and do not let the decision itself become the deliverable.
