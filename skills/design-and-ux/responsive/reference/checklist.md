# Verification protocol

Run this after fixing, on every surface you touched. A fix that resolves 320px and breaks 768px is common enough that re-sweeping is not optional.

## Per width

At each stop on the ladder — 320, 390, 768, 1024, 1440, 1920 — check in this order. Overflow comes first because it invalidates every judgment after it.

**1. Overflow**
- [ ] No horizontal scrollbar, and the page does not drag sideways
- [ ] Nothing is clipped at the right edge
- [ ] Any deliberate horizontal scroll (table, carousel) is contained and obviously scrollable

**2. Structure and reading order**
- [ ] Reading order matches the intended priority
- [ ] Grouping still reads — related things near, unrelated things apart
- [ ] Nothing overlaps
- [ ] DOM order matches visual order (tab through it)

**3. Targets**
- [ ] Every interactive element is at least 24×24 CSS px, or has 24px of clear space
- [ ] Primary actions reach 44×44 at touch widths
- [ ] Adjacent targets do not touch
- [ ] Every hover-revealed control has a tap path

**4. Text**
- [ ] No truncation that loses meaning
- [ ] Body text at least 16px, form fields at least 16px
- [ ] Line length comfortable — roughly 45–75 characters on reading content
- [ ] Headings break sensibly, no single-word last lines
- [ ] Long strings (URLs, emails, tokens) wrap

**5. Media**
- [ ] Images inside their containers, aspect preserved
- [ ] No layout shift as media loads
- [ ] Focal points still visible after cropping
- [ ] Embeds scale with the container

**6. Sticky and fixed**
- [ ] Sticky elements still stick
- [ ] Fixed elements do not cover content or each other
- [ ] Nothing sits under the notch or home indicator
- [ ] A fixed bottom bar survives the mobile keyboard being open

**7. States**
- [ ] Modals, drawers, menus, and tooltips fit and are dismissible
- [ ] Empty, loading, and error states hold up at this width
- [ ] Long content and long lists do not break the layout

## Beyond the ladder

- [ ] **400% zoom at 1280px** — reaches the same 320 CSS px as narrowing, but scales text and spacing together and exposes different bugs
- [ ] **The in-between drag** — move slowly through the range rather than sampling fixed widths; breakage clusters around breakpoints
- [ ] **Landscape phone** (roughly 844×390) — short viewport height, where `vh`-based layouts and modals fail
- [ ] **Browser font size set to large** — catches `px` sizing that ignores user preference
- [ ] **Longest realistic content** — the longest name, title, and label the product will actually hold
- [ ] **Longest translation**, if the product is or will be localized

## The gate

Report every item, with pass, fail, or unverified. Never report "responsive" without this list, and never mark an item passed that you did not actually check.

| # | Gate | Status | Evidence |
|---|---|---|---|
| 1 | No horizontal scroll, 320px and up | | width checked, surface |
| 2 | Reflows at 320px with nothing lost | | |
| 3 | Usable at 400% zoom | | |
| 4 | Targets ≥ 24×24 (44×44 primary touch) | | |
| 5 | Body and field text ≥ 16px on mobile | | |
| 6 | No fixed heights on text containers | | |
| 7 | Nothing under notch, home indicator, or chrome | | |

## Report format

1. **Verdict** — passing, or the count of gate items still failing.
2. **Gate table** — the seven items above.
3. **Fixed** — each failure with its width, file, cause, and the change made. Group by cause, not by file; one cause usually produced several symptoms.
4. **Remaining** — anything not fixed, with why: out of scope, needs a design decision, or needs the user to choose.
5. **Unverified** — every check you could not run, and what would be needed to run it. An unverified check is never reported as a pass.
6. **Structural notes** — patterns worth fixing at the source rather than per-instance: a component that keeps overflowing in different slots wants a container query; repeated breakpoint magic numbers want a fluid token.

Do not narrate the sweep width by width. The gate table plus the grouped fix list is the deliverable.
