# No-argument routing: the context-aware menu

Read this when the user invokes the skill with no argument. They are asking "what should I do?" Make the menu context-aware instead of static.

Gather the signals yourself before answering. Look at what the project actually contains: whether `PRODUCT.md` and `DESIGN.md` exist, what surfaces the code defines, what the preview currently looks like, and what the user changed most recently. If there is no `PRODUCT.md`, the project has no captured context yet: lead the menu with `init` as the top recommendation (one line on why) and still show the rest below; don't silently jump into init.

Otherwise lead with the **2-3 highest-value next commands**, each with a one-line reason pulled from what you actually observed, followed by the full menu (the Commands table in SKILL.md, grouped by category). **Never auto-run a command; the recommendation is a suggestion the user confirms.**

Reason over the signals; there is no score to obey:

- `DESIGN.md` missing while real UI code exists → `document` (capture the visual system).
- No critique has ever been recorded under `docs/design/critiques/` → for a set-up project with a real surface, offering `critique <surface>` is a strong default.
- A recorded critique with a low score or open P0 / P1 findings → `polish` (it reads that snapshot as its backlog), or re-run `critique` if the snapshot looks stale.
- Recent edits concentrated on one surface → scope `audit` or `polish` to those files specifically, naming them.
- If the project targets `ios`, `android`, or `adaptive`, don't lead with web-only checks; the HTML/CSS anti-pattern families don't apply to native app code.
- Otherwise group by intent (build new / improve what's there), tailored to the current surface and platform.

**Before recommending, scan the most relevant surface yourself.** Open the files the user most recently touched, or the project's main surface if nothing is dirty, and read them against the anti-pattern families in [craft-floor.md](craft-floor.md) and [audit.md](audit.md). Fold the hits into your picks: many quality or contrast hits → `audit` or `polish`; a specific slop family → the matching command (gradient text or eyebrows → `quieter` / `typeset`, flat or gray palette → `colorize`, and so on). It's a real, current signal that beats guessing. If the project is large, sample the primary surface rather than walking the whole tree; never block the suggestion on an exhaustive scan.

Keep it to 2-3 pointed picks with the exact command to type. The menu stays the fallback; the recommendation is the lede.
