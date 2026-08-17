# Failure catalog: symptom → cause → fix

Find the actual cause before editing. Most responsive bugs present as the same symptom — horizontal scroll — from a dozen unrelated causes, and the fix for one can worsen another.

Examples are Tailwind, since that is what Lovable builds with. The plain-CSS equivalent is noted where the utility name obscures it.

---

## Finding an overflow's source

Before consulting the table, locate the offending element. In order of speed:

1. **Narrow the preview to 320px and look for what extends past the edge.** Often visible immediately.
2. **Outline everything.** Temporarily add `* { outline: 1px solid red }` and scan for a box crossing the boundary. Remove it after.
3. **Bisect.** Comment out half the page's sections, check, repeat on the failing half. Reliable when the culprit is invisible (a transparent or absolutely positioned element).
4. **Walk the DOM upward** from the widest visible element, checking each ancestor's computed width against the viewport.

An overflowing element is almost never the one that *looks* too wide — it is usually a parent that cannot shrink, or a transparent absolutely positioned element with no containment.

---

## Horizontal overflow

| Symptom | Cause | Fix |
|---|---|---|
| Flex row overflows; a child refuses to shrink below its content | Flex items default to `min-width: auto`, so they will not shrink past their intrinsic content width. **This is the single most common cause.** | Add `min-w-0` to the flex child that should shrink. For truncation, `min-w-0` is required *in addition to* `truncate`. |
| Grid column blows out past its track | `1fr` is shorthand for `minmax(auto, 1fr)`, and `auto` will not go below content width | Use `grid-cols-[minmax(0,1fr)]`, or add `min-w-0` to the grid child |
| Full-bleed section causes scroll on desktop only | `w-screen` / `100vw` includes the vertical scrollbar's width; the element starts at the content edge and overhangs by that amount | Use `w-full`. For genuine full-bleed inside a padded container, `w-full` plus negative margins matched to the container padding, or set `body { container-type: inline-size }` and use `100cqw` |
| Element wider than the phone | Fixed width: `w-[400px]`, `min-w-[600px]` | `w-full max-w-[400px]` — cap the width, never floor it |
| A long URL, email, hash, or token pushes the layout out | Unbreakable strings do not wrap at any width | `break-words` (`overflow-wrap: anywhere` for the hardest cases). On a flex child, pair with `min-w-0` |
| A row of buttons or tags overflows instead of wrapping | `whitespace-nowrap` or `flex-nowrap` on content that should wrap | `flex-wrap` on the container; keep `whitespace-nowrap` only on individual labels that must not break mid-phrase |
| A decorative blob, glow, or rotated element causes scroll | Absolutely positioned element extending past the viewport with no containing ancestor clipping it | `overflow-hidden` on its nearest positioned ancestor — **the section, never `body`** |
| Negative margins pull content past the edge | `-mx-*` larger than the parent's padding at small widths | Make the negative margin responsive, or restructure so the parent owns the bleed |
| Table overflows | Tables have an intrinsic minimum width and will not reflow | Wrap in `<div class="overflow-x-auto">`. Two-dimensional data is explicitly allowed to scroll under WCAG 1.4.10 — do not force it to stack |
| `<pre>` or code block overflows | Preformatted text does not wrap by design | Wrapper with `overflow-x-auto`, or `whitespace-pre-wrap break-words` when wrapping is acceptable |
| Element with `w-full` overflows its padded parent | `box-sizing: content-box` somewhere, so padding adds to the declared width | `box-border` (Tailwind's preflight sets this globally; a stray `box-content` or third-party stylesheet is the usual culprit) |
| Gaps between wrapped items are wrong or cause overflow | `space-x-*` applies margins that do not account for wrapping | Use `gap-*` on a flex or grid container. `gap` is wrap-aware; `space-x` is not |
| Auto-fit grid overflows on narrow screens | `repeat(auto-fit, minmax(20rem, 1fr))` forces a 20rem minimum even at 320px | `repeat(auto-fit, minmax(min(100%, 20rem), 1fr))` — the `min(100%, …)` is what makes it safe |

## Text and reflow

| Symptom | Cause | Fix |
|---|---|---|
| Text clipped or overlapping its container | Fixed height on a text container | Remove the height; use `min-h-*` if a floor is needed |
| Heading breaks awkwardly, one word on the last line | No wrap balancing | `text-balance` on headings, `text-pretty` on body copy |
| Line length uncomfortable on wide screens | No maximum measure | `max-w-prose` or `max-w-[65ch]` on reading content |
| Layout breaks in another language | Text expansion — German and Finnish run 30–40% longer than English | Never size containers to the current string; test with the longest expected translation |
| Layout breaks with browser font-size overrides or at 400% zoom | Sizes in `px` that ignore user settings | `rem` for type and spacing that should scale with user preference |
| Text unreadably small on mobile | Type scaled down at breakpoints below the floor | 16px minimum for body. A field below 16px makes iOS Safari zoom the page on focus |
| Type jumps abruptly between breakpoints | Discrete sizes per breakpoint | Fluid type with `clamp()` — see [techniques.md](techniques.md) |

## Layout structure

| Symptom | Cause | Fix |
|---|---|---|
| Looks fine at 375px and 1440px, broken at 768–900px | Only two breakpoints considered; the middle was never designed | Sweep the in-between range; the tablet width is where most layouts fail |
| A component breaks in a sidebar but works on a full-width page | Media queries respond to the viewport, not to the space the component occupies | Container queries — see [techniques.md](techniques.md) |
| Content stacks in the wrong order on mobile | Visual reordering via `order-*`, `flex-row-reverse`, or grid placement that DOM order does not match | Fix the DOM order. Keyboard and screen-reader order follow the DOM, so visual reordering that diverges from it is an accessibility failure, not just a layout preference |
| Everything is centered and reads as a single undifferentiated column on mobile | Default centering with no hierarchy | Alignment should express grouping; centering everything removes the signal |
| Sidebar or modal unusable on small screens | Desktop pattern applied unchanged | Sheet, drawer, or full-screen at mobile widths |
| Huge empty space on large screens | No maximum container width | `max-w-7xl mx-auto` or equivalent on the page shell |

## Touch and interaction

| Symptom | Cause | Fix |
|---|---|---|
| Icon buttons hard to hit | Target smaller than 24×24 CSS px | Pad the target to at least 24×24 (44×44 for primary actions). The *hit area* must grow, not only the icon — `p-*` on the button, not a bigger glyph |
| Adjacent targets misfire | Targets meet the size floor but touch each other | 24px of clear space between targets, or make each larger |
| Feature unreachable on touch | Hover-only affordance — a menu, tooltip, or control that appears on `:hover` | Provide a tap path. Gate hover enhancements behind `@media (hover: hover)` so touch devices get the accessible variant |
| Fixed bottom bar covered by the mobile keyboard | `position: fixed` does not account for the virtual keyboard | Use `dvh` units, or the `VirtualKeyboard` API where the pattern demands precision. Verify with a focused field |
| Sticky header stops sticking | An ancestor has `overflow-x: hidden` (or any `overflow` other than `visible`) | Remove the overflow from the ancestor and fix the real overflow cause |
| Scroll traps inside a modal or drawer | Nested scroll containers without scroll containment | `overscroll-contain` on the inner scroller |

## Images and media

| Symptom | Cause | Fix |
|---|---|---|
| Image overflows the container | No maximum width | `max-w-full h-auto`. Tailwind preflight handles this for bare `<img>`; wrapped or background images often escape it |
| Layout shifts as images load | No reserved space | `aspect-ratio` on the container, or explicit `width` and `height` attributes on the image |
| Phones download a desktop-sized image | One source for all widths | `srcset` and `sizes`, or a responsive image component. This is a responsive failure, not only a performance one |
| Embed or iframe overflows | Fixed dimensions | Wrapper with `aspect-video` (or the correct ratio) and `w-full h-full` on the iframe |
| Background image crops the subject on mobile | `background-size: cover` with a centre focal point | `object-position` / `background-position` tuned per breakpoint, or a differently cropped source for narrow screens |

## Viewport and device chrome

| Symptom | Cause | Fix |
|---|---|---|
| Full-height section cut off, or a scrollbar appears when mobile browser chrome retracts | `h-screen` / `100vh` is a fixed value that ignores the collapsing address bar | `min-h-dvh` for the dynamic height. `svh` when the layout must fit with chrome *visible*; `lvh` when it should fill the largest state |
| Content under a notch or the home indicator | No safe-area handling | `env(safe-area-inset-*)` in padding, and `viewport-fit=cover` in the viewport meta |
| Page zooms unexpectedly when a field is focused on iOS | Input font-size below 16px | Set the field to 16px or larger. Do not fix this with `user-scalable=no` — disabling zoom is an accessibility violation |
| Page can't be zoomed at all | `maximum-scale=1` or `user-scalable=no` in the viewport meta | Remove them. Users must be able to zoom to 400% (WCAG 1.4.4) |
| Missing or wrong viewport meta | Absent `<meta name="viewport">` | `<meta name="viewport" content="width=device-width, initial-scale=1">` — plus `viewport-fit=cover` when handling safe areas |

## Anti-fixes

These appear to work and make things worse. Remove them when found.

- **`overflow-x: hidden` on `body` or `html`.** Hides the symptom while the element stays overflowing and unreachable, and breaks `position: sticky` for every descendant.
- **`user-scalable=no` / `maximum-scale=1`.** Stops iOS focus-zoom by removing the user's ability to zoom at all. Fix the font size instead.
- **A desktop copy and a mobile copy of the same component**, toggled with `hidden md:block`. Doubles the maintenance, ships both to every device, and they drift apart. Justified only when the two are genuinely different components, not two renderings of one.
- **Breakpoint-tuned magic numbers** (`mt-[27px] md:mt-[43px]`). A symptom of fighting the layout rather than fixing it. Find the structural cause.
- **`transform: scale()` to shrink a desktop layout onto a phone.** Makes text blurry and targets unhittable, and defeats zoom.
