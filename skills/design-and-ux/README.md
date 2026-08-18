# design-and-ux

Design and UX skills: art direction, visual systems, typography, layout, responsive behaviour, accessibility — work on the interface, not on content or code in general.

| Skill | What it does |
|---|---|
| [art-direction](art-direction/) | 21 design commands: build a visual direction, critique it, refine it, make an interface bolder or quieter. Derived from [Impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0). |
| [responsive](responsive/) | Makes the interface work at every width from 320px up, verified against a pass/fail gate. Execution and verification, not redesign. |

## How they divide the work

They meet at exactly one point, and it is worth keeping clear:

- **`art-direction`'s `adapt` command** decides *what the experience should become* in another context: whether mobile needs different navigation, less content, a different order of priority. That is a design decision.
- **`responsive`** takes the design as it stands and makes it genuinely hold at every width: overflow, reflow, touch targets, fluid type, safe areas. That is execution and verification, and it does not touch the visual identity.

If the layout is right but breaks on a phone, you want `responsive`. If the layout is wrong for a phone, you want `adapt`.

Add skills here as `skills/design-and-ux/<skill-name>/SKILL.md` — see [`skills/_template/`](../_template/).
