# Triage: the first five minutes

Run this before opening any file. Most wasted debugging time is spent fixing a cause that was never established.

## Gather the evidence

Collect all six before forming a hypothesis. Anything you cannot get, name explicitly as missing — a gap you know about is manageable, a gap you assumed away is not.

1. **The exact error text.** Verbatim, not paraphrased. Stack trace and file/line if present. If the user described the error in prose, ask for the actual text or read it from the console yourself.
2. **Where it appears.** Build output, browser console, network tab, edge function logs, or only visible in the UI. The location narrows the layer before you read a single line of code.
3. **What the user expected.** Without this you cannot tell a bug from a misunderstanding about intended behaviour.
4. **What actually happened.** Specifically. "It doesn't work" is not a symptom; "the list renders empty although three rows exist in the table" is.
5. **When it last worked.** The change between the last good state and now is the highest-value clue in the whole process. If it never worked, say so — that is a different investigation.
6. **What has already been tried.** Including automatic fix attempts. Repeating a failed fix is common and completely wasted.

## Classify the failure

The class determines the playbook. Ask in this order — the first yes wins.

| Question | If yes | Class |
|---|---|---|
| Does the app fail to build, or render nothing at all? | [build-and-preview.md](build-and-preview.md) | Hard failure |
| Is there a server-side error — function, database, auth, permissions? | [backend.md](backend.md) | Backend failure |
| Does it run without errors but do the wrong thing? | [behavior.md](behavior.md) | Logic failure |
| Has this been fixed and come back, or resisted two attempts? | [loops.md](loops.md) | Systemic |

A hard failure outranks everything: a project that will not build cannot be reasoned about, so clear that first even when the interesting bug is elsewhere.

## Narrow before you read

Two questions cut the search space faster than reading code:

**Which layer?** Data arrives from the database, through an API or function, into state, then into render. Find the last point where the data is provably correct and the first where it is provably wrong. The bug is between them. A log at each boundary answers in one pass what code reading answers in twenty minutes.

**Which change?** If it worked before, compare the current state against the last working version and read the diff. The cause is nearly always inside it. Ask directly what changed between the two versions and what in that change could produce this symptom.

## Form more than one hypothesis

Write down at least two possible causes before testing any of them. A single hypothesis becomes the conclusion by default, and the first plausible explanation is frequently not the right one — especially when a standard fix does not work.

Then invert the question. Instead of "why is this broken", ask **"under what conditions would this behaviour be correct?"** If a list renders empty, empty is the correct rendering for an empty array — so the question becomes why the array is empty, which is a different and more tractable search.

Test each hypothesis with something that can disprove it. A log, a temporary hard-coded value, a narrowed query. Evidence that only confirms what you already believe has told you nothing.

## Before you leave triage

You should be able to state, in one sentence: *the symptom is X, caused by Y, which I confirmed by Z.* If the sentence has a gap, stay in triage. A fix applied over a gap in that sentence is a guess.
