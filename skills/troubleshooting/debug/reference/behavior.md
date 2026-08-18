# Wrong behaviour: it runs, but does the wrong thing

No error, no crash — the app simply does not do what it should. Harder than a build error, because nothing points at the location. The whole method is to convert "wrong" into a specific divergence between expected and actual at a specific point.

## State the divergence first

Before reading code, write one sentence: **expected X, got Y, at Z.** If you cannot fill in all three, you are not ready to look for a cause. "The filter doesn't work" is not a divergence; "selecting Active still shows archived rows, on the projects list" is.

Then find the last point where things are provably right and the first where they are provably wrong. Everything outside that window is not the bug.

## A component or section disappeared

The most common post-refactor symptom, and it splits cleanly in two. Determine which before investigating further, because they lead in opposite directions.

**Is it rendering at all?** Put a log at the top of the component body — not inside a conditional, not in an effect.

- **Nothing logs.** The component is not mounted. The parent stopped rendering it: removed from the parent's markup during a refactor, an import dropped, a conditional wrapping it now evaluates false, or a route no longer matches. Look at the parent, not the component.
- **It logs.** The component mounts and returns nothing visible. Either it returns early on a condition that is now always true, it renders an empty collection, or it renders but is invisible — zero height, clipped by an ancestor, behind another element, or with no content because its data is empty.

Confirming which half you are in takes one log and eliminates half the search space. Do it before reading the component.

## It worked before the last change

The strongest lead available. Compare the current state against the last working version and read the diff — the cause is nearly always inside it, even when the change looks unrelated to the symptom.

Ask what changed between the two versions and what in that change could produce this specific symptom. Do not accept "nothing relevant changed": if behaviour changed, something did, and a shared component or a type edited for one feature is the classic invisible culprit.

If the diff is large, bisect. Revert half, test, repeat on the failing half. Slower to describe than to do, and it always terminates.

## State that will not update

The UI shows stale data after an action that should have changed it.

| Symptom | Usual cause |
|---|---|
| Action succeeds, UI unchanged until reload | Cached query never invalidated after the mutation |
| Value updates once, then stops | State initialised from a prop and never resynced when the prop changes |
| Update applies then reverts | Two sources of truth for the same value, and the second overwrites the first |
| Change visible in one place, not another | The same data held in two independent states rather than one shared source |
| Effect runs at the wrong time, or endlessly | Dependency list wrong — missing a value it reads, or containing one recreated every render |

The underlying question is always the same: **where does this value actually live, and who is allowed to change it?** Two answers to that question is the bug. The fix is a single source of truth, not another synchronising effect.

## Data arrives wrong rather than absent

The request succeeded and returned something, but not the right thing. Follow the pipeline in order and check the shape at each hop: query → response → transformation → state → props → render. The divergence has one specific edge.

Watch for the recurring shape traps: a number that arrives as a string, a date that is a string until parsed, a nullable column treated as always present, a field renamed on one side of the boundary only, an array that is empty rather than absent.

If the data is correct all the way to the component and still renders wrong, the bug is in rendering logic — a condition, a sort, a filter, a key — not in the data path.

## Role- and permission-dependent behaviour

If the app has roles, always establish **which role the user was in**. A shared component behaving correctly for one role and wrongly for another is a logic bug in the shared path, not a data problem, and testing as the wrong role produces a phantom bug that cannot be reproduced.

After any change to shared logic, re-check every role that touches it. This is the most common source of "fixed it, but broke it for someone else".

## When it will not narrow

If the divergence resists isolation, rebuild the failing piece minimally: a fresh, stripped version of that component with hard-coded data. If the minimal version works, reintroduce the real pieces one at a time until it breaks — the piece that breaks it is the cause. If the minimal version also fails, the cause is outside the component entirely.

If two attempts have already failed, stop here and continue in [loops.md](loops.md).
