# Scoping into buildable increments

Turning "add comments and likes" into something that can be built, checked, and corrected before it has grown roots.

## First, resolve the request

Most feature requests carry unstated assumptions, and every one of them is a bug waiting to be written confidently. Before decomposing anything, answer these — from the project where possible, from the user where not:

- **Who uses it, and in which role?** If the app has roles, a feature that ignores them produces the classic bug where shared logic behaves correctly for one role and wrongly for another.
- **What is the smallest version that is genuinely useful?** Not the smallest that technically exists — the smallest a real user would be glad to have.
- **What happens in the unhappy cases?** Empty, loading, failed, unauthorised, too much data, concurrent edits.
- **Does anything like this already exist?** In a grown project, half of new features are second implementations of something already there.
- **What must not change?** Existing behaviour that the new work sits next to and could break.

Ask about the ones that would change the design. Do not open a questionnaire — two or three questions that matter beat ten that do not. And where you assume rather than ask, **write the assumption into the plan** so the user can correct it in a sentence.

## Break it into bricks

One brick is one thing that can be built and verified on its own. The test of a good decomposition is that each step leaves the app working and demonstrably better than before.

A reliable order for most features:

1. **The data.** Schema, relationships, and access policies. First because everything above it depends on the shape, and changing it later means changing everything built on top.
2. **The read path.** Get the data on screen, in its plainest form, with real data rather than placeholders. Proves the schema and the query before any interaction exists.
3. **The write path.** One action, end to end, with validation server-side.
4. **The states.** Empty, loading, error. These are the ones that get skipped and the ones users hit first.
5. **The rest of the actions.** Edit, delete, and whatever else, one at a time.
6. **The polish.** Only once the thing works.

Each brick gets verified before the next starts. When something breaks, you know exactly which step caused it — which is the entire reason for building this way rather than all at once.

**Do not batch.** Five things implemented in one pass produce a failure that could have come from any of them, and untangling that costs more than the sequencing saved. If a plan step contains "and", it is probably two steps.

## Name what it touches

Before building, list what the work will reach:

- **Files and components**, especially shared ones — a change to something used in eight places is eight chances to regress.
- **The data model.** New tables need policies from the moment they exist, not later.
- **Existing behaviour** that could break, and which roles would notice.
- **The fragile areas** it comes near: auth, payments, migrations. If it touches one, say so explicitly and treat that brick with the caution the `debug` skill's fragile-area recipe describes.

## Say what it actually costs

When the user asks "what am I signing up for", they want the real answer, including the parts that are not code:

- The **increments and their rough order**, so the shape of the work is visible.
- **What gets harder afterwards.** A feature that adds a permission dimension makes every future feature slightly more complex, permanently.
- **What it commits you to** — data that will need migrating, a dependency that will need updating, a surface that will need maintaining.
- **What could go wrong**, and which brick carries the risk.

An honest cost, given before starting, is what lets someone decide to build half of it — which is frequently the right call and is unavailable once the work is underway.

## Hand off

End with the first brick, small enough to build and check immediately, and the explicit note that the plan is a proposal rather than a decision already taken.

Then stop. Planning that slides into implementation without the user agreeing to the plan has skipped the only step that made it worth doing.

## Handing a brick to the build

Once a brick is agreed, the request that implements it carries three things beyond the task itself.

**Expected behaviour, not just the feature.** "When the user clicks Add to Cart, show a success message and update the cart count in the header" is buildable. "Add a cart" is a guess.

**Context for anything non-obvious** — which existing component to use, which page to match the styling of, which pattern this should follow.

**Guardrails on anything fragile.** Name the files and areas that must not change:

> Add this to @src/pages/dashboard. Do not modify @src/shared/Layout.tsx or the existing authentication logic.

Naming specific paths is far more effective than "don't break anything", and it is the single cheapest protection against collateral edits. The `debug` skill's recipes carry longer forms for genuinely delicate areas.

## While it builds

**Queue the next steps rather than waiting.** Prompts sent during a build are queued visibly and processed in order, and can be reordered, edited, paused, or removed before they run. This is how the brick sequence gets executed without babysitting each step — but only queue bricks that do not depend on the outcome of the one running.

**Stop early when it goes wrong.** Stopping halts the current task and **keeps everything done up to that point** — the work is not lost, and the run is charged for what was completed. That makes stopping cheap: the moment a build is visibly heading the wrong way, stop it and add the missing context rather than letting it finish and then correcting a larger diff.

If the partial work is not wanted, undo reverts to the previous state.

**Watch the visible steps.** Which files are being touched is the earliest signal that a request was understood differently than intended — a brick that was supposed to touch one page opening shared components means the scope was read wider than you meant.
