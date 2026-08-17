---
name: responsive
description: Use when the user wants an app, site, page, or component to work correctly on every screen size — "make it responsive", "fix it on mobile", "it breaks on my phone", "it doesn't look right on tablet", "there's horizontal scrolling", "the layout overflows", "make it work on small screens", "test it at different breakpoints", "adapt it to any device". Covers auditing every width from 320px up, diagnosing overflow and reflow failures, applying fluid type and container queries, meeting touch-target and zoom accessibility requirements, and verifying the result against a pass gate. This is execution and verification rather than visual redesign — use it to make a layout actually work at every size, not to decide what the experience should be.
---

# Responsive

Make the target work correctly at every screen size, then prove it. This is a mechanical discipline with a pass/fail gate, not a matter of taste — a layout either survives 320px and 400% zoom or it does not.

**Responsive is not "it has breakpoints."** A page with `md:` and `lg:` variants everywhere can still fail every gate below. What counts is measured behavior at real widths.

## The gate

The work is done when all seven hold on every surface in scope. Report each one explicitly; never claim "responsive" without walking this list.

1. **No horizontal scroll** at any width from 320px upward. Not hidden — absent.
2. **Content reflows at 320px** with nothing lost or unreachable (WCAG 1.4.10). Two-dimensional content — data tables, maps, diagrams, code — may scroll inside its own container.
3. **Usable at 400% zoom** on a 1280px viewport, which is the same 320 CSS px reflow requirement reached the other way. Test both; they expose different bugs.
4. **Every interactive target is at least 24×24 CSS px** (WCAG 2.2 AA, SC 2.5.8), or has 24px of clear spacing around it. Primary touch actions get 44×44.
5. **Body text is at least 16px on mobile.** Below that, iOS Safari zooms the whole page when a field takes focus.
6. **No fixed heights on anything containing text.** Text grows with translation, user font settings, and long content.
7. **No content under the notch, home indicator, or browser chrome** on devices that have them.

A gate item you could not verify is reported as unverified, never as passed.

## Procedure

### 1. Scope and map

Name the surfaces in scope. If the user said "the whole app," list the routes and confirm the list rather than sweeping silently — a full app sweep is many surfaces, and they should know what you are about to touch.

For each surface, note which of its regions are structural (page shell, navigation, main grid) and which are components that get reused in different-sized slots. Structural regions belong to media queries; reusable components belong to container queries. Getting this split right prevents most of the churn.

### 2. Sweep

Inspect each surface in the preview at this ladder, in this order:

| Width | What it represents | What it catches |
|---|---|---|
| **320px** | WCAG reflow floor, smallest real phone | overflow, unbreakable strings, cramped targets |
| **390px** | the common phone | real-world mobile layout |
| **768px** | tablet portrait | the awkward middle where layouts collapse badly |
| **1024px** | tablet landscape, small laptop | premature desktop layout |
| **1440px** | standard desktop | the intended design |
| **1920px+** | large desktop | unbounded line lengths, stretched containers |

Then two more passes that are not widths:

- **400% zoom at 1280px.** Catches what narrow-viewport testing misses, because zoom scales text and spacing together.
- **The in-between drag.** Move slowly through the range rather than sampling the six fixed widths. Breakage clusters just before and after breakpoints, which is exactly where fixed-width testing has blind spots.

At each stop, check in this order: horizontal overflow first (it invalidates everything else), then reading order and grouping, then touch targets, then text truncation and wrapping, then images and media, then sticky and fixed elements, then interactive states.

Record every failure with its width, its file, and the element. A failure without a location is not actionable.

### 3. Diagnose

Route each failure through [reference/failures.md](reference/failures.md), which maps symptoms to causes to fixes. Find the actual cause before editing. The same symptom — horizontal scroll — has a dozen distinct causes, and the fix for one makes another worse.

**Never apply `overflow-x: hidden` to `body` or `html`.** It hides the symptom, leaves the offending element still overflowing and unreachable, and silently breaks `position: sticky` on every descendant. If you find it already there, treat it as a bug to remove and fix underneath, not as a solution.

### 4. Fix

- **Mobile-first.** Base styles describe the smallest screen; every variant adds capability upward. In Tailwind, unprefixed utilities are the mobile state and `md:` / `lg:` layer on top. Writing desktop styles as the base and overriding them downward is how a codebase accumulates specificity fights.
- **Fix at the source.** A width constraint belongs on the element that owns the width, not on an ancestor patched to contain it.
- **Prefer the intrinsic solution to the breakpoint.** Techniques in [reference/techniques.md](reference/techniques.md) — fluid `clamp()` type, intrinsic grid, container queries — remove whole classes of breakpoint. Reach for a media query when the layout genuinely changes structure, not to nudge a value.
- **Preserve the design.** This skill makes the existing design work at every size. If the layout needs a different structure on mobile because the experience should genuinely differ there, that is a design decision — say so and hand off, do not redesign under the banner of a responsive fix.
- **One concern per change.** Overflow fixes, target-size fixes, and type-scale fixes touch different properties; batching them makes regressions untraceable.

### 5. Verify

Re-sweep the full ladder from step 2 on everything you touched. A fix that resolves 320px and breaks 768px is common enough that the re-sweep is not optional.

Then report the gate: each of the seven items with pass, fail, or unverified, and for anything not passing, what remains and where. See [reference/checklist.md](reference/checklist.md) for the full verification protocol and the report format.

## Scope boundaries

- **Not visual redesign.** Preserve the identity, palette, type, and component character. If they need to change, that is the `art-direction` skill's job.
- **Not a native-app skill.** This covers web and mobile web. Native iOS/Android layout follows platform conventions instead.
- **Not performance work**, except where a responsive decision causes it: oversized images served to phones, layout shift from unreserved media, and hidden-but-loaded desktop markup are in scope precisely because they are responsive failures.
