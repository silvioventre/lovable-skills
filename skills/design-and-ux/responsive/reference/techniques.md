# Techniques: the modern responsive toolkit

Four tools cover nearly everything, and they divide the work cleanly:

| Tool | Owns |
|---|---|
| **Intrinsic layout** (grid/flex that adapts with no query) | layouts that need no breakpoint at all |
| **Container queries** | reusable components adapting to their slot |
| **Media queries** | page-level structure and device capability |
| **Fluid values** (`clamp()`) | type and spacing that scale continuously |

Reach for the highest row that solves the problem. Every breakpoint you avoid is a state you never have to test.

---

## Intrinsic layout: no query at all

The best responsive code has no breakpoints, because the layout adapts to available space by construction.

**Auto-fitting grid.** Cards reflow from four columns to one with no media query:

```html
<div class="grid gap-6 grid-cols-[repeat(auto-fit,minmax(min(100%,18rem),1fr))]">
```

The `min(100%, 18rem)` matters and is the part people omit. Plain `minmax(18rem, 1fr)` forces an 18rem minimum, which overflows at 320px. Wrapping it in `min(100%, …)` lets the track collapse below 18rem when the container is narrower than that, which is exactly the small-screen case.

**Flex that wraps on its own:**

```html
<div class="flex flex-wrap gap-4">
  <div class="flex-1 basis-64 min-w-0">…</div>
</div>
```

`basis-64` is the preferred width, `flex-1` lets it grow, wrapping happens when the basis no longer fits. `min-w-0` prevents the shrink-refusal described in [failures.md](failures.md).

**Sidebar that collapses when there is no room**, with no breakpoint:

```html
<div class="flex flex-wrap gap-8">
  <aside class="flex-1 basis-64 grow-0">…</aside>
  <main class="flex-1 basis-[30rem] min-w-0">…</main>
</div>
```

When the main region can no longer hold 30rem beside the sidebar, the two stack. The switch happens at the width the *content* requires, not at a number you guessed.

## Container queries: components that adapt to their slot

A media query asks how wide the *window* is. That is the wrong question for a component that appears in a full-width page, a half-width grid cell, and a narrow sidebar. Container queries ask how much room *this component* has.

```html
<div class="@container">
  <article class="flex flex-col @md:flex-row @md:items-center gap-4">
    <img class="w-full @md:w-40 rounded-lg" …>
    <div class="min-w-0">…</div>
  </article>
</div>
```

The card lays out vertically in a narrow slot and horizontally in a wide one, on the same page, at the same viewport width.

Use **named containers** when they nest, so a child does not accidentally query the wrong ancestor:

```html
<div class="@container/sidebar">
  <div class="@container/card">
    <div class="@lg/sidebar:hidden @sm/card:block">…</div>
```

Container breakpoints are not viewport breakpoints: `@md` is 448px of container width, while `md:` is 768px of viewport. Do not carry numbers across.

**The split:** media queries for the page shell and anything device-dependent; container queries for every component that gets reused in differently sized slots.

## Fluid values with `clamp()`

`clamp(MIN, PREFERRED, MAX)` scales continuously instead of jumping at breakpoints.

```css
font-size: clamp(2rem, 1.5rem + 2.5vw, 4rem);
```

Read it as: never below 2rem, never above 4rem, and in between it grows with the viewport. The `1.5rem +` base is what keeps it accessible — a preferred value in pure `vw` ignores the user's browser font-size setting, while a `rem + vw` sum still responds to it.

Same technique for spacing, which is what keeps rhythm proportional instead of leaving desktop-sized gaps on a phone:

```css
padding-block: clamp(3rem, 8vw, 8rem);
```

In Tailwind, either as an arbitrary value — `text-[clamp(2rem,1.5rem+2.5vw,4rem)]` — or, better for anything used more than once, as a theme token:

```css
@theme {
  --text-display: clamp(2rem, 1.5rem + 2.5vw, 4rem);
  --spacing-section: clamp(3rem, 8vw, 8rem);
}
```

Do not make everything fluid. Body copy wants a stable, comfortable size; display type and section spacing are where fluid scaling earns its keep.

## Viewport units

| Unit | Meaning | Use for |
|---|---|---|
| `dvh` | dynamic — tracks the browser chrome as it collapses | full-height sections, the common default |
| `svh` | small — viewport with chrome *visible* | content that must fit without the chrome hiding it |
| `lvh` | large — viewport with chrome hidden | backgrounds that should fill the largest state |
| `vh` | fixed, ignores chrome entirely | avoid on mobile; it is why hero sections get cut off |

```html
<section class="min-h-dvh">
```

Prefer `min-h-*` to `h-*` so content longer than the viewport still expands the box instead of overflowing it.

`vw` has its own trap: it includes the vertical scrollbar. See the `w-screen` row in [failures.md](failures.md).

## Safe areas

For devices with a notch, rounded corners, or a home indicator:

```html
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
```

```css
.app-shell {
  padding-top: max(1rem, env(safe-area-inset-top));
  padding-bottom: max(1rem, env(safe-area-inset-bottom));
}
```

The `max()` keeps your normal padding on devices with no inset, rather than collapsing to zero.

Fixed bottom bars need the bottom inset, or the home indicator sits on top of the controls.

## Input and capability queries

Screen width does not tell you the input method. A touchscreen laptop is wide *and* touch.

```css
@media (hover: hover) and (pointer: fine) {
  /* mouse: hover affordances are safe here */
}
@media (pointer: coarse) {
  /* touch: larger targets, no hover-dependent paths */
}
```

Gate hover-revealed controls behind `(hover: hover)` and give touch an explicit tap path. A control that only appears on hover is invisible on a phone.

Honour `prefers-reduced-motion` for any transform or parallax tied to scroll or breakpoint transitions.

## Text wrapping

```css
h1, h2, h3 { text-wrap: balance; }  /* even line lengths, no orphan word */
p          { text-wrap: pretty; }   /* avoids orphans and bad rag */
```

Tailwind: `text-balance` and `text-pretty`. Balance is intended for short headings; applying it to long body text is wasted work.

## Logical properties

`ms-4` / `me-4` / `ps-4` / `pe-4` and `border-s` / `border-e` follow the writing direction instead of the physical screen. If the product will ever ship in Arabic or Hebrew, logical properties mean the layout mirrors correctly instead of needing a parallel RTL stylesheet.

## `aspect-ratio`

```html
<div class="aspect-video w-full">
```

Replaces the padding-top percentage hack, and reserves space so media loading does not shift the layout.
