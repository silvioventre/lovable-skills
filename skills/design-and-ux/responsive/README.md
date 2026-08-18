# responsive

Makes a Lovable app, site, or component work correctly at every screen size — and proves it against a pass/fail gate instead of declaring victory.

Responsive is treated here as a mechanical discipline, not a matter of taste. A page covered in `md:` and `lg:` variants can still fail every gate; what counts is measured behavior at real widths.

## Install

In Lovable: **Settings → Skills → Add → Import from GitHub**, and paste:

```
https://github.com/silvioventre/lovable-skills/tree/main/skills/design-and-ux/responsive
```

## Use

```
/responsive make the whole app work on mobile
/responsive the pricing page has horizontal scroll on my phone
/responsive check the dashboard at every breakpoint
```

Or just describe the problem — "it breaks on tablet", "non funziona sul telefono" — and Lovable matches it.

## The gate

Work is done when all seven hold, each reported explicitly:

1. No horizontal scroll at any width from 320px up — absent, not hidden
2. Content reflows at 320px with nothing lost (WCAG 1.4.10)
3. Usable at 400% zoom on a 1280px viewport
4. Interactive targets ≥ 24×24 CSS px, 44×44 for primary touch actions (WCAG 2.2 SC 2.5.8)
5. Body and form-field text ≥ 16px on mobile
6. No fixed heights on text containers
7. Nothing under the notch, home indicator, or browser chrome

## What's inside

| File | Contents |
|---|---|
| `SKILL.md` | The gate, the width ladder, the five-phase procedure |
| `reference/failures.md` | Diagnostic catalog: symptom → cause → fix, plus the anti-fixes that look like solutions |
| `reference/techniques.md` | Intrinsic layout, container queries, `clamp()`, `dvh`/`svh`/`lvh`, safe areas, capability queries |
| `reference/checklist.md` | Per-width verification protocol and the report format |

## Scope

Execution and verification — making an existing design work at every size. It does not redesign the experience: if a layout should genuinely be a different thing on mobile, that is a design decision, and the [art-direction](../art-direction/) skill's `adapt` command owns it. Web and mobile web only.

## License

MIT — see the [repository LICENSE](../../../LICENSE).
