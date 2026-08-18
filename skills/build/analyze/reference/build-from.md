# Building from a file or a finding

The most valuable thing this capability does: the analysis and the build happen in one conversation, so what was learned can become what gets built without re-explaining it.

Three shapes recur.

## From a data file

A spreadsheet someone has been maintaining by hand becomes an app.

The file is not just data — **it is a specification of how someone actually works**, written by the person who does the work. The columns are the fields they care about, the sheets are the workflows, the colour-coding and the notes column are the rules nobody wrote down. Read it as a requirements document, not as an import.

Before building:

- **What does one row represent**, and what is the real entity behind it?
- **Which columns are entered, which are derived?** Derived ones become computed rather than stored fields.
- **What do the ad-hoc conventions encode?** A highlighted row, a suffix in a name, a notes column with recurring phrases — each is a status or a category the app should model properly.
- **Who else touches this file?** That determines whether roles and permissions are in scope.
- **What is painful about the current version?** The answer names the feature that justifies the whole build.

Then hand off to `plan` for scoping rather than building the whole thing at once. A spreadsheet turned into an app in a single pass produces a faithful reproduction of the spreadsheet, including its problems.

**Import the real data early**, in an increment of its own. Real data breaks assumptions that clean sample data never does — inconsistent formats, missing values, entries that violate the rules the file appeared to follow.

## From a specification document

A PDF or document describing what to build.

**Summarise the requirements back before building anything.** Specifications contain contradictions, gaps, and requirements that are decisions rather than facts. Reading it back surfaces those while they are cheap.

Separate explicitly:

- **What the document states.**
- **What it implies but does not say** — the states, errors, and edge cases specifications routinely omit.
- **What it leaves open**, which must be decided by someone.
- **What conflicts** with itself or with the existing app.

Then build the first version of one part, not all of it. A specification implemented wholesale is a specification whose misreadings all ship together.

## From an analysis

The strongest form, because the finding motivates the change and the evidence is already present.

A drop-off analysis becomes a reworked onboarding. A revenue breakdown becomes a dashboard. A usage pattern becomes a feature.

Two disciplines keep this honest:

**Make the causal claim explicit before acting on it.** "Users drop at step 3" is an observation; "step 3 asks for information users do not have yet" is a hypothesis about why, and the redesign follows from the second, not the first. State the hypothesis so it can be challenged before it becomes work.

**Decide how you will know it worked.** The same analysis that motivated the change can measure it afterwards — but only if the metric is named now. A change shipped on the strength of data, with no plan to re-measure, is data used as decoration.

## Where this hands off

This skill covers reading the source and understanding what it asks for. Turning that into a scoped sequence of increments is the `plan` skill, and it should be used for anything beyond a single small feature.

The reason to hand off rather than continue: everything learned here is context, and context is exactly what makes a plan good. Do not lose it by building immediately — carry it into the planning step.
